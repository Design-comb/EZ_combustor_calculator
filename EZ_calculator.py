import os
import tkinter
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys_MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import tkinter as tk
from tkinter import ttk
import math

import PIL.Image
from PIL import ImageTk, Image

########################################################################################################################
# CI 계산하는 함수
########################################################################################################################
def calculate():
    Combustor_number = float(e1.get())
    Burner_design = float(e2.get())
    Aspect_ratio = float(e3.get())
    Heat_release_rate1 = float(e4.get())
    Combustion_intensity1 = float(e5.get())
    Inlet_pressure = float(e6.get())
    Burner_diameter = ((4*((Heat_release_rate1*0.001)/(Combustion_intensity1*Inlet_pressure))/(Burner_design*3.14*Aspect_ratio*Combustor_number))**(1/3))*1000
    Burner_diameter = round(Burner_diameter, 2)

    e7.delete(0, len(e7.get())) #결과 출력 전 창 비우기
    e7.insert(0, Burner_diameter) #결과 출력

########################################################################################################################
# Swirl number 계산하는 함수
########################################################################################################################

    Center_body_diameter = float(e8.get())
    Nozzle_diameter = float(e9.get())
    Swirl_angle = float(e10.get())
    Tan_theta = math.tan(math.radians(Swirl_angle))
    Swirl_number = (2/3)*((1-(Center_body_diameter/Nozzle_diameter)**3)/(1-(Center_body_diameter/Nozzle_diameter)**2))*Tan_theta
    Swirl_number = round(Swirl_number, 3)

    e11.delete(0, len(e11.get())) #결과 출력 전 창 비우기
    e11.insert(0, Swirl_number)

########################################################################################################################
# Combustion loading parameter 계산하는 함수
########################################################################################################################

    Air_mass_flow = float(e12.get())
    Correction_factor = float(e13.get())
    Inlet_pressure = float(e14.get())
    Heat_release_rate2 = float(e15.get())
    Combustion_intensity2 = float(e16.get())
    Air_mass_flow_IU = Air_mass_flow*2.204623
    Inlet_pressure_IU = Inlet_pressure*9.869233
    Vt = (Heat_release_rate2*0.001)/(Combustion_intensity2*Inlet_pressure)
    Vt_IU = Vt*35.314667
    Combustion_loading_parameter = (Air_mass_flow_IU)/((Inlet_pressure_IU**(Correction_factor))*Vt_IU)
    Combustion_loading_parameter = round(Combustion_loading_parameter, 5)

    e17.delete(0, len(e17.get())) #결과 출력 전 창 비우기
    e17.insert(0, Combustion_loading_parameter)

########################################################################################################################
#입출력 창을 초기화 하는 함수
########################################################################################################################
def retry(): #입출력 창을 초기화 하는 함수, Clean button
    e1.delete(0, len(e1.get()))
    e2.delete(0, len(e2.get()))
    e3.delete(0, len(e3.get()))
    e4.delete(0, len(e4.get()))
    e5.delete(0, len(e5.get()))
    e6.delete(0, len(e6.get()))
    e8.delete(0, len(e8.get()))
    e9.delete(0, len(e9.get()))
    e10.delete(0, len(e10.get()))
    e12.delete(0, len(e12.get()))
    e13.delete(0, len(e13.get()))
    e14.delete(0, len(e14.get()))
    e15.delete(0, len(e15.get()))
    e16.delete(0, len(e16.get()))


########################################################################################################################
#기본설정
########################################################################################################################
window = Tk()
window.title('EZ combustor calculator') #프로그램 제목
p1=PhotoImage(file=resource_path('Logo.png')) #프로그램 아이콘
window.iconphoto(False, p1) #아이콘 설정
window.geometry('450x650') #프로그램 창 크기
window.resizable(width=False, height=False) #창 크기 수정못하도록 설정

notebook = ttk.Notebook(window)
notebook.pack(pady=0) #탭 위아래 높이 조정

frame1 = ttk.Frame(notebook, width=430, height=620)
frame1.pack(expand=1, fill='both')
frame2 = ttk.Frame(notebook, width=430, height=620)
frame2.pack(expand=1, fill='both')
frame3 = ttk.Frame(notebook, width=430, height=620)
frame3.pack(expand=1, fill='both')
frame4 = ttk.Frame(notebook, width=430, height=620)
frame4.pack(expand=1, fill='both')

