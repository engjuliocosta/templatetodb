import pytest
import unittest
from unittest.mock import patch, MagicMock
from infra.repository.movierepo import MovieRepository
from infra.entities.movies import Movies


class TestMovieRepository(unittest.TestCase):

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test__init__(self, mock_db):
        """
        Must test if the class is initialized
        """
        self.repository = MovieRepository()
        mock_db.assert_called_once()

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_select_filmes(self, mock_db):
        """
        Must est if the select_filmes method returns movies correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = MovieRepository()

        # Mock response
        fake_movies = [MagicMock(), MagicMock()]
        self.mock_session.query.return_value.all.return_value = fake_movies

        # Call the method
        result = self.repository.select_filmes()

        # Assertions
        self.mock_session.query.assert_called_once()
        assert result == fake_movies

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_insert_filme_success(self, mock_db):
        """
        Must test if the insert_filme method inserts correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = MovieRepository()

        # Mock response
        fake_movie = Movies()
        self.repository.insert_filme(fake_movie)

        self.mock_session.add.assert_called_with(fake_movie)
        self.mock_session.commit.assert_called_once()

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_insert_data_failure(self, mock_db):
        """
        Must test if the insert_filme method raises an exception
        """
        # Configurando o mock da sessão
        mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = mock_session

        # Criando o repository com a sessão mockada
        repository = MovieRepository()

        # Configurando o mock para simular uma exceção ao adicionar um filme
        fake_movie = Movies()
        mock_session.add.side_effect = Exception("Erro simulado")

        # Testando se uma exceção é levantada
        with pytest.raises(Exception) as exc_info:
            repository.insert_filme(fake_movie)

        # Verificações
        assert "Erro simulado" in str(exc_info.value)
        mock_session.rollback.assert_called_once()

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_delete_success(self, mock_db):
        """
        Must test if the delete_filme method deletes correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = MovieRepository()

        # Mock response
        fake_movie = Movies()
        self.repository.delete_filme(fake_movie)

        self.mock_session.delete.assert_called_with(fake_movie)
        self.mock_session.commit.assert_called_once()

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_delete_failure(self, mock_db):
        """
        Must test if the delete_filme method raises an exception
        """
        # Configurando o mock da sessão
        mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = mock_session
        mock_session.delete.side_effect = Exception("Erro simulado")

        repository = MovieRepository()

        fake_movie = Movies()

        with pytest.raises(Exception) as exc_info:
            repository.delete_filme(fake_movie)

        assert "Erro simulado" in str(exc_info.value)
        mock_session.rollback.assert_called_once()

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_update_success(self, mock_db):
        """
        Must test if the update_filme method updates correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = MovieRepository()

        # Mock response
        fake_movie = Movies()
        self.repository.update_filme(fake_movie)

        self.mock_session.merge.assert_called_with(fake_movie)
        self.mock_session.commit.assert_called_once()

    @patch('infra.repository.movierepo.DBConnectionHandler')
    def test_update_failure(self, mock_db):
        """
        Must test if the update_filme method raises an exception
        """
        # Configurando o mock da sessão
        mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = mock_session
        mock_session.merge.side_effect = Exception("Erro simulado")

        repository = MovieRepository()

        fake_movie = Movies()

        with pytest.raises(Exception) as exc_info:
            repository.update_filme(fake_movie)

        assert "Erro simulado" in str(exc_info.value)
        mock_session.rollback.assert_called_once()


if __name__ == '__main__':
    unittest.main()
