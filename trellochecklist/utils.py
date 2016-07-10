def get_board_by_name(trello, name):
    return next(board for board in trello.get_boards() if board.name == name)


def get_card_by_name(board, name):
    return next(card for card in board.get_cards() if card.name == name)


def add_checklist(card, name, items):
    checklist = card.add_checklists({'name': name})
    for item in items:
        checklist.add_item({'name': item})
