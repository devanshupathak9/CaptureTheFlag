import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip address and port changes at each spawn
server_addr = ("83.136.253.59", 53104)
client.connect(server_addr)

i = 0
ctf_flag = ""

while True:
    request = client.recv(1024).decode("utf-8").strip()
    print(request, "\n")
    if "Index out of range!" in request:
        break
    if "Character at Index" in request:
        ctf_flag += request.split("\n")[0][-1]

    client.sendall(f"{i}\n".encode("utf-8"))
    i += 1
client.close()

print(ctf_flag)
