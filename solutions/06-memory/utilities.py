"""
Utility functions for memory game.

Functions
---------
position_from_index : Compute position from index.
create_card : Create card dictionary.
index_from_position : Compute card index from position.
remaining_cards : Count number of remaning cards.
"""

from psychopy import visual

def position_from_index(index):
    """
    Compute position from index.
    Assumes 4 x 2 (columns x rows) layout.

    Parameters
    ----------
    index : int
        0..7 index

    Returns
    ----------
    tuple : (x, y) in norm units
    """
    iy = index // 4
    ix = index % 4
    return (-0.75 + 0.5 * ix, 0.5 - iy)

def create_card(win, filename, index):
    """
    Create card dictionary.

    Parameters
    ----------
    win : psychopy.visual.Window
    filename : str
    index : int
        0..7 range.

    Returns
    ----------
    dict
    """
    return {
        "front" : visual.ImageStim(win, filename, pos=position_from_index(index)),
        "back" : visual.Rect(win, size=(0.5, 1), fillColor="green", lineColor="white", pos=position_from_index(index)),
        "filename" : filename,
        "side" : "back",
        "show" : True
    }

def index_from_position(pos):
    """
    Compute card index from position.
    Assumes 4 x 2 (columns x rows) layout.

    Parameters
    ----------
    pos : tuple
        (x, y) in norm units

    Returns
    ----------
    int : 0..7 range index
    """
    ix = int((pos[0] + 1) / 0.5) # left is negative
    iy = 1 - int((pos[1] + 1))   # up is positive
    return ix + iy * 4

def remaining_cards(cards):
    """
    Count number of remaning cards.

    Parameters
    ----------
    cards : list
        List of dictionaries with logical "show" field.

    Returns
    ----------
    int : number of cards with "show" equal True
    """
    return len([card 
                for card in cards
                if card['show']])
