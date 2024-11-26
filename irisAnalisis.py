# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Evrt3M2iwy18Y6_k2aDTwxkrkll0LBvg

# PROYECTO 1 DE DATA SCIENCE - ENFOCADO EN APLICAR ANÁLISIS EXPLORATORIO DE DATOS

# DATASET IRIS

El dataset Iris, introducido por Ronald Fisher en 1936, es un clásico conjunto de datos multiclase usado para tareas de clasificación.

Contiene 150 muestras de tres especies de flores (Iris setosa, Iris virginica e Iris versicolor), con cuatro características:

   1. longitud de sépalos
   2. anchura de sépalos
   3. Longitud de pétalos
   4. Anchura de pétalos

## Objetivo

El objetivo principal es construir un modelo que, usando estas características, clasifique correctamente las especies de flores con la mayor precisión posible.

# 1. INICIALIZACIÓN

## 1.1. IMPORTS
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

"""## 1.2. AJUSTES INICIALES"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

plt.style.use('bmh')
sns.set(style='whitegrid')

"""# 2. CARGA Y PREPROCESAMIENTO DEL DATASET

## 2.1. LECTURA DE DATOS
"""

df = pd.read_csv('Iris.csv')

print(df)

"""## 2.2. PREPROCESAMIENTO"""

df.rename({'SepalLengthCm':'sep_l',
           'SepalWidthCm':'sep_a',
           'PetalLengthCm':'pet_l',
           'PetalWidthCm':'pet_a',
           'Species':'especie'},
          axis=1, inplace=True)

"""#  3. LIMPIEZA DE DATOS"""

df.drop('Id', axis=1, inplace=True)
df.head(7)

"""# 4. ANÁLISIS DESCRIPTIVO"""

df.head(8)

"""### DIMENSIONES DEL DATASET"""

df.shape

"""### INFORMACIÓN GENERAL DEL DATASET"""

df.info()

df.describe()

"""### RECUENTO DE LA VARIABLE A PREDECIR"""

df['especie'].value_counts()

couns = df['especie'].value_counts()
sns.countplot (data= df, x='especie', palette='pastel')

"""### COMPROBACIÓN DE VARIABLES NULAS"""

df.isnull().sum(axis=0)

"""# 5. ANÁLISIS UNIVARIANTE

## 5.1. LONGITUD DEL SÉPALO
"""

# 1. Histograma con KDE
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.histplot(df['sep_l'], kde=True, bins=20, color='purple')
plt.title('Histograma con KDE - Longitud del sépalo')
plt.xlabel('Longitud del sépalo (cm)')
plt.ylabel('Frecuencia')

# 2. Boxplot
plt.subplot(1, 3, 2)
sns.boxplot(y=df['sep_l'], color='lightgreen')
plt.title('Boxplot - Longitud del sépalo')
plt.xlabel('Longitud del sépalo (cm)')
plt.ylabel('')

# 3. Violin plot
plt.subplot(1, 3, 3)
sns.violinplot(y=df['sep_l'], color='lightblue')
plt.title('Violin plot - Longitud del sépalo')
plt.xlabel('Longitud del sépalo (cm)')
plt.ylabel('')

# Mostrar los gráficos
plt.tight_layout()
plt.show()

"""## 5.2. ANCHO DEL SÉPALO"""

# 1. Histograma con KDE
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.histplot(df['sep_a'], kde=True, bins=20, color='purple')
plt.title('Histograma con KDE - Ancho del sépalo')
plt.xlabel('Ancho del sépalo (cm)')
plt.ylabel('Frecuencia')

# 2. Boxplot
plt.subplot(1, 3, 2)
sns.boxplot(y=df['sep_a'], color='lightgreen')
plt.title('Boxplot - Ancho del sépalo')
plt.xlabel('Ancho del sépalo (cm)')
plt.ylabel('')

# 3. Violin plot
plt.subplot(1, 3, 3)
sns.violinplot(y=df['sep_a'], color='lightblue')
plt.title('Violin plot - Ancho del sépalo')
plt.xlabel('Ancho del sépalo (cm)')
plt.ylabel('')

# Mostrar los gráficos
plt.tight_layout()
plt.show()

"""## 5.3. LONGITUD DEL PÉTALO"""

# 1. Histograma con KDE
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.histplot(df['pet_l'], kde=True, bins=20, color='purple')
plt.title('Histograma con KDE - Longitud del pétalo')
plt.xlabel('Longitud del pétalo (cm)')
plt.ylabel('Frecuencia')

