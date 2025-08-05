## Data Sheet **AD3300/1/4/5**

### ADI Confidential Optimized all Hardware Edge Node, 10BASE-T1S Ethernet to the Edge Bus (E [2] B) Transceiver



**FEATURES**


- 10BASE-T1S IEEE 802.3-2022 compliant PHY with support for
PLCA and an integrated MAC

- 10BASE-T1S PHY operating modes




 - Point-to-point half-duplex (≥ 15 m)

 - Multidrop configuration half-duplex (≥ 25 m, ≥ 8 nodes)

- PLCA features: PLCA coordinator, burst mode, precedence
mode, and multiple PLCA IDs

- MAC Features


 - AD3300 only: OPEN Alliance 10BASE-T1x MAC-PHY serial
interface


 - AD3300 only: Transmit priority queues

 - 16 MAC address filters


- IEEE 802.1AS / IEEE 1588 support for TSN using the gPTP
combined with sensor timestamping and actuator synchronization


- Low Complexity Ethernet Engine

 - Provides a deterministic, low-latency data path between
10BASE-T1S to the SAIF


 - 12 SAIF pins support simultaneous operation of several common sensor/actuator interface standards and functions, including SPI, I [2] C, UART, PWM, GPIO, Flexible I/O, and bridge to
LIN


 - SMC enables periodic read and write functions on all interfa
ces


 - AD3300 supports dual mode: MAC-PHY and LCE operation
simultaneously




 - AD3304/5 only: Bridge to ISELED and ILaS

- OPEN Alliance features sleep/wake-up, topology discovery, and
advanced diagnostics

 - Enable output pin (EN) to power down the regulated supply
inputs in sleep mode




 - Support for local (WAKE input pin) and network (wake-up
pulse) wake

- Suitable for 12 V, 24 V, 48 V automotive electrical systems or
operating from 5 V levels only

- Detection capability for over voltage and under voltage events
when monitoring the VBAT pin

- General-purpose ADC

- SSC for handling fault conditions

- Low-current 3.3 V LDO using the LVDD pin as an output

- Compatible with power delivery over data cable

- Provides robust EMC/EMI performance

 - Low cost bus interface network with no external ESD components required

 - Enhanced noise immunity providing additional performance
for noisy environments

- Low power consumption: maximum current of 50 mA in functional modes of operation and 40 μA in sleep mode

- 1.8 V to 3.3 V I/O logic levels with support for 5 V inputs

- −40°C to +150°C junction temperature range

- Small package: 4 mm x 4 mm 24-lead LFCSP (QFN) package

- AEC-Q100 qualified for automotive applications



**VBAT** **EN** **DVDD** **LVDD** **DVDDIO** **AVDD** **TEST** **XTAL_I/_O**





**WAKE**


**HOST INTERFACE:**

**SPI**
**I** **[2]** **C**

**UART**

**LIN**

**GPIO/PWM**

**VOLTAGE MONITOR**

**FLEXIBLE I/O**

**ILaS/ISELED***


**SSC I/O**


***AD3304/AD3305 only**













**ETH_P**


**ETH_N**



**Rev. SpB**


