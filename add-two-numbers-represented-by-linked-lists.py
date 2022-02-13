#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def reverse(head):
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr :
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        
        l1 = reverse(first)
        l2 = reverse(second)
        head = l1
        prev = None
        c = 0
        sum = 0
        while l1 is not None and l2 is not None:
            sum = c+l1.data+l2.data
            l1.data = sum%10
            c = int(sum//10)
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l1 is not None or l2 is not None:
            if l2 is not None:
                prev.next = l2
            l1 = prev.next
            while l1 is not None:
                sum = c+l1.data
                l1.data = sum%10
                c = int(sum/10)
                prev = l1
                l1 = l1.next
        if c>0:
            prev.next = Node(c)
        return reverse(head)
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
