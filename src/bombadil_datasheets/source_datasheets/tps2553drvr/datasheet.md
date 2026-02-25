Reference
Design



Support &
Community



Product

Folder



Sample &
Buy



Technical

Documents



Tools &
Software



**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016
### **TPS255xx Precision Adjustable Current-Limited Power-Distribution Switches**



**1** **Features**


1• Up to 1.5-A Maximum Load Current

- ±6% Current-Limit Accuracy at 1.7 A (Typical)

- Meets USB Current-Limiting Requirements

- Backwards Compatible With TPS2550 and
TPS2551

- Adjustable Current Limit: 75 mA to 1700 mA
(Typical)

- Constant-Current (TPS255x) and Latch-Off
(TPS255x-1) Versions

- Fast Overcurrent Response - 2 µs (Typical)

- 85-m Ω High-Side MOSFET (DBV Package)

- Reverse Input-Output Voltage Protection

- Operating Range: 2.5 V to 6.5 V

- Built-In Soft Start

- 15-kV ESD Protection per IEC 61000-4-2 (With
External Capacitance)

- UL Listed – File No. E169910 and NEMKO
IEC60950-1-am1 ed2.0

- [See the TI Switch Portfolio](http://www.ti.com/usbpower)


**2** **Applications**


- USB Ports and Hubs

- Digital TVs

- Set-Top Boxes

- VOIP Phones



**3** **Description**
The TPS255x and TPS255x-1 power-distribution
switches are intended for applications where
precision current limiting is required or heavy
capacitive loads and short circuits are encountered
and provide up to 1.5 A of continuous load current.
These devices offer a programmable current-limit
threshold between 75 mA and 1.7 A (typical) through
an external resistor. Current-limit accuracy as tight as
±6% can be achieved at the higher current-limit
settings. The power-switch rise and fall times are
controlled to minimize current surges during turnon
and turnoff.


TPS255x devices limit the output current to a safe
level by using a constant-current mode when the
output load exceeds the current-limit threshold.
TPS255x-1 devices provide circuit breaker
functionality by latching off the power switch during
overcurrent or reverse-voltage situations. An internal
reverse-voltage comparator disables the powerswitch when the output voltage is driven higher than
the input to protect devices on the input side of the
switch. The FAULT output asserts low during
overcurrent and reverse-voltage conditions.


**Device Information** **[(1)]**






|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|TPS2552|SOT-23 (6)|2.90 mm x 1.60 mm|
|TPS2552|WSON (6)|2.00 mm x 2.00 mm|
|TPS2553|SOT-23 (6)|2.90 mm x 1.60 mm|
|TPS2553|WSON (6)|2.00 mm x 2.00 mm|



(1) For all available packages, see the orderable addendum at

the end of the data sheet.


**Typical Application**









**Fault Signal**


**Control Signal**


1



















Copyright © 2016, Texas Instruments Incorporated



An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**Table of Contents**



**1** **Features** .................................................................. 1
**2** **Applications** ........................................................... 1
**3** **Description** ............................................................. 1
**4** **Revision History** ..................................................... 2
**5** **Device Comparison Table** ..................................... 4
**6** **Pin Configuration and Functions** ......................... 5
**7** **Specifications** ......................................................... 5

7.1 Absolute Maximum Ratings ...................................... 5
7.2 ESD Ratings ............................................................ 6
7.3 Recommended Operating Conditions....................... 6
7.4 Thermal Information.................................................. 6
7.5 Electrical Characteristics........................................... 7
7.6 Typical Characteristics.............................................. 8
**8** **Parameter Measurement Information** ................ 11
**9** **Detailed Description** ............................................ 13

9.1 Overview ................................................................. 13
9.2 Functional Block Diagram ....................................... 13
9.3 Feature Description................................................. 13
9.4 Device Functional Modes........................................ 15
9.5 Programming........................................................... 15



**10** **Application and Implementation** ........................ 17
10.1 Application Information.......................................... 17
10.2 Typical Applications .............................................. 17
**11** **Power Supply Recommendations** ..................... 24
11.1 Self-Powered and Bus-Powered Hubs ................. 24
11.2 Low-Power Bus-Powered and High-Power BusPowered Functions .................................................. 24
11.3 Power Dissipation and Junction Temperature ...... 24
**12** **Layout** ................................................................... 25
12.1 Layout Guidelines ................................................. 25
12.2 Layout Example .................................................... 25
**13** **Device and Documentation Support** ................. 26
13.1 Device Support...................................................... 26
13.2 Related Links ........................................................ 26
13.3 Receiving Notification of Documentation Updates 26
13.4 Community Resources.......................................... 26
13.5 Trademarks........................................................... 26
13.6 Electrostatic Discharge Caution............................ 26
13.7 Glossary................................................................ 26
**14** **Mechanical, Packaging, and Orderable**
**Information** ........................................................... 26



**4** **Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision E (February 2012) to Revision F** **Page**


- Added _ESD Rating_ table, _Feature Description_ section, _Device Functional Modes_, _Application and Implementation_
section, _Power Supply Recommendations_ section, _Layout_ section, _Device and Documentation Support_ section, and
_Mechanical, Packaging, and Orderable Information_ section ................................................................................................. 1


- Changed 1300 mA to 1700 mA in the adjustable current limit bullet under the _Features_ section ......................................... 1


- Changed from 1.2 A to 1.5 A.................................................................................................................................................. 4


**Changes from Revision D (June 2011) to Revision E** **Page**


- Changed VEN to VEN in Recommended Operating Conditions ............................................................................................... 6

- Changed ~~V~~ EN to VEN in Recommended Operating Conditions ............................................................................................... 6


**Changes from Revision C (September 2009) to Revision D** **Page**


- Changed From: Fast Overcurrent Response - 2-µS (typ) To: Fast Overcurrent Response - 2-µs (typ) in the Features ...... 1


- Added text To Feature - UL Listed "and NEMKO IEC60950-1-am1 ed2.0"........................................................................... 1


- Added Features Item "See the TI Switch Portfoilo"................................................................................................................ 1


- Changed the DEVICE INFORMATION table, and Deleted Note 3 ........................................................................................ 1


- Added ESD-system level (contact/air) to the ABS MAX table, and Added Note 3 ................................................................ 6


- Added text to the REVERSE-VOLTAGE PROTECTION section: "A reverse.....when this occurs.".................................... 14



2



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**Changes from Revision B (February 2009) to Revision C** **Page**


- Added Feature - Up to 1.5 A Maximum Load Current............................................................................................................ 1


- Changed 1.3 A (typ) To: 1.7 A (typ) ....................................................................................................................................... 1


- Added Text - and provide up to 1.5 A of continuous load current.......................................................................................... 1


- Changed From: 19.1 k Ω ≤ RILIM ≤ 232 k Ω To: 15 k Ω ≤ RILIM ≤ 232 k Ω . ................................................................................. 5

- Changed IOUT values for 1.2A and 1.5A ................................................................................................................................. 6

- Changed TJ values for 1.2A and 1.5A.................................................................................................................................... 6

- Added RILIM = 15 k Ω option .................................................................................................................................................... 7

- Changed Text From: current-limit threshold between 75 mA and 1.3 A (typ) To: current-limit threshold between 75
mA and 1.7 A (typ)................................................................................................................................................................ 13


- Changed Text From: The recommended 1% resistor range for RILIM is 19.1 k Ω ≤ RILIM ≤ 232 k Ω to ensure stability
To: The recommended 1% resistor range for RILIM is 15 k Ω ≤ RILIM ≤ 232 k Ω to ensure stability........................................ 15

- Changed From: where 19.1 k Ω ≤ RILIM ≤ 232 k Ω . To: where 15 k Ω ≤ RILIM ≤ 232 k Ω . ........................................................ 15

- Changed Figure 23 - Current-Limit Threshold vs RILIM ........................................................................................................ 16

- Changed Table 2 - added rows for Current Limit of 1400 to 1700....................................................................................... 19


**Changes from Revision A (December 2008) to Revision B** **Page**


- Added To Features - UL Listed – File No. E169910 .............................................................................................................. 1


- Changed Figure 17 Ttitle From: Current Limit Threshold Vs RILM ......................................................................................... 9

- Changed Figure 18 Ttitle From: Current Limit Threshold Vs RILM ......................................................................................... 9


**Changes from Original (November 2008) to Revision A** **Page**


- Changed Title from: Adjustable Current-Limited Power-Distribution Switches to: Precision Adjustable CurrentLimited Power-Distribution Switches ...................................................................................................................................... 1



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



3


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**5** **Device Comparison Table**



4



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**6** **Pin Configuration and Functions**



**TPS255x DBV Package**

**6-Pin SOT-23**

**Top View**



**TPS255x DRV Package**

**6-Pin WSON**

**Top View**














|Col1|Col2|1 6<br>2 5<br>3 4|OUT<br>ILIM|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||


|OUT<br>ILIM|1 6<br>2 PAD 5<br>3 4|
|---|---|
|**FAULT**|**FAULT**|



EN = Active Low for the TPS2552


EN = Active High for the TPS2553


Add –1 to part number for latch-off version



EN = Active Low for the TPS2552


EN = Active High for the TPS2553


Add –1 to part number for latch-off version



**Pin Functions**























|PIN|Col2|Col3|Col4|Col5|I/O|DESCRIPTION|
|---|---|---|---|---|---|---|
|**NAME**|**TPS2552**|**TPS2552**|**TPS2553**|**TPS2553**|**TPS2553**|**TPS2553**|
|**NAME**|**SOT-23**|**WSON**|**SOT-23**|**WSON**|**WSON**|**WSON**|
|EN|3|4|—|—|I|Enable input, logic low turns on power switch|
|EN|—|—|3|4|I|Enable input, logic high turns on power switch|
|FAULT|4|3|4|3|O|Active-low open-drain output, asserted during<br>overcurrent, overtemperature, or reverse-voltage<br>conditions.|
|GND|2|5|2|5|—|Ground connection; connect externally to PowerPAD|
|ILIM|5|2|5|2|O|External resistor used to set current-limit threshold;<br>recommended 15 kΩ ≤RILIM ≤232 kΩ.|
|IN|1|6|1|6|I|Input voltage; connect a 0.1 µF or greater ceramic<br>capacitor from IN to GND as close to the IC as<br>possible.|
|OUT|6|1|6|1|O|Power-switch output|
|PowerPAD™|—|PAD|—|PAD|—|Internally connected to GND; used to heat-sink the part<br>to the circuit board traces. Connect PowerPAD to GND<br>pin externally.|


Add –1 for Latch-Off version


**7** **Specifications**


**7.1** **Absolute Maximum Ratings**

over operating free-air temperature range (unless otherwise noted) [(1)(2)]





|Col1|MIN MAX|UNIT|
|---|---|---|
|Voltage range on IN, OUT, EN or EN, ILIM, FAULT|–0.3<br>7|V|
|Voltage range from IN to OUT|–7<br>7|V|
|IO<br>Continuous output current|Internally Limited||
|Continuous total power dissipation|See the_ Thermal Information_||
|Continuous FAULT sink current|0<br>25|mA|
|ILIM source current|0<br>1|mA|
|TJ<br>Maximum junction temperature|–40<br>150|°C|
|Tstg<br>Storage temperature|–65<br>150|°C|


(1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under _Recommended_
_Operating Conditions_ . Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) Voltages are referenced to GND unless otherwise noted.



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



5


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**7.2** **ESD Ratings**






|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic discharge|Human body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)<br>Electrostatic discharge|Charged device model (CDM), per JEDEC specification JESD22-<br>C101(2)|±500|±500|
|V(ESD)<br>Electrostatic discharge|IEC 61000-4-2 contact discharge(3)|±8000|±8000|
|V(ESD)<br>Electrostatic discharge|IEC 61000-4-2 air-gap discharge(3)|±15000|±15000|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
(3) Surges per EN61000-4-2. 1999 applied to output terminals of EVM. These are passing test levels, not failure threshold.


