# src\test_open_meta_app_all_flow_test.py

import time
from pywinauto import mouse
from pywinauto.keyboard import send_keys

def test_only_meta_app(meta_app):
    """This test launches ONLY the MetaScalp application."""
    
    # Get main window
    main_window = meta_app.window()
    time.sleep(10)
    send_keys("{VK_LWIN down}{TAB}{VK_LWIN up}")

    time.sleep(4)
    main_window.wait("visible", timeout=15)


    time.sleep(30)
    assert main_window.is_visible(), "MetaScalp window did not open properly"
