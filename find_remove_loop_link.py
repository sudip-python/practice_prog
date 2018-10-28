class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        node = self.root
        while(node.next):
            node = node.next
        if node.next != None:
            raise Exception("Problemo")
        new_node = Node(value)
        node.next = new_node
        return new_node

    def find_loop(self):
        node = self.root
        if node.next == None or node.next.next == None:
            return False
        fast_pointer = node.next.next
        slow_pointer = node.next
        while fast_pointer and slow_pointer and fast_pointer.next:
            if fast_pointer == slow_pointer:
                self.remove_loop(slow_pointer)
                return True
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        return False

    def remove_loop(self, loop_node):
        cur_node = self.root
        l_start = loop_node.next
        last_node = loop_node
        found_match = False
        node_to_be_found = None
        while not found_match:
            if l_start == cur_node:
                node_to_be_found = last_node
                found_match = True
                last_node = l_start
                l_start = l_start.next
            cur_node = cur_node.next
        print node_to_be_found.value
        node_to_be_found.next = None

    def lprint(self):
        cur_node = self.root
        while cur_node:
            print cur_node.value
            cur_node = cur_node.next



ll = LinkedList(10)
n2 = ll.add(20)
ll.add(30)
n4 = ll.add(40)
n4.next = n2
print ll.find_loop()
ll.lprint()
