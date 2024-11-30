
Интеллектуальный помощник для создания учебных материалов


Установка на Windows:
1. Создание виртуальное окружение:
    ```
    python -m venv .venv
    ```
2. Активировать виртаульное окружение:
    ```
    .\.venv\Scripts\activate  
    ```
3. Если после этой команды ".\.venv\Scripts\activate " у вас появилась папка (.venv) то:
4. Скачать нужную вам библиотеку(помните некоторые библиотеки не работают без опр. файлой) библиотеку:
    ```
    pip install *название вашей библиотеки*
    ```
5. Выключить виртуальное окружение:
    ```
    deactivate
    ```
Файлы нужны для работы с кодом:
1. "ffmpeg" ссылка на скачивание "https://www.videohelp.com/software/ffmpeg", если у вас не работает код и пишет
"файл не найден" введите следующие в cmd
```
pip install ffmpeg или pip install python-ffmpeg
если все равно не работает идем другим способом, pip install ffmpeg-downloader
ffdl install --add--path
```
По коду:
Ссылки на таблицы для файла "обучение_ии_py.py"
1. data = pd.read_csv("/content/32 подкаста без стоп слов - Лист1.csv")  ссылка: https://docs.google.com/spreadsheets/d/1dwsGmCylcmW0sAarrmvlFyIYSe5Gk-B_6ksULVHIYHw/edit?gid=0#gid=0
2. таблица без стоп листов и слова в начальной форме - lemmas_output.csv (1).csv) ссылка: https://docs.google.com/spreadsheets/d/1ylhaht8s3b7dXjb77vuL4oTkd6fVE-pqgh-E_rkTlMI/edit?gid=1030516438#gid=1030516438
3. with open('1 - 1.csv.csv', 'r', encoding='utf-8') as file: ссылка: https://docs.google.com/spreadsheets/d/1NzyXlaAfuW4G80f1R610hWyGV8vz4O8nq2tileEFh-Q/edit?gid=225818973#gid=225818973

Теперь пройдусь по программам, они разделены для меньшей нагрузки. 
1. Программа для скачивания mp3 файлов с сайта "https://castbox.fm/categories/10058?country=ru" находить в файле под названием "sait_to_mp3.py", проявите терпение во время работы программы.
2. Программа для конвертации из mp3 в maw находить в файле под названием "mp3_to_maw.py", проявите терпение во время работы программы.
3.  Программа для конвертации из maw в txt находить в файле под названием "maw_to_txt.py", проявите терпение во время работы программы(один файл из maw в txt конвертируетьтся около 10 минут)
4. Для работы с таблицый в питоне я конвертировал файла из xslx в csv программа находить в файле под названием "xslx_to_csv.py"
5. Дальше идет обучение ии программа лежит в файле "обучение_ии_py.py" там и токенизация и приведение слов в начальный вид








