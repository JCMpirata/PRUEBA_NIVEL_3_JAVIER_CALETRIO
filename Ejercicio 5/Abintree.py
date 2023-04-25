
from AslistH_Nodo import SList

class BinaryNode:
    
        def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
            self.elem = elem
            self.left = node_left
            self.right = node_right
    
        def __eq__(self, other: 'BinaryNode') -> bool:
            """checks if two nodes (subtrees) are equal o not"""
            return other is not None and self.elem == other.elem and self.left == other.left and self.right == other.right
    
        def __str__(self):
            return str(self.elem)
        
class BinaryTree:
    def __init__(self) -> None:
        "crea un arbol binario vacio"
        self._root = None

    def __eq__(self, other: 'BinaryTree') -> bool:
        "chequea si dos arboles binarios son iguales o no"
        return other is not None and self._root == other._root

    def size(self) -> int:
        "Retorna el numero de nodos"
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        "retorna el tamaño del subarbol que cuelga de node"
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        "Retorna la altura del arbol"
        return self._height(self._root)
    
    def height_subarbol_izquierdo(self) -> int:
        "Retorna la altura del subarbol izquierdo"
        return self._height(self._root.left)
    
    def height_subarbol_derecho(self) -> int:
        "Retorna la altura del subarbol derecho"
        return self._height(self._root.right)

    def _height(self, node: BinaryNode) -> int:
        "retorna la altura del nodo"
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def preorder(self) -> None:
        "imprime el recorrido preorder (root, left, right) traversal del arbol"
        # self.draw()
        print('Preorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._preorder(self._root)
        print()

    def _preorder(self, node: BinaryNode) -> None:
        "imprime el recorrido preorder (root, left, right) traversal del subarbol que cuelga de nodo"
        if node is not None:
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder_list(self) -> list:
        "retorna una lista con el preorder traversal del arbol"
        # self.draw()
        result = []
        self._preorder_list(self._root, result)
        return result

    def _preorder_list(self, node: BinaryNode, pre_list: list) -> None:
        "rellena pre_list con el preorder traversal del nodo del subarbol"
        if node is not None:
            pre_list.append(node.elem)
            self._preorder_list(node.left, pre_list)
            self._preorder_list(node.right, pre_list)

    def postorder(self) -> None:
        "imprime el recorrido postorder (left, right, root) traversal del arbol"
        # self.draw()
        print('Postorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._postorder(self._root)
        print()

    def _postorder(self, node: BinaryNode) -> None:
        "imprime el recorrido preorder (root, left, right) traversal del subarbol que cuelga de nodo"
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem, end=' ')  # end=' ' avoid new line

    def postorder_list(self) -> list:
        "devuelve una lista con el recorrido postorder del arbol"
        # self.draw()
        result = []
        self._postorder_list(self._root, result)
        return result

    def _postorder_list(self, node: BinaryNode, post_list: list) -> None:
        "rellena post_list con el postorder traversal del nodo del subarbol"
        if node is not None:
            self._postorder_list(node.left, post_list)
            self._postorder_list(node.right, post_list)
            post_list.append(node.elem)

    def inorder(self) -> None:
        "imprime el recorrido inorder (left, root, right) traversal del arbol"
        # self.draw()
        print('Inorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._inorder(self._root)
        print()

    def _inorder(self, node: BinaryNode) -> None:
        "imprime el recorrido inorder (left, root, right) traversal del subarbol que cuelga de nodo"
        if node is not None:
            self._inorder(node.left)
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._inorder(node.right)

    def inorder_list(self) -> list:
        "devuelve una lista con el recorrido inorder del arbol"
        # self.draw()
        result = []
        self._inorder_list(self._root, result)
        return result

    def _inorder_list(self, node: BinaryNode, in_list: list) -> None:
        "rellena in_list con el inorder traversal del nodo del subarbol"
        if node is not None:
            self._postorder_list(node.left, in_list)
            in_list.append(node.elem)
            self._postorder_list(node.right, in_list)

    def level_order(self) -> None:
        "imprime el orden de nivel del arbol. O(n)"
        if self._root is None:
            print('tree is empty')
        else:
            print("Level order: ", end= ' ')  # avoid the new line

            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)

            print()

    def level_order_list(self) -> list:
        "imprime el orden de nivel del arbol. O(n)"
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                result.append(current.elem)
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)

        return result

    def depth(self, node):
        "devuelve la profundidad del nodo; esta es la longitud desde la raíz hasta el nodo"
        depth_level = None

        if self._root is None:
            print('Error: the tree is empty')
        else:
            # we can use SList with tail and head
            depth_level = 0

            list_nodes = SList()
            list_nodes.addLast(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                if current == node:
                    return depth_level
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)
                depth_level += 1

        print('Not found ', node.elem)
        return None

    def draw(self) -> None:
        "imprime el arbol en forma de diagrama"
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)