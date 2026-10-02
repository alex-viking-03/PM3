from App import App
from database import create_tables
import customtkinter as ctk

def main():
    create_tables()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()