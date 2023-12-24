from unittest import TestCase, mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.movies import Movies

"""
    Declare mocks here:
    Stubs are used for testing purposes
    Mocks are used for production code
"""


class ConnectionHandler:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Movies),
                     mock.call.filter(Movies.gender == "action")
                     ],
                    [Movies(title="The Matrix", gender="action", year=1999)],
                )
            ]
        )


def test_select(self):
    response = self.session.query(Movies).filter(Movies.gender == "action").all()
    assert response
