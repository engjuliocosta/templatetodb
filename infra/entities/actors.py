from infra.configs.base import BASE
from sqlalchemy import Column, String, Integer, ForeignKey


class Actors(BASE):
    """Actors table"""
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    movie_title = Column(Integer, ForeignKey("films.movie_title"))

    def __repr__(self):
        """Represent actors table"""
        return (f'<Actors (name={self.name}, '
                f'gender={self.gender}, '
                f'movie_title={self.movie_title})>')
