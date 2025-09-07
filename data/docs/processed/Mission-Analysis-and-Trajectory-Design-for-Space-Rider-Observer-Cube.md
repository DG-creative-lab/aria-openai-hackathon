### **POLITECNICO DI TORINO**

#### Master’s degree course in Aerospace Engineering Academic Year 2022/2023 Graduation Session July

# **Mission Analysis and Trajectory Design for Space** **Rider Observer Cube**

#### **Supervisors: Defended By:** Prof. Sabrina Corpino Alfredo Gili Dott. Giorgio Ammirante


I


## Abstract

The work of this thesis focuses on two aspects of a 12U CubeSat mission: mission analysis and trajectory
design and optimization. The project in question is Space Rider Observe Cube (SROC), an innovative ESA
demonstration mission carried out by a CubeSat that will be deployed from Space Rider; the mission aims at
demonstrating critical capabilities and technologies required to successfully execute a rendezvous and
docking mission in a safety-sensitive context. Moreover, the project aims at demonstrating key technologies
in the area of proximity operations, especially in the domain of in-orbit servicing, space exploration, and
debris mitigation.


The trajectory design and optimization are achieved by the update and the enhancement of a Matlab code,
previously created by Politecnico di Torino, which interfaces the user with an STK scenario through the STK
Object model software interface. The synergized use of the two software enables the Matlab function to
iterate different possible trajectory solutions on Astrogator, STK’s tool for trajectory design. The relevant
results and properties of these solutions are then saved by the Matlab function in dedicated structures or
plotted in graphs to help the successive analysis and selection of an optimal Mission Control Sequence. This
software analysis tool is used to set the optimal Mission Control Sequence for two ConOps for the SROC
mission: the Observe and the Observe&Retrieve scenarios. Moreover, several deviations from the mission
phases reported in the ConOps are analysed to assess how they affect the subsequent phases. For each of
these possible deviations, it is then verified which respects the constraints on the total duration, total
deltaV, and safety for Space Rider.


The mission analysis part of the thesis focuses on the analysis of the illumination conditions and the ground
station coverage during the mission. An acceptable Line of Sight angle is required during several phases of
the mission since SROC hosts different sensors operating in the visible spectrum to perform its navigation
functions and to take pictures of Space Rider when in its proximity. The ground station coverage is
fundamental to guarantee the downlink of the mission data and to send the send commands to SROC;
during some safety-critical phases, such as the Final Approach, it is fundamental to guarantee a sufficiently
long window of GS visibility.


Finally, several tools of the software DRAMA are described and used to evaluate the orbital lifetime of SROC
(OSCAR tool), its re-entry survival prediction, and the associated on-ground risk for any object surviving the
re-entry phase (SARA tool), and the deltaV cost to be allocated for the debris collision avoidance

manoeuvres.


II


III


## Contents

**LIST OF FIGURES ......................................................................................................................................................... 3**


**LIST OF TABLES ............................................................................................................................................................ 6**


**ACRONYMS ................................................................................................................................................................. 8**


**1** **INTRODUCTION .................................................................................................................................................11**


1.1 The CubeSat Standard ................................................................................................................................. 11

1.2 SROC Mission Introduction ......................................................................................................................... 12

1.3 Space Rider Mission Overview .................................................................................................................... 13

1.4 Thesis outline .............................................................................................................................................. 14


**2** **SROC MISSION OVERVIEW ................................................................................................................................16**


2.1 SROC Mission Architecture ......................................................................................................................... 16

2.2 SROC Mission Requirements ....................................................................................................................... 18

2.2.1 ConOps Requirements ................................................................................................................... 19
2.2.2 Observation Requirements ............................................................................................................ 21
2.2.3 Orbit and Trajectory Requirements ............................................................................................... 22
2.3 SROC Concept of Operations ...................................................................................................................... 23

2.3.1 Observe & Retrieve Scenario ......................................................................................................... 25
2.3.1.1 Observe & Retrieve mission: Commissioning and Performance Verification Phase ....... 25
2.3.1.2 Observe & Retrieve mission: Proximity Operations Phase ............................................. 27
2.3.2 Observe Scenario ........................................................................................................................... 29


**3** **STK SCENARIO ...................................................................................................................................................31**


3.1 Proximity operations ................................................................................................................................... 31

3.2 STK Scenario ................................................................................................................................................ 34

3.2.1 Scenario Settings ............................................................................................................................ 34
3.2.2 Mission Control Sequence ............................................................................................................. 37


**4** **UPDATED MATLAB FUNCTIONS .........................................................................................................................46**


4.1 Analysis Process Overview .......................................................................................................................... 46
4.2 IPA Optimization.......................................................................................................................................... 47

4.3 HP Sequence ............................................................................................................................................... 52


**5** **NOMINAL SCENARIOS ANALYSIS .......................................................................................................................56**


5.1 Ground Station Visibility Analysis ............................................................................................................... 56

5.2 Final Approach Analysis .............................................................................................................................. 59

5.3 WSE Design of Experiment .......................................................................................................................... 61

5.3.1 Ideal Safety Ellipse ......................................................................................................................... 61

5.3.2 DoE Results .................................................................................................................................... 64
5.3.3 Nominal Observation Cycle ............................................................................................................ 68

5.4 Nominal Scenarios DeltaV Budget .............................................................................................................. 73


**6** **VARIANT SCENARIOS ANALYSIS .........................................................................................................................76**


6.1 Variant Events Before HP2 .......................................................................................................................... 76

6.1.1 Longer HP1 ..................................................................................................................................... 78
6.1.2 Longer Commissioning Phase ........................................................................................................ 79


1


6.1.2.1 DeltaV-Down Solution .................................................................................................... 80
6.1.2.2 Time-Down Solution ....................................................................................................... 81
6.1.2.3 Alternative Time-Down Solutions – ATD-1 ..................................................................... 82
6.1.2.4 Alternative Time-Down Solutions – ATD-2 ..................................................................... 86
6.1.2.5 Alternative Time-Down Solutions – ATD-3 ..................................................................... 88
6.1.3 Longer Commissioning and HP1 .................................................................................................... 91
6.1.3.1 DeltaV-Down Solution .................................................................................................... 92
6.1.3.2 Time-Down Solution ....................................................................................................... 93
6.1.3.3 Alternative Time-Down Solutions – ATD-1 ..................................................................... 94
6.1.3.4 Alternative Time-Down Solutions – ATD-2 ..................................................................... 97
6.1.3.5 Alternative Time-Down Solutions – ATD-3 ................................................................... 100
6.2 Variant Events After HP2 ........................................................................................................................... 103
6.2.1 Second Observation cycle ............................................................................................................ 103
6.2.2 End of Mission Phase Analysis ..................................................................................................... 105

6.2.2.1 Hohmann Manoeuvre .................................................................................................. 107

6.2.2.2 CAM near the EP........................................................................................................... 109

6.2.2.3 Semi-Major Axis Increase Manoeuvre .......................................................................... 110

6.3 Variant Scenarios Results Summary .......................................................................................................... 113


**7** **DRAMA ANALYSIS ........................................................................................................................................... 123**


7.1 CROC tool .................................................................................................................................................. 123

7.2 Collision Avoidance Manoeuvre Evaluation .............................................................................................. 123

7.2.1 MASTER Analysis .......................................................................................................................... 124

7.2.2 ARES set-up .................................................................................................................................. 126

7.2.3 Ares results .................................................................................................................................. 128

7.3 OSCAR tool ................................................................................................................................................ 132

7.4 SARA tool .................................................................................................................................................. 135

7.4.1 SARA settings and SROC model definition ................................................................................... 136
7.4.2 SARA results ................................................................................................................................. 139


**8** **CONCLUSIONS ................................................................................................................................................. 142**


**BIBLIOGRAPHY ........................................................................................................................................................ 144**


2


## _List of Figures_

Figure 1.1: CubeSat family from 1U to 12U. Credits: The CubeSat Program, Cal Poly SLO [1]. ....................... 11
Figure 1.2: Space Rider mission. Credits: ESA [5] ............................................................................................ 13
Figure 2.1: SROC external view ........................................................................................................................ 18
Figure 2.2: SROC mission for both the Observe and the Observe & Retrieve scenarios ................................. 24
Figure 2.3: CPVP for nominal (5 days) and variant (10 days) commissioning .................................................. 26
Figure 2.4: IPA + OPA Rendezvous ................................................................................................................... 27
Figure 2.5: Observation sub-phase .................................................................................................................. 28
Figure 3.1: RTN (left) for an elliptical orbit and RIC (right) for a circular orbit ................................................ 31
Figure 3.2: Angle between the InTrack axis of the RIC coordinate system and the velocity vector for the first
12 hours of the simulation .............................................................................................................................. 32
Figure 3.3: Angle between the InTrack axis of the RIC coordinate system and the velocity vector for the first
12 hours of the simulation (no effects of Earth non-sphericity) ..................................................................... 32
Figure 3.4: Space Rider's orbit and reference system ..................................................................................... 33
Figure 3.5: The perimeter of Space Rider's Keep Out Zone in STK .................................................................. 35
Figure 3.6: Example of a target sequence ....................................................................................................... 35
Figure 3.7: ESA prediction for the monthly mean F10.7 index [16] ................................................................ 36
Figure 3.8: ESA prediction for the Monthly AP Index [16] ............................................................................... 37
Figure 3.9: SROC initial trajectory after the deployment ................................................................................ 37
Figure 3.10: SROC deployment overview ........................................................................................................ 38
Figure 3.11: RIC components during the commissioning ................................................................................ 39
Figure 3.12: SROC semi-major axis during commissioning .............................................................................. 39
Figure 3.13: HP1 Trajectory ............................................................................................................................. 40
Figure 3.14: SROC InTrack during IPA ............................................................................................................... 40
Figure 3.15: SROC's relative final motion at the end of the IPA ...................................................................... 41
Figure 3.16: Last orbits for IPA (red) and the OPA (green)............................................................................... 41
Figure 3.17: SROC's trajectory during the OPA – InTrack-Radial plane view ................................................... 42
Figure 3.18: SROC's trajectory during the OPA – CrossTrack-Radial plane view .............................................. 43
Figure 3.19: Last part of the OPA rendezvous (green) and WSE (blue) ........................................................... 43
Figure 3.20: Last relative orbits of the free flight propagation ........................................................................ 44
Figure 3.21: SROC's reltavi trajectory during the HP3 insertion ...................................................................... 45
Figure 3.22: SROC's final relative position at the end of the HP3 insertion .................................................... 45
Figure 4.1: Analysis Process Overview ............................................................................................................. 47
Figure 4.2: Diagram showing the functioning of the IPA optimization ............................................................ 48
Figure 4.3: trajectory during the 24 hours propagation (green) after the IPA (red) ........................................ 49
Figure 4.4: Final position of a not valid HP2 insertion ..................................................................................... 50
Figure 4.5: RIC Rate at the end of the IPA and during the HP2 insertion (up); zoom on the RIC rate after the
ZRV2 manoeuvre (down) ................................................................................................................................. 51
Figure 4.6:Trajectory of a propagation segment (red) after the nominal HP2 insertion (green) .................... 51
Figure 4.7: Matlab functions flowchart ........................................................................................................... 52
Figure 4.8: HP sequence segments .................................................................................................................. 53
Figure 4.9: SROC Range as function of the time from the beginning of the HP; HP2 is on the left and HP3 on
the right ........................................................................................................................................................... 54
Figure 4.10: SROC trajectory as function of the time from the beginning of the HP; HP2 is on the left and
HP3 on the right ............................................................................................................................................... 54
Figure 5.1: GS take over ................................................................................................................................... 58
Figure 5.2: GS take over with an additional ground station ............................................................................ 58
Figure 5.3: INMARSAT -4 GEO constellation .................................................................................................... 59
Figure 5.4: LOS angle during the first 24 after the HP3 end ............................................................................ 60
Figure 5.5: Zoom on one acceptable interval .................................................................................................. 60


3


Figure 5.6: Illumination and GS visibility analysis ............................................................................................ 61
Figure 5.7: Safety Ellipse Plane ........................................................................................................................ 62
Figure 5.8: View perpendicular to the Safety Ellipse ....................................................................................... 62
Figure 5.9: Walking Safety Ellipse offset .......................................................................................................... 63
Figure 5.10: Walking Safety Ellipse geometry.................................................................................................. 63
Figure 5.11:RIC components as functions of the time for the two highlighted WSE (6 hr on the left and 8
hours on the right) ........................................................................................................................................... 66
Figure 5.12: Range as function of the time for the WSE with the longest actual observation duration ......... 68
Figure 5.13: Satisfaction interval for every constraint ..................................................................................... 69
Figure 5.14: LOS illumination angle during the observation phase ................................................................. 69
Figure 5.15: Satisfaction interval for every constraint with a different HP2 duration ..................................... 70
Figure 5.16: Ground station access during the free flight (the SROC line refers to the total access) .............. 71
Figure 5.17: Satisfaction interval for every constraint considering a longer observation sub-phase .............. 72
Figure 6.1: Pre-HP2 variant scenarios .............................................................................................................. 77
Figure 6.2: HP1 trajectory in RIC coordinates for a longer commissioning ..................................................... 78
Figure 6.3: Propagation of a 10-days long commissioning .............................................................................. 79
Figure 6.4: InTrack position as function of the time during the IPA - LongComm (DD) ................................... 80
Figure 6.5: SROC Trajectory during HP1 - LongComm (DD) ............................................................................. 81
Figure 6.6: Alternative time-down solutions comparison and definition ........................................................ 82
Figure 6.7: 3D plot of the total deltaV as function of the total duration and the IPA InTrack target – ATD-1 . 82
Figure 6.8: Total DeltaV as function of the total Duration – ATD-1 ................................................................. 83
Figure 6.9: DeltaV trend according to the IPA duration - ATD-1 ...................................................................... 84
Figure 6.10: 3D plot of the total deltaV as function of the total duration and the IPA InTrack target – ATD-2 86
Figure 6.11: InTrack as a function of the time - ATD-2 .................................................................................... 87
Figure 6.12: 3D plot of the total deltaV as function of the total duration and the IPA InTrack target – ATD-3 88
Figure 6.13: Selected solution for the ATD-3 ................................................................................................... 89
Figure 6.14: InTrack as a function of the time - ATD-3 .................................................................................... 90
Figure 6.15: SROC’s trajectoty during HP1 for a longer commissioning and HP1 ........................................... 92
Figure 6.16: IPA InTrack as a function of the time - LongComm&HP1 (DD) .................................................... 93
Figure 6.17: 3d plot of the results of the ATD-1 analysis ................................................................................. 94
Figure 6.18: Optimal solutions – ATD-1 ........................................................................................................... 95
Figure 6.19: DeltaV trend - ATD-1 .................................................................................................................... 95
Figure 6.20: 3D plot of the results of the ATD-2 analysis ................................................................................ 98
Figure 6.21: Total DeltaV as function of the total duration for the ATD-2 analysis ......................................... 98
Figure 6.22: InTrack as a function of the time - ATD-2 .................................................................................... 99
Figure 6.23: 3D plot of the results of the ATD-3 analysis .............................................................................. 100
Figure 6.24: Total DeltaV as function of the total duration for the ATD-3 analysis ....................................... 101
Figure 6.25: InTrack as a function of the time - ATD-3 .................................................................................. 102
Figure 6.26: Second OPA after the first free flight ......................................................................................... 103
Figure 6.27: Comparison between the range as a function of the time for the first (left) and second(right)
inspection ...................................................................................................................................................... 104
Figure 6.28: Comparison between the range as a function of the time for the first (left) and second(right)
inspection ...................................................................................................................................................... 104
Figure 6.29: HP3 insertion after the second inspection cycle ....................................................................... 105
Figure 6.30: SROC’s range as a function of the time ..................................................................................... 106
Figure 6.31: SROC’s range as a function of the time - zoom on the minimum ranges .................................. 106
Figure 6.32: several Keplerian elements during approximately two SR's orbits ........................................... 107
Figure 6.33: SROC semi-major axis and position vector magnitude before and after the manoeuvre ......... 108
Figure 6.34: SROC’s range as a function of the time considering the Hohmann manoeuvre ....................... 108
Figure 6.35: SROC’s range as a function of the time considering the Hohmann manoeuvre - zoom on the
minimum ranges ............................................................................................................................................ 108
Figure 6.36: Radial separation at the EP ........................................................................................................ 109


4


Figure 6.37: angle between the two orbital planes as a function of the time .............................................. 110
Figure 6.38: 𝜙 angle....................................................................................................................................... 111
Figure 6.39: 𝜙 as a function of the time if the manoeuvre is performed ..................................................... 112
Figure 6.40: 𝜙 as a function of the time if no manoeuvre is performed ...................................................... 112
Figure 6.41: Range as a function of the time if the manoeuvre is performed .............................................. 112
Figure 6.42: Range as a function of the time - zoom on the final hours before the EP ................................. 113
Figure 7.1: SROC body in CROC...................................................................................................................... 123
Figure 7.2:Flux Distribution according to the Impact Azimuth ...................................................................... 125
Figure 7.3: Flux Distribution according to the Impact Elevation ................................................................... 125
Figure 7.4: Flux Distribution according to the Impact Velocity ..................................................................... 126
Figure 7.5: Flux Distribution according to the Object Diameter .................................................................... 126
Figure 7.6: ARES settings ............................................................................................................................... 128
Figure 7.7: Risk reduction and residual risk as function of the ACPL ............................................................ 128
Figure 7.8: Manoeuvres frequency as function of the ACPL ......................................................................... 129
Figure 7.9: First case - Risk reduction and residual risk as function of the ACPL........................................... 129
Figure 7.10: First case - Manoeuvres frequency as function of the ACPL ..................................................... 129
Figure 7.11: Second case - Risk reduction and residual risk as function of the ACPL .................................... 130
Figure 7.12: Second case - Manoeuvres frequency as function of the ACPL ................................................ 130
Figure 7.13: Third case - Risk reduction and residual risk as function of the ACPL ....................................... 130
Figure 7.14: Third case - Manoeuvres frequency as function of the ACPL .................................................... 130
Figure 7.15: Minimum ACPL=10 [-7] - Risk reduction and residual risk as function of the ACPL....................... 131
Figure 7.16: Minimum ACPL=10 [-7] - Manoeuvres frequency as function of the ACPL ................................... 131
Figure 7.17: Required deltaV as function of the number of revolutions for long and short term strategy .. 131
Figure 7.18: Risk reduction, residual risk and remaining risk in function of the mean number of avoidance

manoeuvres ................................................................................................................................................... 132
Figure 7.19: ECSS Sample - SROC altitude vs time ......................................................................................... 133
Figure 7.20: Latest prediction - SROC altitude vs time .................................................................................. 134
Figure 7.21: Lifetime comparison between the worst case and nominal case ............................................. 134
Figure 7.22: Solar activity comparison between worst case and nominal case ............................................ 135
Figure 7.23: Monte Carlo sampling - SROC altitude vs time .......................................................................... 135
Figure 7.24: SARA Basic Settings .................................................................................................................... 136
Figure 7.25: Comparison between SROC internal view (left) with the SARA model (right) .......................... 139
Figure 7.26: Altitude as function of the Time of all Objects .......................................................................... 140
Figure 7.27: Altitude as function of the Downrange of all Objects ............................................................... 141


5


## _List of Tables_

Table 2.1: SROC Mission Architecture ............................................................................................................. 16

Table 2.2: ConOps for Observe & Retrieve scenario ........................................................................................ 24
Table 2.3: ConOps for Observe scenario .......................................................................................................... 24
Table 2.4: Detailed mission phases for the Observe & Retrieve scenario ....................................................... 25
Table 2.5: CPVP sub-phases - Observe & Retrieve - Nominal .......................................................................... 27
Table 2.6: POP sub-phases - Observe & Retrieve - Nominal ........................................................................... 29
Table 2.7: Detailed mission phases for the Observe scenario ......................................................................... 30
Table 3.1: Space Rider Orbital Parameters for the Baseline Scenario ............................................................. 34
Table 4.1: deltaV budget for IPA + HP2 insertion + ZeroRelVel2 ...................................................................... 50
Table 4.2: deltaV and duration of all the HP2 segments ................................................................................. 55
Table 4.3: deltaV and duration of all the HP2 segments ................................................................................. 55
Table 5.1: Ground Station visibility analysis .................................................................................................... 56
Table 5.2: Ground Stations list ......................................................................................................................... 57
Table 5.3: WSE DoE DeltaVs ............................................................................................................................. 65
Table 5.4: WSE DoE FreeFlight Duration .......................................................................................................... 65
Table 5.5: Total duration of the actual observation [hr] .................................................................................. 66
Table 5.6: Total duration of the actual observation [%]................................................................................... 67
Table 5.7: Suitable observation intervals ......................................................................................................... 70
Table 5.8: Suitable observation intervals with a different HP2 duration ......................................................... 70
Table 5.9: Summary of the access analysis during the free flight.................................................................... 71
Table 5.10: Suitable observation intervals with a longer observation phase .................................................. 71
Table 5.11: Summary of the access analysis during the free flight considering a longer observation subphase ............................................................................................................................................................... 72
Table 5.12: DeltaV budget for the nominal observe scenario ......................................................................... 73
Table 5.13: Time budget for the nominal Observe scenario ........................................................................... 74
Table 5.14: DeltaV budget for the nominal Observe&Retrieve scenario ........................................................ 74
Table 5.15: Time budget for the nominal Observe&Retrieve scenario ........................................................... 75
Table 6.1: DeltaV and duration comparison between the nominal and the LongHP1 - DeltaV-Down (DD)
scenarios .......................................................................................................................................................... 78
Table 6.2: DeltaV and duration comparison between the nominal and the LongHP1 - Time-down (TD)
scenarios .......................................................................................................................................................... 79
Table 6.3: DeltaV and duration comparison between the nominal and the LongComm – DeltaV-Down (DD)
scenarios .......................................................................................................................................................... 80
Table 6.4: DeltaV and duration comparison between the nominal and the LongComm - Time-Down (TD)
scenarios .......................................................................................................................................................... 81
Table 6.5: DeltaV and duration comparison between the nominal and the LongComm – ATD-1 scenarios .. 84
Table 6.6: Detailed results properties - ATD-1 ................................................................................................. 85
Table 6.7: Detailed results properties - ATD-2 ................................................................................................. 87
Table 6.8: DeltaV and duration comparison between the nominal and the LongComm – ATD-2 scenarios .. 88
Table 6.9 Detailed results properties - ATD-3 .................................................................................................. 89
Table 6.10: Duration comparison between the nominal and all the time-down solutions in case of a longer
commissioning ................................................................................................................................................. 90
Table 6.11: DeltaV comparison between the nominal and all the time-down solutions in case of a longer
commissioning ................................................................................................................................................. 91
Table 6.12: DeltaV and duration comparison between the nominal and the LongComm&HP1 (DeltaV-down)
scenarios .......................................................................................................................................................... 93
Table 6.13: DeltaV and duration comparison between the nominal and the LongComm&HP1 (Time-down)
scenarios .......................................................................................................................................................... 94
Table 6.14: Detailed results for the ATD-1 solution ......................................................................................... 96


6


Table 6.15: DeltaV and duration comparison between the nominal and the LongComm&HP1 (ATD-1)
scenarios .......................................................................................................................................................... 97
Table 6.16: Detailed results for the ATD-2 solution ......................................................................................... 99
Table 6.17: DeltaV and duration comparison between the nominal and the LongComm&HP1 (ATD-1)
scenarios ........................................................................................................................................................ 100
Table 6.18: Detailed results for the ATD-3 solution ....................................................................................... 101
Table 6.19:Duration comparison between the nominal and all the time-down solutions in case of a longer
commissioning and HP1 ................................................................................................................................ 102
Table 6.20: DeltaV comparison between the nominal and all the time-down solutions in case of a longer
commissioning ............................................................................................................................................... 103
Table 6.21: DeltaV and duration comparison between the nominal and the 2 Inspections scenarios ......... 105
Table 6.22: DeltaV cost for different radial separation values ....................................................................... 110
Table 6.23: Overview for the Observe&Retrieve scenarios ........................................................................... 114

Table 6.24: Overview for the Observe scenarios ........................................................................................... 115

Table 6.25: Overview for the Observe&Retrieve scenarios - Longer HP2 and HP3 ....................................... 117
Table 6.26:Overview for the Observe scenarios - Longer HP2 ...................................................................... 119
Table 6.27: DeltaV budget for the variant scenario MCS with the highest deltaV cost ................................. 121
Table 6.28: Time budget for the variant scenario MCS with the highest deltaV cost ................................... 121
Table 6.29: DeltaV budget for the variant scenario MCS with the highest duration ..................................... 122
Table 6.30: Time budget for the variant scenario MCS with the highest duration ........................................ 122
Table 7.1: Orbit definition in DRAMA ............................................................................................................ 124
Table 7.2: CAM deltaV summary ................................................................................................................... 132
Table 7.3: Components of the SARA model ................................................................................................... 138


7


## _Acronyms_

**ARES** Assessment of Risk Event Statistics


**ASI** Agenzia Spaziale Italiana


**ATD** Alternative Time-Down


**CAM** Collision Avoidance Manoeuvres


**ConOps** Concept of Operations


**COTS** Commercial Off The Shelf


**CPG** Centre Spatial Guyanais


**CPVP** Commissioning and Performance Verification Phase


**CROC** Cross Section of Complex Bodies


**DD** DeltaV-Down


**DOCKS** Docking System


**DoE** Design of Experiment


**DRAMA** Debtris Risk Assessment and Mitigation Analysis


**DRP** Docking & Retrieval Phase


**EMP** End of Mission Phase


**EP** Encounter Point


**ESA** European Space Agency


**FF** free flight


**GS** Ground Station


**HCW** Hill-Clohessy-Whiltshire


**HDRM** Hold Down & Release Mechanism


**HP** Hold Point


**IPA** In Plane Approach


**IPLP** Integration & Pre-Launch Phase


**KOZ** Keep Out Zone


**LCM** Load Controller Module


**LEO** Low Earth Orbit


**LEOP** Launch & Early Operations Phase


**LOS** Line Of Sight


**MCC** Mission Control Centre


**MCS** Mission Control Sequence


**MPCB** Multi-Purpose Cargo Bay


8


**MPCD** Multi-Purpose CubeSat Dispenser


**OPA** Out of Plane Approach


**OSCAR** Orbital SpaceCraft Active Removal


**POP** Proximity Operations Phase


**Qx** Quarter x (of a year)


**SARA** Re-entry Survival and Risk Analysis


**SR** Space Rider


**SROC** Space Rider Observer Cube


**STK** System Tool Kit


**TD** Time-Down


**UHF** Ultra-high frequency


**WSE** Walking Safety Ellipses


**ZeroRelVel** Zero Relative Velocity


9


10


## _1 Introducton_ _i_

##### 1.1 The CubeSat Standard

CubeSat is a small satellites class developed by Prof. Jordi Puig-Suari at California Polytechnic State
University (Cal Poly) and Prof. Bob Twiggs at Stanford University’s Space Systems Development Laboratory
(SSDL) starting from 1999. It adopts a standard size and form factor, whose base unit is called ‘U’: as per
CubeSat Design Specification [1], a 1U CubeSat is a cube with a 10 cm side and a maximum weight of 2 kg.


The adoption of this standard is due to the original goal of this project: to provide affordable access to space
for the university and the science community [2]. Indeed, the standardized CubeSat platform can help
reduce the cost and the duration of the development of a space mission, since it promotes a highly
modular, highly integrated system where most, if not all, subsystems can be purchased as COTS products
from many different suppliers. Moreover, standard dimensions enable the use of a container to store the
CubeSat inside a launcher, thus minimizing flight safety issues and simplifying its accommodation.


In the last years, with the increase in the complexity and performance required by the recent CubeSat
mission, bigger form factors were used, such as 6U and 12U (used by SROC). A comparison of the volume
and shape of the most usual form factors is shown in Figure 1.1.
## _i_



_Figure 1.1: CubeSat family from 1U to 12U. Credits: The CubeSat Program, Cal Poly SLO [1]._


Thanks to all these advantages and the introduction of miniaturized technologies, CubeSat have also gained
increasingly more attention from government agencies and commercial groups. For example, ESA finds this
technology very promising in the following applications [3]:


  Driving the drastic miniaturisation of systems, recurring to new approaches to packing and
integration of subsystems

  Demonstrating, in an affordable way, new technologies and novel techniques for formation flying,
proximity operations, rendezvous and docking (SROC falls within this category)

  Carrying out distributed multiple in-situ measurements

  - Deploying small payload

  Augmenting solar system exploration


11


_Chapter 1 - Introductoni_

##### 1.2 SROC Mission Introducton i


Space Rider Observer Cube (SROC) is an ESA mission for in-orbit servicing developed by Politecnico di
Torino, Tyvak International and the University of Padova.


**SROC mission statement**
_To operate a CubeSat in LEO to demonstrate capabilities in the close-proximity operations domain in a_

_safety-critical context, including rendezvous and docking with another operational spacecraft._


The SROC multipurpose space system is constituted by a 12U CubeSat (which will be referred to as SROC
from here on out) and a deployment & retrieval system. The mission features Proximity Operations in the
vicinity of Space Rider, then Docking with the mothership and re-entering Earth with it, while always
ensuring the maximum safety for Space Rider.


To perform this mission, critical technologies and capabilities in the area of proximity operation will be
developed and tested, thus advancing key technologies in the field of proximity operations. This in-orbit
demonstration can provide a great drive forward for nanosatellites application in many fields, such as
inspection missions, in-orbit servicing, space exploration and debris mitigation.


The SROC mission will advance current CubeSat technology and capabilities with respect to:


  formation flight, in terms of:

`o` Proximity Navigation
`o` Guidance and Control
`o` Communications
`o` Autonomous operations

  - deployment, docking and retrieval of CubeSats:

`o` Guidance, navigation and control algorithms for close approach up to docking
`o` Deployment and retrieval mechanisms
`o` Docking systems

  space targets observation:

`o` Imaging


Since the project aims at demonstrating many in-orbit novelties in a very high safety-sensitive context, it
may be imposed to implement the SROC programme through different missions with an increasingly high
level of complexity and safety criticality to Space Rider. For this reason, two possible mission concepts have
been defined:


  - Baseline case: the Observe & Retrieve scenario is implemented. This means that SROC is deployed
by Space Rider, performs inspection in its proximity, approaches it, docks with it and it is stowed
inside its cargo bay to re-enter Earth. This scenario would also benefit the Space Rider programme,
since it would demonstrate its capability to deploy and safely retrieve payloads.

  Reduced case: the Observe mission is implemented. It consists of a simplified ConOps where SROC
is not retrieved by Space Rider. Instead, it is safely disposed into space after inspecting SR. This
scenario could be used if the baseline case were considered too much complex or time-demanding.
It is also possible to revert from the Baseline case to the Reduce case in case of off-nominal events
which could prevent a safe docking with Space Rider.


Both the aforementioned ConOps are discussed in Section 2.3. Another possible mission concept, which
was considered during the first phases of the project, involved the repetition of multiple deployments and
retrievals during the same mission; however, this scenario, called Observe & Reuse, was excluded for the
first SROC mission. It is noted that the work of this thesis focuses on the task proposed for the Phase B2 of
the project.


12


_Chapter 1 - Introductoni_

##### 1.3 Space Rider Mission Overview


Space Rider ( **Space** **R** eusable **I** ntegrated **D** emonstrator for **E** urope **R** eturn) is an uncrewed orbital lifting
body spaceplane developed by ESA to provide affordable and routine access to space [4]. The project is part
of ASI’s Programme for Reusable In-orbit Demonstrator in Europe (PRIDE) and has Avio and Thales Alenia
Space as the main manufacturers. Its first flight is currently scheduled for Q4 2024 onboard Vega-C.


Space Rider will operate in LEO and it will be used to provide a space laboratory for many different types of
payload to operate in orbit for a wide variety of applications in missions lasting for a maximum duration of
two months. Space Rider’s main fields are (bur are not limited to) [5]:


  Micro-gravity experimentation

  In-orbit Demonstration & Validation of technologies for exploration, orbital infrastructure servicing,
Earth observation, Earth science, and Telecoms. The SROC mission falls within this category

  In-orbit Applications for Earth monitoring and satellites inspections

  Educational missions

  European pathfinder for commercial services in access and return from Space


The spacecraft is composed of two modules: the Service module (developed by Avio) and the Re-entry
module (developed by Thales). The first one will provide power, thanks to the deployable solar panels,
at **t** iude control, and deorbit capability to the Re-entry module; the two modules will separate just before
the atmospheric re-entry (as shown in Figure 1.2).

_i_

**t**



_Figure 1.2: Space Rider mission. Credits: ESA [5]_


The aerodynamic shape of the Re-entry module is a simple lifting body, which was chosen instead of
operational wings or vertical fins to optimize the internal volume of the Vega rocket fairing. The 3-axis
control is achieved using rear flaps. To guarantee the landing of this module, the lifting body shape will
decelerate the speed below Mach 0.8, then one or two drogue parachutes will be deployed (at 15-12 km of
altitude) to decrease the speed even more. Finally, a controllable gliding parachute, called parafoil, will be
deployed to control the descent phase and guarantee a nearly horizontal touchdown (at approximately 35
m/s) with no wheels [6].


13


_Chapter 1 - Introductoni_

##### 1.4 Thesis outline


This thesis focuses on the mission analysis and the trajectory optimization for the SROC mission. After the
introduction, which aimed on giving some context about the CubeSat standard, the mission and the main
actors involved in the SROC project, the following Chapters will be discussed:


  - **SROC Mission Overview** : the SROC mission is further presented: the mission architecture ( Section
2.1), a selection of requirements ( Section 2.2) and the different concepts of operations ( Section
2.3) are discussed. It is also explained why two different ConOps will be considered for this thesis:
the Observe&Retrieve and the Observe scenarios. This chapter aims at giving more context to the
reader, by highlighting the properties of each phase and their subphases, thus explaining the
constraints or the goals which drive the successive mission analysis and trajectory optimization. Of
course, it is not presented the entirety of the requirements, as well as the two concepts of
operation, but only the portion of them that are interesting for the scope of this analysis. Regarding
the requirements, only the following are reported:

`o` ConOps Requirements (Sub-section 2.2.1);
`o` Observation Requirements (Sub-section 2.2.2);
`o` Orbit & Trajectory (Sub-section 2.2.3).

  - **STK Scenario** : this chapter describes the reference system used for the analysis (Section 3.1) and
the STK scenario (Section 3.2). This last treatment is divided into two parts: the first one is the
description of the settings of the virtual models of SROC and Space Rider (SR) and the assumptions
at the foundation of the orbital propagators used (Sub-section 3.2.1). The second part (Sub-section
3.2.2) describes the nominal Mission Control Sequence (MCS), which is the collection of different
segments used by STK to simulate SROC’s relative trajectory to SR.

  **Updated Matlab Functions** : it illustrates how the STK scenario and the Matlab functions are used
together to define and optimize SROC’s trajectory (Section 4.1). After describing the functioning of
the software foundation for this analysis, the focus switches to two Matlab functions in particular:
the IPA optimization one (Section 4.2) and HP definition one (Section 4.3). Only these two functions
are detailly described since they are the ones that have been mostly changed. The other smaller
changes that have been applied to the code are also listed at the beginning of the chapter.

  - **Nominal Scenarios Analysis** : after describing how the different software is used to set, analyse, and
optimize the mission, it is possible to illustrate the analysis performed to study the Nominal
Scenarios. Two Nominal Scenarios are considered: the Observe and the Observe & Retrieve. The
first one will be adopted for the first mission of SROC, while the second one will be the baseline for
the successive mission. These tasks were already performed in previous cycles of the mission,
however, they needed to be performed again to be updated, since they referred to an outdated
orbit. The main tasks associated with this update are the following:

`o` Study the ground station visibility analysis (Section 5.1) and propose different solutions to

increase the duration of the longest visibility window;
`o` Study both the visibility and the ground station coverage required to perform the Final

