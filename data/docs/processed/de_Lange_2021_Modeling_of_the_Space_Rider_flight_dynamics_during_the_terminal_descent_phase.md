# Modeling of the Space Rider flight dynamics during the terminal descent phase

Citation for published version (APA):
de Lange, M., Tóth, R., & Verhoek, C. (2021). Modeling of the Space Rider flight dynamics during the terminal
descent phase. Eindhoven University of Technology.


Document license:
CC BY-NC-SA


Document status and date:
Published: 01/12/2021


Document Version:
Accepted manuscript including changes made at the peer-review stage


Please check the document version of this publication:


- A submitted manuscript is the version of the article upon submission and before peer-review. There can be
important differences between the submitted version and the official published version of record. People
interested in the research are advised to contact the author for the final version of the publication, or visit the
DOI to the publisher's website.

- The final author version and the galley proof are versions of the publication after peer review.

- The final published version features the final layout of the paper including the volume, issue and page
numbers.

[Link to publication](https://research.tue.nl/en/publications/adf56647-1a13-4e4a-9dc6-b0815ca94cd4)


General rights
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners
and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.


- Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
- You may not further distribute the material or use it for any profit-making activity or commercial gain
- You may freely distribute the URL identifying the publication in the public portal.


If the publication is distributed under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license above, please
follow below link for the End User Agreement:

www.tue.nl/taverne


Take down policy
If you believe that this document breaches copyright please contact us at:

openaccess@tue.nl

providing details and we will investigate your claim.


Download date: 05. Sept. 2025


## **Modeling of the Space Rider flight dynamics during the** **terminal descent phase**

_**Author:**_
Matthis de Lange (1009253)


_**Supervisors:**_
dr. ir. Roland T´oth

ir. Chris Verhoek


_**External supervisor:**_
dr. Valentin Preda (ESA)


Eindhoven University of Technology, 2021


Department of Electrical Engineering


## **Abstract**

The European Space Agency (ESA) is developing a module, named the Space Rider (SR). With
the SR it is possible to do research in the earths low orbit. The SR can return to earth and is
capable of landing at a predefined position by means of a guided parafoil. This report discusses,
which dynamical effects are relevant to construct a model, describing the flight dynamics of the
SR during its guided parafoil descend. First the already existing models, which are found in
the literature, are discussed. A 6 degrees of freedom (DoF) and a 12 DoF model is presented.
THe models are simulated in Simulink. The results are analyses and compared with simulation
results found in the literature for an already existing model. The models are linearized and
the flight dynamics of the linearizations are analyzed. It can be concluded that the gravity,
aerodynamics and apparent mass are all relevant to the flight dynamics during the descent of the
SR. The 6 DoF models shows the overall flight behavior needed for position, velocity and heading
control. The 12 DOF model give additional dynamics, which are insightful in the presence of
wind disturbances or during the landing.


1


## **List of Symbols**

Table 1: Model parameters

|Symbol|Definition|Unit|
|---|---|---|
|_g_<br>_ρ_<br>_I_<br>pp<br>_m_p<br>_b_p<br>_c_p<br>_t_p<br>_S_p<br>_µ_<br>_m_<br>pam<br>_I_<br>pam<br>_I_ l<br>l<br>_m_l<br>_S_l<br>_r_cp<br>_r_cam<br>_r_c<br>l<br>_C_Fp<br>_C_Mp<br>_C_Fl<br>_C_Ml<br>_K_t_,⃗r_<br>_K_t_,⃗η_<br>_D_t_,⃗r_<br>_D_t_,⃗η_|Gravity constant<br>Air pressure<br>Parafoil inertia matrix<br>Parafoil mass<br>Parafoil wingspan<br>Parafoil chord<br>Parafoil thickness<br>Parafoil reference area<br>Parafoil rigging angle<br>Parafoil apparent mass matrix<br>Parafoil apparent inertia matrix<br>Load inertia matrix<br>Load mass<br>Load reference area<br>Parafoil mass position vector<br>Apparent mass position vector<br>Load mass position vector<br>Parafoil aerodynamic force coefcients<br>Parafoil aerodynamic moment coefcients<br>Load aerodynamic force coefcients<br>Load aerodynamic moment coefcients<br>Spring coefcient matrix<br>Torsion spring coefcient matrix<br>Damping coefcient matrix<br>Torsion damping coefcient matrix|_ms_~~_−_2~~<br>_kg/m_3<br>_kgm_2<br>_kg_<br>_m_<br>_m_<br>_m_<br>_m_2<br>_rad_<br>_kg_<br>_kgm_2<br>_kgm_2<br>_kg_<br>_m_2<br>_m_<br>_m_<br>_m_<br>_−_<br>_−_<br>_−_<br>_−_<br>_N/m_<br>_N/rad_<br>_Ns/m_<br>_Ns/rad_|



2


## **Contents**

**1** **Introduction** **4**


**2** **Literature review** **6**

2.1 Existing models and complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Apparent mass effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Aerodynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.4 Experimental results and validation . . . . . . . . . . . . . . . . . . . . . . . . . . 8


**3** **Analytical Model** **10**
3.1 Reference frames and rotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

3.2 Aerodynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3 Apparent mass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4 Tension line model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

3.5 Six DoF model of PADS flight dynamics . . . . . . . . . . . . . . . . . . . . . . . 16
3.6 Twelve DoF model model of PADS flight dynamics . . . . . . . . . . . . . . . . . 18
3.7 Additional descriptions of dynamic effects . . . . . . . . . . . . . . . . . . . . . . 20
3.8 Model Composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21


**4** **Implementation and Simulation** **23**
4.1 Simulink model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

4.2 Steady state model behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.3 Dynamic model behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28


**5** **Linearization** **31**


**6** **Validation** **35**

6.1 Steady state flight behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
6.2 Dynamical flight behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


**7** **Discussion and Conclusion** **39**


3


## **1 Introduction**

Research in low earth orbit gives opportunities for experiments and exploration of technology,
which is not possible in a planet environment, because it is dominated by gravity. To overcome
the effect of gravity to do microgravity research, multiple methods are currently used. Like a
vacuum chamber, in which a free fall can be reached, an airplane in parabolic flight or by launching a rocket within the earths atmosphere. The approaches have limitations on the experiment
length up to several minutes. Therefore, ESA is currently developing a module, the Space Rider
(SR), that can do research in low orbit. The SR is launched in low orbit and can stay there for
multiple months to perform microgravity research. Other possible tasks could be validation and
demonstration of robotic exploration, earth observation and telecommunication. Even satellite
inspection is a possibility [1].


One of the objectives of the project is the re-usability of the SR. Therefore, the SR should
return to the earth, such that it is undamaged and retrievable. A strategy is developed for the
decent of the SR. First, the SR re-enters the atmosphere at a high velocity. As following, A
drogue parachute is used to decelerate the SR to a velocity and altitude at which the guided
parafoil can be deployed. With the guided parafoil, the SR ca steer and navigate to the landing
point, where it eventually lands gently. This last part, which is the terminal guidance phase, is
full of challenges. The control of the SR is handled by the Guidance, Navigation and Control
system (GNC) and should be able to guide the SR to a precision landing in the presence of wind
disturbances and ensure a soft landing. A soft landing means an impact with bounded velocity.


One way to quantify the performance of the developed GNC solution is by performing a MonteCarlo simulation for different wind disturbances and creating a normal distribution around the
landing position and the desired impact velocity. This can provide sufficient verification of the
landing precision of the GNC. To support the development of such a simulation environment a
model is needed that captures the relevant descending dynamics of the SR with the parafoil [2].
The developed GNC solution can be improved with the simulation environment. This report
answers the question: Which dynamic effects acting on the SR during the terminal guidance
phase should be considered, to describe the flight dynamics of the Space Rider w.r.t. the desired
landing precision and landing constraints of the GNC system?


The Space Rider during the terminal descent phase is connected to the parafoil with tension
lines as shown in Figure 1. The Space Rider steers itself by deflecting the parafoils trailing edge,
eventually very similar as an airplane would be steered. The steering lines, which are not the
same as the tension lines, connect the trailing edge of the parafoil and the SR. They are controlled by the GNC system. The SR with the guided parafoil falls in the category of precision
aerial delivery systems (PADS) and can be modeled accordingly.


4


Figure 1: The Space Rider guided by a parafoil


Yakimenko [3] gives an overview of some proposed models to capture the flight dynamics of a
PADS. As low fidelity model a 3 DoF model is used, assuming a point mass moving with a
velocity in three directions. The complexity is increased with a 6 DoF model, where the whole
system is assumed to be one rigid body. By including some relative DoF between the parafoil
and the load a 7-9 DoF model can be created. A 12 DoF model is obtained when the load can

move in all six directions relative to the parafoil. The models included aerodynamics, apparent
mass and gravity as dynamc effects.


The report structure is as following. First, a literature overview is given. The existing models,
which describe the flight dynamics of a PADS are presented, in terms of the included dynamic
effects. Next a 6 DoF mathematical model is proposed for a PADS, which is extended to a 12
DoF model. In the models, the aerodynamic effect, apparent mass effect and the gravity will
be considered. As following the implementation of these mathematical models in Simulink is
shown and the flight dynamics are analyses through simulation of the model implementation.
Especially, the contribution of the apparent mass to the flight dynamics and the differences in the
flight dynamics between the 6 DoF and the 12 DoF models are analyzed. With the simulation
results, the model is linearized in multiple operation points. The dynamic flight behavior of the
linear models gives an overview of flight dynamics of the overall model and also gives an inside
in the non-linearity of the overall model. This gives an insight to improve the GNC solution.
Lastly, some notes are given on the presented work, together with future recommendations and
a conclusion is made. w.r.t. the research question.


5


## **2 Literature review**

In the literature a lot of different models, representing the flight dynamics of a PADS, are
available. The presented models have varying complexity from 3-4 DoF models, 6 DoF models,
7-9 DoF models and a 12 DoF model. Furthermore, the models can be characterized by the
included dynamics effects and how these dynamics are included. Sec. 2.1 describes the complexity
order of the models and the included dynamc effects. Additional literature of the dynamic effects
is discussed in Sec. 2.2 and 2.3. Also simulation parameters simulation results and experimental
results are found in the literature and are discussed in Sec. 2.4.


**2.1** **Existing models and complexity**


For each model complexity the included dynamic effects are discussed. the models are presented
in order of complexity. The 3 DoF models are described by Yakimenko [4], Bonaccorsi [5] and
Rademacher [6]. The model consists of a point mass, which can move in the x-y-z direction,
with a velocity vector. The acting forces on the system are the gravity and aerodynamic lift and
drag. The aerodynamics are modeled with a constant trim coefficient, which can be altered for
the control deflections. With the control deflections the system can be decelerated and steered.
A delay is used to approximate the repose time of the system to a control input. The output of
the system are the position and velocity and the inputs are the control deflections. The wind is
embedded as the disturbance. Yakimenko extends the model in [4] to a 4 DoF model by including
a yawing rate in the model.


The model complexity is increased with the 6 DoF model, described by Figueroa-Gonz´alez [2],
Yakimenko [3], [4], Bonaccorsi [5], Ward [7], and Mazouz [8]. The PADS is represented as one
rigid body with a single mass and inertia. The model can move along the axis of a Cartesian coordinate system, but also rotate with the Euler angles. The model therefore considers the velocity
vector but also the angular velocity. In the 6 DoF models the following dynamic effects are included. The gravity, still works the same as in the 4-3 DoF models. The aerodynamics, consisting
of a drag, lift and side force as well as three aerodynamic moments. The aerodynamic coefficients
are used to express the aerodynamic force and moment. These coefficients can be described with
a linear model in an operation range as used by Yakimenko [3], [4], Bonaccorsi [5] and Mazouz [8]
or with a mix of a look-up table and a linear model as is used by Figueroa-Gonz´alez [2]. In a
6 DoF model the apparent mass can be included. The apparent mass describes additional pressure forces on the body. Figueroa-Gonz´alez [2] argues that the effect is not significant for their
application. They say it is only relevant for application with loading more than 5 [ _Kg/m_ [2] ].
Yakimenko [4], Bonaccorsi [5] and Mazouz [8] argue it is important for their application. They
implement the apparent mass effect, with the momentum and angular momentum of the apparent
mass being decoupled in a center of apparent mass. Yakimenko [3] also implements the effect in
a version where the momentum and angular momentum of the apparent mass are not decoupled.
The output of the model describes the position and orientation of rigid body with its velocity
and angular rate. The input of the model are the control deflections and the wind is a disturbance.


The system derived by Ward [9] is considered a 6 DoF model. Even though the paper considers the parafoil and the load as separate rigid body, it also uses rigid connections to connect
both bodies. These rigid lines can be controlled to vary the center of mass (CoM) of the system
steer the direction of the system. The type aerodynamic model is the same as used by Yakimenko [4]. The apparent mass is considered, but the implementation manner remains unclear.


6


A 7-9 DoF model includes relative degrees to freedom between the parafoil and the load. Yakimenko [4] shows three models for 7-9 DoF. The aerodynamic and gravity are separated in a set
of dynamic effects for the load and for the parafoil. Each degree of freedom represents an extra
rotation the load can make, in an attachment point, w.r.t. the parafoil. The expressions for the
aerodynamics of the load and parafoil are similar to the expressions used in the 6 DoF model.
The apparent mass is considered in decoupled form.


Redelinghuys [10], Sleger [11], Yakimenko [3] and Zhu [12] all present an 8 DoF model. Zhu [12]
allows a relative pitch and yaw angle between the load and the parafoil. The relative motion is
constraint with tension forces. A torsional spring-damper system is used. To model the aerodynamics, the parafoil is divided in multiple panels and the aerodynamic drag and lift are modeled
per panel. The aerodynamic moment is derived as a result of the aerodynamic force. The load
is only influenced by a drag component. A linear model is used to determine the aerodynamic
coefficients and a coupled apparent mass effect is considered. The 8 DoF model developed by [11]
considers the same relative pitch and yaw angles as additional degrees of freedom. The same
approach is used to constrain the relative angles, with tension forces. The aerodynamics are considered the same as used by Yakimenko [4]. The apparent mass effect is considered in decoupled
form. Yakimenko [3] develops a general model structure for an 8 DoF model, but does not show
how specific components can be modeled.


A different type of model is introduced by Redelinghuys [10]. The added DoF are still a relative
pitch and yaw angle. Instead of defining the model along the classical Newtonian formulations,
the model presented is based on the Hamiltonian approach. A non-linear restoring moment is
formulated on the relative yaw angle. The paper considers the combination of a parafoil with
an unmanned air vehicles (UAV). Therefore, a full aerodynamic expression is used for both
the parafoil and the load. This includes a drag, lift and side force and all three aerodynamic
moments. The coefficients for the parafoil are calculated with Computational Fluid Dynamics
(CFD) and a fit was determined on top of the lookup table. This gives a linearization in a moving
operation point. The aerodynamic coefficients of the UAV are constant and the apparent mass
is not included.


A 12 DoF model is presented by Glouchtchenko [13]. Both the parafoil and the load are considered as a rigid body. The aerodynamic forces and gravity are separately modeled on both
bodies. A suspension line model is proposed as a spring damper system. Four suspension lines
are modeled into one single joint. The parafoil is connected to the joint with a half rigid and half
spring damper connection. This brings as difficulty that the position of the joint is determined
by solving the force balance of multiple spring damper systems. The aerodynamics are partly
determined via a look-up map and with a linear model. The apparent mass is embedded in
coupled form in the parafoil rigid body.


To conclude, the 3-4 DoF models are used when considering only steady-state flight dynamics, due to the constant aerodynamic coefficients. The turning response is an approximation
with a delay. The 6 DoF models are used to consider the dynamic behavior of the system and
has varying steady-state flight dynamics due to a more comprehensive aerodynamic model with
varying aerodynamic coefficients. Due to the implementation of an inertia and the moments
working on the system, the 6 DoF model can turn with all three Euler angles. A 7-9 DoF model
is used to express some relative DoF between the load and the parafoil, these extra DoF can be
constraint with spring-damper systems. A 12 DoF model give the load full relative movement
freedom with respect of the parafoil, the relative DoF is constraint with multiple spring-damper


7


systems representing the tension lines. All presented models consider the gravity and the aerodynamics relevant for the flight dynamics of the PADS. The 6-12 DoF model considers a more
comprehensive expression for the aerodynamics, than the 3-4 DoF models. In the 6-12 DoF
models the aerodynamic coefficients can be modeled in a linear model, a look-up table or a mixture of both. The aerodynamic coefficients are obtained via analytical expressions, experimental
result or CFD analyzes. The apparent mass is only included as relevant to the flight dynamics
in the 6-12 DoF models. The apparent mass can be included in the 6-12 DoF models. Not all
papers included the apparent mass, based on the application. The apparent mass is included
in to manners. The first one considers the momentum and angular momentum of the apparent
mass to be decoupled, while the second approach considers it coupled. The apparent mass is
discussed further in Sec. 2.2.


**2.2** **Apparent mass effect**


The apparent mass effect on a PADS is described by Lissaman and Brown [14] and by Barrows

[15]. Here Lissaman and Brown [14] describes the relevance of the apparent mass effect on
parafoil-load systems as: ’very significant for vehicles with wing load of the order less than 5

[ _Kg/m_ [2] ] and exceedingly important if the lifting surface is significantly displaced from the major
mass’. They derive in [14] representations, which approximates the effect with a diagonal mass
matrix and diagonal inertia matrix. As result the momentum and angular momentum of the
apparent mass are decoupled. The paper also shows how to derive the mass and inertia matrix.
Barrows shows in [15] that for an arced parafoil system the decoupled from is in general not
true. The paper presents a method to determine coupled representation of the force and moment
equations. Also additions to calculated the coupled mass and inertia matrix are presented. In a
PADS model the apparent mass effect is of importance, since the lifting surface is significantly
displaced from the major mass. The decoupled form is still used as a simpler approximation of
the apparent mass, It disregards of diagonal term between the mass and inertia matrix.


**2.3** **Aerodynamics**


One of the most important parts of the model is the set of aerodynamic forces and moments,
which depend on the aerodynamic coefficients. Obtaining the aerodynamic coefficients or an
expression for the coefficients is not trivial. For airplane wings the lifting line theory is suitable
to derive the aerodynamic coefficients [16], but this theory does not full capture the aerodynamic
effect of a parafoil [17]. Bennett and Fox [18] describes how a set of coefficient is obtained experimentally. On the basis of this, Lingard [17] and Jann [16] try to extend the lifting line theory
with the experimental results. They tried to obtain a general expression based on the parafoil
geometry. It is shown that the theory matches the experimental results within a certain regions.
M¨uller [19] describes a software tool in which the aerodynamic coefficients can be obtained numerically through CFD. The tool is verified with test flight data. In general all methods give set
of coefficients suitable for an PADS model within a operation range. The CFD method can be
scaled easily.


**2.4** **Experimental results and validation**


Although the papers, given in Sec 2.1-2.3 present a model. Neither of those papers present a full
set of simulation parameters as well as a full set of simulation results or experimental data. Most


8


papers present the model as part of a developed control strategy and only show results related to
the control solution. Some papers present a complete set of model parameters like [20], but not
an extensive set of result to validate the model with. Other papers present simulation or experiment results, but not enough of the used model parameter as in [7] and [18]. Glouchtchenko [13]
gives a model validation based on simulations made by Van der Kolf [21], who gives a complete
set of parameters including a extensive set of aerodynamic parameters. Multiple typos where
found in the aerodynamic parameters. Van der Kolf presents data of both steady state flight
behavior and dynamic flight behavior. The model Van der Kolf is simulating is a 8 DoF model,
but his data can be used to validate general dynamics.


9


## **3 Analytical Model**

In this section the analytical models are derived. First the reference frames are introduced.
The orientation, velocity and angular velocity vectors are defined and the rotation matrices are
given. The aerodynamic model, apparent mass and tension line model are described next. Then
the 6 DoF model and the 12 DoF models are derived. Lastly, the general model is composted.
The model is created using [4], [8], [2] and [9]. These models represents the PADS as one rigid
body. With the use of [22] and [13] the 6 DoF model is extended to a 12 DoF model in which
the parafoil and the payload are considered as two separate rigid bodies. The two bodies are
connected with tension lines. The PADS system is shown as a schematic representation in Figure
2. The following assumptions are made


 The parafoil is treated as a rigid body of fixed shape once completely inflated.


 The apparent mass center corresponds to the parafoils center of mass.


Figure 2: Schematic representation of PADS


**3.1** **Reference frames and rotations**


Four reference frames are defined for modeling purposes. The reference frames are shown in
Figure 2 and the reference frames will be denoted with a super script. The first frame is the
North-East-Down or world frame denoted by _{_ n _}_, which is an inertial frame fixed in a planetary


10


point. The frame axis are denoted as _x_ [n], _y_ [n] and _z_ [n] . The _x_ [n] axis is positive towards the north,
the _y_ [n] axis is positive towards the east and the _z_ [n] axis is positive pointing towards the center of
the planet.


The model is derived in a body fixed frame. Three body fixed reference frames will be used.
Firstly, a body fixed frame in the center of mass of the rigid body will be used for the 6 DoF
model. This frame is denoted with _{_ c _}_, with the axis _x_ [c] positive along the longitudinal axis of
the PADS in the plane of symmetry, the _z_ [c] axis is perpendicular to the _x_ [c] axis positive pointing
down and the _y_ [c] axis is perpendicular to the _x_ [c] - _z_ [c] plane, positive defined by the right-hand rule.


Secondly, a body fixed frame is used in the center of mass of the parafoil, denoted with _{_ p _}_ . The
axis _x_ [p] is positive along the longitudinal axis of the parafoil in the plane of symmetry, the _z_ [p]

axis is perpendicular to the _x_ [p] axis positive pointing down and the _y_ [p] axis is perpendicular to
the _x_ [p] - _z_ [p] plane positive defined by the right-hand rule.


Lastly, a body fixed frame is placed in the center of mass of the load. The frame is denoted with
_{_ l _}_ and the axis _x_ [l] is positive along the longitudinal axis of the load in the plane of symmetry,
the _z_ [l] axis is perpendicular to the _x_ [l] axis positive pointing down and the _y_ [l] axis is perpendicular
to the _x_ [l] - _z_ [l] plane positive defined by the right-hand rule.


In each body fixed frame the orientation w.r.t. the _{_ n _}_ frame can be represented in Euler
angles. The angle _ϕ_ represents a rotation around the x-axis, _θ_ a rotation around the y-axis and
_ψ_ a rotation around the z-axis. This is summarized as _⃗η_ = � _ϕ_ _θ_ _ψ_ [�] _[⊤]_ . In a body fixed frame
these angles could also be referred to as roll, pitch and yaw. _µ_ is a specific defined angle. It
describes the relative rotation between the parafoil frame and the rigid body frame around the
y-axis. The meaning of _µ_ is also shown in Figure 2. The velocity in each frames is denoted with
_⊤_ _⊤_
( _V_ _[⃗]_ ) and is decomposed in � _u_ _v_ _w_ � . The angular velocity _⃗ω_ is decomposed as � _p_ _q_ _r_ � .
The time derivative of the Euler angles of an arbitrary body fixed frame _{_ b _}_ can be determined

as



_d⃗η_ [b]

_dt_ [(] _[⃗ω]_ [b] _[, ⃗η]_ [b] [) =]



1 sin( _ϕ_ [b] ) tan( _θ_ [b] ) cos( _ϕ_ [b] ) tan( _θ_ [b] )

 0 cos( _ϕ_ [b] ) _−_ sin( _ϕ_ [b] )

 0 _−_ sin( _ϕ_ [b] ) cos(1 _θ_ [b] ) cos( _ϕ_ [b] ) cos(1 _θ_ [b] )









_⃗ω_ [b] _._ (1)



~~�~~ ~~�~~ � ~~�~~

_T_


Any vector in a frame can be rotated to another frame with the Euler angles by multiplying with
one or multiple of the corresponding matrices as



 _,_ _R_ ( _θ_ [b] ) =







 _,_



 cos(0 _θ_ [b] ) 01 _−_ sin(0 _θ_ [b] )

 sin( _θ_ [b] ) 0 cos( _θ_ [b] )



(2)



_R_ ( _ψ_ [b] ) =



 _−_ cos(sin( _ψψ_ [b][b] )) cos(sin( _ψψ_ [b][b] )) 00

0 0 1






 _,_



_R_ ( _ϕ_ [b] ) =



 10 cos(0 _ϕ_ [b] ) sin(0 _ϕ_ [b] )

 0 _−_ sin( _ϕ_ [b] ) cos( _ϕ_ [b] )



such that a rotation with al three Euler angles would result in


_R_ ( _⃗η_ [b] ) = _R_ ( _ψ_ [b] ) _R_ ( _θ_ [b] ) _R_ ( _ϕ_ [b] ) _._ (3)


The rotation order matters and is defined as above. By using Euler angles there is a chance
that gimbal lock will occur in the model. If for instance, if the angle _θ_ becomes [1] 2 _[π]_ [ the rotation]


11


matrices lose a degree of freedom and also its rank. A rotation with _ϕ_ or _ψ_ will result in the
same rotation around the z-axis, but a rotation around the x-axis is not possible. The model
for the PADS should not operate at _θ_ = [1] 2 _[π]_ [, in normal operation conditions, but it is possible.]

This phenomena is avoided by expressing the orientation in quaternions. Quaternions are a
generalization of the complex numbers and are formally written as _q_ 0 + _q_ 1 _i_ + _q_ 2 _j_ + _q_ 3 _k_ . _q_ _i_ is a
real number. _i, j, k_ are the direction vectors. The properties of _i, j, k_ are given in [23]. By using
quaternion w.r.t Euler angles an intuitive understanding of the angle is lost. Therefore, the model
is presented in Euler angles, but implemented in Simulink in quaternions. The orientation in
_⊤_
quaternions is described as _⃗q_ = � _q_ 0 _q_ 1 _q_ 2 _q_ 3 � . A vector can be rotated from the world
frame to an arbitrary body fixed frame _{_ b _}_ with the rotation matrix following [23] defined as



2 � _q_ 0 [b] _[q]_ 3 [b] [+] _[ q]_ 1 [b] _[q]_ 2 [b] � ( _q_ 0 [b] [)] [2] _[ −]_ [(] _[q]_ 1 [b] [)] [2] [ + (] _[q]_ 2 [b] [)] [2] _[ −]_ [(] _[q]_ 3 [b] [)] [2] 2 � _q_ 2 [b] _[q]_ 3 [b] _[−]_ _[q]_ 0 [b] _[q]_ 1 [b] �



_R_ ( _⃗q_ [b] ) =



 (2 _q_ � 0 [b] _q_ [)] 0 [b][2] _[q]_ [ + (] 3 [b] [+] _[q][ q]_ 1 [b] 1 [b] [)] [2] _[q][ −]_ 2 [b] � [(] _[q]_ 2 [b] [)] [2] _[ −]_ [(] _[q]_ 3 [b] [)] [2] 2( _q_ � 0 [b] _q_ [)] 1 [b][2] _[q][ −]_ 2 [b] _[−]_ [(] _[q]_ 1 [b] _[q]_ 0 [b] [)] [2] _[q]_ [ + (] 3 [b] � _[q]_ 2 [b] [)] [2] _[ −]_ [(] _[q]_ 3 [b] [)] [2] 22 �� _qq_ 02 [b][b] _[q][q]_ 23 [b][b] [+] _[−][ q][q]_ 10 [b][b] _[q][q]_ 31 [b][b] ��

 2 � _q_ 1 [b] _[q]_ 3 [b] _[−]_ _[q]_ 0 [b] _[q]_ 2 [b] � 2 � _q_ 0 [b] _[q]_ 1 [b] [+] _[ q]_ 2 [b] _[q]_ 3 [b] � ( _q_ 0 [b] [)] [2] _[ −]_ [(] _[q]_ 1 [b] [)] [2] _[ −]_







2 � _q_ 1 [b] _[q]_ 3 [b] _[−]_ _[q]_ 0 [b] _[q]_ 2 [b] � 2 � _q_ 0 [b] _[q]_ 1 [b] [+] _[ q]_ 2 [b] _[q]_ 3 [b] � ( _q_ 0 [b] [)] [2] _[ −]_ [(] _[q]_ 1 [b] [)] [2] _[ −]_ [(] _[q]_ 2 [b] [)] [2] [ + (] _[q]_ 3 [b] [)] [2]



 _._



(4)
The time derivative of the quaternion representation _⃗q_ [b] for an arbitrary body fixed frame _{_ b _}_ is
given as





b
 _⃗ω_ _._ (5)



_−q_ 1 [b] _−q_ 2 [b] _−q_ 3 [b]
_q_ 0 [b] _−q_ 3 [b] _q_ 2 [b]
_q_ 3 [b] _q_ 0 [b] _−q_ 1 [b]
_−q_ 2 [b] _q_ 1 [b] _q_ 0 [b]



_d⃗q_ [b]



_q_

_dt_ [(] _[⃗ω]_ [b] _[, ⃗q]_ [b] [) = 1] 2



2









**3.2** **Aerodynamics**


The aerodynamics of the PADS system can be separated in the aerodynamics of the parafoil and
the load, working in the parafoil frame and load frame respectively. The aerodynamics of the
parafoil are described with the parafoil aerodynamic force ( _F_ _[⃗]_ p [p] a [) and moment (] _[ ⃗M]_ [ p] p a [) as]

_⃗F_ p [p] a [(] _[⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [) =] _ρ||V_ _[⃗]_ p [p] _,_ air 2 _[||]_ 2 [2] _[S]_ [p] _R_ ( _α_ p _, β_ p ) _C_ Fp ( _α_ p _, β_ p _, V_ _[⃗]_ p [p] _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [)] _[,]_

_⃗M_ p [p] a [(] _[⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [) =] _ρ||V_ _[⃗]_ p [p] _,_ air 2 _[||]_ 2 [2] _[S]_ [p] _C_ Mp ( _α_ p _, β_ p _, V_ _[⃗]_ p [p] _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [)] _[,]_



_w_ p [p] _,_ air
_α_ p = tan _[−]_ [1]
� _u_ ~~[p]~~ p _,_ air



�



(6)



_,_



_β_ p = tan _[−]_ [1]







_v_ p [p] _,_ air


p [2]

 ~~�~~ _u_ p _,_ air [+]



p [2] p [2]
_u_ p _,_ air [+] _[ w]_ p _,_ air





 _,_



here _ρ_ is the air density, _S_ p is the aerodynamic reference area of the parafoil, _V_ _[⃗]_ p [p] _,_ air [is the air]
velocity of the parafoil. _α_ p is the angle of attack of the parafoils air velocity and _β_ p is the sideslip
angle of the parafoil air velocity. _⃗ω_ p [p] [is the angular velocity of the parafoil.] _[ C]_ [Fp] [and] _[ C]_ [Mp] [are the]
vectors with aerodynamic coefficients for the parafoil. _δ_ r and _δ_ l are the relative right and left
parafoil deflection respectively. The aerodynamics of the load are described in the same manner


12


with the aerodynamic force ( _F_ _[⃗]_ l [l] a [) and the aerodynamic moment (] _[ ⃗M]_ [ l] l a [) as]


_ρ||V_ _[⃗]_ l [l] _,_ air _[||]_ 2 [2] _[S]_ [l]
_⃗F_ l [l] a [(] _[⃗V]_ [ l] l _,_ air _[, ⃗ω]_ l [l] [) =] 2 _R_ ( _α_ l _, β_ l ) _C_ Fl ( _α_ l _, β_ l _, V_ _[⃗]_ l [l] _,_ air _[, ⃗ω]_ l [l] [)] _[,]_

_ρ||V_ _[⃗]_ l [l] _,_ air _[||]_ 2 [2] _[S]_ [l]
_⃗M_ l [l] a [(] _[⃗V]_ [ l] l _,_ air _[, ⃗ω]_ l [l] [) =] 2 _C_ Ml ( _α_ l _, β_ l _, V_ _[⃗]_ l [l] _,_ air _[, ⃗ω]_ l [l] [)] _[,]_



_α_ l = tan _[−]_ [1] _w_ l [l] _,_ air
� _u_ [l] l _,_ air



�



(7)



_,_





 _,_







_β_ l = tan _[−]_ [1]







_v_ l [l] _,_ air
 ~~�~~ _u_ [l] l _,_ [2] air [+]



_u_ [l] l _,_ [2] air [+] _[ w]_ l [l] _,_ [2] air



here _V_ _[⃗]_ l [l] _,_ air [is the air velocity of the load,] _[ α]_ [l] [ and] _[ β]_ [l] [ are the angle of attack and the slideslip]
angle of the load. _⃗ω_ l [l] [is the angular velocity of the load.] _[ C]_ [Fl] [ and] _[ C]_ [Ml] [ are the vectors with the]
aerodynamic coefficients of the load. It should be noted that depending on the geometry of
the load the given expression may be over complicated. Depending on the geometry, it could
be that the lift and side component are not significant and only the drag component is considered.



The aerodynamic coefficients can be obtained through the lifting line theory [24], [16], computed
from measurement data [18] or calculated via Computational Fluid Dynamics (CFD) [19], [2].
The coefficients are highly nonlinear and dependent on a lot of different variables. Different
papers use different manners to implement this. One of the solutions is a linearization around
an operation point as is used in [9]. The other end of the spectrum is the use of a look-up table
in which the coefficients for specific variables will be obtained through interpolation on known
data as is used in [2]. A lot of papers use a mixture between both methods. [10] developed a
linearization in a moving operation point. The dependencies chosen for the aerodynamic coefficients are _α_, _β_, the dimensionless angular velocity (¯ _ω_ ), the symmetrical deflection ( _δ_ s ), and
the asymmetric deflection ( _δ_ a ). For an arbitrary reference frame _{_ b _}_, the dimensionless angular
velocity is given as

_p_ ¯ [b] _b_ b _p_ [b]

¯ 1

   

[b] [b]



_p_ ¯ [b]


¯



_q_ [b]

_r_ ¯ [b]





_c_ b _q_ [b]

_b_ b _r_ [b]







_._ (8)








_q_ ¯ [b]

_r_ ¯ [b]







1

=
 2 _||V_ _[⃗]_ b [b] _,_



2 _||V_ _[⃗]_ b [b] _,_ air _[||]_



 _bc_ bb _pq_ [b][b]

 _b_ b _r_ [b]



The symmetric and asymmetric deflection ( _δ_ s ) and ( _δ_ a ) are determined as


_δ_ s = min( _δ_ r _, δ_ l ) _δ_ a = _δ_ r _−_ _δ_ l _._ (9)


The aerodynamic coefficients for the parafoil used in this research are given as follows,





 =



_−C_ D _,_ p ( _α_ p _, δ_ s )

 _C_ Y _β,_ p _β_ p + _C_ Yp _,_ p _p_ ¯ [p] + _C_ Yr _,_ p _r_ ¯ p + _C_ Y _δ_ a _,_ p _δ_ a

 _−C_ L _,_ p ( _α_ p _, δ_ s )










_,_




_C_ Fp =


_C_ Mp =



_−C_ D _,_ p



_C_ Y _,_ p
 _−C_ L _,_ p



_C_ l _,_ p



_C_ m _,_ p
 _C_ n _,_ p







_C_ l _β,_ p _β_ p + _C_ lp _,_ p _p_ ¯ [p] + _C_ lr _,_ p _r_ ¯ [p] + _C_ l _δ_ a _,_ p _δ_ a

 _C_ m _,_ p ( _α_ p _, δ_ s ) + _C_ mq _,_ p _q_ ¯ [p]

 _C_ n _β,_ p _β_ p + _C_ np _,_ p _p_ ¯ [p] + _C_ nr _,_ p _r_ ¯ [p] + _C_ n _δ_ a _,_ p ( _δ_ s



(10)





 =













_C_ n _β,_ p _β_ p + _C_ np _,_ p _p_ ¯ [p] + _C_ nr _,_ p _r_ ¯ [p] + _C_ n _δ_ a _,_ p ( _δ_ s _, δ_ a )



13


which is a mixture between a linear model and a lookup table. The aerodynamic coefficients for
the load are given via a linear model as





 _,_



 =



_−C_ D0 _,_ l _−_ _C_ D _α,_ l _α_ l [2]

 _C_ Y _β,_ l _β_ l

 _−C_ L0 _,_ l _−_ _C_ L _α,_ l _α_ l



_C_ Fl =


_C_ Ml =


**3.3** **Apparent mass**



_−C_ D _,_ l

 _C_ Y _,_ l

 _−C_ L _,_ l



(11)



_C_ l _,_ l

 _C_ m _,_ l

 _C_ n _,_ l



 =



_C_ m0 _,_ l + _C_ m _α,_ l _α_ l + _C_ mq _,_ l _q_ ¯ [l]

_C_ n _β,_ l _β_ l + _C_ np _,_ l _p_ ¯ [l] + _C_ nr _,_ l _r_ ¯ [l]



_C_ l _β,_ l _β_ l + _C_ mp _,_ l _p_ ¯ [l] + _C_ mr _,_ l _r_ ¯ [l]


¯

 _C_ m0 _,_ l + _C_ m _α,_ l _α_ l + _C_ mq _,_ l _q_ [l]

 _C_ n _β,_ l _β_ l + _C_ np _,_ l _p_ ¯ [l] + _C_ nr _,_ l _r_ ¯ [l]







 _._



The apparent mass describes the effect of an moving body through a fluid and setting the fluid
in motion. The moving fluid results in pressure forces on the body. Therefore, the body takes
additional energy to move [14]. The effect is not widely used in all applications for a body moving through fluid or air. The apparent mass effect is minimal if the mass of the body is much
larger than the mass of the air set into motion. For lighter than air vehicles and parachutes this
effect can be significant. For systems in which the lifting surface is significantly displaced from
the major mass, the apparent mass effect is exceedingly important [14]. Lissaman and Brown
describe in [14] how the energy of the moving fluid can be captured as


2 _T_ = _Au_ [2] + _Bv_ [2] + _Cw_ [2] + _I_ _A_ _p_ [2] + _I_ _B_ _q_ [2] + _I_ _C_ _r_ [2] _._ (12)


Figure 3: Volumetric Representation of the apparent mass (Lissaman and Brown) [14]


From here on it is assumes that the mass of the moving fluid is capture in an ellipsoidal body.
For each direction a different ellipsoidal body is modeled, as shown in Figure 3. One apparent
mass center is found such that the apparent mass matrix ( _m_ [p] p m [) and the apparent inertia matrix]
( _I_ p [p] m [) are defined as]



_I_ A 0 0

 0 _I_ B 0

 0 0 _I_ C



 _._ (13)





_m_ [p]
p m [=]



 _A_ 0 _B_ 0 00


0 0 _C_




 _I_ [p]

 p m [=]







In [14] expressions are given to determined the apparent mass and inertia matrices. The resulting
force ( _F_ _[⃗]_ p [p] m [) and moment (] _[ ⃗M]_ [ p] p m [) of the moving mass in the body are expressed as]



= _−m_ [p] p m _dV_ _[⃗]_ _dt_ p [p] _,_ air _−_ _⃗ω_ p [p] _[×][ m]_ [p] p m _[⃗V]_ [ p] p _,_ air (14)

�


14



_⃗F_ [p]
p m



_dV_ _[⃗]_ _dt_ p [p] _,_ air _, V_ _[⃗]_ p [p] _,_ air _[, ⃗ω]_ p [p]
�


and

_⃗M_ [p]
p m



_d⃗ω_ p _d⃗ω_ [p]
� _dt_ p _[, ⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] � = _−I_ p [p] m _dt_ p _[−]_ _[⃗V]_ [ p] p _,_ air _[×][ m]_ [p] p m _[⃗V]_ [ p] p _,_ air _[−]_ _[⃗ω]_ p [p] _[×][ I]_ p [p] m _[⃗ω]_ p [p] _[.]_ (15)



where _V_ _[⃗]_ p [p] _,_ air [is the parafoil velocity. The term] _[ ⃗V]_ [ p] p _,_ air _[×][ m]_ [p] p m _[⃗V]_ [ p] p _,_ air [can be neglected as it may also]

_dV_ _[⃗]_ p [p] _,_ air = _dV_ _[⃗]_ p [p]
be considered in the aerodynamics [4], [11]. Following Yakimenko [4] _dt_ _dt_ [. The time]
dependency of the wind vector and the orientation are disregarded. Barrows argues in [15] that
in general finding one single center of apparent mass is not trivial. Therefore, it is impossible to
decouple the equations of motion in one single point. A total apparent momentum ( _P_ _[⃗]_ p [p] m [) and]
angular momentum ( _H_ _[⃗]_ p [p] m [) is found as]

 _⃗P_ p [p] m   p m _D_ p [p] m   _⃗V_ p [p] _,_ air 

_[m]_ [p]







 _⃗V_ p [p] _,_ air


_⃗ω_ [p]

 p







_⃗P_ [p]

 p m

_⃗H_ [p]
 p m













 =







_D_ [p]
p m p m

_D_ [p] _[⊤]_ _I_ [p]
 _[m]_ p [p] m p m



_⃗ω_ [p]
p



_,_ (16)




with _D_ [p]
p m [as a matrix with the coupling terms. The resulting force and moment can be written]

as



_⃗F_ [p]
p m


and


_⃗M_ [p]
p m



_dV_ _[⃗]_ _dt_ p [p] _,_ air _,_ _[d⃗ω]_ _dt_ p [p] _[, ⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p]
� �



_dV_ _[⃗]_ _dt_ p [p] _,_ air _,_ _[d⃗ω]_ _dt_ p [p] _[, ⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p]
� �



= _−m_ [p] p m _dV_ _[⃗]_ _dt_ p [p] _,_ air _−_ _D_ p [p] m _d⃗ωdt_ p [p] _[−]_ _[⃗ω]_ p [p] _[×][ m]_ [p] p m [(] _[⃗V]_ [ p] p _,_ air _[−]_ _[D]_ p [p] m _[⃗ω]_ p [p] [)] (17)



(18)



= _−D_ p [p] m _[⊤]_ _dV_ _[⃗]_ _dt_ p [p] _,_ air _−_ _I_ p [p] m _d⃗ωdt_ p [p] _[−]_ _[⃗V]_ [ p] p _,_ air _[×][ m]_ [p] p m [(] _[⃗V]_ [ p] p _,_ air _[−]_ _[D]_ p [p] m _[⃗ω]_ p [p] [)]


_−⃗ω_ p [p] _[×][ m]_ [p] p m _[D]_ p [p] m _[⊤]_ _[⃗V]_ [ p] p _,_ air _[−]_ _[⃗ω]_ p [p] _[×][ I]_ p [p] m _[⃗ω]_ p [p]



Despite of this [4,7,8,20] all assume that a single centroid for the apparent mass can be found.
For simplicity and to study the added effect of the apparent mass, this approach will be used in
this research.


**3.4** **Tension line model**


In the 12 DoF model, a tension line model connects the parafoil to the load. The tension
lines are modeled as a spring-damper system, with an equilibrium vector. The tension line can
be stretched and compressed in each direction separately with a different spring and damping
constant. The equilibrium vector is equal to the relative position vector of the the load w.r.t.
the parafoil. On top a torsion spring-damper system is used to constrain the relative rotation
between the bodies. For each angle a different stiffness and damping is set. The parafoil tension
force ( _F_ _[⃗]_ p [p] t [) and moment (] _[ ⃗M]_ [ p] p t [) are represented as]



= _−K_ t _,⃗r_ ( _⃗r_ t [p] _[−]_ _[⃗r]_ [ p] eq [)] _[ −]_ _[D]_ [t] _[,⃗r]_
�


= _−K_ t _,⃗η_ ( _⃗η_ [t] _−_ _⃗η_ [eq] ) _−_ _D_ t _,⃗η_
�



_d⃗η_ t
� _dt_



_,_
�



(19)

_,_
�



_⃗F_ [p]
p t


_⃗M_ [p]
p t



� _⃗r_ t [p] _[, d⃗r]_ _dt_ t [ p]

_⃗η_ [t] _,_ _[d⃗][η]_ [ t]
� _dt_



_d⃗r_ t p
� _dt_



in which _K_ t _,⃗r_ is diag([ _k_ t _,_ x _k_ t _,_ y _k_ t _,_ z ]) with the stiffness coefficients and _D_ t _,⃗r_ is diag([ _d_ t _,_ x _d_ t _,_ y _d_ t _,_ z ])
with damping coefficients. _⃗r_ t [p] is the relative position vector w.r.t. to the parafoil. _K_ t _,⃗η_ is


15


diag([ _k_ t _,ϕ_ _k_ t _,θ_ _k_ t _,ψ_ ]) with stiffness coefficients and _D_ t _,⃗η_ is diag([ _d_ t _,ϕ_ _d_ t _,θ_ _d_ t _,ψ_ ]) with damping
coefficients. _⃗η_ [t] is the load orientation w.r.t. the parafoil. The tension force ( _F_ _[⃗]_ l [l] t [) and moment]
( _M_ _[⃗]_ l [l] t [) acting on the load and are expressed as]



� _⃗r_ t [p] _[, d⃗r]_ _dt_ t [ p]



_⃗η_ [t] _,_ _[d⃗][η]_ [ t]
� _dt_



_,_
�



(20)

_._
�



_⃗F_ l [l] t



� _⃗r_ t [p] _[, ⃗η]_ [ t] _[,]_ _[d⃗r]_ _dt_ t [ p]



= _−R_ ( _⃗η_ [t] ) _[⊤]_ _F_ _[⃗]_ p [p] t
�


= _−R_ ( _⃗η_ [t] ) _[⊤]_ _M_ _[⃗]_ p [p] t
�



_⃗M_ l [l] t



_⃗η_ [t] _,_ _[d⃗][η]_ [ t]
� _dt_



**3.5** **Six DoF model of PADS flight dynamics**


As mentioned earlier, the 6 DoF model describes the PADS system as one rigid body with one
mass and one inertia in the CoM of the system. Therefore, the masses the parafoil ( _m_ p ) and the
load mass ( _m_ l ) is added as one mass ( _m_ c ). The parafoils inertia ( _I_ p [p] [) and the load inertia (] _[I]_ l [l] [) is]
added in one inertia in the CoM of the system ( _I_ c [c] [). The total inertia is defined in the] _[ {]_ [c] _[}]_ [ frame.]
The total mass in the CoM is found as


_m_ c = _m_ p + _m_ l (21)


The inertia of the parafoil, which is defined in the parafoil frame, should be rotated with _µ_ to
express it in the _{_ c _}_ frame. Then the total inertia in the CoM is determined as


_I_ p [c] [=] _[ R]_ [(] _[µ]_ [)] _[⊤]_ [(] _[I]_ p [p] [)] _[R]_ [(] _[µ]_ [) +] _[ m]_ [p] [(] _[⃗r]_ [ c] c _,_ p _[⊤]_ _[⃗r]_ [ c] c _,_ p _[I]_ [3x3] _[ −]_ _[⃗r]_ [ c] c _,_ p _[⃗r]_ [ c] c _,_ p _[⊤]_ [)] _[,]_



_I_ l [c] [=] _[ I]_ l [l] [+] _[ m]_ [l] [(] _[⃗r]_ [ c] c _,_ l _[⊤]_ _[⃗r]_ [ c] c _,_ l _[I]_ [3x3] _[ −]_ _[⃗r]_ [ c] c _,_ l _[⃗r]_ [ c] c _,_ l _[⊤]_ [)] _[,]_

_I_ c [c] [=] _[ I]_ p [c] [+] _[ I]_ l [c] _[,]_



(22)



in which _⃗r_ c [c] _,_ p [is the position vector from the CoM to the parafoil mass and] _[ ⃗r]_ [ c] c _,_ l [is the position]
vector from the CoM to the load mass. _I_ [3x3] is a 3 by 3 identity matrix. The position vector to
the CoM ( _⃗r_ c [c] [) is determined as]


_⃗r_ c [c] [=] _[ m]_ _[−]_ c [1] � _m_ p _⃗r_ c [c] _,_ p [+] _[ m]_ [l] _[⃗r]_ [ c] c _,_ l � (23)


when all the position vectors are correctly defined the CoM should be in the zero coordinate
of the _{_ c _}_ frame. The position vector from the CoM to the center of gravity is also zero. The
equations of motion for the PADS modeled as one 6 DoF rigid body are dependent on the sum
of forces and moments. The 6 DOF model has contributions from the parafoil aerodynamics
(p a ), load aerodynamics (l a ), the gravity (g) and the apparent mass (p m ). An index set _D_ is
constructed as _{_ p a _,_ l a _,_ g _,_ p m _}_ to sum all the contributions. The Equation of Motion (EoM) for
the acceleration of the body is given as



�



_m_ c _ddtV_ _[⃗]_ c [c] [+] _[ ⃗ω]_ c [c] _[×][ m]_ [c] _[⃗V]_ [ c] c [=] � _⃗F_ i [c]

_i∈D_



_dV_ _[⃗]_ c [c] c c _[, ⃗ω]_ [c] _[, ⃗η]_ [ c] _[, δ]_ [r] _[, δ]_ [l]
_dt_ _[, d⃗ω]_ _dt_ [c] _[, ⃗V]_ [ c]
�



_,_ (24)



in which _V_ _[⃗]_ c [c] [is the body velocity in the CoM,] _[ ⃗ω]_ c [c] [is the body angular velocity in the CoM and]
_⃗η_ [c] is the orientation w.r.t. the world frame of the body. _F_ _[⃗]_ i [c] [represents a contributing force in]
the index set of _D_ . The EoM for the angular acceleration is given as



_d⃗ω_ cc c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] _[, δ]_ [r] _[, δ]_ [l]
� _dt_ _[, ⃗V]_ [ c]


16



+ _⃗r_ i [c] _[×][ ⃗F]_ [ c] i
�



_dV_ _[⃗]_ c [c] c c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] _[, δ]_ [r] _[, δ]_ [l]
_dt_ _[, d⃗ω]_ _dt_ [c] _[, ⃗V]_ [ c]
�



_,_

��

(25)



_I_ c [c] _d⃗ωdt_ c [c] [+] _[⃗ω]_ c [c] _[×][I]_ c [c] _[⃗ω]_ c [c] [=] �

_i∈D_



_⃗M_ i [c]
�



_,_


with _M_ _[⃗]_ _i_ [c] [as a contributing moment within the index set of] _[ D]_ [.] _[ ⃗r]_ [ c] i [is the corresponding position]
vector from the contribution to the CoM. The first contribution is the parafoil aerodynamic force
( _F_ _[⃗]_ p [c] a [) and moments (] _[ ⃗M]_ [ c] p a [) are defined as]


_⃗F_ p [c] a [(] _[⃗V]_ [ c] c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] _[, δ]_ [r] _[, δ]_ [l] [) =] _[ R]_ [(] _[µ]_ [)] _[⊤]_ _[⃗F]_ [ p] p a [(] _[⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [)] _[,]_



_⃗M_ p [c] a [(] _[⃗V]_ [ c] c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] _[, δ]_ [r] _[, δ]_ [l] [) =] _[ R]_ [(] _[µ]_ [)] _[⊤]_ _[⃗M]_ [ p] p a [(] _[⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [)] _[,]_

_⃗V_ p [p] _,_ air [=] _[ R]_ [(] _[µ]_ [)] � _⃗V_ c [c] _[−]_ _[⃗r]_ [ c] p a _[×][ ⃗ω]_ c [c] [+] _[ R]_ [(] _[⃗η]_ [ c] [)] _[⃗V]_ [ n] w � _,_

_⃗ω_ p [p] [=] _[ R]_ [(] _[µ]_ [)] _[⃗ω]_ c [c] _[,]_



(26)



here _V_ _[⃗]_ w [n] [is the wind velocity vector.] _[ ⃗F]_ [ p] p a [and] _[ ⃗M]_ [ p] p a [are given in (6). The second contribution are]
load aerodynamics. The load aerodynamic force ( _F_ _[⃗]_ l [c] a [) and moments (] _[ ⃗M]_ [ c] l a [) are expressed similar]
as the parafoil aerodynamics as



_⃗F_ l [c] a [(] _[⃗V]_ [ c] c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] [) =] _[ ⃗F]_ [ l] l a [(] _[⃗V]_ [ l] l _,_ air _[, ⃗ω]_ l [l] [)]
_⃗M_ l [c] a [(] _[⃗V]_ [ c] c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] [) =] _[ ⃗M]_ [ l] l a [(] _[⃗V]_ [ l] l _,_ air _[, ⃗ω]_ l [l] [)]
_⃗V_ l [l] _,_ air [=] _[ ⃗V]_ [ c] c _[−]_ _[⃗r]_ [ l] l a _[×][ ⃗ω]_ c [c] [+] _[ R]_ [(] _[⃗η]_ [ c] [)] _[⃗V]_ [ n] w
_⃗ω_ l [l] [=] _[ ⃗ω]_ c [c] _[,]_



