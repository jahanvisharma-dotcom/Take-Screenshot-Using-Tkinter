#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
from tkinter import messagebox 
import pyautogui 
import os 
root = Tk() 
time = IntVar() 
time.set(3) 
def take_shot(): 
    timeleft = time.get() 
    if timeleft > 0: 
        timeleft -= 1 
        time. set( timeleft) 
        root.after(1000, take_shot) 
    else: 
        s = pyautogui.screenshot() 
        s.save(os.getcwd()+"\shot.png") 
        messagebox.showinfo("Shot", "shot saved!") 
        time.set(3) 
print ("Current working dir : %s" % os.getcwd())        
l = Label(root,textvariable = time,fg="red") 
l.pack() 
Button(root,text = f"Take Shot 3 secs", command = take_shot).pack()

root.mainloop() 


# In[ ]:




