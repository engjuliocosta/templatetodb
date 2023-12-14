from infra.configs.connection import DBConnectionHandler
from infra.entities.actors import Actors


class ActorRepository:
    """
    Actor Repository
    """

    def __init__(self):
        """
        Class Constructor
        """
        self._db = DBConnectionHandler()

    def select_actors(self):
        """
        Select actors
        :return:
        """
        with self._db.session() as session:
            actors = session.query(Actors).all()
            return actors
