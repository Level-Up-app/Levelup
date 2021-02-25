from flask import Flask
from app import init_app
from config import Config


app = init_app()

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
