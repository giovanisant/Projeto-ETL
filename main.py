import os

from dotenv import load_dotenv
from connect_postgresql import load_data_to_db
from kaggle_dataset import download_dataset
from kaggle_dataset import create_dataframe

#Carregar variáveis de ambiente do arquivo .env
load_dotenv('envi_variables.env')



def main():
 
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

    download_dataset(dataset_name, dataset_path)

    df = create_dataframe(file_path)

    if df is not None:
        load_data_to_db(df, table_name, db_uri)

if __name__ == '__main__':
    main()
