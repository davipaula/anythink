import typer

from guesser_service import guess_word


def main():
    guess = typer.prompt("Guess a word!")

    while guess != "/q":
        result = guess_word(guess)

        if not result.found:
            typer.echo(f"The word you guessed was not recognized. Please try again!")
        else:
            if result.position == 1:
                typer.echo("Congratulations! You guessed the right word!")
                typer.Abort()
            else:
                typer.echo(f"The word you guessed is in position {result.position}")

        guess = typer.prompt("Guess the word")


if __name__ == "__main__":
    typer.run(main)
