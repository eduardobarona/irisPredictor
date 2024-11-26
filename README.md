# Análisis y Predicción del Iris Dataset con Flask y Frontend en HTML

Este repositorio contiene un análisis completo del **Iris Dataset**, realizado en un **notebook de Google Colab**, junto con un modelo de predicción basado en **Decision Tree**, y una implementación de la aplicación web que permite interactuar con el modelo de manera fácil.

## Descripción del Proyecto

El objetivo de este proyecto es analizar el **Iris Dataset**, entrenar un modelo de predicción utilizando **Decision Tree** y crear una aplicación web que permita hacer predicciones sobre el tipo de especie de Iris basándose en las características de las flores (longitud y ancho del sépalo y pétalo). El modelo se desplegó utilizando un backend en **Flask** y una interfaz de usuario en **HTML, CSS, y JavaScript**. La página web permite al usuario ingresar las medidas de una flor de Iris y obtener la predicción de la especie, mostrando además una imagen representativa de la especie predicha.

![prediccionIris](https://github.com/user-attachments/assets/b14ae863-23b2-4597-b182-0647e71bed75) 

## Estructura del Proyecto

El repositorio está dividido en los siguientes componentes:

1. **Backend (Flask)**:  
   - `app.py`: Contiene la lógica del servidor Flask, donde se carga el modelo de predicción, se configuran las rutas de la API y se gestionan las predicciones.
   - `modelo_rf.pkl`: El modelo de predicción entrenado con Decision Tree, guardado en formato `pkl` para su carga y reutilización en el backend.

2. **Frontend (HTML, CSS, JavaScript)**:
   - `index.html`: Contiene el formulario donde el usuario puede ingresar las características de la flor de Iris. Después de la predicción, se muestra el resultado junto con una imagen correspondiente a la especie predicha.
   - `style.css`: El archivo de estilos para la interfaz de usuario, con un diseño limpio y sencillo.

3. **Análisis (Google Colab)**:
   - `Iris_Analysis.ipynb`: El notebook de Google Colab donde se realiza todo el análisis del Iris Dataset. Aquí se entrenó el modelo de predicción utilizando **Decision Tree**, se evaluaron diferentes métricas y se generaron las visualizaciones.

## Pasos para Ejecutar el Proyecto

### 1. **Preparación del Backend (Flask)**

1. Clona este repositorio:
   git clone https://github.com/tu-usuario/iris-prediction-app.git
   cd iris-prediction-app

2. Crea un entorno virtual e instala las dependencias:

    python3 -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate     # Para Windows
    pip install -r requirements.txt
    Asegúrate de tener el archivo del modelo modelo_rf.pkl en la misma carpeta que app.py.

3. Ejecuta el servidor Flask:

    python app.py
    El servidor Flask estará corriendo en http://localhost:5000.

### 2. Preparación del Frontend
El frontend ya está listo para ser servido como archivos estáticos. Si estás ejecutando el servidor Flask localmente, solo necesitas asegurarte de que el archivo index.html esté accesible desde la carpeta raíz de tu proyecto o desde un servidor web.

1. Abre el archivo index.html en tu navegador o configúralo en un servidor (por ejemplo, Netlify o GitHub Pages).

2. Conecta el frontend con el backend asegurándote de que la URL de la API en el archivo JavaScript apunte a la URL correcta de tu servidor Flask:

    const response = await fetch('http://localhost:5000/predict', { ... });

3. Despliegue en Producción

Backend:
Puedes desplegar el backend utilizando plataformas como Heroku o AWS.
Si usas Heroku, asegúrate de seguir los pasos de despliegue de una aplicación Flask en Heroku.

Frontend:
El frontend está listo para ser desplegado en plataformas como Netlify o GitHub Pages.
Si usas Netlify, sigue los pasos para conectar tu repositorio de GitHub y hacer el despliegue de tu aplicación estática.

4. Interacción con la Aplicación Web

Formulario de Entrada:
Los usuarios pueden ingresar las características de la flor de Iris (longitud y ancho del sépalo y pétalo).

Predicción:
Al enviar el formulario, la aplicación hará una llamada a la API del backend, donde el modelo de Decision Tree predice la especie de Iris (Setosa, Versicolor o Virginica).

Resultado:
Se muestra el nombre de la especie predicha y una imagen correspondiente a la especie.

## Dependencias
Este proyecto usa las siguientes librerías:

- Flask: Para crear el backend y manejar las peticiones HTTP.
- Flask-CORS: Para habilitar las peticiones CORS desde el frontend.
- Joblib: Para cargar el modelo de predicción.
- Numpy: Para procesar las características de entrada y manipular matrices.
- Pandas: Usado en el análisis de datos (no se utiliza directamente en el backend).

Para instalar las dependencias:

    pip install -r requirements.txt

## Análisis en Google Colab

El análisis realizado en Google Colab se encuentra en el archivo Iris_Analysis.ipynb, que contiene:

- Carga y exploración del dataset.
- Análisis exploratorio de los datos (EDA).
- Entrenamiento y evaluación del modelo de Decision Tree.
- Visualizaciones para comprender mejor las relaciones entre las características de las flores.

## Imágenes
Asegúrate de tener las siguientes imágenes en tu carpeta de proyecto:

- setosaIris.jpg: Imagen representativa de la especie Setosa.
- versicolorIris.jpeg: Imagen representativa de la especie Versicolor.
- virginicaIris.jpg: Imagen representativa de la especie Virginica.

## Licencia
Este proyecto está bajo la licencia MIT. 
