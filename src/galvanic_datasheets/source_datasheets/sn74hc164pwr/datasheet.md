Support &
Community


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**



Product

Folder



Sample &
Buy



Technical

Documents



Tools &

Software



SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015
### **SNx4HC164 8-Bit Parallel-Out Serial Shift Registers**



**1** **Features** **3** **Description**

- These 8-bit shift registers feature AND-gated serial



1 - Wide Operating Voltage Range of 2 V to 6 V




- Outputs Can Drive Up to 10 LSTTL Loads inputs and an asynchronous clear (CLR) input. The
gated serial (A and B) inputs permit complete control

- Low Power Consumption, 80- μ A Maximum I CC over incoming data; a low at either input inhibits entry

- Typical t pd = 20 ns of the new data and resets the first flip-flop to the low

- ±4-mA Output Drive at 5 V level at the next clock (CLK) pulse. A high-level input
enables the other input, which then determines the

- Low Input Current of 1- μ A Maximum state of the first flip-flop. Data at the serial inputs can

- AND-Gated (Enable/Disable) Serial Inputs be changed while CLK is high or low, provided the

- minimum set-up time requirements are met. Clocking
Fully Buffered Clock and Serial Inputs

- Direct Clear occurs on the low-to-high-level transition of CLK.

- On Products Compliant to MIL-PRF-38535, **Device Information** **[(1)]**
All Parameters Are Tested Unless Otherwise **PART NUMBER** **PACKAGE** **BODY SIZE (NOM)**
Noted. On All Other Products, Production SOIC (14) 8.65 mm × 3.91 mm
Processing Does Not Necessarily Include Testing PDIP (14) 19.30 mm × 6.35 mm
of All Parameters. SN74HC164


**2** **Applications** TSSOP (14) 5.00 mm × 4.40 mm


- Programable Logic Controllers

- Appliances LCCC (14) 9.39 mm × 9.39 mm

- Video Display Systems

|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|SN74HC164|SOIC (14)|8.65 mm × 3.91 mm|
|SN74HC164|PDIP (14)|19.30 mm × 6.35 mm|
|SN74HC164|SO (14)|10.30 mm × 5.30 mm|
|SN74HC164|TSSOP (14)|5.00 mm × 4.40 mm|
|SN54HC164|CDIP (14)|19.94 mm × 6.92 mm|
|SN54HC164|CFP (14)|9.21 mm × 6.29 mm|
|SN54HC164|LCCC (14)|9.39 mm × 9.39 mm|

(1) For all available packages, see the orderable addendum at

- Output Expander the end of the data sheet.


**Logic Diagram (Positive Logic)**



**CLK**


**A**


**B**


**CLR**





















**Q** **A**



**Q** **B**



**Q** **C**



**Q** **E**



**Q** **F**



**Q** **G**





**Q** **H**



**Q** **D**



1



Pin numbers shown are for the D, J, N, NS, PW, and W packages.


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**Table of Contents**


**1** **Features** .................................................................. 1 **8** **Parameter Measurement Information** ................ 13

**2** **Applications** ........................................................... 1 **9** **Detailed Description** ............................................ 14

**3** **Description** ............................................................. 1 9.1 Overview ................................................................. 14

**4** **Revision History** ..................................................... 2 9.2 Functional Block Diagram ....................................... 14

**5** **Device Comparison Table** ..................................... 3 9.3 Feature Description................................................. 14



9.4 Device Functional Modes........................................ 14
**6** **Pin Configuration and Functions** ......................... 4

**7** **Specifications** ......................................................... 6 **10** **Application and Implementation** ........................ 15

7.1 Absolute Maximum Ratings ...................................... 6 10.1 Application Information.......................................... 15

7.2 ESD Ratings ............................................................ 6 10.2 Typical Application ............................................... 15

7.3 Recommended Operating Conditions....................... 6 **11** **Power Supply Recommendations** ..................... 17



7.4 Thermal Information.................................................. 7 **12** **Layout** ................................................................... 17

7.5 Electrical Characteristics, T A = 25°C ........................ 7 12.1 Layout Guidelines ................................................. 17

7.6 Electrical Characteristics, T A = –55°C to 125°C ....... 7 12.2 Layout Example .................................................... 17

7.7 Electrical Characteristics, T A = –55°C to 85°C ......... 8 **13** **Device and Documentation Support** ................. 18

7.8 Timing Requirements, T A = 25°C.............................. 8 13.1 Documentation Support ........................................ 18

7.9 Timing Requirements, T A = –55°C to 125°C ............ 9 13.2 Related Links ........................................................ 18

7.10 Timing Requirements, T A = –55°C to 85°C ............ 9 13.3 Community Resources.......................................... 18

7.11 Switching Characteristics, T A = 25°C.................... 10 13.4 Trademarks........................................................... 18

7.12 Switching Characteristics, T A = –55°C to 125°C .. 10 13.5 Electrostatic Discharge Caution............................ 18

7.13 Switching Characteristics, T A = –55°C to 85°C .... 11 13.6 Glossary................................................................ 18
7.14 Typical Characteristics.......................................... 12 **14** **Mechanical, Packaging, and Orderable**
**Information** ........................................................... 18


**4** **Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision F (October 2013) to Revision G** **Page**


- Added _Applications_ section, _Device Information_ table, _Pin Configuration and Functions_ section, _ESD Ratings_ table,
_Thermal Information_ table, _Typical Characteristics_ section, _Feature Description_ section, _Device Functional Modes_,
_Application and Implementation_ section, _Power Supply Recommendations_ section, _Layout_ section, _Device and_
_Documentation Support_ section, and _Mechanical, Packaging, and Orderable Information_ section....................................... 1


