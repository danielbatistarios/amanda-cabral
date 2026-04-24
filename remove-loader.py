#!/usr/bin/env python3
"""Remove loader animation from all non-home HTML files."""

import os
import re
import sys

BASE = '/Users/jrios/amanda-cabral-contadora'
DRY_RUN = '--apply' not in sys.argv


def get_files():
    files = []
    for root, dirs, filenames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d != 'node_modules']
        for f in filenames:
            if f == 'index.html':
                path = os.path.join(root, f)
                if path != os.path.join(BASE, 'index.html'):
                    files.append(path)
    return sorted(files)


def remove_loader_css_in_block(css):
    """Remove all loader CSS from a style block."""
    # Remove section comment markers (both // and /* */ styles)
    css = re.sub(r'[ \t]*/\*\s*[=─\-\s]*(?:LOADER|Loader)[=─\-\s]*\*/\s*\n?', '', css)
    css = re.sub(r'[ \t]*/\*\s*Loader:[^\*]*\*/\s*\n?', '', css)
    css = re.sub(r'[ \t]*/\*\s*(?:LOADER|Loader)\s*\*/\s*\n?', '', css)  # inline /* Loader */

    # Remove .loader* and #loader CSS blocks (selector + braces)
    loader_sel = re.compile(
        r'(?:(?<=\n)|(?<=^))[ \t]*(?:\.loader[\w\-.()\s:,>~+\[\]"=*]*|#loader[\w\-.()\s:,>~+\[\]"=*]*)[ \t]*(?:[\{,])',
        re.MULTILINE
    )

    for _ in range(50):
        m = loader_sel.search(css)
        if not m:
            break
        rule_start = m.start()

        brace_pos = css.find('{', m.start())
        if brace_pos == -1:
            break

        depth = 1
        pos = brace_pos + 1
        while depth > 0 and pos < len(css):
            if css[pos] == '{':
                depth += 1
            elif css[pos] == '}':
                depth -= 1
            pos += 1
        while pos < len(css) and css[pos] in '\n\r':
            pos += 1

        css = css[:rule_start] + css[pos:]

    # Remove @keyframes loader*
    for _ in range(20):
        m = re.search(r'[ \t]*@keyframes\s+loader\w*\s*\{', css)
        if not m:
            break
        brace_pos = m.end() - 1
        depth = 1
        pos = brace_pos + 1
        while depth > 0 and pos < len(css):
            if css[pos] == '{':
                depth += 1
            elif css[pos] == '}':
                depth -= 1
            pos += 1
        while pos < len(css) and css[pos] in '\n\r':
            pos += 1
        css = css[:m.start()] + css[pos:]

    return css


def remove_loader_css(html):
    def clean_style(m):
        return f'<style>{remove_loader_css_in_block(m.group(1))}</style>'
    return re.sub(r'<style>([\s\S]*?)</style>', clean_style, html)


def remove_loader_div(html):
    """Stack-based removal of loader divs and preceding HTML comments."""
    result = []
    i = 0
    n = len(html)

    while i < n:
        div_m = re.search(r'<div\s+(?:class="loader[^"]*"|id="loader")[^>]*>', html[i:])
        if not div_m:
            result.append(html[i:])
            break

        abs_div_start = i + div_m.start()
        text_before = html[i:abs_div_start]
        comment_m = re.search(
            r'<!--\s*(?:\d+\.\s*)?(?:LOADER|Loader)\s*-->\s*\n?$',
            text_before,
            re.IGNORECASE
        )
        abs_start = (i + comment_m.start()) if comment_m else abs_div_start
        result.append(html[i:abs_start])

        pos = abs_div_start + len(div_m.group(0))
        depth = 1
        while depth > 0 and pos < n:
            open_m = re.search(r'<div[\s>]', html[pos:])
            close_m = re.search(r'</div>', html[pos:])
            if close_m and (not open_m or close_m.start() < open_m.start()):
                pos += close_m.start() + len('</div>')
                depth -= 1
            elif open_m and (not close_m or open_m.start() < close_m.start()):
                pos += open_m.start() + len('<div')
                depth += 1
            else:
                break
        if pos < n and html[pos] == '\n':
            pos += 1
        i = pos

    return ''.join(result)


def find_matching_brace(text, brace_pos):
    """Find closing } matching opening { at brace_pos."""
    depth = 1
    pos = brace_pos + 1
    while depth > 0 and pos < len(text):
        if text[pos] == '{':
            depth += 1
        elif text[pos] == '}':
            depth -= 1
        pos += 1
    return pos


