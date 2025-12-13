import pandas as pd
from langchain_core.documents import Document


class DataManipulation:
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.path, sep=",")
        return df

    def document_transforming(self):
        df = self.read_data()
        docs = [
            Document(
                page_content=row["review"],
                metadata={"product_name": row["product_title"]},
            )
            for _, row in df.iterrows()
        ]

        return docs
