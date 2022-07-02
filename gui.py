arr = [5,4,3,2,1]

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
        ax.set_xlim(-1,10)
        right_side = ax.spines["right"]

        right_side.set_visible(False)
        ax.axis("off")
    def remove_circle(self, lr):
        if lr==1:
            self.circles.pop(0)
            self.circle_color.pop(0)
            self.circle_position.pop(0)
            self.arr.pop(0)
            self.length = self.length - 1
            
        else:
            
            self.circles.pop()
            self.circle_color.pop(0)
            self.circle_position.pop(0)
            self.arr.pop(0)
            self.length = self.length - 1
