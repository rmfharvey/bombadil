**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** [SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021](https://www.ti.com/product/TPS92520-Q1) **[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
## **TPS92520-Q1 4.5-V to 65-V Dual 1.6-A Synchronous Buck LED Driver with SPI Control**

##### **1 Features**

 - AEC-Q100 qualified for automotive applications

–
Grade 1: –40°C to 125°C ambient operating
temperature

– Device HBM classification level H1C

– Device CDM classification level C5

 - [Functional Safety-Capable](http://www.ti.com/technologies/functional-safety/overview.html)

–
[Documentation available to aid functional safety](https://www.ti.com/product/TPS92520-Q1#tech-docs)
[system design](https://www.ti.com/product/TPS92520-Q1#tech-docs)

 - 4.5-V to 65-V wide input voltage range

 - Up to 1.6-A continuous output current with 4%

accuracy

 - Adaptive on-time average current control

 - Programmable switching frequency from 100-kHz
to 2.2-MHz

 - Advanced dimming operation

–
10-bit precision analog dimming

–
10-bit precision internal PWM dimming

–
Supports external PWM dimming input

–
Optimized for external shunt dimming including
LED Matrix Manager

 - Cycle-by-cycle switch overcurrent protection

 - Switch thermal protection

 - Serial peripheral interface (SPI)

–
Configurable analog reference, switching
frequency, and PWM dimming duty cycle

–
Fault monitoring and reporting

 - Limp-home (LH) and stand-alone mode operation **2 Applications**

 - [Automotive headlight and adaptive LED driving](https://www.ti.com/solution/automotive-headlight)
[module](https://www.ti.com/solution/automotive-headlight) **3 Description**

The TPS92520-Q1 is a monolithic dual synchronous
buck LED driver with a wide 4.5-V to 65-V operating
input voltage range that can independently power two
strings of series connected LEDs. The TPS92520-Q1
implements an adaptive on-time average current
mode control and is designed to be compatible with
shunt FET dimming techniques and LED matrix
manager-based dynamic beam headlamps. The
adaptive on-time control provides near constant
switching frequency that can be set between 100-kHz
and 2.2-MHz. Inductor current sensing and closedloop feedback enables better than ±4% accuracy over
wide input voltage, output voltage and ambient
temperature range.


The high performance LED driver can independently
modulate LED current using both analog or PWM
dimming techniques. Linear analog dimming response
with over 16:1 range is obtained by programming the
10-bit IADJ value via SPI. PWM dimming of LED
current is achieved by directly modulating the
corresponding UDIM input pin with the desired duty
cycle or by enabling the internal PWM generator
circuit. The PWM generator translates the 10-bit PWM
register value to a corresponding duty cycle by
comparing it to a programmable digital counter.

The TPS92520-Q1 incorporates advanced SPI
programmable diagnostic and fault protection
featuring: cycle-by-cycle switch current limit, bootstrap
undervoltage, LED open, LED short, thermal warning
and thermal shutdown. An on-board 10-bit ADC
samples critical input parameters required for system
health monitoring and diagnostics.

The TPS92520-Q1 is available in a 8.1-mm x 11-mm
thermally-enhanced 32-pin HTSSOP package with a
2.75-mm x 3.45-mm top-exposed and bottomexposed pad.

**Device Information**

(1) For all available packages, see the orderable addendum at
the end of the data sheet.

LED1+

1 COMP1 CSN1 32

C OUT1 2 UDIM1 CSP1 31 R CS1

R UV12 R UV11 3 PGND BST1 30

GND 4 PGND L 1

SW1 29 C BST1

V5A SCK 24 SPI

C V5A 1110 GNDVIN2 MISOMOSI 2322 BUS

SW2 20

R UV22 R UV21 1415 PGNDUDIM2 CSP2BST2 1918 C BST2 L 2

C OUT2 C COMP2 16 COMP2 CSN2 17 R CS2

LED2+

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||RUV12|RUV11 3 4||||
||||||4|
||||CIN1 5|||
|6 7 CV5D 8||||||
|9 CV5A 10 11 12|9|||||
|||||12||
||||CIN2 13|||
||RUV22|14 RUV21 15||14||



**Simplified Schematic**

|PART NUMBER(1)|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|TPS92520-Q1|HTSSOP|8.1 mm × 11 mm|


Copyright © 2021 Texas Instruments Incorporated [An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1) *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 1

intellectual property matters and other important disclaimers. PRODUCTION DATA.

~~Product~~ ~~Folder~~ ~~Links:~~ ~~*[TPS92520](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*~~ *-* ~~*Q1*~~


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
##### **Table of Contents**


**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Revision History** .............................................................. 2
**5 Pin Configuration and Functions** ...................................3
**6 Specifications** .................................................................. 5

6.1 Absolute Maximum Ratings ....................................... 5
6.2 ESD Ratings .............................................................. 5
6.3 Recommended Operating Conditions ........................5
6.4 Thermal Information ...................................................6

6.5 Electrical Characteristics ............................................6
6.6 Typical Characteristics.............................................. 10
**7 Detailed Description** ......................................................14

7.1 Overview................................................................... 14

7.2 Functional Block Diagram......................................... 15
7.3 Feature Description...................................................15
7.4 Device Functional Modes..........................................29

7.5 Programming............................................................ 31


7.6 Register Maps...........................................................36
**8 Application and Implementation** .................................. 56

8.1 Application Information............................................. 56
8.2 Typical Application.................................................... 60
8.3 Initialization Setup.....................................................65
**9 Power Supply Recommendations** ................................66
**10 Layout** ...........................................................................66

10.1 Layout Guidelines................................................... 66
10.2 Layout Example...................................................... 67
**11 Device and Documentation Support** ..........................68

11.1 Documentation Support.......................................... 68
11.2 Receiving Notification of Documentation Updates.. 68
11.3 Support Resources................................................. 68
11.4 Trademarks............................................................. 68
11.5 Glossary.................................................................. 68
**12 Mechanical, Packaging, and Orderable**
**Information** .................................................................... 68

##### **4 Revision History**

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

**Changes from Revision C (June 2020) to Revision D (February 2021)** **Page**

 - Updated the numbering format for tables, figures and cross-references throughout the document...................1

 - Updated the minimum on-time specification from 90-ns typical to 105-ns typical.............................................. 5

 - Added "SWx to PGND (< 10 µs)" row to *Absolute Maximum Ratings* table....................................................... 5

 - Added "CSPx to CSNx (< 100 µs)" row to *Absolute Maximum Ratings* table.....................................................5

 - Updated t ONx(MIN) MIN value from "75" to "87"....................................................................................................5

 - Updated t ONx(MIN) TYP value from "90" to "105"................................................................................................. 5

 - Updated t ONx(MIN) MAX value from "105" to "123".............................................................................................. 5

 - Updated Figure 6-17 ........................................................................................................................................10

 - Updated the *Functional Block Diagram* ........................................................................................................... 15

 - Updated "90 ns" to 105 ns" in *Minimum On-Time, Off-Time, and Inductor Ripple* section...............................17

 - Updated "1.24 V" to "1.22 V" in the *External PWM Dimming and Input Undervoltage Lockout* section........... 19

 - Updated "!~ 220 µA" to "10 µA" in the *External PWM Dimming and Input Undervoltage Lockout* section.......19

 - Updated "2.8 V" to "2.95 V" in the BSTx Undervoltage Lockout description.................................................... 23

 - Updated "2.8 A" to "2.7 A" in the High-Side Switch Current Limit description.................................................. 23

 - Updated "2.5 A" to "1.5 A" in the Low-Side Switch Current Limit description................................................... 23

 - Updated "4 ms" to "3.6 ms" in the *Faults and Diagnostics* section................................................................... 23

 - Updated "32 ms" to "28.8 ms" in the *Faults and Diagnostics* section............................................................... 23

**Chan** **g** **es from Revision B** **(** **May 2020) to Revision C (June 2020)** **Page**

 - Added DAP package.......................................................................................................................................... 1

**Chan** **g** **es from Revision A** **(** **January 2020) to Revision B (May 2020)** **Page**

 - Changed device status from Advance Information to Production Data.............................................................. 1

2 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**
##### **5 Pin Configuration and Functions**


COMP1

UDIM1

PGND

PGND

VIN1

VIN1

GND

V5D

V5A

GND

VIN2

VIN2

PGND

PGND

UDIM2

COMP2



COMP2

UDIM2

PGND

PGND

VIN2

VIN2

GND

V5A

V5D

GND

VIN1

VIN1

PGND

PGND

UDIM1

COMP1


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021


**Figure 5-1. DAD Package 32-Pin HTSSOP (Top-**
**Exposed PAD) Top View**


**Figure 5-2. DAP Package 32-Pin HTSSOP (Top-**
**Exposed PAD) Top View**


**Table 5-1. Pin Functions**

|PIN|Col2|Col3|I/O|DESCRIPTION|
|---|---|---|---|---|
|NAME|NO.||||
||DAD|DAP|||
|BST1|30|19|P|Supply input for high-side MOSFET gate drive circuit. Connect a ceramic capacitor between BSTx and SWx pins. An internal diode is connected between V5D and BSTx.|
|BST2|19|30|P||
|COMP1|1|16|I/O|Output of internal transconductance error amplifier. Connect an integral compensation network to ensure stability.|
|COMP2|16|1|I/O||
|CSN1|32|17|I|Negative input (–) of internal rail-to-rail transconductance error amplifier. Connect directly to the negative node of the LED current sense resistor, R . CS|
|CSN2|17|32|I||
|CSP1|31|18|I|Positive input (+) of internal rail-to-rail transconductance error amplifier. Connect directly to the positive node of the LED current sense resistor, R . CS|
|CSP2|18|31|I||
|FLT|27|22|O|Open-drain fault indicator. Connect to V5D with a resistor to create an active low fault signal output.|
|GND|7, 10|7, 10|G|Signal ground. Return for the internal voltage reference and analog circuits. Connect to circuit ground to complete return path.|
|LHI|26|23|I|Limp-home and standalone mode LED current reference set point. The voltage can be used instead of SPI registers to set LED current. The operation is configured through the LHCFG1 register. Setting voltage below 148 mV disables both channels and setting the voltage above 200 mV enables both channels.|
|MISO|23|26|O|Open-drain SPI slave data output. Connect a 4.7-kΩ resistor to V5D digital supply voltage.|
|MOSI|22|27|I|SPI slave data input|
|PGND|3, 4, 13, 14|3, 4, 13, 14|G|Ground returns for low-side MOSFETs|
|SCK|24|25|I|SPI clock input|
|SSN|25|24|I|SPI chip select input|
|SW1|28, 29|20, 21|P|Switching output of the regulator. Internally connected to both power MOSFETs. Connect to the power inductor.|
|SW2|20, 21|28, 29|P||



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 3

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 5-1. Pin Functions** **(** **continued** **)**

|PIN|Col2|Col3|I/O|DESCRIPTION|
|---|---|---|---|---|
|NAME|NO.||||
||DAD|DAP|||
|UDIM1|2|15|I|Undervoltage lockout and external PWM dimming input. Connect to VIN through a resistor divider to implement input undervoltage protection. Diode couple external PWM signal to enable dimming. Do not float.|
|UDIM2|15|2|I||
|V5A|9|8|P|Analog supply voltage. Locally decouple to GND using a 100-nF to 1-µF ceramic capacitor located close to the controller.|
|V5D|8|9|P|Digital supply voltage. Locally decouple to GND using a 2.2-µF to 4.7-µF ceramic capacitor located close to the controller.|
|VIN1|5, 6|11, 12|P|Power inputs and connections to high-side MOSFET drain node. Connect to the power supply and bypass capacitors C . The path from the VIN pin to high IN frequency bypass C and PGND must be as short as possible. IN|
|VIN2|11, 12|5, 6|P||



4 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**
##### **6 Specifications**
###### **6.1 Absolute Maximum Ratings**

Over o p eratin g free-air tem p erature ran g e ( unless otherwise noted ) [(1)]


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|Supply Voltage|V5A, V5D to GND|–0.3 5.5|V|
|Boot voltage|BSTx to SWx|–0.3 5.5|V|
||BSTx to PGND|–0.3 70|V|
|Switch node voltage|SWx to PGND|–0.5 65|V|
||SWx to PGND (< 10 µs)|–0.75|V|
||SWx to PGND (< 10 ns)|–3.5|V|
|Drain node voltage|VINx to PGND|–0.3 65|V|
|Current|CSNx to VINx (< 10 µs)|1.5|A|
||GND to CSPx, GND to CSNx (< 10 µs)|430|mA|
|Inputs|CSNx - VINx|0.5|V|
||CSPx, CSNx to GND|–0.5 65|V|
||CSPx to CSNx|–0.3 0.3|V|
||CSPx to CSNx (< 100 µs)|–0.5 0.5|V|
||UDIMx to GND|–0.3 60|V|
||COMPx, LHI to GND|–0.3 5.5|V|
||MOSI, SCK, SSN to GND|–0.3 5.5|V|
|Outputs|MISO, FLT to GND|–0.3 5.5|V|
|Junction temperature|T J|150|°C|
|Lead temperature|Soldering, 10 s|260|°C|
|Storage temperature|T stg|–65 150|°C|


(1) Stresses beyond those listed under *Absolute Maximum Rating* may cause permanent damage to the device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under
*Recommended Operating Conditions* . Exposure to absolute-maximum-rated conditions for extended periods may affect device
reliability.

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.
###### **6.3 Recommended Operating Conditions**

Over o p eratin g free-air tem p erature ran g e ( unless otherwise noted )

|6.2 ESD Ratings|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||VALUE|UNIT|
|V (ESD)|Electrostatic discharge|Human body model (HBM), per AEC Q100-002(1)||±2000|V|
|||Charged device model (CDM), per AEC Q100-011|Corner pins (1, 16, 17, and 32)|±750||
||||Other pins|±500||


|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|V IN|Input voltage|4.5 63|V|
|V, V 5A 5D|Bias supply|4.5 5 5.3|V|
|∆V (CSP- CSN)|Sensed inductor current ripple|20|mV|
|dv /dt CSP|CSP slew-rate|5|V/µs|
|I LED|LED current|1.6|A|
|f SW|Switching frequency|100 2200|kHz|
|f UDIM|External PWM dimming frequency|1000|Hz|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 5

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
###### **6.3 Recommended Operating Conditions (continued)**

Over o p eratin g free-air tem p erature ran g e ( unless otherwise noted )

(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
report.
(2) The package thermal impedance is calculated in accordance with JESD51-7 standard with a 4-layer board and 2 W power dissipation.
(3) A heatsink or airflow would yield a much better R θJA . **6.5 Electrical Characteristics**

-40°C ≤ T J ≤ 150°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D =C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx =
100 mΩ, no load on SWx, LHI p in floatin g ( unless otherwise noted )

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|T A|Ambient temperature|–40 125|°C|
|T J|Junction temperature|–40 150|°C|


|6.4 Thermal Information|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|THERMAL METRIC(1)||DEVICE||UNIT|
|||DAD (HTSSOP)|DAP (HTSSOP)||
|||32|32||
|R θJA|Junction-to-ambient thermal resistance(2) (3)|56.7|26.2|°C/W|
|R θJC(top)|Junction-to-case (top) thermal resistance|1.8|16.3|°C/W|
|R θJB|Junction-to-board thermal resistance|28.1|8.3|°C/W|
|Ψ JT|Junction-to-top characterization parameter|1.1|0.2|°C/W|
|Ψ JB|Junction-to-board characterization parameter|27.8|8.2|°C/W|
|R θJC(bot)|Junction-to-case (bottom) thermal resistance|-|1.8|°C/W|


|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|EXTERNAL ANALOG AND GATE DRIVE SUPPLIES (V5D, V5A)|||||
|V V5D,A(UVLO)|V and V UVLO threshold 5D 5A|Rising|4.10 4.26|V|
|||Falling|3.84 4.00|V|
|||Hysteresis|100|mV|
|I V5A(STBY)|Analog supply stand-by current|V = V = 0 V UDIM1 UDIM2|4 5|mA|
|I V5D(STBY)|Gate drive supply stand-by current|V = V = 0 V UDIM1 UDIM2|0.9 1.3|mA|
|I V5A(SLEEP)|Analog supply sleep state current||16 300|nA|
|I V5D(SLEEP)|Gate drive supply sleep state current||17 24|µA|
|I VINx(SLEEP)|VIN pin sleep state current|V = 15 V INx|2 4|μA|
|I V5D(SW)|Gate drive supply switching current|V = 5 V, f = 1 MHz, CH1 V5D SW and CH2 switching|12 20|mA|
|HIGH-SIDE FET (SWx, BOOTx)|||||
|R DSx(ON-HS)|High-side MOSFET on resistance|V = 6 V, V = 11 V, I = INx BSTx HSx 100 mA|227 440|mΩ|
|V BSTx(UV)|Bootstrap UVLO threshold|Falling, V = 6 V, V = 0 V INx SWx|2.60 2.95 3.30|V|
|||Hysteresis, V = 6 V, V = 0 INx SWx V|120 184 250|mV|
|I Q(xBST)|Bootstrap pin quiescent current|V = 5 V, V = 0 V BSTx SWx|200 250 300|µA|
|LOW-SIDE FET (SWx)|||||
|R DSx(ON-LS)|Low-side MOSFET on resistance|V = 6 V, I = 100 mA INx LSx|227 440|mΩ|
|HIGH-SIDE FET CURRENT LIMIT|||||
|I HSx(ILIM)|High-side current limit threshold|V = 6 V INx|2.1 2.7 3.5|A|



6 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
###### **6.5 Electrical Characteristics (continued)**

-40°C ≤ T J ≤ 150°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D =C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx =
100 mΩ, no load on SWx, LHI p in floatin g ( unless otherwise noted )

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|t HSx(LEB)|High-side current sense leading-edge blanking period|V = 6 V INx|35 60 80|ns|
|t HSx(RES)|Current limit response time|V = 6 V INx|20|ns|
|LOW-SIDE FET CURRENT LIMIT|||||
|I LSx(ILIM)|Low-side sinking current limit threshold|V = 6 V INx|1.00 1.50 2.15|A|
|t LSx(LEB)|Low-side current sense leading-edge blanking period|V = 6 V INx|76|ns|
|OSCILLATOR|||||
|f OSC|Oscillator frequency||9.2 10.8 12.4|MHz|
|ANALOG TO DIGITAL CONVERTER (VDD, VIN1, VIN2, VCSN1, VCSN2, LHI, TEMP)|||||
|t CONV|ADC conversion time||18|µs|
|V ADC(FS)|ADC full scale||2.38 2.45 2.52|V|
|q ADC|ADC LSB||2.4|mV|
|ADC INL|Integral nonlinearity||–2 2|LSB|
|ADC DNL|Differential nonlinearity||–2 2|LSB|
|q TEMP|Temperature LSB||1.4|count|
|ADC TEMP|ADC measurement output|T = 25 °C J|414|count|
|||T = 125 °C J|553|count|
|K VINx|VINx sense resistor divider ratio||0.037||
|K V5D|V5D sense resistor divider ratio||0.45||
|K LHI|LHI sense resistor divider ratio||1||
|ANALOG ADJUST SETTING AND CURRENT SENSE AMPLIFIER (CSPx, CSNx)|||||
|V DACx(FS)|DAC full scale||2.38 2.45 2.52|V|
|q DAC|DAC resolution||2.33 2.40 2.47|mV|
|DACx INL|Integral nonlinearity||–1 1|LSB|
|DACx DNL|Differential nonlinearity|CHxADJ stepped (63-64, 127-128, 255-256, 511-512, 1022-1023)|–0.85 0.85|LSB|
|V (CSPx-CSNx)|Current sense threshold|V = 6 V, CSPx ILED_REF_DACx = 1023|167.5 173.0 178.5|mV|
|||V = 6 V, CSPx ILED_REF_DACx = 512|83.0 88.5 94.0|mV|
|||V = 6 V, CSPx ILED_REF_DACx = 192|29.0 34.5 40.0|mV|
|||V = 6 V, CSPx ILED_REF_DACx = 63|6.5 12.5 18.5|mV|
|g mx(LV)|Level shift amplifier transconductance|V = 63 V, V = 5 V INx CSNx|50|µA/V|
|V CSPx(SHT)|Output short circuit detection threshold|Rising|2.65|V|
|||Falling|2.45|V|
|VALLEY CURRENT COMPARATOR (CSPx, CSNx)|||||
|V VALx(OS)|Systematic comparator offset voltage|V < 2.4 V CSNx|17|mV|
|ON-TIME GENERATOR|||||
|t ONx(MIN)|Minimum on-time.|V = 4.5 V INx|87 105 123|ns|
|t ONx|Programmed on-time|V = 50 V, V = 38 V, INx CSPx tonx_DAC = 39|295 375 460|ns|
|||V = 50 V, V = 25 V, INx CSPx tonx_DAC = 7|900 1155 1400|ns|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 7

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
###### **6.5 Electrical Characteristics (continued)**

-40°C ≤ T J ≤ 150°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D =C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx =
100 mΩ, no load on SWx, LHI p in floatin g ( unless otherwise noted )

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|OFF-TIME GENERATOR|||||
|t OFFx(MIN)|Minimum off-time|V = 4.5 V INx|44 57 68|ns|
|PWM DIMMING and PROGRAMMABLE UVLO INPUT (DIMx)|||||
|V UDIMx(EN)|UDIM input threshold|Rising|1.22 1.27|V|
|||Falling|1.075 1.120|V|
|I UDIMx(UVLO)|UDIM source current (UVLO hysteresis)|V = 1.5 V UDIMx|8 10 12|µA|
|ERROR AMPLIFIER (COMPx)|||||
|g M|Transconductance|V = 63 V INx|450|µA/V|
|I COMPx(SRC)|COMPx current source capacity|V = 63 V, V = 0 V, INx (CSPx–CSNx) CHxIADJ = 578|45|µA|
|I COMPx(SINK)|COMPx current sink capacity|V = 63 V, V = 200 INx (CSPx–CSNx) mV, CHxIADJ = 578|45|µA|
|EA x(BW)|Bandwidth|Unity gain|3|MHz|
|EA (VD)|Input differential sense range||–225 225|mV|
|EA (CM)|Input common mode range|V = 63 V INx|0 V – 0.5 INx|V|
|I COMPx(LKG)|COMPx leakage current|V = 0 V UDIMx|2.5|nA|
|V COMPx(ST)|COMPx startup threshold|Rising|2.45|V|
|||Hysteresis|250|mV|
|V COMPx(OV)|COMPx over-voltage detection threshold|Rising|3.0 3.2|V|
|||Hysteresis|60|mV|
|R COMPx(DCH)|COMPx discharge FET resistance||230|Ω|
|V COMPx(RST)|Reset voltage|Falling|100|mV|
|LIMP HOME CURRENT SET POINT (LHI)|||||
|I LHI|Source current|V = 6 V IN|8 10 12|µA|
|V LHI(SD)|Shutdown threshold|Rising, V = 6 V IN|174 200 227|mV|
|||Falling, V = 6 V IN|119 148 176|mV|
|FAULT INDICATOR (FLT)|||||
|R (FLT)|Fault pin pull-down resistance||3 7|Ω|
|T OC|Hiccup retry delay time||3.6|ms|
|SERIAL PERIPHERAL INTERFACE (MOSI, MISO, SCK, SSN)|||||
|V OL-MISO|Output low voltage threshold|I = 10 mA MISO|0.5|V|
|R DS-MISO||I = 10 mA MISO|50|Ω|
|V INPUT(RISE)|Logic threshold (SSN, SCK, MOSI)|Rising|1.8|V|
|V INPUT(FALL)||Falling|0.8|V|
|t SS-SU|SSN setup time|Falling edge of SSN to 1st SCK rising edge|500|ns|
|t SS-H|SSN hold time|Falling edge of 16th SCK to SSN rising edge|250|ns|
|t SS-HI|SSN high time|Time SSN must remain high between transactions|1000|ns|
|t SCK|SCK period|Clock period|500|ns|
|D SCK|SCK duty cycle|Clock duty cycle|40 60|%|
|t SU|MOSI setup time|MOSI valid to rising edge SCK|125|ns|
|t H|MOSI hold time|MOSI valid after rising edge SCK|140|ns|



8 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
###### **6.5 Electrical Characteristics (continued)**

-40°C ≤ T J ≤ 150°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D =C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx =
100 mΩ, no load on SWx, LHI p in floatin g ( unless otherwise noted )

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|t HI_Z|MISO tri-state time|Time to tri-state MISO after SSN rising edge|110 320|ns|
|t MISO_HL|MISO valid high-to-low|Time to place valid "0" on MISO after falling SCK edge|320|ns|
|t MISO_LH|MISO valid low-to-high|Time to tri-state MISO after falling SCK edge|320+t RC|ns|
|t ZO_HL|MISO drive time high-to-low|SSN Falling Edge to MISO falling|320|ns|
|THERMAL SHUTDOWN|||||
|T SD|Thermal shutdown threshold||175|°C|
|T SD(HYS)|Thermal shutdown hysteresis||16|°C|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 9

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
###### **6.6 Typical Characteristics**

T A = T J = 25°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D = C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx = 100
mΩ, no load on SWx, LHI pin floating (unless otherwise noted)

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||||VCSN ICSN|


|Col1|Col2|Col3|Col4|Col5|Col6|1|LED|9 L|ED|
|---|---|---|---|---|---|---|---|---|---|
|||||||3 6|LED LED|12 15|LED LED|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|R|isin|g|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||
||||||||||||||||||F|allin|g|
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||


|174.5 174 (mV) 173.5 Threshold 173 V(CSP-CSN) 172.5 172 171.5 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) V = 3 V CSN Figure 6-1. V Current Sense Threshold vs Temperature (CSP–CSN)|10 7.5 (%) 5 Error 2.5 Threshold 0 -2.5 V(CSP-CSN) -5 -7.5 -10 100 200 300 400 500 600 700 800 900 1000 1100 CHxIADJ Count V = 3 V V = 60 V CSN IN Figure 6-2. V Current Sense Error vs IADJ Count (CSP–CSN)|
|---|---|
|140 120 100 (µA) 80 ICSN 60 Current, 40 20 CSN 0 -20 -40 0 0.25 0.5 0.75 1 1.25 1.5 1.75 2 2.25 2.5 CSN Voltage, VCSN (V) CHxEN = 0, CHxIADJ = 0 0 V < V < 2.5 V CSN Figure 6-3. CSN Source Current vs CSN Voltage|2.25 7 2.2 6 (PA) 2.15 5 (V) Current 2.1 4 Voltage Leakage 2.05 3 VCSN 2 2 ICSN 1.95 VCSN 1 ICSN 1.9 0 0 200 400 600 800 1000 1200 IADJ Count ChxEN = 0 Figure 6-4. CSN Voltage and Leakage Current vs IADJ Count|
|24 1 LED 9 LED 21 3 LED 12 LED (mV) 6 LED 15 LED 18 Pk-Pk 15 Voltage 12 Sense 9 6 Minimum 3 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 Average Inductor Current (A) L = 68 µH V = 60 V IN Figure 6-5. Minimum Ripple Voltage vs Average Inductor Current|4.22 Rising 4.18 Falling (V) 4.14 Threshold 4.1 4.06 POR 4.02 V5A 3.98 V5D, 3.94 3.9 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-6. V POR Threshold vs Temperature 5D,A|



10 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
###### **6.6 Typical Characteristics (continued)**

T A = T J = 25°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D = C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx = 100
mΩ, no load on SWx, LHI pin floating (unless otherwise noted)

|19.8 19.5 19.2 18.9 (µA) 18.6 Current 18.3 18 IV5D(SLEEP) 17.7 17.4 17.1 16.8 16.5 16.2 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-7. V5D Sleep Current vs Temperature|450 (m:) 425 400 Resistance 375 350 325 On 300 MOSFET 275 250 225 High-Side 200 175 150 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-8. High Side MOSFET On Resistance vs Temperature|
|---|---|
|2.965 2.955 (V) 2.945 Threshold 2.935 2.925 UVLO 2.915 2.905 Bootstrap 2.895 2.885 2.875 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-9. Bootstrap UVLO Threshold vs Temperature|220 215 210 (mV) 205 Hysteresis 200 195 190 185 UVLO 180 175 Bootstrap 170 165 160 155 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-10. Bootstrap UVLO Hysteresis vs Temperature|
|3.2 3.1 (A) 3 Threshold 2.9 2.8 Limit 2.7 2.6 Current 2.5 2.4 High-Side 2.3 2.2 2.1 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-11. High-Side Current Limit Threshold vs Temperature|425 (m:) 400 375 Resistance 350 325 300 On 275 MOSFET 250 225 Low-side 200 175 150 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-12. Low-Side MOSFET On Resistance vs Temperature|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 11

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
###### **6.6 Typical Characteristics (continued)**

T A = T J = 25°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D = C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx = 100
mΩ, no load on SWx, LHI pin floating (unless otherwise noted)

|2 (A) Threshold 1.8 1.6 Limit Current 1.4 Sinking 1.2 1 Low-Side 0.8 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-13. Low-Side Sinking Current Limit Threshold vs Temperature|10.875 10.85 10.825 (MHz) 10.8 10.775 Frequency 10.75 10.725 10.7 Oscillator 10.675 10.65 10.625 10.6 10.575 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-14. Oscillator Frequency vs Temperature|
|---|---|
|2.452 2.451 2.45 (V) Scale 2.449 Full 2.448 ADC 2.447 2.446 2.445 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-15. ADC Full Scale vs Temperature|2.452 2.451 2.45 (V) Scale 2.449 Full 2.448 DAC 2.447 2.446 2.445 -40 -20 0 20 40 60 80 100 120 140 160 Temperature Figure 6-16. DAC Full Scale vs Temperature|
|112 111 110 (ns) 109 on-time 108 107 Minimum 106 105 104 103 102 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-17. Minimum On-time vs Temperature|64 62 60 (ns) 58 off-time 56 Minimum 54 52 50 48 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-18. Minimum Off-time vs Temperature|



12 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
###### **6.6 Typical Characteristics (continued)**

T A = T J = 25°C, V 5D = V 5A = 5 V, V IN = 24 V, V UDIMx = 5 V, C V5D = C V5A = 4.7 µF C BSTx = 0.1 µF, C COMPx = 1 nF, R CSx = 100
mΩ, no load on SWx, LHI pin floating (unless otherwise noted)

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|R|isin|g|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||
|||||||||||||||||||F|alli|ng|
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||3 L|EDs|
|||||||||6 L|EDs|
|||||||||9 L 12|EDs LEDs|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
||||||I|LED = 7|50 mA|
||||||I|LED = 1|A|


|1.28 Rising 1.26 Falling 1.24 (V) 1.22 Threshold 1.2 1.18 1.16 Input 1.14 UDIM 1.12 1.1 1.08 1.06 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-19. UDIM Input Threshold vs Temperature|3.24 (V) Threshold 3.23 3.22 Detection 3.21 3.2 Over-voltage 3.19 3.18 3.17 COMP 3.16 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-20. COMP Overvoltage Detection Threshold vs Temperature|
|---|---|
|30 27.5 25 (nA) 22.5 Current 20 17.5 15 Leakage 12.5 10 COMP 7.5 5 2.5 0 -40 -20 0 20 40 60 80 100 120 140 160 Temperature (°C) Figure 6-21. COMP Leakage Current vs Temperature|0.975 0.95 0.925 0.9 (%) 0.875 Efficiency 0.85 0.825 0.8 3 LEDs 6 LEDs 0.775 9 LEDs 12 LEDs 0.75 0 200 400 600 800 1000 1200 1400 1600 1800 LED Current (mA) V = 60 V f = 437 kHz IN SW Figure 6-22. Efficiency vs LED Current|
|0.9675 0.967 0.9665 0.966 0.9655 (%) 0.965 Efficiency 0.9645 0.964 0.9635 0.963 ILED = 750 mA 0.9625 ILED = 1 A 0.962 150 200 250 300 350 400 450 500 550 Switching Frequency (kHz) V = 45 V V = 60 V CSN IN Figure 6-23. Efficiency vs Switching Frequency||



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 13

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
##### **7 Detailed Description**
###### **7.1 Overview**

The TPS92520-Q1 is a dual synchronous buck LED driver with a 4.5-V to 65-V input voltage range. It can deliver
up to 1.6 A of continuous current per channel and power two independent strings of one to 16 series-connected
LEDs. The device implements an adaptive on-time current regulation control technique to achieve fast transient
response. This architecture uses a comparator and a one-shot on-timer that varies inversely with input and
output voltage to maintain a near-constant frequency. The integrated low offset rail-to-rail error amplifier enables
closed-loop regulation of LED current and ensures better than 4% accuracy over a wide input, output, and
temperature range.

The LED current reference is set by the 10-bit IADJ DAC and is programmed by the CHxIADJ register to achieve
over a 16:1 linear analog dimming range. Pulse width modulation (PWM) dimming of the LED current is achieved
by either programming the internal PWM generator or by modulating the duty cycle of external voltage signal at
UDIMx input. When enabled, the internal PWM generator sets the LED current duty cycle based on the 10-bit
CHxPWM command. The external UDIMx input acts as an enable and directly controls the LED current. This
device optimizes the inductor current response and is capable of achieving over a 1000:1 PWM dimming ratio.

The device incorporates an enhanced programmable fault feature including the following:

 - Cycle-by-cycle switch overcurrent limit

 - Input undervoltage protection

 - Boot undervoltage protection

 - Comp overvoltage warning

 - Thermal warning

 - LED short circuit indication

In addition, thermal shutdown (TSD) protection is implemented to limit the junction temperature at 175°C
(typical). For each fault, there is an associated fault read-bit in the status registers that can be easily accessed
via SPI read commands.

The TPS92520-Q1 includes a communication watchdog timer that enables standalone and limp-home (LH)
function. When enabled, the watchdog timer monitors the SPI communication during start-up and normal
operation. Communication failure at start-up forces the device in stand-alone mode operation. In this mode, the
operation of each channel is controlled by UDIMx and LHI inputs while the SPI communication is disabled. Limphome (LH) mode is activated on detection of communication failure during normal operation. In LH mode, the
device operation is controlled by the limp-home registers that are initialized and loaded during the device start-up

sequence.

14 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
###### **7.2 Functional Block Diagram**

UDIM1

CSP1

CSN1

SSN

VIN2

SW2

CSP2

CSN2

|Col1|UVLO por clk_m + Rising: 4.1 V Oscillator BST Falling: 4.0 V uvlo UVLO Hys: 100 mV Digital Supply ch1_en Analog Supply slp_o LEB bstuv1 VBG Switch slp_o Bandgap VIN1 lsilim1 2VBG Control HS Current V5A slp_o Sleep Enable hsilim1 and Limit Thermal Switch + Circuit Sensor Fault VBST(UV) – Logic VLHI + V5A LS Current Limit VBG pwm1 Circuit + V5D LEB ch1_en UVLO & On Time VIN1 PWM ton1 INPUT ton1 Control VIN1 udim1 bstuv1 Valley Current 2VBG Control lsilim1 Toffmin1 hsilim1 V-I Converter 5 V toffmin1 VIADJ1 VCSN1 Logic + + IO iadj1 DAC VIADJ1 PWM IADJ1 open1 LED Fault short1 Detection adc_sel VIN1 VIN2 fault Digital Logic adcout VCSN1 Channel 1 VCSN2 ADC V5D VLHI fpin ch2_en VTMP open2 ton2 open1 short2 short1 udim2 open2 bstuv2 Channel 2 short2 lsilim2 uvlo por hsilim2 slp toffmin2 ts1 ts2 iadj2 DAC VIADJ2 IADJ2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
||||| **7.3 Feature Description**

**7.3.1 Buck Converter Switching Operation**

The following operating description of the TPS92520-Q1 refers to the *Functional Block Diagram* and the
waveforms in Figure 7-1. The main control loop of the TPS92520-Q1 is based on an adaptive on-time pulse
width modulation (PWM) technique that combines a constant on-time control with an inductor valley current
sense circuit for pseudo-fixed frequency operation. This proprietary control technique enables closed-loop
regulation of LED current and fast dynamic response necessary to meet the requirements for LED pixel control
and LED matrix beam applications.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 15

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

V (CSP-CSN)

V VAL

|N)|Col2|
|---|---|
|) S L|VIN LVCSNuRCS VC LSNuRCS|
|||
|||



V SW

V IN

t ON t OFF t SW

|W|Col2|Col3|
|---|---|---|
|W N 0|||
||||
||||



**Figure 7-1. Adaptive On Time Control Buck Converter Waveforms**

In steady state, the high-side MOSFET is turned on at the beginning of each cycle. The on-time duration of this
MOSFET is controlled by an internal one-shot timer and the high-side MOSFET is turned off after the timer
expires. The one-shot timer duration is set by the output voltage measured at the CSP pin, V CSP, and the input
voltage measured at the VIN pin, V IN, to maintain a pseudo-fixed frequency. During the on-time interval, the
inductor current increases with a slope proportional to the voltage applied across its terminals (V IN – V CSP ).

The low-side MOSFET is turned on after a fixed deadtime and the inductor current then decreases with the

constant slope proportional to the output voltage, V CSP . Inductor current measured by the external sense resistor
is compared to the valley threshold, V VAL, by an internal high-speed comparator. This MOSFET is turned off and
the one-shot timer is initiated when the sensed inductor current falls below the valley threshold voltage. The
high-side MOSFET is turned on again after a fixed deadtime.

The internal rail-to-rail error amplifier sets the valley threshold voltage and regulates the average inductor current
based on a reference value set by CHxIADJ-DAC. A simple integral loop compensation circuit consisting of a
capacitor connected from the COMP pin to GND provides a stable and high-bandwidth response. As the inductor
current is directly sensed by an external resistor, the device operation is not sensitive to the ESR of the output
capacitors and is compatible with common multi-layered ceramic capacitors (MLCC).

**7.3.2 Switching Frequency and Adaptive On-Time Control**

The TPS92520-Q1 uses an adaptive on-time control scheme and does not have a dedicated on-board oscillator.
The one-shot timer incorporates a 6-bit current steering DAC and is programmed by the CHxTON registers. The
on-time is calculated internally using Equation 1 and is inversely proportional to the measured input voltage, V IN,
and proportional to the measured CSP voltage, V CSP .

�8 �6
##### 4 10u u CHxTON 5 : 0 > @ � 18 10u V CSP

t ON u CHxTON 5 : 0 > @ � 1 V IN (1)

Given the duty ratio of the buck converter is V CSP / V IN, the switching period, T SW, remains nearly constant over
all operating points. Use Equation 2 to calculate the switching period.

�8 �6 V IN 4 10u u CHxTON 5 : 0 > @ � 18 10u

T SW t ON u V CSP CHxTON 5 : 0 > @ � 1 (2)

Use Equation 3 to calculate the switching frequency.

16 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

##### CHxTON 5 : 0 > @ � 1

f SW �8 �6 4 10u u CHxTON 5 : 0 > @ � 18 10u (3)

TI recommends a switching frequency setting between 110 kHz and 2.2 MHz, corresponding to a decimal value
of the CHxTON register ranging from 1 to 43.

**7.3.3 Minimum On-Time, Off-Time, and Inductor Ripple**

Buck converter operation is impacted by minimum on-time, minimum off-time, and minimum peak-to-peak
inductor ripple limitations. The converter reaches the minimum on-time of 105 ns (typ) when operating with high
input voltage and low-output voltage. In this control scheme, the off-time continues to increase and the switching
frequency reduces to regulate the inductor current and LED current to the desired value.

V

OUT(MIN)

f SW(MIN) ; t ON t ON(MIN)
t u V

ON(MIN) IN(MAX) (4)

The converter reaches the minimum off-time of 57 ns (typ) when operating in dropout (low input voltage and high
output voltage). As the on-time and off-time are fixed, the duty cycle is constant and the buck converter operates
in open-loop mode. The inductor current and LED current are not in regulation. The CHxTOFFMIN bit is set to
indicate operation at maximum duty cycle. The converter continues to switch unless disabled by resetting the
CHxEN bit. Upon detection of a minimum off-time operation, the device disables the error amplifier and
disconnects the COMP pin to maintain charge on the compensation network. This ensures fast response with
minimum LED current overshoot as the converter recovers from dropout condition.

The behavior and response of valley comparator is dependent on sensed peak-to-peak voltage ripple,
ΔV (CSP-CSN), and is a function of current sense resistor, R CS, and peak-to-peak inductor current ripple, Δi L(PK-PK) .
To ensure periodic switching, the sensed peak-to-peak ripple needs to exceed the minimum value, specified in
Figure 6-5. At high (near 100%) or low (near 0%) duty cycles, the inductor current ripple may not be sufficient to
ensure periodic switching. Under such operating conditions, the converter transitions from periodic switching to a
burst sequence, forcing multiple on-time and off-time cycles at a rate higher than the programmed frequency.
Although the converter may not operate in a periodic manner, the closed-loop control continues regulating the
average LED current with a larger ripple value corresponding to higher peak-to-peak inductor ripple. TI
recommends choosing an inductor, output capacitor, and switching frequency to ensure minimum sensed peakto-peak ripple voltage under nominal operating condition is greater than 20 mV. The *Application and*
*Implementation* section summarizes the detailed design procedure.

**7.3.4 LED Current Regulation and Error Amplifier**

The reference voltage, V IADJ, set by the 10-bit CHxIADJ-DAC, is internally scaled by a gain factor of 1/14 via a
resistor network. An internal rail-to-rail error amplifier generates an error signal proportional to the difference
between the scaled reference voltage (V IADJ / 14) and the inductor current measured by the differential voltage
drop between CSP and CSN, V (CSP-CSN) . This error drives the COMP pin voltage, V COMP, and directly controls
the valley threshold of the inductor current. Zero average DC error and closed-loop regulation is achieved by
implementing an integral compensation network consisting of a capacitor connected from the output of the error
amplifier to GND. As a good starting point, TI recommends a capacitor value between 1 nF and 10 nF between
the COMP pin and GND. The choice of compensation network must ensure a minimum of 60° of phase margin
and 10 dB of gain margin. The *Application and Implementation* section summarizes the detailed design
procedure.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 17

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

CSP1

CSN1

COMP1

V-I Converter

IADJ1 0 V to 2.45 V +

140k

**Figure 7-2. Closed-loop LED Current Regulation**

|Col1|Valley Current Control|Col3|Col4|
|---|---|---|---|



LED current is dependent on the current sense resistor, R CS . Use Equation 5 to calculate the LED current.
##### V � CSP CSN� � V IADJ V DAC(FS) CHxIADJ 9 : 0 > @

I LED u
R CS 14 u R CS 1024 14 u R CS (5)

LED current accuracy is a function of the tolerance of the external sense resistor, R CS, and the variation in the
sense threshold, V (CSP-CSN), caused by internal mismatch and temperature dependency of the analog
components. The TPS92520-Q1 incorporates low offset rail-to-rail amplifiers, and is capable of achieving LED
current accuracy of ±4% over common-mode range and a junction temperature range of –40°C to 150°C. The
internal offset of the device can be measured and compensated using the lower LSBs of the 10-bit CHxIADJDAC. Therefore, the error can be further reduced and the LED current accuracy can be improved to be better
than ±3%.

**7.3.5 Start-up Sequence**

The start-up circuit allows the COMP pin voltage to gradually increase, thus reducing the LED current overshoot
and current surges. The switching operation is initiated after the COMP pin voltage exceeds 2.45 V. A 250-mV
hysteresis window allows the device to operate when COMP voltage is within the expected operating range of
2.2 V to 2.7 V. Switching is disabled on detection of low COMP voltage to avoid excessive negative inductor
current.

18 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


V COMP

2.45

V SW

V IN


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

t


t

|N 0|Col2|Col3|Col4|
|---|---|---|---|



I LED

t

**Figure 7-3. Soft-Start Sequence**

The duration of soft start, t ss, depends on the size of the compensation capacitor and the error amplifier source
current, I COMP(SRC) .


t SS 2.45 u C COMP
I

COMP(SRC)


(6)


The source current, I COMP(SRC) is a function of the transconductance, g M, of the error amplifier and error
generated between the reference and the current sensed voltage.

I COMP(SRC) g M u §¨ V IADJ � V (CSP CSN)�    © 14 ¹ (7)

With no current flowing through the LEDs, the soft start duration depends on the choice of compensation
capacitor, C COMP, and the reference voltage, V IADJ .

The CHxCOMPOV bit in the STATUS1 register is set when the COMP voltage deviates from the nominal range
and exceeds 3.2 V. This indicates a fault condition where the converter is operating in open-loop and the LED
current is out of regulation. The corresponding channel can be disabled by resetting the CHxEN bit via a SPI
command or controlling the UDIMx input.

**7.3.6 Analog Dimming and Forced Continuous Conduction Mode**

Analog dimming is accomplished by the SPI interface through the adjustment of the 10-bit CHxIADJ registers.
The TPS92520-Q1 improves the linear range of analog dimming by supporting forced continuous conduction
mode of operation. With synchronous MOSFETs, the inductor current is allowed to go negative for part of the
switching cycle, thus enabling linear dimming with over 16:1 dimming range.

**7.3.7 External PWM Dimming and Input Undervoltage Lockout (UVLO)**

The UDIM pin is a dual-function input that features an accurate 1.22-V threshold with programmable hysteresis
as shown in Figure 7-4. This pin functions as both the external PWM dimming input for the LEDs and as a VIN
UVLO. When the rising pin voltage exceeds the 1.22-V threshold, 10 µA (typical) of current is driven out of the
UDIM pin into the resistor divider providing programmable hysteresis.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 19

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

Standard

PWM

VIN

R UVH UDIM

R UV1

PWM

**Figure 7-4. External PWM Dimming**

The brightness of LEDs can be varied by modulating the duty cycle of the signal directly connected to the UDIM
input. In addition, either an n-channel MOSFET or a Schottky diode can be used to couple an external PWM
signal when using UDIM input in conjunction with UVLO functionality. With an n-channel MOSFET, the
brightness is proportional to the negative duty cycle of the external PWM signal. With an Schottky diode, the
brightness is proportional to the positive duty cycle of the external PWM signal.

When using the UDIM pin for UVLO and PWM dimming concurrently, the UVLO circuit can have an extra resistor
to set the hysteresis. This allows the standard resistor divider to have smaller values, minimizing PWM delays. TI
recommends at least 1 V of hysteresis when PWM dimming if you are operating near the UVLO threshold. Use
Equation 8 to define the rising threshold.


R UV1 � R UV2
V V u

IN(RISE) UDIM(RISE)

R UV1

Use Equation 9 to define the hysteresis.

UVLO only:


(8)


V HYS I UDIM(UVLO) u R UV2 (9)

PWM and UVLO:
##### § R UVH u � R UV1 � R UV2 � ·

V HYS I UDIM(UVLO) u ¨¨©R UV2 � R UV1 ¸¸¹ (10)

**7.3.8 Internal PWM Dimming**

The TPS92520-Q1 incorporates an internal 10-bit counter to independently configure PWM dimming for each
channel. To use the internal PWM, set the CHxINTPWM bit in the SYSCFG1 register. The duty cycle of the
internal PWM can be set using a 10-bit value in the CHxPWML and CHxPWMH registers. Since CHxPWM is a
10-bit value, a PWM duty cycle update can require two SPI writes, one to the CHxPWMH and another to the
CHxPWML register. In order to prevent transferring unintentional values, the contents of the two registers are
only transferred to the CHxPWM counter upon the write to the CHxPWML register. Therefore, to update the
PWM duty cycle, it is required to write a value to the CHxPWMH first, and in a consecutive command, write a
value to the CHxPWML register. In addition, to avoid corrupting the progress of the current PWM duty cycle, the
update from the CHxPWM register to the CHxPWM counter occurs two PWM CLK counts before the end of each
PWM period (at the count of 1022).

The clock to the 10-bit PWM counter is set by a 3-bit value in the PWMDIV register. Equation 11 and Equation
12 show the relationship between the PWM CLK and PWM frequency with a 10.8-MHz oscillator, CLK M .

20 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**

PWM CLK CLK M
PWM DIV

PWM PWM CLK
FREQ
1024


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

(11)

(12)


For example, a PWMDIV[2:0] register setting of decimal value 5 sets the division ratio to 24 and results in a
PWM frequency of 439 Hz. Refer to *Section 7.6.3.7* for more details.

The device can be controlled through the input of the UDIM independent of the internal PWM setting. The signal
at the UDIM input is ANDed with the internal PWM to generate a combined output which controls the switching
operation. Therefore, each channel can be independently disabled based on the external UDIM signal, even
when the device is configured to operate based on internal PWM settings.

**7.3.9 Shunt FET Dimming or Matrix Beam Application**

V CSN

V LED12

V LED1

|N 2 1|Col2|
|---|---|
|||



V (CSP-CSN)

V VAL

|t|Col2|
|---|---|
|) L 0||
|||
|||



**Figure 7-5. Shunt FET Dimming Transient Response**

The TPS92520-Q1 is compatible with shunt FET dimming and LED Matrix Manager devices. The fast dynamic
response and adaptive on-time control topology ensure near ideal current source behavior with minimum
inductor current overshoot or undershoot. In contrast to constant off-time control, the control loop is able to
maintain LED current regulation under shorted output condition. The off-time of the converter naturally adapts to
the inductor slope and valley command while keeping the average LED current constant. Figure 7-5 shows the
shunt-FET dimming transient with all LEDs switched from on to off.

The device behavior is impacted by the falling slew-rate of CSN node, V CSN . A large slew-rate in conjunction
with the parasitic capacitances from CSP and CSN to GND results in differential voltage forcing the converter to
burst with minimum on-time and minimum off-time. To avoid switch node bursting TI recommends a maximum
slew-rate (dv/dt) of 5 V/µs.

**7.3.10 Bias Supply**

The device is powered by an external 5-V supply connected to V5D and V5A pins. Operation is enabled when
V5D and V5A exceed the 4.1-V (typ) rising threshold and is disabled when either V5D or V5A drops below the 4V (typ) falling threshold. The comparator provides 100-mV of hysteresis to avoid chatter during transitions. The
V5D supply powers the internal digital logic, a 10.8-MHz oscillator, and the high-side and low-side gate driver
circuits. The V5A supply powers the analog-to-digital converter (ADC), the digital-to-analog converters (DACs),
and the sensitive analog circuits. The two bias pins can be connected together on the PCB or through a series
10-Ω resistor between V5D and V5A with 5-V external supply connected directly to the V5D pin. TI recommends
a capacitor from each pin to GND . The recommended range for the bypass capacitor from V5D pin to ground is
between 1 µF and 4.7 µF. The recommended range from the V5A pin to ground is between 100 nF and 1 µF.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 21

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

The bypass capacitor from V5D to GND must be 10 times larger than the bootstrap capacitor, C BST, to support
proper operation during PWM dimming. The voltage on V5D and V5A must never exceed 5.5 V.

The power cycle (PC) bit indicates a fault condition when both V5D and V5A are below the 4 V. At power up, the
PC bit is set and must be cleared before enabling the operation of individual channels. Reading the STATUS3
register clears the PC bit.

In device sleep state, the V5A input is internally disconnected to reduce power consumption. As the internal
voltage drops below the 4-V threshold, the V5AUV bit is set in the STATUS3 register to indicate bias
undervoltage condition. The fault clears when the device is programmed to exit the sleep state and assumes
normal operation. See the *Device Functional Modes* section for more details.

**7.3.11 Bootstrap Supply**

The TPS92520-Q1 contains both high-side and low-side N-channel MOSFETs. The high-side gate driver works
in conjunction with an internal bootstrap diode and an external bootstrap capacitor, C BST . During the on-time of
the low-side MOSFET, the SW pin voltage is approximately 0 V and C BST is charged from the V5D supply
through the internal diode. TI recommends a 0.1-µF to 1-µF capacitor connected with short traces between the
BST and SW pins. A larger capacitor is required to prevent a bootstrap undervoltage fault when operating at low
PWM dimming frequencies.

**7.3.12 ADC**

The TPS92520-Q1 incorporates a 10-bit successive approximation register (SAR) ADC. The single ADC is
multiplexed to sample the following signals:

 - VINx

 - CSNx

 - V5D

 - LHI

 - Internal temperature sensor nodes

The SAR ADC sampling and conversion require 18 µs typical. Priority is given to CSNx inputs to ensure
accurate output voltage measurement when operating at low PWM duty cycles. The ADC scheduler samples
CSN1 and CSN2 inputs four times consecutively followed by other input parameters. The complete round-robin
sampling sequence is illustrated in Figure 7-6.

**Figure 7-6. ADC Sampling Sequence**

|1|2|3|4|5|6|7|8|9|10|11 18|19|20 27|28|29 36|37|38 45|46|47|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VIN1|CSN1|CSN2|CSN1|CSN2|CSN1|CSN2|CSN1|CSN2|V5D|CSN1 CSN2|VIN2|CSN1 CSN2|LHI|CSN1 CSN2|TEMP|CSN1 CSN2|VIN1|CSN1|



The CSN1 and CSN2 inputs are sampled at an interval of 36 µs with an additional delay occurring every 9 [th]

sample. All other parameters are sampled at a rate of 810 µs. For example, VIN1 input is sampled after 45 ADC
conversion cycles. The round robin sampling scheme ensures an adequate sampling speed to allow for very fast
failure detection without data link loss, even when PWM dimming.

***7.3.12.1 Input Voltage Measurement: VINx***

The VINx ADC input is a measurement of the V INx pin voltage. The VINx pin voltage is internally attenuated by
0.037 to achieve an 8-bit conversion ratio of 65/255 (V/dec). The CHxVIN register is updated based on the 8
MSBs of ADC conversion. The last 2 LSBs are ignored. The contents of the register provide diagnostics of input
power supply or, in many applications, the pre-regulator boost converter output voltage.

22 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

***7.3.12.2 LED Voltage Measurement: CSNx***

The ADC updates the CHxVLED register every time after sampling the CSNx input. The CSNx pin voltage is
internally attenuated by 0.037 to achieve an 8-bit conversion ratio of 65/255 (V/dec). Since the sampling interval
is asynchronous to the PWM operation, the logic incorporates two additional registers, CHxVLEDON and
CHxVLEDOFF, to save the output voltage information based on the PWM operation. The contents of the
CHxVLED register are copied to CHxVLEDON on the falling edge of the PWM signal to record the CSNx voltage
when the PWM input was high. Similarly, the CHxVLED register is copied to CHxVLEDOFF on the rising edge of
the PWM signal to record the CSNx voltage when the PWM input was low. This ensures the most consistent
LED voltage reading during PWM operation.

***7.3.12.3 Bias Supply Measurement: V5D***

The V5D pin measurement indicates the status of the external bias converter. The V5D pin voltage is internally
attenuated by 0.45 to achieve an 8-bit conversion ratio of 5.33/255 (V/dec).

***7.3.12.4 External Limp-Home Input Measurement: LHI***

The ADC monitors the LHI pin and sets the internal current reference in limp-home mode. The LHI input voltage
is digitized to achieve a 10-bit reference with resolution of 2.45/1023 (V/dec). The LHIL and LHIH registers are
updated based on the ADC output.

***7.3.12.5 Junction Temperature Measurement: TEMP***

The combined TEMPL and TEMPH register values represent the 10-bit junction temperature measurement with
a resolution of 1°C/LSB. The register is only updated when TEMPL is read. Therefore, TEMPL must be read first
followed by TEMPH to read the junction temperature. Use Equation 13 to calculate the junction temperature.

T J 0.7168 u TEMP[9 : 0] � 271.51 (13)

**7.3.13 Faults and Diagnostics**

Table 7-1 summarizes the device behavior under fault conditions.

**Table 7-1. Fault Descri** **p** **tion**

|FAULT|DETECTION|DESCRIPTION|
|---|---|---|
|Thermal Warning|T > T J J(LMT)|Thermal warning (TW) bit is set in the STATUS3 register when the junction temperature exceeds the threshold programmed by TWLMT[9:2].|
|Thermal Protection|T > 175°C J|Each channel is protected by an individual thermal sensor located close to the switching MOSFETs. The thermal protection is activated in the event the maximum MOSFET temperature exceeds the typical value of 175°C. The corresponding channel is forced into shutdown mode and the CHxTS bit is set in the STATUS2 register. This feature is designed to prevent overheating and damage to the internal switching MOSFETs.|
|SPI Error|—|A communication error is indicated by the SPE bit and it is set high. The device enters stand-alone mode or LIMP-HOME mode of operation when the watchdog timer duration expires (CMWTAP register) and the watchdog timeout event counter (CMWTO[1:0] in the STATUS3 register).|
|V5D Undervoltage Lockout|V < 4.1 V 5D(RISE)|The device enters the undervoltage lockout (UVLO). The switching operation is disabled, the COMP capacitor is discharged, and the digital logic is reset to default values. The power cycle (PC) bit is set in the STATUS3 register.|
||V > 4 V 5D(FALL)||
|V5A Undervoltage Lockout|V < 4.1 V 5A(RISE)|In SLEEP mode, the internal V5A node is disconnected to reduce the current consumption. The switching operation is disabled and the COMP capacitor is discharged. The V5AUV bit is set in the STATUS3 register.|
||V > 4 V 5A(FALL)||
|VINx Undervoltage Lockout|V < 1.12 V UDIMx|The device disables switching operation for the corresponding channel. Switching is enabled when the input voltage rises above the turnon threshold, V . IN(RISE)|
|BSTx Undervoltage Lockout|V > 3.14V BSTx(RISE)|The device turns off the high-side MOSFET and turns on the low-side MOSFET for the corresponding channel. The CHxBSTUV bit is set in the STATUS2 register. Normal switching operation is resumed once the bootstrap voltage exceeds 2.95 V.|
||V < 2.95 V BSTx(FALL)||
|COMPx Overvoltage|V > 3.2 V COMPx|The CHxCOMPOV bit in the STATUS1 register is set to indicate that the COMP voltage exceeded the normal operating range. This information is provided for device diagnostics.|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 23

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-1. Fault Descri** **p** **tion** **(** **continued** **)**

All the faults and diagnostics features, except V 5D UVLO and V INx UVLO, have an associated Fault-Read bit in

|FAULT|DETECTION|DESCRIPTION|
|---|---|---|
|Short CHx Output|V < 2.45 V CSNx|The CHxSHORT bit is set in the STATUS1 register to indicate an output short circuit condition based on sensed CSNx voltage.|
|High-Side Switch Current Limit|I > 2.7 A HS|The device turns off the high-side MOSFET and discharges the COMP capacitor when the drain current exceeds 2.7 A typical. The low-side switch is turned on to discharge the inductor and output capacitor. The CHxHSILIM bit is set in the STATUS1 register. The fault recovery is based on the device configuration.|
|Low-Side Switch Current Limit|I > 1.5 A LS|The device turns off both high-side and low-side MOSFETs and discharges the COMP capacitor when the drain current exceeds 1.5 A typical. The CHxLSILIM bit is set in the STATUS1 register. The fault recovery is based on the device configuration.|
|Minimum Off-Time|—|The CHxTOFFMIN bit is set in the STATUS2 register when the corresponding channel reaches the maximum possible duty cycle. This usually occurs during dropout condition or PWM dimming operation. The compensation network is disconnected from the output of the error amplifier to prevent COMP voltage from exceeding the normal operating range. Normal operation is resumed once the off-time increases above the minimum limit.|

the STATUS1, STATUS2, and STATUS3 registers. Upon occurrence of a fault, the associated Fault-Read bit is
set in the register map. Reading these registers clears the bits if the condition no longer exists. The clearing of
the Fault-Read bits happens at the end of the SPI transfer read response, not at the end of the read command.

The TPS92520-Q1 can be configured to auto-restart or latch-off on detection of the thermal shutdown, high-side,
or low-side current limit faults. The device enters the latched-off state when the bit associated with the fault and
channel is set high in the SYSCFG2 register. This forces the device to disable the channel and remain off upon
the detection of the fault condition. The channel can be turned back on by clearing the fault bit in STATUS1 and
by re-setting the CHxEN bit in the SYSCFG1 register.

If the fault is configured as non-latched (the CHxTS, CHxHSILIMFL, or CHxLSILIMFL bit is set to 0 in the
SYSCFG2 register), a restart sequence is initiated to attempt recovery from the fault condition. In the case of
thermal shutdown fault, the restart is initiated after the MOSFET temperature decreases by the fixed hysteresis
of 10°C. A soft-start sequence is initiated and switching operation is enabled. For a high-side or low-side current
limit fault, a fixed timer is initiated on detection of the fault. The fault timer is programmable with a range of 3.6
ms to 28.8 ms by IFT[1:0] bits in SYSCFG2 register. A restart is initiated by the expiration of the fault timer and
switching operation is enabled.

The TPS92520-Q1 logic has a communication watchdog timer that is based on the system clock (CLK). The
watchdog timer is enabled by default upon power-up (the CMWEN bit is set to 1 in the SYSCFG1 register). The
communications watchdog timer tap point is programmed by writing the desired value to the CMWTAP register.

The tap point defines the timing of the communication watchdog timer (a 25-bit counter). By default, the tap point
is set to bit 24 corresponding to 1.67 s of duration. The communication watchdog monitors the status of SPI bus
and defines the device operation in case of SPI communication error (SPE bit set to 1). See the *Device*
*Functional Modes* for more details.

The high-side current limit, low-side current limit, and thermal protection faults force the FLT pin low when biased
through an external resistor and connected to a 5-V supply. The FLT output can be used in conjunction with a
microcontroller or system basis chip (SBC) as an interru p t and can be used to aid in fault diagnostics. Setting the
FPINRST bit to one in SYSCFG1 register resets the FLT pin out when no active faults are detected by the
device.

**Table 7-2. Faults and Dia** **g** **nostics Summar** **y**

|LIST|DESCRIPTION|FAULT OR DIAGNOSTIC|FAULT READ BIT|ENABLE FAULT TIMER|FLT INDICATION|ENABLE LATCH|
|---|---|---|---|---|---|---|
|TW|Thermal Warning|Diagnostics|Yes|No|No|No|
|CHxTP|Thermal Protection|Fault|Yes|No|Yes|Yes|
|VINx (UVLO)|VIN Supply Undervoltage Lockout|Fault|No|No|No|No|



24 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-2. Faults and Dia** **g** **nostics Summar** **y** **(** **continued** **)**

|LIST|DESCRIPTION|FAULT OR DIAGNOSTIC|FAULT READ BIT|ENABLE FAULT TIMER|FLT INDICATION|ENABLE LATCH|
|---|---|---|---|---|---|---|
|CHxBSTUV|BST Supply Undervoltage Lockout|Fault|Yes|No|No|No|
|CHxCOMPOV|COMP Overvoltage|Diagnostics|Yes|No|No|No|
|CHxSHORT|Short Circuit Detected|Diagnostics|Yes|No|No|No|
|CHxHSILIM|High-side Current Limit|Fault|Yes|Yes|Yes|Yes|
|CHxLSILIM|Low-side Current Limit|Fault|Yes|Yes|Yes|Yes|
|CHxTOFFMIN|Minimum Off Time|Diagnostics|Yes|No|No|No|
|V5AUV|V5A Undervoltage|Diagnostics|Yes|No|No|No|
|PC|Power On Reset (Power Cycle)|Fault|Yes|No|Yes|Yes|
|SPE|SPI Communication Error|Diagnostics|Yes|No|No|No|
|LHSW|Limp-Home Mode (Communication Error)|Fault|Yes|No|No|No|


**7.3.14 Output Short Circuit Fault**

The TPS92520-Q1 monitors the CSNx voltage to detect output short circuit faults. A short failure is indicated
when the CSNx voltage drops below 2.45 V. The corresponding CHxSHORT bit is set in the STATUS1 register.
The device continues to regulate current and operate without interruption in case of short circuit. The
microcontroller can detect short circuit either by reading the STATUS1 register or by reading the CSNx voltage
measured by the ADC (CHxVLED register). Upon detection of a short, the microcontroller is required to take
action by writing to SYSCFG1 register via SPI. A short circuit fault in standalone mode or limp-home mode does
not impact the device behavior. The device continues to operate and regulate current without interruption.

**Figure 7-7. Cable harness parasitic inductance**

|Col1|CSNx CSPx VINx L R PAR SWx CS LED+ t SH C OUT L PAR PGNDx /('Å|
|---|---|



The voltage transient imposed on CSPx and CSNx inputs during short circuit is dependent on the output
capacitance and is influenced by the cable harness impedance. The inductance associated with a long cable
harness resonates with the charge stored on the output capacitor and forces CSPx and CSNx voltage to ring
below ground. The negative voltage and current are dependent on the parasitic cable harness inductance and
resistance.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 25

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Figure 7-8. Short Circuit Fault Transient Behavior**

|CSN LED 0|t SH t|
|---|---|
|||



When using a long cable harness, a diode is recommended to clamp the negative voltage across CSPx and
CSNx input, as shown in Figure 7-9. TI recommends a low forward voltage Schottky diode or a fast recovery
silicon diode with reverse blocking voltage rating greater than the maximum output voltage. The diode is required
to be placed close to the output capacitor and should ensure that the current flowing through CSP and CSN
nodes under negative transient condition is below the absolute maximum rating of the device.

|Col1|VINx SWx LED+ C D OUT RP PGNDx /('Å|
|---|---|



**Figure 7-9. CSP and CSN Transient Protection Using an External Diode**

**7.3.15 Output Open Circuit Fault**

An LED open circuit fault ultimately causes the output voltage to increase and settle close to the input voltage.
When this occurs, the TPS92520-Q1 switching operation is then controlled by the fixed on-time and minimum
off-time resulting in a duty cycle close to 100%. However during open circuit, the dynamic behavior of the device
and buck converter is influenced by the input voltage, V IN, and the output capacitor, C OUT, value. The device
response to open circuit can be categorized into the following three distinct cases.

Case 1: For a Buck converter design with a small output capacitor, the switching operation in open load
condition excites the inductor and the output capacitor resonance, forcing the output voltage to oscillate. The
frequency and amplitude of the oscillation are based on the resonant frequency and Q-factor of the tank. The
open-circuit is detected by checking the CHxCOMPOV, CHxTOFFMIN bits in STATUS1 and STATUS2 registers
and by polling the CHxVLED register to verify the output voltage measured by internal ADC.

26 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


V CSN

V IN

V COMPx(OV)


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

t

|OMP|tOC t|
|---|---|
|x(OV)||
|||


**Figure 7-10. Open Circuit Condition with Output Voltage Oscillation**

Case 2: For a buck converter design with larger output capacitor, the inductor Q-factor and resonant frequency
are much lower than the switching frequency. In this case, output voltage rises to input voltage and the converter
continues to switch with minimum off-time. The open-circuit fault is detected by checking the CHxTOFFMIN bit in
STATUS2 register and by polling the CHxVLED register to verify the output voltage measured by internal ADC.

V CSN

V IN

t

**Figure 7-11. Open circuit Condition with Minimum Off-time Operation**

Case 3: When operating at higher input voltage, the larger gate-to-drain charge depletes the bootstrap capacitor
and triggers bootstrap UVLO protection. When bootstrap voltage is below 2.95 V, undervoltage protection is
triggered. Due to insufficient gate drive supply, the high-side MOSFET RDS ON is larger than typical value tripping
the high side current limit circuit. On detection of high-side current limit, the low-side FET is turned on, causing
the output capacitor to discharge and trip the low-side current limit. Further attempts to restart the converter
cause the low-side protection to trigger and the sequence continues until the output capacitor is discharged to
ground. The operation is illustrated in Figure 7-12.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 27

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

|VBST|Col2|Col3|
|---|---|---|
|5 V 8 V|||
||||
||||
||||


|VCSN|t|Col3|
|---|---|---|
|V IN|||
||t||
||||


I SW t OC



t

|0 6 A|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|


**Figure 7-12. Open Circuit Condition with Bootstrap Undervoltage Lockout Fault**

The open circuit can be detected by reading the CHxHSILIM, CHxLSILIM bits in the STATUS1 register and
CHxBSTUV bit in the STATUS2 register in conjunction with the CHxTOFFMIN and CHxVLED register. The
microcontroller can detect and respond to open circuit by polling CHxVLED register in conjunction with reading
CHxTOFFMIN, CHxLSILIM, and CHxBSTUV bits.

Table 7-3 summarizes the device response to open circuit faults. The device can transition between different
modes near the input voltage range of 40 V to 50 V. TI recommends polling STATUS1, STATUS2, and STATUS3
registers to correctly identify an open circuit fault based on the specified input voltage range and choice of output
capacitor.

**Table 7-3. O** **p** **en Circuit Fault Detection Summar** **y**

|Col1|VCSNx ADC|CHxCOMPOV|CHxTOFFMIN|CHxBSTUV|CHxHSILIM|CHxLSILIM|CHxSHORT|
|---|---|---|---|---|---|---|---|
|Case 1|Read CSNx ADC measurement|1|1|0|0|0|0|
|Case 2|Read CSNx ADC measurement|0|1|0|0|0|0|
|Case 3|Ignore CSNx ADC measurement|x|x|1|1|1|1|



28 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **7.4 Device Functional Modes**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021


POR

**Figure 7-13. TPS92520-Q1 Functional Modes**

**7.4.1 Power On Reset (POR)**

The device is in POR state when V5A or V5D input is below the undervoltage lockout threshold. In POR, all of
the register settings are reset to the default values and both channels are turned off. The device exits POR and
enters functional modes when the V5D supply exceeds 4.1 V.

**7.4.2 Detect SPI Communication**

After the existing POR state, the device waits for an SPI transaction. If no transaction with an correct SPI frame
is received for 2 [24] system clock cycles (approximately 1.55 s), the communication watchdog timer times out and
the device enters stand-alone mode of operation. Receiving a valid SPI frame before the watchdog timeout
resets the timer and the device transitions to LOAD mode.

**7.4.3 Standalone Mode**

The TPS92520-Q1 is designed to operate in stand-alone mode without the need for an external microcontroller
or SPI-based communication. In this mode, the watchdog timer circuit is disabled and each channel is
individually controlled by external inputs. The reference current is set based on the LHI pin voltage and the
outputs are enabled using the UDIM inputs. The default value for the on-timer is selected and the channels
operate at a fixed switching frequency of 437 kHz. The device also defaults to auto-restart mode for all faults
with the fault timer set to 3.6 ms typical. Connecting the LHI pin to GND (below 148-mV threshold) disables both
channels and turns off both outputs. If the logic is in Standalone Mode, writing 0xC3 to the RESET register sets

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 29

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

all values to default and returns the state machines to the LOAD state. Likewise, if the logic is in Standalone
Mode, reading STATUS3 register first to clear the CMWTO bits and then writing 0xD4 to the RESET register sets
all values to default and returns the state machine to the DETECT state.

**7.4.4 Load Mode**

The device operation in normal-run mode and limp-home mode is programmed by loading information into the
configuration and control registers via SPI. The CHxEN bit is set low to prevent the converters from turning on
and operating with default system parameters. The PC bit in the STATUS3 register must be cleared by sending a
read command in order to exit this mode. Writing "01" bits to the SLEEP register skips the run mode and the
device directly enters a low-power sleep state.

**7.4.5 Run Mode**

The device advances to run mode when the CHxEN bit is set to "1" in the SYSCFG1 register. In this mode, all
the necessary conditions for initiating the soft-start sequence are checked. The LHSW bit in the SYSCFG1
register must be "0" and cannot have any active latched faults present to initiate switching operation. If a latched
fault occurs in this state, the CHxEN bit is reset and the COMP capacitor is discharged, thus forcing the device
back to load mode. Otherwise, the device attempts to resume operation after waiting for the fault timer to
timeout.

In the event of SPI communication failure, the device transitions to limp-home mode. For this to occur, the
watchdog timer must be enabled (the CMWEN bit equals 1 in the SYSCFG1 register). The device enters limphome mode after counting three consecutive watchdog timeout events. Alternatively, the device can be forced
into limp-home mode by setting the LHSW bit high in the SYSCFG1 register.

Transition to sleep mode is initiated by writing "01" bits to the SLEEP register via SPI. This causes the device to
enter a low-power state.

**7.4.6 Sleep Mode**

In sleep mode, the following occurs:

1. The internal regulators are disconnected from the V5A pin.

2. The oscillator is disabled.

3. The CHxEN bit is set low.

4. The channels are disabled.

5. ADC and DAC operation are disabled.

6. The MOSFETs are turned off.

In addition, the resistor divider networks for VINx measurements and V5D measurement are disconnected to
conserve power. Only the SPI communication logic, powered by V5D supply, is active and the SPI bus is
monitored to check command writes to the SLEEP register. Upon receiving the wake command (writing "00" to
SLEEP[1:0] bits in SLEEP register), the device transitions from sleep mode to load mode. In sleep mode, the
output voltage will rise above 3 V as all internal loads are switched off and the leakage current associated with
high-side gate drive is forced through the switch node, SWx.

**7.4.7 Limp-Home Mode**

The TPS92520-Q1 enters the limp-home mode after detecting three consecutive watchdog timeout events or
when the LHSW bit is set high in the SYSCFG1 register. In limp-home mode, the device sets the operation
based on the SPI-programmable LH-registers (register address 0x1E to 0x2D). The limp-home registers must be
programmed upon the initialization of the device in load mode.

The LED current reference can be programmed through the LHxIADJ registers or set by external voltage
measured at the LHI pin by the ADC. To enable LED control by the LHI pin, set the LHEXTIADJ bit in the
LHCFG1 register to "1". Equation 14 expresses the relationship between the LED current and voltage at the LHI
pin, V LHI .

30 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021


I LED V LHI
14 u R CS (14)

The LHI voltage measured by the ADC is converted to a 10-bit value and stored in the LHI registers. An internal
digital low pass filter attenuates any switching noise coupled to the LHI pin. The output of the filter is stored in
the LHIFILT registers.

When the external LHI pin is selected as the LED current reference, an LHI pin voltage below 148 mV disables
both channels and turns off the LEDs. In this condition, the device ensures that no light output is generated for
the associated channels. The LHI pin voltage has to exceed 200 mV to enable both channels. The hysteresis
rejects external noise on LHI pin and avoids light flickering.

To exit limp-home mode, the contents of STATUS3 register must be read to clear the CMWTO bits followed by a
write command to set the LHSW bit in the SYSCFG1 register to "0".
###### **7.5 Programming**

The programming of the TPS92520-Q1 registers can be performed via a serial interface communication. The 4wire control interface in TPS92520-Q1 is compatible with the Serial Peripheral Interface (SPI) bus. A
microcontroller unit (MCU) can write to and read from the device registers to configure the channel operation and
enable or disable a specific channel.

**7.5.1 Serial Interface**

The SPI bus consists of four signals:

 - SSN

 - SCK

 - MOSI

 - MISO

The SSN, SCK, and MOSI pins are TTL inputs into the TPS92520-Q1 while the MISO pin is an open-drain
output. The SPI bus can be configured for both star-connect and daisy-chain network.

A bus transaction is initiated by an MCU on a falling edge of SSN. While SSN is low, the input data present on
the MOSI pin is sampled on the rising edge of SCK with the MS-bit first. The output data is asserted on the
MISO pin at the falling edge of the SCK. Figure 7-14 shows the data transition and sampling edges of SCK.

SSN

**Figure 7-14. SPI Data Format**

A valid transfer requires a non-zero integer multiple of 16 SCK cycles (that is 16, 32, 48, and so forth). If SSN is
pulsed low and no SCK pulses are issued before SSN rises, a SPI error is reported. Similarly, if SSN is raised
before the 16 [th] rising edge of SCK, the transfer is aborted and a SPI error is reported. If SSN is held low after the
16 [th] falling edge of SCK and additional SCK edges occur, the data continues to flow through the TP92520-Q1
shift register and out of the MISO pin. When SSN transitions from low to high, the internal digital block decodes
the most recent 16 bits that were received prior to the SSN rising edge.

SSN must transition to high only after a multiple of 16 SCK cycles for a transaction to be valid. Otherwise a SPI
error is reported. In the case of a write transaction, the TPS92520-Q1 logic performs the requested operation

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 31

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

when SSN transitions high as long as there was no SPI error. In the case of a read transaction, the read data is
transferred during the next frame, regardless of whether an SPI error has occurred.

SSN

**Figure 7-15. SPI Command and Response Sequence**

The data bit on MOSI is shifted into an internal 16-bit shift register (MS-bit first) while data is simultaneously
shifted out of the MISO pin. While SSN is high (bus idle), MISO is tri-stated by the open-drain driver. While SSN
is low, MISO is driven according to the 16-bit data pattern being shifted out based on the prior received
command. To begin a transaction at the falling edge of the SSN, MISO is driven to the MS-bit of the outbound
data and is updated on each subsequent falling edge of SCK.

**7.5.2 Command Frame**

The command frames are the only defined frame-format that are sent from master to slave on MOSI. A
command frame can be either a read command or a write command. A command frame consists of a CMD bit,
six bits of ADDRESS, a PARITY bit (odd parity), and eight bits of DATA. Figure 7-16 shows the format of the
command frame. The bit sequence is as follows:

1. The COMMAND bit (CMD). CMD = 1 means the transfer is a write command; CMD = 0 means it is a read
command.

2. Six bits of ADDRESS (A5:A0)
3. The PARITY bit (PAR). This bit is set by the following equation: PARITY = XNOR(CMD, A5..A0, D7..D0).
4. Eight bits of DATA (D7..D0). For read commands, set the DATA bits to zero.

Both the read and the write command follow the command frame format.

SSN

SCK

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

**Figure 7-16. Command Frame Format**

**7.5.3 Response Frame**

|Col1|C M D|A 5|A 4|A 3|A 2|A 1|A 0|P A R|D 7|D 6|D 5|D 4|D 3|D 2|D 1|D 0|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



There are three possible response frame formats: read response, write response, and write error/POR. These
formats are further described in *Write Response Frame Format* through *Write Error/POR Frame Format* .

***7.5.3.1 Read Response Frame Format***

The read response has the following format:

1. The SPI Error bit (SPE)
2. Five reserved bits (always '11000')
3. The Power-Cycled bit (PC)
4. The Thermal Warning bit (TW)
5. Eight bits of DATA (D7..D0) (only valid if SPE = 0)

32 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021


Figure 7-17 shows the read response format. The frame is sent out by the TPS92520-Q1 following a read
command.

SSN

SCK

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

**Figure 7-17. Read Response Frame Format**

|Col1|S P E|1|1|0|0|0|P C|T W|D 7|D 6|D 5|D 4|D 3|D 2|D 1|D 0|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



***7.5.3.2 Write Response Frame Format***

The write response frame has the following format:

1. The SPI Error bit (SPE)
2. The COMMAND bit (CMD)
3. Six bits of ADDRESS (A5..A0)
4. Eight bits of DATA read from the destination register (D7..D0)

Figure 7-18 shows the write response format. This frame is sent out following a write command if the previously
received frame was a write command and no SPI error occurred during that frame.

The data bits in the write response are read back from the destination register that was just written. There is no
need to issue a read command and evaluate the read response in order to check that the destination register
was written correctly.

SSN

SCK

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

**Figure 7-18. Write Response Frame Format**

|Col1|S P E|C M D|A 5|A 4|A 3|A 2|A 1|A 0|D 7|D 6|D 5|D 4|D 3|D 2|D 1|D 0|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



***7.5.3.3 Write Error/POR Frame Format***

The write error/POR frame is simply a '1' in the MSB followed by all zeroes (see Figure 7-19). This frame is sent
out by the TPS92520-Q1 internal digital block during the first SPI transfer following power-on reset, or following a
write command with a SPI Error.

SSN

SCK

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

MISO

**Figure 7-19. Write Error/POR Frame Format**

**7.5.4 SPI Error**

The TPS92520-Q1 device records a SPI Error if any of the following conditions occur:

1. The SPI command has a non-integer multiple of 16 SCK pulses.
2. Any of the DATA bits during a read command are non-zero.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 33

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

3. There is a parity error in the previously received command.

If any of these conditions are true, the TPS92520-Q1 sets the SPE bit high in the next response frame. A write
command with a SPI error does not write to the register begin addressed. Similarly, a read command does not
clear any active fault bits if the command has a SPI error. Additionally, if a read response has SPE = 1, the read
data bits are invalid and must be disregarded.

**7.5.5 SPI for Multiple Slave Devices in Parallel Configuration**

The TPS92520-Q1 device can be connected in a star configuration where the SSN of each device is
independently controlled by the microcontroller. Figure 7-20 shows the topology when three devices are
connected.

**Figure 7-20. Parallel / Star Configuration**

|MASTER MOSI MISO CLK GPIO GPIO GPIO|Col2|Device 1 Device 2 Device 3 MOSI MISO MOSI MISO MOSI MISO SCK SSN SCK SSN SCK SSN|
|---|---|---|
||||
||||



**7.5.6 SPI for Multiple Slave Devices in Daisy Chain Configuration**

The TPS92520-Q1 device can be connected in a daisy chain configuration to keep GPIO ports available when
multiple devices are communicating to the same microcontroller. Figure 7-21 shows the topology when three
devices are connected.

**Figure 7-21. Daisy Chain Configuration**

|MASTER MOSI MISO CLK GPIO|Col2|Device 1 Device 2 Device 3 MOSI MISO MOSI MISO MOSI MISO SCK SSN SCK SSN SCK SSN|
|---|---|---|
||||
||||



The data is shifted through each slave device, from MOSI input to MISO output through each device's internal
16-bit shift register. After 16 clock cycles, the data has been transferred from one device to another. The
sequence continues until all data is passed through from first device, with MOSI connected to the

34 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021


microcontroller, to the last device, with MISO connected to the micrcontroller. On the rising edge of SSN, each
device decodes the last 16 bits that were received and held in the internal shift register.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 35

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
###### **7.6 Register Maps**

The SPI-accessible registers are each eight bits wide and exist in a six-bit addressable register array (0x00
through 0x3F). The registers in the TPS92520-Q1 device contain programmed information and operating status.
Upon power up, the registers are reset to the default values. Writes to unlisted addresses are not permitted and
can result in undesired operation. Reads of unlisted addresses return the zero value.

Reserved bits ("RESERVED") must be written with '0' values when writing. Registers are read or write unless
indicated otherwise in the description of the register. Table 7-4 lists the TPS92520-Q1 register map.

**Table 7-4. TPS92520-Q1 Re** **g** **ister Ma** **p**

|ADDR|REGISTER|D7|D6|D5|D4|D3|D2|D1|D0|DEFAULT|
|---|---|---|---|---|---|---|---|---|---|---|
|0x00|SYSCFG1|FPINRST|PWMPH|LHSW|CMWEN|CH2INTPWM|CH2EN|CH1INTPWM|CH1EN|00010000|
|0x01|SYSCFG2|IFT[1:0]||CH2TSFL|CH2HSILIMFL|CH2LSILIMFL|CH1TSFL|CH1HSILIMFL|CH1LSILIMFL|00000000|
|0x02|CMWTAP|RESERVED||||CMWTAP[3:0]||||00001000|
|0x03|STATUS1|CH2LSILIM|CH2HSILIM|CH2SHORT|CH2COMPOV|CH1LSILIM|CH1HSILIM|CH1SHORT|CH1COMPOV|n/a|
|0x04|STATUS2|RESERVED||CH2TP|CH2BSTUV|CH2TOFFMIN|CH1TP|CH1BSTUV|CH1TOFFMIN|n/a|
|0x05|STATUS3|STANDALONE|V5AUV|CMWTO[1:0]||TW|PC|CH2STATUS|CH1STATUS|n/a|
|0x06|TWLMT|TWLMT[9:2]||||||||10001010|
|0x07|SLEEP|RESERVED||||||SLEEP[1:0]||00000000|
|0x08|CH1IADJL|RESERVED||||||CH1IADJ[1:0]||00000000|
|0x09|CH1IADJH|CH1IADJ[9:2]||||||||00000000|
|0x0A|CH2IADJL|RESERVED||||||CH2IADJ[1:0]||00000000|
|0x0B|CH2IADJH|CH2IADJ[9:2]||||||||00000000|
|0x0C|PWMDIV|RESERVED|||||PWMDIV[2:0]|||00000100|
|0x0D|CH1PWML|CH1PWM[7:0]||||||||00000000|
|0x0E|CH1PWMH|RESERVED||||||CH1PWM[9:8]||00000000|
|0x0F|CH2PWML|CH2PWM[7:0]||||||||00000000|
|0x10|CH2PWMH|RESERVED||||||CH2PWM[9:8]||00000000|
|0x11|CH1TON|RESERVED||CH1TON[5:0]||||||00000111|
|0x12|CH2TON|RESERVED||CH2TON[5:0]||||||00000111|
|0x13|CH1VIN|CH1VIN[7:0]||||||||n/a|
|0x14|CH1VLED|CH1VLED[7:0]||||||||n/a|
|0x15|CH1VLEDON|CH1VLEDON[7:0]||||||||n/a|
|0x16|CH1VLEDOFF|CH1VLEDOFF[7:0]||||||||n/a|
|0x17|CH2VIN|CH2VIN[7:0]||||||||n/a|
|0x18|CH2VLED|CH2VLED[7:0]||||||||n/a|
|0x19|CH2VLEDON|CH2VLEDON[7:0]||||||||n/a|
|0x1A|CH2VLEDOFF|CH2VLEDOFF[7:0]||||||||n/a|
|0x1B|TEMPL|RESERVED||||||TEMP[1:0]||n/a|
|0x1C|TEMPH|TEMP[9:2]||||||||n/a|
|0x1D|V5D|V5D[7:0]||||||||n/a|
|0x1E|LHCFG1|LHPWMPH|LHEXTIADJ|LH2100DC|LH2INTPWM|LH2EN|LH1100DC|LH1INTPWM|LH1EN|00000000|
|0x1F|LHCFG2|LHIFT[1:0]||LH2TSFL|LH2HSILIMFL|LH2LSILIMFL|LH1TSFL|LH1HSILIMFL|LH1LSILIMFL|00000000|
|0x20|LHIL|RESERVED||||||LHI[1:0]||n/a|
|0x21|LHIH|LHI[9:2]||||||||n/a|
|0x22|LHIFILTL|||||||LHIFILT[1:0]||n/a|
|0x23|LHIFILTH|LHIFILT[9:2]|||||||||
|0x24|LH1IADJL|RESERVED||||||LH1IADJ[1:0]||00000000|
|0x25|LH1IADJH|LH1IADJ[9:2]||||||||00000000|
|0x26|LH2IADJL|RESERVED||||||LH2IADJ[1:0]||00000000|
|0x27|LH2IADJH|LH2IADJ[9:2]||||||||00000000|
|0x28|LHCH1PWML|LH1PWM[7:0]||||||||00000000|
|0x29|LHCH1PWMH|RESERVED||||||LH1PWM[9:8]||00000000|
|0x2A|LHCH2PWML|LH2PWM[7:0]||||||||00000000|
|0x2B|LHCH2PWMH|RESERVED||||||LH2PWM[9:8]||00000000|
|0x2C|LH1TON|RESERVED||LH1TON[5:0]||||||00000111|
|0x2D|LH2TON|RESERVED||LH2TON[5:0]||||||00000111|



36 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-4. TPS92520-Q1 Re** **g** **ister Ma** **p** **(** **continued** **)**

|ADDR|REGISTER|D7|D6|D5|D4|D3|D2|D1|D0|DEFAULT|
|---|---|---|---|---|---|---|---|---|---|---|
|0x2E|RESET|RESET[7:0]||||||||00000000|


Complex bit access types are encoded to fit into small table cells. Table 7-5 shows the codes that are used for
access types in this section.

**Table 7-5. Access T** **yp** **e Codes**

The following sections provide the descriptions for different registers.

**7.6.1 Configuration Registers**

The configuration registers are used to control the device operation and program the fault response.
Configuration registers are read and write capable.

**Table 7-6. Confi** **g** **uration Re** **g** **isters**

***7.6.1.1 SYSCFG1 Register (address = 0x00) [reset = 0x10]***

The SYSCFG1 register is the first system configuration register and it contains bits associated with the enabling
of channels and several device-related functions. Figure 7-22 shows SYSCFG1. Table 7-7 describes SYSCFG1.

**Table 7-7. S** **y** **stem Confi** **g** **uration Re** **g** **ister 1 Field Descri** **p** **tion**

|Access Type|Code|Description|
|---|---|---|
|W|W|Write|
|R|R|Read|
|R/W|R/W|Read and Write|
|RC|RC|Read to clear|
|-n||Value after reset or the default value|


|Address|Acronym|Register Name|Section|
|---|---|---|---|
|0x00|SYSCFG1|System Configuration Register 1|Section 7.6.1.1|
|0x01|SYSCFG2|System Configuration Register 2|Section 7.6.1.2|
|0x02|CMWTAP|Communication Watchdog Timer Tap Point Register|Section 7.6.1.3|


|Figure 7-22. System Configuration Register 1 (SYSCFG1)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|7 6 5 4 3 2 1 0||||||||
|FPINRST|PWMPH|LHSW|CMWEN|CH2INTPWM|CH2EN|CH1INTPWM|CH1EN|
|W-0b R/W-0b R/W-0b R/W-1b R/W-0b R/W-0b R/W-0b R/W-0b||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|FPINRST|W|0|Reset open-drain fault output if there are no active faults in the system. Note that this bit is write-only. Any reads of this register return 0 in the FPINRST bit location. 0 = Do not care 1 = Reset open-drain fault output|
|6|PWMPH|R/W|0|PWM phase shift setting for internal PWM generator 0 = 180° phase shift between internally generated PWM signals 1 = 0° phase shift between internally generated PWM signals|
|5|LHSW|R/W|0|Software limp-home mode. The limp-home mode can be activated by writing to the register. The bit is also set high in case of communication failure. The bit has to be written to zero to return to normal operation. 0 = Normal Operation 1 = Operation in limp-home state|
|4|CMWEN|R/W|1|Communication watch dog timer 0 = Disable communication watch dog timer 1 = Enable communication watch dog timer|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 37

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-7. S** **y** **stem Confi** **g** **uration Re** **g** **ister 1 Field Descri** **p** **tion** **(** **continued** **)**

***7.6.1.2 SYSCFG2 Register (address = 0x01) [reset = 0x00]***

The SYSCFG2 register is the second system configuration register. This register contains bits associated with
enabling fault handling for both channels and configuring the fault timer. Figure 7-23 shows SYSCFG2. Table 7-8
describes SYSCFG2.

**Table 7-8. S** **y** **stem Confi** **g** **uration Re** **g** **ister 2 Field Descri** **p** **tion**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|3|CH2INTPWM|R/W|0|This bit is used to enable internal PWM generator function for channel 2. 0 = LED current duty cycle of channel 2 controlled by the external signal connected to UDIM2 input 1 = LED current duty cycle of channel 2 controlled by the internal PWM generator (registers PWMDIV and CH2PWM). UDIM2 input must be above V . UDIM2(UVLO)|
|2|CH2EN|R/W|0|CH2 enable. This bit controls the operation of channel 2. 0 = Disable LED channel 2 1 = Enable LED channel 2|
|1|CH1INTPWM|R/W|0|This bit is used to enable internal PWM generator function for channel 1. 0 = LED current duty cycle of channel 1 controlled by external signal connected to UDIM1 input 1 = LED current duty cycle of channel 1 controlled by internal PWM generator (registers PWMDIV and CH1PWM). UDIM1 input must be above V . UDIM1(UVLO)|
|0|CH1EN|R/W|0|CH1 enable. This bit controls the operation of channel 1. 0 = Disable LED channel 1 1 = Enable LED channel 1|


|Figure 7-23. System Configuration Register 2 (SYSCFG2)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|7 6 5 4 3 2 1 0|||||||
|IFT|CH2TSFL|CH2HSILIMFL|CH2LSILIMFL|CH1TSFL|CH1HSILIMFL|CH1LSILIMFL|
|R/W - 00b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b|||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|IFT|R/W|00|IFT sets the counter limit for the fault timer as shown below. 00 = 3.6 ms fault timer 01 = 7.2 ms fault timer 10 = 14.4 ms fault timer 11 = 28.8 ms fault timer|
|5|CH2TSFL|R/W|0|Channel 2 thermal shutdown fault response 0 = Channel 2 auto-restarts based on internal temperature hysteresis. 1 = Channel 2 is latched off; CH2EN bit is reset and channel 2 is disabled until the CH2EN bit is programmed high by SPI command.|
|4|CH2HSILIMFL|R/W|0|Channel 2 high-side FET current limit fault response 0 = Channel 2 auto-restarts after the ILIM fault timer has expired. 1 = Channel 2 is latched off; CH2EN bit is reset and channel 2 is disabled until the CH2EN bit is programmed high by SPI command.|
|3|CH2LSILIMFL|R/W|0|Channel 2 low-side FET current limit fault response 0 = Channel 2 auto-restarts after the ILIM fault timer has expired. 1 = Channel 2 is latched off; CH2EN bit is reset and channel 2 is disabled until the CH2EN bit is programmed high by SPI command.|
|2|CH1TSFL|R/W|0|Channel 1 thermal shutdown fault response 0 = Channel 1 auto-restarts based on internal temperature hysteresis. 1 = Channel 1 is latched off; CH1EN bit is reset and channel 1 is disabled until the CH1EN bit is programmed high by SPI command.|
|1|CH1HSILIMFL|R/W|0|Channel 1 high side FET current limit fault response 0 = Channel 1 auto-restarts after the ILIM fault timer has expired. 1 = Channel 1 is latched off; CH1EN bit is reset and channel 1 is disabled until the CH1EN bit is programmed high by SPI command.|



38 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-8. S** **y** **stem Confi** **g** **uration Re** **g** **ister 2 Field Descri** **p** **tion** **(** **continued** **)**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|0|CH1LSILIMFL|R/W|0|Channel 1 low side FET current limit fault response 0 = Channel 1 auto-restarts after the ILIM fault timer has expired. 1 = Channel 1 is latched off; CH1EN bit is reset and channel 1 is disabled until the CH1EN bit is programmed high by SPI command.|


***7.6.1.3 CMWTAP Register (address = 0x02) [reset = 0x08]***

The CMWTAP register sets the tap point (that is the bit number, starting from 0) on the 25-bit communication
watchdog timer to establish the timeout condition. By default, the tap point is set to bit 24. Figure 7-24 shows
CMWTAP. Table 7-9 describes CMWTAP.

**7.6.2 STATUS Registers**

The status registers are used to report warning and fault conditions. Status registers are read-only registers.
Reading the register clears the bits that are set if the condition that caused them no long exists. The clearing of

|Figure 7-24. Communication Watchdog Timer Tap Point Register (CMWTAP)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CMWTAP[3:0]|
|R-0b R/W-1000b||


|Col1|Col2|Col3|Table 7-9.|CMWTAP-to-Tap Point Mapping|
|---|---|---|---|---|
|Bit|Field|Type|Reset|Description|
|7-4|RESERVED|R|0000|Reserved|
|3-0|CMWTAP|R/W|1000|Mapping of CMWTAP bits to the tap points 0000 = Tap point set to bit 16 corresponding to 6.1 ms (typical) watch dog period. 0001 = Tap point set to bit 17 corresponding to 12.1 ms (typical) watch dog period. 0010 = Tap point set to bit 18 corresponding to 24.3 ms (typical) watch dog period. 0011 = Tap point set to bit 19 corresponding to 48.5 ms (typical) watch dog period. 0100 = Tap point set to bit 20 corresponding to 97.1 ms (typical) watch dog period. 0101 = Tap point set to bit 21 corresponding to 194.2 ms (typical) watch dog period. 0110 = Tap point set to bit 22 corresponding to 388.3 ms (typical) watch dog period. 0111 = Tap point set to bit 23 corresponding to 776.7 ms (typical) watch dog period. 1000 through 1111 = Tap point set to bit 24 corresponding to 1.52 s (typical) watchdog period.|

the bits happens at the end of the read response SPI transfer, not at the end of the read command SPI transfer.
All bits are active-high.

**Table 7-10. Status Re** **g** **isters**

***7.6.2.1 STATUS1 Register (address = 0x03)***

Figure 7-25 shows STATUS1. Table 7-11 describes STATUS1.

|Address|Acronym|Register Name|Section|
|---|---|---|---|
|0x03|STATUS1|Status 1 Register (Read-Only)|Section 7.6.2.1|
|0x04|STATUS2|Status 2 Register (Read Only)|Section 7.6.2.2|
|0x05|STATUS3|Status 3 Register (Read Only)|Section 7.6.2.3|


|Figure 7-25. Status 1 Register (Read-Only) (STATUS1)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|7 6 5 4 3 2 1 0||||||||
|CH2LSILIM|CH2HSILIM|CH2SHORT|CH2COMPOV|CH1LSILIM|CH1HSILIM|CH1SHORT|CH1COMPOV|
|RC-0b RC-0b RC-0b RC-0b RC-0b RC-0b RC-0b RC-0b||||||||



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 39

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-11. Status 1 Re** **g** **ister Field Descri** **p** **tion**

***7.6.2.2 STATUS2 Register (address = 0x04)***

STATUS2 register is a read-only register. Figure 7-26 shows STATUS2. Table 7-12 describes STATUS2.

**Table 7-12. Status 2 Re** **g** **ister Field Descri** **p** **tion**

***7.6.2.3 STATUS3 Register (address = 0x05)***

STATUS3 register is a read-only register. Figure 7-27 shows STATUS3. Table 7-13 describes STATUS3.

**Fi** **g** **ure 7-27. Status 3 Re** **g** **ister** **(** **Read Onl** **y)** **(** **STATUS3** **)**

7 6 5 4 3 2 1 0

STANDALONE V5AUV CMWTO[1:0] TW PC CH2STATUS CH1STATUS

R-0b RC-0b RC-00b RC-0b RC-1b RC-0b RC-0b

**Table 7-13. Status 3 Re** **g** **ister Field Descri** **p** **tion**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH2LSILIM|RC|0|Indicates low-side switch current limit fault on channel 2. Low-side switch current is greater than 1.5 A (typical).|
|6|CH2HSILIM|RC|0|Indicates high-side switch current limit fault on channel 2. High-side switch current is greater than 2.7 A (typical).|
|5|CH2SHORT|RC|0|Indicates output short circuit fault on channel 2. CSP pin voltage is below 2.45 V.|
|4|CH2COMPOV|RC|0|Indicates overvoltage condition on COMP2 pin. COMP2 pin voltage is greater than 3.2 V.|
|3|CH1LSILIM|RC|0|Indicates low-side switch current limit fault on channel 1. Low-side switch current is greater than 1.5 A (typical).|
|2|CH1HSILIM|RC|0|Indicates high-side switch current limit fault on channel 1. High-side switch current is greater than 2.7 A (typical).|
|1|CH1SHORT|RC|0|Indicates output short circuit fault on channel 1. CSP pin voltage is below 2.45 V.|
|0|CH1COMPOV|RC|0|Indicates overvoltage condition on COMP1 pin. COMP1 pin voltage is greater than 3.2 V.|


|Figure 7-26. Status 2 Register (Read Only) (STATUS2)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|7 6 5 4 3 2 1 0|||||||
|RESERVED|CH2TP|CH2BSTUV|CH2TOFFMIN|CH1TP|CH1BSTUV|CH1TOFFMIN|
|R-00b RC-0b RC-0b RC-0b RC-0b RC-0b RC-0b|||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R|00|Reserved|
|5|CH2TP|RC|0|Indicates overtemperature thermal protection for channel 2. The channel automatically restarts when the bit is cleared to 0.|
|4|CH2BSTUV|RC|0|Indicates bootstrap undervoltage fault condition on channel 2. BST2 pin voltage is less than 2.95 V.|
|3|CH2TOFFMIN|RC|0|Indicates channel 2 operation at maximum duty cycle.|
|2|CH1TP|RC|0|Indicates overtemperature thermal protection for channel 1. The channel automatically restarts when the bit is cleared to 0.|
|1|CH1BSTUV|RC|0|Indicates bootstrap undervoltage fault condition on channel 1. BST1 pin voltage is less than 2.95 V.|
|0|CH1TOFFMIN|RC|0|Indicates channel 1 operation at maximum duty cycle.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|STANDALONE|R|0|Indicates standalone mode. This bit can be cleared by issuing the RESET or DETECT command (see RESET register).|
|6|V5AUV|RC|0|Indicates V5A undervoltage fault condition.|



40 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-13. Status 3 Re** **g** **ister Field Descri** **p** **tion** **(** **continued** **)**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|5-4|CMWTO|RC|00|Indicates the number of times the communication watchdog timer has expired. 00 = Default (normal operation) 01 = Watchdog has expired 1 time. 10 = Watchdog has expired 2 times. 11 = Watchdog has expired 3 times. Device transitions into limp-home mode.|
|3|TW|RC|0|Indicates overtemperature thermal warning|
|2|PC|RC|1|Power cycle bit is set at power up and is considered a fault. The PC bit must be cleared before the channels can be enabled.|
|1|CH2STATUS|RC|0|Logic OR of the fault bits for channel 2 excluding over temperature thermal warning.|
|0|CH1STATUS|RC|0|Logic OR of the fault bits for channel 1 excluding over temperature thermal warning.|


**7.6.3 Device Control Registers**

The control registers are used to enable sleep mode and program the temperature warning threshold, LED
current, and PWM duty cycle set points. The registers are read- and write-capable.

**Table 7-14. Device Control Re** **g** **isters**

***7.6.3.1 Thermal Warning Limit (address = 0x06) [reset = 0x8A]***

Figure 7-28 shows TWLMT[9:2]. Table 7-15 describes TWLMT[9:2].

**Fi** **g** **ure 7-28. Thermal Warnin** **g** **Limit Re** **g** **ister**

7 6 5 4 3 2 1 0

TWLMT[9:2]

R/W-10001010b

|Address|Acronym|Register Name|Section|
|---|---|---|---|
|0x06|TWLMT[9:2]|Thermal Warning Limit|Section 7.6.3.1|
|0x07|SLEEP|Sleep Command Register|Section 7.6.3.2|
|0x08|CH1IADJL|Channel 1 Analog Current Control Register (LSB)|Section 7.6.3.3|
|0x09|CH1IADJH|Channel 1 Analog Current Control Register (MSB)|Section 7.6.3.4|
|0x0A|CH2IADJL|Channel 2 Analog Current Control Register (LSB)|Section 7.6.3.5|
|0x0B|CH2IADJH|Channel 2 Analog Current Control Register (MSB)|Section 7.6.3.6|
|0x0C|PWMDIV|Internal PWM Clock Divider Register|Section 7.6.3.7|
|0x0D|CH1PWML|Channel 1 PWM Width Register (LSB)|Section 7.6.3.8|
|0x0E|CH1PWMH|Channel 1 PWM Width Register (MSB)|Section 7.6.3.9|
|0x0F|CH2PWML|Channel 2 PWM Width Register (LSB)|Section 7.6.3.10|
|0x10|CH2PWMH|Channel 2 PWM Width Register (MSB)|Section 7.6.3.11|
|0x11|CH1TON|Channel 1 On-Time Register|Section 7.6.3.12|
|0x12|CH2TON|Channel 2 On-Time Register|Section 7.6.3.13|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 41

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-15. Thermal Warnin** **g** **Limit Field Descri** **p** **tion**

***7.6.3.2 SLEEP Command (address = 0x07) [reset = 0x00]***

Figure 7-29 shows the SLEEP register. Table 7-16 describes the SLEEP register.

**Table 7-16. Slee** **p** **Command Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.3 CH1IADJL Control Register (address = 0x08) [reset = 0x00]***

Figure 7-30 shows the CH1IADJL register. Table 7-17 describes the CH1IADJL register.

**Table 7-17. Channel 1 Analo** **g** **Current Control Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.4 CH1IADJH Control Register (address = 0x09) [reset = 0x00]***

Figure 7-31 shows the CH1IADJH register. Table 7-18 describes the CH1IADJH register.

**Fi** **g** **ure 7-31. Channel 1 Analo** **g** **Current Control Re** **g** **ister** **(** **MSB** **)**

7 6 5 4 3 2 1 0

CH1IADJ[9:2]

R/W-00000000b

**Table 7-18. Channel 1 Analo** **g** **Current Control Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.5 CH2IADJL Control Register (address = 0x0A) [reset = 0x00]***

Figure 7-32 shows the CH2IADJL register. Table 7-19 describes the CH2IADJL register.

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|TWLMT[9:2]|R/W|10001010|TWLMT[9:2] sets the Thermal Warning (TW) bit when the most significant 8 bits of the ADC reading of the TEMP value exceed the programmed value. The default value is 138 decimal, or 0x8Ah (corresponding to a temperature of 125°C).|


|Figure 7-29. Sleep Command Register|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|SLEEP[1:0]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|SLEEP|R/W|00|Device sleep mode. The low-power sleep mode can be activated by writing to the register. 00 = Exit sleep mode and return to normal operation (SLEEP OFF). 01 = Enter sleep mode (SLEEP ON). 10 = No effect 11 = No effect|


|Figure 7-30. Channel 1 Analog Current Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CH1IADJ[1:0]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|CH1IADJ[1:0]|R/W|00|Channel 1 analog current control. The 2 LSBs of the 10-bit IADJ DAC for channel 1 can be programmed by writing to the register.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1IADJ[9:2]|R/W|00000000|Channel 1 analog current control. The 8 MSBs of the 10-bit IADJ DAC for channel 1 can be programmed by writing to the register.|



42 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-19. Channel 2 Analo** **g** **Current Control Re** **g** **ister Field Descri** **p** **tion**

|Figure 7-32. Channel 2 Analog Current Control Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CH2IADJ[1:0]|
|R-000000b R/W-00b||

|BIT|FIELD|TYPE|RESET|DESCRIPTION|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|CH2IADJ[1:0]|R/W|00|Channel 2 analog current control. The 2 LSBs of the 10-bit IADJ DAC for channel 2 can be programmed by writing to the register.|


***7.6.3.6 CH2IADJH Control Register (address = 0x0B) [reset = 0x00]***

Figure 7-33 shows the CH2IADJH register. Table 7-20 describes the CH2IADJH register.

**Fi** **g** **ure 7-33. Channel 2 Analo** **g** **Current Control Re** **g** **ister** **(** **MSB** **)**

7 6 5 4 3 2 1 0

CH2IADJ[9:2]

R/W-00000000b

**Table 7-20. Channel 2 Analo** **g** **Current Control Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.7 PWMDIV Register (address = 0x0C) [reset = 0x04]***

Figure 7-34 shows the PWMDIV register. Table 7-21 describes the PWMDIV register.

**Table 7-21. Internal PWM Clock Divider Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.8 CH1PWML Register (address = 0x0D) [reset = 0x00]***

Figure 7-35 shows the CH1PWML register. Table 7-22 describes the CH1PWML register.

**Fi** **g** **ure 7-35. Channel 1 PWM Width Re** **g** **ister** **(** **LSB** **)**

7 6 5 4 3 2 1 0

CH1PWM[7-0]

R/W-00000000b

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH2IADJ[9:2]|R/W|00000000|Channel 2 analog current control. The 8 MSBs of the 10-bit IADJ DAC for channel 2 can be programmed by writing to the register.|


|Figure 7-34. Internal PWM Clock Divider Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|PWMDIV[2:0]|
|R-00000b R/W-100b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-3|RESERVED|R|00000|Reserved|
|2-0|PWMDIV[2:0]|R/W|100|This 3-bit value selects the clock divider for the internal PWM generator. The PWM clock is derived based on typical oscillator frequency of 10.8 MHz. 000 = Divide oscillator clock by 7 (f = 1507 Hz). PWM 001 = Divide oscillator clock by 8 (f = 1318 Hz). PWM 010 = Divide oscillator clock by 10 (f = 1055 Hz). PWM 011 = Divide oscillator clock by 12 (f = 879 Hz). PWM 100 = Divide oscillator clock by 16 (f = 659 Hz). PWM 101 = Divide oscillator clock by 24 (f = 439 Hz). PWM 110 = Divide oscillator clock by 49 (f = 215 Hz). PWM 111 = Divide oscillator clock by 98 (f = 108 Hz). PWM|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 43

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-22. Channel 1 PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.9 CH1PWMH Register (address = 0x0E) [reset = 0x00]***

Figure 7-36 shows the CH1PWMH register. Table 7-23 shows the CH1PWMH register.

**Table 7-23. Channel 1 PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.10 CH2PWML Register (address = 0x0F) [reset = 0x00]***

Figure 7-37 shows the CH2PWML register. Table 7-24 describes the CH2PWML register.

**Fi** **g** **ure 7-37. Channel 2 PWM Width Re** **g** **ister** **(** **LSB** **)**

7 6 5 4 3 2 1 0

CH2PWM[7:0]

R/W-00000000b

**Table 7-24. Channel 2 PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.11 CH2PWMH Register (address = 0x10) [reset = 0x00]***

Figure 7-38 shows the CH2PWMH register. Table 7-25 describes the CH2PWMH register.

**Table 7-25. Channel 2 PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.3.12 CH1TON Register (address = 0x11) [reset = 0x07]***

Figure 7-39 shows the CH1TON register. Table 7-26 describes the CH1TON register.

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1PWM[7:0]|R/W|00000000|Channel 1 PWM width control. The 8 LSBs of the 10-bit PWM WIDTH for channel 1 can be programmed by writing to the register.|


|Figure 7-36. Channel 1 PWM Width Register (MSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CH1PWM[9:8]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|CH1PWM[9:8]|R/W|00|Channel 1 PWM width control. The 2 MSBs of the 10-bit PWM WIDTH for channel 1 can be programmed by writing to the register.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH2PWM[7:0]|R/W|00000000|Channel 2 PWM width control. The 8 LSBs of the 10-bit PWM WIDTH for channel 2 can be programmed by writing to the register.|


|Figure 7-38. Channel 2 PWM Width Register (MSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CH2PWM[9:8]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|CH2PWM[9:8]|R/W|00|Channel 2 PWM width control. The 2 MSBs of the 10-bit PWM WIDTH for channel 2 can be programmed by writing to the register.|


|Figure 7-39. Channel 1 On-Time Register|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CH1TON[5:0]|



44 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Figure 7-39. Channel 1 On-Time Register (continued)**

R-00b R/W-000111b

**Table 7-26. Channel 1 On-Time Re** **g** **ister Field Descri** **p** **tion**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R|00|Reserved|
|5-0|CH1TON[5:0]|R/W|000111|Channel 1 on-time control. The pseudo-fixed switching frequency for channel 1 is set by writing to this register. Default value is set to ensure 437-kHz switching frequency.|


***7.6.3.13 CH2TON Register (address = 0x12) [reset = 0x07]***

Figure 7-40 shows the CH1TON register. Table 7-27 describes the CH1TON register.

**Table 7-27. Channel 2 On-Time Re** **g** **ister Field Descri** **p** **tion**

**7.6.4 ADC Measurements**

The output of ADC conversion is stored in the ADC measurement registers. ADC measurement registers are
read-only registers. Only the 8 MSBs from 10-bit ADC are used and the remaining 2 LSBs are ignored.

**Table 7-28. ADC Measurements**

***7.6.4.1 CH1VIN Measurement (address = 0x13)***

Figure 7-41 shows the CH1VIN register. Table 7-29 describes the CH1VIN register.

**Fi** **g** **ure 7-41. CH1VIN Re** **g** **ister**

7 6 5 4 3 2 1 0

CH1VIN[7:0]

R-00000000b

|Figure 7-40. Channel 2 On-Time Register|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|CH2TON[5:0]|
|R-00b R/W-000111b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R|00|Reserved|
|5-0|CH2TON[5:0]|R/W|000111|Channel 2 on-time control. The pseudo-fixed switching frequency for channel 2 is set by writing to this register. Default value is set to ensure 437 kHz switching frequency.|


|Address|Acronym|Register Name|Section|
|---|---|---|---|
|0x13|CH1VIN|CH1VIN Register|Section 7.6.4.1|
|0x14|CH1VLED|CH1VLED Register|Section 7.6.4.2|
|0x15|CH1VLEDON|CH1VLEDON Register|Section 7.6.4.3|
|0x16|CH1VLEDOFF|CH1VLEDOFF Register|Section 7.6.4.4|
|0x17|CH2VIN|CH2VIN Register|Section 7.6.4.5|
|0x18|CH2VLED|CH2VLED Register|Section 7.6.4.6|
|0x19|CH2VLEDON|CH2VLEDON Register|Section 7.6.4.7|
|0x1A|CH2VLEDOFF|CH2VLEDOFF Register|Section 7.6.4.8|
|0x1B|TEMPL|TEMPL Register|Section 7.6.4.9|
|0x1C|TEMPH|TEMPH Register|Section 7.6.4.10|
|0x1D|V5D|V5D Register|Section 7.6.4.11|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 45

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-29. CH1VIN Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.2 CH1VLED Measurement (address = 0x14)***

Figure 7-42 shows the CH1VLED register. Table 7-30 describes the CH1VLED register.

**Fi** **g** **ure 7-42. CH1VLED Re** **g** **ister**

7 6 5 4 3 2 1 0

CH1VLED[7:0]

R-00000000b

**Table 7-30. CH1VLED Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.3 CH1VLEDON Measurement (address = 0x15)***

Figure 7-43 shows the CH1VLEDON register. Table 7-31 describes the CH1VLEDON register.

**Fi** **g** **ure 7-43. CH1VLEDON Re** **g** **ister**

7 6 5 4 3 2 1 0

CH1VLEDON[7:0]

R-00000000b

**Table 7-31. CH1VLEDON Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.4 CH1VLEDOFF Measurement (address = 0x16)***

Figure 7-44 shows the CH1VLEDOFF register. Table 7-32 describes the CH1VLEDOFF register.

**Fi** **g** **ure 7-44. CH1VLEDOFF Re** **g** **ister**

7 6 5 4 3 2 1 0

CH1VLEDOFF[7:0]

R-00000000b

**Table 7-32. CH1VLEDOFF Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.5 CH2VIN Measurement (address = 0x17)***

Figure 7-45 shows the CH2VIN register. Table 7-33 describes the CH2VIN register.

**Fi** **g** **ure 7-45. CH2VIN Re** **g** **ister**

7 6 5 4 3 2 1 0

CH2VIN[7:0]

R-00000000b

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1VIN|R|00000000|ADC measurement of the drain voltage node for channel 1. The VIN1 pin voltage is internally attenuated by 0.037 to achieve an 8-bit conversion ratio of 65/255 (V/dec). The full scale reading represents 65 V at VIN1 node.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1VLED|R|00000000|ADC measurement of the CSN1 node for channel 1. The CSN1 pin voltage is internally attenuated by 0.037 to achieve an 8-bit conversion ratio of 65/255 (V/dec). The full scale reading represents 65 V at CSN1 node.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1VLEDON|R|00000000|ADC measurement of the CSN1 node for channel 1 before falling edge of PWM signal.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1VLEDOFF|R|00000000|ADC measurement of the CSN1 node for channel 1 before rising edge of PWM signal.|



46 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-33. CH2VIN Re** **g** **ister Field Descri** **p** **tion**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH2VIN|R|00000000|ADC measurement of the drain voltage node for channel 2. The VIN2 pin voltage is internally attenuated by 0.037 to achieve an 8-bit conversion ratio of 65/255 (V/dec). The full scale reading represents 65 V at VIN2 node.|


***7.6.4.6 CH2VLED Measurement (address = 0x18)***

Figure 7-46 shows the CH2VLED register. Table 7-34 describes the CH2VLED register.

**Fi** **g** **ure 7-46. CH2VLED Re** **g** **ister**

7 6 5 4 3 2 1 0

CH2VLED[7:0]

R-00000000b

**Table 7-34. CH2VLED Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.7 CH2VLEDON Measurement (address = 0x19)***

Figure 7-47 shows the CH2VLEDON register. Table 7-35 describes the CH2VLEDON register.

**Fi** **g** **ure 7-47. CH2VLEDON Re** **g** **ister**

7 6 5 4 3 2 1 0

CH2VLEDON[7:0]

R-00000000b

**Table 7-35. CH2VLEDON Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.8 CH2VLEDOFF Measurement (address = 0x1A)***

Figure 7-48 shows the CH2VLEDOFF register. Table 7-36 describes the CH2VLEDOFF register.

**Fi** **g** **ure 7-48. CH2VLEDOFF Re** **g** **ister**

7 6 5 4 3 2 1 0

CH2VLEDOFF[7:0]

R-00000000b

**Table 7-36. CH2VLEDOFF Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.9 TEMPL Measurement (address = 0x1B)***

Figure 7-49 shows the TEMPL register. Table 7-37 describes the TEMPL register.

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH2VLED|R|00000000|ADC measurement of the CSN2 node for channel 2. The CSN2 pin voltage is internally attenuated by 0.037 to achieve an 8-bit conversion ratio of 65/255 (V/dec). The full scale reading represents 65 V at CSN2 node.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH2VLEDON|R|00000000|ADC measurement of the CSN2 node for channel 2 before falling edge of PWM signal.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH2VLEDOFF|R|00000000|ADC measurement of the CSN2 node for channel 2 before rising edge of PWM signal.|


|Figure 7-49. TEMPL Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|TEMP[1:0]|
|R-000000b R-00b||



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 47

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-37. TEMPL Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.10 TEMPH Measurement (address = 0x1C)***

Figure 7-50 shows the TEMPH register. Table 7-38 describes the TEMPH register.

**Fi** **g** **ure 7-50. TEMPH Re** **g** **ister**

7 6 5 4 3 2 1 0

TEMP[9:2]

R-00000000b

**Table 7-38. TEMPH Re** **g** **ister Field Descri** **p** **tion**

***7.6.4.11 V5D Measurement (address = 0x1D)***

Figure 7-51 shows the V5D register. Table 7-39 describes the V5D register.

**Fi** **g** **ure 7-51. V5D Re** **g** **ister**

7 6 5 4 3 2 1 0

V5D[7:0]

R-00000000b

**Table 7-39. V5D Re** **g** **ister Field Descri** **p** **tion**

**7.6.5 Limp-Home Configuration and Command Registers**

The limp-home registers are used to control the device when operating in limp-home mode. Limp-home registers
are read and write capable.

**Table 7-40. Lim** **p** **-Home Confi** **g** **uration and Command Re** **g** **isters**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|TEMP[1:0]|R|00|ADC measurement of the junction temperature. The register reports the 2 LSBs of the junction/exposed pad temperature.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|TEMP[9:2]|R|00000000|ADC measurement of the junction temperature. The register reports the 8 MSBs of the junction/exposed pad temperature.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|V5D[7:0]|R|00000000|ADC measurement of the 5-V bias supply. The V5D pin voltage is internally attenuated by 0.45 to achieve an 8-bit conversion ratio of 5.33/255 (V/dec).|


|Address|Acronym|Register Name|Section|
|---|---|---|---|
|0x1E|LHCFG1|Limp-Home Configuration Register 1|Section 7.6.5.1|
|0x1F|LHCFG2|Limp-Home Configuration Register 2|Section 7.6.5.2|
|0x20|LHIL|Limp-Home Mode External Current Reference (LSB)|Section 7.6.5.3|
|0x21|LHIH|Limp-Home Mode External Current Reference (MSB)|Section 7.6.5.4|
|0x22|LHIFILTL|Limp-Home Mode Filtered External Current Register (LSB)|Section 7.6.5.5|
|0x23|LHIFILTH|Limp-Home Mode Filtered External Current Register (MSB)|Section 7.6.5.6|
|0x24|LH1IADJL|Channel 1 Limp-Home Mode Analog Current Register (LSB)|Section 7.6.5.7|
|0x25|LH1IADJH|Channel 1 Limp-Home Mode Analog Current Register (MSB)|Section 7.6.5.8|



48 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-40. Lim** **p** **-Home Confi** **g** **uration and Command Re** **g** **isters** **(** **continued** **)**

|Address|Acronym|Register Name|Section|
|---|---|---|---|
|0x26|LH2IADJL|Channel 2 Limp-Home Mode Analog Current Register (LSB)|Section 7.6.5.9|
|0x27|LH2IADJH|Channel 2 Limp-Home Mode Analog Current Register (MSB)|Section 7.6.5.10|
|0x28|LH1PWML|Channel 1 Limp-Home Mode PWM Width Register (LSB)|Section 7.6.5.11|
|0x29|LH1PWMH|Channel 1 Limp-Home Mode PWM Width Register (MSB)|Section 7.6.5.12|
|0x2A|LH2PWML|Channel 2 Limp-Home Mode PWM Width Register (LSB)|Section 7.6.5.13|
|0x2B|LH2PWMH|Channel 2 Limp-Home Mode PWM Width Register (MSB)|Section 7.6.5.14|
|0x2C|LH1TON|Channel 1 Limp-Home Mode On- Time Register|Section 7.6.5.15|
|0x2D|LH2TON|Channel 2 Limp-Home Mode On- Time Register|Section 7.6.5.16|


***7.6.5.1 LHCFG1 Register (address = 0x1E) [reset =0x00]***

The LHCFG1 register contains bits associated with the enabling of channels and several device-related
functions when operating in limp-home mode. Figure 7-52 shows the LHCFG1 register. Table 7-41 describes the
LHCFG1 register.

**Table 7-41. Lim** **p** **-Home Confi** **g** **uration Re** **g** **ister 1 Field Descri** **p** **tion**

|Figure 7-52. Limp-Home Configuration Register 1 (LHCFG1)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|7 6 5 4 3 2 1 0||||||||
|LHPWMPH|LHEXTIADJ|LH2100D|LH2INTPWM|LH2EN|LH1100D|LH1INTPWM|LH1EN|
|R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|LHPWMPH|R/W|0|PWM phase shift setting for internal PWM generator in limp-home mode. 0 = 180° phase shift between internally-generated PWM signals 1 = 0° phase shift between internally generated PWM signals|
|6|LHEXTIADJ|R/W|0|This bit is used to select between internal or external current reference set point. The external reference is set by voltage on LHI pin and is converted to a 10-bit value by internal ADC. 0 = Use internal LHxIADJ register as the CHxIADJ setting in limp-home mode. 1 = Use external LHI reference as the CHxIADJ setting in limp-home mode.|
|5|LH2100D|R/W|0|Set channel 2 PWM duty cycle to 100% in limp-home mode. 0 = LED current duty cycle based on internal or external command 1 = LED current duty cycle set to 100%|
|4|LH2INTPWM|R/W|0|This bit is used to enable internal PWM generator function for channel 2 in limp- home mode. 0 = LED current duty cycle of channel 2 controlled by an external signal connected to UDIM2 input 1 = LED current duty cycle of channel 2 controlled by an internal PWM generator (registers PWMDIV and LH2PWM). UDIM2 input must be above V UDIM2(UVLO) threshold.|
|3|LH2EN|R/W|0|CH2 enable. This bit controls the operation of channel 2 in limp-home mode. 0 = Disable LED channel 2. 1 = Enable LED channel 2.|
|2|LH1100D|R/W|0|Set channel 1 PWM duty cycle to 100% in limp-home mode. 0 = LED current duty cycle based on internal or external command 1 = LED current duty cycle set to 100%|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 49

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-41. Lim** **p** **-Home Confi** **g** **uration Re** **g** **ister 1 Field Descri** **p** **tion** **(** **continued** **)**

***7.6.5.2 LHCFG2 Register (address = 0x1F) [reset =0x00h]***

The LHCFG2 register contains bits associated with enabling fault handling for both channels and configuring
fault timer in limp-home mode. Figure 7-53 shows the LHCFG2 register. Table 7-42 describes the LHCFG2
register.

**Table 7-42. Lim** **p** **-Home Confi** **g** **uration Re** **g** **ister 2 Field Descri** **p** **tion**

***7.6.5.3 LHIL Measurement (address = 0x20)***

Figure 7-56 shows the LHI measurement register. Table 7-43 describes the LHI measurement register.

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|1|LH1INTPWM|R/W|0|This bit is used to enable internal PWM generator function for channel 1 in limp- home mode. 0 = LED current duty cycle of channel 1controlled by external signal connected to UDIM1 input 1 = LED current duty cycle of channel 1 controlled by internal PWM generator (registers PWMDIV and LH1PWM). UDIM1 input must be above V UDIM1(UVLO) threshold.|
|0|LH1EN|R/W|0|CH1 enable. This bit controls the operation of channel 1 in limp-home mode. 0 = Disable LED channel 1. 1 = Enable LED channel 1.|


|Figure 7-53. Limp-Home Configuration Register 2 (LHCFG2)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|7 6 5 4 3 2 1 0|||||||
|LHIFT[1:0]|LH2TSFL|LH2HSILIMFL|LH2LSILIMFL|LH1TSFL|LH1HSILIMFL|LH1LSILIMFL|
|R/W-00b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b R/W-0b|||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|LHIFT|R/W|00|LHIFT sets the counter limit for the ILIM fault timer in limp-home mode. 00 = 3.6 ms fault timer 01 = 7.2 ms fault timer 10 = 14.4 ms fault timer 11 = 28.8 ms fault timer|
|5|LH2TSFL|R/W|0|Channel 2 thermal shutdown fault response in limp-home mode 0 = Channel 2 auto-restarts based on internal temperature hysteresis. 1 = Channel 2 is latched off; CH2EN bit is reset and channel 2 is disabled until the CH2EN bit is programmed high by SPI command.|
|4|LH2HSILIMFL|R/W|0|Channel 2 high-side FET current limit fault response in limp-home mode 0 = Channel 2 auto-restarts after the ILIM fault timer has expired. 1 = Channel 2 is latched off; CH2EN bit is reset and channel 2 is disabled until the CH2EN bit is programmed high by SPI command.|
|3|LH2LSILIMFL|R/W|0|Channel 2 low-side FET current limit fault response in limp-home mode 0 = Channel 2 auto-restarts after the ILIM fault timer has expired. 1 = Channel 2 is latched off; CH2EN bit is reset and channel 2 is disabled until the CH2EN bit is programmed high by SPI command.|
|2|LH1TSFL|R/W|0|Channel 1 thermal shutdown fault response in limp-home mode 0 = Channel 1 auto-restarts based on internal temperature hysteresis. 1 = Channel 1 is latched off; CH1EN bit is reset and channel 1 is disabled until the CH1EN bit is programmed high by SPI command.|
|1|LH1HSILIMFL|R/W|0|Channel 1 high-side FET current limit fault response in limp-home mode 0 = Channel 1 auto-restarts after the ILIM fault timer has expired. 1 = Channel 1 is latched off; CH1EN bit is reset and channel 1 is disabled until the CH1EN bit is programmed high by SPI command.|
|0|LH1LSILIMFL|R/W|0|Channel 1 low-side FET current limit fault response in limp-home mode 0 = Channel 1 auto-restarts after the ILIM fault timer has expired. 1 = Channel 1 is latched off; CH1EN bit is reset and channel 1 is disabled until the CH1EN bit is programmed high by SPI command.|



50 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-43. Channel 1 Lim** **p** **-Home Mode External Current Reference Field Descri** **p** **tion**

|Figure 7-54. Limp-Home Mode External Current Reference (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LHI[1:0]|
|R-000000b R-00b||

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|LHI[1:0]|R|00|External current reference set point in limp-home mode. The LHI input voltage is digitized to achieve a 10-bit reference with resolution of 2.45/1023 (V/dec). The 2 LSBs of the 10-bit ADC measurement of LHI pin voltage.|


***7.6.5.4 LHIH Measurement (address = 0x21)***

Figure 7-55 shows the LHIH register. Table 7-44 describes the LHIH register.

**Fi** **g** **ure 7-55. Lim** **p** **-Home Mode External Current Reference** **(** **MSB** **)**

7 6 5 4 3 2 1 0

LHI[9:2]

R-00000000b

**Table 7-44. Lim** **p** **-Home Mode External Current Reference Field Descri** **p** **tion**

***7.6.5.5 LHIFILTL Register (address = 0x22)***

Table 7-45 shows the LHIFILTL register. Table 7-46 describes the LHIFILTL register.

**Table 7-46. Lim** **p** **-Home Mode Filtered External Current Field Descri** **p** **tion**

***7.6.5.6 LHIFILTH Register (address = 0x23)***

Table 7-47 shows the LHIFILTH register. Table 7-48 describes the LHIFILTH register.

**Table 7-47. Lim** **p** **-Home Mode Filtered External Current Re** **g** **ister** **(** **MSB** **)**

7 6 5 4 3 2 1 0

LHIFILT[9:2]

R-00000000b

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|LHI[9:2]|R|00000000|External current reference in limp-home mode. The LHI input voltage is digitized to achieve a 10-bit reference with resolution of 2.45/1023 (V/dec). The 8 MSBs of the 10-bit ADC measurement of LHI pin voltage.|


|Table 7-45. Limp-Home Mode Filtered External Current Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LHIFILT[1:0]|
|R-000000b R-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|LHIFLT[1:0]|R|00|Filtered ADC measurement of LHI input. The register reports the 2-LSB of the low- pass filtered LHI input voltage. This register is only updated when LHIFILTH is read. This means that LHIFILTH must always be read first, then LHIFILTL (read LHIFILTL only if 10-bit resolution is desired).|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 51

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Table 7-48. Lim** **p** **-Home Mode Filtered External Current Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.7 LH1IADJL Register (address = 0x24) [reset = 0x00]***

Figure 7-56 shows the LH1IADJL register. Table 7-49 describes the LH1IADJL register.

**Table 7-49. Channel 1 Lim** **p** **-Home Mode Analo** **g** **Current Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.8 LH1IADJH Register (address = 0x25) [reset = 0x00]***

Figure 7-57 shows the LH1IADJH register. Table 7-50 describes the LH1IADJH register.

**Fi** **g** **ure 7-57. Channel 1 Lim** **p** **-Home Mode Analo** **g** **Current Re** **g** **ister** **(** **MSB** **)**

7 6 5 4 3 2 1 0

LH1IADJ[9:2]

R/W-00000000b

**Table 7-50. Channel 1 Lim** **p** **-Home Mode Analo** **g** **Current Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.9 LH2IADJL Register (address = 0x26) [reset = 0x00]***

Figure 7-58 shows the LH2IADJL register. Table 7-51 describes the LH2IADJL register.

**Table 7-51. Channel 2 Lim** **p** **-Home Mode Analo** **g** **Current Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.10 LH2IADJH Register (address = 0x27) [reset = 0x00]***

Figure 7-59 shows the LH2IADJH register. Table 7-52 describes the LH2IADJH register.

**Fi** **g** **ure 7-59. Channel 2 Lim** **p** **-Home Mode Analo** **g** **Current Re** **g** **ister** **(** **MSB** **)**

7 6 5 4 3 2 1 0

LH2IADJ[9:2]

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|1-0|LHIFLT[9:2]|R|00000000|Filtered ADC measurement of LHI input. The register reports the 8-MSB of the low- pass filtered LHI input voltage. LHIFILTH register can be read repeatedly without reading LHIFILTL register if 8-bit resolution is sufficient.|


|Figure 7-56. Channel 1 Limp-Home Mode Analog Current Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LH1IADJ[1:0]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|LH1IADJ[1:0]|R/W|00|Channel 1 analog current control in limp-home mode. The 2 LSBs of the 10-bit IADJ DAC for channel 1 can be programmed by writing to the register.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|LH1IADJ[9:2]|R/W|00000000|Channel 1 analog current control in limp-home mode. The 8 MSBs of the 10-bit IADJ DAC for channel 1 can be programmed by writing to the register.|


|Figure 7-58. Channel 2 Limp-Home Mode Analog Current Register (LSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LH2IADJ[1:0]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|LH2IADJ[1:0]|R/W|00|Channel 2 analog current control in limp-home mode. The 2 LSBs of the 10-bit IADJ DAC for channel 2 can be programmed by writing to the register.|



52 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Figure 7-59. Channel 2 Limp-Home Mode Analog Current Register (MSB) (continued)**

R/W-00000000b

**Table 7-52. Channel 2 Lim** **p** **-Home Mode Analo** **g** **Current Re** **g** **ister Field Descri** **p** **tion**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|LH2IADJ[9:2]|R/W|00000000|Channel 2 analog current control in limp-home mode. The 8 MSBs of the 10-bit IADJ DAC for channel 2 can be programmed by writing to the register.|


***7.6.5.11 LH1PWML Register (address = 0x28) [reset = 0x00]***

Figure 7-60 shows the LH1PWML register. Table 7-53 describes the LH1PWML register.

**Fi** **g** **ure 7-60. Channel 1 Lim** **p** **-Home Mode PWM Width Re** **g** **ister** **(** **LSB** **)**

7 6 5 4 3 2 1 0

LH1PWM[7:0]

R/W-00000000b

**Table 7-53. Channel 1 Lim** **p** **-Home Mode PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.12 LH1PWMH Register (address = 0x29) [reset = 0x00]***

Figure 7-61 shows the LH1PWMH register. Table 7-54 describes the LH1PWMH register.

**Table 7-54. Channel 1 Lim** **p** **-Home Mode PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.13 LH2PWML Register (address = 0x2A) [reset = 0x00]***

Figure 7-62 shows the LH2PWML register. Table 7-55 describes the LH2PWML register.

**Fi** **g** **ure 7-62. Channel 2 Lim** **p** **-Home Mode PWM Width Re** **g** **ister** **(** **LSB** **)**

7 6 5 4 3 2 1 0

LH2PWM[7:0]

R/W-00000000b

**Table 7-55. Channel 2 Lim** **p** **-Home Mode PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.14 LH2PWMH Register (address = 0x2B) [reset = 0x00]***

Figure 7-63 shows the LH2PWMH register. Table 7-56 describes the LH2PWMH register.

**Fi** **g** **ure 7-63. Channel 2 Lim** **p** **-Home Mode PWM Width Re** **g** **ister** **(** **MSB** **)**

7 6 5 4 3 2 1 0

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|LH1PWM[7:0]|R/W|00000000|Channel 1 PWM width control in limp-home mode. The 8 LSBs of the 10-bit PWM WIDTH for channel 1 can be programmed by writing to the register.|


|Figure 7-61. Channel 1 Limp-Home Mode PWM Width Register (MSB)|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LH1PWM[9:8]|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|LH1PWM[9:8]|R/W|00|Channel 1 PWM width control in limp-home mode. The 2 MSBs of the 10-bit PWM WIDTH for channel 1 can be programmed by writing to the register.|


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|LH2PWM[7:0]|R/W|00000000|Channel 2 PWM width control in limp-home mode. The 8 LSBs of the 10-bit PWM WIDTH for channel 2 can be programmed by writing to the register.|



Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 53

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

**Figure 7-63. Channel 2 Limp-Home Mode PWM Width Register (MSB) (continued)**

**Table 7-56. Channel 2 Lim** **p** **-Home Mode PWM Width Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.15 LH1TON Register (address = 0x2C) [reset = 0x07]***

Figure 7-64 shows the LH1TON register. Table 7-57 describes the LH1TON register.

**Table 7-57. Channel 1 Lim** **p** **-Home Mode On-Time Re** **g** **ister Field Descri** **p** **tion**

***7.6.5.16 LH2TON Register (address = 0x2D) [reset = 0x07]***

Figure 7-65 shows the LH2TON register. Table 7-58 describes the LH2TON register.

**Table 7-58. Channel 2 Lim** **p** **-Home Mode On-Time Re** **g** **ister Field Descri** **p** **tion**

**7.6.6 RESET Register (address = 0x2E) (Write-Only)**

Figure 7-66 shows the RESET register. Table 7-59 describes the RESET register. RESET command does not
reset the PC bit in the STATUS3 register to the power-on default value.

**Fi** **g** **ure 7-66. RESET Re** **g** **ister**

7 6 5 4 3 2 1 0

RESET[7:0]

W-00000000b

|RESERVED|LH2PWM[9:8]|
|---|---|
|R-000000b R/W-00b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|000000|Reserved|
|1-0|LH2PWM[9:8]|R/W|00|Channel 2 PWM width control in limp-home mode. The 2 MSBs of the 10-bit PWM WIDTH for channel 2 can be programmed by writing to the register.|


|Figure 7-64. Channel 1 Limp-Home Mode On-Time Register|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LH1TON[5:0]|
|R-00b R/W-000111b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R|00|Reserved|
|5-0|LH1TON[5:0]|R/W|000111|Channel 1 on-time control in limp-home mode. The pseudo-fixed switching frequency for channel 1 is set by writing to this register. Default value is set to ensure 437-kHz switching frequency.|


|Figure 7-65. Channel 2 Limp-Home Mode On-Time Register|Col2|
|---|---|
|7 6 5 4 3 2 1 0||
|RESERVED|LH2TON[5:0]|
|R-00b R/W-000111b||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R|00|Reserved|
|5-0|LH2TON[5:0]|R/W|000111|Channel 2 on-time control in limp-home mode. The pseudo-fixed switching frequency for channel 2 is set by writing to this register. Default value is set to ensure 437-kHz switching frequency.|



54 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**Table 7-59. RESET Re** **g** **ister Field Descri** **p** **tion**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|RESET|W|00000000|Write 0xC3 to the RESET register to reset all writable registers to their default values. If the logic is in stand-alone mode, writing 0xC3 returns the channel enable state machines to the LOAD state. Watchdog timer is disabled.|
|||||Write 0xD4 to the RESET register to reset all writable registers to their default values. If the logic is in stand-alone mode, reading the STATUS3 register to clear the CMWTO bits and then writing 0xD4 to the RESET register returns the channel enable state machines to the DETECT state. Watchdog timer is enabled.|
|||||This register is write-only. Reads of this register return 0.|


Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 55

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
##### **8 Application and Implementation**

**Note**

Information in the following applications sections is not part of the TI component specification, and TI
does not warrant its accuracy or completeness. TI’s customers are responsible for determining
suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.
###### **8.1 Application Information**

Figure 8-1 shows a schematic of a typical application for the TPS92520-Q1.

LED1+

C COMP1

1 32

COMP1 CSN1

C OUT1 2 R CS1

UDIM1

31

CSP1

R UV12 R UV11 3 PGND BST1 30

4 L 1

GND PGND

29 C BST1

SW1

C IN1 5 28

V IN VIN1 SW1

6

VIN1

27

FLT

7

GND

26

5V C V5D 8 LHI

V5D

Supply 9 SSN 25

V5A

24

SCK SPI

C V5A 10 MISO 23 BUS

GND

22

MOSI

11

VIN2

12 21

V IN VIN2 SW2

20

SW2

C IN2 13

GND PGND

14 19 C BST2 L 2

PGND BST2

R UV22 R UV21

18

CSP2

15

UDIM2

C OUT2 C COMP2 16 17 R CS2

COMP2 CSN2

LED2+

**Figure 8-1. Buck LED Driver**

**8.1.1 Duty Cycle Consideration**

The switch duty cycle, D, defines the converter operation and is a function of the input and output voltages. In
steady state, the duty cycle is defined using Equation 15:


D V CSN
V IN


(15)


There is no limitation for small duty cycles, since at low duty cycles, the switching frequency is reduced as
needed to always ensure current regulation. The maximum duty cycle attainable is limited by the minimum offtime duration and is a function of switching frequency.

56 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

**8.1.2 Switching Frequency Selection**

Nominal switching frequency (t ON - t ON(MIN) ) is set by programming the CHxTON register. The switching varies
slightly over operating range and temperature based on converter efficiency. Table 8-1 shows common switching
frequencies and corresponding CHxTON register values.

**8.1.3 LED Current Set Point**

|Col1|Table 8-1. Frequency Setting|Col3|
|---|---|---|
|FREQUENCY|CHxTON REGISTER VALUE (DECIMAL)|CHxTON REGISTER VALUE (BINARY)|
|220 kHz|3|000011|
|437 kHz|7|000111|
|1.064 MHz|19|010011|
|1.66 MHz|31|011111|
|2.23 MHz|43|101011|



The LED current is set by the external resistor, R CS, and the CHxIADJ register value. The current sense resistor,
R CS, is selected to meet the maximum LED current specification and 90% of the full-scale range of CHxIADJDAC.

0.9 u V

DAC(FS)

R CS
14 Iu

LED(MAX) (16)

The LED current can be varied between minimum and maximum specified limits by writing to the CHxIADJ
register.

**8.1.4 Inductor Selection**

The inductor is sized to meet the ripple specification at 50% duty cycle. TI recommends a minimum of 30%
peak-to-peak inductor ripple to ensure periodic switching operation. Use Equation 17 to calculate the inductor
value.

V

IN(TYP)

L
4 u 'i L u f SW (17)

Use Equation 18 and Equation 19 to calculate the RMS and peak currents through the inductor. It is important
that the inductor is rated to handle these currents.

§ 'i 2         
i ¨I 2 � L(MAX) ¸
L(RMS) LED(MAX)

¨ 12 ¸
© ¹
(18)

'i

L(MAX)
i L(PK) I LED(MAX) �
2 (19)

**8.1.5 Output Capacitor Selection**

The output capacitor value depends on the total series resistance of the LED string, r D, and the switching
frequency, f SW . The capacitance required for the target LED ripple current is calculated using *Equation 20* .

'i

L(MAX)

C OUT
8 u f SW u r D u 'i LED (20)

For applications where the converter supports pixel beam or matrix LED loads, additional design considerations
influence the selection of output capacitor. The size of the output capacitor depends on the slew-rate control of

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 57

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

the LED bypass switches and must be carefully selected while considering the overshoot current created by the
dv/dt of the bypass switch.

When choosing the output capacitors, it is important to consider the ESR and ESL characteristics since they
directly impact the LED current ripple. Ceramic capacitors are the best choice due to the following:

 - Low ESR

 - High ripple current rating

 - Long lifetime

 - Good temperature performance

With ceramic capacitor technology, it is important to consider the derating factors associated with higher
temperature and DC bias operating conditions. TI recommends an X7R dielectric with a voltage rating greater
than maximum LED stack voltage.

**8.1.6 Input Capacitor Selection**

The input capacitor buffers the input voltage for transient events and decouples the converter from the supply. TI
recommends a 2.2-µF input capacitor across the VIN pin and PGND placed close to the device, and connected
using wide traces. X7R-rated ceramic capacitors are the best choice due to the low ESR, high ripple current
rating, and good temperature performance. Additional capacitance can be required to further limit the input
voltage deviation during PWM dimming operation.

**8.1.7 Bootstrap Capacitor Selection**

The bootstrap capacitor biases the high-side gate driver during the high-side FET on-time. The required
capacitance depends on the PWM dimming frequency, PWM FREQ, and is sized to avoid boot undervoltage and
fault during PWM dimming operation. The bootstrap capacitance, C BST, is calculated using *Equation 21* .

I

Q(BST)

C BST
#### � V 5D � V BST(HYS) � V BST(UV) � u PWM FREQ (21)

Table 8-2 summarizes the TI recommended bootstrap capacitor value for different PWM dimming frequencies.

**Table 8-2. Bootstra** **p** **Ca** **p** **acitor Value**

**8.1.8 Compensation Capacitor Selection**

A simple integral compensator is recommended to achieve stable operation across the wide operating range.
The bode plot of the loop gain with different compensation capacitors is shown in Figure 8-2. The buck converter
behaves as a single pole system with additional phase lag caused by the switching behavior. The gain and
phase margin is then determined by the choice of the switching frequency and is independent of other design
parameters. TI recommends a 1-nF to 10-nF capacitor to achieve bandwidth between 4 kHz and 40 kHz. The
choice of compensation capacitor impacts the transient response, the shunt FET dimming behavior and PWM
dimming performance. A larger compensation capacitor (lower bandwidth) is recommended to limit the LED
current overshoot on the rising edge of internal or external PWM signal. A smaller compensation capacitor
(higher bandwidth) is recommend to improve shunt FET dimming response.

|PWM DIMMING FREQUENCY (Hz)|BOOTSTRAP CAPACITOR (µF)|
|---|---|
|1507|0.1|
|1318|0.15|
|1055|0.22|
|879|0.22|
|659|0.33|
|439|0.47|
|215|1|
|108|2|



58 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|2. 1|2 nF|nF|Col37|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||3. 4. 6.|3 7 8|nF nF nF||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||10|n|F||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||


1000 2000 3000 5000 10000 20000 50000 100000 200000 500000 1000000 2000000 5000000 1E+7

Frequency (Hz)

L = 68 µH, f SW = 437 kHz

**Figure 8-2. Simulated Bode Plot of Loop Gain**

**8.1.9 Input Undervoltage Protection**

Figure 8-1 shows that the undervoltage protection threshold is programmed using a resistor divider, R UV1 and
R UV2, from the input voltage, V IN, to ground. Use Equation 22 and Equation 23 to calculate the resistor values.


R UVx2 V HYS
I

UDIM(UVLO)


(22)


V

UDIM(RISE)

R UVx1 V � V u R UVx2

INx(RISE) UDIM(RISE) (23)

**8.1.10 CSN Protection Diode**

An external Schottky diode is selected to protect the CSP / CSN node by clamping the negative voltage during
short circuit transient. The Schottky diode should be selected based on the length of the cable harness and the
choice of output capacitor. A Schottky diode with low forward voltage drop at room-temperature and nonrepetitive peak surge current rating of 10 A for duration of 5 µs is recommended. The diode should be located
close to the CSN pin.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 59

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
###### **8.2 Typical Application**

VLED2


C2

1uF GND

CH2_EN


2200pF

C4

C7

2.2uF

C9



GND


D1

60V


GND


CH1_EN



R1

0.33W

0.1

5V

R5

0.33W

0.1

|U1|Col2|
|---|---|
|COMP1 CSN1 UDIM1 CSP1 PGND BST1 PGND SW1 VIN1 SW1 VIN1 FLT GND LHI V5D SSN V5A SCK GND MISO VIN2 MOSI VIN2 SW2 PGND SW2 PGND BST2 UDIM2 CSP2 COMP2 CSN2||
||17|


**Figure 8-3. Application Schematic**

**8.2.1 Design Requirements**

|Col1|Col2|Table 8-3. Design Parameters|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|PARAMETER||CONDITIONS|MIN|TYP|MAX|UNIT|
|V IN|Input Voltage||58|60|62|V|
|N S|Number of LEDs||1||16||
|V FLED|LED forward voltage drop||2.8|3|3.4|V|
|r D|LED string series resistance|N x r D(LED)|0.1||1.6|Ω|
|V OUT|Output voltage|Ns x V FLED|2.8||54.4|V|
|I LED|LED current||100||1600|mA|
|Δi LED|LED current ripple|Defined as percentage peak-to-peak at maximum LED current. 5 % of maximum LED current.|||80|mA|
|Δi L|Inductor current ripple|Defined as percentage peak-to-peak at maximum LED current||30||%|
|V IN(RISE)|Start input voltage|Input voltage rising||54||V|
|V IN(FALL)|Stop input voltage|Input voltage falling||52||V|
|f PWM|PWM frequency|||439||Hz|
|D PWM|PWM dimming duty cycle||4||100|%|
|f SW|Switching frequency|||437||kHz|
|T A|Ambient temperature|||25||°C|



60 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**

***8.2.1.1 Detailed Design Procedure***

**8.2.1.1.1 Calculating Duty Cycle**

Solve for duty cycle D, D MAX, and D MIN :

V OUT(MAX) 54.4
D MAX 0.938
V 58

IN(MIN)


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

(24)

(25)


V OUT(MIN) 2.8
D MIN 0.0452
V 62

IN(MAX) (25)

**8.2.1.1.2 Calculating Minimum On-Time and Off-Time**

Solve for minimum on-time, t ON(DMIN) at minimum duty cycle and minimum off-time, t OFF(DMAX) at maximum duty
cycle:


V OUT(MIN) 1 2.8 1 �9
t u u 103.3 10u

ON(DMIN) V IN(MAX) f SW 62 437 10u 3 (26)

V OUT(MAX) 1 54.4 1 �9
t u u 142 10u

ON(DMAX) V IN(MIN) f SW 58 437 10u 3 (27)

**8.2.1.1.3 Minimum Switching Frequency**

Confirm minimum switching frequency at t ON(DMIN), f SW(MIN) :

V OUT(MIN) 2.8 3
f SW(MIN) t ON(DMIN) u V IN(MAX) 103.3 10u �9 u 62 437.2 10u (28)

For the design specification, t ON(DMIN) - t ON(MIN) and f SW(MIN) = f SW .

**8.2.1.1.4 LED Current Set Point**

Solve for sense resistor, R CS :

0.9 u V DAC(FS) 0.9 u 2.45
R CS 0.0984
14 Iu 14 1.6u

LED(MAX) (29)

A standard resistor of 100 mΩ with tolerance better than 1 % and low temperature coefficient is selected.

**8.2.1.1.5 Inductor Selection**

The inductor is selected to meet the recommended 30% peak-to-peak inductor ripple specification:

V IN(TYP) V IN(TYP) 60 �6
L 71.5 10u
4 u 'i L u f SW 4 u 0.3 Iu LED(MAX) u f SW 4 u 0.3 1.6u u 437x10 3 (30)

The closest standard capacitor is 68 µH.

 - Lower inductor values increase the peak-to-peak inductor current, which minimizes size and cost at the
expense of reduced efficiency and larger output capacitor.

 - Higher inductance values decrease the peak-to-peak inductor current, which increases efficiency but reduces
the operating range based on minimum sense voltage ripple, ΔV (CSP-CSN) specification.

**8.2.1.1.6 Output Capacitor Selection**

The minimum output capacitance is selected to meet the LED current ripple specification:

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 61

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

'i L(MAX) 0.48 �6

C OUT 8 u f SW u r D(MAX) u 'i LED(MAX) 8 u 437 10u 3 u1.6 u 80 10u �3 1.07 10u (31)

A standard 1-µF, 100-V X7R capacitor is selected.

**8.2.1.1.7 Bootstrap Capacitor Selection**

Referring to Table 8-2, a standard 470-nF, 16-V X7R capacitor is selected to support PWM frequency of 439 Hz.

**8.2.1.1.8 Compensation Capacitor Selection**

A compensation capacitor of 2.2 nF is selected to achieve balanced transient response between PWM dimming
and shunt FET dimming.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||||||2. 1|2 nF|nF||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||3. 4. 6.|3 7 8|nF nF nF||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||10|n|F||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||



1000 2000 3000 5000 10000 20000 50000 100000 200000 500000 1000000 2000000 5000000 1E+7

Frequency (Hz)

**Figure 8-4. Simulated Buck Converter Bode Plot**

**8.2.1.1.9 External Channel Enable and PWM dimming**

The device channel enable function and external PWM signal is achieved by controlling UDIM input via
microcontroller. The device modulates the LED current based on the PWM duty cycle of the external signal.
Input undervoltage lockout function is implemented by reading the VIN register value sampled by ADC. Refer to
the *Section 7.3.12* section for further details regarding ADC sampling and measurement.

62 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

|8.2.2 Application Curves|Col2|
|---|---|
|Ch1: SW voltage (10 V/div); Ch3: Inductor current (200 mA/ div); Ch4: COMP voltage (400 mV/div); Time: 50 µs/div Figure 8-5. Start-up Transient|Ch1: SW voltage (10 V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (200 mA/div); Time: 1 µs/div Figure 8-6. Normal Operation|
|Ch1: SW voltage (10V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (200 mA/div); Ch4: LED current (200 mA/div); Time: 500 µs/div Figure 8-7. Internal PWM Dimming Transient|Ch1: SW voltage (10V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (200 mA/div); Ch4: LED current (200 mA/div); Time: 5 µs/div Figure 8-8. Internal PWM Dimming (Rising Edge)|
|Ch1: SW voltage (10V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (200 mA/div); Ch4: LED current (200 mA/div); Time: 5 µs/div Figure 8-9. Internal PWM Dimming (Falling Edge)|Ch1: SW voltage (10 V/div); Ch2: Output voltage (4 V/div); Ch4: LED current (200 mA/div); Time: 400 µs/div Figure 8-10. Shunt Dimming with Matrix Manager|


Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 63

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**

|Ch1: SW voltage (10 V/div); Ch2: Output voltage (4 V/div); Ch4: LED current (200 mA/div); Time: 400 µs/div Figure 8-11. Shunt Dimming (LEDs ON-OFF Transient)|Ch1: SW voltage (10 V/div); Ch2: Output voltage (4 V/div); Ch4: LED current (200 mA/div); Time: 50 µs/div Figure 8-12. Shunt Dimming (LEDs OFF to LEDs ON)|
|---|---|
|Ch1: SW voltage (10 V/div); Ch2: Output voltage (4 V/div); Ch4: LED current (200 mA/div); Time: 50 µs/div Figure 8-13. Shunt Dimming (LEDs ON to LEDs OFF)|Ch1: SW voltage (10V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (200 mA/div); Ch4: LED current (200 mA/div); Time: 50 µs/div Figure 8-14. Output Short Circuit Fault|
|Ch1: SW voltage (10V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (200 mA/div); Ch4: LED current (200 mA/div); Time: 40 µs/div Figure 8-15. Output Short Circuit Fault Recovery|Ch1: SW voltage (10V/div); Ch2: Output voltage (4 V/div); Ch3: Inductor current (400 mA/div); Ch4: LED current (200 mA/div); Time: 40 µs/div Figure 8-16. Output Open Circuit Fault|



64 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

**[www.ti.com](https://www.ti.com)** SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021
###### **8.3 Initialization Setup**

The device is enabled with default watchdog timer on power up, V 5D - V 5D(POR) .

**8.3.1 Initialize Device without Watchdog timer**

The following steps must be implemented before the default watchdog timer times out in 1.55 s (typ).
1. Read register 0x05 to clear the PC (Power Cycle) bit (D2).
2. Write byte 0x00 to register 0x00. This will set bit D7 to 0 and reset FLT indicator. It also set bit D4 to 0 and
disable the watchdog timer and bit .
3. Configure the device by writing to registers 0x00 to 0x02 and 0x06 to 0x12. The channels are disabled by
setting CHxEN to 0 (register 0x00 bits D2 and D0).
4. Enable channels by setting ChxEN bits to 1. Write D2 and D0 bits to 1 in register 0x00.

If the watchdog timer is not disabled or the device does not receive a valid SPI command in 1.55 s after power
up, the device will transition to standalone mode. The operation in standalone mode can be detected by reading
register 0x05. If bit D7 is set then the device is operating in standalone mode. To exit standalone mode, write
byte 0xC3.

**8.3.2 Initialize Device with Watchdog Timer**

The following steps must be implemented before the default watchdog timer times out in 1.55 s (typ).
1. Read register 0x05 to clear the PC (Power Cycle) bit (D2).
2. Write byte 0x10 to register 0x00. This will set bit D7 to 0 and reset the FLT indicator. Watchdog timer enabled
by setting bit D4 to 1.
3. To change the default watchdog timeout value, modify the contents of register 0x02 to select the desired
watchdog timeout period.
4. Repeatedly write or read a register within the specified period in step 2 in order to avoid triggering a
watchdog timer time out event.
5. Configure the device by writing to registers 0x00 to 0x02 and 0x06 to 0x12. The channels are disabled by
setting CHxEN to 0 (register 0x00 bits D2 and D0).
6. Enable channels by setting ChxEN bits to 1. Write D2 and D0 bits to 1 in register 0x00.

If the watchdog timer is not disabled or the device does not receive a valid SPI command in 1.55 s after power
up, the device will transition to standalone mode. The operation in standalone mode can be detected by reading
register 0x05. If bit D7 is set then the device is operating in standalone mode. To exit standalone mode, write
byte 0xD4 to register 0x2E.

**8.3.3 Limp-Home Mode**

The following steps must be implemented to program the limp-home mode.
1. Enable limp-home mode by enabling watchdog timer by setting D4 bit to 1 in register 0x00.
2. Configure limp-home mode by writing to registers 0x1E to 0x2D.
3. Test limp-home configuration by toggling LHSW bit (D5) in register 0x00.

Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 65

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
##### **9 Power Supply Recommendations**

This device is designed to operate from an input voltage supply range between 4.5 V and 65 V. The input can be
a car battery or another preregulated power supply. Additional bulk capacitance or an input filter can be required
in addition to the ceramic bypass capacitors to address converter stability, noise, and EMI concerns. **10 Layout**
###### **10.1 Layout Guidelines**

The performance of any switching converter depends as much on the layout of the PCB as the component
selection. The following guidelines can help you design a PCB with the best power converter performance.

 - Place ceramic high-frequency bypass capacitors as close as possible to the TPS92520-Q1 VIN and PGND
pins. Grounding for both the input and output capacitors must consist of localized top side planes that
connect to the PGND pins.

 - Place bypass capacitors for V5D and V5A close to the pins and ground the capacitors to device ground.

 - Differentially route the CSP and CSN pins to sense resistor. Route the traces away from noisy nodes,
preferably through a layer on the other side of a shielding/ground layer.

 - Use ground plane in one of the middle layers for noise shielding.

 - Make VIN and ground connection as wide as possible. This reduces any voltage drops on the input of the
converter and maximizes efficiency.

**10.1.1 Compact Layout for EMI Reduction**

Radiated EMI is generated by the high di/dt from pulsing currents in switching converters. The larger the area
covered by the path of a pulsing current, the more electromagnetic emission is generated. The key to minimize
radiated EMI is to identify the pulsing current path and minimize the area of the path. In buck converters, the
pulsing current path is from the VIN side of the input capacitors through the HS switch, through the LS switch,
and then returns to the ground of the input capacitor.

High-frequency ceramic bypass capacitors at the input side provide primary path for the high di/dt components of
the pulsing current. Placing ceramic capacitors as close as possible to the VIN and PGND pins is the key to EMI
reduction.

The PCB copper connection of the SW pin to the inductor must be as short as possible and just wide enough to
carry the LED current without excessive heating. Short, thick traces or, copper pours (shapes), must be used for
high current conduction path to minimize parasitic resistance. Place the output capacitor close to the CSN pin
and grounded closely to the PGND pin.

***10.1.1.1 Ground Plane***

TI recommends using one of the middle layers as a solid ground plane. The ground plane provides shielding for
sensitive circuits and traces. It also provides a quiet reference potential for the control circuitry. Connect the GND
and PGND pins to the ground plane using vias right next to the bypass capacitors. PGND pins are connected to
the source of the internal LS switch. They must be connected directly to the grounds of the input and output
capacitors. The PGND net contains noise at the switching frequency and can bounce due to load variations.

66 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **10.2 Layout Example**


**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**

SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021

|Col1|1|
|---|---|


|Col1|2|
|---|---|


|Col1|3|
|---|---|


|Col1|4|
|---|---|


|Col1|5|
|---|---|


|Col1|6|
|---|---|


|Col1|7|
|---|---|


|Col1|8|
|---|---|


|Col1|9|
|---|---|


|Col1|10|
|---|---|


|Col1|11|
|---|---|


|Col1|12|
|---|---|


|Col1|13|
|---|---|


|Col1|14|
|---|---|


|Col1|15|
|---|---|


|Col1|16|
|---|---|



**Figure 10-1. TPS92520-Q1 Layout Example**

|32|Col2|
|---|---|

|31|Col2|
|---|---|

|30|Col2|
|---|---|

|29|Col2|
|---|---|

|28|Col2|
|---|---|

|27|Col2|
|---|---|

|26|Col2|
|---|---|

|25|Col2|
|---|---|

|24|Col2|
|---|---|

|23|Col2|
|---|---|

|22|Col2|
|---|---|

|21|Col2|
|---|---|

|20|Col2|
|---|---|

|19|Col2|
|---|---|

|18|Col2|
|---|---|

|17|Col2|
|---|---|


Copyright © 2021 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* 67

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

**[TPS92520-Q1](https://www.ti.com/product/TPS92520-Q1)**
SLUSD66D – SEPTEMBER 2019 – REVISED FEBRUARY 2021 **[www.ti.com](https://www.ti.com)**
##### **11 Device and Documentation Support**
###### **11.1 Documentation Support**

**11.1.1 Related Documentation**

For related documentation see the following:

Texas Instruments, *[TPS92520-Q1 Launchpad Evaluation Module User's Guide](https://www.ti.com/lit/pdf/SLUUC29)* **11.2 Receiving Notification of Documentation Updates**

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on *Alert me* to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document. **11.3 Support Resources**

TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml) **11.4 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners. **11.5 Glossary**

**[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022)** This glossary lists and explains terms, acronyms, and definitions.
##### **12 Mechanical, Packaging, and Orderable Information**

The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

68 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSD66D&partnum=TPS92520-Q1)* Copyright © 2021 Texas Instruments Incorporated

Product Folder Links: *[TPS92520-Q1](https://www.ti.com/product/tps92520-q1?qgpn=tps92520-q1)*


-----

### **PACKAGE OPTION ADDENDUM**

www.ti.com 15-Feb-2021
###### **PACKAGING INFORMATION**


**Orderable Device** **Status**


**Package Type Package**


**Op Temp (°C)** **Device Marking**

(4/5)



**Eco Plan**

(2)


**MSL Peak Temp**

(3)


TPS92520QDADRQ1 ACTIVE HTSSOP DAD 32 2000 RoHS & Green NIPDAU Level-3-260C-168 HR -40 to 125 TPS

92520Q

TPS92520QDAPRQ1 ACTIVE HTSSOP DAP 32 2000 RoHS & Green NIPDAU Level-3-260C-168 HR -40 to 125 TPS92520Q

**(1)** The marketing status values are defined as follows:
**ACTIVE:** Product device recommended for new designs.
**LIFEBUY:** TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
**NRND:** Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
**PREVIEW:** Device has been announced but is not in production. Samples may or may not be available.
**OBSOLETE:** TI has discontinued the production of the device.

**(2)** **RoHS:** TI defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substance
do not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may
reference these types of products as "Pb-Free".
**RoHS Exempt:** TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.
**Green:** TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based
flame retardants must also meet the <=1000ppm threshold requirement.

**(3)** MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

**(4)** There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

**(5)** Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation
of the previous line and the two combined represent the entire Device Marking for that device.

**(6)** Lead finish/Ball material - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two
lines if the finish value exceeds the maximum column width.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information
provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and
continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals.
TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 1


-----

### **PACKAGE OPTION ADDENDUM**

www.ti.com 15-Feb-2021

Addendum-Page 2


-----

### **PACKAGE MATERIALS INFORMATION**

www.ti.com 29-Apr-2024
###### **TAPE AND REEL INFORMATION**


**REEL DIMENSIONS**

*All dimensions are nominal


**TAPE DIMENSIONS**

Reel Width (W1)

|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||W B0|
||||||||
||||||||
|vity|||A0||||


|A0|Dimension designed to accommodate the component width A0 Cavity|
|---|---|
|A0|Dimension designed to accommodate the component width|
|B0|Dimension designed to accommodate the component length|
|K0|Dimension designed to accommodate the component thickness|
|W|Overall width of the carrier tape|
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

Pack Materials-Page 1

|Device|Package Type|Package Drawing|Pins|SPQ|Reel Diameter (mm)|Reel Width W1 (mm)|A0 (mm)|B0 (mm)|K0 (mm)|P1 (mm)|W (mm)|Pin1 Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TPS92520QDADRQ1|HTSSOP|DAD|32|2000|330.0|24.4|8.6|11.5|1.6|12.0|24.0|Q1|
|TPS92520QDADRQ1|HTSSOP|DAD|32|2000|330.0|24.4|8.8|11.8|1.8|12.0|24.0|Q1|
|TPS92520QDAPRQ1|HTSSOP|DAP|32|2000|330.0|24.4|8.8|11.8|1.8|12.0|24.0|Q1|


-----

### **PACKAGE MATERIALS INFORMATION**

www.ti.com 29-Apr-2024

*All dimensions are nominal

Pack Materials-Page 2

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TPS92520QDADRQ1|HTSSOP|DAD|32|2000|350.0|350.0|43.0|
|TPS92520QDADRQ1|HTSSOP|DAD|32|2000|367.0|367.0|45.0|
|TPS92520QDAPRQ1|HTSSOP|DAP|32|2000|367.0|367.0|45.0|


-----

-----

## **PACKAGE OUTLINE**
# DAD0032A PowerPAD   TSSOP - 1.15 mm max hei TM g ht

~~SCALE~~ ~~1~~ . ~~600~~

PLASTIC SMALL OUTLINE

|Col1|0.1|C|
|---|---|---|


|C|A|B|
|---|---|---|



PowerPAD is a trademark of Texas Instruments.

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.
4. Reference JEDEC registration MO-153.

www.ti.com


-----

## **EXAMPLE BOARD LAYOUT**
# DAD0032A PowerPAD   TSSOP - 1.15 mm max hei TM g ht

PLASTIC SMALL OUTLINE

NOTES: (continued)

5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

www.ti.com


-----

## **EXAMPLE STENCIL DESIGN**
# DAD0032A PowerPAD   TSSOP - 1.15 mm max hei TM g ht

PLASTIC SMALL OUTLINE

NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
8. Board assembly site may have different recommendations for stencil design.

www.ti.com


-----

## **GENERIC PACKAGE VIEW**
# **DAP 32 PowerPAD TM  TSSOP - 1.2 mm max hei g ht**

**8.1 x 11, 0.65 mm pitch** PLASTIC SMALL OUTLINE

This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.

4225303/A

www.ti.com


-----

## **PACKAGE OUTLINE**
# DAP0032F SCALE 1.500 PowerPAD   TSSOP - 1.2 mm max hei TM g ht

PLASTIC SMALL OUTLINE

PowerPAD is a trademark of Texas Instruments.

NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.
4. Reference JEDEC registration MO-153.
5. Features may differ and may not be present.

www.ti.com


-----

## **EXAMPLE BOARD LAYOUT**
# DAP0032F PowerPAD   TSSOP - 1.2 mm max hei TM g ht

PLASTIC SMALL OUTLINE

NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
8. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
numbers SLMA002 (www.ti.com/lit/slma002) and SLMA004 (www.ti.com/lit/slma004).
9. Size of metal pad may vary due to creepage requirement.

www.ti.com


-----

## **EXAMPLE STENCIL DESIGN**
# DAP0032F PowerPAD   TSSOP - 1.2 mm max hei TM g ht

PLASTIC SMALL OUTLINE

NOTES: (continued)

|STENCIL THICKNESS|SOLDER STENCIL OPENING|
|---|---|
|0.1|4.60 X 4.54|
|0.125|4.11 X 4.06 (SHOWN)|
|0.15|3.75 X 3.71|
|0.175|3.47 X 3.43|


10. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
11. Board assembly site may have different recommendations for stencil design.

www.ti.com


-----

##### **IMPORTANT NOTICE AND DISCLAIMER**

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
Copyright © 2024, Texas Instruments Incorporated


-----

