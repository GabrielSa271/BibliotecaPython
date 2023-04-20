import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define a função para a equação diferencial
def f(y, t, params):
    k, a = params
    dydt = k * y - a * y**2
    return dydt

# Define as condições iniciais e os parâmetros
y0 = 10
t = np.linspace(0, 10, 101)
k = 0.5
a = 0.1
params = (k, a)

# Resolve a equação diferencial
sol = odeint(f, y0, t, args=(params,))

# Plota o resultado
plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
