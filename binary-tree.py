'''
Binary tree copied from my my binary tree in C with some extra details

'''
from os import system


letters={
    "n0":0,
    "o":1,
    "m":2,
    "q":3,
    "g":4,
    "z":5,
    "t":6,
    "y":7,
    "k":8,
    "c":9,
    "n":10,
    "x":11,
    "d":12,
    "b":13,
    "rooti":14,
    "j":15,
    "w":16,
    "p":17,
    "a":18,
    "r":19,
    "l":20,
    "e":21,
    "u":22,
    "f":23,
    "i":24,
    "v":25,
    "s":26,
    "h":27}


class Node:
    def __init__(self, val = 0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

root = Node(letters["rooti"])


def inorder(node=root):
    if node is None:
        return True
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def inorder_iterative(node=root):
    stack=[]
    while (stack or node is not None):
        if node is not None:
            stack.append(node)
            node=node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right

def preorder(node=root):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)



def preorder_iterative(node=root):
    stack=[]
    while (stack or node is not None):
        if node is not None:
            stack.append(node)
            print(node.val)
            node=node.left
        else:        
            node = stack.pop()
            node = node.right

def postorder(node=root):         
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

def postorder_iterative(node=root):
    last =  None
    stack = []

    while True:
        if node and node is not last:
            stack.append(node)
            node = node.left
        elif stack:
            aux = stack[-1]
            if aux.right is not node:
                node = aux.right
            else:
                node = last = stack.pop()
                print(last.val)
        else:
            break




def fill_tree(node, actual=root):
    if actual:
        if node.val > actual.val:
            if actual.right is not None:
                fill_tree(node,actual.right)
            else:
                actual.right=node

        else:
            if actual.left is not None:
                fill_tree(node,actual.left)            
            else:
                actual.left=node
    return

def busca_letra(letra,actual=root):
    if actual:

        if actual.val==letters[letra]:
            print("\n")
            return

        elif actual.val<=letters[letra]:
            print(".",end="")
            busca_letra(letra,actual.right)
            
        elif actual.val>=letters[letra]:
            print("_",end="")
            busca_letra(letra,actual.left)

    return 
def tree_vals():
    fill_tree(Node(letters["t"]))
    fill_tree(Node(letters["e"]))
    fill_tree(Node(letters["m"]))
    fill_tree(Node(letters["n"]))
    fill_tree(Node(letters["a"]))
    fill_tree(Node(letters["i"]))
    fill_tree(Node(letters["o"]))
    fill_tree(Node(letters["g"]))
    fill_tree(Node(letters["k"]))
    fill_tree(Node(letters["d"]))
    fill_tree(Node(letters["w"]))
    fill_tree(Node(letters["r"]))
    fill_tree(Node(letters["u"]))
    fill_tree(Node(letters["s"]))
    fill_tree(Node(letters["q"]))
    fill_tree(Node(letters["z"]))
    fill_tree(Node(letters["y"]))
    fill_tree(Node(letters["c"]))
    fill_tree(Node(letters["x"]))
    fill_tree(Node(letters["b"]))
    fill_tree(Node(letters["j"]))
    fill_tree(Node(letters["p"]))
    fill_tree(Node(letters["l"]))
    fill_tree(Node(letters["f"]))
    fill_tree(Node(letters["v"]))
    fill_tree(Node(letters["h"]))	


def Error():
    print("Opcion no valida")
    return False

def Salida():
    print("Chao")
    return True

def traductor():
    palabra = input("Palabra a convertir: ")
    for x in palabra:
        if x == " ":
            continue
        busca_letra(x)
        print(" ",end="")
def title():
    print(
            " 888888b.   d8b                                   \n",
            "888  \"88b  Y8P                                   \n", 
            "888  .88P                                        \n",
            "8888888K.  888 88888b.   8888b.  888d888 888  888\n", 
            "888  \"Y88b 888 888 \"88b     \"88b 888P\"   888  888\n", 
            "888    888 888 888  888 .d888888 888     888  888\n", 
            "888   d88P 888 888  888 888  888 888     Y88b 888\n",
            "8888888P\"  888 888  888 \"Y888888 888      \"Y88888\n", 
            "                                              888\n", 
            "                                         Y8b d88P\n", 
            "                                          \"Y88P\"\n"  
)
def inorderM():
    print("inorder")
    inorder()
    print("-------------------------------")
    print("inorder iterative")
    inorder_iterative()
    print("-------------------------------")
def preorderM():
    print("preorder")
    preorder()
    print("-------------------------------")
    print("preorder iterative")
    preorder_iterative()

    print("-------------------------------")
def postorderM():
    print("postorder")
    postorder()
    print("-------------------------------")
    print("postorder iterative")
    postorder_iterative()
    print("-------------------------------")

options={1:inorderM,2:preorderM,3:postorderM,4:traductor,0:Salida}
def menu():
    try:
        title()
        print(" 1. Recorrido inorder.\n",
               "2. Recorrido preorder \n",
               "3. Recorrido postorder\n",
               "4. Traductor binario\n",
               "0. Salir")
        opc=int(input("Seleccion: "))
        print("\n------------------------------------------")
        if options.get(opc, Error)():
            return False
        return True

    except ValueError:
        print("Solo numeros")
        return True

    except KeyboardInterrupt:
        return False


if __name__=="__main__":
    
    tree_vals()
    while True:
        system("cls")
        if not menu():
            break
        system("pause")