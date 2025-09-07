"""
Convert one or more *digital* PDFs to Markdown using PyMuPDF4LLM.

- CPU-only (no Torch, no GPU)
- Minimal dependencies: pymupdf4llm (pulls in PyMuPDF)
- Outputs: <stem>.md and <stem>.metadata.json in the chosen folder

Usage (from repo root):
  uv pip install pymupdf4llm
  uv run python backend/tools/pdf_to_markdown_pymupdf.py \
    --input data/docs/space_rider_manual \
    --out   data/docs/processed
"""

from __future__ import annotations
import argparse
import json
import time
from pathlib import Path

import pymupdf4llm              # fast PDF -> Markdown
import fitz                     # PyMuPDF (for metadata/page count)


def collect_pdfs(path: Path) -> list[Path]:
    if path.is_file() and path.suffix.lower() == ".pdf":
        return [path]
    if path.is_dir():
        return sorted(p for p in path.glob("*.pdf") if p.is_file())
    raise FileNotFoundError(f"No PDFs found at: {path}")


def convert_pdf(pdf: Path, out_dir: Path) -> tuple[Path, float]:
    out_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    md_text = pymupdf4llm.to_markdown(str(pdf))            # main conversion
    elapsed = time.time() - t0

    md_path = out_dir / f"{pdf.stem}.md"
    md_path.write_text(md_text, encoding="utf-8")

    # lightweight metadata
    with fitz.open(str(pdf)) as doc:
        meta = {
            "engine": "pymupdf4llm",
            "filetype": "pdf",
            "pages": doc.page_count,
            "pdf_metadata": doc.metadata or {},
        }
    (out_dir / f"{pdf.stem}.metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    return md_path, elapsed


def main():
    ap = argparse.ArgumentParser(description="PDF → Markdown via PyMuPDF4LLM (CPU-only).")
    ap.add_argument("-i", "--input", type=Path, default=Path("data/docs/space_rider_manual"),
                    help="PDF file or folder")
    ap.add_argument("-o", "--out",   type=Path, default=Path("data/docs/processed"),
                    help="Output directory")
    args = ap.parse_args()

    pdfs = collect_pdfs(args.input)
    if not pdfs:
        print("No PDFs to process.")
        return

    for pdf in pdfs:
        print(f"\n🔄 Converting: {pdf.name}")
        try:
            md_path, secs = convert_pdf(pdf, args.out)
            print(f"✅ Saved: {md_path}  ({secs:.2f}s, ~{md_path.stat().st_size} bytes)")
        except Exception as e:
            print(f"❌ Failed: {pdf.name} — {e}")

    print("\n🎉 Done.")


if __name__ == "__main__":
    main()