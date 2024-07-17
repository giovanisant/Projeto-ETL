import kaggle

#func para baixar o dataset
def download_dataset():
    #dataset do kaggle
    dataset_name = 'fronkongames/steam-games-dataset'

    #caminho do arquivo baixado
    dataset_path = './data/'
    
    kaggle.api.dataset_download_files(dataset_name, path = dataset_path, unzip = True)
    print(f'Dataset baixado e descompactado em {dataset_path}')



    