Technical

Documents

|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|TMUX1574|TSSOP (16)|5.00 mm × 4.40 mm|
|TMUX1574|UQFN (16)|2.60 mm x 1.80 mm|
|TMUX1574|SOT-23-THIN (16)|4.20 mm x 2.00 mm|


�



�



Support &
Community


�



Product

Folder


�



Order

Now


�



Tools &

Software


�



�



�



�



�



**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019

### **TMUX1574 Low-Capacitance, 2:1 (SPDT) 4-Channel,** **Powered-Off Protected Switch with 1.8 V Logic**


�



�



**1** **Features**


1 - Wide supply range: 1.5 V to 5.5 V

- Low on-capacitance: 7.5 pF

- Low on-resistance: 2 Ω

- High bandwidth: 2 GHz

- -40°C to +125°C operating temperature

- 1.8 V Logic Compatible

- Supports Input Voltage Beyond Supply

- Integrated Pull Down Resistor on Logic Pins

- Bidirectional Signal Path

- Fail-Safe Logic

- Powered-off Protection up to 3.6 V Signals

–
Pinout compatible to SN74CBTLV3257


**2** **Applications**


- Flash memory sharing

- JTAG multiplexing

- SPI multiplexing

- eMMC multiplexing

- [Servers](http://www.ti.com/solution/server)

- [Data center switches & routers](http://www.ti.com/solution/data-center-switches)

- [Wireless infrastructure](http://www.ti.com/applications/communications-equipment/wireless-infrastructure/overview.html)

- [PC & notebooks](http://www.ti.com/applications/personal-electronics/pc-notebooks/overview.html)

- [Building automation](http://www.ti.com/applications/industrial/building-automation/overview.html)

- [Grid infrastructure](http://www.ti.com/applications/industrial/grid-infrastructure/overview.html)

- [ePOS](http://www.ti.com/applications/industrial/epos/overview.html)

- [Appliances](http://www.ti.com/solution/appliances_user_interface_connectivity_modules)


�



**3** **Description**
The TMUX1574 is a complementary metal-oxide
semiconductor (CMOS) switch. The TMUX1574
offers 2:1 SPDT switch configuration with 4-channels.
Wide operating supply of 1.5 V to 5.5 V allows for use
in a broad array of applications from servers and
communication equipment to industrial applications.
The device supports bidirectional analog and digital
signals on the source (SxA, SxB) and drain (Dx) pins
and can pass signals above supply up to V DD x 2,
with a maximum input/output voltage of 5.5 V.


Powered-off Protection up to 3.6 V on the signal path
of the TMUX1574 provides isolation when the supply
voltage is removed (V DD = 0 V). Without this
protection feature, switches can back-power the
supply rail through an internal ESD diode and cause
potential damage to the system.


Fail-Safe Logic circuitry allows voltages on the logic
control pins to be applied before the supply pin,
protecting the device from potential damage. All
control inputs have 1.8 V logic compatible thresholds,
ensuring both TTL and CMOS logic compatibility
when operating in the valid supply voltage range.
Integrated pull down resistor on the logic pins
removes external components to reduce system size
and cost.


**Device Information** **[(1)]**


�



�



�



(1) For all available packages, see the package option addendum

at the end of the data sheet.


**Application Example** **Block Diagram**


�



V I/O V DD 0.1µF V DD


�



�



S1A
D1
S1B


�



�



�



�



�



�



�



�



�



S2A

S2B


S3A

S3B


S4A

S4B


�


|JTAG<br>DEBUG,<br>SPI, GPIO|Col2|Col3|
|---|---|---|
|JTAG<br>DEBUG,<br>SPI, GPIO|||
|JTAG<br>DEBUG,<br>SPI, GPIO|||
|JTAG<br>DEBUG,<br>SPI, GPIO|||
|JTAG<br>DEBUG,<br>SPI, GPIO|||



�



D2


D3


D4


�



�



�



SEL


�



EN


�



�


1



*Internal 6MO �Pull-Down on Logic Pins


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.



�


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Table of Contents**



**1** **Features** .................................................................. 1

**2** **Applications** ........................................................... 1
**3** **Description** ............................................................. 1
**4** **Revision History** ..................................................... 2
**5** **Pin Configuration and Functions** ......................... 3
**6** **Specifications** ......................................................... 5

6.1 Absolute Maximum Ratings ...................................... 5
6.2 ESD Ratings.............................................................. 5
6.3 Recommended Operating Conditions....................... 5

6.4 Thermal Information.................................................. 5

6.5 Electrical Characteristics........................................... 6

6.6 Dynamic Characteristics ........................................... 7
6.7 Timing Requirements................................................ 8
6.8 Typical Characteristics.............................................. 9

**7** **Parameter Measurement Information** ................ 14


7.1 On-Resistance ........................................................ 14

7.2 Off-Leakage Current ............................................... 14
7.3 On-Leakage Current ............................................... 15
7.4 I POFF Leakage Current............................................ 15

7.5 Transition Time ....................................................... 16

7.6 t ON (EN) and t OFF (EN) Time....................................... 16
7.7 t ON (VDD) and t OFF (VDD) Time................................... 17
7.8 Break-Before-Make Delay....................................... 17
7.9 Propagation Delay................................................... 18

7.10 Skew ..................................................................... 18

7.11 Charge Injection.................................................... 19



7.12 Capacitance .......................................................... 19

7.13 Off Isolation........................................................... 20

7.14 Channel-to-Channel Crosstalk.............................. 20

7.15 Bandwidth ............................................................. 21

**8** **Detailed Description** ............................................ 22


8.1 Overview ................................................................. 22

8.2 Functional Block Diagram ....................................... 22
8.3 Feature Description................................................. 22

8.4 Device Functional Modes........................................ 24

8.5 Truth Tables............................................................ 24

**9** **Application and Implementation** ........................ 25

9.1 Application Information............................................ 25
9.2 Typical Application ................................................. 25
**10** **Power Supply Recommendations** ..................... 26
**11** **Layout** ................................................................... 27
11.1 Layout Guidelines ................................................. 27
11.2 Layout Example .................................................... 28
**12** **Device and Documentation Support** ................. 29
12.1 Documentation Support ........................................ 29
12.2 Receiving Notification of Documentation Updates 29
12.3 Community Resources.......................................... 29

12.4 Trademarks........................................................... 29

12.5 Electrostatic Discharge Caution............................ 29
12.6 Glossary................................................................ 29
**13** **Mechanical, Packaging, and Orderable**
**Information** ........................................................... 30



**4** **Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision B (September 2019) to Revision C** **Page**


- Added prop delay and skew specs for DYY package ........................................................................................................... 8


- Changed Figure 20 to include prop. delay and skew for DYY package .............................................................................. 12


**Changes from Revision A (December 2018) to Revision B** **Page**


- Added the SOT-23-THIN (DYY) package to the data sheet .................................................................................................. 1


- Added thermal information for DYY package......................................................................................................................... 5


**Changes from Original (October 2018) to Revision A** **Page**


- Changed the document status From: _Advanced Information_ To: _Production_ data ................................................................ 1



2



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**5** **Pin Configuration and Functions**



**PW Package**
**16-Pin TSSOP**

**Top View**


Not to scale



**DYY Package**
**16-Pin SOT-23-THIN**

**Top View**



**RSV Package**

**16-Pin UQFN**

**Top View**







Not to scale


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



3


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Pin Functions**






|PIN|Col2|Col3|TYPE(1)|DESCRIPTION(2)|
|---|---|---|---|---|
|**NAME**|**TSSOP /**<br>**SOT-23-THIN**|**UQFN**|**UQFN**|**UQFN**|
|SEL|1|15|I|Select pin: controls state of switches according to Table 1. Internal 6 MΩ pull-down to<br>GND.|
|S1A|2|16|I/O|Source pin 1A. Can be an input or output.|
|S1B|3|1|I/O|Source pin 1B. Can be an input or output.|
|D1|4|2|I/O|Drain pin 1. Can be an input or output.|
|S2A|5|3|I/O|Source pin 2A. Can be an input or output.|
|S2B|6|4|I/O|Source pin 2B. Can be an input or output.|
|D2|7|5|I/O|Drain pin 2. Can be an input or output.|
|GND|8|6|P|Ground (0 V) reference|
|D3|9|7|I/O|Drain pin 3. Can be an input or output.|
|S3B|10|8|I/O|Source pin 3B. Can be an input or output.|
|S3A|11|9|I/O|Source pin 3A. Can be an input or output.|
|D4|12|10|I/O|Drain pin 4. Can be an input or output.|
|S4B|13|11|I/O|Source pin 4B. Can be an input or output.|
|S4A|14|12|I/O|Source pin 4A. Can be an input or output.|
|EN|15|13|I|Active low enable: When this pin is high, all switches are turned off. When this pin is low,<br>SEL pin controls the signal path selection. Internal 6 MΩ pull-down to GND.|
|VDD|16|14|P|Positive power supply. This pin is the most positive power-supply potential. For reliable<br>operation, connect a decoupling capacitor ranging from 0.1 µF to 10 µF between VDD and<br>GND.|



(1) I = input, O = output, I/O = input and output, P = power
(2) Refer to Device Functional Modes for what to do with unused pins.



4



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**6** **Specifications**


**6.1** **Absolute Maximum Ratings**

Over operating free-air temperature range (unless otherwise noted). [(1)(2)(3)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|VDD|Supply voltage|–0.5<br>6|V|
|VSEL or VEN|Logic control input pin voltage (SEL or EN)|–0.5<br>6|V|
|ISEL or IEN|Logic control input pin current (SEL or EN)|–30<br>30|mA|
|VS or VD|Source or drain pin voltage|–0.5<br>6|V|
|IS or ID (CONT)|Source and drain pin continuous current: (SxA, SxB, Dx)|–25<br>25|mA|
|Tstg|Storage temperature|–65<br>150|°C|
|TJ|Junction temperature|150|°C|



(1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under _Recommended_
_Operating Conditions_ . Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The algebraic convention, whereby the most negative value is a minimum and the most positive value is a maximum.
(3) All voltages are with respect to ground, unless otherwise specified.


**6.2** **ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human body model (HBM), per ANSI/ESDA/JEDEC JS-<br>001(1)|±2000|V|
|V(ESD)|Electrostatic discharge|Charged-device model (CDM), per JEDEC specification<br>JESD22-C101(2)|±750|±750|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**6.3** **Recommended Operating Conditions**

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|VDD|Supply voltage|1.5<br>5.5|V|
|VS or VD|Signal path input/output voltage (source or drain pin), VDD ≥1.5 V(1)|0<br>VDD x 2|V|
|VS_off or VD_off|Signal path input/output voltage (source or drain pin), VDD < 1.5 V(2)|0<br>3.6|V|
|VSEL or VEN|Logic control input voltage (EN, SEL)|0<br>5.5|V|
|TA|Ambient temperature|–40<br>125|ºC|



(1) Device input and output can operate up to V DD x 2, with a maximum input and output voltage of 5.5 V.
(2) V S_off and V D_off refers to the voltage at the source or drain pins when supply is less than 1.5 V.


**6.4** **Thermal Information**







|THERMAL METRIC(1)|Col2|DEVICE|DEVICE|DEVICE|UNIT|
|---|---|---|---|---|---|
|**THERMAL METRIC(1)**|**THERMAL METRIC(1)**|**PW (TSSOP)**|**DYY (SOT-23)**|**RSV (UQFN)**|**RSV (UQFN)**|
|**THERMAL METRIC(1)**|**THERMAL METRIC(1)**|**16 PINS**|**16 PINS**|**16 PINS**|**16 PINS**|
|RθJA|Junction-to-ambient thermal resistance|117.4|123.0|129.2|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|47.9|70.5|69.7|°C/W|
|RθJB|Junction-to-board thermal resistance|63.7|50.4|58.7|°C/W|
|ΨJT|Junction-to-top characterization parameter|6.9|5.0|3.6|°C/W|
|ΨJB|Junction-to-board characterization parameter|63.1|50.3|56.8|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|N/A|N/A|N/A|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
report.


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



5


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**6.5** **Electrical Characteristics**


V DD = 1.5 V to 5.5 V, GND = 0V, T A = –40°C to +125°C
Typical values are at V DD = 3.3 V, T A = 25°C, (unless otherwise noted).














|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|
|VDD|Power supply voltage||1.5<br>5.5|V|
|IDD|Active supply current|VSEL = 0 V, 1.4V or VDD<br>VS = 0 V to 5.5 V|40<br>68|μA|
|IDD_STANDB<br>Y|Supply current when disabled|VEN = 1.4 V or VDD<br>VS = 0 V to 5.5 V|7.5<br>15|µA|
|**DC CHARACTERISTICS**|**DC CHARACTERISTICS**|**DC CHARACTERISTICS**|**DC CHARACTERISTICS**|**DC CHARACTERISTICS**|
|RON|On-resistance|VS = 0 V to VDD*2<br>VS(max) = 5.5 V<br>ISD = 8 mA<br>Refer to ON-State Resistance Figure|2<br>4.5|Ω|
|ΔRON|On-resistance match between channels|VS = VDD<br>ISD = 8 mA<br>Refer to ON-State Resistance Figure|0.07<br>0.28|Ω|
|RON (FLAT)|On-resistance flatness|VS = 0 V to VDD<br>ISD = 8 mA<br>Refer to ON-State Resistance Figure|1<br>1.8|Ω|
|IPOFF|Powered-off I/O pin leakage current|VDD = 0 V<br>VS = 0 V to 3 V<br>VD = 0 V<br>TA = 25℃<br>Refer to Ipoff Leakage Figure|–10<br>0.01<br>10|nA|
|IPOFF|Powered-off I/O pin leakage current|VDD = 0 V<br>VS = 0 V to 3.6 V<br>VD = 0 V<br>Refer to Ipoff Leakage Figure|–2<br>0.01<br>2|µA|
|IS(OFF)<br>ID(OFF)|OFF leakage current|Switch Off<br>VD = 0.8*VDD / 0.2*VDD<br>VS = 0.2*VDD / 0.8*VDD<br>Refer to Off Leakage Figure|–100<br>0.03<br>100|nA|
|ID(ON)<br>IS(ON)|ON leakage current|Switch On<br>VD = 0.8*VDD / 0.2*VDD, S pins floating<br>or<br>VS = 0.8*VDD / 0.2*VDD, D pins floating<br>Refer to On Leakage Figure|–50<br>0.01<br>50|nA|
|**LOGIC INPUTS**|**LOGIC INPUTS**|**LOGIC INPUTS**|**LOGIC INPUTS**|**LOGIC INPUTS**|
|VIH|Input logic high||1.2<br>5.5|V|
|VIL|Input logic low||0<br>0.45|V|
|IIH|Input high leakage current|VSEL = 1.8 V, VDD|1<br>±2|μA|
|IIL|Input low leakage current|VSEL = 0 V|0.2<br>±2|μA|
|RPD|Internal pull-down resistor on logic pins||6|MΩ|
|CI|Logic input capacitance|VSEL = 0 V, 1.8 V or VDD<br>f = 1 MHz|3|pF|



6



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**6.6** **Dynamic Characteristics**


V DD = 1.5 V to 5.5 V, GND = 0V, T A = –40°C to +125°C
Typical values are at V DD = 3.3 V, T A = 25°C, (unless otherwise noted).














|PARAMETER|Col2|TEST CONDITIONS|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|COFF|Source and drain off capacitance|VS = 2.5 V<br>VSEL= 0 V<br>f = 1 MHz<br>Refer to Capacitance Figure|Switch<br>OFF|3.5<br>6|pF|
|CON|Source and drain on capacitance|VS = 2.5 V<br>VSEL= 0 V<br>f = 1 MHz<br>Refer to Capacitance Figure|Switch<br>ON|7.5<br>12|pF|
|QC|Charge Injection|VS = VDD/2<br>RS = 0 Ω, CL =1 nF<br>Refer to Charge Injection Figure|Switch<br>ON|3.5|pC|
|OISO|Off isolation|RL = 50 Ω<br>f = 100 kHz<br>Refer to Off Isolation Figure|Switch<br>OFF|–90|dB|
|OISO|Off isolation|RL = 50 Ω<br>f = 1 MHz<br>Refer to Off Isolation Figure|Switch<br>OFF|–75|dB|
|XTALK|Channel to Channel crosstalk|RL = 50 Ω<br>f = 100 kHz<br>Refer to Crosstalk Figure|Switch<br>ON|–90|dB|
|BW|Bandwidth|RL = 50 Ω<br>Refer to Bandwidth Figure|Switch<br>ON|2|GHz|
|ILOSS|Insertion loss|RL = 50 Ω<br>f = 1 MHz<br>Refer to Bandwidth Figure|Switch<br>ON|–0.12|dB|



Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



7


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**6.7** **Timing Requirements**


V DD = 1.5 V to 5.5 V, GND = 0V, T A = –40°C to +125°C
Typical values are at V DD = 3.3 V, T A = 25°C, (unless otherwise noted).










|PARAMETER|Col2|TEST CONDITIONS|MIN NOM MAX|UNIT|
|---|---|---|---|---|
|tTRAN|Transition time from control input|VDD = 2.5 V to 5.5 V<br>VS = VDD<br>RL = 200 Ω, CL = 15pF<br>Refer to Transition Timing Figure|160<br>350|ns|
|tTRAN|Transition time from control input|VDD < 2.5 V<br>VS = VDD<br>RL = 200 Ω, CL = 15pF<br>Refer to Transition Timing Figure|180<br>580|ns|
|tON(EN)|Device turn on time from enable pin|VS = VDD<br>RL = 200 Ω, CL = 15pF<br>Refer to Ton(EN) & Toff(EN) Figure|12<br>35|µs|
|tOFF(EN)|Device turn off time from enable pin|VS = VDD<br>RL = 200 Ω, CL = 15pF<br>Refer to Ton(EN) & Toff(EN) Figure|50<br>95|ns|
|tON(VDD)|Device turn on time (VDD to output)|VS = 3.6 V<br>VDD rise time = 1us<br>RL = 200 Ω, CL = 15pF<br>Refer to Ton(vdd) & Toff(vdd) Figure|20<br>60|µs|
|tOFF(VDD)|Device turn off time (VDD to output)|VS = 3.6 V<br>VDD fall time = 1us<br>RL = 200 Ω, CL = 15pF<br>Refer to Ton(vdd) & Toff(vdd) Figure|1.2<br>2.7|µs|
|tOPEN (BBM)|Break before make time|VS = 1 V<br>RL = 200 Ω, CL = 15pF<br>Refer to Topen(BBM) Figure|0.5|ns|
|tSK(P)|Inter - channel skew - QFN (RSV)|Refer to Tsk Figure|5|ps|
|tSK(P)|Inter - channel skew - DYY (SOT-23)|Refer to Tsk Figure|9|ps|
|tSK(P)|Inter - channel skew - TSSOP (PW)|Refer to Tsk Figure|18|ps|
|tPD|Propagation delay - QFN (RSV)|Refer to Tpd Figure|50|ps|
|tPD|Propagation delay - DYY (SOT-23)|Refer to Tpd Figure|75|ps|
|tPD|Propagation delay - TSSOP (PW)|Refer to Tpd Figure|95|ps|



8



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**6.8** **Typical Characteristics**


At T A = 25°C, V DD = 5 V (unless otherwise noted).




















|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
||VDD|= 1.5 V|VD|D = 5.5 V||
|||||||
|||VD|D = 3.3 V|||


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||TA = 85qC|TA|= 125qC||
||||||
|TA = -4|0qC|TA|= 25qC||




























|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||T|A = 85qC||TA|= 125qC||
||||||||
||T|A = -40qC||TA|= 25qC||


|Col1|Col2|Col3|
|---|---|---|
|TA = 85qC|TA = 125qC||
||||
|TA = -40qC|TA = 25qC||




















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
||||V|DD =|3.3 V|3.3 V||||||
||||||||V|DD =|5.5 V|||
|||||||||||||
|||||||||||||
|||||||||||||
||||V|DD = 1|.5 V|.5 V||||||
|||||||||||||


|Col1|TA|= 125q|C|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||TA = 85|qC||
||||||||
||T|A = 25q|C||||
||||||||
|= -40qC|||||||









|5<br>4<br>(:)<br>3 Resistance<br>VDD = 1.5 V VDD = 5.5 V<br>2<br>On<br>1<br>VDD = 3.3 V<br>0<br>0 1 2 3 4 5 5.5<br>Source or Drain Voltage (V)<br>D001<br>T = 25°C<br>A<br>Figure 1. On-Resistance vs Source or Drain Voltage|5<br>4<br>(:)<br>3 Resistance<br>TA = 125qC<br>TA = 85qC<br>2<br>On<br>1<br>TA = -40qC TA = 25qC<br>0<br>0 1 2 3 4 5 5.5<br>Source or Drain Voltage (V)<br>D002<br>V = 5.5 V<br>DD<br>Figure 2. On-Resistance vs Source or Drain Voltage|
|---|---|
|Source or Drain Voltage (V)<br>On Resistance (:)<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>0<br>1<br>2<br>3<br>4<br>TA = 25qC<br>TA = 125qC<br>TA = 85qC<br>TA = -40qC<br>D003<br>VDD = 3.3 V<br>**Figure 3. On-Resistance vs Source or Drain Voltage**|Source or Drain Voltage (V)<br>On Resistance (:)<br>0<br>0.5<br>1<br>1.5<br>0<br>1<br>2<br>3<br>4<br>TA = 25qC<br>TA = 125qC<br>TA = 85qC<br>TA = -40qC<br>D004<br>VDD = 1.5 V<br>**Figure 4. On-Resistance vs Source or Drain Voltage**|
|Logic Voltage (V)<br>Supply Current (PA)<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>65<br>VDD = 3.3 V<br>VDD = 5.5 V<br>VDD = 1.5 V<br>D005<br>TA = 25°C<br>**Figure 5. Supply Current vs Logic Voltage**|Supply Voltage (V)<br>Supply Current (PA)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>6<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>TA = 25qC<br>TA = 125qC<br>TA = 85qC<br>TA = -40qC<br>D006<br>**Figure 6. Supply Current vs Supply Voltage**|


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



9


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
|||||||||V<br>|DD = 5<br>|.5 V<br>|
|||||||||~~V~~<br>V|DD~~ =~~<br>DD = 1|~~.3 V~~<br>.5 V|


|V<br>V<br>V|DD = 5.<br>DD = 3.<br>DD = 1.|5 V<br>3 V<br>5 V|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
























|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||VDD =<br>VDD =<br>VDD =|.5 V<br>3.3 V<br>1.5 V|


|Col1|VDD =|5.5 V|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||VDD =<br>|3.3 V<br>|||||||
||~~DD =~~|~~.5 V~~|||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


























|Typical Characteristics (continued)|Col2|
|---|---|
|Source or Drain Voltage (V)<br>On Leakage (pA)<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>-10<br>-5<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>D007<br>VDD = 5.5 V<br>~~V~~DD~~ = 3.3 V~~<br>VDD = 1.5 V<br>TA = 25°C<br>**Figure 7. On-Leakage vs Source or Drain Voltage**|Temperature (qC)<br>On Leakage (nA)<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>-0.5<br>0<br>0.5<br>1<br>1.5<br>2<br>D008<br>VDD = 5.5 V<br>VDD = 3.3 V<br>V~~DD~~ = 1.5 V<br>**Figure 8. On-Leakage vs Temperature**|
|Source Voltage (V)<br>Off Leakage (nA)<br>0<br>1<br>2<br>3<br>4<br>5<br>5.5<br>-0.15<br>-0.1<br>-0.05<br>0<br>0.05<br>0.1<br>D009<br>VDD =  5.5 V<br>VDD =  3.3 V<br>VDD =  1.5 V<br>TA = 25°C<br>**Figure 9. Off-Leakage vs Source or Drain Voltage**|Temperature (qC)<br>Off Leakage (nA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>-0.3<br>0<br>0.3<br>0.6<br>0.9<br>1.2<br>1.5<br>1.8<br>2.1<br>2.4<br>2.7<br>3<br>D010<br>VDD = 5.5 V<br>VDD = 3.3 V<br>~~VDD = 1.5 V~~<br>**Figure 10. Off-Leakage vs Temperature**|
|Source Voltage (V)<br>IPOFF (nA)<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0.8<br>0.9<br>1<br>D011<br>TA = 25°C<br>**Figure 11. IPOFF Leakage vs Source or Drain Voltage**|Temperature (qC)<br>IPOFF Leakage (nA)<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>-2<br>0<br>2<br>4<br>6<br>8<br>10<br>D012<br>VSource = 3 V<br>**Figure 12. IPOFF Leakage vs Temperature**|



10



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
|||||||Tran|siton_F|alling|
|||||||Tran|siton_R|ising|
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Tran|siton_F|alling|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
||||||||~~Tra~~|~~siton_~~|~~ising~~|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||


















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||TO<br>TO|N(VDD)<br>FF(VDD)|
|||||||||
|||||||||












|Typical Characteristics (continued)|Col2|
|---|---|
|Temperature (qC)<br>IPOFF Leakage (nA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>-100<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>700<br>D013<br>VSource = 3.6 V<br>VDrain = 0 V<br>**Figure 13. IPOFF Leakage vs Temperature**|TA = 25°C<br>RL= 200 Ω<br>**Figure 14. IPOFF Leakage vs Source or Drain Voltage**|
|Supply Voltage (V)<br>Transition Time (nS)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>6<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>160<br>180<br>D015<br>Transiton_Falling<br>Transiton_Rising<br>TA = 25°C<br>**Figure 15. TTRANSITION vs Supply Voltage**|Temperature (qC)<br>Transition Time (nS)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>20<br>45<br>70<br>95<br>120<br>145<br>170<br>195<br>220<br>D016<br>Transiton_Falling<br>~~Transiton_Rising~~<br>VDD = 5.5 V<br>**Figure 16. TTRANSITION vs Temperature**|
|Supply Voltage (V)<br>Time (PS)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>5<br>10<br>15<br>20<br>25<br>D017<br>TON(VDD)<br>TOFF(VDD)<br>TA = 25°C<br>**Figure 17. TON (VDD) and TOFF (VDD) vs Supply Voltage**|Supply Voltage (V)<br>Time (PS)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>5<br>10<br>15<br>20<br>25<br>D018<br>TA = 25°C<br>**Figure 18. TON (EN) vs Supply Voltage**|



Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



11


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**
















|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||Propagation Delay - P|Propagation Delay - P|W||
||||||
||||||
||Propagation|Propagation|Delay - D|YY|
|~~opagation Delay - R~~|~~V~~|~~V~~|||
||||||
|Skew - PW|||||
||Skew - DYY|Skew - DYY|Skew -|RSV|
||||||
||||||
||||||
















|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|VDD = 5|.5 V|||
|||||
|VDD = 3.3 V||||
|||||
|V||||
|||||
|||||
|||||


|Col1|Col2|Col3|Col4|C<br>C|SOFF<br>SON|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||


















|Isolation|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|sstalk||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||






|Typical Characteristics (continued)|Col2|
|---|---|
|Supply Voltage (V)<br>Time (nS)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>D019<br>TA = 25°C<br>**Figure 19. TOFF (EN) vs Supply Voltage**|Supply Voltage (V)<br>Time (ps)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Propagation Delay - PW<br>Skew - PW<br>~~Propagation Delay - RSV~~<br>Skew - RSV<br>Propagation Delay - DYY<br>Skew - DYY<br>D020<br>TA = 25°C<br>**Figure 20. Skew and Propagation Delay vs Supply Voltage**|
|Source Voltage (V)<br>Charge Injection (pC)<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>VDD = 5.5 V<br>VDD = 3.3 V<br>VDD = 1.5 V<br>D021<br>TA = 25°C<br>**Figure 21. Charge Injection vs Source Voltage**|Frequency (Hz)<br>Capacitance (pF)<br>0<br>2<br>4<br>6<br>8<br>10<br>1M<br>10M<br>100M<br>1G<br>D022<br>CSOFF<br>CSON<br>TA = 25°C<br>VDD = 1.5 V to 5.5 V<br>**Figure 22. Capacitance vs Frequency**|
|Frequency (Hz)<br>Attenuation (dB)<br>-120<br>-110<br>-100<br>-90<br>-80<br>-70<br>-60<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>100k<br>1M<br>10M<br>100M<br>1G<br>D023<br>Off Isolation<br>Crosstalk<br>TA = 25°C<br>VDD = 3.3 V<br>**Figure 23. Off Isolation and Crosstalk vs Frequency**|Frequency (Hz)<br>Attenuation (dB)<br>-6<br>-5<br>-4<br>-3<br>-2<br>-1<br>0<br>1M<br>10M<br>100M<br>1G<br>D024<br>TA = 25°C<br>VDD = 1.5 V to 5.5 V<br>**Figure 24. On-Response vs Frequency**|



12



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**6.8.1** **Eye Diagrams**







Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



13


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**7** **Parameter Measurement Information**


**7.1** **On-Resistance**


The on-resistance of a device is the ohmic resistance between the source (Sx) and drain (Dx) pins of the device.
The on-resistance varies with input voltage and supply voltage. The symbol R ON is used to denote on-resistance.
The measurement setup used to measure R ON is shown in Figure 27. Voltage (V) and current (I SD ) are measured
using this setup, and R ON is computed as shown below with R ON = V / I SD :











V S


**7.2** **Off-Leakage Current**



**Figure 27. On-Resistance Measurement Setup**



Source leakage current is defined as the leakage current flowing into or out of the source pin when the switch is
off. This current is denoted by the symbol I S (OFF) .


Drain leakage current is defined as the leakage current flowing into or out of the drain pin when the switch is off.
This current is denoted by the symbol I D (OFF) .


The setup used to measure both off-leakage currents is shown in Figure 28.



V DD



V DD





















V S


V S











V D


V D











14



**Figure 28. Off-Leakage Measurement Setup**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**7.3** **On-Leakage Current**


Source on-leakage current is defined as the leakage current flowing into or out of the source pin when the switch
is on. This current is denoted by the symbol I S (ON) .


Drain on-leakage current is defined as the leakage current flowing into or out of the drain pin when the switch is
on. This current is denoted by the symbol I D (ON) .


Either the source pin or drain pin is left floating during the measurement. Figure 29 shows the circuit used for
measuring the on-leakage current, denoted by I S(ON) or I D(ON) .



V DD







N.C.


N.C.


N.C.


N.C.











N.C.


N.C.





V S


V S



V D


V D















V DD







**Figure 29. On-Leakage Measurement Setup**


**7.4** **I** **POFF** **Leakage Current**


I POFF leakage current is defined as the leakage current flowing into or out of the source pin when the device is
powered off. This current is denoted by the symbol I POFF .


The setup used to measure both I POFF leakage current is shown in Figure 30.


V DD









V S


V S





V D


V D









**Figure 30. I** **POFF** **Leakage Measurement Setup**


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



15


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**7.5** **Transition Time**


Transition time is defined as the time taken by the output of the device to rise or fall 10% after the select signal
has risen or fallen past the logic threshold. The 10% transition measurement is utilized to provide the timing of
the device. The time constant from the load resistance and load capacitance can be added to the transition time
to calculate system level timing. Figure 31 shows the setup used to measure transition time, denoted by the
symbol t TRANSITION .


V DD


V DD



ADDRESS
DRIVE t r

(V SEL )













0 V


OUTPUT


0 V

























V SEL



**Figure 31. Transition-Time Measurement Setup**


**7.6** **t** **ON (EN)** **and t** **OFF (EN)** **Time**


The t ON (EN) time is defined as the time taken by the output of the device to rise to 90% after the enable has fallen
past the logic threshold. The 90% measurement is used to provide the timing of the device being enabled in the
system. Figure 32 shows the setup used to measure the enable time, denoted by the symbol t ON (EN) .


The t OFF (EN) time is defined as the time taken by the output of the device to fall to 90% after the enable has fallen
past the logic threshold. The 90% measurement is used to provide the timing of the device being disabled in the
system. Figure 32 shows the setup used to measure enable time, denoted by the symbol t OFF (EN) .


V DD


V DD



DRIVE











0 V







OUTPUT





0 V



V EN


|Col1|VDD<br>S1A<br>D1<br>S1B<br>S4A<br>D4<br>S4B<br>EN<br>GND|
|---|---|
|||



16



**Figure 32. t** **ON (EN)** **and t** **OFF (EN)** **Time Measurement Setup**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**7.7** **t** **ON (VDD)** **and t** **OFF (VDD)** **Time**


The t ON (VDD) time is defined as the time taken by the output of the device to rise to 90% after the supply has
risen past the supply threshold. The 90% measurement is used to provide the timing of the device turning on in
the system. Figure 33 shows the setup used to measure turn on time, denoted by the symbol t ON (VDD) .


the t OFF (VDD) time is defined as the time taken by the output of the device to fall to 90% after the supply has fallen
past the supply threshold. The 90% measurement is used to provide the timing of the device turning off in the
system. Figure 33 shows the setup used to measure turn off time, denoted by the symbol t OFF (VDD) .


V DD



V DD


(V DD )


0 V


OUTPUT


0 V







V DD



















**Figure 33. t** **ON (VDD)** **and t** **OFF (VDD)** **Time Measurement Setup**


**7.8** **Break-Before-Make Delay**


Break-before-make delay is a safety feature that prevents two inputs from connecting when the device is
switching. The output first breaks from the on-state switch before making the connection with the next on-state
switch. The time delay between the _break_ and the _make_ is known as break-before-make delay. Figure 34 shows
the setup used to measure break-before-make delay, denoted by the symbol t OPEN(BBM) .


V DD


V DD



0 V


Output


0 V

|Col1|Col2|Col3|Col4|tBBM 2|
|---|---|---|---|---|
|90%|90%|90%|90%|90%|
|90%||tBBM1|||
||||||



t OPEN (BBM) = min ( t BBM 1, t BBM 2)





V SEL


|Col1|VDD<br>S1A<br>D1<br>S1B<br>S4A<br>D4<br>S4B<br>SEL<br>GND|
|---|---|
|||



**Figure 34. Break-Before-Make Delay Measurement Setup**


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



17


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**7.9** **Propagation Delay**


Propagation delay is defined as the time taken by the output of the device to rise or fall 50% after the input signal
has risen or fallen past the 50% threshold. Figure 35 shows the setup used to measure propagation delay,
denoted by the symbol t PD .


V DD



Input
(V S )



250 mV


0 V















Output


0 V


**7.10** **Skew**



t Prop Delay = max ( t PD 1, t PD 2 )



V S


V S


V S


V S





**Figure 35. Propagation Delay Measurement Setup**



Skew is defined as the difference between propagation delays of any two outputs of the same device. The skew
measurement is taken from the output of one channel rising or falling past 50% to a second channel rising or
falling past the 50% threshold when the input signals are switched at the same time. Figure 36 shows the setup
used to measure skew, denoted by the symbol t SK .


V DD



Output 1


0 V


Output 2


0 V



t SKEW = max ( t SK 1, t SK 2 )















V S


V S


V S


V S





18



**Figure 36. Skew Measurement Setup**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**7.11** **Charge Injection**


The amount of charge injected into the source or drain of the device during the falling or rising edge of the gate
signal is known as charge injection, and is denoted by the symbol Q C . Figure 37 shows the setup used to
measure charge injection from source (Sx) to drain (Dx).


V DD



V DD



V S





OUTPUT



V EN V OUT





0 V


Output


V S


**7.12** **Capacitance**



C L



OUTPUT





V OUT





|Col1|VDD<br>S1A<br>D1<br>S1B<br>S4A<br>D4<br>S4B<br>EN<br>GND|
|---|---|
|||


**Figure 37. Charge-Injection Measurement Setup**



C L



The parasitic capacitance of the device is captured at the source (Sx), drain (Dx), and select (SELx) pins. The
capacitance is measured in both the on and off state and is denoted by the symbol C ON and C OFF . Figure 38
shows the setup used to measure capacitance.


V DD







Capacitance is measured at S X, D X,
and logic pins during ON and OFF
conditions


|1 MHz<br>Capacitance<br>Meter|Col2|
|---|---|
|1 MHz<br>Capacitance<br>Meter||









**Figure 38. Capacitance Measurement Setup**


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



19


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**7.13** **Off Isolation**


Off isolation is defined as the ratio of the signal at the drain pin (Dx) of the device when a signal is applied to the
source pin (Sx) of an off-channel. The characteristic impedance, Z 0, for the measurement is 50 Ω . Figure 39
shows the setup used to measure off isolation. Use off isolation equation to compute off isolation.

















**Figure 39. Off Isolation Measurement Setup**



˜ § V OUT ¨ ¸
© V S ¹



(1)



V
Off Isolation 20 Log˜ ¨
V



OUT



S



**7.14** **Channel-to-Channel Crosstalk**


Crosstalk is defined as the ratio of the signal at the drain pin (Dx) of a different channel, when a signal is applied
at the source pin (Sx) of an on-channel. The characteristic impedance, Z 0, for the measurement is 50 Ω .
Figure 40 shows the setup used to measure, and the equation used to compute crosstalk.





















**Figure 40. Channel-to-Channel Crosstalk Measurement Setup**



˜ § V OUT ¨ ¸
© V S ¹



(2)



V
Channel-to-Channel Crosstalk 20 Log˜ ¨
V



OUT



S



20



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**7.15** **Bandwidth**


Bandwidth is defined as the range of frequencies that are attenuated by less than 3 dB when the input is applied
to the source pin (Sx) of an on-channel, and the output is measured at the drain pin (Dx) of the device. The
characteristic impedance, Z 0, for the measurement is 50 Ω . Figure 41 shows the setup used to measure
bandwidth.


V DD





|0.1µF<br>NETWORK<br>VDD<br>ANALYZER<br>VS<br>S 50Ÿ<br>VSIG<br>D<br>VOUT<br>SxA / SxB / Dx RL<br>50Ÿ<br>GND RL<br>50Ÿ|Col2|
|---|---|
|GND<br>**NETWORK**<br>**ANALYZER**<br>VOUT<br>S<br>D<br>50Ÿ<br>VSIG<br>RL<br>50Ÿ<br>VS<br>VDD<br>0.1µF<br>SxA / SxB / Dx<br>RL<br>50Ÿ|**NETWORK**<br>**ANALYZER**<br>VOUT<br>50Ÿ<br>VSIG<br>RL<br>50Ÿ|
|GND<br>S<br>D<br>VDD<br>SxA / SxB / Dx|GND<br>S<br>D<br>VDD<br>SxA / SxB / Dx|
|||


**Figure 41. Bandwidth Measurement Setup**









#PPAJQ=PEKJ = 20 × .KC ~~(~~ [8] [17][6]
8 5 ~~[)]~~


Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



(3)


21


�



**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**8** **Detailed Description**


**8.1** **Overview**


The TMUX1574 is a high speed 2:1 (SPDT) 4-ch. switch with powered-off protection up to 3.6 V. Wide
operating supply of 1.5 V to 5.5 V allows for use in a wide array of applications from servers and
communication equipment to industrial applications. The device supports bidirectional analog and digital
signals on the source (SxA, SxB) and drain (Dx) pins. The wide bandwidth of this switch allows little or no
attenuation of high-speed signals at the outputs to pass with minimum edge and phase distortion as well as
propagation delay.
The enable (EN) pin is an active-low logic pin that controls the connection between the source (SxA, SxB)
and drain (Dx) pins of the device. The select pin (SEL) controls the state of all four channels of the
TMUX1574 and determines which source pin is connected to the drain. Fail-Safe Logic circuitry allows
voltages on the logic control pins to be applied before the supply pin, protecting the device from potential
damage. All logic control inputs have 1.8V logic compatible thresholds, ensuring both TTL and CMOS logic
compatibility when operating in the valid supply voltage range.
Powered-off protection up to 3.6 V on the signal path of the TMUX1574 provides isolation when the supply
voltage is removed (V DD = 0 V). Without this protection feature, the system can back-power the supply rail
through an internal ESD diode and cause potential damage to the system.


**8.2** **Functional Block Diagram**

�



�



�



S1A
D1
S1B


�



S2A

S2B


S3A

S3B


S4A

S4B


�



D2


D3


D4


�



�



SEL


�



EN


�



*Internal 6MO �Pull-Down on Logic Pins


**8.3** **Feature Description**


**8.3.1** **Bidirectional Operation**


The TMUX1574 conducts equally well from source (SxA, SxB) to drain (Dx) or from drain (Dx) to source (SxA,
SxB). Each channel has very similar characteristics in both directions and supports both analog and digital
signals.


**8.3.2** **Beyond Supply Operation**


When the TMUX1574 is powered from 1.5 V to 5.5 V, the valid signal path input/output voltage ranges from
GND to V DD x 2, with a maximum input/output voltage of 5.5 V.


Example 1: If the TMUX1574 is powered at 1.5V, the signal range is 0 V to 3 V.


Example 2: If the TMUX1574 is powered at 3V, the signal range is 0 V to 5.5 V.


Example 3: If the TMUX1574 is powered at 5.5V, the signal range is 0 V to 5.5 V.


Other voltage levels not mentioned in the examples support Beyond Supply Operation as long as the supply
voltage falls within the recommended operation conditions of 1.5 V to 5.5 V.



�


22



�


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**Feature Description (continued)**


**8.3.3** **1.8 V Logic Compatible Inputs**


The TMUX1574 has 1.8-V logic compatible control inputs. Regardless of the V DD voltage, the control input
thresholds remain fixed, allowing a 1.8-V processor GPIO to control the TMUX1574 without the need for an
external translator. This saves both space and BOM cost. For more information on 1.8 V logic implementations,
refer to _[Simplifying Design with 1.8 V logic Muxes and Switches.](http://www.ti.com/lit/pdf/SCAA126)_


**8.3.4** **Powered-off Protection**


Powered-off protection up to 3.6 V on the signal path of the TMUX1574 provides isolation when the supply
voltage is removed (V DD = 0 V). When the TMUX1574 is powered-off, the I/Os of the device remain in a high-Z
state. Powered-off protection minimizes system complexity by removing the need for power supply sequencing
on the signal path. The device performance remains within the leakage performance mentioned in the Electrical
Specifications. For more information on powered-off protection, refer to _[Eliminate Power Sequencing with](http://www.ti.com/lit/pdf/SCDA015A)_
_[Powered-off Protection Signal Switches](http://www.ti.com/lit/pdf/SCDA015A)_ .


**8.3.5** **Fail-Safe Logic**


The TMUX1574 has Fail-Safe Logic on the control input pins (SELx) which allows for operation up to 5.5 V,
regardless of the state of the supply pin. This feature allows voltages on the control pins to be applied before the
supply pin, protecting the device from potential damage. Fail-Safe Logic minimizes system complexity by
removing the need for power supply sequencing on the logic control pins. For example, the Fail-Safe Logic
feature allows the select pins of the TMUX1574 to be ramped to 5.5 V while V DD = 0 V. Additionally, the feature
enables operation of the TMUX1574 with V DD = 1.5 V while allowing the select pins to interface with a logic level
of another device up to 5.5 V.


**8.3.6** **Low Capacitance**


The TMUX1574 has very low capacitance in both the ON and OFF states on the source and drain pins. Low
capacitance helps to reduce large overshoots and ringing of an amplifier circuit when the switch is connected to
the feedback network. Additionally, low capacitance improves system settling time by reducing the switch time
constant formed by the On-resistance and On-capacitance. For more information on the benefits of low
capacitance refer to _[Improve Stability Issues with Low C](http://www.ti.com/lit/pdf/SCAA128)_ _ON_ _Multiplexers._


**8.3.7** **Integrated Pull-Down Resistors**


The TMUX1574 has internal weak pull-down resistors (6 M Ω ) to GND to ensure the logic pins are not left
floating. This feature integrates up to four external components and reduces system size and cost.



Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



23


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**8.4** **Device Functional Modes**


The enable (EN) pin is an active-low logic pin that controls the connection between the source (SxA, SxB) and
drain (Dx) pins of the device. When the enable pin is pulled high, all switches are turned off. When the enable is
pulled low, the select pin controls the signal path selection. The select pin (SEL) controls the state of all four
channels of the TMUX1574 and determines which source pin is connected to the drain pins. When the select pin
is pulled low, the SxA pin conducts to the corresponding Dx pins. When the select pin is pulled high, the SxB pin
conducts to the corresponding Dx pins. The TMUX1574 logic pins have internal weak pull-down resistors (6 M Ω )
to GND so that it powers-on in a known state.


The TMUX1574 can be operated without any external components except for the supply decoupling capacitors.
Unused logic control pins should be tied to GND or V DD in order to ensure the device does not consume
additional current as highlighted in _[Implications of Slow or Floating CMOS Inputs](http://www.ti.com/lit/pdf/SCBA004D)_ . Unused signal path inputs
(SxA, SxB, or Dx) should be connected to GND.


**8.5** **Truth Tables**


**Table 1. TMUX1574 Truth Table**






|INPUTS|Col2|Selected Source Pins Connected To Drain Pins (Dx)|
|---|---|---|
|**EN**|**SEL**|**SEL**|
|0|0|S1A connected to D1<br>S2A connected to D2<br>S3A connected to D3<br>S4A connected to D4|
|0|1|S1B connected to D1<br>S2B connected to D2<br>S3B connected to D3<br>S4B connected to D4|
|1|X(1)|Hi-Z (OFF)|



24



(1) X denotes _don't care_ .


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**9** **Application and Implementation**


**NOTE**
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TI’s customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.


**9.1** **Application Information**


The TMUX15xx family offers high-speed system performance across a wide operating supply (1.5 V to 5.5 V)
and operating temperature (-40°C to +125°C). The TMUX1574 supports a number of features that improve
system performance such as 1.8 V logic compatibility, supports input voltages beyond supply, Fail-Safe Logic,
and Powered-off Protection up to 3.6 V. These features make the TMUX15xx a family of protection multiplexers
and switches that can reduce system complexity, board size, and overall system cost.


**9.2** **Typical Application**


Common applications that require the features of the TMUX1574 include multiplexing various protocols from a
possessor or MCU such as SPI, JTAG, or standard GPIO signals. The TMUX1574 provides superior isolation
performance when the device is powered. The added benefit of powered-off protection allows a system to
minimize complexity by eliminating the need for power sequencing in hot-swap and live insertion applications.
The example shown in Figure 42 illustrates the use of the TMUX1574 to multiplex an SPI bus to multiple flash
memory devices.



1.8 V



3.3 V 0.1µF 3.3 V

























**Figure 42. Multiplexing Flash Memory**


**9.2.1** **Design Requirements**


For this design example, use the parameters listed in Table 2.


**Table 2. Design Parameters**

|PARAMETERS|VALUES|
|---|---|
|Supply (VDD)|3.3 V|
|Input / Output signal range|0 V to 3.3 V|
|Control logic thresholds|1.8 V compatible|



Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



25


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**9.2.2** **Detailed Design Procedure**


The TMUX1574 can be operated without any external components except for the supply decoupling capacitors.
The TMUX1574 has internal weak pull-down resistors (6 M Ω ) to GND so that it powers-on with the switches in a
known state. All inputs signals passing through the switch must fall within the recommend operating conditions of
the TMUX1574 including signal range and continuous current. For this design example, with a supply of 3.3 V,
the signals can range from 0 V to 3.3 V when the device is powered. This example can also utilize the Poweredoff Protection feature and the inputs can range from 0 V to 3.6 V when V DD = 0 V. The max continuous current
can be 25 mA. Due to the voltage range and high speed capability, the TMUX1574 example is suitable for use in
SPI, JTAG, and I2S applications. Refer to _[Enabling SPI-based flash memory expansion by using multiplexers](http://www.ti.com/lit/pdf/SCDA016)_ for
more information on using switches and multiplexers for SPI protocol expansion.


**9.2.3** **Application Curves**


Two important specifications when using a switch or multiplexer to pass signals are the device propagation delay
and skew.


100



90


80


70


60


50


40


30


20


10











0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||Propa|gation D|elay - P|elay - P|W||
||||||||||
||||||||||
|~~Propa~~|~~gation~~|~~elay -~~|~~SV~~|Prop|agation|agation|Delay -|DYY|
||||||||||
||||||||||
||Skew|- PW|||||||
||||S|kew - D|YY|YY|Skew -|RSV|
||||||||||
||||||||||
||||||||||



1.5 2 2.5 3 3.5 4 4.5 5 5.5



Supply Voltage (V)



D020



**Figure 43. Propagation Delay and Skew Measurement**


**10** **Power Supply Recommendations**


The TMUX1574 operates across a wide supply range of 1.5 V to 5.5 V. Do not exceed the absolute maximum
ratings because stresses beyond the listed ratings can cause permanent damage to the devices.


Power-supply bypassing improves noise margin and prevents switching noise propagation from the V DD supply to
other components. Good power-supply decoupling is important to achieve optimum performance. For improved
supply noise immunity, use a supply decoupling capacitor ranging from 0.1 μ F to 10 μ F from V DD to ground.
Place the bypass capacitors as close to the power supply pins of the device as possible using low-impedance
connections. TI recommends using multi-layer ceramic chip capacitors (MLCCs) that offer low equivalent series
resistance (ESR) and inductance (ESL) characteristics for power-supply decoupling purposes. For very sensitive
systems, or for systems in harsh noise environments, avoiding the use of vias for connecting the capacitors to
the device pins may offer superior noise immunity. The use of multiple vias in parallel lowers the overall
inductance and is beneficial for connections to ground planes.



26



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**11** **Layout**


**11.1** **Layout Guidelines**


When a PCB trace turns a corner at a 90° angle, a reflection can occur. A reflection occurs primarily because of
the change of width of the trace. At the apex of the turn, the trace width increases to 1.414 times the width. This
increase upsets the transmission-line characteristics, especially the distributed capacitance and self–inductance
of the trace which results in the reflection. Not all PCB traces can be straight and therefore some traces must
turn corners.Figure 44 shows progressively better techniques of rounding corners. Only the last example (BEST)
maintains constant trace width and minimizes reflections.



WORST BETTER BEST


|W|Col2|
|---|---|
|1W min.<br>||
|||



W


**Figure 44. Trace Example**


Route the high-speed signals using a minimum of vias and corners which reduces signal reflections and
impedance changes. When a via must be used, increase the clearance size around it to minimize its
capacitance. Each via introduces discontinuities in the signal’s transmission line and increases the chance of
picking up interference from the other layers of the board. Be careful when designing test points, throughhole pins are not recommended at high frequencies.
Do not route high speed signal traces under or near crystals, oscillators, clock signal generators, switching
regulators, mounting holes, magnetic devices or ICs that use or duplicate clock signals.
Avoid stubs on the high-speed signals traces because they cause signal reflections.
Route all high-speed signal traces over continuous GND planes, with no interruptions.
Avoid crossing over anti-etch, commonly found with plane splits.
When working with high frequencies, a printed circuit board with at least four layers is recommended; two
signal layers separated by a ground and power layer as shown in Figure 45.


Power Plane

|Col1|Col2|Col3|Signal|
|---|---|---|---|
|||||
||||GND|
|||||
||||Power|
|||||
|||Signal|Signal|



**Figure 45. Example Layout**


The majority of signal traces must run on a single layer, preferably Signal 1. Immediately next to this layer must
be the GND plane, which is solid with no cuts. Avoid running signal traces across a split in the ground or power
plane. When running across split planes is unavoidable, sufficient decoupling must be used. Minimizing the
number of signal vias reduces EMI by reducing inductance at high frequencies.


Figure 46 illustrates an example of a PCB layout with the TMUX1574. Some key considerations are:



Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



27


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Layout Guidelines (continued)**


Decouple the V DD pin with a 0.1- μ F capacitor, placed as close to the pin as possible. Make sure that the
capacitor voltage rating is sufficient for the V DD supply.


High-speed switches require proper layout and design procedures for optimum performance.


Keep the input lines as short as possible.


Use a solid ground plane to help reduce electromagnetic interference (EMI) noise pickup.


Do not run sensitive analog traces in parallel with digital traces. Avoid crossing digital and analog traces if
possible, and only make perpendicular crossings when necessary.


**11.2** **Layout Example**


Wide (low inductance)
trace for power





























28



**Figure 46. Example Layout**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


**[www.ti.com](http://www.ti.com)** SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019


**12** **Device and Documentation Support**


**12.1** **Documentation Support**


**12.1.1** **Related Documentation**


Texas Instruments, _[Improve Stability Issues with Low CON Multiplexers](http://www.ti.com/lit/pdf/SCAA128)_ .


Texas Instruments, _[Enabling SPI-based flash memory expansion by using multiplexers](http://www.ti.com/lit/pdf/SCDA016)_ .


Texas Instruments, _[Simplifying Design with 1.8 V logic Muxes and Switches](http://www.ti.com/lit/pdf/SCAA126)_ .


Texas Instruments, _[Eliminate Power Sequencing with Powered-off Protection Signal Switches](http://www.ti.com/lit/pdf/SCDA015A)_ .


Texas Instruments, _[System-Level Protection for High-Voltage Analog Multiplexers](http://www.ti.com/lit/pdf/SBAA227)_ .


Texas Instruments, _[High-Speed Interface Layout Guidelines](http://www.ti.com/lit/pdf/SPRAAR7G)_ .


Texas Instruments, _[High-Speed Layout Guidelines](http://www.ti.com/lit/pdf/SCAA082A)_ .


Texas Instruments, _[QFN/SON PCB Attachment](http://www.ti.com/lit/pdf/SLUA271)_ .


Texas Instruments, _[Quad Flatpack No-Lead Logic Packages](http://www.ti.com/lit/pdf/SCBA017)_ .


**12.2** **Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on _Alert me_ to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document.


**12.3** **Community Resources**


[TI E2E™support forums are an engineer's go-to source for fast, verified answers and design help — straight](http://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](http://www.ti.com/corp/docs/legal/termsofuse.shtml)


**12.4** **Trademarks**

E2E is a trademark of Texas Instruments.


**12.5** **Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with
appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more
susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.


**12.6** **Glossary**


[SLYZ022 —](http://www.ti.com/lit/pdf/SLYZ022) _TI Glossary_ .

This glossary lists and explains terms, acronyms, and definitions.



Copyright © 2018–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_



29


**[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)**


SCDS391C –OCTOBER 2018–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**13** **Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.



30



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SCDS391C&partnum=TMUX1574)_ Copyright © 2018–2019, Texas Instruments Incorporated


Product Folder Links: _[TMUX1574](http://www.ti.com/product/tmux1574?qgpn=tmux1574)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 24-Jul-2025


**PACKAGING INFORMATION**

























**(1)** **Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)


**(2)** **Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.


**(3)** **RoHS values:** [Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.](https://www.ti.com/lit/szzq088)


**(4)** **Lead finish/Ball material:** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 24-Jul-2025


**(5)** **MSL rating/Peak reflow:** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.


**(6)** **Part marking:** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 24-Jul-2025


**TAPE AND REEL INFORMATION**



**REEL DIMENSIONS**


*All dimensions are nominal







**TAPE DIMENSIONS**


|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||B0W|
||||||||
||||||||
|vity|vity|vity|A0|A0|||






|A0|Dimension designed to accommodate the component width A0 Cavity|
|---|---|
|A0<br>|Dimension designed to accommodate the component width|
|B0<br>|Dimension designed to accommodate the component length<br><br>|
|K0<br>|Dimension designed to accommodate the component thickness<br>|
|W<br>|Overall width of the carrier tape<br>|
|P1|Pitch between successive cavity centers|



Reel Width (W1)


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
|TMUX1574DYYR|SOT-23-<br>THIN|DYY|16|3000|330.0|12.4|4.8|3.6|1.6|8.0|12.0|Q3|
|TMUX1574DYYRG4|SOT-23-<br>THIN|DYY|16|3000|330.0|12.4|4.8|3.6|1.6|8.0|12.0|Q3|
|TMUX1574PWR|TSSOP|PW|16|2000|330.0|12.4|6.9|5.6|1.6|8.0|12.0|Q1|
|TMUX1574PWRG4|TSSOP|PW|16|2000|330.0|12.4|6.9|5.6|1.6|8.0|12.0|Q1|
|TMUX1574RSVR|UQFN|RSV|16|3000|178.0|13.5|2.1|2.9|0.75|4.0|12.0|Q1|
|TMUX1574T8RSVR|UQFN|RSV|16|3000|180.0|9.5|2.1|2.9|0.75|4.0|8.0|Q1|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 24-Jul-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TMUX1574DYYR|SOT-23-THIN|DYY|16|3000|336.6|336.6|31.8|
|TMUX1574DYYRG4|SOT-23-THIN|DYY|16|3000|336.6|336.6|31.8|
|TMUX1574PWR|TSSOP|PW|16|2000|353.0|353.0|32.0|
|TMUX1574PWRG4|TSSOP|PW|16|2000|353.0|353.0|32.0|
|TMUX1574RSVR|UQFN|RSV|16|3000|189.0|185.0|36.0|
|TMUX1574T8RSVR|UQFN|RSV|16|3000|189.0|185.0|36.0|



Pack Materials-Page 2


## **PACKAGE OUTLINE** **DYY0016A SOT-23-THIN - 1.1 mm max height**

PLASTIC SMALL OUTLINE



































NOTES:


1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed
0.15 per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.50 per side.
5. Reference JEDEC Registration MO-345, Variation AA


**www.ti.com**


## **EXAMPLE BOARD LAYOUT** **DYY0016A SOT-23-THIN - 1.1 mm max height**

PLASTIC SMALL OUTLINE












|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||























NOTES: (continued)


6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


**www.ti.com**


## **EXAMPLE STENCIL DESIGN** **DYY0016A SOT-23-THIN - 1.1 mm max height**

PLASTIC SMALL OUTLINE
















|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||





NOTES: (continued)
8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.


**www.ti.com**


## **PACKAGE OUTLINE**

# **PW0016A TSSOP - 1.2 mm max height**

~~SCALE 2.500~~


SMALL OUTLINE PACKAGE























NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-153.


www.ti.com


## **EXAMPLE BOARD LAYOUT**

# **PW0016A TSSOP - 1.2 mm max height**

SMALL OUTLINE PACKAGE































NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**

# **PW0016A TSSOP - 1.2 mm max height**

SMALL OUTLINE PACKAGE

















NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.


www.ti.com


## **GENERIC PACKAGE VIEW**

# **RSV 16 UQFN - 0.55 mm max height**

**1.8 x 2.6, 0.4 mm pitch** ULTRA THIN QUAD FLATPACK - NO LEAD


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4231225/A


www.ti.com


## **PACKAGE OUTLINE**

# **RSV0016A UQFN - 0.55 mm max height**

~~SCALE 5.000~~


ULTRA THIN QUAD FLATPACK - NO LEAD


























|16X|0.25 0.15|Col3|Col4|Col5|
|---|---|---|---|---|
||0.07|C|A|B|
||0.05|0.05|0.05|0.05|



NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.


www.ti.com


## **EXAMPLE BOARD LAYOUT**

# **RSV0016A UQFN - 0.55 mm max height**

ULTRA THIN QUAD FLATPACK - NO LEAD































NOTES: (continued)

3. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).


www.ti.com


## **EXAMPLE STENCIL DESIGN**

# **RSV0016A UQFN - 0.55 mm max height**

ULTRA THIN QUAD FLATPACK - NO LEAD













NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


www.ti.com


**IMPORTANT NOTICE AND DISCLAIMER**


TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS”
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.


These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.


These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you
will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these

resources.


[TI’s products are provided subject to TI’s Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with](https://www.ti.com/legal/terms-conditions/terms-of-sale.html)
such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for
TI products.


TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE


Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2025, Texas Instruments Incorporated


