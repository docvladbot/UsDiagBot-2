# UsDiagBot
Telegram-бот для анализа изображений и видео УЗИ.

## Возможности
- Поддержка изображений и видео (1 кадр в секунду)
- Модели FetalNet и FetalCLIP (заглушки)
- Автоматический ответ пользователю

## Установка
1. Загрузите проект на GitHub
2. Разверните на Render (Python Background Worker)
3. Добавьте переменную окружения `TOKEN` — ваш Telegram Bot Token

## Запуск
```
python bot.py
```

## Пример
Пользователь отправляет УЗИ, бот отвечает с диагнозом.
