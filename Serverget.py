import socket
#####################################################################
#         DEVELOPED BY ENDER - KUSTAS - CYBER SECURITY              #
#####################################################################

HOST = 'localhost'
PORT = 8080
ADDR = (HOST,PORT)
BUFSIZE = 5000
incfilename=0
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

while True:
  incfilename = incfilename + 1
  conn, addr = serv.accept()
  print 'client connected ... ', addr
  myfile = open('picture%s.jpg'% str(incfilename), 'wb')
  soundfile = open('record%s.wav'% str(incfilename), 'wb')
  while True:
    data = conn.recv(BUFSIZE)
    if not data: break
    myfile.write(data)
    soundfile.write(data)
    print 'writing file ....'


