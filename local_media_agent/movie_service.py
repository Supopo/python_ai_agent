from local_media_agent.movie import Movie
from local_media_agent.movie_repository import MovieRepository
from local_media_agent.movie_scanner import MovieScanner


class MovieService:
    def __init__(self, movie_scanner: MovieScanner, movie_repository: MovieRepository):
        self.movie_scanner = movie_scanner
        self.movie_repository = movie_repository



    # 扫描电影，添加到数据库中
    def scan_and_add_movies(self, directory: str):
        self.directory = directory
        # 扫描电影
        movies = self.movie_scanner.scan(directory)
        # 清空旧数据
        self.movie_repository.clear_all_movies()
        # 保存新数据
        for movie in movies:
            try:
                self.movie_repository.add_movie(movie)
            except ValueError as e:
                print(f"电影添加失败: {e}, 电影: {movie.name}") 
        # 返回电影列表
        return movies


    # 获取所有电影
    def get_all_movies(self) -> list[Movie]:
        return self.movie_repository.get_all_movies(self.directory)