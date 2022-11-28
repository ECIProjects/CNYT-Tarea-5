from qiskit import QuantumCircuit, transpile
from qiskit import Aer


# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)
# Entrada
#circuit.x(0)
#circuit.x(1)
circuit.barrier(0, 1)
# Se añade Uf, la forma reversible de la función.
#circuit.x(0)
#circuit.cx(0, 1)
#circuit.x(1)
#circuit.x(0)
circuit.barrier(0, 1)
# Se mapean las medidas cuánticas a los bits cuánticos (se le da la "vuelta" al orden de los bits para que podamos leerlos de la forma correcta).
circuit.measure([0,1], [1,0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)
# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
print("\nQubit value for 00 is:", counts)
# Draw the circuit
print(circuit)
# Plot a histogram
#plot_histogram(counts)
#plt.show()


simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(1)
circuit.barrier()
#circuit.x(0)
#circuit.cx(0, 1)
#circuit.x(1)
#circuit.x(0)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 01 is:", counts)
print(circuit)

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.barrier()
#circuit.x(0)
#circuit.cx(0, 1)
#circuit.x(1)
#circuit.x(0)
circuit.barrier()
circuit.measure([0,1], [1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 10 is:", counts)
print(circuit)

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.x(1)
circuit.barrier()
#circuit.x(0)
#circuit.cx(0, 1)
#circuit.x(1)
#circuit.x(0)
circuit.barrier()
circuit.measure([0,1], [1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nQubit value for 11 is:", counts)
print(circuit)
