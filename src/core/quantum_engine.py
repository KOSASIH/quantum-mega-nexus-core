import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class QuantumEngine:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def apply_hadamard(self, qubit):
        """Apply Hadamard gate to a specific qubit."""
        self.circuit.h(qubit)

    def apply_cnot(self, control, target):
        """Apply CNOT gate with control and target qubits."""
        self.circuit.cx(control, target)

    def measure(self):
        """Measure all qubits."""
        self.circuit.measure_all()

    def run(self, shots=1024):
        """Run the quantum circuit and return the results."""
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, simulator, shots=shots)
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def reset(self):
        """Reset the quantum circuit."""
        self.circuit = QuantumCircuit(self.num_qubits)

# Example usage
if __name__ == "__main__":
    engine = QuantumEngine(num_qubits=2)
    engine.apply_hadamard(0)
    engine.apply_cnot(0, 1)
    engine.measure()
    results = engine.run()
    print("Quantum Measurement Results:", results)
