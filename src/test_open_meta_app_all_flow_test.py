from pywinauto import Desktop
import time

def test_only_meta_app(meta_app):
    print("Ждём появления окна MetaScalp...")

    timeout = 25
    for _ in range(timeout):
        windows = Desktop(backend="uia").windows()
        for w in windows:
            if "MetaScalp" in w.window_text():
                main_window = w
                print("Нашли окно MetaScalp!")
                time.sleep(3)
                main_window.restore()
                time.sleep(2)
                main_window.maximize()
                return
        time.sleep(1)

    raise RuntimeError("Окно MetaScalp не появилось за 25 секунд")
    time.sleep(5)
    main_window.close()