**7.3** **Recommended Operating Conditions**


over operating free-air temperature range (unless otherwise noted)












|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VIN<br>Input voltage, IN|VIN<br>Input voltage, IN|2.5<br>6.5|V|
|~~V~~EN<br>Enable voltage|TPS2552/52-1|0<br>6.5|V|
|VEN<br>Enable voltage|TPS2553/53-1|0<br>6.5|V|
|VIH<br>High-level input voltage on EN or EN|VIH<br>High-level input voltage on EN or EN|1.1|V|
|VIL<br>Low-level input voltage on EN or EN|VIL<br>Low-level input voltage on EN or EN|0.66|0.66|
|IOUT<br>Continuous output current,<br>OUT|–40 °C ≤TJ ≤125 °C|0<br>1.2|A|
|IOUT<br>Continuous output current,<br>OUT|–40 °C ≤TJ ≤105 °C|0<br>1.5|0<br>1.5|
|RILIM<br>Current-limit threshold resistor range (nominal 1%) from ILIM to GND|RILIM<br>Current-limit threshold resistor range (nominal 1%) from ILIM to GND|15<br>232|kΩ|
|IO<br>Continuous FAULT sink current|IO<br>Continuous FAULT sink current|0<br>10|mA|
|Input de-coupling capacitance, IN to GND|Input de-coupling capacitance, IN to GND|0.1|µF|
|TJ<br>Operating virtual junction<br>temperature(1)|IOUT ≤1.2 A|–40<br>125|°C|
|TJ<br>Operating virtual junction<br>temperature(1)|IOUT ≤1.5 A|–40<br>105|–40<br>105|



(1) See _Power Dissipation and Junction Temperature_ for details on how to calculate maximum junction temperature for specific applications
and packages.


**7.4** **Thermal Information**







|THERMAL METRIC(1)|TPS2552|Col3|TPS2553|Col5|UNIT|
|---|---|---|---|---|---|
|**THERMAL METRIC(1)**|**DBV (SOT-23)**|**DRV (WSON)**|**DBV (SOT-23)**|**DRV (WSON)**|**DRV (WSON)**|
|**THERMAL METRIC(1)**|**6 PINS**|**6 PINS**|**6 PINS**|**6 PINS**|**6 PINS**|
|RθJA<br>Junction-to-ambient thermal resistance|182.6|72|182.6|72|°C/W|
|RθJC(to<br>p)<br>Junction-to-case (top) thermal resistance|122.2|85.3|122.2|85.3|°C/W|
|RθJB<br>Junction-to-board thermal resistance|29.4|41.3|29.4|41.3|°C/W|
|ψJT<br>Junction-to-top characterization parameter|20.8|1.7|20.8|1.7|°C/W|
|ψJB<br>Junction-to-board characterization parameter|28.9|41.7|28.9|41.7|°C/W|
|RθJC(b<br>ot)<br>Junction-to-case (bottom) thermal resistance|—|11.1|—|11.1|°C/W|


