**1 Features**


## **DRV883x Low-Voltage H-Bridge Driver**

**3 Description**




 - H-Bridge Motor Driver

  - Drives a DC Motor or Other Loads

  - Low MOSFET On-Resistance: HS + LS
280 mΩ

 - 1.8-A Maximum Drive Current

 - Separate Motor and Logic Supply Pins:

  - Motor VM: 0 to 11 V

  - Logic VCC: 1.8 to 7 V

 - PWM or PH-EN Interface

  - DRV8837: PWM, IN1 and IN2

  - DRV8838: PH and EN

 - Low-Power Sleep Mode With 120-nA Maximum
Sleep Current

  - nSLEEP pin

 - Small Package and Footprint

  - 8-Pin WSON With Thermal Pad

  - 2.0 × 2.0 mm

 - Protection Features

  - VCC Undervoltage Lockout (UVLO)

  - Overcurrent Protection (OCP)

  - Thermal Shutdown (TSD)

**2 Applications**


 - Cameras

 - DSLR Lenses

 - Consumer Products

 - Toys

 - Robotics

 - Medical Devices



The DRV883x family of devices provides an
integrated motor driver solution for cameras,
consumer products, toys, and other low-voltage or
battery-powered motion control applications. The
device can drive one dc motor or other devices
like solenoids. The output driver block consists of Nchannel power MOSFETs configured as an H-bridge
to drive the motor winding. An internal charge pump
generates needed gate drive voltages.


The DRV883x family of devices can supply up to
1.8 A of output current. It operates on a motor power
supply voltage from 0 to 11 V, and a device power
supply voltage of 1.8 V to 7 V.


The DRV8837 device has a PWM (IN1-IN2) input
interface; the DRV8838 device has a PH-EN
input interface. Both interfaces are compatible with
industry-standard devices.


Internal shutdown functions are provided for
overcurrent protection, short-circuit protection,
undervoltage lockout, and overtemperature.

**Device Information** [(1)]

|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|DRV8837|WSON (8)|2.00 mm × 2.00 mm|
|DRV8838|DRV8838|DRV8838|



(1) For all available packages, see the orderable addendum at
the end of the data sheet.



1.8 V to 7 V

VCC



0 V to 11 V

VM










|Col1|PWM or|
|---|---|
|Controller|PH and EN|
|Controller||
|Controller|nSLEEP|
|Controller||



**DRV883x Simplified Diagram**


[Copyright © 2021 Texas Instruments IncorporatedAn IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837) _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 1

intellectual property matters and other important disclaimers. PRODUCTION DATA.


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1
**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Revision History** .............................................................. 2
**5 Pin Configuration and Functions** ...................................4

Pin Functions.................................................................... 4
5.1 Dapper Pin Functions................................................. 4
**6 Specifications** .................................................................. 6

6.1 Absolute Maximum Ratings........................................ 6
6.2 ESD Ratings............................................................... 6
6.3 Recommended Operating Conditions.........................6
6.4 Thermal Information....................................................6
6.5 Electrical Characteristics.............................................8
6.6 Timing Requirements.................................................. 9
6.7 Typical Characteristics.............................................. 10
**7 Detailed Description** ...................................................... 11



7.1 Overview................................................................... 11
7.2 Functional Block Diagram......................................... 11
7.3 Feature Description...................................................13
7.4 Device Functional Modes..........................................16
**8 Power Supply Recommendations** ................................19

8.1 Bulk Capacitance...................................................... 19
**9 Layout** .............................................................................20

9.1 Layout Guidelines..................................................... 20
9.2 Layout Example........................................................ 20
9.3 Power Dissipation..................................................... 20
**10 Device and Documentation Support** ..........................21

10.1 Documentation Support.......................................... 21
10.2 Related Links.......................................................... 21
10.3 Receiving Notification of Documentation Updates..21
10.4 Community Resources............................................21
10.5 Trademarks............................................................. 21



**4 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision E (June 2016) to Revision F (April 2021)** **Page**

 - Updated the numbering format for tables, figures, and cross-references throughout the document..................1

 - Added in the _Independent Half-Bridge Control_ section.....................................................................................13


**Changes from Revision D (December 2015) to Revision E (June 2016)** **Page**

 - Changed the threshold type to the input logic voltage parameters in the _Electrical Characteristics_ table..........8

 - Changed the units for the input logic hysteresis parameter from mV to V in the _Electrical Characteristics_ table
............................................................................................................................................................................8

 - Added the _Receiving Notification of Documentation Updates_ section .............................................................21


**Changes from Revision C (February 2014) to Revision D (December 2015)** **Page**

 - Clarified the input interface for each device in the _Description_ section ............................................................. 1

 - Added CDM and HBM ESD ratings to the _ESD Ratings_ table ...........................................................................6


