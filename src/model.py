from sentence_transformers import SentenceTransformer

# Load a pre-trained sentence transformer model
# "all-MiniLM-L6-v2" is a lightweight, efficient model for semantic similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

def encode(texts):
    """
    Encodes a list of input texts into dense vector embeddings using a pre-trained model.

    Args:
        texts (List[str]): List of sentences or paragraphs to be encoded.

    Returns:
        torch.Tensor: Tensor of embeddings (1 per input text), normalized to unit length.
    """
    return model.encode(
        texts, 
        convert_to_tensor=True,            # Return embeddings as a PyTorch tensor
        normalize_embeddings=True          # Normalize vectors to have unit length (important for cosine similarity)
    )
