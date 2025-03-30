import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, '/var/www/html/Budget_Manager_Web')

from app import app as application  # Ensure this points to the correct Flask app