(27)



_⃗F_ l [l] a [and] _[ ⃗M]_ [ l] l a [are given in (7). The third contribution is the gravity force, which only works along]
the _z_ n axis of the world frame. The gravity force ( _F_ _[⃗]_ g [c] [) is modeled as]





_,_ (28)




_⃗F_ g [c] [(] _[⃗η]_ [ c] [) =] _[ m]_ [c] _[g]_



 sin( _−ϕ_ sin( [c] ) cos( _θ_ [c] ) _θ_ [c] )

 cos( _ϕ_ [c] ) cos( _θ_ [c] )



here _g_ is the gravitational constant. The EoM (25) might have suggested that the gravity also
has a moment contribution ( _M_ _[⃗]_ g [c] [). The gravity is a force acting in the CoM of the rigid body.]
Therefore, this component is absent and set to zero. The last contribution is the apparent mass.
The apparent mass is expressed in the parafoil frame and is rotated from the parafoil frame to
the _{_ c _}_ frame. The apparent mass force ( _F_ _[⃗]_ p [c] m [) and moment (] _[ ⃗M]_ [ c] p m [) are given as]



�



_⃗F_ [c]
p m



_dV_ _[⃗]_ c [c] c c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c]
_dt_ _[, d⃗ω]_ _dt_ [c] _[, ⃗V]_ [ c]
� �



