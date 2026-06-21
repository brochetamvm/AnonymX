import pandas as pd
import logging
from typing import List, Tuple
from src.models import UserPII

logger = logging.getLogger("DataProcessor")

def mask_email(email: str) -> str:
    #Mascaramento simples para GDPR.
    #Exemplo: 'marcus.brocheta@empresa.it' vira 'm***a@empresa.it'
    try:
        name_part, domain = email.split('@')
        if len(name_part) > 2:
            masked_name = name_part[0] + "***" + name_part[-1]
        else:
            masked_name = "***"
        return f"{masked_name}@{domain}"
    except ValueError:
        return "***@***.com"

def process_and_anonymize(users: List[UserPII]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    #Recebe os usuários validados, aplica regras da GDPR e gera métricas
    #Retorna dois DataFrames: os dados limpos e o agrupamento por cidade

    if not users:
        logger.warning("Nenhum usuário para processar.")
        return pd.DataFrame(), pd.DataFrame()

    #Objeto Pydantic -> Dicionário -> Tabela do Pandas (DataFrame)
    #Método '.model_dump()' extrai os dados do Pydantic de forma segura
    df = pd.DataFrame([user.model_dump() for user in users])
    logger.info(f"DataFrame montado na memória com {len(df)} registros.")

    #Achatar os dados
    #Como o 'address' era uma classe aninhada, ele vem como um dicionário
    #Vamos extrair apenas a 'city' para uma coluna separada e reta
    df['city'] = df['address'].apply(lambda x: x['city'])

    #GDPR Core: Minimização de Dados e Pseudonimização
    #Se não precisamos do telefone ou do CEP para o relatório, DELETE-OS
    df = df.drop(columns=['address', 'phone'])
    
    #Aplicando a máscara no e-mail em todas as linhas de uma vez só!
    df['email'] = df['email'].apply(mask_email)
    
    #Equivalente SQL: SELECT city, COUNT(*) as user_count FROM df GROUP BY city
    city_metrics = df.groupby('city').size().reset_index(name='user_count')
    
    logger.info("Processamento e conformidade com GDPR concluídos com sucesso.")
    return df, city_metrics

#teste
if __name__ == "__main__":
    from src.models import UserAddress
    
    # Criamos um "mock" (dado falso) apenas para testar se a regra funciona
    mock_user_1 = UserPII(
        id=1, name="Marcus Brocheta", email="marcus@italia.com", 
        phone="12345", address=UserAddress(city="Roma", zipcode="00100")
    )
    mock_user_2 = UserPII(
        id=2, name="Mario Rossi", email="mario.rossi@azienda.it", 
        phone="98765", address=UserAddress(city="Milano", zipcode="20100")
    )
    mock_user_3 = UserPII(
        id=3, name="Luigi Bianchi", email="luigi@italia.com", 
        phone="55555", address=UserAddress(city="Roma", zipcode="00100")
    )
    
    df_clean, df_metrics = process_and_anonymize([mock_user_1, mock_user_2, mock_user_3])
    
    print("\n--- 🛡️ DADOS ANONIMIZADOS (Prontos para o Banco de Dados) ---")
    print(df_clean)
    
    print("\n--- 📊 MÉTRICAS AGREGADAS (Prontas para o PowerBI/Dashboards) ---")
    print(df_metrics)
    print("\n")