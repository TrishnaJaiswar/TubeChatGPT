from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough , RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "IIvORO248Zs"

try:
    ytt = YouTubeTranscriptApi()

    transcript_list = ytt.list(video_id)

    transcript = transcript_list.find_transcript(["en"])

    fetched = transcript.fetch()

    text = " ".join(chunk.text for chunk in fetched)

    print(text)

except Exception as e:
    print(type(e).__name__)
    print(e)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = splitter.create_documents([text])


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.index_to_docstore_id



retriever  = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":2})

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY from the provided, just say you don't know if you don't know the answer.
    {context}
    Question: {question}
    """,
    input_variables=["context",'question']
)

question = input("Enter your question:")
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({'context': context_text, "question": question})

answer = llm.invoke(final_prompt)


def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})  

parser = StrOutputParser()
main_chain = parallel_chain | prompt | llm | parser

def ask_question(question):
    return main_chain.invoke(question)