= _R_ ( _µ_ ) _[⊤]_ _F_ _[⃗]_ p [p] m



_dV_ _[⃗]_ _dt_ p [p] _,_ air _, V_ _[⃗]_ p [p] _,_ air _[, ⃗ω]_ p [p]
�



_,_



_d⃗ω_ p
p
� _dt_ _[, ⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] � _,_



_⃗M_ [c]
p m



_d⃗ω_ cc c _[, ⃗ω]_ c [c] _[, ⃗η]_ [ c] = _R_ ( _µ_ ) _[⊤]_ _M_ _[⃗]_ p [p] m
� _dt_ _[, ⃗V]_ [ c] �



_⃗V_ p [p] _,_ air [=] _[ R]_ [(] _[µ]_ [)(] _[⃗V]_ [ c] c _[−]_ _[⃗r]_ [ c] p m _[×][ ⃗ω]_ c [c] [+] _[ R]_ [(] _[⃗η]_ [ c] [)] _[⃗V]_ [ n] w [)] _[,]_



(29)



_dV_ _[⃗]_ p [p] _,_ air = _R_ ( _µ_ )
_dt_



_dV_ _[⃗]_ c [c] c
_dt_ _[−]_ _[⃗r]_ [ c] p m _[×][ d⃗ω]_ _dt_ [c]
�



