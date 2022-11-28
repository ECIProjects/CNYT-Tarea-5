from qiskit import QuantumCircuit, transpile
from qiskit import Aer


def BinToDec(binary):
    pos = 0
    dec = 0
    binary = binary[::-1]
    for digit in binary:
        mult = 2**pos
        dec += int(digit) * mult
        pos += 1
    return dec


def DecToBin(dec):
    binary = ""
    while dec != 0:
        binary += str(dec % 2)
        dec = dec // 2
    binary = binary[::-1]
    while len(binary) < 5:
        binary = "0" + binary
    return binary

# Matriz para f(x) = 0
def IdentityMatrix(n):
    matrix = [[0 for k in range(n)] for j in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

# Matriz para f(x) = 1 ⊕ x_0
def ReverseFirstQuarter(n):
    matrix = [[0 for k in range(n)] for l in range(n)]
    for i in range(0, (n//2), 2):
        matrix[i][i+1] = 1
        matrix[i+1][i] = 1
    for n in range((n//2), n):
        matrix[n][n] = 1
    return matrix

# Matriz para f(x) = x_0
def ReverseLastQuarter(n):
    matrix = [[0 for k in range(n)] for l in range(n)]
    for i in range(n//2, n, 2):
        matrix[i][i+1] = 1
        matrix[i+1][i] = 1
    for n in range(0, n//2):
        matrix[n][n] = 1
    return matrix

# Matriz para f(x) = 1 ⊕ x_3
def ReversePairPos(n):
    matrix = [[0 for k in range(n)] for l in range(n)]
    for i in range(0, n, 4):
        matrix[i][i+1] = 1
        matrix[i+1][i] = 1
    for n in range(2, n, 4):
        matrix[n][n] = 1
        matrix[n+1][n+1] = 1
    return matrix

#matrix = IdentityMatrix(32)
#matrix = ReverseFirstQuarter(32)
#matrix = ReverseLastQuarter(32)
#matrix = ReversePairPos(32)
#for i in range(len(matrix)):
#    print(*matrix[i])


# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Se leen todos los qubits
circuit = QuantumCircuit(5, 5)
# Entrada (todas en 0 excepto la ultima)
circuit.barrier()
# Circuito Función (Uf)
circuit.cx(3, 4)
circuit.barrier()
# IBM lee de derecha a izquierda, se debe acomodar la entrada para que de salida en la forma como leemos.
circuit.measure([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)
# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
print("\nQubit value for 00000 is:", counts)
# Draw the circuit
print(circuit)

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(0)
circuit.barrier()
circuit.cx(3, 4)
circuit.barrier()
circuit.measure([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 10000 is:", counts)
print(circuit)

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(1)
circuit.barrier()
circuit.cx(3, 4)
circuit.barrier()
circuit.measure([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 01000 is:", counts)
print(circuit)

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(2)
circuit.barrier()
circuit.cx(3, 4)
circuit.barrier()
circuit.measure([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 00100 is:", counts)
print(circuit)

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(3)
circuit.barrier()
circuit.cx(3, 4)
circuit.barrier()
circuit.measure([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 00010 is:", counts)
print(circuit)
