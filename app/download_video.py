import re
from yt_dlp import YoutubeDL
import asyncio
async def download_video(url, quality, output_path='.'):
    """
    Скачивает видео с YouTube по ссылке и указанному качеству с использованием yt-dlp.

    :param url: Ссылка на видео YouTube.
    :param quality: Желаемое качество видео (например, '720p', '1080p').
    :param output_path: Путь для сохранения видео (по умолчанию текущая папка).
    :return: Путь к скачанному файлу.
    """
    try:
        # Настройки для скачивания
        ydl_opts = {
            'format': f'bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]',  # Фильтр по качеству
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Путь для сохранения
        }

        # Скачиваем видео
        print(f"Скачивание видео...")
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)

        print(f"Видео успешно скачано: {file_path}")
        return file_path

    except Exception as e:
        print(f"Ошибка при скачивании видео: {e}")
        return None

# # Пример использования
# video_url = 'https://youtu.be/LtgsjK2VnJg?si=N3t8D7KkuIYOw0CH'
# quality = '480p'  # Укажите желаемое качество (без 'p')
# download_video(video_url, quality, output_path='./videos')

async def check_links(text):
    # Регулярные выражения для поиска ссылок
    instagram_pattern = r'https?://(www\.)?instagram\.com/\S+'
    youtube_pattern = r'https?://(www\.)?youtube\.com/\S+'
    youtube_short_pattern = r'https?://youtu\.be/\S+'  # Новое регулярное выражение для коротких ссылок YouTube
    vk_pattern = r'https?://(www\.)?vk\.com/\S+'
    video_pattern = r'https?://\S+\.(mp4|avi|mov|mkv)'
    rutube_pattern = r'https?://(www\.)?rutube\.ru/\S+'

    # Проверка на наличие ссылок
    if re.search(instagram_pattern, text):
        return "instagram"
    if re.search(youtube_pattern, text) or re.search(youtube_short_pattern,
                                                     text):
        return "youtube"
    if re.search(vk_pattern, text):
        return "vk"
    if re.search(video_pattern, text):
        return "video"
    if re.search(rutube_pattern, text):
        return "rutube"
    else:
        return None
