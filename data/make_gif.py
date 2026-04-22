import glob
import imageio.v2 as imageio
import pandas as pd
import matplotlib.pyplot as plt

seq_files = sorted(glob.glob("data/frame_seq_*.csv"))
par_files = sorted(glob.glob("data/frame_par_*.csv"))

images = []

for i in range(min(len(seq_files), len(par_files))):
    seq = pd.read_csv(seq_files[i], header=None)
    par = pd.read_csv(par_files[i], header=None)

    plt.figure(figsize=(8,4))

    plt.subplot(1,2,1)
    plt.title(f"Secuencial Día {i}")
    plt.imshow(seq)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title(f"Paralelo Día {i}")
    plt.imshow(par)
    plt.axis('off')

    filename = "temp.png"
    plt.savefig(filename)
    images.append(imageio.imread(filename))
    plt.close()

imageio.mimsave("sir_comparacion.gif", images, fps=10)

print("✅ GIF comparativo creado: sir_comparacion.gif")
