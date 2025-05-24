from pystray import Icon, Menu, MenuItem
from PIL import Image
import threading
import os
import sys

def run_tradutor():
    # Importa a partir do caminho relativo ao run.py
    from src.main import main
    main()

def resource_path(relative_path):
    """Obtém caminho absoluto, útil para PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def criar_tray():
    def on_exit(icon, item):
        icon.stop()
        os._exit(0)  # Encerra imediatamente o processo

    # Caminho do ícone (deve estar na mesma pasta do .exe ou usar resource_path)
    icon_path = resource_path("icon.ico")
    image = Image.open(icon_path)

    # Criar menu da bandeja
    menu = Menu(
            MenuItem("Ctrl+C - Selecionar", None, enabled=False),
            MenuItem("Alt+T - Traduzir e Falar", None, enabled=False),
            MenuItem("Ctrl+Q - Sair (atalho)", None, enabled=False),
            Menu.SEPARATOR,
            MenuItem("Sair agora", on_exit))

    # Rodar tradutor em thread separada
    threading.Thread(target=run_tradutor, daemon=True).start()

    # Iniciar ícone na bandeja
    Icon("Tradutor de Voz", image, "Tradutor de Voz", menu).run()

if __name__ == "__main__":
    criar_tray()
