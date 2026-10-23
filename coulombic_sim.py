# This is a simulation demonstrating Coulomb's law of electrostatic attractions; I was bored.
# Probably useful for AP Chemistry or AP Physics C.
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

canvas = tk.Canvas(root, width=1250, height=900, bg="#FFFFFF")
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

calc_frame = tk.Frame(root, width=350, bg="#EEEEEE")
calc_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
calc_frame.pack_propagate(False)

# charge indicator bars
bar_width: int = 120
bar_height: int = 12
max_charge: float = 5.0

# q1 charge bar
q1_bar_bg = canvas.create_rectangle(315, 300, 435, 312, fill="#DDDDDD", outline="")
q1_bar_fill = canvas.create_rectangle(375, 300, 375, 312, fill="#999999", outline=""
)
q1_bar_label = canvas.create_text(375, 285, text="q\u2081 = 0.00 C",font=("Helvetica", 12))

# q2 charge bar
q2_bar_bg = canvas.create_rectangle(840, 300, 960, 312, fill="#DDDDDD", outline="")
q2_bar_fill = canvas.create_rectangle(900, 300, 900, 312, fill="#999999", outline="")
q2_bar_label = canvas.create_text(900, 285, text="q₂ = 0.00 C",font=("Helvetica", 12))

# create charge visualizations
q1_frames = ["q_1_frame.png", "q_1_frame2.png", "q_1_frame3.png"]
q1_spr = Sprite(canvas, q1_frames, x=375, y=400,delay=100)
q1_spr.start()

q2_frames = ["q_2_frame.png", "q_2_frame1.png", "q_2_frame2.png"]
q2_spr = Sprite(canvas, q2_frames, x=900, y=400,delay=110)
q2_spr.start()

# updates the bar above the charge sprites
def update_charge_bar(q, bg_id, fill_id, label_id, x, y, name):
    fraction = min(abs(q) / max_charge, 1.0)
    filled_width = bar_width * fraction 
    canvas.coords(bg_id,x - bar_width / 2, y, x + bar_width / 2, y + bar_height)
    canvas.coords(fill_id,x - bar_width / 2, y, x - bar_width / 2 + filled_width, y + bar_height)

    # blue = positive charge
    # red = negative charge
    # gray = neutral charge
    if q > 0:
        color = "#2196F3"
    elif q < 0:
        color = "#F44336"
    else:
        color = "#999999"

    canvas.itemconfig(fill_id, fill=color)
    canvas.coords(label_id, x, y - 12)
    canvas.itemconfig(label_id, text=f"{name} = {q:.2f} C")

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
    separation = 150 + ((r - 0.1) / 99.9) * 500
    center_x = 637.5
    q1_x = center_x - separation / 2
    q2_x = center_x + separation / 2

    q1_spr.setX(q1_x)
    q2_spr.setX(q2_x)
    
    update_charge_bar(
        q_1, q1_bar_bg, q1_bar_fill, q1_bar_label,
        q1_x, 300, "q\u2081"
    )
    update_charge_bar(
        q_2, q2_bar_bg, q2_bar_fill, q2_bar_label,
        q2_x, 300, "q₂"
    )
    
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
q_1_label.pack(pady=10, side=tk.TOP, anchor=tk.W)

q_2_label = tk.Label(calc_frame, text="q\u2082 (in C): " + str(q_2), font=sfont)
q_2_label.pack(pady=10, side=tk.TOP, anchor=tk.W)

r_label = tk.Label(calc_frame, text="r (in m): " + str(r), font=sfont)
r_label.pack(pady=10, side=tk.TOP, anchor=tk.W)

f_coulomb_label = tk.Label(calc_frame, text="F = " + str(F_coulomb) + " N", font=(sfont,19))
f_coulomb_label.pack(pady=10, side=tk.TOP, anchor=tk.W,)

# sliders
q_1_slider = tk.Scale(calc_frame, from_=-5, to=5, resolution=0.01, orient=tk.HORIZONTAL,command=upd_q_1, label="q\u2081")
q_1_slider.pack(pady=10, side=tk.TOP, fill=tk.X)

q_2_slider = tk.Scale(calc_frame, from_=-5, to=5, resolution=0.01, orient=tk.HORIZONTAL,command=upd_q_2, label="q\u2082")
q_2_slider.pack(pady=10, side=tk.TOP, fill=tk.X)

r_slider = tk.Scale(calc_frame, from_=1, to=100, resolution=0.01, orient=tk.HORIZONTAL,command=upd_r, label="r")
r_slider.pack(pady=10, side=tk.TOP, fill=tk.X)
r_slider.set(r)
upd_r(r)

root.mainloop()


