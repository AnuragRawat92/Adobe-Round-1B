import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text content from all pages of a given PDF file.

    Parameters:
        pdf_path (str): Path to the PDF file.

    Returns:
        List[Dict]: A list of dictionaries, each containing the page number,
                    extracted text, and a title for the page.
    """
    
    # Open the PDF file using PyMuPDF
    doc = fitz.open(pdf_path)
    pages = []

    # Iterate through each page in the PDF
    for page_number, page in enumerate(doc, start=1):
        # Extract plain text from the current page
        text = page.get_text()

        # Append structured page data to the list
        pages.append({
            "page_number": page_number,  # 1-based index
            "text": text,                # Raw extracted text
            "title": f"Page {page_number}"  # Optional title field
        })

    # Return the list of extracted page data
    return pages
