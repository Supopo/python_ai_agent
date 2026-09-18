from dataclasses import dataclass
from enum import Enum


class MediaType(Enum):
    MOVIE = "movie"
    AUDIO = "audio"
    UNKNOWN = "unknown"

@dataclass
class Movie:
    name: str   # 文件名
    path: str   # 文件路径
    size: int   # 文件大小
    extension: str  # 文件类型
    media_type: MediaType = MediaType.MOVIE # 媒体类型
    year: int | None = None # 年份

    def size_to_mb(self) -> float:
        return self.size / 1024 / 1024
    
    def size_to_gb(self) -> float:
        return self.size / 1024 / 1024 / 1024

    def __str__(self) -> str:
        return f"{self.name} ({self.extension}) "
