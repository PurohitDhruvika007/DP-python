class Selection_sort:
    def __init__(self,n):
        self.list=[]
        self.n=n
    def input_element(self):
        for i in range(self.n):
            data=int(input(f"enter {i+1} element="))
            self.list.append(data)
    def display(self):
        for i in self.list:
            print(i,end="\t")
        print()
    def sorting(self):
        for i in range(self.n):
            for j in range(i+1,self.n):
                if self.list[i]>self.list[j]:
                    temp=self.list[j]
                    self.list[j]=self.list[i]
                    self.list[i]=temp
n=int(input("enter the number of element="))
sort=Selection_sort(n)
sort.input_element()
sort.display()
sort.sorting()
print("elements after sorting = ")
sort.display()

        
