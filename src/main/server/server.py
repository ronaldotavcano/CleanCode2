from flask import Flask
from src.main.routes.users_route import user_routes_bp

app = Flask(__name__)

# Adiciona todas as rotas que começarem com @user_routes_bp (Usuários)
app.register_blueprint(user_routes_bp)