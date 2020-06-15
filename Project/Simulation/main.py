import numpy
import random
import tkinter as tk
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Start population 
start = int(input("Start population: "))
# Total population for Virus simulation.
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
# Grid of time points (in days)
t = numpy.linspace(0, 180, 180)

#-- Start population ---
def start_population(time_period, pop_initial):
    pop = []
    init_age_limit = 2
    age_of_dying = 80
    start_birth_age = 24
    end_birth_age = 45
    
    while True:
        num_men = 0
        num_wom = 0
        pop = []
        for i in range(0, pop_initial):
            age = int(random.random() * init_age_limit) + 1
            gender = random.random()
            if gender < .5:
                gender = 0
                num_men = num_men + 1
            else:
                gender = 1
                num_wom = num_wom + 1
            ch_num = 0
            dead = 0
            buf = [age, gender, ch_num, dead]
            pop.append(buf)
        if num_men == num_wom:
            break

    birthing_prob = [.7, .5, .1, .01, .0001, .0000001, .000000001]

    alive_pop_vs_time = []
    tot_pop_vs_time = []
    number_of_child = []
    ax.clear()

    for t in range(time_period):
        num_pop = 0
        num_ch = 0
        for i in pop:
            if i[3] == 1:
                continue
            i[0] = i[0] + 1
            # Checking age for birthing and number of children assuming no one has more than 7
            if i[0] >= start_birth_age and i[0] <= end_birth_age and i[2] < 7:
                if random.random() < birthing_prob[i[2]]:
                    i[2] = i[2] + 1
                    age = 1
                    gender = random.random()
                    if gender < .5:
                        gender = 0
                    else:
                        gender = 1
                    ch_num = 0
                    dead = 0
                    buf = [age, gender, ch_num, dead]
                    pop.append(buf)
                    # Selecting the mate
                    partner = pop[int(random.random() * len(pop))]
                    # Making sure the mate is of teh opposite sex
                    if i[2] != partner[2] and partner[0] >= 18 and partner[0] <= 40:
                        # Increase the num of child of the mate by one
                        partner[2] = partner[2] + 1

            if i[0] > age_of_dying:
                i[3] = 1
            if i[3] == 0:
                num_pop = num_pop + 1
            if i[0] < 18:
                num_ch = num_ch + 1

        alive_pop_vs_time.append(num_pop)
        tot_pop_vs_time.append(len(pop))
        number_of_child.append(num_ch)

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

if __name__ == '__main__':
    root.mainloop()