# PDF RO Name Renamer

A Streamlit-based web application that automatically extracts specific information from PDF files and renames them according to a predefined naming convention.

The application is designed to automate the tedious process of renaming large batches of PDF reports, significantly reducing manual effort and minimizing human error.

---

## Features

- Upload multiple PDF files simultaneously
- Automatically extract:
  - Divisional Office
  - RO Name
- Rename PDFs using the following format:

```
<Divisional_Office>_<RO_Name>.pdf
```

### Example

Input:

```
report_68515.pdf
```

Extracted Data:

```
Divisional Office : Durgapur DO
RO Name           : M/S JAYSWAL AUTO SERVICE
```

Output:

```
Durgapur_DO_M_S_JAYSWAL_AUTO_SERVICE.pdf
```

---

## How It Works

1. Upload one or more PDF files.
2. The application reads the text from each PDF.
3. It extracts:
   - Divisional Office
   - RO Name
4. The extracted values are sanitized to create valid filenames.
5. Every PDF is renamed automatically.
6. All renamed PDFs are packaged into a ZIP archive.
7. Download the ZIP with a single click.

---

## Preview

The application displays a preview table before downloading.

| Original File | Divisional Office | RO Name | New File |
|---------------|-------------------|---------|----------|
| report_68515.pdf | Durgapur DO | M/S JAYSWAL AUTO SERVICE | Durgapur_DO_M_S_JAYSWAL_AUTO_SERVICE.pdf |

---

## Technologies Used

- Python
- Streamlit
- PyMuPDF (fitz)
- pandas
- Regular Expressions (Regex)
- zipfile
- io

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

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

## Dependencies

```
streamlit
PyMuPDF
pandas
```

---

## Supported PDF Format

The application expects PDF files containing text-based content where the following information is available:

- Divisional Office
- RO Name

These values are extracted automatically and used to generate the output filename.

---

## Output Format

The generated filename follows the convention:

```
<Divisional_Office>_<RO_Name>.pdf
```

Example:

```
Kolkata_DO_M_S_TRINATH_SERVICE_STATION_(I-548).pdf
```

---

## Error Handling

If the required information cannot be extracted from a PDF, the application labels it as:

```
ERROR_<original_filename>.pdf
```

This makes it easy to identify files that require manual review.

---

## Key Highlights

- Batch processing of multiple PDF files
- Automatic metadata extraction
- Intelligent filename sanitization
- Duplicate filename handling
- ZIP archive generation
- Progress bar for processing status
- Preview table before download
- User-friendly web interface

---

## Future Enhancements

- OCR support for scanned PDFs
- Folder upload support
- Excel report containing original and renamed filenames
- Custom naming pattern configuration
- Search and filtering in preview table
- Desktop executable (.exe) version
- Cloud deployment support

---

## Author

Developed by **Saptarshi Bandyopadhyay**

Python | Streamlit | Data Analytics | Automation
