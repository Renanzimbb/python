#Tema 2 > Análise de Dados Quantitativos Com Python > Módulo 4 > Medidas de dispersão ou variabilidade no Python
import statistics
import numpy as np

comprimento = [3,5,6,8,7,3]

# Variancia Populacional
variancia = statistics.variance(comprimento)
print(variancia)

# Desvio Padrão (Standard Deviation)
desvio_padrao = statistics.stdev(comprimento)
print(desvio_padrao)

# Amplitude (Pick to Pick)
amplitude = np.ptp(comprimento)
print(amplitude)

# QUANTIS
q1, q2, q3 = np.percentile(comprimento,[25,50,75])
print(q1)

# PERCENTIS

    
# DECIS