# Simulación SIR con Método Monte Carlo

Este proyecto implementa una simulación del modelo epidemiológico SIR utilizando el método de Monte Carlo, en versiones secuencial y paralela.

## Descripción

El modelo SIR divide la población en:
- Susceptibles (S)
- Infectados (I)
- Recuperados (R)

Se simula la propagación de una enfermedad mediante procesos probabilísticos para analizar su comportamiento en el tiempo.


## Estructura del proyecto

SIR_MONTECARLO_SIM/
│
├── .vscode/              # Configuración de Visual Studio Code
├── data/                 # Datos base o configuraciones de entrada
├── sequential/           # Implementación secuencial del modelo SIR
├── parallel/             # Implementación paralela del modelo SIR
├── results/              # Resultados generados por las simulaciones
│
├── README.md             # Documentación del proyecto
│
├── output_seq.csv        # Resultados de la simulación secuencial
├── output_omp.csv        # Resultados de la simulación paralela
├── times_auto.csv        # Tiempos de ejecución (comparación rendimiento)
│
├── sir_seq.exe           # Ejecutable versión secuencial
├── sir_omp.exe           # Ejecutable versión paralela
│
├── sir_comparacion.gif   # Visualización comparativa de ambas simulaciones
├── temp.png              # Imagen temporal generada durante simulación


## Funcionamiento

1. Se inicializa una población con individuos susceptibles, infectados y recuperados.
2. Se definen probabilidades de contagio y recuperación.
3. Se simulan múltiples iteraciones utilizando el método de Monte Carlo.
4. Se registran los resultados en archivos CSV.
5. Se comparan resultados entre ejecución secuencial y paralela.


## Ejecución

### Opción 1: Ejecutables

Ejecutar directamente:

sir_seq.exe  
sir_omp.exe  

### Opción 2: Código fuente

python sequential/sir_simulation.py


## Resultados

Los archivos CSV contienen:

- Evolución de S, I y R en el tiempo
- Comparación entre métodos
- Medición de tiempos de ejecución

El archivo GIF muestra visualmente la diferencia entre ambas implementaciones.


## Objetivo

- Simular la propagación de una enfermedad usando Montecarlo
- Comparar rendimiento entre ejecución secuencial y paralela
- Analizar el comportamiento del modelo SIR
