# AnonymX: GDPR-Compliant ETL Data Pipeline

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458.svg)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-e92063.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)

*(🇮🇹 Versione in Italiano in basso)*

## Project Overview
AnonymX is a robust, asynchronous **ETL (Extract, Transform, Load)** pipeline designed with **European GDPR compliance** at its core. It simulates a real-world corporate scenario: extracting raw user data from a legacy API, validating it strictly, masking Personally Identifiable Information (PII), and persisting the clean data into a relational database for secure analytical use.

## Key Features & Architecture
1. **Asynchronous Ingestion:** Uses `httpx` and `asyncio` for non-blocking API calls, ensuring high performance and resilience to network latency.
2. **Strict Data Validation:** Implements `Pydantic` as a data contract to validate incoming payloads, ensuring data quality and preventing database corruption.
3. **GDPR Data Processor:** Utilizes `Pandas` for vectorized data manipulation:
   * **Data Minimization:** Drops unnecessary PII (e.g., phone numbers).
   * **Pseudonymization:** Applies masking algorithms to sensitive fields (e.g., emails).
   * **Data Flattening & Analytics:** Flattens nested JSON structures and generates aggregated metrics for Business Intelligence tools.
4. **Agnostic Persistence:** Uses `SQLAlchemy` ORM to perform bulk inserts. Configured for SQLite for portability, production-ready for PostgreSQL.

## How to Run

**1. Clone the repository and enter the directory:**
```bash
git clone https://github.com/your-username/AnonymX.git
cd AnonymX
```

**2. Create and activate the virtual environment (Windows):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Environment Variables:**
Create a `.env` file in the root directory and add the following:
```text
ENVIRONMENT=development
API_URL=https://jsonplaceholder.typicode.com/users
DATABASE_URL=sqlite:///anonymx_data.db
```

**5. Run the Orchestrator:**
```bash
python main.py
```

---

# 🇮🇹 AnonymX: Pipeline Dati ETL conforme al GDPR

## Panoramica del Progetto
AnonymX è una robusta pipeline **ETL (Extract, Transform, Load)** asincrona progettata mettendo al centro la **conformità al GDPR europeo**. Simula uno scenario aziendale reale: l'estrazione di dati grezzi degli utenti da un'API legacy, la loro rigorosa validazione, il mascheramento delle informazioni personali identificabili (PII) e il salvataggio dei dati puliti in un database relazionale per un utilizzo analitico sicuro.

## Funzionalità e Architettura
1. **Ingestione Asincrona:** Utilizza `httpx` e `asyncio` per chiamate API non bloccanti, garantendo alte prestazioni.
2. **Validazione Rigorosa dei Dati:** Implementa `Pydantic` come contratto dati per validare i payload in ingresso.
3. **Elaborazione Dati GDPR:** Utilizza `Pandas` per la manipolazione vettoriale dei dati:
   * **Minimizzazione dei dati:** Elimina PII non necessarie (es. numeri di telefono).
   * **Pseudonimizzazione:** Applica algoritmi di mascheramento a campi sensibili (es. email).
   * **Analytics:** Appiattisce strutture JSON nidificate e genera metriche aggregate.
4. **Persistenza Agnostica:** Utilizza l'ORM `SQLAlchemy` per eseguire inserimenti massivi.

## Come Eseguire il Progetto

**1. Clona il repository ed entra nella cartella:**
```bash
git clone https://github.com/your-username/AnonymX.git
cd AnonymX
```

**2. Crea e attiva l'ambiente virtuale (Windows):**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**3. Installa le dipendenze:**
```bash
pip install -r requirements.txt
```

**4. Variabili d'Ambiente:**
Crea un file `.env` nella cartella principale e aggiungi quanto segue:
```text
ENVIRONMENT=development
API_URL=https://jsonplaceholder.typicode.com/users
DATABASE_URL=sqlite:///anonymx_data.db
```

**5. Esegui l'Orchestratore:**
```bash
python main.py