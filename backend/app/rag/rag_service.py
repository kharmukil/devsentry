from backend.app.rag.chunker import DocumentChunker
from backend.app.rag.document_loader import DocumentLoader
from backend.app.rag.retriever import SimpleRetriever


class RAGService:
    def __init__(self, data_directory: str):
        self.loader = DocumentLoader(data_directory)
        self.chunker = DocumentChunker(500)

        documents = self.loader.load_documents()
        chunks = self.chunker.chunk_documents(documents)

        self.retriever = SimpleRetriever(chunks)

    def retrieve(self, query: str, top_k: int = 3) -> list[dict]:
        return self.retriever.retrieve(
            query,
            top_k=top_k,
        )