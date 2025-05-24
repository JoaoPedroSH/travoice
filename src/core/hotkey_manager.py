"""
Gerenciador de atalhos de teclado
"""

import keyboard


class HotkeyManager:
    def __init__(self, settings):
        self.settings = settings
        self.callbacks = {}
        self.hotkeys_registered = False

    def set_callbacks(self, callbacks):
        """
        Define callbacks para os atalhos
        
        Args:
            callbacks (dict): Dicionário com callbacks para cada ação
        """
        self.callbacks = callbacks

    def start(self):
        """Registra todos os atalhos de teclado"""
        if self.hotkeys_registered:
            return
            
        hotkeys = self.settings.get_hotkeys()
        
        try:
            # Registra atalhos básicos
            keyboard.add_hotkey(hotkeys['copy'], self._safe_callback('copy'))
            keyboard.add_hotkey(hotkeys['translate'], self._safe_callback('translate'))
            keyboard.add_hotkey(hotkeys['stop'], self._safe_callback('stop'))
            keyboard.add_hotkey(hotkeys['test'], self._safe_callback('test'))
            keyboard.add_hotkey(hotkeys['menu'], self._safe_callback('menu'))
            keyboard.add_hotkey(hotkeys['config'], self._safe_callback('config'))
            
            self.hotkeys_registered = True
            
        except Exception as ex:
            raise Exception(f"Erro ao registrar atalhos: {ex}")

    def _safe_callback(self, action):
        """
        Cria um callback seguro que trata exceções
        
        Args:
            action (str): Nome da ação
            
        Returns:
            function: Callback seguro
        """
        def callback():
            try:
                if action in self.callbacks:
                    # Pequeno delay para evitar conflitos
                    import time
                    if action == 'copy':
                        time.sleep(0.15)
                    
                    self.callbacks[action]()
            except Exception as ex:
                print(f"❌ Erro no atalho {action}: {ex}")
                
        return callback

    def wait_for_quit(self):
        """Aguarda o comando de sair"""
        quit_hotkey = self.settings.get_setting('hotkeys', 'quit')
        keyboard.wait(quit_hotkey)

    def unregister_all(self):
        """Remove todos os atalhos registrados"""
        try:
            keyboard.unhook_all()
            self.hotkeys_registered = False
        except Exception:
            pass