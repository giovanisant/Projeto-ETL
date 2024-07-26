import os
import pandas as pd
from sqlalchemy import create_engine
import kaggle
from dotenv import load_dotenv

#Carregar variáveis de ambiente do arquivo .env
load_dotenv('envi_variables.env')

#Baixa e descompacta o dataset do Kaggle
def download_dataset(dataset_name, dataset_path):
    
    kaggle.api.dataset_download_files(dataset_name, path = dataset_path, unzip=True)
    print(f'Dataset baixado e descompactado em {dataset_path}')

#Cria um DataFrame a partir de um arquivo CSV
def create_dataframe(file_path):
    
    try:
        data = pd.read_csv(file_path)
        df = pd.DataFrame(data)
        print("Dataframe criado com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao criar DataFrame: {e}")
        return None

#Carrega os dados do DataFrame para uma tabela no banco de dados
def load_data_to_db(df, table_name, db_uri):
    
    try:
        engine = create_engine(db_uri)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print("Tabela criada e dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados no banco de dados: {e}")

def main():
    #Configurações vindas do arquivo .env
    dataset_name = os.getenv('DATASET_NAME')
    dataset_path = os.getenv('DATASET_PATH')
    dataset_file = os.getenv('DATASET_FILE')

    #Verificar se os caminhos estão definidos
    if dataset_path is None:
        raise ValueError("A variável de ambiente DATASET_PATH não está definida")
    if dataset_file is None:
        raise ValueError("A variável de ambiente DATASET_FILE não está definida")
    
    file_path = os.path.join(dataset_path, dataset_file)
    table_name = os.getenv('TABLE_NAME')
    db_uri = os.getenv('DATABASE_URI')

    #Verificar se a URI do banco de dados está definida
    if not db_uri:
        print("Erro: A variável de ambiente DATABASE_URI não está definida.")
        return

    #Baixar e descompactar o dataset
    download_dataset(dataset_name, dataset_path)

    #Criar DataFrame
    df = create_dataframe(file_path)

    if df is not None:
        #Carregar dados no banco de dados
        load_data_to_db(df, table_name, db_uri)

if __name__ == '__main__':
    main()
