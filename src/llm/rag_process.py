from src.embedding import EmbeddingModel
from src.configuration import Config
from google.cloud import firestore
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


class RagProcessing:
    def __init__(self, query: str):
        self.query = query
        self.config = Config()
        self.client = firestore.Client(project=self.config.PROJECT_ID)
        self.embedding = EmbeddingModel()

    def define_llm(self):
        llm_model = ChatGroq(model_name=self.config.LLM_MODEL_NAME)

        return llm_model

    def define_prompt(self):
        prompt = PromptTemplate(
            template="""
            Você é um recomendador de produtos eletrônicos. Sua base de conhecimento
            será obtida através de um processo de RAG em uma base de vetores.
            Você recebera um contexto e deverá responser a pergunta do usuário.

            Pergunta: {query}\n\n
            Contexto: {context} 
            """,
            input_variables=["query", "context"],
        )

        return prompt

    def rag_chain(self):
        self.context = self.embedding.similarity_search_execution(self.query)

        prompt = self.define_prompt()
        llm_model = self.define_llm()

        chain = prompt | llm_model
        response = chain.invoke({"query": self.query, "context": self.context})

        return response.content
