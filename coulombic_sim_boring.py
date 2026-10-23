# this one doesn't have art in it
# dependencies
import math
import tkinter as tk
from anim import Sprite
# vars
q_1: float = 0.0 # in coulombs 
q_2: float = 0.0 # also in coulombs
r: float = 1.0 # in meters
k_e: float = 8.9875517923e9 # coulomb's constant in N·m²/C²
# i could have also used permittivity of free space but this is easier

# formula 
F_coulomb: float = (k_e * ((abs(q_1 * q_2)) / (math.pow(r,2)))) # in N

# initialize window 
root = tk.Tk()
root.title("coulomb's law visualizer/simulation/wtv")
root.geometry("1600x900")
sfont = ("Helvetica", 16)

# create gui
# update vals
def upd_q_1(val):
    global q_1
    q_1 = float(val)
    q_1_label.config(text="q\u2081 (in C): " + str(val))
    update_charge_bar(q_1, q1_bar_bg, q1_bar_fill, q1_bar_label, canvas.coords(q1_spr.id)[0], 300, "q\u2081")
    upd_f_coulomb()

def upd_q_2(val):
    global q_2
    q_2 = float(val)
    q_2_label.config(text="q\u2082 (in C): " + str(val))
    update_charge_bar(q_2, q2_bar_bg, q2_bar_fill, q2_bar_label, canvas.coords(q2_spr.id)[0], 300, "q\u2082")
    upd_f_coulomb()

def upd_r(val):
    global r
    r = float(val)
    r_label.config(text="r (in m): " + str(val))
    upd_f_coulomb()

def upd_f_coulomb():
    global F_coulomb
    F_coulomb = (k_e * ((abs(q_1 * q_2)) / (math.pow(r,2))))
    if r == 0:
        f_coulomb_label.config(text="r ≠ 0")
    else:
        f_coulomb_label.config(text="F = " + str(f"{F_coulomb:.3e}") + " N")

# labels
q_1_label = tk.Label(calc_frame, text="q\u2081 (in C): " + str(q_1), font=sfont)
q_1_label.pack()

q_2_label = tk.Label(calc_frame, text="q\u2082 (in C): " + str(q_2), font=sfont)
q_2_label.pack()

r_label = tk.Label(calc_frame, text="r (in m): " + str(r), font=sfont)
r_label.pack()

f_coulomb_label = tk.Label(calc_frame, text="F = " + str(F_coulomb) + " N", font=(sfont,19))
f_coulomb_label.pack()

# sliders
q_1_slider = tk.Scale(calc_frame, from_=-5, to=5, resolution=0.01, orient=tk.HORIZONTAL,command=upd_q_1, label="q\u2081")
q_1_slider.pack()

q_2_slider = tk.Scale(calc_frame, from_=-5, to=5, resolution=0.01, orient=tk.HORIZONTAL,command=upd_q_2, label="q\u2082")
q_2_slider.pack()

r_slider = tk.Scale(calc_frame, from_=1, to=100, resolution=0.01, orient=tk.HORIZONTAL,command=upd_r, label="r")
r_slider.pack()
r_slider.set(r)
upd_r(r)

root.mainloop()


