from dotenv import load_dotenv

from google.cloud import firestore
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from src.embedding import EmbeddingModel
from src.configuration import Config


load_dotenv()


class RagProcessing:
    def __init__(self):
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

            Caso o contexto não tenha relação com a pergunta, responsa por
            sua própria conta. Pode acontecer com perguntas simples e cumprimentos
            """,
            input_variables=["query", "context"],
        )
        return prompt

    def rag_chain(self, query):
        self.context = self.embedding.similarity_search_execution(query)

        prompt = self.define_prompt()
        llm_model = self.define_llm()

        chain = prompt | llm_model
        response = chain.invoke({"query": query, "context": self.context})
        return response.content
