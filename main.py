from multiprocessing import current_process
from secrets import choice
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
import kivy.utils as utils
from time import sleep
import threading
from random import randint


class MainWidget(RelativeLayout):
    user_choices = {
        "rock": "lib/rock.png",
        "scissors": "lib/scissors.png",
        "paper": "lib/paper.png",
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.init_variables, 0)

    def init_variables(self, *args):
        self.user_choice = self.ids.user_choice
        self.ai_choice_image = self.ids.ai_choice_image

    def on_press_rock_button(self):
        choice = self.user_choices["rock"]
        self.user_choice.source = choice
        self.ai_choice()
        self.check_win(self.ai_choice_text, choice)

    def on_press_scissors_button(self):
        choice = self.user_choices["scissors"]
        self.user_choice.source = choice
        self.ai_choice()
        self.check_win(self.ai_choice_text, choice)

    def on_press_paper_button(self):
        choice = self.user_choices["paper"]
        self.user_choice.source = choice
        self.ai_choice()
        self.check_win(self.ai_choice_text, choice)

    def set_button_color(self, button):
        selected_button = button.canvas.before.get_group("color")[0]
        selected_button.rgb = utils.get_color_from_hex("#84a98c")

    def reset_button_color(self, button):
        selected_button = button.canvas.before.get_group("color")[0]
        selected_button.rgb = utils.get_color_from_hex("#2f3e46")

    def ai_choice(self, *args):
        random_choice = randint(0, 2)
        random_sleep = randint(5, 10)

        val = list(self.user_choices.values())
        self.ai_choice_text = val[random_choice]

        def animate():
            for _ in range(0, random_sleep):
                for i in self.user_choices.values():
                    self.ai_choice_image.source = i
                    sleep(0.1)
            self.ai_choice_image.source = self.ai_choice_text

        threading.Thread(target=animate).start()
        return self.ai_choice_text

    def check_win(self, ai_choice, user_choice):
        rock = self.user_choices["rock"]
        scissors = self.user_choices["scissors"]
        paper = self.user_choices["paper"]
        if ai_choice == rock:
            if user_choice == paper:
                print("WIN")
            elif user_choice == rock:
                print("TIE")
            else:
                print("LOSE")

        if ai_choice == scissors:
            if user_choice == rock:
                print("WIN")
            elif user_choice == scissors:
                print("TIE")
            else:
                print("LOSE")

        if ai_choice == paper:
            if user_choice == scissors:
                print("WIN")
            elif user_choice == paper:
                print("TIE")
            else:
                print("LOSE")


class RockPaperScissorsApp(App):
    def build(self):
        return MainWidget()


RockPaperScissorsApp().run()
