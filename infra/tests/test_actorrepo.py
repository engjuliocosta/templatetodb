import pytest
import unittest
from unittest.mock import patch, MagicMock
from infra.repository.actorrepo import ActorRepository
from infra.entities.actors import Actors


class TestActorRepository(unittest.TestCase):

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test__init__(self, mock_db):
        """
        Must test if the class is initialized
        """
        self.repository = ActorRepository()
        mock_db.assert_called_once()

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_select_actors(self, mock_db):
        """
        Must est if the select_actors method returns actors correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = ActorRepository()

        # Mock response
        fake_actors = [MagicMock(), MagicMock()]
        self.mock_session.query.return_value.all.return_value = fake_actors

        # Call the method
        result = self.repository.select_actors()

        # Assertions
        self.mock_session.query.assert_called_once()
        assert result == fake_actors

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_insert_actor_success(self, mock_db):
        """
        Must test if the insert_actor method inserts correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = ActorRepository()

        # Mock response
        fake_actor = Actors()
        self.repository.insert_actor(fake_actor)

        self.mock_session.add.assert_called_with(fake_actor)
        self.mock_session.commit.assert_called_once()

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_insert_data_failure(self, mock_db):
        """
        Must test if the insert_actor method raises an exception
        """
        # Configurando o mock da sessão
        mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = mock_session

        # Criando o repository com a sessão mockada
        repository = ActorRepository()

        # Configurando o mock para simular uma exceção ao adicionar um filme
        fake_actor = Actors()
        mock_session.add.side_effect = Exception("Erro simulado")

        # Testando se uma exceção é levantada
        with pytest.raises(Exception) as exc_info:
            repository.insert_actor(fake_actor)

        # Verificações
        assert "Erro simulado" in str(exc_info.value)
        mock_session.rollback.assert_called_once()

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_delete_success(self, mock_db):
        """
        Must test if the delete_actor method deletes correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = ActorRepository()

        # Mock response
        fake_actor = Actors()
        self.repository.delete_actor(fake_actor)

        self.mock_session.delete.assert_called_with(fake_actor)
        self.mock_session.commit.assert_called_once()

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_delete_failure(self, mock_db):
        """
        Must test if the delete_actor method raises an exception
        """
        # Configurando o mock da sessão
        mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = mock_session
        mock_session.delete.side_effect = Exception("Erro simulado")

        repository = ActorRepository()

        fake_actor = Actors()

        with pytest.raises(Exception) as exc_info:
            repository.delete_actor(fake_actor)

        assert "Erro simulado" in str(exc_info.value)
        mock_session.rollback.assert_called_once()

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_update_success(self, mock_db):
        """
        Must test if the update_actor method updates correctly
        """
        self.mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = self.mock_session
        self.repository = ActorRepository()

        # Mock response
        fake_actor = Actors()
        self.repository.update_actor(fake_actor)

        self.mock_session.merge.assert_called_with(fake_actor)
        self.mock_session.commit.assert_called_once()

    @patch('infra.repository.actorrepo.DBConnectionHandler')
    def test_update_failure(self, mock_db):
        """
        Must test if the update_actor method raises an exception
        """
        # Configurando o mock da sessão
        mock_session = MagicMock()
        mock_db.return_value.session.return_value.__enter__.return_value = mock_session
        mock_session.merge.side_effect = Exception("Erro simulado")

        repository = ActorRepository()

        fake_actor = Actors()

        with pytest.raises(Exception) as exc_info:
            repository.update_actor(fake_actor)

        assert "Erro simulado" in str(exc_info.value)
        mock_session.rollback.assert_called_once()


if __name__ == '__main__':
    unittest.main()
