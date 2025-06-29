import datetime

import typer

from zm05 import mathtools

app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))

@app.command()
def lcm(x: int, y: int): 
    """
    最小公倍数
    """
    typer.echo(mathtools.lcm(x, y))

@app.command()
def average():
    n=input()
    ave=[float(x) for x in n.split()]
    return sum(ave)/ len(ave)
print(average())