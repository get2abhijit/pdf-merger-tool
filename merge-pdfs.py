import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_files.sort()

    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    merger = PdfMerger()
    errors = []
    merged_count = 0
    deleted_count = 0

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        try:
            merger.append(pdf_path)
            merged_count += 1
        except Exception as e:
            errors.append(f"Failed to add '{pdf_file}': {e}")

    folder_name = os.path.basename(os.path.normpath(folder_path))
    base_output_name = f"{folder_name}.pdf"
    output_path = os.path.join(folder_path, base_output_name)
    suffix = 1
    while os.path.exists(output_path):
        output_path = os.path.join(folder_path, f"{folder_name}_{suffix}.pdf")
        suffix += 1

    try:
        merger.write(output_path)
        merger.close()
        print(f"Successfully merged {merged_count} PDF files into '{output_path}'.")
        if errors:
            print("Errors:")
            for err in errors:
                print(f"  - {err}")
        if delete_originals:
            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                try:
                    os.remove(pdf_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"Failed to delete '{pdf_file}': {e}")
            print(f"Deleted {deleted_count} original PDF files.")
    except Exception as e:
        print(f"Error writing merged PDF: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Merge all PDFs in a folder into one PDF.")
    parser.add_argument("folder", nargs="?", default=os.getcwd(), help="Folder containing PDF files (default: current directory)")
    parser.add_argument("--delete", action="store_true", help="Delete original PDF files after merge")
    args = parser.parse_args()

    folder = args.folder
    delete_originals = args.delete
    if args.folder == os.getcwd():
        print(f"No folder argument provided. Using current directory: {folder}")
    merge_pdfs_in_folder(folder)
