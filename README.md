# SIR Modeling of spread of COVID-19

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
