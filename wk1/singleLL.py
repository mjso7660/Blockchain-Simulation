# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:35:14 2018

@author: Min Joon So, Shailesh Patro
Blockchain wk1 assignment
"""
class Node:
    '''
    class node for doubly linked list
    '''
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def get_value(self, key):
        '''
        returns a corresponding value for the given key
        '''
        temp = self.head
        while temp is not None:
            if temp.key is key:
                return temp.value
            temp = temp.next
        if temp is None:
            return None
    
    def push(self, key, value):
        '''
        adds a new node at the head
        '''
        if not self.check_key(key):
            return
        new_node = Node(key, value)
        new_node.next = self.head

        self.head = new_node
        
    def append(self, key, value):
        '''
        append a new node at the tail
        '''
        if not self.check_key(key):
            return
        new_node = Node(key, value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        if temp.next is None:
            temp.next = new_node     
 
    def delete(self, key):
        '''
        deletes a node with given key
        '''
        if self.head.key is key:
            self.head = self.head.next
        temp = self.head
        while temp.next is not None:
            if temp.next.key is key:
                temp.next = temp.next.next
                break
            temp = temp.next
        temp = None
        return                                    
        
    def insert_after_key(self, loc, key, value = None):
        '''
        searches for a given key and inserts a new node with 'key'' and 'value' after
        loc: key of the node after which a new node will be inserted
        '''
        if not self.check_key(key):
            return
        temp = self.head
        while temp is not None:
            if temp.key is loc:
                new_node = Node(key, value)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next
        if temp is None:
            print("not found")
            
    def insert_after_node(self, original_node, node_insert):
        if node_insert.next is not None:
            print("Error")
            return
        if original_node.next is None:
            original_node.next = node_insert
            return
        node_insert.next = original_node.next
        original_node.next = node_insert
        return
            
    def traversal(self):
        '''
        prints all keys and values
        '''
        temp = self.head
        if temp is None:
            return None
        while temp is not None:
            print(temp.key,temp.value)
            temp = temp.next
        return
    
    def reverse(self):
        '''
        reversed a list
        '''
        current = self.head                 # Initialize current to start of list (head)
        previous = None                     # Since we want the new tail to point to None and since there is no node before
        while (current != None):            # Initiate a while loop that runs as long as current node is not null, loop
            nextnode =  current.next        # Create a pointing variable called "nextnode" to next node
            current.next = previous         # Set current node to previous (for the first run, head node points to None/Null), now we are breaking the link of the first node to second node, this is where nextnode is used)
            previous = current              # Move previous 
            current = nextnode              # Move current
        self.head = previous                # When the loop is complete move the head to last node (new head of list)
    
    def check_key(self, new_key):
        '''
        new_key: key of a new node to be inserted
        returns True if new_key doesn't overlap with anyother keys. If the key already exits, return False
        '''
        temp = self.head
        while temp is not None:
            if temp.key is new_key:
                print("key alread exists")
                return False
            temp = temp.next
        return True

# End of class definition
# Start of public functions

def deep_copy(llist):
    '''
    llist: linked list to copy
    returns a deep copy of given linked list
    '''
    new_llist = LinkedList()
    temp = llist.head
    while temp is not None:
        new_node = Node(temp.key, temp.value)
        if new_llist.head is None:
            new_llist.head = new_node
        llist.insert_after_node(temp, new_node)
        temp = temp.next.next
    temp = llist.head
    while temp is not None:
        next_node = temp.next
        if next_node.next is None:
            temp.next = None;
            return new_llist
        temp.next = next_node.next
        next_node.next = temp.next.next
        temp = temp.next
    return new_llist
    
def check_same(llist1,llist2):
    '''
    checks if given linked lists are the identical
    '''
    temp1 = llist1.head
    temp2 = llist2.head
    while temp1 is not None and temp2 is not None:
        if (temp1.key, temp1.value) != (temp2.key, temp2.value):
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1 is not None or temp2 is not None:
        return False
    return True


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1,'Min Joon')
    llist.push(3,'Shailesh')
    llist.push(2,'Blockchain')
    llist.push(2,'error')       #key '2' already exists
    llist.push(5,'CooperUnion')
    llist.push(4,1)
    llist.push(6,3.141)
    llist.insert_after_key(2, 8, 7)
    llist.insert_after_key(5, 7, '*')
    llist.append(0,'a')
    llist.append(9, 4)
    #print keys and values
    llist.traversal()
    print("----")
    #deep-copy, reversed
    new_list = deep_copy(llist)
    new_list.reverse()
    new_list.traversal()
    print("----")
    #check if they match
    print(check_same(new_list,llist))
