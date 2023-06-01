from app import RockPaperScissorsApp
from kivy.config import Config

if __name__ == "__main__":
    Config.set("kivy", "window_icon", "icons/icon.ico")
    RockPaperScissorsApp().run()
