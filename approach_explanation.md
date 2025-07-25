Approach Explanation – Round 1B: Persona-Driven Document Intelligence
Objective
The goal of this challenge is to build a Persona-Driven Document Intelligence System that can automatically extract and rank the most relevant sections from a set of documents based on a given persona and a specific task/job. This is essentially a context-aware document summarization and filtering task tailored to specific user roles such as "PhD Researcher" or "Investment Analyst".

Methodology
Our solution is designed as a modular, extensible pipeline consisting of the following stages:

1. PDF Text Extraction
We use PyMuPDF (fitz) to extract text from input PDF documents. Each page is represented as structured data including page number, text, and source document name. This granularity helps in identifying the most relevant parts of the documents later in the pipeline.

2. Persona-Task Conditioning
The system reads a persona_job.json file containing persona and job description like:

json
Copy
Edit
{
  "persona": "PhD Researcher in Computational Biology",
  "job": "Prepare a comprehensive literature review..."
}
The two fields are concatenated to form a semantic query string used for relevance scoring in the next stage.

3. Semantic Ranking (Top-K Retrieval)
Each page and the persona-job string are embedded using a SentenceTransformer model (all-MiniLM-L6-v2). Cosine similarity is computed between the query embedding and each page embedding to rank relevance. The top K relevant pages (e.g., 5) are selected for further analysis.

4. Subsection Refinement
Selected top-K pages are further processed to refine their content and extract focused subsections. This is useful when full pages contain mixed content, and we want to retain only the segments directly related to the persona’s intent. This stage may use summarization models or simple pattern filtering for now, but is designed to be extensible.

5. Output Serialization
All results are saved to a structured JSON file under the output/ directory. The output includes:

Metadata (persona, job, input file list, timestamp)

Ranked sections

Refined sub-section texts

Testing Across Multiple Collections
The code is generalized to process multiple document sets ("collections") such as:

collection1_gnn: Academic papers related to Graph Neural Networks

collection2_business: Company annual reports for business analysis

collection3_chemistry: Educational textbook chapters for exam prep

Each collection contains its own set of input PDFs and a persona_job.json file. The output files are saved independently per collection.

Virtual Environment (venv) Setup
We use Python’s venv module to isolate dependencies and ensure reproducibility:

bash
Copy
Edit
# Create virtual environment
python -m venv venv311

# Activate (on Windows)
.\venv311\Scripts\activate

# Install dependencies
pip install -r requirements.txt
This approach avoids conflicts with global packages and ensures a consistent development environment.

Docker Support
The project includes a Dockerfile for containerized execution. This ensures that the pipeline can run consistently across different systems without needing manual environment setup. The container includes all necessary dependencies and runs the main processing script when started.

Let me know if you'd like the .md file generated, or if you want me to format it into your repository structure.