# !pip install docling

from docling.document_converter import DocumentConverter
from pathlib import Path

converter = DocumentConverter()

# Caso os arquivos estejam em outro local atualize o PATH abaixo
input_folder = Path("/content/sample_data/pdfs")
output_folder = Path("/content/sample_data/markdown")

output_folder.mkdir(exist_ok=True)

for pdf_path in input_folder.glob("*.pdf"):

    print(f"Convertendo: {pdf_path.name}")

    result = converter.convert(pdf_path)

    markdown = result.document.export_to_markdown()

    output_path = output_folder / f"{pdf_path.stem}.md"

    output_path.write_text(
        markdown,
        encoding="utf-8"
    )

    print(f"✓ {output_path.name}")