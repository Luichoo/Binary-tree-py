'''
Binary tree copied from my my binary tree in C with some extra details

'''
from os import system
import nodes as nd
import time

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
        nd.busca_letra(x)
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
    start = time.time()
    nd.inorder()
    print("Total time = %.6f" % (time.time()-start))
    print("-------------------------------")
    print("inorder iterative")
    start = time.time()
    nd.inorder_iterative()
    print("Total time = %.6f" % (time.time()-start))
    print("-------------------------------")
def preorderM():
    print("preorder")
    start = time.time()
    nd.preorder()
    print("Total time = %.6f" % (time.time()-start))
    print("-------------------------------")
    print("preorder iterative")
    start = time.time()
    nd.preorder_iterative()
    print("Total time = %.6f" % (time.time()-start))
    print("-------------------------------")
def postorderM():
    print("postorder")
    start = time.time()
    nd.postorder()
    print("Total time = %.6f" % (time.time()-start))
    print("-------------------------------")
    print("postorder iterative")
    start = time.time()
    nd.postorder_iterative()
    print("Total time = %.6f" % (time.time()-start))
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
    
    nd.tree_vals()
    while True:
        system("cls")
        if not menu():
            break
        system("pause")