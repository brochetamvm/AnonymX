import asyncio
import httpx
import logging
from typing import List, Dict, Any

from config.settings import config
from src.models import UserPII

#Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("IngestionPipeline")

async def fetch_users_data() -> List[UserPII]:
    #Busca dados de usuários na API e os blinda usando o Pydantic.
    #Retorna uma lista de objetos 'UserPII' válidos.
    logger.info(f"Iniciando extração de dados da API: {config.api_url}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(config.api_url, timeout=10.0)
            response.raise_for_status()
            
            raw_data = response.json()
            logger.info(f"Sucesso! {len(raw_data)} registros brutos capturados.")
            
            # Validação
            validated_users = []
            
            for user_dict in raw_data:
                try:
                    #Tenta converter o dicionário bruto em um objeto UserPII
                    #** desempacota o dicionário (chave=valor) para dentro do modelo
                    user_valid = UserPII(**user_dict)
                    validated_users.append(user_valid)
                except Exception as val_error:
                    #Se um único usuário vier corrompido, pegamos o erro aqui,
                    #registramos no log e o sistema continua processando os outros
                    logger.warning(f"Usuário ID {user_dict.get('id')} rejeitado pelo Pydantic: {val_error}")
            
            logger.info(f"Validação concluída: {len(validated_users)} de {len(raw_data)} usuários aceitos.")
            return validated_users
            
        except httpx.HTTPError as exc:
            logger.error(f"Falha de rede ao conectar na API: {exc}")
            return []
        except Exception as exc:
            logger.critical(f"Erro inesperado no sistema: {exc}")
            return []

#teste
if __name__ == "__main__":
    logger.info("Iniciando teste de Ingestão + Validação...")
    
    users = asyncio.run(fetch_users_data())
    
    if users:
        print("\n--- TESTANDO O OBJETO VALIDADO PELO PYDANTIC ---")
        primeiro_usuario = users[0]
        
        print(f"ID: {primeiro_usuario.id}")
        print(f"Nome: {primeiro_usuario.name}")
        print(f"E-mail: {primeiro_usuario.email}")
        print(f"Cidade (Aninhada): {primeiro_usuario.address.city}")
        print("------------------------------------------------\n")
        print(users)