import subprocess
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_nmap(command):
    """Execute the Nmap command and capture the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def parse_prompt(prompt):
    """Parse the user's prompt to generate the appropriate Nmap command."""
    ip_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", prompt)
    ip_address = ip_match.group(1) if ip_match else None

    if "open ports" in prompt.lower():
        nmap_command = f"nmap -p- {ip_address}"
    elif "OS detection" in prompt.lower():
        nmap_command = f"nmap -O {ip_address}"
    elif "version scan" in prompt.lower():
        nmap_command = f"nmap -sV {ip_address}"
    elif "ping" in prompt.lower():
        nmap_command = f"nmap -sn {ip_address}"
    else:
        nmap_command = f"nmap {ip_address}"

    return nmap_command

@app.route('/scan', methods=['POST'])
def scan():
    """Process the user's prompt and execute the corresponding Nmap command."""
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    # Parse the prompt to generate the Nmap command
    nmap_command = parse_prompt(prompt)
    
    # Execute the Nmap command and return the result
    scan_result = execute_nmap(nmap_command)
    
    return jsonify({"result": scan_result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
