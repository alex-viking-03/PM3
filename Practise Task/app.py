from ui.main_window import MainWindow
from database.database import create_tables

class App:
    def __init__(self):
        create_tables() #Создаем таблицы
        self.window = MainWindow() #Создаем собственное окно window (экземпляр класса MainWindow)

    def run(self):
        self.window.mainloop() #Зацикливаем его и заставляем слушать события