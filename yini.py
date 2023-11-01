import random

numlist=random.sample(range(0,10),5)

while numlist[0]==0:

    numlist=random.sample(range(0,10),5)

num=int(''.join([str(i) for i in numlist]))

inputnum=int(input("输入号："))

bonus=0

count=0

if inputnum==num:

 bonus=10000

else:

 for i in set(str(inputnum)):

  if int(i) in numlist:

   count+=1

 bonus=1000*count

print("彩票号：%d" % num)

print("奖皮山金：前唤%d元" % bonus)

(注意源代码的缩进)

#!/usr/bin/python
from Tkinter import *
import random
class snake(Frame):
        def __init__(self, master=None):
 宴和改               Frame.__init__(self, master)
                 = [(0,0)]
                id = []
                 = [ -1, -1 ]
                id = -1
                count = 10
                 = 500
                 = 3
                self.speed = 500
                 = self.winfo_toplevel()
                .resizable(False, False)
                ()
                self.canvas = Canvas(self)
                ()
                self.canvas.config(, ,relief=RIDGE)
                self.drawgrid()
                s = 
                id = self.canvas.create_rectangle([0][0]*s,[0][1]*s,
                        ([0][0]+1)*s, ([0][1]+1)*s, fill="yellow")
                id.insert(0, id)
                self.bind_all("<KeyRelease>", self.keyrelease)
                self.drawfood()
                self.after(self.speed, self.drawsnake)
        def drawgrid(self):
                s = 
                for i in range(0, count+1):
                        self.canvas.create_line(i*s, 0, i*s, )
                        self.canvas.create_line(0, i*s, , i*s)
        def drawsnake(self):
                s = 
                head = [0]
                new = [head[0], head[1]]
                if  == 1:
                        new[1] = (head[1]-1) % count
                elif  == 2:
                        new[0] = (head[0]+1) % count
                elif  == 3:
                        new[1] = (head[1]+1) % count
                else:
                        new[0] = (head[0]-1) % count
                next = ( new[0], new[1] )
                if next in :
                        exit()
                elif next == ([0], [1]):
                        .insert(0, next)
                      晌判  id.insert(0, id)
                        self.drawfood()
                else:
                        tail = ()
                        id = ()
                        (id, (next[0]-tail[0])*s, (next[1]-tail[1])*s)
             棚和           .insert(0, next)
                        id.insert(0, id)
                self.after(self.speed, self.drawsnake)
        def drawfood(self):
                s = 
                x = random.randrange(0, count)
                y = random.randrange(0, count)
                while (x, y) in :
                        x = random.randrange(0, count)
                        y = random.randrange(0, count)
                id = self.canvas.create_rectangle(x*s,y*s, (x+1)*s, (y+1)*s, fill="yellow")
                [0] = x
                [1] = y
                id = id
        def keyrelease(self, event):
                if event.keysym == "Up" and  != 3:
                         = 1
                elif event.keysym == "Right" and  !=4:
                         = 2
                elif event.keysym == "Down" and  != 1:
                         = 3
                elif event.keysym == "Left" and  != 2:
                         = 4
app = snake()
app.master.title("Greedy Snake")
app.mainloop()
————————————————
版权声明：本文为CSDN博主「chatgpt002」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/chatgpt002/article/details/132019972
