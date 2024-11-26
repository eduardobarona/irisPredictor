from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

# Cargar el modelo
model = joblib.load('modelo_rf.pkl')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Bienvenido a la página de predicción Iris'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)  # Obtener los datos enviados en formato JSON
        features = np.array(data['features']).reshape(1, -1)  # Procesar las características
        
        # Realizar la predicción
        prediction = model.predict(features)

        # Dependiendo de la predicción, asignamos una imagen y un nombre en español
        if prediction[0] == 'Iris-setosa':
            especie = "Setosa"
            image_url = "setosaIris.jpg"  # Aquí pones la URL de la imagen de la clase 0 (Setosa)
        elif prediction[0] == 'Iris-versicolor':
            especie = "Versicolor"
            image_url = "versicolorIris.jpeg"  # URL de la imagen para la clase 1 (Versicolor)
        else:
            especie = "Virginica"
            image_url = "virginicaIris.jpg"  # URL para la clase 2 (Virginica)
        
        return jsonify({'prediccion': especie, 'imagen': image_url})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

print("Clases del modelo:", model.classes_)
