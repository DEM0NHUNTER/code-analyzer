# Aegis Code Analyzer (Microservice)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-e92063?style=for-the-badge&logo=pydantic)
![AST](https://img.shields.io/badge/AST-Parsing-yellow?style=for-the-badge)

A high-performance static analysis engine designed to evaluate code quality and complexity metrics.

This microservice acts as the "Brain" of the Aegis developer platform, parsing raw Python source code into an **Abstract Syntax Tree (AST)** to calculate Cyclomatic Complexity and extraction function metadata without executing the potentially unsafe code.

---

## 🏗 Architecture

This service is built as a stateless microservice using **FastAPI** for high-throughput asynchronous processing.

* **Core Engine:** Uses `radon` and standard `ast` libraries to traverse the syntax tree.
* **Validation:** **Pydantic V2** ensures strict typing of incoming payloads, preventing injection attacks.
* **Performance:** Capable of analyzing thousands of lines of code in milliseconds.

### The Pipeline
1.  **Ingest:** API receives raw code string via POST.
2.  **Parse:** Code is tokenized and converted to an AST.
3.  **Analyze:** Visitors traverse the tree to count decision points (branches, loops).
4.  **Report:** Returns a structured JSON report with complexity scores per function.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+

### 1. Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate  # Windows
# source venv/bin/activate  # Mac/Linux
