from gurobipy import GRB
import gurobipy as gp
import matplotlib.pyplot as plt
import numpy as np
import sys


def opt_lin_case1(numVars, constraints, optimzation_func):
    """
    Function that solves LP models with only chaning optimzation func
    """

    # gurobipy model
    m = gp.Model("Case 1")
    m.setParam('OutputFlag', 0)
    # adding varibles
    X = m.addVars(numVars,1, vtype=GRB.CONTINUOUS, name="x", lb=-GRB.INFINITY, ub=GRB.INFINITY)
    #setting obejctive
    m.setObjective(gp.quicksum(optimzation_func[i]*X[i,0] for i in range(numVars)), GRB.MINIMIZE)

    # add constriant to inusre this is a cycle
    m.addConstrs(X[i,0] >= constraints[0][i] for i in range(numVars))
    m.addConstrs(X[i,0] <= constraints[1][i] for i in range(numVars))
    m.optimize()
    
    # checking if model is feasible
    try:
        x = m.getAttr('X', X.values())
    except:
        print("MODEL IS INFEASINBLE")
        return -1*np.ones(numVars)
    return x

def opt_quad_case1(numVars, quad, optimzation_func):
    """
    Function that solves LP models with only chaning optimzation func
    """

    # gurobipy model
    m = gp.Model("Case 1")
    m.setParam('OutputFlag', 0)
    # adding varibles
    X = m.addVars(numVars,1, vtype=GRB.CONTINUOUS, name="x", lb=-GRB.INFINITY, ub=GRB.INFINITY)
    #setting obejctive
    m.setObjective(gp.quicksum(optimzation_func[i]*X[i,0] for i in range(numVars)), GRB.MINIMIZE)

    # add constriant to inusre this is a cycle
    m.addConstr(X[1,0]*X[1,0] <= X[0,0])
    m.addConstr(X[0,0]*X[0,0] <= X[1,0])
   # m.addConstrs(X[i,0] <= constraints[1][i] for i in range(numVars))
    m.optimize()
    
    # checking if model is feasible
    try:
        x = m.getAttr('X', X.values())
    except:
        print("MODEL IS INFEASINBLE")
        return -1*np.ones(numVars)
    return x

def opt_circle_case1(numVars, rad, optimzation_func):
    """
    Function that solves LP models with only chaning optimzation func
    """

    # gurobipy model
    m = gp.Model("Case 1")
    m.setParam('OutputFlag', 0)
    # adding varibles
    X = m.addVars(numVars,1, vtype=GRB.CONTINUOUS, name="x", lb=-GRB.INFINITY, ub=GRB.INFINITY)
    #setting obejctive
    m.setObjective(gp.quicksum(optimzation_func[i]*X[i,0] for i in range(numVars)), GRB.MAXIMIZE)

    # add constriant to inusre this is a cycle
    m.addConstr(X[1,0]*X[1,0]+X[0,0]*X[0,0] <= rad**2)
   # m.addConstrs(X[i,0] <= constraints[1][i] for i in range(numVars))
    m.optimize()
    
    # checking if model is feasible
    try:
        x = m.getAttr('X', X.values())
    except:
        print("MODEL IS INFEASINBLE")
        return -1*np.ones(numVars)
    return x


numVars = 2
constraints = [[0 for x in range(numVars)] for y in range(2)] 
upper = 5
lower = -1
option = 2
t = np.linspace(0,100,1000)

