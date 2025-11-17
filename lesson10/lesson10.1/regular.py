import re

file_path = r"C:\Users\TEMP.IUCA.065\Desktop\lesson10\lesson10.1\mockdata.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Имена
names = re.findall(r'^(\w+)', text, flags=re.MULTILINE)

# Фамилии
surnames = re.findall(r'^\w+\s+(\w+)', text, flags=re.MULTILINE)

# Типы файлов — расширения после точки
types = re.findall(r'\.(\w+)\b', text)

print("Имена:")
for n in names:
    print(n)

print("\nФамилии:")
for s in surnames:
    print(s)

print("\nТипы файлов:")
for t in types:
    print(t)
