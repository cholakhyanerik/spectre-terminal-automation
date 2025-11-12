import os
import pytest
from dotenv import load_dotenv
from pywinauto import Application

@pytest.fixture(scope="session")
def app():
    """Launch and return the desktop application."""
    load_dotenv()
    exe_path = os.getenv("EXE_PATH")
    if not exe_path or not os.path.exists(exe_path):
        raise FileNotFoundError(f"EXE_PATH not found or invalid: {exe_path}")

    app = Application(backend="uia").start(exe_path)
    yield app
    app.kill()