**Changes from Revision B (December 2013) to Revision C (February 2014)** **Page**

 - Added the DRV8838 device information, specifications, and timing diagrams...................................................1

 - Added Device Information table..........................................................................................................................1

 - Added a PWM interface diagram .......................................................................................................................1

 - Added more information to the Detailed Description and moved information from the Functional Description ...
11

 - Added functional block diagram for DRV8838 ................................................................................................. 11

 - Added the _Application and Implementation_ section .........................................................................................17

 - Added _Power Supply Recommendations_, _Layout_, _Device and Documentation Support_, and _Mechanical,_
_Packaging, and Orderable Information_ sections...............................................................................................19


2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



**Changes from Revision A (August 2012) to Revision B (December 2013)** **Page**

 - Changed Features section..................................................................................................................................1

 - Changed Recommended Operating Conditions................................................................................................. 6

 - Changed Electrical Characteristics section........................................................................................................ 8

 - Changed Timing Requirements section..............................................................................................................9

 - Changed Power Supplies and Input Pins section.............................................................................................16


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 3


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


**5 Pin Configuration and Functions**



















**Figure 5-1. DSG Package 8-Pin WSON With**
**Thermal Pad DRV8837 Top View**


**Pin Functions**



**Figure 5-2. DSG Package 8-Pin WSON With**
**Thermal Pad DRV8838 Top View**















|PIN|Col2|Col3|I/O|DESCRIPTION|
|---|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|**NO.**|
|**NAME**|**DRV8837**|**DRV8838**|**DRV8838**|**DRV8838**|
|**POWER AND GROUND**|**POWER AND GROUND**|**POWER AND GROUND**|**POWER AND GROUND**|**POWER AND GROUND**|
|GND|4|4|—|Device ground<br>This pin must be connected to ground.|
|VCC|8|8|I|Logic power supply<br>Bypass this pin to the GND pin with a 0.1-µF ceramic capacitor rated for VCC.|
|VM|1|1|I|Motor power supply<br>Bypass this pin to the GND pin with a 0.1-µF ceramic capacitor rated for VM.|
|**CONTROL**|**CONTROL**|**CONTROL**|**CONTROL**|**CONTROL**|
|EN|—|5|I|ENABLE input|
|IN1|6|—|I|IN1 input<br>See the_Section 7_ section for more information.|
|IN2|5|—|I|IN2 input<br>See the_Section 7_ section for more information.|
|PH|—|6|I|PHASE input<br>See the_Section 7_ section for more information.|
|nSLEEP|7|7|I|Sleep mode input<br>When this pin is in logic low, the device enters low-power sleep mode. The device operates<br>normally when this pin is logic high. Internal pulldown|
|**OUTPUT**|**OUTPUT**|**OUTPUT**|**OUTPUT**|**OUTPUT**|
|OUT1|2|2|O|Motor output<br>Connect these pins to the motor winding.|
|OUT2|3|3|O|O|


**5.1 Dapper Pin Functions**

|PIN|Col2|Col3|I/O|DESCRIPTION|
|---|---|---|---|---|
|**NAME**|**DRV8837**<br>**NO.**|**DRV8838**<br>**NO.**|**DRV8838**<br>**NO.**|**DRV8838**<br>**NO.**|
|GND|4|4|—|Device ground<br>This pin must be connected to ground.|
|VCC|8|8|I|Logic power supply<br>Bypass this pin to the GND pin with a 0.1-µF ceramic capacitor rated for VCC.|



4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021









|PIN|Col2|Col3|I/O|DESCRIPTION|
|---|---|---|---|---|
|**NAME**|**DRV8837**<br>**NO.**|**DRV8838**<br>**NO.**|**DRV8838**<br>**NO.**|**DRV8838**<br>**NO.**|
|VM|1|1|I|Motor power supply<br>Bypass this pin to the GND pin with a 0.1-µF ceramic capacitor rated for VM.|
|EN|—|5|I|ENABLE input|
|IN1|6|—|I|IN1 input<br>See the_Section 7_ section for more information.|
|IN2|5|—|I|IN2 input<br>See the_Section 7_ section for more information.|
|PH|—|6|I|PHASE input<br>See the_Section 7_ section for more information.|
|nSLEEP|7|7|I|Sleep mode input<br>When this pin is in logic low, the device enters low-power sleep mode. The device operates<br>normally when this pin is logic high. Internal pulldown|
|OUT1|2|2|O|Motor output<br>Connect these pins to the motor winding.|
|OUT2|3|3|O|O|


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 5


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


**6 Specifications**
**6.1 Absolute Maximum Ratings**


