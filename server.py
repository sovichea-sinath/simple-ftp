import socket
import os
from helpers import get_local_ip, recv_all, recv_until_done

# ip = get_local_ip(os.uname().sysname)
ip = 'localhost'
port = int(input('please input port number: '))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.bind((ip, port))
  print(f'bind to {ip}:{port}')
  sock.listen()
  conn, addr = sock.accept()

  while True:
    print('get file size.')
    file_size = int(recv_all(conn).decode())
    print(f'file is {file_size} bytes long')
    if file_size > 1073741824:
      print('file size exceed!')
      conn.sendall(b'restart')
      continue
    conn.sendall(b'ok')
    file_location = recv_all(conn).decode()
    dir_path = '/'.join(file_location.split('/')[:-1]) + '/'
    file_name = file_location.split('/')[-1]
    if len(dir_path) > 0:
      if not os.path.exists(dir_path):
        print('file size exceed!')
        conn.sendall(b'restart')
        continue
    conn.sendall(b'ok')
    print('reciving file...')
    data = recv_until_done(conn, file_size)
    with open(file_location, 'wb') as wFile:
      wFile.write(data)
    
    print('file created')

