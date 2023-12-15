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

    def insert_actor(self, actor: Actors):
        """
        Insertion of a movie
        :param actor:
        :return:
        """
        with self._db.session() as session:
            try:
                session.add(actor)
                session.commit()
            except:
                session.rollback()
                raise

    def delete_actor(self, actor: Actors):
        """
        Delete a movie
        :param actor:
        :return:
        """
        with self._db.session() as session:
            try:
                session.delete(actor)
                session.commit()
            except:
                session.rollback()
                raise

    def update_actor(self, actor: Actors):
        """
        Update a movie
        :param actor:
        :return:
        """
        with self._db.session() as session:
            try:
                session.merge(actor)
                session.commit()
            except:
                session.rollback()
                raise
