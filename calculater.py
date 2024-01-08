from tkinter import *
x=Tk()
y=Entry(x,border=6)
y.grid(row=0,columnspan=3,ipadx=120,ipady=12,sticky='w')

def z(x):
        if x=="del":
                ro=y.get()
                ro=ro[0:len(ro)-1]
                y.delete(0,END)
                y.insert(0,ro)
        elif x=="cl":
                y.delete(0,END)
        elif x=="tot":
                su=y.get()
                y.delete(0,END)
                x=round(eval(su),5)
                y.insert(0,str(x))
        else:
                h=y.get()
                h+=x
                y.delete(0,END)
                y.insert(0,h)
                
icon=[["1","2","3"],['4','5','6'],['7','8','9'],['0','.','+'],['-','x','='],['%','/','<--'],['(',')',"clear"]]
oper=[["1","2","3"],['4','5','6'],['7','8','9'],['0','.','+'],['-','*','tot'],['%','/','del'],['(',')',"cl"]]

for i in range(1,8,1):
    for j in range(3):
        exec(f"a_{i}_{j}=Button(x,text=icon[{i-1}][{j}],command=lambda:z(oper[{i-1}][{j}]),border=4)")
        exec(f"a_{i}_{j}.grid(row={i},column={j},ipadx=40,ipady=25,columnspan=1,sticky='nsew')")
        
x.mainloop()




