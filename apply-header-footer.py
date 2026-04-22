#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_header_footer(index_path):
    """Extrai header e footer da index.html"""
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Encontra o header (tudo antes de <main>)
    main_match = re.search(r'<main[^>]*>', content)
    if not main_match:
        raise ValueError("Não encontrou <main> na index.html")

    header = content[:main_match.start()]

    # Encontra o footer (tudo depois de </main>)
    main_close = content.rfind('</main>')
    if main_close == -1:
        raise ValueError("Não encontrou </main> na index.html")

    footer = content[main_close + len('</main>'):]

    # Remove o corpo vazio entre header e footer
    main_content = content[main_match.start():main_close + len('</main>')]

    return header, footer

def apply_header_footer_to_page(page_path, header, footer):
    """Aplica header e footer a uma página, preservando seu conteúdo principal"""
    with open(page_path, 'r', encoding='utf-8') as f:
        page_content = f.read()

    # Encontra <main> ou <body>
    main_match = re.search(r'<main[^>]*>(.*?)</main>', page_content, re.DOTALL)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', page_content, re.DOTALL)

    if main_match:
        # Se tem <main>, preserva o conteúdo dentro
        main_inner = main_match.group(1)
        updated = header + f'<main>{main_inner}</main>' + footer
    elif body_match:
        # Se não tem <main>, tira tudo de <body> e reaplica
        body_inner = body_match.group(1)
        # Remove header/footer antigos se existirem
        body_inner = re.sub(r'<header[^>]*>.*?</header>', '', body_inner, flags=re.DOTALL)
        body_inner = re.sub(r'<footer[^>]*>.*?</footer>', '', body_inner, flags=re.DOTALL)
        updated = header + f'<main>{body_inner}</main>' + footer
    else:
        raise ValueError(f"Não encontrou <main> ou <body> em {page_path}")

    return updated

def main():
    project_dir = Path('/Users/jrios/amanda-cabral-contadora')
    index_path = project_dir / 'index.html'

    # Arquivos a atualizar (13 páginas)
    pages_to_update = [
        'author.html',
        'bio.html',
        'consultoria-tributaria.html',
        'faq.html',
        'gestao-contabil-industrial.html',
        'holding-patrimonial.html',
        'planejamento-tributario.html',
        'recuperacao-creditos-tributarios.html',
        'servicos.html',
    ]

    # Extrai header e footer
    print("Extraindo header e footer de index.html...")
    header, footer = extract_header_footer(index_path)
    print(f"✓ Header: {len(header)} caracteres")
    print(f"✓ Footer: {len(footer)} caracteres")

    # Aplica em cada página
    for page_file in pages_to_update:
        page_path = project_dir / page_file
        if not page_path.exists():
            print(f"⚠ Arquivo não encontrado: {page_file}")
            continue

        print(f"\nAtualizando {page_file}...")
        try:
            updated_content = apply_header_footer_to_page(page_path, header, footer)

            # Backup
            backup_path = project_dir / f"{page_file}.bak"
            if not backup_path.exists():
                with open(backup_path, 'w', encoding='utf-8') as f:
                    with open(page_path, 'r', encoding='utf-8') as orig:
                        f.write(orig.read())
                print(f"  → Backup criado: {page_file}.bak")

            # Salva arquivo atualizado
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  ✓ {page_file} atualizado ({len(updated_content)} caracteres)")

        except Exception as e:
            print(f"  ✗ Erro ao atualizar {page_file}: {e}")

    print("\n✓ Pronto! Todas as páginas foram atualizadas com o header/footer global.")

if __name__ == '__main__':
    main()
