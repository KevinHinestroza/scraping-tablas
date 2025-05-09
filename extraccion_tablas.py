# === [CÓDIGO 1] Extraer la tabla número 9 desde Wikipedia y guardar en Excel ===

from selenium import webdriver
import pandas as pd
from io import StringIO
import time

driver = webdriver.Chrome()
url = "https://es.wikipedia.org/wiki/Torneo_Apertura_2025_(Colombia)"
driver.get(url)
time.sleep(3)

html = driver.page_source
driver.quit()

html_io = StringIO(html)
tablas = pd.read_html(html_io)

# Guardar la tabla 9 (índice 9)
tabla_9 = tablas[9]
tabla_9.to_excel("tabla_wikipedia_numero_9.xlsx", index=False)

print("✅ ¡Tabla 9 extraída y guardada exitosamente!")


# === [CÓDIGO 2] Leer todas las tablas con pandas.read_html() + StringIO ===

driver = webdriver.Chrome()
driver.get("https://es.wikipedia.org/wiki/Torneo_Apertura_2025_(Colombia)")
time.sleep(3)

html = driver.page_source
driver.quit()

html_io = StringIO(html)
tablas = pd.read_html(html_io)

# Mostrar las tablas para inspección
for i, t in enumerate(tablas):
    print(f"TABLA {i}:\n", t.head(), "\n")


# === [CÓDIGO 3] Extraer la tabla manualmente con Selenium (fila por fila) ===

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://es.wikipedia.org/wiki/Torneo_Apertura_2025_(Colombia)"
driver.get(url)
time.sleep(3)

tabla = driver.find_element(By.CLASS_NAME, "wikitable")
filas = tabla.find_elements(By.TAG_NAME, "tr")[1:]

posiciones, equipos, puntos = [], [], []

for fila in filas:
    columnas = fila.find_elements(By.TAG_NAME, "td")
    if len(columnas) >= 3:
        posiciones.append(columnas[0].text.strip())
        equipos.append(columnas[1].text.strip())
        puntos.append(columnas[2].text.strip())

df = pd.DataFrame({
    "Posición": posiciones,
    "Equipo": equipos,
    "Puntos": puntos
})
df.to_excel("tabla_de_puntos.xlsx", index=False)

driver.quit()
print("✅ ¡Tabla extraída manualmente y guardada!")
