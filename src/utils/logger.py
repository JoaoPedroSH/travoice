"""
Sistema de logging para o aplicativo
"""

import datetime
import sys
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

def log(msg):
    logging.info(msg)

class Logger:
    def __init__(self, show_timestamp=False):
        self.show_timestamp = show_timestamp

    def _format_message(self, level, message):
        """
        Formata mensagem de log
        
        Args:
            level (str): Nível do log
            message (str): Mensagem
            
        Returns:
            str: Mensagem formatada
        """
        if self.show_timestamp:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            return f"[{timestamp}] {level}: {message}"
        return message

    def info(self, message):
        """
        Log de informação
        
        Args:
            message (str): Mensagem de informação
        """
        formatted = self._format_message("INFO", message)
        print(formatted)

    def warning(self, message):
        """
        Log de aviso
        
        Args:
            message (str): Mensagem de aviso
        """
        formatted = self._format_message("WARNING", message)
        print(formatted)

    def error(self, message):
        """
        Log de erro
        
        Args:
            message (str): Mensagem de erro
        """
        formatted = self._format_message("ERROR", message)
        print(formatted, file=sys.stderr)

    def debug(self, message):
        """
        Log de debug
        
        Args:
            message (str): Mensagem de debug
        """
        formatted = self._format_message("DEBUG", message)
        print(formatted)