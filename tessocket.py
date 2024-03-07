import socket

# Ganti alamat IP dan port sesuai dengan server Netcat Anda
server_ip = "192.168.18.194"
server_port = 8080

# Membuat objek socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Terhubung ke server
client_socket.connect((server_ip, server_port))

# Kirim data ke server
message = "Hello, server!"
client_socket.sendall(message.encode())

# Terima data dari server
data = client_socket.recv(1024)
print("Received from server:", data.decode())

# Tutup koneksi
client_socket.close()
