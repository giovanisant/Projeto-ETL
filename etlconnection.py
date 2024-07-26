

from sqlalchemy import create_engine

def get_engine(database_uri):
    
    # Cria e retorna um engine para o banco de dados usando SQLAlchemy.
  
    engine = create_engine(database_uri)
    return engine
