import os
os.environ["TORCH_COMPILE_DISABLE"] = "1"

from pathlib import Path
from docling.document_converter import DocumentConverter

converter = DocumentConverter()

def convert_pdf(pdf_path: str):
    pdf = Path(pdf_path)

    result = converter.convert(str(pdf))

    output = pdf.with_suffix(".md")

    output.write_text(
        result.document.export_to_markdown(),
        encoding="utf-8"
    )

    print(f"Saved: {output}")

# Convert one PDF
#convert_pdf(".././dados_entrada/bioetica_e_ia.pdf")
convert_pdf(".././dados_entrada/escrita_academica_ia.pdf")