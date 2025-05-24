"""
Módulo de síntese de fala (Text-to-Speech)
"""

import pyttsx3
import threading
import time


class TTSEngine:
    def __init__(self, settings):
        self.settings = settings
        self.callbacks = {}
        self.current_engine = None
        self.is_speaking = False

    def set_callbacks(self, callbacks):
        """
        Define callbacks para eventos do TTS
        
        Args:
            callbacks (dict): Dicionário com callbacks
        """
        self.callbacks = callbacks

    def _create_engine(self):
        """Cria uma nova instância do engine TTS"""
        try:
            engine = pyttsx3.init()
            tts_config = self.settings.get_setting('tts')
            
            # Configura propriedades
            engine.setProperty('rate', tts_config['rate'])
            engine.setProperty('volume', tts_config['volume'])
            
            # Tenta definir voz em português
            self._set_portuguese_voice(engine, tts_config['voice_preference'])
            
            return engine
            
        except Exception as ex:
            if self.callbacks.get('on_error'):
                self.callbacks['on_error'](f"Erro ao criar engine TTS: {ex}")
            return None

    def _set_portuguese_voice(self, engine, voice_preferences):
        """Tenta definir uma voz em português"""
        try:
            voices = engine.getProperty('voices')
            
            for preference in voice_preferences:
                for voice in voices:
                    if preference.lower() in voice.name.lower():
                        engine.setProperty('voice', voice.id)
                        return
                        
        except Exception:
            pass  # Se não conseguir definir voz específica, usa a padrão

    def speak(self, text):
        """
        Reproduz texto via TTS em thread separada
        
        Args:
            text (str): Texto a ser falado
        """
        if self.is_speaking:
            return
            
        thread = threading.Thread(target=self._speak_text, args=(text,))
        thread.daemon = True
        thread.start()

    def _speak_text(self, text):
        """Executa a fala do texto"""
        try:
            if self.callbacks.get('on_start'):
                self.callbacks['on_start']()
                
            self.is_speaking = True
            self.current_engine = self._create_engine()
            
            if not self.current_engine:
                return
                
            self.current_engine.say(text)
            self.current_engine.runAndWait()
            
        except Exception as ex:
            if self.callbacks.get('on_error'):
                self.callbacks['on_error'](ex)
        finally:
            self.is_speaking = False
            self._cleanup_engine()
            
            if self.callbacks.get('on_finish'):
                self.callbacks['on_finish']()

    def _cleanup_engine(self):
        """Limpa a instância do engine"""
        try:
            if self.current_engine:
                del self.current_engine
                self.current_engine = None
        except:
            pass

    def stop(self):
        """Para a fala atual (limitado pelo pyttsx3)"""
        # pyttsx3 não tem método para parar fala em andamento
        # Apenas marca que não está mais falando
        self.is_speaking = False

    def is_speaking_active(self):
        """
        Verifica se está falando
        
        Returns:
            bool: True se estiver falando
        """
        return self.is_speaking