class Queue:
    def  __init__(self,n):
        self.rear=-1
        self.front=-1
        self.queue=[None]*n
        self.n=n
    def enqueue(self,data):
        if self.rear==self.n-1:
            print("queue overflow")
            return
        self.rear+=1
        self.queue[self.rear]=data
        if self.front==-1:
            self.front=0
    def dequeue(self):
        if self.front==-1:
            print("queue underflow")
            return
        else:
            data=self.queue[self.front]
            self.front+=1
            if self.rear<self.front:
                self.rear=self.front=-1
            return data
    def display(self):
        if self.front!=-1:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
        else:
            print("queue is empty")
    def is_empty(self):
        if self.front==-1:
            print("queue is empty")
        else:
            print("queue is not empty")
    def is_full(self):
        if self.rear==self.n-1:
            print("queue is full")
        else:
            print("queue is not full")

n=int(input("enter the size of queue="))
q=Queue(n)
while(True):
    print("\n\n\nselect from the fillowing option:")
    print("1.enqueue")
    print("2.dequeue")
    print("3.display")
    print("4.is empty")
    print("5.is full")
    print("6.exit")
    choice=int(input("enter the choice="))
    if choice==1:
        data=int(input("enter the data="))
        q.enqueue(data)
    elif choice==2:
        data=q.dequeue()
        print("deleted element is = ",data)
    elif choice==3:
        q.display()
    elif choice==4:
        q.is_empty()
    elif choice==5:
        q.is_full()
    elif choice==6:
        print("bye bye ! this code is compleated")
        break
    else:
        print("enter the valid choice")


           













            
    
