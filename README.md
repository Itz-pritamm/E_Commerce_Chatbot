# 🛍️ AI-Powered E-Commerce Chatbot

An intelligent **E-Commerce Customer Support Chatbot** built using **Retrieval-Augmented Generation (RAG)**, **LangChain**, **Groq Llama 3**, **ChromaDB**, **Semantic Router**, and **SQLite**.

The chatbot provides accurate answers to customer FAQs and retrieves product information through a hybrid AI architecture that combines vector search with structured database queries.

---

## 🚀 Features

- 🤖 AI-powered conversational assistant
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic query routing
- 🛒 Product search using SQLite
- 💬 Customer FAQ support
- ⚡ Fast inference using Groq Llama 3
- 🧠 HuggingFace Embeddings
- 📦 ChromaDB Vector Database
- 🎨 Interactive Streamlit UI

---

# 🏗️ Architecture

```
                     User
                       │
               Streamlit Interface
                       │
                Semantic Router
                /              \
               /                \
        FAQ Questions      Product Queries
             │                    │
      ChromaDB Retrieval      SQLite Database
             │                    │
      Relevant Documents     Product Details
               \                /
                \              /
                 Groq Llama 3
                      │
               AI Generated Response
```

---

# 📌 Project Workflow

### 1️⃣ User asks a question

Examples

- What is your return policy?
- Show me laptops under ₹60,000.
- Which phone has the best camera?
- Can I cancel my order?

---

### 2️⃣ Semantic Router

The user's query is first classified into one of two categories:

- FAQ Query
- Product Query

This improves response accuracy while reducing unnecessary LLM calls.

---

### 3️⃣ FAQ Pipeline (RAG)

For customer support questions:

- Convert query into embeddings
- Search similar FAQs in ChromaDB
- Retrieve relevant context
- Send context to Groq Llama 3
- Generate accurate response

```
User Question
      │
Embedding Generation
      │
Similarity Search
      │
Relevant FAQs
      │
Groq Llama 3
      │
Final Answer
```

---

### 4️⃣ Product Pipeline

For product-related queries:

- Detect product intent
- Search SQLite database
- Retrieve matching products
- Send structured product information to LLM
- Generate natural language response

```
User Query
      │
SQLite Search
      │
Matching Products
      │
Groq Llama 3
      │
Final Response
```

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | Web Interface |
| LangChain | LLM Orchestration |
| Groq Llama 3 | Large Language Model |
| ChromaDB | Vector Database |
| HuggingFace Embeddings | Semantic Search |
| SQLite | Product Database |
| Semantic Router | Intent Classification |
| Pandas | Data Processing |

---

# 📂 Project Structure

```
E_Commerce_Chatbot/
│
├── app.py
├── products.db
├── faq.csv
├── requirements.txt
├── README.md
│
├── chroma_db/
│
├── chains/
│
├── prompts/
│
├── router/
│
├── utils/
│
└── assets/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Itz-pritamm/E_Commerce_Chatbot.git
```

Move into the project directory

```bash
cd E_Commerce_Chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 💡 Example Queries

### FAQ

- What is your return policy?
- How long does shipping take?
- Can I cancel my order?
- Do you provide warranty?

### Product

- Show me gaming laptops
- Best phone under ₹30,000
- Recommend wireless headphones
- Which laptop has 16GB RAM?
- Show products from Samsung

---

# 🎯 Key AI Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector Search
- Semantic Search
- Intent Classification
- Prompt Engineering
- Large Language Models (LLMs)
- AI Chatbots
- Hybrid Search Architecture
- Structured + Unstructured Data Retrieval

---

# 📈 Future Improvements

- Conversation Memory
- Order Tracking Integration
- Voice Assistant Support
- Multi-language Support
- Recommendation Engine
- User Authentication
- Admin Dashboard
- Product Recommendation using Hybrid Search
- Deployment on AWS/GCP/Azure

---

# 📸 Demo

Add screenshots or a GIF of the application here.

Example:

```
assets/homepage.png
assets/chatbot_demo.gif
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 👨‍💻 Author

**Pritam Gupta**

GitHub: https://github.com/Itz-pritamm

LinkedIn: Add your LinkedIn profile here.

---

# ⭐ If you found this project useful, consider giving it a Star!
