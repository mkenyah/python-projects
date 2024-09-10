from flask import Flask, render_template, request
import socket
import threading
import datetime

app = Flask(__name__)

clients = []
clients_info = {}
lock = threading.Lock()

# Function to handle incoming messages from clients
def handle_client(conn, addr):
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break

            decoded_message = message.decode('utf-8')
            print(f"Received message from {addr}: {decoded_message}")

        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            break

    lock.acquire()
    clients.remove(conn)
    if addr in clients_info:
        del clients_info[addr]
    lock.release()
    conn.close()

# Route to render the chat interface
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket route for receiving messages from clients
@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    ip_address = request.remote_addr
    location = "Unknown"  # You can enhance this to fetch location if needed
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"{current_date} | {ip_address} | {location} | {message}"
    print(f"Message received on server: {full_message}")
    return '', 204

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(3)
    print("Server listening on port 5555")

    while True:
        conn, addr = server.accept()
        print(f"New connection from {addr}")

        lock.acquire()
        clients.append(conn)
        clients_info[addr] = conn
        lock.release()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    app.run(debug=True)
