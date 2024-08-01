from sqlalchemy import create_engine


def load_data_to_db(df, table_name, db_uri):
    
    try:
        engine = create_engine(db_uri)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print("Tabela criada e dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados no banco de dados: {e}")