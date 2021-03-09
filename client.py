import socket
from helpers import recv_all

ip = input('please input the host ip: ')
port = int(input('please input the host port: '))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.connect((ip, port))
  while True:
    file_path = input('please enter file name: ')
    with open(file_path, 'rb') as rFile:
      # read file.
      data = rFile.read()
      size = str(len(data)).encode()
      # send file size to the server.
      sock.sendall(size)
      msg = recv_all(sock)
      if msg != b'ok':
        print('file size exceed!')
        continue
      # send file_path
      new_path = input('save as?: ')
      sock.sendall(new_path.encode())
      msg = recv_all(sock)
      if msg != b'ok':
        print('file path not found!')
        continue
      print('sending file')
      sock.sendall(data)
      print('file complete transfer!')