(1) For more information about traditional and new thermal metrics, see the _[Semiconductor and IC Package Thermal Metrics](http://www.ti.com/lit/pdf/spra953)_ application
report.



6



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**7.5** **Electrical Characteristics**





































|PARAMETER|TEST CONDITIONS(1)|Col3|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**POWER SWITCH**|**POWER SWITCH**|**POWER SWITCH**|**POWER SWITCH**|**POWER SWITCH**|
|rDS(on)<br>Static drain-source on-state resistance|DBV package, TJ = 25°C|DBV package, TJ = 25°C|85<br>95|mΩ|
|rDS(on)<br>Static drain-source on-state resistance|DBV package, –40°C ≤TJ ≤125°C|DBV package, –40°C ≤TJ ≤125°C|135|135|
|rDS(on)<br>Static drain-source on-state resistance|DRV package, TJ = 25°C|DRV package, TJ = 25°C|100<br>115|100<br>115|
|rDS(on)<br>Static drain-source on-state resistance|DRV package, –40°C ≤TJ ≤105°C|DRV package, –40°C ≤TJ ≤105°C|140|140|
|rDS(on)<br>Static drain-source on-state resistance|DRV package, –40°C ≤TJ ≤125°C|DRV package, –40°C ≤TJ ≤125°C|150|150|
|tr<br>Rise time, output|CL = 1 µF, RL = 100 Ω,<br>(see Figure 20)|VIN = 6.5 V|1.1<br>1.5|ms|
|tr<br>Rise time, output|CL = 1 µF, RL = 100 Ω,<br>(see Figure 20)|VIN = 2.5 V|0.7<br>1|0.7<br>1|
|tf<br>Fall time, output|CL = 1 µF, RL = 100 Ω,<br>(see Figure 20)|VIN = 6.5 V|0.2<br>0.5|0.2<br>0.5|
|tf<br>Fall time, output|CL = 1 µF, RL = 100 Ω,<br>(see Figure 20)|VIN = 2.5 V|0.2<br>0.5|0.2<br>0.5|
|**ENABLE INPUT EN OR EN**|**ENABLE INPUT EN OR EN**|**ENABLE INPUT EN OR EN**|**ENABLE INPUT EN OR EN**|**ENABLE INPUT EN OR EN**|
|Enable pin turn on/off threshold|||0.66<br>1.1|V|
|IEN<br>Input current|VEN = 0 V or 6.5 V,~~V~~EN = 0 V or 6.5 V|VEN = 0 V or 6.5 V,~~V~~EN = 0 V or 6.5 V|–0.5<br>0.5|µA|
|ton<br>Turnon time|CL = 1 µF, RL = 100 Ω, (see Figure 20)|CL = 1 µF, RL = 100 Ω, (see Figure 20)|3|ms|
|toff<br>Turnoff time|CL = 1 µF, RL = 100 Ω, (see Figure 20)|CL = 1 µF, RL = 100 Ω, (see Figure 20)|3|ms|
|**CURRENT LIMIT**|**CURRENT LIMIT**|**CURRENT LIMIT**|**CURRENT LIMIT**|**CURRENT LIMIT**|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|RILIM = 15 kΩ, –40°C ≤TJ ≤105°C|RILIM = 15 kΩ, –40°C ≤TJ ≤105°C|1610<br>1700<br>1800|mA|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|RILIM = 20 kΩ|TJ = 25°C|1215<br>1295<br>1375|1215<br>1295<br>1375|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|RILIM = 20 kΩ|–40°C ≤TJ ≤125°C|1200<br>1295<br>1375|1200<br>1295<br>1375|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|RILIM = 49.9 kΩ|TJ = 25°C|490<br>520<br>550|490<br>520<br>550|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|RILIM = 49.9 kΩ|–40°C ≤TJ ≤125°C|475<br>520<br>565|475<br>520<br>565|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|RILIM = 210 kΩ|RILIM = 210 kΩ|110<br>130<br>150|110<br>130<br>150|
|IOS<br>Current-limit threshold (Maximum DC<br>output current IOUT delivered to load)<br>and Short-circuit current, OUT<br>connected to GND|ILIM shorted to IN|ILIM shorted to IN|50<br>75<br>100|50<br>75<br>100|
|tIOS<br>Response time to short circuit|VIN = 5 V (see Figure 21)|VIN = 5 V (see Figure 21)|2|µs|
|**REVERSE-VOLTAGE PROTECTION**|**REVERSE-VOLTAGE PROTECTION**|**REVERSE-VOLTAGE PROTECTION**|**REVERSE-VOLTAGE PROTECTION**|**REVERSE-VOLTAGE PROTECTION**|
|Reverse-voltage comparator trip point<br>(VOUT – VIN)|||95<br>135<br>190|mV|
|Time from reverse-voltage condition<br>to MOSFET turn off|VIN = 5 V|VIN = 5 V|3<br>5<br>7|ms|
|**SUPPLY CURRENT**|**SUPPLY CURRENT**|**SUPPLY CURRENT**|**SUPPLY CURRENT**|**SUPPLY CURRENT**|
|IIN_off<br>Supply current, low-level output|VIN = 6.5 V, No load on OUT,~~V~~EN = 6.5 V or VEN = 0 V|VIN = 6.5 V, No load on OUT,~~V~~EN = 6.5 V or VEN = 0 V|0.1<br>1|µA|
|IIN_on<br>Supply current, high-level output|VIN = 6.5 V, No load on OUT|RILIM = 20 kΩ|120<br>140|µA|
|IIN_on<br>Supply current, high-level output|VIN = 6.5 V, No load on OUT|RILIM = 210 kΩ|100<br>120|µA|
|IREV<br>Reverse leakage current|VOUT = 6.5 V, VIN = 0 V|TJ = 25 °C|0.01<br>1|µA|
|**UNDERVOLTAGE LOCKOUT**|**UNDERVOLTAGE LOCKOUT**|**UNDERVOLTAGE LOCKOUT**|**UNDERVOLTAGE LOCKOUT**|**UNDERVOLTAGE LOCKOUT**|
|UVLO<br>Low-level input voltage, IN|VIN rising|VIN rising|2.35<br>2.45|V|
|Hysteresis, IN|TJ = 25 °C|TJ = 25 °C|25|mV|
|**FAULT FLAG**|**FAULT FLAG**|**FAULT FLAG**|**FAULT FLAG**|**FAULT FLAG**|
|VOL<br>Output low voltage, FAULT|I/FAULT = 1 mA|I/FAULT = 1 mA|180|mV|
|Off-state leakage|V/FAULT = 6.5 V|V/FAULT = 6.5 V|1|µA|
|FAULT deglitch|FAULT assertion or de-assertion due to overcurrent condition|FAULT assertion or de-assertion due to overcurrent condition|5<br>7.5<br>10|ms|
|FAULT deglitch|FAULT assertion or de-assertion due to reverse-voltage condition|FAULT assertion or de-assertion due to reverse-voltage condition|2<br>4<br>6|ms|
|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|
|Thermal shutdown threshold|||155|°C|
|Thermal shutdown threshold in<br>current-limit|||135|°C|
|Hysteresis|||10|°C|


(1) Pulse-testing techniques maintain junction temperature close to ambient temperature; thermal effects must be taken into account
separately.


Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



7


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**7.6** **Typical Characteristics**


|Figure 1. Turnon Delay and Rise Time|Figure 2. Turnoff Delay and Fall Time|
|---|---|
|**Figure 3. Device Enabled into Short-Circuit**|**Figure 4. Full-Load to Short-Circuit Transient Response**|
|**Figure 5. Short-Circuit to Full-Load Recovery Response**|**Figure 6. No-Load to Short-Circuit Transient Response**|



8



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016






|R = 20 kW|Col2|Col3|Col4|
|---|---|---|---|
|<br>~~**ILIM**~~||||
|||||
||**VLO Rising**|||
|||||
|||||
||**UVLO Falling**|||
|||||
|||||
|||||



|Typical Characteristics (continued)|Col2|
|---|---|
|**Figure 7. Short-Circuit to No-Load Recovery Response**|**Figure 8. No Load to 1-Ω Transient Response**|
|**Figure 9. 1-Ω to No Load Transient Response**|**Figure 10. Reverse-Voltage Protection Response**|
|**Figure 11. Reverse-Voltage Protection Recovery**|**2.30**<br>**T - Junction Temperature - °C**<br>**J**<br>**-50**<br>**0**<br>**50**<br>**100**<br>**150**<br>**UVLO - Undervoltage Lockout - V**<br>**2.40**<br>**2.31**<br>**2.32**<br>**2.33**<br>**2.34**<br>**2.35**<br>**2.36**<br>**2.37**<br>**2.38**<br>**2.39**<br>**UVLO Rising**<br>**R**<br>**= 20 k**<br>~~**ILIM**~~<br>W<br>**UVLO Falling**<br>**Figure 12. UVLO – Undervoltage Lockout – V**|


Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



9


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**














|M= 20 kW|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||~~**V**~~<br>~~**= 6.5 V**~~<br>||
|||<br>~~**IN**~~||
|||||
|||||
||||**V**<br>**= 2.5 V**<br>**IN**|
|||||


|RILIM= 20 kW|V = 6.5 V|Col3|Col4|
|---|---|---|---|
|<br><br>|<br>~~**IN**~~|<br>~~**V**~~<br>~~**= 5 V**~~<br>**IN**||
|||||
|||||
|||<br>||
||**V**<br>**I**|~~**V**~~<br>~~**= 3**~~<br>~~**IN**~~<br>**= 2.5 V**<br>**N**|~~** 3 V**~~|
|||||
|||||
|||||
|||||


























|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
||~~**DRV Package**~~|||
|||**DBV Packa**|** ge**|
|||||
|||||
|||||


|VIN= 5 V,|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**R**<br>**= 20 k,**<br>**T**<br>**= 25°C**<br><br>**ILIM**<br>~~**A**~~<br>W|||||
|<br>|||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||


























|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||~~**T**~~<br>~~**=**~~<br>|~~** 40°**~~|||||
||<br>~~**A**~~||||||
||**T**<br>**=**<br>**A**|** 25°C**|||||
||||||||
||~~**T**~~<br>~~**= 1**~~<br>~~**A**~~|~~** 5°C**~~|||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||||~~**V**~~<br>~~**= 6.5 V,**~~<br>**R**<br>**= 20 k**<br>~~**IN**~~<br><br>W|
|||||||<br>~~**ILIM**~~|






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|~~**T**~~<br>|~~**= -40°C**~~<br>||**T**<br>**=**<br>~~**A**~~|** 25°C**||||||
||<br>|||||**T**<br>**= 1**<br>**A**|** 25°C**|||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||||||||~~**V**~~<br><br>|~~**= 6.5 V,**~~||
||||||||**R**<br>~~**IN**~~<br>~~**ILI**~~|<br>**= 200**<br>|**  k**<br>W|
|||||||||||










|Typical Characteristics (continued)|Col2|
|---|---|
|**0**<br>**I**<br>**- Supply Current, Output Disabled -**<br>**A**<br>**IN**<br>m<br>**0.40**<br>**0.04**<br>**0.08**<br>**0.12**<br>**0.16**<br>**0.20**<br>**0.24**<br>**0.28**<br>**0.32**<br>**0.36**<br>**T - Junction Temperature - °C**<br>**J**<br>**-50**<br>**0**<br>**50**<br>**100**<br>**150**<br>**V**<br>**= 2.5 V**<br>**IN**<br>~~**V**~~<br>~~**= 6.5 V**~~<br>~~**IN**~~<br>**R**<br>**= 20 k**<br>**ILIM**<br>W<br>**Figure 13. IIN – Supply Current, Output Disabled – µA**|**0**<br>**I**<br>**- Supply Current, Output Enabled -**<br>**A**<br>**IN**<br>m<br>**150**<br>**15**<br>**30**<br>**45**<br>**60**<br>**75**<br>**90**<br>**105**<br>**120**<br>**135**<br>**T - Junction Temperature - °C**<br>**J**<br>**-50**<br>**0**<br>**50**<br>**100**<br>**150**<br>**R**<br>**= 20 k**<br>~~**ILIM**~~<br>W<br>~~**V**~~<br>~~**= 6.5 V**~~<br>~~**IN**~~<br>~~**V**~~<br>~~**= 5 V**~~<br>**IN**<br>~~**V**~~<br>~~**= 3.3 V**~~<br>~~**IN**~~<br>**V**<br>**= 2.5 V**<br>**IN**<br>**Figure 14. IIN – Supply Current, Output Enabled – µA**|
|**0**<br>**Peak Current - A**<br>**0**<br>**1.5**<br>**3**<br>**4.5**<br>**6**<br>**Current Limit Response -**<br>**s**<br>m<br>**20**<br>**2**<br>**4**<br>**6**<br>**8**<br>**10**<br>**12**<br>**14**<br>**16**<br>**18**<br>**V**<br>**= 5 V,**<br>**R**<br>**= 20 k,**<br>**T**<br>**= 25°C**<br>**IN**<br>**ILIM**<br>~~**A**~~<br>W<br>**Figure 15. Current Limit Response – µs**|**0**<br>**DBV Package**<br>**r**<br>**- Static Drain-Source On-State Resistance - m**<br>**DS(on)**<br>W<br>**25**<br>**50**<br>**75**<br>**100**<br>**125**<br>**150**<br>~~**DRV Package**~~<br>**T - Junction Temperature - °C**<br>**J**<br>**-50**<br>**0**<br>**50**<br>**100**<br>**150**<br>**Figure 16. MOSFET rDS(on) Vs. Junction Temperature**|
|**0**<br>**100**<br>**200**<br>**300**<br>**400**<br>**500**<br>**600**<br>**700**<br>**800**<br>**900**<br>**1000**<br>**1100**<br>**1200**<br>**1300**<br>**1400**<br>**0**<br>**100**<br>**200**<br>**300**<br>**400**<br>**500**<br>**600**<br>**700**<br>**800**<br>**900**<br>**1000**<br>**IDS - Static Drain-Source Current - mA**<br>**V**<br>**- V**<br>**- 100 mV/div**<br>**IN**<br>**OUT**<br>~~**T**~~<br>~~**= 125°C**~~<br>~~**A**~~<br>**T**<br>**= 25°C**<br>**A**<br>~~**T**~~<br>~~**= -40°C**~~<br>~~**A**~~<br>~~**V**~~<br>~~**= 6.5 V,**~~<br>**R**<br>**= 20 k**<br>~~**IN**~~<br>~~**ILIM**~~<br>W<br>**Figure 17. Switch Current Vs. Drain-Source Voltage Across**<br>**Switch**|**0**<br>**10**<br>**20**<br>**30**<br>**40**<br>**50**<br>**60**<br>**70**<br>**80**<br>**90**<br>**100**<br>**110**<br>**120**<br>**130**<br>**140**<br>**150**<br>**0**<br>**100**<br>**200**<br>**300**<br>**400**<br>**500**<br>**600**<br>**700**<br>**800**<br>**900**<br>**1000**<br>**IDS - Static Drain-Source Current - mA**<br>**V**<br>**- V**<br>**- 100 mV/div**<br>**IN**<br>**OUT**<br>**T**<br>**= 25°C**<br>~~**A**~~<br>**T**<br>**= 125°C**<br>**A**<br>~~**V**~~<br>~~**= 6.5 V,**~~<br>**R**<br>**= 200 k**<br>~~**IN**~~<br>~~**ILIM**~~<br>W<br>~~**T**~~<br>~~**= -40°C**~~<br>~~**A**~~<br>**Figure 18. Switch Current Vs. Drain-Source Voltage Across**<br>**Switch**|



10



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**8** **Parameter Measurement Information**



**TPS2552**









**Fault Signal**


**Control�Signal**











**Figure 19. Typical Characteristics Reference Schematic**


**OUT**



**TEST�CIRCUIT**































**VOLTAGE�WAVEFORMS**


**Figure 20. Test Circuit and Voltage Waveforms**


Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



11


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**Parameter Measurement Information (continued)**


**Decreasing**
**Load�Resistance**


**IOUT**

|UT|Decr<br>Load|
|---|---|
|||



**IOS**


**Figure 22. Output Voltage vs Current-Limit Threshold**



12



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**9** **Detailed Description**


**9.1** **Overview**


The TPS255x and TPS255x-1 are current-limited, power-distribution switches using N-channel MOSFETs for
applications where short circuits or heavy capacitive loads are encountered and provide up to 1.5 A of
continuous load current. These devices allow the user to program the current-limit threshold between 75 mA and
1.7 A (typical) through an external resistor. Additional device shutdown features include overtemperature
protection and reverse-voltage protection. The device incorporates an internal charge pump and gate drive
circuitry necessary to drive the N-channel MOSFET. The charge pump supplies power to the driver circuit and
provides the necessary voltage to pull the gate of the MOSFET above the source. The charge pump operates
from input voltages as low as 2.5 V and requires little supply current. The driver controls the gate voltage of the
power switch. The driver incorporates circuitry that controls the rise and fall times of the output voltage to limit
large current and voltage surges and provides built-in soft-start functionality. There are two device families that
handle overcurrent situations differently. The TPS255x family enters constant-current mode while the TPS255x-1
family latches off when the load exceeds the current-limit threshold.


**9.2** **Functional Block Diagram**



























Copyright © 2016, Texas Instruments Incorporated


A. TPS255x parts enter constant current mode during current limit condition; TPS255x-1 parts latch off


**9.3** **Feature Description**


**9.3.1** **Overcurrent Conditions**


The TPS255x and TPS255x-1 respond to overcurrent conditions by limiting their output current to the IOS levels
shown in Figure 23. When an overcurrent condition is detected, the device maintains a constant output current
and reduces the output voltage accordingly. Two possible overload conditions can occur.


The first condition is when a short circuit or partial short circuit is present when the device is powered-up or
enabled. The output voltage is held near zero potential with respect to ground and the TPS255x ramps the
output current to IOS. The TPS255x devices limits the current to IOS until the overload condition is removed or the
device begins to thermal cycle. The TPS255x-1 devices will limit the current to IOS until the overload condition is
removed or the internal deglitch time (7.5-ms typical) is reached and the device is turned off. The device remains
off until power is cycled or the device enable is toggled.



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



13


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**Feature Description (continued)**


The second condition is when a short circuit, partial short circuit, or transient overload occurs while the device is
enabled and powered on. The device responds to the overcurrent condition within time tIOS (see Figure 21). The
current-sense amplifier is overdriven during this time and momentarily disables the internal current-limit
MOSFET. The current-sense amplifier recovers and limits the output current to IOS. Similar to the previous case,
the TPS255x limits the current to IOS until the overload condition is removed or the device begins to thermal
cycle; the TPS255x-1 limits the current to IOS until the overload condition is removed or the internal deglitch time
is reached and the device is latched off.


The TPS255x thermal cycles if an overload condition is present long enough to activate thermal limiting in any of
the above cases. The device turns off when the junction temperature exceeds 135°C (typical) while in current
limit. The device remains off until the junction temperature cools 10°C (typical) and then restarts. The TPS255x
cycles on and off until the overload is removed (see Figure 5 and Figure 7) .


**9.3.2** **Reverse-Voltage Protection**


The reverse-voltage protection feature turns off the N-channel MOSFET whenever the output voltage exceeds
the input voltage by 135 mV (typical) for 4-ms (typical). A reverse current of (VOUT – VIN)/rDS(on)) are present when
this occurs. This prevents damage to devices on the input side of the TPS255x and TPS2552-1/TPS2253-1 by
preventing significant current from sinking into the input capacitance. The TPS255x devices allow the N-channel
MOSFET to turn on once the output voltage goes below the input voltage for the same 4-ms deglitch time. The
TPS255x-1 devices keep the device turned off even if the reverse-voltage condition is removed and do not allow
the N-channel MOSFET to turn on until power is cycled or the device enable is toggled. The reverse-voltage
comparator also asserts the FAULT output (active-low) after 4-ms.


