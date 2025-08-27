import os
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=os.environ.get("ROOT_DIR", "/data"),
                   help="Корневая папка (можно переменной окружения ROOT_DIR)")
    p.add_argument("--create", action="store_true",
                   help="Создавать папки (если не указан, только печать путей)")
    args = p.parse_args()

    base_entities = [
        ["Поставщики данных", "Сети"],
        ["Поставщики данных", "Дистрибьюторы"]
    ]
    years = [2023, 2024, 2025]
    months = [f"{i:02d}" for i in range(1, 13)]
    clients = [f"Client_{i:02d}" for i in range(1, 41)]
    purchase_types = ["Type1", "Type2", "Type3", "Type4", "Type5"]

    all_paths = []
    for entity_parts in base_entities:
        for year in years:
            for month in months:
                for client in clients:
                    for p_type in purchase_types:
                        path = os.path.join(args.root, *entity_parts, str(year), month, client, p_type)
                        all_paths.append(path)
                        if args.create:
                            os.makedirs(path, exist_ok=True)

    for pth in all_paths[:20]:
        print(pth)

    output_file = os.path.join(args.root, "folders_list.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(all_paths))

    print(f"\nВсего путей: {len(all_paths)}")
    print(f"Список сохранён в файл: {output_file}")

if __name__ == "__main__":
    main()
