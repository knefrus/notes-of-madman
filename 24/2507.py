import pyautogui
import time

def type_milliseconds():
    try:
        while True:
            # Печатает текст "1 сотая секунды"
            pyautogui.typewrite("11"
                                "1"
                                "1"
                                "1"
                                "")
            # Нажимает Enter (отправить)
            pyautogui.press("enter")
            # Пауза в 0.01 секунды
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nСкрипт остановлен вручную.")

# Убедитесь, что курсор находится в нужном текстовом поле перед запуском
print("Переключитесь в нужное окно, начнется через 5 секунд...")
time.sleep(5)  # Время, чтобы переключиться на нужное окно
type_milliseconds()