**9.3.3** **FAULT Response**


The FAULT open-drain output is asserted (active low) during an overcurrent, overtemperature, or reverse-voltage
condition. The TPS255x asserts the FAULT signal until the fault condition is removed and the device resumes
normal operation. The TPS255x-1 asserts the FAULT signal during a fault condition and remains asserted while
the part is latched-off. The FAULT signal is de-asserted once device power is cycled or the enable is toggled and
the device resumes normal operation. The TPS255x and TPS255x-1 are designed to eliminate false FAULT
reporting by using an internal delay _de-glitch_ circuit for overcurrent (7.5-ms typical) and reverse-voltage (4-ms
typical) conditions without the need for external circuitry. This ensures that FAULT is not accidentally asserted
due to normal operation such as starting into a heavy capacitive load. The deglitch circuitry delays entering and
leaving fault conditions. Overtemperature conditions are not deglitched and assert the FAULT signal immediately.


**9.3.4** **Undervoltage Lockout (UVLO)**


The undervoltage lockout (UVLO) circuit disables the power switch until the input voltage reaches the UVLO
turnon threshold. Built-in hysteresis prevents unwanted on and off cycling due to input voltage drop from large
current surges.


**9.3.5** **ENABLE (EN or EN)**


The logic enable controls the power switch, bias for the charge pump, driver, and other circuits to reduce the
supply current. The supply current is reduced to less than 1-µA when a logic low is present on EN. A logic low
input on EN or a logic high input on EN enables the driver, control circuits, and power switch. The enable input is
compatible with both TTL and CMOS logic levels.


