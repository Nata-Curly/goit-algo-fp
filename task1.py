class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort_linked_list_insertion(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, head, new_node):
        if head is None or head.data >= new_node.data:
            new_node.next = head
            return new_node

        current = head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return head

    def merge_sorted_lists(self, list1, list2):
        dummy_node = Node(0)
        tail = dummy_node

        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break

            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        return dummy_node.next


llist = LinkedList()

llist.insert_at_beginning(3)
llist.insert_at_end(5)
llist.insert_at_end(12)
llist.insert_at_end(9)
llist.insert_at_end(15)

print("\nЗв'язний список до реверсування:")
llist.print_list()
llist.reverse_linked_list()
print("\nЗв'язний список після реверсування:")
llist.print_list()

llist1 = LinkedList()
llist2 = LinkedList()

llist1.insert_at_end(5)
llist1.insert_at_end(10)
llist1.insert_at_end(15)

llist2.insert_at_end(2)
llist2.insert_at_end(12)
llist2.insert_at_end(7)
llist2.insert_at_end(8)

llist1.sort_linked_list_insertion()
print("-" * 40)
print("\nПерший відсортований зв'язний список:")
llist1.print_list()

llist2.sort_linked_list_insertion()
print("\nДругий відсортований зв'язний список:")
llist2.print_list()

merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(llist1.head, llist2.head)
print("-" * 40)
print("\nОб'єднаний відсортований зв'язний список:")
merged_list.print_list()
