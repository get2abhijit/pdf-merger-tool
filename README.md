# PDF Merger Tool

A fast and simple Python utility to merge all PDF files in a folder into a single PDF. The output PDF is named after the containing folder and saved in the same location. If a file with the same name exists, a numeric suffix is added automatically.

## Features
- Merges all PDF files in a folder, sorted alphabetically
- Output PDF named after the folder (e.g., `foldername.pdf`)
- Handles filename conflicts by adding a numeric suffix
- Displays number of files merged and any errors
- Works as a Python script or standalone Windows executable

## Requirements
- Python 3.7+
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- (Optional) [PyInstaller](https://pyinstaller.org/) for creating an executable

## Installation
### 1. Clone the Repository
```
git clone https://github.com/get2abhijit/pdf-merger-tool.git
cd pdf-merger-tool
```

### 2. Set Up Virtual Environment (Recommended)
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:
```
pip install PyPDF2
```

## Usage
### Run as Python Script
```
python merge-pdfs.py <folder_path> [--delete]
```
- If `<folder_path>` is omitted, the script merges PDFs in the current directory.
- Add the optional `--delete` flag to delete original PDF files after merging. This flag is OFF by default.

### Example
```
python merge-pdfs.py C:\Users\YourName\Documents\PDFs --delete
```

### Output
- Merged PDF will be saved as `PDFs.pdf` (or `PDFs_1.pdf`, etc. if a conflict exists) in the same folder.
- Console output shows how many files were merged, how many were deleted (if `--delete` is used), and any errors.

## Create a Standalone Executable (Windows)
1. Ensure your virtual environment is activated.
2. Run the provided batch script:
   ```
   make_exe.bat merge-pdfs.py
   ```
3. The executable will be created in the `dist` folder.
4. You can now run the `.exe` file without Python installed:
   ```
   dist\merge-pdfs.exe <folder_path> [--delete]
   ```
   - Add `--delete` to remove original PDFs after merging.

## Troubleshooting
- If you see missing import errors, ensure you are running the script inside the virtual environment.
- For large PDFs or many files, merging may take longer.
- If you encounter permission errors, check that you have write access to the target folder.

## License
MIT License

## Contributing
Pull requests and suggestions are welcome! Please open an issue for bugs or feature requests.

## Author
get2abhijit
