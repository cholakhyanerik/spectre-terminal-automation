# src/conftest.py
import os
import pytest
from dotenv import load_dotenv
from pywinauto import Application


@pytest.fixture(scope="session")
def app():
    """Launch Spectre Terminal application."""
    load_dotenv()

    exe_path = os.getenv("EXE_PATH")
    if not exe_path or not os.path.exists(exe_path):
        raise FileNotFoundError(f"EXE_PATH invalid or not found: {exe_path}")

    app = Application(backend="uia").start(exe_path)
    yield app
    app.kill()


@pytest.fixture(scope="session")
def meta_app():
    """Launch MetaScalp application through its .lnk shortcut."""
    load_dotenv()

    meta_path = os.getenv("META_EXE_PATH")
    if not meta_path or not os.path.exists(meta_path):
        raise FileNotFoundError(f"META_EXE_PATH invalid or not found: {meta_path}")

    print(f"Launching MetaScalp from shortcut: {meta_path}")

    # Run the .lnk shortcut via explorer
    explorer_cmd = f'explorer.exe "{meta_path}"'

    app = Application(backend="uia").start(explorer_cmd)
    yield app

    try:
        app.kill()
    except Exception:
        pass
