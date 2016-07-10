import click

from trolly.client import Client

from . import utils


@click.command()
@click.option('--board', 'board_name', required=True)
@click.option('--card', 'card_name', required=True)
@click.option('--checklist-name', default='Checklist')
@click.option('--api-key', envvar='TRELLO_API_KEY',
              help='If not specified will use environment variable TRELLO_API_KEY')
@click.option('--token', envvar='TRELLO_APP_TOKEN',
              help='If not specified will use environment variable TRELLO_APP_TOKEN')
@click.argument('file', type=click.File())
def main(board_name, card_name, checklist_name, api_key, token, file):
    """Create a Trello checklist from a text file."""
    items = [line.strip() for line in file]
    trello = Client(api_key, token)
    board = utils.get_board_by_name(trello, board_name)
    card = utils.get_card_by_name(board, card_name)
    utils.add_checklist(card, checklist_name, items)
