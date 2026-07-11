import numpy as np
import matplotlib.pyplot as plt

with open("Alturas.csv", "r", encoding="utf-8") as archivo:
    lectura_archivo = archivo.readlines()

    alturas_hombres = []
    alturas_mujeres = []
    alturas_totales = []

    for datos in lectura_archivo:
        datos_corregidos = datos.strip().split(",")

        alturas = datos_corregidos[1]
        genero = datos_corregidos[2].replace('"', '')

        if genero == "Hombre":
            alturas_hombres.append(float(alturas))
            alturas_totales.append(float(alturas))
        elif genero == "Mujer":
            alturas_mujeres.append(float(alturas))
            alturas_totales.append(float(alturas))

matriz_hombres = np.array(alturas_hombres)
matriz_mujeres = np.array(alturas_mujeres)
matriz_alturas = np.array(alturas_totales)

promedio_hombres = np.mean(matriz_hombres)
promedio_mujeres = np.mean(matriz_mujeres)
promedio_general = np.mean(matriz_alturas)

nombres = []
for i in range(len(matriz_alturas)):
    nombres.append(f"{i+1}")

print(f"Promedio de altura de hombres: {promedio_hombres:.2f} cm")
print(f"Promedio de altura de mujeres: {promedio_mujeres:.2f} cm")

plt.subplot(2, 1, 1)
plt.gcf().set_facecolor("#DCDCDC")
plt.title("Alturas en Santiago de Chile")
plt.bar(nombres, matriz_alturas, color="#4e79a7")
plt.xticks([])
plt.ylim(150, 200)

plt.subplot(2, 1, 2)
plt.gcf().set_facecolor("#DCDCDC")
plt.title("Promedio de Alturas")
plt.ylabel("Altura en centimetros")
plt.bar(["Hombre", "Mujer"], [promedio_hombres, promedio_mujeres], color=["#4e79a7", "#f28e2b"])
plt.ylim(150, 180)
plt.show()
