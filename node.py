import ecc
import message

class Node:
    def __init__(self, id_node, ip, net):
        self.id_node = id_node
        self.ip = ip
        self.net = net

    def getNet(self):
        return self.net
        
    def __repr__(self):
        return "Node({},{})".format(self.id_node, self.ip)

class MasterNode(Node):
    def __init__(self, id_node, ip, net):
        super().__init__(id_node, ip, net)
        self.messures = []
        self.kGsum = 0 * ecc.S256Point(ecc.x1, ecc.y1)
        self.qsum = 0 * ecc.S256Point(ecc.x1, ecc.y1)
    
    def __repr__(self):
        return "MasterNode({},{})".format(self.id_node, self.ip)

    def send(self, server):
        for i in range(0, len(self.messures)):
            self.kGsum = self.kGsum + self.messures[i].kG
            self.qsum = self.qsum + self.messures[i].q
            
        server.rcv(self.id_node, self.messures, self.kGsum, self.qsum)
    
    def rcv(self, id_sender, message):
        self.messures.append(message)
        print("Message received {} sent by node {}".format(message, id_sender))

class SlaveNode(Node):
    def __init__(self, id_node, ip, net):
        super().__init__(id_node, ip, net)
        
    def __repr__(self):
        return "SlaveNode({},{})".format(self.id_node, self.ip)
    
    def send(self, message, master):
        if(master.getNet() != self.getNet()):
            exit()

        master.rcv(self.id_node, message.encrypt())

class Server:
    def __init__(self, server_id, ip):
        self.server_id = server_id
        self.ip = ip

    def __repr__(self):
        return "Server({},{})".format(self.server_id, self.ip)

    def rcv(self, id_master, messures, kGsum, qsum):
        print("Message received {} sent by master {}".format(message, id_master))
        print(ecc.S256Point.decrypt(kGsum, qsum))

class NodeNet:
    def __init__(self, net_id, nodes, master, ip):
        self.net_id = net_id
        self.nodes = nodes
        self.master = master
        self.ip = ip

    def __repr__(self):
        return "Net_{}({}) with nodes {}, Master: {}".format(self.net_id, self.ip, self.nodes, self.master)




# CREATING THE NODE NET
# CREATING THE MASTER NODE
# master = MasterNode(1, "192.168.1.1", 1)
# CREATING THE SLAVES NODES
# slave1 = SlaveNode(2, "192.168.1.2", 1)
# slave2 = SlaveNode(3, "192.168.1.3", 1)
# slave3 = SlaveNode(4, "192.168.1.4", 1)
# slave4 = SlaveNode(5, "192.168.1.5", 1)
# slave5= SlaveNode(6, "192.168.1.6", 1)
# LIST OF NODES
# nodes = [slave1, slave2, slave3, slave4, slave5]
# NODES NET
# net = NodeNet(1, nodes, master, "192.168.1.0")
# CREATING THE SERVER
# server = Server(1, "209.125.1.59")

