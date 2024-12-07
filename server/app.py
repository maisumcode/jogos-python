from flask import Flask, render_template, jsonify
import socket
import webbrowser
from contextlib import closing
import logging
import os
import time

app = Flask(__name__, 
    template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
    static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
)

def find_free_port():
    """Encontra uma porta livre no sistema"""
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(('127.0.0.1', 0))
            s.listen(1)
            port = s.getsockname()[1]
            return port
    except Exception as e:
        print(f"Erro ao encontrar porta livre: {e}")
        return 5000  # Porta padrão caso ocorra erro

def get_local_ip():
    """Obtém o IP local da máquina"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html', games=[
        {
            "id": "snake",
            "name": "Snake",
            "description": "Jogo da cobrinha clássico",
        },
        {
            "id": "tetris",
            "name": "Tetris",
            "description": "Tetris clássico",
        }
    ])

@app.route('/api/games')
def list_games():
    """Lista os jogos disponíveis"""
    games = [
        {
            "id": "snake",
            "name": "Snake",
            "description": "Jogo da cobrinha clássico"
        },
        {
            "id": "tetris",
            "name": "Tetris",
            "description": "Tetris clássico"
        }
    ]
    return jsonify(games)

@app.route('/api/scores')
def get_scores():
    """Retorna o ranking global"""
    # TODO: Implementar integração com banco de dados
    scores = [
        {"player": "Player1", "game": "snake", "score": 100},
        {"player": "Player2", "game": "tetris", "score": 1000}
    ]
    return jsonify(scores)

@app.route('/snake')
def snake_game():
    """Página do jogo Snake"""
    return render_template('snake.html')

@app.route('/tetris')
def tetris_game():
    """Página do jogo Tetris"""
    return render_template('tetris.html')

@app.route('/play/<game_id>', methods=['POST'])
def play_game(game_id):
    """Inicia um jogo específico"""
    try:
        if game_id == 'snake':
            return jsonify({"success": True, "redirect": "/snake"})
        elif game_id == 'tetris':
            return jsonify({"success": True, "redirect": "/tetris"})
        else:
            return jsonify({"success": False, "error": "Jogo não encontrado"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

def start_server():
    """Inicia o servidor com porta dinâmica e abre o navegador"""
    try:
        port = find_free_port()
        local_ip = get_local_ip()
        hostname = socket.gethostname()

        print("\n🎮 Plataforma de Jogos Python")
        print("\nIniciando servidor...")
        
        # Configurar logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger('werkzeug')
        logger.setLevel(logging.INFO)

        # Esperar um pouco antes de abrir o navegador
        def open_browser():
            time.sleep(1)  # Reduzido para 1 segundo
            webbrowser.open(f'http://127.0.0.1:{port}')

        # Iniciar o navegador em uma thread separada
        from threading import Timer
        Timer(0.5, open_browser).start()

        print("\nServidor iniciado em:")
        print(f"- Local: http://127.0.0.1:{port}")
        print(f"- Rede Local: http://{local_ip}:{port}")
        print(f"- Nome Amigável: http://{hostname}.local:{port}")
        
        # Iniciar servidor com reloader manual
        app.run(host='127.0.0.1', port=port, debug=True, use_reloader=False)

    except Exception as e:
        print(f"\n❌ Erro ao iniciar o servidor: {e}")
        print("\nTentando iniciar em configuração alternativa...")
        try:
            app.run(host='127.0.0.1', port=5000, debug=False)
        except Exception as e2:
            print(f"\n❌ Erro fatal ao iniciar o servidor: {e2}")
            print("Por favor, verifique se não há outro servidor rodando e tente novamente.")

if __name__ == '__main__':
    start_server() 