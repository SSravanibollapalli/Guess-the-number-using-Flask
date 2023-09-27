from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)

@app.route('/')
def display():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="img">'\


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_num:
        return '<h1 style = "color:red">Too Low, Try Again!</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="img">'
    elif guess > random_num:
        return '<h1 style = "color:purple">Too High, Try Again!</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="img">'
    else:
        return '<h1 style = "color:green">You found me!</h1>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="img">'


if __name__ == '__main__':
    app.run()
