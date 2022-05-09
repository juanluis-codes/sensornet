import node
import message
import ecc
import messagetopoint

slaves = []
masters = []
nets = []
nodes = []

# Creating the Masters nodes
for i in range(0, 50):
    masters.append(node.MasterNode(1, ("192.168." + str(i + 1) + ".1"), i + 1))

# Creating the Slaves nodes
for i in range(0, 50):
    for j in range(0, 25):
        slaves.append(node.SlaveNode(j + 2, ("192.168." + str(i + 1) + "." + str(j + 2)), i + 1)) 

# Creating the nets
for i in range(0, 50):
    for j in range(0, 25):
        nodes.append(slaves[(i * 25) + j])
        
    nets.append(node.NodeNet(i + 1, nodes, masters[i], ("192.168." + str(i + 1) + ".0")))
    nodes = []

server = node.Server(1, "209.125.1.59")

for i in range(0, 25):
    slaves[i].send(message.Message(ecc.S256Point(ecc.x1, ecc.y1)), masters[0])
masters[0].send(server)





#for i in range(0, 50):
#    print(masters[i])
#    for j in range(0, 25):
#        print(slaves[(i * 25) + j])

#for i in range(0, 50):
#    print(nets[i])
#    print()
    

