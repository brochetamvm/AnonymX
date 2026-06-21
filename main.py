import asyncio
import logging

from src.ingestion import fetch_users_data
from src.processors import process_and_anonymize
from src.database import save_to_database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(name)s] - %(message)s"
)
logger = logging.getLogger("MainOrchestrator")

async def main():
    logger.info("=== 🚀 INICIANDO O PIPELINE ENTERPRISE ANONYMX ===")

    #Ingestão Assíncrona e Validação Rígida (Pydantic)
    logger.info("Passo 1/3: Executando extração assíncrona da API...")
    users_validated = await fetch_users_data()
    
    if not users_validated:
        logger.error("❌ Pipeline abortado: Nenhum dado válido extraído da origem.")
        return

    #Transformação de Dados e Conformidade GDPR (Pandas)
    logger.info("Passo 2/3: Tratando dados e aplicando mascaramento GDPR...")
    df_clean, df_metrics = process_and_anonymize(users_validated)

    #Persistência Robusta no Banco de Dados (SQLAlchemy)
    logger.info("Passo 3/3: Gravando dados e métricas no Banco de Dados...")
    save_to_database(df_clean, df_metrics)

    logger.info("=== 🎉 PIPELINE EXECUTADO COM SUCESSO ===")

if __name__ == "__main__":
    #O ecossistema de ingestão é assíncrono, 
    #asyncio para iniciar o loop de eventos principal do sistema.
    asyncio.run(main())