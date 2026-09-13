from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from operator import itemgetter


import os

EMBEDDING_MODEL="qwen3-embedding:4b"
VECTOR_DIMENSION=1536

LLM_MODEL="qwen3:8b"

embedding = OllamaEmbeddings(model=EMBEDDING_MODEL, dimensions=VECTOR_DIMENSION)
vector_store = PineconeVectorStore(index_name=os.environ["INDEX_NAME"], embedding=embedding)
retriever = vector_store.as_retriever(search_kwargs={"k":3})
llm = ChatOllama(model=LLM_MODEL)
prompt_template = ChatPromptTemplate.from_template(template="""
    Answer the question only based on the given context:

    {context}   
    
    Question: {question}
    
    """)
    
def format_docs(documents: list[Document]) -> str:
    return "\n\n".join([document.page_content for document in documents])

def create_retrieval_chain_with_lcel():
    retrieval_chain = (
        
        RunnablePassthrough.assign(
            context=itemgetter("question") | retriever | format_docs
        )
        | prompt_template 
        | llm 
        | StrOutputParser()
    )

    return retrieval_chain

def retrieval_augmentation_generation(question: str) -> None:

    lcel_chain = retriever | (lambda x: { "context": format_docs([y.page_content for y in x]), "question": question} ) | prompt_template | llm

    response = lcel_chain.invoke(input=question)
    # return [x.page_content for x in results]
    
    return response.content

def main():
    query  = "What is pinecone in machine learning?"
    retrieval_chain = create_retrieval_chain_with_lcel()
    result = retrieval_chain.invoke({ "question": query })
    print(result)

if __name__ == "__main__":
    main()