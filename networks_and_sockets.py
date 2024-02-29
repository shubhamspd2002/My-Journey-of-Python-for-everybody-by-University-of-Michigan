import socket

url = "http://data.pr4e.org/intro-short.txt"
url_parts = url.split('/')
host = url_parts[2]
path = '/' + '/'.join(url_parts[3:])

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    mysock.connect((host, 80))

    # Send a GET request
    request = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.sendall(request.encode())

    # Receive and print the response
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket
    mysock.close()
