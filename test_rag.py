"""
Test the Simple RAG system
"""
from simple_rag import SimpleRAG

def main():
    print(" Simple RAG Test")
    print("=" * 30)
    
    # Create RAG system
    rag = SimpleRAG()
    
    # Load our sample document
    rag.load_document("data/python_info.txt")
    
    # Test some questions
    questions = [
        "Who created Python?",
        "What is Python used for?",
        "What are Python's key features?"
    ]
    
    for question in questions:
        print(f"\n{question}")
        answer = rag.ask(question)
        print(f" {answer}")
        print("-" * 50)

if __name__ == "__main__":
    main()