over operating ambient temperature range (unless otherwise noted) [(1)] [(2)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|Motor power-supply voltage|VM|–0.3<br>12|V|
|Logic power-supply voltage|VCC|–0.3<br>7|V|
|Control pin voltage|IN1, IN2, PH, EN, nSLEEP|–0.5<br>7|V|
|Peak drive current|OUT1, OUT2|Internally limited|A|
|Operating virtual junction temperature, TJ|Operating virtual junction temperature, TJ|–40<br>150|°C|
|Storage temperature, Tstg|Storage temperature, Tstg|–60<br>150|°C|



(1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress ratings
only, and do not imply functional operation of the device at these or any other conditions beyond those indicated under _Recommended_

_Operating Conditions_ . Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) All voltage values are with respect to network ground pin.


**6.2 ESD Ratings**


over operating ambient temperature range (unless otherwise noted)






|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic<br>discharge|Human body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±3000|V|
|V(ESD)<br>Electrostatic<br>discharge|Charged device model (CDM), per JEDEC specification JESD22-C101(2)|±1500|±1500|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**6.3 Recommended Operating Conditions**


over operating ambient temperature range (unless otherwise noted) [(1)]

|Col1|MIN MAX|UNIT|
|---|---|---|
|VM<br>Motor power supply voltage|0<br>11|V|
|VCC<br>Logic power supply voltage|1.8<br>7|V|
|IOUT<br>Motor peak current|0<br>1.8|A|
|fPWM<br>Externally applied PWM frequency|0<br>250|kHz|
|VLOGIC<br>Logic level input voltage|0<br>5.5|V|
|TA<br>Operating ambient temperature|–40<br>85|°C|



(1) Power dissipation and thermal limits must be observed.


**6.4 Thermal Information**


over operating free-air temperature range (unless otherwise noted)







|THERMAL METRIC(1)|DRV883x|UNIT|
|---|---|---|
|**THERMAL METRIC**(1)|**DSG (WSON)**|**DSG (WSON)**|
|**THERMAL METRIC**(1)|**8 PINS**|**8 PINS**|
|RθJA<br>Junction-to-ambient thermal resistance|60.9|°C/W|
|RθJC(top)<br>Junction-to-case (top) thermal resistance|71.4|°C/W|
|RθJB<br>Junction-to-board thermal resistance|32.2|°C/W|
|ψJT<br>Junction-to-top characterization parameter|1.6|°C/W|
|ψJB<br>Junction-to-board characterization parameter|32.8|°C/W|


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


over operating free-air temperature range (unless otherwise noted)



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



|THERMAL METRIC(1)|DRV883x|UNIT|
|---|---|---|
|**THERMAL METRIC**(1)|**DSG (WSON)**|**DSG (WSON)**|
|**THERMAL METRIC**(1)|**8 PINS**|**8 PINS**|
|RθJC(bot)<br>Junction-to-case (bottom) thermal resistance|9.8|°C/W|


(1) For more information about traditional and new thermal limits, see the _[Semiconductor and IC Package Thermal Metrics](https://www.ti.com/lit/pdf/SPRA953)_ application
report.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 7


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


**6.5 Electrical Characteristics**































|PARAMETER|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|
|**POWER SUPPLIES (VM, VCC)**|**POWER SUPPLIES (VM, VCC)**|**POWER SUPPLIES (VM, VCC)**|**POWER SUPPLIES (VM, VCC)**|
|VM<br>VM operating voltage||0<br>11|V|
|IVM<br>VM operating supply current|VM = 5 V; VCC = 3 V;<br>No PWM|40<br>100|μA|
|IVM<br>VM operating supply current|VM = 5 V; VCC = 3 V;<br>50 kHz PWM|0.8<br>1.5|mA|
|IVMQ<br>VM sleep mode supply current|VM = 5 V; VCC = 3 V;<br>nSLEEP = 0|30<br>95|nA|
|VCC<br>VCC operating voltage||1.8<br>7|V|
|IVCC<br>VCC operating supply current|VM = 5 V; VCC = 3 V;<br>No PWM|300<br>500|μA|
|IVCC<br>VCC operating supply current|VM = 5 V; VCC = 3 V;<br>50 kHz PWM|0.7<br>1.5|mA|
|IVCCQ<br>VCC sleep mode supply current|VM = 5 V; VCC = 3 V;<br>nSLEEP = 0|5<br>25|nA|
|**CONTROL INPUTS (IN1 or PH, IN2 or EN, nSLEEP)**|**CONTROL INPUTS (IN1 or PH, IN2 or EN, nSLEEP)**|**CONTROL INPUTS (IN1 or PH, IN2 or EN, nSLEEP)**|**CONTROL INPUTS (IN1 or PH, IN2 or EN, nSLEEP)**|
|VIL<br>Input logic-low voltage falling<br>threshold||0.25 × VCC<br>0.38 × VCC|V|
|VIH<br>Input logic-high voltage rising<br>threshold||0.46 × VCC<br>0.5 × VCC|V|
|VHYS<br>Input logic hysteresis||0.08 × VCC|V|
|IIL<br>Input logic low current|VIN = 0 V|–5<br>5|μA|
|IIH<br>Input logic high current|VIN = 3.3 V|50|μA|
|IIH<br>Input logic high current|VIN = 3.3 V, DRV8838 nSLEEP pin|60|μA|
|RPD<br>Pulldown resistance||100|kΩ|
|RPD<br>Pulldown resistance|DRV8838 nSLEEP pin|55|kΩ|
|**MOTOR DRIVER OUTPUTS (OUT1, OUT2)**|**MOTOR DRIVER OUTPUTS (OUT1, OUT2)**|**MOTOR DRIVER OUTPUTS (OUT1, OUT2)**|**MOTOR DRIVER OUTPUTS (OUT1, OUT2)**|
|rDS(on)<br>HS + LS FET on-resistance|VM = 5 V; VCC = 3 V;<br>IO = 800 mA; TJ = 25°C|280<br>330|mΩ|
|IOFF<br>Off-state leakage current|VOUT = 0 V|–200<br>200|nA|
|**PROTECTION CIRCUITS**|**PROTECTION CIRCUITS**|**PROTECTION CIRCUITS**|**PROTECTION CIRCUITS**|
|VUVLO<br>VCC undervoltage lockout|VCC falling|1.7|V|
|VUVLO<br>VCC undervoltage lockout|VCC rising|1.8||
|IOCP<br>Overcurrent protection trip level||1.9<br>3.5|A|
|tDEG<br>Overcurrent deglitch time||1|μs|
|tRETRY<br>Overcurrent retry time||1|ms|
|TTSD<br>Thermal shutdown temperature|Die temperature TJ|150<br>160<br>180|°C|


8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**6.6 Timing Requirements**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021















|NO.|Col2|Col3|MIN MAX|UNIT|
|---|---|---|---|---|
|1|t1<br>Delay time, PHASE high to OUT1 low|SeeFigure 6-1.|160|ns|
|2|t2<br>Delay time, PHASE high to OUT2 high|t2<br>Delay time, PHASE high to OUT2 high|200|ns|
|3|t3<br>Delay time, PHASE low to OUT1 high|t3<br>Delay time, PHASE low to OUT1 high|200|ns|
|4|t4<br>Delay time, PHASE low to OUT2 low|t4<br>Delay time, PHASE low to OUT2 low|160|ns|
|5|t5<br>Delay time, ENBL high to OUTx high|t5<br>Delay time, ENBL high to OUTx high|200|ns|
|6|t6<br>Delay time, ENBL low to OUTx low|t6<br>Delay time, ENBL low to OUTx low|160|ns|
|7|t7<br>Output enable time|SeeFigure 6-2.|300|ns|
|8|t8<br>Output disable time|t8<br>Output disable time|300|ns|
|9|t9<br>Delay time, INx high to OUTx high|t9<br>Delay time, INx high to OUTx high|160|ns|
|10|t10<br>Delay time, INx low to OUTx low|t10<br>Delay time, INx low to OUTx low|160|ns|
|11|t11<br>Output rise time|t11<br>Output rise time|30<br>188|ns|
|12|t12<br>Output fall time|t12<br>Output fall time|30<br>188|ns|
||twake<br>Wake time, nSLEEP rising edge to part active|twake<br>Wake time, nSLEEP rising edge to part active|30|μs|


EN


PH





OUT1


OUT2





DRV8838



**Figure 6-1. Input and Output Timing for DRV8838**


IN1


IN2







OUT1


OUT2


OUTx



















DRV8837





**Figure 6-2. Input and Output Timing for DRV8837**


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 9


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**










|VC|C = 2 V|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|~~V~~<br>V|~~C = 3 V~~<br>C = 7 V||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||VM = 2<br>|V<br>|
|||||||||
|||||||~~VM = 5~~<br>VM = 1|~~   V~~<br>  1 V|
|||||||||
|||||||||
|||||||||
|||||||||


















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||VM =<br>|2 V<br>|
|||||||~~VM =~~<br>VM =|~~   V~~<br>  11 V|
|||||||||
|||||||||
|||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|VC<br>|C = 2 V<br>|C = 2 V<br>|C = 2 V<br>|C = 2 V<br>|C = 2 V<br>|C = 2 V<br>|
|~~VC~~<br>VC|~~C = 3 V~~<br>C = 7 V||||||
||||||||
||||||||










|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
||||||VM = 2 V, V<br>|CC = 2 V<br>||
||||||VM = 5 V, V<br>VM = 11 V,|CC = 3 V<br>    VCC = 5V||
|||||||||
|||||||||
|||||||||








|6.7 Typical Characteristics|Col2|
|---|---|
|Ambient Temperature (ºC)<br>VM Sleep Current (PA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>90<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>D002<br>VM = 2 V<br>~~VM = 5 V~~<br>VM = 11 V<br>**Figure 6-3. IVMQ vs TA**|Ambient Temperature (ºC)<br>VCC Sleep Current (PA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>90<br>0<br>0.002<br>0.004<br>0.006<br>0.008<br>0.01<br>0.012<br>0.014<br>0.016<br>0.018<br>0.02<br>D003<br>VCC = 2 V<br>~~VCC = 3 V~~<br>VCC = 7 V<br>**Figure 6-4. IVCCQ vs TA**|
|Ambient Temperature (ºC)<br>VM Operating Current (mA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>90<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>D004<br>VM = 2 V<br>~~VM = 5 V~~<br>VM = 11 V<br>**Figure 6-5. IVM vs TA (50-kHz PWM)**|Ambient Temperature (ºC)<br>VCC Operating Current (mA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>90<br>0.65<br>0.7<br>0.75<br>0.8<br>0.85<br>D005<br>VCC = 2 V<br>~~VCC = 3 V~~<br>VCC = 7 V<br>**Figure 6-6. IVCC vs TA (50-kHz PWM)**|
|Ambient Temperature (qC)<br>H S  +  L S  r D S (o n ) (m : )<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>90<br>200<br>300<br>400<br>500<br>600<br>700<br>D005<br>VM = 2 V, VCC = 2 V<br>VM = 5 V, VCC = 3 V<br>VM = 11 V, VCC = 5V<br>**Figure 6-7. HS + LS rDS(on) vs TA**|Ambient Temperature (qC)<br>H S  +  L S  r D S (o n ) (m : )<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>90<br>200<br>300<br>400<br>500<br>600<br>700<br>D005<br>VM = 2 V, VCC = 2 V<br>VM = 5 V, VCC = 3 V<br>VM = 11 V, VCC = 5V<br>**Figure 6-7. HS + LS rDS(on) vs TA**|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7 Detailed Description**
**7.1 Overview**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



The DRV883x family of devices is an H-bridge driver that can drive one dc motor or other devices like solenoids.
The outputs are controlled using either a PWM interface (IN1 and IN2) on the DRV8837 device or a PH-EN
interface on the DRV8838 device.


A low-power sleep mode is included, which can be enabled using the nSLEEP pin.


These devices greatly reduce the component count of motor driver systems by integrating the necessary driver
FETs and FET control circuitry into a single device. In addition, the DRV883x family of devices adds protection
features beyond traditional discrete implementations: undervoltage lockout, overcurrent protection, and thermal
shutdown.


**7.2 Functional Block Diagram**



























**Figure 7-1. DRV8837 Functional Block Diagram**


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 11


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**

























**Figure 7-2. DRV8838 Functional Block Diagram**


12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3 Feature Description**

**7.3.1 Bridge Control**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



The DRV8837 device is controlled using a PWM input interface, also called an IN-IN interface. Each output is
controlled by a corresponding input pin.


Table 7-1 shows the logic for the DRV8837 device.


**Table 7-1. DRV8837 Device Logic**

|nSLEEP|IN1|IN2|OUT1|OUT2|FUNCTION (DC MOTOR)|
|---|---|---|---|---|---|
|0|X|X|Z|Z|Coast|
|1|0|0|Z|Z|Coast|
|1|0|1|L|H|Reverse|
|1|1|0|H|L|Forward|
|1|1|1|L|L|Brake|



The DRV8838 device is controlled using a PHASE/ENABLE interface. This interface uses one pin to control the
H-bridge current direction, and one pin to enable or disable the H-bridge.


Table 7-2 shows the logic for the DRV8838.


**Table 7-2. DRV8838 Device Logic**

|nSLEEP|PH|EN|OUT1|OUT2|FUNCTION (DC MOTOR)|
|---|---|---|---|---|---|
|0|X|X|Z|Z|Coast|
|1|X|0|L|L|Brake|
|1|1|1|L|H|Reverse|
|1|0|1|H|L|Forward|



**7.3.2 Independent Half-Bridge Control**


Independent half-bridge control is possible with the DRV8837 without adopting more discrete components, as
shown in Section 7.3.2. Two inductive loads (M1 and M2), which could be motors or solenoids, are tied between
VM and OUTx, while the corresponding inputs (C1 and C2) are swapped before being fed to INx.


**Figure 7-3. Independent Half-Bridge Control Circuit**


The control logic for independent half-bridge drive is shown in Table 7-3. Columns INx and OUTx show the
original logic of the DRV8837. Note that although a swap is included in this implementation, it is still valid that


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 13


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


Cx = 1 spins a motor or energizes a solenoid connected at corresponding Mx, while Cx = 0, stops the motor or
discharges the solenoid.


**Table 7-3. Independent Half-Bridge Drive Logic**

|C1|C2|IN1|IN2|OUT1|OUT2|M1|M2|
|---|---|---|---|---|---|---|---|
|0|0|0|0|Z|Z|Off: Braking mode 1|Off: Braking mode 1|
|1|0|0|1|L|H|On: Driving mode|Off: Braking mode 2|
|0|1|1|0|H|L|Off: Braking mode 2|On: Driving mode|
|1|1|1|1|L|L|On: Driving mode|On: Driving mode|



Figure 7-4 shows the driving mode and the two current decay paths during current regulation when PWM input
control is used. The driving mode occurs when the corresponding half-bridge Cx signal is _**HIGH**_ . When the
Cx signal is _**LOW**_, the corresponging half bridge can go into either braking mode 1 or braking mode 2. In
braking mode 1, both the high- and low-side MOSFETs of the half-bridge are tri-stated, and the recirculation
current flows through the body diode of the high-side MOSFET as well as the motor itself. This braking mode
happens when both C1 and C2 are _**LOW**_ . If one of the Cx input is _**LOW**_ and the other HIGH, the half-bridge
corresponding to the _**LOW**_ Cx input will go into braking mode 2. In braking mode 2, the low-side FET is _**OFF**_
while its high-side counterpart is _**ON**_ . The recirculation current flows through the high-side MOSFET and the
motor.


**Figure 7-4. Normal Driving and Current Decay Modes**


When each of the Cx inputs are independently controlled with different PWM frequencies and duty cycle, each
half-bridge will go into a combination of braking mode 1 and braking mode 2. Figure 7-5 show a driving and
decay example with independent PWM inputs. If the half-bridge spends more time in braking mode 1, the motor
average speed will be lower since more power is dissipated through the MOSFET body diode. To reduce the
power dissipated during braking mode 1, it is recommended to placed Schottky diodes with forward voltage less
than 0.6V across the motors as shown in Figure 7-6. Note that if On/Off control mode (constant HIGH or LOW at
inputs) is used, the two braking modes do not interact with each other and hence have no effect on the average
speed of the two motors.


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3.3 Sleep Mode**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021


**Figure 7-5. Driving and Decay Examples with Independent PWM Inputs**


**Figure 7-6. Improved Application Circuit for Better Motor Performance**



If the nSLEEP pin is brought to a logic-low state, the DRV883x family of devices enters a low-power sleep mode.
In this state, all unnecessary internal circuitry is powered down.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 15


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


**7.3.4 Power Supplies and Input Pins**


The input pins can be driven within the recommended operating conditions with or without the VCC, VM, or both
power supplies present. No leakage current path will exist to the supply. Each input pin has a weak pulldown
resistor (approximately 100 kΩ) to ground.


The VCC and VM supplies can be applied and removed in any order. When the VCC supply is removed, the
device enters a low-power state and draws very little current from the VM supply. The VCC and VM pins can be
connected together if the supply voltage is between 1.8 and 7 V.


The VM voltage supply does not have any undervoltage-lockout protection (UVLO) so as long as VCC > 1.8 V;
the internal device logic remains active, which means that the VM pin voltage can drop to 0 V. However, the load
cannot be sufficiently driven at low VM voltages.


**7.3.5 Protection Circuits**


The DRV883x family of devices is fully protected against VCC undervoltage, overcurrent, and overtemperature
events.


_**7.3.5.1 VCC Undervoltage Lockout**_


If at any time the voltage on the VCC pin falls below the undervoltage lockout threshold voltage, all FETs in the
H-bridge are disabled. Operation resumes when the VCC pin voltage rises above the UVLO threshold.


_**7.3.5.2 Overcurrent Protection (OCP)**_


An analog current-limit circuit on each FET limits the current through the FET by removing the gate drive. If
this analog current limit persists for longer than tDEG, all FETs in the H-bridge are disabled. Operation resumes
automatically after tRETRY has elapsed. Overcurrent conditions are detected on both the high-side and low-side
FETs. A short to the VM pin, GND, or from the OUT1 pin to the OUT2 pin results in an overcurrent condition.


_**7.3.5.3 Thermal Shutdown (TSD)**_


If the die temperature exceeds safe limits, all FETs in the H-bridge are disabled. After the die temperature falls to
a safe level, operation automatically resumes.


_**7.3.5.4**_


**Table 7-4. Fault Behavior**

|FAULT|CONDITION|H-BRIDGE|RECOVERY|
|---|---|---|---|
|VCC undervoltage (UVLO)|VCC < 1.7 V|Disabled|VCC > 1.8 V|
|Overcurrent (OCP)|IOUT > 1.9 A (MIN)|Disabled|tRETRY elapses|
|Thermal Shutdown (TSD)|TJ > 150°C (MIN)|Disabled|TJ < 150°C|



**7.4 Device Functional Modes**


The DRV883x family of devices is active unless the nSLEEP pin is brought logic low. In sleep mode, the
H-bridge FETs are disabled Hi-Z. The DRV883x is brought out of sleep mode automatically if nSLEEP is brought
logic high.


The H-bridge outputs are disabled during undervoltage lockout, overcurrent, and overtemperature fault
conditions.


**Table 7-5. Operation Modes**

|MODE|CONDITION|H-BRIDGE|
|---|---|---|
|Operating|nSLEEP pin = 1|Operating|
|Sleep mode|nSLEEP pin = 0|Disabled|
|Fault encountered|Any fault condition met|Disabled|



16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**Application and Implementation**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



**Note**


Information in the following applications sections is not part of the TI component specification, and
TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining
suitability of components for their purposes. Customers should validate and test their design
implementation to confirm system functionality.


**8.1 Application Information**


The DRV883x family of devices is device is used to drive one dc motor or other devices like solenoids. The
following design procedure can be used to configure the DRV883x family of devices.


**8.2 Typical Application**













VCC


0.1 µF









**Figure 8-1. Schematic of DRV883x Application**


**8.2.1 Design Requirements**


Table 8-1 lists the required parameters for a typical usage case.


**Table 8-1. System Design Requirements**

|DESIGN PARAMETER|REFERENCE|EXAMPLE VALUE|
|---|---|---|
|Motor supply voltage|VM|9 V|
|Logic supply voltage|VCC|3.3 V|
|Target rms current|IOUT|0.8 A|



**8.2.2 Detailed Design Procedure**
_**8.2.2.1 Motor Voltage**_


The appropriate motor voltage depends on the ratings of the motor selected and the desired RPM. A higher
voltage spins a brushed dc motor faster with the same PWM duty cycle applied to the power FETs. A higher
voltage also increases the rate of current change through the inductive motor windings.


_**8.2.2.2 Low-Power Operation**_


When entering sleep mode, TI recommends setting all inputs as a logic low to minimize system power.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 17


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**

|8.2.3 Application Curves|Col2|
|---|---|
|**Figure 8-2. 50% Duty Cycle, Forward Direction**|**Figure 8-3. 50% Duty Cycle, Reverse Direction**|
|**Figure 8-4. 20% Duty Cycle, Forward Direction**|**Figure 8-5. 20% Duty Cycle, Reverse Direction**|



**Note**


DIR_V is an indication of the motor direction. It is not a pin of the DRV883x device.


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**8 Power Supply Recommendations**
**8.1 Bulk Capacitance**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



Having appropriate local bulk capacitance is an important factor in motor-drive system design. It is generally
beneficial to have more bulk capacitance, while the disadvantages are increased cost and physical size.


The amount of local capacitance needed depends on a variety of factors, including:


 - The highest current required by the motor system

 - The power-supply capacitance and ability to source current

 - The amount of parasitic inductance between the power supply and motor system

 - The acceptable voltage ripple

 - The type of motor used (brushed dc, brushless dc, stepper)

 - The motor braking method


The inductance between the power supply and motor drive system limits the rate at which current can change
from the power supply. If the local bulk capacitance is too small, the system responds to excessive current
demands or dumps from the motor with a change in voltage. When adequate bulk capacitance is used, the
motor voltage remains stable and high current can be quickly supplied.


The data sheet generally provides a recommended value, but system-level testing is required to determine the
appropriate size of bulk capacitor.










|Parasitic Wire<br>Inductance<br>Power Supply Motor Drive System<br>VM<br>+ + Motor<br>– Driver<br>GND<br>Local IC Bypass<br>Bulk Capacitor Capacitor|Col2|
|---|---|
|+<br>–|Local<br>Bulk Capacitor<br>**Motor**<br>**Driver**<br>VM<br>GND<br>+<br>IC Bypass<br>Capacitor|



**Figure 8-1. Example Setup of Motor Drive System With External Power Supply**


The voltage rating for bulk capacitors should be higher than the operating voltage, to provide margin for cases
when the motor transfers energy to the supply


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 19


**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021 **[www.ti.com](https://www.ti.com)**


**9 Layout**
**9.1 Layout Guidelines**


The VM and VCC pins should be bypassed to GND using low-ESR ceramic bypass capacitors with a
recommended value of 0.1 µF rated for VM and VCC . These capacitors should be placed as close to the
VM and VCC pins as possible with a thick trace or ground plane connection to the device GND pin.


**9.2 Layout Example**



0.1 µF



0.1 µF



















**Figure 9-1. Simplified Layout Example**


**9.3 Power Dissipation**


Power dissipation in the DRV883x family of devices is dominated by the power dissipated in the output FET
resistance, or rDS(on). Use Equation 1 to estimate the average power dissipation when running a stepper motor.


PTOT   - r DS(on)   - (IOUT(RMS) )2 (1)


where


 - PTOT is the total power dissipation

 - rDS(on) is the resistance of the HS plus LS FETs

 - IOUT(RMS) is the rms or dc output current being supplied to the load

The maximum amount of power that can be dissipated in the device is dependent on ambient temperature and
heatsinking.


**Note**


The value of rDS(on) increases with temperature, so as the device heats, the power dissipation
increases.


The DRV883x family of devices has thermal shutdown protection. If the die temperature exceeds approximately
150°C, the device is disabled until the temperature drops to a safe level.


Any tendency of the device to enter thermal shutdown is an indication of either excessive power dissipation,
insufficient heatsinking, or too high an ambient temperature.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ Copyright © 2021 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**10 Device and Documentation Support**
**10.1 Documentation Support**

**10.1.1 Related Documentation**


For related documentation see the following:

 - _[Calculating Motor Driver Power Dissipation](https://www.ti.com/lit/pdf/SLVA504)_

 - _[DRV8837EVM User’s Guide](https://www.ti.com/lit/pdf/SLVU749)_

 - _[DRV8838EVM User’s Guide](https://www.ti.com/lit/pdf/SLVUA43)_

 - _[Independent Half-Bridge Drive with DRV8837](https://www.ti.com/lit/pdf/SLVA539)_

 - _[Understanding Motor Driver Current Ratings](https://www.ti.com/lit/pdf/SLVA505)_


**10.2 Related Links**



**DRV8837, DRV8838**
SLVSBA4F – JUNE 2012 – REVISED APRIL 2021



The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to sample or buy.


**Table 10-1. Related Links**









|PARTS|PRODUCT FOLDER|SAMPLE & BUY|TECHNICAL<br>DOCUMENTS|TOOLS &<br>SOFTWARE|SUPPORT &<br>COMMUNITY|
|---|---|---|---|---|---|
|DRV8837|Click here|Click here|Click here|Click here|Click here|
|DRV8838|Click here|Click here|Click here|Click here|Click here|


**10.3 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on _Alert me_ to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document.


**10.4 Community Resources**
**10.5 Trademarks**
All trademarks are the property of their respective owners.

**Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSBA4F&partnum=DRV8837)_ 21


### **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Nov-2025


**PACKAGING INFORMATION**





















**(1) Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)


**(2) Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.


**(3) RoHS values:** [Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.](https://www.ti.com/lit/szzq088)


**(4) Lead finish/Ball material:** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.


**(5) MSL rating/Peak reflow:** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.


**(6) Part marking:** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Nov-2025


and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 15-Aug-2025


**TAPE AND REEL INFORMATION**



**REEL DIMENSIONS**


*All dimensions are nominal





Reel Width (W1)



**TAPE DIMENSIONS**


|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||B0W|
||||||||
||||||||
|vity|vity|vity|A0|A0|||






|A0|Dimension designed to accommodate the component width A0 Cavity|
|---|---|
|A0<br>|<br>Dimension designed to accommodate the component width|
|B0<br>|Dimension designed to accommodate the component length<br> <br>|
|K0<br>|<br>Dimension designed to accommodate the component thickness<br>|
|W<br>|<br>Overall width of the carrier tape<br>|
|P1|Pitch between successive cavity centers|



**QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE**

Sprocket Holes

|Q1|Q2|
|---|---|
|Q3|Q4|


|Q1|Q2|
|---|---|
|Q3|Q4|



Pocket Quadrants























|Device|Package<br>Type|Package<br>Drawing|Pins|SPQ|Reel<br>Diameter<br>(mm)|Reel<br>Width<br>W1 (mm)|A0<br>(mm)|B0<br>(mm)|K0<br>(mm)|P1<br>(mm)|W<br>(mm)|Pin1<br>Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DRV8837DSGR|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|DRV8837DSGRG4|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|DRV8838DSGR|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|DRV8838DSGRG4|WSON|DSG|8|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 15-Aug-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|DRV8837DSGR|WSON|DSG|8|3000|182.0|182.0|20.0|
|DRV8837DSGRG4|WSON|DSG|8|3000|210.0|185.0|35.0|
|DRV8838DSGR|WSON|DSG|8|3000|182.0|182.0|20.0|
|DRV8838DSGRG4|WSON|DSG|8|3000|182.0|182.0|20.0|



Pack Materials-Page 2


## **GENERIC PACKAGE VIEW**
# **DSG 8 WSON - 0.8 mm max height**

**2 x 2, 0.5 mm pitch** PLASTIC SMALL OUTLINE - NO LEAD


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4224783/A


www.ti.com


## **PACKAGE OUTLINE**
# DSG0008A SCALE 5.500 WSON - 0.8 mm max height

PLASTIC SMALL OUTLINE - NO LEAD














|SIDE WALL<br>METAL THICKNESS<br>DIM A|Col2|
|---|---|
|OPTION 1|OPTION 2|
|0.1|0.2|



















NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DSG0008A WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD








|Col1|Col2|
|---|---|
|||



















NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.


www.ti.com


## **EXAMPLE STENCIL DESIGN**
# **DSG0008A WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD























NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


www.ti.com


**IMPORTANT NOTICE AND DISCLAIMER**

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS”
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.


These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.


These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully
indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.


[TI’s products are provided subject to TI’s Terms of Sale, TI’s General Quality Guidelines, or other applicable terms available either on](https://www.ti.com/legal/terms-conditions/terms-of-sale.html)
[ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable](https://www.ti.com)
warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products
are standard, catalog, general purpose devices.


TI objects to and rejects any additional or different terms you may propose.


IMPORTANT NOTICE


Copyright © 2025, Texas Instruments Incorporated


Last updated 10/2025


