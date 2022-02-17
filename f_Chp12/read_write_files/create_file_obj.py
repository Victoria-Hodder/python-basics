from pathlib import Path

path = Path.home() / "Documents" / "hello.txt"
path.touch()
file = path.open(mode='r', encoding='utf-8')
file.close()

file_path = "/home/i554209/Documents/hello.txt"
file = open(file_path, mode = 'r', encoding = 'utf-8')
print(file)
file.close()
