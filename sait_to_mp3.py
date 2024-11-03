from bs4 import BeautifulSoup
import requests
import os

# URL категории подкастов
url = 'https://castbox.fm/categories/10058?country=ru'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

# Находим все блоки с подкастами
divs = soup.find_all("div", class_="topCover")

# Создаем директорию для скачанных файлов, если ее нет
download_dir = 'downloads'
os.makedirs(download_dir, exist_ok=True)

# Счетчик для названий файлов
file_counter = 1

for div in divs:
    # Ищем все вложенные ссылки на эпизоды
    links = div.find_all('a', href=True)
    
    for link in links:
        # Формируем полный URL
        full_url = "https://castbox.fm" + link['href']
        episode_response = requests.get(full_url)
        episode_html = episode_response.content
        
        # Используем BeautifulSoup для парсинга HTML
        episode_soup = BeautifulSoup(episode_html, 'html.parser')
        
        # Находим все ссылки на эпизоды
        for a in episode_soup.find_all("a", class_="ctrlItem play", href=True):
            episode_url = "https://castbox.fm" + a["href"]
            print(f"Скачивание эпизода: {episode_url}")

            # Запрашиваем HTML-код страницы эпизода
            episode_response = requests.get(episode_url)
            episode_html = episode_response.content
            episode_detail_soup = BeautifulSoup(episode_html, 'html.parser')

            # Ищем ссылку для .mp3
            audio_source = episode_detail_soup.find("source", src=True)
            if audio_source:
                src = audio_source["src"]
                print(f"Ссылка на аудиофайл: {src}")

                # Формируем имя файла с учетом счетчика
                file_name = f"audio{file_counter}.mp3"
                file_path = os.path.join(download_dir, file_name)

                # Скачиваем файл
                audio_response = requests.get(src)
                with open(file_path, 'wb') as f:
                    f.write(audio_response.content)
                    print(f"Файл сохранен: {file_path}")
                    file_counter += 1  # Увеличиваем счетчик для следующего файла
            else:
                print("Ссылка на аудиофайл не найдена.")
