# 📊 Scraping de Tablas de Wikipedia con Python

Este proyecto contiene 3 scripts en Python que permiten extraer automáticamente tablas de Wikipedia, en especial del artículo del **Torneo Apertura 2025 (Colombia)**, usando:

- `Selenium`: para cargar la página dinámicamente.
- `pandas.read_html()`: para extraer las tablas completas.
- `StringIO`: para procesar el HTML como archivo.
- `Excel`: como formato de salida de datos.

---

## 📁 Archivos incluidos

- `extraccion_tablas_wikipedia.py`: contiene 3 versiones de código para extraer las tablas.
- `requirements.txt`: lista de librerías necesarias.

---

## ✅ Qué hace cada código

### 1. Extrae **todas** las tablas de Wikipedia y muestra sus contenidos
```python
pd.read_html(StringIO(driver.page_source))