�



_,_



_d⃗ω_ p [p] _d⃗ω_ cc
_dt_ [=] _[ R]_ [(] _[µ]_ [)] � _dt_ � _,_


with _F_ _[⃗]_ [p]
p m [and] _[ ⃗M]_ [ p] p m [given in (14),(15) respectively.]


17


**3.6** **Twelve DoF model model of PADS flight dynamics**


The twelve DoF model is an extension of the six DoF model. Instead of looking at one rigid body,
the parafoil and the SR or load will be considered as two separate rigid bodies. This makes some
parts of the modeling easier. There is no need to combine the masses and inertia’s in one mass
and inertia in the CoM. There are two centers of mass, one for the parafoil and one for the load.
The two rigid body should be contraint with respect to each other. Thi makes the modeling
more complex. The tension lines allow for relative motion between the parafoil and the load. A
tension line model is introduced to constrain the relative movement of the load w.r.t. the parafoil.


The index set of forces and moments _D_ given for the 6 DoF model is separated in a set for
the parafoil _P_ and a set for the load _L_ . _P_ consists of the parafoil aerodynamics (p a ), the parafoil
gravity (p g ), the parafoil apparent mass (p m ) and the parafoil tension line (p t ). This gives _P_
as _{_ p a _,_ p g _,_ p m _,_ p t _}_ . _L_ consists of the load aerodynamics (l a ), the load gravity (l g ) and the load
tension line (l t ). This gives _L_ as _{_ l a _,_ l g _,_ l t _}_ . Two sets of equations of motion are used to determine
the motion of the parafoil and the load. The parafoil EoM are given as



�



_dV_ _[⃗]_ [p]
_m_ p _dt_ p + _⃗ω_ p [p] _[×][ m]_ [p] _[⃗V]_ [ p] p [=] � _⃗F_ i [p]

_i∈P_



_dV_ _[⃗]_ [p]
p p p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p] _[, δ]_ [r] _[, δ]_ [l]
_dt_ _[, d⃗ω]_ _dt_ [p] _[, ⃗V]_ [ p]
�



(30)



and


_d⃗ω_ [p]
_I_ p [p] _dt_ p [+] _[⃗ω]_ p [p] _[×][I]_ p [p] _[⃗ω]_ p [p] [=] �

_i∈P_



_⃗M_ i [p]
�



_d⃗ω_ p
p p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p] _[, δ]_ [r] _[, δ]_ [l]
� _dt_ _[, ⃗V]_ [ p]



+ _⃗r_ i [p] _[×][ ⃗F]_ [ p] i
�



_dV_ _[⃗]_ [p]
p p p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p] _[, δ]_ [r] _[, δ]_ [l]
_dt_ _[, d⃗ω]_ _dt_ [p] _[, ⃗V]_ [ p]
� ��



_._



(31)
_⃗F_ i [p] represents the different force contributions of _P_ and _M_ _[⃗]_ i [p] represents the different moment
contributions of _P_ . _⃗r_ i [p] is the corresponding position vector from the contribution to the parafoil
CoM. _⃗η_ [p] is the parafoil orientation w.r.t. the world frame. The EoM for the load are



�



_m_ l _ddtV_ _[⃗]_ l [l] [+] _[ ⃗ω]_ l [l] _[×][ m]_ [l] _[⃗V]_ [ l] l [=] � _⃗F_ i [l]

_i∈L_



_dV_ _[⃗]_ l [l] l
l _[, ⃗ω]_ l [l] _[, ⃗η]_ [ l] _[, δ]_ [r] _[, δ]_ [l]
_dt_ _[, d⃗ω]_ _dt_ [l] _[, ⃗V]_ [ l]
�



(32)



and


_I_ l [l] _d⃗ωdt_ l [l] [+] _[ ⃗ω]_ l [l] _[×][ I]_ l [l] _[⃗ω]_ l [l] [=] �

_i∈L_



_⃗M_ i [l]
�



��



_d⃗ω_ ll
� _dt_ _[, ⃗V]_ [ l] l _[, ⃗ω]_ l [l] _[, ⃗η]_ [ l] _[, δ]_ [r] _[, δ]_ [l]



+ _⃗r_ i [l] _[×][ ⃗F]_ [ l] i
�



_dV_ _[⃗]_ l [l] l
l _[, ⃗ω]_ l [l] _[, ⃗η]_ [ l] _[, δ]_ [r] _[, δ]_ [l]
_dt_ _[, d⃗ω]_ _dt_ [l] _[, ⃗V]_ [ l]
�



_._



(33)
_⃗F_ i [l] [represents the different force contributions of] _[ L]_ [ and] _[ ⃗M]_ [ l] i [represents the different moment]
contributions of _L_ . _⃗r_ i [l] [is the corresponding position vector from the contribution to the load]
CoM. _⃗η_ [l] is the load orientation w.r.t. the world frame. The aerodynamic contribution to the
parafoil dynamics is expressed as


_⃗F_ p [p] a [(] _[⃗V]_ [ p] p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p] _[, δ]_ [r] _[, δ]_ [l] [) =] _[ ⃗F]_ [ p] p a [(] _[⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [)] _[,]_



_⃗M_ p [p] a [(] _[⃗V]_ [ p] p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p] _[, δ]_ [r] _[, δ]_ [l] [) =] _[ ⃗M]_ [ p] p a [(] _[⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p] _[, δ]_ [r] _[, δ]_ [l] [)] _[,]_

_⃗V_ p [p] _,_ air [=] _[ ⃗V]_ [ p] p _[−]_ _[⃗r]_ [ p] p a _[×][ ⃗ω]_ p [p] [+] _[ R]_ [(] _[⃗η]_ [ p] [)] _[⃗V]_ [ n] w


18



_._ (34)


_⃗F_ p [p] a [and] _[ ⃗M]_ [ p] p a [are given in (6). The aerodynamic contribution to the load is modeled as]


_⃗F_ l [l] a [(] _[⃗V]_ [ l] l _[, ⃗ω]_ l [l] [) =] _[ ⃗F]_ [ l] l a [(] _[⃗V]_ [ l] l _,_ air _[, ⃗ω]_ l [l] [)] _[,]_
_⃗M_ l [l] a [(] _[⃗V]_ [ l] l _[, ⃗ω]_ l [l] [) =] _[ ⃗M]_ [ l] l a [(] _[⃗V]_ [ l] l _,_ air _[, ⃗ω]_ l [l] [)] _[,]_
_⃗V_ l [l] _,_ air [=] _[ ⃗V]_ [ l] l _[−]_ _[⃗r]_ [ l] la _[×][ ⃗ω]_ l [l] [+] _[ ⃗V]_ _[ c]_ w _[.]_


with _F_ _[⃗]_ l [l] a [and] _[ ⃗M]_ [ l] l a [are given in (7) The gravity force (] _[⃗F]_ [ p] p g [) of the parafoil is determined as]



(35)





_,_ (36)




_⃗F_ [p]
p g [(] _[⃗η]_ [ p] [) =] _[ m]_ [p] _[g]_


