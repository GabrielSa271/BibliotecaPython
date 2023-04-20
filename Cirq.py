import cirq

# Cria um circuito quântico
qubit = cirq.GridQubit(0, 0)
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5,  # Raiz quadrada da porta X
    cirq.measure(qubit, key='m')  # Medição do qubit com resultado 'm'
)

# Executa o circuito em um simulador
simulator = cirq.Simulator()
result = simulator.run(circuit)

# Exibe os resultados da medição
print(result)