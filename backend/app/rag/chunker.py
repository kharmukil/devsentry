class DocumentChunker:
    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def chunk_documents(self, documents: list[dict]) -> list[dict]:
        chunks = []

        for document in documents:
            content = document["content"]
            source = document["source"]

            for start in range(0, len(content), self.chunk_size):
                chunk_text = content[start:start + self.chunk_size]

                chunks.append(
                    {
                        "source": source,
                        "content": chunk_text,
                    }
                )

        return chunks