import telebot
from config import TOKEN, DATABASE
from logic import create_graph, load_cities
import os

bot = telebot.TeleBot(TOKEN)
all_cities = load_cities()

class DB_Map:
    def __init__(self, db_path):
        self.db_path = db_path

    def add_city(self, user_id, city_name):
        return city_name in [city['name'].lower() for city in all_cities]

    def select_cities(self, user_id):
        return ["London", "Paris"]

manager = DB_Map(DATABASE)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может показывать города на карте. Напиши /help для списка команд.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды:\n"
                                      "/show_city <город> <цвет> - Показать город на карте с маркером выбранного цвета\n"
                                      "/remember_city <город> - Запомнить город\n"
                                      "/show_my_cities <цвет> - Показать мои города на карте с маркерами выбранного цвета")

@bot.message_handler(commands=['show_city'])
def handle_show_city(message):
    parts = message.text.split()
    city_name = ' '.join(parts[1:-1])
    marker_color = parts[-1] if parts[-1] in folium.Icon.color_options else 'blue'
    user_id = message.chat.id
    file_path = f'{user_id}_city.png'
    create_graph(file_path, [city_name], marker_color=marker_color)
    with open(file_path, 'rb') as map_file:
        bot.send_photo(user_id, map_file)
    os.remove(file_path)

@bot.message_handler(commands=['remember_city'])
def handle_remember_city(message):
    user_id = message.chat.id
    city_name = ' '.join(message.text.split()[1:])
    if manager.add_city(user_id, city_name):
        bot.send_message(message.chat.id, f'Город {city_name} успешно сохранен!')
    else:
        bot.send_message(message.chat.id, 'Такого города я не знаю. Убедись, что он написан на английском!')

@bot.message_handler(commands=['show_my_cities'])
def handle_show_visited_cities(message):
    user_id = message.chat.id
    parts = message.text.split()
    marker_color = parts[-1] if parts[-1] in folium.Icon.color_options else 'blue'
    cities = manager.select_cities(user_id)
    if cities:
        file_path = f'{user_id}_my_cities.png'
        create_graph(file_path, cities, marker_color=marker_color)
        with open(file_path, 'rb') as map_file:
            bot.send_photo(user_id, map_file)
        os.remove(file_path)
    else:
        bot.send_message(message.chat.id, 'У вас еще нет сохраненных городов.')

if __name__ == "__main__":
    bot.polling()
