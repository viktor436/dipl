"""
Тества модел от HuggingFace Endpoints заедно с допълнено генериране от векторна база данни 
"""

#####################TEST 1 sentence##################################
import token
from langchain_community.llms import HuggingFaceEndpoint
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

HUGGINGFACEHUB_API_TOKEN = "hf_***"

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
db = Chroma(persist_directory="C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\chroma_db", embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={'k': 1})

model = HuggingFaceEndpoint(
    endpoint_url=f"https:/***.aws.endpoints.huggingface.cloud",
    huggingfacehub_api_token = HUGGINGFACEHUB_API_TOKEN,
)

prompt = ChatPromptTemplate.from_template("""[INST]Отговори на въпроса като имаш в предвид следния контекст:

<context>
{context}
</context>

Question: {input}[/INST]""")

document_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)
response = retrieval_chain.invoke({"input": "Какво гласи член 2 (2) от Валутния закон?"})
print(response["answer"])


###############################################################################################################################################
############TEST LIST###################################################################################################################################
import token
from langchain_community.llms import HuggingFaceEndpoint
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

HUGGINGFACEHUB_API_TOKEN = "hf_***"

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
db = Chroma(persist_directory="C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\chroma_db", embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={'k': 1})

model = HuggingFaceEndpoint(
    endpoint_url=f"https:/***.aws.endpoints.huggingface.cloud",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)

prompt_template = """[INST]Отговори на въпроса като имаш в предвид следния контекст:

<context>
{context}
</context>

Question: {input}[/INST]"""

prompt = ChatPromptTemplate.from_template(prompt_template)

document_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

questions = [
"Кой метали са благородни според валутния закон?",
"Кой отговаря за качеството на водите според законодателството",
"Как се определя ректор на университет според законодателството?",
"***"
]

with open("responses2.txt", "w", encoding="utf-8") as file:
    for question in questions:
        response = retrieval_chain.invoke({"input": question})
        file.write(f"Question: {question}\n")
        file.write("Answer: " + response["answer"] + "\n\n")

print("Responses have been saved to responses.txt.")