notebook.add(frame1, text='Combustion intensity')
notebook.add(frame2, text='Swirl nubmer')
notebook.add(frame3, text='Combustion loading parameter')
notebook.add(frame4, text='About')

########################################################################################################################
#첫번째 탭 Combustion intensity
########################################################################################################################
#Label로 프로그램 안내 정보 출력, place로 위치를 지정
l1= Label(frame1, text = "1. Combustion intensity(CI)",
          fg = "orange", font = "helvetica 16 bold")
l1.place(x=10, y=5)

l2 = Label(frame1, text = "Combustion intensity = heat release / (P3 x Vt)",
           font = "helvetica 10 bold")
l2.place(x=60, y=40)

l3 = Label(frame1, text = "V = Vt / n = A x L = (a x (π x d^3 x Aspect ratio)) / 4",
           font = "helvetica 10 bold")
l3.place(x=50, y=60)

l4 = Label(frame1, text = "1. Combustor number : n")
l4.place(x=50, y=100)
e1 = Entry(frame1)
e1.place(x=220, y=100, width=60, heigh=20)
l5 = Label(frame1, text = "Unit : none")
l5.place(x=290, y=100)

l6 = Label(frame1, text = "2. Burner design : a")
l6.place(x=50, y=130)
e2 = Entry(frame1)
e2.place(x=220, y=130, width=60, heigh=20)
l7 = Label(frame1, text = "Unit : none")
l7.place(x=290, y=130)
l8 = Label(frame1, text = "*Value - cylinderical : 1, non-cylinderical : 0.65~0.7",
           fg = "gray")
l8.place(x=60, y=150)

l9 = Label(frame1, text = "3. Aspect ratio")
l9.place(x=50, y=170)
e3 = Entry(frame1)
e3.place(x=220, y=170, width=60, heigh=20)
l10 = Label(frame1, text = "Unit : none")
l10.place(x=290, y=170)
l11 = Label(frame1, text = "*Value range : 2.4~4.0",
           fg = "gray")
l11.place(x=60, y=190)

l12 = Label(frame1, text = "4. Heat release rate")
l12.place(x=50, y=210)
e4 = Entry(frame1)
e4.place(x=220, y=210, width=60, heigh=20)
l13 = Label(frame1, text = "Unit : kW")
l13.place(x=290, y=210)

l14 = Label(frame1, text = "5. Combustion intensity")
l14.place(x=50, y=240)
e5 = Entry(frame1)
e5.place(x=220, y=240, width=60, heigh=20)
l15 = Label(frame1, text = "Unit : none")
l15.place(x=290, y=240)
l16 = Label(frame1, text = "*Value - Power generator : 200~250, Air craft : 1000~1500",
           fg = "gray")
l16.place(x=45, y=260)

l17 = Label(frame1, text = "6. Inlet pressure : P3")
l17.place(x=50, y=280)
e6 = Entry(frame1)
e6.place(x=220, y=280, width=60, heigh=20)
l18 = Label(frame1, text = "Unit : Mpa")
l18.place(x=290, y=280)

########################################################################################################################
#계산결과 버너 직경 D
########################################################################################################################
l19 = Label(frame1, text = "Burner diameter : d",
            fg = "red", font = "helvetica 10 bold")
l19.place(x=60, y=310)
e7 = Entry(frame1)
e7.place(x=220, y=310, width=60, heigh=20)
l20 = Label(frame1, text = "Unit : mm")
l20.place(x=290, y=310)


# 클릭 시 함수 calculator를 실행함.
# 계산하기, 다시하기 버튼 생성 및 이벤트를 처리함.
b1 = Button(frame1, text = "Calculate", command=calculate)
b1.place(x=250, y=340)
b2 = Button(frame1, text = "Clear", command=retry)
b2.place(x=320, y=340)

########################################################################################################################
#Combustor Geometry
########################################################################################################################
img1 = Image.open(resource_path('Combustor_geometry.png'))
resized1 = img1.resize((305,210), Image.ANTIALIAS)
new_img1 = ImageTk.PhotoImage(resized1)
l21 = Label(frame1, image = new_img1)
l21.place(x=60, y=380)


########################################################################################################################
#두번째 탭 Combustion intensity
########################################################################################################################
l22= Label(frame2, text = "2. Swirl number(SN)",
          fg = "orange", font = "helvetica 16 bold")
