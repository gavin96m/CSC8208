### NBG code

Position 1:  Chamber paced

- O = none
- A = atrium
- V = ventricle
- D = dual

Position 2: Chamber sensed

- O = none
- A = atrium
- V = ventricle
- D = dual

Position 3:  Response to sensing

- O = none
- T = triggered
- I = inhibited
- D = dual (triggered and inhibited)


Position 4:  Whether rate response is active(R) or disabled(0)

Position 5:  Multisite pacing: absent (0), atrial (A), ventricular (V) or dual (D: A+V). 





### Components

#### version 1 （5）

> [link](https://ieeexplore-ieee-org.libproxy.ncl.ac.uk/document/5562916/references#references)

Lowest Rate Interval (LRI)

Atrio-Ventricular Interval(AVI)

Three auxiliary components

- post ventricular atrial refractory period (PVARP)

  > a blocking interval where atrial sensing cannot occur and mimics the atrial refractory period

- ventricular refractory period (VRP)

  > the blocking interval for ventricular events

- upper rate interval (URI)

  > provides an upper bound for ventricular pacing

  

#### version 2

> from simulation(DOO)

Lower Rate Limit (ppm)", 
Atrial Amplitude (V)", 
Atrial Pulse Width (ms)", 
Ventricular Amplitude (V)", 
Ventricular Pulse Width (ms)", 
Max Sensor Rate",
Reaction Time (ms)",
Response Factor ",
Recovery Time (ms)"



#### version 3

[link](https://www.cardiocases.com/en/pacingdefibrillation/clinical-situation/pm/traditional-pacing-modes)

TODO





### Feature

- Heart Test Cases

  - Multiple cases (matching multiple common symptoms)

    > Generate two ECGs, one for the original state
    > Another for post-assisted state via pacemaker

- Secure (?)

- Remote control modifications

- Battery challenge

  > (set the gas pedal to run faster and simulate power) (?)

- Algorithm





