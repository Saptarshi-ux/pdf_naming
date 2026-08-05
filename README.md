# PDF RO Name Renamer

A Python and Streamlit-based web application that automates the renaming of PDF files by extracting specific information directly from the document.

The application reads each uploaded PDF, extracts the **Divisional Office** and **RO Name**, renames the PDF according to a predefined naming convention, and provides all renamed files as a downloadable ZIP archive.

---

## Project Highlights

- Developed a production-ready PDF automation tool using **Python** and **Streamlit**.
- Automates bulk PDF renaming by extracting information directly from PDF documents.
- Eliminates repetitive manual file renaming, significantly reducing processing time and human error.
- Supports batch processing of multiple PDF files in a single upload.
- Automatically creates a ZIP archive containing all renamed PDFs.
- Includes duplicate filename handling, robust error handling, and processing status reporting.
- Designed with an intuitive web interface for non-technical users.

---

## Features

- Upload multiple PDF files simultaneously.
- Automatically extract:
  - Divisional Office
  - RO Name
- Rename files using the format:

```
DivisionalOffice_ROName.pdf
```

Example:

```
Durgapur_DO_M_S_JAYSWAL_AUTO_SERVICE.pdf
```

- Automatic filename sanitization.
- Duplicate filename detection and handling.
- Preview table showing:
  - Original Filename
  - Divisional Office
  - RO Name
  - New Filename
  - Processing Status
  - Error Message (if any)
- Download all renamed PDFs as a single ZIP archive.
- Gracefully handles invalid or unsupported PDF files without stopping the entire process.

---

## Tech Stack

- Python 3
- Streamlit
- PyMuPDF (fitz)
- Pandas
- Regular Expressions (re)
- ZipFile
- BytesIO

---

## Project Structure

```
PDF_RO_Name_Renamer/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_pdfs/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/pdf-ro-name-renamer.git
```

Navigate to the project directory

```bash
cd pdf-ro-name-renamer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Requirements

```
streamlit==1.49.1
PyMuPDF==1.26.4
pandas==2.3.2
```

---

## How It Works

1. Upload one or more PDF files.
2. The application extracts the text from every uploaded PDF.
3. It identifies:
   - Divisional Office
   - RO Name
4. The filename is generated using the format:

```
DivisionalOffice_ROName.pdf
```

5. A preview table is displayed showing the extracted information.
6. All renamed PDFs are packaged into a ZIP archive.
7. Download the ZIP file with a single click.

---

## Example

Original files

```
report_68515.pdf
report_68571.pdf
report_68632.pdf
```

Renamed files

```
Durgapur_DO_M_S_JAYSWAL_AUTO_SERVICE.pdf

Kolkata_DO_M_S_TRINATH_SERVICE_STATION.pdf

Kolkata_DO_M_S_MAYA_FUELS_&_SERVICES_COMPANY.pdf
```

---

## Error Handling

The application includes robust error handling to ensure uninterrupted processing.

- Invalid or corrupted PDF files are skipped.
- Processing continues even if one or more files fail.
- Missing Divisional Office or RO Name fields are reported.
- Duplicate filenames are automatically resolved.
- A detailed processing status is displayed for every uploaded file.

---

## Performance

The application is optimized for bulk processing and supports uploading multiple PDF files in a single batch.

Features include:

- Batch PDF processing
- Memory-efficient PDF handling
- Automatic ZIP generation
- Progress indicator
- Duplicate filename management
- Preview before download

---

## Future Improvements

Potential enhancements include:

- Drag-and-drop folder support
- OCR support for scanned PDFs
- Excel report export
- Custom filename templates
- Advanced search and filtering
- Docker deployment
- User authentication
- Cloud storage integration
- Translating draft into anotehr language

---

## License

This project is intended for educational and document automation purposes.

---

## Author

**Saptarshi Bandyopadhyay**

Machine Learning Specialist | Data Analyst | Python Developer

GitHub: [https://github.com/your-username](https://github.com/Saptarshi-ux)
LinkedIn: [https://linkedin.com/in/your-profile](https://www.linkedin.com/in/saptarshi-sb1729/)