**[DOCUMENT FEEDBACK](https://form.analog.com/Form_Pages/feedback/documentfeedback.aspx?doc=AD3300 1 4 5.pdf&product=AD3300 1 4 5&rev=SpB)**


**[TECHNICAL SUPPORT](http://www.analog.com/en/content/technical_support_page/fca.html)**



_**Figure 1. AD3301/4/5 Functional Block Diagram**_


Information furnished by Analog Devices is believed to be accurate and reliable "as is". However, no responsibility is assumed by Analog
Devices for its use, nor for any infringements of patents or other rights of third parties that may result from its use. Specifications subject to
change without notice. No license is granted by implication or otherwise under any patent or patent rights of Analog Devices. Trademarks and
registered trademarks are the property of their respective owners.All Analog Devices products contained herein are subject to release and
availability.


## Data Sheet **AD3300/1/4/5**

### ADI Confidential Optimized all Hardware Edge Node, 10BASE-T1S Ethernet to the Edge Bus (E [2] B) Transceiver



**VBAT** **EN** **DVDD** **LVDD** **DVDDIO** **AVDD** **TEST** **XTAL_I/_O**



















**ETH_P**


**ETH_N**





_**Figure 2. AD3300 Functional Block Diagram (Dual mode)**_



E [2] B and the E [2] B logo are trademarks of Analog Devices, Inc.
**APPLICATIONS**


- Automotive internal and external lighting

- Automotive body and chassis domain control


**Rev. SpB**




- Automotive sensor and actuator networking

- Automotive Ethernet based zonal architectures


- Automotive in-vehicle networking



**[DOCUMENT FEEDBACK](https://form.analog.com/Form_Pages/feedback/documentfeedback.aspx?doc=AD3300 1 4 5.pdf&product=AD3300 1 4 5&rev=SpB)**


**[TECHNICAL SUPPORT](http://www.analog.com/en/content/technical_support_page/fca.html)**



Information furnished by Analog Devices is believed to be accurate and reliable "as is". However, no responsibility is assumed by Analog
Devices for its use, nor for any infringements of patents or other rights of third parties that may result from its use. Specifications subject to
change without notice. No license is granted by implication or otherwise under any patent or patent rights of Analog Devices. Trademarks and
registered trademarks are the property of their respective owners.All Analog Devices products contained herein are subject to release and
availability.


## Data Sheet AD3300/1/4/5



**TABLE OF CONTENTS**


Features................................................................ 1

Applications........................................................... 2
General Description...............................................4
External Specifications.......................................5
Specifications........................................................ 6
Operating Conditions..........................................6
Electrical Characteristics....................................7
Power Consumption Characteristics.................. 9
OPEN Alliance SPI I/O Timing Specifications.. 10
SAIF I/O Timing Specifications.........................11
System Specifications...................................... 17
Absolute Maximum Ratings.................................18
Thermal Resistance......................................... 18
Electrostatic Discharge (ESD) Ratings.............18
ESD Caution.....................................................19



Pin Configuration and Function Descriptions...... 20
Designer Reference.............................................23
Power Configurations.......................................23
Layout Guidelines.............................................23
Electromagnetic Compatibility (EMC)...............25
Power Supply Requirements...............................26
Operating Modes..............................................26
Power-Up Sequence........................................ 26
Power-Down Sequence....................................27
Remote Node Interfaces......................................28
Typical Connection Diagrams..............................29
Outline Dimensions............................................. 31

Automotive Products........................................... 33
Ordering Guide.................................................33
Evaluation Boards............................................ 33



**REVISION HISTORY**


**03/2025—Rev. SpA to Rev. SpB**
Crystal circuit Transconductance (g M ) added in Table 1..................................................................................6
C IN and C OUT combined to a single pin capacitance parameter C PIN in Table 2............................................. 7
I DVDDIO calculation added (DVDDIO Current)..................................................................................................9
Routing notes updated...................................................................................................................................24
AD3301 only: CS-24-2 (LFCSP_SS) package added....................................................................................31
AD3301 only: CS-24-2 (LFCSP_SS) package option added.........................................................................33


**01/2025—Rev. Sp0 to Rev. SpA**
Generic open drain support removed.............................................................................................................. 1
AD3300 only: Default mode (OTP configuration) added..................................................................................4
OTP programming temperature range extended in Table 1.............................................................................6
Temperature sensor added in Table 2..............................................................................................................7
AD3300 only: t 32 parameter min. timing value replaced by max. timing value in Table 4..............................10
t 33 parameter description clarified in Table 4................................................................................................. 10
AD3300 only: TS_CAPT and TS_TIMER timings added in Table 5...............................................................11
System EMI/EMC compliance with SAEJ2962-3 added in Table 8............................................................... 17
Clarification added to thermal resistance simulation in Table 11................................................................... 18
FICDM class corrected (C2b → C2a) in Table 13..........................................................................................19
Additional information to pin descriptions added in Table 14.........................................................................21
Layout guidelines updated.............................................................................................................................23
Lockout mode description updated................................................................................................................26
Power down sequence updated.....................................................................................................................27
Footnote added to Table 16........................................................................................................................... 28

Notes added to Table 17................................................................................................................................30


**05/2024—Revision Sp0: Initial Version**


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 3 of 33**


## Data Sheet AD3300/1/4/5

**GENERAL DESCRIPTION**



The AD3300/AD3301/AD3304/AD3305 are highly optimized, all
hardware remote devices for 10BASE-T1S Ethernet connectivity
to remote sensors and actuators. They provide the ability to remove
microcontrollers from edge nodes in automotive applications.



The PHY is compliant with the IEEE 802.3 [™] -2022 Ethernet standard for short reach 10 Mbps single pair Ethernet, and operates in
point-to-point (half-duplex) configurations up to at least 15 m and
multidrop configurations up to at least 25 m with up to at least 8
nodes.


Physical layer collision avoidance (PLCA) is supported for improving latency and throughput performance in a half-duplex communication system. The PLCA block includes PLCA coordinator mode,
burst mode, and precedence mode. Multiple PLCA IDs reduce
latency as certain nodes can be prioritized using more than one
transmit opportunity within a PLCA cycle.


OPEN Alliance TC10/TC14 features include:


- Sleep/Wake-up

- Topology Discovery

- Advanced diagnostics including dynamic channel quality (DCQ)
and signal quality index (SQI)


The transceiver contains an integrated media access control (MAC)
interface with 16 MAC address filters.


Only the AD3300 model allows direct connectivity with a host
controller via an OPEN Alliance 10BASE-T1x MAC-PHY Serial
Interface. This SPI enables the use of lower capability processors
without an integrated MAC, which provides for the lowest overall
system level power consumption. Incoming Ethernet frames can
be assigned to different transmit priority queues. Full switching
capability between the 10BASE-T1S network interface, OA-SPI,
and SAIF is supported. This enables, for example, a processor
shared access to the 10BASE-T1S network in conjunction with the
LCE (dual mode).


The AD3300 default configuration has the MAC-PHY OA-SPI interface disabled (LCE only mode). The user must enable the
MAC-PHY OA-SPI interface over the network via an E [2] B message,
setting the node to dual mode access. For systems requiring local
microcontroller OA-SPI interface access on power-up, the dual
mode configuration can be programmed into the OTP.


Time-sensitive networking (TSN) is supported using the IEEE
802.1AS [™] / IEEE 1588 [™] engine to synchronize with a generalized
precision time protocol (gPTP) grandmaster. gPTP enables highprecision clock recovery with ultra-low jitter for synchronization to a
common network time and timestamping of sensor data.


Over voltage (OV) and under voltage (UV) events can be detected
when monitoring the battery via the VBAT pin using programmable
over voltage and under voltage thresholds.



The integrated safe state controller (SSC) can monitor fault detection mechanisms and place the device in a safely defined mode of
operation in the event of a fault condition. This ensures that the
10BASE-T1S node enters a pre-defined state in the event of a local
fault.


In addition, E [2] B [™] simplifies the networking of sensors and actuators in the vehicle by integrating a low complexity Ethernet (LCE)
hardware engine, removing the need for microcontrollers in sensor
and actuator nodes. This offers the ability to implement an all-hardware edge node, greatly simplifying edge node implementation.


A system utilizing E [2] B comprises a controller node with a 10BASET1S interface along with one or more AD3300/1/4/5 devices. All
AD3300/1/4/5 devices operate in remote mode (LCE running E [2] B
protocol), bridging directly from the IEEE 10BASE-T1S network
to sensors and/or actuators. All software can be removed from
the edge nodes and centralized either in the controller node or
in another node/device on the Ethernet network. An E [2] B network
example is shown in Figure 3.


The E [2] B transport protocol (EBTP) specifies a highly optimized
remote control protocol (RCP) to transport control and interface
data over a network between E [2] B capable entities. These entities
include, but are not limited to, E [2] B transceivers and T1S compliant
MAC-PHYs combined with a controller running the E [2] B transport
protocol driver. The E [2] B software uses this protocol to configure
all E [2] B remote nodes and to packet or parse E [2] B data within
Ethernet frames. This enables efficient communication to/from the
remote nodes. The E [2] B software layer can be run on a controller
node connected directly to the IEEE 10BASE-T1S bus / network.
Or alternatively on a zonal or central processing unit that may be
connected through one or more Ethernet switch devices.


The AD3300/1/4/5 consume Ethernet frames generated by the E [2] B
software layer in the controller node. These frames may contain
status requests, configuration commands, or data frames for connected actuators. Responses for status requests and configuration
frames or data from connected sensors are automatically transmitted back to the E [2] B controller node.


If the frames contain data for the connected sensor/actuator interface (SAIF), the E [2] B remote node outputs this data via the pre-configured pins. If a response is captured and an acknowledgment is
required, the E [2] B remote node prepares the response frame which
is transmitted back to the E [2] B controller node.


All of the Ethernet frame parsing and response frame generation
is performed exclusively in hardware (no software stack needed)
by the AD3300/1/4/5. This means that no external processor is
required at the sensor/actuator to enable the connection to the
IEEE 10BASE-T1S network. The resulting network can be used to
create both simple and complex control loops.



**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 4 of 33**


## Data Sheet AD3300/1/4/5

**GENERAL DESCRIPTION**



The AD3300/1/4/5 supports many common automotive sensor/actuator interface protocols, for example SPI, I [2] C, UART, GPIO, and
PWM. Additional interfaces can be implemented using Flexible
I/O. Bridging to several commonly used automotive networking
protocols such as LIN is supported as well.


Additionally, the AD3304/5 supports other internal lighting network
protocols such as ISELED [1] and ILaS [2]



The scannable memory controller (SMC) block enables simple
functions to be repeated on a defined time interval. The SMC
provides flexibility and adaptability, allowing the system to respond
to changes in conditions or requirements effectively without any
instruction from the software other than the configuration, reducing
traffic on the Ethernet bus.
































|CONTROLLER NODE DROP NODE<br>SAIF<br>(SPI) SENSOR/<br>AD3301/4/5<br>ZONAL ECU ACTUATOR<br>ETHERNET WITH CPU OA-SPI AD3300/6 10BASE-T1S<br>NETWORK OPERATING IN OPERATING IN SAIF l<br>E2B CONTROLLER SW MAC-PHY MODE E2B REMOTE (UART) SENSOR/ a<br>MODE ACTUATOR<br>i<br>t<br>SAIF* n<br>SENSOR/<br>e<br>*AD3300 DUAL-MODE ONLY ACTUATOR DROP NODE<br>d n<br>OA-SPI LOCAL MICRO- AD3300 CONTROLLER i o d<br>f<br>n i e<br>OPERATING IN SAIF t<br>E2B DUAL MODE (I2C) SENSOR/ o a r<br>DROP NODE ACTUATOR i<br>C m u<br>AD3301/4/5<br>SAIF q<br>LIN LIN LIN (LIN) OPERATING IN r<br>NETWORK TRX E2B REMOTE END NODE I o e<br>D<br>MODE SAIF (PWM) SENSOR/ f R<br>AD3301/4/5 ACTUATOR A n<br>OPERATING IN SAIF I A<br>E2B REMOTE (GPIO) SENSOR/<br>LIN LIN MODE ACTUATOR<br>ACTUATOR SENSOR|CONTROLLER NODE<br>ZONAL ECU<br>OA-SPI AD3300/6<br>WITH CPU<br>OPERATING IN<br>MAC-PHY MODE<br>E2B CONTROLLER SW<br>i<br>t<br>SAIF* n<br>SENSOR/<br>*AD3300 DUAL-MODE ONLY ACTUATOR|10BASE-T1S|DROP NODE<br>SAIF<br>(SPI) SENSOR/<br>AD3301/4/5<br>ACTUATOR<br>OPERATING IN SAIF<br>E2B REMOTE (UART) SENSOR/<br>MODE ACTUATOR|
|---|---|---|---|
|**ETHERNET**<br>**NETWORK**<br>**AD3301/4/5**<br>**OPERATING IN**<br>**E2B REMOTE**<br>**MODE**<br>**DROP NODE**<br>**AD3300**<br>**OPERATING IN**<br>**E2B DUAL MODE**<br>**SENSOR/**<br>**ACTUATOR**<br>**DROP NODE**<br>**AD3301/4/5**<br>**OPERATING IN**<br>**E2B REMOTE**<br>**MODE**<br>**END NODE**<br>**ZONAL ECU**<br>**WITH CPU**<br>**AD3300/6**<br>**OPERATING IN**<br>**MAC-PHY MODE**<br>**CONTROLLER NODE**<br>**E2B CONTROLLER SW**<br>**OA-SPI**<br>**10BASE-T1S**<br>**SAIF**<br>**(I2C)**<br>**AD3301/4/5**<br>**OPERATING IN**<br>**E2B REMOTE**<br>**MODE**<br>**DROP NODE**<br>**LIN**<br>**TRX**<br>**LIN**<br>**SENSOR**<br>**LIN**<br>**ACTUATOR**<br>**SAIF**<br>**(LIN)**<br>**LIN**<br>**LIN**<br>**NETWORK**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF**<br>**(SPI)**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF**<br>**(UART)**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF**<br>**(PWM)**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF**<br>**(GPIO)**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF***<br>***AD3300 DUAL-MODE ONLY**<br>**LOCAL MICRO-**<br>**CONTROLLER**<br>**OA-SPI**<br>ADI Confidential<br>Information<br>A Required|**ZONAL ECU**<br>**WITH CPU**<br>**AD3300/6**<br>**OPERATING IN**<br>**MAC-PHY MODE**<br>**CONTROLLER NODE**<br>**E2B CONTROLLER SW**<br>**OA-SPI**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF***<br>***AD3300 DUAL-MODE ONLY**<br>nti<br>|**10BASE-T1S**<br>|**AD3301/4/5**<br>**OPERATING IN**<br>**E2B REMOTE**<br>**MODE**<br>**END NODE**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF**<br>**(PWM)**<br>**SENSOR/**<br>**ACTUATOR**<br>**SAIF**<br>**(GPIO)**<br><br>|



_**Figure 3. Example Conceptual E**_ _**[2]**_ _**B Network**_



**EXTERNAL SPECIFICATIONS**


The AD3300/AD3301/AD3304/AD3305 10BASE-T1S transceivers
conform to the specifications listed below.


- IEEE Standard 802.3 [™] -2022


- IEEE 802.3 Clause 148 PLCA Reconciliation Sublayer (RS)

- OPEN Alliance 10BASE-T1x MAC-PHY Serial Interface V1.1


- OPEN Alliance TC10/TC14 10BASE-T1S Sleep/Wake-up version 1.0


1 Protocol: Integrated Smart Ecosystem Light Emitting Diode.
2 Field Bus: ISELED Light and Sensor.




- OPEN Alliance TC14 10BASE-T1S Topology Discovery Specification version 1.0


- OPEN Alliance TC14 Advanced diagnostic features for 10BASET1S automotive Ethernet PHYs version 1.1

- AD3300/1/4/5 is compatible with the I [2] C-bus specification v2.1

- AD3300/1/4/5 conforms to the LIN specification v2.2

- AD3304/5 is compatible with ISELED and ILaS interface by
INOVA Semiconductors



**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 5 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**OPERATING CONDITIONS**


AVDD = 4.75 V to 5.25 V; DVDDIO = 1.71 V to 3.47 V; DVDD and LVDD from internal LDO; All specifications at −40°C to +150°C junction
temperature, unless otherwise noted.









|Table 1. Operating Conditions Parameter|Symbol|Conditions / Comments|Min Typ Max|Unit|
|---|---|---|---|---|
|POWER REQUIREMENTS<br>Digital Core Power Supply<br>Low-voltage Supply<br>Digital Input and Output Power Supply<br>Analog Power Supply<br>Always-on Domain Supply<br>|VDVDD<br>VLVDD<br>1<br>VDVDDIO<br>VAVDD<br>VVBAT<br>|Power supply output. Generated from internal LDO<br>Power supply output. Generated from internal LDO<br>Power supply input. Can be supplied from LVDD1<br>Power supply input<br>Power supply input<br>l|1.1<br>3.05<br>3.3<br>3.45<br>1.71<br>3.47<br>4.75<br>5<br>5.25<br>4.5<br>70|V<br>V<br>V<br>V<br>V|
|POWER ON RESET<br>Exit From Reset<br>Entry Into Reset<br>|VVBAT<br>VAVDD<br>VVBAT<br>VAVDD<br><br><br>|Always-on domain functional<br>All other IC domains functional<br>Independent from AVDD: Complete IC in reset<br>Complete IC in reset excluding always-on domain<br>entia<br> <br>|3.2<br>3.9<br>4.2<br>4.7<br>3.2<br>3.9<br>4.2<br>4.7<br>|V<br>V<br>V<br>V|
|TEMPERATURE<br>Junction Temperature for OTP Programming<br>Junction Temperature<br>|TJ<br>TJ<br><br><br>|nfid<br>tion<br>e|-40<br>+120<br>-40<br>+150<br>|°C<br>°C|
|REFERENCE CLOCK INPUT<br>Transconductance<br>**External Crystal (XTAL)**<br>Crystal Frequency<br>Crystal Frequency Tolerance<br>Crystal Shunt Capacitance<br>Crystal Load Capacitance2<br>Crystal Equivalent Series Resistance (ESR)<br>**External Clock Input (CLK_IN)**<br>Clock Input Frequency<br>Clock Input Frequency Tolerance<br>Clock Input Voltage Range<br>Clock Input Duty Cycle<br>AD|gM<br>CSHUNT<br>CLOAD<br>Rs<br>I C<br>I<br>|Requirements for an external crystal used on XTAL_I/<br>CLK_IN pin and XTAL_O pin<br>Over full temperature range and life-time<br>When driving XTAL_I with an oscillator<br>Over full temperature range and lifetime<br>DC-coupled sine or square wave at XTAL_I/CLK_IN pin<br><br>nforma<br>NDA Requir|6.25<br>25<br>-100<br>+100<br>3<br>12<br>100<br>25<br>-100<br>+100<br>0.8<br>1.1<br>40<br>60<br>|mS<br>MHz<br>ppm<br>pF<br>pF<br>Ω<br>MHz<br>ppm<br>Vp-p<br>%|


1 Maximum 10 mA DC current.


2 Load capacitance _C_ _LOAD_ _= (C1 x C2)/(C1 + C2) + C_ _STRAY_, where _C_ _STRAY_ is the stray capacitance including routing and package parasitics. C1 and C2 are the capacitors


loaded on PCB.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 6 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**ELECTRICAL CHARACTERISTICS**


The digital inputs are 5 V tolerant.


Limited support for 5 V open drain outputs (I [2] C, ISELED and Flexible I/O only).


_**Table 2. Electrical Characteristics**_











|Parameter|Symbol|Conditions / Comments|Min Typ Max|Unit|
|---|---|---|---|---|
|DIGITAL INPUTS<br>Input High Voltage<br>Input Low Voltage<br>Input Pull-up Resistance<br>Input Pull-down Resistance<br>Input Leakage Current|VIH<br>VIL<br>RPU<br>RPD<br>IIN<br>|SAIF[11:0] / OA-SPI1<br>DVDDIO: 2.5 V to 3.3 V<br>DVDDIO: 1.8 V to < 2.5 V<br>DVDDIO = 3.63 V, VPAD = 0 V<br>DVDDIO = 3.63 V, VPAD = 3.63 V<br>DVDDIO = 3.63 V, VPAD = 5.5 V<br>tia|DVDDIO × 0.7<br>DVDDIO × 0.7<br>5.5<br>4.5<br>−0.3<br>DVDDIO × 0.3<br>15<br>30<br>15<br>22<br>30<br>40<br>-2<br>+2<br>l|V<br>V<br>V<br>kΩ<br>kΩ<br>kΩ<br>µA|
|DIGITAL INPUTS<br>WAKE Input Threshold<br>Input Leakage Current|IIN<br>|WAKE<br>Active high<br>Active low2<br>WAKE: 0 V to 70 V<br>iden<br><br>|0.95<br>0.9<br>1<br>1.05<br>1<br>-1<br>+1<br><br> <br>d|V<br>V<br>µA|
|ADC<br>Input Range<br>Input Absolute Error<br>Input Voltage Sensitivity<br>DC Signal Voltage Input<br>Bandwidth<br>ADC Resolution<br>Sample Rate<br>Input Impedance|A|SAIF[5:0]<br>I Conf<br>Informati<br> Req|0<br>3.6<br>±50<br>±8<br>20<br>12<br>500<br>1<br><br><br>uire|V<br>mV<br>mV<br>kHz<br>bit<br>kSPS<br>MΩ|
|TEMPERATURE SENSOR<br>Temperature Range<br>Temperature Accuracy||DA|-40<br>150<br>±20<br><br><br>|°C<br>°C|
|DIGITAL OUTPUTS<br>Output High Voltage<br>Output Low Voltage<br>High Impedance Leakage<br>Current|VOH<br>VOL<br>ILEAK|SAIF[11:0]<br>Load condition = 2 mA<br>EN<br>Load condition = 25 µA<br>SAIF[11:0]<br>Load condition = 2 mA<br>EN<br>Load condition = 250 µA<br>N|DVDDIO – 0.4<br>2.5<br>3.6<br>0.4<br>0.4<br>-2<br>+5<br>|V<br>V<br>V<br>V<br>µA|
|DIGITAL I/O<br>Pin Capacitance|CPIN|SAIF[11:0]|7|pF|
|10BASE-T1S PHY<br>Differential Capacitance<br>Output Signal Swing||ETHP, ETHN<br>Measurement frequency = 10 MHz<br>Driving the 50 Ω differential load|43<br>74<br>0.8<br>1<br>1.2|pF<br>VP-P|


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 7 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


1 AD3300 only.

2 40 mV to 50 mV hysteresis on the WAKE input pin.

3 V CM = 2.5 V, Temp. = +25°C, IC powered.



4 V CM = -5 V to +10 V, Temp. = -40°C to +150°C, IC powered and unpowered.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 8 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**POWER CONSUMPTION CHARACTERISTICS**


_**Table 3. Power Consumption Characteristics**_


**Parameter** **Symbol** **Conditions / Comments** **Min** **Typ** **Max** **Unit**


Battery Power Supply I VBAT 28 40 µA

DVDDIO Current Consumption [1] I DVDDIO The DVDDIO current is determined by a number of
external factors [2]



Analog Power Supply Standby Mode I AVDD 2.3 3 mA

Analog Power Supply Active Mode [3] I AVDD 48 mA

Analog Power Supply Active Mode [4] I AVDD Transmitting 50 mA
Receiving 30 mA

Battery Power Supply Sleep Mode I VBATSleep 28 40 µA



Analog Power Supply Sleep Mode [5] I AVDDSleep 50 µA


1 When sourcing from LVDD, do not exceed the DC current limit of 10 mA.


2 See DVDDIO Current.


3 MAC-PHY with 10 Mbps Ethernet throughput, 15 MHz OA-SPI clock.


4 Remote node.


5 Typically AVDD supply is turned off using EN pin function saving AVDD current when in sleep mode.


**DVDDIO Current**


I DVDDIO is application specific, but is typically dominated by the sum of Output Dynamic Current and Input Dynamic Current:


I DVDDIO = I OD + I ID


The on-chip I/O current I DVDDIO is based on dynamic switching currents on the digital I/O pins.


The dynamic current, due to switching activity on an output pin, is calculated using the following equation:


Output Dynamic Current I OD = C PIN + C L × V DVDDIO × f


Where:


- C PIN = dynamic, transient power dissipation capacitance internal to the transceiver output pins (see Table 2).

- C L = total load capacitance that an output pin sees outside the transceiver.

- V DVDDIO = DVDDIO supply voltage.

- f = frequency of switching on the pin.


The dynamic current, due to switching activity on an input pin, is calculated using the following equation:


Input Dynamic Current I ID = C PIN × V DVDDIO × f


Where:


- C PIN = dynamic, transient power dissipation capacitance internal to the transceiver input pins (see Table 2).

- V DVDDIO = DVDDIO supply voltage.

- f = frequency of switching on the pin.


Further aspects that may need to be taken into account include the contributions due to additional resistive loads (either internal or external
pull-up/pull-down) and any open-drain configuration of output drivers.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 9 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**OPEN ALLIANCE SPI I/O TIMING SPECIFICATIONS**


_**Table 4. OA-SPI Timing Specifications**_


**DVDDIO = 1.8 V** **DVDDIO = 3.3 V**
**Parameter** **Symbol** **Conditions / Comments** **Unit**
**Min** **Max** **Min** **Max**


OPEN Alliance compliant SPI (OA-SPI) OPEN Alliance SPI pins
(SCLK, IRQ, CS, CITO, and COTI)


SCLK Frequency 8 22.5 8 25 MHz

SCLK Frequency Dual mode [1] 8 15 8 15 MHz



SCLK Duty Cycle 25/75 75/25 25/75 75/25 %


CS High Time t 25 SCLK frequency = 15 MHz 120 120 ns


CS Setup Time t 26 SCLK frequency = 15 MHz 17 17 ns



CS Hold Time t 27 SCLK frequency = 15 MHz 17 17 ns


COTI Input Setup Time Before Sample Edge t 28 SCLK frequency = 15 MHz 5 5 ns


COTI Input Hold Time After Sample Edge t 29 SCLK frequency = 15 MHz 5 5 ns


CITO Output Valid (Delay After Drive Edge) t 30 SCLK frequency = 15 MHz 14 12 ns


CITO Output Hold Time After Drive Edge t 31 SCLK frequency = 15 MHz 5 4 ns


CITO Output Disable Time t 32 SCLK frequency = 15 MHz 20 20 ns


CITO Output Valid (Delay After CS Edge) t 33 SCLK frequency = 15 MHz 15 12 ns


1 AD3300 model only.


**CS**







**SCLK**


**COTI**


**CITO**


|Col1|Col2|Col3|
|---|---|---|
||**t**||
||**26**|**26**|
||||






















|o a<br>i<br>C m u<br>t 25 q<br>r<br>I o e<br>t t D<br>26 27 f R<br>A n<br>t t 28 29 I A<br>MSB MSB-1 MSB-2 1 LSB<br>D<br>t 33 t 30 t 31 t 32<br>MSB MSB-1 MSB-2 1 LSB|Col2|t|
|---|---|---|
|**t33**<br>**t28**<br>**t29**<br>**t26**<br>**t25**<br>**t27**<br>**t32**<br>**LSB**<br>**LSB**<br>**1**<br>**1**<br>**MSB-2**<br>**MSB-2**<br>**MSB-1**<br>~~**M**~~**SB**<br>**MSB**<br>**t30**<br>**t31**<br>**MSB-1**<br>ADI Co<br>Informa<br>DA Requi|**t33**<br>**t28**<br>**t29**<br>**t26**<br>**t25**<br>**t27**<br>**t32**<br>**LSB**<br>**LSB**<br>**1**<br>**1**<br>**MSB-2**<br>**MSB-2**<br>**MSB-1**<br>~~**M**~~**SB**<br>**MSB**<br>**t30**<br>**t31**<br>**MSB-1**<br>ADI Co<br>Informa<br>DA Requi|**25**|
|**t33**<br>**t28**<br>**t29**<br>**t26**<br>**t25**<br>**t27**<br>**t32**<br>**LSB**<br>**LSB**<br>**1**<br>**1**<br>**MSB-2**<br>**MSB-2**<br>**MSB-1**<br>~~**M**~~**SB**<br>**MSB**<br>**t30**<br>**t31**<br>**MSB-1**<br>ADI Co<br>Informa<br>DA Requi|**t33**<br>**t28**<br>**t29**<br>**t26**<br>**t25**<br>**t27**<br>**t32**<br>**LSB**<br>**LSB**<br>**1**<br>**1**<br>**MSB-2**<br>**MSB-2**<br>**MSB-1**<br>~~**M**~~**SB**<br>**MSB**<br>**t30**<br>**t31**<br>**MSB-1**<br>ADI Co<br>Informa<br>DA Requi||
|**t33**<br>**t28**<br>**t29**<br>**t26**<br>**t25**<br>**t27**<br>**t32**<br>**LSB**<br>**LSB**<br>**1**<br>**1**<br>**MSB-2**<br>**MSB-2**<br>**MSB-1**<br>~~**M**~~**SB**<br>**MSB**<br>**t30**<br>**t31**<br>**MSB-1**<br>ADI Co<br>Informa<br>DA Requi|**t**|**t**|
|**t33**<br>**t28**<br>**t29**<br>**t26**<br>**t25**<br>**t27**<br>**t32**<br>**LSB**<br>**LSB**<br>**1**<br>**1**<br>**MSB-2**<br>**MSB-2**<br>**MSB-1**<br>~~**M**~~**SB**<br>**MSB**<br>**t30**<br>**t31**<br>**MSB-1**<br>ADI Co<br>Informa<br>DA Requi|**27**|**27**|



_**Figure 4. OPEN Alliance 10BASE-T1x MAC-PHY Serial Interface Timing**_


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 10 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**SAIF I/O TIMING SPECIFICATIONS**


**Note:** All output timings are derived from an internal 100 MHz clock (10 ns period). Accuracy of output timings is optimized using periods or bit
times being a multiple of 10 ns.


**Note:** Higher frequencies may require the highest drive strength setting depending on the system design.


**SAIF Interfaces Timing Specifications**











|Table 5. SAIF Timing Specifications Parameter|Symbol|Conditions / Comments|Min Typ Max|Unit|
|---|---|---|---|---|
|TS_CAPT<br>Pulse Width<br>TS_TIMER<br>Period<br>Period Error1<br>Jitter Error2<br>Jitter Error3<br>Jitter Error4<br>||idential<br>on<br>|80<br>32<br>8,589,934,560<br>0<br>-2<br>2<br>-12<br>12<br>-25<br>25<br>|ns<br>ns<br>ns<br>ns<br>ns<br>ns|
|SAIF = UART<br>Baud Rate<br>Baud Rate Error<br>Baud Rate Error<br>|I C<br><br>|SAIF[11:0] configured for UART interface<br>(UART_RX and UART_TX)<br>For standard baud rates in the supported<br>range up to 921600 bps<br>For standard baud rates above 921600 bps<br>onf<br>ormati<br>equir|600<br>6250000<br>-1<br>1<br>-2<br>2<br>|bps<br>%<br>%|
|SAIF = PWM<br>Frequency Range<br>Frequency Accuracy<br>Frequency Jitter<br>Duty Cycle<br>Duty Cycle Resolution<br>Duty Cycle Accuracy<br>Duty Cycle Jitter<br>A|I<br>|SAIF[11:0] configured for pulse width<br>modulation interface (PWM[11:0])<br><br>nf<br>NDA R|0.1<br>1.0x106<br>2000<br>15000<br>3000<br>15000<br>0<br>100<br>0.78125<br>4000<br>15000<br>3000<br>15000<br>|Hz<br>ppm<br>ppm<br>%<br>%<br>ppm<br>ppm|
|SAIF = Clock Generator<br>Frequency Range<br>Frequency Accuracy<br>Frequency Jitter<br>Duty Cycle||SAIF[11:0] configured for clock generation mode<br>Fixed frequencies from look-up table|0.25<br>25<br>10<br>200<br>1<br>45/55<br>50/50<br>55/45|MHz<br>ppm<br>ns<br>%|
|SAIF = LIN Controller<br>Bit Rate||SAIF[11:0] configured for LIN interface<br>(LIN_EN, LIN_TXD, LIN_RXD)|1<br>20|kbps|
|SAIF = ISELED / ILaS5<br>Bit Width (Downstream)<br>Bit Width (Upstream)|tBW_DS<br>tBW_US|SAIF[11:0] configured for INOVA Semiconductors<br>compatible ISELED or ILaS interface|500<br>384<br>714|ns<br>ns|


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 11 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


_**Table 5. SAIF Timing Specifications (Continued)**_


**Parameter** **Symbol** **Conditions / Comments** **Min** **Typ** **Max** **Unit**


Frame Downstream t Frame CRC enabled 80 x t BW


CRC disabled 70 x t BW


Frame Synchronization t Frame_S 15 x t BW

Frequency Synchronization t Freq_S 5 x t BW


Service Data Unit Downstream t SDU 50 x t BW


1 Linked to gPTP grandmaster clock when gPTP functionality is used.

2 TS_TIMER_HI + TS_TIMER_LO Period = Multiples of 80 ns. For example 80 ns, 160 ns, 240 ns.



3 TS_TIMER_HI + TS_TIMER_LO Period = Multiples of 32 ns.

4 TS_TIMER_HI + TS_TIMER_LO Period - QE_CORR = All other integer values which are non-multiples of 32 ns or 80 ns.

5 Only available on AD3304/5 product models.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 12 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**SPI Controller Mode Timing Specifications**


**Note:** Clock switching characteristics require a period based on a multiple of 10 ns.


**Note:** Accuracy is improved when using a half-period being a multiple of 10 ns.





|Table 6. SPI Controller Mode Timing Specifications Parameter|Symbol|Conditions / Comments|Min Typ Max|Unit|
|---|---|---|---|---|
|SAIF = SPI Controller||SAIF[11:0]configured for SPI Controller Mode<br>(SCLK,~~ CS~~n1, COTI and CITO)|||
|Timing Requirements<br>Data Input Setup Time Before SCLK Edge<br>Data Input Hold Time After SCLK Edge<br>|tDSU<br>tDHD<br>|DVDDIO = 3.3 V<br>DVDDIO = 3.3 V<br>|5<br>10|ns<br>ns|
|Switching Characteristics<br>SCLK Frequency<br>CS Setup Time Before SCLK Edge<br>CS Hold Time After SCLK Edge<br>LOW Period of the SCLK5<br>HIGH Period of the SCLK5<br>Data Output Valid After SCLK Edge<br>Data Output Setup Time Before SCLK Edge<br>Data Output Fall Time<br>Data Output Rise Time<br>SCLK Rise Time<br>SCLK Fall Time<br>|fSCLK<br>tCS<br>tSFS<br>tSL<br>tSH<br>tDAV<br>tDOSU<br>tDF<br>tDR<br>tSR<br>tSF<br>Co<br><br>|nfidential<br>rmation<br>quired|0.1<br>20<br>See2<br>See3<br>See4<br>18.5<br>18.5<br>±8<br>0<br>2.5<br>2.5<br>2.4<br>2.4<br>|MHz<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns<br>ns|


1 n = up to 8, default: active low, polarity configurable.

2 CSB_TO_SCLK −1 × BAUD_RATE_PERIOD .


3 INTERBYTE_SPACING × 10ns + SCLK_TO_CSB −1 × BAUD_RATE_PERIOD .


4 INTERBYTE_SPACING × 10ns + ceil [550ns ] BAUD_RATE_PERIOD × BAUD_RATE_PERIOD .


5 The final SCLK period in a SPI transaction may be substantially longer than nominally expected.


**CS**







**SCLK**
**(POLARITY = 0)**


**SCLK**
**(POLARITY = 1)**


**COTI**


**CITO**













**t** **DSU** **t** **DHD**


_**Figure 5. SPI Controller Mode Timing (Phase Mode = 1)**_


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 13 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**CS**







**SCLK**
**(POLARITY = 0)**


**SCLK**
**(POLARITY = 1)**


**COTI**


**CITO**


|tCS<br>tDOSU|Col2|tSFS|
|---|---|---|
|**tDOSU**<br>**t**~~**CS**~~ <br>|**MSB**<br>|**MSB**<br>|
|**tDOSU**<br>**t**~~**CS**~~ <br>|||



**t** **DSU** **t** **DHD**

|Col1|MSB IN|Col3|i<br>t<br>n<br>BITS[6:1] LSB IN|
|---|---|---|---|
||**MSB IN**<br><br><br><br>|||



_**Figure 6. SPI Controller Mode Timing (Phase Mode = 0)**_









**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 14 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**I** **[2]** **C Controller Mode Timing Specifications**


_**Table 7. I**_ _**[2]**_ _**C Controller Mode Timing Specifications**_


**Standard Mode** **Fast Mode** **Fast Mode Plus**
**Parameter** **Symbol** **Conditions / Comments** **Unit**
**Min** **Max** **Min** **Max** **Min** **Max**


SAIF = I [2] C Controller [1] SAIF[10:9] configured for I [2] C

Controller Mode (SDA and SCL).

Drive-strength = 20 mA,

and DVDDIO = 3.3 V required


Serial Clock (SCL) Frequency f SCL 0 100 0 400 0 1000 kHz



Hold Time (Repeated) START Condition t HD;STA After this period, the first clock pulse

is generated



4.0 0.6 0.26 μs



LOW Period of SCL t LOW 4.7 1.3 0.5 μs


HIGH Period of SCL t HIGH 4.0 0.6 0.26 μs


Set-up Time for a Repeated START Condition t SU;STA 3.25 0.6 0.26 μs


Data Hold Time t HD;DAT 0 0 0 μs


Data Set-up Time t SU;DAT 250 100 50 ns



Rise Time of Both SDA and SCL Signals t r



2
105 1000 105 300 105 120 ns



Fall Time of Both SDA and SCL Signals t f 300 300 120 ns


Set-up Time for STOP Condition t SU;STO 2.9 0.37 0.23 μs



Bus Free Time Between a STOP and START


Condition



t BUF 4.7 1.3 0.5 μs



Data Valid Time t VD;DAT 3.45 0.9 0.45 μs


Data Valid Acknowledge Time t VD;ACK 3.45 0.9 0.45 μs


1 Clock stretching is not supported after the ACK-bit and immediately before STOP condition.

2 Minimum rise time must be guaranteed by system implementation considering pull-up resistors and bus capacitance:


t r = 0 . 8473 × C b × R p .


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 15 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**



**SCL**





**cont.**


**cont.**




|Col1|tf|Col3|tr tSU;DAT|Col5|Col6|
|---|---|---|---|---|---|
||**70 %**<br>**30 %**||||**tHIGH**<br>**tVD;DAT**<br><br><br>**70 %**<br>**30 %**|
|||||||
||**tHD;STA**|**tHD;STA**||||
||**tHD;STA**|**tHD;STA**||||
||**S**|**S**|**1/fSCL**<br><br>|**1/fSCL**<br><br>|**1/fSCL**<br><br>|





**SDA**


**SCL**



**1** **[st]** **clock cycle**



**S** **r** **P** **S**
**9** **[th]** **clock**


|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**tSU;STA**<br><br>**L**||||||
|**tSU;STA**<br><br>**L**||||**t**<br>|**t**<br>|
|**tSU;STA**<br><br>**L**||**Sr**<br>|**Sr**<br>|**Sr**<br>|**Sr**<br>|


|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
||**P**<br>|||**S**|**S**|



_**Figure 7. I**_ _**[2]**_ _**C Controller Mode Timing**_


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 16 of 33**


## Data Sheet AD3300/1/4/5

**SPECIFICATIONS**


**SYSTEM SPECIFICATIONS**


_**Table 8. System Specifications**_


**Parameter** **System Specification**


System EMI/EMC Meets or exceeds industry specifications for robustness (ISO 11452-2, ISO 11452-4, ISO 7637-3, ISO7637-2, SAEJ2962-3) and emissions
(CISPR25, SAEJ2962-3)



System ESD Rating Meets ISO 10605 severity levels (±12 kV) on the 10BASE-T1S interface without any external ESD protection


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 17 of 33**


## Data Sheet AD3300/1/4/5

**ABSOLUTE MAXIMUM RATINGS**



_**Table 9. Tolerant Voltage on Digital I/O Pins for Different Power Supplies**_


**Voltage** **Minimum DVDDIO** **Maximum digital I/O voltage**


3.3 V operation 2.97 V 5.5 V


0 V 3.63 V


2.5 V operation 2.25 V 5.5 V


0 V 3.63 V


1.8 V operation [1] 1.62 V 4.5 V


0 V 3.63 V


1 Not tolerant to 5 V input voltage.




- _θ_ JMA is the junction to ambient thermal resistance in moving air.

- _θ_ JB is the junction to board thermal resistance.

- _θ_ JC is the junction to case thermal resistance.

- _Ψ_ _JT_ is the junction to top thermal characterization parameter.

- _Ψ_ _JB_ is the junction to board thermal characterization parameter.


_**Table 11. Thermal Resistance**_


**Parameter** **Unit** **Air flow conditions**


**No airflow** **1 m/s** **2 m/s** **3 m/s**


_**θ**_ **JA** **(°C/W)** **70.8** **[ 1]** **56.1** **[ 4]** **53.6** **[ 4]** **52.0** **[ 4]**



_**Table 10. Absolute Maximum Ratings**_


**Parameter** **Rating**


DVDDIO to GND 3.63 V


AVDD to GND 5.5 V


VBAT to GND 70 V


WAKE to GND 70 V


XTAL_I/CLKIN to GND -0.3 V to +1.8 V


XTAL_O to GND -0.3 V to +1.35 V

ETH_P/ETH_N (Common Mode) [1] ±20 V


Storage temperature range −60°C to +150°C


Solder reflow, per JEDEC J-STD-020 260°C


Junction temperature while biased −40°C to +150°C


1 Maximum ETH_P/ETH_N receiver common mode DC offset. The ETH_P/

ETH_N transmitter should not be enabled if driving into a low impedance DC

load. This can result in device damage.


Stresses at or above those listed under Absolute Maximum Ratings
may cause permanent damage to the product. This is a stress
rating only; functional operation of the product at these or any other
conditions above those indicated in the operational section of this
specification is not implied. Operation beyond the maximum operating conditions for extended periods may affect product reliability.


**THERMAL RESISTANCE**


Thermal performance is directly linked to the printed circuit
board (PCB) design and operating environment. Careful attention to
PCB thermal design is required.


The thermal characteristics provided in this section are provided for
package comparison and estimation purposes only. They are not
intended for accurate system temperature calculation. Thermal simulation is required for accurate temperature analysis that accounts
for all the impacts of each specific 3D system design, including, but
not limited to other heat sources, the use of heat-sinks, and the
system enclosure.


Thermal data is generated according to the JEDEC JESD51 series
of specifications:


- _θ_ JA is the junction to ambient thermal resistance in natural
convection.



_θ_ JB2 (°C/W) 38.9   -   -   
_θ_ JC3 (°C/W) 51.7   -   -   

**1.** Simulated data based on JEDEC 2s2p thermal test board with
4 thermal vias under the exposed paddle in a JEDEC Natural
Convection environment.

**2.** Simulated data based on JEDEC 2s2p thermal test board with 4
thermal vias under the exposed paddle in a JEDEC Junction To
Board environment.

**3.** Simulated using a JEDEC 1s thermal test board with a cold
plate attached to the package top and measured at the package
top surface.
**4.** Simulated data based on JEDEC 2s2p thermal test board with
4 thermal vias under the exposed paddle in a JEDEC Forced
Convection environment.


When using the device, the _T_ JMAX must not go above 150°C. The
following equation calculates the junction temperature using the
measured package surface temperature and applies only when not
using a heat sink on the DUT:


_T_ _J_ = _T_ _S_ + ( _Ψ_ _JT_ × _W_ _TOTAL_ ).


Where: _T_ _J_ is the junction temperature of the DUT. _T_ _S_ is the package
surface temperature (°C). _W_ _TOTAL_ is the total power consumption of
the DUT.


_W_ _TOTAL_ = ((VBAT × _I_ _VBAT_ ) + ( _DVDDIO_ × _I_ _DVDDIO_ ) + (AVDD × _I_ _AVDD_ ).


Values of _θ_ JA are provided for package comparison and PCB
design considerations. Use _θ_ JA for a first-order approximation of _T_ J
by the following equation:


_TJ_ = _T_ _A_ + (θ _JA_ × _W_ _TOTAL_ ).


Where _T_ _A_ = ambient temperature (°C).


**ELECTROSTATIC DISCHARGE (ESD) RATINGS**


The following ESD information is provided for handling of ESD-sensitive devices in an ESD-protected area only. Human body model
(HBM) ratings are per ANSI/ESDA/ JEDEC JS-001.



_Ψ_ JT1 (°C/W) 2.4 - - 
_Ψ_ JB1 (°C/W) 37.6 - - 


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 18 of 33**


## Data Sheet AD3300/1/4/5

**ABSOLUTE MAXIMUM RATINGS**


Field induced charged device model (FICDM) ratings are per ANSI/ESDA/JEDEC JS-002.


_**Table 12. AD3300/AD3301/AD3304/AD3305, 24-lead [LFCSP] – ETH_P, ETH_N**_
_**pins**_


**ESD Model** **Withstand Threshold (V)** **Class**


HBM [1] ±8 k 2


1 HBM level is relative to GND paddle reference.


_**Table 13. AD3300/AD3301/AD3304/AD3305, 24-lead [LFCSP]**_


**ESD Model** **Withstand Threshold (V)** **Class**



HBM ±2.5 k 2


FICDM ±500 C2a



**ESD CAUTION**


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 19 of 33**


## Data Sheet AD3300/1/4/5

**PIN CONFIGURATION AND FUNCTION DESCRIPTIONS**



**NOTES**

**1. EXPOSED PAD IS THE ONLY ELECTRICAL**

**GROUND. SOLDER THE EXPOSED**

**PAD TO AN EXTERNAL GROUND PLANE**

**UNDERNEATH THE IC FOR THERMAL**

**DISSIPATION.**





18 AVDD

17 ETH_P
16 ETH_N
15 WAKE

14 EN

13 VBAT





_**Figure 8. AD3301/4/5 Pin Configuration**_



**NOTES**

**1. EXPOSED PAD IS THE ONLY ELECTRICAL**

**GROUND. SOLDER THE EXPOSED**

**PAD TO AN EXTERNAL GROUND PLANE**

**UNDERNEATH THE IC FOR THERMAL**

**DISSIPATION.**





18 AVDD

17 ETH_P
16 ETH_N
15 WAKE

14 EN

13 VBAT



_**Figure 9. AD3300 Dual Mode Pin Configuration**_


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 20 of 33**


## Data Sheet AD3300/1/4/5

**PIN CONFIGURATION AND FUNCTION DESCRIPTIONS**


_**Table 14. AD3300/AD3301/AD3304/AD3305 Pin Function Descriptions**_


**Pin No** **Mnemonic** **Type** **Description**


1 SAIF6/CS Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.
Also serves as SPI chip select (CS) input (active low) when OA-SPI interface is enabled. [1]

**Note:** Optional: 10 kΩ pull-up resistor.


2 SAIF5/IRQ Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.
Also serves as interrupt output when OA-SPI interface is enabled. [1]


3 DVDD Power Decoupling for the internally generated digital core power supply (1.1 V).
Requires a 10 nF and 1 μF decoupling capacitor.



4 SAIF4/SCLK Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.
Also serves as SPI serial clock (SCLK) input when OA-SPI interface is enabled. [1]

**Note:** Optional: 10 kΩ pull-down resistor.


5 SAIF3 Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.


6 LVDD Power Decoupling for the internally generated 3.3 V, regulated from AVDD, and used to power the analog logic. LVDD can
be used to drive DVDDIO at 3.3 V and / or to source an off-chip supply if desired. The DC current in total (DVDDIO +
off-chip) that can be supplied from this pin is 10 mA.
Requires a 100 nF and 2.2 μF decoupling capacitor.


7 DVDDIO Power Separate supply for the I/O circuitry, to allow the digital I/O level to be controlled as suits the application. It can run from
1.8 V to 3.3 V.

Requires a 100 nF and 4.7 μF decoupling capacitor.


8 SAIF2/ Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.
TS_CAPT Also serves as input for the synchronized timer to trigger the capture of a timestamp when OA-SPI interface is enabled

(optional). [1]


DNC when not used.


9 SAIF1/ Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.
TS_TIMER Also serves as the output of the synchronized timer when OA-SPI interface is enabled (optional). [1]


DNC when not used.


10 SAIF0 Digital input/output Multipurpose input/output pin used for the sensor/actuator interface.


11 XTAL_O Analog output Crystal amplifier (25 MHz) output pin.


12 XTAL_I Analog input Crystal amplifier (25 MHz) input pin. Direct clock reference (25 MHz) input pin.


13 VBAT Power Supply input for the always-on domain. It can connect to 5 V or battery supply.
Requires a filter network (100 Ω resistor and 10 μF capacitor) that prevents damage or malfunction during electrical

events or electrical event testing. An additional 100 nF capacitor can be used for improved noise immunity.


14 EN Digital output An output pin is asserted when the 10BASE-T1S transceiver is in an Awake mode (see Operating Modes); it can be
used as an active-high enable or an active-low inhibit. For example, for an external DC/DC regulator generating the
AVDD supply. Always driven, DNC or connect to a test point when not used.
**Note:** It is not recommended to pull this pin to GND using a resistor. Ensure load not exceeding the driving capability of

this pin (see Table 2).


15 WAKE Digital input Input that can be used for an external device to trigger the 10BASE-T1S transceiver to exit the sleep mode. WAKE is
triggered by a positive edge > 1 V. Default: disabled.
**Note:** Optional: 10 kΩ pull-down resistor. Do not leave floating/unconnected. Short to GND when not used. When

connecting externally (off-PCB), the pin will need an off-chip filter for EMI protection).


16 ETH_N Analog input/output 10BASE-T1S negative differential pin.
**Note:** Differential signal, symmetric design.


17 ETH_P Analog input/output 10BASE-T1S positive differential pin.
**Note:** Same as ETH_N.


18 AVDD Power 5 V supply input; it can be powered off when the 10BASE-T1S transceiver is not in an Awake mode (see Operating
Modes) to save power.
Requires a 100 nF and 4.7 μF decoupling capacitor.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 21 of 33**


## Data Sheet AD3300/1/4/5

**PIN CONFIGURATION AND FUNCTION DESCRIPTIONS**


_**Table 14. AD3300/AD3301/AD3304/AD3305 Pin Function Descriptions (Continued)**_


**Pin No** **Mnemonic** **Type** **Description**


19 TEST Digital input Short to GND.

**Note:** Do not leave floating/unconnected.


20 SAIF11 Digital input/output Multipurpose input/output pin used for sensor/actuator interface.

21 SAIF10 Digital input/output Multipurpose input/output pin used for sensor/actuator interface.

Pull pin high or low with an external resistor to set bit3 of the MAC address and/or PLCA ID [2] . Pin level must remain

steady until the initial SW configuration is complete and the MAC address and/or PLCA ID is stored.

Supports true open drain functionality (increased drive strength and inbuilt I [2] C glitch filter on the input side) for I [2] C

compatibility.



**Note:** Add weak pulling resistors to enable override, for example,100 kΩ.


22 SAIF9 Digital input/output Multipurpose input/output pin used for sensor/actuator interface.

Pull pin high or low with an external resistor to set bit2 of the MAC address and/or PLCA ID [2] . Pin level must remain

steady until the initial SW configuration is complete and the MAC address and/or PLCA ID is stored.

**Note:** Add weak pulling resistors to enable override, for example, 100 kΩ.

Supports true open drain functionality (increased drive strength and inbuilt I [2] C glitch filter on the input side) for I [2] C

compatibility.


23 SAIF8/COTI Digital input/output Multipurpose input/output pin used for sensor/actuator interface.

Pull pin high or low with an external resistor to set bit1 of the MAC address and/or PLCA ID [2] . Pin level must remain

steady until the initial SW configuration is complete and the MAC address and/or PLCA ID is stored.

**Note:** Add weak pulling resistors to enable override, for example, 100 kΩ.

Also serves as SPI COTI (controller output target input) signal when OA-SPI interface is enabled. [1]

**Note:** Optional: 10 kΩ pull-down resistor.


24 SAIF7/CITO Digital input/output Multipurpose input/output pin used for sensor/actuator interface.

Pull pin high or low with an external resistor to set bit0 of the MAC address and/or PLCA ID [2] . Pin level must remain

steady until the initial software configuration is complete and the MAC address and/or PLCA ID is stored.

**Note:** Add weak pulling resistors to enable override, for example, 100 kΩ.

Also serves as SPI CITO (controller input target output) signal when OA-SPI interface is enabled. [1]

**Note:** Optional: 33 Ω series resistor at the source side of the signal.


EXP_PAD GND Ground Exposed paddle. Connect to ground.


Any SAIF can be left unconnected. The pins are three-stated when not enabled in pin multiplexing.


All other pins must be connected as per the description.


1 AD3300 only

2 The 4 LSBs of the PLCA ID is determined by sampling those pins and then providing the value using a look-up table (LUT). By default (unprogrammed OTP), the PLCA ID's

are 1:1 (matching the MAC address LSBs). If a different PLCA ID mapping is needed, the OTP LUT must be programmed accordingly.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 22 of 33**


## Data Sheet AD3300/1/4/5

**DESIGNER REFERENCE**



The following sections provide information on typical power configurations as well as board layout guidelines.


**POWER CONFIGURATIONS**


There are two power configurations to consider for the AD3300/
AD3301/AD3304/AD3305 transceiver: battery power and 5 V pow
er.


In the battery power configuration, the following attributes must be
considered:



**LAYOUT GUIDELINES**




- Application of UVLO and OVLO thresholds are disabled by
default from boot.


- UVLO and OVLO thresholds can be programmed into OTP for
end use and applied upon boot.

- The battery supply feeds the VBAT pin of AD3300/AD3301/
AD3304/AD3305 and powers the DC/DC regulator.

- AD3300/AD3301/AD3304/AD3305 always-on domain is kept
powered via the VBAT pin.

- Always-on domain enables sleep/wake-up functions.

- AD3300/AD3301/AD3304/AD3305 can monitor the VBAT voltage
level for over voltage (OV) and under voltage (UV) events.

- AD3300/AD3301/AD3304/AD3305 can decide whether or not to
enter the sleep mode thereby disabling the DC/DC regulator 5 V
output.



The layout of the AD3300/AD3301/AD3304/AD3305 10BASE-T1S
transceiver devices must be executed in line with the following
specific requirements. These requirements are critical for systems
aiming to achieve compliance with automotive EMC standards.
Further to these specific requirements, best layout practices should
always be followed. The following figure shows the placement
of the 10BASE-T1S network components like the common-mode
choke and AC-coupling capacitors.


_**Figure 12. T1S Termination Network and Connectors, Combined View**_


**10BASE-T1S Connector Pinout Guidelines**


The following points should be considered for the 10BASE-T1S
connector pinout:


- The connector pitch (distance between the pair of pins) should
be between 2 mm and 4 mm. A higher pitch than 4 mm and / or
additional untwist of the cable causes high impedance mismatch.

- Spare pins around Ethernet pins are recommended; at least one
pin on both sides.

- If power/ground wire to the node is also on the same row, it is
recommended to place those wires at least 2-pins away.

- On two-row connectors, the pins under ETH pair can be another
ETH pair (for example daisy-chain).

- Another balanced differential bus can also be used.


- Do not connect single-ended signals on these pins (for example
ground, power or LIN).

- In the case of daisy chain implementation at the connector level
for the same Ethernet PHY, vertical cascading is recommended.

- Immediate adjacent horizontal cascading of 2-pairs should be
avoided, this will lead to imbalance and asymmetry. When not
possible otherwise, one-pin spacing should be respected, maintaining symmetry.

- In case of two Ethernet PHYs on the same ECU, two Ethernet
signal pairs can be cascaded vertically, below each other. If
placed horizontally, it is recommended to have one empty pin
between the Ethernet signal pairs.


|Col1|VBAT_PROTECTED|Col3|
|---|---|---|
||**VBAT_PROTECTED**<br><br><br>||










|A n<br>I<br>VBAT VIN D<br>EN EN<br>N<br>AD330x DC/DC<br>5 V<br>WAKE AVDD VOUT|Col2|Col3|n|Col5|
|---|---|---|---|---|
|**AD330x**<br>**VBAT**<br>**EN**<br>**AVDD**<br>**WAKE**<br>**DC/DC**<br>**VIN**<br>**EN**<br>**VOUT**<br>**5 V**<br>A<br>In<br>ND|**AD330x**<br>**VBAT**<br>**EN**<br>**AVDD**<br>**WAKE**<br>|**DC/DC**<br>**VIN**<br>**EN**<br>**VOUT**<br><br>I<br>ND|**DC/DC**<br>**VIN**<br>**EN**<br>**VOUT**<br><br>I<br>ND|**DC/DC**<br>**VIN**<br>**EN**<br>**VOUT**<br><br>I<br>ND|
||||||
||||||



_**Figure 10. Battery Power Configuration**_


In the 5 V power configuration figure, the 5 V rail feeds both the
VBAT and AVDD pins. VBAT monitoring is not supported.














|Col1|VBAT<br>EN<br>AD330x<br>WAKE AVDD|
|---|---|
|||
|||



_**Figure 11. 5 V Power Configuration**_



**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 23 of 33**


## Data Sheet AD3300/1/4/5

**DESIGNER REFERENCE**




- There should not be any flooding/pours (ground, power or other)
in the area of the connector pin courtyard. This rule is applicable
for all layers, if the connector is a through-hole part.

- Track/trace the signals Ethernet P, Ethernet N, power, and
ground, but no flooding is wanted.

- AD3300/AD3301/AD3304/AD3305 reference hardware uses a
through hole NanoMQS connector by TE. The connector choice



should consider RF parameters effecting the link segment:
CIDM, Intra pair skew, Insertion Loss, Return Loss, LCL,
LCTL, ANEXT, AFEXT. The 10BASE-T1S System Implementation Specification and the IEEE Std 802.3-2022 Specification
refers to ECU connectors for 10BASE-T1S interfaces.



**NOT RECOMMENDED**





**NOT RECOMMENDED** **NOT RECOMMENDED** **NOT RECOMMENDED** **RECOMMENDED**


**ACCEPTABLE** **RECOMMENDED** **RECOMMENDED**



**RECOMMENDED**



**RECOMMENDED**



**NOT RECOMMENDED** **NOT RECOMMENDED** **ACCEPTABLE** **RECOMMENDED** **RECOMMENDED**


_**Figure 13. Connector Pinout Guidelines Summary Diagram**_



**Passive Device Placement and Layout**


Place decoupling capacitors for any power pin on the same side
of the PCB as the transceiver with the smaller capacitor closest to
the respective pin. The following figure shows the placement of the
AD3300/AD3301/AD3304/AD3305 power decoupling components.


_**Figure 14. Power decoupling components**_


**Common-Mode Choke Parasitic Capacitance**


The following points should be considered for the board design:


- Refer to Open Alliance CMC specification

- The parasitic capacitance between the common mode choke
and adjacent ground planes must be minimized to ensure that
the common-mode choke rejects common-mode noise across
the specified frequency range.




- High speed layout techniques should be used to minimize the
parasitic capacitance of the landing pads and the choke’s body
to the ground plane below the component.

- Minimizing parasitic capacitance supports the goal of maximizing
the differential bandwidth with minimum insertion loss.


- Use ground relief in the ground plane underneath the choke for
reducing parasitic capacitance to ground.


**Power Supply Requirements**


For specific power supply values, see the Power Consumption
Characteristics. The general rules for managing the power supply

are:


- The requirements for the AD3300/AD3301/AD3304/AD3305
power supply pin filtering are found in the Bill of Material
(BoM).The passive components (termination resistors and accoupling capacitors) must be sized to adequately handle BCI
events.


- Ensure that the digital and analog power supplies are isolated
to minimize potential coupling paths between the noisy and
sensitive power supplies.

- Employ double vias if possible, when connecting AD3300/
AD3301/AD3304/AD3305 supplies to minimize the supply inductance. In situations where this is not possible, analog supplies
take priority.


**General Layout Guidelines**


Taking the previously outlined slots into account, take care to ensure the voids in any plane are not large enough to unintentionally
disrupt the path for power and/or return currents, on the plane. The
following figure shows an example of a situation to avoid.



**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 24 of 33**


## Data Sheet AD3300/1/4/5

**DESIGNER REFERENCE**


                     - Match any vias in the signal route with the same impedance of
the signal line. Typical target 50 Ω impedance.

                     - When placing signal vias, it is recommended to place ground, or
return, vias close by in order to provide a short path to ground.


_Plane Notes_



_**Figure 15. Unintentional Disrupted Power Plane**_


_General Requirements_


- The AD3300/AD3301/AD3304/AD3305 contains a common
ground thermal exposed pad. The exposed pad must be connected directly to a solid, contiguous ground plane through a
thermal via array.

- Carefully consider the return currents for signals on the PCB and
simplify their path using techniques such as employing planar
capacitors and using stitching vias.


_Component Placement Notes_


- Ideally, place common mode choke, AC coupling caps and termination on the same side of the PCB as the AD3300/AD3301/
AD3304/AD3305 device.


- Keep decoupling caps close and on same the side of the PCB as
the AD3300/AD3301/AD3304/AD3305 device.


- Keep crystal resonator close and on the same side of the PCB
as the AD3300/AD3301/AD3304/AD3305 device.


_DUT Area_


- For proper thermal management, the AD3300/AD3301/AD3304/
AD3305 device must have its ground paddle connected to a
continuous PCB ground plane.

- Use stitching into internal layers to sink heat (9 vias – 3 x 3).


_Performance Requirements_


- Each single-ended Ethernet signal trace has impedance control
of 50 Ω. The preferred option for optimal EMC performance is
stripline routing but microstrip routing may also be used. Refer to
the Altium Guidelines for more information.


_Routing Notes_


- Ethernet P and Ethernet N: Reduce stub length as much as
possible.

- Ethernet P and Ethernet N: On the trace routing try to minimize
single ended and differential capacitance.

- Length match Ethernet P and Ethernet N. Try not to introduce
imbalance in length and also imbalance in coupling to neighboring nets/potentials. To match the trace lengths, different routing
techniques can be used. It is recommended to apply those
techniques on the same end of the length-matched pair.




- AD3300/AD3301/AD3304/AD3305 reference hardware has implemented a copper ground plane void underneath the common
mode choke (three layers deep).

- The internal ground layer reference immediately below the common-mode choke which is on an external layer should have
an area of ground cut-out that matches the dimension of the
courtyard of the common-mode choke.


**ELECTROMAGNETIC COMPATIBILITY (EMC)**


This section provides information on EMC performance.


Information on the exact testing methods and results are available
in a comprehensive EMC report, which is available on request from
a local Analog Devices sales team or Analog Devices sales office.
The transceiver features that influence the EMC performance are
listed below.


|Table 15. Device Features for EM Block matio equire|MC Performance Emissions Aid e|Immunity Aid|
|---|---|---|
|Differential signaling<br><br><br>|Yes<br>|Yes|
|10BASE-T1S link encoding<br><br><br>|Yes<br>|Yes|


|Table 15. Device Features for EM Block Differential signaling 10BASE-T1S link encoding Termination scheme: matio A Require|MC Performance Emissions Aid Yes Yes e|Immunity Aid Yes Yes|
|---|---|---|
|Common-mode choke<br><br><br>|Yes<br>|Yes|
|On-chip ESD protection<br><br><br>|No<br>|Yes|



**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 25 of 33**


## Data Sheet AD3300/1/4/5

**POWER SUPPLY REQUIREMENTS**



**OPERATING MODES**


The operating modes of the AD3300/AD3301/AD3304/AD3305 are
the always-on reset (initial state), awake (reset, normal, and standby), sleep, and lockout.


Always-on reset mode is triggered when VBAT reset threshold is
asserted. The IC is in reset in always-on reset mode.



Sleep mode is a very low power state. Only the always-on circuitry,
including the sleep/wake-up controller, is powered.



In reset mode all circuitry is in a power down or reset state apart
from the always-on circuitry. Reset mode is the initial awake state.
In this mode all SAIF are in tri-state.


Normal mode is the default mode of operation. The AD3300/
AD3301/AD3304/AD3305 is fully functional in this mode, able to
activate any functional feature and to interact with all interfaces
connected to it.


Standby mode keeps the AD3300/AD3301/AD3304/AD3305 awake
with all circuitry powered but biased for low activity. The benefit
versus sleep mode is much faster boot time to normal mode.


**AWAKE MODES**



Lockout mode is reached when UVLO or OVLO VBAT thresholds are asserted. This mode puts the AD3300/AD3301/AD3304/
AD3305 in a low power state, regardless of the awake mode
the AD3300/AD3301/AD3304/AD3305 is in. Once the UVLO or OVLO condition has been de-asserted, the AD3300/AD3301/AD3304/
AD3305 returns to the awake mode initial state of reset. If during
lockout mode, the VBAT RESET threshold is asserted, this will
put the AD3300/AD3301/AD3304/AD3305 in always-on reset mode.
The wake-up controller is not active in lockout mode.


**Note:** The EN output pin is asserted when the AD3300/AD3301/
AD3304/AD3305 is in an awake mode.


**START**























_**Figure 16. Operating Mode State Diagram**_



**POWER-UP SEQUENCE**


There are no power-up sequence requirements between the VBAT,
AVDD, and DVDDIO supply when using up to 3.3 V I/O supply.


When using 5 V I/O logic, the DVDDIO supply must be >2.5
V before any 5 V logic signal is driven into the AD3300/AD3301/



AD3304/AD3305 device. This also applies to when the DVDDIO
supply is being powered from LVDD 3.3 V supply. Failure to do this
will exceed the absolute maximum ratings of the AD3300/AD3301/
AD3304/AD3305 device.


XTAL_I input must be present no later than 0.5 s after power-on.



**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 26 of 33**


## Data Sheet AD3300/1/4/5

**POWER SUPPLY REQUIREMENTS**



**Note:** Ensure that AVDD supply can handle 120 mA of in-rush
current on start-up.


**POWER-DOWN SEQUENCE**



>2.5 V as long as 5 V I/O signals are driven into the AD3300/
AD3301/AD3304/AD3305 digital inputs.



There are no power-down sequence requirements between the
VBAT, AVDD, and DVDDIO supply. DVDDIO supply must remain


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 27 of 33**


## Data Sheet AD3300/1/4/5

**REMOTE NODE INTERFACES**



Table 16 provides the list of the remote node interfaces available
on the AD3300/1/4/5. Up to four different serial interfaces can be
configured for concurrent operation. Internal multiplexing allows any


_**Table 16. Supported Remote Node Interfaces**_



remote node interface pins to be assigned to any of the twelve
sensor/actuator interface pins - SAIF[11:0].



















|Remote Node Interface|Number of Interfaces Available|Interface Pin Type|Pin Direction|
|---|---|---|---|
|SPI Controller|1|~~SPI_CS~~1<br>SPI_SCLK<br>SPI_COTI<br>SPI_CITO<br>SPI_IRQ (Optional)|Output<br>Output<br>Output<br>Input<br>Input|
|I2C Controller<br>|1<br>|I2C_SCL<br>I2C_SDA<br>|Output<br>Input/Output|
|LIN Controller<br>|2<br>|LIN_EN<br>LIN_TXD<br>LIN_RXD<br>ial|Output<br>Output<br>Input|
|Port Controller2<br>GPIO<br>PWM<br>|12<br>12<br>de<br><br>|GPIO[11:0]<br>PWM[11:0]<br><br>n<br>|Input/Output<br>Output|
|UART<br>|1<br>fi<br><br>|UART_RX<br>UART_TX<br><br><br>|Input<br>Output|
|ADC<br>|13<br><br><br>|SAIF[5:0]<br>VBAT4, DVDDIO, LVDD, DVDD, AVDD5<br><br><br>ir|Input<br>Input6|
|Flexible I/O<br>|2<br><br><br>|SAIF[11:0]<br><br><br>|Input/Output|
|ISELED or ILaS<br>|27 or 48<br>I<br>r<br>|SIOP<br>SION<br><br><br>|Input/Output<br>Input/Output|


1 Up to 8 chip select signals supported.

2 The port controller interface supports GPIO, PWM, and fixed clock functions.

3 All SAIF and voltages listed can be monitored simultaneously.


4 Attenuated 20x.


5 Attenuated 3x.


6 Internally routed to ADC.

7 Only available on AD3304/5.

8 Only available on AD3305.


**Note:** The 10BASE-T1S network throughput may limit the data rate
of different interfaces when operating simultaneously.


The list below provides some example configurations of different
interface types operating simultaneously:


- Port controller configured for 12x GPIOs = 12x SAIF pins used

- Port controller configured for 3x GPIOs (3 pins) and 2x PWM (2
pins) + 1x LIN (3 pins) + 1x ISELED (2 pins) + I [2] C (2 pins) = 12x
SAIF pins used

- 1x SPI (4 pins) + 1x LIN (3 pins) + 1x I [2] C (2 pins) + 1x ISELED
(2 pins) = 11x SAIF pins used

- 1x SPI (4 pins) + 1x LIN (3 pins) + 1x UART (2 pins) = 9x SAIF
pins used





**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 28 of 33**


## Data Sheet AD3300/1/4/5

**TYPICAL CONNECTION DIAGRAMS**


**DROP NODE CONFIGURATION**










|Col1|Col2|C1 100 nF|
|---|---|---|
||||
||||
||||


|Col1|Col2|C1 100 nF|
|---|---|---|
||||
||||









**or 1.8 V, 2.5 V, or 3.3 V**















**WAKE INPUT TO WAKE**

**FROM SLEEP MODE**


**ENABLE OUTPUT**













_**Figure 17. Typical Connection Diagram with 10BASE-T1S in Remote Mode**_


**DROP NODE CONFIGURATION**










|D|Col2|C1 100 nF DI|
|---|---|---|
||||
||||







**or 1.8 V, 2.5 V, or 3.3 V**


**OPEN ALLIANCE**

**MACPHY SERIAL**


**WAKE INPUT TO WAKE**

**FROM SLEEP MODE**

**ENABLE OUTPUT**






















|Col1|Col2|C1 100 nF|
|---|---|---|
||||
||||
||||



_**Figure 18. Typical Connection Diagram with 10BASE-T1S in Dual Mode**_


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 29 of 33**


## Data Sheet AD3300/1/4/5

**TYPICAL CONNECTION DIAGRAMS**



**V** **P-P**















_**Figure 19. Typical Oscillator Connection Diagram**_





_**Table 17. Oscillator Circuit Component Selection**_



**Clock V** **P-P** **R5** **R6** **C16** **Rs**


3.3 V 3.6 kΩ 1.8 kΩ 5 pF 100 Ω



2.5 V 3.6 kΩ 2.4 kΩ 7 pF 100 Ω


1.8 V 3.6 kΩ 4.5 kΩ 15 pF 100 Ω


**Note:** Assumes a parasitic input capacitance (PCB + Pin) of ~10 pF.

**Note:** Rs: Series damping resistor, application specific, recommended value.


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 30 of 33**


## Data Sheet AD3300/1/4/5

**OUTLINE DIMENSIONS**


_**Figure 20. 24-lead Lead Frame Chip Scale Package [LFCSP]**_
_**4 x 4 mm Body and 0.95 mm Package Height**_
_**(CP-24-17)**_
_**Dimensions are shown in millimeters**_


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 31 of 33**


## Data Sheet AD3300/1/4/5

**OUTLINE DIMENSIONS**


**DETAIL A**
**(JEDEC 95)**



**PIN 1**
**INDICATOR**
**AREA**



**4.10**

**4.00 SQ**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||





**INDICATOR AREA OPTIONS**
**(SEE DETAIL A)**


**0.20 MIN**



**0.30 MIN**










|3.90|Col2|Col3|
|---|---|---|
|**3.90**<br>|||
|**3.90**<br>|||


|0.30 0.25 0.18|Col2|Col3|Col4|
|---|---|---|---|
|**1**<br>**24**<br>**18**<br>**19**<br>**EXPOSED**<br>|**1**<br>**24**<br>**18**<br>**19**<br>**EXPOSED**<br>|**1**<br>**24**|**1**<br>**24**|
|**1**<br>**24**<br>**18**<br>**19**<br>**EXPOSED**<br>|**EXPOSED**<br>|**EXPOSED**<br>|**EXPOSED**<br>|
|**12**<br>**13**<br><br>~~**P**~~**A**<br>|~~**P**~~**A**<br>|~~**D**~~<br>||
|**12**<br>|**12**<br>|**12**<br>|**12**<br>|



**TOP VIEW** **BOTTOM VIEW**



**1.00**

**0.95** **SIDE VIEW**
**0.05 MAX**

**0.02 NOM**



**0.30**


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
|**0.50**<br>**BSC**<br>**0.50**<br>**0.40**<br><br>**BOTTOM VIEW**<br>**1**<br>**24**<br>**7**<br>**12**<br>**13**<br>**18**<br>**19**<br>**6**<br>**0.25**<br>**0.18**<br>**0.2**<br>**2.70**<br>**2.60**<br>**2.50**<br>**EXPOSED**<br>~~**P**~~**A**~~**D**~~<br>**PI**<br>**IN**<br>**(SE**<br>**MIN**<br>ial|||||



**FOR PROPER CONNECTION OF**
**THE EXPOSED PAD, REFER TO**
**THE PIN CONFIGURATION AND**
**FUNCTION DESCRIPTIONS**
**SECTION OF THIS DATA SHEET.**



**COPLANARITY**
**0.08**


**0.20 REF**



**SEATING**
**PLANE**





_**Figure 21. 24-lead Lead Frame Chip Scale Package [LFCSP_SS]**_
_**4 x 4 mm Body, With Side Solderable Leads**_
_**(CS-24-2)**_
_**Dimensions are shown in millimeters**_


[For the latest package outline information and land patterns (footprints), go to Package Index.](https://www.analog.com/en/resources/packaging-quality-symbols-footprints/package-index.html)


**[analog.com](http://www.analog.com/en/index.html)** **Rev. SpB | 32 of 33**


## Data Sheet AD3300/1/4/5

**AUTOMOTIVE PRODUCTS**


All automotive-qualified models are available with controlled manufacturing to support the quality and reliability requirements of automotive
applications. Note that these automotive models may have specifications that differ from the commercial models. Only the automotive-grade
products shown are available for use in automotive applications. Contact your local Analog Devices account representative for specific product
ordering information.



ILaS [®] is a registered mark of INOVA Semiconductors GmbH.


I [2] C refers to a communications protocol originally developed by Philips Semiconductors (now NXP Semiconductors).


Updated: February 17, 2025



**ORDERING GUIDE**


**Model** **[1]** **Temperature Range** **Package Description** **Packing Quantity** **Package Option**


AD3300WBCPZ -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) TRAY, 490 CP-24-17


AD3300WBCPZ-RL -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) REEL, 5000 CP-24-17


AD3301WBCPZ -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) TRAY, 490 CP-24-17


AD3301WBCPZ-RL -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) REEL, 5000 CP-24-17


AD3301WBCSZ -40°C to +150°C 24-Lead LFSCP_SS (4mm x 4mm x 0.95mm w/ EP) TRAY, 490 CS-24-2


AD3301WBCSZ-RL -40°C to +150°C 24-Lead LFSCP_SS (4mm x 4mm x 0.95mm w/ EP) REEL, 5000 CS-24-2


AD3304WBCPZ -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) TRAY, 490 CP-24-17


AD3304WBCPZ-RL -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) REEL, 5000 CP-24-17


AD3305WBCPZ -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) TRAY, 490 CP-24-17


AD3305WBCPZ-RL -40°C to +150°C 24-Lead LFSCP (4mm x 4mm x 0.95mm w/ EP) REEL, 5000 CP-24-17


1 Z = RoHS Compliant Part.


**EVALUATION BOARDS**


**Model** **Description**


EVAL-AD3301KTZ E [2] B Remote Node Generic


EVAL-AD3304KTZ E [2] B Remote Node 2 ISELED/ILaS Channels


EVAL-AD3305KTZ E [2] B Remote Node 4 ISELED/ILaS Channels


EVAL-AD3300KTZ E [2] B Dual Mode Controller Node



©2023-2024 Analog Devices, Inc. All rights reserved. Trademarks and
registered trademarks are the property of their respective owners.
One Analog Way, Wilmington, MA 01887-2356, U.S.A.



**Rev. SpB | 33 of 33**


