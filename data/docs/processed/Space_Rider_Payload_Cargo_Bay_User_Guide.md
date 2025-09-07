ESA UNCLASSIFIED – Releasable to the Public

#### **SPACE RIDER USER GUIDE**


Prepared by Space Rider Team


Document Type TN - Technical Note


Reference ESA-STS-SR-TN-2018-0002


Issue/Revision 2.0


Date of Issue 06/12/2023


Status Approved


ESA UNCLASSIFIED – Releasable to the Public

# **APPROVAL**










|Title Space Rider User Guide|Col2|
|---|---|
|Issue Number<br>2|Revision Number<br>0|
|Author<br>Space Rider Team|Date<br>06/12/2023|
|Checked By<br>Safety<br>Lucio Gradoni|Date<br>06/12/2023<br>Digitally signed by Lucio<br>Gradoni<br>Date: 2023.12.07 16:10:08<br>+01'00'|
|Checked By<br>Security<br>Danilo Ingami|Date<br>06/12/2023<br>Danilo<br>Ingami<br>Digitally signed by<br>Danilo Ingami<br>Date: 2023.12.07<br>16:53:42 +01'00'|
|Approved By<br> <br>Fabio Caramelli|Date<br>06/12/2023<br>Fabio<br>Caramelli<br>Digitally signed by Fabio<br>Caramelli<br>Date: 2023.12.07 17:18:22<br>+01'00'|
|Authorised By<br> <br>Dante Galli|Date<br>06/12/2023<br>Digitally signed by Dante Gal<br>Date: 2023.12.07 17:22:23<br>+01'00'|


# **CHANGE LOG**

Reason for change Issue Nr Revision Number Date


Update to system CDR status close-out 2.0 0 06/12/2023

|CHANGE RECORD|Col2|Col3|Col4|
|---|---|---|---|
|Issue Number<br>2|Revision Number<br>0|Revision Number<br>0|Revision Number<br>0|
|Reason for change|Date|Pages|Paragraph(s)|
|Update to system CDR status close-out|06/12/2023|All|All|


# **DISTRIBUTION**


Name/Organisational Unit


Releasable to the Public


Page 2/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **Table of Contents**


1 EXECUTIVE SUMMARY ......................................................................................... 8


1.1 Scope ...................................................................................................................... 8


1.2 Responsibilities ....................................................................................................... 8


1.3 Definitions ................................................................................................................ 9


1.4 Introduction to Space Rider System ...................................................................... 12


1.4.1 What is the Space Rider? ...................................................................................... 12


1.4.2 What does Space Rider offer? .............................................................................. 13


1.4.3 Typical Space Rider P/L applications .................................................................... 14


1.5 Mission Phases and Profiles ................................................................................. 15


1.5.1 Pre-launch (including Late-Access activities) ........................................................ 15


1.5.2 Launch and ascent ................................................................................................ 16


1.5.3 Orbital flight (including Commissioning) ................................................................ 16


1.5.4 Preparation for De-Orbiting ................................................................................... 20


1.5.5 De-Orbiting ............................................................................................................ 20


1.5.6 Re-entry, Descent and Landing ............................................................................. 20


1.5.7 Post-Landing (including Early-Retrieval activities) ................................................. 21


1.5.8 Post-Flight ............................................................................................................. 21


1.6 In-Orbit Services and Close-Proximity Operations Capabilities ............................. 22


1.6.1 Current Capabilities ............................................................................................... 23


1.6.2 Future Capabilities................................................................................................. 23


1.7 Commercial Exploitation ........................................................................................ 24


2 SPACE RIDER SYSTEM ARCHITECTURE ......................................................... 25


2.1 Flight Segment ...................................................................................................... 26


2.1.1 Space Rider Vehicle .............................................................................................. 27


2.2 Ground Segment ................................................................................................... 32


2.2.1 Mission Control Centre (MCC) .............................................................................. 33


2.3 Landing Site(s) ...................................................................................................... 35


Page 3/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


2.3.1 Landing Site Ground Elements .............................................................................. 36


2.3.2 Landing Site Facilities ............................................................................................ 37


2.4 Launch System and Launch Site (complementary to SRS) ................................... 39


2.4.1 Launcher System................................................................................................... 39


2.4.2 Launch Site Facilities ............................................................................................. 40


3 INTERFACES ........................................................................................................ 41


3.1 Co-ordinates and Reference Frame ...................................................................... 41


3.1.1 Space Rider Vehicle Reference Frame ................................................................. 41


3.2 Mechanical interface .............................................................................................. 42


3.2.1 Mechanical interface connections ......................................................................... 43


3.2.2 Mass and Volume Capability ................................................................................. 45


3.3 Thermal interface................................................................................................... 46


3.3.1 Thermal Control System ........................................................................................ 46


3.3.2 Thermal Conductive Coupling ............................................................................... 47


3.3.3 Thermal Radiative Decoupling .............................................................................. 47


3.4 Electrical interface ................................................................................................. 48


3.4.1 Electrical Power System ........................................................................................ 48


3.4.2 Connectors and power lines .................................................................................. 48


3.4.3 Voltage, current and grounding parameters .......................................................... 50


3.5 Data and Communication interface ....................................................................... 51


3.5.1 Data and Communications interface on-board ...................................................... 51


3.5.2 P/L Data and Communications interface with ground ............................................ 53


3.6 EMC interface ........................................................................................................ 53


3.6.1 Single point of grounding ....................................................................................... 53


4 ENVIRONMENTS.................................................................................................. 54


4.1 Mechanical Environment ....................................................................................... 54


4.1.1 Transportation and Handling ................................................................................. 54


4.1.2 Stiffness requirements ........................................................................................... 54


4.1.3 Quasi-Static (QSL) and Low Frequency (LFL) Loads ............................................ 55

Page 4/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


4.1.4 Sine Loads ............................................................................................................ 55


4.1.5 Random Vibro-Acoustic Environment .................................................................... 56


4.1.6 Shock Environment ............................................................................................... 57


4.1.7 Pressure Environment ........................................................................................... 58


4.1.8 Microgravity ........................................................................................................... 59


4.1.9 Re-entry, Descent and Landing loads ................................................................... 60


4.2 Thermal Environment ............................................................................................ 61


4.2.1 Integration, Transportation and Ground Launch Facility Operations ..................... 61


4.2.2 Launch, Ascent and Orbital phases ....................................................................... 62


4.2.3 Re-entry, Descent and Landing phases ................................................................ 62


4.3 Electromagnetic Environment ................................................................................ 63


4.3.1 RF Compatibility levels .......................................................................................... 63


4.3.2 Aggregate Radiated Susceptibility ......................................................................... 63


4.3.3 Aggregate Radiated Emission ............................................................................... 64


4.4 Space Environment ............................................................................................... 66


4.4.1 External Vacuum ................................................................................................... 66


4.4.2 Atomic Oxygen ...................................................................................................... 66


4.4.3 Cosmic Radiation .................................................................................................. 66


4.4.4 Solar Light ............................................................................................................. 67


4.5 Cleanliness and Contamination Control ................................................................ 67


4.5.1 Cleanliness ............................................................................................................ 67


4.5.2 Contamination analysis ......................................................................................... 68


5 PAYLOAD DESIGN, DEVELOPMENT AND VERIFICATION ............................... 69


5.1 P/L Interface design aspects ................................................................................. 69


5.1.1 Payload Categories ............................................................................................... 70


5.2 Safety requirements .............................................................................................. 71


5.3 Product Assurance Requirements ......................................................................... 73


5.4 Cleanliness and Contamination Requirements ...................................................... 73


5.5 Design Reviews and Follow-Up ............................................................................. 73

Page 5/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


5.6 Payload Deliverables ............................................................................................. 75


5.6.1 Payload Design and Development Technical Documents ..................................... 75


5.6.2 Payload Contractual Documents ........................................................................... 75


5.6.3 Safety Documents ................................................................................................. 76


5.6.4 Payload Models ..................................................................................................... 77


5.7 Export Control ....................................................................................................... 79


6 AGGREGATE VERIFICATION AND INTEGRATION ............................................ 80


6.1 The Payload Aggregate ......................................................................................... 80


6.2 Aggregate Preparation Process ............................................................................ 80


6.2.1 Phase I: Payloads Feasibility Phase...................................................................... 81


6.2.2 Phase IIa: Preliminary Aggregate Definition .......................................................... 81


6.2.3 Phase IIb: Aggregate Definition Confirmation ........................................................ 82


6.2.4 Phase III: Final Aggregate Design ......................................................................... 82


6.2.5 Phase IV: Final Aggregate AIT .............................................................................. 82


6.2.6 Phase V: Aggregate Flight Operations .................................................................. 83


6.2.7 Phase VI: Aggregate Post-flight Operations .......................................................... 83


6.3 Aggregate Verification ........................................................................................... 84


6.4 Aggregate Compatibility Analysis and Tests ......................................................... 84


6.4.1 System-Level Mission Analyses ............................................................................ 84


6.4.2 System-Level Fit Checks ....................................................................................... 84


6.4.3 Preliminary Integration, Electrical and Functional Tests ........................................ 84


6.4.4 Final Integration, Electrical and Functional Tests, Mass Properties ...................... 85


6.4.5 Mechanical, Thermal and EMC Analyses for Aggregate Acceptance ................... 85


6.5 Aggregate Assembly, Integration and Test ............................................................ 85


6.6 Aggregate Safety Acceptance Process ................................................................. 86


7 SPACE RIDER SERVICES FOR PAYLOADS ...................................................... 87


7.1 Mechanical services .............................................................................................. 87


7.1.1 Standard Mounting – Accommodation Service ...................................................... 87


Page 6/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


7.1.2 Non-Standard Mounting – Missioning Hardware Service ...................................... 88


7.2 Thermal services ................................................................................................... 89


7.3 Power services ...................................................................................................... 89


7.4 Data and Communication services ........................................................................ 89


7.4.1 Cybersecurity Aspects ........................................................................................... 90


7.4.2 P/L Security in Space Rider: Opportunities for Independent Protection Measures 91


7.4.3 In-Flight services ................................................................................................... 93


7.4.4 Ground-services .................................................................................................... 93


7.4.5 Mixed services ....................................................................................................... 96


7.5 Microgravity services ............................................................................................. 98


7.5.1 Standard microgravity service ............................................................................... 98


7.5.2 Extreme microgravity service ................................................................................ 98


7.6 Observation / Field-of-View services ..................................................................... 98


7.6.1 Earth-observation service ...................................................................................... 99


7.6.2 Deep-space observation service ......................................................................... 100


7.7 Exposure / Protection To / From External (Space) Environment ......................... 100


7.7.1 Exposure to external environment service .............................................................. 100


7.7.2 Sun-pointing and Sun-avoidance services .......................................................... 100


7.8 Atmospheric services .......................................................................................... 101


7.9 Separation, Retrieval and Robotic Handling services .......................................... 101


7.10 Additional services (Upon Customer’s Request) ................................................. 101


8 DOCUMENTS ..................................................................................................... 102


8.1 Reference Documents ......................................................................................... 102


9 ACRONYMS ........................................................................................................ 103


ANNEX A 108


Possible Applications for Science and Technology Research ............................................. 108


ANNEX B 109


Space Rider Payload Mission Timeline................................................................................ 109


Page 7/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **1 EXECUTIVE SUMMARY**

#### **1.1 Scope**


This document intends to give a commercial prospective and an overview of the essential


technical data to potential Space Rider’s Customers. Information about its general aspects is


reported in the current section while system architecture, data regarding the system interfaces,


the exposed environments, as well as available features and services are detailed in the


following chapters.


Together with reference documents (see section 8.1) the aim of the User Guide is to preliminary


assess the compatibility of a P/L and its mission with Space Rider, to constitute the general


payload service provisions and specifications, and to initiate the P/L preparation of all technical


and operational activities for the launch and its safe return on Earth.


Terms and definitions used in the document can be found below (see section 1.3) as well as


acronyms table (see section 9).


The Customer who is willing to explore flying solutions with Space Rider is welcome to contact


ESA for further details.

#### **1.2 Responsibilities**


This document is produced with the contribution of TAS-I as Flight Segment (FS) entity


responsible for the cargo-bay interfaces. Images and illustrations are courtesy of TAS-I and


AVIO.


ESA is the end responsible of the SR User Guide for the Maiden Flight.


Page 8/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **1.3 Definitions**



**Multi-Purpose Cargo Bay**


**(MPCB)**



The Space Rider cargo-bay, designed to host multiple


Payload with different needs.



**Compartment** Reference volume inside the Space Rider MPCB, defined by


specific interface features with the hosted Payload(s).



**Payload (P/L)**


**Standard Payload (STD)**


**Late-Access (LA)**


**Early Retrieval (ER)**


**Payload**


**Payloads Aggregate**


**(PLAG)**


**Aggregate Design**


**Authority (ADA)**



Object allocated in the MPCB. It could either be a Laboratory


carrying Experiments or an individual Experiment.


Payload that does not require late access/early retrieval


capability nor field of view or direct space exposure.


Payload that requires to be installed just prior to launch


and/or to be recovered just after landing (e.g., environmental


sensitive P/Ls).


The configured list of P/Ls qualified for a specific Space Rider


mission.


The Entity in charge of detailed design, development, I/F


control, verification, missionization (i.e., mission timeline


definition), integration/de-integration and support to flight


operations of the PLAG dedicated to each specific mission.



**MPCB Operator** **[1]** The Entity in charge of the service management, definition of


the Aggregate configuration, final approval of Aggregate


detailed design, negotiation and contract signature with


Customers, verification of vehicle services compliance with


Customers requirements and P/Ls compliance to applicable


mission constraints, management of the End-to-End Payload


1 Limited to SRS Maiden Flight preparation, this role will be covered by ESA.

Page 9/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


Aggregate mission, follow-up, and approval of the Aggregate


Design Authority activities.


**Mission Operator** The Entity(ies) in charge of the launch preparation, the


launch execution, and the management of the Spacecraft


mission until landing and retrieval.



**Customer**


**/ Sub Aggregator**



The Entity owning one or more Payloads.



**Laboratory** A facility dedicated to hosting and managing a defined


number of Experiments during the mission.


**Experiment** A unique item accommodated in a Laboratory or provided as


an individual item.


**Experiment Owner** The Entity in charge of the development of an Experiment.


**Cartridge** Elements of one or more Experiments that are installed in the


Payload through the Late Access service and/or retrieved in


Early Retrieval, due to their sensitivity to the waiting time


before experiment conditions are met.


**Missioning Hardware** Customized hardware to meet aggregate-level requirements,


designed by ADA for a specific Space Rider mission.


**Extension-Kit** Hardware designed to enhance SR built-in capabilities to


meet payload-level requirements upon Customer request.


Page 10/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


Page 11/114



_**Figure 1-1: Definitions graph**_



Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **1.4 Introduction to Space Rider System**


This section will introduce the Space Ryder System describing its composition and general


aspects, features and capabilities and a description on why you should consider flying with it.

##### **_1.4.1 What is the Space Rider?_**


The Space Rider System (SRS) is the first European affordable, independent, re-usable,


uncrewed end-to-end commercial transportation system for routine access to and return from


Low Earth Orbit (LEO). When referring to the SRS, we consider the entire ecosystem of flight


segment, ground segment and facilities that are needed to perform a mission and to support


the Customers for their business. The Space Rider (SR) vehicle, as the main part of the SRS


flight segment, is an uncrewed robotic laboratory about the size of two minivans composed by


a re-entry module and an orbital module. Its dynamic configuration allows P/Ls for an array of


applications, orbit altitudes and inclinations (compatible with the performance of the launcher),


and mission durations. After being launched it will stay in Low Earth Orbit (LEO) for about two


months, while performing experiments inside its cargo bay such as technology demonstration


and research activities in different fields (e.g., pharmaceutics, biology, physical science, ...). At


the end of its mission, the re-entry module will return to Earth and land on a dedicated area to


retrieve the flown payloads while the orbital module performs a destructive re-entry. The re

entry module is then refurbished for another flight.


_**Figure 1-2: The Space Rider (SR) vehicle.**_

Page 12/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_1.4.2 What does Space Rider offer?_**


The Space Rider will offer a unique set of capabilities and services to Customer’s P/Ls:


  A design based on flight-proven ESA IXV Vehicle.


  Extended exposure (two months or more) in Low Earth Orbit (LEO) environment.


  Open Multi-Purpose Cargo-Bay (MPCB) with a wide Field of View (FoV) for Earth or


deep-space observation, and fine-pointing capability.


  Microgravity environment with low g-forces and jitter during flight with high-quality


microgravity environment reaching levels down to 5 x 10 [-6 ] g.


  Reduced in-flight safety constraints vs human spaceflight safety standards and factors.


  Platform provided in-flight services (i.e., attitude control, power, thermal, telemetry and


telecommands) as well as on-ground services (i.e., telemetry stations, in-orbit control


centre, user’s stations for monitoring of in-flight operations).


  - Short time-to-flight, with a maximum advanced flight booking period of one year [2] .


  Reusability roadmap with organisation for a launch rate of up-to 2 launches per year


allowing shorter time-to-space and shorter time-to-data.


  Standard payloads installation in the cargo bay, as well as late-access installation at the


launch pad until a few hours before launch for environmental sensitive P/Ls.


  Return capability with high down-mass / up-mass ratio and precision soft-landing due to


the use of a parafoil that provides governability, both in gliding and in descent speed.


  Early post-landing retrieval of environment sensitive P/Ls with fast access directly at the


landing area.


  Post-flight retrieval of Standard Payloads at dedicated Landing site facility.


  User privacy protection at different levels (e.g., experiment design, data, operations,


industrial knowledge protection).


2 From the FSA signature.

