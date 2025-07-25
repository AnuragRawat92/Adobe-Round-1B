from .model import encode
import torch

def rank_sections(pages, persona_job_desc, top_k=5):
    """
    Ranks document sections based on their relevance to the persona's job description.

    Args:
        pages (List[Dict]): List of page-level dictionaries containing text and metadata.
        persona_job_desc (str): Combined persona and job description as a single string.
        top_k (int): Number of top relevant sections to return.

    Returns:
        Tuple[List[Dict], List[int]]: 
            - List of top-k ranked section metadata (with document, page number, etc.)
            - List of corresponding indices for these top-k pages.
    """
    
    # Extract plain text from all pages
    doc_texts = [p["text"] for p in pages]

    # Generate dense vector embeddings for each page
    doc_embeddings = encode(doc_texts)

    # Encode the persona-job description into an embedding (1D tensor)
    query_embedding = encode([persona_job_desc])[0]

    # Compute similarity scores (dot product here, equivalent to cosine if normalized)
    scores = torch.matmul(doc_embeddings, query_embedding)

    # Get indices of the top-k most relevant sections
    ranked_indices = torch.topk(scores, k=min(top_k, len(pages))).indices.cpu().numpy()

    # Build metadata list for top-k ranked sections
    ranked_sections = []
    for rank, idx in enumerate(ranked_indices, start=1):
        page = pages[idx]
        ranked_sections.append({
            "document": page["document"],         # PDF file name
            "page_number": page["page_number"],   # Page number in the PDF
            "section_title": page["title"],       # Section title (e.g., Page 3)
            "importance_rank": rank               # Rank based on similarity score
        })

    return ranked_sections, ranked_indices
