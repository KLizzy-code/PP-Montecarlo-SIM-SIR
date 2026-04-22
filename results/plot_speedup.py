import pandas as pd
import matplotlib.pyplot as plt

# Leer datos (ajusta la ruta)
df = pd.read_csv("../results/times_auto.csv")

# Calcular speed-up
T1 = df['time'].iloc[0]
df['speedup'] = T1 / df['time']

# Mostrar tabla
print(df)

# Graficar
plt.figure()
plt.plot(df['cores'], df['speedup'], marker='o')
plt.xlabel("Número de cores")
plt.ylabel("Speed-up")
plt.title("Strong Scaling - Modelo SIR")
plt.grid()

# Guardar imagen
plt.savefig("speedup.png")

plt.show()

print("Gráfica guardada como speedup.png")
