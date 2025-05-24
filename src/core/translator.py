"""
Módulo de tradução de textos
"""

from deep_translator import GoogleTranslator


class Translator:
    def __init__(self, settings):
        self.settings = settings
        self._setup_translator()

    def _setup_translator(self):
        """Configura o tradutor com base nas configurações"""
        lang_config = self.settings.get_setting('languages')
        self.translator = GoogleTranslator(
            source=lang_config['source'], 
            target=lang_config['target']
        )

    def translate(self, text):
        """
        Traduz um texto
        
        Args:
            text (str): Texto a ser traduzido
            
        Returns:
            str: Texto traduzido
        """
        if not text or not text.strip():
            raise ValueError("Texto vazio não pode ser traduzido")
            
        return self.translator.translate(text.strip())

    def change_target_language(self, target_lang):
        """
        Muda o idioma de destino
        
        Args:
            target_lang (str): Código do idioma de destino
        """
        self.settings.update_setting('languages', 'target', target_lang)
        self._setup_translator()

    def change_source_language(self, source_lang):
        """
        Muda o idioma de origem
        
        Args:
            source_lang (str): Código do idioma de origem
        """
        self.settings.update_setting('languages', 'source', source_lang)
        self._setup_translator()