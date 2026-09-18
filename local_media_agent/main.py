import sys
from pathlib import Path

# 保证无论怎么启动，都能找到本包
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from local_media_agent.movie_repository import MovieRepository
from local_media_agent.movie_scanner import MovieScanner
from local_media_agent.movie_service import MovieService


def main():
    print("=" * 50)
    print("Movie Agent - Day 2")
    print("=" * 50)

    # 创建对象
    movie_scanner = MovieScanner()
    movie_repository = MovieRepository()
    movie_service = MovieService(movie_scanner, movie_repository)

    # 输入扫描目录，并扫描电影
    directory = input("请输入扫描目录: ")

    print()
    print("正在扫描电影...")
    print()

    # 扫描电影，并存到数据库中
    movie_service.scan_and_add_movies(directory)

    print()
    print("扫描完成")
    print() 

    # 显示所有电影
    movies = movie_service.get_all_movies()
    print(f"共找到 {len(movies)} 部电影")
    for movie in movies:
        print(f"电影名称: {movie.name},\r\n路径: {movie.path}, \r\n大小: {movie.size}, \r\n扩展名: {movie.extension}, \r\n-----")

    


if __name__ == "__main__":
    main()
