"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # track new nodes in array
        # connect all new nodes
        # track old index
        # 
        index_dict = {}
        nodes_list = []
        curr = head

        while curr:
            index_dict[curr] = len(nodes_list)
            new_node = Node(curr.val)
            nodes_list.append(new_node)
            curr = curr.next
        
        for index, node in enumerate(nodes_list):
            if index != 0:
                nodes_list[index - 1].next = node


        for old_node, index in index_dict.items():
            if not old_node.random:
                continue
            new_node = nodes_list[index]
            random_index = index_dict[old_node.random]
            new_node.random = nodes_list[random_index]
        return nodes_list[0] if nodes_list else None
                





