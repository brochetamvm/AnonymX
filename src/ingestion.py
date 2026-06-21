import asyncio
import httpx
import logging
from typing import List, Dict, Any

# Configurações do settings.py
from config.settings import config

# Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("IngestionPipeline")

async def fetch_users_data() -> List[Dict[str, Any]]:
    # Busca dados de usuários de forma assíncrona na API configurada.
    logger.info(f"Iniciando extração de dados da API: {config.api_url}")
    
    # O 'async with' garante que a conexão será fechada no final, funcionando como o bloco try..finally do Delphi.
    async with httpx.AsyncClient() as client:
        try:
            # Fazemos o GET assíncrono (await diz: "Eu vou buscar os dados na API. Enquanto a API não responde, devolva o controle para o Python fazer outras coisas")
            response = await client.get(config.api_url, timeout=10.0)
            
            # Valida se o status code é 200 (OK). Se for 404, 500, etc., gera um erro.
            response.raise_for_status()
            
            # Converte a resposta bruta em um dicionário Python (JSON)
            data = response.json()
            logger.info(f"Sucesso! {len(data)} registros capturados da origem.")
            
            return data
            
        except httpx.HTTPError as exc:
            logger.error(f"Falha de rede ao conectar na API: {exc}")
            return []
        except Exception as exc:
            logger.critical(f"Erro inesperado no sistema: {exc}")
            return []

# Bloco de execução isolada (só roda se você executar ESTE arquivo diretamente)
if __name__ == "__main__":
    logger.info("Iniciando teste de Ingestão Isolado...")
    
    # Executa a nossa função assíncrona
    dados_extraidos = asyncio.run(fetch_users_data())
    
    # Se conseguiu baixar os dados, mostra apenas o primeiro registro para conferirmos
    if dados_extraidos:
        print("\n--- DADOS DO PRIMEIRO USUÁRIO CAPTURADO ---")
        print(dados_extraidos[0])
        print("-------------------------------------------\n")