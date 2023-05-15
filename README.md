# Multi-tool-convertor
Проект розробляється для тренування програмування та роботи з різними бібліотеками.
Збірник написаних функцій які виконані у форматі API щоб їх можно було підключити до будь якого проекту. Написаний для тренування у програмуванні мови Python. На разі включає у себе:
- Бот для телеграму з інтерфейсом для користувача ~~з підключенням до API~~ 
- Конвертор аудіо файлів
- Конвертор зображень
- Конвертор відео файлів


# Встановлення
Для встановлення проекту потрібно виконати наступний код:
```bash
pip install -r requirements.txt
```

# Використання
Для того що б запустити проект потрібно прописати:
```bash
python -m uvicorn app.main:app --log_level="info" --reload
```
Також для запуску бота потрібно прописати у консолі:
```bash
python start_bot.py
```
Або запустити файл `run.py`
```bash
python run.py
```

У браузері можно перейти по шляху *localhost:8000/docs* для того щоб відкрити документацію API у якій описані реалізовані API
- З реалізацією телеграм бота допомогла бібліотека [aiogram](https://aiogram.dev)
- Для конвертування музикик було використано бібліотеку [pydub](http://pydub.com)
- Для конвертування зображень було використано бібліотеку [Pillow](https://pillow.readthedocs.io/en/stable/)
- Для конвертування відео файлів було використано бібліотеку [MoviePy](https://zulko.github.io/moviepy/)

# Автори
Github: [@nananaseek](https://github.com/nananaseek)

Telegram: @ehita

# TODO 
- ~~Створити бота для телеграма~~ та підключити його до API
- Конвертування документів
- Конвертування мов програмування
- Конвертування архівів
- Конвертування аудіо книг
- Функція Text to Speech і навпаки
- Функція вирізки звука з відео
- Функція скачування відео з youtube.com
- Функція скачування з тіктоку без вотер марки