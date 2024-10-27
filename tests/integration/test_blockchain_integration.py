import unittest
from blockchain.block import Block
from blockchain.chain import Chain

class TestBlockchainIntegration(unittest.TestCase):
    def setUp(self):
        self.chain = Chain()

    def test_block_addition(self):
        block = Block(index=1, transactions=['tx1', 'tx2'])
        self.chain.add_block(block)
        self.assertEqual(self.chain.get_latest_block().index, 1)

    def test_chain_integrity(self):
        block1 = Block(index=1, transactions=['tx1', 'tx2'])
        block2 = Block(index=2, transactions=['tx3', 'tx4'])
        self.chain.add_block(block1)
        self.chain.add_block(block2)
        self.assertTrue(self.chain.is_chain_valid())

if __name__ == "__main__":
    unittest.main()
