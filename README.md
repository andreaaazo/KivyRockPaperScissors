<div align="center">

  <h1> KivyRockPaperScissors </h1>

  <br />

  <p>A simple rock/paper/scissors game, with a lot of built-in features!</p>

  <p>Challenge yourself, and try to beat our bot!</p>

</div>

<br />

<br />

## 📒 Index

- [Features](https://github.com/andreaaazo/KivyRockPaperScissors#%EF%B8%8F-features)
- [How-We-Made-It](https://github.com/andreaaazo/KivyRockPaperScissors#-how-we-made-it)
- [To-do](https://github.com/andreaaazo/KivyRockPaperScissors#-to-do)
- [Frameworks](https://github.com/andreaaazo/KivyRockPaperScissors#-frameworks)

<br />

<br />

## ⚡️ Features

- Challenge yourself with the AI bot
- Check your winstreak and your score
- Full dynamic game, with some animations

<br />

<br />

## 💡 How-We-Made-It

### Introduction

To create our GUI we used the `Kivy` framework.

```python
import kivy.utils as utils
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, NumericProperty
```

With the `Kivy` framework we have created the app. The full game stays in the `MainWidget` class.

```python
class RockPaperScissorsApp(App):
    def build(self):
        return MainWidget()
```

<br />

### Realizing the GUI

Before start coding the GUI, we used Figma to create a prototype and setting up the aspect of our game.
We also draw the widget layouts to help us code faster, and to undestand better which layout to use.

![alt text](https://github.com/andreaaazo/KivyRockPaperScissors/blob/main/unusued/gui.png)

The interface is fully coded in the `rockpaperscissors.kv` file.  
Check it out [here](https://github.com/andreaaazo/KivyRockPaperScissors/blob/main/rockpaperscissors.kv).

### Passing objects from `.kv` to `.py`

To pass the needed objects, firstly, we have declared some variables at the beginning of the widget definition in the `.kv` file:

```
<MainWidget>:

    ai_choice_img: ai_choice_img
    user_choice_img: user_choice_img
    scoreboard: scoreboard
```

Secondarly, we have assigned an `id` to the desired objects, with the same name of the variable:

```
Image:
  id: user_choice_img
  ...
```

In the `main.py` file we have declared the same variables, with the value `ObjectProperty(None)`:

```python
user_choice_img = ObjectProperty(None)
```

### Passing variables from `.py` to `.kv`

To update the text labels dynamically, we have declared some variables in the `.py` file. With the value `NumericProperty(0)` for an integer, and `StringProperty("")` for a string:

```python
ai_score = NumericProperty(0)
```

To pass the variables in the `.ky` file, we simply wrote `root.` before the declaration:

```
Label:
    text: str(root.ai_score)
```

### Writing the game mechanics

We wrote the mechanics in the `MainWidget()` class in the `.py` file.

We implemented `Threading` to help us to manage better the timing, and it gave us the ability to create some funny animations.

Every `Button` action, raises the `main` function and starts a new `Thread`:

```python
def main(self):
    self.change_user_choice_img()
    self.ai_turn()
    self.check_win()
    self.update_result_to_gui()
    self.reset_game()
```

To help us to manage the Bot animation we used the function `.join()`:

```python
def check_win(self):
        ai_choice = self.ai_choice
        user_choice = self.user_choice

        def start():
            # Wait for animation to end
            self.thread_ai_animation.join()
```

The game mechanic is fully coded in the `main.py` file.  
Check it out [here](https://github.com/andreaaazo/KivyRockPaperScissors/blob/main/main.py).

<br />

<br />

## 👀 To-do

- [x] Finish basic game
- [x] Publish first release
- [ ] Add AI latest moves history

<br />

<br />

## 🧬 Frameworks

[Kivy](https://kivy.org/doc/stable/)

[Threading](https://docs.python.org/3/library/threading.html)

[Random](https://docs.python.org/3/library/random.html)

[Secrets](https://docs.python.org/3/library/secrets.html)

[Time](https://docs.python.org/3/library/time.html)
