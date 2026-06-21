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
2. **Strict Data Validation:** Implements `Pydantic` as a data contract to validate incoming payloads, ensuring data quality and preventing database corruption (Parse, don't validate).
3. **GDPR Data Processor:** Utilizes `Pandas` for vectorized data manipulation:
   * **Data Minimization:** Drops unnecessary PII (e.g., phone numbers).
   * **Pseudonymization:** Applies masking algorithms to sensitive fields (e.g., emails).
   * **Data Flattening & Analytics:** Flattens nested JSON structures and generates aggregated metrics (e.g., user count by city) for Business Intelligence tools.
4. **Agnostic Persistence:** Uses `SQLAlchemy` ORM to perform bulk inserts. Currently configured for SQLite for portability, but production-ready for PostgreSQL with a single `.env` variable change.

## How to Run

1. **Clone the repository and enter the directory:**
   ```bash
   git clone https://github.com/your-username/AnonymX.git
   cd AnonymX
Create and activate the virtual environment:

Bash
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
Install dependencies:

Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file in the root directory:

Plaintext
ENVIRONMENT=development
API_URL=https://jsonplaceholder.typicode.com/users
DATABASE_URL=sqlite:///anonymx_data.db
Run the Orchestrator:

Bash
python main.py
🇮🇹 AnonymX: Pipeline Dati ETL conforme al GDPR

Panoramica del Progetto
AnonymX è una robusta pipeline ETL (Extract, Transform, Load) asincrona progettata mettendo al centro la conformità al GDPR europeo. Simula uno scenario aziendale reale: l'estrazione di dati grezzi degli utenti da un'API legacy, la loro rigorosa validazione, il mascheramento delle informazioni personali identificabili (PII) e il salvataggio dei dati puliti in un database relazionale per un utilizzo analitico sicuro.

Funzionalità e Architettura
Ingestione Asincrona: Utilizza httpx e asyncio per chiamate API non bloccanti, garantendo alte prestazioni e resilienza alla latenza di rete.

Validazione Rigorosa dei Dati: Implementa Pydantic come contratto dati per validare i payload in ingresso, garantendo la qualità dei dati ed evitando la corruzione del database.

Elaborazione Dati GDPR: Utilizza Pandas per la manipolazione vettoriale dei dati:

Minimizzazione dei dati: Elimina PII non necessarie (es. numeri di telefono).

Pseudonimizzazione: Applica algoritmi di mascheramento a campi sensibili (es. email).

Analytics: Appiattisce strutture JSON nidificate e genera metriche aggregate (es. conteggio utenti per città) per strumenti di Business Intelligence.

Persistenza Agnostica: Utilizza l'ORM SQLAlchemy per eseguire inserimenti massivi. Attualmente configurato per SQLite per portabilità, ma pronto per la produzione con PostgreSQL modificando una singola variabile nel file .env.

Come Eseguire il Progetto
Clona il repository ed entra nella cartella:

Bash
git clone https://github.com/your-username/AnonymX.git
cd AnonymX
Crea e attiva l'ambiente virtuale:

Bash
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
Installa le dipendenze:

Bash
pip install -r requirements.txt
Variabili d'Ambiente:
Crea un file .env nella cartella principale:

Plaintext
ENVIRONMENT=development
API_URL=https://jsonplaceholder.typicode.com/users
DATABASE_URL=sqlite:///anonymx_data.db
Esegui l'Orchestratore:

Bash
python main.py