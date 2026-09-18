from pathlib import Path

from local_media_agent.movie import Movie


# 电影扫描器
class MovieScanner:
    # 扫描指定目录下的所有电影文件，返回电影列表
    def scan(self, directory: str) -> list[Movie]:
        directory_path = Path(directory)

        # 判断目录是否存在
        if not directory_path.exists():
            raise FileNotFoundError(f"目录不存在: {directory}")

        # 判断目录是否是文件夹
        if not directory_path.is_dir():
            raise NotADirectoryError(f"目录不是文件夹: {directory}")

        # 扫描文件夹下的所有电影文件
        movies = []
        # 遍历文件夹下的所有文件
        for file in directory_path.iterdir():
            if file.is_file():  # noqa: SIM102
                # 判断文件是否是电影文件
                if file.suffix.lower() in [".mp4", ".avi", ".mkv", ".mov", ".wmv"]:
                    movie = Movie(
                        name=file.name,
                        path=str(file.resolve()),
                        size=file.stat().st_size,
                        extension=file.suffix.lower(),
                    )
                    movies.append(movie)
                    print(f"电影扫描成功: {movie.name}")
        return movies
