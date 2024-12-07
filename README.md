# 🐍 Plataforma de Jogos Python

Uma plataforma modular para jogos Python que combina a diversão dos jogos clássicos com uma arquitetura moderna e expansível.

## 🎯 Características Principais

### Sistema Base

- [x] Menu principal interativo
- [x] Sistema de pontuação global e individual
- [x] Troca de tema claro/escuro
- [x] Interface responsiva e moderna
- [x] Sistema de plugins para novos jogos
- [x] Gerenciamento de estados e saves

### Servidor Web

- [x] Backend Flask para multiplayer
- [x] Sistema de ranking online
- [x] API REST para integrações
- [x] Múltiplos pontos de acesso:
  - Local: `http://localhost:PORTA`
  - Rede: `http://SEU-IP:PORTA`
  - DNS Local: `http://SEU-COMPUTADOR.local:PORTA`

### Controles Universais

- **Pause**: P ou Espaço
- **Menu**: M ou ESC
- **Tema**: T
- **Reiniciar**: R

## 🎮 Jogos Disponíveis

### 🐍 Snake

- Controles com setas direcionais
- Modos de dificuldade
- Power-ups especiais
- Ranking local e online

### 🟦 Tetris

- Sistema de rotação intuitivo
- Preview da próxima peça
- Sistema de hold piece
- Modos de jogo variados

## 📁 Estrutura do Projeto

```
jogos-python/
├── server/
│   ├── app.py           # Servidor Flask
│   ├── routes.py        # Rotas da API
│   └── database.py      # Gerenciamento de dados
├── core/
│   ├── game_manager.py  # Gerenciador de jogos
│   ├── state.py         # Gerenciamento de estado
│   └── events.py        # Sistema de eventos
├── ui/
│   ├── menu.py          # Menu principal
│   ├── theme.py         # Sistema de temas
│   └── components/      # Componentes reutilizáveis
├── games/
│   ├── base.py          # Classe base para jogos
│   ├── snake/
│   │   ├── main.py
│   │   └── assets/
│   └── tetris/
│       ├── main.py
│       ├── blocks.py
│       └── assets/
└── utils/
    ├── config.py        # Configurações
    └── helpers.py       # Funções auxiliares
```

## 🚀 Como Executar

### 1. Requisitos do Sistema

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Para MacOS: XQuartz (opcional)

### 2. Instalação

```bash
# Clone o repositório
git clone https://github.com/maisumcode/jogos-python.git

# Instale as dependências
pip install -r requirements.txt

# Para MacOS (opcional)
brew install --cask xquartz
```

### 3. Iniciando a Plataforma

#### Modo Servidor (Recomendado)

```bash
# Inicia o servidor Flask com interface web
python server/app.py
```

O servidor irá:

- Encontrar uma porta livre automaticamente
- Mostrar as URLs de acesso:
  - Local: `http://localhost:PORTA`
  - Rede Local: `http://SEU-IP:PORTA`
  - Nome Amigável: `http://SEU-COMPUTADOR.local:PORTA`
- Abrir o navegador automaticamente

#### Recarregamento de Alterações

O servidor possui duas formas de recarregar alterações feitas no código:

1. **Recarregamento Automático** (Ativado por padrão)

   - O servidor detecta alterações nos arquivos
   - Recarrega automaticamente quando você salva um arquivo
   - Útil durante o desenvolvimento
   - Algumas alterações podem requerer reinício manual

2. **Reinício Manual** (Se necessário)
   - Pare o servidor atual (Ctrl+C)
   - Inicie novamente com:
   ```bash
   python server/app.py
   ```

#### Modo Offline (Jogos Individuais)

```bash
# Para jogar Snake
python games/snake/main.py

# Para jogar Tetris
python games/tetris/main.py
```

## 🔧 Desenvolvimento

### Adicionando Novos Jogos

1. Crie uma nova pasta em `games/`
2. Implemente a classe base `GamePlugin`
3. Adicione assets e configurações
4. Registre o jogo no `game_manager.py`

```python
from core.base import GamePlugin

class NewGame(GamePlugin):
    def __init__(self):
        super().__init__(
            name="Novo Jogo",
            version="1.0.0",
            author="Seu Nome"
        )
```

### API REST

- `GET /api/games` - Lista jogos disponíveis
- `GET /api/scores` - Ranking global
- `POST /api/scores` - Registra nova pontuação
- `GET /api/players` - Lista jogadores online

## 📈 Versão

Versão atual: 1.0.0

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/NovoJogo`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo jogo'`)
4. Push para a branch (`git push origin feature/NovoJogo`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
