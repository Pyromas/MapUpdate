# Telegram Bot для Отображения Городов на Карте

Этот проект представляет собой Telegram-бота, который может отображать города на карте с заливкой континентов и океанов. Пользователь может указать цвет маркеров для отображения городов.

## Требования

- Python 3.6+
- Библиотеки:
  - `matplotlib`
  - `mpl_toolkits.basemap`
  - `python-telegram-bot`
  - `Pillow`

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
    cd ваш-репозиторий
    ```

2. Установите необходимые библиотеки:

    ```bash
    pip install matplotlib basemap python-telegram-bot Pillow
    ```

## Конфигурация

1. Создайте бота в Telegram и получите токен. Следуйте инструкциям в [официальном руководстве](https://core.telegram.org/bots#6-botfather).

2. Вставьте токен вашего бота в файл `bot.py`, заменив строку `"YOUR_TOKEN"` на ваш токен:

    ```python
    updater = Updater("YOUR_TOKEN", use_context=True)
    ```

## Запуск

Запустите бота:

```bash
python bot.py
```
Использование

После запуска бота введите следующие команды в чате с ботом:

/start - Приветственное сообщение.
/draw_all_cities [color] - Отображение всех городов на карте. Опционально укажите цвет маркеров.
Пример: /draw_all_cities red
/draw_city <city_name> [color] - Отображение указанного города на карте. Опционально укажите цвет маркеров.
Пример: /draw_city Moscow blue
Пример
Пример карты с городами:


Описание кода
logic.py
Файл logic.py содержит функции для создания карты и нанесения городов:

create_map(cities, marker_color='skyblue'): Создает карту с городами и заливает континенты и океаны.
draw_map(fig, ax): Отображает созданную карту.
bot.py
Файл bot.py содержит реализацию Telegram-бота и обработку команд:

start(update: Update, context: CallbackContext): Приветственное сообщение.
draw_all_cities(update: Update, context: CallbackContext): Отображает все города на карте.
draw_city(update: Update, context: CallbackContext): Отображает указанный город на карте.
main(): Запускает бота.
