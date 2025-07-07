"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    ruta = "files/input/clusters_report.txt"
    lineas = open(ruta, encoding="utf-8").read().splitlines()[4:]     #descartar encabezado
    
    registros = []
    trozo = []

    for linea in lineas + ['']: #'' para procesar última línea
        if linea.strip():
            trozo.append(linea.strip())
        else:
            if trozo:
                bloque = " ".join(trozo)
                partes = bloque.split()
                
                num_cluster = int(partes[0])
                cantidad = int(partes[1])
                porcentaje = float(partes[2].replace(',', '.'))
                

                texto_claves = " ".join(partes[4:])
                texto_claves = " ".join(texto_claves.split())
                if texto_claves.endswith('.'):
                    texto_claves = texto_claves[:-1]
                texto_claves = texto_claves.replace(' ,', ',')
                
                registros.append({
                    'cluster': num_cluster,
                    'cantidad_de_palabras_clave': cantidad,
                    'porcentaje_de_palabras_clave': porcentaje,
                    'principales_palabras_clave': texto_claves
                })
                trozo = []
    
    df_clusters = pd.DataFrame(registros)
    return df_clusters

print(pregunta_01())