import os

# Корневая папка (путь к SFTP или локальному каталогу)
root = r"C:\Users\user\Desktop"

# Основные сущности (каждая — список подпапок)
base_entities = [
    ["Поставщики данных", "Сети"],
    ["Поставщики данных", "Дистрибьюторы"]
]

# Конфигурация
years = [2023, 2024, 2025]
months = [f"{i:02d}" for i in range(1, 13)]
clients = [f"Client_{i:02d}" for i in range(1, 41)]
purchase_types = ["Type1", "Type2", "Type3", "Type4", "Type5"]

# Режим работы: True = создать папки, False = только вывести список
create_folders = True

# Список всех путей
all_paths = []

for entity_parts in base_entities:
    for year in years:
        for month in months:
            for client in clients:
                for p_type in purchase_types:
                    path = os.path.join(root, *entity_parts, str(year), month, client, p_type)
                    all_paths.append(path)
                    if create_folders:
                        os.makedirs(path, exist_ok=True)

# Вывод примера в консоль (первые 20 путей)
for p in all_paths[:20]:
    print(p)

# Записываем весь список в файл
output_file = os.path.join(root, "folders_list.txt")
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(all_paths))

print(f"\nВсего путей: {len(all_paths)}")
print(f"Список сохранён в файл: {output_file}")