Page 13/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_1.4.3 Typical Space Rider P/L applications_**


The Space Rider provides easy access to and return from space to payloads requiring micro

gravity and/or exposure to the space environment, with accurate pointing capabilities, at lower


price and shorter time conditions with respect to other commercially available competitors.


The Space Rider will enable a wide variety of applications such as (but not limited to):


  Microgravity experimentation


  In-orbit Demonstration (IOD) & Validation (IOV) of technologies for exploration, orbital


infrastructure servicing, Earth observation, Earth science, Telecom, …


  In-orbit Services (IOS) for Earth monitoring, satellites inspections, …


  European pathfinder for commercial services in access and return from space (i.e.,


commercial space manufacturing).


  - Educational missions.


A non-exhaustive list of the scientific and technology research fields that may benefit from the


Space Rider services is provided in [ANNEX A].


Page 14/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **1.5 Mission Phases and Profiles**


This section presents a typical sequence of events for Space Rider mission profiles.


_**Figure 1-3: Depiction of Space Rider mission phases.**_

##### **_1.5.1 Pre-launch (including Late-Access activities)_**


This phase includes different activities such as pre-integration and tests, P/Ls accommodation,


transport to launch site, final integration and tests, transport to launch pad and integration with


launcher, installation of environmental sensitive P/Ls during Late-Access operations through


the fairing doors and the side panels of the vehicle.


_**Figure 1-4: Late-access capability prior to launch.**_


Page 15/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_1.5.2 Launch and ascent_**


This phase starts from the launch on-top of VEGA-C until the injection of SRS into orbit and


the commissioning to begin its orbital phase and operations. Space Rider System operations


are autonomous during this phase, and no telecommands will be sent from the Mission Control


Centre (MCC) during launch and ascent.


_**Figure 1-5: Launch and Ascent phases.**_

##### **_1.5.3 Orbital flight (including Commissioning)_**


This phase starts with the commissioning and vehicle-level preparations to initiate P/L level


activities (e.g., solar array deployment and cargo-bay door opening). Payloads’ operations


follow a mission timeline, managed by the Mission Control Centre (MCC). This period will last


two months or more, with each orbit lasting approximately 90 minutes in a typical 400 Km orbit.


_**Figure 1-6: Orbital phase.**_


Page 16/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**1.5.3.1 Mission Profile and Orbital Attitude Modes**


During the orbital phase P/L Customers will operate for the aim of a specific purpose (e.g.,


exploit a micro-gravity environment, observation of a specific target, high dissipation, etc.) and


this will require that SR to maintain a specific attitude for a specific amount of time. The


Payload’s needs and relative Space Rider attitude(s) are agreed before the flight, during the


mission analysis phase. The below table shows an example of possible SRS attitudes for a


quasi-equatorial circular LEO orbit:



|Attitude<br>Mode|Primary<br>Pointing|Secondary Pointing|Microgravity Level|Typical<br>P/L|
|---|---|---|---|---|
|Nose-to-<br>Nadir|SR Nose to<br>Nadir|Cargo-Bay to Anti-Velocity /<br>Velocity Vector (RWs OFF,<br>MTQ ON)|Extreme micro-g<br>5 x 10-6 g|Biological|
|Nose-to-<br>Nadir|SR Nose to<br>Nadir|Cargo-Bay to Anti-Velocity /<br>Velocity Vector (RWs ON,<br>MTQ ON, RACS ON for<br>desaturation)|Standard micro-g<br>5 x 10-5 g|IOD|
|Tail-to-Sun|SR Tail to Sun<br>direction|-|Standard micro-g<br>5 x 10-5 g|Biological<br>High<br>dissipation|
|Nose-out-of-<br>Plane|SR Nose normal<br>to Orbital Plane|- Z RM|Standard micro-g<br>5 x 10-5 g|Biological|
|Bay-to-Earth|Cargo-Bay to<br>Nadir|SR Nose to Velocity Vector|Standard micro-g<br>5 x 10-5 g|Earth<br>Observation|
|Bay-to-<br>Space|Cargo-Bay to<br>Zenith direction|SR Nose to Velocity Vector|Standard micro-g<br>5 x 10-5 g|Deep Space<br>Observation<br>|
|Inertial|MPCB Inertial<br>Fixed|-|Standard micro-g<br>5 x 10-5 g|Deep Space<br>Observation|
|Bay-to-Out-<br>of-Plane|Cargo-Bay<br>to Space|SR Nose to Velocity Vector|Standard micro-g<br>5 x 10-5 g|Deep Space<br>Observation|


Page 17/114













_**Table 1-1: Orbital attitudes modes**_



Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


_Nose-to-Nadir (N2N)_


Performed pointing the nose of the SR Vehicle to Nadir and assuming the Cargo-bay pointing


to velocity vector. This attitude is foreseen mainly for Extreme micro-g services (see 7.5.2).


_Tail-to-Sun (T2S)_


Performed pointing the tail of the SR Vehicle to Sun direction and the secondary pointing


assuming the SR Cargo-bay pointing to orbital plane. This attitude is foreseen mainly for


Standard micro-g service and for high dissipation needs (see 7.5.1).


_Nose Out-of-Plane (OOP)_


Performed pointing the nose of the SR Vehicle normal to orbital plane and the secondary


pointing assuming the SR Cargo-bay parallel to orbital plane. This attitude is foreseen mainly


for Standard micro-g service (see 7.5.1).


_Bay-to-Earth / Nadir (B2E)_


Performed pointing the SR Cargo-bay to the direction of Earth (i.e., to Nadir) and the secondary


pointing assuming the SR Vehicle nose pointing to velocity vector. This attitude is foreseen


mainly for Earth observation services (see 7.6.1).


_**Figure 1-7 Bay-to-Earth attitude mode.**_


Page 18/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


_Bay-to-Space / Zenith (B2Z)_


Performed pointing the SR Vehicle Cargo-Bay to Space (i.e., to Zenith) and the SR Vehicle


nose to velocity vector. This attitude is foreseen mainly for deep-space observation (see 7.6.2).


_**Figure 1-8 Bay-to-Space attitude mode.**_


_Inertial_


Performed when a specific target pointing is required, mainly for space observation (see 7.6.2).


_Bay-out-of-Plane_


Performed pointing the SR Vehicle Cargo-Bay to space. This attitude is mainly foreseen for


Deep-space observation service as alternative to Bay-to-Zenith attitude mode (see 7.6.2).


_**Figure 1-9 Bay-out-of-Plane attitude mode.**_


Page 19/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_1.5.4 Preparation for De-Orbiting_**


Upon receiving authorization from Mission Control Centre, the Space Rider and its Payloads


will be reconfigured for de-orbit (e.g., vehicle avionics cooling-down, radiator stowage, and


cargo-bay door closure), waiting for the final authorization for De-orbit that is sent based on the


readiness status of all involved parts (vehicle, control centre and landing site conditions).

##### **_1.5.5 De-Orbiting_**


Upon the reconfiguration of the SRS for de-orbit, with activities such as P/Ls cool-down (as


preparation for descent environment), radiator stowage, cargo-bay door closure final


authorization for de-orbit is given, Space Rider will start an automatic sequence to configure


the system for de-orbit and execute the de-orbit boost. This phase ends with the separation of


the Re-entry Module from the AVUM orbital one. The re-entry module proceeds to descent


phase while the orbital module performs a destructive re-entry.


_**Figure 1-10: De-orbit, re-entry, and orbital module separation.**_

##### **_1.5.6 Re-entry, Descent and Landing_**


The Re-entry Module performs autonomously the coasting, re-entry and descent sequences


going from hypersonic to transonic flight until the triggering of a subsonic parachute, slowing


down at the subsonic regime. At an altitude between 6 and10 km, there is the deployment of a


guided parafoil for a controlled descent up to the Landing Area at the Landing Site, where it


reaches ground with proper touchdown conditions and landing accuracy.


Page 20/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


_**Figure 1-11: Re-entry, descent, and landing phases.**_

##### **_1.5.7 Post-Landing (including Early-Retrieval activities)_**


Upon landing, the re-entry module is monitored, and a remotely guided mobile hangar covers


the vehicle prior to operators are allowed to approach and perform the safety activities and


early retrieval of payloads. Early-retrieval payloads are handed over to the Customers for


processing at a dedicated Payload Processing Facility (PPF) at the Landing Site that


guarantees proper level of cleanliness and is equipped with office and laboratory equipment


and tools. The re-entry module is moved to another facility for passivation and decontamination


of the thrusters, retrieval of standard payloads and preparation for shipment to the


refurbishment facilities.


_**Figure 1-12: Post-landing Early-retrieval phase.**_

##### **_1.5.8 Post-Flight_**


A post-flight analysis is performed to identify any non-nominal behaviour and refurbishment


needs. The re-entry module undergoes detailed inspections of all subsystems to complete the


refurbishment sequence and the maintenance or replacement activities are performed. Upon


this, the re-entry module is ready for a next flight with a new orbital module, within six-months.


Page 21/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **1.6 In-Orbit Services and Close-Proximity Operations Capabilities**


Designed to be an affordable, independent, re-usable, uncrewed end-to-end commercial


transportation system for routine access to and return from Low Earth Orbit (LEO), its concept


can be extended to serve as In-Orbit Services (IOS) and Close-Proximity Operations (CPO)


platform in addition to a pure commercial exploitation medium.


Studies for the implementation of technologies and system architecture evolutions are ongoing


to support in-orbit operations. Some related features and capabilities are currently present,


others will be implemented in the near future or will be designed on-demand to support more


complex tasks. In the figure below is shown a vision for Space Rider in-orbit servicing


capabilities:


_**Figure 1-13: Space Rider vision for In-Orbit Services.**_


Page 22/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_1.6.1 Current Capabilities_**


The SR Vehicle is natively designed to perform IOD/IOV of technologies developed for the In

Orbit Services and Close Proximity Operations domains with the unique capability to return the


hosted dedicated P/Ls back to Earth (e.g., for further analyses or possible re-use). In addition,


SR can perform orbital manoeuvres and maintain specific attitudes for the release of small


satellites or CubeSat from P/Ls dispenser during its mission providing in such a way a transport


capability as a service. For this purpose, activities are ongoing to consolidate the definition of


proper zones, forbidden areas, and relative approach corridors to the SR Vehicle.


_**Figure 1-14: Example of P/L separation from SR.**_

##### **_1.6.2 Future Capabilities_**


The SR Vehicle and its architecture can be enhanced to support advanced IOS/CPO


capabilities, making it a cooperative (i.e., capable to control its state in terms of orbit / attitude


and communicate with the visiting vehicle) and prepared (i.e., equipped with proper interfaces)


platform. For example, to support Close Proximity Operations, studies are ongoing on equip


the vehicle with visual markers to support both relative navigation (from rendezvous up to a


very-close distance from vehicle) close and capture phases (docking / berthing operations).


In addition to allow (passive) docking and/or berthing operations, dedicated analyses are


ongoing for the integration of a standard-based mechanical capture interface able to sustain


Page 23/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


design loads and rigidity during joint operations. These operations can vary from: operate


from/to SR Cargo-Bay exchanging P/Ls with other space infrastructures (e.g., space-tugs), life

extension or de-orbiting tasks, inspection, refurbishment, assembly and/or manufacturing.


Many of these activities also requires a robotic arm to perform complex manipulating tasks,


and in this domain, activities are ongoing to host a set of robotic arms demonstrators in order


to better address the above-mentioned capabilities.


_**Figure 1-15: Space Rider mission’s concept for IOS and CPO – artistic impression.**_

#### **1.7 Commercial Exploitation**


ESA is committed to support and provide access to space to European research, development,


and commercial entities. Commercialisation potential and European competitiveness are focus


areas for ESA which is mapping the value chain, European supply, and world-wide demand


with the final goal to promote international market access to Space Rider that plays a game

changer role in these emerging markets thanks to its flexibility and potential short lead time


response to Customer needs. For example, microgravity exposure capability is fundamental


for development and commercialisation of new products, dedicated market surveys suggest


forthcoming steep increase of market demand for experimentation and in-space manufacturing


in LEO for pharmaceutical and bio-tech applications and current and future IOD/IOV and In

Orbit Services / Close Proximity Operations related markets in Europe and worldwide.


Page 24/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **2 SPACE RIDER SYSTEM ARCHITECTURE**


The Space Rider System (SRS) is composed by the vehicle itself and all the ground-based


sites, facilities and equipment used by operators and support personnel for the management


of the spacecraft for the launch, in orbit operations, distribution of payload data and telemetry,


re-entry, landing and refurbishment phases. The overall SRS architecture is composed by:


  The Flight Segment


  The Ground Segment


  The Landing Site(s)


In addition, the SRS will use and will be interfaced with a Launch System to reach orbit and a


Launch Base from which performs its mission.


_**Figure 2-1: Space Rider System (SRS) Architecture**_


Page 25/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **2.1 Flight Segment**


The Flight Segment (FS) is the part of the SRS architecture that will comprehends the Space


Rider Vehicle, that will reach the orbit carrying the payloads inside its cargo-bay and all the


related facilities for integration, test, and refurbishment in addition to all the ground support


equipment and test models. In particular, the FS include:


  Space Rider Vehicle:


`o` Including its Multi-Purpose Cargo Bay (MPCB), hosting the payloads.


  Integration, Test and Refurbishment Facilities.


In addition, the FS will use and will be interfaced with different Ground Support Equipment and


Test Models (e.g., RM Avionic Test Bench or ATB).


_**Figure 2-2: SRS Flight Segment architecture.**_


Page 26/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_2.1.1 Space Rider Vehicle_**


The Space Rider Vehicle is an uncrewed spacecraft, part of the SRS flight segment, composed


by two modules, the AVUM Orbital Module (AOM) and the Re-entry Module (RM).


_**Figure 2-3 Space Rider Vehicle.**_


**AVUM Orbital Module (AOM)**


The AOM is a modified version of the VEGA-C upper stage, able to supply power, perform


manoeuvres and provide attitude control to the SR vehicle, up to the separation of the two


modules. It is made of a slightly adapted VEGA-C upper stage and the ALEK (AVUM Lifetime


Extension Kit), a newly developed avionic module whose purpose is to provide electrical power


(through dedicate solar arrays, see Figure 2-4) and attitude control. After separation and de

orbiting boost, AOM is disposed by means of a destructive atmospheric re-entry.


_**Figure 2-4 AVUM Orbital Module (AOM) artist’s impression**_


Page 27/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Re-entry Module (RM)**


The RM is a modified version of the IXV (Intermediate eXperimental Vehicle [3] ) equipped with a


dedicated cargo-bay for hosting P/Ls, able to perform ground landing and to re-fly after


refurbishment. The cargo-bay door opens during the orbital phase to allow observation and


exposure to the space environment, and to provide thermal control via a deployable radiator.


The RM is also equipped with two lateral compartments, that can be accessed right before


launch and after landing, dedicated to environmental sensitive P/Ls. At the end of its orbital


phase, the RM is separated from the AOM, performs atmospheric re-entry and a guided landing


on ground where P/Ls are retrieved. The RM is designed to perform 6 flights, upon limited


refurbishment.


_**Figure 2-5 Space Rider - Re-entry Module (RM)**_


_Multi-Purpose Cargo Bay (MPCB)_


The P/Ls hosted on a SR flight will be accommodated in the so-called Multi-Purpose Cargo


Bay (MPCB) a dedicated section of the RM where P/Ls interfaces and services are provided.


The MPCB allows the accommodation of multiple P/L configurations as well as the necessary


structures for mechanical fixation and thermal control. It can accommodate sealed or vented


P/Ls, directly or partially exposed (e.g., direct illumination, field-of-view, etc.) to space


3 https://www.esa.int/Enabling_Support/Space_Transportation/IXV

Page 28/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


environment. The internal geometrical volume available goes up to 1.2 m [3], able to


accommodate up to 600 Kg of P/L instruments [4] mass. The maximum allowed mass for the


Payload Aggregate is also driven by launcher capability.


_**Figure 2-6: The Multi-Purpose Cargo Bay (MPCB)**_


The accessibility to the MPCB is guaranteed by the MPCB door (as shown in Figure 2-7) that


allows an access dimension of 1200 mm x 718 mm (including door fixed mechanisms) during


the Standard Payload integration and retrieval operations. For the Late-Access integration and


Early-Retrieval operations of environmental sensitive P/Ls, the RM is also equipped with two


lateral doors (see Figure 2-7) that allow an access dimension of 575 mm x 262 mm dedicated


to access to the outer face of P/Ls mounted on selected LA/ER Support Plates (see section


3.2.1 for further details). A digital PDF-based interactive 3D model of the SR MPCB can be


provided on demand for a more detailed overview [RD9].


4 Net instruments, including dedicated P/L hardware (e.g., brackets, adapters, etc.) but excluding any missioning
hardware required for the instrument to be operated since part of the SRS provided services (e.g., thermal
control, telemetry, power, propulsion, attitude, orbit control, etc.).

Page 29/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


_**Figure 2-7 MPCB Main door access main dimensions.**_


The MPCB provides 7 P/Ls aluminium made Support Plates (SP) which purposes are to be:


  The standardized mechanical fixing interface between P/Ls and the RM cold structure.


  The thermal conductive path between the P/Ls and the RM Thermal Control System.


The Figure 2-8 shows the position of the Support Plates within the RM MPCB. For further


details on the Support Plates as mechanical and thermal interfaces see section 3.2 and 3.3.


_**Figure 2-8 MPCB Support Plates overview**_


Page 30/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Integration, Test and Refurbishment Facilities**


For what concerns integration, test, and refurbishment facilities for P/Ls and SR vehicle [5] :


