from qiskit import QuantumCircuit, transpile
from qiskit import Aer


# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Se lee solo el primer qubit
circuit = QuantumCircuit(2, 1)
# Entrada (siempre debe ser {0,1})
circuit.x(1)
circuit.barrier()
# Deutsch's Algorithm
circuit.h(0)
circuit.h(1)
circuit.barrier()
# Circuito Función (Uf)
#circuit.x(0)
#circuit.cx(0, 1)
#circuit.x(1)
#circuit.x(0)
circuit.barrier()
#
circuit.h(0)
circuit.barrier()
# IBM lee de derecha a izquierda, se debe acomodar la entrada para que de salida en la forma como leemos.
circuit.measure([0], [0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)
# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
print("\nFunction is:", counts)
# Draw the circuit
print(circuit)