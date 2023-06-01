import kivy.utils as utils
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, NumericProperty

import threading
from secrets import choice
from time import sleep
from random import randint, choice


class MainWidget(RelativeLayout):
    choices = {
        "rock": "assets/images/rock.png",
        "scissors": "assets/images/scissors.png",
        "paper": "assets/images/paper.png",
    }

    ai_choice = ""
    user_choice = ""

    user_choice_img = ObjectProperty(None)
    ai_choice_img = ObjectProperty(None)

    scoreboard_text = ""
    scoreboard = ObjectProperty(None)

    ai_score = NumericProperty(0)
    user_score = NumericProperty(0)

    user_winstreak = NumericProperty(0)
    ai_winstreak = NumericProperty(0)

    user_on_winstreak = False
    ai_on_winstreak = False

    main_thread = None
    thread_ai_animation = None
    thread_check_win = None
    thread_update_result = None
    thread_reset_game = None

    game_is_started = False

    main_color = "#84A98C"
    second_color = "#2F3E46"
    third_color = "#CAD2C5"

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_press_button(self, user_choice: str):
        """
        Handles button press event.

        :param user_choice: The user's choice.
        """
        self.user_choice = user_choice
        self.main_thread = threading.Thread(target=self.main)
        self.check_if_game_is_started()

    def main(self):
        """
        Main game logic.
        """
        self.change_user_choice_img()
        self.ai_turn()
        self.check_win()
        self.update_result_to_gui()
        self.reset_game()

    def set_button_color(self, button):
        """
        Sets the button color.

        :param button: The button widget.
        """
        button_bg = button.canvas.before.get_group("color")[0]

        # Change button background
        button_bg.rgb = utils.get_color_from_hex(self.main_color)

    def reset_button_color(self, button):
        """
        Resets the button color.

        :param button: The button widget.
        """
        button_bg = button.canvas.before.get_group("color")[0]

        # Change button background
        button_bg.rgb = utils.get_color_from_hex(self.second_color)

    def reset_button_color(self, button):
        """
        Resets the button color.

        :param button: The button widget.
        """
        button_bg = button.canvas.before.get_group("color")[0]

        # Change button background
        button_bg.rgb = utils.get_color_from_hex(self.second_color)

    def ai_turn(self, *args):
        """
        Simulates the AI's turn.
        """
        self.ai_choice = choice(list(self.choices.keys()))

        ai_choice_img = self.choices[self.ai_choice]
        duration_anim = randint(3, 6)

        def animations():
            """
            Perform AI animation.
            """
            for _ in range(0, duration_anim):
                for i in self.choices:
                    image = self.choices[i]
                    self.ai_choice_img.source = image
                    sleep(0.1)
            self.ai_choice_img.source = ai_choice_img

        self.thread_ai_animation = threading.Thread(target=animations)
        self.thread_ai_animation.start()

    def check_win(self):
        """
        Checks the result of the game.
        """
        ai_choice = self.ai_choice
        user_choice = self.user_choice

        def start():
            """
            Start checking the result.
            """
            # Wait for animation to end
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
        """
        Changes the image of the user's choice.
        """
        self.user_choice_img.source = self.choices[self.user_choice]

    def update_result_to_gui(self):
        """
        Updates the game result to the GUI.
        """

        def start():
            """
            Start updating the result to the GUI.
            """
            self.thread_check_win.join()

            scoreboard = self.scoreboard
            scoreboard_text = self.scoreboard_text

            # Update scoreboard
            scoreboard.text = self.scoreboard_text

            # Update User and AI score
            if scoreboard_text == "WIN":
                self.user_score += 1
                self.user_on_winstreak = True
                self.ai_on_winstreak = False
                self.check_winstreak()

            elif scoreboard_text == "LOSE":
                self.ai_score += 1
                self.user_on_winstreak = False
                self.ai_on_winstreak = True
                self.check_winstreak()

            else:
                pass

        self.thread_update_result = threading.Thread(target=start)
        self.thread_update_result.start()

    def check_if_game_is_started(self):
        """
        Checks if the game is already started.
        """
        if self.game_is_started:
            pass
        else:
            self.main_thread.start()
            self.game_is_started = True

    def check_winstreak(self):
        """
        Checks if there is a win streak for either the user or the AI.
        """
        if self.user_on_winstreak:
            self.user_winstreak += 1
            self.ai_winstreak = 0
        elif self.ai_on_winstreak:
            self.ai_winstreak += 1
            self.user_winstreak = 0

    def reset_game(self):
        """
        Resets the game state.
        """

        def start():
            """
            Start resetting the game state.
            """
            self.thread_update_result.join()
            self.game_is_started = False

        self.thread_reset_game = threading.Thread(target=start)
        self.thread_reset_game.start()
