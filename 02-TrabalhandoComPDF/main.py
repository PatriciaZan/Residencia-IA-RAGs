# receber inputs (dados_entrada)
# Extrair pfd para .md
# criar outputs separados (dados_saida)

import os
os.environ["TORCH_COMPILE_DISABLE"] = "1"

from pathlib import Path
from docling.document_converter import DocumentConverter


#linkar a pasta de entrada e de saida
input_folder = Path('./dados_entrada')
output_folder = Path('./dados_saida')

# fazer a conversão de cada pdf - loop
converter = DocumentConverter()


for pdf_file in input_folder.glob('*.pdf'):
    print(f"Está convertendo o arquivo pdf: {pdf_file.name}")

    result = converter.convert(str(pdf_file))

    md_file = output_folder / f"{pdf_file.stem}.md"

    # salvar o novo arquivo
    md_file.write_text(result.document.export_to_markdown(), encoding="utf-8")

    print(f"Documento transformando para md")
















