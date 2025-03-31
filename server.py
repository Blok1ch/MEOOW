from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    print("Открыли страницу")  # Для проверки
    return send_file('index.html')

@app.route('/api/pages')
def get_pages():
    image_folder = "manga_photos"  # Имя твоей папки с фотками
    if not os.path.exists(image_folder):
        print(f"Папки {image_folder} нет!")
        return jsonify({"title": "Ошибка", "pages": []})
    images = [f"/images/{f}" for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    print("Нашёл фотки:", images)  # Для проверки
    return jsonify({"title": "Моя манга", "pages": images})

@app.route('/images/<filename>')
def serve_image(filename):
    print(f"Показываю фотку: {filename}")  # Для проверки
    return send_file(f"manga_photos/{filename}")  # Путь к твоей папке

if __name__ == "__main__":
    app.run(port=3000)