Approach after the HP3 (Section 5.2);
`o` Perform the Desing of Experiment (DoE) to define the best relative trajectory (specifically

called Walking Safety Ellipse) during the observation phase;
Finally, after updating the STK scenario, the Matlab functions, and the Walking Safety Ellipse, the
deltaV budget and the total duration breakdown into the duration of the single mission segments
(referred as “time budget”) for the nominal scenarios are presented (Section 5.4).

  - **Variant Scenarios Analysis** : here, one of the most important parts of the work is described: the
study of the variant scenarios which could take place instead of the nominal ones. The main variant
mission segments, caused by a programmatic or operational event, are analysed and discussed to
assess the robustness of the SROC mission. For each mission segment considered, the origin of his
divergence with the nominal scenario, its impact on the total deltaV and the total duration of the
mission are presented. For a few variant scenarios which may cause relevant problems for the total
duration of the mission, possible recovery manoeuvres are discussed. As it will be better explained


14


_Chapter 1 - Introductoni_


in the relative section, to simplify the analysis, the Hold Point 2 was used as a discontinuity point
where the effects of the variant events prior to it do not impact the successive mission segments.
Therefore, the Chapter is divided into the following sections:

`o` Variant mission segments before HP2 (Section 6.1);
`o` Variant mission segments after HP2 (Section 6.2), which also include the analysis of

different manoeuvre to avoid or delay the encounter with Space Rider after the end of the
proximity operation phase. In fact, because of the drag, SROC drifts more and more away
from SR until it approaches it from behind;
Finally, all these variant scenarios are summarized in several tables to understand which ones must
be labelled as off-nominal. The criteria by which a scenario is defined as off-nominal are also
described (Section 6.3).

- **DRAMA Analysis** : this final chapter focuses on the different tasks performed using the ESA’s
software DRAMA and its following tools:

`o` CROC: used to define the mass and volume properties of the spacecraft (Section 7.1);
`o` ARES and Master used to evaluate the Collision Avoidance Manoeuvres (CAMs) from space

debris (Section 7.2);
`o` OSCAR: used to verify that the mission is compliant with ESA’s space debris mitigation for

agency projects [7] (Section 7.3).
`o` SARA: used to verify that the whole spacecraft will burn in the atmosphere and to assess

the risk of on-ground objects surviving the re-entry (Section 7.4).


15


## _2 SROC Mission Overview_

##### 2.1 SROC Mission Architecture

Summarizes the mission architecture, describing the baseline mission with some possible options which are
still being analysed.


_Table 2.1: SROC Mission Architecture_













|Mission elements|Description of baseline|Comments|
|---|---|---|
||||
|**Subject**|Space Rider observatons|For the baseline design it is required to<br>achieve a 1 cm spatal resoluton|
|**Subject**|Close Proximity Operatons<br>demonstraton|This demonstraton will include the<br>following manoeuvres:<br> <br>Hold Points (HP) acquisiton<br> <br>Inserton into rendezvous<br>trajectories to Space Rider<br> <br>Inserton into Space Rider<br>observaton trajectories<br>It will also determine the relatve distance<br>from Space Rider and the acquisiton of<br>Space Rider imagery|
|**Subject**|Docking & Retrieval capability<br>demonstraton (occurs only for the<br>Observe & Retrieve scenario)|SROC is deployed and retrieved|
|**Payload**|Visual camera|Visual camera with_ad-hoc_optcs|
|**Space Segment**|1 CubeSat (SROC)|The CubeSat (Figure 2.1) has a 12U form<br>factor and it is equipped with cold gas<br>propulsion system and body mounted solar<br>arrays|
|**Space Segment**|1 Mult-Purpose CubeSat Dispenser<br>(MPCD)|This deployer is used only for the baseline<br>scenario,<br>since<br>it<br>requires<br>specifc<br>propertes to guarantee the docking with<br>SROC. In case the reduce scenario is<br>considered, a standard 12U CubeSat<br>deployer could be used instead|
|**Space Segment**|1 Docking System (DOCKS)|DOCK is the interface between the MPCD<br>and SROC; it includes:<br> <br>Sensor suite for supportng the<br>navigaton functon for relatve<br>distance minor to 1 m<br> <br>Mechanisms to provide sof and<br>hard docking of SROC to Space<br>Rider|


16


_Chapter 2 - SROC Mission Overview_











|Orbit and<br>constellation|Quasi-equatorial circular Low Earth<br>Orbit at 400 km with i = 5.2 deg|Col3|
|---|---|---|
|**Orbit and**<br>**constellaton**|Formaton fight with respect to<br>Space Rider|Rendezvous trajectories:<br> <br>In-plane approach segment<br> <br>Out-of-plane approach segment<br>Space Rider observaton:<br> <br>Walking Safety Ellipses (WSE) with<br>relatve inclinaton change and<br>variable geometry<br>HP inserton and maintenance<br>Potental Collision Avoidance Manoeuvres<br>(CAM) to avoid space debris<br>Docking: along the in-track axis|
|**Orbit and**<br>**constellaton**|Disposal orbit|Potental Collision Avoidance Manoeuvres<br>(CAM) to avoid space debris, up to<br>passivaton of the satellite. Of course, this<br>secton only applies for the Observe<br>scenario.|
|**Orbit and**<br>**constellaton**|Re-entry (uncontrolled) orbit|Natural decay within 2025-11-16; this<br>applies only for the Observe scenario.|
|**Communicaton**<br>**Architecture**|Store and Forward architecture|Direct link to Earth for communicatons<br>purposes.<br>Another opton, although not baselined, is<br>to use the crosslink between SROC and the<br>MPCD to support the navigaton functon.<br>_Note: a third opton, described in Secton_<br>_5.1, envisages the use of a GEO satellite_<br>_constellaton to perform data relay of_<br>_SROC’s data_|
|**Ground Segment**|Ground staton network|Network of S-band and UHF ground<br>statons; the compatbility with Estrack<br>network is guaranteed|
|**Ground Segment**|Mission Control Centre (MCC)|SROC MCC is in Torino and will be in<br>contact with the Space Rider MCC for<br>specifc mission phases or needs.|
|**Operatons**|Mission Planning|Main driver for operatons design: safety,<br>reliability and autonomy|
|**Operatons**|Spacecraf Control|Compliant with ESA standard|
|**Operatons**|Flight Dynamics|Compliant with Space Rider operatons|
|**Launch Segment**|Centre Spatal Guyanais (CSG) + Vega<br>C + Space Rider|The launch was assumed to take plane<br>during Q4 2024, during Space Rider<br>maiden fight|


17




_Chapter 2 - SROC Mission Overview_


_Figure 2.1: SROC external view_

##### 2.2 SROC Mission Requirements


The high-level requirements for the SROC mission were written considering:


  the Technology Traceability Matrix and the mission objectives

  - the Statement of Work for the development of Phase B1 of the project

  - the Mission Requirements Document made available during Phase B1

  - Space Rider User Manual, and other requirements and constraints linked to the Space Rider project,
such as the Payload Safety, Space Debris and Collision Avoidance Requirements

  the Space Debris Mitigation Policy for Agency Project [7]

  - the trajectory design and mission analysis conducted as part of the Phase B1


Reporting the full SROC requirements specification would be unnecessary to understand the aspects of the
mission concerning this thesis, which are mission analysis and trajectory design. Instead, a collection of the
most relevant to the scope of this work is presented in the following format:


18


_Chapter 2 - SROC Mission Overview_

|Requirement ID|Requirement Title|
|---|---|
|Requirement text|Requirement text|



2.2.1 ConOps Requirements

|SROC-MIS-001|CubeSat in SR mission|
|---|---|
|The mission shall employ a CubeSat as a SR Deployable Payload (D-PL (KZ)) that can separate from Space<br>Rider MPCB into its own free-fying mission with operatons within the Space Rider Keep Out Zone|The mission shall employ a CubeSat as a SR Deployable Payload (D-PL (KZ)) that can separate from Space<br>Rider MPCB into its own free-fying mission with operatons within the Space Rider Keep Out Zone|


|SROC-MIS-002|Mission Scenarios|
|---|---|
|The mission shall be compatble with the mission scenarios defned as:<br> <br>"Observe and Retrieve" (baseline scenario)<br> <br>“Observe” (reduced scenario)<br> <br>_Note: the "Observe and Reuse" mission (enhanced scenario, considered in Phase 0/A) will be considered as_<br>_a future development, but it is excluded as possible scenario for the frst fight and it has not been studied in_<br>_Phase B1_|The mission shall be compatble with the mission scenarios defned as:<br> <br>"Observe and Retrieve" (baseline scenario)<br> <br>“Observe” (reduced scenario)<br> <br>_Note: the "Observe and Reuse" mission (enhanced scenario, considered in Phase 0/A) will be considered as_<br>_a future development, but it is excluded as possible scenario for the frst fight and it has not been studied in_<br>_Phase B1_|


|SROC-MIS-003|Launch date|
|---|---|
|SROC mission shall be compatble with the Space Rider's launch date on Q4 2024 (TBC).<br>_Note: Compliance with other late launch dates shall also be guaranteed_|SROC mission shall be compatble with the Space Rider's launch date on Q4 2024 (TBC).<br>_Note: Compliance with other late launch dates shall also be guaranteed_|


|SROC-MIS-006|Mission phases|
|---|---|
|The following mission phases shall be defned, listed chronologically:<br>• Integraton and Pre-Launch Phase (IPLP)<br>• Launch and Early Operatons Phase (LEOP)<br>• Commissioning and Performance Verifcaton Phase (CPVP)<br>• Proximity Operatons Phase (POP)<br>• Docking and Retrieval Phase (DRP) - only for the "Observe and Retrieve Scenario"<br>• End of Mission Phase (EMP)|The following mission phases shall be defned, listed chronologically:<br>• Integraton and Pre-Launch Phase (IPLP)<br>• Launch and Early Operatons Phase (LEOP)<br>• Commissioning and Performance Verifcaton Phase (CPVP)<br>• Proximity Operatons Phase (POP)<br>• Docking and Retrieval Phase (DRP) - only for the "Observe and Retrieve Scenario"<br>• End of Mission Phase (EMP)|


|SROC-MIS-008|LEOP sub-phases|
|---|---|
|The LEOP shall be divided into the following sub-phases to support SROC release in space:<br> <br>Launch<br> <br>Deployment|The LEOP shall be divided into the following sub-phases to support SROC release in space:<br> <br>Launch<br> <br>Deployment|


|SROC-MIS-009|CPVP functions 1|
|---|---|
|During the CPVP, calibraton and performance verifcaton of all subsystems shall be performed|During the CPVP, calibraton and performance verifcaton of all subsystems shall be performed|


|SROC-MIS-010|CPVP functions 2|
|---|---|
|During the CPVP, compliance to performance specifcatons needed for safe proximity operatons shall be|During the CPVP, compliance to performance specifcatons needed for safe proximity operatons shall be|



19


_Chapter 2 - SROC Mission Overview_


demonstrated.


_Note: are excluded functions that cannot be tested with the target at a certain distance (e.g. close proximity_
_sensors performance) and/or around a virtual point instead of at the actual target (e.g. docking)_

|SROC-MIS-011|CPVP sub-phases|
|---|---|
|The CPVP shall be divided into the following sub-phases to support SROC verifcaton:<br> <br>Commissioning<br> <br>Verifcaton|The CPVP shall be divided into the following sub-phases to support SROC verifcaton:<br> <br>Commissioning<br> <br>Verifcaton|


|SROC-MIS-012|Commissioning duration|
|---|---|
|The Commissioning phase shall take no longer than 7 (TBC) days<br>_Note: target duraton is 5 days_|The Commissioning phase shall take no longer than 7 (TBC) days<br>_Note: target duraton is 5 days_|


|SROC-MIS-013|POP functions|
|---|---|
|During the POP, SROC shall perform on-orbit observatons of Space Rider taken in its vicinity|During the POP, SROC shall perform on-orbit observatons of Space Rider taken in its vicinity|


|SROC-MIS-014|POP sub-phases|
|---|---|
|The POP shall be divided into the following sub-phases to support autonomous safe proximity operatons:<br> <br>Rendezvous <br> <br>Observaton|The POP shall be divided into the following sub-phases to support autonomous safe proximity operatons:<br> <br>Rendezvous <br> <br>Observaton|


|SROC-MIS-015|POP sub-phases|
|---|---|
|During the DRP, the mission shall demonstrate in orbit CubeSat docking and retrieval capabilites|During the DRP, the mission shall demonstrate in orbit CubeSat docking and retrieval capabilites|


|SROC-MIS-016|DRP sub-phases|
|---|---|
|The DRP shall be divided into the following sub-phases to support safe docking and retrieval operatons of<br>SROC into Space Rider MPCB:<br> <br>Closing <br> <br>Final Approach <br> <br>Matng <br> <br>Retrieval|The DRP shall be divided into the following sub-phases to support safe docking and retrieval operatons of<br>SROC into Space Rider MPCB:<br> <br>Closing <br> <br>Final Approach <br> <br>Matng <br> <br>Retrieval|


|SROC-MIS-017|EMP functions|
|---|---|
|The EMP shall consist of:<br> <br>Moving SROC into a disposal orbit which does not interfere with Space Rider (for "Observe<br>Scenario"); or <br> <br>Retrieval and storage of SROC in the MPCD for Earth return within the Space Rider MPCB (for<br>"Observe & Retrieve Scenario")|The EMP shall consist of:<br> <br>Moving SROC into a disposal orbit which does not interfere with Space Rider (for "Observe<br>Scenario"); or <br> <br>Retrieval and storage of SROC in the MPCD for Earth return within the Space Rider MPCB (for<br>"Observe & Retrieve Scenario")|



20


_Chapter 2 - SROC Mission Overview_

|SROC-MIS-018|EMP subphases|
|---|---|
|The EMP shall be divided into the following sub-phases according to the applicable mission scenario:<br>-Observe and Retrieve scenario:<br> <br>Re-entry<br> <br>Post-landing<br> <br>Post-fight<br>-Observe scenario:<br> <br>Disposal<br> <br>Re-entry|The EMP shall be divided into the following sub-phases according to the applicable mission scenario:<br>-Observe and Retrieve scenario:<br> <br>Re-entry<br> <br>Post-landing<br> <br>Post-fight<br>-Observe scenario:<br> <br>Disposal<br> <br>Re-entry|


|SROC-MIS-019|Scenario switch|
|---|---|
|In case of of-nominal performance during the "Observe & Retrieve Scenario", the mission shall be able to<br>revert back to the "Observe Scenario" and SROC shall be decommissioned accordingly|In case of of-nominal performance during the "Observe & Retrieve Scenario", the mission shall be able to<br>revert back to the "Observe Scenario" and SROC shall be decommissioned accordingly|


|SROC-MIS-020|Hold points|
|---|---|
|The SROC approach trajectory towards SR shall include predefned hold-points where SROC can receive<br>“go/no-go” commands from the SROC and SR mission control centres|The SROC approach trajectory towards SR shall include predefned hold-points where SROC can receive<br>“go/no-go” commands from the SROC and SR mission control centres|


|SROC-MIS-021|Collision Avoidance Manoeuvre (CAM)|
|---|---|
|SROC shall be able to perform CAMs, commanded by the SROC MCC, in case of high-risk conjuncton<br>events with spacecraf or space debris|SROC shall be able to perform CAMs, commanded by the SROC MCC, in case of high-risk conjuncton<br>events with spacecraf or space debris|


|SROC-MIS-022|CAM capability|
|---|---|
|In case of of-nominal performance during the "Observe & Retrieve Scenario", the mission shall be able to<br>revert back to the "Observe Scenario" and SROC shall be decommissioned accordingly|In case of of-nominal performance during the "Observe & Retrieve Scenario", the mission shall be able to<br>revert back to the "Observe Scenario" and SROC shall be decommissioned accordingly|


|SROC-MIS-023|ESTRACK compatibility|
|---|---|
|All aspects of the SROC mission shall be compatble with the network of ESA ground statons|All aspects of the SROC mission shall be compatble with the network of ESA ground statons|


|SROC-MIS-026|Space Debris Mitigation Policy|
|---|---|
|All aspects of the SROC mission shall be compliant with the Space Debris Mitgaton for Agency Projects [7]|All aspects of the SROC mission shall be compliant with the Space Debris Mitgaton for Agency Projects [7]|



2.2.2 Observaton Requirements i

|SROC-MIS-040|SR observation phase coverage|
|---|---|
|The mission should achieve at least 90% (TBC) of Space Rider coverage mapping except for areas which<br>might be permanently in shadow during the observaton|The mission should achieve at least 90% (TBC) of Space Rider coverage mapping except for areas which<br>might be permanently in shadow during the observaton|


|SROC-MIS-044|Observation Distance|
|---|---|
|The observaton and imagery of Space Rider shall be taken from a relatve distance between SROC and<br>Space Rider > 200 (TBC) m, i.e. from outside the KOZ|The observaton and imagery of Space Rider shall be taken from a relatve distance between SROC and<br>Space Rider > 200 (TBC) m, i.e. from outside the KOZ|



21


_Chapter 2 - SROC Mission Overview_

|SROC-MIS-045|SR Single Inspection duratoi n|
|---|---|
|Each observaton cycle of Space Rider shall have a duraton of at least 4 (TBC) hours|Each observaton cycle of Space Rider shall have a duraton of at least 4 (TBC) hours|


|SROC-MIS-046|Observation cycles|
|---|---|
|SROC shall perform at least 1 (TBC) observaton cycle of Space Rider|SROC shall perform at least 1 (TBC) observaton cycle of Space Rider|


|SROC-MIS-047|Relative velocity|
|---|---|
|The transversal component of the relatve velocity between SROC spacecraf and Space Rider surface shall<br>be less than 1.5 (TBC) m/s during the observaton of Space Rider.<br>_Note: considering an imaging system exposure tme of 0.01 s._|The transversal component of the relatve velocity between SROC spacecraf and Space Rider surface shall<br>be less than 1.5 (TBC) m/s during the observaton of Space Rider.<br>_Note: considering an imaging system exposure tme of 0.01 s._|



2.2.3 Orbit and Trajectory Requirements

|SROC-MIS-050|Operational orbit|
|---|---|
|SROC shall be compatble with an operatonal orbit in LEO (nominal 400 km circular) and inclinaton<br>between 5-55 degrees, or SSO|SROC shall be compatble with an operatonal orbit in LEO (nominal 400 km circular) and inclinaton<br>between 5-55 degrees, or SSO|


|SROC-MIS-051|HP1 trajectory|
|---|---|
|SROC shall be able to acquire a trajectory around a virtual point (HP1) with null mean moton in the<br>positve InTrack directon at a defned relatve distance from Space Rider.<br>_Note: the relatve distance between HP1 and SR along the positve InTrack axis depends on the duraton of_<br>_the Commissioning phase. The range is approximately 330 – 1400 km_|SROC shall be able to acquire a trajectory around a virtual point (HP1) with null mean moton in the<br>positve InTrack directon at a defned relatve distance from Space Rider.<br>_Note: the relatve distance between HP1 and SR along the positve InTrack axis depends on the duraton of_<br>_the Commissioning phase. The range is approximately 330 – 1400 km_|


|SROC-MIS-052|HP1 maintenance|
|---|---|
|SROC shall be able to maintain the HP1 trajectory for at least 3 (TBC) hours without manoeuvring<br>_Note: the HP1 is useful to perform manoeuvres for demonstratng the required capabilites for proximity_<br>_operatons (e.g., orbit determinaton and control, atude determinaton and control) and to decide_<br>_whether to start the rendezvous or not_|SROC shall be able to maintain the HP1 trajectory for at least 3 (TBC) hours without manoeuvring<br>_Note: the HP1 is useful to perform manoeuvres for demonstratng the required capabilites for proximity_<br>_operatons (e.g., orbit determinaton and control, atude determinaton and control) and to decide_<br>_whether to start the rendezvous or not_|


|SROC-MIS-053|HP2 trajectory|
|---|---|
|SROC shall be able to acquire a hold point (HP2) at 2 - 5 (TBC) km from Space Rider along the positve<br>InTrack axis<br>_Note: the HP2 is useful to set up the navigaton sensor suite for proximity operatons and lock the target._<br>_The set up and locking can be also done during the rendezvous, i.e. without the need of HP2, but having a_<br>_steady point in space is preferred from a GNC perspectve_|SROC shall be able to acquire a hold point (HP2) at 2 - 5 (TBC) km from Space Rider along the positve<br>InTrack axis<br>_Note: the HP2 is useful to set up the navigaton sensor suite for proximity operatons and lock the target._<br>_The set up and locking can be also done during the rendezvous, i.e. without the need of HP2, but having a_<br>_steady point in space is preferred from a GNC perspectve_|


|SROC-MIS-054|HP2 maintenance|
|---|---|
|||
|SROC shall maintain the trajectory in the HP2 with null relatve moton wrt SR for at least 3 (TBC) hours|SROC shall maintain the trajectory in the HP2 with null relatve moton wrt SR for at least 3 (TBC) hours|



22


_Chapter 2 - SROC Mission Overview_

|SROC-MIS-056|WSE geometry|
|---|---|
|SROC shall perform the observaton of SR remaining within a passive safe and out of plane Walking Safety<br>Ellipse (WSE) trajectory, whose geometry is defned by the following parameters:<br> <br>_Note: see Secton 5.3 for a more detailed descripton_|SROC shall perform the observaton of SR remaining within a passive safe and out of plane Walking Safety<br>Ellipse (WSE) trajectory, whose geometry is defned by the following parameters:<br> <br>_Note: see Secton 5.3 for a more detailed descripton_|


|SROC-MIS-057|SROC KOZ|
|---|---|
|SROC trajectories shall not cross the Space Rider KOZ defned as 200 (TBC) m radius sphere centred at the<br>Space Rider vehicle centre of mass<br>_Note: SROC is allowed to enter the KOZ during mission-specifc phases (deployment, fnal approach and_<br>_docking) agreed with Space Rider_|SROC trajectories shall not cross the Space Rider KOZ defned as 200 (TBC) m radius sphere centred at the<br>Space Rider vehicle centre of mass<br>_Note: SROC is allowed to enter the KOZ during mission-specifc phases (deployment, fnal approach and_<br>_docking) agreed with Space Rider_|


|SROC-MIS-058|HP3 trajectory|
|---|---|
|SROC shall be able to acquire one of the following holding trajectories (HP3) to reach the Radial or InTrack<br>axis depending on the selected docking opton:<br> <br>InTrack docking: Holding consists of a trajectory with null relatve moton wrt Space Rider < 150<br>(TBC) m along the positve InTrack axis <br> <br>Radial docking: Holding consists of a passive-safe out-of-plane closing trajectory untl reaching the<br>radial axis/approach corridor. This trajectory maintains SROC < 150 (TBC) m mean distance from<br>Space Rider.|SROC shall be able to acquire one of the following holding trajectories (HP3) to reach the Radial or InTrack<br>axis depending on the selected docking opton:<br> <br>InTrack docking: Holding consists of a trajectory with null relatve moton wrt Space Rider < 150<br>(TBC) m along the positve InTrack axis <br> <br>Radial docking: Holding consists of a passive-safe out-of-plane closing trajectory untl reaching the<br>radial axis/approach corridor. This trajectory maintains SROC < 150 (TBC) m mean distance from<br>Space Rider.|


|SROC-MIS-059|HP3 maintenance|
|---|---|
|SROC shall maintain the holding trajectory HP3 for at least 3 (TBC) hours|SROC shall maintain the holding trajectory HP3 for at least 3 (TBC) hours|


|SROC-MIS-060|Maximum deltaV|
|---|---|
|The ΔV for all SROC manoeuvres shall be less than 20 (TBC) m/s including margins|The ΔV for all SROC manoeuvres shall be less than 20 (TBC) m/s including margins|

##### i

##### 2.3 SROC Concept of Operat i ons


As mentioned before, three possible mission scenarios have been conceived: observe, observe & retrieve,
observe & reuse. While the observe & reuse scenario was not evaluated, both the observe and observe &
retrieve were analysed, although later on it was decided to implement the observe scenario for SROC’s first
mission. Figure 2.2 shows the main phases for both the scenarios, highlighting the fact that, until the
completion of the inspection phase, the two missions are identical.


23


_Chapter 2 - SROC Mission Overview_


_Figure 2.2: SROC mission for both the Observe and the Observe & Retrieve scenarios_


In the baseline scenario, SROC will be launched inside Space Rider with Vega C (the target launch is the
Space Rider Maiden Flight, which is scheduled for Q4 2024), then it will be deployed in orbit using the
MPCD. Once deployed, SROC will finish the commissioning, then it will fly in formation with Space Rider and
take pictures of it. Instead of performing the docking with SR, the SROC spacecraft will be decommissioned
in orbit without further interaction with Space Rider. Table 2.2 and Table 2.3 describe the two ConOps and
their relative mission phases and sub-phases.



_Table 2.2: ConOps for Observe & Retrieve scenario_



_Table 2.3: ConOps for Observe scenario_










|Mission phase|Mission subphases|
|---|---|
|||
|**Integraton & Pre-**<br>**Launch Phase (IPLP)**| <br>Integraton Phase<br> <br>Pre-Launch Phase|
|**Launch & Early**<br>**Operatons Phase**<br>**(LEOP)**| <br>Launch Phase<br> <br>Deployment Phase|
|**Commissioning and**<br>**Performance**<br>**Verifcaton Phase**<br>**(CPVP)**| <br>Commissioning<br>Phase<br> <br>Verifcaton Phase|
|**Proximity Operatons**<br>**Phase (POP)**| <br>Rendezvous Phase<br> <br>Space<br>Rider<br>Observaton Phase|
|**End of Mission Phase**<br>**(EMP)**| <br>Disposal phase<br> <br>Re-entry phase|


|Mission phase|Mission subphases|
|---|---|
|**Integraton & Pre-**<br>**Launch Phase (IPLP)**| <br>Integraton Phase<br> <br>Pre-Launch Phase|
|**Launch & Early**<br>**Operatons Phase**<br>**(LEOP)**| <br>Launch Phase<br> <br>Deployment Phase|
|**Commissioning and**<br>**Performance**<br>**Verifcaton Phase**<br>**(CPVP)**| <br>Commissioning<br>Phase<br> <br>Verifcaton Phase|
|**Proximity Operatons**<br>**Phase (POP)**| <br>Rendezvous Phase<br> <br>Space<br>Rider<br>Observaton Phase|
|**Docking & Retrieval**<br>**Phase (DRP)**| <br>Closing Phase<br> <br>Final<br>Approach<br>Phase<br> <br>Matng Phase<br> <br>Retrieval Phase|
|**End of Mission Phase**<br>**(EMP)**| <br>Re-entry Phase<br> <br>Post-landing Phase<br> <br>Post-fight Phase|



For the Observe and Retrieve scenario, the maximum duration from the deployment to the docking with
Space Rider is less than 30 days (the duration of the nominal scenario in STK is 13.773 days considering also
the margins). For the Observe scenario, the duration of the operation part is very similar, while it requires a
maximum time of 1 year to lower its orbit and disintegrate in Earth’s atmosphere. Any off-scenarios where
one or more mission phases last longer than the nominal case are addressed in Chapter 6.


24


_Chapter 2 - SROC Mission Overview_


2.3.1 Observe & Retrieve Scenario


Table 2.4 describes with more details the Observe & Retrieve scenario phases, with their subphases,
objectives, initial and final conditions.


_Table 2.4: Detailed mission phases for the Observe & Retrieve scenario_


i i



i i



i i



i i


|Mission phase|Mission subphase|Phase description|
|---|---|---|
|**Integraton**<br>**& **<br>**Pre-**<br>**Launch Phase (IPLP)**| <br>Integraton Phase<br> <br>Pre-Launch Phase|_Objectve_: SROC is ready for launch<br>_Inital conditon_: SROC/MPCD ready for<br>integraton into SR<br>_Final conditon_: SR ready for launch|
|**Launch & Early**<br>**Operatons Phase**<br>**(LEOP)**| <br>Launch Phase<br> <br>Deployment Phase|_Objectve_: SROC is released from SR<br>_Inital conditon_: SR is launched<br>_Final conditon_: SROC is distant from SR of at least<br>200 m (TBC)|
|**Commissioning and**<br>**Performance**<br>**Verifcaton Phase**<br>**(CPVP)**| <br>Commissioning Phase<br> <br>Verifcaton Phase|_Objectve_: SROC is commissioned and all its critcal<br>capabilites for proximity operaton are verifed<br>_Inital conditon_: SROC is distant from SR of at<br>least 200 m (TBC)<br>_Final conditon_: SROC is travelling along a safe<br>trajectory from SR (>300 km)|
|**Proximity Operatons**<br>**Phase (POP)**| <br>Rendezvous Phase<br> <br>Space Rider Observaton<br>Phase|_Objectve_: SR performs close observaton of SR<br>_Inital conditon_: SROC is travelling along a safe<br>trajectory from SR (>300 km)<br>_Final conditon_: SROC accomplishes the<br>observaton cycle(s)|
|**Docking & Retrieval**<br>**Phase (DRP)**| <br>Closing Phase<br> <br>Final Approach Phase<br> <br>Matng Phase<br> <br>Retrieval Phase|_Objectve_: SROC goes back into SR’s MPCB<br>_Inital conditon_: SROC accomplishes the<br>observaton cycle(s)<br>_Final conditon_: SROC is stowed into the MPCD<br>into SR’s MPCB|
|**End of Mission Phase**<br>**(EMP)**| <br>Re-entry Phase<br> <br>Post-landing Phase<br> <br>Post-fight Phase|_Objectve_: SROC returns to Earth inside SR’s MPCB<br>_Inital conditon_: ROC is stowed into the MPCD<br>into SR’s MPCB<br>_Final conditon_: SROC and the MPCD are<br>uninstalled from SR’s MPCB and checked out|



In the next sub-sections, the LEOP, CPVP and POP mission phases will be further analysed, while the LEOP,
ILP and EMP will not be detailed because they do not present any manoeuvres in formation with Space
Rider. The Final Approach Phase and the Mating Phase will also not be detailed and they are not analysed
by this thesis, since they involve specific manoeuvre and navigation techniques that are easier to simulate
and analyse in other software than STK.


2.3.1.1 Observe & Retrieve mission: Commissioning and Performance Verifcat i on Phase i


This phase starts when SROC has left SR KOZ and the first signal generated by the satellite has been received
by the ground segment. The KOZ is a fictitious sphere centred in the centre of Space Rider which separates
the space which can be traversed by SROC and the space which cannot be used by the satellite; it is a
constrained aimed at guaranteeing the safety of Space Rider, which can only be transgressed during
previously accepted mission phases (such as the deployment and the Docking and retrieval phase).


25


_Chapter 2 - SROC Mission Overview_


The commissioning and performance verification phase consists of preparing the satellite for its nominal
operations and verifying its critical capability for performing proximity operations in the actual operative
environment. It is composed of two sub-phases: commissioning and performance verification. Figure 2.3
and Table 2.5 present a recap of this phase.

**t** **t**



_Figure 2.3: CPVP for nominal (5 days) and variant (10 days) commissioning_


The commissioning phase duration was evaluated considering the commissioning of previous mission
running the Tyvak bus and adding a safety margin. Since the maximum duration of the mission is relatively
short, it is fundamental to reduce the maximum duration of this phase by evaluating the maximum number
of ground stations able to communicate with SR; for this reason, Section 5.1 is dedicated to this analysis. For
now, the nominal case considers a 5-day commissioning, while a variant longer than 10 days is considered in
Section 6.1. In conclusion, the duration is yet to be confirmed, because it is necessary to confirm the
following information:


  Time needed for checking and calibrating the components

  Number and duration of passes above the ground stations


During this sub-phase SROC is moving along a free flight (FF) trajectory which ends, for the nominal case, at
approximately 373 km along the positive InTrack with respect to Space Rider (the definition of the RIC
coordinate system can be found in Section 3.1).


The performance verification phase is fundamental to test some critical functions of SROC required to
execute proximity manoeuvres; however, the performance of close proximity navigation sensors and of the
payload cannot be tested this far from the target. Since during this phase Space Rider is very distant, the
only capabilities that can be tested are the ones that can be performed using a virtual point. The exact
sequence of operation is yet to be defined, however, the main capabilities to be tested should be the
following:


  Insertion in a Hold Point (HP1) to stop the drift away from Space Rider;

  Collision Avoidance Manoeuvre: at least one artificial CAM, which would use the parameters
calculated for a real CAM performed in proximity of Space Rider, should be tested to verify its
correct execution;

  Insertion into the Walking Safety Ellipse: again, this manoeuvre uses the parameters that define a
real insertion into a trajectory with specific geometrical features (see Section 5.3 for a more indepth definition of the WSE) to observe Space Rider and performs it around a virtual point;

  - At **t** iude change: different manoeuvres to control the at **t** iude will be executed to test the system
performances in terms of pointing accuracy, stability and slew rate. The exact number of
manoeuvres to be tested is yet to be defined;


26


_Chapter 2 - SROC Mission Overview_


  Testing of Space-to-Ground and Ground-to-Space communication links and interoperations with
Space Rider MCC;


_Table 2.5: CPVP sub-phases - Observe & Retrieve - Nominal_


i



i



i


|Sub-phase|Characteristics|Description|
|---|---|---|
|**Commissioning**|_Objectve_: to prepare SROC for<br>nominal operatons<br>_Duraton_: 5 days (target)<br>_Environment_: LEO/FF<br>_Relatve_ _distance_: 1-373 km|_Startng event_: SROC autobeaconing to ground<br>(frst signal acquisiton)<br>_Intermediate events_: <br> <br>Commissioning procedures: RF link<br>establishment, post deployment checkout<br>of platorm subsystems<br> <br>Calibraton of thruster and cameras<br> <br>Test of critcal equipment<br>_Ending event_: post commissioning test passed|
|**Verifcaton**|_Objectve_: rehearsal of critcal<br>operatons<br>_Duraton_: 2 days (target)<br>_Environment_: LEO/FF<br>_Relatve_ _distance_: ~ 373 km|_Startng event_: Command from ground to start<br>experimental phase<br>_Intermediate events_: <br> <br>Test of HP inserton manoeuvre(s)<br> <br>Test of CAM(s)<br> <br>Test of atude manoeuvre(s)<br> <br>Test of WSE inserton manoeuvre(s)<br> <br>Test of communicaton link (TBC)<br>_Ending event_: Verifcaton test passed|



2.3.1.2 Observe & Retrieve mission: Proximity Operatons Phase i


This phase is one of the most critical and featuring of the SROC mission since it is when the satellite
rendezvous Space Rider and then takes pictures of it, thus proving his capabilities of flying in formation with
Space Rider and performing proximity operations. It is divided into two sub-phases: Rendezvous sub-phase
(illustrated in Figure 2.4) and Observation sub-phase (Figure 2.5).

i



_Figure 2.4: IPA + OPA Rendezvous_


27


_Chapter 2 - SROC Mission Overview_


The rendezvous sub-phase first starts with an In-Plane Approach (IPA) where SROC uses its propulsion
system to move from HP1 to a position in proximity to HP2 (from the STK simulation it is at 7 km InTrack),
then SROC performs a Hold Point insertion manoeuvre to reach HP2 with the desired relative velocity. The
HP2 was added to switch between the navigation sensor from far-range navigation to close-range navigation
and as a go/no-go moment where SROC receives from the ground the command to proceed with the
inspection phase. After the completion of the HP2 SROC performs an Out-of-Plane Approach (OPA) to move
to negative InTrack and start the Observation phase.


_Figure 2.5: Observation sub-phase_


The Observation sub-phase consists of one (or more) observation cycle(s), each composed of an inspection
following a Walking Safety Ellipse and a free flight segment. To define the number of observation cycles, the
following factors must be considered:


  - The maximum deltaV available (requirement SROC-MIS-060) limits the maximum number of cycles

  The minimum SR surface to be covered defines a minimum number of cycles (requirement SROCMIS-040)


