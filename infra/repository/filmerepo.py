from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filme


class FilmesRepository:
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
            filmes = session.query(Filme).all()
            return filmes

    def insert_filme(self, filme: Filme):
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

    def delete_filme(self, filme: Filme):
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

    def update_filme(self, filme: Filme):
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
