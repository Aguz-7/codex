# Aplicación de Checklist para Diagnóstico de Celulares

Esta aplicación permite verificar de forma rápida el funcionamiento de distintos componentes de un teléfono móvil. Al finalizar la revisión se genera automáticamente un informe en formato **TXT** y **PDF** con los resultados.

## Requisitos
- Python 3.11 o superior
- La biblioteca [fpdf](https://pypi.org/project/fpdf/) para generar el PDF

Puede instalar la dependencia con:
```bash
pip install fpdf
```

## Uso
Ejecute el script desde una terminal:
```bash
python phone_checklist.py
```
Se abrirá una ventana donde podrá ingresar el modelo de celular y registrar si cada función **Funciona** o presenta **Falla**. Tras presionar **Generar informe** se crean dos archivos en el mismo directorio con la fecha actual en el nombre.
