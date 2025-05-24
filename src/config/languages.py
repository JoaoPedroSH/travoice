"""
Gerenciador de idiomas suportados
"""


class LanguageManager:
    """Gerencia os idiomas disponíveis para tradução"""
    
    SUPPORTED_LANGUAGES = {
        'pt': 'Português',
        'en': 'Inglês',
        'es': 'Espanhol',
        'fr': 'Francês',
        'de': 'Alemão',
        'it': 'Italiano',
        'ja': 'Japonês',
        'ko': 'Coreano',
        'zh': 'Chinês',
        'ru': 'Russo',
        'ar': 'Árabe',
        'hi': 'Hindi',
        'auto': 'Detecção Automática'
    }

    @classmethod
    def get_language_name(cls, code):
        """
        Obtém o nome do idioma pelo código
        
        Args:
            code (str): Código do idioma
            
        Returns:
            str: Nome do idioma
        """
        return cls.SUPPORTED_LANGUAGES.get(code, f"Idioma ({code})")

    @classmethod
    def get_supported_languages(cls):
        """
        Retorna todos os idiomas suportados
        
        Returns:
            dict: Dicionário com códigos e nomes dos idiomas
        """
        return cls.SUPPORTED_LANGUAGES.copy()

    @classmethod
    def is_valid_language(cls, code):
        """
        Verifica se um código de idioma é válido
        
        Args:
            code (str): Código do idioma
            
        Returns:
            bool: True se o código for válido
        """
        return code in cls.SUPPORTED_LANGUAGES