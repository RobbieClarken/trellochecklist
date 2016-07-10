from unittest.mock import Mock, MagicMock, call

from trellochecklist.utils import get_board_by_name, get_card_by_name, \
                                  add_checklist


class MockWithName(Mock):
    def __new__(cls, name=None, **kwargs):
        mock = Mock(**kwargs)
        mock.configure_mock(name=name)
        return mock


def test_get_board_by_name_returns_board():
    boards = [MockWithName(name='first'),
              MockWithName(name='second'),
              MockWithName(name='third')]
    trello_mock = Mock(**{'get_boards.return_value': boards})
    assert get_board_by_name(trello_mock, 'second') is boards[1]


def test_get_card_by_name_returns_board():
    cards = [MockWithName(name='first'),
             MockWithName(name='second'),
             MockWithName(name='third')]
    board_mock = Mock(**{'get_cards.return_value': cards})
    assert get_card_by_name(board_mock, 'second') is cards[1]


def test_add_checklist():
    checklist_mock = MagicMock()
    card_mock = Mock(**{'add_checklists.return_value': checklist_mock})
    add_checklist(card_mock, 'Shopping List', ['milk', 'bread'])
    assert card_mock.add_checklists.call_args == call({'name': 'Shopping List'})
    assert checklist_mock.add_item.call_args_list == [call({'name': 'milk'}),
                                                      call({'name': 'bread'})]
