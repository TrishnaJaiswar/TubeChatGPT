# TubeChatGPT
An AI-powered YouTube learning assistant that enables real-time interaction while users watch educational videos. It answers questions, explains concepts, summarizes content, and provides contextual guidance without interrupting the learning experience.
# 🎥 YouTube Learning Assistant (RAG Chatbot)

An AI-powered chatbot that transforms YouTube videos into an interactive learning experience. Instead of passively watching videos, users can ask questions in real time and receive accurate, context-aware answers generated directly from the video's transcript.

## 🚀 Features

- 🔍 Extracts transcripts from YouTube videos
- 💬 Real-time question answering based on video content
- 🧠 Retrieval-Augmented Generation (RAG) for accurate responses
- 📄 Semantic chunking and vector embeddings for efficient retrieval
- 🤖 LLM-powered conversational interface
- ⚡ Interactive Streamlit web application
- 🎯 Helps users understand complex concepts without rewatching the entire video

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq LLM**
- **Hugging Face Embeddings**
- **Chroma Vector Database**
- **YouTube Transcript API**
- **Streamlit**

## 📌 How It Works

1. User enters a YouTube video URL.
2. The application extracts the video ID.
3. The transcript is fetched using the YouTube Transcript API.
4. The transcript is split into semantic chunks.
5. Chunks are converted into vector embeddings and stored in Chroma.
6. When a user asks a question:
   - The retriever finds the most relevant transcript chunks.
   - The retrieved context is passed to the LLM.
   - The LLM generates an accurate, context-aware answer.

## 📂 Project Workflow

```
YouTube URL
      │
      ▼
Extract Video ID
      │
      ▼
Fetch Transcript
      │
      ▼
Text Chunking
      │
      ▼
Generate Embeddings
      │
      ▼
Store in Chroma Vector DB
      │
      ▼
User Question
      │
      ▼
Retriever
      │
      ▼
LLM (Groq)
      │
      ▼
Generated Answer
```

## 🎯 Use Cases

- Interactive learning from educational YouTube videos
- Quick concept clarification
- Video summarization
- Exam preparation
- Revision without rewatching videos
- Self-paced learning

## 📸 Demo

_Add screenshots or a GIF of your application here._

## ⚙️ Installation

```bash
git clone <repository-url>

cd youtube-learning-assistant

pip install -r requirements.txt

streamlit run app.py
```

## 🔑 Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key
HF_TOKEN=your_huggingface_token
```

## 📖 Future Improvements

- Support multiple YouTube videos
- Chat history and memory
- Multi-language transcript support
- Voice-based interaction
- PDF notes generation
- Quiz generation from video content
- Video timestamp citations
- Conversation memory across sessions

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

---

**Built with ❤️ using LangChain, RAG, Groq, Chroma, and Streamlit.**
