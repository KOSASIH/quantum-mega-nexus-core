import unittest
from network.node import Node
from network.communication import Communication

class TestNetworkIntegration(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(node_id=1, host='localhost', port=5001)
        self.node2 = Node(node_id=2, host='localhost', port=5002)
        self.node1.register_peer(('localhost', 5002))
        self.node2.register_peer(('localhost', 5001))

    def test_peer_registration(self):
        self.assertIn(('localhost', 5002), self.node1.peers)
        self.assertIn(('localhost', 5001), self.node2.peers)

    def test_broadcast_message(self):
        message = {'type': 'test', 'content': 'Hello, Node 2!'}
        Communication.broadcast(self.node1.peers, message)
        # Here you would implement a way to verify that Node 2 received the message

if __name__ == "__main__":
    unittest.main()
