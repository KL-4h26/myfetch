import platform
import distro
import subprocess
import datetime

def format_text(text: str) -> str:
    return text + " " * (46 - len(text))

def insert_data(text: str):
    # Получаем начальные данные что бы не делать лишние запросы
    get_uname = platform.uname()

    # Выводит текущий дистрибутив
    text = text.replace("%distro", format_text(f"{distro.name()} {distro.version()} {get_uname.machine}"))

    # Выводит пользователя (.stdout[0:-1] убирает лишний \n)
    text = text.replace("%user", format_text(f"You: {subprocess.run("whoami", text=True, capture_output=True).stdout[0:-1]}@{get_uname.node}"))

    # Инофрмация о ядре
    text = text.replace("%kernel", format_text(f"Kernel: {get_uname.release}"))

    # Текущее время (Может вывод изменится в будущем)
    text = text.replace("%time", format_text(f"Time: {str(datetime.datetime.now()).split(".")[0]}"))

    # Вывод версии оболочки (Может вывод изменится в будущем)
    text = text.replace("%shell", format_text(f"Bash: {subprocess.run(['bash', '--version'], capture_output=True, text=True).stdout.split(" ")[3]}"))

    # Вывод информации о RAM (Может вывод изменится в будущем)
    mem = subprocess.run(["free", "-h"], capture_output=True, text=True).stdout.split(" ")
    text = text.replace("%memory", format_text(f"Memory: {mem[57]}/{mem[50]}"))

    return text
