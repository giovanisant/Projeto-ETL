import pandas as pd

def load_data_from_csv(file_path):
    
    # Carrega dados de um arquivo CSV em um DataFrame do Pandas.
 
    data = pd.read_csv(file_path)
    df = pd.DataFrame(data)
    print(f"DataFrame criado com sucesso!")
    return df

def save_dataframe_to_db(df, engine, table_name):
    
    # Salva o DataFrame em uma tabela no banco de dados.
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Tabela '{table_name}' criada e dados inseridos com sucesso!")
