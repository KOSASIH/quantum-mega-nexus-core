#!/bin/bash

# Environment setup script for the Quantum Mega Nexus project

# Function to display usage
usage() {
    echo "Usage: $0"
    exit 1
}

# Function to install system dependencies
install_dependencies() {
    echo "Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv git
    echo "System dependencies installed."
}

# Function to create a virtual environment
create_virtualenv() {
    echo "Creating a virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
}

# Function to activate the virtual environment and install Python packages
install_python_packages() {
    echo "Activating virtual environment and installing Python packages..."
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Python packages installed."
}

# Function to set up environment variables
setup_environment_variables() {
    echo "Setting up environment variables..."
    export NODE_ENV=development
    export DATABASE_URL="sqlite:///data.db"
    echo "Environment variables set."
}

# Main function to run the setup
main() {
    install_dependencies
    create_virtualenv
    install_python_packages
    setup_environment_variables
    echo "Environment setup complete."
}

# Check if the script is run without arguments
if [ $# -ne 0 ]; then
    usage
fi

# Run the main setup function
main
