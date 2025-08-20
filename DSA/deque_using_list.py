class Queue:
    def __init__(self):
        self.queue=[]
    def insert_right(self,data):
        print("data inserted from right: ")
        self.queue.append(data)
    def insert_left(self,data):
        print("data inserted from left:")
        self.queue.insert(0,data)
    def delete_right(self):
        if len(self.queue)!=0:
            return self.queue.pop()
        else:
            print("queue is underflow")
            return
    def delete_left(self):
        if len(self.queue)!=0:
            return self.queue.pop(0)
        else:
            print("queue is underflow")
            return
    def display(self):
        if self.queue is None:
            print("queue is empty")
        else:
            for item in self.queue:
                print(item,end="\t")
q=Queue()

while(True):
    print("\n\n1.insert from right")
    print("2.insert from left")
    print("3.delete from right")
    print("4.delete from left")
    print("5.display all elements")
    print("6.exit the code")
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
            print("deleted element is ",data)
    elif(choice==4):
        data=q.delete_left()
        if data is not None:
            print("deleted element is ",data)
    elif(choice==5):
        q.display()
    elif(choice==6):
        print("code is ended")
        break
    else:
        print("please enter the valid input")















        
        
