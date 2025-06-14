from transformers import pipeline, AutoTokenizer

# Load model and tokenizer
MODEL_NAME = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

MAX_TOKENS = 1024

def split_into_chunks(text, max_tokens=MAX_TOKENS):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        input_ids = tokenizer(" ".join(current_chunk), return_tensors="pt", truncation=False)["input_ids"]
        if input_ids.shape[1] >= max_tokens:
            chunks.append(" ".join(current_chunk[:-1]))  # add all except last word
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_text(text):
    """Summarize long text by chunking it into model-friendly sizes"""
    chunks = split_into_chunks(text)
    summaries = []

    for chunk in chunks:
        summary = summarizer(chunk, max_length=200, min_length=60, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    return "\n\n".join(summaries)
