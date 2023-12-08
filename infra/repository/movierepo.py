from infra.configs.connection import DBConnectionHandler
from infra.entities.movies import Movies


class MovieRepository:
    """
    Repositório de filmes
    """

    def __init__(self):
        """
        Construtor da classe
        """
        self._db = DBConnectionHandler()

    def select_filmes(self):
        """
        Seleciona todos os filmes
        :return:
        """
        with self._db.session() as session:
            filmes = session.query(Movies).all()
            return filmes

    def insert_filme(self, filme: Movies):
        """
        Insere um filme
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
        Deleta um filme
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
        Atualiza um filme
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
