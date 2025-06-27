<h1 align="center">SCARLET SCRAPER  "trash hacking" 🤡</h1>
<p align="center">
  <img src="https://www.meme-arsenal.com/memes/bd536d4123e64d0bd263642ffd5c59a4.jpg"> 
  
</p>
<p align="left">
  <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green"> 
</p>
:construction: Proyecto en construcción :construction:


# 🕸️ Scarlet Scraper

Este proyecto es una herramienta desarrollada en Python que permite **explorar, extraer URLs internas, localizar datos tipo: pdf, word, excel, etc** de un sitio web de forma eficiente.
## 🚀 Características principales

- Utiliza múltiples tareas concurrentes para explorar sitios rápidamente.
- Extrae y muestra URLs válidas pertenecientes al mismo dominio.
- Detecta si una URL pertenece a un **subdominio** del objetivo.
- Muestra el estado de cada URL (válida o no encontrada).
- Presenta una **interfaz en consola** con colores para facilitar la lectura.
- Incluye una animación tipo **banner con barra de carga** al inicio.
- Localiza archivos de tipo texto: pdf, word, etc.

## 📁 Estructura del Proyecto

- `asyncio` y `aiohttp` para la gestión de tareas concurrentes.
- `BeautifulSoup` para el análisis del contenido HTML.
- `deque` para manejar la cola de URLs pendientes por procesar.
- `urljoin` y `urlparse` para reconstruir y validar URLs.

## 💡 ¿Cómo funciona?

1. El usuario ingresa una URL base.
2. El crawler comienza a explorar dicha URL y las que se encuentren dentro de su mismo dominio.
3. Cada página es descargada y analizada para encontrar nuevos enlaces.
4. Las URLs válidas se almacenan y se muestran con indicadores visuales:
   - ✅ Verde: URL válida del mismo dominio.
   - 🔵 Azul: Subdominio.
   - ❌ Rojo: URL inválida o con error HTTP (ej. 404).
5. El proceso continúa hasta agotar las URLs encontradas.

## 📦 Requisitos

Antes de ejecutar el script, asegúrate de instalar las dependencias:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
aiohttp
beautifulsoup4
```

## ▶️ Ejecución

```bash
**Ejecución en Windows:**

  1. pip install -r requirements.txt
  2. python scarlet_v2.py
```
```
**Ejecución en Linux:** 

  1. python3 -m venv venv
  2. source venv/bin/activate
  3. pip install -r requirements.txt
  4. python3 scarlet_v2.py
```



> Al iniciar, se mostrará un banner animado. Luego, se te pedirá que ingreses la URL objetivo (por ejemplo: `https://ejemplo.com`).

## 🧑‍💻 Autor

**Bot-Collab**  
Pentester Ético | Desarrollador Python

## 🛡️ Uso Ético

> Esta herramienta ha sido creada con fines educativos y de auditoría ética. **No debe utilizarse sin el permiso del propietario del sitio web**. El uso indebido es responsabilidad del usuario.
