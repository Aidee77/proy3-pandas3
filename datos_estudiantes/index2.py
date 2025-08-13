# importar la libreria pandas
import pandas as pd

# 1. Leer datos desde el archivo CSV
df = pd.read_csv("estudiantes.csv")

# 2. Mostrar la tabla completa
print("** Tabla completa ***")
print(df)

# 3. Filtrar alumnos con calificación mayor y menor a 90
print("\n📌 Alumnos con calificación mayor a 90:")
print(df[df['Nota'] > 90])

print("\n📌 Alumnos con calificación menor a 90:")
print(df[df['Nota'] < 90])

# 4. Sumar todas las notas
suma_notas = df['Nota'].sum()
print(f"\n📌 Suma total de las notas: {suma_notas}")

# 5. Nota máxima y mínima
nota_maxima = df['Nota'].max()
nota_minima = df['Nota'].min()

print(f"\n📌 Nota máxima: {nota_maxima}")
print(f"📌 Nota mínima: {nota_minima}")
