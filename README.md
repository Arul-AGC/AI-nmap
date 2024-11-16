# Nmap Prompt Tool

This tool allows you to perform Nmap scans using natural language prompts. Simply input a prompt, and the tool will automatically generate and execute the corresponding Nmap command.

## Requirements

- Kali Linux (or any Linux distribution with Nmap installed)
- Python 3.x
- Nmap

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nmap_prompt_tool.git
   cd nmap_prompt_tool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Nmap is installed:
   ```bash
   sudo apt update
   sudo apt install nmap
   ```

4. Run the tool:
   ```bash
   python app.py
   ```

   The tool will start running a Flask web server on your local machine.

## Usage

1. Send a POST request to the `/scan` endpoint with a JSON body containing the prompt.

### Example Requests:

#### Request:
```bash
curl -X POST http://localhost:5000/scan -H "Content-Type: application/json" -d '{"prompt": "scan 192.168.1.1 for open ports"}'
```

#### Response:
```json
{
  "result": "Nmap scan result here"
}
```

## Note

- This tool interprets prompts and converts them into Nmap commands.
- Example prompts: "scan this IP", "perform version scan", "OS detection for 192.168.1.1", etc.
