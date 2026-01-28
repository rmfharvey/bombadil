Reference
Design



Technical

Documents



Support &
Community



Product

Folder



Order

Now



Tools &
Software



**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019

### **LM5050-1, LM5050-1-Q1 High-Side OR-ing FET Controller**



**1** **Features**


1• Available in Standard and AEC-Q100 Qualified
Versions LM5050Q0MK-1 (up to 150°C TJ) and
LM5050Q1MK-1 (up to 125°C TJ)

- [Functional safety capable](http://www.ti.com/technologies/functional-safety/overview.html)

  - Documentation available to aid functional
safety system design

- Wide Operating Input Voltage Range, VIN: 1 V to
75 V (VBIAS required for VIN < 5 V)

- 100-V Transient Capability

- Charge Pump Gate Driver for External N-Channel
MOSFET

- Fast 50-ns Response to Current Reversal

- 2-A Peak Gate Turnoff Current

- Minimum VDS Clamp for Faster Turnoff

- Package: SOT-6 (Thin SOT-23-6)


**2** **Applications**
Active OR-ing of Redundant (N+1) Power
Supplies



**3** **Description**
The LM5050-1/-Q1 High Side OR-ing FET Controller
operates in conjunction with an external MOSFET as
an ideal diode rectifier when connected in series with
a power source. This ORing controller allows
MOSFETs to replace diode rectifiers in power
distribution networks thus reducing both power loss
and voltage drops.


The LM5050-1/-Q1 controller provides charge pump
gate drive for an external N-Channel MOSFET and a
fast response comparator to turn off the FET when
current flows in the reverse direction. The LM5050-1/Q1 can connect power supplies ranging from 5 V to
75 V and can withstand transients up to 100 V.


**Device Information** **[(1)]**

|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|LM5050-1|SOT (6)|2.90 mm × 1.60 mm|
|LM5050-1-Q1|LM5050-1-Q1|LM5050-1-Q1|



(1) For all available packages, see the orderable addendum at

the end of the data sheet.



**Full Application**





Shutdown









**Typical Redundant Supply Configuration**





















1



An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Table of Contents**



**1** **Features** .................................................................. 1
**2** **Applications** ........................................................... 1
**3** **Description** ............................................................. 1
**4** **Revision History** ..................................................... 2
**5** **Pin Configuration and Functions** ......................... 3
**6** **Specifications** ......................................................... 4

6.1 Absolute Maximum Ratings ...................................... 4
6.2 ESD Ratings: LM5050-1 .......................................... 4
6.3 ESD Ratings: LM5050-1-Q1 ..................................... 4
6.4 Recommended Operating Conditions....................... 4
6.5 Thermal Information.................................................. 4
6.6 Electrical Characteristics........................................... 5
6.7 Typical Characteristics.............................................. 8
**7** **Detailed Description** ............................................ 11

7.1 Overview ................................................................. 11
7.2 Functional Block Diagram ....................................... 12
7.3 Feature Description................................................. 12



7.4 Device Functional Modes........................................ 13
**8** **Application and Implementation** ........................ 14

8.1 Application Information............................................ 14
8.2 Typical Applications ................................................ 16
**9** **Power Supply Recommendations** ...................... 21
**10** **Layout** ................................................................... 21
10.1 Layout Guidelines ................................................. 21
10.2 Layout Example .................................................... 21
**11** **Device and Documentation Support** ................. 22
11.1 Documentation Support ........................................ 22
11.2 Related Links ........................................................ 22
11.3 Community Resources.......................................... 22
11.4 Trademarks........................................................... 22
11.5 Electrostatic Discharge Caution............................ 22
11.6 Glossary................................................................ 22
**12** **Mechanical, Packaging, and Orderable**
**Information** ........................................................... 22



**4** **Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision E (December 2015) to Revision F** **Page**


- Added Functional safety capable link to the _Features_ section............................................................................................... 1


**Changes from Revision D (June 2013) to Revision E** **Page**


- Added _ESD Ratings_ table, _Feature Description_ section, _Device Functional Modes_, _Application and Implementation_
section, _Power Supply Recommendations_ section, _Layout_ section, _Device and Documentation Support_ section, and
_Mechanical, Packaging, and Orderable Information_ section ................................................................................................. 1



2



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**5** **Pin Configuration and Functions**


**DDC Package**

**6-Pin SOT**



6


5


4



OUT


GATE


IN



VS


GND


OFF



1


2


3


|Col1|Col2|Top View|Col4|
|---|---|---|---|
|||||
|||**L**||
|||**M50**|**M50**|
|||**50**||
|||**MK**|**MK**|
|||**-1**||
|||||



**Pin Functions**







|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**NO.**|**NAME**|**NAME**|**NAME**|
|1|VS|I|The main supply pin for all internal biasing and an auxiliary supply for the internal gate drive<br>charge pump. Typically connected to either VOUT or VIN; a separate supply can also be used.|
|2|GND|PWR|Ground return for the controller|
|3|OFF|I|A logic high state at the OFF pin will pull the GATE pin low and turn off the external MOSFET.<br>Note that when the MOSFET is off, current will still conduct through the FET's body diode. This<br>pin should may be left open or connected to GND if unused.|
|4|IN|I|Voltage sense connection to the external MOSFET Source pin.|
|5|GATE|O|Connect to the Gate of the external MOSFET. Controls the MOSFET to emulate a low forward-<br>voltage diode.|
|6|OUT|O|Voltage sense connection to the external MOSFET Drain pin.|


Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



3


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**6** **Specifications**


**6.1** **Absolute Maximum Ratings**

over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|MIN MAX|UNIT|
|---|---|---|
|IN, OUT Pins to Ground(2)|–0.3<br>100|V|
|GATE Pin to Ground(2)|–0.3<br>100|V|
|VS Pin to Ground|–0.3<br>100|V|
|OFF Pin to Ground|–0.3<br>7|V|
|Storage Temperature|−65<br>150|°C|



(1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under _Recommended_
_Operating Conditions_ . Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The GATE pin voltage is typically 12 V above the IN pin voltage when the LM5050-1 is enabled (that is, OFF Pin is Open or Low, and
VIN > VOUT). Therefore, the absolute maximum rating for the IN pin voltage applies only when the LM5050-1 is disabled (that is, OFF
Pin is logic high), or for a momentary surge to that voltage because the Absolute Maximum Rating for the GATE pin is also 100 V


**6.2** **ESD Ratings: LM5050-1**






|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)<br>Electrostatic discharge|Machine model (MM)(2)|±150|±150|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) The MM is a 200-pF capacitor discharged through a 0- Ω resistor (that is, directly) into each pin. Applicable test standard is JESD-A115A.


