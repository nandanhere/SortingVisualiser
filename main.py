
from sorting import Sorting
import pygame_menu
import pygame,math,random,time
from pygame.display import update
from pygame.draw import rect
import matplotlib.cm as cm
import numpy as np
# TODO : make the window resizable
pygame.init()
running = True
w = 1200 
h = 800
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('sorter')
num = 200
arr = [random.randint(0,num - 2) for _ in range(num)]
cycle = []

maximum = max(arr)
fromx = 0;xinc = 1
fromy = 0;yinc = 1
height = h // maximum
width = w // maximum
sortingClass = Sorting(fromx,fromy,width,height,screen,cycle)
isSorted = False
func = sortingClass.bubbleSort
def selectAlgo(_,i):
    global sortingClass,arr,func
    l = ["","bubbleSort","insertSort","selectionSort","mergeSort","quickSort","heapSort"]
    func = getattr(sortingClass,l[i])
def selectColor(_,i):
    global sortingClass
    cycle = []
    l = ["","rainbow","gray","summer","prism"]
    f = getattr(cm,l[i])
    for [r,g,b,_] in f(np.linspace(0, 1, num)):
        r *= 255
        g *= 255
        b *= 255
        cycle.append((r,g,b))
    sortingClass.cycle = cycle
selectColor(None,1)
    
def sortIt():
    func(arr)
def reset():
    global arr
    arr = [random.randint(0,num - 2) for _ in range(num)]
menu = pygame_menu.Menu('Sorting Visualiser', w, h,
                       theme=pygame_menu.themes.THEME_DARK) #type:ignore
menu.add.button('Start', sortIt)
menu.add.button('Reset array', reset)
menu.add.dropselect('Algorithm :', [('Bubble Sort', 1), ('Insert Sort', 2),("Selection Sort",3),("Merge Sort",4),("Quick Sort",5),("Heap Sort",6)], onchange=selectAlgo)
menu.add.dropselect('Color Scheme :', [('Rainbow', 1), ('Black / White', 2),("Summer",3),("Prism",4)], onchange=selectColor)
menu.add.button('Quit', pygame_menu.events.EXIT) #type:ignore

while running:
    menu.mainloop(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
