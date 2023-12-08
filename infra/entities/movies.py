from infra.configs.base import BASE
from sqlalchemy import Column, String, Integer


class Movies(BASE):
    """
    Entite Filme
    """
    __tablename__ = 'filmes'
    movie_title = Column(String(50), primary_key=True)  # Titulo do filme
    director = Column(String(50), nullable=False)  # Diretor
    gender = Column(String(50), nullable=False)  # Genero
    year = Column(Integer, nullable=False)

    def __repr__(self):
        """
        Representação do objeto
        :return: os dados do objeto
        """
        return (f"<Movies(title='{self.titulo}', "
                f"director='{self.diretor}', "
                f"type='{self.genero}',"
                f"year='{self.year}')>")




