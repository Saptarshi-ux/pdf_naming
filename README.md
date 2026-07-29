# PDF RO Name Renamer

A Streamlit-based web application that automatically renames multiple PDF files by extracting the **RO Name** from each PDF and packaging the renamed files into a downloadable ZIP archive.

This tool is designed to eliminate manual renaming when working with large batches of PDF reports.

---

## Features

- Upload multiple PDF files simultaneously
- Automatically extract the **RO Name** from each PDF
- Rename files in the format:

```
DDO_<RO_NAME>.pdf
```

Example:

```
report_68515.pdf
        ↓
DDO_M_S_JAYSWAL_AUTO_SERVICE.pdf
```

- Handles duplicate RO names automatically
- Removes invalid filename characters
- Displays a preview of old and new filenames
- Downloads all renamed PDFs as a single ZIP file
- Simple and user-friendly Streamlit interface

---

## How It Works

1. Upload one or more PDF files.
2. The application reads the text from each PDF using **PyMuPDF**.
3. It searches for the following pattern:

```
RO Name <RO_NAME> RO Type
```

4. The extracted RO Name is sanitized to create a valid filename.
5. The original PDF is renamed.
6. All renamed PDFs are packaged into a ZIP archive.
7. Download the ZIP with a single click.

---

## Project Structure

```
.
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pdf-ro-name-renamer.git
cd pdf-ro-name-renamer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## Requirements

- Python 3.9+
- Streamlit
- PyMuPDF
- pandas

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Example

### Input Files

```
report_68515.pdf
report_68516.pdf
report_68517.pdf
```

### Extracted RO Names

```
M/S JAYSWAL AUTO SERVICE
ABC PETROLEUM
XYZ FILLING STATION
```

### Output Files

```
DDO_M_S_JAYSWAL_AUTO_SERVICE.pdf
DDO_ABC_PETROLEUM.pdf
DDO_XYZ_FILLING_STATION.pdf
```

Downloaded as:

```
Renamed_PDFs.zip
```

---

## Supported PDF Format

The application expects PDFs containing text in the following format:

```
RO SAP Code XXXXX

RO Name M/S JAYSWAL AUTO SERVICE

RO Type
```

The RO Name is extracted from the text between:

```
RO Name
```

and

```
RO Type
```

---

## Technologies Used

- Python
- Streamlit
- PyMuPDF (fitz)
- pandas
- zipfile
- io
- re

---

## Future Improvements

- OCR support for scanned PDFs
- Folder upload support
- Excel report containing old and new filenames
- Search and filter functionality
- Progress statistics
- Automatic processing of entire directories
- Desktop executable (.exe) version

---

## License

This project is released under the MIT License.

---

## Author

Developed using Python and Streamlit for automating bulk PDF renaming based on extracted RO Names.
