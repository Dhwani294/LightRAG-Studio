# 🚀 LightRAG Studio Enterprise

<div align="center">

### Enterprise-Grade Document Intelligence Platform

Hybrid Retrieval • Knowledge Graphs • Agentic Search • Local LLMs • Enterprise Observability

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)]
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)]
[![LightRAG](https://img.shields.io/badge/LightRAG-Core-orange.svg)]
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]
[![Status](https://img.shields.io/badge/Status-Active%20Development-success.svg)]

</div>

---

## 📖 Overview

LightRAG Studio Enterprise is a production-grade document intelligence platform designed to transform unstructured documents into searchable knowledge.

The platform combines modern Retrieval Augmented Generation (RAG), knowledge graph construction, hybrid retrieval pipelines, and agentic workflows to enable intelligent question answering over enterprise data.

Unlike traditional RAG systems, LightRAG Studio is designed with scalability, observability, and future SaaS deployment in mind.

---

## ✨ Core Features

### Document Intelligence

- PDF ingestion
- DOCX ingestion
- TXT ingestion
- Markdown ingestion
- OCR support
- Metadata extraction
- SHA256 hashing
- Deduplication pipeline
- Intelligent chunking

### Retrieval Engine

- Vector retrieval
- Hybrid retrieval
- Semantic search
- Context compression
- Reranking pipeline
- Citation generation

### Knowledge Graph

- Entity extraction
- Relationship extraction
- Graph construction
- Graph visualization
- Graph querying

### LLM Layer

- OpenAI support
- Ollama support
- Gemini support
- Anthropic support
- Provider abstraction
- Model registry
- Cost tracking
- Token tracking

### Agentic Workflows

- Query planning
- Tool calling
- Reflection
- Self correction
- Retrieval routing
- Multi-step reasoning

### Enterprise Features

- FastAPI backend
- Structured logging
- OpenTelemetry
- Prometheus metrics
- Grafana dashboards
- JWT authentication
- RBAC
- Docker deployment
- Kubernetes readiness

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │    Frontend     │
                    │ React + Vite    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    │   API Layer     │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼

 ┌──────────────┐  ┌────────────────┐  ┌────────────────┐
 │ Ingestion    │  │ Hybrid RAG     │  │ Knowledge Graph│
 │ Engine       │  │ Engine         │  │ Engine         │
 └──────┬───────┘  └───────┬────────┘  └───────┬────────┘
        │                  │                   │
        ▼                  ▼                   ▼

 ┌──────────────┐  ┌────────────────┐  ┌────────────────┐
 │ Vector DB    │  │ Agent Layer    │  │ Graph Storage  │
 └──────────────┘  └────────────────┘  └────────────────┘

                             │
                             ▼

                    ┌─────────────────┐
                    │  LLM Providers  │
                    │ OpenAI/Ollama   │
                    │ Gemini/Claude   │
                    └─────────────────┘
```

---

## 📂 Repository Structure

```text
lightrag-studio/

├── app/
├── api/
├── core/
├── services/
├── repositories/
├── models/
├── schemas/
├── workers/
├── tests/
├── docs/
├── scripts/
├── frontend/
├── deployment/
└── data/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Dhwani294/LightRAG-Studio.git

cd lightrag-studio
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

Create:

```bash
.env
```

Example:

```env
APP_NAME=LightRAG Studio

OPENAI_API_KEY=

GEMINI_API_KEY=

ANTHROPIC_API_KEY=

DEFAULT_PROVIDER=mock

DEFAULT_MODEL=mock-model
```

---

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## 🧪 Testing

Run tests:

```bash
pytest
```

Static typing:

```bash
mypy .
```

Linting:

```bash
ruff check .
```

---

## 🛣️ Development Roadmap

### Completed

- Repository foundation
- Enterprise configuration
- Document ingestion engine
- OCR support
- Validation pipeline
- Deduplication
- LLM abstraction layer

### In Progress

- Model registry
- Dynamic provider loading

### Upcoming

- OpenAI integration
- Ollama integration
- Vector database layer
- Knowledge graph engine
- Agent orchestration
- Hybrid RAG engine
- Frontend dashboard
- Observability stack
- Kubernetes deployment

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

---

## 📜 License

MIT License

---

## ⭐ Project Vision

LightRAG Studio aims to become a fully featured open-source document intelligence platform that combines retrieval, graph reasoning, and agentic workflows into a unified enterprise-ready system.