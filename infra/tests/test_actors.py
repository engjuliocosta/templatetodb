import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from unittest.mock import patch

from infra.configs.base import BASE
from infra.entities.actors import Actors
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
        session.query(Actors).delete()  # Limpa a tabela antes de cada teste
        session.commit()

    def test_create_actor(self, session):
        # Teste de criação de uma instância de Actors
        actor = Actors(name="John Doe", gender="Male", movie_title="Movie 1")
        session.add(actor)
        session.commit()
        assert actor.id is not None  # Verifica se o ID foi gerado

    def test_actor_representation(self, session):
        # Teste do método __repr__ da classe
        actor = Actors(name="Jane Doe", gender="Female", movie_title="Movie 2")
        session.add(actor)
        session.commit()
        assert str(actor) == f'<Actors (name=Jane Doe, gender=Female, movie_title=Movie 2)>'

# Rodar os testes com pytest
