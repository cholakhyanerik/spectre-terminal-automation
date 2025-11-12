# src/test_open_app.py
import time
from pywinauto import mouse

def test_open_maximize_and_click_order_book(app):
    """Open app, maximize window, and click '+ Order Book' text in top-left corner."""
    main_window = app.window(title_re=".*")
    main_window.wait("visible", timeout=10)

    # Maximize window (using pywinauto method for reliability)
    main_window.maximize()

    # Wait for maximize animation
    time.sleep(2)

    # Now click '+ Order Book' near the top-left corner
    rect = main_window.rectangle()

    # Approximate coords of '+ Order Book' text:
    # From your screenshot, it's near top-left but with some padding from the left and top edges.
    x = rect.left + 50   # 50 pixels from left edge (adjust if needed)
    y = rect.top + 45    # 25 pixels from top edge (adjust if needed)

    mouse.click(coords=(x, y))

    # Optional: wait a bit to observe the click effect
    time.sleep(3)

    # Assert window is still visible after click
    assert main_window.is_visible(), "Main window is not visible"


    time.sleep(2)

    # Now click '+ Order Book' near the top-left corner
    centreAddOrderBook = main_window.rectangle()

    x = centreAddOrderBook.left + 1000   # 50 pixels from left edge (adjust if needed)
    y = centreAddOrderBook.top + 580    # 25 pixels from top edge (adjust if needed)

    mouse.click(coords=(x, y))

    # Optional: wait a bit to observe the click effect
    time.sleep(3)

    # Assert window is still visible after click
    assert main_window.is_visible(), "Main window is not visible"