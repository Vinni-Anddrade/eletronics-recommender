from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_google_firestore import FirestoreVectorStore
from configuration import Config
from data_reader import DataManipulation
from google.cloud import firestore


class EmbeddingModel:
    def __init__(self):
        self.config = Config()
        self.client = firestore.Client(project=self.config.PROJECT_ID)

        self.create_embedding()

    def create_documents(self):
        data_manager = DataManipulation(self.config.DATA_PATH)
        self.docs = data_manager.document_transforming()

    def create_embedding(self):
        embedding_model = HuggingFaceEmbeddings(
            model_name=self.config.EMBEDDING_MODEL_NAME
        )

        self.vector_store = FirestoreVectorStore(
            collection=self.config.VECTOR_COLLECTION,
            embedding_service=embedding_model,
            client=self.client,
        )

    def embedding_documents(self):
        self.create_documents()

        self.vector_store.add_documents(documents=self.docs)

    def similarity_search_execution(self, query: str):
        result = self.vector_store.similarity_search(query=query, k=2)

        return " || ".join(
            [
                f"product_name: {result[0].metadata["metadata"]["product_name"]} "
                f"--- product_description: {data.page_content}"
                for data in result
            ]
        )


if __name__ == "__main__":
    # Embedding documents into Firestore GCP pipeline (execute it exclusively to write the vectors into firestore)
    embedding_object = EmbeddingModel()
    embedding_object.embedding_documents()