the gravity force ( _F_ _[⃗]_ l [l] g [) of the load is]


_⃗F_ l [l] g [(] _[⃗η]_ [ l] [) =] _[ m]_ [l] _[g]_



 sin( _−ϕ_ sin( [p] ) cos( _θ_ [p] ) _θ_ [p] )

 cos( _ϕ_ [p] ) cos( _θ_ [p] )



 sin( _−ϕ_ sin( [l] ) cos( _θ_ [l] ) _θ_ [l] )

 cos( _ϕ_ [l] ) cos( _θ_ [l] )



 _._ (37)





The apparent mass force and moment are expressed as



�



_⃗F_ [p]
p m



_dV_ _[⃗]_ [p]
p p
_dt_ _[,]_ _[d⃗ω]_ _dt_ [p] _[, ⃗V]_ [ p] p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p]
� �



= _F_ _[⃗]_ [p]
p m



_dV_ _[⃗]_ _dt_ p [p] _,_ air _, V_ _[⃗]_ p [p] _,_ air _[, ⃗ω]_ p [p]
�



_,_



_⃗M_ [p]
p m



_d⃗ω_ p _d⃗ω_ p
� _dt_ p _[, ⃗V]_ [ p] p _[, ⃗ω]_ p [p] _[, ⃗η]_ [ p] � = _M_ _[⃗]_ p [p] m � _dt_ p _[, ⃗V]_ [ p] p _,_ air _[, ⃗ω]_ p [p]



_,_
�



(38)



_⃗V_ p [p] _,_ air [=] _[ ⃗V]_ [ p] p _[−]_ _[⃗r]_ [ p] p m _[×][ ⃗ω]_ p [p] [+] _[ R]_ [(] _[⃗η]_ [ p] [)] _[⃗V]_ [ n] w _[,]_

_dV_ _[⃗]_ p [p] _,_ air = _[d⃗V]_ [ p] p _−_ _⃗r_ [p] p
_dt_ _dt_ p m _[×][ d⃗ω]_ _dt_ [p] _[,]_



with _F_ _[⃗]_ [p]
p m [and] _[ ⃗M]_ [ p] p m [given in (14),(15) respectively. The parafoil tension line forces and moments]

are
_⃗F_ p [p] t [(] _[⃗r]_ [ p] p _[,⃗r]_ l [ p] _[, ⃗η]_ [ p] _[, ⃗η]_ [ l] _[, ⃗V]_ [ p] p _[, ⃗V]_ [ l] l _[, ⃗ω]_ p [p] [) =] _[ ⃗F]_ [ p] p t _⃗r_ t [p] _[, d⃗r]_ t [ p] _,_



� _⃗r_ t [p] _[, d⃗r]_ _dt_ t [ p]



_⃗M_ p [p] t [(] _[⃗η]_ [ p] _[, ⃗η]_ [ l] _[, ⃗ω]_ p [p] _[, ⃗ω]_ l [l] [) =] _[ ⃗M]_ [ p] p t



_⃗η_ [t] _,_ _[d⃗][η]_ [ t]
� _dt_



_,_
�


_,_
�



_⃗r_ t [p] [=] _[ R]_ [(] _[⃗η]_ [ p] [)(] _[⃗r]_ [ n] p _[−]_ _[⃗r]_ [ n] l [)] _[,]_

_⃗η_ [t] = _⃗η_ [p] _−_ _⃗η_ [l]

_d⃗rdt_ t [p] = _⃗r_ t [p] _[×][ ω]_ p [p] [+] _[ ⃗V]_ [ p] p _[−]_ _[R]_ [(] _[⃗η]_ [ t] [)] _[⃗V]_ [ l] l



(39)



_d⃗η_ [t]

p _[−]_ _[J]_ [(] _[⃗η]_ [ l] [)] _[⃗ω]_ l [l] _[,]_
_dt_ [=] _[ J]_ [(] _[⃗η]_ [ p] [)] _[⃗ω]_ [p]

_⃗r_ p [n] [is the position vector of the parafoil defined in the world frame. Similar] _[ ⃗r]_ [ n] l is the position
vector of the load defined in the world frame. _F_ _[⃗]_ p [p] t [and] _[ ⃗M]_ [ p] p t [are given in (19). The load tension]
line force and moments are



�



_⃗F_ l [l] t [(] _[⃗r]_ [ p] p _[,⃗r]_ l [ p] _[, ⃗η]_ [ p] _[, ⃗η]_ [ l] _[, ⃗V]_ [ p] p _[, ⃗V]_ [ l] l _[, ⃗ω]_ p [p] [) =] _[ ⃗F]_ [ l] l t



� _⃗r_ t [p] _[, ⃗η]_ [ t] _[, d⃗r]_ _dt_ t [ p]



_._ (40)
�



_⃗M_ l [l] t [(] _[⃗η]_ [ p] _[, ⃗η]_ [ l] _[, ⃗ω]_ p [p] _[, ⃗ω]_ l [l] [) =] _[ ⃗M]_ [ l] l t


19



_⃗η_ [t] _,_ _[d⃗][η]_ [ t]
� _dt_


with _F_ _[⃗]_ l [l] t [and] _[ ⃗M]_ [ l] l t [given in (20).]


**3.7** **Additional descriptions of dynamic effects**


In this report one more involved aerodynamic model and one more complex tension line model
are explored. First the aerodynamic model is explained. The parafoil can be divided in multiple
panels. The panels can rotate w.r.t. each other, resulting in a flexible representation of the
parafoil. The aerodynamic force is then also expressed as a force per panel, instead of one
aerodynamic force for the whole parafoil. In [4] an aerodynamic expression is derived for the
aerodynamic force ( _F_ _[⃗]_ p [p] a _,i_ [) per panel as]



( _u_ [i] i _,_ air [)] [2] [ + (] _[w]_ i [i] _,_ air [)] [2]



(41)



_⃗F_ p [p] a _,_ i [(] _[⃗V]_ [ i] i _,_ air _[, δ]_ [i] [) = 1] 2 _[ρS]_ [i]



_⃗F_ p [p] a _,_ i [(] _[⃗V]_ [ i] i _,_ air _[, δ]_ [i] [) = 1]



 _C_ L _δ_ i

�








_w_ i [i] _,_ air

 0

 _−u_ [i] i _,_ air





+




_C_ D _δ_ i �( _u_ [i] i _,_ air [)] [2] [ + (] _[v]_ i [i] _,_ air [)] [2] [ + (] _[w]_ i [i] _,_ air [)] [2]



_u_ [i] i _,_ air

 _v_ i [i] _,_ air

 _w_ i [i] _,_ air













 _,_



with _V_ _[⃗]_ i [i] _,_ air [as the air velocity of the panel,] _[ δ]_ [i] [ as the deflection of the panel,] _[ S]_ [i] [ as the aerodynamic]
reference area of the panel. _C_ L _δ_ i and _C_ D _δ_ i are the aerodynamic lift and drag coefficient of the
panel, dependent on _δ_ i . The resulting force can be modeled on each panel. The total resulting
aerodynamic moments ( _M_ _[⃗]_ p [p] a [) is]



_⃗M_ p [p] a [(] _[⃗V]_ [ i] _i,_ air _[, δ]_ _[i]_ _[,⃗r]_ _i_ [ p] _[, ⃗η]_ [ i] [) =]



_N_
�


_i_



� _⃗r_ _i_ [p] _[×][ R]_ [(] _[⃗η]_ [ i] [)] _[⃗F]_ [ p] p a _,i_ [(] _[⃗V]_ [ i] _i,_ air _[, δ]_ _[i]_ [)] � _,_ (42)



here _N_ is the amount of panels. _⃗r_ i [p] [is the position vector from the parafoil CoM to the panel and]
_⃗η_ [i] is the orentation of the panel w.r.t. the parafoil. Since in this report the parafoil is considered
as one rigid body, this aerodynamic expression reduces to the expression given in (6). Therefore,
this expression is not implemented.


The tension line model given in (19) is a simplistic model. A general PADS consists of tens
of tension lines, instead of just one. The moments due to the tension lines are in reality a result
of the tension line forces, instead of a torsion stiffness and damping. Multiple tension line forces
are then modeled between the attachment points of the parafoil and the load. [13] and [22] use
a similar approach. The tension lines between the parafoil and the payload are modeled as multiple 1D spring-damper systems, which are only able to handle load in one direction and only if
the line is stretched. compressing the line is not realistic, thus creating a nonlinear model. The
tension force ( _F_ t ) is expressed as


_F_ t = _−k_ ( _l −_ _l_ eq ) _−_ _dl_ [˙] (43)


with _l_ being the length of the line, _l_ eq as the equilibrium length, _k_ is the spring constant and
_d_ is the damping constant. In a three dimensional space it is assumed that the force directly
counteracts the excitation. Only the velocity is damped, which is inline with the excitation. This
results in a tension force ( _F_ _[⃗]_ t [p] [) in one of the load attachments points as]



�



_⃗F_ t [l] [=] _[ −][k⃗r]_ [ l] t �1 _−_ _||⃗rl_ te [l] q _[||]_ [2]


20



_−_ _d_
�



_⃗r_ ˙ lt _⊤_ _⃗r_ t [l]
� _⃗r_ t [l] _[⊤]_ _⃗r_ t [l]



_⃗r_ t [l] _[.]_ (44)


The length _l_ is replaced with the position vector from the attachment point on the parafoil to
the attachment point on the load ( _⃗r_ t [l] [). The line force only works if] _[ ||][⃗r]_ [ l] t _[||]_ [2] _[> l]_ [eq] [. By modeling]
multiple lines between multiple attachments point, the tension moments follow as a result of the
tension forces.


**3.8** **Model Composition**


By embedding all the forces and moments in the EoM and rearranging terms the 6 DoF model
can be written as a nonlinear model. The model is based on the vectors _ζ_ = [ _V_ _[⃗]_ c [c] _[⊤]_ _⃗ω_ c [c] _[⊤]_ []] _[⊤]_ [,]
_ξ_ = [ _⃗r_ c [n] _[⊤]_ _⃗η_ [c] _[⊤]_ ] _[⊤]_, _δ_ is the left and right deflection ( _δ_ l & _δ_ r ). _w_ is the disturbance, which is the
wind velocity ( _V_ _[⃗]_ w [n] [). The model is]


_M_ _ζ_ [˙] = _C_ _ζ_ ( _ζ_ ) _ζ_ + _C_ _w_ ( _ζ, ξ, w_ ) + _D_ ( _ζ, ξ, δ, w_ ) + _G_ ( _ξ_ ) (45)


with _M_ as the mass matrix with the mass, inertia and the apparent mass. _C_ _ζ_ ( _ζ_ ) embeds al
terms related to the EoM and apparent mass based on the vector _ζ_ . _C_ _w_ ( _ζ, ξ, w_ ) embeds the
remaining terms of the apparent mass. They become zero if the wind disturbance is not present.
_D_ ( _ζ, ξ, δ, w_ ) are all the aerodynamic terms and _G_ ( _ξ_ ) is the gravity. _ζ_ and _ξ_ are related through



˙ _R_ ( _⃗η_ [c] ) _[⊤]_ 0
_ξ_ =
� 0 _T_ ( _⃗η_ [c] )�

� ~~��~~ ~~�~~

_J_



_ζ._ (46)



By defining the state vector as [ _x_ _[⊤]_ 1 _x_ _[⊤]_ 2 []] _[⊤]_ [= [] _[ζ]_ _[⊤]_ _[ξ]_ _[⊤]_ []] _[⊤]_ [a state space is constructed as]



˙ 0 _J_ ( _x_ 1 )
_x_ = _f_ ( _x, u, w_ ) =
�0 _M_ _[−]_ [1] _C_ _ζ_ ( _x_ 2 )



0
_x_ +
� � _M_ _[−]_ [1] [ _C_ _w_ ( _x_ 1 _, x_ 2 _, w_ ) + _D_ ( _x_ 1 _, x_ 2 _, u, w_ ) + _G_ ( _x_ 1 )]



(47)
�



The inputs are the parafoil left and right deflection. This gives _u_ = _δ_ . _w_ is the disturbance
and is still defined as the wind velocity ( _V_ _[⃗]_ w [n] [). Four outputs of interest are defined. The first is]
the heading angle, also presented as _ψ_, the second is the turning rate defined as _ψ_ [˙] . The third
and fourth are the vertical and horizontal velocities of the load, defined in the world frame. The
output is defined as






=










_ψψ_ ˙ [l][l]
~~�~~ ( _u_ ~~[n]~~ l [)] [2]



( _u_ ~~[n]~~ l [)] [2] [+ (] _[v]_ l ~~[n]~~ [)] [2]
_w_ l [n]



_y_ = _h_ ( _x_ ) =



_ψ_ ˙ [l]



_ψ_ [l]

_V_ h [n]

 _V_ v [n]





 (48)


(49)



with
_⃗η_ [l] = _⃗η_ [c] _,_

˙
_⃗η_ [l] = _J_ ( _⃗η_ [l] ) _⃗ω_ l [l] _[,]_


_⃗V_ l [n] [=] _[ R]_ _[⊤]_ [(] _[⃗η]_ [ l] [)] _⃗V_ c [c] _[−]_ _[⃗r]_ [ l] l _[×][ ⃗ω]_ c [c] _._
� �



The 12 DoF model is written similar as (45). The vector _ζ_ becomes [ _V_ _[⃗]_ p [p] _[⊤]_ _⃗V_ l [l] _[⊤]_ _⃗ω_ p [p] _[⊤]_ _⃗ω_ l [l] _[⊤]_ []] _[⊤]_

and _ξ_ becomes [ _⃗r_ p [n] _[⊤]_ _⃗r_ l [n] _[⊤]_ _⃗η_ [p] _[⊤]_ _⃗η_ [l] _[⊤]_ ] _[⊤]_ . The tension force is added in the matrices _C_ _ξ_ ( _ξ_ ),
_D_ _ζ_ ( _ξ_ ) and _S_ . The system is expressed as


_M_ _ζ_ [˙] = _C_ _ζ_ ( _ζ_ ) _ζ_ + _C_ _w_ ( _ζ, ξ, w_ ) + _C_ _ξ_ ( _ξ_ ) _ξ_ + _D_ _ζ_ ( _ξ_ ) _ζ_ + _D_ ( _ζ, ξ, δ, w_ ) + _G_ ( _ξ_ ) + _S._ (50)


21


The vector _ξ_ and _ζ_ are related through










˙
_ξ_ =










_R_ ( _⃗η_ [p] ) _[⊤]_ 0 0 0
0 _R_ ( _⃗η_ [l] ) _[⊤]_ 0 0
0 0 _T_ ( _⃗η_ [p] ) 0
0 0 0 _T_ ( _⃗η_ [l] )



_ζ._ (51)



~~�~~ � ~~�~~ �

_J_


The state vector for the 12 DoF model is [ _x_ _[⊤]_ 1 _x_ _[⊤]_ 2 []] _[⊤]_ [= [] _[ζ]_ _[⊤]_ _ξ_ _[⊤]_ ] _[⊤]_ . The state space model is
almost similar to the one constructed in (63) for the 6 DoF model and by adding the tension
force results in



˙ 0 _J_ ( _x_ 1 )
_x_ = _f_ ( _x, u, w_ ) =
� _M_ _[−]_ [1] _C_ _ξ_ ( _x_ 1 ) _M_ _[−]_ [1] [ _C_ _ζ_ ( _x_ 2 ) + _D_ _ζ_ ( _x_ 1 )]



0 _J_ ( _x_ 1 )
_x, u, w_ ) = _x_ +
� _M_ _[−]_ [1] _C_ _ξ_ ( _x_ 1 ) _M_ _[−]_ [1] [ _C_ _ζ_ ( _x_ 2 ) + _D_ _ζ_ ( _x_ 1 )]�


