from numpy import true_divide
from pygame.display import update
import pygame,sys,time
class Sorting:
    arr = []
    def __init__(self,fromx,fromy,width,height,screen,cycle):
        self.fromx = fromx
        self.fromy = fromy
        self.width = width
        self.height = height
        self.screen = screen
        self.cycle = cycle
        (self.x,self.y) = self.screen.get_size()
    def checkIfQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False
        
    def drawOnScreen(self,name,arr):
        self.screen.fill((0,0,0))
        for k in arr:
            hei = self.height * k
            pygame.draw.rect(self.screen,self.cycle[k],(self.fromx,self.y - hei,self.width,hei))
            self.fromx += self.width 
        self.fromx = 0
        font = pygame.font.Font('freesansbold.ttf',32)
        showName = font.render(name,True,(255,255,255))
        self.screen.blit(showName,(0,00))
        pygame.display.update()
    def bubbleSort(self,arr):
        global fromx, fromy,width,height
        for i in range(len(arr) - 1):
            if self.checkIfQuit(): return
            for j in range(i + 1,len(arr)):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
                    self.drawOnScreen('Bubble Sort',arr)
    def selectionSort(self,arr):
        n = len(arr)
        for i in range(n):
            if self.checkIfQuit() : return
            small = i
            for j in range(i + 1,n):
                if arr[j] < arr[small]:
                    small = j
            self.screen.fill((0,0,0))
            arr[small],arr[i] = arr[i],arr[small]
            self.drawOnScreen("Selection Sort",arr)
    def insertSort(self,arr):
        n = len(arr)
        for i in range(1,n):
            if self.checkIfQuit(): return
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.drawOnScreen("Insert Sort",arr)
    def mergeSort(self,arr):
        global truth
        truth = False
        temp = arr
        def merge(b,c,a,base):
            global truth
            i = j = k = 0
            p = len(b); q = len(c)
            while(i < p and j < q):
                if truth: return
                if b[i] <= c[j]:
                    a[k] = b[i] ; i += 1
                else:
                    a[k] = c[j] ; j += 1
                if self.checkIfQuit():
                     truth = True
                k += 1
            if i == p:
                a[k : p + q ] = c[j : q]
            else:
                a[k : p + q] = b[i : p]
            temp[base : base + p + q] = a
            self.drawOnScreen("MergeSort",temp)
            return a
        def mergesort(a,base):
            global truth
            if truth: return
            n = len(a)
            if self.checkIfQuit(): return
            if(n > 1):
                b =  a[0 :(n//2)]
                c = a[(n//2) : n]
                mergesort(b,base)
                mergesort(c,n//2)
                merge(b,c,a,base)
            return a
        mergesort(arr,0)
    def quickSort(self,arr):
        global truth;truth = False
        def partition(a,l,r) -> int:
            global truth
            #takes a subarray and returns the partition position
            pivot = a[l]
            i = l 
            for k in range(l, r + 1):
                if truth : return -1
                if self.checkIfQuit():
                 truth = True
                if a[k] <= pivot:
                    a[i], a[k] = a[k] , a[i]
                    i += 1
                    self.drawOnScreen("QuickSort",a)
            a[i - 1], a[l] = a[l], a[i - 1]
            self.drawOnScreen("QuickSort",a)
            return i - 1
        def quicksort(a,l,r):
            global truth
            if(l < r) and not truth:
                s  =  partition(a,l,r)  
                quicksort(a,l,s - 1)
                quicksort(a,s + 1, r)
        self.drawOnScreen("QuickSort",arr)
        quicksort(arr,0,len(arr) - 1)
    def heapSort(self,a):
            global truth
            truth = False
            def max_heap(arr,n,parent):
                global truth
                if truth : return
                if self.checkIfQuit():
                    truth = True
                largest = parent
                left =  2 * parent + 1 # Left = 2*i... here we did taking into consideration array starts at 0
                right = 2 * parent + 2 # Right = 2 * i + 1

                if left < n and arr[left] > arr[largest]:
                    largest = left
                if right < n and arr[right] > arr[largest]:
                    largest = right 
                if largest != parent:
                    arr[largest],arr[parent] = arr[parent],arr[largest]
                    self.drawOnScreen("Heap Sort",arr)
                    max_heap(arr,n,largest)
            def heapsortWithMaxHeap(arr):
                n = len(arr)
                global truth
                if truth : return
                for i in range(n // 2 - 1, -1, -1):
                        max_heap(arr,n, i)
                for i in range(n - 1, 0, -1):
                        arr[i],arr[0] = arr[0],arr[i]
                        max_heap(arr, i, 0)
            heapsortWithMaxHeap(a)

