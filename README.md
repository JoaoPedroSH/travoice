# TRAVOICE - Tradutor com Voz

## Estrutura do Projeto

```
travoice/
├── .gitattributes
├── LICENSE
├── README.md
├── build
    └── travoice
    │   ├── Analysis-00.toc
    │   ├── EXE-00.toc
    │   ├── PKG-00.toc
    │   ├── PYZ-00.pyz
    │   ├── PYZ-00.toc
    │   ├── base_library.zip
    │   ├── localpycs
    │       ├── pyimod01_archive.pyc
    │       ├── pyimod02_importers.pyc
    │       ├── pyimod03_ctypes.pyc
    │       ├── pyimod04_pywin32.pyc
    │       └── struct.pyc
    │   ├── travoice.pkg
    │   ├── warn-travoice.txt
    │   └── xref-travoice.html
├── config.json
├── dist
    └── travoice.exe
├── icon.ico
├── install.md
├── launcher.py
├── requirements.txt
├── run.py
├── src
    ├── __pycache__
    │   └── main.cpython-313.pyc
    ├── config
    │   ├── __pycache__
    │   │   └── settings.cpython-313.pyc
    │   ├── init.py
    │   ├── languages.py
    │   └── settings.py
    ├── core
    │   ├── __pycache__
    │   │   ├── hotkey_manager.cpython-313.pyc
    │   │   ├── translator.cpython-313.pyc
    │   │   └── tts_engine.cpython-313.pyc
    │   ├── hotkey_manager.py
    │   ├── init.py
    │   ├── translator.py
    │   └── tts_engine.py
    ├── init.py
    ├── main.py
    └── utils
    │   ├── __pycache__
    │       ├── clipboard.cpython-313.pyc
    │       └── logger.cpython-313.pyc
    │   ├── clipboard.py
    │   ├── init.py
    │   └── logger.py
└── travoice.spec
```

## Funcionalidades Principais

### ✨ Novas Features
- 🌐 **Seleção de idiomas**: Escolha idioma de origem e destino
- ⚙️ **Configuração persistente**: Configurações salvas em arquivo JSON
- 🎛️ **Menu interativo**: Interface de configuração via console
- 📁 **Estrutura modular**: Código organizado em módulos
- 🔧 **Hotkeys personalizáveis**: Teclas de atalho configuráveis
- 📊 **Sistema de logs**: Melhor rastreamento de erros
- 🎯 **Detecção automática**: Auto-detecção de idioma opcional

### 🎮 Comandos Disponíveis
- `Ctrl+C` → Copiar texto selecionado
- `Alt+T` → Traduzir e falar
- `Alt+I` → Parar fala
- `Alt+V` → Testar voz
- `Alt+M` → Mostrar menu
- `Alt+C` → Configurar idiomas
- `Ctrl+Q` → Sair do programa

### 🌍 Idiomas Suportados
O sistema suporta todos os idiomas do Google Translate, incluindo:
- Português (pt)
- Inglês (en)
- Espanhol (es)
- Francês (fr)
- Alemão (de)
- Italiano (it)
- Japonês (ja)
- Chinês (zh)
- E muitos outros...

3. **Configurar idiomas**:
   - Pressione `Alt+C` para abrir o menu de configuração
   - Escolha os idiomas de origem e destino
   - As configurações são salvas automaticamente

4. **Usar o tradutor**:
   - Selecione um texto em qualquer aplicativo
   - Pressione `Ctrl+C` para copiar
   - Pressione `Alt+T` para traduzir e ouvir

## Melhorias Implementadas

### 🏗️ Arquitetura
- **Separação de responsabilidades**: Cada módulo tem uma função específica
- **Configuração centralizada**: Todas as configurações em um local
- **Tratamento de erros robusto**: Melhor handling de exceções
- **Threading otimizado**: Performance melhorada para TTS

### 🔧 Funcionalidades
- **Configuração dinâmica**: Altere idiomas sem reiniciar
- **Preview de texto**: Visualize o texto antes da tradução
- **Persistência**: Configurações mantidas entre sessões
- **Logs detalhados**: Melhor debugging e monitoramento
