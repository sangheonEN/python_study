class Node:
    def __init__(self, data, next_address = None):
        self.data = data
        self.next_address = next_address

def add(data):
    node_a = head
    while node_a.next_address:
        node_a = node_a.next_address
    node_a.next_address = Node(data)

node1 = Node(1)
head = node1
for i in range(2, 10):
    add(i)

node_output = head
while node_output.next_address:
    print(node_output.data)
    node_output = node_output.next_address
print(node_output.data)

print("new node insert!!!!!")

# 링크드 리스트 사이에 하나의 원소를 넣고 싶다. 1 <1.5> 2 3 4 .. 9  <1.5> 값을 넣고 싶다.
# 1. Node1가 가르키는 다음 Node 주소를 <1.5>값이 있는 Node로 가르킴
# 2. <1.5> 값이 있는 Node에서 2 값이 있는 Node 주소를 가르키게함.
# 3. node1이 가르키는 node2로의 주소를 저장하고
# 4. 지금 node1에서 node1.5 주소를 가르키게하고
# 5. node1.5를 node2의 주소를 가르키게 한다.

node_insert = head
search = True
node_new = Node(1.5)
while search:
    if node_insert.data == 1:
        # print(node_insert.data)
        search = False
    else:
        node_insert = node_insert.next_address

node_2_address = node_insert.next_address
node_insert.next_address = node_new
node_new.next_address = node_2_address

node_insert = head
while node_insert.next_address:
    print(node_insert.data)
    node_insert = node_insert.next_address
print(node_insert.data)



















