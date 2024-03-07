import subprocess

# Ganti alamat IP dan port sesuai dengan server Ncat Anda
server_ip = "192.168.1.1"
server_port = 8080

# Membentuk perintah Ncat
ncat_command = f"ncat {server_ip} {server_port}"

# Menjalankan perintah Ncat
process = subprocess.Popen(ncat_command, shell=True)

# Menunggu proses selesai (Anda dapat menghapus baris ini jika tidak perlu)
process.wait()