From previous analyses performed on the WSE and the payload, it was proved that one observation cycle is
enough to meet the requirement SROC-MIS-040. After the WSE insertion, SROC moves along a free flight
relative trajectory and takes pictures of Space Rider when it is in payload range. Then after this segment,
the satellite keeps moving in a free flight motion, but instead of taking pictures of Space Rider, it sends to
the Ground mission data (this segment is called free flight). Defining the correct WSE was a complex task
(discussed in Section 5.3) which involved considering many different parameters and constraints, such as
the total access time of SROC to the Ground Stations during FF or the constraint of not surpassing the 2 km
InTrack position during the FF to avoid losing the lock of SROC visual navigation sensors on SR. Here are just
reported the results useful to the description of the ConOps:


  WSE observation duration: 8 hr

  free flight duration: 8.06 hr

  free flight final InTrack position: 2 km


After this phase, the satellite will either perform a second observation cycle (variant scenario) or pass to the
successive phase (DRP).


28


_Chapter 2 - SROC Mission Overview_


_Table 2.6: POP sub-phases - Observe & Retrieve - Nominal_



|Sub-phase|Characteristics|Description|
|---|---|---|
|**Rendezvous**|_Objectve_: to reduce the relatve<br>distance from SR, reaching a<br>precise positon relatve to it<br>_Duraton_: 5.76 (TBC) days<br>_Environment_: LEO/FF<br>_Relatve_ _distance_: 373 km to<br>hundred meters (>200 m)|_Startng event_: SROC receives the command to<br>start the rendezvous from the Ground<br>_Intermediate events_: <br> <br>IPA: trajectory in the Radial-InTrack plane<br>to reach a specifc positon along positve<br>InTrack (7 km)<br> <br>HP2 inserton to move to the desired fnal<br>positon (2 km along positve InTrack) with<br>the desired fnal relatve velocity (null<br>relatve velocity)<br> <br>HP2 maintenance: maintain of a hold point<br> <br>OPA: trajectory out of the Radial-InTrack<br>plane to reach a specifc positon along<br>negatve InTrack (<600 m)<br>_Ending event_: Acquisiton of the inital conditon to<br>start the observaton sub-phase|
|**Observaton**|_Objectve_: inserton into the WSE<br>to observe SR<br>_Duraton_: 16.06 (TBC) hours<br>_Environment_: LEO/FF<br>_Relatve_ _distance_: > 200 m to 2<br>km|_Startng event_: Command from ground to start the<br>observaton orbit<br>_Intermediate events_: <br> <br>WSE inserton manoeuvre<br> <br>Observaton of SR during WSE<br> <br>Free Flight (FF)<br> <br>OPA to start another Observaton cycle<br>(of-nominal scenario)<br> <br>Manoeuvres to correct the trajectory if<br>needed<br>_Ending event_: Completon of the observaton<br>cycle(s)|


2.3.2 Observe Scenario





For the observe scenario, the ConOps are identical to the Observe & Retrieve scenario until the end of the
Proximity Operations Phase. After that, there is no Docking & Retrieval Phase, but a different End of Mission
Phase. As mentioned before, this scenario was created in case the Observe & Retrieve scenario is
considered too complex for the first mission; moreover, the Observe & Retrieve scenario was designed to
revert back to the Observe scenario in case any off-nominal conditions occur in orbit. This switch can occur
until the final approach is completed.


This scenario required to analyse its EMP phase (described in Sub-section 6.2.2) since it is fundamental to
ensure that no encounter points with Space Rider will happen and that the spacecraft will still be able to
perform CAMs to avoid hitting space debris and provide a more sustainable mission for the space
environment. For this reason, SROC will not be passivated immediately after the proximity operation
completions.


29


_Chapter 2 - SROC Mission Overview_


_Table 2.7: Detailed mission phases for the Observe scenario_





|Mission phase|Mission subphase|Phase description|
|---|---|---|
|**Integraton**<br>**& **<br>**Pre-**<br>**Launch Phase (IPLP)**| <br>Integraton Phase<br> <br>Pre-Launch Phase|_Objectve_: SROC is ready for launch<br>_Inital conditon_: SROC/MPCD ready for<br>integraton into SR<br>_Final conditon_: SR ready for launch|
|**Launch & Early**<br>**Operatons Phase**<br>**(LEOP)**| <br>Launch Phase<br> <br>Deployment Phase|_Objectve_: SROC is released from SR<br>_Inital conditon_: SR is launched<br>_Final conditon_: SROC is distant from SR of at least<br>200 m (TBC)|
|**Commissioning and**<br>**Performance**<br>**Verifcaton Phase**<br>**(CPVP)**| <br>Commissioning Phase<br> <br>Verifcaton Phase|_Objectve_: SROC is commissioned and all its critcal<br>capabilites for proximity operaton are verifed<br>_Inital conditon_: SROC is distant from SR of at<br>least 200 m (TBC)<br>_Final conditon_: SROC is travelling along a safe<br>trajectory from SR (>300 km)|
|**Proximity Operatons**<br>**Phase (POP)**| <br>Rendezvous Phase<br> <br>Space Rider Observaton<br>Phase|_Objectve_: SR performs close observaton of SR<br>_Inital conditon_: SROC is travelling along a safe<br>trajectory from SR (>300 km)<br>_Final conditon_: SROC accomplishes the<br>observaton cycle(s)|
|**End of Mission Phase**<br>**(EMP)**| <br>Disposal Phase<br> <br>Re-entry Phase|_Objectve_: SROC is disposed according to ESA<br>Space Debris Mitgaton<br>_Inital conditon_: SROC accomplishes the<br>observaton cycle(s)<br>_Final conditon_: SROC burned in Earth atmosphere|


30




## _3 STK Scenario_

In this chapter, the settings of the STK scenario and the mission control sequence are described. Before
diving into the description of the software functions, it is also given some context regarding the coordinate
reference systems and the assumption behind the trajectory analysis.

##### 3.1 Proximity operat i ons


Spacecraft proximity operations are the maintenance or the targeting of a desired relative position,
orientation and/or velocity between at least two satellites. This is a complex kind of analysis that requires
the definition and study of the orbits of all the satellites involved: to simplify it and better understand the
relative state of one satellite to another, a Satellite Coordinate System is used [12]. These systems have the
origin in the centre of mass of a “leader” satellite and move with it; this means that the motion of the other
satellite, called “follower”, is evaluated with respect to the leader. Other treaties also use the term “chief”
for the leader and the term “deputy” for follower.


One of these systems, called RTN (Radial Transverse Normal) or LVLH (Local Vertical, Local Horizon) is
centred in the centre of mass of the “leader” satellite, moves with it and has the following axes:


  - R axis points out of from the satellite along the geocentric radius vector; the Radial displacement is
the one evaluated along this axis

  - N axis is normal to the orbital plane; the CrossTrack displacements are the ones evaluated along this

axis

  T axis is normal to the position vector and positive in the direction of the velocity vector; the
AlongTrack displacement is the one evaluated along this axis


If the orbit is circular, the S axis is aligned to the velocity vector: this frame, called RIC (Radial InTrack
CrossTrack) is the reference system that will be used from here on out (see Figure 3.1 for a comparison with
RTN). This reference system is basically the same as the RTN one, with the CrossTrack axis coinciding with
the T axis and with the InTrack axis coinciding with the S axis and parallel to the velocity vector.
##### i



_Figure 3.1: RTN (left) for an elliptical orbit and RIC (right) for a circular orbit_


Of course, this is an approximation, since Space Rider’s orbit is not perfectly circular because of the effect of
the non-sphericity of the Earth (the maximum degree and order of the gravity model used for the
propagator are described in Sub-section 3.2.1). However, as shown in Figure 3.2, the maximum angle
between Space Rider velocity vector and the InTrack axis of the RIC reference system is approximately 0.08
degrees at most, so identifying the distance along the I axis as InTrack generates an almost negligible error.


31


_Chapter 3 - STK Scenario_


_Figure 3.2: Angle between the InTrack axis of the RIC coordinate system and the velocity vector for the first 12 hours of the_

_simulation_


Instead, if a propagator which does not consider any of the effects of the non-sphericity of the Earth is used,
the angle between this vector is negligible (Figure 3.3). Both this graph and the previous one were obtained
using STK’s analysis workbench tool.


_Figure 3.3: Angle between the InTrack axis of the RIC coordinate system and the velocity vector for the first 12 hours of the_

_simulation (no effects of Earth non-sphericity)_


The motion of one satellite with respect to another one is described by a system of non-linear differential
equations, that, with specific conditions, can be linearized and solved more easily. The simplified HillClohessy-Whiltshire (HCW) equations are obtained by making the following assumptions [11]:


1. Small relative position vector magnitude compared to the chief position vector magnitude
2. Pure Keplerian motion of both the leader and the follower
3. Leader spacecraft is on a circular orbit


The assumption of the circular orbit for the leader spacecraft has already been discussed; the first
assumption is respected since, in the nominal scenario, the furthest relative distance is 373 km, which is
one order of magnitude less than Space Rider position vector magnitude (6778.1 km). The pure Keplerian
motion assumption is a rough approximation since the STK scenario considers the effects of external forces
such as the atmospheric drag and the solar radiation pressure. Moreover, even the effects of a continuous
thrust cannot be evaluated under this assumption, since 𝐹 𝑡ℎ𝑟𝑢𝑠𝑡 must be null. However, the effect of an


32


_Chapter 3 - STK Scenario_


impulsive manoeuvre can still be assessed, just by using its resulting velocity as the initial condition to
restart the analysis. Under this assumption the HCW equations are homogeneous:


𝑥̈ + 2𝑛𝑧̇ = 0
𝑦̈ + 𝑛 [2] 𝑦= 0
𝑧̈ −2𝑛𝑥̇ −3𝑛 [2] 𝑧= 0



Where 𝑛=

𝑇 [ and ] [𝑇] [ is the orbital period of the leader satellite. The solutions of this equation are the ]
following:



Where 𝑛=



2∗𝜋



𝑥(𝑡) = −[6𝑛𝑧(0) + 3𝑥̇(0)]𝑡+ [𝑥(0) − [2𝑧̇(0)] 𝑛



𝑛 ] + [6𝑧(0) + [4𝑥̇(0)] 𝑛



𝑛 ] sin (𝑛𝑡) + [2𝑧̇(0)] 𝑛



cos (𝑛𝑡)
𝑛



𝑦(𝑡) = [𝑦̇(0)] sin (𝑛𝑡) + 𝑦(0)cos (𝑛𝑡)

𝑛



𝑧(𝑡) = [4𝑧(0) + [2𝑥̇(0)] 𝑛



𝑛 ] −[3𝑧(0) + [2𝑥(0)] 𝑛



sin (𝑛𝑡) + [𝑧(0)]
𝑛 ~~]~~ 𝑛



sin (𝑛𝑡)
𝑛



𝑥̇(𝑡) = −[6𝑛𝑧(0) + 3𝑥̇(0)] + [6𝑧(𝑜)𝑛+ 4𝑥̇(0)]cos (𝑛𝑡) −2𝑧̇(0)sin (𝑛𝑡)
𝑦̇(𝑡) = 𝑦̇(0)cos (𝑛𝑡) −𝑦(0)𝑛sin (𝑛𝑡)
𝑧̇(𝑡) = 𝑧̇(0)cos 𝑢(𝑛𝑡) + [3𝑛𝑧(0) + 2𝑥̇(0)]sin (𝑛𝑡)


Where 𝑥(0), 𝑦(0), 𝑧(0), 𝑥̇(0), 𝑦̇(0) and 𝑧̇(0) are respectively the positions and velocities along the Radial,
InTrack and CrossTrack directions. Although the inconsistency with the assumptions at the base of the
simplified Hill-Clohessy-Whiltshire equations, this model was still used to perform a small calculation, that is
evaluate the initial conditions to perform the WSE, since it could still give a solid guess of SROC motion
during this sub-phase.


_Figure 3.4: Space Rider's orbit and reference system_


While SROC is defined according to the RIC reference system, Space Rider’s reference orbit is J2000, one of
the most used Earth Centred Inertial reference system. Its axes (shown in Figure 3.4) are defined as follows:


  - X axis: it points from the centre of the Earth to the vernal equinox;

  Y axis: it is defined by the cross-product between Z and X;


33


_Chapter 3 - STK Scenario_


  - Z axis: is normal to the mean equator of date at epoch J2000 (1 January 2000 at 12:00 Universal
Time), which is approximately Earth’s spin axis orientation at that epoch;


Another Satellite Coordinate System which has been used during the analysis is the VNC (Velocity Normal
Co-Normal) reference system [13]. It is centred in the spacecraft’s centre of mass, and the axes point in the
following direction:


  - V: along the Velocity vector

  - N: along the orbit normal

  - C: completes the orthogonal triad ( 𝑍 [̂ ] = 𝑉 [̂ ] × 𝑁 [̂] )


This system is used to define the Thrust Vector components in STK.

##### 3.2 STK Scenario


Now that the coordinate reference system and the analysis process have been defined, this section focuses
on the STK scenario, its settings, and its mission control sequence. Regarding the mission control sequence,
for now, only the nominal Observe & Retrieve and Observe scenarios will be considered, while the variant
analysis will be presented in Chapter 6.


3.2.1 Scenario Setngs ti


The following Space Rider orbit for the Baseline scenario was assumed:


_Table 3.1: Space Rider Orbital Parameters for the Baseline Scenario_

|Orbital Parameter|Value|
|---|---|
|Apoapsis Alttude|400 km|
|Eccentricity|0|
|Inclinaton|6.2 deg|
|Right Ascension of the Ascending node (RAAN)|0 deg|
|Angle of Perigee|0 deg|
|True Anomaly|0 deg|



Since the launch date of Space Rider maiden flight is still not precisely defined, but just refers to a generic
Q4 2024, it was assumed the beginning of the SROC mission on 01 November 2024 (during the middle
month of the fourth quarter). The radius of the KOZ was also updated from 150 m to 200 m (Figure 3.5) to
comply with the new minimum distance required by the Space Rider project.


34


_Chapter 3 - STK Scenario_


_Figure 3.5: The perimeter of Space Rider's Keep Out Zone in STK_


Space Rider’s orbit and its properties, as well as SROC’s, were defined using the Astrogator Tool of STK [10].
This capability enables specialized analysis for orbit manoeuvring and trajectory design and calculates the
ephemeris of the selected satellite(s) following the Mission Control Sequence (MCS). This sequence is
composed of different mission segments, which are dived into two categories: those that generate
ephemeris (for example a manoeuvre or a propagation segment) and those that affect the execution of the
MCS. Among this last category, there are two fundamental blocks:


  Target sequence: it defines manoeuvres and propagations in terms of the desired goal. What the
control sequence does is run the segments nested within it and apply the profiles to the run
according to its configuration. In this analysis two types of profiles have been used: search (which
defines a goal and changes the selected variables to achieve them) and segment configuration
(which is used to change the configuration of a specified segment inside the target sequence). An
example of a target sequence is shown in Figure 3.6: the target sequence “IPA Rendezvous” uses a
search profile (specifically a differential corrector) that evaluates the necessary value for the control
parameter (in this case thrust during the “IPA Rendezvous Man” manoeuvre) to get the equality
constraint (7 km along InTrack at the end of propagation segment “PropToSR”).


_Figure 3.6: Example of a target sequence_


  Sequence: this structural element organizes the segments nested within and defines the nature of
the results to pass on to the next segment of the MCS. It also allows to set number of times that the
sequence will run.


To define the properties of the spacecraft (e.g.: its mass, drag area) and its initial orbit, the segment Initial
State is used. For Space Rider, the following properties were set:


35


_Chapter 3 - STK Scenario_


  - Dry Mass: 4165 km;

  - At **t** iude fixed with TPS towards nadir direction;

  Propagator: Space Rider motion is assumed to be controlled, therefore only the effect of the
gravitation force is considered (JGM2 model with maximum order and degree equal to 4). The Joint
Gravity Model (JGM) version 2 is a model that describes Earth’s gravity field up to degree and order
70. It was developed by Goddard Space Flight Centre in cooperation with American universities and
private companies [14];


For SROC the following properties were set:


  - Dry mass: 24 km

  Drag coefficient: 2.2

  - Drag area: 0.06 m [2]

  Solar Radiation Pressure coefficient: 1.3

  Solar Radiation Pressure area: 0.06 m [2]

  - Propagator: it uses the following disturbances:

`o` Gravitational Force: JGM2 with maximum degree and order equal to 4.
`o` Lunar Third Body Force
`o` Solar Third Body Force
`o` Drag Model: drag with MSISE 1990 Atmospheric Density Model. It uses fixed values for the

solar flux and geomagnetic effects: Daily F 10.7 = 150, Average F 10.7 =150 and K p =3 (they are
STK’s default values for the model). The solar radio flux F 10.7 is an indicator of the solar
activity which correlates well with the number of sunspots and UV and visible solar
irradiance records. When this activity changes, the thermospheric density changes too, thus
varying the atmospheric drag: the higher the solar activity, the higher the atmospheric drag

[15]. The K p index is used to characterize the magnitude of geomagnetic storms and
disturbances in Earth’s magnetic field; geomagnetic storms can produce large short-term
increases in upper atmosphere temperature and density, increasing drag on satellites and
changing their orbits.

**t**



_Figure 3.7: ESA prediction for the monthly mean F10.7 index [16]_


36


_Chapter 3 - STK Scenario_


Figure 3.7 and Figure 3.8 show the prediction by ESA for the monthly mean F 10.7 index and
the A p index (it is another index comparable to K p but can be easily converted to it using an
online converter [17]). The middle and darker line in both graphs represents the 50
percentile of the prediction and it was used to verify the reliability of STK’s default values.
Using F 10.7 = 150 for both the daily and average values is very consistent with the prediction
by ESA, while the value for the K p is a bit higher than the average predicted by ESA (3
instead of 2.75), however, it was still considered reliable enough.


_Figure 3.8: ESA prediction for the Monthly AP Index [16]_


`o` Spherical Solar Radiation Pressure: it uses the Dual Cone shadow model, which uses the

actual size and distance of the Sun to model regions of full, partial (penumbra), and zero
(umbra) sunlight.


For the drag/solar radiation pressure area of SROC, it was used the area of the +Z surface of a 12U CubeSat,
while for the propagator it was decided to consider more disturbances than Space Rider. The reason behind
this choice is that Space Rider was assumed to be following a controlled orbit, where only the effects of
gravity are considered. These external forces, especially the atmospheric drag, change the orbital
parameters of SROC during the mission and can affect, some in a bigger magnitude than the others, the
required deltaV or duration of each manoeuvre.


3.2.2 Mission Control Sequence


This paragraph describes all the mission segments, in which all the different phases and subphases of the
mission have been divided to compose the following Mission Control Sequence (MCS).


**PreDeployment** : this phase is used to define all the properties of SROC, which have been discussed in the
previous section.


_Figure 3.9: SROC initial trajectory after the deployment_


37


_Chapter 3 - STK Scenario_


**Deployment** : this impulsive manoeuvre was made to simulate the deployment of SROC from Space Rider’s
MPCB; for this reason, since it will not be performed in the real mission, the deltaV accounted for this
manoeuvre will not be considered in the total deltaV evaluation. A previous study defined this manoeuvre
to avoid any possible collision/conjunction with Space Rider:


  - Azimuth: 180 deg

  Elevation: -80 deg

  - Magnitude: 0.5 m/sec


Figure 3.9 and Figure 3.10 show the deployment direction and the initial trajectory of SROC after the
deployment.


_Figure 3.10: SROC deployment overview_


**Commissioning** : this segment is just a propagation one which simulates the free flight during SROC’s
commissioning sub-phase. Its stopping condition is the duration: after 5 days the commissioning ends. At
the end of this mission segment, the final SROC position is:


  - Radial: -10.5 km

  - InTrack: 372.9 km

  - CrossTrack: -0.007 km


What happens during this propagation is that, because of the drag force, SROC decreases its semi-major
axis (Figure 3.12) and increases its relative speed, especially along the InTrack direction (as shown in Figure
3.11, where the InTrack position increases exponentially). This behaviour would be seen also if the effects of
the drag force were considered for Space Rider’s propagator since it has a bigger ballistic coefficient.


38


_Chapter 3 - STK Scenario_


_Figure 3.11: RIC components during the commissioning_


_Figure 3.12: SROC semi-major axis during commissioning_


**HP1** : this target sequence simulates the verification sub-phase. As explained in Sub-section 2.3.1.1, since
the main manoeuvres to be performed in this sub-phase are yet to be decided, this mission segment was
only modelled as a manoeuvre (“Enter HP”) and a propagation segment (“Hold Point)”, with the differential
corrector set to ensure that the semi-major axis of SROC at the end of the sequence will be the same as
Space Rider’s. As it can be seen from Figure 3.13, the segment shown here is not a proper hold point, since
the relative RIC components vary by a few km during it, but it is more a manoeuvre to slow down SROC’s
drift from Space Rider. However, this nomenclature was still kept in order to be coherent with the Mission
Analysis Report [19]. Finally, the duration has been set temporarily set to 4.5 hours, which was the value
used for the previous studies. When the Verification sub-phase will be better defined, it is probable that the
manoeuvres performed for this segment will change, thus changing its duration and deltaV required.


39


_Chapter 3 - STK Scenario_


_Figure 3.13: HP1 Trajectory_


**IPA Rendezvous** : this target sequence simulates the In-Plane Approach rendezvous. Its duration is set to
5.76 days and the InTrack target for the differential corrector is 7 km; these two values are the result of an
optimization, whose main constraint and objectives are described in Section 4.2. This target sequence
comprises an impulsive manoeuvre segment (“IPA Rendezvous Man”) followed by a propagation one
(“PropToSR”). The control parameter for the differential corrector is the thrust along the V axis of SROC’s
VNC coordinate reference system.


_Figure 3.14: SROC InTrack during IPA_


40


_Chapter 3 - STK Scenario_


_Figure 3.15: SROC's relative final motion at the end of the IPA_


**HP2 Insertion** : this target sequence, is again composed of an impulsive manoeuvre segment (“HPInsertion
Man”) and a propagation segment (“PropToHP”); its duration (2 hours) was evaluated using the same
optimization process used for the IPA Rendezvous, while the InTrack Target (2 km) was chosen to get SROC
as close as possible to Space Rider, while also respecting the observation requirements. Figure 3.16 shows
the passage from the last moments of the IPA to the OPA. The desired results of the differential corrector
are all the relative position vectorial components on the RIC axes (0 km along CrossTrack, 2 km along
InTrack and 0 km along Radial) at the end of the propagation segment. The control parameters are the
thrust vectors along all three axes of the VNC reference system.


_Figure 3.16: Last orbits for IPA (red) and the OPA (green)_


**ZeroRelVel2:** the HP2 insertion manoeuvre is completed with this target sequence, which has only an
impulsive manoeuvre and it is set at zero the relative velocity between SROC and Space Rider. By doing so,
at the end of this segment, the satellite has null relative velocity and has a relative position of 2 km along


41


_Chapter 3 - STK Scenario_


the InTrack axis and 0 km for both the Radial and CrossTrack axes. The control parameters are again the
thrust vectors along all three axes of the VNC reference system.


**HP2 Sequence** : this segment was not part of the first version of the code but was added during the
development of this thesis to provide an HP2 more similar to the actual manoeuvre, where the position is
continuously controlled to guarantee an almost constant relative position with respect to the target. The
manoeuvre was set to last 4.5 hours. The details about how it works and how it has been defined are
reported in Section 4.3. The sequence is divided into nested sequences and each of them is composed by
the following segments:


  HP2 target sequence: it targets the desired relative position, and it is in turn composed of a finite
manoeuvre and a propagation segment;

  ZeroRelVel target sequence: it sets to zero the relative velocity of SROC;

  Propagation segment: SROC freely propagates until its relative position exceeds the maximum error
on the relative position.


**Inspection** : this is another sequence composed of the following segments:


  - OPA Rendezvous: it is a target sequence that simulates the Out-Of-Plane Rendezvous from the HP2
to the insertion to the WSE. It contains one impulsive manoeuvre segment (called “PositionMan”)
and one propagation segment (called “PropToWSE”). The differential corrector is set to reach the
following position:

`o` Radial: 0.216 km

`o` InTrack: -0.047 km

`o` CrossTrack: -0.129 km
This is the starting point for the WSE, and it is evaluated using a Matlab function described in
Section 5.3. Figure 3.17 and Figure 3.18 show SROC’s relative trajectory respectively on the InTrackRadial and CrossTrack-Radial planes.


_Figure 3.17: SROC's trajectory during the OPA – InTrack-Radial plane view_


42


_Chapter 3 - STK Scenario_


_Figure 3.18: SROC's trajectory during the OPA – CrossTrack-Radial plane view_


  WSE Insertion: this target sequence is only composed of an impulsive manoeuvre, called
“VelocityMan”. The target profile sets the desired values for InTrack, Radial and CrossTrack rates,
defined by the same Matlab function used to define the WSE insertion point.

  Inspection: this segment is just a propagation one lasting 8 hours. It simulates the observation
phase as one uncontrolled propagation. The impulsive manoeuvre boosts the WSE along negative
InTrack, then, because of the effect of the drag force, the WSE starts moving along positive InTrack.
By doing so the duration of the observation phase increases. Figure 3.19 shows SROC’s relative
trajectory during the Inspection.


Although the nominal scenario considers only one observation cycle, by considering all these mission
segments inside a single sequence, it is easier to add more inspection by simply copying and pasting the
external one.


_Figure 3.19: Last part of the OPA rendezvous (green) and WSE (blue)_


43


_Chapter 3 - STK Scenario_


**Free Flight** : this propagation segment represents the free flight after the inspection, during which the
satellite sends to the Ground the mission data. It presents two stopping conditions and only one of them is
required to stop the propagation: either the duration exceeds 16 hours (which should be more than enough
to downlink the data) or the relative range exceed 2 km. In the nominal case, the condition which actually
stops the propagation is the second one, thus causing the duration to last 8.06 hr. Figure 3.20 shows,
besides the position and speed in the RIC reference frame, that the range at the end of the free flight is 1.99
km. This segment and the WSE could be represented by only one propagation segment since there are no
manoeuvres between them. The division between these two is the result of a trade-off between how much
time after the WSE insertion can be deputed to the observation and how much is required to send data to
the Ground. For the Observe scenario, this is the last segment considered, while for the Observe&Retrieve,
the free flight is followed by the HP3 insertion.


_Figure 3.20: Last relative orbits of the free flight propagation_


**HP3 Insertion** : this target sequence has the same structure as the one used for the HP2 insertion; it is
composed of an impulsive manoeuvre segment (“HPInsertion Man”) and a propagation segment
(“PropToHP”); its duration (2.7 hours) was evaluated using the same optimization process used for the IPA
Rendezvous, while the InTrack Target (0.2 km) was chosen to get SROC just at the limit of Space Rider’s KOZ.
The desired results of the differential corrector are all the relative position vectorial components on the RIC
axes (0 km along CrossTrack, 0.2 km along InTrack and 0 km along Radial) at the end of the propagation
segment. The control parameters are the thrust vectors along all three axes of the VNC reference system.
Figure 3.21 shows SROC’s relative trajectory during this segment, while Figure 3.22 highlights that the final
position is at the perimeter of the KOZ.


44


_Chapter 3 - STK Scenario_


_Figure 3.21: SROC's reltavi trajectory during the HP3 insertion_


_Figure 3.22: SROC's final relative position at the end of the HP3 insertion_


**ZeroRelVel3** : this target sequence, its segments, its control parameters, and its desired results are the same

as for ZeroRel2.


**HP3 Sequence** : this sequence is similar to the HP2 sequence, with the only difference being the desired
relative position, which is now 0 km along CrossTrack, 0.2 km along InTrack and 0 km along Radial.


45


## _4 ons_ _Updated Matlab Funct i_

The Matlab functions are a crucial part of the analysis process performed for this study. They work as an
interface between the user and the STK, automating actions that would be tedious and repetitive to
perform and which would greatly increase the analysis time. The main tasks of these functions usually are:


  Setting the mission segments (e.g.: defining the duration and the stopping condition of a
propagation segment, the target results and the control parameters of the differential corrector);

  - Manage the MCS, by adding or removing segments;

  - Run the STK scenario;

  Post-process the data from STK (e.g.: defining the optimal manoeuvre or producing plots);


The Matlab code has been organized in the following way: a main function sets the interface with STK and
the scenario, then calls specific functions to define or analyse each mission segment. This software
structure was already defined before starting this thesis, however, before actually using or expanding it, it
was reorganized and updated. This process was necessary since until phase B1 several mains and functions
were produced to analyse mission segments or scenarios which are now discarded or significantly different.
Since describing exactly every minor change would be unnecessarily long and not particularly important to
understand the scope of this thesis, the main features of this first task work can be summarized as follows:


  When there was one or more variation of the same function, they were condensed into a single
function; of course, keeping only the useful features;

  Small errors were identified and corrected;

  - All the variables’ names were updated to be consistent with the nomenclature used in the Mission
Analysis Report [19]; this change was also applied to the JSON files and the STK scenario;


The only major changes which will be further discussed are:


  Improvement of the performances of both the IPA optimization (Section 4.2) and HP definition
(Section 4.3) functions;

  Addition of several flags to avoid entering the KOZ during the Observation Phase (Section 5.3)

##### 4.1 Analysis Process Overview


Figure 4.1 illustrates the workflow which was followed every time an analysis was performed:


  The Matlab function is started;

  The Matlab function retrieves all the information required to set the STK scenario, which usually are
the properties of each mission segment, such as its duration, the propagator used during the
propagation phase or the desired target for a target sequence. These data are saved in different
JSON files;

  Using the STK object model [8][9] the Matlab function connects to STK scenario and sets the
Astrogator propagator for SROC;

  The STK scenario performs the orbital propagation and evaluates the thrust magnitude and
orientation required to get the desired result(s) for the target sequences;

  The STK object model is used by the Matlab function to retrieve the output of the STK simulation, to
produce tables and graphs. If its relative control flag is true, STK can also overwrite each of the JSON
files according to the results of the analysis;


46


_Chapter 4 - Updated Matlab Functonsi_

_i_

##### i i



_Figure 4.1: Analysis Process Overview_


The STK Object model is an object-oriented interface to STK, built on Microsoft Component Object Model
(COM) technology and, among the different environments to which is compatible, it can be used in Matlab.
This Object model is a collection of different COM libraries containing type, interface, events, and classes
representing the many aspects of the STK application structure; for this thesis, it was mostly used the STK
Astrogator COM library, since the purpose of the Matlab function is to model and analyse the MCS in
Astrogator.

##### 4.2 IPA Opt i mizat i on


The definition of the optimal IPA manoeuvre is one of the most complex and long analyses performed by
the Matlab and STK functions. First, it is important to define what makes an IPA the optimal one: the
minimization of the total deltaV cost required to perform the IPA, the HP2 insertion, and the zeroing of the
relative velocity (called ZeroRelVel2 in the MCS). The reason why these three deltaVs are considered
together is that the constraints imposed on the IPA, which are the target position and the duration of the
segment itself, determine both the final relative position and velocity of SROC, thus also affecting the
successive mission segments. The effect on the mission segments after the HP2 is considered negligible
since the HP2 always starts at a specific relative position (0 km Radial, 2 km InTrack and 0 km CrossTrack)
and relative velocity (null).


47


_Chapter 4 - Updated Matlab Functonsi_

_i_



_Figure 4.2: Diagram showing the functioning of the IPA optimization_


Before the update, the IPA optimization function evaluated only the deltaV of the IPA itself and the HP2
insertion; now it also evaluates the effect on the ZeroRelVel2 manoeuvre. Moreover, the function used to
evaluate the optimal IPA more times than necessary, thus increasing the run time.


Figure 4.2 shows how the updated version of the function works. The possible IPA manoeuvres are
evaluated by considering every combination between the elements of a vector composed of target InTrack
values with the elements of a vector composed of IPA duration values (External Loop). For each
combination, the STK scenario is run, and its results are analysed to determine if the solution is valid, which
means that the IPA must fulfil the following constraints:


  The IPA final InTrack position obtained in STK must not differ by more than 0.5 km from the desired
final InTrack position;

  SROC must not cross below 200 m along the InTrack axis during a 24-hour propagation after the IPA
completion. The Matlab interface with STK is used to add a 24-hour propagation segment, then, at
the end of the optimal IPA definition, this segment is eliminated since it does not really occur in the


48


_Chapter 4 - Updated Matlab Functonsi_


mission ConOps. This condition was added to assess the safety of this manoeuvre in case an offnominal condition prevented SROC to perform the successive manoeuvres for 24 hours; this period
of time was chosen to simulate the time required to assess the occurrence of a fault and to make SR
perform a Collision Avoidance Manoeuvre from SROC. Figure 4.3 shows that the 24-hour
propagation (in green) after the IPA (in red) does not cause SROC to decrease its InTrack distance
below 200 m. In fact, the minimum InTrack distance is approximately 5 km away from Space Rider.
At the beginning of the propagation, SROC is moving at a low speed and it is progressively slowed
down by the atmospheric drag until its relative speed changes its direction from toward SR to the
opposite direction. This means that even if this propagation lasted more, it would not change the
minimum relative distance, but it would only cause SROC to move away even more from SR, thus
making an SR collision avoidance manoeuvre useless.

_i_



_Figure 4.3: trajectory during the 24 hours propagation (green) after the IPA (red)_


If the IPA iteration is valid, the Inner Loop is started: all the possible HP2 insertions are evaluated iterating
on the duration of the propagation segment during the insertion. The final position is fixed at 0 km along
CrossTrack, 2 km along InTrack and 0 km along Radial. An HP2 insertion is considered valid if:


  The IPA final InTrack position obtained in STK must not differ by more than 0.5 km from the desired
final InTrack position;

  SROC must not cross below 200 m along the InTrack axis during the propagation to the insertion
point. This constraint was set for safety purposes to avoid SROC from passing through the KOZ or
flying “behind”, that is in the negative InTrack, SR. Figure 4.4 shows an example of a not-valid HP2
insertion manoeuvre: although the final position is the one desired, SROC reaches it by passing
behind SR;


49


_Chapter 4 - Updated Matlab Functonsi_

_i_



_Figure 4.4: Final position of a not valid HP2 insertion_


When an HP2 insertion is valid, the successive ZeroRelVel manoeuvre is evaluated and its deltaV cost is
saved. After iterating on all the possible HP2 insertions and simulating their relative ZeroRelVel manoeuvres,
the optimal insertion, in terms of minimum total deltaV for both the insertion and the ZeroRelVel
manoeuvre, is evaluated. It is noted that this is not the absolute optimal result, but only the optimal result
for a specific IPA. When the External Loop finishes, which means all the possible IPAs have been evaluated,
the optimal IPA + HP2 insertion + ZeroRelVel manoeuvre is determined. Finally, the selected sequence is set
on STK, and the scenario is run to save these changes.


Table 2.1 shows the improvement in the total deltaV cost with respect to the previous version of the code.
While the cost for the IPA is almost the same, the updated version of the code sets an insertion that
requires a higher deltaV but guarantees a lower deltaV for the ZeroRelVel manoeuvre. The previous version
of the code, instead, includes a much less deltaV-consuming insertion, but a much higher ZeroRelVel
manoeuvre. This is because it considers only the insertion in the optimization process, so it sets the less
deltaV-consuming inspection, with no regard for the cost of the successive manoeuvre.


_Table 4.1: deltaV budget for IPA + HP2 insertion + ZeroRelVel2_

|Mission segment|Previous Code|Updated Code|
|---|---|---|
|**IPA Rendezvous deltaV [m/s]**|0.486|0.485|
|**HP2 Inserton deltaV [m/s]**|0.188|1.280|
|**ZeroRelVel#2 deltaV [m/s]**|1.877|0.423|
|**Total Sequence deltaV [m/s]**|2.551|2.188|



Figure 4.5 shows the evolution of the RIC rate during the last hours of the IPA and the whole HP2 insertion.
As shown in the lower image, the relative velocity of SROC is almost null for every RIC component: the
kinetic energy variation required to nullify the relative speed is very low, thus demanding a low deltaV
impulse during the ZeroRelVel manoeuvre.


50


_Chapter 4 - Updated Matlab Functonsi_

_i_



S

_i_



