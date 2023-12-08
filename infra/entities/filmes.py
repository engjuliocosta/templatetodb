from infra.configs.base import BASE
from sqlalchemy import create_engine, Column, String, Integer


class Filme(BASE):
    """
    Entidade Filme
    """
    __tablename__ = 'filmes'
    titulo = Column(String(50), primary_key=True)  # Titulo do filme
    diretor = Column(String(50), nullable=False)  # Diretor
    genero = Column(String(50), nullable=False)  # Genero

    def __repr__(self):
        """
        Representação do objeto
        :return: os dados do objeto
        """
        return f"<Filme(titulo='{self.titulo}', diretor='{self.diretor}', genero='{self.genero}')>"