0
� _M_ _[−]_ [1] [ _C_ _w_ ( _x_ 1 _, x_ 2 _, w_ ) + _D_ ( _x_ 1 _, x_ 2 _, u, w_ ) + _G_ ( _x_ 1 ) + _S_ ]�



(52)
�



The outputs are defined as the heading of the load ( _ψ_ [l] ), the turning rate of the the load ( _ψ_ [˙] [l] ) and
the vertical and horizontal velocity of the load as defined in the output of the 6 DoF model as





 (53)






=










_ψψ_ ˙ [l][l]
~~�~~ ( _u_ ~~[n]~~ l [)] [2]



( _u_ ~~[n]~~ l [)] [2] [+ (] _[v]_ l ~~[n]~~ [)] [2]
_w_ l [n]







_y_ = _h_ ( _x_ ) =



_ψ_ ˙ [l]



_ψ_ [l]

_V_ h [n]

 _V_ v [n]



with
_⃗V_ l [n] [=] _[ R]_ _[⊤]_ [(] _[⃗η]_ [ l] [)] _[⃗V]_ [ l] l _[.]_ (54)


22


## **4 Implementation and Simulation**

The proposed models are implemented in Matlab and Simulink. Both the 6 DoF model
and the 12 DoF model are implemented, such that it is possible to enable and disable the
contributions to the model. The added added effect of the contributions can be compared. The
contributions which can be enabled and disabled are the gravity, the parafoil aerodynamics, the
load aerodynamics and the apparent mass. Sec. 4.1 will show the Simulink implementation and
Sec. 4.2 and 4.3 show the simulation results. Two videos are created with Simscape. One shows
the simulation result of the 6 DoF model and the other video shows the same simulation for the

12 DoF model. They are found at `[https://youtu.be/vr0LlCARQw4](https://youtu.be/vr0LlCARQw4)` and `[https://youtu.be/](https://youtu.be/CT686KLwrkk)`

`[CT686KLwrkk](https://youtu.be/CT686KLwrkk)` .


**4.1** **Simulink model**


Both the 6 DoF and the 12 DoF have a similar implementation. Therefore, only the 12 DoF
Simulink model will be discussed. The model overview is shown in Figure 4 The model consists
of 5 part:


 Input


 Wind model


 Simscape model


 Forces and Moments


 Model data


 Output data


The Input consists of the input variables of the model. In this case the left and right deflection
are given as an vector based on a time vector. The wind model determines the wind velocity
vector in the position of the parafoil and the load. A simple wind model is implemented. The
wind velocity is only based on the position in the world frame. The Simscape model, is based on
the Simscape multibody library and captures the motion of the parafoil and the load, based on
the masses, inertias, input forces and input moments. The gravity is also part of the Simscape
model and the tension line between the parafoil and load is modeled with a Simscape Cartesian
joint and a gimbal joint with internal spring-damper dynamics. In the Simscape models all the
needed states are measured. The measure states can be viewed in the model data section. The

forces and moments determine the aerodynamic forces and moments and the apparent mass force
and moment based on the measured states. In the section a corresponding Matlab model is
called, which calculates the forces and moments, corresponding with the presented equation in
Section 3. The output data determines the specific defined outputs of the model.


23


Figure 4: 12 DoF Simulink model, overview


To elaborate a bit on the used Simscape library. Figure 5 shows the implementation of the
parafoil. The parafoil frame is connected through a 6 DoF joint to the world frame. On the
side of the parafoil frame, a mass block is connected including the parafoil mass and inertia,
a visualization file is connected and an external force and moments block is connected. The
sensors are connected between the world frame and the parafoil frame measuring the position
and orientation of the parafoil frame with respect of the world frame and the body velocity and
body angular velocity in the parafoil frame. The measured state are connected the output of the
Simulink block and also send to the Matlab workspace.


Figure 5: Simscape - parafoil model


The Simulink model can be called from Matlab as following. The simulation folder contains
the sub-folders ’models’, with the models of the SR and ’functions’ with all the needed Matlab
function to run the model. The parameter file can also be found in this folder. These folders are
added to the Matlab path. As following a struct Enable is defined, enabling the model contri

24


butions. additionally, Enable.W enables the wind model. Enable.Database enables a look-up
table for the aerodynamic coefficient otherwise a linear model is used. Enable.Interp enables
linear interpolation between the coefficients in the aerodynamic look-up table. As following the
system parameters are loaded. The input vector is created based on a time vector and the state
vector at _t_ = 0 is defined. As last the Simulink model is called and the simulation results are
loaded in Matlab. In Matlab code this looks like


1 %% Add to path

2 addpath([currentFolder,' _\_ function'])

3 addpath([currentFolder,' _\_ models'])


4


5 %% System mode


6 Enable.F g = true;


7 Enable.P aero = true;


8 Enable.L aero = true;


9 Enable.AM = true;


10 Enable.W = true;


11 Enable.Interp = true;


12 Enable.Database = 1;


13


14 %% Load system parameters

15 [Sys.Env,Sys.CoM,Sys.Para,Sys.Load,Sys.Lines] = Sys Parameters(Enable);

16 Sys.Env.W = [0;0;0]; %wind velocity vector


17


18 %% Simulations


19 t.step = 1e-3;


20 t.end = 40;


21 t.span = 0:t.step:t.end;

22 ∆ = 0*ones(length(t.span),2);

23 input = [t.span' ∆ ];


24


25 %% x0 state vector


26 TW.x0 = zeros(28,1);


27 TW.x0(4:6) = -Sys.Lines.r;


28 TW.x0(7:9) = [0 0 0]';


29 TW.x0(13:15) = [1;0;0];


30 TW.x0(16:18) = [1;0;0];


31 TW.x0(25:27) = Sys.Lines.r;


32


33 %% Call Simulink


34 in = Simulink.SimulationInput('Twelve DoF simscape model joint');

35 in=in.setExternalInput(input);

36 Sl TW.out=sim(in);


**4.2** **Steady state model behavior**


With the Simulink model it is possible to make simulations and analyze the behavior of the
constructed models. First the steady state flight behavior will be analyzed for the 6 DoF model
and the 12 DoF model. Next, the dynamic behavior is analyzed. When the PADS is dropped
from a height, the system will converge to steady state motion. The velocity and the angular
velocity of the model become constant as long as the model is not disturbed by disturbances or a
change in the control inputs. For each constant control input the model converges to a different
steady-state point. The steady state motion of the model can be found as equilibrium points
of the body velocity and the body angular velocity. The EoM should be solved, such that the
derivatives of the body velocity and angular velocity are zero. The corresponding velocity and


25


angular velocity is the equilibrium point. A constant pitch and roll angle are also included. The
model dynamics are dependent on those. For each equilibrium point there is a corresponding
constant control input. The equilibrium point and the corresponding control input always come
in pairs. Solving the system for these equilibrium points is difficult, due to the complexity of the
aerodynamic forces, but the attractive equilibrium points can be found by means of simulation
or a successive root-finding algorithm, like the Newton–Raphson method. The parameter set
given in [21] is used for simulation, since the set of parameters is all most complete and the
paper presents results with which later on the model can be compared with. Since landing the
load/SR is of interest, the flight behavior from the loads point of view is analyzed, thus when
is referred to the velocity, angles or angular velocity, the corresponding state of the load in the
load frame is meant.


1





0.5


0


-0.5


-1


-1.5





1


0.5


0


-0.5


-1



















-5



0 5 10 15 20 -10



10



0



Figure 6: Convergence for _δ_ s = 0



Figure 7: Convergence for _δ_ s = 0 _._ 5



When simulating the system with a constant control input, The velocity component _⃗v_ l [l] [converges]
to zero, as well as the angular velocity ( _⃗ω_ l [l] [) and the roll angle (] _[ϕ]_ [l] [). The yaw angle (] _[ψ]_ [l] [) can be]
any constant value. The velocity components _u_ [l] l [and] _[ w]_ l [l] [and the angle] _[ θ]_ [l] [ converge to a steady]
state, as is shown in Figure 6. and 7. These are of interest to find the equilibrium point. By
substituting the known values in the EoM of both models, the system can be reduced to a force
and moment balance between the aerodynamic forces and moments and the gravity force. Solving the system analytically is complex due to the expressions of the aerodynamics. It is possible
to determine a local Jacobian of the system, but this takes up to a couple of minutes. This
is too slow to use in an successive algorithm. Therefore, the Broyden’s method is used to find
state velocities and angles. Figure 6 shows multiple simulations from different initial conditions
together with the approximated equilibrium point for zero control deflections. The figure shows
all simulations converging to the same point of steady state motion. Broyden’s method gives
the same equilibrium point. Figure 7 shows similar results for a constant symmetric deflection
of 0.5. The resulting equilibrium point is determined for each constant symmetric deflection as
shown in Figure 8. The figures show the ability of the parafoil to brake its forward velocity ( _u_ [l] l [)]
by 3.5 [m/s]. It increases its downward velocity slightly ( _u_ [l] l [) by 0.3 [m/s]. The apparent mass]
effect decreases the forward velocity by 1.5 [m/s] and increases the downward velocity with 0.2

[m/s]. It increases the pitch ( _θ_ [l] ) with 0.11 [rad]. The 6 DoF model and the 12 DoF model do
not show differences significant to the flight dynamics.


26


14


13


12


11


10


9
0 0.25 0.5 0.75 1



1.8


1.6


1.4


1.2


1
0 0.25 0.5 0.75 1



-0.15


-0.2


-0.25


-0.3


-0.35
0 0.25 0.5 0.75 1





3.5


3


2.5


2


1.5


1





Figure 8: Steady state flight behavior for _δ_ s


3


2


1


0


-1







-2


-1.5





0.5















Figure 9: Convergence _V_ _[⃗]_ l [l] [for] _[ δ]_ _[a]_ [ = 0] _[.]_ [5]



Figure 10: Convergence _⃗ω_ l [l] [for] _[ δ]_ _[a]_ [ = 0] _[.]_ [5]



The same analysis can be done for constant asymmetrical deflections as input. The right deflection is kept at zero. The left deflection is varied from 0 to 1. The simulations show that the
system reaches a steady state motion, with a steady state velocity, angular velocity and a steady
state pitching and rolling angle. The yaw angle does not converge. To find the equilibrium point,
the system should be solved for all derivatives being zero with exception of the yaw rate and
the position. Since Brodyen’s method is unable to converge, the equilibrium point is determined
based on the simulations. Figure 9 and 10 show the velocity and angular velocity converging to
a single point for 0.5 asymmetric deflection. The same figures can be made for other asymmetric
deflections.


Figure 11 and 12 show the equilibrium points for the velocity and the angular velocity versus a constant asymmetric deflection. The forward velocity increases between 1 and 2 [m/s] with
an asymmetric deflection varying from .25 to 1. The side velocity ( _v_ l [l] [) increases with 1 [m/s]]
from .25 to 1 asymmetric deflection. The downwards velocity decreases with 0.2 [m/s] for the 6
DoF and 0.4 [m/s] for the 12 DoF model. The angular velocity _p_ [l] l [decreases from -0.02 [] _[s]_ _[−]_ [1] [] for]
_δ_ _a_ is 0.25 to -0.3 [ _s_ _[−]_ [1] ] for _δ_ _a_ is 1. _r_ l [l] [).] _[ q]_ l [l] [) increases from 0.02 [] _[s]_ _[−]_ [1] [] to 0.3-0.45 [] _[s]_ _[−]_ [1] [].] _[ r]_ l [l] [decreases]
with -0.3 [ _s_ _[−]_ [1] ]. The roll angle decreases from -0.1 [rad] to -0.65 [rad]. the pitch angle decreases
to -0.3 [rad] to -0.55 [rad]. The apparent mass effect gives a clear difference in all velocities,
angular velocities and body angles. Moreover, the figures show divergences between the 6 DoF
model and 12 DoF model. Especially the downwards velocity diverges with 0.2 [m/s] difference
for _δ_ _a_ = 1. This differences could be caused by a small relative roll and pitch angle between the
parafoil and the load.


27


16


15


14


13


12


11
0.25 0.5 0.75 1



1.5


1


0.5


0
0.25 0.5 0.75 1



1.4


1.2


1


0.8
0.25 0.5 0.75 1



Figure 11: Steady state flight behavior _δ_ _a_ _→_ _V_ _[⃗]_ l [l]



0


-0.1


-0.2


-0.3


-0.4
0.25 0.5 0.75 1



0.5


0.4


0.3


0.2


0.1


0
0.25 0.5 0.75 1



0


-0.1


-0.2


-0.3


-0.4


-0.5
0.25 0.5 0.75 1



0


-0.2


-0.4


-0.6



Figure 12: Steady state flight behavior _δ_ _a_ _→_ _⃗ω_ l [l]


-0.2


-0.3


-0.4


-0.5



-0.8
0.25 0.5 0.75 1



-0.6
0.25 0.5 0.75 1



Figure 13: Steady state flight behavior _δ_ _a_ _→_ _⃗η_ [l]


**4.3** **Dynamic model behavior**


To analyze the dynamic flight behavior, the system in steady state is disturbed by changing the
control deflection from zero to either a symmetric or an asymmetric deflection. Figure 14 shows
the dynamic behavior of the forward velocity and the downward velocity and the pitch for a
symmetric deflection of 0.25 and 0.75. The forward velocity gives a rise time of 2 [s], a settling
time of 7.5 [s] and a relative overshoot of 0.33 [-]. The apparent mass adds a steady state offset
in the flight behavior. It does not seem to affect the dynamic flight behavior. The 6 DoF and
12 DoF model do not show differences. The downwards velocity has a rise time of 0.2 [s] and a
settling time of 4 [s] and a relative overshoot of 0.2 [-]. The 12 DoF model shows some additional
oscillations due to the spring damper connecting the parafoil and the load. The 12 DoF model


28


has a rise time of 0.05 [s] and a settling time of 5 [s] and a relative overshoot of 2.3 [-]. The apparent mass only shifts the behavior. The pitch _θ_ [l] oscillates with a rise time of 0.1 [s], but a settling
time of over 15 [s]. The relative overshoot is 0.3 [-]. Moreover, the apparent mass only adds
a steady state shift. The 12 DoF does not show additional flight behavior w.r.t. the 6 DoF model.


Figure 14: Dynamic response _δ_ _s_


The same analysis can be made for an asymmetric deflection. The control deflection is changed
from zero deflection to a constant asymmetric deflection of 0.25 and 0.75. The dynamic response
of the flight behavior is shown in 15-17. The exact characteristics of the response are given in
Table 2. Here the apparent mass also adds a steady state offset to the system, in the forward
and downward velocity as well as in the angle _θ_ [l] . A steady state in the flight dynamics is introduced in the side velocity, the angular velocities and the roll angle. They all start from zero and
converge to a constant value. Differences between the 6 DoF and 12 DoF model are visible. The
12 DoF model shows oscillations in _v_ l [l] [,] _[ r]_ l [l] [and some minor oscillations in] _[ p]_ [l] l [.]



1.4


1.2


1
30 40 50 60


1.6


1.4


1.2


1
30 40 50 60



14


12


10


14


12


10



30 40 50 60


30 40 50 60



1.5


1


0.5


0
30 40 50 60


1.5


1


0.5


0
30 40 50 60



Figure 15: Dynamic response _δ_ _a_ _→_ _V_ _[⃗]_ l [l]


29


0


-0.1


-0.2


0


-0.1


-0.2



30 40 50 60


30 40 50 60



30 40 50 60


30 40 50 60



30 40 50 60


30 40 50 60



0.3


0.2


0.1


0


0.3


0.2


0.1


0



0


-0.2


-0.4


0


-0.2


-0.4



0


-0.1



Figure 16: Dynamic response _δ_ _a_ _→_ _⃗ω_ l [l]


