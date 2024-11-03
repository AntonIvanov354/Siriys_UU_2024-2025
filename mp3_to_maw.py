import speech_recognition as sr
from pydub import AudioSegment
import os

# Укажите путь к вашей папке с файлами
path = "G:\\picec\\"
file_base_name = "СФ идёт под жёсткий фонк в хорошем качестве"

# Конвертируем файлы с 1 до N (укажите нужное количество файлов для конвертации)
number_of_files = 10  # Задайте нужное количество файлов
for i in range(1, number_of_files + 1):
    input_file = os.path.join(path, f"{file_base_name}{i}.mp3")
    output_file = os.path.join(path, f"udi1o{i}.wav")  # Сохраним как .wav

    # Проверяем, существует ли файл
    if os.path.exists(input_file):
        # Загрузка звукового файла в формате MP3
        audio_mp3 = AudioSegment.from_file(input_file, format="mp3", ffmpeg="G:\\picec\\ffmpeg")
        
        # Конвертация в формат WAV
        audio_mp3.export(output_file, format="wav")
        print(f"Конвертация {input_file} в {output_file} завершена.")
    else:
        print(f"Файл {input_file} не найден.")