from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config


class DBConnectionHandler:
    """
    Classe de conexão com o banco
    """

    def __init__(self):
        """
        Método construtor
        """
        self.connection_string = config("CONNECTION_STRING")
        self.engine = self.create_database_engine()
        self.session = None

    def create_database_engine(self):
        """
        Cria o engine de conexão
        """
        engine = create_engine(self.connection_string)
        return engine

    def get_engine(self):
        """
        Retorna o engine de conexão
        """
        return self.engine

    def __enter__(self):
        """
        Método de entrada
        """
        session_make = sessionmaker(bind=self.engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método de saída
        """
        self.session.close()
