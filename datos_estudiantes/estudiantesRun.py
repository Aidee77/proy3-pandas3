# importar la libreria pandas
import pandas as pd

# 1. Leer datos desde el archivo CSV
# df=variable data frame tabla
df = pd.read_csv("estudiantes.csv")

# 2. Mostrar la tabla completa
print("** Tabla completa***")
print(df)