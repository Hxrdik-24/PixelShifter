"""Batch-convert images into standalone colored HTML ASCII art files.

Usage:
    python batch_ascii.py input_images output_html
    python batch_ascii.py photo.jpg output_html --width 120
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path
from typing import Iterable

from PIL import Image, UnidentifiedImageError

ASCII_CHARS = "@%#*+=-:. "
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif", ".tiff"}


def image_to_ascii(image_path: Path, width: int) -> str:
    """Render an image as color-preserving HTML spans."""
    with Image.open(image_path) as source:
        image = source.convert("RGB")
        height = max(1, round(width * image.height / image.width * 0.5))
        image = image.resize((width, height))

        lines = []
        for y in range(height):
            row = []
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                brightness = 0.299 * r + 0.587 * g + 0.114 * b
                character = ASCII_CHARS[round(brightness / 255 * (len(ASCII_CHARS) - 1))]
                row.append(
                    f'<span style="color:rgb({r},{g},{b})">{html.escape(character)}</span>'
                )
            lines.append("".join(row))

    return "<br>\n".join(lines)


def iter_images(input_path: Path) -> Iterable[Path]:
    if input_path.is_file():
        yield input_path
        return

    yield from sorted(
        path
        for path in input_path.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def write_document(art: str, title: str, output_path: Path) -> None:
    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin: 0; padding: 2rem; background: #050505; color: #eee; font-family: monospace; }}
  h1 {{ text-align: center; font-size: 1.2rem; letter-spacing: .12em; }}
  pre {{ width: max-content; max-width: 100%; margin: 2rem auto; overflow: auto; line-height: .55; font-size: 8px; }}
</style>
</head>
<body><h1>{html.escape(title)}</h1><pre>{art}</pre></body>
</html>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert an image or image directory to colored HTML ASCII art.")
    parser.add_argument("input", type=Path, help="Image file or directory containing images")
    parser.add_argument("output", type=Path, help="Output HTML file or directory")
    parser.add_argument("--width", type=int, default=100, help="ASCII width (default: 100)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        raise SystemExit(f"Input does not exist: {args.input}")
    if args.width < 1:
        raise SystemExit("--width must be greater than zero")

    images = list(iter_images(args.input))
    if not images:
        raise SystemExit("No supported images found.")

    batch_mode = args.input.is_dir()
    for image_path in images:
        output_path = args.output / f"{image_path.stem}.html" if batch_mode else args.output
        try:
            art = image_to_ascii(image_path, args.width)
            write_document(art, image_path.name, output_path)
            print(f"Created {output_path}")
        except (UnidentifiedImageError, OSError) as error:
            print(f"Skipped {image_path}: {error}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
