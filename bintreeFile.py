
class node():
    def __init__ (self, value, left=None, right = None):
        self.value = value 
        self.right = right
        self.left = left 

class Bintree():
    def __init__(self):
        self.root = None
    
    def put(self, newvalue):
        #sorterar in newvalue i trädet 
        self.root = self.putta(self.root, newvalue)

    def __contains__(self, value):
        #true om value finns i trädet, false annars
        return self.finns(self.root, value)
    
    def write(self):
        #skriver ut träder i inorder
        self.skriv(self.root)
        print("\n")
    
    def putta(self, p, newvalue):
        #om trädet är tomt, skapa ny nod
        if p is None:
            return node(newvalue)

        #om värdet ska ligga till vänster
        if newvalue < p.value:
            p.left = self.putta(p.left, newvalue)

        #om värdet ska ligga till höger
        if newvalue > p.value:
            p.right = self.putta(p.right, newvalue)

        #om värdet redan finns, gör inget 
        return p 


    def finns(self, p, value):
        #om värdet finns 
        if p is None:
            return False 

        if value == p.value:
            return True

        if value < p.value:
            return self.finns(p.left, value)

        return self.finns(p.right, value)
    
    def skriv(self, p):
        if p is None:
            return 

        self.skriv(p.left)
        print(p.value)
        self.skriv(p.right)