
0. **Configuração**:
```json
{
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
        "auto_detect_language": true,
        "show_preview": true,
        "max_preview_length": 50
    }
}
```

1. **Instalação**:
    ```bash
    python3 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. **Executar**:
    ```bash
    python run.py
    ```

3. **Criar Executável**:
    ```bash
    pyinstaller --noconsole --onefile --add-data "icon.ico;." --name travoice launcher.py
    ```
    --onefile: gera um único .exe
    --noconsole: oculta o terminal (se for app com interface gráfica). Remova essa flag se quiser o terminal.