from pathlib import Path
from unittest.mock import patch, call, MagicMock

from click.testing import CliRunner

from trellochecklist.cli import main


@patch('trellochecklist.cli.Client')
@patch('trellochecklist.cli.utils')
def test_cli(utils, Client):
    trello = MagicMock()
    board = MagicMock()
    card = MagicMock()

    Client.return_value = trello
    utils.get_board_by_name.return_value = board
    utils.get_card_by_name.return_value = card

    test_file = str(Path(__file__).with_name('list.txt'))
    runner = CliRunner()
    result = runner.invoke(main, ['--board', 'Home', '--card', 'Shopping',
                                  '--checklist-name', 'Groceries',
                                  '--api-key', '1a2b', '--token', '3e4d',
                                  test_file])
    assert result.exit_code == 0
    assert Client.call_args == call('1a2b', '3e4d')
    assert utils.get_board_by_name.call_args == call(trello, 'Home')
    assert utils.get_card_by_name.call_args == call(board, 'Shopping')
    assert utils.add_checklist.call_args == call(card, 'Groceries', ['milk', 'eggs'])
