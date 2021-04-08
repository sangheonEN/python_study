# 1개의 Node에 2개의 데이터가 있으니 class로 정의하는게 효율적
# Node 생성 [데이터, 다음 데이터 주소]

# 링크드 리스트 만들기 (add 함수 Build)
# 1. 다음 node를 가르키는 주소가 있으면
# 2. 다음 node에 접근하기 위해서 해당 node에 다음 node 주소를 저장
# 3. 마지막 node로 링크드 리스트가 끝났으면, 마지막 node의 주소 저장 구역에 새로 생성한 Node를 가르키게 한다.

class Node:
    def __init__(self, data, next_address = None):
        self.data = data
        self.next_address = next_address

def add(data):
    node = head
    while node.next_address:
        node = node.next_address
    node.next_address = Node(data)

# 링크드 리스트 만들기
node1 = Node(1)
head = node1
for i in range(2, 10):
    add(i)

# 링크드 리스트 출력하기
node_1 = head
while node_1.next_address:
    print(node_1.data)
    node_1 = node_1.next_address
print(node_1.data)



# class Node:
#     def __init__(self, data, address = None):
#         self.data =data
#         self.address = address
#
# def add(data):
#     node = head
#     while node.address:
#         node = node.address
#     node.address = Node(data)
#
# node1 = Node(1)
# head = node1
# for idx in range(2, 10):
#     add(idx)
#
# # 첫 번째 node 부터 탐색하기 위해 변수 head로 처음 node에 접근
# node = head
# while node.address:
#     print(node.data)
#     node = node.address
# print(node.data)

# # Node 생성 [데이터, 다음 데이터 주소]
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
# # Node 객체 생성 첫 번째 Node 만들고 연결하기
# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2 # node1에 저장되는 주소 배열에 node2의 주소값을 저장
# first_node = node1 # 첫 번째 node의 주소값을 알게됨

# # 링크드리스트를 구성하는 node1, node2 객체 생성
# node1 = Node(1)
# node2 = Node(2)
# # node1에 node2의 주소를 저장
# node1.address = node2
# # 이 링크드 리스트를 읽거나 탐색하려면 가장 앞의 Node의 정보를 미리 알아 두어야 한다.
# head = node1


