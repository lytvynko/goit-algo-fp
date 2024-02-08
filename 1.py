class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_list_from_array(arr):
    head = ListNode(arr[0]) if arr else None
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()        

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

arr = [3, 1, 4, 2]
head = create_list_from_array(arr)

reversed_head = reverse_linked_list(head)
print("Реверсований список:")
print_list(reversed_head)

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    left_half, right_half = split_list(head)
    left = merge_sort_linked_list(left_half)
    right = merge_sort_linked_list(right_half)

    return merge_sorted_lists(left, right)

def split_list(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow.next
    slow.next = None
    return head, middle

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

print("Завдання 1:")
print("Оригінальний список:")
print_list(head)

sorted_head = merge_sort_linked_list(reversed_head)
print("\nЗавдання 2:")
print("Відсортований список:")
print_list(sorted_head)

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
list1 = create_list_from_array(arr1)
list2 = create_list_from_array(arr2)
print("\nЗавдання 3:")
print("Перший відсортований список:")
print_list(list1)
print("Другий відсортований список:")
print_list(list2)
merged_head = merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
print_list(merged_head)