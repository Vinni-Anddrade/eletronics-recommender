from utils.tools import read_yaml


class Config:
    def __init__(self):
        CONFIG_PATH = "../src/config/config.yaml"
        config = read_yaml(CONFIG_PATH)

        self.LLM_MODEL_NAME = config["LLM_MODEL_NAME"]
        self.EMBEDDING_MODEL_NAME = config["EMBEDDING_MODEL_NAME"]
        self.PROJECT_ID = config["PROJECT_ID"]
        self.VECTOR_COLLECTION = config["VECTOR_COLLECTION"]
        self.DATA_PATH = config["DATA_PATH"]