**9.3.6** **Thermal Sense**


The TPS255x and TPS255x-1 have self-protection features using two independent thermal-sensing circuits that
monitor the operating temperature of the power switch and disable operation if the temperature exceeds
recommended operating conditions. The TPS255x device operates in constant-current mode during an
overcurrent conditions, which increases the voltage drop across power-switch. The power dissipation in the
package is proportional to the voltage drop across the power switch, which increases the junction temperature
during an overcurrent condition. The first thermal sensor turns off the power switch when the die temperature
exceeds 135°C (minimum) and the part is in current limit. Hysteresis is built into the thermal sensor, and the
switch turns on after the device has cooled approximately 10°C.



14



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**Feature Description (continued)**


The TPS255x and TPS255x-1 also have a second ambient thermal sensor. The ambient thermal sensor turns off
the power-switch when the die temperature exceeds 155°C (minimum) regardless of whether the power switch is
in current limit and turns on the power switch after the device has cooled approximately 10°C. The TPS255x and
TPS255x-1 families continue to cycle off and on until the fault is removed.


The open-drain fault reporting output FAULT is asserted (active low) immediately during an overtemperature
shutdown condition.


**9.4** **Device Functional Modes**


There are no other functional modes.


**9.5** **Programming**


**9.5.1** **Programming the Current-Limit Threshold**


The overcurrent threshold is user programmable through an external resistor. The TPS255x and TPS255x-1 use
an internal regulation loop to provide a regulated voltage on the ILIM pin. The current-limit threshold is
proportional to the current sourced out of ILIM. The recommended 1% resistor range for RILIM is 15 k Ω ≤ RILIM ≤
232 k Ω to ensure stability of the internal regulation loop. Many applications require that the minimum current limit
is above a certain current level or that the maximum current limit is below a certain current level, so it is
important to consider the tolerance of the overcurrent threshold when selecting a value for RILIM. The following
equations and Figure 23 can be used to calculate the resulting overcurrent threshold for a given external resistor
value (RILIM). Figure 23 includes current-limit tolerance due to variations caused by temperature and process.
However, the equations do not account for tolerance due to external resistor variation, so it is important to
account for this tolerance when selecting RILIM. The traces routing the RILIM resistor to the TPS255x and
TPS255x-1 must be as short as possible to reduce parasitic effects on the current-limit accuracy.


RILIM can be selected to provide a current-limit threshold that occurs 1) above a minimum load current or 2)
below a maximum load current.


To design above a minimum current-limit threshold, find the intersection of RILIM and the maximum desired load
current on the IOS(min) curve and choose a value of RILIM below this value. Programming the current limit above a
minimum threshold is important to ensure start-up into full load or heavy capacitive loads. The resulting
maximum current-limit threshold is the intersection of the selected value of RILIM and the IOS(max) curve.

To design below a maximum current-limit threshold, find the intersection of RILIM and the maximum desired load
current on the IOS(max) curve and choose a value of RILIM above this value. Programming the current limit below a
maximum threshold is important to avoid current limiting upstream power supplies, causing the input voltage bus
to droop. The resulting minimum current-limit threshold is the intersection of the selected value of RILIM and the
IOS(min) curve.


Current-Limit Threshold Equations (IOS):



IOSmax (mA) = 22980V0.94

R k



I (mA) =



0.94
ILIM







IOSnom(mA) = 23950V0.977

R k



I (mA) =



0.977
ILIM




 


IOSmin(mA) = 25230V1.016

R k



I (mA) =



1.016
ILIM







where


15 k Ω ≤ RILIM ≤ 232 k Ω . (1)


While the maximum recommended value of RILIM is 232 k Ω, there is one additional configuration that allows for
a lower current-limit threshold. The ILIM pin may be connected directly to IN to provide a 75 mA (typical) currentlimit threshold. Additional low-ESR ceramic capacitance may be necessary from IN to GND in this configuration
to prevent unwanted noise from coupling into the sensitive ILIM circuitry.



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



15


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**Programming (continued)**


**1800**


**1700**


**1600**


**1500**



**1400**


**1300**


**1200**


**1100**

**1000**


**900**


**800**


**700**


**600**


**500**


**400**

**300**


**200**


**100**


**0**



|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|**IOS(max)**||||
|||||
|||||
||~~**I**~~|||
||~~**OS(nom)**~~|||
|~~**IOS(min)**~~||||
|||||


**15 25** **35** **45** **55** **65** **75** **85** **95** **105 115 125** **135 145 155** **165 175 185** **195 205** **215 225** **235**


**RILIM** **-�Current�Limit�Resistor�-�k**              

**Figure 23. Current-Limit Threshold vs RILIM**



16



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**10** **Application and Implementation**


**NOTE**
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TI’s customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.


**10.1** **Application Information**


**10.1.1** **Constant-Current vs Latch-Off Operation and Impact on Output Voltage**


Both the constant-current devices (TPS255x) and latch-off devices (TPS255x-1) operate identically during normal
operation, that is, the load current is less than the current-limit threshold and the devices are not limiting current.
During normal operation the N-channel MOSFET is fully enhanced, and VOUT = VIN - (IOUT x rDS(on)). The voltage
drop across the MOSFET is relatively small compared to VIN, and VOUT ≉ VIN.


Both the constant-current devices (TPS255x ) and latch-off devices (TPS255x-1) operate identically during the
initial onset of an overcurrent event. Both devices limit current to the programmed current-limit threshold set to
RILIM by operating the N-channel MOSFET in the linear mode. During current-limit operation, the N-channel
MOSFET is no longer fully-enhanced and the resistance of the device increases. This allows the device to
effectively regulate the current to the current-limit threshold. The effect of increasing the resistance of the
MOSFET is that the voltage drop across the device is no longer negligible (VIN ≠ VOUT), and VOUT decreases. The
amount that VOUT decreases is proportional to the magnitude of the overload condition. The expected VOUT can
be calculated by,

IOS × RLOAD


where


IOS is the current-limit threshold and RLOAD is the magnitude of the overload condition. (2)

For example, if IOS is programmed to 1 A and a 1 Ω overload condition is applied, the resulting VOUT is 1 V.


While both the constant-current devices (TPS255x ) and latch-off devices (TPS255x-1) operate identically during
the initial onset of an overcurrent event, they behave differently if the overcurrent event lasts longer than the
internal delay _de-glitch_ circuit (7.5-ms typical). The constant-current devices (TPS255x ) assert the FAULT flag
after the deglitch period and continue to regulate the current to the current-limit threshold indefinitely. In practical
circuits, the power dissipation in the package increases the die temperature above the overtemperature
shutdown threshold (135°C minimum), and the device turns off until the die temperature decreases by the
hysteresis of the thermal shutdown circuit (10°C typical). The device turns on and continues to thermal cycle until
the overload condition is removed. The constant-current devices resume normal operation once the overload
condition is removed. The latch-off devices (TPS255x-1) assert the FAULT flag after the deglitch period and
immediately turn off the device. The device remains off regardless of whether the overload condition is removed
from the output. The latch-off devices remain off and do not resume normal operation until the surrounding
system either toggles the enable or cycles power to the device.


