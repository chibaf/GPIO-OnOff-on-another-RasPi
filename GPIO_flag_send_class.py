def mkline(flags):  # pack flags into a line
  line=''
  for i in range(0,len(flags)):
    if i==0:
      line=str(flags[0])
    else:
      line=line+","+str(flags[i])
  return line

class GPIO_flag_send:

  def __init__(self,host,port):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establish socket connection
    s.connect((host, port))
    self.Socket=s #socket
    
  def flag_send(self,s,flags):
    line=mkline(flags)
    s.send(str.encode(line))  #send flags

