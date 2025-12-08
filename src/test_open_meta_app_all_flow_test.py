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
                
                # Проверяем, не свернуто ли окно, и восстанавливаем если нужно
                if main_window.is_minimized():
                    main_window.restore()

                assert main_window.is_visible() and not main_window.is_minimized(), "Окно приложения недоступно!"
                return
        time.sleep(1)

    raise RuntimeError("Окно MetaScalp не появилось за 25 секунд")
