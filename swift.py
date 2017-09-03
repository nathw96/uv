import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))
print(s.getsockname()[0])
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('172.16.9.226', 5557))
b = bytearray([15, 156, 10, 113, 45, 0, 40, 49, 54, 51, 32, 85, 116, 105, 108, 105, 115, 97, 116, 101, 117, 114, 115, 32, 40, 49, 49, 49, 51, 32, 66, 111, 116, 115, 41, 32, 67, 111, 110, 110, 101, 99, 116, 195, 169, 115, 46, 0, 1, 50, 10, 109, 8, 0, 6, 103, 114, 97, 116, 111, 115, 10, 113, 25, 0, 20, 65, 98, 111, 110, 110, 101, 109, 101, 110, 116, 32, 58, 32, 103, 114, 97, 116, 117, 105, 116, 0, 1, 49])
while True:

        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format( address ))

        response = client.recv(255)
        if response != "":
                print(response)
                client.send(b)
                

print("Close")

client.close()
stock.close()
