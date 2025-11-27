import click as cli


@cli.command()
@cli.option('-u', '--user', type=str, help="Enter a username of github to get activities.")
def app(user: str):
    if not user:
        raise cli.exceptions.BadArgumentUsage("Sorry, you need a user param")
    cli.echo(f"User: {user}")