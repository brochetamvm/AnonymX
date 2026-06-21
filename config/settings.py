from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str
    api_url: str
    db_user: str
    db_pass: str

    # Diz ao Pydantic para ler as variáveis do arquivo .env
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

# Instancia a configuração para o resto do sistema usar
config = Settings()