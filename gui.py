import matplotlib.pyplot as plt
import random

#arr = [5,4,3,2,1]

class GUI:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.circles = []
        self.circle_color = []
        self.circle_position = []
        x = 1
        for i in range(self.length):
            color = '#{:06x}'.format(random.randrange(254**3))
            circle = plt.Circle(( x , 1 ), 1 , color = color)
            self.circles.append(circle)
            self.circle_color.append(color)
            self.circle_position.append(x)
            x+=2
            
    def plot(self):
        fig, ax = plt.subplots()
        ax = fig.add_subplot(111)
        for i in range(self.length):
            label = ax.annotate(str(self.arr[i]), xy=(self.circle_position[i], 1), fontsize=10, ha="center")
            ax.add_artist( self.circles[i] )   
        ax.set_ylim(-2,4)
        ax.set_xlim(0,self.length*2)
        right_side = ax.spines["right"]

        right_side.set_visible(False)
        ax.axis("off")
    def remove_circle(self, lr):
        if lr == 'l':
            self.circles.pop(0)
            self.circle_color.pop(0)
            self.circle_position.pop(0)
            self.arr.pop(0)
            self.length = self.length - 1
            
        elif lr == 'r':
            self.circles.pop(self.length - 1)
            self.circle_color.pop(self.length - 1)
            self.circle_position.pop(self.length - 1)
            self.arr.pop(self.length - 1)
            self.length = self.length - 1