def remove_js_loader(html):
    """Remove all JS loader patterns."""

    # Pattern 1: Old LP IIFE: /* === LOADER === */ \n (function() { ... })();
    html = re.sub(
        r'\n?[ \t]*/\*\s*={3,}\s*LOADER\s*={3,}\s*\*/\s*\n\s*\(function\(\)\s*\{[\s\S]*?\}\)\(\);\s*\n?',
        '\n',
        html
    )

    # Pattern 2: Any loader comment (// or /* */) followed by const loader or window.addEventListener
    # Handles:
    #   // ── LOADER ── / // ---- LOADER ---- / // LOADER / /* ── LOADER ── */
    loader_comment_re = re.compile(
        r'\n[ \t]*(?://\s*[-─\s]*LOADER[-─\s]*|/\*\s*[-─\s]*LOADER[-─\s]*\*/)\s*\n'
    )

    def remove_loader_comment_blocks(text):
        for _ in range(20):
            m = loader_comment_re.search(text)
            if not m:
                break
            start = m.start()
            pos = m.end()
            rest = text[pos:]

            # Case A: const loader = document.getElementById('loader');
            const_m = re.match(r'[ \t]*const loader\s*=\s*document\.getElementById\([\'"]loader[\'"]\);\s*\n', rest)
            if const_m:
                pos += len(const_m.group())
                rest2 = text[pos:]
                # Find "if (loader) {" block(s) that follow
                while True:
                    if_m = re.match(r'[ \t]*if\s*\(loader\)\s*\{', rest2)
                    if not if_m:
                        break
                    brace_pos = pos + rest2.index('{')
                    end_pos = find_matching_brace(text, brace_pos)
                    while end_pos < len(text) and text[end_pos] == '\n':
                        end_pos += 1
                    pos = end_pos
                    rest2 = text[pos:]
                text = text[:start] + '\n' + text[pos:]

            # Case B: window.addEventListener('load', () => { ... }); (multiline)
            elif re.match(r'[ \t]*window\.addEventListener\([\'"]load[\'"]', rest):
                # Find the end of this statement (find matching closing of the addEventListener call)
                # Simple approach: find next ; at depth 0
                j = pos
                depth = 0
                while j < len(text):
                    c = text[j]
                    if c in '({':
                        depth += 1
                    elif c in ')}':
                        depth -= 1
                        if depth <= 0:
                            j += 1
                            break
                    j += 1
                # Find the ; and any trailing chars
                if j < len(text) and text[j] == ';':
                    j += 1
                while j < len(text) and text[j] in '\n\r':
                    j += 1
                text = text[:start] + '\n' + text[j:]

            # Case C: just the comment (e.g., cases of // LOADER + single-line setTimeout not on next line)
            else:
                text = text[:start] + '\n' + text[pos:]

        return text

    html = remove_loader_comment_blocks(html)

    # Pattern 6: holding-patrimonial / desenquadrar-mei specific loader JS block inside IIFE
    # Must run BEFORE Pattern 3 so const loader isn't stripped first
    # // Loader\nconst loader = ... \nconst words = ...\nconst fill = ...\nlet wi = ...\nfunction showWord(){...}\nshowWord();
    def remove_holding_loader(text):
        m = re.search(r'\n[ \t]*//\s*Loader\s*\n[ \t]*const loader\s*=\s*document\.getElementById', text)
        if not m:
            return text
        start = m.start()
        showword_m = re.search(r'\n[ \t]*showWord\(\);\s*\n', text[start:])
        if showword_m:
            end_pos = start + showword_m.end()
            # Inject initReveal() call before closing })(); of IIFE
            closing_m = re.search(r'\n\}\)\(\);', text[end_pos:])
            if closing_m:
                inject_pos = end_pos + closing_m.start()
                text = (text[:start] + '\n' +
                        text[end_pos:inject_pos] +
                        "\n  document.body.classList.add('cursor-ready'); initReveal();" +
                        text[inject_pos:])
            else:
                text = text[:start] + '\n' + text[end_pos:]
        else:
            nl = text.find('\n', start + 1)
            text = text[:start] + text[nl:]
        return text

    html = remove_holding_loader(html)

    # Pattern 3: orphaned "const loader = ..." + "if (loader) {}" (no comment prefix)
    def remove_standalone_const_loader(text):
        pattern = re.compile(r'\n[ \t]*const loader\s*=\s*document\.getElementById\([\'"]loader[\'"]\);')
        for _ in range(20):
            m = pattern.search(text)
            if not m:
                break
            start = m.start()
            pos = m.end()
            # Skip newline
            if pos < len(text) and text[pos] == '\n':
                pos += 1
            # Find if (loader) { block(s)
            for _ in range(5):
                if_m = re.match(r'[ \t]*if\s*\(loader\)\s*\{', text[pos:])
                if not if_m:
                    break
                brace_pos = pos + text[pos:].index('{')
                end_pos = find_matching_brace(text, brace_pos)
                while end_pos < len(text) and text[end_pos] == '\n':
                    end_pos += 1
                pos = end_pos
            text = text[:start] + '\n' + text[pos:]
        return text

    html = remove_standalone_const_loader(html)

    # Pattern 4: loaderDelay variable - replace block with direct call
    # "const loaderDelay = ...\n if (...) { setTimeout(attachObserver, loaderDelay); } else { ... }"
    def fix_loader_delay(text):
        m = re.search(r'\n[ \t]*const loaderDelay\s*=[^\n]+\n', text)
        if not m:
            return text
        start = m.start()
        pos = m.end()
        # Remove loaderDelay if/else block
        if_m = re.match(r'[ \t]*if\s*\([^)]+\)\s*\{', text[pos:])
        if if_m:
            brace_pos = pos + text[pos:].index('{')
            end_pos = find_matching_brace(text, brace_pos)
            # Check for else
            rest_after = text[end_pos:end_pos+30].strip()
            if rest_after.startswith('else'):
                else_brace = text.index('{', end_pos)
                end_pos = find_matching_brace(text, else_brace)
            while end_pos < len(text) and text[end_pos] == '\n':
                end_pos += 1
            # Replace with direct call
            text = text[:start] + '\n        if (document.readyState === \'complete\') { attachObserver(); } else { window.addEventListener(\'load\', attachObserver); }\n' + text[end_pos:]
        return text

    html = fix_loader_delay(html)

    # Pattern 5: Remove orphaned if (loader) { ... } blocks
    # These are left behind when const loader was removed but if block wasn't matched
    def remove_orphaned_if_loader(text):
        pattern = re.compile(r'\n([ \t]*)if\s*\(loader(?:\s*&&[^)]+)?\)\s*\{')
        for _ in range(20):
            m = pattern.search(text)
            if not m:
                break
            # Verify "loader" variable is NOT defined in preceding 300 chars
            preceding = text[max(0, m.start()-300):m.start()]
            if re.search(r'(?:const|var|let)\s+loader\s*=', preceding):
                break  # variable still defined nearby, skip
            brace_pos = m.end() - 1
            depth = 1
            pos = brace_pos + 1
            while depth > 0 and pos < len(text):
                if text[pos] == '{':
                    depth += 1
                elif text[pos] == '}':
                    depth -= 1
                pos += 1
            while pos < len(text) and text[pos] == '\n':
                pos += 1
            text = text[:m.start()] + '\n' + text[pos:]
        return text

    html = remove_orphaned_if_loader(html)

    # Pattern 7: faq print CSS .loader reference
    # nav, .faq-tabs, .reading-prog, .loader, .pre-footer, footer { display: none !important; }
    html = re.sub(r',\s*\.loader(?=\s*[,{])', '', html)

    # Pattern 8: Remove comments that reference loader (single-line comments)
    html = re.sub(r'\n[ \t]*//[^\n]*\bloader\b[^\n]*(?:terminar|sumir|dura|margem|registramos|viewport)[^\n]*', '', html)

    return html


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    html = remove_loader_css(html)
    html = remove_loader_div(html)
    html = remove_js_loader(html)

    remaining_lines = []
    for i, line in enumerate(html.split('\n'), 1):
        if 'loader' in line.lower():
            remaining_lines.append((i, line.strip()))

    return html, original != html, remaining_lines


def main():
    files = get_files()
    print(f"Mode: {'DRY RUN' if DRY_RUN else 'APPLY'}")
    print(f"Files to process: {len(files)}\n")

    total_remaining = 0
    changed = 0

    for path in files:
        rel = path.replace(BASE + '/', '')
        html, modified, remaining_lines = process_file(path)
        total_remaining += len(remaining_lines)
        if modified:
            changed += 1

        status = 'CHANGED' if modified else 'UNCHANGED'
        flag = f' ⚠ {len(remaining_lines)} refs' if remaining_lines else ''
        print(f"  [{status}] {rel}{flag}")

        for lineno, line in remaining_lines:
            print(f"    L{lineno}: {line[:120]}")

        if not DRY_RUN and modified:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)

    print(f"\nSummary: {changed}/{len(files)} files changed, {total_remaining} loader refs remaining")
    if total_remaining == 0:
        print("✓ Zero loader references remaining!")


if __name__ == '__main__':
    main()
