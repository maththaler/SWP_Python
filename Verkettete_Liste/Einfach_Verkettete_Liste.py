
class Node:
    def __init__(self, sequence) -> None:
        self.sequence = sequence
        self.head = None


class Einfach_Verkettete_Liste:
    def __init__(self, sequence=None) -> None:
        self.index = 0
        self._len = 0
        if sequence is not None:
            self.head = Node(sequence)
            self._len += 1

    def insert_at_beginning(self, sequence):
        self._len += 1
        node = Node(sequence)
        if self.head is None:
            self.head = node
        else:
            node.head = self.head
            self.head = node

    def insert_at_end(self, sequence):
        self._len += 1
        new_node = Node(sequence)
        node = self.head
        while node.head is not None:
            node = node.head
        node.head = new_node

    def __len__(self):
        return self._len
    
    def all_elements(self):
        l = []
        node = self.head
        while node is not None:
            l.append(node.sequence)
            node = node.head
        return l
    
    def __iter__(self):
        return self
    
    def get_element_index(self, index):
        if index < self._len:
            node = self.head
            for _ in range(index):
                node = node.head
            return node.sequence
        else:
            return None

    
    def __next__(self):
        #Frage: Als Liste einfach all_elemts hernehmen?
        if self.head is None:
            raise StopIteration
        if self.index < self._len:
            node = self.head
            for _ in range(self.index):
                node = node.head
            self.index += 1
            return node.sequence
        else:
            self.index = 0
            raise StopIteration


    


if __name__ == "__main__":
    evk = Einfach_Verkettete_Liste(1)
    evk.insert_at_beginning(2)
    evk.insert_at_end(3)
    print(evk.all_elements())
    print(len(evk))
    print(evk.get_element_index(3))
    for a in evk:
        print(a)

    print("XXX")
    for b in evk:
        print(b)
