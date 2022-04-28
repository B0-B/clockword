#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------
#       clockword © B0-B
#       source: https://github.com/B0-B/clockword
#       Version: 1.0.3
# ---------------------------------
from os import path
from time import sleep
from datetime import datetime
import tkinter as tk
from random import choice, uniform
from traceback import print_exc
import ctypes as ct
class clockword(tk.Tk):
    def __init__(self, background='#000', foreground='#fff', font=('Times New Roman', 16), dpi=70, opacity=0.7):
        tk.Tk.__init__(self)
        self.prefix = ['It is', "We've got", "Now it's"]
        self.frac = ["o'clock", 'half', 'a quarter']
        self.preps = ['to', 'past', 'close to', 'just after']
        self.hours = ['midnight', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
        self.mins = ['five', 'ten', 'twenty']
        self.greeting = 'hello word.'
        self.display = tk.StringVar()
        self.display.set(self.greeting)
        self.refresh = 60
        self.font = font
        self.bg = background
        self.fg = foreground
        self.opacity = opacity
        self.dpi = dpi # dots per inch resolution
        self.buildUI()  # create gui
        self.after(2000, self.readTime)
        self.mainloop()
    def buildUI(self):
        self.tk.call('tk', 'scaling', int(self.dpi/72))
        self.update()
        self.wm_attributes('-toolwindow', 'True')
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(self.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value),ct.sizeof(value))
        self.title(self.__class__.__name__)
        self.configure(bg=self.bg) 
        self.geometry('360x90')
        self.attributes('-alpha', self.opacity)
        lab = tk.Label(self, textvariable=self.display, font=self.font,
            fg=self.fg, bg=self.bg, height=5, width=30)
        lab.pack()
        try:
            self.iconbitmap(path.dirname(path.abspath(__file__))+'/orange.ico')
        except:
            print_exc()
    def currentTime2Text(self):
        print('update ...')
        text = "{} {} {} {} {}"
        now = datetime.now()
        m = now.minute
        if now.hour == 12:
            h = 12
        else:
            h = now.hour % 12
        if m < 5:
            return text.format(choice(self.prefix), self.hours[h], self.frac[0], '', '')
        elif m < 10:
            return text.format(self.prefix[0], self.preps[3], self.hours[h], '', '')
        elif m < 15:
            return text.format(self.prefix[0], self.mins[1], self.preps[1], self.hours[h], '')
        elif m < 20:
            return text.format(self.prefix[0], self.frac[2], self.preps[1], self.hours[h], '')
        elif m < 25:
            return text.format(self.prefix[0], self.mins[2], self.preps[1], self.hours[h], '')
        elif m < 30:
            return text.format(self.prefix[0], self.mins[2], self.mins[0], self.preps[1], self.hours[h])
        elif m < 35:
            return text.format(choice(self.prefix), self.frac[1], self.preps[1], self.hours[h], '')
        elif m < 40:
            return text.format(self.prefix[0], self.mins[2], self.mins[0], self.preps[0], self.hours[(h+1)%12])
        elif m < 45:
            return text.format(self.prefix[0], self.mins[2], self.preps[0], self.hours[(h+1)%12], '')
        elif m < 50:
            return text.format(self.prefix[0], self.frac[2], self.preps[0], self.hours[(h+1)%12], '')
        elif m < 55:
            return text.format(self.prefix[0], self.mins[1], self.preps[0], self.hours[(h+1)%12], '')
        elif m < 60:
            return text.format(self.prefix[0], self.preps[2], self.hours[(h+1)%12], '', '')
    def readTime(self):
        try:
            self.display.set(self.currentTime2Text())
        except Exception as e:
            print_exc()
        finally:
            self.after(self.refresh*1000, self.readTime)
if __name__ == '__main__': 
    clockword(background='#000', foreground='#fff', font=('Times New Roman', 18), 
            dpi=300, opacity=0.7, style='typewriter')