1. The RM will be prepared at Integration Facility at TAS-I premises in Turin (TO), Italy.


Here will also be executed the P/Ls fit check on the MPCB of the RM Flight Model (FM)


and the preliminary integration tests between P/Ls electrical and functional test models


and the RM Avionic Test Bench (ATB) (for further details see section 5.6.4 and 6.4).


2. For the Maiden Flight (MF) only, prior to be moved to the launch site, the SR vehicle will


be shipped to the ESA ESTEC in Noordwijk, The Netherlands for its environmental test


campaign. After that, at same location, the final integration tests will be performed


between the delivered Customer’s qualified P/Ls and the RM Flight Model (FM).


3. At this point the SR will be shipped to the launch site at Europe’s Spaceport in Kourou,


French Guiana. Here remaining P/Ls that are environmental sensitive and or require


late-access capability will be lately integrated.


4. After the flight, the P/Ls are recovered and returned to the Customers and the RM will


be shipped to the Refurbishment Facility at TAS-I premises in Turin (TO), Italy.


_**Figure 2-9: Integration, Test and Refurbishment Facilities and locations.**_


5 For a more comprehensive list of P/Ls test and activities, their related locations and time schedule please refer
to the ANNEX B.

Page 31/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **2.2 Ground Segment**


The Ground Segment (GS) is in charge of vehicle and P/Ls monitor and control from target


orbit achievement until early post landing phase when the vehicle is switched off. It is


composed by all the facilities and equipment based on the ground for the management of the


SRS operations and its activities include (but not limited to):


  Receiving and processing TM data both in real time and through TM dumps.


  Prepare, validate, and upload TC products both for S/C and for Payloads as needed.


  Plan and re-plan mission activities including payloads operations.


  Ensure attitude and orbit control as required by system and payloads needs.


  Monitor the AOM during its re-entry phase.


  Monitor the RM during atmospheric re-entry phase as allowed by the duration of the


blackout phase and availability of Ground Stations.


  Monitor and command as needed the RM during approach and landing operations.


  Support the RM activities during the post landing phase up to the vehicle switch off.


  Archive data (received TM and sent TC) and generate long term archiving products.


_**Figure 2-10: SRS Ground Segment architecture.**_


Page 32/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_2.2.1 Mission Control Centre (MCC)_**


The Mission Control Centre is the part of the G/S dedicated to the control of the vehicle (and


its payloads) during the launch, orbital and landing operations. It is composed by:


  The Vehicle Control Centre (VCC) composed by:


`o` Vehicle Control Centre – Orbital Control (VCC-OC)


`o` Vehicle Control Centre – Landing Control (VCC-LC)


  The Payloads Ground Control Centre (PGCC)


All the communications between the SR vehicle and the MCC during the mission is guaranteed


by the use of a world-wide Ground Station Network (GSN).


**Vehicle Control Centre (VCC)**


The VCC is the part of the Ground Segment that is in charge to control and monitor the SR


vehicle during all its mission timeline, sub-divided in orbital and landing control centre.


_Vehicle Control Centre – Orbital Control (VCC-OC)_


Located at Fucino Space Centre, Italy, under Telespazio (TPZ) responsibility. It is in charge of


monitoring and control the SR vehicle after orbit achievement and until de-orbit (including AOM


re-entry), exchanging data with Launch Site, worldwide located Ground Stations, and Payloads


Ground Control Centre (PGCC) in Turin via secured network links. It is also in charge of


organizing and coordinating the Ground Station Network (a mix of ESTRACK and Commercial


Ground Stations used to allow world-wide coverage for a SR mission).


_Vehicle Control Centre – Landing Control (VCC-LC)_


Located in Turin, Italy, under ALTEC responsibility. It is in charge of monitoring and manage


the RM during re-entry, descent and landing phases, exchanging data with the Landing Site


(also managing the Landing Site Ground Station), ensuring this way the successful recovery


of the RM at the end of the mission.


Page 33/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Payloads Ground Control Centre (PGCC)**


Located in Turin, Italy, under ALTEC responsibility. It is in charge to manage the P/Ls


operations during the orbital phase and to provide to the P/L Customers user dedicated


services via secured network link. The PGCC is dedicated to the monitoring and control of the


P/Ls, interfacing with the User’s Payload Operations Centre (UPOC) for data exchange.


The ground segment, through the PGCC, will make available to the end-users a set of services


that will allow an easy management of the P/L requests, their mission planning, monitoring of


their activities and P/L data delivery (see section 7.4.4 for further details).


**User Payload Operations Centre (UPOC)**


During mission operations, the PGCC will interface directly only with the Customers, though


their designated User Payload Operations Centre (UPOC). The PGCC represents the access


point for UPOC(s) to the SRS mission and P/L(s) data and provide all the means for Customers


to both submit user operation requests for P/L planning activities, monitor P/L status and


retrieve P/L acquisition data, other than providing visibility to a subset of pre-agreed information


regarding the spacecraft that can be useful for P/L planning (see section 7.4.4 for further


details).


Page 34/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **2.3 Landing Site(s)**


The SR re-entry module is capable to perform a controlled re-entry, descent, and touchdown


at chosen Landing Site (LDS), depending on mission characteristics and purposes. The


compatible landing site must be in the proximity of an airport or a port with a dock and equipped


with proper landing areas and facilities to support the P/Ls retrieval operations and the


preparation for the shipment and refurbishment phase of the RM. The currently identified


Landing Site(s) for the SR vehicle are:


  The Europe’s Spaceport in Kourou, French Guiana (for near-equatorial missions and


baseline for the MF).


  Santa Maria Airport, Santa Maria, in the Azores, Portugal (for mid-inclination missions).


  An undisclosed location, in Italy.


The identified Landing Site, based on baseline landing site architecture, should provide the


following facilities and ground-related elements:


_**Figure 2-11: SRS Landing Site(s) architecture.**_


Page 35/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_2.3.1 Landing Site Ground Elements_**


The Landing Site Ground Elements is composed, among others, by the following main blocks:


  Operations Management Room


  Safety Control Room and Neutralization Service


  Weather Monitoring System


  Radar and Video Tracking System


The LDS will also use the Ground Station Antenna to communicate with RM during re-entry.


**Operations Management Room**


The Operations Management Room hosts the Landing Site Director of Operations (LSDO),


Room, who is the responsible for the coordination of all the Landing Site operations. Focal


point of the Landing Site in direct voice link with the Operations Director at the VCC. Also


reporting the readiness of the Landing Site to proceed with the de-orbiting of the Space Rider.


**Safety Control Room and Neutralization Service**


Hosts the Landing Site Safety authority, responsible for all the safety aspects of the Landing


Site up until Landing, including activating the neutralization system of the RM, if necessary.


After landing, the Post Landing Ground Safety Office (PLGSO) takes over the safety aspects.


**Weather Monitoring System**


It will provide services towards the VCC-LC, including forecast, nowcast, soundings, low and


medium altitude wind measurements during preparation, de-orbit, and landing phases.


**RADAR and Video Tracking System**


The Landing Site will provide both a primary and a secondary RADAR to track the vehicle


during the last phase of the mission. The Video Tracking System instead, is capable of visually


tracking the vehicle during the final phase of the flight up to 21 km distance and until vehicle


touch-down.


Page 36/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_2.3.2 Landing Site Facilities_**


The Landing Site (LDS) Facilities part is composed by four main blocks:


  Space Rider Port (SRP).


  Decontamination Facility, Vehicle Inspection & Check Facility, Post-Landing Processing


Facility and Packing, Handling, Storage and Transport Facility.


  Payloads Processing Facilities and Laboratories (PPF & Labs).


At LDS a Mobile Hangar (MH) will also be used to operate on the RM just after the landing.


**Space Rider Port (SRP)**


The Space Rider Port (SRP) is a dedicated access-controlled area inside the Landing Site (LS)


dedicated to RM operations. It comprises the following zones:


  **Landing Area** : dedicated area comprising the Touchdown Zone and the Rollout Zone.


  **Touch-down Zone (TZ)** : dedicated area for touch-down of RM inside the Landing Area.


  **Roll-out Zone (ROZ)** : dedicated safe zone beyond the Touchdown Zone.


  **Roofed Storage Zone** : dedicated zone with roof close to the Landing Area, to


accommodate the Mobile Hangar (MH), RM GSE and offices.


_**Figure 2-12: Space Rider Port**_


Before being transported to the Post-Landing Processing Facilities, the RM will undergo cool

down and power-down phases, deactivation of the electric and pyrotechnic circuits and


retrieval of environmental sensitive P/Ls directly at the Landing Area with the use of the Mobile

Page 37/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


Hangar (MH) equipped with thermal, contamination sensors and an air conditioning system to


protect and cool-down the RM immediately after landing. After about an hour, escape suit


operators enter the MH and retrieve the environmental sensitive P/Ls via RM side panels.


**Facilities for the Management of the Vehicle**


The RM will then be moved to the decontamination where all hazardous material remaining will


be passivated or decontaminated to keep the subsequent operations on the RM safe. The RM


will be inspected, and the operators will proceed to the retrieval of Standard Payloads


(consequently moved to the Payloads Processing Facilities), recorded flight and P/Ls data.


Finally, the RM will be prepared for storage and shipment to the refurbishment site.


**Payloads Processing Facilities and Laboratories**


The P/Ls recovered after landing will be moved from the Post-Landing Processing Facility (or


directly from the Landing Area for biological sensitive P/Ls) to a dedicated Payload Processing


Facility (PPF) via an environmental controlled path. PPF has a size of at least 8 m x 5 m,


equipped with regular offices and laboratory tools, refrigerators and one ESD workbench


among others. It guarantees ISO 8 level of cleanliness and maintaining a temperature of 22 ±


3 °C and a RH between 45% and 65% (see [RD1] and [RD2] for further details).


  - **Laboratories** : Bio-Safety Level-1 class laboratory [6] will be made available to Customers


at the LDS within driving distance from the Landing Area compatible with P/Ls needs.


_**Figure 2-13: Flow of Re-entry Module and Payloads operations after landing.**_


6 Bio-Safety Level-2 (or above) class laboratory availability can be evaluated on demand.

Page 38/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **2.4 Launch System and Launch Site (complementary to SRS)**


The Launch System and Launch Site (LS) are respectively the launcher and the spaceport


from which SRS will lift-off to start its mission.


  The Launch System


`o` VEGA-C launcher


  The Europe’s Spaceport in Kourou, French Guiana (including):


`o` Launch Site Ground Elements


`o` Launch Site Facilities


_**Figure 2-14: SRS Launcher System and Launch Base architecture.**_

##### **_2.4.1 Launcher System_**


The baseline launch system for the SR is the VEGA-C, an upgraded and more powerful version


of the VEGA launcher that increases the performance and the flexibility for multiple payloads


missions allowing quasi-equatorial or polar orbits.


A detailed description of the baseline launch system, performance, typical mission profiles,


environmental conditions, interfaces and in general all launcher-related aspects can be found


in [RD1] and [RD2].


Page 39/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_2.4.2 Launch Site Facilities_**


The Europe’s Spaceport in Kourou, French Guiana will be the baseline Launch Site (LS),


providing all the facilities and support services to perform the launch of the SR vehicle. The


site will also provide the ground segment for the management of launch sequence and early


flight phase.


Different facilities and support structures will be made available to the Customers to support


late-integration and payload management. A detailed description of CSG facilities,


environmental conditions, services (e.g., power supply, communication networks,


transportation and handling, fluids, and gases, etc.) in addition to operations policy and


planning constraints and in general all launch base related aspects can be found in [RD1] and


[RD2].


_**Figure 2-15: The Europe's Spaceport at Centre Spatial Guyanais (CSG).**_


Page 40/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **3 INTERFACES**

#### **3.1 Co-ordinates and Reference Frame**

##### **_3.1.1 Space Rider Vehicle Reference Frame_**


The Space Rider vehicle reference frames are a right-handed, orthogonal coordinate systems


used for geometrical configuration, design drawings and dimensions.


The Re-entry Module (RM) reference frame has the origin at the base of the RM vehicle, at the


geometric centre of the launcher adapter ring, positioned at 206.4 mm long the positive “X”


direction w.r.t the interface plane between RM and AOM.


  The positive “X” is along the vehicle centre line positioned at 206.4 mm long the positive


“X” direction w.r.t the launcher interface flange between RM and AOM.


  The positive “Y” is, parallel to the side upon which the thermal protection and flaps are,


pointing port side.


The positive “Z” is opposite to the thermal protection and flaps. The RM coordinate system is


tilted of 1.3 degree about -Y axis with respect to the AOM X axis (the latter parallel to the


launcher vertical axis).


_**Figure 3-1: SR Reference System.**_


Page 41/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **3.2 Mechanical interface**


The MPCB is equipped with so-called Support Plates that provide the mechanical interface to


the P/Ls. There are 7 Support Plates, distributed according to the following list:

|Support Plate Number|Description / Remarks|
|---|---|
|Plate #1|Vertical Backward / Aft|
|Plate #2|Bottom|
|Plate #3|Vertical Forward / Bow|
|Plate #4|Late-Access / Early-Retrieval Lateral Starboard (-Y)|
|Plate #5|Late-Access / Early-Retrieval Lateral Port (+Y)|
|Plate #6|Lateral Forward Starboard (-Y)|
|Plate #7|Lateral Forward Port (+Y)|



_**Figure 3-2: MPCB Support Plates definition**_


_**Figure 3-3 MPCB Support Plates allocation**_


Page 42/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_3.2.1 Mechanical interface connections_**


**Standard Payloads plate interface connection**


P/Ls installed during standard integration will be hosted in one of the MPCB compartments and


mechanical fastening on the MPCB support plates. Each MPCB support plate has the following


characteristics:

|Parameter|Value|
|---|---|
|Material|Aluminium|
|Drilled Holes Dimension|M6 threaded holes|
|Plate Drilled Pattern|58 mm standard pitch in each In-Plane direction|
|Thickness|13 mm Lateral plates<br>8.5 mm Bottom and Vertical Plates|
|Flatness|<0.1 mm for surface 100x100 mm2 <br>≤0.2 mm for the overall Support Plate surface|
|Roughness|< 3.2 μm|



_**Table 3-1: Support Plates mechanical fastening parameters.**_


The P/Ls mechanical fastening is ensured by the use of fasteners and bolts and the


allocation will be iterated and finally determined by the ADA through the PLAG design


process after evaluation of P/Ls requirements and aggregate’s constraints. Any further needs


or mechanical interface adaptation rising during PLAG design process should be addressed


to the ADA for evaluation.


Page 43/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Late-Access interface connection**


P/Ls with equipment that cannot be installed during standard integration (i.e., experiment’s


cartridges with environmental sensitive material) can be hosted in one of the two MPCB


dedicated lateral compartments in order to be accessed by a TAS-I (RM Prime) human


operator briefly prior launch (see ANNEX B). The LA compartments are accessed through


dedicated launcher fairing’s doors and via SR RM lateral panels (see Figure 3-4):


_**Figure 3-4: RM Late-Access door dimension.**_


P/L equipment’s that requires LA capability shall implement design solutions to guarantee an


easy integration flow, intended as an activity that would involve the human operator installing


the items (e.g. cartridges) on the P/L docking interface making use of their handling capability,


fast or self-locking mechanism in order to ensure required interface connections (e.g.: fastening


possibly without the use of tools and/or bolts preferring a plug-in/plug-and-play mechanism).


The need of a human operator will impose additional handling, dimension, weight, and safety


constraints to LA P/Ls:

|Description|Value|
|---|---|
|VEGA-C Fairing doors diameter|420 mm|
|RM LA compartment door dimensions|262 mm x 575 mm|
|LA P/L maximum allowed mass|<= 6 Kg|
|Late-Access integration time window|30 min7|



_**Table 3-2: Late-Access interface constraints**_


7 This time is considered for both compartments, operated in parallel (see ANNEX B).

Page 44/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


The P/L docking interface part, designed, qualified, and provided by the Customer, that will


host the LA equipment(s), will be fixed on the SR RM Support Plates and will provide thermal,


power and data connectivity. This will be integrated at the Europe integration site as baseline.

##### **_3.2.2 Mass and Volume Capability_**


The maximum allowed mass for each Support Plate is:

|Support Plate|Mass [kg]|
|---|---|
|Plate #1|65|
|Plate #2|230|
|Plate #3|85|
|Plate #4 Late-Access / Early-Retrieval|70|
|Plate #5 Late-Access / Early-Retrieval|70|
|Plate #6|40|
|Plate #7|40|
|**Total**|**600**|



_**Table 3-3 Support Plates mass capability.**_


The above reported mass breakdown shall be intended considering eventually P/Ls needed


missioning hardware. For the volume capability, due to the irregularity of the MPCB


compartments, detailed information about the available volume parameter for each


compartment will be provided after P/L preliminary accommodation. A 3D digital model of the


MPCB and relative compartments is available and reported as [RD9]. For Deployable-PL and


Movable-PL structures the volume and kinematics envelope will further depend on CPO and/or


safety constraints.


P/L accommodation in MPCB Support Plates shall be part of PLAG design specific to each


mission performed by the ADA. P/L positioning will be subject to this logic in compliance with


Customer requirements (e.g., mass, volume, FoV, …).


Page 45/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **3.3 Thermal interface**

##### **_3.3.1 Thermal Control System_**


The SR RM can provide thermal dissipation to the hosted P/Ls through the Thermal Control


System (TCS) via the MPCB aluminium-made Support Plates which provide the thermal control


interface to the P/Ls. The Support Plates provide a heat conductive path to a heat pipe network


and a deployable radiator on the MPCB main door (when open) allowing passive heat rejection.


_**Figure 3-5 RM MPCB Thermal control system**_


