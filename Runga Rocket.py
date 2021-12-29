
import math
import matplotlib.pyplot as plt
import numpy as np

# Input functions


def asking_t():
    print("____________________________________________________________")
    print("[TIME PERIOD OF SIMULATION]")
    myinput= input("Would you like to \n \n (a) Simulate the orbit for 19,000 seconds (default) \n \n (b) Simulate the orbit for a custom time period \n \n CHOICE: ")
    while myinput!= 'a' or myinput!= 'b' or myinput!= 'c':
        if myinput == "a":
            tmax= 19000
            break
        elif myinput == "b":
            myinputt = input("Please input the simulating time (s): ")
            tmax= int(myinputt)
            break
        
    print("____________________________________________________________")  
    return tmax

def asking_xy():
    print("____________________________________________________________")
    print("[X AND Y COORDINATES]")
    myinput= input("Would you like to \n \n (a) Keep the default x and y coordinates (15000 km) \n \n (b) Change it \n \n CHOICE: ")
    while myinput!= 'a' or myinput!= 'b' or myinput!= 'c':
        if myinput == "a":
            print("\n you have chosen the starting x coordinate to be 15000 km for x and y")
            x1= 15000000
            y1= 0
            break
        elif myinput == "b":
            print("\n you have chosen to use custom starting coordinates.")
            myinputx = input("Please input the starting x coordinate (km): ")
            myinputy = input("Please input the starting y coordinate (km): ")
            x1= float(myinputx)*1000
            y1= float(myinputy)*1000
            break
        
    print("____________________________________________________________")  
    return x1,y1


def asking_v():
    print("____________________________________________________________")
    print("[VX AND VY VALUES]")
    myinput= input("Would you like to \n \n (a) Keep the default vx and vy values (5153 m/s) \n \n (b) Change it \n \n CHOICE: ")
    while myinput!= 'a' or myinput!= 'b' or myinput!= 'c':
        if myinput == "a":
            print("\n you have chosen the starting x coordinate to be 3,600 km for x and y")
            vx= 0
            vy= 5153
            break
        elif myinput == "b":
            print("\n you have chosen to use custom starting coordinates.")
            print('Default: 0m (vx) and 5153.2m (vy)')
            myinputvx = input("Please input the starting vx value (m/s): ")
            myinputvy = input("Please input the starting vy value (m/s): ")
            vx= float(myinputvx)
            vy= - float(myinputvy)
            break
        
    print("____________________________________________________________")  
    return vx,vy

#vx 'f1'
def dx_dt(vx):
    dx_dt= vx
    return dx_dt
#vy
def dy_dt(vy):
    dy_dt= vy
    return dy_dt
#ax
def dvx_dt(x,y):
    r=(float(x)**2 + float(y)**2)**(1/2)
    rm=((Rm-x)**2 + y**2)**(1/2)
    dvx_dt= ((-G * M * x)/ abs(r)**3)+ ((G * Mm * (Rm-x))/ abs(rm)**3)
    return dvx_dt
    #ay
def dvy_dt(x,y):
    r= (float(x)**2 + float(y)**2)**(1/2)
    rm= ((Rm-x)**2 + y**2)**(1/2)
    dvy_dt= ((-G * M * y) / abs(r)**3)- ((G * Mm * (y))/ abs(rm)**3)
    return dvy_dt  




