# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# self
# In Python, self refers to the instance of the class that is calling the method.
# When defining methods inside a class, the first parameter of each method must be self

# Why is "self" needed?
# When you call a method on an instance of a class (for example, my_solution.deleteNode(node)), Python automatically passes the instance (my_solution) as the first argument to the method. By convention, this first argument is named self.

# Why is self required even though it's not used inside deleteNode?
# It's required by Python's syntax for all instance methods in a class.
# It provides consistency across the code so that methods can always reference the instance they belong to, even if in this case it’s not strictly necessary.

