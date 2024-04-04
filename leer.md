	# Análisis de Contratos de Compra-Venta con GPT-3

## Descripción General

Este repositorio alberga scripts en Python para el análisis de contratos de compra-venta de bienes raíces con GPT-3 de OpenAI, diseñados para extraer información crucial como nombres, números de identificación, roles en el contrato, cantidades y monedas involucradas. Dada la sensibilidad de los datos personales, el proyecto emplea ejemplos ficticios para el afinado fino del modelo, aunque ha analizado más de 100,000 contratos reales de compra y venta de los últimos cinco años.

## Contenidos

- `pdf_to_txt.py`: Convierte documentos PDF en archivos de texto para análisis.
- `prepare_fine_tuning.py`: Prepara y sube los datos para el afinado fino del modelo GPT-3.
- `fine_tuning.py`: Inicia el proceso de afinado fino con OpenAI.
- `model_pdf_gpt.py`: Analiza el texto de los contratos para extraer información estructurada.

## Uso

1. Instala las dependencias con `pip install -r requirements.txt`.
2. Coloca los PDFs de los contratos en el directorio especificado.
3. Ejecuta los scripts en el orden indicado.
4. Consulta la información extraída en el archivo CSV generado.

## JSONL para el Fine-Tuning

Se incluye el archivo `.JSONL` necesario para el afinado fino del modelo con ejemplos de datos ficticios, reflejando el enfoque de análisis para más de 100,000 contratos reales durante los últimos cinco años, respetando las preocupaciones sobre la privacidad de datos.

## Nota de Seguridad

Las claves API y los datos sensibles se manejan de forma segura, asumiendo prácticas responsables de gestión de datos.

## Descargo de Responsabilidad

Esta herramienta es para fines de investigación e información, asegurando que el manejo de datos cumpla con las leyes y regulaciones de privacidad.
