
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

root=Node(letters["rooti"])


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