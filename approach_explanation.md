# Approach Explanation – Round 1B: Persona-Driven Document Intelligence

## Objective

The goal of this challenge is to build a Persona-Driven Document Intelligence System that extracts and ranks the most relevant sections from a collection of documents, based on a given persona and their job-to-be-done. This combines intelligent document understanding with personalized context awareness — enabling targeted summarization for specific roles such as a PhD Researcher, Investment Analyst, or Student.

## Methodology

Our solution is implemented as a modular pipeline consisting of the following stages:

### 1. PDF Text Extraction

We use PyMuPDF (fitz) to extract page-level text from PDFs. Each page is stored with metadata such as page number, document name, and raw text. This granularity enables semantic filtering later in the pipeline.

### 2. Persona Conditioning

The system reads a JSON file containing the persona and job description:

```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job": "Prepare a comprehensive literature review..."
}
```
These are concatenated into a single semantic query string used for matching relevant content in the documents.

3. Semantic Ranking (Top-K Retrieval)
Each page and the query are embedded using the SentenceTransformer model (all-MiniLM-L6-v2). Cosine similarity is computed between the query and each page embedding, and the top-K most relevant pages (typically K=5) are selected for deeper analysis.

4. Subsection Refinement
Top-ranked pages often contain a mix of useful and generic content. We apply further filtering and light summarization to extract precise sub-sections that better match the persona’s intent. This stage is designed to be easily extended to include more advanced models.

5. Output Serialization
The final structured results are saved in a JSON format for each collection under the output/ directory. Each output file includes:

Metadata: input documents, persona, job, and timestamp

Ranked sections: document name, page number, section title, and importance rank

Subsection analysis: document name, refined text, and page number(s)

Dataset Handling
We process multiple collections of documents such as:

collection1_gnn: Research papers on Graph Neural Networks

collection2_business: Annual reports for tech companies

collection3_chemistry: Organic chemistry textbook chapters

Each collection contains an input_docs/ folder and a persona_job.json file. Outputs are stored separately per collection.

Constraints Compliance
Our solution is built to meet the challenge constraints:

✅ CPU-only execution

✅ Model size under 1GB

✅ Processing time under 60 seconds per collection

Docker Support
We include a Dockerfile to containerize the entire pipeline. This ensures the system runs reliably across environments without dependency issues.

To build and run:
 ```
docker build -t adobe-round-1b .
docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" adobe-round-1b
```
 This makes it easy to reproduce results and test submissions without local setup.
