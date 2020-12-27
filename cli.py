import click
from pizzeria import *


@click.group()
def cli():
    pass


@cli.command()
def menu():
    p.menu()


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    p.order(pizza, delivery)


if __name__ == "__main__":
    pizza_list = [Margarita(), Pepperony()]
    p = Pizzeria(pizza_list)
    cli()
