import kaggle
import pandas as pd


def download_dataset(dataset_name, dataset_path):
    
    kaggle.api.dataset_download_files(dataset_name, path = dataset_path, unzip=True)
    print(f'Dataset baixado e descompactado em {dataset_path}')


def create_dataframe(file_path):
    
    try:
        data = pd.read_csv(file_path)
        df = pd.DataFrame(data)
        print("Dataframe criado com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao criar DataFrame: {e}")
        return None