-0.2


-0.25



-0.2
25 30 35 40 45 50 55 60


0


-0.2


-0.4


-0.6

25 30 35 40 45 50 55 60



-0.3


25 30 35 40 45 50 55 60


0


-0.2


-0.4


25 30 35 40 45 50 55 60



Figure 17: Dynamic response _δ_ _a_ _→_ _⃗η_ [l]


Table 2: Dynamic behavior for an asymmetric input





|Col1|δ = 0.25<br>a|Col3|Col4|δ = 0.75<br>a|Col6|Col7|
|---|---|---|---|---|---|---|
|**Variable**<br>**Model**|_tr_ [s]|_ts_ [s]|_Mp_ [-]|_tr_ [s]|_ts_ [s]|_Mp_ [-]|
|_u_l<br>l<br>6DoF<br>12DoF|0.76<br>0.67|12.88<br>13.03|1.70<br>1.81|6.31<br>6.41|11.03<br>11.11|2.467<br>2.38|
|_v_l<br>l<br>6DoF<br>12DoF|0.16<br>0.16|9.87<br>9.87|1.72<br>2.73|0.19<br>0.18|4.00<br>6.92|1.02<br>1.66|
|_w_l<br>l<br>6DoF<br>12DoF|0.17<br>0.09|11.29<br>12.86|1.01<br>1.16|9.81<br>6.65|14.12<br>10.80|5.33<br>1.93|
|_p_l<br>l<br>6DoF<br>12DoF|0.15<br>0.05|1.87<br>2.06|1.00<br>1.08|0.29<br>0.26|1.05<br>1.51|1.00<br>1.02|
|_q_l<br>l<br>6DoF<br>12DoF|0.05<br>0.05|13.02<br>13.10|1.68<br>1.61|9.78<br>9.86|9.80<br>9.92|1.04<br>1.04|
|_r_l<br>l<br>6DoF<br>12DoF|10.32<br>0.28|10.34<br>10.43|1.09<br>1.45|2.57<br>0.26|6.79<br>7.26|1.00<br>1.30|


30


## **5 Linearization**

Both the 6 DoF and 12 DoF models, which are developed in this report are nonlinear. To still get
an intuitive understanding on how the non-linearities affect the model, the model is linearized
around an equilibrium point. The linearizations are compared with each other to assess how
different the model behavior in these equilibrium points actually is. A comparison is made
through the frequency responses of the different linearizations. The model is linearized through
a first order Taylor expansion. The general expression of a non-linear state space model is as
follows

˙
_x_ = _f_ ( _x, u, w_ ) _,_
(55)
_y_ = _h_ ( _x_ ) _._


A first order Taylor approximation is made in the equilibrium point ( _x_ _[∗]_, _u_ _[∗]_, _w_ _[∗]_ ) leading to the
expression




_[∂][f]_ [(] _[x][,][ u][,][ w]_ [)] ���

_∂x_ � _x_ _[∗]_ _,u_ _[∗]_ _,w_ _[∗]_

~~�~~ ~~��~~ ~~�~~
_A_




_[∂][f]_ [(] _[x][,][ u][,][ w]_ [)] ���

_∂u_ � _x_ _[∗]_ _,u_ _[∗]_ _,w_ _[∗]_

� ~~�~~ � ~~�~~

_B_




_[∂][f]_ [(] _[x][,][ u][,][ w]_ [)] ���

_∂w_ � _x_ _[∗]_ _,u_ _[∗]_ _,w_ _[∗]_

~~�~~ ~~��~~ ~~�~~

_W_



( _u−u_ _[∗]_ )+ _[∂][f]_ [(] _[x][,][ u][,][ w]_ [)]



_∂w_



( _w−w_ _[∗]_ )



_x_ ˙ _≈_ _f_ ( _x_ _[∗]_ _, u_ _[∗]_ _, w_ _[∗]_ )+ _[∂][f]_ [(] _[x][,][ u][,][ w]_ [)]



( _x−x_ _[∗]_ )+ _[∂][f]_ [(] _[x][,][ u][,][ w]_ [)]



_∂u_



_∂x_



(56)



and




_[∂h]_ [(] _[x]_ [)] ���

_∂x_ � _x_ _[∗]_

~~�~~ ~~�~~ � �
_C_



_y ≈_ _h_ ( _x_ _[∗]_ ) + _[∂h]_ [(] _[x]_ [)]



( _x −_ _x_ _[∗]_ ) _._ (57)



_∂x_



When considering a wind disturbance, the model leads to an equilibrium point for constant symmetric deflections. For constant asymmetric deflection the model does not lead to a equilibrium
point. As a result the term _f_ ( _x_ _[∗]_ _, u_ _[∗]_ _, w_ _[∗]_ ) is not zero. This term is seen as a constant input, by
introducing _ν_ as an auxiliary input. By expressing the system variables ( _x −_ _x_ _[∗]_ ) as ˜ _x_, ( _u −_ _u_ _[∗]_ )
as ˜ _u_, ( _w −_ _w_ _[∗]_ ) as ˜ _w_ and _y −_ _h_ ( _x_ _[∗]_ ) as ˜ _y_ the linearized system is described as


_x_ ˙˜ _≈_ _Ax_ ˜ + _ν_ + _W_ ˜ _w_

˜ ˜ (58)
_y ≈_ _Cx._


here, _ν_ is expressed as
_ν_ = _Bu_ ˜ + _f_ ( _x_ _[∗]_ _, u_ _[∗]_ _, w_ _[∗]_ ) (59)


Since the point ( _x_ _[∗]_ _, u_ _[∗]_ _, w_ _[∗]_ ) is not necessarily an equilibrium point of the system, the system
is linearized along an equilibrium trajectory. The system is linearized in all the points in the
trajectory. All these models together result in a linear parameter varying (LPV) model. An LPV
model varies over the scheduling variable _p_ . The the scheduling variable _p_ ( _t_ ) may vary over time
and is assumed to be exogenous. This results in a LPV system as


˙˜
_x ≈_ _A_ ( _p_ )˜ _x_ + _ν_ (˜ _u, p_ ) + _W_ ( _p_ ) ˜ _w_

˜ (60)
_y ≈_ _C_ ( _p_ )˜ _x._


with _p_ related to the equilibrium trajectory as


_p_ = Ψ( _x_ _[∗]_ _, u_ _[∗]_ _, w_ _[∗]_ ) (61)


In this report a linearization is made for zero wind disturbance. For a constant input, the states


31


of the model converge to an equilibrium position. The model can be linearized in this equilibrium
point and one linear system is obtained for each constant input. Not all the states converge to
an equilibrium point. In the 6 DoF model this are the position vectors and the yaw angle. The
derivative of the yaw angle becomes constant and can be embedded as a constant input to the
system. This is also done in (59). The position does not affect the input-output relation and can
be taken out of the linearized model.



The position vectors and the yaw angles do not converge to an equilibrium point in the 12
DoF model. This is problematic since the dynamics depend on these states. The tension force is
dependent on the positions and the yaw angles. This can be solved by recognizing that the model
is only dependent on the relative position ( _⃗r_ t [p] [) and the relative yaw angle (] _[ψ]_ [ t] [), expressed in the]
parafoil frame. These state actually do converge to an equilibrium point and can be determined
based on other converging state variables as

_⃗r_ ˙˙ pt = _I_ 3x3 _−R_ ( _⃗η_ [t] ) [ _⃗r_ t [p] []] _[×]_ 0
� _⃗η_ t � � 0 0 _T_ ( _ϕ_ [p] _, θ_ [p] ) _−T_ ( _ϕ_ [l] _, θ_ [l] )� _ζ._ (62)

� ~~�~~ � ~~�~~

_E_


Here [ _⃗r_ t [p] []] _[×]_ [is the crossproduct matrix of] _[ ⃗r]_ [ p] t [. By adding these variables to state vector as] _[ x]_ [3] [,]
the state equation is rewritten as



�



= _I_ 3x3 _−R_ ( _⃗η_ [t] ) [ _⃗r_ t [p] []] _[×]_ 0
� � 0 0 _T_ ( _ϕ_ [p] _, θ_ [p] ) _−T_ ( _ϕ_ [l] _, θ_ [l] )



_ζ._ (62)







_._ (63)








_x_ +




˙
_x_ =







00 _M_ _[−]_ [1] [ _C_ _ζ_ ( _Jx_ ( 2 _x_ ) + 1 ) _D_ _ζ_ ( _x_ 3 )] _M_ _[−]_ [1] _C_ 0 _ξ_ ( _x_ 3 )

0 _E_ ( _x_ 1 _, x_ 3 ) 0







 _M_ _[−]_ [1] [ _D_ ( _x_ 2 _, u_ 0) + _G_ ( _x_ 1 ) + _S_ ]

0




Now the actual position of the parafoil and the load do not contribute to the systems dynamics
and also not to the input-output relation. The same hold for the parafoil yaw angle. The load
yaw angle does not contribute to the systems dynamics, but is an output. The yaw rate converges
to an equilibrium point, which can be treated as an additional constant input.


The system is linearized for different symmetric deflection ( _δ_ _s_ ) and asymmetric deflections ( _δ_ _a_ ),
which leads to different steady state point _x_ _[∗]_ and _u_ _[∗]_ . The wind disturbance is kept at zero. For
each linearization the transfer function is constructed from the input ˜ _u_ to the output _y_ . Figure
18 and 19 show the resulting frequency responses for the 6 DoF model.


The responses of the 6 DoF model show two interesting things. First, the low frequency behavior
differs per linearization. Especially the low frequency gain for the zero deflection linearization
differs. Secondly, the resonances and the anti-resonances are placed at varying frequencies per
linearization. The different resonances and anti-resonances also result in different phases. The
left and right deflection are 180 [deg] shifted for linearizations at a constant symmetric deflection.


32


10 [-2] 10 [0] 10 [2]



0


-50


-100


0

-20

-40


0


-50


-100


0


-50


-100
10 [-2] 10 [0] 10 [2]



10 [-2] 10 [0] 10 [2]



0


-50


-100


0


-20


-40


0


-50


-100


0
-20
-40
-60

10 [-2] 10 [0] 10 [2]



Frequency (Hz)


Figure 18: Magnitude response linear 6 DoF models



Frequency (Hz)



180


0


-180


-360


270
180
90
0
-90
-180


270

180

90

0

-90


360


180


0
10 [-2] 10 [0] 10 [2]



10 [-2] 10 [0] 10 [2]



10 [-2] 10 [0] 10 [2]



540
360
180
0
-180
-360


540

360

180

0

-180


720
540
360
180
0
-180


360


180


0
10 [-2] 10 [0] 10 [2]



Frequency (Hz)



Frequency (Hz)



Figure 19: Phase response linear 6 DoF models


The resulting linearizations for the 12 DoF model is shown in Figure 20 and 21. The overall
system behavior is similar to the 6 DoF model, with different low frequency gains and moving
resonances and anti-resonances. The linearizations show that the 12 DoF model has additional

behavior in terms of resonances and anti resonances, which vary for the different equilibrium
point. Especially the response of _V_ h [n] [gives changing behavior for a linearization in an asymmet-]
ric deflection point. The phase changes for different linearizations.


The 6 DoF and 12 DoF models are linearized in different equilibrium points. The resulting
models have varying linear behavior in each equilibrium point. In the magnitude responses the


33


low frequency gains are different and the positions of the resonances and anti-resonances differ.



10 [-2] 10 [0] 10 [2]



0


-100


-200


0


-50


-100


0


-50


-100


0


-50


-100


10 [-2] 10 [0] 10 [2]



10 [-2] 10 [0] 10 [2]



0


-100


-200


0


-50


-100


0


-50


-100


0


-50


-100


10 [-2] 10 [0] 10 [2]



Frequency (Hz)



Frequency (Hz)



180


0


-180


-360


360

180

0

-180

-360


270

180

90

0

-90


720
540
360
180
0
-180
10 [-2] 10 [0] 10 [2]



Figure 20: Magnitude response linear 12 DoF models


720

360

0

-360

-720


540
360
180
0
-180
-360


1440
1080
720
360
0
-360



10 [-2] 10 [0] 10 [2]



10 [-2] 10 [0] 10 [2]



1080

720

360

0

-360
10 [-2] 10 [0] 10 [2]



Frequency (Hz)


Figure 21: Phase response linear 12 DoF models


34



Frequency (Hz)


## **6 Validation**

The constructed models are validated w.r.t. the simulation results shown by Van der Kolf in [21].
This paper presents a complete set of parameters together with the simulation results. Van der
Kolf simulates an 8 DoF model. The paper presents the following variables for the system, with
which the models can be validated:


 The angle of attack of the parafoil ( _α_ p ),


 The parafoil pitch angle ( _θ_ p ),


 The load glide path angle ( _γ_ l ),


 The horizontal velocity of the load ( _V_ h [n] [),]


 The vertical velocity of the load ( _V_ v [n] [),]


In [10] the corresponding 8 DoF model is presented. The load is able to rotate relative to the
parafoil with a pitch and yaw angle. Some differences between the models are expected due to
the different model order. Moreover, the model used, do not include the apparent mass. The
added behavior to the flight dynamics is already discussed. therefore, the validation will be
done without the apparent mass effect. First the steady state flight behavior, resulting from a
constant symmetric deflection is compared. The symmetric deflections varies from 0 to 1 [-].
Next the steady state flight behavior, as a result of an asymmetric deflection, is compared. The
asymmetric deflection varies between 0 and 1 [-]. Lastly, both the dynamic flight behavior as
a result of an symmetric deflection and an asymmetric deflection are compared to the reported
simulations of Van der Kolf.


**6.1** **Steady state flight behavior**


The horizontal load velocity is calculated as



_V_ h [n] [=]
�



( _u_ [n] l [)] [2] [ + (] _[v]_ l [n] [)] [2] (64)



The vertical velocity equals the _w_ l [n] [and the glide path angle can be determined as]



_γ_ [l] = tan _[−]_ [1] _V_ nv
� _V_ h [n]



(65)
�



Table 3: Difference in steady state behavior


Variable Van der Kolf 6DoF model 12DoF model

_V_ h ~~[n]~~ [[m/s]] 12.99 12.98 12.98
_V_ v [n] [[m/s]] 5.14 5.22 5.22
_γ_ [l] [deg] 21.63 21.91 21.91
_α_ [p] [deg] 3.53 3.53 3.53
_θ_ [p] [deg] -18.1 -18.39 -18.37


Table 3 shows the steady state behavior for zero control deflection, together with the reported
values of Van der Kolf. There are only small differences. _V_ v [n] [has a difference of 0.08 [m/s],]
resulting in 0.28 [deg] difference in _γ_ [l] . The parafoil pitch angle ( _θ_ [p] ) differs with 0.28 [deg]. The


35


steady state flight behavior, as a result of an constant symmetric deflection, of the 6DoF and
12Dof model with the reported values are shown in Figure 22. The found steady state values
are almost the same for zero deflection but diverge for increasing symmetric deflections. For a
symmetric deflection of 1 the 6DoF and the 12DoF model show as sudden increase w.r.t. to the
lower deflections. This is not the case in the presented simulation results of Van der Kolf.



13


12


11


10



Load word velocity

5.5


5


4.5



9
0 0.25 0.5 0.75 1



4
0 0.25 0.5 0.75 1



Figure 22: Steady state response to _δ_ _s_


The steady state response, resulting from constant asymmetric deflections are shown in Figure
23. The steady states is the same for zero deflection, but diverge for increasing asymmetric
deflections. The horizontal velocity stays between 13 and 12.4 [m/s] for both models, while the
reported velocity increases first to 14.4 [m/s] and decreases for asymmetric deflections higher
than 0.7 [-] to 12.5 [m/s]. The maximum difference is 1.9 [m/s]. The vertical velocity are both
increasing. The modeled velocity increases slower than the reported, leading to a difference
of maximal 7 [m/s]. The yaw rate gives a maximum difference of 0.2 [rad/s]. The absolute
differences are shown in Table 4. The difference in turning rate is not given for symmetric
deflections. The system is not turning for a symmetric deflection and therefore it is also not
reported by Van der Kolf.



