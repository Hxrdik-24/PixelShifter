# 🌌 PixelShifter

PixelShifter is a Python toolkit for turning images and videos into creative terminal or browser visuals. It includes background removal, colored HTML ASCII art, batch conversion, and real-time terminal video rendering.

> **Status:** Experimental learning project. APIs and output formats may change.

## ✨ Features

- **Background removal** with `withoutbg`, saving transparent PNG assets.
- **Colored image-to-HTML ASCII** rendering with Pillow.
- **Batch ASCII conversion** for a single image or an entire directory.
- **Colored video-to-terminal ASCII** playback with OpenCV and optional audio through pygame.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Louis-Low/PixelShifter.git
cd PixelShifter
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Optional tools can be installed with:

```bash
python -m pip install withoutbg opencv-python pygame
```

## 🚀 Usage

### Remove an image background

```bash
python img_bg_remover.py
```

Enter the input image path and an output filename when prompted. Use `.png` for the output to preserve transparency.

### Convert one image to colored HTML ASCII

```bash
python imgtoAcsii.py
```

The script asks for an image path and an ASCII width, then creates `ascii_output.html`. Open that file in a browser to view the result.

### Batch-convert images to HTML ASCII

The batch tool accepts either one image or a directory. Directory input is searched recursively for common image formats.

```bash
# Convert one image
python batch_ascii.py photo.jpg output/photo.html --width 120

# Convert every supported image below ./images
python batch_ascii.py ./images ./generated_ascii --width 100
```

Supported formats include `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.gif`, and `.tiff`.

### Play a video as colored terminal ASCII

```bash
python videoToAscii.py
```

Provide a video path when prompted. A terminal that supports ANSI true-color produces the best result. Audio playback depends on the local pygame/SDL setup.

## 🗂️ Project layout

| File or directory | Purpose |
| --- | --- |
| `img_bg_remover.py` | Removes an image background using `withoutbg`. |
| `imgtoAcsii.py` | Creates a colored HTML ASCII page from one image. |
| `batch_ascii.py` | Converts one image or a directory of images to HTML ASCII files. |
| `videoToAscii.py` | Plays a video as colored terminal ASCII. |
| `examples/` | Space for sample inputs and experiments. |
| `requirements.txt` | Python dependency list for the core tools. |

## 🛠️ Troubleshooting

- If Pillow cannot open a file, check that the path exists and that the image format is supported.
- For a smaller terminal or slower machine, lower the ASCII width.
- If video audio fails, video rendering can still work; verify that pygame and your system audio device are available.
- Use a terminal with ANSI true-color support for the best video output.
- Generated HTML output is ignored by Git through `.gitignore`.

## 🗺️ Roadmap

- [x] Basic background removal.
- [x] Image-to-HTML colored ASCII.
- [x] Batch image-to-HTML conversion.
- [x] Colored video playback.
- [ ] Add a unified `pixelshifter` command.
- [ ] Add automated tests and CI.
- [ ] Add privacy tools such as EXIF metadata stripping.
- [ ] Add more image effects and export formats.

## 🤝 Contributing

Issues and pull requests are welcome. For a new tool, please include:

1. A short description of the feature.
2. Installation or dependency requirements.
3. A usage example.
4. Any limitations or platform-specific notes.

Please keep generated media and local environment files out of commits.

## 📄 License

No license has been declared yet. Until a license is added, all rights remain with the repository owner.

**Author:** Hardik Prajapati