- Added Military Disclaimer to _Features_ list. ............................................................................................................................. 1


- Added Handling Ratings table................................................................................................................................................ 6


**Changes from Revision E (November 2010) to Revision F** **Page**


- Updated document to new TI data sheet format. ................................................................................................................... 1


- Removed Ordering Information table. .................................................................................................................................... 1


- Updated operating temperature range. .................................................................................................................................. 6


2 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**5** **Device Comparison Table**

|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|SN74HC164D|SOIC (14)|8.65 mm × 3.91 mm|
|SN74HC164N|PDIP (14)|19.30 mm × 6.35 mm|
|SN74HC164NS|SO (14)|10.30 mm × 5.30 mm|
|SN74HC164PW|TSSOP (14)|5.00 mm × 4.40 mm|
|SN54HC164J|CDIP (14)|19.94 mm × 6.92 mm|
|SN54HC164W|CFP (14)|9.21 mm × 6.29 mm|
|SN54HC164FK|LCCC (14)|9.39 mm × 9.39 mm|



Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 3


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**6** **Pin Configuration and Functions**


**D, N, NS, J, W, or PW Package**
**14-Pin SOIC, PDIP, SO, CDIP, CFP, or TSSOP**

**Top View**





A

B

Q A
Q B
Q C
Q D

GND





V CC
Q H
Q G
Q F
Q E

CLR


CLK


|Col1|Col2|Col3|
|---|---|---|
||1<br>2<br>3<br>4<br>5<br>6<br>7<br>14<br>13<br>12<br>11<br>10<br>9<br>8||
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



**Pin Functions**

|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**SOIC, PDIP, SO,**<br>**CDIP, CFP, or**<br>**TSSOP NO.**|**NAME**|**NAME**|**NAME**|
|1|A|I|Gated Serial Input 1|
|2|B|I|Gated Serial Input 2|
|3|QA|O|Parallel Output|
|4|QB|O|Parallel Output|
|5|QC|O|Parallel Output|
|6|QD|O|Parallel Output|
|7|GND|-|Ground|
|8|CLK|I|Clock|
|9|CLR|I|Clear 1 Active-Low|
|10|QE|O|Parallel Output|
|11|QF|O|Parallel Output|
|12|QG|O|Parallel Output|
|13|QH|O|Parallel Output|
|14|VCC|—|Power|



4 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**FK Package**
**20-Pin LCCC**

**Top View**



Q E



Q A

NC


Q B

NC


Q C







Q G

NC


Q F

NC





NC – No internal connection


**Pin Functions**

|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**LCCC NO.**|**NAME**|**NAME**|**NAME**|
|1|NC|—|No Connect|
|2|A|I|Gated Serial Input 1|
|3|B|I|Gated Serial Input 2|
|4|QA|O|Parallel Output|
|5|NC|—|No Connect|
|6|QB|O|Parallel Output|
|7|NC|—|No Connect|
|8|QC|O|Parallel Output|
|9|QD|O|Parallel Output|
|10|GND|—|Ground|
|11|NC|—|No Connect|
|12|CLK|I|Clock|
|13|CLR|I|Clear 1 Active-Low|
|14|QE|O|Parallel Output|
|15|NC|—|No Connect|
|16|QF|O|Parallel Output|
|17|NC|—|No Connect|
|18|QG|O|Parallel Output|
|19|QH|O|Parallel Output|
|20|VCC|—|Power|



Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 5


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**7** **Specifications**


**7.1** **Absolute Maximum Ratings**

over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|MIN MAX|UNITS|
|---|---|---|---|
|VCC<br>Supply voltage|VCC<br>Supply voltage|−0.5<br>7|V|
|IIK<br>Input clamp current(2)|VI < 0 or VI > VCC|±20|mA|
|IOK<br>Output clamp current(2)|VO < 0 or VO > VCC|±20|mA|
|IO<br>Continuous output current|VO = 0 to VCC|±25|mA|
|Continuous current through VCC or GND|Continuous current through VCC or GND|±50|mA|
|Tstg<br>Storage temperature|Tstg<br>Storage temperature|–65<br>150|°C|



(1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress ratings
only, and functional operation of the device at these or any other conditions beyond those indicated under _Recommended Operating_
_Conditions_ is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The input and output voltage ratings may be exceeded if the input and output current ratings are observed.


**7.2** **ESD Ratings**

|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic discharge|Human body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)<br>Electrostatic discharge|Charged-device model (CDM), per JEDEC specification JESD22-C101(2)|±1000|±1000|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**7.3** **Recommended Operating Conditions**

over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|SN54HC164|SN74HC164|UNIT|
|---|---|---|---|---|
|||**MIN**<br>**NOM**<br>**MAX**|**MIN**<br>**NOM**<br>**MAX**|**MIN**<br>**NOM**<br>**MAX**|
|VCC<br>Supply voltage|VCC<br>Supply voltage|2<br>5<br>6|2<br>5<br>6|V|
|VIH<br>High-level input voltage|VCC = 2 V|1.5|1.5|V|
|VIH<br>High-level input voltage|VCC = 4.5 V|3.15|3.15|3.15|
|VIH<br>High-level input voltage|VCC = 6 V|4.2|4.2|4.2|
|VIL<br>Low-level input voltage|VCC = 2 V|0.5|0.5|V|
|VIL<br>Low-level input voltage|VCC = 4.5 V|1.35|1.35|1.35|
|VIL<br>Low-level input voltage|VCC = 6 V|1.8|1.8|1.8|
|VI<br>Input voltage|VI<br>Input voltage|0<br>VCC|0<br>VCC|V|
|VO<br>Output voltage|VO<br>Output voltage|0<br>VCC|0<br>VCC|V|
|Input transition rise and fall<br>Δt/Δv(2)<br>time|VCC = 2 V|1000|1000|ns|
|Input transition rise and fall<br>Δt/Δv(2)<br>time|VCC = 4.5 V|500|500|500|
|Input transition rise and fall<br>Δt/Δv(2)<br>time|VCC = 6 V|400|400|400|
|TA<br>Operating free-air temperature|TA<br>Operating free-air temperature|–55<br>125|–40<br>125|°C|



