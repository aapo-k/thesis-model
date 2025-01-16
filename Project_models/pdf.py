import asyncio

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

#Make sure this is the location of your pdf file
file_path = (
    "file path"
)

#Loads pdf page by page
async def load_pages():
    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

#Searches each page by vectorizing them and using OpenAI text embeddings.. For better response quality, the chunks can be optimized.
def pdf_vector_search(query: str) -> str:
    pages = asyncio.run(load_pages())
    vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-small"))
    docs = vector_store.similarity_search(query, k=2)
    results = ""
    for doc in docs:
        results += f'Page {doc.metadata["page"]}: {doc.page_content}\n\n'
    return results

#print(pdf_vector_search("lignin"))