l22.place(x=10, y=5)

l23 = Label(frame2, text = "Swirl number = 2/3 x (1 - (Dc/Do)^3) / (1 - (Dc/Do)^2) x tanθ",
           font = "helvetica 10 bold")
l23.place(x=25, y=40)
l24 = Label(frame2, text = "Dc = Center body diameter, Do = Nozzle diameter, θ = Swirl angle",
           fg = "gray", font = "helvetica 9 bold")
l24.place(x=30, y=60)

l25 = Label(frame2, text = "1. Center body diameter : Dc")
l25.place(x=50, y=100)
e8 = Entry(frame2)
e8.place(x=220, y=100, width=60, heigh=20)
l26 = Label(frame2, text = "Unit : mm")
l26.place(x=290, y=100)

l27 = Label(frame2, text = "2. Nozzle diameter : Do")
l27.place(x=50, y=130)
e9 = Entry(frame2)
e9.place(x=220, y=130, width=60, heigh=20)
l28 = Label(frame2, text = "Unit : mm")
l28.place(x=290, y=130)

l29 = Label(frame2, text = "3. Swirl angle : θ")
l29.place(x=50, y=160)
e10 = Entry(frame2)
e10.place(x=220, y=160, width=60, heigh=20)
l30 = Label(frame2, text = "Unit : angle")
l30.place(x=290, y=160)

########################################################################################################################
#계산결과 Swirl nubmer
########################################################################################################################
l31 = Label(frame2, text = "Swirl number : SN",
            fg = "red", font = "helvetica 10 bold")
l31.place(x=60, y=190)
e11 = Entry(frame2)
e11.place(x=220, y=190, width=60, heigh=20)
l32 = Label(frame2, text = "Unit : none")
l32.place(x=290, y=190)

# 클릭 시 함수 calculator를 실행함.
# 계산하기, 다시하기 버튼 생성 및 이벤트를 처리함.
b3 = Button(frame2, text = "Calculate", command=calculate)
b3.place(x=250, y=220)
b4 = Button(frame2, text = "Clear", command=retry)
b4.place(x=320, y=220)

########################################################################################################################
#Swirler image
########################################################################################################################
img2 = Image.open(resource_path('Swirler.png'))
resized2 = img2.resize((405,250), Image.ANTIALIAS)
new_img2 = ImageTk.PhotoImage(resized2)
l33 = Label(frame2, image = new_img2)
l33.place(x=10, y=300)

########################################################################################################################
#세번째 탭 Combustion loading parameter
########################################################################################################################
l34= Label(frame3, text = "3. Combustion loading parameter(CLP)",
          fg = "orange", font = "helvetica 16 bold")
l34.place(x=10, y=5)

l35 = Label(frame3, text = "Combustion loading parameter = Mair / (Pair)^n x Vt",
           font = "helvetica 10 bold")
l35.place(x=50, y=40)
l36 = Label(frame3, text = "CLP is imperial units. This program converts SI units to Imperial units.",
           fg = "Gray", font = "helvetica 9 bold")
l36.place(x=15, y=60)

l37 = Label(frame3, text = "1. Air mass flow : Mair")
l37.place(x=50, y=90)
e12 = Entry(frame3)
e12.place(x=220, y=90, width=60, heigh=20)
l38 = Label(frame3, text = "Unit : kg/s")
l38.place(x=290, y=90)

l37 = Label(frame3, text = "2. Correction factor : n")
l37.place(x=50, y=120)
e13 = Entry(frame3)
e13.place(x=220, y=120, width=60, heigh=20)
l38 = Label(frame3, text = "Unit : none")
l38.place(x=290, y=120)

l39 = Label(frame3, text = "*Value - 1 or 1.8 or 2",
            fg = "Gray")
l39.place(x=60, y=140)
l40 = Label(frame3, text = "")
l40.place(x=290, y=140)

l41 = Label(frame3, text = "3. Inlet pressure : Pair")
l41.place(x=50, y=160)
e14 = Entry(frame3)
e14.place(x=220, y=160, width=60, heigh=20)
l42 = Label(frame3, text = "Unit : Mpa")
l42.place(x=290, y=160)

l43 = Label(frame3, text = "4. Heat release rate")
l43.place(x=50, y=190)
e15 = Entry(frame3)
e15.place(x=220, y=190, width=60, heigh=20)
l44 = Label(frame3, text = "Unit : kW")
l44.place(x=290, y=190)

