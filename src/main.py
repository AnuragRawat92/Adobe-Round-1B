import os
from src.extract_text import extract_text_from_pdf
from src.rank_sections import rank_sections
from src.sub_section_analysis import get_refined_text
from src.utils import load_persona_job, save_output

def process_collection(collection_name: str):
    """
    Processes a single document collection:
    - Extracts text from PDFs
    - Ranks relevant sections based on persona & task
    - Refines top sections
    - Saves structured output to JSON
    """
    print(f"\n📂 Processing: {collection_name}")
    
    # Define paths for the current collection
    base_dir = f"data/{collection_name}"
    pdf_dir = os.path.join(base_dir, "input_docs")
    persona_job_file = os.path.join(base_dir, "persona_job.json")
    output_path = f"output/{collection_name}_output.json"

    # Collect all PDF file paths in the input_docs directory
    input_pdfs = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    if not input_pdfs:
        print(f"⚠️ No PDFs found in {pdf_dir}")
        return

    # Load persona and job/task from JSON file
    persona, job = load_persona_job(persona_job_file)
    persona_job = f"{persona}: {job}"

    print(f"👤 Persona: {persona}")
    print(f"🧠 Job: {job}")
    print(f"📄 PDFs to process: {len(input_pdfs)}")

    all_pages = []
    
    # Extract text page-by-page from each PDF
    for pdf in input_pdfs:
        pages = extract_text_from_pdf(pdf)
        for p in pages:
            p["document"] = os.path.basename(pdf)  # Tag each page with document name
        all_pages.extend(pages)

    # Rank the most relevant sections for the persona/job
    sections, top_indices = rank_sections(all_pages, persona_job)

    # Further refine the selected top sections
    sub_sections = get_refined_text(all_pages, top_indices)
    
    # Save final output in structured format
    save_output(
        [os.path.basename(p) for p in input_pdfs],  # List of input filenames
        persona,
        job,
        sections,
        sub_sections,
        output_path
    )
    print(f"✅ Output saved to: {output_path}")

def main():
    """
    Orchestrates processing of multiple predefined document collections.
    Each collection represents a test case with:
    - a set of PDFs
    - persona and task
    - expected customized output
    """
    collections = [
        "collection1_gnn",        # Research papers on Graph Neural Networks
        "collection2_business",   # Business analyst use case (e.g., annual reports)
        "collection3_chemistry"   # Educational content for a chemistry student
    ]

    # Run processing for each collection sequentially
    for col in collections:
        process_collection(col)

# Entry point for script execution
if __name__ == "__main__":
    main()