**10.2** **Typical Applications**


**10.2.1** **Two-Level Current-Limit Circuit**


Some applications require different current-limit thresholds depending on external system conditions. Figure 24
shows an implementation for an externally controlled, two-level current-limit circuit. The current-limit threshold is
set by the total resistance from ILIM to GND (see the _Programming the Current-Limit Threshold_ section). A logiclevel input enables or disables MOSFET Q1 and changes the current-limit threshold by modifying the total
resistance from ILIM to GND. Additional MOSFET and resistor combinations can be used in parallel to Q1/R2 to
increase the number of additional current-limit levels.


**NOTE**
ILIM must never be driven directly with an external signal.



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



17


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**Typical Applications (continued)**









**Output**









**Fault Signal**










|ut 0.1 F �|Col2|
|---|---|
|**0.1**<br>**F**<br>m|**OUT**<br>**IN**<br>**GND**<br>**FAULT**<br>**ILIM**<br>**EN**<br>**Power Pad**|
|** k**<br>**LT**<br>W|** k**<br>**LT**<br>W|
|||



Copyright © 2016, Texas Instruments Incorporated


**Figure 24. Two-Level Current-Limit Circuit**


_**10.2.1.1**_ _**Design Requirements**_


For this example, use the parameters shown in Table 1.


**Table 1. Design Requirements**

|PARAMETER|VALUE|
|---|---|
|Input voltage|5 V|
|Output voltage|5 V|
|Above a minimum current limit|1000 mA|
|Below a maximum current limit|500 mA|



_**10.2.1.2**_ _**Detailed Design Procedures**_


**10.2.1.2.1** **Designing Above a Minimum Current Limit**


Some applications require that current limiting cannot occur below a certain threshold. For this example, assume
that 1 A must be delivered to the load so that the minimum desired current-limit threshold is 1000 mA. Use the
IOS equations and Figure 23 to select RILIM.



I (mA) = 1000mA



OSmin

IOSmin (mA) = R 25230V1.016k



I (mA) =



1.016
ILIM







RILIM (k�) = �����I25230VmA



1
1.016







������IOSmin25230VmA ������



ILIM ���IOSmin



R (k�) = 24k



(3)



ILIM




- 


Select the closest 1% resistor less than the calculated value: RILIM = 23.7 k Ω . This sets the minimum current-limit
threshold at 1 A . Use the IOS equations, Figure 23, and the previously calculated value for RILIM to calculate the
maximum resulting current-limit threshold.



R (k�) = 23.7k



ILIM




- 


22980V
IOSmax (mA) = R 0.94k



OSmax RILIM0.94







22980V
IOSmax (mA) = 23.70.94k�
I (mA) = 1172.4mA



(4)



OSmax 0.94







OSmax



The resulting maximum current-limit threshold is 1172.4 mA with a 23.7-k Ω resistor.



18



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**10.2.1.2.2** **Designing Below a Maximum Current Limit**


Some applications require that current limiting must occur below a certain threshold. For this example, assume
that the desired upper current-limit threshold must be below 500 mA to protect an up-stream power supply. Use
the IOS equations and Figure 23 to select RILIM.



IOSmax (mA) = 500mA

IOSmax (mA) = R22980V0.94k



I (mA) =



0.94
ILIM







RILIM(k� ��� 22980V
) = I�� mA



1
0.94







������ OSmax22980VmA ���� ~~�~~ 


ILIM ��� OSmax



R (k�) = 58.7k



(5)



ILIM




- 


Select the closest 1% resistor greater than the calculated value: RILIM = 59-k Ω . This sets the maximum currentlimit threshold at 500 mA . Use the IOS equations, Figure 23, and the previously calculated value for RILIM to
calculate the minimum resulting current-limit threshold.



R (k�) = 59k



ILIM




- 


25230V
IOSmin(mA) = RILIM1.016k



25230V
IOSmin(mA) = R 1.016k







25230V
IOSmin(mA) = 591.016k
I (mA) = 400.6mA



(6)



OSmin 1.016







OSmin



The resulting minimum current-limit threshold is 400.6 mA with a 59-k Ω resistor.


**10.2.1.2.3** **Accounting for Resistor Tolerance**


The previous sections described the selection of RILIM given certain application requirements and the importance
of understanding the current-limit threshold tolerance. The analysis focused only on the TPS255x and TPS255x1 performance and assumed an exact resistor value. However, resistors sold in quantity are not exact and are
bounded by an upper and lower tolerance centered around a nominal resistance. The additional RILIM resistance
tolerance directly affects the current-limit threshold accuracy at a system level. The following table shows a
process that accounts for worst-case resistor tolerance assuming 1% resistor values. Step one follows the
selection process outlined in the application examples above. Step two determines the upper and lower
resistance bounds of the selected resistor. Step three uses the upper and lower resistor bounds in the IOS
equations to calculate the threshold limits. It is important to use tighter tolerance resistors, for example, 0.5% or
0.1%, when precision current limiting is desired.



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



19


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**Table 2. Common RILIM** **Resistor Selections**











|DESIRED<br>NOMINAL<br>CURRENT<br>LIMIT<br>(mA)|IDEAL<br>RESISTOR<br>(kΩ)|CLOSEST<br>1% RESISTOR<br>(kΩ)|RESISTOR TOLERANCE|Col5|ACTUAL LIMITS|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**DESIRED**<br>**NOMINAL**<br>**CURRENT**<br>**LIMIT**<br>**(mA)**|**IDEAL**<br>**RESISTOR**<br>**(kΩ)**|**CLOSEST**<br>**1% RESISTOR**<br>**(kΩ)**|**1% LOW (kΩ)**|**1% HIGHT**<br>**(kΩ)**|**IOS MIN (mA)**|**IOS NOM (mA)**|**IOS MAX (mA)**|
|75|SHORT ILIM to IN|SHORT ILIM to IN|SHORT ILIM to IN|SHORT ILIM to IN|50.0|75.0|100.0|
|120|226.1|226|223.7|228.3|101.3|120.0|142.1|
|200|134.0|133|131.7|134.3|173.7|201.5|233.9|
|300|88.5|88.7|87.8|89.6|262.1|299.4|342.3|
|400|65.9|66.5|65.8|67.2|351.2|396.7|448.7|
|500|52.5|52.3|51.8|52.8|448.3|501.6|562.4|
|600|43.5|43.2|42.8|43.6|544.3|604.6|673.1|
|700|37.2|37.4|37.0|37.8|630.2|696.0|770.8|
|800|32.4|32.4|32.1|32.7|729.1|800.8|882.1|
|900|28.7|28.7|28.4|29.0|824.7|901.5|988.7|
|1000|25.8|26.1|25.8|26.4|908.3|989.1|1081.0|
|1100|23.4|23.2|23.0|23.4|1023.7|1109.7|1207.5|
|1200|21.4|21.5|21.3|21.7|1106.0|1195.4|1297.1|
|1300|19.7|19.6|19.4|19.8|1215.1|1308.5|1414.9|
|1400|18.3|18.2|18.0|18.4|1310.1|1406.7|1517.0|
|1500|17.0|16.9|16.7|17.1|1412.5|1512.4|1626.4|
|1600|16.0|15.8|15.6|16.0|1512.5|1615.2|1732.7|
|1700|15.0|15.0|14.9|15.2|1594.5|1699.3|1819.4|


**10.2.1.2.4** **Input and Output Capacitance**


Input and output capacitance improves the performance of the device; the actual capacitance must be optimized
for the particular application. For all applications, TI recommends placing a 0.1-µF or greater ceramic bypass
capacitor between IN and GND as close to the device as possible for local noise de-coupling. This precaution
reduces ringing on the input due to power-supply transients. Additional input capacitance may be needed on the
input to reduce voltage overshoot from exceeding the absolute maximum voltage of the device during heavy
transient conditions. This is especially important during bench testing when long, inductive cables are used to
connect the evaluation board to the bench power-supply.


TI recommends placing a high-value electrolytic capacitor on the output pin when large transient currents are
expected on the output.


_**10.2.1.3**_ _**Application Curves**_



20



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**10.2.2** **Auto-Retry Functionality**


Some applications require that an overcurrent condition disables the part momentarily during a fault condition
and re-enables after a pre-set time. This _auto-retry_ functionality can be implemented with an external resistor and
capacitor. During a fault condition, FAULT pulls low disabling the part. The part is disabled when EN is pulled
low, and FAULT goes high impedance allowing CRETRY to begin charging. The part re-enables when the voltage
on EN reaches the turnon threshold, and the auto-retry time is determined by the resistor-capacitor time
constant. The device continues to cycle in this manner until the fault condition is removed.







**TPS2553**





**RLOAD**















Copyright © 2016, Texas Instruments Incorporated


