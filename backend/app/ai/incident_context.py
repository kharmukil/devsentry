from backend.app.rag.rag_service import RAGService


class IncidentContext:
    def __init__(self):
        self.rag = RAGService("sample-data/project-data")

    def retrieve(self, query: str) -> list[dict]:
        return self.rag.retrieve(
            query,
            top_k=3,
        )
