# import pandas as pd
# from download import download_dataset
# from sqlalchemy import create_engine
# import kaggle


# def main():
#     #dataset do kaggle
#     dataset_name = 'fronkongames/steam-games-dataset'

#     #caminho do arquivo baixado
#     dataset_path = './data/'
    
#     kaggle.api.dataset_download_files(dataset_name, path = dataset_path, unzip = True)
#     print(f'Dataset baixado e descompactado em {dataset_path}')

#     DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost:5432/DBSTEAMGAMES'

#     #Engine do SQLAlchemy
#     engine = create_engine(DATABASE_URI)

#     #Criando um dataframe
#     arquivo = './data/games.csv'
#     data = pd.read_csv(arquivo)
#     df = pd.DataFrame(data)
#     print(f"Dataframe criado com sucesso!")

#     #Jogando o DataFrame em uma nova tabela chamada 'games'
#     df.to_sql('games', engine, if_exists='replace', index=False)

#     print("Tabela criada e dados inseridos com sucesso!")
    

# if __name__ == '__main__':
#     main()
    


from download import download_dataset
from etlconnection import get_engine
from data_processing import load_data_from_csv, save_dataframe_to_db

def main():

    download_dataset()
    
    # URI do banco de dados
    DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost:5432/DBSTEAMGAMES'
    
    # Caminho para o arquivo CSV
    CSV_FILE_PATH = './data/games.csv'
    
    # Obtendo o engine do banco de dados
    engine = get_engine(DATABASE_URI)
    
    # Carregando dados do CSV
    df = load_data_from_csv(CSV_FILE_PATH)
    
    # Salvando dados no banco de dados
    save_dataframe_to_db(df, engine, 'games')

if __name__ == '__main__':
    main()
