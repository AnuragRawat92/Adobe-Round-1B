def get_refined_text(pages, top_indices):
    """
    Extracts and lightly summarizes the text content of top-ranked pages.

    Args:
        pages (List[Dict]): List of all page dictionaries containing text and metadata.
        top_indices (List[int]): Indices of the top-ranked pages to extract from.

    Returns:
        List[Dict]: A list of dictionaries containing document name, page number, and refined text.
    """
    
    refined = []

    # Iterate over each top-ranked page index
    for idx in top_indices:
        page = pages[idx]
        text = page["text"]

        # Crude summarization: take the first 5 non-empty lines from the page
        summary = "\n".join(text.strip().split("\n")[:5])

        # Append the summary and metadata to the refined list
        refined.append({
            "document": page["document"],         # Name of the PDF document
            "page_number": page["page_number"],   # Page number in the PDF
            "refined_text": summary               # Lightly summarized content
        })

    return refined
