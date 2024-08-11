# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    
    #변환된 연결 리스트를 합하는 함수
    def addTwoNumbers(self, l1, l2):
        str1, str2 = "", ""
        while l1 or l2:
            if l1:
                char1 = str(l1.val)
                str1 = str1 + str(char1)
                l1 = l1.next
            if l2:
                char2 = str(l2.val)
                str2 = str2 + str(char2)
                l2 = l2.next        
        res = int(str1[::-1]) + int(str2[::-1])
        res = str(res)[::-1]
        res = list(map(int, str(res)))

        return self.toList(res)
    
    #입력받은 리스트를 연결 리스트로 변환하는 함수
    def toList(self, list):
        nodeList = ListNode()
        for i, val in enumerate(list):
            if i == 0:
                nodeList.val = val
            else :
                node = nodeList
                while node.next != None:
                    node = node.next
                node.next = ListNode(val)
        return nodeList

s = Solution()
li1 = [2,4,3]
li2 = [5,6,4]

nodelist1 = s.toList(li1)
nodelist2 = s.toList(li2)

result = s.addTwoNumbers(nodelist1, nodelist2)
print(result)
r = []

add_num=[s]
slsah=[]
while result:
    r.append(result.val)
    result = result.next
    