if option==1:

    for i in range(2):
        for j in range(numVars):
            if i == 0:
                constraints[i][j] = lower
            else:
                constraints[i][j] = upper

    for i in range(0,len(t)):
        optimzation_func = [0 for y in range(numVars)] 

        for j in range(numVars):
            if j%2 ==0:
                optimzation_func[j] = (np.sinh(t[i]))
            else:
                optimzation_func[j] = (np.cos(t[i])*np.abs(t[i]))**2

        x_sol = opt_lin_case1(numVars,constraints,optimzation_func)

        if numVars == 2:
            plt.figure(1);plt.clf()
            ax1 = plt.subplot(1,2,1)
            x = np.linspace(1.25*lower,1.25*upper,10)
            upper_arr = upper*np.ones(len(x))
            lower_arr = lower*np.ones(len(x))
            ax1.plot(x,lower_arr,'r-')
            ax1.plot(x,upper_arr,'r-')
            ax1.plot(lower_arr,x,'r-')
            ax1.plot(upper_arr,x,'r-')
            ax1.plot(x_sol[0],x_sol[1],'bo')
            ax1.set_xlim([1.25*lower, 1.25*upper])
            ax1.set_ylim([1.25*lower, 1.25*upper])
            ax1.set_xlabel('x_1')
            ax1.set_ylabel('x_2')

            plt.title("Current Optimal solution at time = "+ str(np.round(t[i],2)) + ": x_1 func = sin(t) and x_2 func = cos(t)")
            plt.draw()
            plt.pause(.000000000000001)

    if numVars == 3:
        plt.figure(1);plt.clf()
        ax1 = plt.subplot(1,2,1, projection='3d')
        x = np.linspace(1.25*lower,1.25*upper,10)
        upper_arr = upper*np.ones(len(x))
        lower_arr = lower*np.ones(len(x))

        zeros = np.zeros(len(x))
        ax1.plot(x,lower_arr,zeros,'r-')
        ax1.plot(x,upper_arr,zeros,'r-')
        ax1.plot(lower_arr,x,zeros,'r-')
        ax1.plot(upper_arr,x,zeros,'r-')
        ax1.plot(x,zeros,lower_arr,'r-')
        ax1.plot(x,zeros,upper_arr,'r-')
        ax1.plot(lower_arr,zeros,x,'r-')
        ax1.plot(upper_arr,zeros,x,'r-')
        ax1.plot(zeros,x,lower_arr,'r-')
        ax1.plot(zeros,x,upper_arr,'r-')
        ax1.plot(zeros,lower_arr,x,'r-')
        ax1.plot(zeros,upper_arr,x,'r-')
        ax1.plot(x,upper_arr,upper_arr,'r-')
        ax1.plot(upper_arr,upper_arr,x,'r-')
        
        ax1.plot(x_sol[0],x_sol[1],x_sol[2],'bo')
        ax1.set_xlim([1.25*lower, 1.25*upper])
        ax1.set_ylim([1.25*lower, 1.25*upper])
        ax1.set_zlim([1.25*lower, 1.25*upper])
        ax1.set_xlabel('x_1')
        ax1.set_ylabel('x_2')

        plt.title("Current Optimal solution at time = "+ str(np.round(t[i],2)) + ": x_1 func = sin(t) and x_2 func = cos(t)")
        plt.draw()
        plt.pause(.000000000000001)

elif option==2:
    quad = 10
    tplot = []
    tplot2 = [[0],[0],[0]]

    for i in range(0,len(t)):
        optimzation_func = [0 for y in range(numVars)] 

        for j in range(numVars):
            if j%2 ==0:
                optimzation_func[j] = np.sin(t[i]) 
            
            else:
                optimzation_func[j] = np.cos(t[i])  

        x_sol = opt_quad_case1(numVars,quad,optimzation_func)
        x_sol2 = list(x_sol)
        x_sol2.append(t[i])
        tplot.append(x_sol2)
        tplot2[0].append(x_sol[0])
        tplot2[1].append(x_sol[1])
        tplot2[2].append(x_sol2[2])


        if numVars == 2:
            print(x_sol)
            
            plt.figure(1);plt.clf()
            ax1 = plt.subplot(1,2,1)
            x = np.linspace(-5, 5,100)
            y = x**2
            y2 = x**2
            ax1.plot(y,x,'r-')
            ax1.plot(x,y2,'r-',label="Feasible Region Bounds")
            ax1.plot(x_sol[0],x_sol[1],'bo',label="Optimal Solution")
            ax1.set_xlim([-1, 2])
            ax1.set_ylim([-1, 2])
            ax1.set_xlabel(r'$x_1$')
            ax1.set_ylabel(r'$x_2$')
            ax1.set_title(r'Feasible Region and Optimal Solution at time $t = '+str(np.round(t[i],2))+'$')
            ax1.legend()

            ax1 = plt.subplot(1,2,2,projection='3d')
            ax1.plot(tplot2[0],tplot2[1],tplot2[2])
            ax1.scatter3D(tplot[i][0],tplot[i][1],tplot[i][2])
            ax1.set_xlim([-1, 1])
            ax1.set_ylim([-1, 3])
            ax1.set_zlim([0, 50])
            ax1.set_xlabel('x_1')
            ax1.set_ylabel('x_2')
            ax1.view_init(10, 30)
            
            #plt.title("Current Optimal solution at time = "+ str(np.round(t[i],2)) + ": x_1 func = sin(t) and x_2 func = cos(t)")
            plt.draw()
            plt.pause(.000000000000001)


elif option==3:
    rad = 5
    circle1 = plt.Circle((0, 0), rad, color='b', fill=False)
    plt.figure(1);plt.clf()
    for i in range(0,len(t)):

        optimzation_func = [0 for y in range(numVars)] 

        for j in range(numVars):
            if j%2 ==0:
                optimzation_func[j] = np.sin(t[i])  
            
            else:
                optimzation_func[j] = np.cos(t[i])   

        x_sol = opt_circle_case1(numVars,rad,optimzation_func)
        if numVars == 2:
            ax1 = plt.subplot(1,2,1)
            ax1.cla()
            ax1.add_patch(circle1)
            ax1.plot(x_sol[0],x_sol[1],'bo')
           # ax1.set_xlim([1.25*lower, 1.25*upper])
           # ax1.set_ylim([1.25*lower, 1.25*upper])
            ax1.set_xlabel('x_1')
            ax1.set_ylabel('x_2')

            plt.title("Current Optimal solution at time = "+ str(np.round(t[i],2)) + ": x_1 func = sin(t) and x_2 func = cos(t)")
            plt.draw()
            plt.pause(.000000000000001)

sys.exit()