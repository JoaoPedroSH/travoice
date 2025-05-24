"""
Módulo principal do Tradutor com Voz
"""

import sys
import os
from pathlib import Path

# Adiciona o diretório raiz ao path
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from src.core.translator import Translator
from src.core.tts_engine import TTSEngine
from src.core.hotkey_manager import HotkeyManager
from src.utils.clipboard import ClipboardManager
from src.utils.logger import Logger
from src.config.settings import Settings


class TradutorVoz:
    def __init__(self):
        self.settings = Settings()
        self.logger = Logger()
        self.clipboard = ClipboardManager()
        self.translator = Translator(self.settings)
        self.tts = TTSEngine(self.settings)
        self.hotkey_manager = HotkeyManager(self.settings)
        
        self.ultimo_texto = ""
        self.texto_pendente = None
        self.falando = False
        
        self._setup_callbacks()

    def _setup_callbacks(self):
        """Configura os callbacks para os diferentes componentes"""
        self.hotkey_manager.set_callbacks({
            'copy': self.copiar_texto,
            'translate': self.traduzir_e_falar,
            'stop': self.parar_fala,
            'test': self.testar_tts,
            'menu': self.mostrar_menu,
            'config': self.mostrar_config
        })
        
        self.tts.set_callbacks({
            'on_start': self._on_tts_start,
            'on_finish': self._on_tts_finish,
            'on_error': self._on_tts_error
        })

    def copiar_texto(self):
        """Copia texto da área de transferência"""
        try:
            texto = self.clipboard.get_text()
            
            if texto and texto != self.ultimo_texto:
                if self.falando:
                    self.texto_pendente = texto
                    self.logger.info(f"📋 Texto copiado (pendente): {self._preview_text(texto)}")
                else:
                    self.ultimo_texto = texto
                    self.logger.info(f"📋 Texto copiado: {self._preview_text(texto)}")
            else:
                self.logger.warning("⚠️ Nenhum texto válido na área de transferência")
                
        except Exception as ex:
            self.logger.error(f"❌ Erro ao copiar: {ex}")

    def traduzir_e_falar(self):
        """Traduz o texto copiado e reproduz via TTS"""
        if self.falando:
            return

        if not self.ultimo_texto:
            return

        try:
            self.logger.info("🔄 Traduzindo...")
            traduzido = self.translator.translate(self.ultimo_texto)
            self.logger.info(f"🌍 Tradução: {self._preview_text(traduzido)}")
            
            self.tts.speak(traduzido)
            
        except Exception as ex:
            self.logger.error(f"❌ Erro na tradução: {ex}")
            self.falando = False

    def parar_fala(self):
        """Para a reprodução de fala"""
        if self.falando:
            self.logger.info("⏹️ Tentando parar fala...")
            self.tts.stop()
        else:
            self.logger.info("🔇 Nenhuma fala ativa.")

    def testar_tts(self):
        """Testa o sistema TTS"""
        if self.falando:
            self.logger.info("🔊 Aguarde terminar a fala atual...")
            return
            
        self.logger.info("🧪 Testando TTS...")
        self.tts.speak("Teste de voz funcionando")

    def mostrar_menu(self):
        """Exibe o menu de comandos"""
        hotkeys = self.settings.get_hotkeys()
        
        menu = [
            "\n" + "="*50,
            "🚀 Tradutor com Voz - MENU",
            "\n📝 COMANDOS DISPONÍVEIS:",
            f"   {hotkeys['copy'].upper()}     → Copiar texto selecionado",
            f"   {hotkeys['translate'].upper()}      → Traduzir e falar",
            f"   {hotkeys['stop'].upper()}      → Parar fala",
            f"   {hotkeys['test'].upper()}      → Testar voz",
            f"   {hotkeys['menu'].upper()}      → Mostrar este menu",
            f"   {hotkeys['config'].upper()}      → Mostrar configurações",
            f"   {hotkeys['quit'].upper()}     → Sair do programa",
            "="*50
        ]
        
        for linha in menu:
            print(linha)

    def mostrar_config(self):
        """Exibe as configurações atuais"""
        config = self.settings.get_all_settings()
        
        print("\n" + "="*50)
        print("⚙️ CONFIGURAÇÕES ATUAIS")
        print(f"\n🌍 Idiomas:")
        print(f"   Origem: {config['languages']['source']}")
        print(f"   Destino: {config['languages']['target']}")
        print(f"\n🔊 TTS:")
        print(f"   Velocidade: {config['tts']['rate']}")
        print(f"   Volume: {config['tts']['volume']}")
        print(f"\n⌨️ Atalhos:")
        for acao, tecla in config['hotkeys'].items():
            print(f"   {acao.capitalize()}: {tecla}")
        print("="*50)

    def _preview_text(self, texto):
        """Cria uma prévia do texto para exibição"""
        max_len = self.settings.get_setting('general', 'max_preview_length')
        if len(texto) > max_len:
            return f"{texto[:max_len]}..."
        return texto

    def _on_tts_start(self):
        """Callback chamado quando TTS inicia"""
        self.falando = True

    def _on_tts_finish(self):
        """Callback chamado quando TTS termina"""
        self.falando = False
        self._processar_texto_pendente()

    def _on_tts_error(self, error):
        """Callback chamado quando há erro no TTS"""
        self.logger.error(f"❌ Erro no TTS: {error}")
        self.falando = False

    def _processar_texto_pendente(self):
        """Processa texto que foi copiado durante a fala"""
        if self.texto_pendente:
            pendente = self.texto_pendente
            self.texto_pendente = None
            self.ultimo_texto = pendente
            self.logger.info("🔁 Processando texto pendente...")
            # Pequena pausa antes de processar o próximo
            import time
            time.sleep(0.5)
            self.traduzir_e_falar()

    def iniciar(self):
        """Inicia o sistema"""
        try:
            self.mostrar_menu()
            self.hotkey_manager.start()
            self.logger.info("\n✅ Sistema iniciado! Use os comandos acima.")
            self.hotkey_manager.wait_for_quit()
            
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            self.logger.error(f"❌ Erro no sistema: {ex}")
        finally:
            self.logger.info("\n👋 Programa finalizado.")


def main():
    """Função principal"""
    tradutor = TradutorVoz()
    tradutor.iniciar()


if __name__ == "__main__":
    main()