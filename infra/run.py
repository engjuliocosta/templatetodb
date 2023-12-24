from infra.repository.movierepo import MovieRepository
from infra.repository.actorrepo import ActorRepository


repo_movies = MovieRepository()
repo_actors = ActorRepository()

response_movie = repo_movies.select_filmes()
response_actor = repo_actors.select_actors()
