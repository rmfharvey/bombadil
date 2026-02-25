**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)
#### **TCA9535 Low-Voltage 16-Bit I [2] C and SMBus Low-Power I/O Expander** **with Interrupt Output and Configuration Registers**



**1 Features**

- I [2] C to Parallel port expander

- Wide power supply voltage range of 1.65 V to
5 V

- Low standby-current consumption

- Open-drain active-low interrupt output

- 5-V tolerant I/O ports

- 400-kHz Fast I [2] C bus

- Polarity inversion register

- Address by three hardware address pins for use of
up to eight devices

- Latched outputs with high-current drive capability
for directly driving LEDs

- Latch-up performance exceeds 100 mA per
JESD 78, class II

- ESD protection exceeds JESD 22

  - 2000-V Human-Body Model (A114-A)

  - 1000-V Charged-Device Model (C101)

**2 Applications**


- Servers

- Routers (telecom switching equipment)

- [Personal computers](https://www.ti.com/applications/personal-electronics/pc-notebooks/overview.html)

- [Personal electronics (for example, gaming](https://www.ti.com/applications/personal-electronics/overview.html)
consoles)

- [Industrial automation](https://www.ti.com/applications/industrial/factory-automation/products.html?keyMatch=FACTORY)

- [Products with GPIO-limited processors](https://www.ti.com/interface/i2c/general-purpose-ios-gpios/products.html?keyMatch=GPIO)


|PART NUMBER|PACKAGE(1)|BODY SIZE (NOM)|
|---|---|---|
|TCA9535|TSSOP (24)|7.80 mm x 4.40 mm|
|TCA9535|SSOP (24)|6.20 mm x 5.30 mm|
|TCA9535|WQFN (24)|4.00 mm x 4.00 mm|
|TCA9535|VQFN (24)|4.00 mm x 4.00 mm|





**3 Description**


The TCA9535 is a 24-pin device that provides 16
bits of general purpose parallel input and output (I/O)
expansion for the two-line bidirectional I [2] C bus or
(SMBus) protocol. The device can operate with a
power supply voltage ranging from 1.65 V to 5.5 V.


The TCA9535 consists of two 8-bit Configuration
(input or output selection), Input Port, Output Port,
and Polarity Inversion (active-high or active-low
operation) registers. At power on, the I/Os are
configured as inputs. The system controller can
enable the I/Os as either inputs or outputs by writing
to the I/O configuration bits.


[The TCA9535 is identical to the TCA9555, except that](http://www.ti.com/product/TCA9555)
the TCA9535 does not include the internal I/O pull-up
resistor, which requires pull-ups and pull-downs on
unused I/O pins when configured as an input and
undriven.


**Device Information**









(1) For all available packages, see the orderable addendum at
the end of the data sheet.





I [2] C or SMBus Controller
(e.g. Processor)




|VCC P00<br>SDA P01<br>SCL P02<br>INT P03<br>P04<br>P05<br>P06<br>P07<br>TCA9535<br>P10<br>P11<br>P12<br>P13<br>A2 P14<br>A1 P15<br>A0 P16<br>GND P17|Col2|Col3|
|---|---|---|
|TCA9535<br>SDA<br>SCL<br>INT<br>VCC<br>GND<br>A0<br>P00<br>P01<br>P02<br>P03<br>P04<br>P05<br>P06<br>P07<br>A1<br>A2<br>P10<br>P11<br>P12<br>P13<br>P14<br>P15<br>P16<br>P17|TCA9535<br>SDA<br>SCL<br>INT<br>VCC<br>GND<br>A0<br>P00<br>P01<br>P02<br>P03<br>P04<br>P05<br>P06<br>P07<br>A1<br>A2<br>P10<br>P11<br>P12<br>P13<br>P14<br>P15<br>P16<br>P17|TCA9535<br>SDA<br>SCL<br>INT<br>VCC<br>GND<br>A0<br>P00<br>P01<br>P02<br>P03<br>P04<br>P05<br>P06<br>P07<br>A1<br>A2<br>P10<br>P11<br>P12<br>P13<br>P14<br>P15<br>P16<br>P17|
||||
||||
||||
||||
||||



**Block Diagram**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1
**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Revision History** .............................................................. 2
**5 Pin Configuration and Functions** ...................................3
**6 Specifications** .................................................................. 4

6.1 Absolute Maximum Ratings........................................ 4
6.2 ESD Ratings............................................................... 4
6.3 Recommended Operating Conditions.........................4
6.4 Thermal Information....................................................5
6.5 Electrical Characteristics.............................................5
6.6 I [2] C Interface Timing Requirements.............................6
6.7 Switching Characteristics............................................7
6.8 Typical Characteristics................................................ 8
**7 Detailed Description** ......................................................14

7.1 Overview................................................................... 14
7.2 Functional Block Diagram......................................... 14
7.3 Feature Description...................................................15
7.4 Device Functional Modes..........................................16



7.5 Programming............................................................ 16
7.6 Register Maps...........................................................22
**8 Application and Implementation** .................................. 23

8.1 Application Information............................................. 23
8.2 Typical Application.................................................... 23
**9 Power Supply Recommendations** ................................27
**10 Layout** ...........................................................................29

10.1 Layout Guidelines................................................... 29
10.2 Layout Example...................................................... 29
**11 Device and Documentation Support** ..........................30

11.1 Documentation Support.......................................... 30
11.2 Receiving Notification of Documentation Updates.. 30
11.3 Support Resources................................................. 30
11.4 Trademarks............................................................. 30
11.5 Electrostatic Discharge Caution.............................. 30
11.6 Glossary.................................................................. 30
**12 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 30



**4 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision D (June 2016) to Revision E (May 2022)** **Page**

 - Globally changed instances of legacy terminology to controller and target where I [2] C is mentioned..................1

 - Changed VCC to GND on the Controlled Switch in Figure 8-1 .........................................................................23


**Changes from Revision C (May 2016) to Revision D (June 2016)** **Page**

 - Added DB package ............................................................................................................................................1


**Changes from Revision B (August 2015) to Revision C (May 2016)** **Page**

 - Added RGE package.......................................................................................................................................... 1

 - Added IOL for different Tj ....................................................................................................................................4

 - Deleted ΔICC spec from the Electrical Characteristics table, added ΔICC typical characteristics graph............. 5

 - Changed ICC standby into different input states, with increased maximums ..................................................... 5

 - Changed Cio maximum ...................................................................................................................................... 5


**Changes from Revision A (September 2009) to Revision B (August 2015)** **Page**

 - Added _Pin Configuration and Functions_ section, _ESD Ratings_ table, _Feature Description_ section, _Device_
_Functional Modes_, _Application and Implementation_ section, _Power Supply Recommendations_ section, _Layout_
section, _Device and Documentation Support_ section, and _Mechanical, Packaging, and Orderable Information_
section................................................................................................................................................................ 1


2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**5 Pin Configuration and Functions**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



INT


A1

A2

P00

P01

P02

P03

P04

P05

P06

P07

GND



VCC
SDA

SCL

A0

P17

P16

P15

P14

P13

P12

P11

P10









P00
P01
P02
P03
P04
P05







A0
P17
P16
P15
P14
P13


|Col1|1 24<br>2 23<br>3 22<br>4 21<br>5 20<br>6 19<br>7 18<br>8 17<br>9 16<br>10 15<br>11 14<br>12 13|Col3|
|---|---|---|
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||
||||



**Figure 5-1. DB, PW (TSSOP) Package**

**24-Pin (Top View)**



The exposed center pad, if used, must be connected as a
secondary ground or left electrically open.
**Figure 5-2. RTW (WQFN), RGE (VQFN) Package**

**24-Pin (Top View)**



**Table 5-1. Pin Functions**











|PIN|Col2|Col3|TYPE|DESCRIPTION|
|---|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|**NO.**|
|**NAME**|**DB, PW**|**RTW,**<br>**RGE**|**RTW,**<br>**RGE**|**RTW,**<br>**RGE**|
|A0|21|18|Input|Address input 0. Connect directly to VCC or ground|
|A1|2|23|Input|Address input 1. Connect directly to VCC or ground|
|A2|3|24|Input|Address input 2. Connect directly to VCC or ground|
|GND|12|9|—|Ground|
|~~INT~~|1|22|Output|Interrupt output. Connect to VCC through an external pull-up resistor|
|P00(1)|4|1|I/O|P-port I/O. Push-pull design structure. At power on, P00 is configured as an input|
|P01(1)|5|2|I/O|P-port I/O. Push-pull design structure. At power on, P01 is configured as an input|
|P02(1)|6|3|I/O|P-port I/O. Push-pull design structure. At power on, P02 is configured as an input|
|P03(1)|7|4|I/O|P-port I/O. Push-pull design structure. At power on, P03 is configured as an input|
|P04(1)|8|5|I/O|P-port I/O. Push-pull design structure. At power on, P04 is configured as an input|
|P05(1)|9|6|I/O|P-port I/O. Push-pull design structure. At power on, P05 is configured as an input|
|P06(1)|10|7|I/O|P-port I/O. Push-pull design structure. At power on, P06 is configured as an input|
|P07(1)|11|8|I/O|P-port I/O. Push-pull design structure. At power on, P07 is configured as an input|
|P10(1)|13|10|I/O|P-port I/O. Push-pull design structure. At power on, P10 is configured as an input|
|P11(1)|14|11|I/O|P-port I/O. Push-pull design structure. At power on, P11 is configured as an input|
|P12(1)|15|12|I/O|P-port I/O. Push-pull design structure. At power on, P12 is configured as an input|
|P13(1)|16|13|I/O|P-port I/O. Push-pull design structure. At power on, P13 is configured as an input|
|P14(1)|17|14|I/O|P-port I/O. Push-pull design structure. At power on, P14 is configured as an input|
|P15(1)|18|15|I/O|P-port I/O. Push-pull design structure. At power on, P15 is configured as an input|
|P16(1)|19|16|I/O|P-port I/O. Push-pull design structure. At power on, P16 is configured as an input|
|P17(1)|20|17|I/O|P-port I/O. Push-pull design structure. At power on, P17 is configured as an input|
|SCL|22|19|Input|Serial clock bus. Connect to VCC through a pull-up resistor|
|SDA|23|20|Input|Serial data bus. Connect to VCC through a pull-up resistor|
|VCC|24|21|—|Supply voltage|


(1) If port is unused, it must be tied to either VCC or GND through a resistor of moderate value (about 10 kΩ)


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 3


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**6 Specifications**


**6.1 Absolute Maximum Ratings**

over operating free-air temperature range (unless otherwise noted) [(1)]







|Col1|Col2|Col3|MIN MAX|UNIT|
|---|---|---|---|---|
|VCC<br>Supply voltage|VCC<br>Supply voltage|VCC<br>Supply voltage|–0.5<br>6|V|
|VI<br>Input voltage(2)|VI<br>Input voltage(2)|VI<br>Input voltage(2)|–0.5<br>6|V|
|VO<br>Output voltage(2)|VO<br>Output voltage(2)|VO<br>Output voltage(2)|–0.5<br>6|V|
|IIK<br>Input clamp current|IIK<br>Input clamp current|VI < 0|–20|mA|
|IOK<br>Output clamp current|IOK<br>Output clamp current|VO < 0|–20|mA|
|IIOK<br>Input-output clamp current|IIOK<br>Input-output clamp current|VO < 0 or VO > VCC|±20|mA|
|IOL<br>Continuous output low current|IOL<br>Continuous output low current|VO = 0 to VCC|50|mA|
|IOH<br>Continuous output high current|IOH<br>Continuous output high current|VO = 0 to VCC|–50|mA|
|ICC|Continuous current through GND|Continuous current through GND|–250|mA|
|ICC|Continuous current through VCC|Continuous current through VCC|160|mA|
|Tj(MAX) Maximum junction temperature|Tj(MAX) Maximum junction temperature|Tj(MAX) Maximum junction temperature|100|°C|
|Tstg<br>Storage temperature|Tstg<br>Storage temperature|Tstg<br>Storage temperature|–65<br>150|°C|


(1) Operation outside the _Absolute Maximum Ratings_ may cause permanent device damage. Absolute maximum ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under _Recommended Operating Conditions_ .
If briefly operating outside the _Recommended Operating Conditions_ but within the _Absolute Maximum Ratings_, the device may not
sustain damage, but it may not be fully functional. Operating the device in this manner may affect device reliability, functionality,
performance, and shorten the device lifetime.
(2) The input negative-voltage and output voltage ratings may be exceeded if the input and output current ratings are observed.


**6.2 ESD Ratings**






|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)<br>Electrostatic discharge|Charged-device model (CDM), per JEDEC specification JESD22-C101(2)|±1000|±1000|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**6.3 Recommended Operating Conditions**

over operating free-air temperature range (unless otherwise noted)













|Col1|Col2|Col3|MIN|MAX|UNIT|
|---|---|---|---|---|---|
|VCC<br>Supply voltage|VCC<br>Supply voltage|VCC<br>Supply voltage|1.65<br>5.5|1.65<br>5.5|V|
|VIH<br>High-level input voltage|SCL, SDA|SCL, SDA|0.7 × VCC<br>VCC (1)|0.7 × VCC<br>VCC (1)|V|
|VIH<br>High-level input voltage|A2–A0, P07–P00, P17–P10|A2–A0, P07–P00, P17–P10|0.7 × VCC<br>5.5|0.7 × VCC<br>5.5|V|
|VIL<br>Low-level input voltage|SCL, SDA, A2–A0, P07–P00, P17–P10|SCL, SDA, A2–A0, P07–P00, P17–P10|–0.5<br>0.3 × VCC|–0.5<br>0.3 × VCC|V|
|IOH<br>High-level output current|P07–P00, P17–P10|P07–P00, P17–P10|–10|–10|mA|
|IOL<br>Low-level output current(2)|P07–P00, P17–P10|Tj ≤ 65°C|25|25|mA|
|IOL<br>Low-level output current(2)|P07–P00, P17–P10|Tj ≤ 85°C|18|18|18|
|IOL<br>Low-level output current(2)|P07–P00, P17–P10|Tj ≤ 100°C|11|11|11|
|IOL<br>Low-level output current(2)|~~INT~~, SDA|Tj ≤ 85°C|6|6|mA|
|IOL<br>Low-level output current(2)|~~INT~~, SDA|Tj ≤ 100°C|3.5|3.5|3.5|
|TA<br>Operating free-air temperature|TA<br>Operating free-air temperature|TA<br>Operating free-air temperature|–40<br>85|–40<br>85|°C|


(1) For voltages applied above VCC, an increase in ICC results.
(2) The values shown apply to specific junction temperatures, which depend on the RθJA of the package used. See the _Calculating_
_Junction Temperature and Power Dissipation_ section on how to calculate the junction temperature.


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**6.4 Thermal Information**







**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)







|THERMAL METRIC(1)|TCA9535|Col3|Col4|Col5|UNIT|
|---|---|---|---|---|---|
|**THERMAL METRIC**(1)|**PW**<br>**(TSSOP)**|**DB**<br>**(SSOP)**|**RTW**<br>**(WQFN)**|**RGE**<br>**(VQFN)**|**RGE**<br>**(VQFN)**|
|**THERMAL METRIC**(1)|**24 PINS**|**24 PINS**|**24 PINS**|**24 PINS**|**24 PINS**|
|RθJA<br>Junction-to-ambient thermal resistance|108.8|92.9|43.6|48.4|°C/W|
|RθJC(top)<br>Junction-to-case (top) thermal resistance|54|53.5|46.2|58.1|°C/W|
|RθJB<br>Junction-to-board thermal resistance|62.8|50.4|22.1|27.1|°C/W|
|ψJT<br>Junction-to-top characterization parameter|11.1|21.9|1.5|3.3|°C/W|
|ψJB<br>Junction-to-board characterization parameter|62.3|50.1|22.2|27.2|°C/W|
|RθJC(bot)<br>Junction-to-case (bottom) thermal resistance|N/A|N/A|10.7|15.3|°C/W|


(1) For more information about traditional and new thermal metrics, see the _[Semiconductor and IC Package Thermal Metrics](https://www.ti.com/lit/pdf/SPRA953)_ application
report.


**6.5 Electrical Characteristics**


over recommended operating free-air temperature range (unless otherwise noted)


















|PARAMETER|Col2|TEST CONDITIONS|V<br>CC|MIN TYP(1) MAX|UNIT|
|---|---|---|---|---|---|
|VIK<br>Input diode clamp voltage|VIK<br>Input diode clamp voltage|II = –18 mA|1.65 V to 5.5 V|–1.2|V|
|VPORR<br>Power-on reset voltage, VCC rising|VPORR<br>Power-on reset voltage, VCC rising|VI = VCC or GND, IO = 0||1.2<br>1.5|V|
|VPORF<br>Power-on reset voltage, VCC falling|VPORF<br>Power-on reset voltage, VCC falling|VI = VCC or GND, IO = 0||0.75<br>1|V|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –8 mA|1.65 V|1.2|V|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –8 mA|2.3 V|1.8|1.8|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –8 mA|3 V|2.6|2.6|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –8 mA|4.75 V|4.1|4.1|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –10 mA|1.65 V|1|1|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –10 mA|2.3 V|1.7|1.7|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –10 mA|3 V|2.5|2.5|
|VOH<br>P-port high-level output voltage(2)|VOH<br>P-port high-level output voltage(2)|IOH = –10 mA|4.75 V|4|4|
|IOL<br>Low-level output<br>current|SDA|VOL = 0.4 V|1.65 V to 5.5 V|3|mA|
|IOL<br>Low-level output<br>current|P port(3)|VOL = 0.5 V|1.65 V to 5.5 V|8|8|
|IOL<br>Low-level output<br>current|P port(3)|VOL = 0.7 V|1.65 V to 5.5 V|10|10|
|IOL<br>Low-level output<br>current|~~INT~~|VOL = 0.4 V|1.65 V to 5.5 V|3|3|
|II<br>Input leakage current|SCL, SDA Input<br>leakage|VI = VCC or GND|1.65 V to 5.5 V|±1|μA|
|II<br>Input leakage current|A2–A0 Input<br>leakage|VI = VCC or GND|1.65 V to 5.5 V|±1|±1|
|IIH<br>Input high leakage<br>current|P port|VI = VCC|1.65 V to 5.5 V|1|μA|
|IIL<br>Input low leakage<br>current|P port|VI = GND|1.65 V to 5.5 V|–1|μA|



Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 5


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**6.5 Electrical Characteristics**


over recommended operating free-air temperature range (unless otherwise noted)


















|PARAMETER|Col2|TEST CONDITIONS|V<br>CC|MIN TYP(1) MAX|UNIT|
|---|---|---|---|---|---|
|ICC<br>Quiescent current|Operating mode|VI = VCC or GND, IO = 0,<br>I/O = inputs, fSCL = 400 kHz,<br>No load|5.5 V|22<br>40|μA|
|ICC<br>Quiescent current|Operating mode|VI = VCC or GND, IO = 0,<br>I/O = inputs, fSCL = 400 kHz,<br>No load|3.6 V|11<br>30|11<br>30|
|ICC<br>Quiescent current|Operating mode|VI = VCC or GND, IO = 0,<br>I/O = inputs, fSCL = 400 kHz,<br>No load|2.7 V|8<br>19|8<br>19|
|ICC<br>Quiescent current|Operating mode|VI = VCC or GND, IO = 0,<br>I/O = inputs, fSCL = 400 kHz,<br>No load|1.95 V|5<br>11|5<br>11|
|ICC<br>Quiescent current|Standby mode|VI = VCC, IO = 0, I/O = inputs,<br>fSCL = 0 kHz, No load|5.5 V|1.5<br>3.9|1.5<br>3.9|
|ICC<br>Quiescent current|Standby mode|VI = VCC, IO = 0, I/O = inputs,<br>fSCL = 0 kHz, No load|3.6 V|0.9<br>2.2|0.9<br>2.2|
|ICC<br>Quiescent current|Standby mode|VI = VCC, IO = 0, I/O = inputs,<br>fSCL = 0 kHz, No load|2.7 V|0.6<br>1.8|0.6<br>1.8|
|ICC<br>Quiescent current|Standby mode|VI = VCC, IO = 0, I/O = inputs,<br>fSCL = 0 kHz, No load|1.95 V|0.6<br>1.5|0.6<br>1.5|
|ICC<br>Quiescent current|Standby mode|VI = GND, IO = 0, I/O =<br>inputs,<br>fSCL = 0 kHz, No load|5.5 V|1.5<br>8.7|1.5<br>8.7|
|ICC<br>Quiescent current|Standby mode|VI = GND, IO = 0, I/O =<br>inputs,<br>fSCL = 0 kHz, No load|3.6 V|0.9<br>4|0.9<br>4|
|ICC<br>Quiescent current|Standby mode|VI = GND, IO = 0, I/O =<br>inputs,<br>fSCL = 0 kHz, No load|2.7 V|0.6<br>3|0.6<br>3|
|ICC<br>Quiescent current|Standby mode|VI = GND, IO = 0, I/O =<br>inputs,<br>fSCL = 0 kHz, No load|1.95 V|0.4<br>2.2|0.4<br>2.2|
|CI<br>Input capacitance|SCL|VI = VCC or GND|1.65 V to 5.5 V|3<br>8|pF|
|Cio<br>Input-output pin<br>capacitance|SDA|VIO = VCC or GND|1.65 V to 5.5 V|3<br>9.5|pF|
|Cio<br>Input-output pin<br>capacitance|P port|VIO = VCC or GND|1.65 V to 5.5 V|3.7<br>9.5|3.7<br>9.5|



(1) All typical values are at nominal supply voltage (1.8-, 2.5-, 3.3-, or 5-V VCC) and TA = 25°C.
(2) Each I/O must be externally limited to a maximum of 25 mA, and each octal (P07–P00 and P17–P10) must be limited to a maximum
current of 100 mA, for a device total of 200 mA.
(3) The total current sourced by all I/Os must be limited to 160 mA (80 mA for P07–P00 and 80 mA for P17–P10).


**6.6 I** **[2]** **C Interface Timing Requirements**

over recommended operating free-air temperature range (unless otherwise noted) (see Figure 7-2)

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|**I2C BUS—STANDARD MODE**|**I2C BUS—STANDARD MODE**|**I2C BUS—STANDARD MODE**|**I2C BUS—STANDARD MODE**|
|fscl<br>I2C clock frequency|fscl<br>I2C clock frequency|0<br>100|kHz|
|tsch<br>I2C clock high time|tsch<br>I2C clock high time|4|µs|
|tscl<br>I2C clock low time|tscl<br>I2C clock low time|4.7|µs|
|tsp<br>I2C spike time|tsp<br>I2C spike time|50|ns|
|tsds<br>I2C serial-data setup time|tsds<br>I2C serial-data setup time|250|ns|
|tsdh<br>I2C serial-data hold time|tsdh<br>I2C serial-data hold time|0|ns|
|ticr<br>I2C input rise time|ticr<br>I2C input rise time|1000|ns|
|ticf<br>I2C input fall time|ticf<br>I2C input fall time|300|ns|
|tocf<br>I2C output fall time|10-pF to 400-pF bus|300|ns|
|tbuf<br>I2C bus free time between stop and start|tbuf<br>I2C bus free time between stop and start|4.7|µs|
|tsts<br>I2C start or repeated start condition setup|tsts<br>I2C start or repeated start condition setup|4.7|µs|
|tsth<br>I2C start or repeated start condition hold|tsth<br>I2C start or repeated start condition hold|4|µs|
|tsps<br>I2C stop condition setup|tsps<br>I2C stop condition setup|4|µs|
|tvd(data)<br>Valid data time|SCL low to SDA output valid|3.45|µs|
|tvd(ack)<br>Valid data time of ACK condition|ACK signal from SCL low to<br>SDA (out) low|3.45|µs|
|Cb<br>I2C bus capacitive load|Cb<br>I2C bus capacitive load|400|pF|
|**I2C BUS—FAST MODE**|**I2C BUS—FAST MODE**|**I2C BUS—FAST MODE**|**I2C BUS—FAST MODE**|
|fscl<br>I2C clock frequency|fscl<br>I2C clock frequency|0<br>400|kHz|
|tsch<br>I2C clock high time|tsch<br>I2C clock high time|0.6|µs|
|tscl<br>I2C clock low time|tscl<br>I2C clock low time|1.3|µs|



6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**6.6 I** **[2]** **C Interface Timing Requirements (continued)**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



over recommended operating free-air temperature range (unless otherwise noted) (see Figure 7-2)

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|tsp<br>I2C spike time|tsp<br>I2C spike time|50|ns|
|tsds<br>I2C serial-data setup time|tsds<br>I2C serial-data setup time|100|ns|
|tsdh<br>I2C serial-data hold time|tsdh<br>I2C serial-data hold time|0|ns|
|ticr<br>I2C input rise time|ticr<br>I2C input rise time|20<br>300|ns|
|ticf<br>I2C input fall time|ticf<br>I2C input fall time|20 × (VCC /<br>5.5 V)<br>300|ns|
|tocf<br>I2C output fall time|10-pF to 400-pF bus|20 × (VCC /<br>5.5 V)<br>300|ns|
|tbuf<br>I2C bus free time between stop and start|tbuf<br>I2C bus free time between stop and start|1.3|µs|
|tsts<br>I2C start or repeated start condition setup|tsts<br>I2C start or repeated start condition setup|0.6|µs|
|tsth<br>I2C start or repeated start condition hold|tsth<br>I2C start or repeated start condition hold|0.6|µs|
|tsps<br>I2C stop condition setup|tsps<br>I2C stop condition setup|0.6|µs|
|tvd(data)<br>Valid data time|SCL low to SDA output valid|0.9|µs|
|tvd(ack)<br>Valid data time of ACK condition|ACK signal from SCL low to<br>SDA (out) low|0.9|µs|
|Cb<br>I2C bus capacitive load|Cb<br>I2C bus capacitive load|400|pF|



**6.7 Switching Characteristics**

over recommended operating free-air temperature range, CL ≤ 100 pF (unless otherwise noted) (see Figure 7-2 and Figure
7-3)

















|PARAMETER|Col2|FROM<br>(INPUT)|TO<br>(OUTPUT)|MIN MAX|UNIT|
|---|---|---|---|---|---|
|tiv<br>Interrupt valid time|tiv<br>Interrupt valid time|P port|~~INT~~|4|μs|
|tir<br>Interrupt reset delay time|tir<br>Interrupt reset delay time|SCL|~~INT~~|4|μs|
|tpv|Output data valid; For VCC = 2.3 V–5.5 V|SCL|P port|200|ns|
|tpv|Output data valid; For VCC = 1.65 V–2.3 V|Output data valid; For VCC = 1.65 V–2.3 V|Output data valid; For VCC = 1.65 V–2.3 V|300|ns|
|tps<br>Input data setup time|tps<br>Input data setup time|P port|SCL|150|ns|
|tph<br>Input data hold time|tph<br>Input data hold time|P port|SCL|1|μs|


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 7


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics**


TA = 25°C (unless otherwise noted)






















|Col1|V|cc = 1.65 V|Vcc =|3.3 V|Vcc = 5.5V|
|---|---|---|---|---|---|
||~~V~~<br>V|~~cc = 1.8 V~~<br>c = 2.5 V|~~Vcc =~~<br>Vcc =|~~  3.6 V~~<br>  5 V||
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


|Vcc =|1.65 V|Vcc = 3.3|V Vcc|= 5.5V|Col6|
|---|---|---|---|---|---|
|~~Vcc =~~<br>Vcc|~~  1.8 V~~<br>  2.5 V|~~Vcc = 3.6~~<br>Vcc = 5 V|~~   V~~|||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||


























|-<br>2|40qC<br>5qC|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~8~~|~~5qC~~|~~5qC~~|||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~8~~|~~qC~~|~~   V~~|||||||||||
|~~V~~|~~ =~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|~~  .65~~|
|~~C~~||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


























|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||85|qC||||||||||||
|||||||||||||||
|VC|C = 1|.8 V||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~8~~|~~qC~~||||||||||||
|~~V~~|~~ =~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|~~  .5 V~~|
|~~C~~|~~C~~|||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||














|40<br>Vcc = 1.65 V Vcc = 3.3 V Vcc = 5.5V<br>36 Vcc = 1.8 V Vcc = 3.6 V<br>32 Vcc = 2.5 V Vcc = 5 V<br>(µA)<br>28<br>Current<br>24<br>20<br>Supply<br>16<br>12 -<br>ICC<br>8<br>4<br>0<br>-40 -15 10 35 60 85<br>TA - Temperature (°C)<br>D001<br>Figure 6-1. Supply Current vs Temperature for Different Supply<br>Voltage (V )<br>CC|2.2<br>Vcc = 1.65 V Vcc = 3.3 V Vcc = 5.5V<br>2 Vcc = 1.8 V Vcc = 3.6 V<br>1.8 Vcc = 2.5 V Vcc = 5 V<br>(µA)<br>1.6<br>Current<br>1.4<br>1.2<br>Supply<br>1<br>0.8 -<br>ICC<br>0.6<br>0.4<br>0.2<br>-40 -15 10 35 60 85<br>TA - Temperature (°C)<br>D002<br>Figure 6-2. Standby Supply Current vs Temperature for<br>Different Supply Voltage (V )<br>CC|
|---|---|
|VCC - Supply Voltage (V)<br>ICC - Supply Current (µA)<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>D003<br>-40qC<br>25qC<br>~~85qC~~<br>**Figure 6-3. Supply Current vs Supply Voltage for Different**<br>**Temperature (TA)**|VOL - Output Low Voltage (V)<br>IOL - Sink Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>D004<br>~~VCC = 1.65 V~~<br>-40qC<br>25qC<br>~~85qC~~<br>**Figure 6-4. I/O Sink Current vs Output Low Voltage for Different**<br>**Temperature (TA) for VCC = 1.65 V**|
|VOL - Output Low Voltage (V)<br>IOL - Sink Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>D005<br>VCC = 1.8 V<br>-40qC<br>25qC<br>85qC<br>**Figure 6-5. I/O Sink Current vs Output Low Voltage for Different**<br>**Temperature (TA) for VCC = 1.8 V**|VOL - Output Low Voltage (V)<br>IOL - Sink Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>D006<br>~~VCC = 2.5 V~~<br>-40qC<br>25qC<br>~~85qC~~<br>**Figure 6-6. I/O Sink Current vs Output Low Voltage for Different**<br>**Temperature (TA) for VCC = 2.5 V**|



8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics (continued)**


TA = 25°C (unless otherwise noted)





**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)












|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||85|qC||||||||||||
|||||||||||||||
|VC|C = 3|.3 V||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
||85|qC||||||||||||
|||||||||||||||
|VCC|= 5|V||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||




























|Col1|-4|0qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~2~~<br>85|~~qC~~<br>qC||||||||||||
|~~V~~|~~ =~~|~~  .5 V~~||||||||||||
|~~C~~|~~C~~|||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|1.8 V<br>1.8 V|, 1 mA<br>, 10 mA|3.3 V, 10<br>5 V, 1 mA|mA|Col5|Col6|
|---|---|---|---|---|---|
|~~3.3 V~~|~~, 1mA~~|~~5 V, 10 m~~|~~   A~~|~~   A~~||
|||||||
|||||||
|||||||
|||||||
|||||||


























|Col1|-4<br>25<br>85|0qC<br>qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VC|C = 1|.65|V|||||||||||
|||||||||||||||
|||||||||||||||


|Col1|-4<br>25<br>85|0qC<br>qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|VCC|= 1|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|.8 V|
|||||||||||||||
|||||||||||||||
|||||||||||||||














|70<br>-40qC<br>25qC<br>60<br>85qC<br>(mA)<br>50<br>VCC = 3.3 V<br>Current<br>40<br>30 Sink<br>-<br>20 IOL<br>10<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>VOL - Output Low Voltage (V)<br>D007<br>Figure 6-7. I/O Sink Current vs Output Low Voltage for Different<br>Temperature (T ) for V = 3.3 V<br>A CC|80<br>-40qC<br>70 25qC<br>85qC<br>60 (mA)<br>VCC = 5 V<br>50 Current<br>40<br>Sink<br>30<br>-<br>IOL<br>20<br>10<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>VOL - Output Low Voltage (V)<br>D009<br>Figure 6-8. I/O Sink Current vs Output Low Voltage for Different<br>Temperature (T ) for V = 5 V<br>A CC|
|---|---|
|VOL - Output Low Voltage (V)<br>IOL - Sink Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>D010<br>~~VCC = 5.5 V~~<br>-40qC<br>~~25qC~~<br>85qC<br>**Figure 6-9. I/O Sink Current vs Output Low Voltage for Different**<br>**Temperature (TA) for VCC = 5.5 V**|TA - Temperature (°C)<br>VOL - Output Low Voltage (V)<br>-40<br>-15<br>10<br>35<br>60<br>85<br>0<br>50<br>100<br>150<br>200<br>250<br>300<br>D011<br>1.8 V, 1 mA<br>1.8 V, 10 mA<br>~~3.3 V, 1mA~~<br>3.3 V, 10 mA<br>5 V, 1 mA<br>~~5 V, 10 mA~~<br>**Figure 6-10. I/O Low Voltage vs Temperature for Different VCC**<br>**and IOL**|
|VCC-VOH - Output High Voltage (V)<br>IOH - Source Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>5<br>10<br>15<br>20<br>D012<br>VCC = 1.65 V<br>-40qC<br>25qC<br>85qC<br>**Figure 6-11. I/O Source Current vs Output High Voltage for**<br>**Different Temperature (TA) for VCC = 1.65 V**|VCC-VOH - Output High Voltage (V)<br>IOH - Source Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>5<br>10<br>15<br>20<br>25<br>D013<br>VCC = 1.8 V<br>-40qC<br>25qC<br>85qC<br>**Figure 6-12. I/O Source Current vs Output High Voltage for**<br>**Different Temperature (TA) for VCC = 1.8 V**|



Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 9


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics (continued)**


TA = 25°C (unless otherwise noted)














|Col1|-4|0qC<br>q|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
||~~2~~<br>85|~~C~~<br>qC||||||||||||
|||||||||||||||
|VC|C = 2|.5 V||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~8~~|~~qC~~||||||||||||
|~~V~~|~~ =~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|~~  .3 V~~|
|~~C~~|~~C~~|||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


























|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
||85|qC||||||||||||
|||||||||||||||
|||||||||||||||
|VC|C = 5|V||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|-4<br>25|0qC<br>qC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||85|qC||||||||||||
|VC|C = 5|.5 V||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||






























|1.65<br>2.5 V|V, 10 mA<br>, 10 mA|5 V, 10<br>5.5 V, 10|mA<br>mA|Col5|Col6|
|---|---|---|---|---|---|
|<br>3.6 V|<br>, 10 mA|||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||


|1.65 V<br>1.8 V|3.3<br>5 V|V|Col4|Col5|Col6|
|---|---|---|---|---|---|
|~~2.5 V~~|~~5.5~~|||||
|||||||
|||||||
|||||||
|||||||
|||||||














|40<br>-40qC<br>35 25qC<br>85qC<br>(mA)<br>30<br>VCC = 2.5 V<br>Current<br>25<br>20<br>Source<br>15<br>-<br>10 IOH<br>5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>VCC-VOH - Output High Voltage (V)<br>D014<br>Figure 6-13. I/O Source Current vs Output High Voltage for<br>Different Temperature (T ) for V = 2.5 V<br>A CC|60<br>-40qC<br>25qC<br>50 85qC<br>(mA)<br>40 VCC = 3.3 V Current<br>30<br>Source<br>20<br>-<br>IOH<br>10<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>VCC-VOH - Output High Voltage (V)<br>D015<br>Figure 6-14. I/O Source Current vs Output High Voltage for<br>Different Temperature (T ) for V = 3.3 V<br>A CC|
|---|---|
|VCC-VOH - Output High Voltage (V)<br>IOH - Source Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>D016<br>VCC = 5 V<br>-40qC<br>25qC<br>85qC<br>**Figure 6-15. I/O Source Current vs Output High Voltage for**<br>**Different Temperature (TA) for VCC = 5 V**|VCC-VOH - Output High Voltage (V)<br>IOH - Source Current (mA)<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>D017<br>VCC = 5.5 V<br>-40qC<br>~~25qC~~<br>85qC<br>**Figure 6-16. I/O Source Current vs Output High Voltage for**<br>**Different Temperature (TA) for VCC = 5.5 V**|
|TA - Temperature (°C)<br>VCC-VOH - I/O High Voltage (mV)<br>-40<br>-15<br>10<br>35<br>60<br>85<br>50<br>100<br>150<br>200<br>250<br>300<br>350<br>400<br>D018<br>1.65 V, 10 mA<br>2.5 V, 10 mA<br>3.6 V, 10 mA<br>5 V, 10 mA<br>5.5 V, 10 mA<br>**Figure 6-17. VCC – VOH Voltage vs Temperature for Different VCC**|TA - Temperature (°C)<br>Delta ICC (µA)<br>-40<br>-15<br>10<br>35<br>60<br>85<br>0<br>3<br>6<br>9<br>12<br>15<br>18<br>D019<br>1.65 V<br>1.8 V<br>~~2.5 V~~<br>3.3 V<br>5 V<br>~~5.5 V~~<br>**Figure 6-18. Δ ICC vs Temperature for Different VCC (VI = VCC –**<br>**0.6 V)**|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**Parameter Measurement Information**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



A. CL includes probe and jig capacitance.
B. All inputs are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr/tf ≤ 30 ns.
C. All parameters and waveforms are not applicable to all devices.


**Figure 7-1. I** **[2]** **C Interface Load Circuit and Voltage Waveforms**


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 11


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**VCC**


**Interrupt Load Configuration**














|CL 1 2 3 4 5 6 7 8<br>Target Address<br>DA S 1 1 1 0 1 A1 A0 1 A<br>Start R/W<br>Condition<br>om<br>ort<br>nto<br>ort<br>tph<br>INT<br>tiv tir|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Data From Port|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Data From Port|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|A P<br>Stop<br>oller Cond|Col29|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**CL**<br>**DA**<br>**INT**<br>**Start**<br>**Condition**<br>**R/W**<br>** om**<br>**ort**<br>** nto**<br>**ort**<br>**Target Address**<br>**8**<br>**7**<br>**6**<br>**5**<br>**4**<br>**3**<br>**2**<br>**1**<br>**A**<br>**tiv**<br>**tph**<br>**tir**<br>**S**<br>**1**<br>**1**<br>**1**<br>**0**<br>**1**<br>**A1 A0**<br>**1**|**1**|**1**|**1**|**0**|**1**|**A1**|** A0**|**1**<br>**A**||||**Dat**|**a 1**|||||**A**||||**Dat**|**a 4**|||**N**|**A**|**P**|
|**CL**<br>**DA**<br>**INT**<br>**Start**<br>**Condition**<br>**R/W**<br>** om**<br>**ort**<br>** nto**<br>**ort**<br>**Target Address**<br>**8**<br>**7**<br>**6**<br>**5**<br>**4**<br>**3**<br>**2**<br>**1**<br>**A**<br>**tiv**<br>**tph**<br>**tir**<br>**S**<br>**1**<br>**1**<br>**1**<br>**0**<br>**1**<br>**A1 A0**<br>**1**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|**Start**<br>**Condition**<br>**R/W**|
|**CL**<br>**DA**<br>**INT**<br>**Start**<br>**Condition**<br>**R/W**<br>** om**<br>**ort**<br>** nto**<br>**ort**<br>**Target Address**<br>**8**<br>**7**<br>**6**<br>**5**<br>**4**<br>**3**<br>**2**<br>**1**<br>**A**<br>**tiv**<br>**tph**<br>**tir**<br>**S**<br>**1**<br>**1**<br>**1**<br>**0**<br>**1**<br>**A1 A0**<br>**1**|||||||||||||||||||||||||||**Data 5**|**Data 5**|
|**CL**<br>**DA**<br>**INT**<br>**Start**<br>**Condition**<br>**R/W**<br>** om**<br>**ort**<br>** nto**<br>**ort**<br>**Target Address**<br>**8**<br>**7**<br>**6**<br>**5**<br>**4**<br>**3**<br>**2**<br>**1**<br>**A**<br>**tiv**<br>**tph**<br>**tir**<br>**S**<br>**1**<br>**1**<br>**1**<br>**0**<br>**1**<br>**A1 A0**<br>**1**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|**tph**|||
|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|**INT**<br>**tiv**|



**0.7** × **VCC**


**0.3** × **VCC**







**0.7** × **VCC**


**0.3** × **VCC**


**0.7** × **VCC**


**0.3** × **VCC**



**Data Into**


**Port (Pn)**



**0.7** × **VCC**


**0.3** × **VCC**



**INT**


|tiv|Col2|
|---|---|
|||



A. CL includes probe and jig capacitance.
B. All inputs are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr/tf ≤ 30 ns.
C. All parameters and waveforms are not applicable to all devices.


**Figure 7-2. Interrupt Load Circuit and Voltage Waveforms**


12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



A. CL includes probe and jig capacitance.
B. tpv is measured from 0.7 × VCC on SCL to 50% I/O (Pn) output.
C. All inputs are supplied by generators having the following characteristics: PRR ≤ 10 MHz, ZO = 50 Ω, tr/tf ≤ 30 ns.
D. The outputs are measured one at a time, with one transition per measurement.
E. All parameters and waveforms are not applicable to all devices.


**Figure 7-3. P-Port Load Circuit and Voltage Waveforms**


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 13


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**7 Detailed Description**
**7.1 Overview**

The TCA9535 device is a 16-bit I/O expander for the I [2] C bus and is designed for 1.65-V to 5.5-V VCC operation.
It provides general-purpose remote I/O expansion for most microcontroller families via the I [2] C interface.


The TCA9535 consists of two 8-bit Configuration (input or output selection), Input Port, Output Port, and Polarity
Inversion (active-high or active-low operation) registers. At power-on, the I/Os are configured as inputs. The
system controller can enable the I/Os as either inputs or outputs by writing to the I/O configuration register
bits. The data for each input or output is kept in the corresponding Input or output register. The polarity of the
Input Port register can be inverted with the Polarity Inversion register. All registers can be read by the system
controller.


The TCA9535 open-drain interrupt ( ~~INT)~~ output is activated when any input state differs from its corresponding
Input Port register state and is used to indicate to the system controller that an input state has changed.


~~INT~~ can be connected to the interrupt input of a microcontroller. By sending an interrupt signal on this line, the
remote I/O can inform the microcontroller if there is incoming data on its ports without having to communicate via
the I [2] C bus. Thus, the TCA9535 can remain a simple target device.


The device outputs (latched) have high-current drive capability for directly driving LEDs. The device has low
current consumption.


The TCA9535 device is similar to the PCA9555, except for the removal of the internal I/O pull-up resistor, which
greatly reduces power consumption when the I/Os are held low. The TCA9535 is equivalent to the PCA9535 with
lower voltage support (down to VCC = 1.65 V), and also improved power-on-reset circuitry for different application
scenarios.

Three hardware pins (A0, A1 and A2) are used to program and vary the fixed I [2] C address and allow up to 8
devices to share the same I [2] C bus or SMBus.


**7.2 Functional Block Diagram**























Pin numbers shown are for the PW package.


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


All I/Os are set to inputs at reset.


**Data From**
**Shift Register**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)


**Figure 7-1. Logic Diagram (Positive Logic)**


**Output Port**
**Register Data**





**Data From**
**Shift Register**







**Write Configuration**
**Pulse**


|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||







**VCC**


**I/O Pin**


**GND**


**Input Port**
**Register Data**


**To INT**


**Polarity**
**Register Data**





**Read Pulse**


**Data From**
**Shift Register**


**Write Polarity**
**Pulse**

|Configuration<br>Register<br>Q1<br>D Q<br>FF<br>D Q<br>CLK Q<br>FF<br>CLK Q<br>Output Port<br>Register<br>Q2<br>Input Port<br>Register<br>D Q<br>FF<br>CLK Q<br>D Q<br>FF<br>CLK Q|Col2|Col3|
|---|---|---|
|**CLK**<br>**D**<br>**Q**<br>**FF**<br>**Configuration**<br>**Register**<br>**Q**<br>**CLK**<br>**D**<br>**Q**<br>**FF**<br>**Q**<br>**Output Port**<br>**Register**<br>**Q1**<br>**Q2**<br>**CLK**<br>**D**<br>**Q**<br>**FF**<br>**Q**<br>**Input Port**<br>**Register**<br>**CLK**<br>**D**<br>**Q**<br>**FF**<br>**Q**|**CLK**<br>**D**<br>**Q**<br>**FF**<br>**Q**|**CLK**<br>**D**<br>**Q**<br>**FF**<br>**Q**|
||||
||||



At power-on reset, all registers return to default values.













**Polarity Inversion**
**Register**



**Figure 7-2. Simplified Schematic of P-Port I/Os**


**7.3 Feature Description**

**7.3.1 5-V Tolerant I/O Ports**


The TCA9535 features I/O ports, which are tolerant up to 5 V. This allows the TCA9535 to be connected to a
large array of devices. To minimize ICC, any input signals must be designed so the input voltage stays within VIH
and VIL of the device as described in the _Electrical Characteristics_ section.

**7.3.2 Hardware Address Pins**

The TCA9535 features 3 hardware address pins (A0, A1, and A2). The user selects the device I [2] C address
by pulling each pin to either VCC or GND to signify the bit value in the address. This allows up to 8 TCA9535
devices to be on the same bus without address conflicts. See the _Functional Block Diagram_ for the 3 address
pins. The voltage on the pins must not change while the device is powered up in order to prevent possible I [2] C
glitches as a result of the device address changing during a transmission. All of the pins must be tied either to
VCC or GND and cannot be left floating.


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 15


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**7.3.3 Interrupt (** ~~**INT)**~~ **Output**


An interrupt is generated by any rising or falling edge of the port inputs in the input mode. After time tiv, the signal
~~INT~~ is valid. Resetting the interrupt circuit is achieved when data on the port is changed to the original setting or
data is read from the port that generated the interrupt. Resetting occurs in the read mode at the acknowledge
(ACK) bit after the rising edge of the SCL signal. Note that the ~~INT~~ is reset at the ACK just before the byte of
changed data is sent. Interrupts that occur during the ACK clock pulse can be lost (or be very short) because
of the resetting of the interrupt during this pulse. Each change of the I/Os after resetting is detected and is
transmitted as ~~INT.~~


Reading from or writing to another device does not affect the interrupt circuit, and a pin configured as an output
cannot cause an interrupt. Changing an I/O from an output to an input may cause a false interrupt to occur
if the state of the pin does not match the contents of the Input Port register. Because each 8-bit port is read
independently, the interrupt caused by port 0 is not cleared by a read of port 1, or the interrupt caused by port 1
is not cleared by a read of port 0.


~~INT~~ has an open-drain structure. ~~INT~~ requires a pull-up resistor to VCC of moderate value (typically about 10 kΩ).

**7.4 Device Functional Modes**

**7.4.1 Power-On Reset (POR)**


When power (from 0 V) is applied to VCC, an internal power-on reset circuit holds the TCA9535 in a reset
condition until VCC has reached VPORR. At that time, the reset condition is released. The TCA9535 registers and
I [2] C-SMBus state machine initialize to their default states. Then, VCC must be lowered to below VPORF and back
up to the operating voltage for a power-reset cycle.


**7.4.2 Powered-Up**


When power has been applied to VCC above VPORR, and the POR has taken place, the device is in a functioning
mode. In this state, the device is ready to accept any incoming I [2] C requests and is monitoring for changes on the
input ports.


**7.5 Programming**

**7.5.1 I** **[2]** **C Interface**

The TCA9535 has a standard bidirectional I [2] C interface that is controlled by a controller device in order to
be configured or read the status of this device. Each target on the I [2] C bus has a specific device address
to differentiate between other target devices that are on the same I [2] C bus. Many target devices require
configuration upon startup to set the behavior of the device. This is typically done when the controller accesses
internal register maps of the target, which have unique register addresses. A device can have one or multiple
registers where data is stored, written, or read. For more information see _Understanding the I_ _[2]_ _C Bus_ application
[report, SLVA704.](https://www.ti.com/lit/pdf/SLVA704)

The physical I [2] C interface consists of the serial clock (SCL) and serial data (SDA) lines. Both SDA and SCL
lines must be connected to VCC through a pull-up resistor. The size of the pull-up resistor is determined by
the amount of capacitance on the I [2] C lines. For further details, see _I_ _[2]_ _C Pull-up Resistor Calculation_ application
[report, SLVA689. Data transfer may be initiated only when the bus is idle. A bus is considered idle if both SDA](https://www.ti.com/lit/pdf/SLVA689)
and SCL lines are high after a STOP condition. See Table 7-1.


Figure 7-3 and Figure 7-4 show the general procedure for a controller to access a target device:


1. If a controller wants to send data to a target:

   - Controller-transmitter sends a START condition and addresses the target-receiver.

   - Controller-transmitter sends data to target-receiver.

   - Controller-transmitter terminates the transfer with a STOP condition.
2. If a controller wants to receive or read data from a target:

   - Controller-receiver sends a START condition and addresses the target-transmitter.

   - Controller-receiver sends the requested register to read to target-transmitter.

   - Controller-receiver receives data from the target-transmitter.


16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


   - Controller-receiver terminates the transfer with a STOP condition.


SCL


SDA



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



SCL


SDA



START Data Transfer STOP

Condition Condition


**Figure 7-3. Definition of Start and Stop Conditions**


SDA line stable while SCL line is high

|0|Col2|
|---|---|
|0||



MSB Bit Bit Bit Bit Bit Bit LSB


Byte: 1010 1010 ( 0xAAh )


**Figure 7-4. Bit Transfer**



ACK



Table 7-1 shows the interface definition.





**Table 7-1. Interface Definition**



|BYTE|BIT|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**BYTE**|**7 (MSB)**|**6**|**5**|**4**|**3**|**2**|**1**|**0 (LSB)**|
|I2C target address|L|H|L|L|A2|A1|A0|R/~~ W~~|
|P0x I/O data bus|P07|P06|P05|P04|P03|P02|P01|P00|
|P1x I/O data bus|P17|P16|P15|P14|P13|P12|P11|P10|


_**7.5.1.1 Bus Transactions**_


Data is exchanged between the controller and the TCA9535 through write and read commands, and this is
accomplished by reading from or writing to registers in the target device.


Registers are locations in the memory of the target which contain information, whether it be the configuration
information or some sampled data to send back to the controller. The controller must write information to these
registers in order to instruct the target device to perform a task.


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 17


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**7.5.1.1.1 Writes**

To write on the I [2] C bus, the controller sends a START condition on the bus with the address of the target, as
well as the last bit (the R/ ~~W~~ bit) set to 0, which signifies a write. After the target sends the acknowledge bit, the
controller then sends the register address of the register to which it wishes to write. The target acknowledges
again, letting the controller know it is ready. After this, the controller starts sending the register data to the target
until the controller has sent all the data necessary (which is sometimes only a single byte), and the controller
terminates the transmission with a STOP condition.


See the _Control Register and Command Byte_ section to see list of the TCA9535 internal registers and a
description of each one.


Figure 7-5 shows an example of writing a single byte to a target register.

###### Controller controls SDA line Target controls SDA line Write to one register in a device



Device (Target) Address (7 bits)





Data Byte to Register N (8 bits)





Register Address N (8 bits)





START R/W=0 ACK ACK


**Figure 7-5. Write to Register**


Figure 7-6 shows the Write to the Polarity Inversion Register.

###### Controller controls SDA line Target controls SDA line



ACK STOP












|Device (Target) Address (7 bits) Register Address 0x02 (8 bits) Data Byte to Register 0x02 (8 bits)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||
|S|0|1|0|0|A2|A1|A0|0|A|0|0|0|0|0|1|0|0|A|D7|D6|D5|D4|D3|D2|D1|D0|A|P|



START R/W=0 ACK ACK ACK STOP


**Figure 7-6. Write to the Polarity Inversion Register**


Figure 7-7 shows the Write to Output Port Registers.


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)














|1 2 3 4 5 6 7 8<br>Target Address|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|9<br>Command Byte|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Data to Port 0|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|S|0|1|0|0|A2|A1|A0|0||A|0|0|||||||0|A<br>0.7|||||||0.0|A<br>1.7|A<br>1.7||||||||A|P|
|S|0|1|0|0|A2|A1|A0|0||A|0||0|0|0|0|0|1|1|1|||Da|a 0|||||7|||Data|1|||1.0|1.0|1.0|
|S|0|1|0|0|A2|A1|A0|0||A|0||||||||||||||||||||||||||||
|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|R/W<br>Start Condition<br>e to Port|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|
||||||||||||||||||||||||||||||||||||||||
|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0|Out from Port 0||||||||||||||||||||||||||||||
|||||||||||||||||||||tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|||
|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|Out from Port 1|||||||||||||||||||Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|Data Valid|
|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|tpv|



**Figure 7-7. Write to Output Port Registers**


**7.5.1.1.2 Reads**


Reading from a target is very similar to writing, but requires some additional steps. In order to read from a target,
the controller must first instruct the target which register it wishes to read from. This is done by the controller
starting off the transmission in a similar fashion as the write, by sending the address with the R/ ~~W~~ bit equal to
0 (signifying a write), followed by the register address it wishes to read from. When the target acknowledges this
register address, the controller sends a START condition again, followed by the target address with the R/ ~~W~~
bit set to 1 (signifying a read). This time, the target acknowledges the read request, and the controller releases
the SDA bus but continues supplying the clock to the target. During this part of the transaction, the controller
becomes the controller-receiver, and the target becomes the target-transmitter.


The controller continues to send out the clock pulses, but releases the SDA line so that the target can transmit
data. At the end of every byte of data, the controller sends an ACK to the target, letting the target know that it
is ready for more data. When the controller has received the number of bytes it is expecting, it sends a NACK,
signaling to the target to halt communications and release the bus. The controller follows this up with a STOP
condition.


See the _Control Register and Command Byte_ section to see list of the TCA9535's internal registers and a
description of each one.


Figure 7-8 shows an example of reading a single byte from a target register.


Controller controls SDA line


Target controls SDA line


Read from one register in a device














|Device (Target) Address (7 bits) Register Address N (8 bits) Device (Target) Address (7 bits) Data Byte from Register N (8 bits)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|<br> <br> <br>|
|S|0|1|0|0|A2|A1|A0|0|A|B7|B6|B5|B4|B3|B2|B1|B0|A<br>S|r<br>0|1|0|0|A2|A1|A0|1<br>A|D7|D6|D5|D4|D3|D2|D1|D0<br>|NA|P|





START R/W=0 ACK ACK





ACK NACK STOP



**Figure 7-8. Read from Register**


After a restart, the value of the register defined by the command byte matches the register being accessed when
the restart occurred. For example, if the command byte references Input Port 1 before the restart, and the restart
occurs when Input Port 0 is being read, the stored command byte changes to reference Input Port 0. The original
command byte is forgotten. If a subsequent restart occurs, Input Port 0 is read first. Data is clocked into the
register on the rising edge of the ACK clock pulse. After the first byte is read, additional bytes may be read, but
the data now reflect the information in the other register in the pair. For example, if Input Port 1 is read, the next
byte read is Input Port 0.


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 19


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


Data is clocked into the register on the rising edge of the ACK clock pulse. There is no limitation on the number
of data bytes received in one read transmission, but when the final byte is received, the bus controller must not
acknowledge the data. Figure 7-9 and Figure 7-10 show two different scenarios of Read Input Port Register.



SCL


SDA

















INT


|1 2 3 4 5 6 7 8|Col2|Col3|Col4|Col5|Col6|Col7|Col8|9<br>I0.x|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|I1.x|Col20|Col21|Col22|Col23|Col24|Col25|Col26|I0.x|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|I1.x|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|Col45|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|S|0|1|0|0<br>A|2 A1|A0|1|A|7|6|5|4|3|3|2|1|0|A|7|6|5|4|3|2|1<br>0|A|7|6|5|4|3|2|1|0<br>|A<br>7|6|5|4|3|2|1|0|1|P|
|R/W<br> From Port 0|R/W<br> From Port 0|R/W<br> From Port 0|R/W<br> From Port 0|R/W<br> From Port 0|R/W<br> From Port 0|R/W<br> From Port 0|R/W<br> From Port 0|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Target|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|
||||||||||||||||||||||||||||||||||||||||||||||
|Into Port 0|Into Port 0|Into Port 0|Into Port 0|Into Port 0|||||||||||||||||||||||||||||||||||||||||
|From Port 1|From Port 1|From Port 1|From Port 1|From Port 1|||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
|Into Port 1|Into Port 1|Into Port 1|Into Port 1|Into Port 1|||||||||||||||||||||||||||||||||||||||||
|||||||||tir|tir|tir|tir|tir|tir||||||||||||||||||||||||||||||||
|tiv|tiv|tiv|tiv|tiv||||||tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|tir|
|tiv|tiv|tiv|tiv|tiv|||||||||||||||||||||||||||||||||||||||||



SCL


SDA



Transfer of data can be stopped at any time by a Stop condition. When this occurs, data present at the latest acknowledge phase is
valid (output mode). It is assumed that the command byte previously has been set to 00 (read Input Port register).
This figure eliminates the command byte transfer, a restart, and target address call between the initial target address call and actual
data transfer from the P port.


**Figure 7-9. Read Input Port Register, Scenario 1**



































INT














|1 2 3 4 5 6 7 8|Col2|Col3|Col4|Col5|Col6|Col7|Col8|9<br>10.x|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|11.x|Col19|Col20|Col21|Col22|Col23|Col24|Col25|10.x|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|11.x|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|Col45|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|S|0|1|0|0<br>A|2<br>A|1 A0|0<br>1|A|||||00||||A|||||10|||A|||||03||||A|A||||11||||1|P|
|R/W<br> rom Port 0|R/W<br> rom Port 0|R/W<br> rom Port 0|R/W<br> rom Port 0|R/W<br> rom Port 0|R/W<br> rom Port 0|R/W<br> rom Port 0|R/W<br> rom Port 0|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|t<br>ph<br>Acknowledge<br>From Target|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|tps<br>Acknowledge<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|t<br>ph<br>Acknowledge<br>From Controller<br>No Acknowledg<br>From Controller|
||||||||||||||||||||||||||||||||||||||||||||||
|to Port 0|to Port 0|to Port 0|to Port 0|to Port 0|Data 00|Data 00|Data 00|||Data 01|Data 01|Data 01|Data 01|Data 01|Data 01|Data 01|||Data 02|Data 02|Data 02|Data 02|Data 02|Data 02|Data 03|Data 03|Data 03|Data 03|Data 03|Data 03|Data 03|Data 03|Data 03||||||||||||
|rom Port 1|rom Port 1|rom Port 1|rom Port 1|rom Port 1||||t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|||t<br>ph|t<br>ph|t<br>ph|t<br>ph|t<br>ph|t<br>ph|||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||
|to Port 1|to Port 1|to Port 1|to Port 1|to Port 1||||Data 10|Data 10|Data 10|Data 10||||||||11<br>Data|11<br>Data|11<br>Data|11<br>Data|11<br>Data|11<br>Data|||||||||||||12<br>Data|12<br>Data|12<br>Data|12<br>Data|12<br>Data|12<br>Data|12<br>Data|12<br>Data|
||||||||||||||||||||||||||t<br>ir|t<br>ir|t<br>ir|t<br>ir|t<br>ir|t<br>ir|t<br>ir|t<br>ir|t<br>ir||||t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|
||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|t<br>iv|



Transfer of data can be stopped at any time by a Stop condition. When this occurs, data present at the latest acknowledge phase is
valid (output mode). It is assumed that the command byte previously has been set to 00 (read Input Port register).
This figure eliminates the command byte transfer, a restart, and target address call between the initial target address call and actual
data transfer from the P port.


**Figure 7-10. Read Input Port Register, Scenario 2**


**7.5.2 Device Address**


Figure 7-11 shows the address byte of the TCA9535.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



R/W

|Target Address|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|0|1|0|0|A2|A1|A0|||
||||||||||



Fixed Programmable


**Figure 7-11. TCA9535 Address**


Table 7-2 shows the address reference of the TCA9535.


**Table 7-2. Address Reference**

|INPUTS|Col2|Col3|I2C BUS TARGET ADDRESS|
|---|---|---|---|
|**A2**|**A1**|**A0**|**A0**|
|L|L|L|32 (decimal), 0×20 (hexadecimal)|
|L|L|H|33 (decimal), 0x21 (hexadecimal)|
|L|H|L|34 (decimal), 0x22 (hexadecimal)|
|L|H|H|35 (decimal), 0x23 (hexadecimal)|
|H|L|L|36 (decimal), 0x24 (hexadecimal)|
|H|L|H|37 (decimal), 0x25 (hexadecimal)|
|H|H|L|38 (decimal), 0x26 (hexadecimal)|
|H|H|H|39 (decimal), 0x27 (hexadecimal)|



The last bit of the target address defines the operation (read or write) to be performed. A high (1) selects a read
operation, while a low (0) selects a write operation.


**7.5.3 Control Register and Command Byte**


Following the successful acknowledgment of the address byte, the bus controller sends a command byte shown
in Table 7-3 that is stored in the control register in the TCA9535. Three bits of this data byte state the operation
(read or write) and the internal register (input, output, polarity inversion, or configuration) that is affected. This
register can be written or read through the I [2] C bus. The command byte is sent only during a write transmission.


When a command byte has been sent, the register that was addressed continues to be accessed by reads until
a new command byte has been sent. Figure 7-12 shows the control register bits.


0 0 0 0 0 B2 B1 B0


**Figure 7-12. Control Register Bits**


**Table 7-3. Command Byte**

|CONTROL REGISTER BITS|Col2|Col3|COMMAND<br>BYTE (HEX)|REGISTER|PROTOCOL|POWER-UP<br>DEFAULT|
|---|---|---|---|---|---|---|
|**B2**|**B1**|**B0**|**B0**|**B0**|**B0**|**B0**|
|0|0|0|0x00|Input Port 0|Read byte|xxxx xxxx|
|0|0|1|0x01|Input Port 1|Read byte|xxxx xxxx|
|0|1|0|0x02|Output Port 0|Read-write byte|1111 1111|
|0|1|1|0x03|Output Port 1|Read-write byte|1111 1111|
|1|0|0|0x04|Polarity Inversion Port 0|Read-write byte|0000 0000|
|1|0|1|0x05|Polarity Inversion Port 1|Read-write byte|0000 0000|
|1|1|0|0x06|Configuration Port 0|Read-write byte|1111 1111|
|1|1|1|0x07|Configuration Port 1|Read-write byte|1111 1111|



Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 21


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**7.6 Register Maps**

**7.6.1 Register Descriptions**


The Input Port registers (registers 0 and 1) shown in Table 7-4 reflect the incoming logic levels of the pins,
regardless of whether the pin is defined as an input or an output by the Configuration Register. It only acts on
read operation. Writes to these registers have no effect. The default value, X, is determined by the externally
applied logic level.

Before a read operation, a write transmission is sent with the command byte to let the I [2] C device know that the
Input Port registers are accessed next.


**Table 7-4. Registers 0 and 1 (Input Port Registers)**

|Bit|I0.7|I0.6|I0.5|I0.4|I0.3|I0.2|I0.1|I0.0|
|---|---|---|---|---|---|---|---|---|
|**Default**|X|X|X|X|X|X|X|X|
|**Bit**|**I1.7**|**I1.6**|**I1.5**|**I1.4**|**I1.3**|**I1.2**|**I1.1**|**I1.0**|
|**Default**|X|X|X|X|X|X|X|X|



The Output Port registers (registers 2 and 3) shown in Table 7-5 show the outgoing logic levels of the pins
defined as outputs by the Configuration register. Bit values in this register have no effect on pins defined as
inputs. In turn, reads from this register reflect the value that is in the flip-flop controlling the output selection, not
the actual pin value.


**Table 7-5. Registers 2 and 3 (Output Port Registers)**

|Bit|O0.7|O0.6|O0.5|O0.4|O0.3|O0.2|O0.1|O0.0|
|---|---|---|---|---|---|---|---|---|
|**Default**|1|1|1|1|1|1|1|1|
|**Bit**|**O1.7**|**O1.6**|**O1.5**|**O1.4**|**O1.3**|**O1.2**|**O1.1**|**O1.0**|
|**Default**|1|1|1|1|1|1|1|1|



The Polarity Inversion registers (registers 4 and 5) shown in Table 7-6 allow polarity inversion of pins defined as
inputs by the Configuration register. If a bit in this register is set (written with 1), the corresponding pin's polarity
is inverted. If a bit in this register is cleared (written with a 0), the corresponding pin's original polarity is retained.


**Table 7-6. Registers 4 and 5 (Polarity Inversion Registers)**

|Bit|N0.7|N0.6|N0.5|N0.4|N0.3|N0.2|N0.1|N0.0|
|---|---|---|---|---|---|---|---|---|
|**Default**|0|0|0|0|0|0|0|0|
|**Bit**|**N1.7**|**N1.6**|**N1.5**|**N1.4**|**N1.3**|**N1.2**|**N1.1**|**N1.0**|
|**Default**|0|0|0|0|0|0|0|0|



The Configuration registers (registers 6 and 7) shown in Table 7-7 configure the directions of the I/O pins. If a bit
in this register is set to 1, the corresponding port pin is enabled as an input with a high-impedance output driver.
If a bit in this register is cleared to 0, the corresponding port pin is enabled as an output.


**Table 7-7. Registers 6 and 7 (Configuration Registers)**

|Bit|C0.7|C0.6|C0.5|C0.4|C0.3|C0.2|C0.1|C0.0|
|---|---|---|---|---|---|---|---|---|
|**Default**|1|1|1|1|1|1|1|1|
|**Bit**|**C1.7**|**C1.6**|**C1.5**|**C1.4**|**C1.3**|**C1.2**|**C1.1**|**C1.0**|
|**Default**|1|1|1|1|1|1|1|1|



22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**8 Application and Implementation**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



**Note**


Information in the following applications sections is not part of the TI component specification, and
TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining
suitability of components for their purposes. Customers should validate and test their design
implementation to confirm system functionality.


**8.1 Application Information**

Applications of the TCA9535 has the device connected as a target to an I [2] C controller (processor), and the I [2] C
bus may contain any number of other target devices. The TCA9535 is typically in a remote location from the
controller, placed close to the GPIOs to which the controller needs to monitor or control.


IO Expanders such as the TCA9535 are typically used for controlling LEDs (for feedback or status lights),
controlling enable or reset signals of other devices, and even reading the outputs of other devices or buttons.


**8.2 Typical Application**


Figure 8-1 shows an application in which the TCA9535 can be used.



























GND


Controlled Switch
(e.g., CBT Device)


ALARM


Subsystem 3
(e.g., Alarm)






|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
||||3|






|Col1|Col2|Col3|100 k<br><br>(X 3)|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X||||||||
|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X||||||||
|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X||10 k<br><br>( 5)<br>X||||||
|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X|7<br>8<br>9<br>10<br>10 k<br><br>( 5)<br>X||10 k<br><br>( 5)<br>X||||||
|11|11|11|11||||||
|13|13|13|13||||||
|14|14|14|14||||||
|15|15|15|15||||||
|15|15|15|15||||||
|15|15|15|15||||||
|15|15|15|15||||||
|15|15|15|15||||||
|15|15|15|15||||||



Device address is configured as 0100100 for this example.
P00, P02, and P03 are configured as outputs.
P01, P04–P07, and P10–P17 are configured as inputs.
Pin numbers shown are for the PW package.


**Figure 8-1. Application Schematic**


**8.2.1 Design Requirements**


The designer must take into consideration the system, to be sure not to violate any of the parameters. Table 8-1
shows some key parameters which must not be violated.


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 23


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**Table 8-1. Design Parameters**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|I2C and Subsystem Voltage (VCC)|5 V|
|Output current rating, P-port<br>sinking (IOL)|25 mA|
|I2C bus clock (SCL) speed|400 kHz|



_**8.2.1.1 Calculating Junction Temperature and Power Dissipation**_


When designing with this device, it is important that the _Recommended Operating Conditions_ not be violated.
Many of the parameters of this device are rated based on junction temperature. So junction temperature must be
calculated in order to verify that safe operation of the device is met. The basic equation for junction temperature
is shown in Equation 1.

###### Tj � TA ��� JA � Pd � (1)


θJA is the standard junction to ambient thermal resistance measurement of the package, as seen in _Thermal_
_Information_ table. Pd is the total power dissipation of the device, and the approximation is shown in Equation 2.

# Pd � �ICC_STATIC � VCC� � �Pd_PORT _L � �Pd_PORT _H (2)


Equation 2 is the approximation of power dissipation in the device. The equation is the static power plus the
summation of power dissipated by each port (with a different equation based on if the port is outputting high,
or outputting low. If the port is set as an input, then power dissipation is the input leakage of the pin multiplied
by the voltage on the pin). Note that this ignores power dissipation in the ~~INT~~ and SDA pins, assuming these
transients to be small. They can easily be included in the power dissipation calculation by using Equation 3
to calculate the power dissipation in ~~INT~~ or SDA while they are pulling low, and this gives maximum power
dissipation.

###### Pd_PORT _L � �IOL � VOL � (3)


Equation 3 shows the power dissipation for a single port which is set to output low. The power dissipated by the
port is the VOL of the port multiplied by the current it is sinking.

## Pd_PORT _H � �IOH � �VCC � VOH�� (4)


Equation 4 shows the power dissipation for a single port which is set to output high. The power dissipated by the
port is the current sourced by the port multiplied by the voltage drop across the device (difference between VCC
and the output voltage).


_**8.2.1.2 Minimizing ICC When I/O is Used to Control LED**_

When an I/O is used to control an LED, normally it is connected to VCC through a resistor as shown in Figure
8-1. Because the LED acts as a diode, when the LED is off, the I/O VIN is about 1.2 V less than VCC. The ΔICC
parameter in the _Electrical Characteristics_ table shows how ICC increases as VIN becomes lower than VCC. For
battery-powered applications, it is essential that the voltage of I/O pins is greater than or equal to VCC when the
LED is off to minimize current consumption.


Figure 8-2 shows a high-value resistor in parallel with the LED. Figure 8-3 shows VCC less than the LED supply
voltage by at least 1.2 V. Both of these methods maintain the I/O VIN at or above VCC and prevent additional
supply current consumption when the LED is off.


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)





VCC



**Figure 8-2. High-Value Resistor in Parallel With LED**


3.3 V 5 V







**Figure 8-3. Device Supplied by Lower Voltage**


**8.2.2 Detailed Design Procedure**


The pull-up resistors, RP, for the SCL and SDA lines need to be selected appropriately and take into
consideration the total capacitance of all targets on the I [2] C bus. The minimum pull-up resistance is a function of
VCC, VOL,(max), and IOL as shown in Equation 5.



VCC     - V
Rp(min) I



CC  



CC OL(max)
p(min) 
IOL



(5)



The maximum pull-up resistance is a function of the maximum rise time, tr (300 ns for fast-mode operation, fSCL
= 400 kHz) and bus capacitance, Cb as shown in Equation 6.


Rp(max)   - tr
0.8473       - Cb (6)


The maximum bus capacitance for an I [2] C bus must not exceed 400 pF for standard-mode or fast-mode
operation. The bus capacitance can be approximated by adding the capacitance of the TCA9535, Ci for SCL or
CIO for SDA, the capacitance of wires/connections/traces, and the capacitance of additional targets on the bus.
For further details, refer to _I_ _[2]_ _C Pull-up Resistor Calculation_ [application report, SLVA689.](https://www.ti.com/lit/pdf/SLVA689)


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 25


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**8.2.3 Application Curves**



25


20


15


10


5





1.8


1.6


1.4


1.2


1


0.8


0.6


0.4


0.2





0

|Col1|Col2|Col3|Col4|Col5|Sta<br>Fa|ndard-<br>st-Mod|Mode<br>e|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||

0 50 100 150 200 250 300 350 400 450



0

|Col1|VDPU|X > 2|V|Col5|Col6|
|---|---|---|---|---|---|
||~~V~~DUP|X~~ </=~~|~~ 2~~|||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5



Bus Capacitance (pF)


Standard-mode: fSCL = 100 kHz, tr = 1 µs
Fast-mode: fSCL = 400 kHz, tr = 300 ns



D008



Pull-Up Reference Voltage (V)

VOL = 0.2 × VCC, IOL = 2 mA when VCC ≤ 2 V
VOL = 0.4 V, IOL = 3 mA when VCC > 2 V



D009



**Figure 8-4. Maximum Pull-Up Resistance (Rp(max))**

**vs Bus Capacitance (Cb)**



**Figure 8-5. Minimum Pull-Up Resistance (Rp(min))**

**vs Pull-Up Reference Voltage (VCC)**



26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**9 Power Supply Recommendations**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



In the event of a glitch or data corruption, TCA9535 can be reset to its default conditions by using the power-on
reset feature. Power-on reset requires that the device go through a power cycle to be completely reset. This
reset also happens when the device is powered on for the first time in an application.


The two types of power-on reset are shown in Figure 9-1 and Figure 9-2.


Time

|CC|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Ramp-Up||Ramp-Down|~~VCC_TRR_GND~~|Re-Ramp-Up||
|Ramp-Up||||||
|~~V~~||~~V~~|Time to Re-Ramp|~~V~~|~~V~~|



**Figure 9-1. VCC Is Lowered Below 0.2 V Or 0 V And Then Ramped Up To VCC**


VCC









Time


|V drops below POR levels<br>IN|Ramp-Down|V<br>CC_TRR_VPOR50|Ramp-Up|Col5|
|---|---|---|---|---|
||||||
||~~VCC_FT~~|Time to Re-Ramp|~~VCC_RT~~||



**Figure 9-2. VCC Is Lowered Below The Por Threshold, Then Ramped Back Up To VCC**


Table 9-1 specifies the performance of the power-on reset feature for TCA9535 for both types of power-on reset.


**Table 9-1. Recommended Supply Sequencing And Ramp Rates**







|PARAMETER(1)|Col2|MIN|TYP|MAX|UNIT|
|---|---|---|---|---|---|
|VCC_FT<br>Fall rate|SeeFigure 9-1|0.1|0.1|0.1|ms|
|VCC_RT<br>Rise rate|SeeFigure 9-1|0.01|0.01|0.01|ms|
|VCC_TRR<br>Time to re-ramp (when VCC drops to VVOR_MIN– 50 mV or<br>when VCC drops to GND)|SeeFigure 9-1|1|1|1|µs|
|VCC_GH<br>The level (referenced to VCC) that VCC can glitch down to, but<br>not cause a functional disruption when VCC_GW|SeeFigure 9-3|1.2|1.2|1.2|V|
|VCC_MV<br>The minimum voltage that VCC can glitch down to without<br>causing a reset (VCC_GH must not be violated)|SeeFigure 9-3|1.5|1.5|1.5|V|
|VCC_GW<br>Glitch width that will not cause a functional disruption|SeeFigure 9-3|10|10|10|μs|
|VPORF<br>Voltage trip point of POR on falling VCC||0.75<br>1<br>1|0.75<br>1<br>1|0.75<br>1<br>1|V|
|VPORR<br>Voltage trip point of POR on rising VCC||1.2<br>1.5|1.2<br>1.5|1.2<br>1.5|V|


(1) TA = –40°C to 85°C (unless otherwise noted)


Glitches in the power supply can also affect the power-on reset performance of this device. The glitch width
(VCC_GW) and height (VCC_GH) are dependent on each other. The bypass capacitance, source impedance, and
device impedance are factors that affect power-on reset performance. Figure 9-3 and Table 9-1 provide more
information on how to measure these specifications.


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 27


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


VCC


Time

|Col1|Col2|Col3|
|---|---|---|
|VCC_GH|VCC_GH|VCC_GH|
|VCC_GH|||
||~~VCC_GW~~||



**Figure 9-3. Glitch Width And Glitch Height**


VPORR is critical to the power-on reset. VPORR is the voltage level at which the reset condition is released and
all the registers and the I [2] C/SMBus state machine are initialized to their default states. The value of VPOR differs
based on the VCC being lowered to or from 0. Figure 9-4 and Table 9-1 provide more details on this specification.


VCC


VPOR


VPORF


Time


Time

|Col1|Col2|
|---|---|
|||
|||



**Figure 9-4. VPOR**


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[www.ti.com](https://www.ti.com)**


**10 Layout**
**10.1 Layout Guidelines**



**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201)



For printed circuit board (PCB) layout of the TCA9535, common PCB layout practice must be followed, but
additional concerns related to high-speed data transfer such as matched impedances and differential pairs are
not a concern for I [2] C signal speeds.


In all PCB layouts, it is a best practice to avoid right angles in signal traces, to fan out signal traces away from
each other upon leaving the vicinity of an integrated circuit (IC), and to use thicker trace widths to carry higher
amounts of current that commonly pass through power and ground traces. By-pass and de-coupling capacitors
are commonly used to control the voltage on the VCC pin, using a larger capacitor to provide additional power
in the event of a short power supply glitch and a smaller capacitor to filter out high-frequency ripple. These
capacitors must be placed as close to the TCA9535 as possible. These best practices are shown in the _Layout_
_Example_ .


For the layout example provided in the _Layout Example_, it must be possible to fabricate a PCB with only 2
layers by using the top layer for signal routing and the bottom layer as a split plane for power (VCC) and ground
(GND). However, a 4 layer board is preferable for boards with higher density signal routing. On a 4 layer PCB,
it is common to route signals on the top and bottom layer, dedicate one internal layer to a ground plane, and
dedicate the other internal layer to a power plane. In a board layout using planes or split planes for power and
ground, vias are placed directly next to the surface mount component pad which needs to attach to VCC, or GND
and the via is connected electrically to the internal layer or the other side of the board. Vias are also used when
a signal trace needs to be routed to the opposite side of the board, but this technique is not demonstrated in the
_Layout Example_ .


**10.2 Layout Example**













= Via to GND Plane


**Figure 10-1. TCA9535 Layout Example**


Copyright © 2022 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ 29


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


**[TCA9535](https://www.ti.com/product/TCA9535)**
[SCPS201E – AUGUST 2009 – REVISED MAY 2022](https://www.ti.com/lit/pdf/SCPS201) **[www.ti.com](https://www.ti.com)**


**11 Device and Documentation Support**
**11.1 Documentation Support**

**11.1.1 Related Documentation**


For related documentation see the following:


 - _I2C Bus Pull-Up Resistor Calculation_ [, SLVA689](https://www.ti.com/lit/pdf/SLVA689)

 - _Maximum Clock Frequency of I2C Bus Using Repeaters_ [, SLVA695](https://www.ti.com/lit/pdf/SLVA695)

 - _Introduction to Logic_ [, SLVA700](https://www.ti.com/lit/pdf/SLVA700)

 - _Understanding the I2C Bus_ [, SLVA704](https://www.ti.com/lit/pdf/SLVA704)

 - _IO Expander EVM User's Guide_ [, SLVUA59A](https://www.ti.com/lit/pdf/SLVUA59A)


**11.2 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Subscribe to updates_ to register and receive a weekly digest of any product information that has changed. For
change details, review the revision history included in any revised document.


**11.3 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**11.4 Trademarks**
TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.
**11.5 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**11.6 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**12 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SCPS201E&partnum=TCA9535)_ Copyright © 2022 Texas Instruments Incorporated


Product Folder Links: _[TCA9535](https://www.ti.com/product/tca9535?qgpn=tca9535)_


##### **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Nov-2025


**PACKAGING INFORMATION**





















**(1) Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)


Addendum-Page 1


##### **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Nov-2025


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
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 2


##### **PACKAGE MATERIALS INFORMATION**

www.ti.com 9-Oct-2025


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
|TCA9535DBR|SSOP|DB|24|2000|330.0|16.4|8.2|8.8|2.5|12.0|16.0|Q1|
|TCA9535DBT|SSOP|DB|24|250|330.0|16.4|8.2|8.8|2.5|12.0|16.0|Q1|
|TCA9535MRGER|VQFN|RGE|24|3000|330.0|12.4|4.25|4.25|1.15|8.0|12.0|Q2|
|TCA9535PWR|TSSOP|PW|24|2000|330.0|16.4|6.95|8.3|1.6|8.0|16.0|Q1|
|TCA9535PWRG4|TSSOP|PW|24|2000|330.0|16.4|6.95|8.3|1.6|8.0|16.0|Q1|
|TCA9535RGER|VQFN|RGE|24|3000|330.0|12.4|4.25|4.25|1.15|8.0|12.0|Q2|
|TCA9535RGERG4|VQFN|RGE|24|3000|330.0|12.4|4.25|4.25|1.15|8.0|12.0|Q2|
|TCA9535RTWR|WQFN|RTW|24|3000|330.0|12.4|4.25|4.25|1.15|8.0|12.0|Q2|
|TCA9535RTWRG4|WQFN|RTW|24|3000|330.0|12.4|4.25|4.25|1.15|8.0|12.0|Q2|


Pack Materials-Page 1


##### **PACKAGE MATERIALS INFORMATION**

www.ti.com 9-Oct-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TCA9535DBR|SSOP|DB|24|2000|353.0|353.0|32.0|
|TCA9535DBT|SSOP|DB|24|250|353.0|353.0|32.0|
|TCA9535MRGER|VQFN|RGE|24|3000|346.0|346.0|33.0|
|TCA9535PWR|TSSOP|PW|24|2000|353.0|353.0|32.0|
|TCA9535PWRG4|TSSOP|PW|24|2000|353.0|353.0|32.0|
|TCA9535RGER|VQFN|RGE|24|3000|346.0|346.0|33.0|
|TCA9535RGERG4|VQFN|RGE|24|3000|346.0|346.0|33.0|
|TCA9535RTWR|WQFN|RTW|24|3000|353.0|353.0|32.0|
|TCA9535RTWRG4|WQFN|RTW|24|3000|353.0|353.0|32.0|



Pack Materials-Page 2


##### **GENERIC PACKAGE VIEW**

#### **RGE 24 VQFN - 1 mm max height**

PLASTIC QUAD FLATPACK - NO LEAD


Images above are just a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4204104/H


#### **PACKAGE OUTLINE**
### RGE0024B SCALE 3.000 VQFN - 1 mm max height

PLASTIC QUAD FLATPACK - NO LEAD






















|0.1|C|A|B|
|---|---|---|---|
|0.05|0.05|0.05|0.05|



NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.


www.ti.com


#### **EXAMPLE BOARD LAYOUT**
### **RGE0024B VQFN - 1 mm max height**

PLASTIC QUAD FLATPACK - NO LEAD































NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.


www.ti.com


#### **EXAMPLE STENCIL DESIGN**
### **RGE0024B VQFN - 1 mm max height**

PLASTIC QUAD FLATPACK - NO LEAD





















NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


www.ti.com


#### **PACKAGE OUTLINE**
### PW0024A SCALE 2.000 TSSOP - 1.2 mm max height

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


#### **EXAMPLE BOARD LAYOUT**
### **PW0024A TSSOP - 1.2 mm max height**

SMALL OUTLINE PACKAGE































NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


#### **EXAMPLE STENCIL DESIGN**
### **PW0024A TSSOP - 1.2 mm max height**

SMALL OUTLINE PACKAGE

















NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.


www.ti.com


#### **GENERIC PACKAGE VIEW**
### **RTW 24 WQFN - 0.8 mm max height**

**4 x 4, 0.5 mm pitch** PLASTIC QUAD FLATPACK - NO LEAD


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4224801/A


www.ti.com


#### **PACKAGE OUTLINE** **RTW0024B WQFN - 0.8 mm max height**

PLASTIC QUAD FLATPACK-NO LEAD







4.15
3.85



PIN 1 INDEX AREA









4219135/B  11/2016



4.15
3.85

|7|Col2|12|Col4|Col5|
|---|---|---|---|---|
|||25|25|25|
|||25|||
||||||
||||||
||||||



24 19


SYMM

24X [0.5]

0.3



13



EXPOSED
THERMAL PAD


2.45±0.1



2X



6


SYMM


1



PIN 1 ID
(OPTIONAL)


|0.3 0.18|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|0.1|C|C|A|B|
|0.05|0.05|C|C|C|



NOTES:


1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.


**www.ti.com**


#### **EXAMPLE BOARD LAYOUT** **RTW0024B WQFN - 0.8 mm max height**

PLASTIC QUAD FLATPACK-NO LEAD


(  2.45)



18


13



24X (0.6)


SYMM


20X (0.5)





(0.97)


(3.8)


SOLDER MASK
OPENING



(R0.05)

TYP


(Ø0.2) TYP

VIA


NOTES: (continued)



|Col1|Col2|Col3|19|
|---|---|---|---|
|||||
|||||
|||||
||25|25|25|
|||||


(0.97)


(3.8)


LAND PATTERN EXAMPLE

SCALE: 20X


0.07 MAX
0.07 MIN
ALL AROUND


SOLDER MASK
OPENING


NON SOLDER MASK



SOLDER MASK



DEFINED
(PREFERRED)


SOLDER MASK DETAILS



SOLDER MASK

DEFINED



4219135/B  11/2016



3. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).


**www.ti.com**


#### **EXAMPLE STENCIL DESIGN** **RTW0024B WQFN - 0.8 mm max height**

PLASTIC QUAD FLATPACK-NO LEAD


4X(  1.08)


(0.64) TYP



(R0.05) TYP


20X (0.5)


METAL

TYP


NOTES: (continued)



|24|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
||25|||||
|||||||
|||||||
|||||||
|||||||


(3.8)


SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL


EXPOSED PAD 25:
78% PRINTED COVERAGE BY AREA UNDER PACKAGE

SCALE: 20X



18


13



(0.64)

TYP


(3.8)


4219135/B  11/2016



4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


**www.ti.com**


##### **MECHANICAL DATA**

MSSO002E – JANUARY 1995 – REVISED DECEMBER 2001


**DB (R-PDSO-G**)** **PLASTIC SMALL-OUTLINE**

**28 PINS SHOWN**




|Col1|Col2|0,15 M|
|---|---|---|
||||



**28**



**15**















































**4040065 /E 12/01**


|PINS **<br>DIM|14|16|20|24|28|30|38|
|---|---|---|---|---|---|---|---|
|A  MAX|6,50|6,50|7,50|8,50|10,50|10,50|12,90|
|A  MIN|5,90|5,90|6,90|7,90|9,90|9,90|12,30|



NOTES: A. All linear dimensions are in millimeters.
B. This drawing is subject to change without notice.
C. Body dimensions do not include mold flash or protrusion not to exceed 0,15.
D. Falls within JEDEC MO-150


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