# 2. Boxplot
plt.subplot(1, 3, 2)
sns.boxplot(y=df['pet_l'], color='lightgreen')
plt.title('Boxplot - Longitud del pétalo')
plt.xlabel('Longitud del pétalo (cm)')
plt.ylabel('')

# 3. Violin plot
plt.subplot(1, 3, 3)
sns.violinplot(y=df['pet_l'], color='lightblue')
plt.title('Violin plot - Longitud del pétalo')
plt.xlabel('Longitud del pétalo (cm)')
plt.ylabel('')

# Mostrar los gráficos
plt.tight_layout()
plt.show()

"""## 5.4. ANCHO DEL PÉTALO"""

# 1. Histograma con KDE
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.histplot(df['sep_a'], kde=True, bins=20, color='purple')
plt.title('Histograma con KDE - Ancho del pétalo')
plt.xlabel('Ancho del pétalo (cm)')
plt.ylabel('Frecuencia')

# 2. Boxplot
plt.subplot(1, 3, 2)
sns.boxplot(y=df['sep_a'], color='lightgreen')
plt.title('Boxplot - Ancho del pétalo')
plt.xlabel('Ancho del pétalo (cm)')
plt.ylabel('')

# 3. Violin plot
plt.subplot(1, 3, 3)
sns.violinplot(y=df['sep_a'], color='lightblue')
plt.title('Violin plot - Ancho del pétalo')
plt.xlabel('Ancho del pétalo (cm)')
plt.ylabel('')

# Mostrar los gráficos
plt.tight_layout()
plt.show()

"""# 6. ANÁLISIS MULTIVARIANTE

## 6.1. LONGITUD DE SÉPALO Y ESPECIE
"""

# Crear una figura con una cuadrícula de 2x2 subgráficos
fig, axs = plt.subplots(2, 2, figsize=(14, 12))

# 1. Histograma de Longitud del Sépalo por Especie
sns.histplot(data=df, x='sep_l', hue='especie', multiple='stack', palette='Set1', bins=20, ax=axs[0, 0])
axs[0, 0].set_title('Histograma de Longitud del Sépalo por Especie')
axs[0, 0].set_xlabel('Longitud del Sépalo (cm)')
axs[0, 0].set_ylabel('Frecuencia')

# 2. Diagrama de Caja (Boxplot) de Longitud del Sépalo por Especie
sns.boxplot(data=df, x='especie', y='sep_l', palette='Set1', ax=axs[0, 1])
axs[0, 1].set_title('Diagrama de Caja de Longitud del Sépalo por Especie')
axs[0, 1].set_xlabel('Especie')
axs[0, 1].set_ylabel('Longitud del Sépalo (cm)')

# 3. Gráfico de Violín de Longitud del Sépalo por Especie
sns.violinplot(data=df, x='especie', y='sep_l', palette='Set1', ax=axs[1, 0])
axs[1, 0].set_title('Gráfico de Violín de Longitud del Sépalo por Especie')
axs[1, 0].set_xlabel('Especie')
axs[1, 0].set_ylabel('Longitud del Sépalo (cm)')

# 4. Gráfico de Dispersión (Scatter Plot) de Longitud del Sépalo por Especie
sns.scatterplot(data=df, x='sep_l', y='pet_l', hue='especie', palette='Set1', style='especie', ax=axs[1, 1])
axs[1, 1].set_title('Gráfico de Dispersión de Longitud del Sépalo y Longitud del Pétalo por Especie')
axs[1, 1].set_xlabel('Longitud del Sépalo (cm)')
axs[1, 1].set_ylabel('Longitud del Pétalo (cm)')
axs[1, 1].legend(title='Especie')

# Ajustar el espacio entre subgráficos
plt.tight_layout()
plt.show()

"""## 6.2. ANCHO DEL SÉPALO Y ESPECIE"""

# Crear una figura con una cuadrícula de 2x2 subgráficos
fig, axs = plt.subplots(2, 2, figsize=(14, 12))

# 1. Histograma de Ancho del Sépalo por Especie
sns.histplot(data=df, x='sep_a', hue='especie', multiple='stack', palette='Set1', bins=20, ax=axs[0, 0])
axs[0, 0].set_title('Histograma de Ancho del Sépalo por Especie')
axs[0, 0].set_xlabel('Ancho del Sépalo (cm)')
axs[0, 0].set_ylabel('Frecuencia')

