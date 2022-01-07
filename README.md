# Extraer seguidores de instagram

Este scraper está programado en python y utiliza el webdriver de chrome para autenticarse en instagram. De esta manera puede consultar un perfil y extraer el nombre de usuario de todas las cuentas que lo siguen.

## 1. `pip install -r requirement.txt`

## 2. duplicar el archivo `.env.example` y cambiarle el nombre a `.env`

## 3. Configurar variables de entorno (`.env`)

```prooperties
IG_USERNAME=
IG_PASSWORD=
DRIVER_PATH=
```

## 4. Descargar chromedriver

Asegurate de elegir la misma versión que tu navegador Google Chrome
https://chromedriver.chromium.org/downloads

## 5. `python3 main.py`

Te pedirá por consola el username de alguna cuenta para extraer la lista de seguidores
`IMPORTANTE`
La cuenta debe ser pública. Si es privada es necesario que te haya aceptado como seguidor

## LISTO

cuando finalize de scrollear la lista de seguidores, fijate en la consola se va a imprimir un array con todos los username.
