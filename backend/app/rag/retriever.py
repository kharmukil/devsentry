import re


class SimpleRetriever:
    def __init__(self, chunks: list[dict]):
        self.chunks = chunks

    def retrieve(self, query: str, top_k: int = 3) -> list[dict]:
        query_words = self._tokenize(query)

        scored_chunks = []

        for chunk in self.chunks:
            chunk_words = self._tokenize(chunk["content"])

            score = len(query_words.intersection(chunk_words))

            if score > 0:
                scored_chunks.append(
                    {
                        "source": chunk["source"],
                        "content": chunk["content"],
                        "score": score,
                    }
                )

        scored_chunks.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return scored_chunks[:top_k]

    def _tokenize(self, text: str) -> set[str]:
        return set(
            re.findall(
                r"\b[a-zA-Z0-9]+\b",
                text.lower(),
            )
        )