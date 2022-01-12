# SIR Modelling of spread of COVID-19 🦠

### Model 1. SIR model for an infectious disease:
The SIR model breaks down the population into three-subgroups on the basis of infection.

* **Susceptible.** The subpopulation at risk of contracting the disease
* **Infectious.** The subpopulation that has become infected.
* **Recovered.** The subpopulation that has recovered from infection and is thought to be immune to the disease.
<a href="https://www.codecogs.com/eqnedit.php?latex={Susceptible}&space;\xrightarrow{\frac{\beta&space;S&space;I}{N}}&space;\text{Infectious}&space;\xrightarrow{\gamma&space;I}&space;\text{Recovered}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{Susceptible}&space;\xrightarrow{\frac{\beta&space;S&space;I}{N}}&space;\text{Infectious}&space;\xrightarrow{\gamma&space;I}&space;\text{Recovered}" title="{Susceptible} \xrightarrow{\frac{\beta S I}{N}} \text{Infectious} \xrightarrow{\gamma I} \text{Recovered}" /></a>

| *Model 1* |
|:--:| 
| <img width="1000" height="250" src="https://github.com/Jeevesh28/SIR-Modelling-Covid-19/blob/main/Graphs/Model1.png">| 


### Model 2. SEIR model:
The SEIR model extends the SIR model by adding an additional population compartment containing those individuals who have been exposed to the virus but not yet infective.
* **Exposed.** The subpopulation that has been exposed to the disease but not yet infective.
<a href="https://www.codecogs.com/eqnedit.php?latex=\text{Susceptible}&space;\xrightarrow{\frac{\beta&space;S&space;I}{N}}&space;\text{Exposed}&space;\xrightarrow{\alpha&space;E}&space;\text{Infectious}&space;\xrightarrow{\gamma&space;I}&space;\text{Recovered}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{Susceptible}&space;\xrightarrow{\frac{\beta&space;S&space;I}{N}}&space;\text{Exposed}&space;\xrightarrow{\alpha&space;E}&space;\text{Infectious}&space;\xrightarrow{\gamma&space;I}&space;\text{Recovered}" title="\text{Susceptible} \xrightarrow{\frac{\beta S I}{N}} \text{Exposed} \xrightarrow{\alpha E} \text{Infectious} \xrightarrow{\gamma I} \text{Recovered}" /></a>

| *Model 2* |
|:--:| 
| <img width="1000" height="250" src="https://github.com/Jeevesh28/SIR-Modelling-Covid-19/blob/main/Graphs/Model2.png">| 

### Model 3. SEIR model with Control:
With vaccines and social distancing norms designed to reduce transmission of the virus from individuals in the infective state to susceptible individuals.
We provide a control **parameter u** to indicate the success of these attempts for modelling purposes. u=0 denotes no controls, while u=1 denotes complete isolation of infective individuals. The goal of this model is to see how a social distancing approach influences an epidemic's outcome.

<a href="https://www.codecogs.com/eqnedit.php?latex=\text{Susceptible}&space;\xrightarrow{(1-u)\frac{\beta&space;S&space;I}{N}}&space;\text{Exposed}&space;\xrightarrow{\alpha&space;E}&space;\text{Infectious}&space;\xrightarrow{\gamma&space;I}&space;\text{Recovered}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{Susceptible}&space;\xrightarrow{(1-u)\frac{\beta&space;S&space;I}{N}}&space;\text{Exposed}&space;\xrightarrow{\alpha&space;E}&space;\text{Infectious}&space;\xrightarrow{\gamma&space;I}&space;\text{Recovered}" title="\text{Susceptible} \xrightarrow{(1-u)\frac{\beta S I}{N}} \text{Exposed} \xrightarrow{\alpha E} \text{Infectious} \xrightarrow{\gamma I} \text{Recovered}" /></a>

| *Model 3* |
|:--:| 
| <img width="1000" height="250" src="https://github.com/Jeevesh28/SIR-Modelling-Covid-19/blob/main/Graphs/Model3.png">| 

### Simulation of SIR model using Mesa Agent-based modelling: 📺
Model the spread of COVID-19 using a model based on the SIR model (susceptible, infectious, recovered). The cells are arranged in a grid and several agents (people) migrate between adjacent cells, potentially infecting one another.

**Assumptions:**
* We have a set number of agents (adjustable parameter) who are given random cells in the grid at the start.
* Throughout the simulation, a fixed percentage (adjustable parameter) of the agents are masked or unmasked.
* At every step, an agent either stays at his/her cell or moves to an adjacent one.
* When a susceptible agent is in the same cell as an infected agent, the chance of infection (adjustable parameter) differs between masked and unmasked agents.
* If an agent is infected, he/she recovers and becomes immune after a certain number of simulation steps (adjustable parameter).
* Immunity goes away after a certain number of steps (adjustable parameter) and the agent becomes susceptible once again.

**Visuals:**
* Agents will be represented as circles in our grid.
* Susceptible agents are blue, infected are orange, recovered and immune are green.
* If a circle is (not) filled it means the agent is (not) masked.

<img src="https://github.com/Jeevesh28/SIR-Modelling-Covid-19/blob/main/GIFs/Simulation.gif" align="left" style="display:inline;" width="450" >

<br />
<br />
<br />
<br />
<br />

The following line chart dynamically shows us the number of susceptible, infected, and recovered agents throughout the simulation:
<br />
<br />
<img src="https://github.com/Jeevesh28/SIR-Modelling-Covid-19/blob/main/GIFs/Graph.gif" style="display:inline;" width="450" >
