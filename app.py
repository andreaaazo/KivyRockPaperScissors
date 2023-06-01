from kivy.app import App
from screen import MainWidget


class RockPaperScissorsApp(App):
    def build(self):
        return MainWidget()
