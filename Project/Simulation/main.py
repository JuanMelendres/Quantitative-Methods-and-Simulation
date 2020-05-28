import numpy
import random
import tkinter as tk
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# start population 
start = int(input("Start population: "))
# Total population, N.
N = 140000
# Number of years.
years = int(input("Number of years: "))
# Initial number of infected and recovered individuals
infected = int(input("Start of infected: "))
recovered = 0
# Everyone is susceptible to infection initially.
susceptible = N - infected - recovered
# Contact rate beta and recovery rate gamma (in 1/days).
beta = 0.15
gamma = 1./20
# A grid of time points (in days)
t = numpy.linspace(0, 180, 180)

#-- Start population ---
def start_population(time_period, pop_initial):
    pop = []
    init_age_limit = 2
    age_of_dying = 80
    start_child_birth_age = 24
    end_child_birth_age = 45
    # the way attributes are arranged are age, gender, number of children, dead
    # defining intial population of N(pop_initial) kids
    
    while True:
        n_m = 0
        n_f = 0
        pop = []
        for i in range(0, pop_initial):
            age = int(random.random() * init_age_limit) + 1
            gender = random.random()
            if gender < .5:
                gender = 0
                n_m = n_m + 1
            else:
                gender = 1
                n_f = n_f + 1
            ch_num = 0
            dead = 0
            buf = [age,gender, ch_num, dead]
            pop.append(buf)
        if n_m == n_f:
            break

    # evolution criteria are people have children after the age of 18 till 40, 
    # probability of having children drastically reduces after 2 and life expectancy is 80.
    # time step is 1 year
    # first_ch_prob = .7
    # second_child_prob = .5
    # third_child_prob = .1
    # fourth_child_prob = .01
    birthing_prob = [.7, .5, .1, .01, .0001, .0000001, .000000001]

    alive_pop_vs_time = []
    tot_pop_vs_time = []
    number_of_child = []

    #plt.ion()
    ax.clear()

    for t in range(time_period):
        n_pop = 0
        n_ch = 0
        for i in pop:
            if i[3] == 1:
                continue
            i[0] = i[0] + 1
            # checking age for birthing and number of children assuming no one has more than 7
            if i[0] >= start_child_birth_age and i[0] <= end_child_birth_age and i[2] < 7:
                #roll the dice
                if random.random() < birthing_prob[i[2]]:
                    # add a human baby based on outcome
                    i[2] = i[2] + 1
                    age = 1
                    gender = random.random()
                    if gender < .5:
                        gender = 0
                    else:
                        gender = 1
                    ch_num = 0
                    dead = 0
                    buf = [age,gender,ch_num,dead]
                    pop.append(buf)
                    #selecting the mate
                    partner = pop[int(random.random() * len(pop))]
                    # making sure the mate is of teh opposite sex
                    if i[2] != partner[2] and partner[0] >= 18 and partner[0] <= 40:
                        # increase the numerb of child of the mate by one
                        partner[2] = partner[2] + 1

            if i[0] > age_of_dying:
                i[3] = 1
            if i[3] == 0:
                n_pop = n_pop + 1
            if i[0] < 18:
                n_ch = n_ch + 1

        alive_pop_vs_time.append(n_pop)
        tot_pop_vs_time.append(len(pop))
        number_of_child.append(n_ch)
        #plt.plot(alive_pop_vs_time)
        #plt.pause(0.05)
        #plt.xlabel('Time (Years)')
        #plt.ylabel('Population')
        #plt.plot(tot_pop_vs_time)
        #plt.plot(alive_pop_vs_time,'r')

    # Red Line
    ax.plot(alive_pop_vs_time)
    # Blue Line
    ax.plot(tot_pop_vs_time)
    # Purple Line
    ax.plot(number_of_child)
    ax.grid(True)
    ax.set_xlabel('$Time (Years)$')
    ax.set_ylabel('$Population$')
    ax.set_title('$Population Growth$')
    line.draw()
    return n_pop
#------------

#-- Virus population ---
# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def virus_simulation():
    # Initial conditions vector
    y0 = susceptible, infected, recovered
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args = (N, beta, gamma))
    S, I, R = ret.T

    # Plot the data on three separate curves for S(t), I(t) and R(t)
    # Blue Line
    ax.plot(t, S, 'b', alpha = 0.5, lw = 2, label = '$Susceptible$')
    # Red Line
    ax.plot(t, I, 'r', alpha = 0.5, lw = 2, label = '$Infected$')
    # Green Line
    ax.plot(t, R, 'g', alpha = 0.5, lw = 2, label = '$Recovered with immunity$')
    ax.grid(True)
    ax.set_xlabel('$Time (days)$')
    ax.set_ylabel('$Population$')
    ax.set_title('$Epidemic$')
    line.draw()
    #print(S + I + R)
#------------

def B0f():
    #start_population(300, 10)
    #start_population(20, 100000)
    ax.clear()
    start_population(years, start)

def B1f():
    ax.clear()
    virus_simulation()


#--- Window root ---
root = tk.Tk()
root.geometry('1420x650')
root.title("Final Project")
#------------

#-- Frames ---
left_frame = tk.Frame(root)
left_frame.place(relx = 0.03, rely = 0.05, relwidth = 0.25, relheight = 0.9)

right_frame = tk.Frame(root, bg = '#C0C0C0', bd = 1.5)
right_frame.place(relx = 0.3, rely = 0.05, relwidth = 0.65, relheight = 0.9)
#---------------

#--- Buttons ---
RH = 0.19

B0 = tk.Button(left_frame, text = "Population", command = B0f)
B0.place(relwidth = 0.2, relheight = 0.05)

B1 = tk.Button(left_frame, text = "Epidemic", command = B1f)
B1.place(rely = (RH * 0.54), relwidth = 0.2, relheight = 0.05)
#------------

#--- Add Plot ---
figure = plt.Figure(figsize = (5,6), dpi = 100)
ax = figure.add_subplot(111)
ax.grid(True), ax.set_xlabel('$Time$'),ax.set_ylabel('$Population$')
line = FigureCanvasTkAgg(figure, right_frame)
line.get_tk_widget().pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
#----------------------

root.mainloop()