class Bubble_sort():
    def __init__(self):
        n=int(input("enter the number of element = "))
        self.n=n
        self.list=[]
    def input_element(self):
        for i in range(self.n):
            data=int(input(f"enter element {i+1}="))
            self.list.append(data)
    def display(self):
        for i in self.list:
            print(i,end="\t")
        print()
    def sorting(self):
        for i in range(self.n):
            for j in range(self.n-1-i):
                if self.list[j]>self.list[j+1]:
                    temp=self.list[j]
                    self.list[j]=self.list[j+1]
                    self.list[j+1]=temp
sort=Bubble_sort()
sort.input_element()
sort.display()
sort.sorting()
print("element afler sorting=")
sort.display()
            
    
