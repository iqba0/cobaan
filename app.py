from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask sudah jalan di cPanel! 🎉'

if __name__ == '__main__':
    app.run()
