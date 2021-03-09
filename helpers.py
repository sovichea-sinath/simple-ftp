import socket

def get_local_ip(sysname: str) -> str:
  if sysname == "Darwin":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
  return socket.gethostbyname(socket.gethostname())

def recv_all(sock: socket.socket):
  '''
  read data from client all at once.
  '''
  BUF_SIZE = 1024
  data = b''
  while True:
    # read 1024 byte at a time.
    recv = sock.recv(BUF_SIZE)
    data += recv
    if len(recv) < BUF_SIZE:
      return data

def recv_until_done(sock: socket.socket, limit):
  # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < limit:
      packet = sock.recv(limit - len(data))
      if not packet:
        return None
      data += packet
    return data