The thermal dissipation capability depends on the current phase of the mission:







|Phase|Thermal Dissipation Capability8|I/F Temperature|
|---|---|---|
|Pre-launch|50 W limited by MPCB door closed.|≤ 40 ± 5 ºC|
|On-orbit|Up to 600 W (attitude dependant)|[-35 ÷ 40] ± 5 ºC|
|On-orbit|Up to 500 W (attitude dependant, micro-gravity)|[15 ÷ 35] ± 5 ºC|
|Post-Landing|50 W limited by MPCB door closed.|≤ 40 ± 5 ºC|


_**Table 3-4: Thermal dissipation parameters.**_


8 For the whole Payload Aggregate.

Page 46/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


On ground, launch and ascent phases Space Rider can guarantee 50 W of thermal dissipation


to the aggregate continuously, this value is driven from thermal dissipation constraints, the


cargo bay door is closed, and the thermal dissipation is achieved through conduction of the


support plates through the structure of the spacecraft. The aggregate power request will be


provided from Space Rider internal battery until the solar array deployment and the value shall


not overcome the value of 50 W until the Cargo Bay door will be open and the commissioning


phase will be ended.

##### **_3.3.2 Thermal Conductive Coupling_**


Thermal dissipation of the heat generated by the P/Ls on the MPCB Support Plates is ensured


by the use of a thermal filler in order to have a good linear contact between the P/L baseplate


and Support Plate. The need of any additional thermal provisions required by the P/L, such as


thermal spacers or specific thermal filler, shall be notified to the ADA.


The allowable payload base contact heat-flux to MPCB support plate I/F shall be in the range:

|Parameter|Value [W/m2]|
|---|---|
|Minimum heat flux|0|
|Maximum heat flux|2000|



_**Table 3-5 Thermal heat-flux range**_

##### **_3.3.3 Thermal Radiative Decoupling_**


Payloads must be radiatively decoupled from the external environment for their thermal control.


Except for the face in contact with the MPCB Support Plate and openings for Payload specific


needs, all Payload faces shall be covered in MLI (provided by the Customers). MLI


characteristics will be provided upon request.


In addition, the top of MPCB will be closed by a special MLI thermal blanket, acting as


sunshade, to prevent sun trapping and solar multiple reflections within the MPCB enclosure.


This thermal blanket will be tailored to meet Payload needs related to FoV, visibility for In Orbit


Services (IOS) and Close Proximity Operations (CPO).


Page 47/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **3.4 Electrical interface**

##### **_3.4.1 Electrical Power System_**


The SR RM can provide electrical power supply to the MPCB hosted payloads through the


Power Distribution Unit (PDU). The power is routed among the MPCB compartments through


lines and the amount depends on the current phase of the mission:





|Phase|Power Supply Capability|
|---|---|
|Other|50 W9 limited by thermal constraints.|
|Orbital nominal|Up to 600 W9 depending on solar panel orientation and<br>vehicle attitude.|
|Orbital<br>maximum|A maximum peak of power consumption of 1 kW12 can be<br>supported for limited time length10 (to be agreed upon<br>optimization).|


_**Table 3-6: Power supply parameters.**_



During Late-Access operations the power supply will be switched off for 30 minutes for


integration. P/Ls shall be able to survive these time windows without any power. Alternatively,


they shall include in their architecture an autonomous battery.


During the ascent phase the Payload Aggregate’s power request will be met using Space


Rider’s internal battery until the solar array deployment. The power value during this phase


shall not exceed the value of 50 W until the Cargo Bay door is open and the commissioning


phase has ended.

##### **_3.4.2 Connectors and power lines_**


Power supply between SR-RM PDU and P/Ls is provided by the use of power lines and


connectors from lateral side of the MPCB mid-bulkhead.


9 For the whole Payload Aggregate.
10 During short periods of maximum 90 minutes, once per day for the whole aggregate. During this period the
RM attitude-related thermal dissipation capability (see 3.3.1) cannot be overcome.

Page 48/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


The overall MPCB electrical power is shared through a total of 11 LCL protected power lines,


nominally according to the distribution in the table below (definitive configuration can be


different for each mission):













|Line nominal<br>power [W]|Number of<br>lines|LCL<br>class|Nominal<br>Current [A]|Output current<br>limit (𝑰 )<br>𝑻𝑹𝑰𝑷|
|---|---|---|---|---|
|40|5|2|≤ 2|2.4 ± 5%|
|100|3|4|≤ 4|4.8 ± 5%|
|200|2|8|≤ 8|9.6 ± 5%|
|400|1|16|≤ 16|19.2 ± 5%|


_**Table 3-7: Power lines typologies.**_


The maximum peak of consumption of 1 kW can be supported through a combination of the


available lines, depending on the aggregate combined needs.


The aggregate power lines will be provided as missioning hardware and manufactured at the


proper length to guarantee the capability to provide each Payload with the requested power


connection.


Power connectors from RM PDU are installed on a plate in the lateral side of the MPCB mid

bulkhead (see Figure 3-6). Depending on power needs, P/Ls should include in their design the


connector(s) of the following typologies:

|Line nominal power [W]|Connector Type|
|---|---|
|40|DEMA-09P-NMB|
|100|340105601B0X11-15-19PN|
|200|340105601B0X10-13-98PN|
|400|340105601B0X10-15-19PC|



_**Table 3-8: Power connector types.**_


The needed connector and its relative position (i.e., which face of the Payload to be installed)


shall be iterated and agreed upon with the Aggregate Design Authority.


11 Where 0X is the connector shell type and can be 00 or 07.

Page 49/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_3.4.3 Voltage, current and grounding parameters_**

|Parameter|Value|
|---|---|
|Voltage|28V unregulated [33÷ 26] V|
|Current|2 – 16A|
|Grounding|Payload(s) shall provide a single point<br>of grounding (SPG)|



_**Table 3-9: Voltage, current and grounding parameters.**_


At switch-on and for any mode change, the in-rush charge (current x time) to any P/L shall be


limited to the following parameter:

|Parameter|Value|
|---|---|
|In-rush charge|Ipeak < 30A|



_**Table 3-10: In-rush current.**_


The maximum total charge will be:







|LCL Class|Min Tripp off time<br>[ms]|Maximum Total charge<br>[mC]|
|---|---|---|
|2|8|16|
|4|8|32|
|8|5|40|
|16|5|80|


_**Table 3-11: Maximum total charge.**_


The aggregate-level test will be performed considering the maximum and the minimum voltage


bus to the P/Ls (compliant to ECSS-E-ST-20-07C).


P/Ls shall make the necessary provisions to have their design compatible with SR power


supply.


Page 50/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **3.5 Data and Communication interface**


The SR RM can provide to the MPCB hosted payloads the capability to send/receive data (TM)


and telecommands (TC) through the Mass Memory Unit (MMU) via On-Board Computer


(OBC). This information is routed among the MPCB compartments through data lines.

##### **_3.5.1 Data and Communications interface on-board_**


**3.5.1.1 Connectors and data lines**


Communication between SR-RM MMU and P/Ls is provided by the use of data lines from MMU


to P/L data interface connector(s).


_**Figure 3-6: Data lines in the MPCB.**_


Data and communication lines available at MPCB level are:

|Line type|Number of available lines|
|---|---|
|Ethernet|20|
|SpaceWire|10|
|RS422|10|



_**Table 3-12: Data and communication line types.**_


The aggregate data lines will be provided as missioning hardware and manufactured at the


proper length to guarantee the capability to provide each Payload with the requested data


connection.


Page 51/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


The SR-RM data connector baseline is:

|Parameter|Value(s)|
|---|---|
|Data connector types|MDMA-9S|



_**Table 3-13: Data and communication connector types.**_


The connector’s relative position (i.e., which face of the Payload to be installed) shall be iterated


and agreed upon with the Aggregate Design Authority.


**3.5.1.2 Protocols**


Data communication is implemented with different protocols at different levels. The Payloads


supported communication protocols are:

|Layer|Protocol(s)|
|---|---|
|Link-level|• Ethernet<br>• SpaceWire<br>• RS-422|
|Network-level|• IP (Ethernet)|
|Transport-level|• UDP (Ethernet)|
|Application-level|• Compliant to the ECSS PUS standard [see RD6],<br>opportunely tailored for SR.<br>• Not compliant to ECSS PUS standard.|



_**Table 3-14: Data and communication supported protocols.**_


**3.5.1.3 Data Rate Transmission On-Board Capability**


Data-rate transmission capability depends on the selected link-level protocol. We can have:

|Protocol|Data-rate|
|---|---|
|Ethernet|12.75 MBytes/s to be shared among all the Payloads<br>connected to this interface and transmitting at the same time|
|SpaceWire|20 MBytes/s to be shared among all the Payloads connected to<br>this interface and transmitting at the same time.<br>Video data from P/Ls to MMU up to 200 Mbps12|



Page 52/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


RS-422 0.125 MBytes/s per payload and therefore constant regardless


of the number of payloads connected to this interface


_**Table 3-15: Data and communication on-board parameters.**_

##### **_3.5.2 P/L Data and Communications interface with ground_**


The data and communication systems allow the P/Ls to communicate with the MCC through


the RM MMU in order to send telemetry and receive telecommands for their operations. The


communication link is performed through the use of the S-band.

|Parameter|Value|
|---|---|
|Downlink capability|2 GB / day12|
|Downlink data-rate|2 Mbps|
|Storage capability (on-board)|3.6 GB / day12|
|Uplink capability|1 batch of commands (600 kbit) / orbit12|
|Uplink data-rate|4 kbit/s|



_**Table 3-16: Data and communication with ground parameters.**_

#### **3.6 EMC interface**

##### **_3.6.1 Single point of grounding_**


Each P/L must provide a single point of grounding interface with respect to MPCB interface.


Each P/L MLI must be grounded with respect to P/L itself.


**3.6.1.1 Late-Access Payloads Grounding**


Late-Access P/Ls or LA elements must be grounded too, e.g., via bonding strap or blind mate


connectors.


12 For the whole Payload Aggregate.

Page 53/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **4 ENVIRONMENTS**


During the preparation and integration of the payloads for a launch, in flight, performing in orbit


operations and finally during the re-entry, descent and landing phases the spacecraft is


exposed to a variety of mechanical, thermal, electromagnetic, and atmospheric-related


environments. This chapter provides a description of the different environments that the


spacecraft, and its hosted payloads, are intended to withstand during its operational cycle.

#### **4.1 Mechanical Environment**


The mechanical environment is described in the present section, and it is exposed showing


different aspects of mechanical constraints and loads to withstand during integration, launch


and re-entry phases.

##### **_4.1.1 Transportation and Handling_**


During transportation to the Launch Site, post-flight transportation and during integration, the


P/Ls shall sustain any simultaneous combination of the Design Limit Loads:









|Load<br>Case|Operation|Load factors [g]|Col4|Col5|
|---|---|---|---|---|
|**Load**<br>**Case**|**Operation**|**X **|**Y **|**Z **|
|1|Hoisting|± 1.4|± 1.4|± 1.4|
|2|Handling|± 1.4|± 1.4|± 1.4|
|3|Transportation|± 3.0|± 3.0|± 3.0|


_**Table 4-1: Transportation and Handling loads.**_

##### **_4.1.2 Stiffness requirements_**


The MPCB hosted payloads shall maintain the first main mode above the specified level to


avoid interactions with SR and VEGA-C launcher structural dynamics:

|Frequency type|Frequency range [Hz]|
|---|---|
|First main mode|> 140|



_**Table 4-2 Primary lateral and longitudinal frequency limit.**_


Page 54/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


In case the above stiffness requirement cannot be met, the P/L Customer shall iterate with the


Aggregate Design Authority (ADA) to assess the compatibility with the SR.

##### **_4.1.3 Quasi-Static (QSL) and Low Frequency (LFL) Loads_**


Quasi-static and low-frequency loads are provided to define maximum mounting interface


loads that P/Ls could experience during the mission. The QSL is the acceleration applied at


the P/L CoG, representative of the force’s summation predicted at the Support Plate-P/L


interface. During any phase, including launch, the MPCB will not induce to the P/Ls loads from


any simultaneous combination, in excess of the following QSL Qualification Loads:


**QSL Qualification Loads [g]**







|Payload<br>Mass13|IP and OOP [g]|Notes|
|---|---|---|
|M ≥ 50 Kg|15|The loads in each direction shall be<br>combined and applied simultaneously|
|M < 50 Kg|22|22|


_**Table 4-3: QSL Qualification loads.**_


The QSL loads are intended as qualification loads (K q included) therefore K p and K m shall be


applied on top to derive the P/L Design Limit Loads according to RD5.

##### **_4.1.4 Sine Loads_**


The Sine loads defined in the table below shall be applied at P/L interface along the three axes:


**Sine Spectra – ALL PLATES** **[14]**







|Payload Mass < 50 Kg|Col2|Payload Mass ≥ 50 Kg|Col4|
|---|---|---|---|
|**Frequency [Hz]**|**IP and OOP [g]**|**Frequency [Hz]**|**IP and OOP [g]**|
|5 – 22|10 [mm]<br>(0 to peak)|5 – 19|10 [mm]<br>(0 to peak)|
|22 – 110|20|19 – 110|14|


_**Table 4-4 Sine loads.**_


13 The payload mass considered as reference is the nominal one (basic mass).
14 Spectrum to be applied at the equipment interface.

Page 55/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


The Sine loads are intended as limit loads (K q excluded) therefore K q, K p and K m shall be


applied on top to derive the P/L Design Limit Loads according to RD5.

##### **_4.1.5 Random Vibro-Acoustic Environment_**


The P/L shall be able to withstand the random acceleration levels due to acoustic vibrations,


Out of Plane and In Plane, in the PSD spectrum below:





























