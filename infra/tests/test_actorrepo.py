import unittest
from infra.repository.actorrepo import ActorRepository
from infra.entities.actors import Actors
from infra.configs.connection import DBConnectionHandler
from decouple import config


class TesteActorRepository(unittest.TestCase):
    """Must test all methods of ActorRepository"""

    def setUp(self):
        """
        Class Constructor
        """
        self._db = DBConnectionHandler()

    def test_select_actors(self):
        """
        Select actors
        :return:
        """
        with self._db.session() as session:
            actors = session.query(Actors).all()
            assert actors