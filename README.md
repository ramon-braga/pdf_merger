# PDF Merger Script

This script merges multiple PDF files into a single document named **"Final PDF.pdf"**. It uses the **PyPDF2** library and follows these steps:

## Steps:
1. Creates a `PdfMerger` object to handle the merging of PDFs.
2. Lists the files in the **"files"** folder and sorts them.
3. Checks if the files have a **".pdf"** extension.
4. Appends each PDF file found to the `merger` object.
5. Finally, writes the combined PDF as **"Final PDF.pdf"**.