|Payload Mass < 50 Kg|Col2|Col3|Payload Mass ≥ 50 Kg|Col5|Col6|
|---|---|---|---|---|---|
|**OOP**|**OOP**|**OOP**|**OOP**|**OOP**|**OOP**|
|**Hz**|**Acceptance**<br>**PSD [g2/Hz]**|**Qualification**<br>**PSD [g2/Hz]**|**Hz**|**Acceptance**<br>**PSD [g2/Hz]**|**Qualification**<br>**PSD [g2/Hz]**|
|20|+ 3 dB/Oct|+ 3 dB/Oct|20|3 dB/Oct|3 dB/Oct|
|80|0.25|0.5|80|0.15|0.3|
|500|0.25|0.5|500|0.15|0.3|
|2000|-6 dB/Oct|-6 dB/Oct|2000|-6 dB/Oct|-6 dB/Oct|
|gRMS|14.4|20.4|gRMS|11.2|15.8|
|**IP**|**IP**|**IP**|**IP**|**IP**|**IP**|
|**Hz**|**Acceptance**<br>**PSD [g2/Hz]**|**Qualification**<br>**PSD [g2/Hz]**|**Hz**|**Acceptance**<br>**PSD [g2/Hz**|**Qualification**<br>**PSD [g2/Hz]**|
|20|4 dB/Oct|4 dB/Oct|20|4 dB/Oct|4 dB/Oct|
|80|0.05|0.1|80|0.05|0.1|
|1000|0.05|0.1|1000|0.05|0.1|
|2000|-3 dB/Oct|-3 dB/Oct|2000|-3 dB/Oct|-3 dB/Oct|
|gRMS|9.1|12.8|gRMS|9.1|12.8|


_**Table 4-5: Random vibroacoustic loads.**_


15 Spectrum to be applied at the equipment interface.

Page 56/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


The qualification of the Payload could be also performed using the vibroacoustic environment


(provided by Space Rider) upon specific request. Random vibration environments from


transportation and ground processing are enveloped by the above-specified levels.


The qualification and acceptance random spectra include K q and K a respectively, K p and K m


shall be applied on top to derive the P/L Design Limit Loads according to [RD5].

##### **_4.1.6 Shock Environment_**


This section describes the envelope for the maximum shock levels at the MPCB interface for


the hosted payloads (hard-mounted, all-locations). Payloads should maintain structural


integrity (no fractures, disassembly, or low-releasable mass) when submitted to the shock


environment represented below:

|Frequency [Hz]|SRS Shock Response Spectrum [g]|
|---|---|
|100<br>|40|
|300<br>|300|
|1000|1000|
|10000|1000|
|||



_**Table 4-6: SRS Shock response spectrum.**_


_**Figure 4-1 Shock level envelope**_


Page 57/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_4.1.7 Pressure Environment_**


During the mission the SR MPCB is subject to the depressurization during the ascent phase


and the re-pressurization during the descent phase. The SR MPCB hosted P/Ls shall withstand


the maximum pressure change rates described in the following sub-sections. The P/L design


shall assure that any venting for the depressurization and re-pressurization can take place


unimpededly and in accordance with the profiles of the MPCB described below.


**De-pressurization profile (Launch and Ascent Phase)**


During the launch and ascent phase, the SR MPCB environment depressurization rate will be:

|Mission Phase|Depressurization rate|
|---|---|
|Launch and Ascent|<= 2200 Pa/sec|



_**Table 4-7 Launch and Ascent depressurization rate.**_


**Re-pressurization profile (Re-entry and Descent Phase)**


During re-entry and descent phases until landing, the P/L shall sustain the following


pressurization profile:


_**Figure 4-2 Re-pressurization profile.**_


Page 58/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_4.1.8 Microgravity_**


The microgravity environment, at the P/L interface, during the orbital phase, in any possible


attitude configuration and operation (e.g., tail-to-sun) shall respect the following envelope:


  for frequencies (f) 0.01≤ f ≤ 0.1 Hz, the Root Mean Square amplitude of the residual


disturbances will be less than 2 x 10 [-6] g;


  -  for 0.1< f ≤ 100 Hz, the disturbances will be less than the product of [2 x 10 [-5] (g)


frequency (Hz)];


  for 100 < f ≤ 300 Hz, the amplitude of the disturbances will not exceed 2 x 10 [-3] g;


  for frequencies (f) above 300 Hz, disturbances with amplitude exceeding 2 x 10 [-3] g will


be indicated on a time scale, in function of their occurrence during a typical reference


mission of the Space Rider. In this case, the mechanical subsystem is normally isolated.


_**Figure 4-3 Micro-gravity environment at MPCB level.**_


Page 59/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


The above microgravity environment will be guaranteed to P/Ls during orbital phase activities


for a specific amount of time according to P/Ls Aggregate design and system constraints.

##### **_4.1.9 Re-entry, Descent and Landing loads_**


During the landing phase (ground impact), the P/L shall withstand the following maximum static


acceleration (design limit level) at the RM CoG:







|Location|Acceleration [g]<br>ALL AXES|
|---|---|
|RM CoG16|± 8.317|


_**Table 4-8: Landing loads.**_


16 P/L adjusted or updated values will be determined after accommodation study. Iteration with the ADA to
reduce impacts can be evaluated.
17 The specified value can be updated but will remain enveloped by the expected loads at launch phase.

Page 60/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **4.2 Thermal Environment**

##### **_4.2.1 Integration, Transportation and Ground Launch Facility Operations_**


P/Ls that will be integrated in the RM MPCB during AIT activities in Europe will be delivered by


the Customers and integrated under the following thermal environmental conditions:

|Parameter|Value|
|---|---|
|Temperature|22 ± 3 °C|
|Relative Humidity|45 – 65 %|



_**Table 4-9: Thermal environmental conditions at AIT site(s) in Europe**_


After the AIT activities in Europe, the P/Ls will be transported inside the RM placed in its


transport and storage container for road / sea and / or air transportation phases from the


integration to launch facilities and encapsulation of the SR stack up, through the SR stack


mating to the launch vehicle and the stand-by period until launch maintained at the following


thermal environmental conditions (see [RD1] and [RD2] for further details):


















|RM<br>Location /<br>Parameter|Transfer<br>between<br>Assembly /<br>Integration<br>Buildings|On Assembly / Integration<br>Buildings|Col4|Transfer to<br>Launch Site|On Launch<br>Pad|
|---|---|---|---|---|---|
|Status|Transport<br>Container|Not<br>Encapsulated|Encapsulated<br>(fairing)|Encapsulated<br>(fairing)|Encapsulated<br>(fairing)|
|Temperature|[-10÷ 50]<br>± 1 °C|22 ± 3°C|Air inlet<br>[11÷ 25]<br>± 1°C|≥ 15 °C|Air inlet<br>[11÷ 25]<br>± 1°C|
|Relative<br>Humidity|20 – 60 %18|55 % ± 10%|55 % ± 5%|≤ 20%|≤ 20%|



_**Table 4-10: Thermal environmental conditions during transportation and integration at Launch Site.**_


18 With no condensation.

Page 61/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_4.2.2 Launch, Ascent and Orbital phases_**


During the launch and ascent phases the thermal environment is affected by limited dissipation


(the MPCB door is closed, and the radiator is not operational, see Table 3-4). After


commissioning (i.e., when the MPCB door is open, and the radiator is operational) the P/Ls


shall be able to withstand the following environment:







|Parameter|Value|
|---|---|
|External sink temperature|4 K (worst cold case assessment)|
|MPCB enclosure emissivity|0.8|
|Solar Electromagnetic Radiation /<br>Solar Particle Radiation19|at 1 AU: 1366.1 W/m2 <br>at aphelion: 1321.6 W/m2 <br>at perihelion: 1412.9 W/m2|
|Integrated spectral irradiance20|1366.1 W/m2|


_**Table 4-11: Thermal environment ascent parameters.**_

##### **_4.2.3 Re-entry, Descent and Landing phases_**


From the moment the MPCB main door closes, and the radiator stop working, the thermal


environment is affected by limited dissipation (see Table 3-4). In addition, we have:






|Parameter|Value|
|---|---|
|P/Ls cool-down phase before de-orbit<br>temperature at the I/F|Down to 5°C|
|MPCB temperature at Support Plate<br>interface with the P/Ls|≤ 40 °C|



_**Table 4-12: Thermal environment re-entry parameters.**_


19 Electromagnetic radiation from the Sun that falls on a unit area of surface normal to the line from the Sun, per
unit time, outside the atmosphere at specified distance.
20 The integrated spectral irradiance has been made to conform to the value of the solar constant accepted by
the space community.

Page 62/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **4.3 Electromagnetic Environment**


The electromagnetic (EMC) environment is described in the present section, and it is exposed


showing different aspects of EMC compatibility constraints.

##### **_4.3.1 RF Compatibility levels_**


A P/L shall emit, to the antenna terminal, a RF power level lower than 60 dB W with respect to


the power level at the fundamental frequency, in the following frequency bands:


  - S-band: 2025-2100 MHz


  - C-band: 4200-4400 MHz


  - C-band: 5400-5900 MHz


This requirement is applicable only for P/Ls with RF transmission equipment. The MIL-STD

461E and CE106 test setup shall be used as guideline for EMC test.

##### **_4.3.2 Aggregate Radiated Susceptibility_**


The P/L Aggregate shall not transmit to the RM, an electromagnetic radiated emission above


the following mask:


_**Figure 4-4 Aggregate Radiated Susceptibility.**_

Page 63/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public





|Frequency<br>Range|Level<br>[dBμV/m]|
|---|---|
|14 [kHz] – 30 [MHz]|132|
|30MHz – 40 [GHz]|126|
|2200 – 2290 [MHz]|150|
|4200 – 4400 [MHz]|140|
|5400 – 5900 [MHz]|150|


_**Table 4-13: Aggregate Radiated Susceptibility levels.**_

##### **_4.3.3 Aggregate Radiated Emission_**


The P/L Aggregate shall be compatible with the following mask:


_**Figure 4-5 Aggregate Radiated Emission.**_









|Frequency<br>Range [MHz]|Level<br>[dBμV/m]|Notes|
|---|---|---|
|417-422|40|Only if the unit is operative during the launcher<br>phase (SE=20dB – Closed door)|


Page 64/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

|420-480|50|Only if the unit is operative during the launcher<br>phase (SE=20dB)|
|---|---|---|
|1164-1300|55|Only if the unit is operative during the launcher<br>phase (SE=20dB)|
|1555-1595|35|GPS|
|2025-2110|20|S Band|
|4200-4400|35|Only if the unit is operative during the re-entry<br>phase|
|5400-5900|65|Only if the unit is operative during the launcher<br>and/or re-entry phases|



_**Table 4-14: Aggregate Radiated Susceptibility.**_


In case of P/L needs not matching with the above shown notching scheme, further iterations


to accommodate EMC compatibility will be possible.


Page 65/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **4.4 Space Environment**


During in-space operations, the RM MPCB hosted payloads will be exposed to different factors,


the main ones are listed below:


  - External Vacuum


  Atomic Oxygen


  - Cosmic Radiation


  Solar Light

##### **_4.4.1 External Vacuum_**


The space vacuum pressure in orbit is a function of the orbit and the quote. At the altitude for


SR reference missions, the pressure of the space environment will be near perfect vacuum:

|Mission Phase|Vacuum pressure range|
|---|---|
|In-Orbit|< 1 x 10-7 Pa|



_**Table 4-15 Vacuum pressure range.**_

##### **_4.4.2 Atomic Oxygen_**


The P/L shall be designed to withstand a fluency of AO/cm [2 ] without degrading their


performances as reported below.

|Mission Phase|ATOX fluency range|
|---|---|
|In-Orbit21|1.6 x 1021Atoms of Oxygen (AO)/cm2|



_**Table 4-16: ATOX fluency range.**_

##### **_4.4.3 Cosmic Radiation_**


Maximum external radiation levels on payloads mounted in the opening of the MPCB doors


depend strongly on the SR attitude and orbital characteristics. A typical radiation levels during


orbital phase at reference altitude can reach up to:


21 Worst case scenario in equatorial orbit for 60 days (exposed P/L).

Page 66/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public









|Radiation<br>type|Level|Note|
|---|---|---|
|Solar Flare(s)|Up to 50 rad<br>(0.5 Gy)|Possible during the whole mission|
|Trapped<br>Particles<br>Exposure|10 rad/day|in case of 400 km polar orbit and considering<br>1 mm of Al shielding|

##### **_4.4.4 Solar Light_**



_**Table 4-17: Typical radiation levels.**_



Irradiation of solar light on payloads mounted in the opening of the MPCB doors depends on


the spacecraft attitude and orbital characteristics.


Users shall specify their experiments needs in terms of solar constant hours (SCh) per day.

#### **4.5 Cleanliness and Contamination Control**

##### **_4.5.1 Cleanliness_**


Payload integration activities will be performed in Europe integration site as baseline in


dedicated ISO 8 clean rooms providing air cleanliness via constant positive pressure, careful


material selection, all personnel wearing PPE and air filtration and dilution.


**Cleanliness at Integration**


The MPCB will ensure towards the P/L the following cleanliness levels, during the integration


phase:


  ISO 8 class contained atmosphere facilities;


  At integration: PAC [ppm] and MOC [g/cm [2] ] values are currently under evaluation and


will be provided at later stage.


**Cleanliness for In-Orbit**


The MPCB will ensure as a baseline towards the P/L the following cleanliness levels during in

orbit:


Page 67/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


  PAC [ppm] and MOC [g/cm [2] ] values are currently under evaluation and will be provided


at later stage.


**Cleanliness at Post-landing**


Landing site design finalisation is ongoing, cleanliness levels at post–landing phase will be


provided at later stage.

##### **_4.5.2 Contamination analysis_**


It is recommended to perform a contamination sensitivity analysis at payload level in order to


determine areas sensitive or not to contamination. Depending on the results of the analysis, it


is recommended to introduce mitigations measures to avoid contamination to sensitive areas.


ESA is available and can be contacted for any advice on this topic.


Page 68/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **5 PAYLOAD DESIGN, DEVELOPMENT AND VERIFICATION**


The P/L design, development and verification process will be performed and managed by the


Customers. The P/L should provide relevant documentation to demonstrate compliance to SRS


I/F constraints and safety requirements.

#### **5.1 P/L Interface design aspects**


During the P/L design process a comprehensive list of aspects must be taken into consideration


at different level of detail (depending on the phase of the development). In general, preliminary


aspects includes (non-exhaustive list):


  Definition of P/L category (see 5.1.1 for further details), overall dimensions and mass.


  Main elements of the P/L (e.g., Single experiment or Laboratory + Experiments, in the


latter case list by broad lines the mission and purpose of all carried experiments).


  Description of P/L thermal control, power and data architecture and budgets.


  Description of any vibration-related (e.g., pumps, etc.) or EMC disturbance (e.g.,


antenna, electromagnetic actuators, etc.) sources.


  Identification and assessment of safety aspects.


  Operational and ground-segment related operations.


The P/L shall also present a development plan, a description of the P/L mission phases from


integration on the vehicle until retrieval after landing (including required P/L technical and


schedule conditions and constraints) and a chronology of P/L activities in-orbit, providing (non

exhaustive list):


  Foreseen operational modes and resources consumption.


  Description of activities performed and duration.


  Description of needed services and environmental constraints.


  Identification of degraded cases.


Page 69/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_5.1.1 Payload Categories_**


The payload design activity should also take into consideration to identify a payload category


in terms of two different point of views, payload needs and payload mobility.


Talking about payload needs, we can have:


  **Standard Payloads (STD)** : payloads that do not require late access/early recovery


nor field of view or need for direct space exposure.


  **Late-Access (LA) / Early-Retrieval (ER) Payloads** : payloads that require to be


installed just prior to launch and/or to be recovered just after landing.


  **Field-of-View (FoV) / Direct Exposure Required (DER) Payloads** : payloads that


require to be directly exposed to the space environment and/or to perform observation


pointing out of MPCB.


In terms of payload mobility instead, an additional classification can be made:


  **Fixed Payload (F-PL)** : any Payload which does not separate from Space Rider MPCB


and remain fixed in its MPCB compartment.


  **Deployable Payload (D-PL)** : any Payload, which can separate from Space Rider


MPCB into its own free-flying mission, divided in three sub-classes:


`o` Payload deployable with no manoeuvre capability ( **D-PL (NM)** )


`o` Payload deployable with manoeuvre capability ( **D-PL (M)** )


`o` Payload deployable with operations within the Space Rider Keep Out Zone


(retrieval/re-visitation) ( **D-PL (KZ)** )


  **Movable Payload (M-PL)** : any Payload which does not separate from Space Rider


MPCB but perform movement inside it (i.e., robotic arm).


Page 70/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **5.2 Safety requirements**


Regarding the applicable safety requirements to P/L design, development and verification


process please consider that proper applicable documentation will be provided (after formal


contact). This documentation includes the technical and system safety, space debris and


collision avoidance requirements applicable to SRS payloads (including payload-provided


ground and flight support systems) to be followed by the Customers and Experiment Owners


(see [RD3]). These requirements are applicable to the ground and flight operations, from the


launch preparation activities of the flight vehicle to the recovery activities of the payloads after


landing. The Customer shall interface with the Experiment Owners to assess the


implementation of the safety requirements at payload level. The process to reach the Safety


Acceptance of the MPCB payloads and experiments is described in [RD4]. During the P/L


design, development and verification process Customers should take into account the following


aspects related to safety (non-exhaustive list):


  **Severity classes** : the consequences of failure of one of the elements of the P/L are


prioritized in severity classes (definitions are reported in [RD4]).


  **Hazard prevention, control, and minimization** : the risks and related consequences


must be clearly identified and included in the P/L safety documentation. Where


applicable an adequate number of safety barriers shall be provided. During ground


operations the P/L functions which may lead to specific consequences should ensure a


safety interception capability, by providing the status and the ability to command or


inhibit at least one of the barriers. In addition, differently from a standard mission, the


Space Rider System will include operation at landing site after the orbital mission and


related safety aspects.


  - **Materials:** safety requirements and aspects related to the presence of hazardous and


forbidden materials (chemical releases, flammable materials, organic and contagious


products, genetically modified organisms, etc.)


  **Fluid systems** : safety requirements and aspects related to the presence of this kind of


systems (leakage, pressure, etc.)


Page 71/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


  **Combustion, high-temperature, and heat-exchanger systems** : safety requirements


and aspects related to the presence of this kind of systems (skin-contact safety


threshold, potentially noxious exhausts, gaseous pressure, etc.).


  **Batteries, static electricity, and electrical systems** : safety requirements and aspects


related to the presence of this kind of systems (isolation, grounding, leakage, fire, etc.).


  **Radiation systems (non-ionising, ionising, optical instruments, and LASERs,**


**etc.)** : safety requirements and aspects related to the presence of this kind of systems


(protections, Threshold Limit Values, Biological Exposure Indices, etc.).


  **Pyrotechnic systems** : safety requirements and aspects related to the presence of this


kind of systems (failure propagation, generation of space debris, etc.).


  **Space-debris mitigation and collision avoidance** : safety requirements and aspects


related to the possibility to generate space-debris or in-flight collisions.


Page 72/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **5.3 Product Assurance Requirements**


ESA recommends to follow the ECSS standards (at latest issues) with availability to support


Customer to address the applicable and required standards.

#### **5.4 Cleanliness and Contamination Requirements**


The P/L FM item, in addition to selected test models must comply with SR cleanliness and


contamination requirements (see section 4.5). If the P/L presents any deviations to the above


ESA shall be informed.


As part of hand-over / incoming inspection activities, cleanliness measurements will be made


to assess the cleanliness levels of the P/L.

#### **5.5 Design Reviews and Follow-Up**


In order to monitor the P/L design, development and verification process and the expected


output through time, the MPCB Operator (as Payload Aggregate responsible) will request the


Customer to certify, at certain point during flight preparation (see ANNEX B), the P/L design


maturity level according to the following criteria:


  Payload performances: for information.


  Payload external interfaces: for approval.


Using the recommended definitions and the typical ECSS project life cycle described in [RD8]


the expected reviews (or equivalent level maturity key point, see [RD7]) t reach the above


criteria are:


  Preliminary Design Review (PDR)


  Critical Design Review (CDR)


  Qualification Review (QR) / Acceptance Review (AR)


  Pre-Shipment Review (PSR).


Relevant milestones must be achieved and certified (Certificate of Compliance) by the


provision of proper documentation to MPCB Operator or equivalent evidence of comparable


Page 73/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


technical achievements in support to the required certification shall be produced by the


Customer.


The MPCB Operator is available to participate as observer during Customer identified P/L main


reviews with the aim to support the Customer and verify the P/L interface requirements


compliance with respect to MPCB interface point of view.


In case a Customer express the need, a P/L design and development process follow-up can


be provided by ESA on-demand. The purpose of this follow-up activity is to be intent not for


qualification purposes but as knowledge support for the maturity reaching point.


Page 74/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **5.6 Payload Deliverables**


Customer are required to provide a set of deliverables during the preparation to flight in


accordance with the approach described in section 5.5. It will be considered as deliverable the


P/L technical documentation with impacts on SR MPCB interfaces, contractual, and safety

related documentation plus possible required P/L test models (see section 5.6.4).

##### **_5.6.1 Payload Design and Development Technical Documents_**


In this section an overview of the principal P/L design and development technical


documentation with impacts on SR MPCB interfaces will be presented. The customer shall


collect all the needed technical information for the P/L acceptance process, e.g. (non

exhaustive list).:


  P/L Interface Requirements Document (P/L IRD)


  P/L Ground and Flight Operations Plan


  - P/L User Manual


  Qualification / Acceptance Test Report


  Certificate of Conformity (CoC)


The full list of expected deliverable technical documentation will be formally listed in the


Statement of Work (section 5.6.2) in accordance with the approach described in section 5.5.

##### **_5.6.2 Payload Contractual Documents_**


An overview of the contractual documentation that will be required to be formally stated


between the P/L Customer and the MPCB Operator to ensure a proper legal framework


between the two entities.


**Memorandum of Understandings (MoU)**


The document where it is formally stated between the P/L Customer and the MPCB Operator


the commitment to continue the work and mutually commit for Customer P/L flight with one of


the SRS planned flights.


Page 75/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Flight Service Agreement (FSA)**


The document where it is formally stated between the P/L Customer and the MPCB Operator


the commitment to continue the work and mutually commit for Customer P/L on a specific and


identified SRS flight (in particular on the Maiden Flight). Applicable to the FSA are the following


programmatical and technical documents:


_Statement of Work (SoW)_


The document where it is formally stated between the P/L Customer and the MPCB Operator


commitment to the list of activities both P/L Customer and MPCB Operator side to be performed


to accept P/L aboard SR according to the required technical documentation issued during


Payload Aggregate preparation process.


_Interface Control Document (ICD)_


The document deals with the technical definition and control of the applicable interfaces


between the SRS and each P/L Customer part of the MPCB Payloads Aggregate for a specific


flight. The scope of this document is to assure and maintain compatibility and coherence of


interfaces development and implementation within the SRS mission and each embarked


Payload. The ICD will be kept up to date according to configuration evolution as defined in the


Payload Aggregate preparation process.

##### **_5.6.3 Safety Documents_**


The documentation expected along the P/L Safety Acceptance Process is reported in [RD4].


The Customer shall provide to the MPCB Operator a preliminary safety analysis for the P/L to


identify the potential risks with consequences on the safety of people, goods and the


environment that could be generated by the P/Ls, and their mitigation measures.


Page 76/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_5.6.4 Payload Models_**


As a verification method for P/Ls, an optimized number of representative P/L model’s (both


analysis and physical models) are identified to achieve a high confidence level in the P/L


verification with the shortest schedule and a suitable weigh of costs and risks. The P/Ls model’s


delivery (see ANNEX B) is planned to decouple the availability vs possible launch date


evolutions and the verification sequence is also structured to synchronize with the SRS


qualification program.


Note that if the Customer is able to provide the P/L FM at expected aggregate integration tests


(see section 6.4) requirement to provide specific P/L representative models can be amended.


**Payloads Analytical Models** **[22]**


Preliminary accommodation and mission feasibility studies relies on P/L analytical models that


will represent in a numerical domain some of the main characteristics of the P/Ls.


Note that the thermo-mechanical verification of the aggregate is performed via coupled load


analyses, so stringent requirements to P/L mathematical models’ correlation and accuracy are


enforced to P/L to ensure quality of analysis results. The development of P/L FEM and TMM


models must follow correlation criteria that will be provided as applicable technical notes.


_Computer-Aided Design Models (CAD)_


A digital 3D model representing the P/L. Information to be reported are sizes, shape, interface’s


location, and mass to perform a digital fit-check and accommodation analysis.


_Finite Element Model (FEM)_


A digital approximation of the P/L structure into simpler pieces whose behaviour can be


described by equations. Used to perform structural analysis, mass properties, and preliminary


and final mission analysis.


22 Additional analytical models (e.g., dynamic envelopes, …) can be required for specific P/L types (e.g., robotic
arms).

Page 77/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


_Thermal-Mathematical Model (TMM)_


A digital numerical model of the P/L represented by concentrated thermal capacitance nodes


or elements, coupled by a network made of thermal nodes. Used to perform a thermal analysis


to size the design and to support the thermal testing verification.


**Payloads Physical Models**


_High Fidelity 3D Mock-Up (3D Mock-Up)_


A 3D model representative of P/L shape to realize the necessary fit checks during verification


phase. The model must be an accurate and precise dimensional reproduction of the P/L


external shape, representative of mechanical I/F, provide location of the grounding, electrical,


data and any other applicable I/F (e.g., fixation points to interface with MPCB thermal blanket).


Late-Access P/Ls model shall also allow preliminary check for the late installation operations


therefore any doors or drawers to be opened must be implemented. No constraints are


applicable to model material, fit checks and integration tests will be done inside the RM FM


Multi-Purpose Cargo Bay, so it is required the compliance of the P/Ls model with the cleaning


requirements.


_Electrical and Functional Model (EFM)_


A model representative of the P/L data and power connector pin function, as well as


representative of the real unit from a functional behaviour and data interface point of view to


realize the preliminary electrical and functional tests. The model must be representative of P/L


electrical and data interfaces and P/L representative software. A lower standard for electrical


components, materials and processes may be used as long as they provide representative


performances but in compliance with the cleaning requirements.


_Representative Dummy (Dummy)_


A model mechanically representative of the characteristics of the P/L in order to be able to


implements the fit checks necessary in verification phase. It shall be accurate and precise in


Page 78/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


mass and dimensional representativity of external shape of the FM item with similar superficial


treatment. The model must be representative of mass, CoG, momentums of inertia, mechanical


I/Fs necessary for integration of the payload any other applicable I/F (e.g., fixation points to


interface with MPCB thermal blanket). In case of non-availability of the P/L Flight Model at


required time, the dummy model will be used as back-up and then would fly. Thus, the FM


requirements are made applicable to it, therefore it shall comply with product assurance and


all cleanliness and contamination requirements. A single instance will be required contractually


to mitigate the risk of P/L FM unavailability at the required delivery date for final integration.


_Flight Model (FM)_


The qualified and flyable model of the P/L needed for final launch campaign integration and


checks.

#### **5.7 Export Control**


Payload Customers will be requested to provide the classification of Payload and its


components in terms of export control regulations.


Page 79/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **6 AGGREGATE VERIFICATION AND INTEGRATION**

#### **6.1 The Payload Aggregate**


The selected P/Ls to be hosted in the MPCB for a specific SR mission are identified as the


Payload Aggregate (PLAG). This configuration is composed by a group of Customer’s


developed and qualified P/Ls to be accommodated in the MPCB in a specific configuration


defined by the Aggregate Design Authority (ADA). The aggregate, managed by the MPCB


Operator, will be considered as a product, and will pass through a preparation, verification, and


integration process to be qualified for the flight.

#### **6.2 Aggregate Preparation Process**


The aggregate preparation is an end-to-end process that will identify and prepare the best


configuration of payloads to be flown for a specific SR mission:


_**Figure 6-1 Payloads Aggregate Preparation Process.**_


  - **Phase I** : ESA Preliminary Aggregate Study, early Customer contacts, preliminary


compatibility evaluation of P/L with SRS.


  - **Phase IIa** : Preliminary Aggregate Definition by Aggregate Design Authority (ADA).


`o` **MOU** **signature** : Formal Customer/MPCB Operator commitment to fly on one of


six SRS flight.


Page 80/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


  - **Phase IIb** : Aggregate Definition Confirmation, aggregate design coherent with


Preliminary Mission Analysis (PMA)


`o` **FSA** **signature** : Formal Customer/MPCB Operator commitment to fly on one


identified SRS flight.


  - **Phase III** : Final Aggregate Design, detailed aggregate design coherent with Final


Mission Analysis (FMA)


  - **Phase IV** : Final Aggregate AIT


  - **Phase V** : Aggregate Flight Operations


  - **Phase VI** : Aggregate Post-flight Operations

##### **_6.2.1 Phase I: Payloads Feasibility Phase_**


At this phase the Space Rider System Operator collect requests from Customers, via open


calls for flight opportunities or direct reception of P/L proposals and evaluate a preliminary


compatibility of P/L with SRS. The Customer, with MPCB Operator technical support, will define


P/L requirements, check preliminary P/L accommodation, build interface and preliminary


contractual documentation. A feasibility study will bring the potential P/Ls to Phase II.

##### **_6.2.2 Phase IIa: Preliminary Aggregate Definition_**


All the P/Ls that are part of the feasibility study are required to provide their preliminary data


regarding requirements and interfaces and safety aspects. A preliminary P/L accommodation


study is then performed by the Aggregate Design Authority (ADA).


At the end, with the results of the feasibility and accommodation studies a Preliminary


Aggregate Definition is generated, and all the P/Ls selected will be invited to sign a


Memorandum of Understanding (see 5.6.2).


Page 81/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_6.2.3 Phase IIb: Aggregate Definition Confirmation_**


At this phase all the P/Ls that are part of the preliminary aggregate design are required to


provide their updated preliminary data regarding requirements and interfaces, safety aspects


and software models. After that Customers are required to demonstrate the P/L maturity at


PDR-level (see 5.5) with the MPCB Operator to verify the preliminary architectural design and


mission concept of operations. In the meantime, the Aggregate Design Authority (ADA) will use


the P/Ls provided data to start a Preliminary Mission Analysis (PMA).


At the end, with the results of the PMA and the P/Ls PDRs there will be the P/Ls selection for


a specific mission and signature of relative Flight Service Agreement (see 5.6.2).

##### **_6.2.4 Phase III: Final Aggregate Design_**


At this phase all the P/Ls that are part of the final aggregate design are required to provide


their consolidated data regarding requirements and interfaces, safety aspects and analytical


models. After that Customers are required to demonstrate the P/L maturity at CDR-level (see


5.5) with the MPCB Operator to verify the final architectural design and mission concept of


operations. The Aggregate Design Authority (ADA) will then use the P/Ls provided data to start


the Final Mission Analysis (FMA) while the Customers are required to provide P/L’s 3D High


Fidelity Mock-Ups for fit checks on FM MPCB and Electrical and Functional Models for tests


with the RM ATB. At the end of this process, P/Ls are required to sustain or provide certification


of compliance for the Qualification Review (QR) and an update of safety information.


At the end, with the results of the FMA and the P/Ls CDRs and QRs there will be the P/Ls


confirmation for the specific SR mission.

##### **_6.2.5 Phase IV: Final Aggregate AIT_**


All the P/Ls selected for the flight must provide a P/L Flight Model or at least a Representative


Dummy at final P/L integration into RM MPCB at integration site in Europe. Then the RM will


be moved to the launch site, at Europe’s Spaceport in Kourou, French Guiana.


After final checks the MPCB door of the SR RM will be closed in preparation for the integration


with the AOM module. The SRS is now ready for the Flight Readiness Review (FRR). After this

Page 82/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


milestone, the SR Vehicle (RM and AOM) and the fairing are being integrated with the VEGA

C launch vehicle. At this point, at the ELV, the late access window for P/Ls integration starts.


The two LA compartments are accessed contemporary by two operators, installing the


environment sensible P/Ls into their housings. When the late-access procedure is finished, the


system can face the last milestone before the lift-off, the Launch Readiness Review (LRR).

##### **_6.2.6 Phase V: Aggregate Flight Operations_**


This phase nominally begins at launch time, and after the ascent phase and LEOP activities


enter the commissioning phase with the initial RM mission attitude and MPCB door aperture.


At this point in time begins the P/Ls experiments window with the execution of mission timeline


during each 90 minutes orbit at different attitudes. The experiments will undergo for plus than


60 days exchanging of TM&TC from/to VCC and PGCC. After two-months in space the


experiments window ends and one day is required to let the avionic and P/Ls cool-down in


preparation for the re-entry. The MPCB door will be closed and after the reception of the


authorization from Landing Site the SR vehicle will perform a de-orbit burn and the separation


of RM (for re-entry) and AOM (for destructive re-entry). The RM will perform the re-entry and


descent phase with its sub-sonic parachute followed by the deployment of a guided parafoil to


steer the RM vehicle up to its touchdown at Landing Site.

##### **_6.2.7 Phase VI: Aggregate Post-flight Operations_**


At the landing site the SR RM will be cooled-down and powered-down to allow operators


access LA compartments to retrieve the environmental sensitive P/Ls. Standard P/Ls are


recovered once the RM is moved to the post-landing facility, where the hand-over of P/Ls from


MPCB Operator to owners can be performed while the RM is moved to refurbishment phase.


Page 83/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **6.3 Aggregate Verification**


The aggregate verification process will verify the compliance to the requirements for a specific


SR mission and its acceptance. If the results of the verification process are satisfactory, the


Payloads Aggregate is ready to perform the mission onboard Space Rider.

#### **6.4 Aggregate Compatibility Analysis and Tests**


The following analyses and compatibility tests will be performed for the qualification and


acceptance of the overall aggregate (see ANNEX B for further details):

##### **_6.4.1 System-Level Mission Analyses_**


**Preliminary Mission Analysis**


All the Aggregate Payload’s must provide (at PDR level) preliminary data for mechanical


aspects, power consumption, thermal dissipation, EMC compatibility, operational aspects, and


relative analytical models (see 5.6.4). The ADA will use all the provided inputs to define the


PMA to establish the correlation between P/Ls and their mission requirements.


**Final Mission Analysis**


All the Aggregate Payload’s must provide (at CDR level) consolidated data for mechanical


aspects, power consumption, thermal dissipation, EMC compatibility, operational aspects, and


relative analytical models (see 5.6.4). The ADA will use all the provided inputs to define the


final mission analysis to establish the correlation between P/Ls and their mission requirements.

##### **_6.4.2 System-Level Fit Checks_**


All the Aggregate Payload’s must provide (at CDR level) a proper high-fidelity 3D mock-up to


perform P/L accommodation fit checks on the RM FM.

##### **_6.4.3 Preliminary Integration, Electrical and Functional Tests_**


Page 84/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


All the Aggregate Payload’s must provide a proper Electrical and Functional Model (see 5.6.4)


to perform preliminary integration, electrical and functional tests on the RM ATB.

##### **_6.4.4 Final Integration, Electrical and Functional Tests, Mass Properties_**


All the Aggregate Payload’s must provide a proper FM or representative dummy (see 5.6.4) to


perform final integration, electrical and functional tests on the RM FM.

##### **_6.4.5 Mechanical, Thermal and EMC Analyses for Aggregate Acceptance_**


All the Aggregate Payload’s information provided at integration will be used by the ADA as


inputs to define the final mechanical, thermal and EMC analyses for the aggregate acceptance


review.

#### **6.5 Aggregate Assembly, Integration and Test**


The SR baseline locations for the Payload Aggregate – Assembly, Integration and Test (AIT)


activities are:


  Standard Payload AIT Site(s):


`o` ESA ESTEC in Noordwijk, The Netherlands (only MF).


`o` TAS-I Premises in Turin, Italy (sub-sequent flights).


  Late-Access / Early Retrieval Payloads AIT Site:


`o` Centre Spatiale Guyanese in Kourou, French Guyana.


The Standard Payloads AIT operation with RM FM will be performed at AIT site(s) in Europe


and back-up activities are based on P/L Representative Dummy. On the contrary operations


on Late Access (LA) P/Ls or cartridges will be carried out at launch site where suitable


equipment and facilities will be put in place to support the relevant tasks.


Every SR mission can be slightly different in terms of P/L logistic accommodation.


Page 85/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **6.6 Aggregate Safety Acceptance Process**


Customers are required to provide P/Ls safety-related information as described in section 5.2


and 5.6.3. The MPCB operator, as Aggregate Responsible will collect the information from all


aggregate P/Ls and will be subjected to a Payload Aggregate Safety Acceptance Process


(managed by the designated Safety Authorities), which includes safety submissions and


associated milestones, that are reported and described in detail in [RD4]. This process outputs


in terms of safety feedback or required actions related to P/Ls safety aspects will be managed


and forwarded to Customer by the MPCB Operator.


Page 86/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **7 SPACE RIDER SERVICES FOR PAYLOADS**


Payload services section reports the list of all the capabilities that the SR RM can provide as a


service to the hosted payloads. Services can be provided as:


  **built-in capability** of SR system via MPCB interfaces.


  **missioning hardware** : a customized set of hardware provided to meet aggregate-level


requirements (e.g., power and data cables, …)


  - **extension-kit** : dedicated hardware to be hosted inside the MPCB, to provide a specific


required capability.

#### **7.1 Mechanical services**


SR Vehicle baseline mechanical services for P/Ls are provided as a built-in capability through


its mechanical interfaces (MPCB Support Plates). Technical information about baseline


mechanical aspects and limitations can be found in section 3.2.1.


Additional mechanical services not envisioned for baseline (e.g., special mechanical adapters,


special fasteners, locking mechanisms, etc.) can be evaluated and eventually provided via the


implementation of dedicated extension-kit(s) upon Customer request.

##### **_7.1.1 Standard Mounting – Accommodation Service_**


This service is provided by the ADA in order to identify the optimal allocation of the P/L [23] inside


the MPCB (in terms of Support Plate allocation, orientation, interference with other P/Ls, …)


taking into consideration its characteristics and requirements that will not require the use of


additional and dedicated HW (i.e. P/L directly mounted on the Support Plate without the need


of brackets, spacers, …).


23 The P/L must be compliant to the MPCB mechanical interface as specified in 3.2.1.

Page 87/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_7.1.2 Non-Standard Mounting – Missioning Hardware Service_**


This service is provided by the ADA in order to identify the optimal allocation of the P/L inside


the MPCB (in terms of Support Plate allocation, orientation, interference with other P/Ls, …)


taking into consideration its characteristics and requirements that will require the use of


additional and dedicated HW.


The requirement for additional and dedicated HW for P/L mounting can be made necessary in


case the P/L requires further structural support (for example to achieve visibility requirements),


complex instrument shapes or to satisfy other P/L specific needs.


An example of this kind of service is the supplementary (optional) Support Plate that can be


placed to the structural-Y part of the MPCB (see Figure 7-1) in order to accommodate P/Ls


that require FoV and/or outer space environment exposition and have no or limited thermal


requirements.


_**Figure 7-1 Structural-Y optional Support Plate**_


Page 88/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **7.2 Thermal services**


SR Vehicle baseline thermal service for P/Ls is provided as a built-in capability through its


Thermal Control System (TCS) based on the conductive path to the network of heat pipes


provided by the MPCB Support Plates. Technical information about baseline thermal


dissipation capability and limitations can be found in section 3.3.1.


Additional thermal services not envisioned for baseline (e.g., high thermal dissipation capability


for P/Ls which dissipation through passive thermal control is not feasible or not sufficient) can


be evaluated and eventually provided via the implementation of dedicated extension-kit(s)


upon Customer request.

#### **7.3 Power services**


SR Vehicle baseline power service is provided as a built-in capability through its Power


Distribution Unit (PDU) based on several P/Ls dedicated power lines present in the MPCB.


Technical information about baseline power supply capability and limitations can be found in


section 3.4.1.


Additional power services not envisioned for baseline (e.g., auxiliary-battery, additional PDU,


etc.) can be evaluated and eventually provided via the implementation of dedicated extension

kit(s) upon Customer request.

#### **7.4 Data and Communication services**


SR Vehicle baseline data and communication services can be divided into In-Flight services,


that are services provided to the P/Ls on-board of the vehicle during orbital phase, Ground

based services that are services provided to the Customers via the Ground Segment or Mixed


services that are services that involves the mixture of both characteristics.


Additional data and communication services not envisioned for baseline can be evaluated and


eventually provided via the implementation of dedicated modifications upon Customer request.


Page 89/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_7.4.1 Cybersecurity Aspects_**


Cybersecurity is mandatory aspect of space missions, with its importance escalating in tandem


with the increasing complexity and connectivity of space vehicles. In this digital era, where


cyber threats are becoming more sophisticated and pervasive, the implementation of robust


cybersecurity measures is not just a precaution, but a necessity.


By ensuring the protection of critical systems and data, Space Rider cybersecurity measures


not only enhance the reliability and safety of its missions but also contribute to the overall


success by maintaining the confidentiality, integrity, and availability of vital mission-related


information. In this context, Space Rider's cybersecurity framework, with its in-depth security


of mission-critical aspects, plays a key role in fortifying the mission against digital threats, thus


ensuring its smooth and successful execution.


For missions like Space Rider, effective cybersecurity safeguards are in place to counter a


number of potential cyber-attacks that could compromise mission integrity, disrupt


communications, or even lead to catastrophic failures.


These security measures are especially significant in the context of Space Rider, where they


provide a robust shield against threats like the following:


**Interception and Eavesdropping**


Transmitted data can be intercepted by unauthorized parties. This data could contain sensitive


mission information or control commands. Space Rider ensures that even if the data sent from


ground to the orbiter is intercepted, it remains unintelligible and useless to the interceptor.


**Unauthorized Command and Control**


One of the most critical threats to a satellite is the unauthorized access and issuance of


commands. This could lead to a hostile takeover of the satellite's functionalities. Security


controls are implemented in Space Rider to ensures that only commands from verified and


trusted sources are accepted and executed.


Page 90/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Data Manipulation**


Cyber attackers could potentially alter the data being transmitted to the orbiter vehicle, leading


to incorrect commands being executed. To counter this Space Rider implements telecommand


encryption, combined with authentication, that helps in maintaining the integrity of the data,


ensuring that any alterations are easily detectable and preventable.


**Man-in-the-Middle Attacks**


These attacks occur when an attacker secretly intercepts and possibly alters the


communication between two parties. Space Rider make use of robust encryption and


authentication protocols make it exceedingly difficult for attackers to insert themselves into the


communication channel.


**Replay Attacks**


This scenario foreseen an attacker that captures a legitimate message and replays it to create


an unauthorized effect. The Space Rider implements sophisticated authentication algorithms


which includes different factors like time stamps or sequence numbers, which help in identifying


and discarding repeated messages.


The benefits of these security measures contributing significantly to raise the resilience of the


mission against cyber threats, thereby preserving the integrity and confidentiality of mission

critical data and maintaining the overall safety and success of the mission.

##### **_7.4.2 P/L Security in Space Rider: Opportunities for Independent Protection_** **_Measures_**


Space Rider's design includes a transparent and segregated infrastructure for P/Ls, which


offers a unique opportunity for Customers to implement their own security measures.


Page 91/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Transparent Infrastructure**


The transparency in Space Rider's infrastructure means that payload operators have clear


visibility into how their payloads are integrated within the vehicle. This visibility allows payload


operators to understand the specific risks and vulnerabilities relevant to their payloads and to


design their security measures accordingly.


**Segregated Infrastructure**


Segregation of the infrastructure ensures that each payload operates within its own dedicated


domain, isolated from the others. This segregation is crucial for security, as it prevents any


potential cross-contamination of cyber threats between payloads. It also means that security


measures implemented by one payload do not inadvertently impact the functionality or security


of another.


**Opportunities for Payload-Specific Security**


Payload operators have the flexibility to implement their own encryption and authentication


measures tailored to their specific needs and risk profiles. For instance, a payload requiring


high confidentiality can employ advanced encryption algorithms to protect its data. Similarly,


payloads with critical control functions can implement robust authentication protocols to ensure


that only authorized commands are executed.


This approach allows for a more customized and targeted cybersecurity strategy for each


payload, catering to diverse requirements and levels of sensitivity. It empowers payload


operators to take charge of their cybersecurity, enabling them to leverage Space Rider's


advanced infrastructure while maintaining control over their specific security needs.


In summary, while Space Rider itself may not yet extend its core cybersecurity protections to


payloads, its transparent and segregated infrastructure provides a conducive environment for


payloads to independently secure themselves, ensuring overall mission integrity and security.


Page 92/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_7.4.3 In-Flight services_**


**Data-storage service**


This service is provided as a built-in capability of the SR Vehicle through its data and


communication system allowing P/Ls to store scientific data into RM mass memory. Technical


information about data storage capability and limitations can be found in section 3.5.1.


**Auxiliary Data Service On-Board**


This service is provided as a built-in capability of the SR Vehicle through its data and


communication system allowing P/Ls to access a selected set of data of the SR Vehicle on

board, to complement or enhance their own P/L experiment data (e.g., Navigation data,


Mission Elapsed Time, Temperature of the I/F plate among others).

##### **_7.4.4 Ground-services_**


The P/Ls generated data (Scientific and Housekeeping Data) are downlinked through the


Space Rider Ground Station Network to the VCC-OC at Fucino Space Centre, during the orbital


phase of the mission. Two types of P/Ls are envisaged:


  **PUS-Compliant P/Ls** : PL HK data is automatically recognized on-board, and it is not


stored in the same file as the scientific data. For PUS compliant P/Ls, it is possible to


downlink in near real-time the P/L HK data during the visibility windows, if requested.


P/L playback HK and scientific data can also be downlinked during the visibility windows,


respecting the thresholds reported above for telemetry downlink. Simple TC routing is


offered based on APID.


  **Not PUS-Compliant P/Ls** : Real-time downlink is not possible. P/L playback HK and


scientific data can be downlinked during the visibility windows, respecting the thresholds


reported above for telemetry downlink. Simple TC routing is offered based on P/L ID.


It is important that P/Ls that are not PUS terminal clearly distinguish between HK and


Scientific files, so that they can be downlinked and processed separately.


Page 93/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


If there is only one data source/physical connection for a P/L, it is up to the P/L to discriminate


that the files for the different experiments can be uniquely identified (if more than one


experiment per P/L).


**Flight Monitoring and Commands services**


This set of services is provided as a built-in capability of the SRS through the PGCC during


mission operations. The PGCC will interface directly only with the Customers P/L through the


User Payload Operations Centre (UPOC), which represent the end-users. They will provide all


the means for P/L users to both submit user operation requests for P/L planning activities,


monitor P/L status and retrieve P/L acquisition data, other than visibility of a subset of pre

agreed information regarding the SR vehicle that can be useful for P/L planning.


PGCC services can be reached from different UPOCs using standard security protocols such


as SSL or by the VPN system based OpenVPN/IPSec solution over Internet. Other dedicated


links can be supported by PGCC only in case a specific UPOC requires them but in this case


the implementation costs will be under the specific UPOC responsibility.


A preliminary list of data exchange from PGCC and UPOC and vice-versa is presented below:







|PGCC → UPOC|UPOC → PGCC|
|---|---|
|P/L live TM<br>(Web-HMI PUS-Compliant P/L)|User Operation Request<br>(Based on the configured templates,<br>via Web-HMI)|
|Auxiliary live SRS TM<br>(Web-HMI)|P/L Direct Operation Request<br>(PDOR, same as UOR)|
|Science Raw P/L TM<br>(Query/Download via Web-HMI, this<br>data includes both HK parameters, for<br>PUS-compliant P/Ls, and HK packets)|P/L Configuration Files<br>(Logically part of UOR/PDOR<br>creation)|
|Playback P/L HK TM|P/L Resource Profiles|


Page 94/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public




|(Visualization/Download via Web-HMI,<br>for PUS-Compliant Payload, otherwise<br>may depends on provided pre-<br>processor)|(Required during missionization<br>activities)|
|---|---|
|Playback SRS Auxiliary TM<br>(Visualization/Download via Web-HMI)||
|Mission Planning Data<br>(Web-HMI)||
|UPOC Notification<br>(Web-HMI/Offline Email)||
|P/L Data Report<br>(Downloadable via Web-HMI/Offline<br>Email)||



_**Table 7-1: PGCC vs UPOC data exchange list.**_


Through the PGCC, the ground segment makes available to the end-users a set of services,


that will allow an easy management of the P/L requests, planning, monitoring of the P/L


activities and data delivery, in particular:


  **Planning Service** : present the status of the mission timeline, together with the data that


the end-user has to take into account to request/perform nominal P/L planning. The


result of the planning process will be visible on the timeline application.


  - **Monitoring Application Service** : It will allow to monitor [24] and visualize the P/L


behaviour of both real time data and archived data.


  **Commandability Service** : generate and submit the User Operations Requests (UORs)


via the front-end web application of the PLMS (located at PGCC). It also allows to


implement and submit a fast request for P/L direct command (PDOR) uplink, for


selected, critical, and urgent issues, providing all input needed to complete the request.


  **Data Processing and Archiving Service** : manage the retrieval, processing, archiving


and distribution of P/L data. Moreover, the DPAS will also manage Space Rider TM/TC


24 The level of monitoring capabilities strictly depends on PL compliance with PUS services.

Page 95/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


auxiliary data and planning data in order to create a consolidated and persistent archive


of linked and correlated data. A long-term archive for the entire set of missions will be


made available and maintained from the PGCC. The long-term archive will allow to,


among others, support P/L’s anomalies’ resolution.


The level of pre-processing on P/L received data can vary depending on their compliancy with


PUS services, in particular:


  For P/L compliant with PUS standard services the following pre-processing capabilities


are envisaged.


`o` P/L Packet and Parameters extraction, indexing and metadata enrichment.


`o` data unit conversion in common PGCC standard ones.


`o` extraction and reconstruction, if needed, of P/Ls science data.


`o` automatic monitoring of P/L status and command implementation based on the


received HK telemetry and science data.


`o` comparison of the actual P/L resource, based on recorded telemetry received from


VCC, with the nominal ones.


  In case the embarked P/L requires the definition of “custom” PUS services, for example


to wrap TM data in proprietary format, only a general set of statistics information and


reporting (e.g., amount of data received, events) can be computed. For the actual P/L


data extraction, other than the extraction of “custom” PUS packet data field, the


execution of user-provided pre-processor can be envisaged, if any. Such pre-processor


shall be validated and made available by the P/L end-user.


Access to the specific data is allowed upon authentication of authorized users.

##### **_7.4.5 Mixed services_**


**Telemetry & Telecommands (TM&TC) service**


This service shall apply to P/Ls that need to upload and download commands and data (e.g.,


video, housekeeping, science data) at each or during specific orbital passes.


Page 96/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


_Downlink capability (TM)_


The maximum reachable amount of downlink data (Telemetry) capability that can be received


from SRS is 2 GB / day for the whole Payload Aggregate at an average downlink data rate of


2 Mbps.


Telemetry encryption service is not provided by default. Further level of encryption can be


implemented by P/L Customers (see section 7.4.1).


_Uplink capability (TC)_


The minimum ensured amount of uplink data (Telecommands) capability is 1 batch of


commands per orbit (600 kb / Orbit) for whole Payload Aggregate, with an uplink data rate of


4 kbps. Baseline Telecommands related services includes on-board pre-programmed TCs in


the Mission Timeline (MTL), Direct Ground TC, TC File and On-Board Control Procedure


(OBCP) services.


Telecommands encryption service is provided by default up to RM level. Further level of


encryption can be implemented by P/L Customers (see section 7.4.1).


**Dedicated-Antenna service**


SR Vehicle baseline does not provide to the MPCB hosted payloads the capability to


send/receive data (TM) and commands (TC) through the direct use of SRS radio-frequency


channels. All the information from/to P/L must be forwarded using the on-board MMU and the


SR GS.


A Dedicated-Antenna service shall apply to P/Ls that need their RF antennas to be installed


within the MPCB (with a proper FoV) to acquire and transmit data independently as part of their


mission [25] . This service availability will be evaluated on a case-by-case basis according to SR


Vehicle project and mission optimization principles and security verification outcomes.


25 In this case, it is the P/L owner’s responsibility to issue their own Request for Frequency Allocation (RFA).

Page 97/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

#### **7.5 Microgravity services**


SR Vehicle baseline microgravity services are provided as a built-in capability through its


navigation and attitude control system. SR Vehicle can freely drift as it moves along its orbital


path with expected g-levels down to 5 x 10 [-6] g. The maximum disturbances the Payload shall


generate towards the re-entry module system is described in section 4.1.8.

##### **_7.5.1 Standard microgravity service_**


This service is provided as a built-in capability of the SR Vehicle when P/Ls require to be


exposed to standard micro-gravity levels (residual acceleration around 5 x 10 [-5] g) reachable


through different SR vehicle attitudes (see 1.5.3.1). A specific mission and operational timeline


considering the defined attitude and duration in accordance with other P/Ls needs and vehicle


constraints (e.g., thermal control, etc.) must be evaluated by the ADA during mission analyses.

##### **_7.5.2 Extreme microgravity service_**


This service is provided as a built-in capability of the SR Vehicle when a P/L requires to be


exposed to extreme micro-gravity levels (residual acceleration greater than 5 x 10 [-6] g)


reachable through a specific SR vehicle attitude (Nose-to-Nadir only, see 1.5.3.1). A specific


mission and operational timeline considering the specific attitude and duration in accordance


with other P/Ls needs and thermal controls must be evaluated by the ADA during mission


analyses.

#### **7.6 Observation / Field-of-View services**


SR Vehicle baseline observation services are provided as a built-in capability through its


navigation and attitude control system. SR Vehicle can provide pointing capability for


observation and/or communication experiments with an angle of view of 90° through the


opening the MPCB door. Possible additional structures can be required to integrate the


instrument at an adequate position and ensure the wider angle of view (see section 0).


Page 98/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


Additional observation services not envisioned for baseline (e.g., fine-pointing, etc.) can be


evaluated and eventually provided via the implementation of dedicated extension-kit(s) upon


Customer request.


_**Figure 7-2 SR MPCB Fiel-of- View capability.**_

##### **_7.6.1 Earth-observation service_**


This service is provided as a built-in capability of the SR Vehicle when a P/L requires to be


pointed directly to Earth through MPCB door upon suitable vehicle attitude placement for


specific observation purposes. A specific mission and operational timeline considering the


defined attitude and duration in accordance with other P/Ls needs (e.g., PA requirements, etc.)


and vehicle constraints (e.g., thermal control, etc.) must be evaluated by the ADA during


mission analyses.


_**Figure 7-3: SRS during Earth-observation service.**_


Page 99/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

##### **_7.6.2 Deep-space observation service_**


This service is provided as a built-in capability of the SR Vehicle when a P/L requires to be


pointed directly to deep space through MPCB door upon suitable vehicle attitude placement


for specific observation purposes. A specific mission and operational timeline considering the


defined attitude and duration in accordance with other P/Ls needs and vehicle constraints (e.g.,


thermal control, etc.) must be evaluated by the ADA during mission analyses.

#### **7.7 Exposure / Protection To / From External (Space) Environment**


Upon MPCB door opening, the SR enables the exposure of the payloads to the space


environment (e.g., radiation, sunlight, …) as described in chapter 0.

##### **_7.7.1 Exposure to external environment service_**


This service is provided as a built-in capability of the SR Vehicle through the accommodation


of the P/L that need exposure to radiation environment for the scope of their flight operations


in a proper location inside the MPCB result of the ADA accommodation activities.

##### **_7.7.2 Sun-pointing and Sun-avoidance services_**


Customer’s P/L can require the availability of pointing their observation instruments directly to


the Sun or total avoiding direct exposure to it.


**Sun-pointing service**


This service is provided as a built-in capability of the SR Vehicle when a P/L requires to be


pointed directly at the sun for specific observation purposes. A specific mission and operational


timeline considering the defined attitude and duration in accordance with other P/Ls needs


(e.g., PA requirements, etc.) and vehicle constraints (e.g., thermal control, etc.) must be


evaluated by the ADA during mission analyses.


Page 100/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


**Sun-avoidance service**


This service is provided as a built-in capability of the SR Vehicle when a P/L requires to avoid


direct sun-light exposure or in case be deactivated if the sun enters in their field of view. A


specific mission and operational timeline considering the defined attitude and duration in


accordance with other P/Ls needs (e.g., PA requirements, etc.) and vehicle constraints (e.g.,


thermal control, etc.) must be evaluated by the ADA during mission analyses.

#### **7.8 Atmospheric services**


SR Vehicle baseline atmospheric services are not provided as a built-in capability. During flight


the MPCB hosted P/Ls are exposed to atmospheric / pressure environment described in 4.1.7.


Additional atmospheric services not envisioned for baseline (e.g., pressurization, ventilation,


auxiliary gases, etc.) can be evaluated and eventually provided via the implementation of


dedicated extension-kit(s) upon Customer request.

#### **7.9 Separation, Retrieval and Robotic Handling services**


SR Vehicle baseline separation service is provided as a built-in capability through its navigation


and attitude control system. SR Vehicle can provide specific attitudes during the release phase


of a deployable P/L from its MPCB (e.g., CubeSat separation from its dispenser) into its own


free-flying mission. Possible additional structures can be required to integrate the P/L at an


adequate position and ensure the wider angle for departure corridor (see section 0).


Additional contextual services not envisioned for baseline (e.g., retrieval service, robotic


handling etc.) can be evaluated and eventually provided via the implementation of dedicated


extension-kit(s) upon Customer request.

#### **7.10 Additional services (Upon Customer’s Request)**


Services or capabilities not listed above but considered required by a Customer can be


evaluated and estimated for implementation upon specific Customer request.


Page 101/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **8 DOCUMENTS**

#### **8.1 Reference Documents**


Users can refer to the following documents for reference information at their latest available


versions:











_**Table 8-1: Reference documents.**_


Page 102/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **9 ACRONYMS**


AAR Aggregate Acceptance Review


ADA Aggregate Design Authority


AIT Assembly, Integration and Test


ALEK AVUM Life-Extension Kit


ALTEC Altec S.p.A.


AO Atoms of Oxygen


AOM AVUM Orbital Module


APID Application ID


AR Acceptance Review


ATB Avionic Test Bench


ATOX Atomic Oxygen


AVIO Avio S.p.A.


AZ Approach Zone


B2E Bay-to-Earth


B2Z Bay-to-Zenith


CAD Computer-Aided Design


CoG Centre of Gravity


CSG Centre Spatiale Guyanese


CPO Close Proximity Operations


DLL Design Limit Loads


D-PL Deployable Payload


D-PL (KZ) Deployable Payload with operations in Keep-Out Zone


D-PL (M) Deployable Payload with manoeuvre capability


D-PL (NM) Deployable Payload with no manoeuvre capability


EA Early-Retrieval


EAR Export Administration Regulations


ECSS European Cooperation for Space Standardization


Page 103/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


EFM Electrical and Functional Model


EGSE Electrical GSE


EMC Electro-Magnetic Compatibility


EPS Electrical Power System


ESA European Space Agency


ESD Electro-Static Discharge


ESTACK European Space Tracking


FEM Finite Element Model


FM Flight Model


FMA Final Mission Analysis


FoV Field of View


F-PL Fixed Payload


FS Flight Segment


FSA Flight Service Agreement


GNSS Global Navigation Satellite System


GS Ground Segment


GSE Ground Support Equipment


GSN Ground Station Network


H0 Launch date / time


HMI Human Machine Interface


HK House Keeping


ID Identification


IMU Inertial Measurement Unit


IOD In-Orbit Demonstration


IOS In-Orbit Services


IOV In-Orbit Validation


IP In-Plane or Internet Protocol


IPSec Internet Protocol Security


ITAR International Traffic in Arms Regulations


Page 104/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


IXV Intermediate eXperimental Vehicle


KOZ Keep-out Zone


LA Late-Access


LCL Latching Current Limiter


LEO Low Earth Orbit


LEOP Launch and Early Operation Phase


LFL Low-Frequency Loads


LDS Landing Site


LS Launch Site


LSDO Landing Site Director of Operations


MCC Mission Control Centre


MCI Mechanical Capture Interface


MF Maiden Flight


MGSE Mechanical GSE


MH Mobile Hangar


MLI Multi-Layer Insulation


MMU Mass Memory Unit


MOC Molecular Contamination


MoU Memorandum of Understanding


MPCB Multi-Purpose Cargo Bay


MTQ Magneto TorQuers


M-PL Movable Payload


N2N Nose-to-Nadir


OBC On-Board Computer


OBCP On-Board Control Procedure


OOP Out-of-Plane


OPSIM Operational SIMulator


OSZ Off-Set Bay-to-Zenith


PA Payload Aggregate


Page 105/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


PAC Particulate Contamination


PDF Portable Document Format


PDOR Payload Direct Operation Request


PDU Power Distribution Unit


PFM Proto-Flight Model


PGCC Payloads Ground Control Centre


P/L Payload


PLAG Payload Aggregate


PLGSO Post-Landing Ground Safety Office


PMA Preliminary Mission Analysis


PPE Personal Protective Equipment


PPF Payload Processing Facility


PUS Packet Utilisation Standard


QR Qualification Review


QSL Quasi-Static Loads


RADAR RAdio Detection And Ranging


REI Regulations concerning the use of facilities at the CSG


RH Relative Humidity


RM Re-entry Module


ROZ Roll-Out Zone


RW Reaction Wheels


SPG Single-Point of Grounding


SR Space Rider


SRS Space Rider System


SSL Secure Socket Layer


SSO Sun-Synchronous Orbit


STD Standard Payload


T2S Tail-to-Sun


TAS-I Thales Alenia Space – Italy S.p.A.


Page 106/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public


TC Telecommand


TCS Thermal Control System


TM Telemetry


TM&TC Telemetry & Telecommand


TMM Thermal-Mathematical Model


TPZ Telespazio S.p.A.


TRP Temperature Reference Point (or Thermal Reference Point)


TZ Touch-down Zone


UDP User Datagram Protocol


UOR User Operation Request


UPOC User’s Payload Control Centre


VCC Vehicle Control Centre


VCC-LC VCC-Landing Control


VCC-OC VCC-Orbital Control


VEGA Vettore Europeo di Generazione Avanzata


VEGA-C VEGA Consolidated


VPN Virtual Private Network


Page 107/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **ANNEX A**

#### **Possible Applications for Science and Technology Research**


Below it will be shown non-exhaustive list of the Scientific and Technology Research fields that


may benefit from the Space Rider services.


Page 108/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

### **ANNEX B**

#### **Space Rider Payload Mission Timeline**





|Time|Actor|Activity|Type|Milestone|
|---|---|---|---|---|
|<br>**_Phase I – Preliminary Aggregate Study_**<br>|<br>**_Phase I – Preliminary Aggregate Study_**<br>|<br>**_Phase I – Preliminary Aggregate Study_**<br>|<br>**_Phase I – Preliminary Aggregate Study_**<br>|<br>**_Phase I – Preliminary Aggregate Study_**<br>|
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|MPCB<br>Operator|Open Call for Flight Opportunities.|||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|Customer|Response to Flight Opportunities or direct contact for P/L preliminary<br>feasibility evaluation:<br>- P/L Questionnaire delivery.|Document(s)<br>Delivery||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|Customer,<br>MPCB<br>Operator &<br>ADA|Preliminary technical meetings for feasibility study.|Technical<br>meeting(s)||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|MPCB<br>Operator &<br>ADA|First feasibility evaluation.|||
|<br>**_Phase IIa: Preliminary Aggregate Definition_**<br>|<br>**_Phase IIa: Preliminary Aggregate Definition_**<br>|<br>**_Phase IIa: Preliminary Aggregate Definition_**<br>|<br>**_Phase IIa: Preliminary Aggregate Definition_**<br>|<br>**_Phase IIa: Preliminary Aggregate Definition_**<br>|
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|Customer|P/L IRD and Preliminary Safety File delivery.|Document(s)<br>Delivery||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|Customer,<br>MPCB<br>Operator &<br>ADA|Interface Progress Meetings.|Technical<br>meeting(s)||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|ADA|Preliminary P/L Accommodation Feasibility|||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|MPCB<br>Operator &<br>ADA|P/L Selection for Preliminary Aggregate Definition|||
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|MPCB<br>Operator &<br>ADA|Preliminary Aggregate Validation||Preliminary<br>Aggregate<br>Validation|
|Commercial<br>opportunities<br>at this stage<br>are evaluated<br>continuously<br>during SR<br>program<br>execution.|Customer &<br>MPCB<br>Operator|Signature of Memorandum of Understanding (MoU)||MoU|
|<br>**_Phase IIb: Aggregate Definition Confirmation_**<br>|<br>**_Phase IIb: Aggregate Definition Confirmation_**<br>|<br>**_Phase IIb: Aggregate Definition Confirmation_**<br>|<br>**_Phase IIb: Aggregate Definition Confirmation_**<br>|<br>**_Phase IIb: Aggregate Definition Confirmation_**<br>|


Page 109/114

















Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public























|Col1|Customer &<br>MPCB<br>Operator as<br>observer|P/L Preliminary Design Review (PDR) or equivalent|Col4|PDR|
|---|---|---|---|---|
||Customer|P/L Preliminary Data Delivery:<br>- Documents at PDR Level<br>- P/L Safety File (Phase 0)|Document(s)<br>Delivery||
||Customer|P/L Preliminary Models:<br>- CAD Model<br>- Thermal Mathematical Model (TMM)<br>- Finite Element Models (FEMs)|Analytical<br>Model(s)<br>Delivery||
||ADA|Start of Preliminary Mission Analysis||PMA<br>Kick-Off|
||ADA &<br>MPCB<br>Operator|End of Preliminary Mission Analysis||PMA<br>Review|
||MPCB<br>Operator|P/L Selection for a specific SR mission<br>- Statement of Work (SoW) to P/L<br>- Interface Control Document (ICD) - Issue 1|Document(s)<br>Delivery||
||Customer<br>& MPCB<br>Operator|Signature of Flight Service Agreement (FSA)||FSA|
|<br>**_Phase III: Final Aggregate Desing_**<br>|<br>**_Phase III: Final Aggregate Desing_**<br>|<br>**_Phase III: Final Aggregate Desing_**<br>|<br>**_Phase III: Final Aggregate Desing_**<br>|<br>**_Phase III: Final Aggregate Desing_**<br>|
||Customer &<br>MPCB<br>Operator as<br>observer|P/L Critical Design Review (CDR) or equivalent||CDR|
||Customer|P/L Consolidated Data Delivery:<br>- Documents at CDR Level (as specified in the SoW)<br>- P/L Safety File (Phase 1)|Document(s)<br>Delivery||
||Customer|P/L Consolidated Models:<br>- CAD Model<br>- Thermal Mathematical Model (TMM)<br>- Finite Element Models (FEMs)|Analytical<br>Model(s)<br>Delivery||
||Customer|High-Fidelity 3D Mock-Up delivery.|Physical<br>Model(s)<br>Delivery||
||SRS Mission<br>Operator|Start of Final Mission Analysis.||FMA Kick-Off|
||ADA|P/Ls Fit Check on RM MPCB.||Fit-Checks|


Page 110/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public



























|T0 –<br>10 Months|<< Space Rider RM PFM moved to ESTEC for ETC >>|Col3|Col4|Col5|
|---|---|---|---|---|
||Customer|P/L Electrical and Functional Model (EFM) delivery|Physical<br>Model(s)<br>Delivery||
||ADA|P/Ls EFM Model Integration, Electrical and Functional Tests on RM ATB.||Preliminary<br>Electrical and<br>Functional Tests|
||Customer &<br>MPCB<br>Operator as<br>observer|P/L Qualification Review (QR) or equivalent||QR/AR|
||Customer|Documents post QR (as specified in the SoW)<br>P/L Safety File (Phase 2) delivery|Document(s)<br>Delivery||
||MPCB<br>Operator|Interface Control Document (ICD) - Issue 2|Document(s)<br>Delivery||
||ADA|End of Final Mission Analysis||FMA<br>Review|
|<br>**_Phase IV: Final Aggregate AIT_**<br>|<br>**_Phase IV: Final Aggregate AIT_**<br>|<br>**_Phase IV: Final Aggregate AIT_**<br>|<br>**_Phase IV: Final Aggregate AIT_**<br>|<br>**_Phase IV: Final Aggregate AIT_**<br>|
||Customer|Pre-Shipment Review (PSR)|<br>|PSR|
||Customer|PSR Documentation (as specified in the SoW)|Document(s)<br>Delivery||
||Customer &<br>MPCB<br>Operator|P/L FM and/or Representative Dummy delivery|Physical<br>Model(s)<br>Delivery|Hand-over to<br>MPCB Operator|
||ADA|P/Ls Integration, Electrical and Functional Tests, and Mass Properties||Final<br>Electrical and<br>Functional Tests|
|T0 –<br>3 Months|**_<< Space Rider RM moved to Launch Site at Kourou >>_**|**_<< Space Rider RM moved to Launch Site at Kourou >>_**|**_<< Space Rider RM moved to Launch Site at Kourou >>_**|**_<< Space Rider RM moved to Launch Site at Kourou >>_**|
|T0 –<br>2 Months|Customer|Environmental sensitive P/L delivery|Physical<br>Model(s)<br>Delivery|Hand-over to<br>MPCB Operator|
||Customer|P/L Safety File (Phase 3) delivery|Document(s)<br>Delivery||
||ADA|Aggregate Acceptance Review||AAR|
||RM Design<br>Authority|MPCB Main Door Closure|||


Page 111/114







Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public



|Col1|SRS Mission<br>Operator|Flight Readiness Review|Col4|FRR|
|---|---|---|---|---|
|T0 –<br>36 h|**_<< Space Rider System (SRS) and fairing integrated with VEGA-C Launch Vehicle at Launch Pad >>_**|**_<< Space Rider System (SRS) and fairing integrated with VEGA-C Launch Vehicle at Launch Pad >>_**|**_<< Space Rider System (SRS) and fairing integrated with VEGA-C Launch Vehicle at Launch Pad >>_**|**_<< Space Rider System (SRS) and fairing integrated with VEGA-C Launch Vehicle at Launch Pad >>_**|
||Launch<br>Operator|Launch Readiness Review||LRR|
|T0 –<br>17 h|ADA|Late-Access window START for P/Ls integration||Late-Access<br>Integration Start|
|T0 –<br>16.5 h|ADA|Late-Access window END for P/Ls integration||Late-Access<br>Integration End|
|T0 –<br>8 h|Launch<br>Operator|Chronology Start|||
|<br>**_Phase V: Aggregate Flight Operations_**<br>|<br>**_Phase V: Aggregate Flight Operations_**<br>|<br>**_Phase V: Aggregate Flight Operations_**<br>|<br>**_Phase V: Aggregate Flight Operations_**<br>|<br>**_Phase V: Aggregate Flight Operations_**<br>|
|T0|<br>**_<< Launch >>_**<br>|<br>**_<< Launch >>_**<br>|<br>**_<< Launch >>_**<br>|<br>**_<< Launch >>_**<br>|
||Launch<br>Operator|Ascent Phase and LEOP<br>Commissioning and MPCB Main Door opening|||
|T0 +<br>3 h|MPCB<br>Operator|Start of Experiments Window|||
|T0 +<br>60 days|MPCB<br>Operator|End of Experiments Window|||
|L0 –<br>1 day|SRS Mission<br>Operator|Avionic and P/Ls Cool-Down|||
||Operations<br>Authority|MPCB Main Door Closure<br>Authorization from Landing Site<br>De-Orbit burn<br>Separation of RM (for re-entry) and AOM (for destructive re-entry).|||
||Operations<br>Authority|Coasting, re-entry, and descent.<br>Sub-sonic Parachute deployment (M=0.2) at 6-10Km alt.<br>Guided Parafoil deployment.|||
|L0|<br>**_<< Touchdown >>_**<br>|<br>**_<< Touchdown >>_**<br>|<br>**_<< Touchdown >>_**<br>|<br>**_<< Touchdown >>_**<br>|
|<br>**_Phase VI: Aggregate Post-flight Operations_**<br>|<br>**_Phase VI: Aggregate Post-flight Operations_**<br>|<br>**_Phase VI: Aggregate Post-flight Operations_**<br>|<br>**_Phase VI: Aggregate Post-flight Operations_**<br>|<br>**_Phase VI: Aggregate Post-flight Operations_**<br>|
||SRS Mission<br>Operator|RM Vehicle Power-down, deactivation of the electric and pyrotechnic circuits<br>(except OBC, PDU and Payload Aggregate powered up at 50W).|||
|L0 +<br>2h|SRS Mission<br>Operator|Operators are allowed to perform payloads early retrieval.|||


Page 112/114











Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public





|L0 +<br>2.5h|MPCB<br>Operator &<br>Customer|Early-retrieval Payloads are moved to PPF.<br>Hand-over of P/Ls from MPCB Operator to owners.|P/Ls FM back<br>to Customer|Col5|
|---|---|---|---|---|
||SRS Mission<br>Operator|RM Vehicle moved to the decontamination Facility|||
||SRS Mission<br>Operator|Operators are allowed to perform MPCB access for retrieval of Standard P/Ls.|||
|L0 +<br>16 days|MPCB<br>Operator &<br>Customer|Hand-over of P/Ls from MPCB Operator to owners.|P/Ls FM back<br>to Customer||
||SRS Mission<br>Operator|RM Vehicle prepared for shipment to the refurbishment facilities.||To<br>Refurbishment|


Page 113/114





_**Table 0-1: Space Rider Mission Timeline**_





Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


ESA UNCLASSIFIED – Releasable to the Public

## **End of Document**


Page 114/114


Issue 2.0   Date 06/12/2023   Ref. ESA-STS-SR-TN-2018-0002


