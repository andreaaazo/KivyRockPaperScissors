from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout


class MainWidget(RelativeLayout):
    pass


class RockPaperScissorsApp(App):
    def build(self):
        return MainWidget()


RockPaperScissorsApp().run()