# 2. Diagrama de Caja (Boxplot) de Ancho del Sépalo por Especie
sns.boxplot(data=df, x='especie', y='sep_a', palette='Set1', ax=axs[0, 1])
axs[0, 1].set_title('Diagrama de Caja de Ancho del Sépalo por Especie')
axs[0, 1].set_xlabel('Especie')
axs[0, 1].set_ylabel('Ancho del Sépalo (cm)')

# 3. Gráfico de Violín de Ancho del Sépalo por Especie
sns.violinplot(data=df, x='especie', y='sep_a', palette='Set1', ax=axs[1, 0])
axs[1, 0].set_title('Gráfico de Violín de Ancho del Sépalo por Especie')
axs[1, 0].set_xlabel('Especie')
axs[1, 0].set_ylabel('Ancho del Sépalo (cm)')

# 4. Gráfico de Dispersión (Scatter Plot) de Ancho del Sépalo por Especie
sns.scatterplot(data=df, x='sep_a', y='pet_a', hue='especie', palette='Set1', style='especie', ax=axs[1, 1])
axs[1, 1].set_title('Gráfico de Dispersión de Ancho del Sépalo y Ancho del Pétalo por Especie')
axs[1, 1].set_xlabel('Ancho del Sépalo (cm)')
axs[1, 1].set_ylabel('Ancho del Pétalo (cm)')
axs[1, 1].legend(title='Especie')

# Ajustar el espacio entre subgráficos
plt.tight_layout()
plt.show()

"""## 6.3. RELACIÓN ENTRE TODAS LAS VARIABLES"""

# Pairplot: muestra la relación entre todas las variables
sns.pairplot(df, hue='especie', markers=["o", "s", "D"], palette="Set1")
plt.suptitle('Pairplot de las variables de Iris', y=1.02)
plt.show()

"""## 6.4. CORRELACIÓN ENTRE VARIABLES"""

# Calculate the correlation matrix only for numerical columns
numerical_columns = ['sep_l', 'sep_a', 'pet_l', 'pet_a']  # List of your numerical columns
correlation_matrix = df[numerical_columns].corr()

# Display the correlation matrix
print(correlation_matrix)

# 2. Heatmap de la correlación entre variables
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Mapa de calor de correlación entre variables')
plt.show()

"""## 6.5. RELACIÓN ENTRE 3 VARIABLES"""

# 3. Scatterplot 3D: mostrar la relación entre 3 variables
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Crear scatterplot 3D usando 3 dimensiones: longitud del sépalo, longitud del pétalo y ancho del pétalo
scatter = ax.scatter(
    df['sep_l'],
    df['pet_l'],
    df['pet_a'],
    c=pd.Categorical(df['especie']).codes,
    cmap='Set1'
)

# Etiquetas
ax.set_xlabel('Longitud del Sépalo (cm)')
ax.set_ylabel('Longitud del Pétalo (cm)')
ax.set_zlabel('Ancho del Pétalo (cm)')
plt.title('Scatterplot 3D - Longitud y ancho del sépalo y pétalo')

# Mostrar gráfico
plt.show()

"""# 7. CONCLUSIONES DEL ANÁLISIS

*   El dataset IRIS se encontraba muy balanceado, sin valores nulos y con la misma cantidad de datos para cada especie.
*   Al realizar el análisis univariante podemos observar que la longitud del sépalo se encuentran con valores esparcidos, permitiendo ser una variable diferenciadora para la clasificación.
*   Al realizar el análisis multivariante podemos observar una diferencia entre las longitudes del sépalo según el tipo de planta, volviendo a confirmar que la variable que se debería utilizar para la clasificación es la longitud del sépalo.
*   Verificando la correlación entre las variables se pudo notar una correlación positiva entre la longitud del sépalo y el pétalo y la longitud del pétalo y el ancho del pétalo, siendo variables a considerar.

# 8. MODELO PREDICTIVO

## 8.1. ENTRENAMIENTO DEL MODELO
"""

# Separar características (X) y etiquetas (y)
X = df.drop(columns=['especie'])
y = df['especie']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

"""## 8.2. EVALUACIÓN DEL MODELO"""

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

"""## 8.3. PRUEBA DE LA PREDICCIÓN"""

nuevos_datos = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=X.columns)
prediccion = model.predict(nuevos_datos)
print(prediccion)

import joblib

# Guardar el modelo
joblib.dump(model, 'modelo_rf.pkl')