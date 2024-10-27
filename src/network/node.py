import hashlib
import json
import time
import socket
import threading

class Node:
    def __init__(self, node_id, host='localhost', port=5000):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.peers = set()
        self.blockchain = []
        self.current_transactions = []
        self.lock = threading.Lock()

    def register_peer(self, peer):
        """Register a new peer in the network."""
        self.peers.add(peer)

    def create_block(self, previous_hash):
        """Create a new block in the blockchain."""
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.blockchain[-1]) if self.blockchain else '0'
        }
        self.current_transactions = []
        self.blockchain.append(block)
        return block

    @staticmethod
    def hash(block):
        """Create a SHA-256 hash of a block."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def start_server(self):
        """Start the node server to listen for incoming connections."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Node {self.node_id} listening on {self.host}:{self.port}")

        while True:
            client_socket, address = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        """Handle incoming client connections."""
        with client_socket:
            data = client_socket.recv(1024).decode()
            print(f"Received data: {data}")
            # Process the received data (e.g., transactions, blocks)

# Example usage
if __name__ == "__main__":
    node = Node(node_id=1)
    threading.Thread(target=node.start_server).start()
