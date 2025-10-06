"""
Interactive RAG - Ask questions from your document
"""
from simple_rag import SimpleRAG

def main():
    print(" Interactive RAG with Azure OpenAI")
    print("=" * 40)
    
    # Create RAG system
    rag = SimpleRAG()
    
    # Load the document
    print("Loading document...")
    rag.load_document("data/python_info.txt")
    
    print("\n Ready! Ask me questions about the document.")
    print("Type 'quit' to exit.\n")
    
    while True:
        # Get user question
        question = input(" Your question: ").strip()
        
        # Check if user wants to quit
        if question.lower() in ['quit', 'exit', 'q']:
            print(" Goodbye!")
            break
        
        if question:
            # Get answer from RAG
            print(" Thinking...")
            answer = rag.ask(question)
            print(f" Answer: {answer}\n")
            print("-" * 50)
        else:
            print("Please enter a question!")

if __name__ == "__main__":
    main()