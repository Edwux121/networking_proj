import socket
import threading
from queue import Queue

target = "192.168.2.1"
queue = Queue()
open_ports = []

def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

#Defining the port range and filling the queue
port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

#Running threads and defining the thread count
for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)