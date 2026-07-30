import streamlit as st
import fitz  # PyMuPDF
import re
import zipfile
import io
import pandas as pd

st.set_page_config(
    page_title="PDF RO Renamer",
    page_icon="📄",
    layout="wide"
)

st.title("PDF RO Name Renamer")

st.write(
    "Upload one or more PDF files. The application will automatically extract the "
    "Divisional Office and RO Name, rename each PDF, and provide a ZIP download."
)


uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type="pdf",
    accept_multiple_files=True
)


def sanitize_filename(name):
    """
    Removes invalid filename characters and replaces spaces with underscores.
    """
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r"\s+", "_", name.strip())
    return name

def extract_ro_name(text):
    """
    Extracts text between:
    RO Name .... RO Type
    """
    pattern = r"RO Name\s+(.*?)\s+RO Type"

    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()

    return None

def extract_divisional_office(text):
    """
    Extracts text between:
    Divisional Office .... Rating Details
    """

    pattern = r"Divisional Office\s+(.*?)\s+Rating Details"

    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()

    return None

if uploaded_files:

    zip_buffer = io.BytesIO()

    preview = []

    used_names = {}

    progress = st.progress(0)

    with zipfile.ZipFile(
        zip_buffer,
        "w",
        compression=zipfile.ZIP_DEFLATED
    ) as zipf:

        for index, pdf in enumerate(uploaded_files):

            # Read uploaded PDF only once
            pdf_bytes = pdf.read()

            doc = fitz.open(
                stream=pdf_bytes,
                filetype="pdf"
            )

            text = ""

            for page in doc:
                text += page.get_text()

            doc.close()

            ro_name = extract_ro_name(text)
            divisional_office = extract_divisional_office(text)

            if ro_name and divisional_office:

                office = sanitize_filename(divisional_office)
                ro = sanitize_filename(ro_name)

                new_name = f"{office}_{ro}.pdf"

                # Handle duplicate filenames
                if new_name in used_names:
                    used_names[new_name] += 1

                    new_name = (
                        f"{office}_{ro}_{used_names[new_name]}.pdf"
                    )
                else:
                    used_names[new_name] = 1

            else:
                new_name = f"ERROR_{pdf.name}"

            preview.append(
                {
                    "Original File": pdf.name,
                    "Divisional Office": divisional_office if divisional_office else "Not Found",
                    "RO Name": ro_name if ro_name else "Not Found",
                    "Renamed File": new_name
                }
            )

            # Add renamed PDF to ZIP
            zipf.writestr(new_name, pdf_bytes)

            progress.progress((index + 1) / len(uploaded_files))

    st.success(
        f"Successfully processed {len(uploaded_files)} PDF file(s)."
    )

    st.subheader("Preview")

    st.dataframe(
        pd.DataFrame(preview),
        use_container_width=True
    )

    st.download_button(
        label="Download Renamed PDFs (ZIP)",
        data=zip_buffer.getvalue(),
        file_name="Renamed_PDFs.zip",
        mime="application/zip"
    )
