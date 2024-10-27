import argparse
import sys
from commands import transaction, blockchain, network

class CLITool:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Quantum Mega Nexus CLI Tool")
        self.subparsers = self.parser.add_subparsers(dest='command')

        # Add command modules
        self.add_transaction_commands()
        self.add_blockchain_commands()
        self.add_network_commands()

    def add_transaction_commands(self):
        """Add transaction-related commands to the CLI."""
        transaction_parser = self.subparsers.add_parser('transaction', help='Manage transactions')
        transaction_subparsers = transaction_parser.add_subparsers(dest='subcommand')

        # Create transaction command
        create_parser = transaction_subparsers.add_parser('create', help='Create a new transaction')
        create_parser.add_argument('--from', required=True, help='Sender address')
        create_parser.add_argument('--to', required=True, help='Receiver address')
        create_parser.add_argument('--amount', type=float, required=True, help='Transaction amount')

    def add_blockchain_commands(self):
        """Add blockchain-related commands to the CLI."""
        blockchain_parser = self.subparsers.add_parser('blockchain', help='Manage blockchain')
        blockchain_subparsers = blockchain_parser.add_subparsers(dest='subcommand')

        # View blockchain command
        view_parser = blockchain_subparsers.add_parser('view', help='View the blockchain')

    def add_network_commands(self):
        """Add network-related commands to the CLI."""
        network_parser = self.subparsers.add_parser('network', help='Manage network')
        network_subparsers = network_parser.add_subparsers(dest='subcommand')

        # Add peer command
        add_peer_parser = network_subparsers.add_parser('add-peer', help='Add a new peer to the network')
        add_peer_parser.add_argument('--host', required=True, help='Peer host address')
        add_peer_parser.add_argument('--port', type=int, required=True, help='Peer port number')

    def run(self):
        """Parse arguments and execute the corresponding command."""
        args = self.parser.parse_args()

        if args.command is None:
            self.parser.print_help()
            sys.exit(1)

        if args.command == 'transaction' and args.subcommand == 'create':
            transaction.create_transaction(args.from, args.to, args.amount)
        elif args.command == 'blockchain' and args.subcommand == 'view':
            blockchain.view_blockchain()
        elif args.command == 'network' and args.subcommand == 'add-peer':
            network.add_peer(args.host, args.port)
        else:
            print("Invalid command or subcommand.")
            sys.exit(1)

# Entry point for the CLI tool
if __name__ == "__main__":
    cli_tool = CLITool()
    cli_tool.run()
