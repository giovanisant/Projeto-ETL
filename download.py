import kaggle

#func para baixar o dataset
def download_dataset():
    dataset_name = 'fronkongames/steam-games-dataset'
    kaggle.api.dataset_download_files(dataset_name, path='./dados/', unzip = True)



    