# 🤖 Simple RAG System with Azure OpenAI

A **simple** Retrieval Augmented Generation (RAG) system that lets you ask questions about your documents using Azure OpenAI.

## 🎯 What does this do?

This system:
1. **Reads your text documents** 📄
2. **Understands them using AI** 🧠  
3. **Answers questions** about the content 💬
4. **Uses Azure OpenAI** (not regular OpenAI) ☁️

**Example:**
- You put a document about Python programming in the `data` folder
- You ask: "Who created Python?"
- It answers: "Guido van Rossum created Python" (based on your document!)

## 🚀 Quick Start (3 Steps)

### Step 1: Install the packages
```bash
pip install -r requirements.txt
```

### Step 2: Configure Azure OpenAI
Edit the `.env` file with your Azure OpenAI details:

```env
AZURE_OPENAI_API_KEY=your_actual_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your-gpt-deployment-name
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME=your-embeddings-deployment-name
```

**🔍 Where to find these in Azure Portal:**
1. Go to **Azure Portal** → **Your OpenAI Resource**
2. **API Key & Endpoint**: Click "Keys and Endpoint" 
3. **Deployment Names**: Click "Model deployments"

### Step 3: Run it!
```bash
# Test with sample questions
python test_rag.py

# OR ask your own questions interactively  
python interactive_rag.py
```

## 📁 What you need in Azure

You need an **Azure OpenAI Resource** with **2 model deployments**:

| Model Type | Example Model | What it does |
|-----------|---------------|--------------|
| **Chat Model** | GPT-4 or GPT-3.5-turbo | Generates answers |
| **Embeddings Model** | text-embedding-ada-002 | Understands document meaning |

## 📂 Files in this project

| File | What it does |
|------|-------------|
| `simple_rag.py` | 🏗️ The main RAG system |
| `test_rag.py` | 🧪 Tests with sample questions |
| `interactive_rag.py` | 💬 Ask your own questions |
| `data/python_info.txt` | 📄 Sample document |
| `.env` | ⚙️ Your Azure OpenAI settings |

## 🎮 How to use with your own documents

1. **Add your text files** to the `data` folder (only `.txt` files for now)
2. **Update the file path** in the scripts:
   ```python
   rag.load_document("data/your_document.txt")
   ```
3. **Run and ask questions!**

## 🔧 Troubleshooting

**❌ "Import errors"**: Run `pip install -r requirements.txt`

**❌ "API key error"**: Check your `.env` file has the correct Azure OpenAI details

**❌ "No documents loaded"**: Make sure you have a `.txt` file in the `data` folder

**❌ "Deployment not found"**: Check your deployment names match what's in Azure Portal

## 🤔 How it works (Simple explanation)

1. **Document Loading**: Reads your text file and splits it into chunks
2. **Vectorization**: Converts text chunks into numbers (vectors) for searching  
3. **Question Processing**: When you ask a question, it finds the most relevant chunks
4. **Answer Generation**: Sends the relevant chunks + your question to Azure OpenAI to generate an answer

**Think of it like:** A smart librarian that instantly finds relevant books and summarizes them to answer your questions! 📚✨