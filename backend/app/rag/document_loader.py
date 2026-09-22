from pathlib import Path


class DocumentLoader:
    def __init__(self, data_directory: str):
        self.data_directory = Path(data_directory)

    def load_documents(self) -> list[dict]:
        documents = []

        for file_path in self.data_directory.glob("*.md"):
            documents.append(
                {
                    "source": str(file_path),
                    "content": file_path.read_text(encoding="utf-8"),
                }
            )

        return documents