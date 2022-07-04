##Kelas Penyimpanan

class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

##Membuat Simpul-simpul dan Mengisi Data
A = _SimpulPohonBiner("Ambarawa")
B = _SimpulPohonBiner("Bantul")
C = _SimpulPohonBiner("Cimahi")
D = _SimpulPohonBiner("Denpasar")
E = _SimpulPohonBiner("Enrekang")
F = _SimpulPohonBiner("Flores")
G = _SimpulPohonBiner("Garut")
H = _SimpulPohonBiner("Halmahera Timur")
I = _SimpulPohonBiner("Indramayu")
J = _SimpulPohonBiner("Jakarta")

##Menghubungkan simpul ortu-anak(sesuai gambar 9.5a)

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

### TREE TRAVERSAL

##Preorder Traversal(dimulai dari simul akar)
def preorderTrav( subpohon):
    if subpohon is not None :
        print( subpohon.data )
        preorderTrav(subpohon.kiri)
        preorderTrav(subpohon.kanan)

preorderTrav(A)

##Inorder Traversal
def inorderTrav(subpohon):
    if subpohon is not None:
        inorderTrav(subpohon.kiri)
        print(subpohon.data)
        inorderTrav(subpohon.kanan)

inorderTrav(A)

##Postorder Traversal

def postorderTrav(subpohon):
    if subpohon is not None:
        postorderTrav(subpohon.kiri)
        postorderTrav(subpohon.kanan)
        print(subpohon.data)
