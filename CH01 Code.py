# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:17:34 2024

@author: Suubane Mahamed
"""

'Part Two ANswers'

'CH01 Q: 1:'

"""
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

x = np.linspace(-10, 10, 100)
ax.plot(x, x, 'k', linewidth=2)  # y = x (black)
ax.plot(x, -x, 'k', linewidth=2)  # y = -x (black)


ax.plot(x, x + 2, 'b', linewidth=3)  # y = x + 2 (blue)
ax.plot(x, x - 2, 'b', linewidth=3)  # y = x - 2 (blue)
ax.plot(x, -x + 2, 'b', linewidth=3)  # y = -x + 2 (blue)
ax.plot(x, -x - 2, 'b', linewidth=3)  # y = -x - 2 (blue)


rect = plt.Rectangle((-10, -10), 20, 20, linewidth=3, edgecolor='r', facecolor='bullet')
ax.add_patch(rect)


ax.grid(True, linestyle='--', alpha=0.7)
ax.set_aspect('equal', 'box')  # Keep the aspect ratio square

ax.set_xticks([])
ax.set_yticks([])


ax.text(0, 0, 'Write your Full Name Here', fontsize=12, ha='center', va='center')

plt.show()

"""

"""

'CH01 Q: 2''CH01 Q: 3' 'CH01 Q: 9'

import numpy as np
import pylab as plt

fig,ax = plt.subplots()

for i in range(30):
    angle = 2 * np.pi * i / 30
    x = 2 * np.cos(angle) 
    y = 2 * np.sin(angle)  
    circle = plt.Circle((x, y), 2, color='k', fill=False, linewidth=1)
    ax.add_patch(circle)


plt.axis('equal')
plt.grid()

plt.show()


"""

"""

# 'CH01 Q: 4' 'CH01 Q: 6' 'CH01 Q: 7'
import pylab as plt
fig,ax=plt.subplots()
squares=[
    
        #((-2,-2),18,'r',),
        #((-1,-1),16,'r'),
        #((0,0),14,'r'),
        ((1,1),6,'b'),
        ((4,4),6,'y'),
        ((7,7),6,'g'),
       
        
        
        
        ]
for square in squares:
    circle=plt.Rectangle(square[0], square[1], square[1], edgecolor=square[2],fill=False,linewidth=3)
    ax.add_patch(circle)
plt.axis("equal")
plt.show()

"""
"""

# 'CH01 Q: 5' , 'CH01 Q: 10'

import pylab as plt

fig,ax=plt.subplots()

for i in range(1,5):
    circle =plt.Circle((0,0),(i+0.3),color='g',linewidth=8,fill=False)
    ax.add_patch(circle)
plt.axis("equal")
plt.show()

"""






"""
'CH01 Q 7'

import pylab as plt
fig, ax = plt.subplots()

squares = [
    
    ((0 , 0), 10 , 'b'),
    ((1, 1), 2 , 'r'),
    ((3 ,3), 2 , 'b'),
    ((5, 5), 2, 'y'),
    ((7, 7), 2, 'g')
    
    ]

for square in squares:
    ax.add_patch(plt.Rectangle(square[0], square[1], square[1], fill = False , edgecolor = square[2], linewidth = 2))

plt.axis('equal')
plt.show()

"""


