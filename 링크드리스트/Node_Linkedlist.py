# 1개의 Node에 2개의 데이터가 있으니 class로 정의하는게 효율적

# Node 생성
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Node 객체 생성 첫 번째 Node 만들고 연결하기
node1 = Node(1)
node2 = Node(2)
node1.next = node2 # node1에 저장되는 주소 배열에 node2의 주소값을 저장
first_node = node1 # 첫 번째 node의 주소값을 알게됨

def add(data):
    