from typing import Optional 
import typer 
import json 
import arrow
from typing import Optional
from .read import read
from .write import writes
from .transform import transform1, transform2
app = typer.Typer(add_completion=False)

@app.command()
def etl(inp:Optional[str]=None,out:Optional[str]=None,tr:Optional[int]=1):
    if inp:
        typer.echo("reading files...")
        p=read(inp)
        print(p)
    else:
        typer.echo("no file name provided")
        return
    if tr==1:
        typer.echo("applying transformation part 1")
        ans=transform1(p)
    elif tr==1:
        typer.echo("applying transormation part 2")
        ans=str(transform2(p))
    else:
        typer.echo("apply correct transformation")
    if out:
        writes(out,ans)
    else:
        typer.echo("provide a filename to write to")


def run() -> None:
    app()
