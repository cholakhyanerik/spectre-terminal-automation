# src\test_open_spectre_app_all_flow_test.py

import time
from pywinauto import mouse
from pywinauto.keyboard import send_keys


def test_open_maximize_and_add_orderbook_withCoin(app):
    """
    Open app, maximize window, and perform clicks to add an Order Book with coin selection.
    """

    # --- Initialize main window ---
    main_window = app.window(title_re=".*")
    main_window.wait("visible", timeout=10)

    # --- Maximize the window ---
    main_window.maximize()
    time.sleep(2)  # Allow maximize animation to finish

    assert main_window.is_visible(), "Main window is not visible after maximizing"
    time.sleep(2)

    # ---------------------------------------------------------
    # Click "+ Order Book"
    # ---------------------------------------------------------
    rect = main_window.rectangle()

    x = rect.left + 1000
    y = rect.top + 580
    mouse.click(coords=(x, y))

    time.sleep(2)


    # ---------------------------------------------------------
    # Orderneri qanakic hetoyva click
    # ---------------------------------------------------------
    rect = main_window.rectangle()

    x = rect.left + 1150
    y = rect.top + 680
    mouse.click(coords=(x, y))
    mouse.click(coords=(x, y))

    time.sleep(2)


    # ---------------------------------------------------------
    # Click inside Order Book modal (coin selection)
    # ---------------------------------------------------------
    modal_rect = main_window.rectangle()

    modal_x = modal_rect.left + 942
    modal_y = modal_rect.top + 552

    time.sleep(1)
    mouse.click(coords=(modal_x, modal_y))
    mouse.click(coords=(modal_x, modal_y))

    time.sleep(3)

    assert main_window.is_visible(), "Main window became invisible after coin modal interactions"

    # ---------------------------------------------------------
    # Search XRP-USDT
    # ---------------------------------------------------------
    default_rect = main_window.rectangle()

    search_x = default_rect.left + 1100
    search_y = default_rect.top + 320

    mouse.click(coords=(search_x, search_y))  # ✅ Correct coordinates

    time.sleep(1)
    send_keys("XRP-USDT")  # Type the text
    time.sleep(1)

    # ---------------------------------------------------------
    # Click default coin (already selected)
    # ---------------------------------------------------------
    default_rect = main_window.rectangle()

    default_x = default_rect.left + 700
    default_y = default_rect.top + 845

    mouse.click(coords=(default_x, default_y))
    time.sleep(1)

    mouse.click(coords=(default_x, default_y))
    time.sleep(10)

    assert main_window.is_visible(), "Main window is not visible after selecting default coin"
