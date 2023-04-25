
class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class SList:
    "Esta es la implementación de una lista enlazada simple. Usamos una referencia al primer nodo, llamado head"
    def __init__(self):
        "Este constructor crea una lista vacía"
        self.head = None
        self.size = 0

    def __len__(self):
        "Devuelve el tamaño de la lista"
        return self.size
    
    def isEmpty(self):
        "Devuelve True si la lista está vacía"
        return len(self) == 0
    
    def __str__(self):
        "Devuelve una cadena con los elementos de la lista"
        result = ''
        nodeIt = self.head
        while nodeIt:
            result += ',' + str(nodeIt.elem)
            nodeIt = nodeIt.next
        if len(result) > 0:
            result = result[1:]
        return result
    
    def addFirst(self, e):
        "Añade un nuevo elemento e al principio de la lista"
        # Creamos el nuevo nodo
        newNode = Node(e)
        # El nuevo nodo debe apuntar al nodo actual head
        newNode.next = self.head
        # Actualizamos la referencia head para que apunte al nuevo nodo
        self.head = newNode
        # Aumentamos el tamaño de la lista
        self.size += 1

    def addLast(self, e):
        "Añade un nuevo elemento e al final de la lista"
        newNode = Node(e)
        if self.isEmpty():
            self.head = newNode
        else:
            # Nos movemos por la lista hasta llegar al último nodo
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            # El último nodo apunta al nuevo nodo
            lastNode.next = newNode
        # Aumentamos el tamaño de la lista
        self.size += 1

    def add(self, e, pos):
        "Añade un nuevo elemento e en la posición pos"
        if pos < 0 or pos > len(self):
            raise IndexError
        if pos == 0:
            self.addFirst(e)
        elif pos == len(self):
            self.addLast(e)
        else:
            newNode = Node(e)
            nodeIt = self.head
            for i in range(pos - 1):
                nodeIt = nodeIt.next
            newNode.next = nodeIt.next
            nodeIt.next = newNode
            self.size += 1

    def removeFirst(self):
        "Elimina el primer elemento de la lista"
        if self.isEmpty():
            raise IndexError
        self.head = self.head.next
        self.size -= 1

    def removeLast(self):
        "Elimina el último elemento de la lista"
        if self.isEmpty():
            raise IndexError
        if len(self) == 1:
            self.head = None
        else:
            nodeIt = self.head
            while nodeIt.next.next:
                nodeIt = nodeIt.next
            nodeIt.next = None
        self.size -= 1

    def getAt(self, index):
        "Devuelve el elemento de la posición index"
        result = None
        if index not in range(0, len(self)):
            print(index, 'Error getAt: indice fuera de rango')
        else:
            nodeIt=self._head
            i=0
            while nodeIt and i<index:
                nodeIt=nodeIt.next
                i+=1

            #nodeIt is at the position index
            result=nodeIt.elem

        return result
    
    def index(self, e):
        "Devuelve la primera posición de e en la lista"
        nodeIt = self.head
        index = 0
        while nodeIt:
            if nodeIt.elem == e:
                return index
            nodeIt = nodeIt.next
            index += 1
        return -1
    
    def insertAt(self, index, e):
        "Inserta un nuevo elemento e en la posición index"
        # Primero comprobamos que el índice sea válido.
        if index not in range(0, len(self) + 1):
            print(index, 'Error insertAt: indice fuera de rango')
        elif index == 0:
            self.addFirst(e)
        elif index == len(self):
            self.addLast(e)
        else:
            # Necesitiamos llegar al nodo anterior(el nodo del index-1)
            previous = self._head
            for i in range(index - 1):
                previous = previous.next
            # Ahora previous apunta al nodo anterior al que queremos insertar
            # Creamos el nuevo nodo
            newNode = Node(e)
            # El nuevo nodo apunta al nodo siguiente al que queremos insertar
            newNode.next = previous.next
            # El nodo anterior al que queremos insertar apunta al nuevo nodo
            previous.next = newNode
            # Aumentamos el tamaño de la lista
            self.size += 1

    def removeAt(self, index):
        "Elimina el elemento de la posición index"
        result = None
        # Primero comprobamos que el índice sea válido.
        if index not in range(0, len(self)):
            print(index, 'Error removeAt: indice fuera de rango')
        elif index == 0:
            self.removeFirst()
        elif index == len(self) - 1:
            self.removeLast()
        else:
            # Necesitamos llegar al nodo anterior
            previous = self._head
            for i in range(index - 1):
                previous = previous.next
            # Ahora previous apunta al nodo anterior al que queremos eliminar
            # El nodo anterior al que queremos eliminar apunta al nodo siguiente al que queremos eliminar
            result = previous.next.elem
            previous.next = previous.next.next
            # Disminuimos el tamaño de la lista
            self.size -= 1
        return result







            
