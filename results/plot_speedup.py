import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/times_auto.csv")

T1 = df['time'].iloc[0]
df['speedup'] = T1 / df['time']

print(df)

plt.figure()
plt.plot(df['cores'], df['speedup'], marker='o')
plt.xlabel("Número de cores")
plt.ylabel("Speed-up")
plt.title("Strong Scaling - Modelo SIR")
plt.grid()

plt.savefig("speedup.png")

plt.show()

print("Gráfica guardada como speedup.png")
