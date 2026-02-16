import sys
import os

# Get the directory containing the tests package
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (project root)
project_root = os.path.dirname(current_dir)

# Add project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)