**Figure 27. Auto-Retry Functionality**


Some applications require auto-retry functionality and the ability to enable or disable with an external logic signal.
Figure 28 shows how an external logic signal can drive EN through RFAULT and maintain auto-retry functionality.
The resistor-capacitor time constant determines the auto-retry time-out period.


**TPS2553**



**RLOAD**





















Copyright © 2016, Texas Instruments Incorporated


**Figure 28. Auto-Retry Functionality With External EN Signal**


_**10.2.2.1**_ _**Design Requirements**_


For this example, use the parameters shown in Table 3.


**Table 3. Design Requirements**

|PARAMETER|VALUE|
|---|---|
|Input voltage|5 V|
|Output voltage|5 V|
|Current|1200 mA|



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



21


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


_**10.2.2.2**_ _**Detailed Design Procedure**_


Refer to _Programming the Current-Limit Threshold_ section for the current limit setting. For auto-retry functionality,
once FAULT asserted, EN pull low, TPS2553 is disabled, FAULT des-asserted, CRETRY is slowly charged to EN
logic high through RFAULT, then enable, after deglitch time, FAULT asserted again. In the event of an overload,
TPS2553 cycles and has output average current. ON-time with output current is decided by FAULT deglitch time.
OFF-time without output current is decided by RFAULT x CRETRY constant time to EN logic high and ton time.
Therefore, set the RFAULT × CRETRY to get the desired output average current during overload.


**10.2.3** **Typical Application as USB Power Switch**









**Fault Signal**


**Control Signal**










|ULT<br>kW|Col2|
|---|---|
|||











Copyright © 2016, Texas Instruments Incorporated


**Figure 29. Typical Application as USB Power Switch**


_**10.2.3.1**_ _**Design Requirements**_


For this example, use the parameters shown in Table 4.


**Table 4. Design Requirements**

|PARAMETER|VALUE|
|---|---|
|Input voltage|5 V|
|Output voltage|5 V|
|Current|1200 mA|



**10.2.3.1.1** **USB Power-Distribution Requirements**


USB can be implemented in several ways regardless of the type of USB device being developed. Several powerdistribution features must be implemented.

- SPHs must:

  - Current limit downstream ports

  - Report overcurrent conditions

- BPHs must:

  - Enable or disable power to downstream ports

  - Power up at <100 mA

  - Limit inrush current (<44 Ω and 10 µF)

- Functions must:

  - Limit inrush currents

  - Power up at <100 mA


The feature set of the TPS255x and TPS255x-1 meets each of these requirements. The integrated current
limiting and overcurrent reporting is required by self-powered hubs. The logic-level enable and controlled rise
times meet the need of both input and output ports on bus-powered hubs and the input ports for bus-powered
functions.



22



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


_**10.2.3.2**_ _**Detailed Design Procedure**_


**10.2.3.2.1** **Universal Serial Bus (USB) Power-Distribution Requirements**


One application for this device is for current limiting in universal serial bus (USB) applications. The original USB
interface was a 12-Mbps or 1.5-Mbps, multiplexed serial bus designed for low-to-medium bandwidth PC
peripherals (for example, keyboards, printers, scanners, and mice). As the demand for more bandwidth
increased, the USB 2.0 standard was introduced increasing the maximum data rate to 480-Mbps. The four-wire
USB interface is conceived for dynamic attach-detach (hot plug-unplug) of peripherals. Two lines are provided for
differential data, and two lines are provided for 5-V power distribution.


USB data is a 3.3-V level signal, but power is distributed at 5 V to allow for voltage drops in cases where power
is distributed through more than one hub across long cables. Each function must provide its own regulated 3.3 V
from the 5-V input or its own internal power supply. The USB specification classifies two different classes of
devices depending on its maximum current draw. A device classified as low-power can draw up to 100 mA as
defined by the standard. A device classified as high-power can draw up to 500 mA. It is important that the
minimum current-limit threshold of the current-limiting power-switch exceed the maximum current-limit draw of
the intended application. The latest USB standard must always be referenced when considering the current-limit
threshold


The USB specification defines two types of devices as hubs and functions. A USB hub is a device that contains
multiple ports for different USB devices to connect and can be self-powered (SPH) or bus-powered (BPH). A
function is a USB device that is able to transmit or receive data or control information over the bus. A USB
function can be embedded in a USB hub. A USB function can be one of three types included in the list below.

- Low-power, bus-powered function

- High-power, bus-powered function

- Self-powered function


SPHs and BPHs distribute data and power to downstream functions. The TPS255x has higher current capability
than required for a single USB port allowing it to power multiple downstream ports.



Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



23


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**11** **Power Supply Recommendations**


**11.1** **Self-Powered and Bus-Powered Hubs**


A SPH has a local power supply that powers embedded functions and downstream ports. This power supply
must provide between 4.75 V to 5.25 V to downstream facing devices under full-load and no-load conditions.
SPHs are required to have current-limit protection and must report overcurrent conditions to the USB controller.
Typical SPHs are desktop PCs, monitors, printers, and stand-alone hubs.


A BPH obtains all power from an upstream port and often contains an embedded function. It must power up with
less than 100 mA. The BPH usually has one embedded function, and power is always available to the controller
of the hub. If the embedded function and hub require more than 100 mA on power up, keep the power to the
embedded function off until enumeration is completed. This can be accomplished by removing power or by
shutting off the clock to the embedded function. Power-switching the embedded function is not necessary if the
aggregate power draw for the function and controller is less than 100 mA. The total current drawn by the buspowered device is the sum of the current to the controller, the embedded function, and the downstream ports,
and it is limited to 500 mA from an upstream port.


**11.2** **Low-Power Bus-Powered and High-Power Bus-Powered Functions**


Both low-power and high-power bus-powered functions obtain all power from upstream ports. Low-power
functions always draw less than 100 mA; high-power functions must draw less than 100 mA at power up and can
draw up to 500 mA after enumeration. If the load of the function is more than the parallel combination of 44 Ω
and 10 µF at power up, the device must implement inrush current limiting.


**11.3** **Power Dissipation and Junction Temperature**


The low ON-resistance of the N-channel MOSFET allows small surface-mount packages to pass large currents.
It is good design practice to estimate power dissipation and junction temperature. The below analysis gives an
approximation for calculating junction temperature based on the power dissipation in the package. However, it is
important to note that thermal analysis is strongly dependent on additional system level factors. Such factors
include air flow, board layout, copper thickness and surface area, and proximity to other devices dissipating
power. Good thermal design practice must include all system level factors in addition to individual component
analysis.


Begin by determining the rDS(on) of the N-channel MOSFET relative to the input voltage and operating
temperature. As an initial estimate, use the highest operating ambient temperature of interest and read rDS(on)
from the typical characteristics graph. Using this value, the power dissipation can be calculated using Equation 7.

PD = rDS(on) × IOUT 2


where

       - PD = Total power dissipation (W)

       - rDS(on) = Power switch on-resistance ( Ω )

       - IOUT = Maximum current-limit threshold (A)

       - This step calculates the total power dissipation of the N-channel MOSFET. (7)


Finally, calculate the junction temperature:

TJ = PD × θ JA + TA


where

       - TA = Ambient temperature (°C)

       - θ JA = Thermal resistance (°C/W)

       - PD = Total power dissipation (W) (8)


Compare the calculated junction temperature with the initial estimate. If they are not within a few degrees, repeat
the calculation using the _refined_ rDS(on) from the previous calculation as the new estimate. Two or three iterations
are generally sufficient to achieve the desired result. The final junction temperature is highly dependent on
thermal resistance θ JA, and thermal resistance is highly dependent on the individual package and board layout.
The _Thermal Information_ table provides example thermal resistances for specific packages and board layouts.



24



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


