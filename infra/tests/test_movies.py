import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from infra.configs.base import BASE
from infra.entities.movies import Movies
from decouple import config


@pytest.fixture(scope="module")
def engine():
    """Fixture for engine"""
    connection_string = config("CONNECTION_STRING")
    return create_engine(connection_string)  # Usando SQLite em memória para testes


@pytest.fixture(scope="module")
def session(engine):
    BASE.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return session


# Testes para a classe Actors
class TestActors:
    @pytest.fixture(autouse=True)
    def prepare_db(self, session):
        session.query(Movies).delete()  # Limpa a tabela antes de cada teste
        session.commit()

    def test_create_movie(self, session):
        # Teste de criação de uma instância de Actors
        movie = Movies(movie_title="Vingadores",
                       director="Joss Whedon",
                       type="Action",
                       year=2012)
        session.add(movie)
        session.commit()
        assert movie.movie_title is not None

    def test_actor_representation(self, session):
        # Teste do método __repr__ da classe
        movie = Movies(movie_title="Vingadores",
                       director="Joss Whedon",
                       type="Action",
                       year=2012)
        session.add(movie)
        session.commit()
        assert str(movie) != (f"<Movies(title='{self.titulo}', "
                              f"director='{self.diretor}', "
                              f"type='{self.genero}',"
                              f"year='{self.year}')>")
