import os
os.system('cls')

#single Linkedlist
class Node :
    def __init__(self,value):
        self.value = value
        self.next = None
class linked_list:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
    def print_list(self):
        temp = self.head
        while temp is not None :
            print(temp.value)
            temp = temp.next
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True
    
    def bubble_sort(self):
        if self.head is None:
            return None
           
        for i in range(self.lenght -1,0,-1):
            current = self.head
            for i in range(i):
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next

    def selection_sort(self):
        if self.head is None:
            return None
        cur = self.head
        while cur:
            min_node = cur
            next_node = cur.next
            while next_node:
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = next_node.next
            temp = cur.value
            cur.value = min_node.value
            min_node.value = temp
            cur = cur.next

    def insertion_sort(self):
        if self.head is None:
            return
        
        sorted_list = None
        current = self.head
        while current is not None:
            next_node = current.next
            sorted_list = self.insert_sorted(sorted_list, current)
            current = next_node
        self.head = sorted_list
        
    def insert_sorted(self, sorted_list, node):
        if sorted_list is None or node.value < sorted_list.value:
            node.next = sorted_list
            return node
        
        current = sorted_list
        while current.next is not None and current.next.value < node.value:
            current = current.next
        node.next = current.next
        current.next = node
        return sorted_list
    def _merge_sort(self,head):

        if head is None or head.next is None:
            return head
    
        # Tìm giá trị giữa của danh sách
        middle = self.getMiddle(head)
        next_to_middle = middle.next
    
        # Phân chia danh sách thành hai nửa
        middle.next = None
    
        # Áp dụng mergeSort cho từng nửa
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)
    
        # Kết hợp hai danh sách đã sắp xếp để tạo ra một danh sách mới đã sắp xếp
        sorted_list = self.sortedMerge(left, right)
        return sorted_list  
    def merge_sort(self):
        return self._merge_sort(self.head)
    # Tìm giá trị giữa của danh sách
    def getMiddle(self,h):
        if (h == None):
            return h
     
        slow = h
        fast = h
     
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
         
        return slow
     
    # Kết hợp hai danh sách đã sắp xếp để tạo ra một danh sách mới đã sắp xếp
    def sortedMerge(self, a, b):
        # Nếu danh sách a rỗng, trả về danh sách b
        result = None
        if a is None:
            return b
     
        # Nếu danh sách b rỗng, trả về danh sách a
        if b is None:
            return a
     
        # So sánh giá trị đầu tiên của hai danh sách và chọn giá trị nhỏ hơn để làm node đầu của danh sách mới
        if a.value <= b.value:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
     
        return result
my_linkedlist =  linked_list(3)
my_linkedlist.append(2)
my_linkedlist.append(9)
my_linkedlist.append(5)
my_linkedlist.merge_sort()
my_linkedlist.print_list()
    