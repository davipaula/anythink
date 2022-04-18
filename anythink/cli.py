import typer

from guesser_service import GuesserService


def main():
    guess = typer.prompt("Guess a word!")
    guesser = GuesserService()

    while True:
        if guess == "/q":
            should_reveal_word = typer.confirm(
                "Do you want to reveal the word?", default=True
            )

            if should_reveal_word:
                typer.echo(f"Today's word is {guesser.get_word_of_day()}!")

            typer.echo("Thanks for playing AnyThink!")

            break

        result = guesser.guess_word(guess)

        if not result.found:
            typer.echo(f"The word you guessed was not recognized. Please try again!")
        else:
            if result.position == 1:
                typer.echo("Congratulations! You guessed the right word!")
                break
            else:
                typer.echo(f"The word you guessed is in position {result.position}")

        guess = typer.prompt("Guess the word")


if __name__ == "__main__":
    typer.run(main)
