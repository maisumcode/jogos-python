# 🐍 Plataforma de Jogos Python

- [x] Menu principal
- [x] Sistema de pontuação individual
- [x] Troca de tema claro/escuro

### Servidor Flask

- [x] Servidor web integrado
- [x] IP local com porta dinâmica
- [x] Múltiplas formas de acesso:
  - `http://localhost:PORTA` (acesso local)
  - `http://SEU-IP:PORTA` (acesso pela rede)
  - `http://SEU-COMPUTADOR.local:PORTA` (nome amigável)
- [x] Compatibilidade com MacOS (evita conflitos com AirDrop)
- [x] Gerenciamento automático de processos
- [x] API REST para controle do jogo

#### Geral

- [x] Painel de Controle Visual
- [x] Pause: P ou Espaço
- [x] Menu: M ou ESC
- [x] Tema: T
- [x] Reiniciar: R

### Interface do Usuário

- [x] Menu Principal Interativo
- [x] Painel de Controle
  - Botão de Pausa
  - Botão de Menu
  - Botão de Tema
  - Botão de Reinício
- [x] Feedback Visual de Ações
- [x] Temas Claro/Escuro (padrão: claro)
- [x] Transições Suaves

### 🎮 Tela Inicial

- Placar do jogador atual
- Painel de controles centralizado mostrando:
  - Controles de movimento
  - Teclas de ação do jogo
  - Atalhos do sistema
- Botões de seleção de modo:
  - Snack
  - Tetris
  - Outros
- Interface limpa e minimalista
- Tema claro ativado por padrão

### 🎮 Tela do Snake Game

- Interface minimalista com tema claro padrão
- Elementos da interface:
  - Título "Snake Game" com ícone 🐍
  - Placar do Jogador
- Características:
  - Design responsivo
  - Transições suaves
  - Feedback visual das ações
  - Área de jogo bem definida
  - Sistema de pontuação integrado
  - Modos de jogo flexíveis

## 📁 Como Executar

1. **Requisitos**

   ```bash
   pip install -r requirements.txt
   ```

   Para MacOS, instale também o XQuartz:

   ```bash
   brew install --cask xquartz
   ```

2. **Iniciando o Servidor**

   ```bash
   python main.py
   ```

3. **Acessando o Jogo**

   O servidor mostrará três URLs diferentes para acesso:

   - Local: `http://localhost:PORTA`
   - Rede Local: `http://SEU-IP:PORTA`
   - Nome Amigável: `http://SEU-COMPUTADOR.local:PORTA`

4. **Telas de Jogo**

   - site principal: Acesse a URL base (ex: `http://localhost:PORTA/`)
   - snack: Adicione `/snack` à URL (ex: `http://localhost:PORTA/snack`)
   - tetris: Adicione `/tetris` à URL (ex: `http://localhost:PORTA/tetris`)

## 📁 Estrutura do Projeto

### Organização Modular

### Responsabilidades dos Módulos

#### 🎯 Core

#### 🖼️ UI

- **Renderer** (`renderer.py`):

  - Renderização gráfica
  - Interface do usuário
  - Textos e mensagens
  - Efeitos visuais

- **Menu** (`menu.py`):

  - Menu principal
  - Seleção entre telas de jogo
  - Navegação interativa

- **Components**:

  - **Button** (`button.py`):

    - Botões interativos
    - Feedback visual
    - Sistema de atalhos

  - **ControlPanel** (`control_panel.py`):
    - Painel de controle do jogo
    - Organização de botões
    - Feedback de estado

#### 🌐 Server (`routes.py`)

- Rotas do servidor Flask
- Gerenciamento de processos
- URLs amigáveis
- API REST

## 🎮 Versão

Versão atual: 0.0.1
