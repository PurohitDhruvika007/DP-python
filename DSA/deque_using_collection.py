from collections import deque
class Queue:
    def __init__(self,size=5):
        self.size=size
        self.queue=deque()
    def insert_right(self,data):
        if len(self.queue)<self.size:
            self.queue.append(data)
            print(f"data inserted from right = {data}")
        else:
            print("queue is overflow")
        
    def insert_left(self,data):
        if len(self.queue)<self.size:
            self.queue.appendleft(data)
            print(f"data inserted from left = {data}")
        else:
            print("queue is overflow")
    def delete_right(self):
        if len(self.queue)==0:
            print("queue is underflow")
            return
        return self.queue.pop()
    def delete_left(self):
        if len(self.queue)==0:
            print("queue is underflow")
            return
        return self.queue.popleft()
    def display(self):
        if self.queue is None:
            print("queue is underflow")
        else:
            for item in self.queue:
                print(item,end="\t");
q=Queue()
while(True):
    print("\n\n1.insert from right")
    print("2.insert from left")
    print("3.delete from right")
    print("4.delete from left")
    print("5.diplay")
    print("6.end the program")
    choice=int(input("enter the choice="))
    if(choice==1):
        data=int(input("enter the element="))
        q.insert_right(data)
    elif(choice==2):
        data=int(input("enter the element="))
        q.insert_left(data)
    elif(choice==3):
        data=q.delete_right()
        if data is not None:
            print("element deleted = ",data)
    elif(choice==4):
        data=q.delete_left()
        if data is not None:
            print("element deleted = ",data)
    elif(choice==5):
        q.display()
    elif(choice==6):
        print("bye bye! code is completed")
        break
    else:
        print("please enter the valid input!!")
    
    
















    
        









        