**6.3** **ESD Ratings: LM5050-1-Q1**






|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic discharge|Human-body model (HBM), per AEC Q100-002(1)|±2000|V|
|V(ESD)<br>Electrostatic discharge|Machine model (MM)(2)|±150|±150|



(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.
(2) The MM is a 200-pF capacitor discharged through a 0- Ω resistor (that is, directly) into each pin. Applicable test standard is JESD-A115A.


**6.4** **Recommended Operating Conditions**


over operating free-air temperature range (unless otherwise noted)



|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|IN, OUT, VS Pins|IN, OUT, VS Pins|5<br>75|V|
|OFF Pin|OFF Pin|0<br>5.5|V|
|Junction Temperature (TJ)|Standard Grade|−40<br>125|°C|
|Junction Temperature (TJ)|LM5050Q0MK-1|−40<br>150|°C|
|Junction Temperature (TJ)|LM5050Q1MK-1|−40<br>125|°C|


**6.5** **Thermal Information**









|THERMAL METRIC(1)|LM5050-1/-Q1|UNIT|
|---|---|---|
|**THERMAL METRIC(1)**|**DDC (SOT)**|**DDC (SOT)**|
|**THERMAL METRIC(1)**|**6 PINS**|**6 PINS**|
|RθJA<br>Junction-to-ambient thermal resistance|180.7|°C/W|
|RθJC(top)<br>Junction-to-case (top) thermal resistance|41.3|°C/W|
|RθJB<br>Junction-to-board thermal resistance|28.2|°C/W|
|ψJT<br>Junction-to-top characterization parameter|0.7|°C/W|
|ψJB<br>Junction-to-board characterization parameter|27.8|°C/W|


(1) For more information about traditional and new thermal metrics, see the _Semiconductor and IC Package Thermal Metrics_ application
[report, SPRA953.](http://www.ti.com/lit/pdf/spra953)



4



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**Thermal Information (continued)**







|THERMAL METRIC(1)|LM5050-1/-Q1|UNIT|
|---|---|---|
|**THERMAL METRIC(1)**|**DDC (SOT)**|**DDC (SOT)**|
|**THERMAL METRIC(1)**|**6 PINS**|**6 PINS**|
|RθJC(bot)<br>Junction-to-case (bottom) thermal resistance|N/A|°C/W|


**6.6** **Electrical Characteristics**


Typical values represent the most likely parametric norm at TJ = 25°C, and are provided for reference purposes only. Unless
















































|PARAMETER|TEST CONDITIONS|Col3|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|**VS PIN**|**VS PIN**|**VS PIN**|**VS PIN**|**VS PIN**|**VS PIN**|
|VVS<br>Operating<br>Supply Voltage<br>Range|TJ = –40°C to 125°C|TJ = –40°C to 125°C|TJ = –40°C to 125°C|5<br>75|V|
|IVS<br>Operating<br>Supply Current|VVS= 5 V, VIN = 5 V<br>VOUT = VIN - 100 mV|TJ = 25°C|TJ = 25°C|75|μA|
|IVS<br>Operating<br>Supply Current|VVS= 5 V, VIN = 5 V<br>VOUT = VIN - 100 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|105|105|
|IVS<br>Operating<br>Supply Current|VVS= 12 V, VIN = 12 V<br>VOUT = VIN - 100 mV|TJ = 25°C|TJ = 25°C|100|100|
|IVS<br>Operating<br>Supply Current|VVS= 12 V, VIN = 12 V<br>VOUT = VIN - 100 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|147|147|
|IVS<br>Operating<br>Supply Current|VVS= 75 V, VIN = 75 V<br>VOUT = VIN - 100 mV|TJ = 25°C|TJ = 25°C|130|130|
|IVS<br>Operating<br>Supply Current|VVS= 75 V, VIN = 75 V<br>VOUT = VIN - 100 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|288|288|
|**IN PIN**|**IN PIN**|**IN PIN**|**IN PIN**|**IN PIN**|**IN PIN**|
|VIN<br>Operating Input<br>Voltage Range|TJ = –40°C to 125°C|TJ = –40°C to 125°C|TJ = –40°C to 125°C|5<br>75|V|
|IIN<br>IN Pin current|VIN = 5 V<br>VVS= VIN<br>VOUT = VIN - 100 mV<br>GATE = Open|TJ = 25°C|TJ = 25°C|190|μA|
|IIN<br>IN Pin current|VIN = 5 V<br>VVS= VIN<br>VOUT = VIN - 100 mV<br>GATE = Open|TJ = –40°C to 125°C|TJ = –40°C to 125°C|32<br>305|32<br>305|
|IIN<br>IN Pin current|VIN = 12 V to 75 V<br>VVS= VIN<br>VOUT = VIN - 100 mV<br>GATE = Open|TJ = 25°C|TJ = 25°C|320|320|
|IIN<br>IN Pin current|VIN = 12 V to 75 V<br>VVS= VIN<br>VOUT = VIN - 100 mV<br>GATE = Open|TJ = –40°C to 125°C|LM5050MK-1,<br>LM5050Q1MK-1|233<br>400|233<br>400|
|IIN<br>IN Pin current|VIN = 12 V to 75 V<br>VVS= VIN<br>VOUT = VIN - 100 mV<br>GATE = Open|TJ = –40°C to 125°C|LM5050Q0MK-1|233<br>475|233<br>475|
|**OUT PIN**|**OUT PIN**|**OUT PIN**|**OUT PIN**|**OUT PIN**|**OUT PIN**|
|VOUT<br>Operating<br>Output Voltage<br>Range|TJ = –40°C to 125°C|TJ = –40°C to 125°C|TJ = –40°C to 125°C|5<br>75|V|
|IOUT<br>OUT Pin Current|VIN = 5 V to 75 V<br>VVS= VIN<br>VOUT = VIN - 100 mV|TJ = 25°C|TJ = 25°C|3.2|µA|
|IOUT<br>OUT Pin Current|VIN = 5 V to 75 V<br>VVS= VIN<br>VOUT = VIN - 100 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|8|8|
|**GATE PIN**|**GATE PIN**|**GATE PIN**|**GATE PIN**|**GATE PIN**|**GATE PIN**|
|IGATE(ON)<br>Gate Pin Source<br>Current|VIN = 5 V<br>VVS = VIN<br>VGATE = VIN<br>VOUT = VIN - 175 mV|TJ = 25°C|TJ = 25°C|30|µA|
|IGATE(ON)<br>Gate Pin Source<br>Current|VIN = 5 V<br>VVS = VIN<br>VGATE = VIN<br>VOUT = VIN - 175 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|12<br>41|12<br>41|
|IGATE(ON)<br>Gate Pin Source<br>Current|VIN = 12 V to 75 V<br>VVS = VIN<br>VGATE = VIN<br>VOUT = VIN - 175 mV|TJ = 25°C|TJ = 25°C|32|32|
|IGATE(ON)<br>Gate Pin Source<br>Current|VIN = 12 V to 75 V<br>VVS = VIN<br>VGATE = VIN<br>VOUT = VIN - 175 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|20<br>41|20<br>41|
|VGS<br>VGATE - VIN in<br>Forward<br>Operation(1)|VIN = 5 V<br>VVS = VIN<br>VOUT = VIN - 175 mV|TJ = 25°C|TJ = 25°C|7|V|
|VGS<br>VGATE - VIN in<br>Forward<br>Operation(1)|VIN = 5 V<br>VVS = VIN<br>VOUT = VIN - 175 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|4<br>9|4<br>9|
|VGS<br>VGATE - VIN in<br>Forward<br>Operation(1)|VIN = 12 V to 75 V<br>VVS = VIN<br>VOUT = VIN - 175 mV|TJ = 25°C|TJ = 25°C|12|12|
|VGS<br>VGATE - VIN in<br>Forward<br>Operation(1)|VIN = 12 V to 75 V<br>VVS = VIN<br>VOUT = VIN - 175 mV|TJ = –40°C to 125°C|TJ = –40°C to 125°C|9<br>14|9<br>14|



(1) Measurement of VGS voltage (that is. VGATE - VIN) includes 1 M Ω in parallel with CGATE.


Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



5


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Electrical Characteristics (continued)**


Typical values represent the most likely parametric norm at TJ = 25°C, and are provided for reference purposes only. Unless













































|PARAMETER|TEST CONDITIONS|Col3|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|tGATE(REV)<br>Gate<br>Capacitance<br>Discharge Time<br>at Forward to<br>Reverse<br>Transition<br>See Figure 1|CGATE = 0(2)|TJ = 25°C|TJ = 25°C|25|ns|
|tGATE(REV)<br>Gate<br>Capacitance<br>Discharge Time<br>at Forward to<br>Reverse<br>Transition<br>See Figure 1|CGATE = 0(2)|TJ = –40°C to 125°C|TJ = –40°C to 125°C|85|85|
|tGATE(REV)<br>Gate<br>Capacitance<br>Discharge Time<br>at Forward to<br>Reverse<br>Transition<br>See Figure 1|CGATE = 10 nF(2)|TJ = 25°C|TJ = 25°C|60|60|
|tGATE(REV)<br>Gate<br>Capacitance<br>Discharge Time<br>at Forward to<br>Reverse<br>Transition<br>See Figure 1|CGATE = 47 nF(2)|TJ = 25°C|TJ = 25°C|180|180|
|tGATE(REV)<br>Gate<br>Capacitance<br>Discharge Time<br>at Forward to<br>Reverse<br>Transition<br>See Figure 1|CGATE = 47 nF(2)|TJ = –40°C to 125°C|TJ = –40°C to 125°C|350|350|
|tGATE(OFF)<br>Gate<br>Capacitance<br>DischargeTime<br>at OFF pin Low<br>to High<br>Transition<br>See Figure 2|CGATE = 47 nF(3)|TJ = 25°C|TJ = 25°C|486|ns|
|IGATE(OFF)<br>Gate Pin Sink<br>Current|VGATE = VIN + 3 V<br>VOUT > VIN + 100 mV<br>t ≤10 ms|TJ = 25°C|TJ = 25°C|2.8|A|
|IGATE(OFF)<br>Gate Pin Sink<br>Current|VGATE = VIN + 3 V<br>VOUT > VIN + 100 mV<br>t ≤10 ms|TJ = –40°C to 125°C|LM5050MK-1,<br>LM5050Q1MK-1|1.8|1.8|
|IGATE(OFF)<br>Gate Pin Sink<br>Current|VGATE = VIN + 3 V<br>VOUT > VIN + 100 mV<br>t ≤10 ms|TJ = –40°C to 125°C|LM5050Q0MK-1|1.4|1.4|
|VSD(REV)<br>Reverse VSD<br>Threshold<br>VIN < VOUT|VIN - VOUT|TJ = 25°C|TJ = 25°C|–28|mV|
|VSD(REV)<br>Reverse VSD<br>Threshold<br>VIN < VOUT|VIN - VOUT|TJ = –40°C to 125°C|TJ = –40°C to 125°C|–41<br>–16|–41<br>–16|
|ΔVSD(REV)<br>Reverse VSD<br>Hysteresis||TJ = 25°C|TJ = 25°C|10|mV|
|VSD(REG)<br>Regulated<br>Forward VSD<br>Threshold<br>VIN > VOUT|VIN = 5 V<br>VVS = VIN<br>VIN - VOUT|TJ = 25°C|TJ = 25°C|19|mV|
|VSD(REG)<br>Regulated<br>Forward VSD<br>Threshold<br>VIN > VOUT|VIN = 5 V<br>VVS = VIN<br>VIN - VOUT|TJ = –40°C to 125°C|LM5050MK-1,<br>LM5050Q1MK-1|1<br>37|1<br>37|
|VSD(REG)<br>Regulated<br>Forward VSD<br>Threshold<br>VIN > VOUT|VIN = 5 V<br>VVS = VIN<br>VIN - VOUT|TJ = –40°C to 125°C|LM5050Q0MK-1|1<br>60|1<br>60|
|VSD(REG)<br>Regulated<br>Forward VSD<br>Threshold<br>VIN > VOUT|VIN = 5 V<br>VVS = VIN<br>VIN - VOUT|TJ = 25°C|TJ = 25°C|22|22|
|VSD(REG)<br>Regulated<br>Forward VSD<br>Threshold<br>VIN > VOUT|VIN = 12 V<br>VVS = VIN<br>VIN - VOUT|TJ = –40°C to 125°C|LM5050MK-1,<br>LM5050Q1MK-1|4.4<br>37|4.4<br>37|
|VSD(REG)<br>Regulated<br>Forward VSD<br>Threshold<br>VIN > VOUT|VIN = 12 V<br>VVS = VIN<br>VIN - VOUT|TJ = –40°C to 125°C|LM5050Q0MK-1|4.4<br>60|4.4<br>60|
|**OFF PIN**|**OFF PIN**|**OFF PIN**|**OFF PIN**|**OFF PIN**|**OFF PIN**|
|VOFF(IH)<br>OFF Input High<br>Threshold<br>Voltage|VOUT = VIN-500 mV<br>VOFF Rising|TJ = 25°C|TJ = 25°C|1.56|V|
|VOFF(IH)<br>OFF Input High<br>Threshold<br>Voltage|VOUT = VIN-500 mV<br>VOFF Rising|TJ = –40°C to 125°C|TJ = –40°C to 125°C|1.75|1.75|
|VOFF(IL)<br>OFF Input Low<br>Threshold<br>Voltage|VOUT = VIN - 500 mV<br>VOFF Falling|TJ = 25°C|TJ = 25°C|1.4|1.4|
|VOFF(IL)<br>OFF Input Low<br>Threshold<br>Voltage|VOUT = VIN - 500 mV<br>VOFF Falling|TJ = –40°C to 125°C|TJ = –40°C to 125°C|1.1|1.1|
|ΔVOFF<br>OFF Threshold<br>Voltage<br>Hysteresis|VOFF(IH) - VOFF(IL)|TJ = 25°C|TJ = 25°C|155|mV|
|IOFF<br>OFF Pin Internal<br>Pulldown|VOFF = 4.5 V|TJ = 25°C|TJ = 25°C|5|µA|
|IOFF<br>OFF Pin Internal<br>Pulldown|VOFF = 4.5 V|TJ = –40°C to 125°C|TJ = –40°C to 125°C|3<br>7|3<br>7|
|IOFF<br>OFF Pin Internal<br>Pulldown|VOFF = 5 V|TJ = 25°C|TJ = 25°C|8|8|


(2) Time from VIN-VOUT voltage transition from 200 mV to -500 mV until GATE pin voltage falls to VIN + 1 V. See Figure 1.
(3) Time from VOFF voltage transition from 0 V to 5 V until GATE pin voltage falls to VIN + 1 V. See Figure 2



6



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


200 mV



VSD(REG)

0 mV


VSD(REV)


-500 mV


VGATE


1.0V


0.0V




|Col1|VIN > VOUT|
|---|---|
|||
|VIN < VOUT<br>tGATE(OFF)|VIN < VOUT|



**Figure 1. Gate OFF Timing for Forward to Reverse Transition**


5.0V



VOFF(IH)

VOFF(IL)


0.0V


VGATE


1.0V


0.0V




|Col1|Col2|
|---|---|
|||
|||
|tGATE(OFF)|tGATE(OFF)|



**Figure 2. Gate OFF Timing for OFF Pin Low to High Transition**


Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



7


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**6.7** **Typical Characteristics**


Unless otherwise stated: VVS = 12 V, VIN = 12 V, VOFF = 0 V, and TJ = 25°C


|Figure 3. I vs V<br>IN IN|Figure 4. I vs V<br>IN IN|
|---|---|
|**Figure 5. IOUT vs VOUT**|**Figure 6. IOUT vs VOUT**|
|**Figure 7. IVS vs VVS**|**Figure 8. IVS vs VVS**|



8



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**Typical Characteristics (continued)**








|Col1|Vin Vout|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||Vout<br>Vgate||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||


|Col1|Col2|Col3|Col4|V<br>V|out<br>gate|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||






|Col1|VOLTS (V)|2<br>2<br>2<br>2<br>1<br>1<br>1<br>1<br>1|6<br>Vin<br>Vout<br>4 Vgate<br>2<br>0<br>8<br>6<br>4<br>2<br>0|Col5|
|---|---|---|---|---|
||||-5<br>0<br>5<br>10<br>15<br>20<br>25<br>30|-5<br>0<br>5<br>10<br>15<br>20<br>25<br>30|
||||TIME (5ms / DIV)|TIME (5ms / DIV)|
||||||


|Col1|VOLTS (V)|2<br>2<br>2<br>2<br>1<br>1<br>1<br>1<br>1|6<br>Vin<br>Vout<br>4 Vgate<br>2<br>0<br>8<br>6<br>4<br>2<br>0|Col5|
|---|---|---|---|---|
||||-50<br>0<br>50<br>100<br>150<br>200<br>250|-50<br>0<br>50<br>100<br>150<br>200<br>250|
||||TIME (50ns / DIV)|TIME (50ns / DIV)|
||||||



|Figure 9. (V - V ) vs V, V = V<br>GATE IN IN VS OUT|Figure 10. (V - V ) vs V, V = V<br>GATE IN IN VS OUT|
|---|---|
|-5<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>24<br>26<br>VOLTS (V)<br>TIME (5ms / DIV)<br>Vin<br>Vout<br>Vgate<br>**Figure 11. Forward CGATE Charge Time, CGATE = 47 nF**|-50<br>0<br>50<br>100<br>150<br>200<br>250<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>24<br>26<br>VOLTS (V)<br>TIME (50ns / DIV)<br>Vin<br>Vout<br>Vgate<br>**Figure 12. Reverse CGATE Discharge, CGATE = 47 nF**|
|**Figure 13. VGATE - VIN vs Temperature**|**Figure 14. tGATE(REV) vs Temperature**|


Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



9


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Typical Characteristics (continued)**


|Figure 15. OFF Pin Thresholds vs Temperature|Figure 16. OFF Pin Pulldown vs Temperature|
|---|---|
|**Figure 17. CGATE Charge and Discharge vs OFF Pin**|**Figure 18. OFF Pin, ON to OFF Transition**|
|**Figure 19. OFF Pin, OFF to ON Transition**|**Figure 20. GATE Pin vs (RDS(ON) × IDS)**|



10



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**7** **Detailed Description**


**7.1** **Overview**


Blocking diodes are commonly placed in series with supply inputs for the purpose of ORing redundant power
sources and protecting against supply reversal. The LM5050 replaces diodes in these applications with an NMOSFET to reduce both the voltage drop and power loss associated with a passive solution. At low input
voltages, the improvement in forward voltage loss is readily appreciated where headroom is tight, as shown in
Figure 2. The LM5050 operates from 5 V to 75 V and it can withstand an absolute maximum of 100 V without
damage. A 12-V or 15-A ideal diode application is shown in Figure 24. Several external components are included
in addition to the MOSFET, Q1. Ideal diodes, like their non-ideal counterparts, exhibit a behavior known as
reverse recovery. In combination with parasitic or intentionally introduced inductances, reverse recovery spikes
may be generated by an ideal diode during an reverse current shutdown. D1, D2 and R1 protect against these
spikes which might otherwise exceed the LM5050 100-V survival rating. COUT also plays a role in absorbing
reverse recovery energy. Spikes and protection schemes are discussed in detail in the _Short Circuit Failure of an_
_Input Supply_ section.


**NOTE**
The OFF pin may be used to active the GATE pull down circuit and turn off the pass
MOSFET, but it does not disconnect the load from the input because Q1’s body diode is
still present.


If Vs is powered while IN is floating or grounded, then about 0.5mA will leak from the Vs
pin into the IC and about 3mA will leak from the OUT pin into the IC. From this leakage,
about 50 uA will flow out of the IN pin and the rest will flow to ground. This does not affect
long term reliability of the IC, but may influence circuit design. See _Reverse Input Voltage_
_Protection With IQ Reduction_ for details on how to avoid this leakage current.



Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



11


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**7.2** **Functional Block Diagram**


|Col1|IN|Col3|
|---|---|---|
||||
||||










|30 µA<br>+12V Charge|Col2|Col3|
|---|---|---|
|30µA<br>+12V Charge|<br>Pump|<br>Pump|
|30µA<br>+12V Charge|<br>Pump||







**7.3** **Feature Description**


**7.3.1** **IN, GATE, and OUT Pins**





When power is initially applied, the load current will flow from source to drain through the body diode of the
MOSFET. Once the voltage across the body diode exceeds VSD(REG) then the LM5050-1 begins charging the
MOSFET gate through a 32 µA (typical) charge pump current source . In forward operation, the gate of the
MOSFET is charged until it reaches the clamping voltage of the 12-V GATE to IN pin Zener diode internal to the
LM5050-1.


The LM5050-1 is designed to regulate the MOSFET gate-to-source voltage. If the MOSFET current decreases to
the point that the voltage across the MOSFET falls below the VSD(REG) voltage regulation point of 22 mV (typical),
the GATE pin voltage will be decreased until the voltage across the MOSFET is regulated at 22 mV. If the
source-to-drain voltage is greater than the VSD(REG) voltage, the gate-to-source voltage will increase and
eventually reach the 12-V GATE to IN pin Zener clamp level.



12



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**Feature Description (continued)**


If the MOSFET current reverses, possibly due to failure of the input supply, such that the voltage across the
LM5050-1 IN and OUT pins is more negative than the VSD(REV) voltage of -28 mV (typical), the LM5050-1 will
quickly discharge the MOSFET gate through a strong GATE to IN pin discharge transistor.


If the input supply fails abruptly, as would occur if the supply was shorted directly to ground, a reverse current
will temporarily flow through the MOSFET until the gate can be fully discharged. This reverse current is sourced
from the load capacitance and from the parallel connected supplies. The LM5050-1 responds to a voltage
reversal condition typically within 25 ns. The actual time required to turn off the MOSFET will depend on the
charge held by the gate capacitance of the MOSFET being used. A MOSFET with 47 nF of effective gate
capacitance can be turned off in typically 180 ns. This fast turnoff time minimizes voltage disturbances at the
output, as well as the current transients from the redundant supplies.


**7.3.2** **VS Pin**


The LM5050-1 VS pin is the main supply pin for all internal biasing and an auxiliary supply for the internal gate
drive charge pump.


For typical LM5050-1 applications, where the input voltage is above 5 V, the VS pin can be connected directly to
the OUT pin. In situations where the input voltage is close to, but not less than, the 5 V minimum, it may be
helpful to connect the VS pin to the OUT pin through an RC Low-Pass filter to reduce the possibility of erratic
behavior due to spurious voltage spikes that may appear on the OUT and IN pins. The series resistor value
should be low enough to keep the VS voltage drop at a minimum. A typical series resistor value is 100 Ω . The
capacitor value should be the lowest value that produces acceptable filtering of the voltage noise.


If Vs is powered while IN is floating or grounded, then about 0.5 mA will leak from the Vs pin into the IC and
about 3mA will leak from the OUT pin into the IC. From this leakage, about 50 uA will flow out of the IN pin and
the rest will flow to ground. This does not affect long term reliability of the IC, but may influence circuit design.
See _Reverse Input Voltage Protection With IQ Reduction_ for details on how to avoid this leakage current.


Alternately, it is possible to operate the LM5050-1 with VIN value as low as 1 V if the VS pin is powered from a
separate supply. This separate VS supply must be from 5 V and 75 V. See Figure 27.


**7.3.3** **OFF Pin**


The OFF pin is a logic level input pin that is used to control the gate drive to the external MOSFET. The
maximum operating voltage on this pin is 5.5 V.


When the OFF pin is high, the MOSFET is turned off (independent of the sensed IN and OUT voltages). In this
mode, load current will flow through the body diode of the MOSFET. The voltage difference between the IN pin
and OUT pins will be approximately 700 mV if the MOSFET is operating normally through the body diode.


The OFF pin has an internal pulldown of 5 µA (typical). If the OFF function is not required the pin may be left
open or connected to ground.


**7.4** **Device Functional Modes**


**7.4.1** **ON/OFF Control Mode**


The MOSFET can be turned off by asserting the OFF pin high. This mode only disables the MOSFET, but VOUT
is still available through the body diode of the MOSFET.


**7.4.2** **External Power Supply Mode**


The Vs pin of the LM5050 can be operated from 5 V to 75 V as the bias input supply. In this mode VIN voltage
can be as low as 1 V, as shown in Figure 27.



Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



13


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**8** **Application and Implementation**


**NOTE**
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TI’s customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.


**8.1** **Application Information**


Systems that require high availability often use multiple, parallel-connected redundant power supplies to improve
reliability. Schottky OR-ing diodes are typically used to connect these redundant power supplies to a common
point at the load. The disadvantage of using OR-ing diodes is the forward voltage drop, which reduces the
available voltage and the associated power losses as load currents increase. Using an N-channel MOSFET to
replace the OR-ing diode requires a small increase in the level of complexity, but reduces, or eliminates, the
need for diode heat sinks or large thermal copper area in circuit board layouts for high power applications.









**Figure 21. OR-ing with Diodes**


The LM5050-1/-Q1 is a positive voltage (that is, high-side) OR-ing controller that will drive an external N-channel
MOSFET to replace an OR-ing diode. The voltage across the MOSFET source and drain pins is monitored by
the LM5050-1 at the IN and OUT pins, while the GATE pin drives the MOSFET to control its operation based on
the monitored source-drain voltage. The resulting behavior is that of an ideal rectifier with source and drain pins
of the MOSFET acting as the anode and cathode pins of a diode respectively.





















14



**Figure 22. OR-ing With MOSFETs**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**Application Information (continued)**


**8.1.1** **MOSFET Selection**


The important MOSFET electrical parameters are the maximum continuous Drain current ID, the maximum
Source current (that is, body diode) IS, the maximum drain-to-source voltage VDS(MAX), the gate-to-source
threshold voltage VGS(TH), the drain-to-source reverse breakdown voltage V(BR)DSS, and the drain-to-source On
resistance RDS(ON).


The maximum continuous drain current, ID, rating must exceed the maximum continuous load current. The rating
for the maximum current through the body diode, IS, is typically rated the same as, or slightly higher than the
drain current, but body diode current only flows while the MOSFET gate is being charged to VGS(TH).


Gate Charge Time = Qg / IGATE(ON)


1. The maximum drain-to-source voltage, VDS(MAX), must be high enough to withstand the highest differential

voltage seen in the application. This would include any anticipated fault conditions.
2. The drain-to-source reverse breakdown voltage, V(BR)DSS, may provide some transient protection to the OUT

pin in low voltage applications by allowing conduction back to the IN pin during positive transients at the OUT
pin.
3. The gate-to-source threshold voltage, VGS(TH), should be compatible with the LM5050-1 gate drive

capabilities. Logic level MOSFETs, with RDS(ON) rated at VGS(TH) at 5 V, are recommended, but sub-Logic
level MOSFETs having RDS(ON) rated at VGS(TH) at 2.5 V, can also be used.
4. The dominate MOSFET loss for the LM5050-1 active OR-ing controller is conduction loss due to source-to
drain current to the output load, and the RDS(ON) of the MOSFET. This conduction loss could be reduced by
using a MOSFET with the lowest possible RDS(ON). However, contrary to popular belief, arbitrarily selecting a
MOSFET based solely on having low RDS(ON) may not always give desirable results for several reasons:

1. Reverse transition detection. Higher RDS(ON) will provide increased voltage information to the LM5050-1

Reverse Comparator at a lower reverse current level. This will give an earlier MOSFET turnoff condition
should the input voltage become shorted to ground. This will minimize any disturbance of the redundant
bus.
2. Reverse current leakage. In cases where multiple input supplies are closely matched it may be possible

for some small current to flow continuously through the MOSFET drain to source (that is, reverse)
without activating the LM5050-1 Reverse Comparator. Higher RDS(ON) will reduce this reverse current
level.
3. Cost. Generally, as the RDS(ON) rating goes lower, the cost of the MOSFET goes higher.
5. The dominate MOSFET loss for the LM5050-1 active OR-ing controller is conduction loss due to source-to
drain current to the output load, and the RDS(ON) of the MOSFET. This conduction loss could be reduced by
using a MOSFET with the lowest possible RDS(ON). However, contrary to popular belief, arbitrarily selecting a
MOSFET based solely on having low RDS(ON) may not always give desirable results for several reasons:

a. Selecting a MOSFET with an RDS(ON) that is too large will result in excessive power dissipation.

Additionally, the MOSFET gate will be charged to the full value that the LM5050-1 can provide as it
attempts to drive the Drain to Source voltage down to the VSD(REG) of 22 mV typical. This increased Gate
charge will require some finite amount of additional discharge time when the MOSFET needs to be
turned off.
b. As a guideline, it is suggest that RDS(ON) be selected to provide at least 22 mV, and no more than 100

mV, at the nominal load current.
c. (22 mV / ID) ≤ RDS(ON) ≤ (100 mV / ID)
d. The thermal resistance of the MOSFET package should also be considered against the anticipated



dissipation in the MOSFET to ensure that the junction temperature (TJ) is reasonably well controlled,
because the RDS(ON) of the MOSFET increases as the junction temperature increases.
6. PDISS = ID2 × (RDS(ON))
7. Operating with a maximum ambient temperature (TA(MAX)) of 35°C, a load current of 10 A, and an RDS(ON) of



10 m Ω, and desiring to keep the junction temperature under 100°C, the maximum junction-to-ambient
thermal resistance rating ( θ JA) must be:



a. R θ JA ≤ (TJ(MAX) - TA(MAX))/(ID2 × RDS(ON))
b. R θ JA ≤ (100°C - 35°C)/(10 A × 10 A × 0.01 Ω )



Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



15


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**Application Information (continued)**


c. R θ JA ≤ 65°C/W


**8.1.2** **Short Circuit Failure of an Input Supply**


An abrupt 0- Ω short circuit across the input supply will cause the highest possible reverse current to flow while
the internal LM5050-1 control circuitry discharges the gate of the MOSFET. During this time, the reverse current
is limited only by the RDS(ON) of the MOSFET, along with parasitic wiring resistances and inductances. Worst
case instantaneous reverse current would be limited to:

ID(REV) = (VOUT - VIN) / RDS(ON) (1)


The internal Reverse Comparator will react, and will start the process of discharging the Gate, when the reverse
current reaches:

ID(REV) = VSD(REV) / RDS(ON) (2)


When the MOSFET is finally switched off, the energy stored in the parasitic wiring inductances will be transferred
to the rest of the circuit. As a result, the LM5050-1 IN pin will see a negative voltage spike while the OUT pin will
see a positive voltage spike. The IN pin can be protected by diode clamping the pin to GND in the negative
direction. The OUT pin can be protected with a TVS protection diode, a local bypass capacitor, or both. In low
voltage applications, the MOSFET drainto- source breakdown voltage rating may be adequate to protect the
OUT pin (that is, VIN + V(BR)DSS(MAX) < 75 V ), but most MOSFET data sheets do not ensure the maximum
breakdown rating, so this method should be used with caution.



Parasitic Parasitic











**Figure 23. Reverse Recovery Current Generates Inductive Spikes at VIN and VOUT pins.**


**8.2** **Typical Applications**


**8.2.1** **Typical Application With Input and Output Transient Protection**



Q1



























OFF/ON





16



**Figure 24. Typical Application With Input and Output Transient Protection Schematic**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**Typical Applications (continued)**


_**8.2.1.1**_ _**Design Requirements**_


Table 1 shows the parameters for Figure 24


**Table 1. Design Parameters**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|Minimum Input Voltage, VINMIN|6 V|
|Maximum Input Voltage, VINMax|50 V|
|Output Current Range, IOUT|0 to 15 A|
|Ambient Temperature Range, TA|0°C to 50°C|



_**8.2.1.2**_ _**Detailed Design Procedure**_


The following design procedure can be used to select component values for the LM5050-1.


**8.2.1.2.1** **Power Supply Components (R1 C1,) Selection**


The LM5050-1 VS pin is the main supply pin for all internal biasing and an auxiliary supply for the internal gate
drive charge pump. The series resistor (R1) value should be low enough to keep the VS voltage drop at a
minimum. A typical series resistor value is 100 Ω . The capacitor value (0.1 uF typical) should be the lowest value
that produces acceptable filtering of the voltage noise.


**8.2.1.2.2** **MOSFET (Q1) Selection**


The MOSFET (Q1) selection procedure is explained in detail in _MOSFET Selection_ . The MOSFET used in the
design example is SUM40N10-30-E3.


**8.2.1.2.3** **D1 and D2 Selection for Inductive Kick-Back Protection**


Diode D1 and capacitor C1 and diode D2 and capacitor C2 in the Figure 27 serve as inductive kick-back
protection to limit negative transient voltage spikes generated on the input when the input supply voltage is
abruptly shorted to zero volts. As a result, the LM5050-1 IN pin will see a negative voltage spike while the OUT
pin will see a positive voltage spike. The IN pin can be protected by schottky diode (D1) clamping the pin to GND
in the negative direction, similarly the OUT pin should be protected with a TVS protection diode (D1), or with a
local bypass capacitor, or both. D1 is selected as 1-A, 60-V Schottky Barrier Rectifier (SS16T3G) and D2 is the
60 V, TVS (SMBJ60A-13-F).


_**8.2.1.3**_ _**Application Curves**_







Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



17


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**8.2.2** **Using a Separate VS Supply for Low Vin Operation**


In some applications, it is desired to operate LM5050-1 from low supply voltage. The LM5050-1 can operate with
a 1-V rail voltage, provided its VS pin is biased from 5 V to 75 V. The detail of such application is depicted in
Figure 27.


VBIAS

5.0V to 75V


GND



VIN
VOUT
1V to 75V













Off/On







**Figure 27. Using a Separate vs Supply for Low Vin Operation Schematic**


**8.2.3** **ORing of Two Power Sources**





















18



**Figure 28. ORing of Two Power Sources**


_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**8.2.4** **Reverse Input Voltage Protection With IQ Reduction**


If Vs is powered while IN is floating or grounded, then about 0.5 mA will leak from the Vs pin into the IC and
about 3 mA will leak from the OUT pin into the IC. From this leakage, about 50 uA will flow out of the IN pin and
the rest will flow to ground. This does not affect long term reliability of the IC, but may influence circuit design.


In battery powered applications, whenever LM5050-1 functionality is not needed, the supply to the LM5050-1 can
be disconnected by turning “OFF” Q2, as shown in Figure 29. This disconnects the ground path of the LM5050-1
and eliminates the current leakage from the battery.


The quiescent current of LM5050-1 can be also reduced by disconnecting the supply to VS pin, whenever
LM5050-1 function is not need.



VIN


ON/OFF
Control


GND





GND






















|SUM40N10-30<br>R1<br>100»<br>IN GATE OUT<br>D1 VS<br>LM5050-1<br>SS16T3<br>CIN Cout D4<br>1uF GND SMBJ60<br>22uF<br>75V D2<br>63V<br>BAS40-7-F<br>D3 C1<br>SS16T3 0.1µF<br>100V<br>Q2<br>NTR5198NLT3G|Col2|Col3|
|---|---|---|
||||
||||



**Figure 29. Reverse Input Voltage Protection With IQ Reduction Schematic**


**8.2.5** **Basic Application With Input Transient Protection**



Q1















OFF/ON





**Figure 30. Basic Application With Input Transient Protection Schematic**


Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



19


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**8.2.6** **48-V Application With Reverse Input Voltage (VIN = –48 V) Protection**



Q1



























**Figure 31. 48-V Application With Reverse Input Voltage (VIN = –48 V) Protection Schematic**


_**8.2.6.1**_ _**Application Curves**_







20



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


**[www.ti.com](http://www.ti.com)** SNVS629F –MAY 2011–REVISED DECEMBER 2019


**9** **Power Supply Recommendations**


When the LM5050-1/-Q1 shuts off the external MOSFET, transient voltages will appear on the input and output
due to reverse recovery, as discussed in _Short Circuit Failure of an Input Supply_ .To prevent LM5050-1 and
surrounding components from damage under the conditions of a direct input short circuit, it is necessary to clamp
the negative transient at IN, and OUT pins with TVS.


**10** **Layout**


**10.1** **Layout Guidelines**


The typical PCB layout for LM5050-1/-Q1 is shown in Figure 34. TI recommends connecting the IN, Gate and
OUT pins close to the source and drain pins of the MOSFET. Keep the traces of the MOSFET drain wide and
short to minimize resistive losses. Place surge suppressors (D1 and D4) components as shown in the example
layout of LM5050-1 in _Layout Example_ .


**10.2** **Layout Example**


R1








|Col1|VS OUT<br>GND Gate<br>OFF IN|Col3|
|---|---|---|
||||
||||










|Col1|D|
|---|---|
|G|G|
|||
|S|S|
|||





**Figure 34. Typical Layout Example With D2PAK N-MOSFET**


Copyright © 2011–2019, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_



21


**[LM5050-1, LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)**


SNVS629F –MAY 2011–REVISED DECEMBER 2019 **[www.ti.com](http://www.ti.com)**


**11** **Device and Documentation Support**


**11.1** **Documentation Support**


**11.1.1** **Related Documentation**


[Achieving Stable VGS Using LM5050-1 with Low Current and Noisy Input Supply, SLVA684](http://www.ti.com/lit/pdf/SLVA684)


**11.2** **Related Links**


The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to sample or buy.


**Table 2. Related Links**









|PARTS|PRODUCT FOLDER|SAMPLE & BUY|TECHNICAL<br>DOCUMENTS|TOOLS &<br>SOFTWARE|SUPPORT &<br>COMMUNITY|
|---|---|---|---|---|---|
|LM5050-1|Click here|Click here|Click here|Click here|Click here|
|LM5050-1-Q1|Click here|Click here|Click here|Click here|Click here|


**11.3** **Community Resources**


[TI E2E™support forums are an engineer's go-to source for fast, verified answers and design help — straight](http://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](http://www.ti.com/corp/docs/legal/termsofuse.shtml)


**11.4** **Trademarks**

E2E is a trademark of Texas Instruments.
All other trademarks are the property of their respective owners.


**11.5** **Electrostatic Discharge Caution**


These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam
during storage or handling to prevent electrostatic damage to the MOS gates.


**11.6** **Glossary**


[SLYZ022 —](http://www.ti.com/lit/pdf/SLYZ022) _TI Glossary_ .

This glossary lists and explains terms, acronyms, and definitions.


**12** **Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.



22



_[Submit Documentation Feedback](http://www.ti.com/feedbackform/techdocfeedback?litnum=SNVS629F&partnum=LM5050-1)_ Copyright © 2011–2019, Texas Instruments Incorporated


Product Folder Links: _[LM5050-1 LM5050-1-Q1](http://www.ti.com/product/lm5050-1?qgpn=lm5050-1)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 31-Oct-2025


**PACKAGING INFORMATION**





















**(1) Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)





**(2) Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.


**(3) RoHS values:** [Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.](https://www.ti.com/lit/szzq088)


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 31-Oct-2025


**(4) Lead finish/Ball material:** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.


**(5) MSL rating/Peak reflow:** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.


**(6) Part marking:** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

**[OTHER QUALIFIED VERSIONS OF LM5050-1, LM5050-1-Q1 :]**

- [[Catalog : ][LM5050-1]](http://focus.ti.com/docs/prod/folders/print/lm5050-1.html)

- [[Automotive : ][LM5050-1-Q1]](http://focus.ti.com/docs/prod/folders/print/lm5050-1-q1.html)


[NOTE: Qualified Version Definitions:]

    - [Catalog - TI's standard catalog product]

    - [Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects]


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 7-Sep-2025


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
|LM5050MK-1/NOPB|SOT-23-<br>THIN|DDC|6|1000|178.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|LM5050MKX-1/NOPB|SOT-23-<br>THIN|DDC|6|3000|178.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|LM5050Q0MK-1/NOPB|SOT-23-<br>THIN|DDC|6|1000|178.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|LM5050Q0MKX-1/NOPB|SOT-23-<br>THIN|DDC|6|3000|178.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|LM5050Q1MK-1/NOPB|SOT-23-<br>THIN|DDC|6|1000|178.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|LM5050Q1MKX-1/NOPB|SOT-23-<br>THIN|DDC|6|3000|178.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|


Pack Materials-Page 1


















### **PACKAGE MATERIALS INFORMATION**

www.ti.com 7-Sep-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|LM5050MK-1/NOPB|SOT-23-THIN|DDC|6|1000|208.0|191.0|35.0|
|LM5050MKX-1/NOPB|SOT-23-THIN|DDC|6|3000|208.0|191.0|35.0|
|LM5050Q0MK-1/NOPB|SOT-23-THIN|DDC|6|1000|208.0|191.0|35.0|
|LM5050Q0MKX-1/NOPB|SOT-23-THIN|DDC|6|3000|208.0|191.0|35.0|
|LM5050Q1MK-1/NOPB|SOT-23-THIN|DDC|6|1000|208.0|191.0|35.0|
|LM5050Q1MKX-1/NOPB|SOT-23-THIN|DDC|6|3000|208.0|191.0|35.0|



Pack Materials-Page 2


## **PACKAGE OUTLINE**
# DDC0006A SCALE 4.000 SOT-23 - 1.1 max height SMALL OUTLINE TRANSISTOR























NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Reference JEDEC MO-193.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DDC0006A SOT-23 - 1.1 max height**

SMALL OUTLINE TRANSISTOR



























NOTES: (continued)

4. Publication IPC-7351 may have alternate designs.
5. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**
# **DDC0006A SOT-23 - 1.1 max height**

SMALL OUTLINE TRANSISTOR













NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
7. Board assembly site may have different recommendations for stencil design.


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


