"""
Simple RAG with Azure OpenAI - Step by Step
"""
import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Load environment variables
load_dotenv()

class SimpleRAG:
    def __init__(self):
        """Initialize the RAG system with Azure OpenAI"""
        print(" Initializing Simple RAG with Azure OpenAI...")
        
        # Setup Azure OpenAI Embeddings
        self.embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        # Setup Azure OpenAI Chat
        self.llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0
        )
        
        # Setup text splitter
        self.text_splitter = CharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=0
        )
        
        self.vectorstore = None
        print("Azure OpenAI RAG initialized!")
    
    def load_document(self, file_path):
        """Load a single text file"""
        print(f"📄 Loading document: {file_path}")
        
        # Load the document
        loader = TextLoader(file_path)
        document = loader.load()
        
        # Split into chunks
        chunks = self.text_splitter.split_documents(document)
        print(f"📝 Created {len(chunks)} chunks")
        
        # Create vector store
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )
        print("Document loaded and vectorized!")
    
    def ask(self, question):
        """Ask a question"""
        if not self.vectorstore:
            return " Please load a document first!"
        
        # Find relevant chunks
        docs = self.vectorstore.similarity_search(question, k=2)  # k=2 mean it gives top 2 relevant chunks
        context = "\n".join([doc.page_content for doc in docs])
        
        # Create prompt
        prompt = f"""
        Use the following context to answer the question.
        
        Context:
        {context}
        
        Question: {question}
        
        Answer:
        """
        
        # Get answer
        response = self.llm.invoke(prompt)
        return response.content