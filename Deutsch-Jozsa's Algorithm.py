from qiskit import QuantumCircuit, transpile
from qiskit import Aer


def constant(counts):
    """Ingresa un diccionario y busca si hay una llave que sea la cadena de ceros, en caso de hallarla retorna true, de
    lo contrario false
    """
    if '0000' in counts.keys():
        return True
    return False

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Se lee solo el primer qubit
circuit = QuantumCircuit(5, 4)
# Entrada (todas en 0 excepto la ultima)
circuit.x(4)
circuit.barrier()
# Deustch-Jozsa's Algorithm
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.h(4)
circuit.barrier()
# Circuito Función (Uf)
circuit.cx(3, 4)
circuit.barrier()
#
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.h(3)
circuit.barrier()
# IBM lee de derecha a izquierda, se debe acomodar la entrada para que de salida en la forma como leemos.
circuit.measure([0, 1, 2, 3], [3, 2, 1, 0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)
# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)
# Grab results from the job
result = job.result()
# Returns counts
counts = result.get_counts(circuit)
if constant(counts):
    print("\nFunction is Constant")
else:
    print("\nFunction is Balanced")
# Draw the circuit
print(circuit)