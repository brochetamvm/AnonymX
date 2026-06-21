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
   git clone [https://github.com/your-username/AnonymX.git](https://github.com/your-username/AnonymX.git)
   cd AnonymX