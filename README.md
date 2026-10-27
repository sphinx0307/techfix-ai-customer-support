# TechFix AI Customer Support Resolution Agent

TechFix is a local, command-line customer-support prototype that answers product questions from a small knowledge base, keeps short conversation context, drafts support tickets for common issues, applies basic request guardrails, and records feedback.

The application uses a local language model through Ollama, so it does not require a hosted LLM API.

## Features

- Retrieval-Augmented Generation (RAG) over local text documents
- FAISS similarity search over document chunks
- Mistral response generation through Ollama
- `nomic-embed-text` embeddings through Ollama
- In-session conversation memory
- Basic keyword-based safety guardrails
- Support-ticket draft generation for common issue categories
- Helpful / not-helpful feedback capture
- Local interaction logging
- Baseline keyword-response agent for comparison

## Architecture

1. The application loads the knowledge-base text files.
2. `vectorstore.py` splits the documents into chunks and creates embeddings.
3. FAISS retrieves relevant chunks for a customer query.
4. `rag_agent.py` sends the retrieved context and recent conversation history to Mistral.
5. The response is returned to the user and the interaction is logged.
6. For issue-related keywords, the agent can generate a support-ticket draft instead of performing retrieval.

See `docs/diagrams/` for the architecture and workflow diagrams.

## Technology stack

- Python 3.10+
- LangChain
- Ollama
- Mistral (`mistral`)
- `nomic-embed-text`
- FAISS CPU
- Local text files as the knowledge base

## Project structure

```text
techfix-ai-customer-support/
├── app.py
├── baseline_agent.py
├── rag_agent.py
├── vectorstore.py
├── memory.py
├── prompts.py
├── tools.py
├── utils.py
├── logger.py
├── feedback.py
├── requirements.txt
├── knowledge_base/
│   ├── faq.txt
│   ├── return_policy.txt
│   ├── troubleshooting.txt
│   └── warranty.txt
├── data/                 # Created at runtime for feedback
├── logs/                 # Created at runtime for interactions
└── docs/
    ├── diagrams/
    └── reports/
```

## Prerequisites

1. Install Python 3.10 or newer.
2. Install [Ollama](https://ollama.com/).
3. Pull the required local models:

```bash
ollama pull mistral
ollama pull nomic-embed-text
```

Keep the Ollama service running while using the application.

## Setup and run

From the project root, create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Choose `1` for the baseline agent or `2` for the RAG-based AI agent. Type `exit` to quit.

The RAG agent builds its FAISS index from the text files in `knowledge_base/` when it starts. Model downloads and initial embedding generation may take time.

## Example queries

- `How long is the laptop warranty?`
- `How long does shipping take?`
- `My laptop battery drains quickly.`
- `Is it covered under warranty?`
- `My laptop keeps overheating.`

## Runtime files and privacy

The application creates `logs/chat_logs.txt` and `data/feedback.json` during use. These files can contain user messages and generated responses, so they are excluded from version control. Do not commit real customer conversations, personal data, credentials, or secrets.

## Limitations

- This is a local prototype, not a production customer-support service.
- Guardrails and ticket categorization are keyword-based and can miss or misclassify requests.
- Conversation memory is in-memory and resets when the application exits.
- Ticket drafts are not submitted to a ticketing platform.
- The knowledge base contains example TechFix policies and should not be treated as real-world commercial policy.
- RAG can still produce incorrect answers; the prompt and retrieval setup reduce but do not eliminate hallucinations.
- Validate model behavior and all policies before any real deployment.

## License

No open-source license is included. Add a license only after deciding how you want others to be allowed to use, modify, and redistribute this project.
