# Multi-tool-convertor
Збірник написаних функцій які викликані у форматі API щоб їх можно було підключити до будь якого проекту. Написаний для тренування у програмуванні мови Python. На разі включає у себе:
- Конвертор аудіо файлів


# Встановлення
Для встановлення проекту потрібно виконати наступний код:
```bash
pip install -r requirements.txt
```

# Використання
Для того що б запустити проект потрібно прописати:
```bash
python -m uvicorn app.main:app
```

У браузері можно перейти по шляху *localhost:8000/docs* для того щоб відкрити документацію API у якій описані реалізовані API  
- Для конвертування музикик було використано бібліотеку [pydub](http://pydub.com)

# Автори
Github: @nananaseek

# TODO 
- Створити бота для телеграма та підключити його до API
- Конвертування відео файлів
- Конвертування картинок
- Конвертування документів
- Конвертування мов програмування
- Конвертування архівів
- Конвертування аудіо книг
- Функція Text to Speech
- Функція вирізки звука з відео