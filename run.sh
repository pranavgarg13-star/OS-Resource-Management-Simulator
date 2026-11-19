
#!/bin/bash

echo "===================================="
echo " OS RESOURCE MANAGEMENT SIMULATOR"
echo "===================================="

# Check Python installation
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed."
    exit 1
fi

echo "Python detected:"
python3 --version

# Move to application directory
cd "$(dirname "$0")" || exit 1

# Create reports folder
mkdir -p reports

# Execute Python application
echo ""
echo "Starting OS Simulator..."

python3 app.py

echo ""
echo "Simulation completed."
