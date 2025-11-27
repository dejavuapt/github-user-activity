import click as cli
from app.git_client import GitClient
from app.git_parse import GitEventsParser
from requests import HTTPError

def do(username: str):
    client = GitClient()
    parser = GitEventsParser()

    try:
        events = parser.parse_events(
            events=client.fetch_events(username)
        )
        cli.secho(f"Recent actions of the {username} user:", fg="cyan")

        for e in events:
            cli.echo(e)
    except HTTPError as e:
        cli.secho(f"There is no user named {username}. Please, check it", fg="red")


@cli.command()
@cli.option('-u', '--user', type=str, help="Enter a username of github to get activities.")
def app(user: str):
    if not user:
        raise cli.exceptions.BadArgumentUsage("Sorry, you need a user param")
    do(user)