l45 = Label(frame3, text = "5. Combustion intensity")
l45.place(x=50, y=220)
e16 = Entry(frame3)
e16.place(x=220, y=220, width=60, heigh=20)
l46 = Label(frame3, text = "Unit : none")
l46.place(x=290, y=220)
l47 = Label(frame3, text = "*Value - Power generator : 200~250, Air craft : 1000~1500",
           fg = "gray")
l47.place(x=45, y=240)

########################################################################################################################
#계산결과 Combustion loading parameter
########################################################################################################################

l48 = Label(frame3, text = "Combustion loaidng parameter : CLP",
            fg = "red", font = "helvetica 10 bold")
l48.place(x=40, y=260)
e17 = Entry(frame3)
e17.place(x=290, y=260, width=60, heigh=20)
l49 = Label(frame3, text = "Unit : [lbm/(sec x atm^1.8 x ft^3)]")
l49.place(x=200, y=290)

# 클릭 시 함수 calculator를 실행함.
# 계산하기, 다시하기 버튼 생성 및 이벤트를 처리함.
b5 = Button(frame3, text = "Calculate", command=calculate)
b5.place(x=50, y=290)
b6 = Button(frame3, text = "Clear", command=retry)
b6.place(x=120, y=290)

########################################################################################################################
#Combustion loading parameter image
########################################################################################################################
img3 = Image.open(resource_path('CLP.png'))
resized3 = img3.resize((405,250), Image.ANTIALIAS)
new_img3 = ImageTk.PhotoImage(resized3)
l50 = Label(frame3, image = new_img3)
l50.place(x=10, y=330)

########################################################################################################################
#About 탭
########################################################################################################################
l150= Label(frame4, text = "NGenesys LAB.",
          fg = "Green", font = "helvetica 30 bold")
l150.place(x=70, y=5)

img50 = Image.open(resource_path('CI_6.png'))
resized50 = img50.resize((405,90), Image.ANTIALIAS)
new_img50 = ImageTk.PhotoImage(resized50)
l151 = Label(frame4, image = new_img50)
l151.place(x=10, y=500)

l152= Label(frame4, text = "▪ Office & Laboratory",
          fg = "Brown", font = "helvetica 12 bold")
l152.place(x=10, y=60)

l153= Label(frame4, text = "- O : Engineering hall 1, #6117, Chosun University.",
          fg = "Black", font = "helvetica 10")
l153.place(x=10, y=85)

l154= Label(frame4, text = "- L : Engineering hall 1, #7116, Next generation energy system lab.",
          fg = "Black", font = "helvetica 10")
l154.place(x=10, y=105)

l154= Label(frame4, text = "- Contact : j.park@chosun.ac.kr",
          fg = "Gray", font = "Times 10 bold italic underline")
l154.place(x=10, y=130)

l155= Label(frame4, text = "▪ System engineering",
          fg = "Brown", font = "helvetica 12 bold")
l155.place(x=10, y=165)

l156= Label(frame4, text = ": Optimization of system considering key components of the system",
          fg = "Black", font = "helvetica 10")
l156.place(x=10, y=185)

l157= Label(frame4, text = ": Research for the system, by the system, of the system",
          fg = "Black", font = "helvetica 10")
l157.place(x=10, y=205)

l158= Label(frame4, text = "▪ Research facilities",
          fg = "Brown", font = "helvetica 12 bold")
l158.place(x=10, y=240)

l159= Label(frame4, text = "- Engine dynamo",
          fg = "Black", font = "helvetica 10")
l159.place(x=10, y=260)

l160= Label(frame4, text = "- LINUX server : Thenderbolt w/ 178 core",
          fg = "Black", font = "helvetica 10")
l160.place(x=10, y=280)

l161= Label(frame4, text = "- 1D cycle analysis tool : GT-Power / GT-Suite / Auto-lion",
          fg = "Black", font = "helvetica 10")
l161.place(x=10, y=300)

l162= Label(frame4, text = "- CFD tool : ANSYS(Unlimited core) / CONVERGE CFD",
          fg = "Black", font = "helvetica 10")
l162.place(x=10, y=320)

########################################################################################################################
#버전정보
########################################################################################################################
l300 = Label(window, text = "                                                                  Release version 2021.1.0.0",
             fg = "gray")
l300.place(x=15, y=620)

window.mainloop()

