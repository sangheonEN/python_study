# # 내가 짠 linked list code
# class Node:
#     def __init__(self, data, next_address=None):
#         self.data = data
#         self.next_address = next_address
#
# def first_Node(data):
#     node = Node(data)
#     head = node
#
#     return head
#
# def add(data, head):
#     node = head
#     while node.next_address:
#         node = node.next_address
#     node.next_address = Node(data)
#
# def list_result_out(head):
#     node_output = head
#     while node_output.next_address:
#         print(node_output.data)
#         node_output = node_output.next_address
#     print(node_output.data)
#
# def new_node_insert(head):
#     node = head
#     search = True
#     newnode = Node(22.3)
#     while search:
#         if node.data == 22:
#             search = False
#         else:
#             node = node.next_address
#
#     nownode_address = node.next_address
#     node.next_address = newnode
#     newnode.next_address = nownode_address
#
# if __name__ == "__main__":
#     head = first_Node(10)
#     for i in range(11, 30):
#         add(i, head)
#     list_result_out(head)
#     # 22.3 Node 추가
#     print("새로운 node 추가!!!")
#     new_node_insert(head)
#     list_result_out(head)

# 선생님이 짠 linked_list
# 1개의 Node 클래스, 1개의 Node 관리 class Build
class Node:
    def __init__(self, data, next_address = None):
        self.data = data
        self.next_address = next_address

class Node_Mgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        node = self.head
        while node.next_address:
            node = node.next_address
        node.next_address = Node(data)

    def output(self):
        node = self.head
        while node.next_address:
            print(node.data)
            node = node.next_address
        print(node.data)

    def insert(self, data):
        node = self.head
        new_node = Node(data)
        flag_search = True
        while flag_search:
            if node.data == 30:
                flag_search = False
            else:
                node = node.next_address
        now_node_address = node.next_address
        node.next_address = new_node
        new_node.next_address = now_node_address

if __name__ == "__main__":
    linkedlist = Node_Mgmt(0)

    for i in range(20, 40):
        linkedlist.add(i)
    linkedlist.insert(30.4)
    linkedlist.output()








