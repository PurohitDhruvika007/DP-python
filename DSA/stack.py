class Stack:
    def __init__(self,n):
        self.n=n
        self.stack=[0]*n
        self.top=-1
    def push(self,elem):
        if self.top==self.n-1:
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=elem
        print(f"element added in stack={self.stack[self.top]}")
    def pop(self):
        if self.top==-1:
            print("stack is underflow")
            return
        elem=self.stack[self.top]
        self.top-=1
        print(f"poped elemnent is {elem}")
    def peep(self,position):
        if self.top==-1:
            print("stack is underflow")
            return
        return (self.stack[(self.top-position)+1])
    def update(self,position,x):
        if self.top==-1:
            print("stack is underflow")
            return
        self.stack[(self.top-position)+1]=x
        print(f"after changing the element in stack {self.stack}")
    def display(self):
        if self.top==-1:
            print("stack is underflow")
            return
        for i in range(self.top,-1,-1):
            print(f"stack{i}={self.stack[i]}")
    def isEmpty(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("stack is not empty")
    def isFull(self):
        if self.top==self.n-1:
            print("stack is full")
        else:
            print("stack is not full")
if __name__=="__main__":
    n=int(input("enter the n="))
    st=Stack(n)
    while(True):
        print("1=push")
        print("2=pop")
        print("3=peep")
        print("4=update")
        print("5=display")
        print("6=is empty")
        print("7=is full")
        print("8=exit")
        choice=int(input("enter your choice from 1 to 8="))
        if(choice==1):
            elem=int(input("enter the element="))
            st.push(elem)
        elif(choice==2):
            st.pop()
        elif(choice==3):
            position=int(input("enter the position="))
            store=st.peep(position)
            print(f"the element on this position is {store}")
        elif(choice==4):
            position=int(input("enter the position="))
            x=int(input("the new element to be placed="))
            st.update(position,x)
        elif(choice==5):
            st.display()
        elif(choice==6):
            st.isEmpty()
        elif(choice==7):
            st.isFull()
        elif(choice==8):
            print("byee....byee....")
            break
        else:
            print("please enter the valid choice")

        
