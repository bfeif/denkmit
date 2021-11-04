# Denkmit
A SRS-flashcard app, specialized for German-language-learning. Uses Django as ORM, Postgres as DB, Poetry for environment management.


## About
The best way to learn a language is to have real conversations in your target language as much as possible! Seems easy enough. However, any language learning process is greatly boosted by book-studying, including a little bit of (yes, I know) memorization. In particular, learning the German language requires an unusually high amount of memorization: adjective declensions, preposition declensions, patternless noun genders, and more.

The point of Denkmit is to enable you to do this necessary memorization as efficiently as possible, by using the well-researched memorization tool of Spaced Repetition Software (SRS).Denkmit gives you exercises in preposition declension, noun gender-guessing, and standard vocabulary learning.

With 5 minutes a day of practicing preposition declensions with Denkmit, you can have all the preposition declensions internalized in under a month.


## Setup
So, you want to Denkmit? At the moment, Denkmit only supports a terminal UI for learning German flashcards. Let's get the project set up:
1. This project uses poetry for environment management, so install that first (instructions [here](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)). If you're on mac/linux, it should be as simple as running `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`.
2. Clone this repository, and `cd` into it (running `ls` should show `your/path/to/denkmit`).
3. Add poetry to your path in whatever shell source file you use, e.g. add `export PATH="$HOME/.poetry/bin:$PATH"` to the end of `~/.bash_profile`. And don't forget to source it, e.g. `source ~/.bash_profile`.
4. Initialize the project by running `./initialize_denkmit.sh`.

Great, the project is set up! Head to the next section to see how to start learning.


## How to Learn Today
So, you've got the project set up, and now you're ready to groove.
1. (Optional) Set the exercises that you want to learn for the day in `config/flashcard_config.py`
2. Get started with your German practice by running `poetry run python flashcards/learn_today_flashcards.py`

Enjoy!
