from pathlib import Path

from local_media_agent.movie import Movie


# 模拟数据库存储电影数据
class MovieRepository:
    def __init__(self):
        self.movies = []

    # 判断电影是否存在
    def is_movie_exists(self, name: str) -> bool:
        return any(movie.name == name for movie in self.movies)

    # 添加电影
    def add_movie(self, movie: Movie):
        # 判断电影是否存在
        if self.is_movie_exists(movie.name):
            raise ValueError(f"电影已存在: {movie.name}")
        # 添加电影
        self.movies.append(movie)

    # 清空所有电影
    def clear_all_movies(self):
        self.movies = []

    # 获取所有电影，返回电影列表
    def get_all_movies(self, directory: str) -> list[Movie]:
        directory_path = Path(directory).resolve()
        movies = []
        for movie in self.movies:
            movie_path = Path(movie.path).resolve()
            # 用 Path 比较，避免 J:/ 与 J:\ 分隔符不一致
            if directory_path == movie_path or directory_path in movie_path.parents:
                movies.append(movie)
        if not movies:
            raise ValueError(f"没有找到电影: {directory}")
        return movies
