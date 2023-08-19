import os
import pandas as pd
import matplotlib.pyplot as plt
from pandasai import PandasAI
from langchain.llms import VertexAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.embeddings import VertexAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQAWithSourcesChain, RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain.llms import LLMChain
from langchain import PromptTemplate, OpenAI, LLMChain

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "Your service account key "

llm = VertexAI(
    model_name="text-bison@001",
    max_output_tokens=512,
    temperature=0,
    top_p=0.8,
    top_k=40,
    verbose=True
)

def supply_data(prompt):
    table_name_list = ["Table1", "Table2", "Table3", "Table4"]
    project_id = "Your GCloud Project Id"
    dataset_id = f"{project_id}.LangchainSupplychain" #.Dataset name from Bigquery

    df_dict = {}
    for table in table_name_list:
        sql_query = f"SELECT * FROM {dataset_id}.{table}"
        df = pd.read_gbq(query=sql_query, project_id=project_id)
        df_dict['df_' + table] = df

    agent = PandasAI(llm)
    res = agent([df_dict['df_' + x] for x in table_name_list], prompt=prompt)
    plt.show()
    return res

tools = [
    Tool(
        name="supply_data",
        func=lambda prompt: supply_data(str(prompt)),
        description="useful for when you need to answer questions. Input should be a fully formed question."
    ),
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=True,
    memory=ConversationBufferMemory(memory_key="chat_history", input_key='input', output_key="output")
)

result = agent({"input": "give me list of order uid "}, return_only_outputs=True)
print(result)