_Figure 4.5: RIC Rate at the end of the IPA and during the HP2 insertion (up); zoom on the RIC rate after the ZRV2 manoeuvre (down)_


Figure 4.6 shows that in case any faults prevented the execution of the ZeroRelVel manoeuvre, SROC would
not enter SR KOZ; the minimum range, in this case, would be 1.119 km.

_i_



_Figure 4.6:Trajectory of a propagation segment (red) after the nominal HP2 insertion (green)_


The discussion so far focused on the analysis process performed by the Matlab code but not on which
functions were used and how they communicate between them. Figure 4.7 schematizes the features of
these functions and how they interact: each coloured blocks represent a Matlab function, whose name is
placed on the top of the block itself. The functions have also been divided between analysis functions,
which actually interface with STK, and utility functions, which process the data obtained from them.


51


_Chapter 4 - Updated Matlab Functonsi_

_i_



_Figure 4.7: Matlab functions flowchart_

##### 4.3 HP Sequence


The Hold Points 2 and 3 were defined using a new Matlab function, called “HoldPointTrue_Sequence”. This
update was made to add the following features to the HP segment and the analysis function:


  Set a minimum and maximum relative distance during the HP

  Model the HP as a sequence of multiple finite burns, instead of a single one


By doing so it will be possible to change the main properties of the segment if or when more precise
constraints will be available. Moreover, this modelling of the HP better reflects what the real segment could
be, thus giving a more faithful estimate of the deltaV which is crucial to the scope of this thesis.


Figure 4.8 shows the segments composing the HP sequence:


  **First Propagation** : this propagation segment takes place after the Hold Point insertion and the
ZeroRelVel manoeuvre. Initially, the satellite is exactly at the desired Hold Point relative position (0
km along CrossTrack, 2 km along InTrack and 0 km along Radial) with an almost null relative velocity,
but because of the effect of the external disturbances it starts accelerating and moves from the
desired position. SROC keeps drifting until it reaches either the maximum or the minimum
acceptable range.

  - **HP Burn #n** : this sequence is composed of three sub-segments:

`o` **HP target sequence** : the desired result of its differential corrector is the final relative

position (0 km along CrossTrack, 2 km along InTrack and 0 km along Radial) and the control
parameter is the thrust along all the 3 VNC axes of SROC and the duration of the
propagation segment (“To Target”). It is composed of a finite manoeuvre segment and a
propagation segment. The target sequence uses three different profiles: the first one is a
differential corrector targeting the aforementioned results considering an impulsive
manoeuvre. Then, a second profile, called “Change Maneuver Type” changes the
manoeuvre from impulsive to finite. The third profile is a differential corrector targeting the
same results but considering a finite manoeuvre. The reason why three profiles were used


52


_Chapter 4 - Updated Matlab Functonsi_


is that a differential corrector targeting a finite manoeuvre usually requires a representative
guess for the thrust vectors: by first running the target sequence with an impulsive
manoeuvre, its results can be used as the first guess values. Another peculiarity of this
target sequence is that the duration of the propagation segment, called “To Target”, after
the manoeuvre is not known in advance: this is why “To Target” ’s duration is one of the
control parameters of the differential corrector. However, to converge on a solution, it is
required to start with an accurate first guess of the actual final values. For this reason, the
Matlab function iterates on a vector of possible durations (from longest to shortest) and
selects the first one which enables the profiles to converge.
`o` **ZeroRelVel** : this target sequence is identical to the ZeroRelVel segment described in Sub
section 3.2.2: its desired result are null relative velocities along all the RIC axes and the
control parameters are the thrust vectors along the three SROC’s VNC axes.
`o` **free flight:** this propagation segment is similar to the First Propagation one: because of the

external disturbances SROC starts drifting from the desired position until either the rangestopping conditions are met or the Hold Point duration is reached.


The HP Sequence can be composed of a different number of HP Burn segments, depending on the total
duration of the HP. If the free flight stops because of the range constraints and the HP is not over, the
Matlab function adds another HP Burn sequence. Its target sequences are reset and recalculated, as well as
the duration of the “To Target” propagation segment. This process is repeated until the HP lasts for the
desired duration. Since the desired HP duration may vary between different analyses, before performing
any action on the whole sequence, the Matlab function erases all the HP Burn sequences except for the first
one, thus avoiding scenarios where the HP sequence at the beginning of the analysis is already longer than

the desired HP.

_i_



_Figure 4.8: HP sequence segments_


Figure 4.9 show the variation of the range during HP2 (left) and HP3 (right). For the first one, the maximum
range error is 11 m, while for the second one is 13 m. These maximum errors show the improvement from
the outdated version of the code which had a maximum error of 20 m. Figure 4.10 shows SROC’s trajectory
in RIC components for HP2 and HP3. Generally, during HP2 SROC tends to oscillate both between a higher
and lower InTrack with respect to the desired position, while during HP3 it mostly moves to higher InTrack
values. For both HPs, the displacement along the CrossTrack axis is almost negligible. This is probably due to
the fact that the biggest disturbance, that is the atmospheric drag, mostly acts on the InTrack and Radial


53


_Chapter 4 - Updated Matlab Functonsi_


positions: by decreasing the spacecraft speed, it changes its semimajor axis, thus varying the InTrack and
Radial coordinates.

_i_


_i_



_Figure 4.9: SROC Range as function of the time from the beginning of the HP; HP2 is on the left and HP3 on the right_

_i_


_i_



_Figure 4.10: SROC trajectory as function of the time from the beginning of the HP; HP2 is on the left and HP3 on the right_


Table 4.2 and Table 4.3 list the duration and the deltaV cost of every segment of respectively HP2 and HP3.
Especially for HP2, the deltaV cost of the manoeuvres and the duration of the successive propagation
segments noticeably vary between the different burns. The different behaviour between the two HPs may
be due to the fact that the ZeroRelVel manoeuvres, although highly reducing the relative speed, still leave
SROC with a small relative velocity with respect to SR., which then influences the successive propagation
segments. Moreover, a more stable behaviour could be achieved by integrating the actual Simulink model
of SROC’s propulsion system and GNC algorithms with STK, or at least by mimicking its behaviour with a
simpler closed-loop controller. In conclusion, the quality and results of this analysis were still considered
more than adequate to evaluate the deltaV required to perform the manoeuvre; in fact, the relative
position achieved at the end of both HPs has a relative range error of less than 0.1% and, as seen, before,
the maximum absolute range error during the HPs is 13 m for HP3.


54


_Chapter 4 - Updated Matlab Functonsi_


_Table 4.2: deltaV and duration of all the HP2 segments_

|Segment|Col2|deltaV [m/s]|Duration [sec]|
|---|---|---|---|
|First Propagaton|First Propagaton|-|2908|
|Burn1|HP Man|3.464·10-3|1.960|
|Burn1|To Target|-|3756|
|Burn1|ZeroRelVel|5.952·10-3|-|
|Burn1|free fight|-|1493|
|Burn2|HP_Man|41.05·10-3|23.22|
|Burn2|To Target|-|544.2|
|Burn2|ZeroRelVel|24.12·10-3|-|
|Burn2|free fight|-|3499|
|Burn3|HP_Man|11.63·10-3|6.577|
|Burn3|To Target|-|1722|
|Burn3|ZeroRelVel|9.820·10-3|-|
|Burn3|free fight|-|2246|
|**Total**<br>**0.096**<br>**16200**|**Total**<br>**0.096**<br>**16200**|**Total**<br>**0.096**<br>**16200**|**Total**<br>**0.096**<br>**16200**|



_Table 4.3: deltaV and duration of all the HP2 segments_

|Segment|Col2|deltaV [m/s]|Duration [sec]|
|---|---|---|---|
|First Propagaton|First Propagaton|-|3615|
|Burn1|HP Man|13.22·10-3|7.476|
|Burn1|To Target|-|1681|
|Burn1|ZeroRelVel|12.02·10-3|-|
|Burn1|free fight|-|3999|
|Burn2|HP_Man|12.90·10-3|7.299|
|Burn2|To Target|-|1812|
|Burn2|ZeroRelVel|10.87·10-3|-|
|Burn2|free fight|-|3583|
|Burn3|HP_Man|26.61·10-3|15.05|
|Burn3|To Target|-|818.8|
|Burn3|ZeroRelVel|17.91·10-3|-|
|Burn3|free fight|-|661.4|
|**Total**<br>**0.094**<br>**16200**|**Total**<br>**0.094**<br>**16200**|**Total**<br>**0.094**<br>**16200**|**Total**<br>**0.094**<br>**16200**|



55


## _5 Nominal Scenarios Analysis_

In the previous Chapter, the updates to the Matlab and the STK scenario were described. After performing
these modifications and enhancements, a few aspects of the Nominal Scenario were re-defined. The fact
that SR’s orbit changed between Phase B1 and Phase B2, made it necessary to perform the following tasks:


  Evaluate the Ground Stations (GS) visibility during the mission;

  Evaluate the illumination conditions and the GS coverage for the Final Approach;

  Define the optimal WSE;

  Estimate the required deltaV and duration of the whole mission;

##### 5.1 Ground Stat i on Visibility Analysis


The analysis of the ground stations has been carried out considering the following assumptions:


  The ground station network in the simulation is composed of ESTRACK stations, a set of commercial
stations including some run by Tyvak and the PoliTo CubeSat Control Centre (C3). The complete list
of the ground stations used is presented in Table 5.2;

  It is required a minimum elevation angle of 10 degrees;

  AzElMask was applied for all ground stations: this mask evaluates the terrain-based visibility
restrictions by extending constant azimuth arrays outwards the point indicated. With this process,
obstruction information is evaluated, and it is used to account for obscuration of the line of sight
when computing the access;

  A minimum access duration of 3 minutes was set to consider the margin of time needed for tracking
the signal and establishing a stable link with SROC;

  - This simulation was carried out considering a 1-month long scenario, from the 1 [st] of November
2024 to the 1 [st] of December 2024;


The analysis was carried out considering the MCS of the nominal scenario; since it ends on the 13 [th] of
November, from that moment onward the state of the satellite was blocked using the Hold segment. This
segment blocks the satellite in the same relative position with respect to SR it has at the end of its previous
segment (in that case the HP3) until the end of the analysis. Table 5.1 reports the number of access for the
whole month, the daily number of access, the average and maximum duration and the number of access
lasting more than 5 minutes for all the ground stations covered by SROC.


_Table 5.1: Ground Station visibility analysis_


##### i


##### i


##### i


##### i


##### i


##### i

