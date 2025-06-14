"""
summarizer.py

Summarizes long-form research text by chunking it into model-compatible segments
and generating concise summaries using a pretrained transformer model.

Author: Jagadeswara Pavan Kumar Varma Pothuri
"""

from transformers import pipeline, AutoTokenizer

# Model and configuration
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
MAX_TOKENS = 1024
MAX_SUMMARY_LENGTH = 120
MIN_SUMMARY_LENGTH = 40

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
summarizer = pipeline("summarization", model=MODEL_NAME)

def split_into_chunks(text: str, max_tokens: int = MAX_TOKENS) -> list:
    """
    Splits input text into smaller chunks that fit within the model's token limit.

    Args:
        text (str): Input text to be chunked.
        max_tokens (int): Maximum number of tokens allowed per chunk.

    Returns:
        list: A list of text chunks suitable for summarization.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        input_ids = tokenizer(" ".join(current_chunk), return_tensors="pt", truncation=False)["input_ids"]
        if input_ids.shape[1] >= max_tokens:
            chunks.append(" ".join(current_chunk[:-1]))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_text(text: str) -> str:
    """
    Summarizes the full input text by processing it in manageable chunks.

    Args:
        text (str): Full input text to summarize.

    Returns:
        str: The aggregated summary.
    """
    chunks = split_into_chunks(text)

    if not chunks:
        return "No content available for summarization."

    try:
        summaries_raw = summarizer(
            chunks,
            max_length=MAX_SUMMARY_LENGTH,
            min_length=MIN_SUMMARY_LENGTH,
            do_sample=False
        )
        summaries = [
            f"Chunk {i + 1}:\n{res['summary_text']}"
            for i, res in enumerate(summaries_raw)
        ]
    except Exception as e:
        return f"Error during summarization:\n{str(e)}"

    return "\n\n".join(summaries)
