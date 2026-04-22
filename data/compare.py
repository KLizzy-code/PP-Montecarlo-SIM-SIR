import os
import pandas as pd
import matplotlib.pyplot as plt

path = "data"

seq_files = sorted([f for f in os.listdir(path) if f.startswith("frame_seq_")])
par_files = sorted([f for f in os.listdir(path) if f.startswith("frame_par_")])

if not seq_files or not par_files:
    print("⚠️ No se encontraron archivos")
    exit()

n = min(len(seq_files), len(par_files))

# 👉 UNA SOLA FIGURA
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

for i in range(n):
    seq = pd.read_csv(os.path.join(path, seq_files[i]), header=None)
    par = pd.read_csv(os.path.join(path, par_files[i]), header=None)

    # Limpiar en vez de crear nueva ventana
    axs[0].clear()
    axs[1].clear()

    axs[0].imshow(seq, vmin=0, vmax=3)
    axs[0].set_title(f"Secuencial - Día {i}")
    axs[0].axis('off')

    axs[1].imshow(par, vmin=0, vmax=3)
    axs[1].set_title(f"Paralelo - Día {i}")
    axs[1].axis('off')

    plt.pause(0.05)  # velocidad de animación

plt.show()