def plot1(t,x,y,vx,vy):
    xvals=[]
    yvals=[]
    vxvals=[]
    vyvals=[]
    tvals=[]
    
    xvalstable=[]
    yvalstable=[]
    vxvalstable=[]
    vyvalstable=[]
    tvalstable=[]
    
    KE = []
    PE = []
    TE = []
    for i in range(0,tmax, h):
    
        k1x= dx_dt(vx)
        k1y= dy_dt(vy)
        k1vx=dvx_dt(x,y)
        k1vy=dvy_dt(x,y)
        
        k2x= dx_dt(vx+((h*k1vx)/2))
        k2y= dy_dt((vy+((h* k1vy)/2)))
        k2vx= dvx_dt((x+((h*k1x)/2)),(y+((h*k1y)/2)))
        k2vy= dvy_dt((x+((h*k1x)/2)),(y+((h*k1y)/2)))
        
        k3x= dx_dt((vx+((h*k2vx)/2)))
        k3y=dy_dt((vy+((h*k2vy)/2)))
        k3vx=dvx_dt((x+((h*k2x)/2)),(y+((h*k2y)/2)))
        k3vy=dvy_dt((x+((h*k2x)/2)),(y+((h*k2y)/2)))
        
        k4x= dx_dt((vx+ h* k3vx))
        k4y=dy_dt((vy+ h*k3vy))
        k4vx=dvx_dt((x+ h* k3x),(y+ h* k3y))
        k4vy=dvy_dt((x+ h* k3x),(y+ h* k3y))
            
        x = x + (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
        xvals.append(x)
        xt= round(x)
        xvalstable.append(xt)
        
        y= y + (h/6)*(k1y + 2*k2y + 2*k3y + k4y)
        yvals.append(y)
        yt= round(y)
        yvalstable.append(yt)
        
        vx= vx + (h/6)*(k1vx + 2*k2vx + 2*k3vx + k4vx)
        vxvals.append(vx)
        vxt= round(vx)
        vxvalstable.append(vxt)
        
        vy= vy + (h/6)*(k1vy + 2*k2vy + 2*k3vy + k4vy)
        vyvals.append(vy)
        vyt = round(vy)
        vyvalstable.append(vyt)
        
        ke = 0.5 * 1 * (vx**2 + vy**2)
        KE.append(ke)
        pe = -(6.67e-11*5.97e24)/(x**2 + y**2)**0.5
        PE.append(pe)
        te = ke + pe
        TE.append(te)
        t = t + h
        tvals.append(t)
        

        
        
    
    return tvals, xvals, yvals, vxvals, vyvals, KE, PE, TE, xvalstable, yvalstable, vxvalstable, vyvalstable


    


MyInput= "0"
while MyInput != "q":

    MyInput= input("____________________________________________________________ \n \n [MAIN MENU] \n \n Would you like to \n \n (a) Simulate a satellite orbiting the earth \n \n (b) Simulate a satellite launched to the moon \n \n (q) Quit\n \n Choice: ")
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~option a
    
    if MyInput == 'a': 
        
        G= 6.67e-11
        M=5.97e24
        Mm= 7.347e22 
        h = 50
        x,y = asking_xy()
        vx, vy = asking_v() #the apparent velocities in mps needed to leave the earth's orbit
        t = 0
        tmax = asking_t()
        
        
        R=0
        Rm=384400000
        rm=0
        
        
        plt.plot(plot1(t,x,y,vx,vy)[1], plot1(t,x,y,vx,vy)[2], label=("without moon"))
        plt.scatter(0,0)
        circle1=plt.Circle((0,0),6300e3, color = 'g')
        plt.gcf().gca().add_artist(circle1)
        plt.xlabel("x Coordinates (m)")
        plt.ylabel("y Coordinates (m)")
        plt.grid(True)
        plt.axis('equal')



        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(plot1(t,x,y,vx,vy)[1], plot1(t,x,y,vx,vy)[2], 0)
        ax.scatter3D(0, 0, 0)
        plt.show()
         
        

        
    
        print("____________________________________________________________")
        input0=0
        input0= input("Would you like to see the change in energy of this orbit? \n \n(a) No \n \n(b) Yes \n \n Choice: ")
        while input0 != 'a' or input0 != 'b':
            if input0 == 'a':
                break
            elif input0 == 'b':
                plt.plot(plot1(t,x,y,vx,vy)[0], plot1(t,x,y,vx,vy)[5], label=("Kinetic Energy"))
                plt.plot(plot1(t,x,y,vx,vy)[0], plot1(t,x,y,vx,vy)[6], label=("Potential Energy"))
                plt.plot(plot1(t,x,y,vx,vy)[0], plot1(t,x,y,vx,vy)[7], label=("Total Energy"))
                plt.legend()
                plt.grid(True)
                plt.xlabel("Time (s)")
                plt.ylabel("Energy (J)")
                plt.show()
                
                break
            else:
                print('Please select "a" or "b": ' )


        print("____________________________________________________________")
        input1=0
        input1= input("would you like to see the plotted data? \n \n (a)Yes \n \n (b)No \n \n Choce: ")
        while input1 == 'a' or input1 == 'a' :
            
            if input1 == 'a':
                print(" t values \t x values \t y values \t vx values \t vy values")
                '''
                print("t -> {:.0f}\tx -> {:.0f}\ty -> {:.0f}\tVx -> {:.0f}\tVy -> {:.10f}".format(t, x, y, vx, vy))
                
                print("%.2f" % a)
                '''
                
                print(plot1(t,x,y,vx,vy)[0],plot1(t,x,y,vx,vy)[8],plot1(t,x,y,vx,vy)[9],plot1(t,x,y,vx,vy)[10],plot1(t,x,y,vx,vy)[11])
                
                break
            if input1 == 'b':
                print("ok")
                break
            else:
                print('Please choose a valid option')

        
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~option b
        
    elif MyInput == 'b':
        print('You have chosen part (b)')
        print("")
        
        G= 6.67e-11
        M=5.972e24
        Mm= 7.35e22 #mass of the moon 
        h = 50

        t = 0
        tmax = 900000

        Rm=384400000
        
                
        
        print("____________________________________________________________")
        myinput_option=0
        myinput_option= input("Would you like to: \n \n (a) plot a single graph \n \n (b) plot and compare four plots of different starting positions \n \n (c) Plot and compare graphs of different starting velocities \n \n Choice: ")
        while myinput_option != 0:
            if myinput_option == 'a':

                x,y = -6500e3, 0
                vx, vy = 0, 10964     
                
                
                print("____________________________________________________________")
                myinput_energies = 0
                myinput_energies = input('Would you like to display the change in energies due to this orbit? \n \n (a) No \n \n (b) Yes \n \n Choice: ')
                while myinput_energies != 'a' or myinput_energies != 'b':
                    
                    if myinput_energies == 'a':
                        print('ok')

                        
                        
                        break
                    
                    elif myinput_energies == 'b':
                        plt.plot(plot1(t,x,y,vx,vy)[0], plot1(t,x,y,vx,vy)[5], label=("Kinetic Energy"))
                        plt.plot(plot1(t,x,y,vx,vy)[0], plot1(t,x,y,vx,vy)[6], label=("Potential Energy"))
                        plt.plot(plot1(t,x,y,vx,vy)[0], plot1(t,x,y,vx,vy)[7], label=("Total Energy"))
                        plt.legend()
                        plt.xlabel("Time (s)")
                        plt.ylabel("Energy (J)")
                        plt.show()
                        

                        
                        break
                    
                    else:
                        print('please enter a valid choice: ')
                        print("____________________________________________________________")
                        break
                    
            
                plt.plot(plot1(t,x,y,vx,vy)[1], plot1(t,x,y,vx,vy)[2], label=("without moon"))
                plt.scatter(0,0, s=90)
                plt.scatter(384400000,0)
                plt.xlabel("x Coordinates (m)")
                plt.ylabel("y Coordinates (m)")
                plt.grid(True)
                plt.axis('equal')
                plt.ylim(-1.5e8,1e8)
                plt.legend()
                plt.show()  
                
                break
            
            
            elif myinput_option == 'b':
                x1 = float(input("Please input your first starting x position (m): "))
                y1 = float(input("Please input your first starting y position (m): "))
                x2 = float(input("Please input your second starting x position (m): "))
                y2 = float(input("Please input your second starting y position (m): "))
                x3 = float(input("Please input your third starting x position (m): "))
                y3 = float(input("Please input your third starting y position (m): "))
                x4 = float(input("Please input your fourth starting x position (m): "))
                y4 = float(input("Please input your fourth starting y position (m): "))                
                
                vx, vy = 0, 10964
                plt.plot(plot1(t,x1,y1,vx,vy)[1], plot1(t,x1,y1,vx,vy)[2], label=(x1, "m"))
                plt.plot(plot1(t,x2,y2,vx,vy)[1], plot1(t,x2,y2,vx,vy)[2], label=(x2, "m"))
                plt.plot(plot1(t,x3,y3,vx,vy)[1], plot1(t,x2,y2,vx,vy)[2], label=(x3, "m"))
                plt.plot(plot1(t,x4,y4,vx,vy)[1], plot1(t,x2,y2,vx,vy)[2], label=(x4, "m"))
                
         
                plt.scatter(0,0, s=90)
                plt.scatter(384400000,0)
                plt.xlabel("x Coordinates (m)")
                plt.ylabel("y Coordinates (m)")
                plt.grid(True)
                plt.axis('equal')
                plt.ylim(-1.5e8,1e8)
                plt.legend()
                plt.show()  
                
                break
            elif myinput_option == 'c':
                vx1 = input("Please input your first vx value(m/s): ")
                vy1 = input("Please input your first vy value(m/s): ")
                vx2 = input("Please input your second vx value(m/s): ")
                vy2 = input("Please input your second vy value(m/s): ")
                vx3 = input("Please input your third vx value(m/s): ")
                vy3 = input("Please input your third vy value(m/s): ")
                vx4 = input("Please input your fourth vx value(m/s): ")
                vy4 = input("Please input your fourth vy value(m/s): ")  
                
                plt.plot(plot1(t,x,y,vx1,vy1)[1], plot1(t,x,y,vx1,vy1)[2], label=(vy1,"m/s"))
                plt.plot(plot1(t,x,y,vx2,vy2)[1], plot1(t,x,y,vx2,vy2)[2], label=(vy2,"m/s"))
                plt.plot(plot1(t,x,y,vx3,vy3)[1], plot1(t,x,y,vx3,vy3)[2], label=(vy3,"m/s"))
                plt.plot(plot1(t,x,y,vx4,vy4)[1], plot1(t,x,y,vx4,vy4)[2], label=(vy4,"m/s"))
                
                x,y = -6500e3, 0
                
                
                plt.scatter(0,0, s=90)
                plt.scatter(384400000,0)
                plt.xlabel("x Coordinates (m)")
                plt.ylabel("y Coordinates (m)")
                plt.grid(True)
                plt.axis('equal')
                plt.ylim(-1.5e8,1e8)
                plt.legend()
                plt.show()  
                break
            
        else:
            print('Please enter a valid choice: ')


    
    elif MyInput == 'q': 
        print('you have chosen to quit')
        
    else:
        print("this is not a valid choice")
    