**[www.ti.com](http://www.ti.com)** SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016


**12** **Layout**


**12.1** **Layout Guidelines**


- TI recommends placing the 100-nF bypass capacitor near the IN and GND pins, and make the connections
using a low-inductance trace.

- TI recommends placing a high-value electrolytic capacitor and a 100-nF bypass capacitor on the output pin
when large transient currents are expected on the output.

- The traces routing the RILIM resistor to the device must be as short as possible to reduce parasitic effects on
the current limit accuracy.

- The PowerPAD must be directly connected to PCB ground plane using wide and short copper trace.


**12.2** **Layout Example**













**Figure 30. Layout Recommendation**


Copyright © 2008–2016, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_



25


**[TPS2552, TPS2553, TPS2552-1, TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)**


SLVS841F –NOVEMBER 2008–REVISED AUGUST 2016 **[www.ti.com](http://www.ti.com)**


**13** **Device and Documentation Support**


**13.1** **Device Support**


[For the TI Switch Portfolio, go here.](http://www.ti.com/usbpower)


**13.2** **Related Links**


The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to sample or buy.


**Table 5. Related Links**









|PARTS|PRODUCT FOLDER|SAMPLE & BUY|TECHNICAL<br>DOCUMENTS|TOOLS &<br>SOFTWARE|SUPPORT &<br>COMMUNITY|
|---|---|---|---|---|---|
|TPS32552|Click here|Click here|Click here|Click here|Click here|
|TPS2553|Click here|Click here|Click here|Click here|Click here|
|TPS2552-1|Click here|Click here|Click here|Click here|Click here|
|TPS2553-1|Click here|Click here|Click here|Click here|Click here|


**13.3** **Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on _Alert me_ to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document.


**13.4** **Community Resources**


The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective
[contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of](http://www.ti.com/corp/docs/legal/termsofuse.shtml)
[Use.](http://www.ti.com/corp/docs/legal/termsofuse.shtml)


**[TI E2E™Online Community](http://e2e.ti.com)** _**TI's Engineer-to-Engineer (E2E) Community.**_ Created to foster collaboration

among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help
solve problems with fellow engineers.


**[Design Support](http://support.ti.com/)** _**TI's Design Support**_ Quickly find helpful E2E forums along with design support tools and

contact information for technical support.


**13.5** **Trademarks**

PowerPAD, E2E are trademarks of Texas Instruments.
All other trademarks are the property of their respective owners.


**13.6** **Electrostatic Discharge Caution**


These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam
during storage or handling to prevent electrostatic damage to the MOS gates.


**13.7** **Glossary**


[SLYZ022 —](http://www.ti.com/lit/pdf/SLYZ022) _TI Glossary_ .

This glossary lists and explains terms, acronyms, and definitions.


**14** **Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.



26



_[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SLVS841F&partnum=TPS2552)_ Copyright © 2008–2016, Texas Instruments Incorporated


Product Folder Links: _[TPS2552 TPS2553 TPS2552-1 TPS2553-1](http://www.ti.com/product/tps2552?qgpn=tps2552)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 21-Feb-2026


**PACKAGING INFORMATION**





















Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 21-Feb-2026





















**(1) Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)


**(2) Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.


Addendum-Page 2


### **PACKAGE OPTION ADDENDUM**

www.ti.com 21-Feb-2026


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

**[OTHER QUALIFIED VERSIONS OF TPS2553, TPS2553-1 :]**

- [[Automotive : ][TPS2553-Q1][, ][TPS2553-Q1]](http://focus.ti.com/docs/prod/folders/print/tps2553-q1.html)


[NOTE: Qualified Version Definitions:]

    - [Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects]


Addendum-Page 3


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 10-Sep-2025


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
|TPS2552DBVR|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2552DBVR-1|SOT-23|DBV|6|3000|178.0|9.0|3.23|3.17|1.37|4.0|8.0|Q3|
|TPS2552DBVR1G4|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2552DBVT|SOT-23|DBV|6|250|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2552DBVT-1|SOT-23|DBV|6|250|178.0|9.0|3.23|3.17|1.37|4.0|8.0|Q3|
|TPS2552DBVT-1|SOT-23|DBV|6|250|179.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2552DBVT-11G4|SOT-23|DBV|6|250|178.0|9.0|3.23|3.17|1.37|4.0|8.0|Q3|
|TPS2552DRVR|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2552DRVR|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2552DRVR-1|WSON|DRV|6|3000|179.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS2552DRVRG4|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2552DRVT|WSON|DRV|6|250|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2552DRVT-1|WSON|DRV|6|250|179.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS2552DRVT-1G4|WSON|DRV|6|250|179.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS2553DBVR|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2553DBVR-1|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 10-Sep-2025























|Device|Package<br>Type|Package<br>Drawing|Pins|SPQ|Reel<br>Diameter<br>(mm)|Reel<br>Width<br>W1 (mm)|A0<br>(mm)|B0<br>(mm)|K0<br>(mm)|P1<br>(mm)|W<br>(mm)|Pin1<br>Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TPS2553DBVR-11G4|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2553DBVRG4|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2553DBVT|SOT-23|DBV|6|250|179.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2553DBVT|SOT-23|DBV|6|250|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2553DBVT-1|SOT-23|DBV|6|250|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS2553DRVR|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2553DRVR-1|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2553DRVR-1|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2553DRVRG4|WSON|DRV|6|3000|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2553DRVT|WSON|DRV|6|250|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2553DRVT-1|WSON|DRV|6|250|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|
|TPS2553DRVT-1G4|WSON|DRV|6|250|180.0|8.4|2.3|2.3|1.15|4.0|8.0|Q2|


Pack Materials-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 10-Sep-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TPS2552DBVR|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS2552DBVR-1|SOT-23|DBV|6|3000|180.0|180.0|18.0|
|TPS2552DBVR1G4|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS2552DBVT|SOT-23|DBV|6|250|210.0|185.0|35.0|
|TPS2552DBVT-1|SOT-23|DBV|6|250|180.0|180.0|18.0|
|TPS2552DBVT-1|SOT-23|DBV|6|250|203.0|203.0|35.0|
|TPS2552DBVT-11G4|SOT-23|DBV|6|250|180.0|180.0|18.0|
|TPS2552DRVR|WSON|DRV|6|3000|210.0|185.0|35.0|
|TPS2552DRVR|WSON|DRV|6|3000|182.0|182.0|20.0|
|TPS2552DRVR-1|WSON|DRV|6|3000|200.0|183.0|25.0|
|TPS2552DRVRG4|WSON|DRV|6|3000|182.0|182.0|20.0|
|TPS2552DRVT|WSON|DRV|6|250|182.0|182.0|20.0|
|TPS2552DRVT-1|WSON|DRV|6|250|200.0|183.0|25.0|
|TPS2552DRVT-1G4|WSON|DRV|6|250|200.0|183.0|25.0|
|TPS2553DBVR|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS2553DBVR-1|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS2553DBVR-11G4|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS2553DBVRG4|SOT-23|DBV|6|3000|210.0|185.0|35.0|



Pack Materials-Page 3


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 10-Sep-2025

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TPS2553DBVT|SOT-23|DBV|6|250|200.0|183.0|25.0|
|TPS2553DBVT|SOT-23|DBV|6|250|210.0|185.0|35.0|
|TPS2553DBVT-1|SOT-23|DBV|6|250|210.0|185.0|35.0|
|TPS2553DRVR|WSON|DRV|6|3000|182.0|182.0|20.0|
|TPS2553DRVR-1|WSON|DRV|6|3000|182.0|182.0|20.0|
|TPS2553DRVR-1|WSON|DRV|6|3000|210.0|185.0|35.0|
|TPS2553DRVRG4|WSON|DRV|6|3000|182.0|182.0|20.0|
|TPS2553DRVT|WSON|DRV|6|250|182.0|182.0|20.0|
|TPS2553DRVT-1|WSON|DRV|6|250|182.0|182.0|20.0|
|TPS2553DRVT-1G4|WSON|DRV|6|250|182.0|182.0|20.0|



Pack Materials-Page 4


### **GENERIC PACKAGE VIEW**

## **DRV 6 WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD


Images above are just a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4206925/F


## **PACKAGE OUTLINE**
# DRV0006D SCALE 5.500 WSON - 0.8 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

























NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DRV0006D WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD































NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If some or all are implemented, recommended via locations are shown.


www.ti.com


## **EXAMPLE STENCIL DESIGN**
# **DRV0006D WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD























NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


www.ti.com


## **PACKAGE OUTLINE**
# DRV0006A SCALE 5.500 WSON - 0.8 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

























NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
4. Minimum 0.1 mm solder wetting on pin side wall. Available for wettable flank version only.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DRV0006A WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD





























NOTES: (continued)

5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
6. Vias are optional depending on application, refer to device data sheet. If some or all are implemented, recommended via locations
are shown.


www.ti.com


## **EXAMPLE STENCIL DESIGN**
# **DRV0006A WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD























NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


www.ti.com


## **PACKAGE OUTLINE**
# DBV0006A SCALE 4.000 SOT-23 - 1.45 mm max height

SMALL OUTLINE TRANSISTOR


















|Col1|Col2|0.2|C|A|B|
|---|---|---|---|---|---|
|||||||







NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Body dimensions do not include mold flash or protrusion. Mold flash and protrusion shall not exceed 0.25 per side.
4. Leads 1,2,3 may be wider than leads 4,5,6 for package orientation.
5. Refernce JEDEC MO-178.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DBV0006A SOT-23 - 1.45 mm max height**

SMALL OUTLINE TRANSISTOR























NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**
# **DBV0006A SOT-23 - 1.45 mm max height**

SMALL OUTLINE TRANSISTOR





















NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.


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


Copyright © 2026, Texas Instruments Incorporated


Last updated 10/2025


