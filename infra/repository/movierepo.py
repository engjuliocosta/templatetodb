from infra.configs.connection import DBConnectionHandler
from infra.entities.movies import Movies


class MovieRepository:
    """
    Movie Repository
    """

    def __init__(self):
        """
        Class Constructor
        """
        self._db = DBConnectionHandler()

    def select_filmes(self):
        """
        Select movies
        :return:
        """
        with self._db.session() as session:
            filmes = session.query(Movies).all()
            return filmes

    def insert_filme(self, filme: Movies):
        """
        Insertion of a movie
        :param filme:
        :return:
        """
        with self._db.session() as session:
            try:
                session.add(filme)
                session.commit()
            except:
                session.rollback()
                raise

    def delete_filme(self, filme: Movies):
        """
        Delete a movie
        :param filme:
        :return:
        """
        with self._db.session() as session:
            try:
                session.delete(filme)
                session.commit()
            except:
                session.rollback()
                raise

    def update_filme(self, filme: Movies):
        """
        Update a movie
        :param filme:
        :return:
        """
        with self._db.session() as session:
            try:
                session.merge(filme)
                session.commit()
            except:
                session.rollback()
                raise
