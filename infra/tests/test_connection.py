import unittest
from unittest.mock import patch, MagicMock
from infra.configs.connection import DBConnectionHandler


class TestDBConnectionHandler(unittest.TestCase):
    """Must test all class DBConnectionHandler"""

    def __init__(self, methodName: str = "runTest"):
        """Construct mock_engine"""
        super().__init__(methodName)
        self.mock_engine = None

    @patch('infra.configs.connection.config')
    @patch('infra.configs.connection.create_engine')
    def setUp(self, mock_create_engine, mock_config):
        """Set up test"""
        mock_config.return_value = 'fake_connection_string'
        mock_create_engine.return_value = self.mock_engine
        self.db_handler = DBConnectionHandler()

    def test_initialization(self):
        """Must test the initialization"""
        self.assertEqual(self.db_handler.connection_string, 'fake_connection_string')
        self.assertEqual(self.mock_engine, None)
        self.assertIsNone(self.db_handler.session)

    @patch('infra.configs.connection.create_engine')
    def test_create_database_engine(self, mock_create_engine):
        """Must test create database engine"""
        # Configura o mock para retornar um valor fictício.
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        # Chama o método a ser testado.
        engine = self.db_handler.create_database_engine()

        # Verifica se create_engine foi chamado com a string de conexão correta.
        mock_create_engine.assert_called_with('fake_connection_string')

        # Verifica se o valor retornado é o que o mock retornou.
        self.assertEqual(engine, mock_engine)

    def test_get_engine(self):
        """Must test get_engine"""
        self.assertEqual(self.mock_engine, None)

    @patch('infra.configs.connection.sessionmaker')
    def test_enter_method(self, mock_sessionmaker):
        """Must test enter_method"""
        mock_session = MagicMock()
        mock_sessionmaker.return_value = lambda: mock_session

        result = self.db_handler.__enter__()

        mock_sessionmaker.assert_called_with(bind=self.mock_engine)
        self.assertEqual(self.db_handler.session, mock_session)
        self.assertEqual(result, self.db_handler)

    def test_exit_method(self):
        """Must test exit_method"""
        # Primeiro, inicialize a session usando __enter__.
        self.db_handler.__enter__()

        # Agora, use um mock para a session.
        self.db_handler.session = MagicMock()

        # Chame __exit__.
        self.db_handler.__exit__(None, None, None)

        # Verifique se a função close foi chamada na session.
        self.db_handler.session.close.assert_called_once()