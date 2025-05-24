"""
Gerenciador da área de transferência
"""

import pyperclip
import time


class ClipboardManager:
    def __init__(self):
        self.last_text = ""

    def get_text(self):
        """
        Obtém texto da área de transferência
        
        Returns:
            str: Texto da área de transferência
        """
        try:
            text = pyperclip.paste()
            return text.strip() if text else ""
        except Exception as ex:
            raise Exception(f"Erro ao acessar área de transferência: {ex}")

    def set_text(self, text):
        """
        Define texto na área de transferência
        
        Args:
            text (str): Texto a ser copiado
        """
        try:
            pyperclip.copy(text)
        except Exception as ex:
            raise Exception(f"Erro ao copiar para área de transferência: {ex}")

    def has_new_text(self):
        """
        Verifica se há novo texto na área de transferência
        
        Returns:
            bool: True se há novo texto
        """
        current_text = self.get_text()
        if current_text and current_text != self.last_text:
            self.last_text = current_text
            return True
        return False

    def get_last_text(self):
        """
        Retorna o último texto capturado
        
        Returns:
            str: Último texto
        """
        return self.last_text