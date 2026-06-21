import logging
import pandas as pd
from sqlalchemy import create_engine
from config.settings import config

logger = logging.getLogger("DatabaseManager")

def save_to_database(df_clean: pd.DataFrame, df_metrics: pd.DataFrame):
    #Recebe os DataFrames processados e salva no banco de dados usando SQLAlchemy
    if df_clean.empty:
        logger.warning("Nenhum dado para salvar no banco.")
        return

    logger.info(f"Conectando ao banco de dados: {config.database_url}")
    
    try:
        #Cria o 'motor' de conexão (Equivalente ao TFDConnection do Delphi)
        engine = create_engine(config.database_url)

        #Salva a tabela de usuários limpos (com GDPR aplicada)
        #O if_exists='replace' recria a tabela do zero (ótimo para testes)
        #Em produção, usaríamos 'append' para adicionar novas linhas
        df_clean.to_sql('users_anonymized', engine, index=False, if_exists='replace')
        logger.info(f"Tabela 'users_anonymized' salva com sucesso ({len(df_clean)} registros).")

        #Salva a tabela analítica de cidades
        df_metrics.to_sql('city_metrics', engine, index=False, if_exists='replace')
        logger.info(f"Tabela 'city_metrics' salva com sucesso ({len(df_metrics)} registros).")
        
    except Exception as e:
        logger.error(f"Erro ao salvar no banco de dados: {e}")

#testes
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    #DataFrames "falsos" rapidinho só para testar a conexão com o banco
    df_teste_users = pd.DataFrame([{"id": 1, "name": "Marcus", "email": "m***s@italia.com"}])
    df_teste_metrics = pd.DataFrame([{"city": "Roma", "user_count": 1}])
    
    logger.info("Iniciando teste isolado do banco de dados...")
    save_to_database(df_teste_users, df_teste_metrics)