import json
from datetime import datetime
import os

def load_persona_job(persona_job_file: str):
    """
    Load the persona and job description from a JSON file.

    Args:
        persona_job_file (str): Path to the JSON file containing 'persona' and 'job'.

    Returns:
        Tuple[str, str]: The persona and job description extracted from the JSON.
    """
    with open(persona_job_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["persona"], data["job"]


def save_output(
    input_documents: list,
    persona: str,
    job: str,
    extracted_sections: list,
    sub_section_analysis: list,
    output_path: str = "output/challenge1b_output.json"
):
    """
    Save the processed output (metadata + extracted insights) to a structured JSON file.

    Args:
        input_documents (list): List of input PDF file names.
        persona (str): The target persona (e.g., 'PhD Researcher').
        job (str): Job description or task the persona wants to accomplish.
        extracted_sections (list): Ranked important sections from documents.
        sub_section_analysis (list): Refined/summarized content from top-ranked sections.
        output_path (str): File path to save the output JSON.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Prepare output data in a structured dictionary
    output_data = {
        "metadata": {
            "input_documents": input_documents,            # Names of input documents
            "persona": persona,                            # Persona provided
            "job_to_be_done": job,                         # Job or task description
            "processing_timestamp": datetime.now().isoformat()  # Timestamp of processing
        },
        "extracted_sections": extracted_sections,          # Top ranked sections
        "sub_section_analysis": sub_section_analysis       # Refined summaries of those sections
    }

    # Write the dictionary to a JSON file with pretty formatting
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
