import ecc
import jacobi
from random import randint

class Message:
    # Building a Message
    def __init__(self, m):
        self.m = m
        self.point = None
        self.setPoint()

    # Represents only the decimal message
    def __repr__(self):
        return 'Message({})'.format(self.m)

    # Set self.m value. If m value is changed then the S256Point will have other value
    def setM(self, m):
        self.m = m
        self.setPoint()

    # Set self.point value
    def setPoint(self):
        self.point = self.toPoint()

    # Getting a S256Point value from a decimal
    def toPoint(self):
        dx = self.m * 100
        dx_bin = bin(int(dx))

        for i in range(0, 16):
            dx_bin += "0"

        dx_bin = dx_bin.replace("0b", "")
        dx = 0

        for i in range(0, len(dx_bin)):
            dx = dx + int(dx_bin[len(dx_bin) - i - 1]) * pow(2, i)

        d = (pow(dx, 3) + 7) % ecc.P
        jacobisymbol = jacobi.calculateLegendre(d, ecc.P)

        while(jacobisymbol != 1):
            dx += 1
            d = (pow(dx, 3) + 7) % ecc.P
            jacobisymbol = jacobi.calculateLegendre(d, ecc.P)

        dy = pow(d, 28948022309329048855892746252171976963317496166410141009864396001977208667916, ecc.P)

        point = ecc.S256Point(dx, dy)
        return point

    # Getting a decimal value from a S256Point
    def toDecimal(self):
        m = self.point.x.num
        m = bin(m)
        m = m.replace("0b", "")
        d = 0

        for i in range(0, len(m) - 16):
            d = d + int(m[len(m) - i - 17]) * pow(2, i)

        return (d / 100)
        
    # Encrypting the message with ECC
    def encrypt(self):
        k = randint(2, ecc.N - 1)
        kG = k * ecc.G
        kP = k * ecc.keyset.publicKey
        q = self.m + kP
        encryption = ("kG = {} q = {}").format(kG, q)
        return EncryptedMessage(kG, q)

class EncryptedMessage:
    def __init__(self, kG, q):
        self.kG = kG
        self.q = q

    def __repr__(self):
        return 'Message({}, {})'.format(self.kG, self.q)

    # Decrypting the encrypted message with ECC
    def decrypt(self):
        message = self.q + ((ecc.N - 1) * (ecc.keyset.privateKey * self.kG))
        return Message(message)


