"""
Gerenciador de configurações do sistema
"""

import json
import os
from pathlib import Path


class Settings:
    def __init__(self):
        self.config_file = self._get_config_path()
        self.settings = self._load_settings()

    def _get_config_path(self):
        """Obtém o caminho do arquivo de configuração"""
        # Busca o arquivo de config na raiz do projeto
        current_dir = Path(__file__).parent
        project_root = current_dir.parent.parent
        return project_root / "config.json"

    def _load_settings(self):
        """Carrega as configurações do arquivo JSON"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self._get_default_settings()
        except Exception:
            return self._get_default_settings()

    def _get_default_settings(self):
        """Retorna configurações padrão"""
        return {
            "languages": {
                "source": "auto",
                "target": "pt"
            },
            "tts": {
                "rate": 180,
                "volume": 0.9,
                "voice_preference": ["portuguese", "brasil", "pt-br"]
            },
            "hotkeys": {
                "copy": "ctrl+c",
                "translate": "alt+t",
                "stop": "alt+i",
                "test": "alt+v",
                "menu": "alt+m",
                "config": "alt+c",
                "quit": "ctrl+q"
            },
            "general": {
                "auto_detect_language": True,
                "show_preview": True,
                "max_preview_length": 50
            }
        }

    def get_setting(self, section, key=None):
        """
        Obtém uma configuração específica
        
        Args:
            section (str): Seção da configuração
            key (str, optional): Chave específica
            
        Returns:
            any: Valor da configuração
        """
        if key is None:
            return self.settings.get(section, {})
        return self.settings.get(section, {}).get(key)

    def get_all_settings(self):
        """
        Retorna todas as configurações
        
        Returns:
            dict: Todas as configurações
        """
        return self.settings.copy()

    def get_hotkeys(self):
        """
        Retorna os atalhos de teclado
        
        Returns:
            dict: Atalhos configurados
        """
        return self.get_setting('hotkeys')

    def update_setting(self, section, key, value):
        """
        Atualiza uma configuração
        
        Args:
            section (str): Seção da configuração
            key (str): Chave a ser atualizada
            value (any): Novo valor
        """
        if section not in self.settings:
            self.settings[section] = {}
        
        self.settings[section][key] = value
        self._save_settings()

    def _save_settings(self):
        """Salva as configurações no arquivo"""
        try:
            # Cria o diretório se não existir
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
        except Exception as ex:
            print(f"❌ Erro ao salvar configurações: {ex}")