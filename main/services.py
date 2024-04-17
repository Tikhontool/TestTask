import csv
import pandas as pd



def collect_categories(csv_file):
    category_columns = [f'category{i}' for i in range(1, 11)]
    categories = set()

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for column in category_columns:
                if column in row:
                    category = row[column].strip()
                    if category:
                        categories.add(category)

    return list(categories)


def get_image_url(csv_file, categories):
    image_urls_list = {}
    image_url = ""

    if len(categories) == 0:
        categories = collect_categories("data.csv")

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            for i in range(1, 11):
                category = row[f'category{i}']
                if category and category in categories:
                    if category not in image_urls_list:
                        image_urls_list[category] = {}
                    image_urls_list[category].update({row['Image_URL']: row['needed_amount_of_shows']})

        max_len = 0
        max_count_show = 0
        for i in image_urls_list.items():
            if len(i[1]) >= max_len:
                max_len = len(i[1])
                check_count = int(max(i[1].values(), key=lambda x: int(x)))
                if check_count > int(max_count_show):
                    image_url, max_count_show = max(i[1].items(), key=lambda k: int(k[1]))




    update_csv_shows("data.csv", image_url)

    return image_url


def update_csv_shows(csv_file, image_url):
    df = pd.read_csv(csv_file)

    if 'Image_URL' in df.columns and 'needed_amount_of_shows' in df.columns:
        mask = df['Image_URL'] == image_url
        if mask.any():
            df.loc[mask, 'needed_amount_of_shows'] -= 1
            df.to_csv(csv_file, index=False)
        else:
            print(f"URL-адрес {image_url} не найден в CSV-файле.")
    else:
        print("В CSV-файле отсутствуют необходимые столбцы.")
