from flask import Flask, request, jsonify
from configparser import ConfigParser
import logging
import os

# Get the current directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Read the configuration file
config = ConfigParser()
config.read(f'{dir_path}/dummy.cfg')

# Ensure the logs directory exists and has the correct permissions
log_dir = os.path.dirname(config['LOGGING']['log_file'])
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)

# Set up logging to the specified log file
logging.basicConfig(
    filename=config['LOGGING']['log_file'],
    level=config['LOGGING']['log_level']
)

# Create the Flask app
app = Flask(__name__)

# Define the dummy endpoint
@app.route('/dummy', methods=['GET'])
def dummy():
    # Retrieve the query parameters
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")

    # Log the request data
    logging.info(f"Received: {firstname} {lastname}")

    # Return the full name as a response
    return f"{firstname} {lastname}"

# Run the app when this file is executed
if __name__ == "__main__":
    # Use environment variables for host and port, with defaults for container
    api_host = os.getenv('FLASK_RUN_HOST', config['APISERVER']['api_host'])
    api_port = int(os.getenv('FLASK_RUN_PORT', config['APISERVER']['api_port']))

    # Start the Flask server
    app.run(host=api_host, port=api_port)
