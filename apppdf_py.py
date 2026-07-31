import streamlit as st
import fitz  # PyMuPDF
import re
import zipfile
import io
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="PDF RO Name Renamer",
    page_icon="📄",
    layout="wide"
)

st.title("PDF RO Name Renamer")

st.write(
    "Upload one or more PDF files. "
    "The application extracts the Divisional Office and RO Name, "
    "renames the PDFs, and provides a ZIP download."
)

# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------

def sanitize_filename(name):
    """
    Removes invalid filename characters and replaces spaces with underscores.
    """

    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r"\s+", "_", name.strip())

    return name


def extract_ro_name(text):
    """
    Extract RO Name between
    RO Name .... RO Type
    """

    match = re.search(
        r"RO Name\s*(.*?)\s*RO Type",
        text,
        flags=re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return None


def extract_divisional_office(text):
    """
    Extract the LAST occurrence of Divisional Office.

    Examples:

    Durgapur DO
    Kolkata DO
    Haldia DO
    """

    matches = re.findall(
        r"Divisional Office\s+(.+?DO)",
        text,
        flags=re.IGNORECASE
    )

    if matches:
        return matches[-1].strip()

    return None


# -------------------------------------------------
# MAIN PROCESS
# -------------------------------------------------

if uploaded_files:

    preview = []

    used_names = {}

    success_count = 0

    failed_count = 0

    zip_buffer = io.BytesIO()

    progress = st.progress(
        0,
        text="Starting..."
    )

    with zipfile.ZipFile(
        zip_buffer,
        mode="w",
        compression=zipfile.ZIP_DEFLATED
    ) as zipf:

        for index, pdf in enumerate(uploaded_files):

            try:

                progress.progress(
                    (index + 1) / len(uploaded_files),
                    text=f"Processing {index + 1} of {len(uploaded_files)}..."
                )

                pdf_bytes = pdf.getvalue()

                doc = None

                try:

                    doc = fitz.open(
                        stream=pdf_bytes,
                        filetype="pdf"
                    )

                    text = "\n".join(
                        page.get_text("text")
                        for page in doc
                    )

                finally:

                    if doc is not None:
                        doc.close()

                divisional_office = extract_divisional_office(text)

                ro_name = extract_ro_name(text)

                if divisional_office and ro_name:

                    office = sanitize_filename(divisional_office)

                    ro = sanitize_filename(ro_name)

                    filename = f"{office}_{ro}.pdf"

                    if filename in used_names:

                        used_names[filename] += 1

                        filename = (
                            f"{office}_{ro}_{used_names[filename]}.pdf"
                        )

                    else:

                        used_names[filename] = 1

                    success_count += 1

                    error_message = ""

                else:

                    filename = f"ERROR_{pdf.name}"

                    failed_count += 1

                    error_message = (
                        "Divisional Office or RO Name not found."
                    )

                preview.append(

                    {
                        "Original File": pdf.name,
                        "Divisional Office": divisional_office if divisional_office else "Not Found",
                        "RO Name": ro_name if ro_name else "Not Found",
                        "New File": filename,
                        "Status": "Success" if error_message == "" else "Failed",
                        "Error": error_message
                    }

                )

                zipf.writestr(
                    filename,
                    pdf_bytes
                )

            except Exception as e:

                failed_count += 1

                preview.append(

                    {
                        "Original File": pdf.name,
                        "Divisional Office": "Error",
                        "RO Name": "Error",
                        "New File": "Not Processed",
                        "Status": "Failed",
                        "Error": str(e)
                    }

                )

                continue

    progress.empty()

    zip_buffer.seek(0)

    st.success(
        f"""
Processed Successfully : {success_count}

Failed : {failed_count}
"""
    )

    st.subheader("Preview")

    df = pd.DataFrame(preview)

    st.dataframe(
        df,
        width="stretch"
    )

    st.download_button(
        label="Download Renamed PDFs (ZIP)",
        data=zip_buffer,
        file_name="Renamed_PDFs.zip",
        mime="application/zip"
    )
