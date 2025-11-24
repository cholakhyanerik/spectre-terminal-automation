# src/test_open_app.py
import time
from pywinauto import mouse

def test_open_maximize_and_add_orderbook_withCoin(app):
    """Open app, maximize window, and click '+ Order Book' text in top-left corner."""
    main_window = app.window(title_re=".*")
    main_window.wait("visible", timeout=10)

    # Maximize window (using pywinauto method for reliability)
    main_window.maximize()

    # Wait for maximize animation
    time.sleep(4)


    # Assert window is still visible after click
    assert main_window.is_visible(), "Main window is not visible"


    time.sleep(3)

    # Now click '+ Order Book' near the top-left corner
    centreAddOrderBook = main_window.rectangle()

    x = centreAddOrderBook.left + 1000   # 50 pixels from left edge (adjust if needed)
    y = centreAddOrderBook.top + 580    # 25 pixels from top edge (adjust if needed)

    mouse.click(coords=(x, y))

    # Optional: wait a bit to observe the click effect
    time.sleep(5)

    ################################################################
    centreAddOrderBookModalCoin = main_window.rectangle()
    x = centreAddOrderBookModalCoin.left + 942   # 50 pixels from left edge (adjust if needed)
    y = centreAddOrderBookModalCoin.top + 552    # 25 pixels from top edge (adjust if needed)
    time.sleep(2)
    mouse.click(coords=(x, y))
    mouse.click(coords=(x, y))
    time.sleep(5)
    # Assert window is still visible after click
    assert main_window.is_visible(), "Main window is not visible"


    ######################################################################

    # Now click '+ Order Book' near the top-left corner
    addDefauledCoinWIchSelected = main_window.rectangle()

    x = addDefauledCoinWIchSelected.left + 700   # 50 pixels from left edge (adjust if needed)
    y = addDefauledCoinWIchSelected.top + 845    # 25 pixels from top edge (adjust if needed)

    mouse.click(coords=(x, y))

    # Optional: wait a bit to observe the click effect
    time.sleep(1)

    mouse.click(coords=(x, y))
    time.sleep(30)
    # Assert window is still visible after click
    assert main_window.is_visible(), "Main window is not visible"