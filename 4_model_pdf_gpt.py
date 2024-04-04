import os
import openai
import csv
# Redundant import, "from openai import OpenAI" is unnecessary.
# from openai import OpenAI
import time

# API key for OpenAI; best practice is to use environment variables for security.
api_key = 'sk-......'
client = openai.OpenAI(api_key=api_key)

# Instructions for GPT to follow, detailing what information to extract from the contract.
content_instrucciones = """
identificando nombres, DNI, roles en el contrato, montos y monedas involucradas,
indicación si la persona recibe o paga, la fecha del contrato, dirección, número de partida y
oficina registral. Si algún campo no está disponible, se debe usar un asterisco (*). La salida debe ser lineal,
con una línea por persona y cada campo separado por | . La dirección, número de partida y oficina registral
son iguales para todas las personas involucradas.
"""

# Directory where the text files are stored.
directorio = '/Users/renzo/Downloads/folder_test'

# CSV file to save the results.
archivo_csv = '/Users/renzo/Downloads/folder_test/resultado2.csv'

# Listing all files in the specified directory that are files (not directories).
archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
tiempo_inicio = time.time()

# Open the CSV file for writing the extracted information.
with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
    escritor_csv = csv.writer(file, delimiter='|')
    
    for archivo in archivos:
        ruta_completa = os.path.join(directorio, archivo)
        
        # Process only text files.
        if ruta_completa.endswith('.txt'):
            with open(ruta_completa, 'r', encoding='utf-8') as file:
                contenido_archivo = file.read()
            
            # Use GPT model to generate completions based on the contract text.
            completion = client.chat.completions.create(
                model="ft:gpt-3.5-turbo-1106:infocore::8ndE5stm",
                messages=[
                    {"role": "system", "content": content_instrucciones},
                    {"role": "user", "content": contenido_archivo}
                ]
            )
            
            # Split the response by new lines and write each to the CSV.
            lineas = completion.choices[0].message.content.split('\n')
            for linea in lineas:
                escritor_csv.writerow([archivo, linea])

# Calculate and print the total processing time.
tiempo_fin = time.time()
print(f"Total processing time: {tiempo_fin - tiempo_inicio} seconds.")