|Location|Access<br>[#/month]|Access >5<br>minutes<br>[#/month]|Access<br>[#/day]|Maximum<br>Duration<br>[min]|Average<br>Duration<br>[min]|
|---|---|---|---|---|---|
|Kourou_Staton|363|277|12|6.624|5.693|
|Malindi_staton_STDN_KENS|438|339|14|6.638|5.778|
|South_suwalesi_LAPAN|438|236|14|5.888|4.833|
|SriLanka_Leasfpace|308|234|10|6.611|5.651|



56


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Table 5.2: Ground Stations list_







|Location|ESTRACK|OWNER|FREQUENCY|
|---|---|---|---|
|Turin|No|Polito|S, UHF|
|AbuDhabi_Tyvak|No|Tyvak|S|
|Awaruna_LeafSpace|No|Leafspace|S, UHF|
|Bardufoss_Tyvak|No|Tyvak|UHF|
|Cebreros_DSA_2|Yes|ESA|Ka, K, X|
|Dongara_Station_AUWA01_STDN_USPS|No|Universal Space<br>Network|S, Ku, X, Ku|
|DSS_26_Goldstone_STDN_D26D|No|NASA||
|Esrange_Station_ESTC_STDN_KU2S|No|SSC|S, X (UHF<br>downlink)|
|Esrange_Station_SSC-CNES|No|SSC|S, X, (UHF<br>downlink)|
|ESRIN|No|ESA||
|Kerguelen_Island_STDN_KGLQ||||
|Kourou_Station|Yes|ESA||
|Malargue_DSA_3|Yes|ESA|Ka, K, X|
|Malindi_Station_STDN_KENS|Yes|ESA|X|
|Masuda_USB_F2||||
|New_Norcia_DSA_1|Yes|ESA|S, X|
|Orbcomm_Hartebeesthoek_A|No|SANSA|S, C, Ext C, X, Ku,<br>DBS, Ka|
|Petaluma_Tyvak|No|Tyvak|S|
|Peterborough_Tyvak|No|Tyvak|S|
|Poker_Flat_Station_PF1_STDN_DX2S|No|NASA|S, C|
|Redu_Station|Yes|ESA|L, X X Ku, Ka|
|RiodeJaneiro_Telespazio|No|Telespazio|L, S, C, Ku, Ka|
|SanDiego_Tyvak|No|Tyvak|UHF|
|Santa_Maria_Station|Yes|ESA/leafspace|S,X|
|Santiago_Leolut|No|Ssc|S, C, Ka|
|Shetland_Islands_LeafSpace|No|Leafspace|S, X, UHF|
|South_Point_Station_USHI01_STDN_USHS|No|Ssc|S, X, Ku|
|south_sulawesi__LAPAN|No|lapan|S|
|SriLanka_LeafSpace|No|Leafspace|S,X|
|Svalbard_STDN_S22S|No|Kongsberg Satellite<br>Services|C, L,S,X and|
|TrollSat_Ground_Station|No|Kongsberg Satellite<br>Services|S, X, C (uplink)|
|Usuda|No|JAXA|S, X|
|Villafranca_VIL-4|No|ESA|S, C|
|SMILE Lab|Yes|ESA|S, UHF|


57


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


The new baseline orbit presents a total number of access and average durations slightly better than the
baseline orbit of phase B1, however, as shown in Figure 5.1, most of the time SROC cannot communicate
with the Ground and the visibility interval with the longest duration is only 6.638 minutes.


_Figure 5.1: GS take over_


_Figure 5.2: GS take over with an additional ground station_


This global coverage could not be adequate for the mission since it may not have communication windows
long enough. This property is not particularly crucial for the downlink of mission data during the free flight,
but it could be fundamental during the commissioning or the final approach, where a combination of
proper illumination conditions and ground station coverage is required (see Section 5.2 for more
information). The duration of the longest access window could be increased by considering more already
existing ground stations or by creating ad-hoc ground stations. Figure 5.2 shows the GS coverage if another
ground station (LAPAN’s Rumpin Ground Station) is added. By doing so, the longest access changes from
6.611 minutes to 10.309 minutes thanks to the uninterrupted passage from the additional ground station to


58


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


the south_sulawesi_LAPAN ground station. However, the possibility to create a significantly longer
uninterrupted coverage window could not be feasible, since a considerable portion of SROC’s ground track
is above the sea and not land. Moreover, considering or even building new ground stations would increase
the cost and the complexity of the project.


An alternative solution could be to use a GEO satellite constellation to perform data relay of SROC’s data to
the Ground. In this scenario, SROC would need a transponder that uses the GEO satellites connectivity;
there are already TRL9 COTS available for this application, such as AddValue’s IDRS system [33], which relies
on Inmarsat GEO satellites. Its mass (1 kg) and volume (125x96x70 mm [3] ) are compatible with SROC’s
remaining mass and volume margins [20]. The real-time connection provided by this service presents the
following properties:


  - Network availability higher than 99.5%;


  - Link budget availability higher than 99%;


  IP session continuity during rapid GEO satellite spot beam handovers;


  - Latency: 0.5 – 1.5 seconds end to end;


  Capability of supporting data rates in excess of 200 Kbps for SROC’s orbit;


_Figure 5.3: INMARSAT -4 GEO constellation_


Figure 5.3 shows the INMARSAT-4 GEO constellation that is the one used by IDRS. A 1-month access analysis
between SROC and the constellation was performed and showed that the satellite is always in line of sight
with at least one element of the constellation. In conclusion, is this solution was confirmed to be feasible
also from other points of view such as the cost, it would be the best way to guarantee an uninterrupted
communication window with SROC.

##### 5.2 Final Approach Analysis


Although the Final Approach and Docking are not evaluated in the STK scenario, the conditions to ensure
their successful outcome have been evaluated in SKT. As stated by the requirement SROC-MIS-111: “The
angle between the Sun Vector and the docking axis shall be less than 60 (TBC) deg for the final approach
and docking”. This angle, also called Line of Sight (LOS) angle in STK, was evaluated from the end of the HP3
to the end of the analysis time (1st Dec 2024). Figure 5.4 shows the LOS as a function of the time for the
first 24 hours after the end of HP3 while Figure 5.5 zooms on one of the many suitable illumination intervals
when the LOS constrain is respected; specifically, the interval in the image lasts 35 minutes.


59


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.4: LOS angle during the first 24 after the HP3 end_


_Figure 5.5: Zoom on one acceptable interval_


The evolution of the LOS angle for the next 29 days is the same as the one reported in Figure 5.4, so from
the end of the HP3 onwards, there are many windows with an acceptable illumination (approximately 15
per day). The next crucial step is to synchronize the start of the Final Approach with a good illumination and
ground station visibility window. Figure 5.6 shows, from top to bottom: the single ground stations visible
from SROC, all the intervals when at least one of them is visible (the brown line referred to as “SROC”), the
intervals with good illumination, and the windows with both good illumination and GS visibility. If the
windows shorter than 3 minutes are discarded from this last set of intervals, the following results are

obtained:


  Min Duration: 201.7 seconds;

  Max Duration: 398.3 seconds;

  Mean Duration: 310 seconds;

  - Number of Intervals: 13;


In conclusion, the 35 minutes window is reduced to an approximately 6.6-minutes window.


60


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.6: Illumination and GS visibility analysis_


Of course, in case the data relay using GEO satellites was considered instead of the direct communication
with the ground station, the suitable intervals to perform the Final Approach would coincide with the ones
with an acceptable LOS angle, since it would always be possible to communicate with SROC through a GEO
satellites constellation.

##### 5.3 WSE Design of Experiment


As mentioned before, during the observation phase SROC will perform observation of SR in its proximity.
During this subphase, SROC will fly in a passively safe trajectory called Walking Safety Ellipse (WSE), whose
geometry depends on the insertion’s relative position and velocity. A Matlab function evaluates these
parameters to generate a WSE which satisfies a set of user-defined constraints. Once the WSE insertion
position has been defined, it is possible to set the OPA target sequence to get there from the HP2, while the
desired insertion velocity becomes the desired result of the WSE insertion target sequence.


5.3.1 Ideal Safety Ellipse


Before showing the results of the WSE DoE, the geometry of the ideal Safety Ellipse is described, to give
some context behind the set of constraints used by the Matlab function to define the WSE. A Safety Ellipse
is an out-of-plane elliptical period relative trajectory around the target spacecraft such that the chaser
(SROC) never crosses the primary spacecraft (SR) velocity vector. Since the drift of the two spacecraft would
not result in a collision, the trajectory is considered passively safe. Figure 5.7 shows several geometrical
features of the Safety Ellipse:


  - The 𝑋 𝐸 and 𝑌 𝐸 axes lay on the Safety Ellipse Plane. The first axis is parallel to the major axis of the
ellipse and points towards negative CrossTrack; 𝑌 𝐸 is perpendicular to 𝑋 𝐸 and it points toward the
positive Radial direction. SR’s centre coincides with the centre of the ellipse;

  - 𝜒 (polar angle) is the angle between SROC distance from the ellipse’s origin and the 𝑋 𝐸 axis; it is
equal to zero at the insertion with the 𝑌 𝑅𝐼𝐶 𝑍 𝑅𝐼𝐶 plane and it is positive counter-clockwise.

  - 𝑎 𝑆𝐸 and 𝑏 𝑆𝐸 are respectively the semi-major and semi-minor axes of the ellipse;


61


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.7: Safety Ellipse Plane_


It is possible to describe SROC’s position in the Safety Ellipse reference frame as a function of the polar
angle:




[



𝑎 𝑆𝐸 cos(𝜒)
𝑏 𝑆𝐸 cos(𝜒)



0



]



_Figure 5.8: View perpendicular to the Safety Ellipse_


Figure 5.8 shows another fundamental geometrical parameter: the inclination angle 𝜃 between the ellipse
plane and the 𝑋 𝑅𝐼𝐶 𝑌 𝑅𝐼𝐶 plane. Moreover, it also shows the maximum radial distance ( 𝑧 𝑚𝑎𝑥 ) and the
maximum CrossTrack distance ( 2𝑥 𝑚𝑎𝑥 ). These two values can be evaluated using the following equations:


2𝑥 𝑚𝑎𝑥 = 𝑎 𝑆𝐸 ∙cos(𝜃)

𝑧 𝑚𝑎𝑥 = 𝑎 𝑆𝐸 ∙sin(𝜃)


62


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.9: Walking Safety Ellipse offset_


This safety ellipse, however, does not correspond to the actual trajectory of SROC: since the satellite
undergoes the effects of the external disturbances and it does not perform any manoeuvre after the WSE to
contrast them, its trajectory is modified. The most evident effect is the motion along the positive InTrack
axis due to the atmospheric drag. For this reason, it is obtained a Walking Safety Ellipse (where “walking”
refers to the translation along the InTrack axis), which is characterized by the InTrack offset Δ𝑦 𝑐 . This
parameter is the distance between the crossing nodes of two ellipses which are the points of the ellipse
with a null CrossTrack (Figure 5.9). The two reference ellipses that define Δ𝑦 𝑐 are the most positive one
(which is the one with the SE centre with the highest InTrack value) and the most negative one (which is the
one with the SE centre with the lowest InTrack value).


_Figure 5.10: Walking Safety Ellipse geometry_


Figure 5.10 shows the relationship between the safety ellipse offset Δ𝑦 𝑐 and 𝑅, which is the maximum range
between SROC and SR. These two parameters are related by the following equation:

𝑅= [Δ𝑦] [𝑐]

2 [+ 2𝑥] [𝑚𝑎𝑥]


63


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


The equations used to approximate in the RIC reference frame the SROC motion along the WSE are shown
below:

𝑥(𝜒) = 𝑥 𝑚𝑎𝑥 𝑠𝑖𝑛(𝜒) − [2𝑦̇] 3𝑛 [𝑐]



𝑦(𝜒) = 2𝑥 𝑚𝑎𝑥 𝑐𝑜𝑠(𝜒) +



𝑦̇ 𝑐 (𝜒− [𝜋] 2



+ 𝑦 𝑐
𝑛




[𝜋]

2 [)]



𝑧(𝜒) = 𝑧 𝑚𝑎𝑥 𝑐𝑜𝑠(𝜒)
𝑥̇(𝜒) = 𝑥 𝑚𝑎𝑥 𝑛𝑐𝑜𝑠(𝜒)
𝑦̇(𝜒) = −2𝑥 𝑚𝑎𝑥 𝑛𝑠𝑖𝑛(𝜒) −𝑦̇ 𝑐

𝑧̇(𝜒) = −𝑧 𝑚𝑎𝑥 𝑛𝑠𝑖𝑛(𝜒)


Where 𝑛 is the mean motion of the primary spacecraft. These equations show that SROC motion depends
on 𝑥 𝑚𝑎𝑥, 𝑧 𝑚𝑎𝑥, 𝜒 and two additional parameters:


  - 𝑦 𝑐 : it is the InTrack distance of the crossing nodes of the initial SE;

  - 𝑦̇ 𝑐 : it is the initial velocity of the SE along the InTrack direction;


The final parameter on which the WSE depends is the desired duration of the inspection. The way that the
Matlab function defines the WSE is the following:


  - 𝑥 𝑚𝑎𝑥 and 𝑧 𝑚𝑎𝑥 are defined by the user; they must be an adequate compromise between the
maximum payload range and the constraint to not enter SR’s KOZ;

  - The duration of the inspection and Δ𝑦 𝑐 are also user-defined;

  - 𝑦 𝑐 and 𝑦̇ 𝑐 are evaluated by the Matlab function through an iterative process until a valid WSE is
founded. To be considered valid, a WSE must respect the following constraints:



Δ𝑦 𝑐



`o` 𝑦 𝑐,𝑚𝑎𝑥 <



Δ𝑦 𝑐



𝑐

2 [ and ] [𝑦] [𝑐,𝑚𝑖𝑛] [> −]



`o` 𝑦 𝑐,𝑚𝑎𝑥 2 [𝑦] [𝑐,𝑚𝑖𝑛] 2 [; ]

`o` SROC trajectory never enters the KOZ during the OPA rendezvous, the observation and the



free flight;

  - Once 𝑦 𝑐 and 𝑦̇ 𝑐 have been calculated, it is possible to define the insertion point of the WSE: this
position is set as the desired result of the OPA Rendezvous target sequence. The desired velocity in
RIC components is also evaluated and set as the desired result for the WSE Insertion target

sequence;


All the above demonstration is just an approximation for the design of a WSE useful for the SR observation,
but it was necessary due to the high complexity of the motion and the disturbances. Further studies and
improvements shall be implemented to increase accuracy and evaluate the effects of the disturbances on
the WSE. This could be done by analytically evaluating the acceleration caused by the disturbances and
therefore calculating the actual trajectory of SROC during the motion. Another option may be using STK’s
pre-built proximity operations manoeuvres. The analysis presented in the next sub-section was still useful to
define a reasonable deltaV guess for both the OPA and the WSE Insertion, as well as giving a first
approximation of the illumination condition of SR during the observation and a solid analysis of the ground
station visibility during the free flight phase after the observation.


5.3.2 DoE Results


A DoE was conducted to select an optimal WSE. But to decide which WSE is the best, it was necessary to
define a set of constraints or parameters to minimize/maximize:


  - **Payload maximum range** : this value was temporarily set to 200 m in the previous study. However,
since then SR’s KOZ has been updated to 200 m, thus making it impossible to respect both
constraints. Since the work performed for this thesis concerns Phase B2, an updated value for the
payload maximum range was not available. For this reason, the intervals during which SR is visible


64


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


by the payload have been calculated considering three possible maximum ranges: 250-300-350 m
(although the values most close to the actual payload requirements should be the first one);

  **Minimum actual observation time** : how much time during the observation SR in the payload range;
since a minimum value had not been defined, it was selected the WSE with the highest actual
observation time;

  **Minimum duration of the single observation** : although the total time may be enough, it could be
obtained by considering periods too short to produce useful data. However, from the analysis of the
WSEs from the DoE, it was noticed that the shortest interval was lasting 165 seconds, which was
considered more than sufficient for the payload to take pictures of SR;


As mentioned before, the Matlab function requires the user to define the following parameters: duration of
the observation, Δ𝑦 𝑐, 𝑥 𝑚𝑎𝑥 and 𝑧 𝑚𝑎𝑥 . Several combinations of sets of these values were tested, and their
results were evaluated in terms of: deltaV required for both the OPA rendezvous and the WSE Insertion,
duration of the FreeFlight and duration of the actual observation (reported both in hours and percentage of
the whole observation segment).


Every set of values for each variable was selected considering the ones used for the WSE DoE in phase B1,

which selected a WSE with:


  - Δ𝑦 𝑐 = 400 𝑚 ;

  - 𝐷𝑢𝑟𝑎𝑡𝑖𝑜𝑛= 6 ℎ𝑟 ;

  - 𝑥 𝑚𝑎𝑥 = 150 𝑚;

  - 𝑧 𝑚𝑎𝑥 = 150 𝑚 ;


For this analysis, higher 𝑥 𝑚𝑎𝑥 and 𝑧 𝑚𝑎𝑥 were considered because the radio of KOZ was increased to 200 m;
since the phase B1 analysis stated that only for a small percentage of the observation SR was in the payload
range, a higher duration was considered to increase the total actual observation time.


_Table 5.3: WSE DoE DeltaVs_

|Col1|Col2|𝒙, 𝒛 [m]<br>𝒎𝒂𝒙 𝒎𝒂𝒙|Col4|Col5|
|---|---|---|---|---|
|𝚫𝒚𝒄** [m]**|**Duration [hr]**|**250-200**|**250-250**|**DeltaV [m/s]**|
|300|6|0.485|0.559|0.559|
|300|8|0.485|0.558|0.558|
|400|6|0.496|0.5689|0.5689|
|400|8|0.491|0.549|0.549|
|600|6|0.459|0.515|0.515|
|600|8|0.459|0.515|0.515|



_Table 5.4: WSE DoE FreeFlight Duration_

|Col1|Col2|𝒙, 𝒛 [m]<br>𝒎𝒂𝒙 𝒎𝒂𝒙|Col4|Col5|
|---|---|---|---|---|
|𝚫𝒚𝒄** [m]**|**Duration [hr]**|**250-200**|**250-250**|**FreeFlight Duration**<br>**[hr]**|
|300|6|8.746|8.745|8.745|
|300|8|6.777|6.776|6.776|
|400|6|8.902|8.898|8.898|
|400|8|6.754|4.96|4.96|
|600|6|10.062|10.061|10.061|
|600|8|8.062|8.061|8.061|



Table 5.3 shows the deltaV of each WSE evaluated and highlights the two solutions with the lowest deltaV
in green. The only difference between the two solutions is the duration of the observation phase, while the
geometrical parameters of the WSEs are the same. The reason why they have the same deltaV is that they


65


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


are the same WSE: they start at the same relative position from SR and with the same initial relative
velocity, but the first one just ends the observation phase two hours before. This is also confirmed by the
duration of their free flight segments (Table 5.4): since they are the same WSE, they take the same total
time to perform the observation and propagate during the free flight to the maximum range stopping
condition. In fact, the total duration of both solutions is 18.062 hours, the only thing that separates them is
the decision to stop performing observations and start the downlink of the data.


_Figure 5.11:RIC components as functions of the time for the two highlighted WSE (6 hr on the left and 8 hours on the right)_


_Table 5.5: Total duration of the actual observation [hr]_





|Col1|Col2|Col3|𝒙, 𝒛 [m]<br>𝒎𝒂𝒙 𝒎𝒂𝒙|Col5|Col6|
|---|---|---|---|---|---|
|𝚫𝒚𝒄** [m]**|**Max Range [m]**|**Duration [hr]**|**250-200**|**250-250**|**Actual Observaton Duration [hr]**|
|300|250|6|0.3792|0.2622|0.2622|
|300|250|8|0.6176|0.4696|0.4696|
|300|300|6|1.5036|1.377|1.377|
|300|300|8|2.1088|1.9352|1.9352|
|300|350|6|2.2974|2.1144|2.1144|
|300|350|8|3.2096|2.9472|2.9472|
|400|250|6|0.4584|0.3138|0.3138|
|400|250|8|0.5136|0.408|0.408|
|400|300|6|1.641|1.431|1.431|
|400|300|8|2.0344|1.9464|1.9464|
|400|350|6|2.664|2.289|2.289|
|400|350|8|3.0944|2.7936|2.7936|
|600|250|6|0.555|0.3552|0.3552|
|600|250|8|0.6472|0.4384|0.4384|
|600|300|6|1.7712|1.5312|1.5312|
|600|300|8|2.1424|1.8616|1.8616|
|600|350|6|2.7888|2.4306|2.4306|
|600|350|8|3.3752|2.9656|2.9656|


66


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Table 5.6: Total duration of the actual observation [%]_






|Col1|Col2|Col3|𝒙, 𝒛 [m]<br>𝒎𝒂𝒙 𝒎𝒂𝒙|Col5|Col6|
|---|---|---|---|---|---|
|𝚫𝒚𝒄** [m]**|**Max Range [m]**|**Duration [hr]**|**250-200**|**250-250**|**Actual Observaton Duration [%]**|
|300|250|6|6.32|4.37|4.37|
|300|250|8|7.72|5.87|5.87|
|300|300|6|25.06|22.95|22.95|
|300|300|8|26.36|24.19|24.19|
|300|350|6|38.29|35.24|35.24|
|300|350|8|40.12|36.84|36.84|
|400|250|6|7.64|5.23|5.23|
|400|250|8|6.42|5.1|5.1|
|400|300|6|27.35|23.85|23.85|
|400|300|8|25.43|24.33|24.33|
|400|350|6|44.4|38.15|38.15|
|400|350|8|38.68|34.92|34.92|
|600|250|6|9.25|5.92|5.92|
|600|250|8|8.09|5.48|5.48|
|600|300|6|29.52|25.52|25.52|
|600|300|8|26.78|23.27|23.27|
|600|350|6|46.48|40.51|40.51|
|600|350|8|42.19|37.07|37.07|



For each solution the evolution of the RIC components and the range as a function of the time were saved
and graphed. Figure 5.11 shows the RIC components of the two highlighted WSE: it is possible to see that
for the first 6 hours, they have the same components. Table 5.5 and Table 5.6 show the actual observation
duration for each of the three maximum payload ranges considered and highlight the highest. As expected,
the actual duration of the observation is higher for the WSE lasting 8 hours than for the ones lasting 6
hours; however, the percentage of the actual observation duration with respect to the total duration is
often lower for the WSE lasting 8 hours. This can be explained by looking at the trajectory of SROC during
these WSEs: for example, Figure 5.11 shows that SROC starts the observation with a slightly negative
InTrack, then the trajectory moves to the more negative InTrack until, because of the effect of the
atmospheric drag, SROC starts moving towards positive InTrack. For a portion of the 8-hour case, SROC is in
the most negative SE, therefore it has a very short interval during which it can observe SR.


67


_-_
_Chapter 5_ _Nominal Scenarios Analysis_

i



_Figure 5.12: Range as function of the time for the WSE with the longest actual observation duration_


Figure 5.12 shows the range as a function of the time for the solution highlighted in green in Table 5.5. With
this WSE, SROC can take pictures of SR during seven intervals, with the shortest one lasting 162 seconds; it
is noticed that, in accordance with what has been said in the last paragraph, by increasing the length of the
observation from 6 hr to 8 hr, only a small interval (approximately 6 minutes) is added to the actual
observation duration.


5.3.3 Nominal Observaton Cycle i


From the results presented in the last sub-section, the WSE with the lowest deltaV and also the highest
actual observation duration is obtained by giving the following inputs to the Matlab function:


  - Δ𝑦 𝑐 = 600 𝑚 ;

  - 𝑥 𝑚𝑎𝑥 = 250 𝑚 ;

  - 𝑧 𝑚𝑎𝑥 = 200 𝑚 ;

  - 𝐷𝑢𝑟𝑎𝑡𝑖𝑜𝑛= 8 ℎ𝑜𝑢𝑟𝑠 ;


The visibility of SR during the observation was analysed using SRK’s tools Analysis Workbench and Access. A
sensor object was attached to SROC, and it was set to always points toward SR, thus simulating the
camera(s) pointing to SR. The visibility, which STK evaluates as access, of the spacecraft from the sensor was
constrained as follows:


  - Maximum range between SROC and SR: 250 m;

  LOS illumination angle less than 60 deg;

  - SR is in sunlight;


Figure 5.13 shows the intervals when each of these constraints is satisfied. The intervals where the range is
less than 250 m (in blue) are the same shown in Figure 5.12, while SR is in sunlight for intervals (in green)
lasting 56 minutes divided by 36 minutes long umbra periods. The LOS illumination angle condition is always
respected (in red): as shown in Figure 5.14 during the observation the maximum angle reached is 54.29
degrees.


68


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.13: Satisfaction interval for every constraint_


_Figure 5.14: LOS illumination angle during the observation phase_


By applying all the constraints, the intervals suitable to perform observation of SR are only three and they
last for a total of 915 seconds (Table 5.7). Although the length of each interval should be enough to take
pictures of SR, the total duration of the actual observation may not be enough to perform a satisfying
observation of SR. This problem could be solved by setting the duration of the HP2 in a way that makes the
moments when SR is in the payload range with the sunlight interval. For example, Figure 5.15 and Table 5.8
shows how the total observation time increases when the HP is performed after 4.3 hours; however, due to
the complex nature of the motion it is difficult to predict how performing the observation at a different
moment will affect the LOS illumination angle. As said at the beginning the DoE description, for further
analyses it will be necessary to increase the accuracy of the WSE definition by evaluating the effects of the
disturbances on the WSE. By doing so, it should be obtained a more “stable” WSE, such that it varies very
little from the input geometrical parameters. Moreover, with a more stable function for the WSE definition,
it could be possible to reduce the 𝑥 𝑚𝑎𝑥 and 𝑧 𝑚𝑎𝑥 without risking the intersection of the WSE with the KOZ.


69


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Table 5.7: Suitable observation intervals_

|Access|Start Time (UTCG)|Stop Time (UTCG)|Duration (sec)|
|---|---|---|---|
|1|12 Nov 2024 13:46:10.830|12 Nov 2024 13:49:54.735|223.905|
|2|12 Nov 2024 15:17:18.207|12 Nov 2024 15:23:09.336|351.128|
|3|12 Nov 2024 16:52:39.080|12 Nov 2024 16:58:18.928|339.848|
|Mean Duraton|-|-|304.960|
|Total Duraton|-|-|914.881|



_Figure 5.15: Satisfaction interval for every constraint with a different HP2 duration_


_Table 5.8: Suitable observation intervals with a different HP2 duration_

|Access|Start Time (UTCG)|Stop Time (UTCG)|Duration (sec)|
|---|---|---|---|
|1|12 Nov 2024 09:09:43.225|12 Nov 2024 09:15:12.745|329.520|
|2|12 Nov 2024 09:40:03.117|12 Nov 2024 09:42:45.466|162.349|
|3|12 Nov 2024 13:36:29.278|12 Nov 2024 13:39:48.232|198.955|
|4|12 Nov 2024 15:08:27.998|12 Nov 2024 15:13:44.707|316.709|
|5|12 Nov 2024 16:44:11.199|12 Nov 2024 16:49:49.577|338.378|
|Mean Duraton|-|-|269.182|
|Total Duraton|-|-|1345.911|



Finally, the GS coverage during the free flight was evaluated, to estimate how long SROC has access to the
ground station network to perform the Downlink of the mission data. Figure 5.16 shows the access during
this phase, while Table 5.9 resume summarizes the results of the analysis. A total time of 1.774 hours
should be enough to downlink the mission data to the ground stations.


70


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.16: Ground station access during the free flight (the SROC line refers to the total access)_


_Table 5.9: Summary of the access analysis during the free flight_

|Results|Value|
|---|---|
|Minimum Duraton|196 sec|
|Maximum Duraton|394 sec|
|Mean Duraton|336 sec|
|Total Duraton|6388 sec|
|Percentage of the free fight|29.28%|



Since the ground station coverage seems more than enough to downlink the mission data, another option is
to increase the duration of the inspection phase in spite of the duration of the free flight. In fact, there is a
portion at the beginning of the free flight when SROC still respects all the observation constraints: to
consider this interval the observation phase was increased from 28800 seconds to 39737 seconds. Figure
5.17 and Table 5.10 show a great increase in the total suitable observation interval, while Table 5.11 shows
that there is still a considerable amount of time to downlink the mission data (1.036 hours).


_Table 5.10: Suitable observation intervals with a longer observation phase_

|Access|Start Time (UTCG)|Stop Time (UTCG)|Duration (sec)|
|---|---|---|---|
|1|12 Nov 2024 13:46:10.830|12 Nov 2024 13:49:54.735|223.905|
|2|12 Nov 2024 15:17:18.208|12 Nov 2024 15:23:09.336|351.128|
|3|12 Nov 2024 16:52:39.081|12 Nov 2024 16:58:18.929|339.848|
|4|12 Nov 2024 18:30:54.677|12 Nov 2024 18:36:12.639|317.961|
|5|12 Nov 2024 20:12:34.937|12 Nov 2024 20:28:56.278|981.342|
|Mean Duraton|-|-|442.837|
|Total Duraton|-|-|2214.184|



71


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Figure 5.17: Satisfaction interval for every constraint considering a longer observation sub-phase_


_Table 5.11: Summary of the access analysis during the free flight considering a longer observation sub-phase_

|Results|Value|
|---|---|
|Minimum Duraton|233 sec|
|Maximum Duraton|394 sec|
|Mean Duraton|339 sec|
|Total Duraton|3731 sec|
|Percentage of the free fight|20.63%|



Since this is a Phase B2 study, this work was carried out before the other mission actors perform new
iterations on their respective work. For example, the payload was initially studied to take pictures from a
maximum range of 200 m: since the KOZ was updated from 150 to 200m, a new study is required to assess
the capability of the camera at higher ranges. For this reason, assessing if the actual observation intervals
are enough to take a sufficient number of useful pictures is not possible at the moment; however this study
constitutes a solid base to help understand the different constraints during the observation sub-phase and,
in case it is changed during future project iterations, the constraints and analysis tools defined in STK for
this DoE will still be useful to rapidly assess the feasibility of the new design.


In conclusion, the WSE presented at the beginning of the sub-section was selected for the nominal scenario.
The two alternative options to increase the actual observation time have not been considered since, as
explained before, is not possible to define minimum observation requirements, so it is not possible to select
one option instead of the other. Moreover, picking one of the other two solutions would not significantly
affect the results of this thesis, which are the deltaV budgets of the nominal and variant scenarios. In fact,
changing the duration of the HP2 would slightly modify an already low deltaV contribution to the total
deltaV budget, while the second option would not even modify it since it just postpones the switch from the
observation to the free flight. To consider the many uncertainties linked to the analysis of the WSE, the
margin on its deltaV was increased and the use of a second observation cycle was considered in the variant
analysis (Chapter 6).


72


_-_
_Chapter 5_ _Nominal Scenarios Analysis_

##### 5.4 Nominal Scenarios DeltaV Budget


After updating the code and analysing some fundamental aspects of the mission, it was possible to run the
complete simulation of the nominal scenarios. The results of these simulations were used to define the
deltaV budget and the time budget. The DeltaV budget is fundamental to evaluate if the mission is feasible
or if some of its aspect need to be modified to be less deltaV-consuming. As stated in requirement SROCMIS-060: “The ΔV for all SROC manoeuvres shall be less than 20 (TBC) m/s including margins”, so it is vital
for the mission to stay below the 20 m/s threshold. The time budget, instead, was not compiled to verify
the compliance with a specific requirement, since there is none; indicatively, it was decided to set a
maximum total duration of 30 days since the total duration of SR’s mission is two months. This information
will be useful in the future phases of the design when it will be clearer at which moment of its orbital
operations SR will deploy SROC and it will be necessary to coordinate SROC’s operations with SR’s.


Table 5.12 shows the deltaV budget for the nominal Observe scenario. The two Virtual CAMs reported in
the table refer to the manoeuvres which could be performed around a virtual point during HP1. Both, as
well as the SR Collision Avoidance Manoeuvre (CAM) were evaluated using different software and
processes, therefore they are not part of this thesis. The Debris CAM (D CAM) was evaluated using the
software DRAMA, whose analysis and results are described in Chapter 7. It is noted that the margin
philosophy used in this study for the deltaV is the one recommended by ESA and reported in the ECSS [27].


_Table 5.12: DeltaV budget for the nominal observe scenario_

|OBSERVE<br>Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**∆V [m/s]**|**Margin**|**∆V [m/s]**|
|HP1|0.489|5%|0.513|
|Virtual CAM + HP1 bis|1.040|100%|2.080|
|Virtual CAM + HP1 ter|0.500|100%|1.000|
|IPA|0.485|5%|0.509|
|HP2Ins|1.280|5%|1.344|
|ZRV2|0.423|5%|0.444|
|HP2|0.096|5%|0.101|
|OPA - Cycle 1|0.266|100%|0.532|
|WSE Insertion - Cycle 1|0.192|100%|0.385|
|OPA - Cycle 2|0.000|100%|0.000|
|WSE Insertion - Cycle 2|0.000|100%|0.000|
|D CAM|0.068|100%|0.136|
|SR CAM|0.600|5%|0.630|
|**∆V TOT [m/s]**|**5.439**|**∆V TOT with**<br>**margins [m/s]**|**7.674**|



Table 5.13 shows the time budget for the nominal Observe Scenario. It considered all the mission phases
until the end of the POP, since the successive phase (EMP) does not require any coordination with SR’s
mission. It is noted that the only part of the Verification sub-phase that has been considered is the HP1
reported in the STK scenario; so the total duration and deltaV could greatly increase when the nominal
Verification sub-phase will be baselined.


73


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Table 5.13: Time budget for the nominal Observe scenario_

|OBSERVE<br>Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**Duration [day]**|**Margin**|**Duration [day]**|
|Commissioning|5.000|5%|5.250|
|HP1|0.188|5%|0.197|
|IPA|5.760|5%|6.048|
|HP2Ins|0.083|5%|0.088|
|HP2|0.188|5%|0.197|
|OPA - Cycle 1|0.167|5%|0.175|
|Observation + FreeFlight - Cycle 1|0.669|5%|0.703|
|OPA - Cycle 2|0.000|5%|0.000|
|Observation + FreeFlight - Cycle 2|0.000|5%|0.000|
|**Duration TOT [day]**|**12.054**|**Duration TOT with**<br>**margins [day]**|**12.657**|



Table 5.14 and Table 5.15 show respectively the deltaV and the time budget for the nominal
Observe&Retrieve scenario. Although this scenario will not be applied for SROC’s first mission, it is useful to
study it for successive missions, when SROC docking capabilities will be tested. The deltaV for the Final
Approach Phase (called Docking) was evaluated outside of this thesis.


_Table 5.14: DeltaV budget for the nominal Observe&Retrieve scenario_

|OBSERVE & RETRIEVE<br>Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**∆V [m/s]**|**Margin**|**∆V [m/s]**|
|HP1|0.489|5%|0.513|
|Virtual CAM + HP1 bis|1.040|100%|2.080|
|Virtual CAM + HP1 ter|0.500|100%|1.000|
|IPA|0.485|5%|0.509|
|HP2Ins|1.280|5%|1.344|
|ZRV2|0.423|5%|0.444|
|HP2|0.096|5%|0.101|
|OPA - Cycle 1|0.266|100%|0.532|
|WSE Insertion - Cycle 1|0.192|100%|0.385|
|OPA - Cycle 2|0.000|100%|0.000|
|WSE Insertion - Cycle 2|0.000|100%|0.000|
|HP3Ins|0.221|5%|0.232|
|ZRV3|0.438|5%|0.459|
|HP3|0.094|5%|0.099|
|Docking|0.900|5%|0.945|
|D CAM|0.068|100%|0.136|
|SR CAM|0.600|5%|0.630|
|**∆V TOT [m/s]**|**7.092**|**∆V TOT with**<br>**margins [m/s]**|**9.409**|



74


_-_
_Chapter 5_ _Nominal Scenarios Analysis_


_Table 5.15: Time budget for the nominal Observe&Retrieve scenario_

|OBSERVE & RETRIEVE<br>Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**Duration [day]**|**Margin**|**Duration [day]**|
|Commissioning|5.000|5%|5.250|
|HP1|0.188|5%|0.197|
|IPA|5.760|5%|6.048|
|HP2Ins|0.083|5%|0.088|
|HP2|0.188|5%|0.197|
|OPA - Cycle 1|0.167|5%|0.175|
|Observation + FreeFlight - Cycle 1|0.669|5%|0.703|
|OPA - Cycle 2|0.000|5%|0.000|
|Observation + FreeFlight - Cycle 2|0.000|5%|0.000|
|HP3Ins|0.113|5%|0.118|
|HP3|0.188|5%|0.197|
|Final Approach|0.007|5%|0.007|
|**Duration TOT [day]**|**12.361**|**Duration TOT with**<br>**margins [day]**|**12.979**|



75


## _6 Variant Scenarios Analysis_

A crucial point for the development of SROC’s Phase B2 project is the analysis of the variant scenarios: each
mission phase was analysed to assess if and how a deviation from its nominal condition could affect the
whole mission. The variant events considered in this study can be divided into two categories:


  Programmatic: they take into consideration that some design features of several mission phases are
yet to be confirmed and that they could change in future design iterations. For example, as
mentioned in Sub-ection 5.3.2, it may be considered necessary to perform two inspections to
successfully observe SR;

  Operative: during SROC’s operations, variant events could modify the execution of one or more
phases. For example, a fault of the RF link establishment during the Commissioning Phase may
increase its duration. Other variant scenarios caused by a thruster error in the direction or the
magnitude of the thrust, have not been evaluated, since they were already considered in a Phase
B1 study;


HP2 was considered as a discontinuity point, after which no previous variant events affect the successive
ones. For this reason, the analysis, and this document too, has been divided as follows:


  Variant events before HP2 (Section 6.1);

  Variant events from HP2 onwards (Section 6.2); they also include a variant EMP: as it is explained in
Sub-section 6.2.2, according to an STK simulation, SROC will not approach SR in its proximity after
the POP. However, a list of possible manoeuvres to avoid an eventual encounter with SR has been
proposed and studied;


Section 6.3 analyses the results of this variants analysis, while also providing deltaV and time budgets of
two variant scenarios for both the Observe and the Observe&Retrieve scenarios. Moreover, all the variant
scenarios obtained are analysed to see which options are viable and which constitute an off-nominal
scenario.

##### 6.1 Variant Events Before HP2


The following variant events were considered:


  Longer Commissioning Phase: it was considered a duration of 10 days instead of 5;

  Longer Verification Phase: it was considered a longer duration (13.5 hours instead of 4.5); although
the Verification Phase is yet to be defined completely, it is still useful to understand how a different
duration may affect the mission;


Figure 6.1 shows the different possible scenarios which can be obtained by combining the nominal and
variant segments of the commissioning and the HP1. The Matlab functions, after analysing a segment
containing a manoeuvre, obtain a set of possible solutions to reach the desired results, and, for the nominal
scenario, they set as nominal the manoeuvre which minimizes the deltaV. For this reason, the nominal
scenarios only have one solution, which is the one minimizing the deltaV, which is referred to as the deltaVdown solution. However, during the analysis of the variant scenario, it came clear that it could have been
useful, for the successive design iteration, to also have a set of time-down solutions, which aim at
decreasing the duration of the mission, while also maintaining an acceptable deltaV budget.


This goal was particularly difficult for the variant scenario with a longer commissioning, where three
alternative solutions to the standard time-down were considered (see Sub-section 6.1.2)


76


_-_
_Chapter 6_ _Variant Scenarios Analysis_



_Figure 6.1: Pre-HP2 variant scenarios_


77


_-_
_Chapter 6_ _Variant Scenarios Analysis_


6.1.1 Longer HP1


For this variant scenario, it was considered a longer HP1, from 4.5 hours to 13.5 hours. From the results
reported in Table 6.1, the deltaV required to perform the HP1 does not change. This is due to how the HP1
manoeuvre has been defined: as mentioned before the target sequence of HP1 does not target a specific
relative position, rather it sets SROC’s semi-major axis to be the same as SR’s. This desired value is reached
with the same manoeuvre as the nominal scenario, the only difference is that SROC propagates for a longer
time. As shown in Figure 6.2, this causes SROC to reach a further final relative position: -11.3 km along the
Radial direction (instead of -10.9 km) and 377 km along the InTrack direction (instead of 373 km).


_Figure 6.2: HP1 trajectory in RIC coordinates for a longer commissioning_


The different relative position reached by SROC affects the successive segments: as shown in Table 6.1, the
deltaV-down solution requires a higher deltaV with respect to the nominal scenario, while the duration of
the segments after the HP1 does not change. Although a 9-hour delay does not have a huge influence on
the total duration of the mission, a time-down solution was still analysed to recover part of the 9 hours lost
in HP1. This was achieved by decreasing the duration of the IPA by 7 hours and 41 minutes, but at the cost
of a higher deltaV. Table 6.2 summarizes the properties of this time-down solution and compares them to
the ones of the nominal Observe&Retrieve scenario. This comparison table, as well as the successive ones,
does not include safety margins; they are considered in the summary in Section 6.3.


_Table 6.1: DeltaV and duration comparison between the nominal and the LongHP1 - DeltaV-Down (DD) scenarios_





|Mission<br>Segment|Nominal [m/s]|Col3|LongHP1 (DD)<br>[m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.489|0.489|
|IPA|0.485|2.188|0.518|2.405|
|HP2Ins|1.280|1.280|1.495|1.495|
|ZRV2|0.423|0.423|0.392|0.392|
|Tot PreHP2|2.677|2.677|2.894|2.894|
|Tot Mission|7.092|7.092|7.309|7.309|


78




|Mission<br>Segment|Nominal [day]|Col3|LongHP1 (DD)<br>[day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|5.000|5.000|
|HP1|0.188|0.188|0.563|0.563|
|IPA|5.760|5.843|5.760|5.843|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Tot PreHP2|11.031|11.031|11.406|11.406|
|Tot Mission|12.361|12.361|12.736|12.736|


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.2: DeltaV and duration comparison between the nominal and the LongHP1 - Time-down (TD) scenarios_



|Mission<br>Segment|Nominal [day]|Col3|LongHP1 (TD)<br>[day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|5.000|5.000|
|HP1|0.188|0.188|0.563|0.563|
|IPA|5.760|5.843|5.440|5.523|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|11.086|11.086|
|Total<br>Mission|12.361|12.361|12.416|12.416|


6.1.2 Longer Commissioning Phase




|Mission<br>Segment|Nominal [m/s]|Col3|LongHP1 (TD)<br>[m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.489|0.489|
|IPA|0.485|2.188|0.521|2.480|
|HP2Ins|1.280|1.280|1.617|1.617|
|ZRV2|0.423|0.423|0.343|0.343|
|Total PreHP2|2.677|2.677|2.969|2.969|
|Total<br>Mission<br>|7.092|7.092|7.383|7.383|



The second variant scenario considers a longer HP1: from 5 days to 10 days. Increasing the duration of the
commissioning poses two main problems:


  The final relative position of SROC at the end of this phase greatly increases because of the
atmospheric drag, which acts for a longer time, further distancing the satellite from SR. As shown in
Figure 6.3, the final relative position of the satellite is:

`o` Radial: -118.44 km

`o` InTrack: 1264.49 km

`o` CrossTrack: -0.13 km
It is noted that the RIC reference system starts losing its meaning at such a high relative position. In
fact, it is not respected one of the assumptions at the base of this relative reference system, which
is that the relative position vector magnitude must be small if compared to the chief position vector
magnitude. A good parameter to compare this final relative position with the one obtained with the
nominal duration of the commissioning is the range: about 1270 km for the first case and 373 km
for the latter.

  The total duration of the mission almost doubles, not only because of the additional five days
required to complete the commissioning phase, but also because the IPA manoeuvre requires more
time to reach the desired target position.


_Figure 6.3: Propagation of a 10-days long commissioning_


79


_-_
_Chapter 6_ _Variant Scenarios Analysis_


6.1.2.1 DeltaV - Down Soluton i


The first solution analysed was the deltaV-down one. The InTrack position as a function of the time during
the optimal IPA is shown in Figure 6.4: as mentioned earlier, the IPA is longer than the nominal case. So, not
only SROC loses 5 days because of the different commissioning, but also requires approximately 6 days
more to execute the IPA.

i



_Figure 6.4: InTrack position as function of the time during the IPA - LongComm (DD)_


Table 6.3 shows the results of the analysis in terms of duration and deltaV. As expected, the total deltaV
increases, although only by approximately 1.2 m/s, since a deltaV solution was applied. This increase is
mainly due to the higher deltaV required to perform the IPA: the required value is 81% higher than the
nominal one. Another interesting observation is that the deltaV of the HP1 changes with respect to the
nominal scenario, although its duration is the nominal one (4.5 hours). This is caused by the decrease of
SROC’s semi-major axis: since it drifts for more days, the drag decreases its height more than the nominal
case. So, it is required a bigger impulse to guarantee a bigger increase in the semi-major axis. The shape of
SROC’s trajectory during the HP1 changes too, but as shown in Figure 6.5, SROC still rotates around a
fictitious point without varying its InTrack position of more than 4 km.


_Table 6.3: DeltaV and duration comparison between the nominal and the LongComm – DeltaV-Down (DD) scenarios_



i



i



i



i

|Mission<br>Segment|Nominal [m/s]|Col3|LongHP1 (DD)<br>[m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|0.879|2.943|
|HP2Ins|1.280|1.280|1.474|1.474|
|ZRV2|0.423|0.423|0.590|0.590|
|Total<br>PreHP2|2.677|2.677|3.830|3.830|
|Total<br>Mission|7.092|7.092|8.245|8.245|



80



i


|Mission<br>Segment|Nominal [day]|Col3|LongHP1 (DD)<br>[day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.188|0.188|
|IPA|5.760|5.843|11.400|11.483|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|21.671|21.671|
|Total<br>Mission|12.361|12.361|23.001|23.001|


_-_
_Chapter 6_ _Variant Scenarios Analysis_

i



_Figure 6.5: SROC Trajectory during HP1 - LongComm (DD)_


6.1.2.2 Time - Down Soluton i


The worrying increase of the total duration of the mission made necessary the study of a time-down
solution.


_Table 6.4: DeltaV and duration comparison between the nominal and the LongComm - Time-Down (TD) scenarios_



i



i



i



i


|Mission<br>Segment|Nominal [day]|Col3|LongHP1 (TD)<br>[day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.188|0.188|
|IPA|5.760|5.843|10.820|10.903|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|21.091|21.091|
|Total<br>Mission|12.361|12.361|22.421|22.421|


|Mission<br>Segment|Nominal [m/s]|Col3|LongHP1 (DD)<br>[m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|0.881|3.107|
|HP2Ins|1.280|1.280|1.679|1.679|
|ZRV2|0.423|0.423|0.547|0.547|
|Total<br>PreHP2|2.677|2.677|3.994|3.994|
|Total<br>Mission|7.092|7.092|8.409|8.409|



i


The total duration obtained with this solution was not as low as hoped: as shown in Table 6.4, the total
duration obtained is just 14 hours less than the deltaV one. As explained in Section 4.2, at the end of the IPA
the trajectory of SROC is propagated for 24 hours to assess the risk to SR in case no manoeuvre is
performed in the successive 24 hours. The IPA optimization functions only considered an IPA valid if it does
not cross 200 m along the InTrack direction during this propagation. The solutions which would decrease
the duration of the IPA are also the ones that would result in a higher relative velocity at the end of the IPA,
which would cause them to cross the 200 m InTrack limit in the successive 24-hour propagations.


For this reason, alternative solutions to reduce the time were considered:


  Alternative Time-down 1 (ATD-1): run the same Matlab function, but without considering the 24hours propagation after the IPA;

  Divide the IPA into two parts: during the first one, it is performed the TD1. However, instead of
propagating until the desired relative position is reached, the satellite performs a second
manoeuvre during the propagation. This additional manoeuvre aims at respecting the 24-hours


81


_-_
_Chapter 6_ _Variant Scenarios Analysis_


propagation constraint by reducing the relative velocity of SROC. Two possible starting points for
the IPA Brake were considered:

`o` Alternative Time-down 2 (ATD-2): the braking manoeuvre is performed 24 hours before the

end of the TD1;
`o` Alternative Time-down 3 (ATD-3) the braking manoeuvre is performed 12 hours before the

end of the TD1;
By doing so, it may be recovered some time by the first part of the IPA, which is faster, while the
second part should guarantee a manoeuvre safe enough.


Figure 6.6 shows how the ATD-2 and the ATD-3 are defined (lower lines) from the ATD-1 (higher lines). For
the ATD-2 and ATD-3, it is important to not confuse the interval of time which is subtracted to the ATD-1
(that is 24 or 12 hours) with the actual duration of the IPA after the brake, which is longer since the relative
motion towards SR has been decreased.

i i



_Figure 6.6: Alternative time-down solutions comparison and definition_


6.1.2.3 Alternatve Time i - Down Solutons i – ATD - 1

i i



_Figure 6.7: 3D plot of the total deltaV as function of the total duration and the IPA InTrack target – ATD-1_


82


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Figure 6.7 shows a plot with all the possible IPA + HP2 insertion + ZRV2 sequences for the ATD-1 solution (all
the circles refer to one analysed sequence). It is noted that the adjective “total” is used to refer to the
entirety of the IPA + HP2 insertion + ZRV2 sequences. These results were obtained by iterating on the
following values:


  - IPA InTrack target: [3:0.5: 7] km;

  IPA Duration: [2:0.1:6] days;


Although the aim of the analysis is to define a time-down solution, as shown in Figure 6.8, the solutions
guaranteeing the lowest total duration are too much expensive deltaV-wise. For this reason, the final
solution has been selected among the ones in the red box.


_Figure 6.8: Total DeltaV as function of the total Duration – ATD-1_


Figure 6.9 shows the trends of both the total deltaV (blue line) and the IPA’s deltaV (red line) as a function
of the duration of the IPA. As expected, the IPA’s deltaV trend decreases with its duration: this can be
explained by considering that the fastest the IPA is, the higher variation in the kinetic energy is required.
The behaviour for the total deltaV, instead, is a bit different: although the trend of the solutions decreases
with the duration of the IPA, the single solutions do not. This discrepancy with the IPA’s deltaV is caused by
the deltaV contribution of the HP2 insertion and ZRV2 manoeuvres.


Different combinations of durations and InTrack targets define a different set of relative positions and
velocities at the end of the IPA, thus influencing the required deltaV for the successive manoeuvres. This
means that small differences in the selection of the moment to end the IPA and start the HP2 insertion (in
the order of tens of minutes) can change the cost of the HP2 insertion and subsequent ZRV2 manoeuvre. Of
course, to consider this factor, it should be used smaller steps for the IPA InTrack target and IPA duration
than the ones considered for this analysis. However, this change was not applied because it would have
increased considerably the analysis time required by the Matlab functions. Moreover, this approach gives a
more conservative estimate of the required deltaV, since, in case an ulterior optimization was required, the
allocated total deltaV could only decrease with respect to the current results. Finally, to consider the
optimal moment to end the IPA with precision in the order of minutes it would be necessary to assess if the
actual manoeuvre could be performed with the same precision during the operative phase. In fact, in case
this condition could not be met by the mission, the allocated deltaV would be lower than the actual one.


83


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Figure 6.9: DeltaV trend according to the IPA duration - ATD-1_


Table 6.5 shows the duration and the deltaV required by the selected ATD-1 and the nominal scenario. Most
of the time lost during the longer commissioning is retrieved and the deltaV required, although higher of
2.268 m/s is still acceptable. This increase is mainly caused by the IPA manoeuvre (which costs 1.664 m/s
instead of 0.489 m/s as in the nominal scenario), although also the other pre-HP2 manoeuvres require a
higher deltaV than in the nominal scenario.


_Table 6.5: DeltaV and duration comparison between the nominal and the LongComm – ATD-1 scenarios_










|Mission<br>Segment|Nominal [day]|Col3|LongComm<br>(ATD-1) [day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.188|0.188|
|IPA|5.760|5.843|3.200|3.283|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|13.471|13.471|
|Total<br>Mission|12.361|12.361|14.802|14.802|


|Mission<br>Segment|Nominal [m/s]|Col3|LongComm<br>(ATD-1) [m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|1.664|4.058|
|HP2Ins|1.280|1.280|2.030|2.030|
|ZRV2|0.423|0.423|0.364|0.364|
|Total<br>PreHP2|2.677|2.677|4.945|4.945|
|Total<br>Mission|7.092|7.092|9.360|9.360|



Table 6.6 reports in each row the following properties of every valid solution: InTrack target, duration and
deltaV of the IPA, duration and deltaV of the HP2 insertion, deltaV for the ZRV2 manoeuvre, total deltaV
and total duration of the IPA + HP2 insertion + ZRV2 sequence. Finally, it also shows, in the last column, the
minutes which would take SROC to cross the 200 m InTrack position if its orbit was propagated after the IPA
instead of performing the HP2 insertion. From the safety point of view, these results are concerning since
they show that for every solution the KOZ is entered in less than 1 hour. For this reason, this ATD-1 solution
may be discarded as off-nominal. The row highlighted in orange is the solution with the lowest total
duration, while the one in yellow is the solution considered for the ATD-1.


84


_-_
_Chapter 6_ _Variant Scenarios Analysis_



_Table 6.6: Detailed results properties - ATD-1_


















|IPA Intrack<br>[km]|IPA Duration<br>[days]|IPA DeltaV<br>[m/s]|HP2Ins<br>Duration [hr]|HP2Ins<br>DeltaV|ZRV2 DeltaV|Total DeltaV|Total time|Time to 200<br>m [min]|
|---|---|---|---|---|---|---|---|---|
|4|2.3|2.221|5|3.955|1.420|7.597|2.508|45|
|4.5|2.3|2.220|5|3.930|1.398|7.549|2.508|46|
|5|2.3|2.220|5|3.905|1.376|7.501|2.508|47|
|5.5|2.3|2.219|5|3.880|1.354|7.453|2.508|47|
|6|2.3|2.218|5|3.854|1.332|7.405|2.508|48|
|6.5|2.3|2.217|5|3.829|1.311|7.357|2.508|49|
|7|2.3|2.216|2|3.944|1.121|7.282|2.383|49|
|6|3|1.752|5|3.687|2.445|7.885|3.208|58|
|6.5|3|1.752|5|3.662|2.423|7.837|3.208|59|
|7|3|1.751|5|3.638|2.400|7.789|3.208|59|
|3|3.2|1.666|2|2.384|0.225|4.274|3.283|43|
|3.5|3.2|1.665|2|2.265|0.219|4.150|3.283|44|
|4|3.2|1.664|2|2.147|0.275|4.086|3.283|45|
|4.5|3.2|1.664|2|2.030|0.364|4.057|3.283|46|
|5|3.2|1.663|3.5|2.257|0.213|4.133|3.346|47|
|5.5|3.2|1.663|3.5|2.214|0.225|4.102|3.346|48|
|6|3.2|1.662|3.5|2.171|0.245|4.078|3.346|49|
|6.5|3.2|1.661|3.5|2.128|0.270|4.060|3.346|50|
|7|3.2|1.661|3.5|2.086|0.299|4.046|3.346|50|
|3.5|3.9|1.418|5|2.864|1.087|5.368|4.108|55|
|4|3.9|1.417|5|2.840|1.065|5.321|4.108|56|
|4.5|3.9|1.417|5|2.815|1.043|5.275|4.108|57|
|5|3.9|1.416|5|2.791|1.021|5.228|4.108|58|
|5.5|3.9|1.416|5|2.766|1.000|5.182|4.108|59|
|6|3.9|1.415|2|2.824|0.824|5.062|3.983|60|
|6.5|3.9|1.415|2|2.701|0.721|4.836|3.983|61|
|7|3.9|1.414|2|2.578|0.625|4.617|3.983|62|
|5.5|4.6|1.253|5|2.710|2.057|6.020|4.808|68|
|6|4.6|1.252|5|2.686|2.035|5.974|4.808|70|
|6.5|4.6|1.252|5|2.662|2.013|5.927|4.808|71|
|7|4.6|1.252|5|2.639|1.991|5.881|4.808|72|
|3|4.8|1.219|2|2.136|0.258|3.613|4.883|55|
|3.5|4.8|1.219|2|2.013|0.276|3.508|4.883|56|
|4|4.8|1.218|2|1.891|0.340|3.450|4.883|57|
|4.5|4.8|1.218|2|1.768|0.430|3.417|4.883|58|
|5|4.8|1.218|3.5|2.026|0.262|3.506|4.946|59|
|5.5|4.8|1.217|3.5|1.983|0.278|3.478|4.946|60|
|6|4.8|1.217|3.5|1.940|0.299|3.456|4.946|61|
|6.5|4.8|1.216|3.5|1.896|0.325|3.438|4.946|63|
|7|4.8|1.216|3.5|1.853|0.354|3.423|4.946|64|
|7|5.3|1.140|5|2.036|2.890|6.066|5.508|79|
|4|5.5|1.116|5|2.478|1.125|4.719|5.708|68|
|4.5|5.5|1.115|5|2.455|1.103|4.673|5.708|69|
|5|5.5|1.115|5|2.431|1.082|4.628|5.708|70|
|5.5|5.5|1.115|5|2.408|1.060|4.583|5.708|71|
|6|5.5|1.114|5|2.384|1.039|4.538|5.708|73|
|6.5|5.5|1.114|2|2.397|0.806|4.317|5.583|74|
|7|5.5|1.114|2|2.276|0.708|4.097|5.583|75|
|3|5.7|1.094|6|1.182|1.003|3.278|5.950|55|
|3.5|5.7|1.094|6|1.180|1.008|3.282|5.950|56|
|4|5.7|1.093|6|1.179|1.013|3.286|5.950|58|
|4.5|5.7|1.093|6|1.178|1.019|3.289|5.950|59|
|5|5.7|1.093|6|1.177|1.024|3.293|5.950|60|
|5.5|5.7|1.092|6|1.176|1.030|3.297|5.950|61|
|6|5.7|1.092|6|1.175|1.035|3.302|5.950|63|
|6.5|5.7|1.092|6|1.174|1.041|3.306|5.950|64|



85


_-_
_Chapter 6_ _Variant Scenarios Analysis_


6.1.2.4 Alternatve Time i - Down Solutons i – ATD - 2


Since the solutions proposed for the ATD-1 may be considered off-nominal for not being safe enough, the
ATD-2 and ATD-3 solutions were proposed to guarantee compliance with the 200 m InTrack limit for a
hypothetical 24-hours propagation at the end of the IPA. A new Matlab function, called “IPA_Brake” was
created to evaluate the ATD-2 and the ATD-3 solutions. To define the ATD-1 solution the same Matlab
function described in Section 4.2 is used, with the only difference being that the hypothetical 24-hour
propagation at the end of the IPA and the relative InTrack check are not performed. At the end of this
analysis, if a specific flag defined by the user in the JSON of the IPA optimization function is true, the
“IPA_Brake” function is called. In short, this is the analysis process performed by this new function:


  Change the duration of the IPA propagation: as mentioned before, the braking manoeuvre is
defined starting from the point of the IPA propagation at 24 (for the ATD-2) and 12 (for the ATD-3)
hours from the end of the propagation itself; the MCS on STK is than run to apply these changes;

  - Add to STK the IPA_Brake target sequence, which is composed of the same segments as the IPA
Rendezvous target sequence:

`o` Manoeuvre segment to perform the braking manoeuvre;
`o` Propagation segment to propagate SROC to the desired InTrack position;
This sequence also has the same desired result (the InTrack position at the end of the propagation)
and the same control parameter (the thrust vector along the V axis of SROC’s VNC reference
system);

  Define the optimal brake manoeuvre in terms of the total deltaV required by the IPA brake + HP2
insertion + ZRV2 manoeuvres. This process is performed exactly as the one for the nominal
scenario:

`o` Different solutions obtained by iterating on the duration and the InTrack target are

analysed. In this case, the IPA duration does not refer to the whole IPA, but only to the
braked part, that is the propagate segment after the IPA brake;
`o` If they are valid, the successive HP2 insertion and ZRV2 manoeuvres are evaluated. The

constraints used to define the validity of the braked section of the IPA are the same used for
the nominal scenario analysis. Of course, since the aim of the ATD-2 and ATD-3 solutions is
to provide a safer solution than the ATD-1, they include the 200 m InTrack limit after a 24hours propagation at the end of the IPA;
`o` All the valid solutions are saved to be post-processed;

i i



_Figure 6.10: 3D plot of the total deltaV as function of the total duration and the IPA InTrack target – ATD-2_


86


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Figure 6.10 shows a 3D plot with all the possible IPA brake + HP2 insertion + ZRV2 sequences for the ATD-2
solution; the “total” adjective in the legend refers to the IPA brake + HP2 insertion and ZRV2 manoeuvres.
These results were obtained by iterating on the following values for the IPA_Brake target sequence:


  - InTrack target: [3:0.5: 7] km;

  Duration: [2:0.1:6] days;


The number of valid results is decisively less than the one for the ATD-1 analysis. This is due to the fact that
many solutions were discarded because they could not respect either the desired target values or the
compliance with the 200 m InTrack limit for the hypothetical 24-hour propagation at the end of the IPA.


Table 6.7 reports in each row the following properties of every valid solution: InTrack target, duration and
deltaV of the IPA Brake, duration and deltaV of the HP2 insertion, deltaV for the ZRV2 manoeuvre, total
deltaV and total duration. In this case, the adjective “total” refers to the IPA + IPA brake + HP2 insertion +
ZRV2 sequence. In fact, to evaluate the total duration, 2.2 days were added: the IPA with no brake would
last 3.2 days, but since the brake is performed 1 day before its theoretical end, the duration of this
propagation segment is just 2.2 days. To evaluate the total deltaV, 1.664 m/s were added to consider the
deltaV required to perform the first part of the IPA.


_Table 6.7: Detailed results properties - ATD-2_













|IPA Intrack<br>[km]|Braked IPA<br>Duration<br>[days]|IPA DeltaV<br>[m/s]|HP2Ins<br>Duration [hr]|HP2Ins<br>DeltaV|ZRV2 DeltaV|Total DeltaV|Total Time|
|---|---|---|---|---|---|---|---|
|3|5.8|1.011|2|4.593|0.283|7.551|8.083|
|3.5|5.8|1.011|2|4.480|0.313|7.468|8.083|
|4|5.8|1.012|2|4.367|0.382|7.425|8.083|
|4.5|5.8|1.012|2|4.255|0.473|7.404|8.083|
|5|5.8|1.012|3.5|4.513|0.290|7.480|8.146|
|5.5|5.8|1.013|3.5|4.475|0.309|7.461|8.146|
|6|5.8|1.013|3.5|4.437|0.331|7.446|8.146|
|6.5|5.8|1.013|3.5|4.399|0.358|7.435|8.146|
|7|5.8|1.014|3.5|4.361|0.388|7.427|8.146|


_Figure 6.11: InTrack as a function of the time - ATD-2_


87


_-_
_Chapter 6_ _Variant Scenarios Analysis_


The row highlighted in yellow in Table 6.7 was selected for the ATD-2 solution since it is both the faster and
the less-expensive deltaV-wise. Because of the braking manoeuvre, the total duration increases
significantly: Figure 6.11 shows that to cover the last 400 km along the InTrack direction SROC takes 5.8
days, while for the ATD-1 it would have taken only 1 day. Table 6.8 shows the deltaV and duration of each
segment before the HP2 (the IPA rows consider both the first and the braked part). In conclusion, the total
duration decreases by 2.819 days with respect to the standard time-down solution, which requires a total of
22.421 days. On the other hand, the total deltaV increases by 79.16% from the nominal scenario.


_Table 6.8: DeltaV and duration comparison between the nominal and the LongComm – ATD-2 scenarios_


i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i


|Mission<br>Segment|Nominal [day]|Col3|Long LongComm<br>(ATD-2) [day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.188|0.188|
|IPA|5.760|5.843|8.000|8.083|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|18.271|18.271|
|Total<br>Mission|12.361|12.361|19.602|19.602|


|Mission<br>Segment|Nominal [m/s]|Col3|Long LongComm<br>(ATD-2) [m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|2.676|7.404|
|HP2Ins|1.280|1.280|4.255|4.255|
|ZRV2|0.423|0.423|0.473|0.473|
|Total<br>PreHP2|2.677|2.677|8.291|8.291|
|Total<br>Mission|7.092|7.092|12.706|12.706|



6.1.2.5 Alternatve Time i - Down Solutons i – ATD - 3


The ATD-3 solution uses the same process and Matlab function used for the ATD-2, with the only difference
being the time before the IPA end at which the brake starts. It was selected a lower value (12 hours) with
the intention of reducing the total duration of the manoeuvre. Figure 6.12 shows the 3D plot with the total
duration, total deltaV and InTrack target of every valid result; for this graph, the adjective “total” refers to
the braked section of the IPA, HP2 insertion and ZRV2 manoeuvres. Generally, every solution presents a
similar deltaV (between 4.3 and 3.5 m/s) and a similar total duration (between approximately 4.2 and 4.6
days).

i i



_Figure 6.12: 3D plot of the total deltaV as function of the total duration and the IPA InTrack target – ATD-3_


88


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Defining which sequence to use for the ATD-3 was simple: as shown in Figure 6.13, the result which
minimizes the duration also presents an acceptably low deltaV, which is only 0.216 m/s higher than the
minimum total deltaV.


_Figure 6.13: Selected solution for the ATD-3_


_Table 6.9 Detailed results properties - ATD-3_













|IPA Intrack<br>[km]|Braked IPA<br>duration<br>[days]|IPA DeltaV<br>[m/s]|HP2Ins<br>Duration [hr]|HP2Ins<br>DeltaV|ZRV2 DeltaV|Total DeltaV|Total time|
|---|---|---|---|---|---|---|---|
|4|4.2|1.110|5|1.922|1.209|5.905|7.108|
|4.5|4.2|1.111|5|1.902|1.186|5.863|7.108|
|5|4.2|1.111|5|1.882|1.164|5.821|7.108|
|5.5|4.2|1.112|5|1.862|1.142|5.779|7.108|
|6|4.2|1.112|5|1.842|1.119|5.738|7.108|
|6.5|4.2|1.113|2|1.960|0.914|5.650|6.983|
|7|4.2|1.113|2|1.851|0.807|5.435|6.983|
|3|4.4|1.110|4.5|1.464|0.981|5.219|7.288|
|3.5|4.4|1.111|4.5|1.466|0.989|5.229|7.288|
|4|4.4|1.111|4.5|1.467|0.997|5.240|7.288|
|4.5|4.4|1.112|4.5|1.469|1.005|5.250|7.288|
|5|4.4|1.112|4.5|1.471|1.014|5.261|7.288|
|5.5|4.4|1.112|4.5|1.473|1.022|5.272|7.288|
|6|4.4|1.113|4.5|1.475|1.031|5.283|7.288|
|6.5|4.4|1.113|4.5|1.477|1.040|5.294|7.288|


Table 6.9 reports in each row the following properties of every valid solution: InTrack target, duration and
deltaV of the IPA Brake, duration and deltaV of the HP2 insertion, deltaV for the ZRV2 manoeuvre, total
deltaV and total duration. In this case, the adjective “total” refers to the IPA + IPA brake + HP2 insertion +
ZRV2 sequence. In fact, to evaluate the total duration, 2.7 days were added: the IPA with no brake would
last 3.2 days, but since the brake is performed 12 hours before its theoretical end, the duration of this
propagation segment is just 2.7 days. To evaluate the total deltaV, 1.664 m/s were added to consider the
deltaV required to perform the first part of the IPA. It is interesting to notice that the solutions are valid only


89


_-_
_Chapter 6_ _Variant Scenarios Analysis_


for a duration of the braked IPA equal to 4.2 or 4.4 days, although the analysis was performed iterating on
the following values for the IPA_Brake target sequence:


  - InTrack target: [3:0.5: 7] km;

  Duration: [2:0.1:6] days;


As for the ATD-2, lower durations were not accepted since they produced faster propagation segments
which did not respect the InTrack limit on the 24-hours propagation after the IPA, while higher duration did
not provide a solution giving the desired InTrack target.


Figure 6.14 shows that delaying the start of the braking manoeuvre of 12 hours guarantees a lower duration
of the braking IPA segment since it starts with an InTrack value of approximately 200 km instead of the ATD2 which performed the same manoeuvre at approximately 400 km along InTrack.


_Figure 6.14: InTrack as a function of the time - ATD-3_


Table 6.10 offers a comparison between the durations of the nominal scenario and all the time-down
solutions in case of longer commissioning. Of course, the ATD-1 solution is the fastest one and guarantees
only a delay of 2.441 days with respect to the nominal scenario, but it is not considered safe for SR. The
ATD-3 recovers a few days, with a total delay of 6.14 days.


_Table 6.10: Duration comparison between the nominal and all the time-down solutions in case of a longer commissioning_



































|Mission<br>Segment|Nominal<br>[day]|Col3|LongHP1 (TD)<br>[day]|Col5|LongHP1<br>(ATD-1) [day]|Col7|LongHP1<br>(ATD-2) [day]|Col9|LongHP1<br>(ATD-3) [day]|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|10.000|10.000|10.000|10.000|10.000|10.000|
|HP1|0.188|0.188|0.188|0.188|0.188|0.188|0.188|0.188|0.188|0.188|
|IPA|5.760|5.843|10.820|10.903|3.200|3.283|8.000|8.083|6.900|6.983|
|HP2Ins|0.083|0.083|0.083|0.083|0.083|0.083|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|-|-|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|21.091|21.091|13.471|13.471|18.271|18.271|17.171|17.171|
|Total<br>Mission|12.361|12.361|22.421|22.421|14.802|14.802|19.602|19.602|18.501|18.501|


90


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Table 6.11 shows the comparison between the deltaVs of the nominal scenario and of all the time-down
solutions in case of a longer commissioning. The ATD-2 And ATD-3 require a higher deltaV since they both
include an additional manoeuvre to brake the IPA. Although the ATD-3 may seem like a good compromise
between the required deltaV and total duration, it may be classified as off-nominal for not being sufficiently
safe since it starts the brake manoeuvre 12 hours before the end of the unbraked IPA segment. This means
that in case no manoeuvre was performed SROC would cross the 200 km InTrack limit in less than 13 hours.
In conclusion, considering the safety constraint, the required deltaV and the duration, the best solution may
be the ATD-2 solution.


_Table 6.11: DeltaV comparison between the nominal and all the time-down solutions in case of a longer commissioning_


Nominal Scenario - LongComm DeltaV







































|Mission<br>Segment|Nominal<br>[m/s]|Col3|LongHP1 (TD)<br>[m/s]|Col5|LongHP1<br>(ATD-1) [m/s]|Col7|LongHP1<br>(ATD-2) [m/s]|Col9|LongHP1<br>(ATD-3)<br>[m/s]|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Comm|-|-|-|-|-|-|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|0.887|0.887|0.887|0.887|0.887|0.887|
|IPA|0.485|2.188|0.881|3.107|1.664|4.058|2.676|5.843|2.777|5.435|
|HP2Ins|1.280|1.280|1.679|1.679|2.030|2.030|4.255|4.255|1.851|1.851|
|ZRV2|0.423|0.423|0.547|0.547|0.364|0.364|0.473|0.473|0.807|0.807|
|Total<br>PreHP2|2.667|2.667|3.994|3.994|4.945|4.945|8.291|8.291|6.322|6.322|
|Total<br>Mission|7.092|7.092|8.409|8.409|9.360|9.360|12.706|12.706|10.737|10.737|


6.1.3 Longer Commissioning and HP1


The third possible deviation from the nominal scenario involves both a longer HP1 (4.5 hours) and
commissioning (10 days). The trajectory during HP1 differs from the ones in the previous case, but the
required deltaV to perform the HP1 insertion manoeuvre is the same for the longer commissioning phase.
This is the equivalent of what has been said for the longer HP1 deviation: the target of the manoeuvre is to
get SR’s semi-major axis at the end of the HP1 and this objective is met with the same manoeuvre for a
duration of both 4.5 and 13.5 hours. The semi-major axis is increased by an impulsive manoeuvre and stays
almost constant for the whole HP1 since its duration is not enough for the external disturbances,
particularly the atmospheric drag, to change it. Figure 6.15 shows the SROC’s trajectory during HP1.


91


_-_
_Chapter 6_ _Variant Scenarios Analysis_

i



_Figure 6.15: SROC’s trajectoty during HP1 for a longer commissioning and HP1_


The principal problems which arise from this scenario are the same discussed in the previous sub-section.
For this reason, the solution investigated are also the same:


  - **DeltaV-down** IPA + HP2 insertion + ZRV2 sequence which minimizes the deltaV;

  - **Time Down** : IPA + HP2 insertion + ZRV2 sequence which minimizes the duration without breaking
the 200 km InTrack constraint on a hypothetical 24-hours propagation after the IPA;

  - **Alternative time-down** :

`o` **ATD-1** : no InTrack constraint on a hypothetical 24-hours propagation after the IPA;
`o` **ATD-2** : solution composed of two parts: during the first one, the same IPA selected for ATD
1 is performed. The second part is constituted by a braking manoeuvre to slow down SROC
enough to respect the 200 km InTrack constraint on a hypothetical 24-hours propagation
after the IPA. This brake manoeuvre is performed 24 hours before the end of the ATD-1;
`o` **ATD-3** : it only differs from the ATD-2 for the time at which the brake is performed (12 hours

before the ATD-1 end instead of 24 hours);


6.1.3.1 DeltaV - Down Soluton i


Figure 6.16 shows the InTrack as a function of the time from the IPA start for the selected solution. The
same considerations made for the DD solution in case of longer commissioning can be applied here.
Actually, SROC starts the IPA at an even higher relative distance from Space Rider, since the longer HP1
causes SROC to drift a few kilometres more. Since SROC starts the IPA at a higher relative position, it also
requires a higher time to perform it in a deltaV-efficient way.


92


_-_
_Chapter 6_ _Variant Scenarios Analysis_

i



_Figure 6.16: IPA InTrack as a function of the time - LongComm&HP1 (DD)_


Table 6.12 shows that, because of the longer commissioning, HP1 and IPA, the duration of the mission is
almost doubled from 12.3 days to 23.5 days. The deltaV, instead, only increases by 21.33% with respect to
the nominal case. Because of the longer HP1, the total duration and deltaV are even higher than the ones
for the longer commissioning case, whose deltaV-down solution lasts for 23 days and required a total deltaV
of 8.245 m/s.


_Table 6.12: DeltaV and duration comparison between the nominal and the LongComm&HP1 (DeltaV-down) scenarios_


i



i



i



i



i



i



i



i



i



i



i



i



i


|Mission<br>Segment|Nominal [day]|Col3|LongComm&HP1<br>(DD) [day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.563|0.563|
|IPA|5.760|5.843|11.480|11.563|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|22.126|22.126|
|Total<br>Mission|12.361|12.361|23.456|23.456|


|Mission<br>Segment|Nominal [m/s]|Col3|LongComm&HP1<br>(DD) [m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|0.906|3.303|
|HP2Ins|1.280|1.280|2.117|2.117|
|ZRV2|0.423|0.423|0.280|0.280|
|Total<br>PreHP2|2.677|2.677|4.190|4.190|
|Total<br>Mission|7.092|7.092|8.605|8.605|



6.1.3.2 Time - Down Soluton i


The time-down solution presents the same problems as the longer commissioning time-down solution: to
respect the 200 km InTrack limit on the 24-hour propagation after the IPA, the relative velocity during the
IPA cannot be too high, thus limiting the minimum duration of the segment. Table 6.12 reports the total
deltaV and duration of this solution and the ones of the nominal scenario. This solution recovers 15 hours
and 20 minutes from the deltaV-down solution, while it requires 23.75% more deltaV than the nominal
scenario. In case this recovery in time was not considered satisfying enough, three alternative time-down
solutions were analysed.


93


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.13: DeltaV and duration comparison between the nominal and the LongComm&HP1 (Time-down) scenarios_


i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i


|Mission<br>Segment|Nominal [day]|Col3|LongComm&HP1<br>(TD) [day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.563|0.563|
|IPA|5.760|5.843|10.840|10.923|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|21.486|21.486|
|Total<br>Mission|12.361|12.361|22.816|22.816|


|Mission<br>Segment|Nominal [m/s]|Col3|LongComm&HP1<br>(TD) [m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|0.908|3.474|
|HP2Ins|1.280|1.280|2.279|2.279|
|ZRV2|0.423|0.423|0.287|0.287|
|Total PreHP2|2.677|2.677|4.361|4.361|
|Total<br>Mission<br>|7.092|7.092|8.776|8.776|



6.1.3.3 Alternatve Time i - Down Solutons i – ATD - 1


Figure 6.17 shows the results of the analysis (purple circles) and a surface interpolating them; here, the
total deltaV is shown as a function of the IPA InTrack target and the total duration. As for the previous ATD-1
analysed, the adjective “total” refers to the combination of the IPA + HP2 insertion and ZRV2 manoeuvre.
These results were obtained by iterating on the following parameters:


  - InTrack target: [2:0.5: 7] km;

  Duration: [2:0.1:6] days;

i i



_Figure 6.17: 3d plot of the results of the ATD-1 analysis_


The optimal solution was selected to reduce the total duration while also avoiding increasing too much the
deltaV. The red box in Figure 6.18 highlights the set of solutions that were considered for ATD-1: they were
selected because, although they are approximately 1 day longer than the shortest solutions, they require
about 1 m/s less.


94


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Figure 6.18: Optimal solutions – ATD-1_


Figure 6.19 shows the trend of the IPA and total duration as a function of the IPA duration for a fixed InTrack
target. As expected, the deltaV cost of the IPA decrease with the increase of its total duration since it
requires a longer IPA, thus a lower change of the kinetic energy. The total deltaV cost, although has a
decreasing trend, does not show this behaviour for every solution. This is caused by the HP2 insertion and
ZRV2 manoeuvres, whose contribution to the total deltaV has already been analysed in Sub-section 6.1.2.3.
It is probable that with a finer step on the duration of both the IPA and the HP2 insertion and of the InTrack
target of the IPA, these deltaV differences could decrease, with the total deltaV progressively decreasing
with the IPA duration for all the solutions.


_Figure 6.19: DeltaV trend - ATD-1_


Table 6.14 reports in each row the following properties of every valid solution: InTrack target, duration and
deltaV of the IPA, duration and deltaV of the HP2 insertion, deltaV for the ZRV2 manoeuvre, total deltaV
and total duration of the IPA + HP2 insertion + ZRV2 sequence. Finally, it also shows, in the last column, the
minutes which would take SROC to cross the 200 m InTrack position if its orbit was propagated after the IPA


95


_-_
_Chapter 6_ _Variant Scenarios Analysis_


instead of performing the HP2 insertion. The row highlighted in orange is the solution with the lowest
duration, while the one in yellow is the selected one. As seen for the longer commissioning’s ATD-1, SROC
crosses the InTrack 200 m limit in less than one hour, thus not achieving the desired safety for Space Rider.


_Table 6.14: Detailed results for the ATD-1 solution_



















|IPA Intrack<br>[km]|IPA<br>Duration<br>[days]|IPA DeltaV<br>[m/s]|HP2Ins<br>Duration<br>[hr]|HP2Ins<br>DeltaV|ZRV2<br>DeltaV|Total<br>DeltaV|Total time|Time to<br>200 [min]|Time to<br>1000 [min]|
|---|---|---|---|---|---|---|---|---|---|
|6.5|2.3|2.243|8|4.034|4.090|10.367|2.633|58|57|
|7|2.3|2.242|8|4.022|4.080|10.344|2.633|59|58|
|3|2.5|2.091|8|3.683|0.621|6.395|2.833|46|44|
|3.5|2.5|2.091|8|3.671|0.613|6.375|2.833|46|45|
|4|2.5|2.090|8|3.660|0.604|6.354|2.833|47|46|
|4.5|2.5|2.089|2.5|3.751|0.386|6.227|2.604|48|47|
|5|2.5|2.088|2|3.627|0.337|6.053|2.583|48|47|
|5.5|2.5|2.088|2|3.507|0.289|5.883|2.583|49|48|
|6|2.5|2.087|2|3.386|0.287|5.760|2.583|50|49|
|6.5|2.5|2.086|2|3.266|0.333|5.685|2.583|50|49|
|7|2.5|2.085|2|3.146|0.410|5.641|2.583|51|50|
|5|3.2|1.689|8|3.258|2.626|7.573|3.533|60|59|
|5.5|3.2|1.688|8|3.247|2.616|7.551|3.533|61|60|
|6|3.2|1.688|8|3.235|2.607|7.530|3.533|62|61|
|6.5|3.2|1.687|8|3.224|2.598|7.509|3.533|63|62|
|7|3.2|1.687|8|3.212|2.588|7.487|3.533|63|62|
|3|3.4|1.612|3.5|2.822|0.218|4.652|3.546|49|47|
|3.5|3.4|1.611|3.5|2.779|0.244|4.635|3.546|49|48|
|4|3.4|1.611|3.5|2.736|0.274|4.621|3.546|50|49|
|4.5|3.4|1.610|3.5|2.694|0.307|4.611|3.546|51|50|
|5|3.4|1.610|3.5|2.651|0.342|4.602|3.546|52|51|
|5.5|3.4|1.609|5|2.752|0.269|4.631|3.608|53|51|
|6|3.4|1.609|5|2.728|0.287|4.624|3.608|53|52|
|6.5|3.4|1.608|5|2.704|0.306|4.618|3.608|54|53|
|7|3.4|1.607|5|2.680|0.325|4.613|3.608|55|54|
|7|3.9|1.443|8|1.776|4.282|7.501|4.233|72|71|
|4|4.1|1.392|8|2.903|1.694|5.989|4.433|63|61|
|4.5|4.1|1.391|8|2.892|1.685|5.969|4.433|63|62|
|5|4.1|1.391|8|2.881|1.676|5.948|4.433|64|63|
|5.5|4.1|1.391|8|2.870|1.667|5.928|4.433|65|64|
|6|4.1|1.390|8|2.859|1.658|5.907|4.433|66|65|
|6.5|4.1|1.390|8|2.848|1.649|5.887|4.433|67|66|
|7|4.1|1.389|8|2.837|1.640|5.867|4.433|68|66|
|3|4.3|1.347|7.5|1.914|0.765|4.026|4.613|51|49|
|3.5|4.3|1.347|7.5|1.914|0.770|4.031|4.613|52|50|
|4|4.3|1.346|7.5|1.915|0.775|4.037|4.613|53|51|
|4.5|4.3|1.346|7.5|1.916|0.781|4.043|4.613|54|52|
|5|4.3|1.345|6|1.773|0.929|4.047|4.550|55|53|
|5.5|4.3|1.345|6|1.773|0.934|4.052|4.550|56|54|
|6|4.3|1.344|6|1.773|0.939|4.056|4.550|56|55|
|6.5|4.3|1.344|6|1.773|0.945|4.061|4.550|57|56|
|7|4.3|1.344|6|1.772|0.950|4.066|4.550|58|57|
|5.5|4.8|1.245|8|1.769|3.332|6.346|5.133|74|73|
|6|4.8|1.245|8|1.758|3.323|6.325|5.133|75|74|
|6.5|4.8|1.244|8|1.747|3.313|6.304|5.133|76|75|
|7|4.8|1.244|8|1.736|3.304|6.284|5.133|77|76|
|3|5|1.214|8|2.742|1.003|4.958|5.333|64|62|
|3.5|5|1.214|8|2.731|0.994|4.939|5.333|65|63|
|4|5|1.213|8|2.721|0.985|4.919|5.333|66|64|
|4.5|5|1.213|8|2.710|0.977|4.900|5.333|67|65|
|5|5|1.212|8|2.700|0.968|4.880|5.333|68|66|
|5.5|5|1.212|8|2.690|0.959|4.861|5.333|69|67|


96


_-_
_Chapter 6_ _Variant Scenarios Analysis_

|6|5|1.212|2|2.902|0.640|4.753|5.083|70|68|
|---|---|---|---|---|---|---|---|---|---|
|6.5|5|1.211|2|2.782|0.554|4.547|5.083|71|69|
|7|5|1.211|2|2.662|0.484|4.356|5.083|72|70|
|7|5.3|1.172|8|2.486|4.528|8.187|5.633|15|13|
|7|5.5|1.144|8|0.754|4.220|6.118|5.833|83|81|
|5|5.7|1.120|8|1.850|2.591|5.561|6.033|77|76|
|5.5|5.7|1.120|8|1.839|2.581|5.541|6.033|79|77|
|6|5.7|1.119|8|1.829|2.572|5.520|6.033|80|78|
|6.5|5.7|1.119|8|1.818|2.563|5.500|6.033|81|79|
|7|5.7|1.119|8|1.808|2.554|5.480|6.033|82|80|
|3|5.9|1.100|2.5|2.655|0.397|4.151|6.004|66|65|
|3.5|5.9|1.100|8|2.647|0.427|4.173|6.233|68|66|
|4|5.9|1.099|2|2.626|0.287|4.013|5.983|69|67|
|4.5|5.9|1.099|2|2.507|0.273|3.879|5.983|70|68|
|5|5.9|1.099|2|2.388|0.309|3.796|5.983|71|69|
|5.5|5.9|1.098|2|2.270|0.382|3.750|5.983|72|70|
|6|5.9|1.098|2|2.152|0.475|3.725|5.983|73|72|
|6.5|5.9|1.098|3.5|2.520|0.273|3.890|6.046|75|73|



Table 6.15 shows a comparison between the ATD-1 solution and the nominal scenario: most of the delay is
recovered and the duration of the whole mission is just 3 days higher. Even the total required deltaV,
although 2.9 m/s higher than the nominal one, is well below the 20 m/s limit.


_Table 6.15: DeltaV and duration comparison between the nominal and the LongComm&HP1 (ATD-1) scenarios_


i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i


|Mission<br>Segment|Nominal [day]|Col3|LongComm&HP1<br>(ATD-1) [day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.563|0.563|
|IPA|5.760|5.843|3.400|3.546|
|HP2Ins|0.083|0.083|0.146|0.146|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|14.109|14.109|
|Total<br>Mission|12.361|12.361|15.439|15.439|


|Mission<br>Segment|Nominal [m/s]|Col3|LongComm&HP1<br>(ATD-1) [m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|1.610|4.602|
|HP2Ins|1.280|1.280|2.651|2.651|
|ZRV2|0.423|0.423|0.342|0.342|
|Total<br>PreHP2|2.677|2.677|5.489|5.489|
|Total<br>Mission|7.092|7.092|9.904|9.904|



6.1.3.4 Alternatve Time i - Down Solutons i – ATD - 2


Figure 6.20 shows the total deltaV as a function of the total duration and the IPA InTrack target; the term
“total deltaV” refers to the deltaV required by the IPA brake + HP2 insertion è ZRV2 manoeuvres, while
“total time” refers to the duration of the propagation segments of the braked IPA and the HP2 insertion.
These results were obtained by iterating on the following parameters:


  - IPA InTrack target: [5, 0.5, 7] km;

  Braked IPA Duration [4.5:0.1:6.5] days;


The range of possible duration of the braked part of the IPA was decreased because, as it has been seen
form the longer commissioning’s ATD-2, it is not necessary to evaluate too low duration since they produce
a too fast IPA which would not respect the 200 m InTrack limit on a hypothetical successive propagation
segment. As expected, all the valid solutions are in a small interval of long total durations, approximately
from 5.88 to 6 days.


97


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Figure 6.20: 3D plot of the results of the ATD-2 analysis_


Figure 6.21 shows the total deltaV as a function of the total time. For this ATD-2, defining the optimal result
was a simple task, since the one with the shortest duration is also the one with the lowest deltaV. This may
seem counterintuitive since, usually the solutions present a total deltaV trend decreasing with the total
duration. As reported in Table 6.16, the acceptable solutions are obtained only for a duration of the braked
segment of the IPA of 5.8 days, so the differences in the total durations and deltaV are caused by the
different combinations of IPA InTrack targets and HP2 insertion durations. For this reason, the analysis of
the deltaV trend, which considers the effect of different IPA duration, cannot be applied here.


_Figure 6.21: Total DeltaV as function of the total duration for the ATD-2 analysis_


It is noted that each row in Table 6.16 refers to one valid ATD-2 solution, with the same column already
described for the previous ATD-2 solution: InTrack target, duration and deltaV of the IPA Brake, duration and
deltaV of the HP2 insertion, deltaV for the ZRV2 manoeuvre, total deltaV and total duration. The adjective
“total” refers to the IPA + IPA brake + HP2 insertion + ZRV2 sequence. In fact, to evaluate the total duration,
2.4 days were added: the IPA with no brake would last 3.7 days, but since the brake is performed 24 hours


98


_-_
_Chapter 6_ _Variant Scenarios Analysis_


before its theoretical end, the duration of this propagation segment is just 2.4 days. To evaluate the total
deltaV, 1.610 m/s were added to consider the deltaV required to perform the first part of the IPA. The
selected solution is the row highlighted in yellow.


_Table 6.16: Detailed results for the ATD-2 solution_













|IPA Intrack<br>[km]|Braked IPA<br>Duration<br>[days]|IPA DeltaV<br>[m/s]|HP2Ins<br>Duration [hr]|HP2Ins<br>DeltaV|ZRV2 DeltaV|Total DeltaV|Total time|
|---|---|---|---|---|---|---|---|
|3.5|5.8|0.931|5|4.533|1.102|8.176|8.408|
|4|5.8|0.932|5|4.513|1.081|8.135|8.408|
|4.5|5.8|0.932|5|4.493|1.060|8.094|8.408|
|5|5.8|0.932|5|4.473|1.039|8.054|8.408|
|5.5|5.8|0.933|5|4.453|1.018|8.014|8.408|
|6|5.8|0.933|2|4.530|0.837|7.909|8.283|
|6.5|5.8|0.933|2|4.418|0.744|7.705|8.283|
|7|5.8|0.934|2|4.306|0.661|7.510|8.283|


Figure 6.22 shows the InTrack during the whole IPA as a function of the time from its start. Most of the
relative distance is recovered in 2.4 days during the first part of the IPA, while the remaining 370 km are
covered in 5.8 days. It is, of course, a great downgrade with respect to the ATD-1, but it is necessary to
increase the safety of the mission to an acceptable level.


_Figure 6.22: InTrack as a function of the time - ATD-2_


Finally, Table 6.16 shows the comparison between the durations and the deltaV of the ATD-2 and the
nominal scenario. Here, the properties of the IPA refer to it as a whole, including both the unbraked and
braked parts.


99


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.17: DeltaV and duration comparison between the nominal and the LongComm&HP1 (ATD-1) scenarios_


i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i



i i


|Mission<br>Segment|Nominal [day]|Col3|LongComm&HP1<br>(ATD-2) [day]|Col5|
|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|
|HP1|0.188|0.188|0.563|0.563|
|IPA|5.760|5.843|8.200|8.283|
|HP2Ins|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|18.846|18.846|
|Total<br>Mission|12.361|12.361|20.176|20.176|


|Mission<br>Segment|Nominal [m/s]|Col3|LongComm&HP1<br>(ATD-2) [m/s]|Col5|
|---|---|---|---|---|
|Comm|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|
|IPA|0.485|2.188|2.543|7.510|
|HP2Ins|1.280|1.280|4.306|4.306|
|ZRV2|0.423|0.423|0.661|0.661|
|Tota<br>PreHP2|2.677|2.677|8.397|8.397|
|Total<br>Mission|7.092|7.092|12.811|12.811|



6.1.3.5 Alternatve Time i - Down Solutons i – ATD - 3


Figure 6.23 shows the total deltaV as a function of the IPA InTrack target and the total duration. The
meaning of the adjective “total” in both this graph and the following graphs and tables are the same used
for the same graphs and tables in the previous sub-section. This analysis was performed considering the
following vectors:


  - IPA InTrack target: [5, 0.5, 7] km;

  Braked IPA Duration: [3:0.1:6.5] days;


A higher number of valid solutions than for the ATD-2 was obtained, although only for a total number of 3
braked IPA durations.

i i



_Figure 6.23: 3D plot of the results of the ATD-3 analysis_


100


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Figure 6.24 shows the total deltaV as a function of the total duration. The selected solution in the red box
both minimizes the deltaV and the duration. Again, the trend of the total duration is different from the
expected one, with the total deltaV not decreasing with the total duration.


_Figure 6.24: Total DeltaV as function of the total duration for the ATD-3 analysis_


As shown in Table 6.18, the trend of the IPA brake deltaV is to increase with the duration, with the
contributions of the HP2 insertion and ZRV2 varying even more in the final deltaV. The discrepancy between
the data reported in the table and the expected behaviour could probably be eliminated by using finer steps
for the duration and InTrack target values used for the analysis. However, this would have increased the
analysis time too much and it would not have been possible to perform analysis this fine on all the possible
variant scenarios. Moreover, this analysis gives more conservative results: with finer steps, the total deltaV
and duration should not significantly change, and slowly better results should be obtained.


_Table 6.18: Detailed results for the ATD-3 solution_



















|IPA<br>Intrack<br>[km]|IPA<br>Duration<br>[days]|IPA<br>DeltaV<br>[m/s]|HP2Ins<br>Duration<br>[hr]|HP2Ins<br>DeltaV|ZRV2<br>DeltaV|Total<br>DeltaV|Total<br>time|
|---|---|---|---|---|---|---|---|
|6|3.5|1.021|2|1.992|0.673|5.296|6.483|
|6.5|3.5|1.022|2|1.880|0.584|5.095|6.483|
|7|3.5|1.022|2|1.769|0.510|4.910|6.483|
|3.5|3.7|1.021|6|1.312|1.287|5.230|6.850|
|4|3.7|1.022|6|1.313|1.294|5.239|6.850|
|4.5|3.7|1.022|6|1.315|1.301|5.248|6.850|
|5|3.7|1.023|6|1.317|1.309|5.258|6.850|
|5.5|3.7|1.023|6|1.319|1.316|5.268|6.850|
|6|3.7|1.024|6|1.321|1.323|5.278|6.850|
|6.5|3.7|1.024|6|1.323|1.331|5.288|6.850|
|7|3.7|1.025|6|1.325|1.338|5.298|6.850|
|3|4.4|1.023|5|2.161|0.614|5.409|7.508|
|3.5|4.4|1.024|5|2.141|0.595|5.369|7.508|
|4|4.4|1.024|2.5|2.127|0.530|5.291|7.404|
|4.5|4.4|1.024|2|2.062|0.449|5.145|7.383|


101


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Figure 6.25 shows SROC’s InTrack as a function of its duration: more than 1200 km are covered during the
first part of the IPA, while to cover the remaining relative distance 3.5 days are required.


_Figure 6.25: InTrack as a function of the time - ATD-3_


Table 6.19 and Table 6.20 compare the duration and deltaV of the nominal scenario and all the time-down
solutions. Generally, the same conclusion made for the longer commissioning analysis can be applied here:
the shortest option is the ATD-1, but it is not safe enough. The TD and ATD-2 solution meet the safety
constraints of the project; however, they present a higher total duration (respectively 22.816 and 20.176
days). The ATD-2 is shorter than 2 days and 15 hours and 22 minutes, however, since it includes an
additional manoeuvre to slow down the IPA, it costs 12.811 m/s instead of 9.904 m/s. Finally, the ATD-3
could be a good compromise between these two options, since it is even shorter and requires a 10.212 m/s
deltaV. However, this manoeuvre is performed 12 hours before the end of the unbraked IPA, which means
that if no braking manoeuvre was performed, SROC would cross the 200 m InTrack limit in approximately 13
hours. For this reason, the solution could be considered not safe enough. The final choice between the TD
and ATD-2 could be the presence of other variant mission segments: in case any of them increased the total
deltaV even more, the additional cost of the ATD-2 could not be worth as much as the time recovered with
respect to the TD solution.


_Table 6.19:Duration comparison between the nominal and all the time-down solutions in case of a longer commissioning and HP1_


Nominal Scenario - LongComm&HP1 Duration









































|Mission<br>Segment|Nominal<br>[day]|Col3|LongComm&<br>HP1 (TD) [day]|Col5|LongComm&<br>HP1 (ATD-1)<br>[day]|Col7|LongComm&<br>HP1 (ATD-2)<br>[day]|Col9|LongComm&<br>HP1 (ATD-3)<br>[day]|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Comm|5.000|5.000|10.000|10.000|10|10|10|10|10.000|10.000|
|HP1|0.188|0.188|0.563|0.563|0.563|0.563|0.563|0.563|0.563|0.563|
|IPA|5.760|5.843|10.840|10.923|3.4|3.55|8.2|8.28|6.400|6.483|
|HP2Ins|0.083|0.083|0.083|0.083|0.146|0.146|0.083|0.083|0.083|0.083|
|ZRV2|-|-|-|-|-|-|-|-|-|-|
|Total<br>PreHP2|11.031|11.031|21.486|21.486|14.109|14.109|18.846|18.846|17.046|17.046|
|Total<br>Mission|12.361|12.361|22.816|22.816|15.439|15.439|20.176|20.176|18.376|18.376|


102


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.20: DeltaV comparison between the nominal and all the time-down solutions in case of a longer commissioning_


Nominal Scenario - LongComm&HP1 DeltaV

##### t


i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i


##### t

i



|Mission<br>Segment|Nominal<br>[m/s]|Col3|LongComm&<br>HP1 (TD)<br>[m/s]|Col5|LongComm&<br>HP1 (ATD-1)<br>[m/s]|Col7|LongComm&<br>HP1 (ATD-2)<br>[m/s]|Col9|LongComm&<br>HP1 (ATD-3)<br>[m/s]|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Comm|-|-|-|-|-|-|-|-|-|-|
|HP1|0.489|0.489|0.887|0.887|0.887|0.887|0.887|0.887|0.887|0.887|
|IPA|0.485|2.188|0.908|3.47|1.610|4.6|2.543|7.51|2.632|4.910|
|HP2Ins|1.280|1.280|2.279|2.279|2.651|2.651|4.306|4.306|1.769|1.769|
|ZRV2|0.423|0.423|0.287|0.287|0.342|0.342|0.661|0.661|0.510|0.510|
|Total<br>PreHP2|2.667|2.667|4.361|4.361|5.489|5.489|8.397|8.397|5.797|5.797|
|Total<br>Mission|7.092|7.092|8.776|8.776|9.904|9.904|12.811|12.811|10.212|10.212|

##### 6.2 Variant Events Afer HP2 t

The main variant segments that take place after the IPA rendezvous are the possibility of a second
inspection cycle and the demand to perform an additional manoeuvre during the EMP phase to avoid a
potential collision with Space Rider. Longer durations for both HP2 and HP3 have also been considered,
although only their results are reported (see Section 6.3), since their analyses only required changing the
input duration given to the same Matlab function described in Section 4.3 and they did not affect the
previous or the successive segments.


6.2.1 Second Observaton cycle i


In Section 5.3 it was described the WSE design process. As mentioned at the end, the total actual
observation time during which SROC can take pictures of SR is relatively low (about 37 minutes). In case
during successive design iterations of the project this value was not considered high enough, a second
observation cycle would be necessary. For this reason, a second observation cycle was considered.
##### t

i



_Figure 6.26: Second OPA after the first free flight_


103


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Figure 6.26 shows that the second OPA rendezvous (in green) starts after the first free flight (in yellow).
After that, a second WSE insertion, a second inspection phase and a second free flight are performed. Since
the second OPA starts with a different relative position and relative from SR than the first one, it is
necessary to evaluate again both the OPA and WSE insertion manoeuvres. The goal of the analysis was to
set a new inspection phase that was as similar as possible to the first one, so it was selected the following
inspection:


  - Same input geometrical parameters

  Similar actual observation time: the number of intervals is the same and their duration is similar,
although the total duration for the second inspection is slightly more (46 minutes in total)

  Almost the same duration for the free flight (8.058 hours instead of 8.060 hours)


Figure 6.27 shows a comparison of the range as a function of the time for both inspections. Although the
second one presents a higher maximum range, it can be seen that the number of intervals of actual
observation, their duration, and the time at which they take place are almost the same.


_Figure 6.27: Comparison between the range as a function of the time for the first (left) and second(right) inspection_


Figure 6.28 compares the RIC components during both inspections: the CrossTrack and Radial components
are very close, while the InTrack reaches a lower minimum from the fourth hour of the propagation onward
(which explains the higher ranges shown in Figure 6.27).


_Figure 6.28: Comparison between the range as a function of the time for the first (left) and second(right) inspection_


104


_-_
_Chapter 6_ _Variant Scenarios Analysis_


Since at the end of the second inspection sequence SROC’s relative position and velocity differ from the first
one, the HP3 insertion deltaV and duration may differ from the nominal observe & retrieve scenario. For
this reason, the HP3 insertion and ZRV3 were re-evaluated for this different scenario. Figure 6.29 shows
SROC’s trajectory during the HP3 insertion, while Table 6.21 reports the deltaV and duration of both the
nominal and this variant scenario. The deltaV cost of the second inspection differs from the first one: the
cost of the WSE insertion is similar, with the second one requiring 0.029 m/s more, while the deltaV of the
second OPA manoeuvre is significantly lower (0.095 m/s instead of 0.226 m/s). The manoeuvres after the
inspection phase are identical in duration and very similar in the deltaV cost, probably because both the
HP3 insertion manoeuvres are performed after similar WSEs and free flight segments.


_Figure 6.29: HP3 insertion after the second inspection cycle_


_Table 6.21: DeltaV and duration comparison between the nominal and the 2 Inspections scenarios_











|Mission<br>Segment|Nominal [day]|2 Inspections<br>[day]|
|---|---|---|
|OPA - Cycle 1|0.167|0.167|
|Inspection +<br>Free Flight -<br>Cycle 1|0.669|0.669|
|OPA - Cycle 2|-|0.171|
|Inspection +<br>Free Flight -<br>Cycle 2|-|0.669|
|HP3Ins|0.113|0.113|
|ZRV3|-|-|
|Total Mission|12.361|13.201|


6.2.2 End of Mission Phase Analysis


|Mission<br>Segment|Nominal [m/s]|2 Inspections<br>[m/s]|
|---|---|---|
|OPA - Cycle 1|0.266|0.266|
|WSE Insertion -<br>Cycle 1|0.192|0.192|
|OPA - Cycle 2|-|0.095|
|WSE Insertion -<br>Cycle 2|-|0.221|
|HP3Ins|0.221|0.208|
|ZRV3|0.438|0.421|
|Total Mission<br>|7.092|7.377|



For the Observe scenario, after the completion of the inspection cycle, SROC is free to drift away from Space
Rider. Since its ballistic coefficient is inferior to Space Rider’s, SROC’s orbit height decreases faster, which
means that its orbital period becomes shorter. This may lead to an unsafe situation where SROC approaches
SR from behind until a point where SROC InTrack is null; this point will be referred to as Encounter Point (EP)
from here on out. Before proceeding with this analysis, it is reminded that in the STK scenario, SR’s orbit is
controlled, thus the effects of the drag are not considered. At this moment, it is unknown if such a fine orbit
control will be applied, although it is more probable that SR will not control its semi-major axis for the
whole mission, rather it will perform one or more manoeuvre to increase it and restore it to the initial
value. Considering SR continuously controlled is, however, a more conservative approach because it


105


_-_
_Chapter 6_ _Variant Scenarios Analysis_


considers the highest difference between SROC and Space Rider’s semi-major axis, which means the highest
difference in the two orbital periods, thus the fastest time to get to the EP.


In the nominal Observe scenario, the orbit SROC orbit was propagated until the EP. Figure 6.30 reports the
evolution of the SROC’s range as a function of the UTC time: the first relative maximum takes place after the
end of the HP1. After that, the successive relative minimum happens during the inspection cycle; next,
SROC’s range increases until it reaches a relative maximum approximately on 29 December 2024. This is the
moment when angle 𝜙, which is the difference between the true anomaly of the two spacecrafts, is 180
degrees. From that point onwards, the range decreases since 𝜙 increases even more until another relative
minimum is reached again. Figure 6.31 zooms on all the relative minimums found by the analysis, which
propagated SROC until May 14 [th] . After the first minimum, the other relative minimums progressively
increase because SROC’s semi-major axis is continuously decreased by the atmospheric drag. The time
intervals between each relative minimum decrease with the time because SROC orbital period increases.


_Figure 6.30: SROC’s range as a function of the time_


_Figure 6.31: SROC’s range as a function of the time - zoom on the minimum ranges_


The first relative minimum is characterized by a 14.787 km range and only a radial separation of 7.734 km. It
is important to notice that the EP takes place on 18 Jan 2025 at 11:20 UTCG which is more than two months
after the end of the inspection cycle (13 Nov 2024 at 01:31 UTCG). Considering that the whole SR mission
should take a maximum of two months to be completed, at the time of the virtual EP the mission would be
completely over. However, three possible solutions to guarantee a minimum radial separation at the EP (20


106


_-_
_Chapter 6_ _Variant Scenarios Analysis_


km) or to further delay it were analysed to define the best option deltaV and safety-wise in case more
assurance is required. Since the EP should not take place during a nominal mission, the results of this
analysis were not considered in the nominal scenario.


6.2.2.1 Hohmann Manoeuvre


The first option envisages a Hohmann manoeuvre shortly after the end of the observation cycle. Its
objective is to guarantee a radial separation of 20 km after its completion. To simulate the manouvre the
following sequence was created:


  “ToApogee”: a propagation segment that ends when SROC is at its apogee;

  - “Change Radius of Periapsis”: a target sequence that includes a manoeuvre segment followed by a
propagation one which propagates until SROC reaches its perigee. The control parameters of the
differential corrector are the thrust vectors of the manoeuvre segment, while the objective is
SROC’s radius of periapsis at the end of the propagation;

  - “Circularize”: this target sequence is composed of only a manoeuvre segment which is used to
reach the desired result of the differential corrector: a null eccentricity;


After defining the sequence in STK, it is necessary to set the desired value for the radius of periapsis. Figure
6.32 shows how the semi-major axis (black), the radius of periapsis (green), the position vector magnitude
(light blue) and eccentricity (purple) vary for SR. The image considers only two hours of the whole
propagation time, but the trend is similar for the whole mission. Because of the gravitational field
disturbances, the eccentricity of SR varies from 10 [-4] to 3·10 [-3] every orbit. When the satellite is at the apogee
(red box) the eccentricity is almost null, so the actual position vector magnitude is less than 1 km more than
the semi-major axis. Instead, when SR is at the perigee (yellow box), the eccentricity is higher, thus
obtaining a radius of periapsis equal to 6758.6 km which is sensibly less than the semi-major axis.


The propagation of both SR and SROC orbits cannot be performed with a precision high enough to
guarantee that the exact moment at which the EP will actually happen is the same as the simulated one. For
this reason, the desired value for SROC’s radius of periapsis was set to 20 km less than the minimum SR’s
radius of periapsis.


_Figure 6.32: several Keplerian elements during approximately two SR's orbits_


Figure 6.33 shows how SROC’s semi-major axis and range from the Earth’s center vary before and after the
Hohmann sequence. The semi-major axis decreases in two different moments: at first, after the radius of
periapsis reduction, then, after the orbit is circularized. It can also be seen that the position vector
magnitude varies similarly to SR.


107


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Figure 6.33: SROC semi-major axis and position vector magnitude before and after the manoeuvre_


Figure 6.34 shows that SROC’s range from SR as a function of the time; the red box highlights how the slope
of the curve greatly increases after the completion of the Hohmann manoeuvre since it moves SROC in a
lower orbit. This causes the EP to take place in less time, on 30 Nov 2024. As shown in Figure 6.35; the
minimum range is reached at the first EP and it is equal to 32.25 km, while the minimum radial separation is
24.24 km and it is reached on 13 Dec 2024.


_Figure 6.34: SROC’s range as a function of the time considering the Hohmann manoeuvre_


_Figure 6.35: SROC’s range as a function of the time considering the Hohmann manoeuvre - zoom on the minimum ranges_


The costs of the two manoeuvres are the following:


  - Radius of apoapsis decrease: 5.446 m/s;

  Circularization: 16.202 m/s


108


_-_
_Chapter 6_ _Variant Scenarios Analysis_


The total deltaV is 21.648 m/s which is more than the total maximum deltaV allocated for the mission. In
conclusion, the Hohmann manoeuvre was considered not feasible for its excessive deltaV cost.


6.2.2.2 CAM near the EP


The second option is a CAM performed 1 day before the envisaged EP. The goal of the CAM is to set a
minimum 20 km radial separation between SR and SROC. To achieve this goal the following segments were
added after the free flight:


  “PropagateToEP”: it is a propagation segment which propagates until SROC reaches the EP; this
condition is evaluated in STK as the moment when the satellite crosses SR’s Radial – CrossTrack
plane;

  - “Backward 1 Day”: the type of this segment is backward sequence. All the segments contained
inside of it are propagated backwards: this means that the initial state is actually the last, in time.
Inside this sequence there is a propagation segment which stop after one day; by doing so, SROC
trajectory is propagated to 1 day before the EP;

  “CAM”: this segment is a target sequence, which contains a manoeuvre and a propagation that
stops when the EP is reached. The differential corrector is set to achieve a desired Radial value using
the manoeuvre thrust as the control parameter.


Since the minimum acceptable radial separation is 20 km, this value was set as the desired result of the
CAM target sequence. Figure 6.36 shows that the radial separation is almost 20 km (18.965 km) at the EP.


_Figure 6.36: Radial separation at the EP_


However, it is important to note that the deltaV required to guarantee a 20 km radial separation between
SROC and SR may differ from the case analysed, because the disturbances to the eccentricity described in
Sub-section 6.2.2.1 may change their heights at the EP. For this reason, several runs where tested to assess
the deltaV cost for different radial separations; the results of this analyses are report in Table 6.22. For
lower values the deltaV required is compatible with the deltaV available for the mission (3.868 m/s for a 20
km radial separation), but for higher values the deltaV is too high: for example, to achieve a 30 km radial
separation a 9.717 m/s deltaV is required. Since it is not possible to assess with total accuracy the state of
the satellites at the EP, it would make sense to consider a higher radial separation than 20 km. However, as
reported in the table, this causes the deltaV cost to greatly increase to non-acceptable values.


109


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.22: DeltaV cost for different radial separation values_

|Radial Separation at the EP [km]|DeltaV cost [m/s]|
|---|---|
|15|2.265|
|20|3.868|
|25|6.305|
|30|9.717|
|40|14.656|



6.2.2.3 Semi - Major Axis Increase Manoeuvre


The last option evaluated was to perform a semi-major increase manoeuvre to increase the orbital period of
SROC, thus delaying the EP. For the sake of this analysis, it is not useful to use the RIC reference system to
measure the relative position of SROC, since when the satellite is far away from SR the assumption of small
relative position vector magnitude compared to the chief position vector magnitude does not hold up. For
this reason, the angle between SROC and SR’s position vectors, called 𝜙, was used as a reference for the
relative position between the two satellites. Figure 6.37 shows the angle between SR and SROC’s normal to
the orbital plane; since its value is almost close to zero, it can be assumed that the two orbits are co-planar
and that the angle 𝜙 lays on this plane.


_Figure 6.37: angle between the two orbital planes as a function of the time_


Figure 6.38 shows the 𝜙 angle seen in the orbital plane. This angle was created in STK using the analysis
workbench tool, which evaluates the angle between 0 and 180 degrees, which means that the angle is not
defined by any direction. The following STK segments were added to study this manoeuvre:


  - “EMPProp1”: it propagates SROC’s trajectory until it is met a user-defined values of 𝜙, which it was
set to 175 degrees for this analysis;

  “SMA Increase”: this target sequence includes a propagation and a manoeuvre segment (in this
order); the propagation segment stops at the perigee: by performing the successive manoeuvre
there, an increase of the apoapsis is obtained. The desired value of the differential corrector is the
semi-major axis, and the control parameter is SROC’s trust vector along the velocity direction.

  “EMPProp2”: this propagation segment propagates until a user-defined epoch. For this analysis, it
was set to more than three months after the end of the free flight (13 Feb 2025 00:00);

  “PropToEP”: this propagation segment propagates SROC’s trajectory until the EP;


110


_-_
_Chapter 6_ _Variant Scenarios Analysis_


These segments are set and run by a Matlab function, which iterates on a vector of user-defined radius of
semi-major axis increases and selects the first one valid.; since the vector contains increasing values, the
first valid one is also the less deltaV-consuming. To set the desired values for the differential corrector, the
analysed semi-major axis increase is added to the semi-major axis at the epoch of the manoeuvre. To be
considered valid, every iteration must stay above a threshold 𝜙 value (for this analysis it was set to 5
degrees) until the end of the “EMPProp2” segment. Finally, the last propagation segment is used to define
when evert valid solution reaches the EP. In conclusion, the Matlab code lets the user investigate which
apoapsis increase manoeuvre guarantees that SROC will stay above a certain 𝜙 values until a desired epoch.
Another value that the user can define is the 𝜙 at which the phasing manoeuvre starts; different values
could be considered to investigate the best moment to perform a less deltaV-consuming manoeuvre, or to
study other variant scenarios which envisage a specific time window to manoeuvre.


_Figure 6.38:_ 𝜙 _angle_


For this analysis, the following vector of apoapsis increase values was used: [5:0.01:8] km. The first solution
was found at 5.600 km, which increases the semi-major axis to 6777.77 km for a deltaV cost equal to 3.112
m/s. Figure 6.39 and Figure 6.40 show the evolution of 𝜙 as a function of the time: in the first picture, it can
be seen that the rate at which 𝜙 increases is noticeably slowed down after the manoeuvre (highlighted in
the red box). Instead, the second picture, which does not consider the semi-major axis increase manoeuvre,
shows how the 𝜙 rate increases with the time, until the EP is reached on 18 Jan 2025. Instead, by
performing the manoeuvre, the EP does not take place until 13 February 2025 23:44 UTCG. Figure 6.41
shows the range as a function of the time: again, after the semi-major axis increase manoeuvre, the range
rate decreases. Figure 6.42 zooms on the last hours before the EP, where the range between SROC and SR
would only be 12.700 km.


Since the deltaV required is acceptable and the option does not envisage any additional operations in the
proximity of SR, this option was picked for the variant EMP scenario.


111


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Figure 6.39:_ 𝜙 _as a function of the time if the manoeuvre is performed_


_Figure 6.40:_ 𝜙 _as a function of the time if no manoeuvre is performed_


_Figure 6.41: Range as a function of the time if the manoeuvre is performed_


112


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Figure 6.42: Range as a function of the time - zoom on the final hours before the EP_

##### 6.3 Variant Scenarios Results Summary


Now that the single variant mission segments have been described, it is possible to study how the
occurrence of one or more of them affect the mission. In particular, it is analysed if every variant scenario
preserves the following nominal properties:


  - Total deltaV less than 20 m/s;

  Total duration less than 30 days;

  IPA safe with respect to SR: this means that after the segment, if no additional manoeuvre is
performed, SROC propagates its orbit without getting closer to SR of less than 200 m along the
InTrack direction for at least 24 hours;


These three properties have been analysed for every possible MCS; since the total number of all the
possibilities considered is very high, all the analysed cases have been divided into four tables to simplify
their browsing:


  - Table 6.23: refers to all the possible variants for the Observe&Retrieve scenario with a nominal
duration for both HP2 and HP3;

  - Table 6.24: reports the results of all the possible variants for the Observe scenario considering a
nominal duration for the HP2;

  - Table 6.25: reports the results of all the possible variants that present a longer HP2 and HP3 (both
lasting 13.5 hours instead of 4.5) for the Observe&Retrieve scenario;

  Table 6.26: reports the results of all the possible variants that present a longer HP2 (lasting 13.5
hours) for the Observe scenario;


Each row in these tables refers to a different MCS and it is highlighted in two possible colours: green if all
the constraints are satisfied, red if at least one of them is not. It is noted that all the Observe scenarios’
variant MCSs consider an additional manoeuvre during the EMP and that the values for the deltaV and the
duration include the margins. It is interesting to notice that all the scenarios considered always respect the
limitations on the deltaV cost and the duration, thus showing the robustness of the mission to alternative
MCSs. Although the ATD-1 and the ATD-3 have been labelled as not safe enough, it is noted that for every
possible variant event there is at least one acceptable solution. So, even if the ATD-1 and ATD-3 are not safe
enough, their relative variant MCSs can be approached using other solutions such as the ATD-2, the timedown, or the deltaV-down solutions. In conclusion, all the solutions which did not respect the nominal
constraints on duration, deltaV cost and safety, have been labelled as off-nominal.


113


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.23: Overview for the Observe&Retrieve scenarios_











|Observe and Retrieve – Nominal HP2 & HP3|Col2|Col3|Col4|
|---|---|---|---|
|**Scenario**|**DeltaV cost**|**Duration**|**Safe**|
|Observe&Retrieve<br>LongerHP1 (DD)|9.637|13.373|Yes|
|Observe&Retrieve<br>LongerHP1 (TD)|9.716|13.037|Yes|
|Observe&Retrieve<br>LongerHP1 (DD)<br>2 Insp|10.236|14.076|Yes|
|Observe&Retrieve<br>LongerHP1 (TD)<br>2 Insp|11.248|13.740|Yes|
|Observe&Retrieve<br>LongerComm (DD)|10.620|24.151|Yes|
|Observe&Retrieve<br>LongerComm (TD)|10.792|23.542|Yes|
|Observe&Retrieve<br>LongerComm (ATD-1)|11.791|15.542|No|
|Observe&Retrieve<br>LongerComm (ATD-2)|15.304|20.582|Yes|
|Observe&Retrieve<br>LongerComm (ATD-3)|13.236|19.426|No|
|Observe&Retrieve<br>LongerComm (DD)<br>2 Insp|12.152|24.854|Yes|
|Observe&Retrieve<br>LongerComm (TD)<br>2 Insp|11.391|24.245|Yes|
|Observe&Retrieve<br>LongerComm (ATD-1)<br>2 Insp|12.390|16.244|No|
|Observe&Retrieve<br>LongerComm (ATD-2)<br>2 Insp|15.904|21.284|Yes|
|Observe&Retrieve<br>LongerComm (ATD-3)<br>2 Insp|13.836|20.129|No|
|Observe&Retrieve<br>LongerComm&HP1<br>(DD)|10.998|24.629|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(TD)|11.177|23.957|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-1)|12.362|16.211|No|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-2)|15.415|21.185|Yes|


114


_-_
_Chapter 6_ _Variant Scenarios Analysis_


|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-3)|12.685|19.295|No|
|---|---|---|---|
|Observe&Retrieve<br>LongerComm&HP1<br>(DD)<br>2 Insp|11.597|25.332|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(TD)<br>2 Insp|11.777|24.660|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-1)<br>2 Insp|12.962|16.914|No|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-2)<br>2 Insp|16.014|21.888|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-3)<br>2 Insp|13.285|19.998|No|



_Table 6.24: Overview for the Observe scenarios_











|Observe – Nominal HP2|Col2|Col3|Col4|
|---|---|---|---|
|**Scenario**|**DeltaV cost**|**Duration**|**Safety**|
|Observe<br>LongerHP1 (DD)|11.170|13.051|Yes|
|Observe<br>LongerHP1 (TD)|10.315|12.715|Yes|
|Observe<br>LongerHP1 (DD)<br>2 Insp|11.800|13.753|Yes|
|Observe<br>LongerHP1 (TD)<br>2 Insp|11.878|13.417|Yes|
|Observe<br>LongerComm (DD)|12.152|23.829|Yes|
|Observe<br>LongerComm (TD)|12.325|22.114|Yes|
|Observe<br>LongerComm (ATD-1)|13.323|15.219|No|
|Observe<br>LongerComm (ATD-2)|14.165|20.259|Yes|
|Observe<br>LongerComm (ATD-3)|14.769|19.104|No|
|Observe<br>LongerComm (DD)<br>2 Insp|12.782|24.532|Yes|
|Observe<br>LongerComm (TD)<br>2 Insp|12.955|23.923|Yes|


115


_-_
_Chapter 6_ _Variant Scenarios Analysis_

|Observe<br>LongerComm (ATD-1)<br>2 Insp|13.395|15.922|No|
|---|---|---|---|
|Observe<br>LongerComm (ATD-2)<br>2 Insp|17.467|20.962|Yes|
|Observe<br>LongerComm (ATD-3)<br>2 Insp|15.399|19.807|No|
|Observe<br>LongerComm&HP1<br>(DD)|12.530|24.307|Yes|
|Observe<br>LongerComm&HP1<br>(TD)|12.710|23.635|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-1)|13.895|15.889|No|
|Observe<br>LongerComm&HP1<br>(ATD-2)|16.948|20.863|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-3)|14.218|18.973|No|
|Observe<br>LongerComm&HP1<br>(DD)<br>2 Insp|13.160|25.009|Yes|
|Observe<br>LongerComm&HP1<br>(TD)<br>2 Insp|13.340|24.337|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-1)<br>2 Insp|14.525|16.591|No|
|Observe<br>LongerComm&HP1<br>(ATD-2)<br>2 Insp|17.578|21.565|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-3)<br>2 Insp|14.848|19.675|No|



116


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.25: Overview for the Observe&Retrieve scenarios - Longer HP2 and HP3_





|Observe and Retrieve – Longer HP2 & HP3|Col2|Col3|Col4|
|---|---|---|---|
|**Scenario**|**DeltaV cost**|**Duration**|**Safety**|
|Observe&Retrieve<br>LongerHP1 (DD)<br>LongerHP2&3|10.244|14.160|Yes|
|Observe&Retrieve<br>LongerHP1 (TD)<br>LongerHP2&3|10.322|13.824|Yes|
|Observe&Retrieve<br>LongerHP1 (DD)<br>2 Insp<br>LongerHP2&3|10.843|14.863|Yes|
|Observe&Retrieve<br>LongerHP1 (TD)<br>2 Insp<br>LongerHP2&3|10.922|14.527|Yes|
|Observe&Retrieve<br>LongerComm (DD)<br>LongerHP2&3|11.227|24.939|Yes|
|Observe&Retrieve<br>LongerComm (TD)<br>LongerHP2&3|11.399|24.330|Yes|
|Observe&Retrieve<br>LongerComm (ATD-1)<br>LongerHP2&3|12.397|16.329|No|
|Observe&Retrieve<br>LongerComm (ATD-2)<br>LongerHP2&3|15911.000|21.369|Yes|
|Observe&Retrieve<br>LongerComm (ATD-3)<br>LongerHP2&3|13.843|20.214|No|
|Observe&Retrieve<br>LongerComm (DD)<br>2 Insp<br>LongerHP2&3|11.826|25.641|Yes|
|Observe&Retrieve<br>LongerComm (TD)<br>2 Insp<br>LongerHP2&3|11.998|25.032|Yes|
|Observe&Retrieve<br>LongerComm (ATD-1)<br>2 Insp<br>LongerHP2&3|12.997|17.032|No|
|Observe&Retrieve<br>LongerComm (ATD-2)<br>2 Insp<br>LongerHP2&3|16.510|22.072|Yes|
|Observe&Retrieve<br>LongerComm (ATD-3)<br>2 Insp<br>LongerHP2&3|14.443|20.916|No|


117


_-_
_Chapter 6_ _Variant Scenarios Analysis_

|Observe&Retrieve<br>LongerComm&HP1<br>(DD)<br>LongerHP2&3|11.605|25.416|Yes|
|---|---|---|---|
|Observe&Retrieve<br>LongerComm&HP1<br>(TD)<br>LongerHP2&3|11.784|24.744|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-1)<br>LongerHP2&3|12.969|16.999|No|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-2)<br>LongerHP2&3|16.022|21.972|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-3)<br>LongerHP2&3|13.292|20.082|No|
|Observe&Retrieve<br>LongerComm&HP1<br>(DD)<br>2 Insp<br>LongerHP2&3|12.204|26.119|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(TD)<br>2 Insp<br>LongerHP2&3|12.384|25.447|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-1)<br>2 Insp<br>LongerHP2&3|13.569|17.701|No|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-2)<br>2 Insp<br>LongerHP2&3|16.621|22.675|Yes|
|Observe&Retrieve<br>LongerComm&HP1<br>(ATD-3)<br>2 Insp<br>LongerHP2&3|13.892|20.785|No|



118


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.26:Overview for the Observe scenarios - Longer HP2_





|Observe – Longer HP2|Col2|Col3|Col4|
|---|---|---|---|
|**Scenario**|**DeltaV cost**|**Duration**|**Safety**|
|Observe<br>LongerHP1 (DD)<br>LongerHP2|11.579|13.444|Yes|
|Observe<br>LongerHP1 (TD)<br>LongerHP2|11.658|13.108|Yes|
|Observe<br>LongerHP1 (DD)<br>2 Insp<br>LongerHP2|12.209|14.147|Yes|
|Observe<br>LongerHP1 (TD)<br>2 Insp<br>LongerHP2|12.288|13.811|Yes|
|Observe<br>LongerComm (DD)<br>LongerHP2|12.562|24.223|Yes|
|Observe<br>LongerComm (TD)<br>LongerHP2|12.734|23.614|Yes|
|Observe<br>LongerComm (ATD-1)<br>LongerHP2|13.733|15.613|No|
|Observe<br>LongerComm (ATD-2)<br>LongerHP2|17.246|20.653|Yes|
|Observe<br>LongerComm (ATD-3)<br>LongerHP2|15.178|19.498|No|
|Observe<br>LongerComm (DD)<br>2 Insp<br>LongerHP2|13.192|24.925|Yes|
|Observe<br>LongerComm (TD)<br>2 Insp<br>LongerHP2|13.364|24.316|Yes|
|Observe<br>LongerComm (ATD-1)<br>2 Insp<br>LongerHP2|14.363|16.316|No|
|Observe<br>LongerComm (ATD-2)<br>2 Insp<br>LongerHP2|17.876|21.356|Yes|
|Observe<br>LongerComm (ATD-3)<br>2 Insp<br>LongerHP2|15.808|20.200|No|


119


_-_
_Chapter 6_ _Variant Scenarios Analysis_


|Observe<br>LongerComm&HP1<br>(DD)<br>LongerHP2|12.940|24.700|Yes|
|---|---|---|---|
|Observe<br>LongerComm&HP1<br>(TD)<br>LongerHP2|13.119|24.028|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-1)<br>LongerHP2|14.304|16.283|No|
|Observe<br>LongerComm&HP1<br>(ATD-2)<br>LongerHP2|17.357|21.256|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-3)<br>LongerHP2|14.628|19.366|No|
|Observe<br>LongerComm&HP1<br>(DD)<br>2 Insp<br>LongerHP2|13.570|25.403|Yes|
|Observe<br>LongerComm&HP1<br>(TD)<br>2 Insp<br>LongerHP2|13.749|24.731|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-1)<br>2 Insp<br>LongerHP2|14.934|16.985|No|
|Observe<br>LongerComm&HP1<br>(ATD-2)<br>2 Insp<br>LongerHP2|17.987|21.959|Yes|
|Observe<br>LongerComm&HP1<br>(ATD-3)<br>2 Insp<br>LongerHP2|15.258|20.069|No|



To simply browse all the different solutions, the duration, and the cost of each of their mission segments, it
was created a database on an Excel document. Then a graphic interface was added to let an external user
select a desired variant for every segment which presents one or more of them. Finally, another Excel sheet
reports the deltaV budget and the duration budget of the selected MCS for both the Observe and the
Observe&Retrieve scenarios, while also reporting the nominal ones for comparison purposes. By doing so,
any user can easily observe the properties of a desired MCS and can confront it to another variant scenario
or to the nominal one. As an example, two couples of tables are here reported:


120


_-_
_Chapter 6_ _Variant Scenarios Analysis_


  Table 6.27 and Table 6.28 respectively show the deltaV and time budget for the variant MCS with
the highest deltaV required, that is the Observe scenario with longer Commissioning, HP1 and HP2,
using an ATD-2 solution for the IPA rendezvous, two observation cycles, and an additional
manoeuvre during the EMP;

  Table 6.29 and Table 6.30 respectively show the deltaV and time budget for the variant MCS with
the longest duration, that is the Observe&Retrieve scenario with longer Commissioning, HP1, HP2
and HP3, using a deltaV-down solution for the IPA rendezvous and two observation cycles;


_Table 6.27: DeltaV budget for the variant scenario MCS with the highest deltaV cost_

|OBSERVE<br>Off- Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**∆V [m/s]**|**Margin**|**∆V [m/s]**|
|HP1|0.887|5%|0.931|
|Virtual CAM + HP1 bis|1.040|100%|2.080|
|Virtual CAM + HP1 ter|0.500|100%|1.000|
|IPA|2.543|5%|2.670|
|HP2Ins|4.306|5%|4.521|
|ZRV2|0.661|5%|0.694|
|HP2|0.486|5%|0.510|
|OPA - Cycle 1|0.266|100%|0.532|
|WSE Insertion - Cycle 1|0.192|100%|0.385|
|OPA - Cycle 2|0.095|100%|0.189|
|WSE Insertion - Cycle 2|0.221|100%|0.441|
|D CAM|0.068|100%|0.136|
|SR CAM|0.600|5%|0.630|
|EMP Manoeuvre|3.112|5%|3.267|
|**∆V TOT [m/s]**|**14.976**|**∆V TOT with**<br>**margins [m/s]**|**17.987**|



_Table 6.28: Time budget for the variant scenario MCS with the highest deltaV cost_

|OBSERVE<br>Off - Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**Duration [day]**|**Margin**|**Duration [day]**|
|Commissioning|10.000|5%|10.500|
|HP1|0.563|5%|0.591|
|IPA|8.200|5%|8.610|
|HP2Ins|0.083|5%|0.088|
|HP2|0.563|5%|0.591|
|OPA - Cycle 1|0.167|5%|0.175|
|Observation + FreeFlight - Cycle 1|0.669|5%|0.703|
|OPA - Cycle 2|0.171|5%|0.179|
|Observation + FreeFlight - Cycle 2|0.669|5%|0.703|
|**Duration TOT [day]**|**21.084**|**Duration TOT with**<br>**margins [day]**|**22.138**|



121


_-_
_Chapter 6_ _Variant Scenarios Analysis_


_Table 6.29: DeltaV budget for the variant scenario MCS with the highest duration_

|OBSERVE & RETRIEVE<br>Variant Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**∆V [m/s]**|**Margin**|**∆V [m/s]**|
|HP1|0.887|5%|0.931|
|Virtual CAM + HP1 bis|1.040|100%|2.080|
|Virtual CAM + HP1 ter|0.500|100%|1.000|
|IPA|0.906|5%|0.951|
|HP2Ins|2.117|5%|2.223|
|ZRV2|0.280|5%|0.294|
|HP2|0.486|5%|0.510|
|OPA - Cycle 1|0.266|100%|0.532|
|WSE Insertion - Cycle 1|0.192|100%|0.385|
|OPA - Cycle 2|0.095|100%|0.189|
|WSE Insertion - Cycle 2|0.221|100%|0.441|
|HP3Ins|0.208|5%|0.218|
|ZRV3|0.421|5%|0.442|
|HP3|0.282|5%|0.296|
|Docking|0.900|5%|0.945|
|D CAM|0.068|100%|0.136|
|SR CAM|0.600|5%|0.630|
|**∆V TOT [m/s]**|**9.468**|**∆V TOT with**<br>**margins [m/s]**|**12.204**|



_Table 6.30: Time budget for the variant scenario MCS with the highest duration_

|OBSERVE & RETRIEVE<br>Off - Nominal Scenario|Col2|Col3|Col4|
|---|---|---|---|
|**Manoeuvre**|**Duration [day]**|**Margin**|**Duration [day]**|
|Commissioning|10.000|5%|10.500|
|HP1|0.563|5%|0.591|
|IPA|11.480|5%|12.054|
|HP2Ins|0.083|5%|0.088|
|HP2|0.563|5%|0.591|
|OPA - Cycle 1|0.167|5%|0.175|
|Observation + FreeFlight - Cycle 1|0.669|5%|0.703|
|OPA - Cycle 2|0.171|5%|0.179|
|Observation + FreeFlight - Cycle 2|0.669|5%|0.703|
|HP3Ins|0.113|5%|0.118|
|HP3|0.563|5%|0.591|
|Final Approach|0.007|5%|0.007|
|**Duration TOT [day]**|**25.046**|**Duration TOT with**<br>**margins [day]**|**26.298**|



122


## _7 DRAMA Analysis_

The ESA software DRAMA (Debris Risk Assessment and Mitigation Analysis) was used to perform several
analyses in order to be compliant with the Space Debris Mitigation [7] and, more in general, to the
Statement of Work for the Phases B2/C/D of SROC [18]. In particular, the following topics were analysed

[21]:


  Computation of the geometric cross-section (with the CROC tool);

  - Collision avoidance manoeuvre frequencies to avoid debris and/or meteoroids along the trajectory
(with the ARES tool);

  Natural decay of the satellite after the proximity operations phase (with the OSCAR tool);

  Re-entry survival prediction for SROC and its main components and the associated risk on ground
for any object surviving the re-entry phase (with the SARA tool);


The last two points apply only to the Observe scenario.

##### 7.1 CROC tool


The analysis with CROC was the first one performed to evaluate the average cross-section of the satellite.
SROC is modelled as a simple box, with width = 0.226 m, height = 0.34 m and depth = 0.226 m as reported
in SROC System Design Definition File [20]. The at **t** iude of the satellite is set to randomly tumbling, as it
happens in many phases during the mission; even during the ones with a controlled at **t** iude, such as the
observation one, the relative orientation of the body axes varies with respect to the RIC axes.

**t**
**t**

##### i



_Figure 7.1: SROC body in CROC_


The output of the results is an average cross-section of 0.1014 m [2] .

##### 7.2 Collision Avoidance Manoeuvre Evaluaton i


The space debris density in the space environment can be evaluated using the ARES tool. This software
combines the orbit information with the accuracy of space surveillance systems to evaluate the statistical
number of collision avoidance manoeuvres as a function of the acceptable risk levels [22]. In particular, the
decision to perform a CAM is related to the risk associated with a near-miss event, which in turn depends
on the geometry of the of the encounter, the collision cross-section, and the uncertainties in the state
vector of both objects. Since in LEO there are many poorly tracked objects with a location uncertainty in the


123


_-_
_Chapter 7_ _DRAMA Analysis_


order of kilometres (assumed to be a Gaussian distribution) and a part of them cannot even be tracked, the
risk threshold is best defined in terms of risk reduction with respect to the unavoidable background
population. This value is defined as a function of the ACPL (Accepted Collision Probability Level), which most
space missions set at 10 [-4] [24].


To start the analysis, the start epoch was set to 2024/11/01, which is when the satellite is deployed in the
STK simulation. Since ARES considers SROC with a spherical shape, the spacecraft radium was set equal to
the distance from the centre of SROC to its furthest point, which is half of the diagonal (0.233 m). The orbit
used for this analysis is the same used in STK and it is defined in Table 7.1.


_Table 7.1: Orbit definition in DRAMA_

|Orbital Parameter|Value|
|---|---|
|Semi-major axis|6771 km|
|Eccentricity|0|
|Inclinaton|6.2 deg|
|Right Ascension of the Ascending node (RAAN)|0 deg|
|Angle of Perigee|0 deg|
|True Anomaly|0 deg|



7.2.1 MASTER Analysis


Before analysing the ACPL it is useful to evaluate the space debris flux in the target orbit in order to
understand the space debris situation that the satellite will encounter. Useful information can be
extrapolated from this analysis, such as the direction from which it can be expected to receive most of the
conjunctions (if there are any). Moreover, this additional analysis, although it is not strictly required to
assess the CAM required, is still recommended in ARES guidelines document [22]. To perform this study an
additional ESA software is used: MASTER (Meteoroid and Space Debris Terrestrial Environment Reference)

[25].


The analysis was conducted on the same orbit described in Table 7.1 and for debris with the same size as
the ones analysed in ARES, which are from 1 cm to 100 m of diameter. Technically, MASTER can provide
fluxes of impact object size down to 1 micrometre, but ARES only considers only an impact object size down
to 1 cm, since it is the best resolution achievable by state-of-the-art ground surveillance systems. The most
relevant results are the 2D flux distribution of the debris according to the azimuth and elevation angles.
From the first one (Figure 7.2) it is possible to see that the flux is distributed between all the possible
azimuth values, which means that there is the possibility of a reverse conjunction (that is debris
approaching SROC from the back). The probability of this type of collision, however, is lower with respect to
one coming from the front, especially if the range from -80 deg to -40 deg is considered.


124


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.2:Flux Distribution according to the Impact Azimuth_


Figure 7.3 represents the flux distribution according to the impact elevation: it shows that most of the
debris are encountered along null or very low elevation angles, with a flux distribution almost constantly
decreasing with the increasing of the impact elevation angles.


_Figure 7.3: Flux Distribution according to the Impact Elevation_


Figure 7.4 shows the Flux Distribution versus the impact velocity expressed in km/s. The flux distribution is
homogeneously distributed across the impact velocity range, which varies from 1 km/s to 28 km/s but
presents the highest values for lower impact velocities.


125


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.4: Flux Distribution according to the Impact Velocity_


Figure 7.5 shows the 2D flux distribution with different object diameters; as it may be expected, for the
minimum diameters there are the maximum values. As mentioned before, the flux distribution is evaluated
considering objects with a diameter set between a minimum and a maximum value. The values selected for
both ARES and Master are the default ones, which in the DRAMA user manual are said to be sufficient for
an adequate risk analysis.


_Figure 7.5: Flux Distribution according to the Object Diameter_


7.2.2 ARES set - up


After setting the spacecraft orbit and radius, and the range size for the debris, the radar equation [21] is
configured to estimate the cataloguing performance:



𝐷 𝑚𝑖𝑛 (ℎ) = 𝐷 𝑟𝑒𝑓 ℎ [ℎ]
∙( 𝑟𝑒𝑓



~~)~~



𝑒𝑥𝑝



Where 𝐷 𝑚𝑖𝑛 is the minimum detectable diameter, 𝐷 𝑟𝑒𝑓 is a reference diameter, ℎ is the orbit altitude and
ℎ 𝑟𝑒𝑓 is a reference altitude. To account for different determination processes for LEO and MEO/GEO objects,
two branches for this equation are provided; ARES evaluates both branches, then chooses the one which
guarantees the minimum detectable diameter. The inputs for both branches are the default ones.


126


_-_
_Chapter 7_ _DRAMA Analysis_


The reason why this equation is used is that ARES’s scope is to simulate the CAM in the entirety of the
actions which would take place in the real operative scenario, to the extent that every supporting space
surveillance network has a certain minimum detectable radius. For this reason, even the time between the
prediction of a collision and the actual occurrence of it is considered; this parameter was set to 1 day. There
is also the possibility to set a global scaling factor to correct the population covariances; to set a neutral
scaling factor, this value was set to 1.


Finally, the collision avoidance strategy was defined. Ten different values for the ACPL were considered as
well as ten values for the orbit revolutions between manoeuvre and event. ARES always considers a short
term (half an orbit) along-track manoeuvre, while these values are used to consider one-day-increasing
durations for the orbit revolutions. The target collision probability level is a scaling factor for the ACPL which
defines the target collision probability for a collision avoidance manoeuvre. It is set to 0.1, which means
that, if the ACPL is 10 [-5], then ARES triggers a manoeuvre for each event with a collision probability level
above 0.1x10 [-5] . The propulsion system category (cold gas) and specific impulse (42 s) were defined in
accordance with SROC system design document [20]. Figure 7.6 shows the complete setup for this analysis.


127


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.6: ARES settings_


7.2.3 Ares results


Figure 7.7 shows the risk reduction and the residual risk as a function of the ACPL. For ACPL values around
5x10 [-5] the risk is reduced by 50%, while with 10 [-6] the risk is reduced by nearly 90%. Typically, what is aimed
at is a risk reduction of around 90% and a ACPL of at least 10 [-4] : in this case, these recommendations are
meth with an ACPL of 10 [-6] . The residual risk is calculated considering all the risks with a collision probability
inferior to the defined threshold; in turn, the risk reduction is the accumulated collision probability of the
events above the decision threshold. Besides these two parameters, there is a third one called remaining
risk, which is the risk due to non-trackable objects, whose contribution is usually not shown since nothing
can be done about them. Figure 7.8 illustrates that the mean number of avoidance manoeuvres increases
almost logarithmically with the decrease of the ACPL, with a maximum value of 0.3 manoeuvres to
guarantee an ACPL of 10 [-6] . This number refers to a mean number evaluated for a year of propagation.


_Figure 7.7: Risk reduction and residual risk as function of the ACPL_


128


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.8: Manoeuvres frequency as function of the ACPL_


Before defining a final value for the ACPL and showing other useful results, a robustness analysis is
recommended [22]. The following cases were considered:


  -30% of the time between the event detection and the event occurrence (0.7 days); for a shorter
interval, DRAMA does not guarantee the capability to avoid the manoeuvre;

  Double the time between the event detection and the event occurrence (2 days);

  - Double the scale factor on covariance (2);


For the first variation, the results (Figure 7.9 and Figure 7.10) show that there is an increase in the risk
reduction (around 91% for an ACPL of 10 [-6] ), but also a decrease in the mean number of avoidance
manoeuvres (almost 0.26 per year for an ACPL of 10 [-6] ). In the second case (Figure 7.11 and Figure 7.12), for
an ACPL of 10 [-6], the risk reduction is only 82% and the required number of avoidance manoeuvres is 0.34 (a
bit more than the nominal case). The third and final case, as expected, shows worse results (Figure 7.13 and
Figure 7.14) than the nominal analysis: for an ACPL of 10 [-6], the risk reduction is approximately 82% and the
required number of manoeuvres is 0.4. Moreover, the risk reduction decreases to 50% for much lower
values (around 10 [-5] ) with respect to the nominal analysis. In conclusion, although noticeable changes
happen between the different scenarios, the robustness of the analysis and the solution is consistent with
the results provided in the verification guidelines of ARES [22].



_Figure 7.9: First case - Risk reduction and residual risk as_

_function of the ACPL_



_Figure 7.10: First case - Manoeuvres frequency as function of the_


_ACPL_


129


_Figure 7.11: Second case - Risk reduction and residual risk as_

_function of the ACPL_


_Figure 7.13: Third case - Risk reduction and residual risk as_

_function of the ACPL_



_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.12: Second case - Manoeuvres frequency as function of_

_the ACPL_


_Figure 7.14: Third case - Manoeuvres frequency as function of_

_the ACPL_



To achieve a much higher risk reduction, the ACPL could be lowered even more. As shown in Figure 7.15 and
Figure 7.16, if an ACPL equal to 10 [-7] is considered, it is obtained a basically null residual risk, but at the cost
of a mean number of avoidance manoeuvre equal to 2.25 (7.5 times more than the nominal case). For this
reason, this option was discarded.


130


_Figure 7.15: Minimum ACPL=10_ _[-7]_ _- Risk reduction and residual_
_risk as function of the ACPL_



_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.16: Minimum ACPL=10_ _[-7]_ _- Manoeuvres frequency as_
_function of the ACPL_



Figure 7.17 shows for the nominal case the required deltaV for one year across the orbit. It is no surprise
that for lower ACPL the deltaV is lower since an inferior manoeuvre frequency is required. Two different
types of strategies are implemented by ARES [23]:


  Short–term strategy: it is the one evaluated for a number of revolutions = 0. It targets additional
radial separation between the two objects at the TCA (Time of Closest Approach).

  Long-term strategy: different manoeuvres are evaluated for different multiples of one revolution.
They target a different phasing and thus a larger along- and/or cross-track separation at the TCA.
The required deltaV to perform these manoeuvres decreases with the increase of the number of
revolutions before the TCA.


For the selected ACPL level (the purple line) the maximum deltaV (0.123 m/s) is required for a long-term
strategy starting one revolution before the TCA. The short-term strategy requires a smaller deltaV
(0.680·10 [-1] m/s).


_Figure 7.17: Required deltaV as function of the number of revolutions for long and short term strategy_


Figure 7.18 shows interesting information about the risk category analysed with this study. Besides the
already defined risk reduction and residual risk, it is also presented the remaining risk, which is, as
explained before, not avoidable. This fixed value increases of 0.1767·10 [-5] the residual risk; for the ACPL
considered the remaining risk is equal to 0.2166·10 [-5] .


131


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.18: Risk reduction, residual risk and remaining risk in function of the mean number of avoidance manoeuvres_


The final step of this analysis was selecting a deltaV for the Debris CAM (called D CAM in the deltaV budget).
Just using one of the deltaVs plotted in Figure 7.17 would not make sense, since they refer to an average of
0.3 CAM per year. These values would be useful to allocate the deltaV budget for missions staying in the
same orbit for several years, which is not the case for SROC. For this reason, the selected deltaV was divided
by 0.3 to assess the deltaV required to perform a single manoeuvre. Considering a CAM performed 6
revolutions before the EP, it is obtained a deltaV equal to 0.0683 m/s. Table 7.2 shows the deltaV required
to perform one CAM and how many hours before the EP the manoeuvre must be performed. The
highlighted solution was considered a good compromise between the preparation time required and the
deltaV.


_Table 7.2: CAM deltaV summary_







|Rev before EP [#]|Time before EP [hr]|DeltaV for 0.3 CAM a<br>year [m/s]|DeltaV for one CAM<br>[m/s]|
|---|---|---|---|
|||||
|0.000|-|0.068|0.227|
|1.000|1.543|0.123|0.411|
|2.000|3.086|0.062|0.205|
|3.000|4.628|0.041|0.137|
|4.000|6.171|0.031|0.103|
|5.000|7.714|0.025|0.082|
|6.000|9.257|0.020|0.068|
|7.000|10.800|0.018|0.059|
|8.000|12.342|0.015|0.051|
|9.000|13.885|0.014|0.046|
|10.000|15.428|0.012|0.041|

##### 7.3 OSCAR tool

OSCAR is used to the de-orbit of a satellite after its nominal end-of-life, to verify the compliance of the
SROC mission with the Space Debris Mitigations for Agency projects [7]. The spacecraft parameters were
defined as follows:


132


_-_
_Chapter 7_ _DRAMA Analysis_


  - Cross-section area [m [2] ]: 0.1014, which is the value computed by CROC.

  - Mass [kg]: 21 kg

  Drag coefficient: 2.2

  Reflectivity coefficient: 1.3


The initial orbit is the same described in Table 7.1, but the begin date (YYYY-MM-DD) is 2021-11-15 at
00:00, which is approximately when the proximity operation phase should end. OSCAR requires to define
the disposal option, which in this case is none. The orbit prediction is dependent on the prediction for the
solar and geomagnetic activities used, since, as it has already been explained in Sub-section 3.2.1, they
were used to model the atmospheric drag. To account for these differences, three analyses were
performed, which all confirm that SROC deorbits less than 13 months, thus respecting the Space Debris
Mitigations for Agency projects [7].


  - **ECSS sample solar cycle** : final date (YYYY-MM-DD) 2025-04-22
This analysis is recommended by the ECSS standard [26] and uses the solar and geomagnetic
parameters of the solar cycle 23 for the complete propagation time span.


_Figure 7.19: ECSS Sample - SROC altitude vs time_


  **Latest predictions** : final date (YYYY-MM-DD) 2025-06-05
This model uses the available up-to-date prediction on solar and geomagnetic activity provided by
ESA. At the time of the analysis, the data were updated on 2023-05-27.


133


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.20: Latest prediction - SROC altitude vs time_


Another analysis based on the latest prediction is the worst case/best case. Specifically, it was
carried out a worst-case analysis with a confidence interval of 95%, which means that the worstcase results in solar and geomagnetic activity resembling historical activity data which is about
47.5% lower than the mean cycle but not higher than the cycle from the latest prediction. The
predicted final date becomes (YYYY-MM-DD) 2025-11-16, as shown in Figure 7.21. Figure 7.22
confirms what has previously been presented regarding the dependence of the orbital lifetime on
the solar activity: the worst case has a lower activity (light blue line), thus the drag is minor and the
orbital lifetime is higher.


_Figure 7.21: Lifetime comparison between the worst case and nominal case_


134


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.22: Solar activity comparison between worst case and nominal case_


  - **Monte Carlo Analysis** : final date (YYYY-MM-DD) 2025-04-09
This analysis is one of the ISO-recommended methods [28] and requires the random selection for
each day within the propagation time span of a solar and geomagnetic activity data triplet (daily
and mean F10.7 as well as daily planetary amplitude Ap) from a specified number of solar cycles,
which can vary between 1 and 6. The results of this analysis, which considers the last five solar
cycles (from 19 to 23), are shown in Figure 7.23.


_Figure 7.23: Monte Carlo sampling - SROC altitude vs time_

##### 7.4 SARA tool


Since the inherited propagation uncertainties do not allow to know in advance if or when a satellite (or one
of its components) will hit Earth’s surface, the risk of a specific re-entry is evaluated and then confronted
with an accepted casualty risk threshold of 10-4 [30]. This assessment is performed using the tool SARA,
whose main settings and satellite model definition are reported in this section.


135


_-_
_Chapter 7_ _DRAMA Analysis_


7.4.1 SARA setngs and SROC model def ti i niton i


First, it is necessary to define the basic settings of the analysis. The software is run in expert mode to
correctly define several parameters which could not be defined in basic mode. The initial orbit is the same
used for ARES and OSCAR (Table 2.1), as well as the beginning date. The inputs for the propagation setting
were defined in accordance with the setting for OSCAR, since SARA uses OSCAR to propagate the state of
the satellite until it reaches 140 km in altitude. From here down, the propagator used is that of SARA, which
also automatically evaluated the cross-section and the drag coefficient. Therefore, the following
propagation settings only define OSCAR’s propagation:


  Reflectivity coefficient: 1.3

  Cross-section: 0.101 m [3]

  Drag coefficient: 2.2


The initial at **t** iude was set to tumbling, while the at **t** iude of the fragments was set to “inherited”, which
means that the at **t** iude is inherited from the satellite. Since the SROC is randomly tumbling, the fragments
will be randomly tumbling too. An important parameter is the Voxelator resolution length, which
determines the size of the voxels used when estimating the aerothermodynamic properties of the
compound object. A voxel is a 3D cube located on a three-dimensional grid used to create 3D models [31]: if
its resolution length is low, it increases the faithfulness of the results, but it will also increase the run-time.
To select a proper value, both the dimension of SROC components and SARA’s limitation on the maximum
number of voxels were considered, obtaining a Voxelator resolution length of 2 mm.


The environment is defined considering a dynamic atmospheric model, which includes a solar and
geomagnetic activity database based on ESA’s latest prediction’s (the same used in OSCAR) and an
atmospheric wind model. Finally, the on-ground risk is defined considering a casualty threshold of 15 J. This
is the lowest kinetic energy to be considered for the on-ground risk assessment; 15J is the default values in
SARA. The re-entry is modelled considering a non-controlled type from a circular orbit with an inclination of
6.2 deg. Figure 7.24 is a screenshot from SARA showing all the basic settings.

ti i i

**t** **t**
**t**


ti i i

**t** **t**
**t**



_Figure 7.24: SARA Basic Settings_


The SROC model was defined considering the recommendations from SARA’s user manual [30]. To produce
an accurate assessment of the re-entry risk, the model was built considering SROC’s components with the
highest mass and volume. Their virtual counterparts are modelled to resemble their mass, volume and
shape as close as possible. Moreover, SARA lets the user select the material of the component from a


136


_-_
_Chapter 7_ _DRAMA Analysis_


material list, whose element either represent a physical material (such as the AA7075) or the properties of a
piece of equipment. One example of this last category is the material El-Mat which is the equivalent
material to model electronic components [29]. By, selecting the material, the following properties are set:
density, melting temperature, specific heat at 300 K, heat of melting, conductivity and emissivity.


Each object added to the model is ordered with a parent-children method: components on the same level
of the hierarchy can be connected one to another; moreover, it is possible to define the connection area
between them and one or more “Dissolution Triggers”, such as the temperature or the altitude. When the
conditions specified on the “Dissolution Trigger” window are met, the components separate from each
other. For each parent component, it is possible to define a “Chid Release Trigger”: when one of the
selected conditions is met the children objects contained inside the parent will be released. It is important
to notice that when the “Chid Release Trigger” is triggered, the parent object disappears from the
simulation even if it has not demised yet. For this reason, no “Child Release Trigger” is active during the
analysis: the objects contained inside another one are released only when the latter is demised.


The higher hierarchical level of the model is composed by of following elements:


  - Structure

  Solar Panel x (the solar panel on the positive x face of SROC)

  Solar Panel y (the solar panel on the negative y face of SROC)

  - UHF Antenna


All the last three objects are connected to the structure, with a connection area equal to the contact area
they have with the structure (0.0174 m [2] for the solar panels and 0.00746 m [2] for the antennas). The
dissolution trigger for all these connections is when the altitude decreases below 103 km, as suggested by
the SARA user manual [30]. Table 7.3 contains a list of all the components added to the model, as well as
their mass, volume, shape and material used. The mass and volume of the components reported in the
SROC system definition file [20] are added to compare the differences with the objects in the SARA model.


It is noticeable that for a few components, the relative error with respect to the system defined in phase B1
is high. This is due to the fact that for some elements it was not possible to equally represent both the
volume and the mass of the objects. For the Load Controller Module (LCM) and the RWA it was preferred to
use a bigger volume to maintain a representative mass of the component. The Torque rod, instead, is
maintained a lower mass since the absolute difference between the actual component is only 58 g which
does not affect significantly the mass budget of the model.


The following materials were used to define the structural and thermal properties of the equipment
composing the satellite [29]:


  - Drama-AA7075: this class is used for aluminum alloys as the baseline. It is used for most of the
components of the model; as suggested in the SARA user manual, if an object:

`o` is constructed primarily of aluminum or magnesium;
`o` has a mass under 5 kg;
`o` contains no contiguous parts of a higher demise temeperature material which are over 50

kg, and the accurate properties of such components are not available, it is allowed to use
the Drama-AA7075 material.

  - Drama-A316: class example for steel alloy baseline.

  - Drama-El-Mat: this material is used to model electronic components, including boards and wiring
thereon, but not the casing that includes them. For this reason, it was used only for the boards and
the wiring.


137


_-_
_Chapter 7_ _DRAMA Analysis_



_Table 7.3: Components of the SARA model_















































|Component|Mass [kg]|Mass<br>Relative<br>Error|Volume [U]|Volume<br>Relative<br>Error|Shape|Material|
|---|---|---|---|---|---|---|
|**Structure**|5.400|0%|12U|0%|Box|Drama-<br>AA7075|
|**Solar**<br>**Panel**<br>**(x2)**|0.540|0%|0.138|-0.7%|Box|Drama-<br>AA7075|
|**Antenna UHF**|0.105|0%|0.077|0%|Box|Drama-<br>AA7075|
|**Thruster**<br>**Module**|4.026|0%|3.703|0%|Box|Drama-<br>AA7075|
|**RWA**|1.059|-11.5%|0.092|+ 95.7%|Box|Drama-A316|
|**Batery**<br>**Module**<br>**Assemlby**|0.473|0%|0.123|0%|Box|Drama-<br>AA7075|
|**Endeavour**<br>**Avionics**<br>**Module**|0.588|0%|0.265|0%|Box|Drama-<br>AA7075|
|**Backplane**<br>**PCBA**|0.48|0%|0.445|0%|Box|Drama-El-<br>Mat|
|**DOCKS-A**|0.272|0%|0.352|-24.6%|Cone|Drama-<br>AA7075|
|**Payload**<br>**Interface**<br>**Board**|0.300|0%|0.124|0%|Box|Drama-<br>AA7075|
|**NFOV Camera**|0.108|0%|0.081|-1.2%|Cylinder|Drama-<br>AA7075|
|**LIDAR**|0.036|0%|0.0259|0%|Box|Drama-A316|
|**Payload**|0.061|0%|0.034|-2.9%|Cylinder|Drama-<br>AA7075|
|**IR Camera**|0.145|0%|0.102|-1.4%|Cylinder|Drama-<br>AA7075|
|**Housekeeping**<br>**Board**|0.092|-12.6%|0.003|-25%|Box|Drama-El-<br>Mat|
|**Torque**<br>**rod**<br>**(x3)**|0.017|-78.4%|0.004|0%|Cylinder|Drama-<br>AA7075|
|**LCM**|0.125|-0.7%|0.031|+ 82.3%|Box|Drama-<br>AA7075|
|**Harness (x2)**|0.148|-6%|0.034|-|Box|Drama-El-<br>Mat|


138


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.25: Comparison between SROC internal view (left) with the SARA model (right)_


SARA user manual [30] recommends creating a model with at least 75% of the spacecraft’s mass. This
recommendation is respected since the total mass of the model is 13.945 kg, while the total mass reported
in the SROC system definition file [20] is 16.062 kg, which means that 84.82% of SROC mass is considered. It
is noted that the reference values used to build the model include the margins on the single component,
while the total system margin is not considered. A comparison between the CAD of the internal
components of SROC and the components of the SARA model is presented in Figure 7.25.


7.4.2 SARA results


The most important result is the assessment of the total re-entry risk:


  - Total casualty area: 0

  - Total casualty probability: 0

  - Total fatality probability: 0


So, according to SARA’s estimate, the satellite does not constitute a potential threat to on-ground safety
since it is completely demised during the re-entry. Before starting the analysis of the re-entry of the
spacecraft and its fragments, it is necessary to define when, according to SARA, an object is demised [32]:


  - Complete mass loss (on both Figure 7.26 and Figure 7.27 these points are marked as “Demise
points”);


139


_-_
_Chapter 7_ _DRAMA Analysis_


  The kinetic energy of the object drops below the 15 J threshold (on the graphs these points are
marked as “Uncritical points”);

  - Ballooning, where an object is not allowed to become unphysically thin (on the graphs these points
are marked as “Ballooning points”);Figure 7.26:


_Figure 7.26: Altitude as function of the Time of all Objects_


Figure 7.26 shows that all the objects demise before impacting with the ground. Approximately for the first
1800 seconds from the start of the re-entry, the compound is still whole, but at 103 km, as imposed by the
dissolution trigger, the solar panels and the antenna separate from the structure and are then demised
respectively around 92 km and 88 km. The structure keeps its re-entry until it demises at approximately 85
km (this point is highlighted by the blue cross in the graph) at 2200 seconds. After that, all the internal
components inside the structure are released and most of them reach the uncritical point in the successive
minutes (red squares). The last component to demise is the RWA which reached the ballooning point at 60
km after approximately 2300 seconds from the start of the re-entry. The reason why this component
demises after all the others is probably due to its material (Drama-A316) which is more resistant than the
Drama-AA7075 to the high temperature faced during the re-entry.


Figure 7.27 shows the downrange of all the objects: all of them demise between a downrange of 15000 km
and 16500 km, with the longest distance obtained by the RWA assembly.


140


_-_
_Chapter 7_ _DRAMA Analysis_


_Figure 7.27: Altitude as function of the Downrange of all Objects_


141


## _8 Conclusions_

This thesis was carried out using three different software (Matlab, STK, and DRAMA) to perform several
tasks related to the mission analysis and trajectory optimization for Phase B2 of the SROC project, a 12U
CubeSat mission. At the beginning of this document, a brief review of the mission was presented to give
some context about the mission objectives, its requirements, and the two Concept of Operations.


All the STK scenarios, Matlab function, and files JSON were reorganized to delete the unnecessary ones or
to unify similar functions into only one; moreover, all the variables used by this software were renamed to
be coherent with the names reported in the MAR produced at the end of the phase B1. Finally, the Matlab
function which optimizes the IPA rendezvous and the one which defines HP2 and HP3 were modified to
improve respectively the optimization of the IPA and the performance during the HPs. After these changes,
the nominal scenario was updated to a new orbit and used to study several aspects of the mission: the WSE
of the observation phase, the ground station coverage, and the optimal time windows to perform the Final
Approach. It was noticed that the ground station coverage may not be enough to guarantee a sufficiently
long communication window, so two possible solutions were presented. Using a GEO satellite constellation
could be the best option since it guarantees an uninterrupted link with SROC.


It was proven that the synergic use of Matlab and STK can greatly decrease the duration of an iterative
analysis by automatizing the set-up, run, and post-processing of every iteration. This property was
particularly useful during the variant scenarios analysis, where STK’s object model interface was used to
connect the STK scenario to the Matlab functions and to evaluate the nominal or variant segments of the
MCS. At first, all the possible variant events were considered isolated, which means that every one of them
was evaluated inside an MCS where no other variant events took place. Thanks to this process it was
possible to assess how every variant event changes the total duration and deltaV cost, and if and how they
influence the successive segments of the MCS. For some variants, different solutions were considered to
either minimize the deltaV cost or the duration of the mission. After that, all the possible combinations of
variant events were analysed for both the Observe and the Observe&Retrieve scenarios. All their results
were saved in an Excel database with an interactive interface that lets an external user define the desired
MCS and then shows the relative DeltaV and duration budgets. All the variant scenarios were analysed to
define which were off-nominal because of a higher deltaV cost, higher duration, or inadequate safety
relative to Space Rider. For every variant MCS it was found at least one valid solution, thus proving the

robustness of the mission.


The ESA software DRAMA was used to study other aspects of the mission, all required by SROC’s Statement
of Work for Phases B2/C/D. The number of CAM manoeuvre and the relative deltaV cost was assessed as a
function of the Accepted Collision Probability Level; since this analysis gave a mean number of annual
manoeuvres inferior to one, the annual deltaV suggested by DRAMA was rescaled to the cost of one

manoeuvre. The OSCAR tool was used to verify the compliance of the SROC mission with the Space Debris
Mitigations for Agency projects and, finally, the tool SARA was used to assess the total re-entry risk. To
perform this last task, a simplified digital twin of SROC was generated using SARA. The results of the analysis
with OSCAR confirmed the compliance with the Space Debris Mitigations for Agency projects, while the
SARA analysis assessed that the mission does not constitute any on-ground risk, since the satellite demises
before an altitude equal to 60 km.


The next step for Phase B2 could involve a new definition for the WSE: as mentioned before, the current
Matlab functions produce an acceptable approximation if used to evaluate the deltaV cost and the duration
of the observation phase, but the fact that it is not possible to define the exact geometrical features of the


142


_Chapter 8 - Conclusions_


WSE does not make it suitable to evaluate other aspects of this phase, such as the interval at which the
range and illuminations constraints are met. This improvement could be pursued through a new Matlab
function that analytically evaluates the desired WSE or using STK’s default segments for rendezvous and
proximity operations. Another interesting update could be adding a thruster set module which is
representative of the properties of SROC’s thruster module. Finally, regarding the analysis of the
communication windows with SROC, it will be necessary to assess if a GEO link is feasible from different
points of view, such as the cost and the system ones.


143


## _Bibliography_


[1] California Polytechnic State Universiy. (2022). _CubeSat Design Specification (1U – 12U), REV 14.1_ .
San Luis Obispo, CA.

[2] NASA. (2017). _CubeSat 101 - Basic Concepts and Processes for First-Time CubeSat Developers._

[3] Walker, R. _Technology_ _CubeSats_ . From The European Space Agency website:
[https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Technology_CubeSats.](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Technology_CubeSats)

[4] _Space Rider_ [. (2023, April 18). Taken from Wikipedia: https://en.wikipedia.org/wiki/Space_Rider](https://en.wikipedia.org/wiki/Space_Rider)

[5] ESA. (2018). _USER GUIDE for the SPACE RIDER Re-usable Free Flyer Platform_ . Ref. ESA-STS-SR-TN
2018-0002

[6] Balossino, A., Battocchio, L., Giacci, M., Guidotti, G., Rufolo, G., Denaro, A., & Paletta, N. (2015).
_Conceptual Design of the Descent Subsystem for the Safe Atmospheric Re-Entry Flight of Space Rider._
7th European Conference for Aeronautics and Space Sciences (EUCASS). DOI:
10.13009/EUCASS2017-624

[7] ESA. (2014, 03 28). _Space Debris Mitigation Policy for Agency Projects_ (ESA/ADMIN/IPOL(2014)2).
Paris.

[8] Analytical Graphics Inc. (2016, March _). STK Object Model_ . Taken from STK 11.0.1 Programming
Interface:
[https://help.agi.com/stkdevkit/11.0/index.html?page=source%2FautomationTree%2FobjModel.htm](https://help.agi.com/stkdevkit/11.0/index.html?page=source%2FautomationTree%2FobjModel.htm)

[9] Analytical Graphics Inc. (2016, March). _Matlab Code Snippet_ . Taken from STK 11.0.1 Programming
Interface:
[https://help.agi.com/stkdevkit/11.0/index.html?page=source%2FstkObjects%2FObjModMatlabCod](https://help.agi.com/stkdevkit/11.0/index.html?page=source%2FstkObjects%2FObjModMatlabCodeSamples.htm)
[eSamples.htm](https://help.agi.com/stkdevkit/11.0/index.html?page=source%2FstkObjects%2FObjModMatlabCodeSamples.htm)

[10] Analytical Graphics Inc. (2023, May). _STK Capabilities - Astrogator_ . Taken from STK Help:
[https://help.agi.com/stk/#gator/astrogator.htm?TocPath=Capabilities%257CAstrogator%257C_____](https://help.agi.com/stk/#gator/astrogator.htm?TocPath=Capabilities%257CAstrogator%257C_____0)
0

[11] D’Amico, S. (2005). _Relative orbital elements as integration constants of Hill’s equations_ . DLR, TN,

05-08.

[12] Vallado, D. (2013). _Fundamentals of Astrodynamics and Applications_, 4th edition. Microcosm Press.

[13] Analytical Graphics Inc. (2023, May). _Vehicle Local Coordinate Axes._ [Taken from STK Help: Vehicle](https://help.agi.com/stk/#gator/eq-coordsys.htm?Highlight=VNC)
[Local Coordinate Axes (agi.com).](https://help.agi.com/stk/#gator/eq-coordsys.htm?Highlight=VNC)

[14] Nerem, R. S., et al. (1994), _Gravity model development for TOPEX/POSEIDON: Joint Gravity Models 1_
_and 2_ . Journal of Geophysical Research, 99( C12), 24421– 24447, doi:10.1029/94JC01376.

[15] R. Mugellesi, D. J. Kerridge (1991). Prediction of solar and geomagnetic activity for ESA low-flying
spacecraft. Proceedings from _2nd International Space Debris Re-entry Workshop_, Vol. 1, Issue 1.

[16] ESA. (2023, May). _Fap_monthly_1+2cycTemps_ . Taken from Index of /SOLMAG:
[https://static.sdo.esoc.esa.int/SOLMAG/.](https://static.sdo.esoc.esa.int/SOLMAG/)

[17] NOAA. _Geomagnetic kp and ap Indices_ . Taken from NOAA - National Centres for Environmental
[Information: https://www.ngdc.noaa.gov/stp/geomag/kp_ap.html.](https://www.ngdc.noaa.gov/stp/geomag/kp_ap.html)

[18] _SPACE RIDER OBSERVER CUBE (SROC) DEMONSTRATOR PHASE B2/C/D_ (ESA-TECMPA-SOW-2023000059).

[19] _Mission Analysis Report_ (SROC-PTO-SYS-TNO-006)

[20] _SROC System Design Definition File_ (SROC-TVK-SYS-DDF-003).

[21] ESA (2022, 02 22). _Debris Risk Assessment and Mitigation Analysis (DRAMA) Software User Manual_
(GEN-SW-SUM-00342-OPS-SD).

[22] ESA (2020, 02 12). _Collision avoidance requirements verification and guidelines based on_
_DRAMA/ARES_ (MIT-COL-MAN-00279-OPS-SD).

[23] ESA (2021, 11 30) _Technical note – Assessment of Risk Even Statistics (ARES)_ MIT-SW-TN-00280-OPS
SD.

[24] ESA (2020, 04 15.) _User Manual – Drama hands-on training: Melpomene_ (MIT-TLS-PR-00267-OPSSD).


144


[25] ESA (2022, 03 23) _Software User Manual – MASTER_ .

[26] ESA-ESTEC (2020, 06 15). _ECSS-E-ST-10-04C (Rev.1) Space engineering – Space environment._

[27] ESA-ESTEC (2012, 06 15). _Margin philosophy for science assessment studies (Rev.3)._

[28] ISO 27852:2016 _Space Systems - Estimation of orbit lifetime_ .

[29] ESA (2021, 11 28) _Material database for re-entry risk verification with SARA_ (MIT-REN-MAN-00324OPS-SD).


[30] Belstead Research Ltd. (2021, 11 2). _RE-ENTRY MODELLING PROCEDURE_ . Ashford, UK.


[31] _Voxel_ [. (2023, May 29). Taken from Wikipedia: Voxel - Wikipedia](https://en.wikipedia.org/wiki/Voxel)

[32] Beck, J., Holbrough, I., Merrifield, J., & Stijn, L. (2021). PROBABILISTIC COMPARISON OF
DESTRUCTIVE RE-ENTRY. _8th European Conference on Space Debris._ _8._ ESA Space Debris Office

[33] IDRS. _IDRS Technology._ Taken from idrsspace: [Technology | Boosting LEO Satellite Fleet Ops](https://www.idrsspace.com/technology)
[Efficiency | IDRS (idrsspace.com).](https://www.idrsspace.com/technology)


145


