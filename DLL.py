class DLLError(Exception):
    """
    Class representing an error related to the DLL class implemented below.
    """
    pass

class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

class DLL:
    """
    Class representing a doubly linked list.
    """
    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    ######### MODIFY BELOW ##########

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.head is None:
            return True
        else:
            return False

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        current_head = self.head
        new_node = DLLNode(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
            self.tail = new_node
            return

        new_node.next = current_head
        current_head.prev = new_node
        self.head = new_node
        self.size += 1


    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        current_tail = self.tail
        new_node = DLLNode(value)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            self.size += 1

            return
        new_node.prev = current_tail
        current_tail.next = new_node
        self.tail = new_node
        self.size += 1


    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.head is None:
            raise DLLError
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
            return
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1


    def delete_back(self):
        """
        Deletes the back node of the list
        """
        current_tail = self.tail
        if current_tail is None:
            raise DLLError
        if current_tail.prev is None:
            self.head = None
            self.tail = None
            self.size = 0
            return
        current_tail.prev.next = None
        self.tail = current_tail.prev
        self.size -= 1

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        current_node = self.head
        if current_node is None:
            raise DLLError
        if self.size == 1:
            if current_node.value == value:
                self.size = 0
                self.tail = None
                self.head = None
                return None
            else:
                raise DLLError

        while current_node:
            if current_node.value == value:
                self.size -= 1
                if current_node is self.head:
                    current_node.next.prev = None
                    self.head = current_node.next
                    return
                if current_node is self.tail:
                    current_node.prev.next = None
                    self.tail = current_node.prev
                    return
                if current_node:
                    current_node.next.prev = current_node.prev
                    current_node.prev.next = current_node.next
                    return

            current_node = current_node.next
        raise DLLError



    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        current_node = self.head
        if current_node is None:
            raise DLLError
        if self.size == 1:
            if current_node.value == value:
                self.size = 0
                self.head = None
                self.tail = None
                return None
        counter = 0
        while current_node:
            if current_node.value == value:
                self.size -= 1
                counter += 1
                if current_node == self.head:
                    current_node.next.prev = None
                    self.head = current_node.next
                if current_node == self.tail:
                    current_node.prev.next = None
                    self.tail = current_node.prev
                else:
                    current_node.next.prev = current_node.prev
                    current_node.prev.next = current_node.next
            current_node = current_node.next
        if counter == 0:
            raise DLLError

    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        current_node = self.head
        if current_node is None:
            raise DLLError
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise DLLError
    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        current_node = self.head
        node_to_update = None
        if current_node is None:
            raise DLLError
        while current_node is not None:
            if current_node.value == value:
                node_to_update = current_node
            if current_node == self.tail:
                if node_to_update is not None:
                    return node_to_update
            current_node = current_node.next
        raise DLLError


    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        return_list = []
        current_node = self.head
        if current_node is None:
            raise DLLError
        while current_node:
            if current_node.value == value:
                return_list.append(current_node)
                if current_node.next is None:
                    if len(return_list) == 0:
                        raise DLLError
                    return return_list
            current_node = current_node.next
        if len(return_list) == 0:
            raise DLLError
        return return_list


    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        current_node = self.head
        count = 0
        while current_node:
            if current_node.value == value:
                count += 1
            current_node = current_node.next
        return count


    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        current_node = self.head
        if self.head is None:
            return None
        if current_node is self.head:
            total = current_node.value
            current_node = current_node.next
        while current_node:
            total += current_node.value
            current_node = current_node.next
        return total


def reverse(LL):
    """
    Reverses a linked list in place
    :param LL: The linked list to reverse
    """
    temp_node = None
    current_node = LL.head
    if LL.size == 1:
        return
    if LL.size == 0:
        return None
    while current_node:
        if current_node == LL.head:
            LL.tail = current_node
        temp_node = current_node.prev
        current_node.prev = current_node.next
        current_node.next = temp_node
        current_node = current_node.prev
    if temp_node is not None:
        LL.head = temp_node.prev


