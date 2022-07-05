####POHON BINER

class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
akar = 8
def ukuranPohon(akar, count = 0):
    if akar is None:
        return count
    else:
        return ukuranPohon(akar.kiri, ukuranPohon(akar.kanan, count+1))
    
A = SimpulPohonBiner('A')
B = SimpulPohonBiner('B')
C = SimpulPohonBiner('C')
D = SimpulPohonBiner('D')
E = SimpulPohonBiner('E')
F = SimpulPohonBiner('F')
G = SimpulPohonBiner('G')
H = SimpulPohonBiner('H')
I = SimpulPohonBiner('I')
J = SimpulPohonBiner('J')

A.kiri = B;A.kanan = C
B.kiri = D;B.kanan = E
C.kiri = F;C.kanan = G
E.kiri = H;G.kanan = I
#preorder traversal
##def preorderTrav(subpohon):
##    if subpohon is not None:
##        print(subpohon.data)
##        preorderTrav(subpohon.kiri)
##        preorderTrav(subpohon.kanan)

##preorderTrav(A)
#inorder traversal
##def inorderTrav(subpohon):
##    if subpohon is not None:
##        inorderTrav(subpohon.kiri)
##        print(subpohon.data)
##        inorderTrav(subpohon.kanan)
##
##inorderTrav(A)

print(ukuranPohon(A))

