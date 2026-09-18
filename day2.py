# ============================
#
#       本地媒体 AI 助手
#
# ============================
#
# 1. 扫描文件夹
# 2. 查看所有文件
# 3. 文件类型统计
# 4. 搜索文件
# 5. 退出
#
# 请输入：

from collections import Counter
from pathlib import Path


def list_files(folder_path):
    """列出目录下的所有文件。"""
    folder = Path(folder_path)
    if not folder.exists():
        print(f"路径不存在: {folder_path}")
        return []
    return [file for file in folder.iterdir() if file.is_file()]


def scan_folder(folder_path):
    return list_files(folder_path)


def view_all_files(folder_path):
    files = list_files(folder_path)
    for file in files:
        print(file)
    return files


def file_type_statistics(folder_path):
    files = list_files(folder_path)
    counts = Counter(file.suffix.lower() or "(无扩展名)" for file in files)
    for ext, count in sorted(counts.items()):
        print(f"{ext}: {count}")
    return counts


def search_file(folder_path, keyword):
    keyword = keyword.lower()
    matches = [
        file for file in list_files(folder_path)
        if keyword in file.name.lower()
    ]
    if not matches:
        print("未找到匹配文件")
    else:
        for file in matches:
            print(file)
    return matches


def quit_app():
    print("退出")


def ask_folder_path():
    """让用户输入有效的文件夹路径。"""
    while True:
        raw = input("请输入文件夹路径（例如 J:/）：").strip().strip('"')
        if not raw:
            print("路径不能为空，请重新输入")
            continue
        # Windows 下 "J:" 表示当前目录，需转成盘符根目录 "J:/"
        if len(raw) == 2 and raw[1] == ":":
            raw = raw + "/"
        folder = Path(raw)
        if not folder.exists():
            print(f"路径不存在: {raw}，请重新输入")
            continue
        if not folder.is_dir():
            print(f"不是文件夹: {raw}，请重新输入")
            continue
        return str(folder)


ROOT = ask_folder_path()
print(f"当前目录: {ROOT}")

while True:
    print("""
1. 扫描文件夹
2. 查看所有文件
3. 文件类型统计
4. 搜索文件
5. 退出
""")
    choice = input("请输入选项(1-5)：").strip()

    if choice == "1":
        print("扫描文件夹")
        for file in scan_folder(ROOT):
            print(file)
    elif choice == "2":
        print("查看所有文件")
        view_all_files(ROOT)
    elif choice == "3":
        print("文件类型统计")
        file_type_statistics(ROOT)
    elif choice == "4":
        print("搜索文件")
        search_file(ROOT, input("请输入关键字："))
    elif choice == "5":
        quit_app()
        break
    else:
        print("无效选项，请输入 1-5")