0

|Col1|6DoF|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||~~12Do~~<br>Van d|~~F~~<br>er Kolf|~~F~~<br>er Kolf||
|||||||
|||||||
|||||||
|||||||

0 0.25 0.5 0.75 1





14


13.5


13


12.5


12
0 0.25 0.5 0.75 1



Load word velocity and yaw rate


15


10


5
0 0.25 0.5 0.75 1



0.6


0.4


0.2



Figure 23: Steady state response to _δ_ _a_


36


Table 4: Difference in steady state behavior

|Variable Model|δ<br>s|Col3|Col4|Col5|δ<br>a|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Variable**<br>**Model**|0.25 [-]|0.5 [-]|0.75 [-]|1 [|-]<br>0.25 [-]|0.5 [-]|0.75 [-]|1 [-]|
|Dif._ V_ n<br>h [m/s]<br>6DoF<br>12DoF|0.04<br>0.04|0.24<br>0.24|0.19<br>0.19|0.2<br>0.2|7<br>0.42<br>7<br>0.41|0.78<br>0.76|1.52<br>1.49|0.49<br>0.53|
|Dif._ V_ h<br>v [m/s]<br>6DoF<br>12DoF|0.07<br>0.07|0.15<br>0.15|0.28<br>0.28|0.4<br>0.4|9<br>0.36<br>9<br>0.36|0.78<br>0.77|7.11<br>7.10|6.77<br>6.74|
|Dif.˙_ψ_l [rad/s]<br>6DoF<br>12DoF|||||0.02<br>0.02|0.20<br>0.20|0.05<br>0.05|0.07<br>0.07|



**6.2** **Dynamical flight behavior**


The same model variables are used to compare the dynamic flight behavior as was used for the
steady states flight behavior. For the response to a symmetric deflection, the horizontal and
vertical velocity of the load are shown. For an asymmetric deflection the horizontal and vertical
velocity of the load and yaw rate are presented. The dynamic flight behavior of the models is
shown in Figure 24. The deflection is changed from a constant zero deflection to a constant
symmetric deflection of 1. It is already shown that the steady state values differ, but the intermediate dynamic flight behavior looks similar for all models. In general the oscillation frequency
of the reported values is slightly higher. The reported values show a bit less damping resulting
in a longer settling time. The differences in rise time, settling time and overshoot are given in
Table 5. This table also shows a large difference in relative overshoot in the vertical load velocity.
The 6 DoF and 12 DoF make a relative smaller step compared to reported simulation.



14


12


10



Load word velocity

6


5


4


3



8

0 10 20 30



2

0 10 20 30



Figure 24: Velocity response from _δ_ _s_ = 0 to _δ_ _s_ = 1


The dynamic response of both models resulting from an asymmetric deflection is shown in Figure
25. The input is changed from zero deflection to 0.4 [-] asymmetric deflection. The steady state
flight behavior is different. The result is inline with the steady state response of Figure 23. The
dynamic flight behavior of the horizontal and vertical velocity of the 6 DoF and 12 DoF model
is similar to the reported dynamic flight behavior. Table 5 shows the difference in rise time
settling time and relative overshoot. The large differences are a result of the different steady
states values. The step the 6 DoF and 12 DoF models are making from the steady state at 0 [s]
to the steady state at 30 [s] is much smaller than the step taken by the reported velocity. The
smaller step result in different rise time, settling time and overshoot. The yaw rate shows other
dynamics, than the reported yaw rate. The oscillation in the yaw rate is a result of the tension
line model constraining the relative movement between the parafoil and the load. The 6 DoF


37


does not show any oscillation, since there is no relative movement. The oscillation of the 12 DoF
model are more damped than the oscillations in the reported yaw rate.



13.5


13


12.5


12


11.5
0 10 20 30



5.5


5


4.5


4
0 10 20 30


Figure 25: Dynamic response to _δ_ _s_



Load word velocity and yaw rate

0.3

6



0.2


0.1


0
0 10 20 30



Table 5: Difference in Dynamic behavior

|Variable Model|δ<br>s|Col3|Col4|δ<br>a|Col6|Col7|
|---|---|---|---|---|---|---|
|**Variable**<br>**Model**|dif._ t_r [s]|dif._ t_s [s]|dif._ M_p [-]|dif._ t_r [s]|dif._ t_s [s]|dif._ M_p [s]|
|_V_ n<br>h [m/s]<br>6DoF<br>12DoF|0.03<br>0.05|0.74<br>0.83|0.03<br>0.03|5.60<br>5.59|4.96<br>6.56|3.00<br>2.93|
|_V_ h<br>v [m/s]<br>6DoF<br>12DoF|0.05<br>0.02|2.03<br>2.18|1.31<br>1.32|3.55<br>3.54|8.50<br>7.14|6.19<br>5.96|
|˙_ψ_l [rad/s]<br>6DoF<br>12DoF||||3.69<br>3.34|1.16<br>0.95|0.56<br>0.56|



38


## **7 Discussion and Conclusion**

Some remarks should be made on the presented work. First of all, Yakimenko argues in [4] that
one of the important parts of the aerodynamic drag in a PADS is the line drag. This is not
discussed in this report, but could be easily taken into account in the sum of forces and moments
in the EoM of the parafoil and the load.


The simulation parameters used in Sec. 4 are also the parameter set given by Van der Kolf
in [21]. This set is extensive, but does not include average parafoil thickness and the arc angle of
the parafoil. These are needed to determine the apparent mass and inertia matrices. Therefore
these parameters are estimated. How accurate these estimations are and how they influence
the overall apparent mass effect is not analyzed. Next, Yakimenko argues in [4], that the term
_⃗V_ p [p] _,_ air _[×][ m]_ [p] p m _[⃗V]_ [ p] p _,_ air [can be neglected in the apparent mass effect, since it could be included in]
the aerodynamic expressions. It remains unclear when this is the case or when not. The term
_⃗V_ p [p] _,_ air _[×][ m]_ [p] p m _[⃗V]_ [ p] p _,_ air [is the main contribution in the steady state offset due to the apparent mass in]
Sec 4. For instance consider the system in steady state for a constant symmetric deflection input.
The angular velocity, acceleration and angular acceleration are zero. This simplifies the apparent
mass effect to only _V_ _[⃗]_ p [p] _,_ air _[×][ m]_ [p] p m _[⃗V]_ [ p] p _,_ air [, resulting in the steady state offsets given in Figure 8.]


A note can be made on the model comparison in the validation. The steady state behavior
of the model is in essence a force moment balance of the aerodynamic effect, the gravity and
the apparent mass. Therefore, the steady state is highly dependent on the accuracy of the
aerodynamic force and moment. In this research the aerodynamics presented in [21] is used, in
which already some numerical mistakes are found in the presented matrices. Next to this the
presented model uses a nonlinear expression to constrain the relative yaw between the parafoil
and the load. The 12 DoF uses a linear spring-damper system. These two things together with
the difference in model order, most likely result in the differences present in the validation. The
validation shows that the model has the same behavior as the reported model for zero deflection.
Similar flight behavior is shown for symmetric deflections. The steady state behavior diverges
with maximal 0.4 [m/s]. For asymmetric deflections the steady state behavior is different. The
dynamic flight behavior is similar in the velocity, but the dynamic flight behavior is different in
the yaw rate.


In the future this research can be extended by weakening the rigid body assumption of the
parafoil and dividing it in multiple panels. The panels can rotate with respect to each other.
This is briefly explained in Sec. 3.7 and an expression for the aerodynamic force per panel is
presented there. Furthermore, a tension line representation could be extended towards modeling
real tension lines, in a realistic configuration. The tension moments could then also be modeled
as a result of the tension force. This is also briefly discussed in Sec. 3.7.


To conclude on the research question: ”Which dynamic effects acting on the SR during the
terminal guidance phase should be considered, to describe the flight dynamics of the Space Rider
w.r.t. the desired landing precision and landing constraints of the GNC system? The literature
review gives an expectation”. The 6 DoF model describes the overall flight dynamics based on
the aerodynamics, gravity and the apparent mass. The 12 DoF model adds internal dynamics
due to relative motion between the load and the parafoil. The following effect are considered
relevant in the literature. The gravity, aerodynamics and the apparent mass. The results of the
constructed models, show that The 6 DoF model describes indeed the overall flight dynamics.
The steady state flight behavior of the 6 DoF model is similar to the steady state flight behavior


39


of the 12 DoF. Small differences are visible, when in the 12 DoF model, the load is rotated
relative to the parafoil. The 12 DoF model adds oscillations to the dynamic behavior, due to
the spring-damper system used for the tension line. This is also visible in the linearization. The
frequency responses of the 6 DoF and the 12 DoF models are similar, but the response of the 12
DoF model shows additional dynamics. The gravity and the aerodynamics act similar in both
models. The model is simulated with and without the apparent mass effect. Comparing the
results shows, that the gravity and aerodynamics account for most of the flight dynamics. The
apparent mass adds a steady state offset in the flight behavior.


The question remains how relevant this is to the SR terminal guidance phase. The gravity,
aerodynamics and apparent mass influence the flight behavior, such that is would be important
to include the dynamic effects for position, velocity or heading control. In terms of position,
velocity or heading, the 12 DoF does not add any flight behavior, compared to the 6 DoF model.
The 12DoF model adds dynamics behavior, which is relevant for a changing wind disturbance, or
during the landing. The 12 DoF model could show how the load is oscillating w.r.t. the parafoil
during a landing. This influences the impact of the landing.


In the future, the model developed in this report can be used to improve the GNC of the
Space Rider during the terminal descent phase. The constructed model and the LPV description
of the model along an equilibrium trajectory, give a first impressions for a control strategy. The
linearizations show that the nonlinear model has moving resonances and varying low frequency
gains. Therefore, it is expected that a nonlinear controller will results in a higher GNC performance, instead of a linear controller. With the constructed LPV model an LPV type of controller
can be used for the GNC solution.


40


## **References**


[1] S. Aerospace, C. Severo, O. Ptm, T. Cantos, D. S. S. L. U, R. D. Poniente, and T. Cantos,
“The Design of the GNC of the Re-entry Module of Space,” _8th European Conference for_
_Aeronautics and Space Sciences_, 2019.


[2] A. Figueroa-Gonz´alez, F. Cacciatore, and R. Haya-Ramos, “Landing guidance strategy of
space rider,” _Journal of Spacecraft and Rockets_, vol. 58, no. 4, pp. 1220–1231, 2021.


[3] O. A. Yakimenko, “On the development of a scalable 8-DoF model for a generic parafoilpayload delivery system,” in _Collection of Technical Papers - 18th AIAA Aerodynamic De-_
_celerator Systems Technology Conference and Seminar_, no. January, pp. 642–654, 2005.


[4] O. A. Yakimenko, _Precision Aerial Delivery Systems: Modeling, Dynamics, and Control_ .
2015.


[5] G. Bonaccorsi, _Guidance & Control of a Parafoil-Based Landing on Titan_ . PhD thesis, 2019.


[6] B. J. Rademacher, P. Lu, A. L. Strahan, and C. J. Cerimele, “In-flight trajectory planning
and guidance for autonomous parafoils,” _Journal of Guidance, Control, and Dynamics_,
vol. 32, no. 6, pp. 1697–1712, 2009.


[7] M. Ward, M. Costello, and N. Slegers, “Specialized system identification for autonomous
parafoil and payload systems,” in _AIAA Atmospheric Flight Mechanics Conference 2010_,
2010.


[8] E. Mooij, R. Mazouz, and M. B. Quadrelli, “Convex optimization guidance for precision
landing on titan,” in _AIAA Scitech 2021 Forum_, pp. 1–21, 2021.


[9] M. Ward, S. Culpepper, and M. Costello, “Parafoil control using payload weight shift,”
_Journal of Aircraft_, vol. 51, no. 1, pp. 204–215, 2014.


[10] C. Redelinghuys, “A flight simulation algorithm for a parafoil suspending an air vehicle,”
_Journal of Guidance, Control, and Dynamics_, vol. 30, no. 3, pp. 791–803, 2007.


[11] N. J. Slegers, “Effects of canopy-payload relative motion on control of autonomous parafoils,”
in _Journal of Guidance, Control, and Dynamics_, vol. 33, pp. 116–125, 2010.


[12] E. Zhu, Q. Sun, P. Tan, Z. Chen, X. Kang, and Y. He, “Modeling of powered parafoil based
on Kirchhoff motion equation,” _Nonlinear Dynamics_, vol. 79, no. 1, pp. 617–629, 2015.


[13] Niccol`o GLOUCHTCHENKO, “Multibody parafoil-payload model for SpaceRider trajectory and inflation loads analysis,” p. 111, 2018.


[14] P. B. Lissaman and G. J. Brown, “Apparent Mass effects on parafoil dynamics,” in
_AIAA/AHS/ASEE Aerospace Design Conference, 1993_, 1993.


[15] T. M. Barrows, “Apparent mass of parafoils with spanwise camber,” in _16th AIAA Aerody-_
_namic Decelerator Systems Technology Conference and Seminar_, vol. 39, 2001.


[16] T. Jann, “Aerodynamic coefficients for a parafoil wing with arc anhedral - Theoretical and
experimental results,” in _17th AIAA Aerodynamic Decelerator Systems Technology Confer-_
_ence and Seminar_, no. May, 2003.


41


[17] J. S. Lingard, “Ram-Air Parachute Design,” _Precision Aerial Delivery Seminar, 13th AIAA_
_Aerodynamic Decelerator Systems Technology Conference_, no. May, pp. 1–51, 1995.


[18] T. Bennett and R. Fox, _Design, Development &amp; Flight Testing of the NASA X-38 7500_
_ft2 Parafoil Recovery System_ .


[19] S. M¨uller, M. Heise, O. Wagner, and G. Sachs, “Paralabs an integrated design tool for
parafoil systems,” in _Collection of Technical Papers - 18th AIAA Aerodynamic Decelerator_
_Systems Technology Conference and Seminar_, pp. 704–714, 2005.


[20] N. Slegers, E. Beyer, and M. Costello, “Use of variable incidence angle for glide slope control
of autonomous parafoils,” in _Journal of Guidance, Control, and Dynamics_, vol. 31, pp. 585–
596, 2008.


[21] G. Van Der Kolf, “Flight Control System for an Autonomous Parafoil,” no. December, 2013.


[22] D. Bodmer, M. Krenmayr, and F. Holzapfel, “Asymptotic tracking position control with
active oscillation damping of a multibody Mars vehicle using two artificial augmentation
approaches,” _CEAS Space Journal_, no. 0123456789, 2021.


[23] M. Ben-Ari, “A Tutorial on Euler Angles and Quaternions,” tech. rep., Weizmann
Institute of Science, 2014. AVALAIBLE AT `[https://www.weizmann.ac.il/sci-tea/](https://www.weizmann.ac.il/sci-tea/benari/sites/sci-tea.benari/files/uploads/softwareAndLearningMaterials/quaternion-tutorial-2-0-1.pdf)`
```
  benari/sites/sci-tea.benari/files/uploads/softwareAndLearningMaterials/
```

`[quaternion-tutorial-2-0-1.pdf](https://www.weizmann.ac.il/sci-tea/benari/sites/sci-tea.benari/files/uploads/softwareAndLearningMaterials/quaternion-tutorial-2-0-1.pdf)` .


[24] J. LINGARD, “The Aerodynamics of Gliding Parachutes,” 1986.


42