(1) All unused inputs of the device must be held at V CC or GND to ensure proper device operation. Refer to the TI application report,
_Implications of Slow or Floating CMOS Inputs_ [, SCBA004.](http://www.ti.com/lit/pdf/SCBA004)
(2) If this device is used in the threshold region (from V IL max = 0.5 V to V IH min = 1.5 V), there is a potential to go into the wrong state from
induced grounding, causing double clocking. Operating with the inputs at t t = 1000 ns and V CC = 2 V does not damage the device;
however, functionally, the CLK inputs are not ensured while in the shift, count, or toggle operating modes.


6 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**7.4** **Thermal Information**

|THERMAL METRIC(1)|SN54HC164|Col3|Col4|SN74HC164|Col6|Col7|Col8|UNIT|
|---|---|---|---|---|---|---|---|---|
|**THERMAL METRIC(1)**|**J**<br>**(CDIP)**|**W**<br>**(CFP)**|**FK**<br>**(LCCC)**|**D**<br>**(SOIC)**|**N**<br>**(PDIP)**|**NS**<br>**(SO)**|**PW**<br>**(TSSOP)**|**PW**<br>**(TSSOP)**|
|**THERMAL METRIC(1)**|**14**<br>**PINS**|**14**<br>**PINS**|**20**<br>**PINS**|**14**<br>**PINS**|**14**<br>**PINS**|**14**<br>**PINS**|**14**<br>**PINS**|**14**<br>**PINS**|
|RθJA<br>Junction-to-ambient thermal<br>resistance|—|—|—|86|80|76|113|°C/W|



(1) For more information about traditional and new thermal metrics, see the _Semiconductor and IC Package Thermal Metrics_ application
[report, SPRA953.](http://www.ti.com/lit/pdf/spra953)


**7.5** **Electrical Characteristics, T** **A** **= 25°C**


over recommended operating free-air temperature range (unless otherwise noted)

|PARAMETER|TEST CONDITIONS|Col3|VCC|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|VOH|VI = VIH or VIL|IOH = –20 μA|2 V|1.9<br>1.998|V|
|VOH|VI = VIH or VIL|IOH = –20 μA|4.5 V|4.4<br>4.499|4.4<br>4.499|
|VOH|VI = VIH or VIL|IOH = –20 μA|6 V|5.9<br>5.999|5.9<br>5.999|
|VOH|VI = VIH or VIL|IOH = –4 mA|4.5 V|3.98<br>4.3|3.98<br>4.3|
|VOH|VI = VIH or VIL|IOH = –5.2 mA|6 V|5.48<br>5.8|5.48<br>5.8|
|VOL|VI = VIH or VIL|IOL = 20 μA|2 V|0.002<br>0.1|V|
|VOL|VI = VIH or VIL|IOL = 20 μA|4.5 V|0.001<br>0.1|0.001<br>0.1|
|VOL|VI = VIH or VIL|IOL = 20 μA|6 V|0.001<br>0.1|0.001<br>0.1|
|VOL|VI = VIH or VIL|IOL = 4 mA|4.5 V|0.17<br>0.26|0.17<br>0.26|
|VOL|VI = VIH or VIL|IOL = 5.2 mA|6 V|0.15<br>0.26|0.15<br>0.26|
|II|VI = VCC or 0|VI = VCC or 0|6 V|±0.1<br>±100|nA|
|ICC|VI = VCC or 0|IO = 0|6 V|8|µA|
|Ci|||2 V to<br>6 V|3<br>10|pF|



**7.6** **Electrical Characteristics, T** **A** **= –55°C to 125°C**


over recommended operating free-air temperature range (unless otherwise noted)

|PARAMETER|TEST CONDITIONS|Col3|VCC|SN54HC164|Recommended<br>SN74HC164|UNIT|
|---|---|---|---|---|---|---|
|**PARAMETER**|**TEST CONDITIONS**|**TEST CONDITIONS**|**VCC**|**MIN**<br>**TYP**<br>**MAX**|**MIN**<br>**TYP**<br>**MAX**|**MIN**<br>**TYP**<br>**MAX**|
|VOH|VI = VIH or VIL|IOH = –20 μA|2 V|1.9|1.9|V|
|VOH|VI = VIH or VIL|IOH = –20 μA|4.5 V|4.4|4.4|4.4|
|VOH|VI = VIH or VIL|IOH = –20 μA|6 V|5.9|5.9|5.9|
|VOH|VI = VIH or VIL|IOH = –4 mA|4.5 V|3.7|3.7|3.7|
|VOH|VI = VIH or VIL|IOH = –5.2 mA|6 V|5.2|5.2|5.2|
|VOL|VI = VIH or VIL|IOL = 20 μA|2 V|0.1|0.1|V|
|VOL|VI = VIH or VIL|IOL = 20 μA|4.5 V|0.1|0.1|0.1|
|VOL|VI = VIH or VIL|IOL = 20 μA|6 V|0.1|0.1|0.1|
|VOL|VI = VIH or VIL|IOL = 4 mA|4.5 V|0.4|0.4|0.4|
|VOL|VI = VIH or VIL|IOL = 5.2 mA|6 V|0.4|0.4|0.4|
|II|VI = VCC or 0|VI = VCC or 0|6 V|±1000|±1000|nA|
|ICC|VI = VCC or 0|IO = 0|6 V|160|160|µA|
|Ci|||2 V to<br>6 V|10|10|pF|



Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 7


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**7.7** **Electrical Characteristics, T** **A** **= –55°C to 85°C**


over recommended operating free-air temperature range (unless otherwise noted)

|PARAMETER|TEST CONDITIONS|Col3|VCC|SN74HC164|UNIT|
|---|---|---|---|---|---|
|**PARAMETER**|**TEST CONDITIONS**|**TEST CONDITIONS**|**VCC**|**MIN**<br>**TYP**<br>**MAX**|**MIN**<br>**TYP**<br>**MAX**|
|VOH|VI = VIH or VIL|IOH = –20 μA|2 V|1.9|V|
|VOH|VI = VIH or VIL|IOH = –20 μA|4.5 V|4.4|4.4|
|VOH|VI = VIH or VIL|IOH = –20 μA|6 V|5.9|5.9|
|VOH|VI = VIH or VIL|IOH = –4 mA|4.5 V|3.84|3.84|
|VOH|VI = VIH or VIL|IOH = –5.2 mA|6 V|5.34|5.34|
|VOL|VI = VIH or VIL|IOL = 20 μA|2 V|0.1|V|
|VOL|VI = VIH or VIL|IOL = 20 μA|4.5 V|0.1|0.1|
|VOL|VI = VIH or VIL|IOL = 20 μA|6 V|0.1|0.1|
|VOL|VI = VIH or VIL|IOL = 4 mA|4.5 V|0.33|0.33|
|VOL|VI = VIH or VIL|IOL = 5.2 mA|6 V|0.33|0.33|
|II|VI = VCC or 0|VI = VCC or 0|6 V|±1000|nA|
|ICC|VI = VCC or 0|IO = 0|6 V|80|µA|
|Ci|||2 V to<br>6 V|10|pF|



**7.8** **Timing Requirements, T** **A** **= 25°C**


over recommended operating free-air temperature range (unless otherwise noted)

|PARAMETER|Col2|V<br>CC|MIN NOM MAX|UNIT|
|---|---|---|---|---|
|fclock<br>Clock frequency|fclock<br>Clock frequency|2 V|6|MHz|
|fclock<br>Clock frequency|fclock<br>Clock frequency|4.5 V|31|31|
|fclock<br>Clock frequency|fclock<br>Clock frequency|6 V|36|36|
|tw<br>Pulse duration|CLR low|2 V|100|ns|
|tw<br>Pulse duration|CLR low|4.5 V|20|20|
|tw<br>Pulse duration|CLR low|6 V|17|17|
|tw<br>Pulse duration|CLK high or low|2 V|80|80|
|tw<br>Pulse duration|CLK high or low|4.5 V|16|16|
|tw<br>Pulse duration|CLK high or low|6 V|14|14|
|tsu<br>Setup time before CLK↑|Data|2 V|100|ns|
|tsu<br>Setup time before CLK↑|Data|4.5 V|20|20|
|tsu<br>Setup time before CLK↑|Data|6 V|17|17|
|tsu<br>Setup time before CLK↑|CLR inactive|2 V|100|100|
|tsu<br>Setup time before CLK↑|CLR inactive|4.5 V|20|20|
|tsu<br>Setup time before CLK↑|CLR inactive|6 V|17|17|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|2 V|5|ns|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|4.5 V|5|5|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|6 V|5|5|



8 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**7.9** **Timing Requirements, T** **A** **= –55°C to 125°C**


over recommended operating free-air temperature range (unless otherwise noted)

|PARAMETER|Col2|V<br>CC|SN54HC164|RECOMMENDED<br>SN74HC164|UNIT|
|---|---|---|---|---|---|
|**PARAMETER**|**PARAMETER**|**VCC**|**MIN**<br>**NOM**<br>**MAX**|**MIN**<br>**NOM**<br>**MAX**|**MIN**<br>**NOM**<br>**MAX**|
|fclock<br>Clock frequency|fclock<br>Clock frequency|2 V|4.2|4.2|MHz|
|fclock<br>Clock frequency|fclock<br>Clock frequency|4.5 V|21|21|21|
|fclock<br>Clock frequency|fclock<br>Clock frequency|6 V|25|25|25|
|tw<br>Pulse duration|CLR low|2 V|150|125|ns|
|tw<br>Pulse duration|CLR low|4.5 V|30|25|25|
|tw<br>Pulse duration|CLR low|6 V|25|21|21|
|tw<br>Pulse duration|CLK high or low|2 V|120|120|120|
|tw<br>Pulse duration|CLK high or low|4.5 V|24|24|24|
|tw<br>Pulse duration|CLK high or low|6 V|20|20|20|
|tsu<br>Setup time before CLK↑|Data|2 V|150|125|ns|
|tsu<br>Setup time before CLK↑|Data|4.5 V|30|25|25|
|tsu<br>Setup time before CLK↑|Data|6 V|25|25|25|
|tsu<br>Setup time before CLK↑|CLR inactive|2 V|150|125|125|
|tsu<br>Setup time before CLK↑|CLR inactive|4.5 V|30|25|25|
|tsu<br>Setup time before CLK↑|CLR inactive|6 V|25|25|25|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|2 V|5|5|ns|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|4.5 V|5|5|5|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|6 V|5|5|5|



**7.10** **Timing Requirements, T** **A** **= –55°C to 85°C**


over recommended operating free-air temperature range (unless otherwise noted)

|PARAMETER|Col2|V<br>CC|SN74HC164|UNIT|
|---|---|---|---|---|
|**PARAMETER**|**PARAMETER**|**VCC**|**MIN**<br>**NOM**<br>**MAX**|**MIN**<br>**NOM**<br>**MAX**|
|fclock<br>Clock frequency|fclock<br>Clock frequency|2 V|5|MHz|
|fclock<br>Clock frequency|fclock<br>Clock frequency|4.5 V|25|25|
|fclock<br>Clock frequency|fclock<br>Clock frequency|6 V|28|28|
|tw<br>Pulse duration|CLR low|2 V|125|ns|
|tw<br>Pulse duration|CLR low|4.5 V|25|25|
|tw<br>Pulse duration|CLR low|6 V|21|21|
|tw<br>Pulse duration|CLK high or low|2 V|100|100|
|tw<br>Pulse duration|CLK high or low|4.5 V|20|20|
|tw<br>Pulse duration|CLK high or low|6 V|18|18|
|tsu<br>Setup time before CLK↑|Data|2 V|125|ns|
|tsu<br>Setup time before CLK↑|Data|4.5 V|25|25|
|tsu<br>Setup time before CLK↑|Data|6 V|21|21|
|tsu<br>Setup time before CLK↑|CLR inactive|2 V|125|125|
|tsu<br>Setup time before CLK↑|CLR inactive|4.5 V|25|25|
|tsu<br>Setup time before CLK↑|CLR inactive|6 V|21|21|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|2 V|5|ns|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|4.5 V|5|5|
|th<br>Hold time, data after CLK↑|th<br>Hold time, data after CLK↑|6 V|5|5|



Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 9


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**7.11** **Switching Characteristics, T** **A** **= 25°C**


over recommended operating free-air temperature range, C L = 50 pF (unless otherwise noted) (see Figure 3)

|PARAMETER|FROM (INPUT)|TO (OUTPUT)|V<br>CC|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|fmax|||2 V|6<br>10|MHz|
|fmax|||4.5 V|31<br>54|31<br>54|
|fmax|||6 V|36<br>62|36<br>62|
|tPHL|CLR|Any Q|2 V|140<br>205|ns|
|tPHL|CLR|Any Q|4.5 V|28<br>41|28<br>41|
|tPHL|CLR|Any Q|6 V|24<br>35|24<br>35|
|tpd|CLK|Any Q|2 V|115<br>175||
|tpd|CLK|Any Q|4.5 V|23<br>35|23<br>35|
|tpd|CLK|Any Q|6 V|20<br>30|20<br>30|
|tt|||2 V|38<br>75|ns|
|tt|||4.5 V|8<br>15|8<br>15|
|tt|||6 V|6<br>13|6<br>13|



**7.12** **Switching Characteristics, T** **A** **= –55°C to 125°C**


over recommended operating free-air temperature range, C L = 50 pF (unless otherwise noted) (see Figure 3)

|PARAMETER|FROM<br>(INPUT)|TO (OUTPUT)|V<br>CC|SN54HC164|RECOMMENDED<br>SN74HC164|UNIT|
|---|---|---|---|---|---|---|
|**PARAMETER**|**FROM**<br>**(INPUT)**|**TO (OUTPUT)**|**VCC**|**MIN**<br>**TYP**<br>**MAX**|**MIN**<br>**TYP**<br>**MAX**|**MIN**<br>**TYP**<br>**MAX**|
|fmax|||2 V|4.2|4.2|MHz|
|fmax|||4.5 V|21|21|21|
|fmax|||6 V|25|25|25|
|tPHL|CLR|Any Q|2 V|295|255|ns|
|tPHL|CLR|Any Q|4.5 V|59|51|51|
|tPHL|CLR|Any Q|6 V|51|46|46|
|tpd|CLK|Any Q|2 V|265|220||
|tpd|CLK|Any Q|4.5 V|53|44|44|
|tpd|CLK|Any Q|6 V|45|38|38|
|tt|||2 V|110|110|ns|
|tt|||4.5 V|22|22|22|
|tt|||6 V|19|19|19|



10 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**7.13** **Switching Characteristics, T** **A** **= –55°C to 85°C**


over recommended operating free-air temperature range, C L = 50 pF (unless otherwise noted) (see Figure 3)

|PARAMETER|FROM (INPUT)|TO (OUTPUT)|V<br>CC|SN74HC164|UNIT|
|---|---|---|---|---|---|
|**PARAMETER**|**FROM (INPUT)**|**TO (OUTPUT)**|**VCC**|**MIN**<br>**TYP**<br>**MAX**|**MIN**<br>**TYP**<br>**MAX**|
|fmax|||2 V|5|MHz|
|fmax|||4.5 V|25|25|
|fmax|||6 V|28|28|
|tPHL|CLR|Any Q|2 V|255|ns|
|tPHL|CLR|Any Q|4.5 V|51|51|
|tPHL|CLR|Any Q|6 V|46|46|
|tpd|CLK|Any Q|2 V|220||
|tpd|CLK|Any Q|4.5 V|44|44|
|tpd|CLK|Any Q|6 V|38|38|
|tt|||2 V|95|ns|
|tt|||4.5 V|19|19|
|tt|||6 V|16|16|



**CLR**


**A**


**B**


**CLK**


**Q** **A**


**Q** **B**


**Q** **C**


**Q** **D**


**Q** **E**


**Q** **F**


**Q** **G**


**Q** **H**


**Clear** **Clear**


**Figure 1. SN74HC164 Example Timing Diagram**


Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 11


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**7.14** **Typical Characteristics**


T A = 25°C


12 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**8** **Parameter Measurement Information**



**V** **CC**


**0 V**


**V** **CC**


**0 V**



**High-Level**
**Pulse**



**Low-Level**


**Pulse**





**V** **CC**


**0 V**


**V** **CC**


**0 V**



**V** **OH**


**V** **OL**





**VOLTAGE WAVEFORMS**

**PULSE DURATIONS**



**V** **CC**


**0 V**


**V** **OH**


**V** **OL**



**Input**


**In-Phase**

**Output**


**Out-of-Phase**

**Output**





**Reference**


**Input**


**Data**

**Input**



**From Output** **Test**
**Under Test** **Point**


**C** **L** **= 50 pF**
**(see Note A)**


**LOAD CIRCUIT**




|50%<br>tsu th<br>90% 90%<br>50% 50%<br>10% 10%<br>tr tf|Col2|Col3|
|---|---|---|
|||**t**<br>**f**|
||||


|Col1|90% 90%<br>tr|Col3|Col4|
|---|---|---|---|
|||||


|t 50% 50%<br>tPLH tPHL<br>e<br>90% 90%<br>t 50% 50%<br>10% 10%<br>tr tf<br>tPHL tPLH<br>e 90% 50% 50% 90%<br>t 10% 10%<br>tf tr|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**90%**<br>**e**<br>**t**|||||**90%**|
|**90%**<br>**e**<br>**t**||**t**<br>**f**|||**t**<br>**r**|



**VOLTAGE WAVEFORMS**

**SETUP AND HOLD AND INPUT RISE AND FALL TIMES**



**VOLTAGE WAVEFORMS**

**PROPAGATION DELAY AND OUTPUT TRANSITION TIMES**



NOTES: A. C L includes probe and test-fixture capacitance.
B. Phase relationships between waveforms were chosen arbitrarily. All input pulses are supplied by generators having the following
characteristics: PRR ≤ 1 MHz, Z O = 50 Ω, t r = 6 ns, t f = 6 ns.
C. For clock inputs, f max is measured when the input duty cycle is 50%.
D. The outputs are measured one at a time with one input transition per measurement.
E. t PLH and t PHL are the same as t pd .


**Figure 3. Load Circuit and Voltage Waveforms**


Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 13


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**9** **Detailed Description**


**9.1** **Overview**


The SN74HC164 is an 8-bit shift register with 2 serial inputs (A and B) connected through an AND gate, as well
as an asynchronous clear (CLR). The device requires a high signal on both A and B in order to set the input data
line high; a low signal on either input will set the input data line low. Data at A and B can be changed while CLK
is high or low, provided that the minimum set-up time requirements are met.


The CLK pin of the SN74HC164 is triggered on a positive or rising-edge signal, from LOW to HIGH. Upon a
positive-edge trigger, the device will store the result of the (A - B) input data line in the first register and
propagate each register’s data to the next register. The data of the last register, QH, will be discarded at each
clock trigger. If a low signal is applied to the CLR pin of the SN74HC164, the device will set all registers to a
value of 0 immediately.


**9.2** **Functional Block Diagram**



**CLK**


**A**


**B**


**CLR**





















**Q** **A**



**Q** **B**



**Q** **C**



**Q** **E**



**Q** **F**



**Q** **G**





**Q** **H**



**Q** **D**



Pin numbers shown are for the D, J, N, NS, PW, and W packages.


**9.3** **Feature Description**


The HC164 has a wide operating voltage range of 2 V to 6 V, outputs that can drive up to 10 LSTTL loads and
Low Power Consumption, 80- μ A maximum I. It is typically t pd = 20 ns and has ±4-mA output drive at 5 V with low
input current of 1- μ A maximum. It also has AND-gated (enable/disable) serial inputs a fully buffered clock and
serial inputs as well as a direct clear.


**9.4** **Device Functional Modes**


Table 1 lists the functional modes of the SNx4HC164.


**Table 1. Function Table** **[(1)(2)]**

|INPUTS|Col2|Col3|Col4|OUTPUTS|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**CLR**|**CLK**|**A**|**B**|**QA**|**QB**|**. . .**|**QH**|
|L|X|X|X|L|L||L|
|H|L|X|X|QA0|QB0||QH0|
|H|↑|H|H|H|QAn||QGn|
|H|↑|L|X|L|QAn||QGn|
|H|↑|X|L|L|QAn||QGn|



(1) Q A0, Q B0, Q H0 = the level of Q A, Q B, or Q H, respectively, before the
indicated steady-state input conditions were established.
(2) Q An, Q Gn = the level of Q A or Q G before the most recent ↑ transition
of CLK: indicates a 1-bit shift.


14 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**10** **Application and Implementation**


**10.1** **Application Information**


The SNx4HC164 is an 8-bit shift register that can be used as a deserializer in order to reduce the number of
GPIO's needed when driving multiple LED's. In order to correctly display the proper output in the LED's a sink
MOSFET was added to prevent the LED's from lighting up until the correct data or the proper clock signal has
been achieved.


**10.2** **Typical Application**






























|8|Col2|
|---|---|
|9||











GND


**Figure 4. Typical Application Diagram**


**10.2.1** **Design Requirements**


Ensure that the incoming clock rising edge meets the criteria in _Recommended Operating Conditions_ .


**10.2.2** **Detailed Design Procedure**


Ensure that input and output voltages do not exceed ratings in _Absolute Maximum Ratings_ .


Input voltage threshold information can be found in _Recommended Operating Conditions_ .


Detailed timing requirements can be found in _Timing Requirements, T_ _A_ _= 25°C_ .


Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 15


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**Typical Application (continued)**


**10.2.3** **Application Curve**


120


110


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


1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5


V CC (V) C001


**Figure 5. Propagation Delay vs Supply Voltage at T** **A** **= 25°C**


16 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


**[www.ti.com](http://www.ti.com)** SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015


**11** **Power Supply Recommendations**


The power supply can be any voltage between the minimum and maximum supply voltage rating located in the
_Recommended Operating Conditions_ table.


Each V CC pin must have a good bypass capacitor in order to prevent power disturbance. For devices with a
single supply, a 0.1- μ F capacitor is recommended and if there are multiple V CC pins then a 0.01- μ F or 0.022- μ F
capacitor is recommended for each power pin. It is ok to parallel multiple bypass caps to reject different
frequencies of noise. 0.1- μ F and 1- μ F capacitors are commonly used in parallel. The bypass capacitor should be
installed as close to the power pin as possible for best results.


**12** **Layout**


**12.1** **Layout Guidelines**


Reflections and matching are closely related to loop antenna theory, but different enough to warrant their own
discussion. When a PCB trace turns a corner at a 90° angle, a reflection can occur. This is primarily due to the
change of width of the trace. At the apex of the turn, the trace width is increased to 1.414 times its width. This
upsets the transmission line characteristics, especially the distributed capacitance and self–inductance of the
trace — resulting in the reflection. It is a given that not all PCB traces can be straight, and so they will have to
turn corners. Figure 6 shows progressively better techniques of rounding corners. Only the last example
maintains constant trace width and minimizes reflections.


**12.2** **Layout Example**



WORST BETTER BEST



W


**Figure 6. Trace Example**


Copyright © 1982–2015, Texas Instruments Incorporated _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ 17


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


**[SN54HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)** **,** **[SN74HC164](http://www.ti.com/product/sn74hc164?qgpn=sn74hc164)**


SCLS115G –DECEMBER 1982–REVISED SEPTEMBER 2015 **[www.ti.com](http://www.ti.com)**


**13** **Device and Documentation Support**


**13.1** **Documentation Support**


**13.1.1** **Related Documentation**


For related docunmentation, see the following:

_Implications of Slow or Floating CMOS Inputs_ [, SCBA004](http://www.ti.com/lit/pdf/SCBA004)


**13.2** **Related Links**


The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to sample or buy.


**Table 2. Related Links**

|PARTS|PRODUCT FOLDER|SAMPLE & BUY|TECHNICAL<br>DOCUMENTS|TOOLS &<br>SOFTWARE|SUPPORT &<br>COMMUNITY|
|---|---|---|---|---|---|
|SN54HC164|Click here|Click here|Click here|Click here|Click here|
|SN74HC164|Click here|Click here|Click here|Click here|Click here|



**13.3** **Community Resources**


The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective
[contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of](http://www.ti.com/corp/docs/legal/termsofuse.shtml)
[Use.](http://www.ti.com/corp/docs/legal/termsofuse.shtml)


**[TI E2E™Online Community](http://e2e.ti.com)** _**TI's Engineer-to-Engineer (E2E) Community.**_ Created to foster collaboration

among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help
solve problems with fellow engineers.


**[Design Support](http://support.ti.com/)** _**TI's Design Support**_ Quickly find helpful E2E forums along with design support tools and

contact information for technical support.


**13.4** **Trademarks**

E2E is a trademark of Texas Instruments.
All other trademarks are the property of their respective owners.


**13.5** **Electrostatic Discharge Caution**


These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam
during storage or handling to prevent electrostatic damage to the MOS gates.


**13.6** **Glossary**


[SLYZ022 —](http://www.ti.com/lit/pdf/SLYZ022) _TI Glossary_ .

This glossary lists and explains terms, acronyms, and definitions.


**14** **Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


18 _[Submit Documentation Feedback](http://www.go-dsp.com/forms/techdoc/doc_feedback.htm?litnum=SCLS115G&partnum=SN54HC164)_ Copyright © 1982–2015, Texas Instruments Incorporated


Product Folder Links: _[SN54HC164 SN74HC164](http://www.ti.com/product/sn54hc164?qgpn=sn54hc164)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 30-Aug-2025


**PACKAGING INFORMATION**





















Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 30-Aug-2025





















**(1)** **Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)


**(2)** **Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.


Addendum-Page 2


### **PACKAGE OPTION ADDENDUM**

www.ti.com 30-Aug-2025


**(3)** **RoHS values:** [Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.](https://www.ti.com/lit/szzq088)


**(4)** **Lead finish/Ball material:** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.


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

**[OTHER QUALIFIED VERSIONS OF SN54HC164, SN54HC164-SP, SN74HC164 :]**

- [[Catalog : ][SN74HC164][, ][SN54HC164]](http://focus.ti.com/docs/prod/folders/print/sn74hc164.html)


- [[Military : ][SN54HC164]](http://focus.ti.com/docs/prod/folders/print/sn54hc164.html)


- [[Space : ][SN54HC164-SP]](http://focus.ti.com/docs/prod/folders/print/sn54hc164-sp.html)


[NOTE: Qualified Version Definitions:]


    - [Catalog - TI's standard catalog product]


    - [Military - QML certified for Military and Defense Applications]


    - [Space - Radiation tolerant, ceramic packaging and qualified for use in Space-based application]


Addendum-Page 3


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 25-Jul-2025


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
|SN74HC164DR|SOIC|D|14|2500|330.0|16.4|6.5|9.0|2.1|8.0|16.0|Q1|
|SN74HC164DR|SOIC|D|14|2500|330.0|16.4|6.5|9.0|2.1|8.0|16.0|Q1|
|SN74HC164DRG3|SOIC|D|14|2500|330.0|16.8|6.5|9.5|2.1|8.0|16.0|Q1|
|SN74HC164DRG4|SOIC|D|14|2500|330.0|16.4|6.5|9.0|2.1|8.0|16.0|Q1|
|SN74HC164DRG4|SOIC|D|14|2500|330.0|16.4|6.5|9.0|2.1|8.0|16.0|Q1|
|SN74HC164NSR|SOP|NS|14|2000|330.0|16.4|8.1|10.4|2.5|12.0|16.0|Q1|
|SN74HC164PWR|TSSOP|PW|14|2000|330.0|12.4|6.9|5.6|1.6|8.0|12.0|Q1|
|SN74HC164PWRG4|TSSOP|PW|14|2000|330.0|12.4|6.9|5.6|1.6|8.0|12.0|Q1|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 25-Jul-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|SN74HC164DR|SOIC|D|14|2500|340.5|336.1|32.0|
|SN74HC164DR|SOIC|D|14|2500|340.5|336.1|32.0|
|SN74HC164DRG3|SOIC|D|14|2500|364.0|364.0|27.0|
|SN74HC164DRG4|SOIC|D|14|2500|340.5|336.1|32.0|
|SN74HC164DRG4|SOIC|D|14|2500|353.0|353.0|32.0|
|SN74HC164NSR|SOP|NS|14|2000|353.0|353.0|32.0|
|SN74HC164PWR|TSSOP|PW|14|2000|356.0|356.0|35.0|
|SN74HC164PWRG4|TSSOP|PW|14|2000|353.0|353.0|32.0|



Pack Materials-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 25-Jul-2025


**TUBE**


**T - Tube**

**height** **L - Tube length**

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||



**B - Alignment groove width**


*All dimensions are nominal

|Device|Package Name|Package Type|Pins|SPQ|L (mm)|W (mm)|T (µm)|B (mm)|
|---|---|---|---|---|---|---|---|---|
|5962-8416201VDA|W|CFP|14|25|506.98|26.16|6220|NA|
|5962-8416201VDA.A|W|CFP|14|25|506.98|26.16|6220|NA|
|84162012A|FK|LCCC|20|55|506.98|12.06|2030|NA|
|SN74HC164N|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164N|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164N.A|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164N.A|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164N.B|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164N.B|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164NE4|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164NE4|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164NE4.A|N|PDIP|14|25|506|13.97|11230|4.32|
|SN74HC164NE4.A|N|PDIP|14|25|506|13.97|11230|4.32|
|SNJ54HC164FK|FK|LCCC|20|55|506.98|12.06|2030|NA|
|SNJ54HC164FK.A|FK|LCCC|20|55|506.98|12.06|2030|NA|
|SNJ54HC164W|W|CFP|14|25|506.98|26.16|6220|NA|
|SNJ54HC164W.A|W|CFP|14|25|506.98|26.16|6220|NA|



Pack Materials-Page 3


## **PACKAGE OUTLINE**

# **D0014A SOIC - 1.75 mm max height**

~~SCALE 1.800~~


SMALL OUTLINE INTEGRATED CIRCUIT

























NOTES:

1. All linear dimensions are in millimeters. Dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm, per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.43 mm, per side.
5. Reference JEDEC registration MS-012, variation AB.


www.ti.com


## **EXAMPLE BOARD LAYOUT**

# **D0014A SOIC - 1.75 mm max height**

SMALL OUTLINE INTEGRATED CIRCUIT



















NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**

# **D0014A SOIC - 1.75 mm max height**

SMALL OUTLINE INTEGRATED CIRCUIT













NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.


www.ti.com


## **GENERIC PACKAGE VIEW**

# **FK 20 LCCC - 2.03 mm max height**

**8.89 x 8.89, 1.27 mm pitch** LEADLESS CERAMIC CHIP CARRIER


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4229370\/A\


www.ti.com


## **PACKAGE OUTLINE**

# J0014A SCALE 0.900 CDIP - 5.08 mm max height

CERAMIC DUAL IN LINE PACKAGE





















NOTES:

1. All controlling linear dimensions are in inches. Dimensions in brackets are in millimeters. Any dimension in brackets or parenthesis are for
reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This package is hermitically sealed with a ceramic lid using glass frit.
4. Index point is provided on cap for terminal identification only and on press ceramic glass frit seal only.
5. Falls within MIL-STD-1835 and GDIP1-T14.


www.ti.com


## **EXAMPLE BOARD LAYOUT**

# **J0014A CDIP - 5.08 mm max height**

CERAMIC DUAL IN LINE PACKAGE



















www.ti.com


## **PACKAGE OUTLINE**

# **PW0014A TSSOP - 1.2 mm max height**

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

# **PW0014A TSSOP - 1.2 mm max height**

SMALL OUTLINE PACKAGE































NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**

# **PW0014A TSSOP - 1.2 mm max height**

SMALL OUTLINE PACKAGE















NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
9. Board assembly site may have different recommendations for stencil design.


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


