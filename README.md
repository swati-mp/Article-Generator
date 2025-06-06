# 📝 Article Generator Chatbot

A multi-LLM powered chatbot that generates informative and structured articles based on user-given topics using open-source models like **LLaMA 2**, **Mistral**, and **Falcon**. Built with Python and Streamlit.

## 🚀 Features

- 🔁 Switch between 3 different LLMs: LLaMA 2, Mistral, Falcon (via Ollama)
- 🧠 Automatically generates articles with Introduction, Body, and Conclusion
- 📊 Tracks generation time and interaction analytics (extendable)
- 🖥️ Simple and intuitive Streamlit UI

## 📦 Tech Stack

- **Frontend/UI:** Streamlit
- **Backend:** Python
- **LLMs:** Mistral, LLaMA 2, Falcon (served locally using [Ollama](https://ollama.com/))
- **Model API Integration:** Localhost via Ollama
- **Analytics (optional extension):** SQLite / Streamlit State

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/article-generator-chatbot.git
cd article-generator-chatbot
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# Or
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama and Pull Models

Make sure [Ollama](https://ollama.com/download) is installed and running.

Then pull the required models:

```bash
ollama pull llama2
ollama pull mistral
ollama pull falcon
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
article-generator-chatbot/
│
├── app.py                     # Streamlit UI
├── llms/
│   ├── llama_model.py         # Generate article using LLaMA 2
│   ├── mistral_model.py       # Generate article using Mistral
│   └── falcon_model.py        # Generate article using Falcon
├── requirements.txt
├── README.md
└── .gitignore


## 🙋‍♀️ Developed By

**Swati Patil**
