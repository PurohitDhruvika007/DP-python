class Quick_sort:
    def __init__(self, n):
        self.n = n
        self.list = []

    def input_element(self):
        for i in range(self.n):
            data = int(input("Enter the data: "))
            self.list.append(data)

    def display(self):
        for i in self.list:
            print(i, end="\t")
        print()

    # Hoare partition with pivot = first element
    def partition(self, low, high):
        pivot = self.list[low]  # first element as pivot
        i = low + 1
        j = high

        while True:
            # move i right until element > pivot
            while i <= j and self.list[i] <= pivot:
                i += 1

            # move j left until element < pivot
            while i <= j and self.list[j] >= pivot:
                j -= 1

            if i <= j:
                # swap arr[i], arr[j]
                self.list[i], self.list[j] = self.list[j], self.list[i]
            else:
                break

        # place pivot in correct position
        self.list[low], self.list[j] = self.list[j], self.list[low]
        return j

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def sorting(self):
        self.quick_sort(0, self.n - 1)


# Driver code
n = int(input("Enter number of elements: "))
q = Quick_sort(n)
q.input_element()
print("Before sorting:")
q.display()
q.sorting()
print("After sorting:")
q.display()
