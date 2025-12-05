# src\test_open_meta_app_all_flow_test.py

import time

def test_only_meta_app(meta_app):
    """This test launches ONLY the MetaScalp application."""
    
    # Get main window
    main_window = meta_app.window(title_re=".*")
    main_window.wait("visible", timeout=15)

    # Maximize
    main_window.maximize()
    time.sleep(1)

    time.sleep(30)
    assert main_window.is_visible(), "MetaScalp window did not open properly"
