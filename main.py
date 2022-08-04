from concurrent.futures import thread
from secrets import choice
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
import kivy.utils as utils
from time import sleep
import threading
from random import randint, choice

from matplotlib import use


class MainWidget(RelativeLayout):
    choices = {
        "rock": "lib/rock.png",
        "scissors": "lib/scissors.png",
        "paper": "lib/paper.png",
    }

    ai_choice = None
    user_choice = None

    user_choice_img = None
    ai_choice_img = None

    scoreboard_text = None
    scoreboard = None

    ai_score = 0
    user_score = 0

    main_thread = threading.Thread
    thread_ai_animation = None
    thread_check_win = None

    main_color = "#84A98C"
    second_color = "#2F3E46"
    third_color = "#CAD2C5"

    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.init_variables, 0)

    def init_variables(self, *args):
        self.user_choice_img = self.ids.user_choice_img
        self.ai_choice_img = self.ids.ai_choice_img
        self.scoreboard = self.ids.scoreboard

    def on_press_rock_button(self):
        self.user_choice = "rock"
        self.main_thread(target=self.main).start()

    def on_press_scissors_button(self):
        self.user_choice = "scissors"
        self.main_thread(target=self.main).start()

    def on_press_paper_button(self):
        self.user_choice = "paper"
        self.main_thread(target=self.main).start()

    def main(self):
        self.change_user_choice_img()
        self.ai_turn()
        self.check_win()

    def set_button_color(self, button):
        button_bg = button.canvas.before.get_group("color")[0]

        # Change button background
        button_bg.rgb = utils.get_color_from_hex(self.main_color)

    def reset_button_color(self, button):
        button_bg = button.canvas.before.get_group("color")[0]

        # Change button background
        button_bg.rgb = utils.get_color_from_hex(self.second_color)

    def ai_turn(self, *args):
        self.ai_choice = choice(list(self.choices.keys()))

        ai_choice_img = self.choices[self.ai_choice]
        duration_anim = randint(5, 10)

        def animations():
            for _ in range(0, duration_anim):
                for i in self.choices:
                    image = self.choices[i]
                    self.ai_choice_img.source = image
                    sleep(0.1)
            self.ai_choice_img.source = ai_choice_img

        self.thread_ai_animation = threading.Thread(target=animations)
        self.thread_ai_animation.start()

    def check_win(self):
        ai_choice = self.ai_choice
        user_choice = self.user_choice

        def start():
            self.thread_ai_animation.join()

            if user_choice == "rock":
                if ai_choice == "scissors":
                    self.scoreboard_text = "WIN"
                elif ai_choice == "rock":
                    self.scoreboard_text = "TIE"
                else:
                    self.scoreboard_text = "LOSE"

            elif user_choice == "scissors":
                if ai_choice == "paper":
                    self.scoreboard_text = "WIN"
                elif ai_choice == "scissors":
                    self.scoreboard_text = "TIE"
                else:
                    self.scoreboard_text = "LOSE"

            else:
                if ai_choice == "rock":
                    self.scoreboard_text = "WIN"
                elif ai_choice == "paper":
                    self.scoreboard_text = "TIE"
                else:
                    self.scoreboard_text = "LOSE"

        self.thread_check_win = threading.Thread(target=start)
        self.thread_check_win.start()

    def change_user_choice_img(self):
        self.user_choice_img.source = self.choices[self.user_choice]

    def update_result_to_gui(self):
        scoreboard = self.scoreboard

        scoreboard.text = self.scoreboard_text


class RockPaperScissorsApp(App):
    def build(self):
        return MainWidget()


RockPaperScissorsApp().run()
