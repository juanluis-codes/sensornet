import ecc
import jacobi

data = float(input("Dato:"))
data = data * 100
data_bin = bin(int(data))
print("Dato*100 en binario: " + data_bin)

for i in range(0, 16):
    data_bin += "0"
print("Binario extendido: " + data_bin)

data_bin = data_bin.replace("0b", "")
data = 0

for i in range(0, len(data_bin)):
    data = data + int(data_bin[len(data_bin) - i - 1]) * pow(2, i)
print("Decimal despues de binario extendido: " + str(data))
    
data1 = (pow(data, 3) + 7) % ecc.P
jacobisimbol = jacobi.calculateLegendre(data1, ecc.P)
print("Jacobi: " + str(jacobisimbol))
print("Se calcula la imagen: " + str(data1))

while(jacobisimbol != 1):
    data = data + 1
    data1 = (pow(data, 3) + 7) % ecc.P
    jacobisimbol = jacobi.calculateLegendre(data1, ecc.P)
    
print("Se calcula la imagen: " + str(data1))
print("Jacobi: " + str(jacobisimbol))

coory = pow(data1, 28948022309329048855892746252171976963317496166410141009864396001977208667916, ecc.P)
print("Coordenada y: " + str(coory))

punto = ecc.S256Point(data, coory)


m = punto.x.num
m = bin(m)
m = m.replace("0b", "")
data2 = 0
for i in range(0, len(m) - 16):
    data2 = data2 + int(m[len(m) - i - 17]) * pow(2, i)
print(data2/100)
