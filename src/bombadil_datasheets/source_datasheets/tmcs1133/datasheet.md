**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)
# **TMCS1133 Precision 1MHz Hall-Effect Current Sensor With Reinforced Isolation** **Working Voltage, Overcurrent Detection and Ambient Field Rejection**



**1 Features**


- High continuous current capability: 80ARMS

- Robust reinforced isolation

- High accuracy

  - Sensitivity error: ±0.1%

  - Sensitivity thermal drift: ±20ppm/°C

  - Sensitivity lifetime drift: ±0.2%

  - Offset error: ±0.2mV

  - Offset thermal drift: ±10μV/°C

  - Offset lifetime drift: ±0.2mV

  - Non-linearity: ±0.1%

- High immunity to external magnetic fields

- Fast Response

  - Signal bandwidth: 1MHz

  - Response time: 120ns

  - Propagation delay: 50ns

  - Overcurrent detection response: 100ns

- Operating supply range: 3V to 5.5V

- Bidirectional and unidirectional current sensing

- Multiple sensitivity options:

  - Ranging from 20mV/A to 150mV/A

- Safety related certifications

  - UL 1577 Component Recognition Program

  - IEC/CB 62368-1


**2 Applications**


- [Solar Energy](https://www.ti.com/applications/industrial/grid-infrastructure/solar-energy/overview.html)

- [EV charging](https://www.ti.com/applications/industrial/energy-infrastructure/ev-charging/overview.html)

- [Power supplies](https://www.ti.com/applications/industrial/power-delivery/overview.html)

- [Industrial AC/DC](https://www.ti.com/solution/industrial-ac-dc)



**3 Description**


The TMCS1133 is a galvanically isolated Hall-effect
current sensor with industry leading isolation and
accuracy. An output voltage proportional to the
input current is provided with excellent linearity and
low drift at all sensitivity options. Precision signal
conditioning circuitry with built-in drift compensation is
capable of less than 1.4% maximum sensitivity error
over temperature and lifetime with no system level
calibration, or less than 0.9% maximum sensitivity
error including both lifetime and temperature drift with
a one-time calibration at room temperature.


AC or DC input current flows through an internal
conductor generating a magnetic field measured
by integrated, on-chip, Hall-effect sensors. Coreless construction eliminates the need for magnetic
concentrators. Differential Hall sensors reject
interference from stray external magnetic fields. Low
conductor resistance increases measurable current
ranges up to ±96A while minimizing power loss and
easing thermal dissipation requirements. Insulation
capable of withstanding 5kVRMS, coupled with a
minimum of 8mm creepage and clearance, provides
high levels of reliable lifetime reinforced working
voltage. Integrated shielding enables excellent
common-mode rejection and transient immunity.


Fixed sensitivity allows the device to operate from a
single 3V to 5.5V power supply, eliminating ratiometry
errors and improving supply noise rejection.


**Package Information**

|PART NUMBER|PACKAGE(1)|PACKAGE SIZE(2)|
|---|---|---|
|TMCS1133|DVG (SOIC, 10)|10.3mm × 10.3mm|



(1) For all available packages, see Section 12.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.










|Passive / PFC<br>Rectifier|DC V+|Bridge Driver|Col4|
|---|---|---|---|
|Passive / PFC<br>Rectifier|DC V–<br>**TMCS1133**|||









**Typical Application**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1
**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Device Comparison** ......................................................... 3
**5 Pin Configuration and Functions** ...................................4
**6 Specifications** .................................................................. 5

6.1 Absolute Maximum Ratings........................................ 5
6.2 ESD Ratings............................................................... 5
6.3 Recommended Operating Conditions.........................5
6.4 Thermal Information....................................................5
6.5 Power Ratings.............................................................6
6.6 Insulation Specifications............................................. 6
6.7 Safety-Related Certifications...................................... 6
6.8 Safety Limiting Values.................................................7
6.9 Electrical Characteristics.............................................8
6.10 Typical Characteristics............................................ 10
**7 Parameter Measurement Information** .......................... 14

7.1 Accuracy Parameters................................................14
7.2 Transient Response Parameters.............................. 17
7.3 Safe Operating Area................................................. 18
**8 Detailed Description** ......................................................20



8.1 Overview................................................................... 20
8.2 Functional Block Diagram......................................... 21
8.3 Feature Description...................................................21
8.4 Device Functional Modes..........................................27
**9 Application and Implementation** .................................. 27

9.1 Application Information............................................. 27
9.2 Typical Application.................................................... 30
9.3 Power Supply Recommendations.............................33
9.4 Layout....................................................................... 33
**10 Device and Documentation Support** ..........................34

10.1 Device Nomenclature..............................................34
10.2 Device Support....................................................... 34
10.3 Documentation Support.......................................... 34
10.4 Receiving Notification of Documentation Updates..35
10.5 Support Resources................................................. 35
10.6 Trademarks............................................................. 35
10.7 Electrostatic Discharge Caution..............................35
10.8 Glossary..................................................................35
**11 Revision History** .......................................................... 35
**12 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 36



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**4 Device Comparison**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



**Table 4-1. Device Comparison**





















|PRODUCT(3)|SENSITIVITY|ZERO CURRENT OUTPUT<br>VOLTAGE|I LINEAR MEASUREMENT RANGE(1)<br>IN|Col5|
|---|---|---|---|---|
|**PRODUCT**(3)|**SENSITIVITY**|**ZERO CURRENT OUTPUT**<br>**VOLTAGE**|**VS = 5V**|**VS = 3.3V**|
|TMCS1133A1A|25mV/A|2.5V|±96A(2)|–96A to 28A(2)|
|TMCS1133A2A|50mV/A|50mV/A|±48A(2)|–48A to 14A(2)|
|TMCS1133A3A|75mV/A|75mV/A|±32A|–32A to 9.3A|
|TMCS1133A4A|100mV/A|100mV/A|±24A|–24A to 7A|
|TMCS1133A5A|150mV/A|150mV/A|±16A|–16A to 4.7A|
|TMCS1133B7A|20mV/A|1.65V|–77.5A to 163A(2)|±77.5A(2)|
|TMCS1133B1A|25mV/A|25mV/A|–62A to 130A(2)|±62A(2)|
|TMCS1133B8A|33mV/A|33mV/A|–47A to 98.5A(2)|±47A(2)|
|TMCS1133B2A|50mV/A|50mV/A|–31A to 65A(2)|±31A|
|TMCS1133B3A|75mV/A|75mV/A|–20.7A to 43.3A(2)|±20.7A|
|TMCS1133B4A|100mV/A|100mV/A|–15.5A to 32.5A|±15.5A|
|TMCS1133B5A|150mV/A|150mV/A|–10.3A to 21.7A|±10.3A|
|TMCS1133C1A|25mV/A|0.33V|–9.2A to 183A(2)|–9.2A to 115A(2)|
|TMCS1133C2A|50mV/A|50mV/A|–4.6A to 91.4A(2)|–4.6A to 57.4A(2)|
|TMCS1133C9A|66mV/A|66mV/A|–3.4A to 69.2A(2)|–3.4A to 43.4A(2)|
|TMCS1133C3A|75mV/A|75mV/A|–3.1A to 60.9A(2)|–3.1A to 38.3A(2)|
|TMCS1133C4A|100mV/A|100mV/A|–2.3A to 45.7A(2)|–2.3A to 28.7A|
|TMCS1133C5A|150mV/A|150mV/A|–1.5A to 30.5A|–1.5A to 19.1A|


(1) Linear range limited by the maximum output swing to power supply (3V to 5.5V) and ground, not by thermal limitations.
(2) Current levels must remain below both allowable continuous DC/RMS and transient peak current safe operating areas to not exceed
device thermal limits. See the _Safe Operating Area_ section.
(3) For more information on the device name and device options, see the _Device Nomenclature_ section.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 3


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**5 Pin Configuration and Functions**





**VS**



Not to scale





**Figure 5-1. DVG Package 10-Pin SOIC Top View**


**Table 5-1. Pin Functions**



|PIN|Col2|TYPE|DESCRIPTION|
|---|---|---|---|
|**NO.**|**NAME**|**NAME**|**NAME**|
|1|IN+|Analog Input|Input current positive pin|
|2|IN–|Analog Input|Input current negative pin|
|3|GND|Analog|Ground|
|4|~~ALERT~~|Digital Output|Sensor diagnostics PWM output, open-drain active low. Connect pin to GND if not<br>used.|
|5|NC|-|Reserved. Pin can be connected to GND or left floating.|
|6|VOUT|Analog Output|Output voltage|
|7|~~OC~~|Digital Output|Overcurrent output, open-drain active low. Connect pin to GND if not used.|
|8|VOC|Analog Input|Overcurrent threshold. Sets overcurrent threshold. Connect pin to VS if not used.|
|9|VS|Analog|Power supply|
|10|VS|Analog|Power supply|


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**6 Specifications**

**6.1 Absolute Maximum Ratings**

over operating free-air temperature range (unless otherwise noted) [(1)]



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



|Col1|Col2|Col3|MIN MAX|UNIT|
|---|---|---|---|---|
|VS|Supply voltage|Supply voltage|GND – 0.3<br>6|V|
||Analog input|VOC|GND – 0.3<br>(VS) + 0.3|V|
||Analog output|VOUT|VOUT|VOUT|
||Digital output|~~ALERT~~,~~ OC~~|~~ALERT~~,~~ OC~~|~~ALERT~~,~~ OC~~|
||No Connection|NC|NC|NC|
|TJ|Junction temperature|Junction temperature|–65<br>165|°C|
|Tstg|Storage temperature|Storage temperature|–65<br>165|°C|


(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.


**6.2 ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±4000|V|
|V(ESD)|Electrostatic discharge|Charged-device model (CDM), per ANSI/ESDA/JEDEC JS-002(2)|±1000|±1000|



(1) JEDEC document JEP155 states that 500V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250V CDM allows safe manufacturing with a standard ESD control process.


**6.3 Recommended Operating Conditions**

over operating free-air temperature range (unless otherwise noted)

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VS|Operating supply voltage|3<br>5<br>5.5|V|
|TA (1)|Operating free-air temperature|–40<br>125|°C|



(1) Input current safe operating area is constrained by junction temperature. Recommended condition based on use with the
_[TMCS1133xEVM](https://www.ti.com/lit/pdf/sbau423)_ . Input current rating is derated for elevated ambient temperatures.


**6.4 Thermal Information**










|THERMAL METRIC(1)|Col2|TMCS1133(2)|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**DVG (SOIC-W-10)**|**DVG (SOIC-W-10)**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**10 PINS**|**10 PINS**|
|RθJA|Junction-to-ambient thermal resistance|27.9|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|26.8|26.8|
|RθJB|Junction-to-board thermal resistance|10.1|10.1|
|ΨJT|Junction-to-top characterization parameter|4.4|4.4|
|ΨJB|Junction-to-board characterization parameter|8.3|8.3|



(1) For more information about traditional and new thermal metrics, see the _[Semiconductor and IC Package Thermal Metrics](https://www.ti.com/lit/pdf/spra953)_ application
note.
(2) Applies when device is mounted on the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/sbau423)_ with 40A input current. For more details, see the _Safe Operating Area_
section.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 5


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**6.5 Power Ratings**
VS = 5.5V, TA = 125℃, TJ = 165℃, device soldered on the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/sbau423)_ .







|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|PD|Maximum power dissipation (both sides)||2.0|W|
|PD1|Maximum power dissipation (current input,<br>side-1)|IIN = 44A|1.9|W|
|PD2|Maximum power dissipation by (side-2)|VS = 5.5V, IQ = 14.5mA, no loads|0.1|W|


**6.6 Insulation Specifications**























|PARAMETER|Col2|TEST CONDITIONS|VALUE|UNIT|
|---|---|---|---|---|
|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|
|CLR|External clearance(1)|Shortest terminal-to-terminal distance through air|≥ 8|mm|
|CPG|External creepage(1)|Shortest terminal-to-terminal distance across the package surface|≥ 8|mm|
|CTI|Comparative tracking index|DIN EN 60112; IEC 60112|≥ 600|V|
||Material group|According to IEC 60664-1|I||
||Overvoltage category per IEC 60664-1|Rated mains voltage ≤ 600VRMS|I-IV||
|VIORM|Maximum repetitive peak isolation voltage|AC voltage (bipolar)|1697|VPK|
|VIOWM|Maximum reinforced isolation working voltage|AC voltage (sine wave); Time Dependent Dielectric Breakdown<br>(TDDB) test, < 1ppm fail rate, see_Input Isolation_ section.|950|VRMS|
|VIOWM|Maximum reinforced isolation working voltage|AC voltage (sine wave); Time Dependent Dielectric Breakdown<br>(TDDB) test, < 1ppm fail rate, see_Input Isolation_ section.|1343|VDC|
|VIOWM|Maximum basic isolation working voltage|AC voltage (sine wave); Time Dependent Dielectric Breakdown<br>(TDDB) test, < 1000ppm fail rate, see_Input Isolation_ section.|1200|VRMS|
|VIOWM|Maximum basic isolation working voltage|AC voltage (sine wave); Time Dependent Dielectric Breakdown<br>(TDDB) test, < 1000ppm fail rate, see_Input Isolation_ section.|1697|VDC|
|VIOTM|Maximum transient isolation voltage|VTEST = √~~2 ~~x VISO, t = 60s (qualification);<br>VTEST = 1.2 × VIOTM, t = 1s (100% production)|7071|VPK|
|VIOSM|Maximum surge isolation voltage(2)|Test method per IEC 62368-1, 1.2/50µs waveform,<br>VTEST = 1.3 × VIOSM (qualification)|10000|VPK|
|qpd|Apparent charge(3)|Method b1: At routine test (100% production) and preconditioning<br>(type test), Vini = 1.2 x VIOTM, tini = 1s, Vpd(m) = 1.875 × VIORM, tm =<br>1s|≤5|pC|
|CIO|Barrier capacitance, input to output(4)|VIO = 0.4 sin (2πft), f = 1MHz|0.6|pF|
|RIO|Isolation resistance, input to output(4)|VIO = 500V, TA = 25°C|>1012|Ω|
|RIO|Isolation resistance, input to output(4)|VIO = 500V, 100°C ≤ TA ≤ 125°C|>1011|Ω|
|RIO|Isolation resistance, input to output(4)|VIO = 500V at TS = 150°C|>109|Ω|
||Pollution degree||2||
|**UL 1577**|**UL 1577**|**UL 1577**|**UL 1577**|**UL 1577**|
|VISO|Withstand isolation voltage|VTEST = VISO, t = 60s (qualification);<br>VTEST = 1.2 × VISO, t = 1s (100% production)|5000|VRMS|


(1) Apply creepage and clearance requirements according to the specific equipment isolation standards of an application. Take care
to maintain the creepage and clearance distance of the board design to make sure that the mounting pads of the isolator on the
printed circuit board do not reduce this distance. Creepage and clearance on a printed circuit board become equal in certain cases.
Techniques such as inserting grooves, ribs, or both on a printed circuit board are used to help increase these specifications.
(2) Testing is carried out in air or oil to determine the intrinsic surge immunity of the isolation barrier.
(3) Apparent charge is electrical discharge caused by a partial discharge (pd).
(4) All pins on each side of the barrier tied together creating a two-terminal device.


**6.7 Safety-Related Certifications**

|UL|Col2|
|---|---|
|UL 1577 Component Recognition Program|Certified according to IEC 62368-1 CB|
|File number: E181974|Certificate number: US-43893-M1-UL|



6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



**6.8 Safety Limiting Values**
Safety limiting intends to minimize potential damage to the isolation barrier upon failure of input or output circuitry.









|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|IS|Safety input current (side 1)(1)|TJ = 165°C, TA = 25°C, see_Thermal Derating Curve, Side 1_.|80|ARMS|
|IS|Safety input, output, or supply current<br>(side 2)(1)|VI = 5V, TJ = 165°C, TA = 25°C, see_Thermal Derating Curve,_<br>_Side 2_.|1.35|1.35|
|PS|Safety input, output, or total power(1)|TJ = 165°C, TA = 25°C, see_Thermal Derating Curve, Both_<br>_Sides_.|6.8|W|
|TS|Safety temperature(1)||165|℃|


(1) The maximum safety temperature, TS, has the same value as the maximum junction temperature, TJ, specified for the device. The
IS and PS parameters represent the safety current and safety power respectively. The maximum limits of IS and PS must not be
exceeded. These limits vary with the ambient temperature, TA as shown in the _Safe Operating Area_ section when used in the
_[TMCS1133xEVM](https://www.ti.com/lit/pdf/sbau423)_ .


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 7


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**6.9 Electrical Characteristics**

at TA = 25°C, VS = 5V on TMCS1133AxA, VS = 3.3V on TMCS1133BxA and TMCS1133CxA (unless otherwise noted)























|PARAMETERS|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**INPUT**|**INPUT**|**INPUT**|**INPUT**|**INPUT**|
|RIN|Input Conductor Resistance|IN+ to IN–|0.7|mΩ|
|RIN|Input Conductor Resistance Temperature Drift|TA= –40ºC to 125ºC|2.1|μΩ/°C|
|IIN,MAX|Maximum Continuous Input Current(1)|TA= 25ºC|80|ARMS|
|IIN,MAX|Maximum Continuous Input Current(1)|TA= 125ºC|44|44|
|**OUTPUT**|**OUTPUT**|**OUTPUT**|**OUTPUT**|**OUTPUT**|
|S|Sensitivity|TMCS1133x7A|20|mV/A|
|S|Sensitivity|TMCS1133x1A|25|25|
|S|Sensitivity|TMCS1133x8A|33|33|
|S|Sensitivity|TMCS1133x2A|50|50|
|S|Sensitivity|TMCS1133x9A|66|66|
|S|Sensitivity|TMCS1133x3A|75|75|
|S|Sensitivity|TMCS1133x4A|100|100|
|S|Sensitivity|TMCS1133x5A|150|150|
|eS|Sensitivity Error|0.05V ≤ VOUT ≤ VS − 0.2V|±0.1<br>±0.4|%|
|Sdrift,therm|Sensitivity Thermal Drift|0.05V ≤ VOUT ≤ VS − 0.2V, TA = −40°C to 125°C|±20<br>±50|ppm/°C|
|Sdrift, life|Sensitivity Lifetime Drift(2)|0.05V ≤ VOUT ≤ VS − 0.2V|±0.2<br>±0.5|%|
|eNL|Nonlinearity Error|VOUT = 0.1V to VS – 0.1V|±0.1|%|
|VOUT,0A|Zero Current Output Voltage|TMCS1133AxA, IIN = 0A|2.5|V|
|VOUT,0A|Zero Current Output Voltage|TMCS1133BxA, IIN = 0A|1.65|1.65|
|VOUT,0A|Zero Current Output Voltage|TMCS1133CxA, IIN = 0A|0.33|0.33|
|VOE|Output Voltage Offset Error|TMCS1133x7A, IIN = 0A|±0.2<br>±1|mV|
|VOE|Output Voltage Offset Error|TMCS1133x1A, IIN = 0A|±0.2<br>±1|±0.2<br>±1|
|VOE|Output Voltage Offset Error|TMCS1133x8A, IIN = 0A|±0.2<br>±1|±0.2<br>±1|
|VOE|Output Voltage Offset Error|TMCS1133x2A, IIN = 0A|±0.3<br>±2|±0.3<br>±2|
|VOE|Output Voltage Offset Error|TMCS1133x9A, IIN = 0A|±0.3<br>±2|±0.3<br>±2|
|VOE|Output Voltage Offset Error|TMCS1133x3A, IIN = 0A|±0.4<br>±3|±0.4<br>±3|
|VOE|Output Voltage Offset Error|TMCS1133x4A, IIN = 0A|±0.5<br>±4|±0.5<br>±4|
|VOE|Output Voltage Offset Error|TMCS1133x5A, IIN = 0A|±0.6<br>±5|±0.6<br>±5|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x7A, IIN = 0A, TA = –40°C to 125°C|±10<br>±25|µV/°C|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x1A, IIN = 0A, TA = –40°C to 125°C|±10<br>±25|±10<br>±25|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x8A, IIN = 0A, TA = –40°C to 125°C|±10<br>±25|±10<br>±25|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x2A, IIN = 0A, TA = –40°C to 125°C|±10<br>±30|±10<br>±30|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x9A, IIN = 0A, TA = –40°C to 125°C|±10<br>±30|±10<br>±30|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x3A, IIN = 0A, TA = –40°C to 125°C|±10<br>±30|±10<br>±30|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x4A, IIN = 0A, TA = –40°C to 125°C|±15<br>±40|±15<br>±40|
|VOE, drift,<br>therm|Output Voltage Offset Thermal Drift|TMCS1133x5A, IIN = 0A, TA = –40°C to 125°C|±15<br>±40|±15<br>±40|
|IOS, drift, life|Offset Lifetime Drift(2)|Input Referred, VOUT,0A / S, IIN = 0A|±10<br>±24|mA|
|PSRR|Power Supply Rejection Ratio|Input Referred, VS = 3V to 5.5V, TA= –40ºC to<br>125ºC|±15<br>±50|mA/V|
|CMTI|Common Mode Transient Immunity(3)|VCM = 1000V, ΔVOUT < 200mV, 1µs|150|kV/µs|
|CMRR|Common Mode Rejection Ratio|Input Referred, DC to 60Hz|5|µA/V|
|CMFR|Common Mode Field Rejection|Uniform External Magnetic Field, Input<br>Referred, DC to 1kHz|10|mA/mT|
||Input Noise Density|Input Referred, Full Bandwidth|130|μA/~~√Hz~~|
|CL,MAX|Maximum Capacitive Load|VOUT to GND|4.7|nF|
||Short Circuit Output Current|VOUT short to GND, short to VS|50|mA|


8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**6.9 Electrical Characteristics (continued)**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



at TA = 25°C, VS = 5V on TMCS1133AxA, VS = 3.3V on TMCS1133BxA and TMCS1133CxA (unless otherwise noted)







































|PARAMETERS|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|SwingVS|Swing to VS Power Supply Rail|RL = 10kΩ to GND, TA= –40ºC to 125ºC|VS – 0.02<br>VS – 0.05|V|
|SwingGND|Swing to GND|Swing to GND|5<br>10|mV|
|**BANDWIDTH & RESPONSE**|**BANDWIDTH & RESPONSE**|**BANDWIDTH & RESPONSE**|**BANDWIDTH & RESPONSE**|**BANDWIDTH & RESPONSE**|
|BW|Analog Bandwidth|- 3dB Gain|1.1|MHz|
|SR|Slew Rate(4)|Output rate of change between reaching 10%<br>and 90% of final value as shown in_Figure 7-2_<br>with a 100ns input step|8|V/µs|
|tr|Response Time(4)|Time between input and output reaching 90%<br>of final values, as shown in_Figure 7-2_ with a<br>100ns input step and a 1V output transition|120|ns|
|tpd|Propagation Delay(4)|Time between input and output reaching 10% of<br>final values as shown in_Figure 7-2_ with a 100ns<br>input step and a 1V output transition|50|ns|
||Current Overload Recovery Time||300|ns|
|**OVER CURRENT DETECTION**|**OVER CURRENT DETECTION**|**OVER CURRENT DETECTION**|**OVER CURRENT DETECTION**|**OVER CURRENT DETECTION**|
|VOC|Over Current Detection Threshold Voltage|VOC = S x IOC / 2.5|0.3<br>VS|V|
||VOC Pin Input Impedance||120|kΩ|
||Over Current Hysteresis|TMCS1133x7A|8.4|A|
||Over Current Hysteresis|TMCS1133x1A|4.5|4.5|
||Over Current Hysteresis|TMCS1133x8A|3.4|3.4|
||Over Current Hysteresis|TMCS1133x2A|3.5|3.5|
||Over Current Hysteresis|TMCS1133x9A|2.5|2.5|
||Over Current Hysteresis|TMCS1133x3A|2.2|2.2|
||Over Current Hysteresis|TMCS1133x4A|1.4|1.4|
||Over Current Hysteresis|TMCS1133x5A|2.7|2.7|
||Vover Current Threshold Error|TA = –40°C to 125°C|±2<br>±10|%|
||Over Current Detection Response Time|IIN step = 120% of IOC|100<br>250|ns|
|~~OC~~,OL|~~OC~~ Pin Pull-down Voltage|IOL = 3mA, TA = –40°C to 125°C|GND<br>0.07<br>0.2|V|
|**DIAGNOSTICS**|**DIAGNOSTICS**|**DIAGNOSTICS**|**DIAGNOSTICS**|**DIAGNOSTICS**|
|~~ALERT~~|Output Frequency||8|kHz|
|~~ALERT~~|Output Duty Cycle, Active Low|Thermal Alert|80|%|
|~~ALERT~~|Output Duty Cycle, Active Low|Sensor Alert|50|50|
|~~ALERT~~|Output Duty Cycle, Active Low|Thermal and Sensor Alert|20|20|
|~~ALERT~~|~~ALERT~~ Pin Pull-down Voltage|IOL = 3mA. TA = –40°C to 125°C|GND<br>0.07<br>0.2|V|
|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|
|VS|Supply Voltage|TA = –40ºC to 125ºC|3.0<br>5.5|V|
|IQ|Quiescent Current|TA = 25ºC|11<br>14|mA|
|IQ|Quiescent Current|TA = –40ºC to 125ºC|14.5|mA|
||Power On Time|Time from VS > 3V to valid output|34|ms|


(1) Thermally limited by junction temperature, see _Absolute Maximum Ratings_ . Applies when device mounted on _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_ . For
more details, see the _Safe Operating Area_ section.
(2) Lifetime and environmental drift specifications based on three lot AEC-Q100 qualification stress test results. Typical values are
population mean +1σ from worst case stress test condition. Maximum values are tested device population mean ±6σ. Devices tested
in AEC-Q100 qualification stayed within maximum limits for all stress conditions. See _Lifetime and Environmental Stability_ section for
more details.
(3) Refer to the _Common-Mode Transient Immunity_ section for details on common-mode transient response.
(4) Refer to the _Transient Response Parameters_ section for details on transient response of the device.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 9


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
|~~S~~<br>S<br>S|~~=25mV~~<br>=75mV/<br>=150m|~~A~~<br>A<br>V/A|||||||


|Col1|S=25mV/<br>S=75mV/<br>S=150m|A<br>A<br>V/A|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||














|S<br>S|=25mV<br>=75mV|/A<br>/A|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~=150m~~|~~/A~~|~~/A~~||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|S=25mV/<br>S=75mV/|A<br>A|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~=150m~~|~~/A~~|~~/A~~||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||



|6.10 Typical Characteristics|Col2|
|---|---|
|Temperature (°C)<br>Sensitivity Error (%)<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>-0.4<br>-0.3<br>-0.2<br>-0.1<br>0<br>0.1<br>~~S=25mV/A~~<br>S=75mV/A<br>S=150mV/A<br>**Figure 6-1. Sensitivity Error vs Temperature**|Termperature (°C)<br>Output Voltage Offset Error (mV)<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>S=25mV/A<br>S=75mV/A<br>~~S=150mV/A~~<br>**Figure 6-2. Offset Error vs Temperature:**<br>**TMCS1133Axx Device Options**|
|Termperature (°C)<br>Output Voltage Offset Error (mV)<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>S=25mV/A<br>S=75mV/A<br>~~S=150mV/A~~<br>**Figure 6-3. Offset Error vs Temperature:**<br>**TMCS1133Bxx Device Options**|Termperature (°C)<br>Output Voltage Offset Error (mV)<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>S=25mV/A<br>S=75mV/A<br>~~S=150mV/A~~<br>**Figure 6-4. Offset Error vs Temperature:**<br>**TMCS1133Cxx Device Options**|
|Temperature (°C)<br>Non-linearity (%)<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>-0.05<br>0.00<br>0.05<br>0.10<br>0.15<br>0.20<br>0.25<br>**Figure 6-5. Non-Linearity vs Temperature**|Population<br>-0.40<br>-0.32<br>-0.24<br>-0.16<br>-0.08<br>0.0<br>0.08<br>0.16<br>0.24<br>0.32<br>0.40<br>Sensitivity Error (%)<br>All sensitivities<br>**Figure 6-6. Sensitivity Error Production**<br>**Distribution**|


10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**











**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



|6<br>3<br>0<br>(dB)<br>-3 Gain<br>-6<br>-9<br>-12<br>10 100 1k 10k 100k 1M 10M<br>Frequency (Hz)<br>Figure 6-7. Sensitivity vs Frequency, All Gains<br>Normalized to 1Hz|60<br>30<br>0<br>(°)<br>-30 Phase<br>-60<br>-90<br>-120<br>10 100 1k 10k 100k 1M 10M<br>Frequency (Hz)<br>Figure 6-8. Phase vs Frequency, All Gains|
|---|---|
|Frequency (Hz)<br>10<br>100<br>1k<br>10k<br>100k<br>1M<br>1m<br>10m<br>100m<br>1<br>10<br>Input Referred PSRR (A/V)<br>**Figure 6-9. PSRR vs Frequency**|Frequency (Hz)<br>10<br>100<br>1k<br>10k<br>100k<br>1M<br>100m<br>1<br>10<br>100<br>Closed-Loop Output Impedance ()<br>**Figure 6-10. Output Impedance vs Frequency**|
|Time (100ns/div)<br>-10<br>2<br>0<br>2.5<br>10<br>3<br>20<br>3.5<br>30<br>4<br>40<br>4.5<br>50<br>5<br>VOUT (V)<br>IIN (A)<br>IIN<br>VOUT<br>**Figure 6-11. Voltage Output Step Response, Rising**|Time (100ns/div)<br>-10<br>2<br>0<br>2.5<br>10<br>3<br>20<br>3.5<br>30<br>4<br>40<br>4.5<br>50<br>5<br>VOUT (V)<br>IIN (A)<br>IIN<br>VOUT<br>**Figure 6-12. Voltage Output Step Response, Falling**|
|**Figure 6-13. Current Overload Response**|**Figure 6-14. Startup Transient Response**|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 11


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**










|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||VS<br>VS|=5V<br>=3.3V|



|VS<br>VS-1<br>(V)<br>VS-2<br>Swing<br>VS-3<br>Voltage<br>GND+3<br>Output<br>GND+2<br>25°C<br>GND+1 -40°C<br>125°C<br>GND<br>0 10 20 30 40 50 60 70 80<br>Output Current (mA)<br>Figure 6-15. Output Swing vs Output Current|13<br>12<br>(mA)<br>11 Current<br>Quiescent<br>10<br>9<br>VS=5V<br>VS=3.3V<br>8<br>-50 -25 0 25 50 75 100 125 150<br>Temperature (°C)<br>Figure 6-16. Quiescent Current vs Temperature|
|---|---|
|Frequency (Hz)<br>10<br>100<br>1k<br>10k<br>100k<br>1M<br>10M<br>1µ<br>10µ<br>100µ<br>1m<br>10m<br>Input Noise Density (A/Hz)<br>**Figure 6-17. Input-Referred Noise Density vs**<br>**Frequency**|Temperature (°C)<br>RIN ()<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>500<br>600<br>700<br>800<br>900<br>1000<br>**Figure 6-18. Input Conductor Resistance vs**<br>**Temperature**|


_**6.10.1 Insulation Characteristics Curves**_





12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 13


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**7 Parameter Measurement Information**

**7.1 Accuracy Parameters**


The ideal first-order transfer function of the TMCS1133 is given by Equation 1, where the output voltage is a
linear function of input current. The accuracy of the device is quantified both by the error terms in the transfer
function parameters, as well as by nonidealities that introduce additional error terms not in the simplified linear
model. See _Total Error Calculation Examples_ for example calculations of total error, including all device error
terms.


VOUT = IIN × S + VREF (1)


where


 - VOUT is the analog output voltage.

 - IIN is the isolated input current.

 - S is the sensitivity of the device.

 - VREF is the zero current reference output voltage for the device variant.

_**7.1.1 Sensitivity Error**_


Sensitivity is the proportional change in the sensor output voltage due to a change in the input conductor current.
This sensitivity is the slope of the first-order transfer function of the sensor (see Figure 7-1). The sensitivity of the
TMCS1133 is tested and calibrated at the factory for high accuracy.


VOUT (V)





|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||VNL|VNL|S = Slope (V/A)<br>best<br>VREF + VFS+|S = Slope (V/A)<br>best<br>VREF + VFS+|fit line|
|||||||
|||||VREF<br>VOUT, 0 A <br>VO|<br>E|
|||||||
|||||||
||VREF ± VFS±|VREF ± VFS±||||


IFS+







IFS± IIN (A)



**Figure 7-1. Sensitivity, Offset, and Nonlinearity Error**


Sensitivity error eS is the deviation from ideal sensitivity and is defined in Equation 2 as the variation of the
best-fit measured sensitivity from the ideal sensitivity.



eS =





where


 - eS is the sensitivity error.

 - Sfit is the best fit sensitivity.

 - SIdeal is the ideal sensitivity.

Sensitivity thermal drift Sdrift,therm is the change in sensitivity with temperature and is reported in ppm/°C. To
calculate sensitivity error at any given temperature T use Equation 3 to multiply the sensitivity thermal drift by the
change in temperature from 25°C and add that value to the sensitivity error at 25°C.


eS, ∆T = eS, 25℃ + Sdrift, therm × ∆T (3)


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


where

 - Sdrift,therm is the sensitivity drift over temperature in ppm/°C.

 - ΔT is the change in device temperature from 25°C.



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



Sensitivity lifetime drift Sdrift,life is the change in sensitivity due to operational and environmental stresses over
the entire lifetime of the device, and is reported as a worst-case percentage change in sensitivity over lifetime at
25°C.


_**7.1.2 Offset Error and Offset Error Drift**_


Offset error is the deviation from the ideal output with zero input current and most often limits measurement
accuracy at low input current levels. Offset error can be referred to the output as offset voltage error or referred
to the input as offset current error. When divided by device sensitivity, S, output voltage offset error VOE is input
referred as input current offset error IOS (see Equation 4). Offset error referred to the input (RTI) allows for more
direct comparisons or offset error with input current. Regardless of whether offset error is referred to the input as
current offset error IOS, or to the output as voltage offset error VOE, offset error is a single error source and must
only be included once in either input-referred or output-referred error calculations.



IOS =



VOE ~~S~~ (4)



As shown in Figure 7-1, the output voltage offset error VOE of the TMCS1133 is the difference between the zero
current output voltage VOUT,0A and the zero current output reference voltage VREF (see Equation 5).


VOE = VOUT, 0A −VREF (5)


The output offset error VOE includes magnetic offset error in the Hall sensor, offset voltage error in the signal
chain, and offset error in the internal zero current output reference voltage VREF.

Offset drift is the change in the offset as a function of temperature T. Output offset drift is reported in µV/°C. To
calculate offset error at any given temperature, multiply the offset drift by the change in temperature and add that
value to the offset error at 25°C (see Equation 6).


VOE, ∆T = VOE, 25℃ + VOE, drift × ∆T (6)


where


 - VOE,drift is the output voltage offset drift with temperature in µV/°C.

 - ΔT is the change in device temperature from 25°C.


_**7.1.3 Nonlinearity Error**_


Nonlinearity is the deviation of the output voltage from a linear relationship to the input current. Nonlinearity
voltage, as shown in Figure 7-1, is the maximum voltage deviation from the best-fit line based on measured
parameters (see Equation 7).


where


 - VOUT,meas is the voltage output at maximum deviation from best fit.

 - Imeas is the input current at maximum deviation from best fit.

 - Sfit is the best-fit sensitivity of the device.

 - VOUT,0A is the device zero current output voltage.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 15


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


Nonlinearity error for the TMCS1133 is specified as a percentage of the full-scale output range, VFS (see
Equation 8).



eNL =



V ~~V~~ NLFS (8)



_**7.1.4 Power Supply Rejection Ratio**_


Power supply rejection ratio (PSRR) is the change in device offset due to variations in supply voltage. Use
Equation 9 to calculate input referred offset errors caused by supply variations on TMCS1133Axx variants.
Use Equation 10 to calculate input referred offset errors caused by supply variations on TMCS1133Bxx and
TMCS1133Cxx variants.


ePSRR, A = PSRR × VS −5V (9)


ePSRR, B = ePSRR, C = PSRR × VS −3.3V (10)


where


 - PSRR is the input referred power supply rejection ratio in mA/V.

 - VS is the operational supply voltage.

_**7.1.5 Common-Mode Rejection Ratio**_


Common-mode rejection ratio (CMRR) quantifies the effective input current error due to varying voltage on the
isolated input of the device. Due to magnetic coupling and galvanic isolation of the current signal, the TMCS1133
has very high rejection of input common-mode voltage. Use Equation 11 to calculate the error contribution from
the input common-mode voltage VCM.


eCMRR = CMRR × VCM (11)


where


 - CMRR is the input-referred common-mode rejection in µA/V.

 - VCM is the operational AC or DC voltage on the input of the device.

_**7.1.6 External Magnetic Field Errors**_


The TMCS1133 suppresses interference from external magnetic fields generated by adjacent high-current
carrying conductors, nearby motors, magnets, or any other sources of stray magnetic fields. Common-mode
field rejection (CMFR) quantifies the effective input-referred error caused by stray magnetic fields. Use Equation
12 to calculate error contributions from stray external magnetic fields BEXT.


eBext = BEXT × CMFR (12)


where


 - BEXT is the intensity of the external magnetic field in mT.

 - CMRF is the common-mode field rejection in mA/mT.


16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**7.2 Transient Response Parameters**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



Critical TMCS1133 transient step response parameters are shown in Figure 7-2. Propagation delay, tpd, is the
time period between the input current waveform reaching 10% of the final value and the output voltage, VOUT,
reaching 10% of the final value. Response time, tr, is the time period between the input current reaching 90% of
the final value and the output voltage reaching 90% of the final value, for an input current step sufficient to cause
a 1V change in the output voltage. Slew rate, SR, is defined as the rate of change between the output voltage
reaching 10% and 90% of the final value during the sufficiently fast input current step.









**me**

                              
**Figure 7-2. Transient Step Response**


_**7.2.1 CMTI, Common-Mode Transient Immunity**_


CMTI is the capability of the device to tolerate a rising or falling voltage step on the input without coupling
significant disturbance on the output signal. The device is specified for the maximum common-mode transition
rate when the output signal does not experience a disturbance greater than 200mV lasting longer than 1µs, as
shown in Figure 7-3 with a 150kV/µs common-mode input step. Higher edge rates than the specified CMTI can
be supported with sufficient filtering or blanking time after common-mode transitions.



1.4


1.2


1.0


0.8


0.6


0.4


0.2


0.0


-0.2





2.5


2.0


1.5


1.0


0.5


0.0


-0.5


-1.0


-1.5


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||||||||||~~V~~|
||||||||||~~CM~~<br>VOUT|



50 (ns/div)


**Figure 7-3. Common-Mode Transient Response**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 17


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**7.3 Safe Operating Area**


The isolated input current safe operating area (SOA) of the TMCS1133 is constrained by self-heating due to
power dissipation in the input conductor. Depending upon the use case, the SOA is constrained by multiple
conditions, including exceeding maximum junction temperature, Joule heating in the leadframe, or leadframe
fusing under extremely high currents. These mechanisms depend greatly on input current amplitude and
duration, along with ambient thermal conditions.


Current SOA strongly depends on the thermal environment and design of the system-level printed circuit board
(PCB). Multiple thermal variables control the transfer of heat from the device to the surrounding environment,
including air flow, ambient temperature, and PCB construction and design. All ratings are for a single TMCS1133
device mounted on the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_, or equivalent PCB design with no air flow under specified ambient
temperature conditions. Device use profiles must satisfy continuous current conduction SOA capabilities for the
thermal environment planned for system operation.


_**7.3.1 Continuous DC or Sinusoidal AC Current**_


The longest thermal time constants of device packaging and PCBs are in the order of seconds; therefore,
any continuous DC or sinusoidal AC periodic waveform with a frequency higher than 1Hz can be evaluated
based on the RMS continuous-current levels. The continuous-current capability has a strong dependence upon
the operating ambient temperature range expected in operation. Figure 7-4 shows the maximum continuous
current-handling capability of the device when mounted on the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_ . Current capability falls off at
higher ambient temperatures because of the reduced thermal transfer from junction-to-ambient and increased
power dissipation in the leadframe. By improving the thermal design of an application, the SOA can be extended
to higher currents at elevated temperatures. Using larger and heavier copper power planes, providing air flow
over the board, or adding heat sinking structures to the area of the device can all improve thermal performance.


**Figure 7-4. Maximum Continuous RMS Current vs Ambient Temperature**


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


_**7.3.2 Repetitive Pulsed Current SOA**_



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



For applications where current is pulsed between a high current and no current, the allowable capabilities
are limited by short-duration heating iwn the leadframe. The TMCS1133 can tolerate higher current ranges
under some conditions, however, for repetitive pulsed events, the current levels must satisfy both the pulsed
current SOA and the RMS continuous current constraint. Pulse duration, duty cycle, and ambient temperature
all impact the SOA for repetitive pulsed events. Figure 7-5, Figure 7-6, Figure 7-7, and Figure 7-8 illustrate
repetitive stress levels based on test results from the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_ under which parametric performance and
isolation integrity is not impacted post-stress for multiple ambient temperatures. At high duty cycles or long pulse
durations, this limit approaches the continuous current SOA for a RMS value defined by Equation 13.


IIN,  RMS = IIN, P × D (13)


where


 - IIN,RMS is the RMS input current level

 - IIN,P is the pulse peak input current

 - D is the pulse duty cycle



500


450


400


350


300


250


200


150


100


50


0





450


400


350


300


250


200


150


100


50


0




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|1|Col24|%|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||
|||||||||||||||||||||||~~5~~<br>1|0|%|
|||||||||||||||||||||||2|5|%|
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|1|Col24|%|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||
|||||||||||||||||||||||~~5~~<br>1|0|%|
|||||||||||||||||||||||~~2~~|~~5~~|~~%~~|
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||



1m 10m 100m 1 10

Current Pulse Duration (s)

TA = 25°C


**Figure 7-5. Maximum Repetitive**
**Pulsed Current vs. Pulse Duration**


450



1m 10m 100m 1 10

Current Pulse Duration (s)

TA = 85°C


**Figure 7-6. Maximum Repetitive**
**Pulsed Current vs. Pulse Duration**


450



400


350


300


250


200


150


100


50


0



400


350


300


250


200


150


100


50


0






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|1|Col24|%|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||
|||||||||||||||||||||||1<br>|0<br>|%<br>|
||||||||||||||||||||||||||
|||||||||||||||||||||||~~2~~|~~5~~|~~%~~|
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|1|Col24|%|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||
|||||||||||||||||||||||1<br>|0<br>|%<br>|
||||||||||||||||||||||||||
|||||||||||||||||||||||~~2~~|~~5~~|~~%~~|
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||
||||||||||||||||||||||||||



1m 10m 100m 1 10

Current Pulse Duration (s)

TA = 105°C


**Figure 7-7. Maximum Repetitive**
**Pulsed Current vs. Pulse Duration**



1m 10m 100m 1 10

Current Pulse Duration (s)

TA = 125°C


**Figure 7-8. Maximum Repetitive**
**Pulsed Current vs. Pulse Duration**



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 19


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


_**7.3.3 Single Event Current Capability**_


Single higher-current events that are shorter duration can be tolerated by the TMCS1133, because the junction
temperature does not reach thermal equilibrium within the pulse duration. Figure 7-9 shows the short-circuit
duration curve for the device for single current-pulse events, where the leadframe resistance changes after
stress. This level is reached before a leadframe fusing event, but must be considered an upper limit for short
duration SOA. For long-duration pulses, the current capability approaches the continuous RMS limit at the given
ambient temperature.


1k


100

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||~~T~~A <br>|~~ =~~<br>|~~ 2~~<br>|~~ °~~<br>|<br>|<br>||
||||||||||||||||||||||||||<br>~~T~~A|<br>~~ =~~|<br>~~ 1~~|<br>~~ 5~~|<br>~~ °~~|<br>~~ C~~||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||

10m 100m 1 10

Pulse Duration (s)


**Figure 7-9. Single-Pulse Leadframe Capability**


**8 Detailed Description**

**8.1 Overview**


The TMCS1133 is a precision Hall-effect current sensor, providing high levels of reliable reinforced isolation
working voltage, ambient field rejection and high current carrying capability. A maximum total lifetime error of
less than 1.4% can be achieved with no system level calibration, or less than 1% maximum total error can be
achieved with a one-time room temperature calibration (including both temperature and lifetime drift). Numerous
device options are provided for both unidirectional and bidirectional current measurements. The input current
flows through a conductor between the isolated input current pins. The conductor has a 0.7mΩ resistance at
room temperature and accommodates up to 44ARMS of continuous current at 125°C ambient temperature when
used with printed circuit boards of comparable thermal design, such as the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_ . The low-ohmic
leadframe path reduces power dissipation compared to alternative current measurement methodologies, and
does not require any external passive components, isolated supplies, or control signals on the high-voltage side.
The magnetic field generated by the input current is sensed by a Hall sensor and amplified by a precision signal
chain. The device can be used for both AC and DC current measurements and has a bandwidth of 1MHz.
There are multiple fixed-sensitivity device options to choose from, providing a wide variety of bidirectional linear
current sensing ranges from ±10A to ±96A, as well as unidirectional linear current sensing ranges from 19A
to 183A. The TMCS1133 can operate with a low voltage supply ranging from 3V to 5.5V, and is optimized for
high accuracy and temperature stability, with both offset and sensitivity compensated across the entire operating
temperature range.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**8.2 Functional Block Diagram**


IN +


IN 

**8.3 Feature Description**

_**8.3.1 Current Input**_

















**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



GND


**Figure 8-1. Function Block Diagram**



Input current to the TMCS1133 passes through the isolated high-voltage side of the package leadframe into
and out of the IN+ and IN– pins. The current flowing through the package generates a magnetic field that is
proportional to the input current, which is measured by an integrated on-chip galvanically-isolated, precision Hall
sensor. As a result of the electrostatic shielding on the Hall sensor die, only the magnetic field generated by the
input current is measured, thus limiting input voltage switching pass-through to the circuitry. This configuration
allows for direct measurement of currents with high-voltage transients without signal distortion on the currentsensor output. The leadframe conductor has a low resistance and a positive temperature coefficient as defined
in _Electrical Characteristics_ .


_**8.3.2 Input Isolation**_


The separation between the input conductor and the Hall sensor die due to the TMCS1133 construction provides
inherent galvanic isolation between package pins 1 and 2 on the high-voltage input side, and package pins
3 through 10 on the low-voltage output side. Insulation capability is defined according to certification agency
definitions and using industry-standard test methods as defined in _Section 6.6_ . Assessment of device lifetime
working voltages follow the IEC 60747-17 standard for basic and reinforced insulation, requiring time-dependent
dielectric breakdown (TDDB) data-projection are based on projected failure rates of less than 1 part per million
(ppm) for reinforced insulation and less than 1000ppm for basic insulation, and a minimum insulation lifetime of
30 years. For reinforced insulation, the IEC 60747-17 standard also requires additional safety margins of 20%
for working voltage, and 50% for insulation lifetime, translating into a minimum required lifetime of 30 years at
800VRMS for the TMCS1133 .

Figure 8-2 shows the intrinsic capability of the isolation barrier to withstand high-voltage stress over the lifetime
of the device. Based on the TDDB data, the intrinsic capability of these devices is 670VRMS with a lifetime > 20
years. Other factors such as operating environment and pollution degree can further limit the working voltage of
the component in an end system.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 21


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**Figure 8-2. Insulation Lifetime**


_**8.3.3 Ambient Field Rejection**_


The TMCS1133 is designed to provide high levels of current measurement accuracy in harsh environments.
Immunity to interference from stray magnetic fields allows for use in close proximity to high current carrying
traces, motor windings, inductors, or any other erroneous source of stray magnetic fields. The TMCS1133
incorporates differential Hall sensors that are strategically located and configured to reject interference from
stray external magnetic fields. Ambient Field Rejection (AFR) limited only by Hall element matching and package
leadframe coupling reduces errors from stray magnetic fields.


_**8.3.4 High-Precision Signal Chain**_


The TMCS1133 uses a precision, low-drift signal chain with proprietary sensor linearization techniques to
provide a highly accurate and stable current measurement across the full temperature range and lifetime of
the device. The device is fully tested and calibrated at the factory to account for any variations in either silicon
processing, assembly, or packaging of the device. The full signal chain provides a fixed sensitivity voltage output
that is proportional to the current flowing through the leadframe of the isolated input.


**8.3.4.1 Temperature Stability**


The TMCS1133 includes a proprietary temperature compensation technique which results in significantly
improved parametric drift across the full temperature range. This compensation technique accounts for changes
in ambient temperature, self-heating, and package stress. A zero-drift signal chain architecture along with
Hall sensor temperature compensation methods enable stable sensitivity while minimizing offset errors across
temperature. System-level performance is drastically improved across required operating conditions.


**8.3.4.2 Lifetime and Environmental Stability**


In addition to large thermal drift, typical magnetic current sensors suffer an additional 2% to 3% drift in sensitivity
due to aging over the lifetime of the device. The same proprietary compensation techniques used in the
TMCS1133 to reduce temperature drift are also used to greatly reduce lifetime drift due to aging from stress and
environmental conditions especially at high operating temperatures. As shown in the _Electrical Characteristics_,
the TMCS1133 has industry leading lifetime sensitivity drift realized after Highly Accelerated Stress Tests (HAST)
at 130°C and 85% relative humidity (RH) during standard three lot AEC-Q100 qualifications. Low sensitivity
and offset drift within the bounds specified in the _Electrical Characteristics_ are also observed after 1000 hour,
125°C high temperature operating life stress tests are performed as prescribed by AEC-Q100 qualifications.
These tests mimic typical device lifetime operation, and show device performance variation due to aging is vastly
improved compared with typical magnetic current sensors. Figure 8-3 and Figure 8-4 show the sensitivity and
offset drift after a 1000 hour, 125°C high temperature operating life stress test as specified by AEC-Q100. Device


22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



operational performance varies over the lifetime of the device. This test mimics typical device lifetime operations
and shows the likelihood of the device vastly improving performance compared to typical magnetic sensors.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||



Input-referred Offset Drift (mA)



**Figure 8-3. Sensitivity Error Drift After AEC-Q100**

**High Temperature Operating Life Stress Test**


_**8.3.5 Internal Reference Voltage**_



**Figure 8-4. Input-Referred Offset Drift After AEC-**
**Q100 High Temperature Operating Life Stress Test**



The TMCS1133 has a precision internal reference that determines the zero current output voltage, VOUT,0A.
Overall current sensing dynamic range can be optimized by choosing either of the three different zero current
output voltage options listed in the _Device Comparison_ table. These extremely low-drift precision zero current
reference options are listed in Equation 14, Equation 15 and Equation 16. These equations are for precise
bidirectional or unidirectional current measurements using various supply voltages ranging between 3.0V to
5.5V.


TMCS11xxAxx ➔ VOUT,0A = VREF = 2.5V (14)


TMCS1133Bxx ➔ VOUT,0A = VREF = 1.65V (15)


TMCS1133Cxx ➔ VOUT,0A = VREF = 0.33V (16)


_**8.3.6 Current-Sensing Measurable Ranges**_


The zero current reference voltage, VREF, along with device sensitivity, S, and supply voltage, VS, determine
the TMCS1133 linear input current measurement ranges listed in the _Device Comparison_ table. The maximum
linear output voltage, VOUT,max, is limited to 100mV less than the supply voltage as shown in Equation 17. The
minimum linear output voltage, VOUT,min, is limited to 100mV above ground as shown in Equation 18.


VOUT, max = VS −100mV (17)


VOUT, min = 100mV (18)


Overall maximum dynamic range can be optimized with proper device selection by referring minimum and
maximum linear output voltage swing to minimum and maximum linear input current range by dividing output
voltage by sensitivity, S (see Equation 19 and Equation 20).



IIN, max + =


IIN, max − =





Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 23


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


where

 - IIN,max+ is the maximum linear measurable positive input current.

 - IIN,max– is the maximum linear measurable negative input current.

 - S is the sensitivity of the device variant.

 - VOUT,0A is the appropriate zero current output voltage.

As examples for determining linear input current measurement range, consider TMCS11xxA2A, TMCS11xxB2A,
and TMCS11xxC2A devices, all with 50mV/A sensitivity as shown in the _Device Comparison_ table. When used
with a 5V supply, the TMCS11xxA2A has a balanced ±48A bidirectional linear current measurement range
about the 2.5V zero current output reference voltage, VREF, as shown in Figure 8-5. When used with a 3.3V
supply, the TMCS11xxB2A has a balanced ±31A bidirectional linear current measurement range about the
1.65V zero current output reference voltage. If used with a 5V supply, the linear current measurement range
of the TMCS11xxB2A can be extended from –31A to 65A as shown in Figure 8-5. The TMCS11xxC2A with a
0.33V zero current reference voltage is intended for measuring unidirectional currents. When used with a 3.3V
supply the TMCS11xxC2A has a unidirectional linear current measurement range from –5A to 57A which can be
extended from –5A to 91.4A when used with a 5V supply.


**Figure 8-5. Output Voltage Relationship to Input Current for TMCS11xxx2A**


_**8.3.7 Overcurrent Detection**_


In addition to the precision analog signal, the TMCS1133 also offers a fast digital overcurrent detection
response. The Overcurrent Detection (OCD) circuit provides an open-drain comparator output that can be used
to trigger a warning or initiate a system shutdown to prevent damage from excessive current flow caused by
short circuits, motor stalls, or other unintended system conditions. This fast digital response can be configured
on both bidirectional and unidirectional devices to assert based on a signal that is anywhere from half to over
twice the full-scale analog measurement range.


Use of this fast digital output ~~OC~~ instead of the precision analog output VOUT to detect overcurrent events
outside the nominal operating current range allows for higher dynamic range with higher sensitivity optimized
for the nominal operating current range. Use of this fast digital output ~~OC~~ also allows for lower overall signal
noise from lower analog signal bandwidth than often needed when using the analog signal chain to detect fast
overcurrent events.


**8.3.7.1 Setting The User Configurable Overcurrent Threshold**


The desired overcurrent threshold, IOC, is set by applying an external voltage, VOC, to the VOC pin according to
Equation 21.



VOC =



S × I2.5OC (21)



24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


where

 - S is the device sensitivity in V/A.

 - IOC is the desired overcurrent threshold in A.

 - VOC is the voltage applied that sets the overcurrent threshold in V.



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



An example of how to set the desired overcurrent threshold, IOC, is shown in Section 8.3.7.1.2. Regardless of
which TMCS1133 sensitivity variant is chosen or which zero current output voltage option is selected, Equation
21 applies when calculating overcurrent threshold voltage VOC. A digital-to-analog converter (DAC) can be used
to set the desired overcurrent threshold IOC, or a simple external resistor divider circuit can be used as shown in
Section 8.3.7.1.1.


_**8.3.7.1.1 Setting Overcurrent Threshold Using Power Supply Voltage**_


A simple external resistor divider driven from the power supply as shown in Figure 8-6 can be used to generate
the external overcurrent voltage VOC applied to the VOC pin to set the desired overcurrent threshold IOC
according to Equation 21.

















IN +


IN 


|R1 R2|Col2|Col3|
|---|---|---|
|VS<br>GN<br>RPU<br>VS<br>VOC<br>OC<br>Differential<br>Hall<br>Element<br>Bias<br>Temperature<br>Compensation<br>----------------------<br>Offset<br>Cancellation<br>VOUT<br>Precision<br>AFE<br>Reinforced Isolation Barrier<br>Precision<br>Reference<br>Sensor & Thermal <br>Diagnostics<br>ALERT<br>~~In ~~Window<br>~~Thr+~~<br>~~T~~hr -<br>Output<br>Amplifier<br>Threshold<br>Generation|VS<br>GN<br>RPU<br>VS<br>VOC<br>OC<br>Differential<br>Hall<br>Element<br>Bias<br>Temperature<br>Compensation<br>----------------------<br>Offset<br>Cancellation<br>VOUT<br>Precision<br>AFE<br>Reinforced Isolation Barrier<br>Precision<br>Reference<br>Sensor & Thermal <br>Diagnostics<br>ALERT<br>~~In ~~Window<br>~~Thr+~~<br>~~T~~hr -<br>Output<br>Amplifier<br>Threshold<br>Generation|VS<br>GN<br>RPU<br>VS<br>VOC<br>OC<br>Differential<br>Hall<br>Element<br>Bias<br>Temperature<br>Compensation<br>----------------------<br>Offset<br>Cancellation<br>VOUT<br>Precision<br>AFE<br>Reinforced Isolation Barrier<br>Precision<br>Reference<br>Sensor & Thermal <br>Diagnostics<br>ALERT<br>~~In ~~Window<br>~~Thr+~~<br>~~T~~hr -<br>Output<br>Amplifier<br>Threshold<br>Generation|
||Reinforced Isolation Barrier|Differential<br>Hall<br>Element<br>Bias<br>Temperature<br>Compensation<br>----------------------<br>Offset<br>Cancellation<br>Precision<br>AFE<br>Precision<br>Reference<br>Sensor & Thermal <br>Diagnostics<br>~~In ~~Window<br>~~Thr+~~<br>~~T~~hr -<br>Output<br>Amplifier<br>Threshold<br>Generation|


GND


**Figure 8-6. User Configurable Overcurrent Threshold Using Power Supply Voltage**


When using a resistor divider as shown in Figure 8-6, R2 must be less than 10kΩ to mitigate the impact of the
VOC input impedance on overcurrent threshold accuracy.


_**8.3.7.1.2 Setting Overcurrent Threshold Example**_


For example, to set a desired overcurrent threshold to IOC = ±50A on bidirectional TMCS1133A3A or
TMCS1133B3A devices with ±32A linear measurement range, as well as on the unidirectional TMCS1133C3A
device, size the resistors R1 and R2 to apply a voltage VOC = 1.5V to the VOC pin according to Equation 21.

with

 - TMCS1133A3A, TMCS1133B3A and TMCS1133B3A device sensitivity, S = 0.075V/A.

 - Desired overcurrent threshold, IOC = ±50A.

 - Applied overcurrent threshold voltage VOC = 1.5V.


**8.3.7.2 Overcurrent Output Response**


Figure 8-7 shows the active-low overcurrent digital output ~~OC~~ response to bidirectional overcurrent events.
When the input current exceeds |±IOC| on a bidirectional device, the fast ~~OC~~ pin is pulled low. The input current
must return to within ±IOC by more than a hysteresis current IHys before the ~~OC~~ pin resets back to the normal
high-state.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 25


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**



**+ IOC**


**– IOC**


OC


_**8.3.8 Sensor Diagnostics**_



|IN Hysteresis|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|+ Threshold|+ Threshold|+ Threshold|+ Threshold|+ Threshold|
|<br>(IOC = 2.5 x VOC / S)|||||
|<br>(IOC = 2.5 x VOC / S)|||||
|– Threshold|||||
|– Threshold|||||
|<br>(– IOC = –2.5 x VOC / S)|||||
||||||


**Figure 8-7. Overcurrent Output Response**



Built-in self-diagnostic features are incorporated in the TMCS1133 to warn when operating conditions invalidate
current sensor measurements. Two critical conditions being monitored are sensor temperature and sensitivity.


**8.3.8.1 Thermal Alert**


As discussed in the _Safe Operating Area_ section, high levels of input current can generate excessive heat inside
the TMCS1133 . High input currents, coupled with elevated ambient temperatures and printed circuit board
thermal design can cause the TMCS1133 to overheat and be permanently damaged by exceeding maximum
allowed junction temperatures. A thermal alert occurs when the internal temperature approaches the maximum
allowed junction temperature.


**8.3.8.2 Sensor Alert**


In addition to temperature, sensor sensitivity and offset are constantly being monitored inside the TMCS1133 . A
sensor alert occurs in the unlikely event Hall sensor sensitivity or offset is out of range compared with factory set
limits.


The active-low ~~ALERT~~ output signal can be used to decipher which of four diagnostic states the TMCS1133
resides. As shown in Figure 8-8, the duty cycle of the 8kHz PWM output signal indicates which, neither, or both
of the thermal and sensor operating condition warnings exist.


**ALERT**

|No<br>Fault|Thermal<br>& Sensor|Sensor|Thermal|
|---|---|---|---|
|||||
|||||



100% 20% 50% 80%

**Duty Cycle**


**Figure 8-8. Sensor Diagnostics Waveform**


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**8.4 Device Functional Modes**

_**8.4.1 Power-Down Behavior**_



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



As a result of the inherent galvanic isolation of the device, very little consideration must be paid to powering
down the device, as long as the limits in the _Absolute Maximum Ratings_ table are not exceeded on any
pins. The isolated current input and the low-voltage signal chain can be decoupled in operational behavior, as
either can be energized with the other shutdown, as long as the isolation barrier capabilities are not exceeded.
The low-voltage power supply can be powered down while the isolated input is still connected to an active
high-voltage signal or system.


**9 Application and Implementation**


**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**9.1 Application Information**


The key feature sets of the TMCS1133 provide significant advantages in any application where an isolated
current measurement is required.

 - Galvanic isolation provides a high isolated working voltage and excellent immunity to input voltage transients.

 - Hall-based measurement simplifies system level designs without the need for a power supply on the highvoltage (HV) side.

 - An input current path through the low impedance conductor minimizes power dissipation.

 - Excellent accuracy and low temperature drift eliminate the need for multipoint calibrations without sacrificing
system performance.

 - A wide operating supply range enables a single device to function across a wide range of voltage levels.


These advantages increase system-level performance while minimizing complexity for any application where
precision current measurements must be made on isolated currents. Specific examples and design requirements
are detailed in the following section.


_**9.1.1 Total Error Calculation Examples**_


Users can calculate the total error for any arbitrary device condition and current level. Consider error sources
like input-referred offset current (IOS), Common Mode Rejection Ratio (CMRR), Power Supply Rejection Ratio
(PSRR), sensitivity error, nonlinearity, as well as errors caused by any external magnetic fields (BEXT). Compare
each of these error sources in percentage terms, as some are significant drivers of error and some have
inconsequential impact to current measurement error. Offset (Equation 22), CMRR (Equation 23), PSRR, and
external magnetic field error (Equation 25) are all referred to the input, and so are divided by the actual input
current IIN to calculate percentage errors. For sensitivity error and nonlinearity error calculations, the percentage
limits explicitly specified in the _Electrical Characteristics_ table can be used.



~~S × I~~ VOEIN [× 100%] (22)



eIos =



IOS
~~I~~ IN [× 100% =]



eCMRR =



CMRR × VCM
~~I~~ IN × 100% (23)





ePSRR, A =





eBext =



BEXT × CMFR
~~I~~ IN × 100% (25)



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 27


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


where

 - VOE is the output-referred offset voltage error.

 - VCM is the input common-mode voltage.

 - ePSRR,A is the power supply rejection error for TMCS1133Axx devices.

 - ePSRR,B is the power supply rejection error for TMCS1133Bxx devices.

 - ePSRR,C is the power supply rejection error for TMCS1133Cxx devices.

 - VS is the supply voltage.

 - CMFR is the common-mode magnetic field rejection.


When calculating error contributions across temperature, only offset error and sensitivity error contributions vary
significantly. To determine the offset error across temperature, use Equation 26 to calculate total input-referred
offset error current, IOS, at any ambient temperature, TA.



eIos,∆T =





where

 - VOE,25°C is the output-referred offset error at 25°C.

 - VOE,drift is the output-referred offset drift with temperature in µV/°C.

 - ΔT is the change in temperature from 25°C.

 - S is the sensitivity of the device variant.


Sensitivity error at 25°C is specified as eS,25°C in the _Electrical Characteristics_ table along with sensitivity
variation over temperature as sensitivity thermal drift Sdrift,therm in ppm/°C. To determine the sensitivity error
across temperature, use Equation 27 to calculate sensitivity error at any ambient temperature, TA, over the given
application operating ambient temperature range between –40°C and 125°C.


eS,∆T = eS, 25℃ + Sdrift, therm × ∆T × 100% (27)


To accurately calculate the total expected error of the device, the contributions from each of the individual
components above must be understood in reference to operating conditions. To account for the individual error
sources that are statistically uncorrelated, use a root sum square (RSS) error calculation to calculate total error.
For the TMCS1133, only the input-referred offset current (IOS), CMRR, and PSRR are statistically correlated.
These error terms are lumped in an RSS calculation to reflect this nature, as shown in Equation 28 for room
temperature and in Equation 29 across a given temperature range. The same methodology can be applied for
calculating typical total error by using the appropriate error term specification.























The total error calculation has a strong dependence on the actual input current, therefore always calculate
total error across the dynamic range that is required. These curves asymptotically approach the sensitivity and
nonlinearity error at high current levels, and approach infinity at low current levels due to offset error terms
with input current in the denominator. Key figures of merit for any current-measurement system include the
total error percentage at full-scale current, as well as the dynamic range of input current over which the error
remains below some key level. Figure 9-1 shows the RSS maximum total error as a function of input current for
a TMCS1133A2A at room temperature and across the full temperature range with a 5.25V supply.


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)


**Figure 9-1. RSS Error vs Input Current**



**9.1.1.1 Room-Temperature Error Calculations**


For room-temperature total error calculations, specifications across temperature and drift are ignored. As an
example, consider a TMCS1133B2A with a supply voltage (VS) of 3.1V and a worst-case common-mode
excursion of 600V to calculate operating-point specific parameters. Consider a measurement error due to an
external 400µT magnetic field generated by a 20ADC current flowing through an adjacent trace or conductor that
is 10mm away. The full-scale current range of the device in specified conditions is slightly greater than ±31A, as
shown in the _Device Comparison_ table. In this case, the calculating error at both 25A and 12.5A highlights error
dependencies on the input-current level. Table 9-1 shows the individual error components and RSS maximum
total error calculations at room temperature under the conditions specified. Relative to other errors, the additional
errors from CMRR, external ambient magnetic fields BEXT and nonlinearity are negligible, and can typically be
excluded from total error calculations.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 29


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**Table 9-1. Total Error Calculation: Room Temperature Example**













|ERROR COMPONENT|SYMBOL|EQUATION|ERROR AT<br>IIN = 25A|ERROR AT<br>IIN = 12.5A|
|---|---|---|---|---|
|Input offset error|eIos|eIos = IOS<br>~~I~~IN × 100% =<br>VOE<br>~~S × I~~IN × 100% =<br>± 2mV<br>~~50mV/A × I~~IN × 100%|±0.16%|±0.32%|
|PSRR error|ePSRR|ePSRR =PSRR × VS −3.3<br>~~I~~IN<br>× 100%|±0.04%|±0.08%|
|CMRR error|eCMRR|eCMRR =CMRR × VCM<br>~~I~~IN<br>× 100%|±0.01%|±0.02%|
|External Field error|eBext|eBext = BEXT× CMFR<br>~~I~~IN<br>× 100%|±0.02%|±0.03%|
|Sensitivity error|eS|Specified in_Electrical Characteristics_|±0.4%|±0.4%|
|Nonlinearity error|eNL|Specified in_Electrical Characteristics_|±0.1%|±0.1%|
|RSS total error|eRSS|eRSS =<br>eIos+ePSRR+eCMRR<br>2 + eBext<br>2 + eS<br>2 + eNL<br>2|0.46%|0.59%|


**9.1.1.2 Full-Temperature Range Error Calculations**







To calculate total error across any specific temperature range, use Equation 28 and Equation 29 for RSS
maximum total errors, similar to the example for room temperatures. Conditions from the example in _Room-_
_Temperature Error Calculations_ are replaced with the respective equations and error components for a –40°C to
85°C temperature range below in Table 9-2.


**Table 9-2. Total Error Calculation: –40°C to 85°C Example**













|ERROR COMPONENT|SYMBOL|EQUATION|ERROR AT<br>IIN = 25A|ERROR AT<br>IIN = 12.5A|
|---|---|---|---|---|
|Input offset error|eIos,ΔT|eIos,∆T = VOE, 25℃+ VOE, drift× ∆T<br>~~S × I~~IN<br>× 100%|±0.30%|±0.61%|
|PSRR error|ePSRR|ePSRR =PSRR × VS −3.3<br>~~I~~IN<br>× 100%|±0.04%|±0.08%|
|CMRR error|eCMRR|eCMRR =CMRR × VCM<br>~~I~~IN<br>× 100%|±0.01%|±0.02%|
|External Field error|eBext|eBext = BEXT× CMFR<br>~~I~~IN<br>× 100%|±0.02%|±0.03%|
|Sensitivity error|eS,ΔT|eS,∆T = eS, 25℃+ Sdrift, therm × ∆T × 100%|±0.70%|±0.70%|
|Nonlinearity error|eNL|Specified in_Electrical Characteristics_|±0.1%|±0.1%|
|RSS total error|eRSS,ΔT|eRSS,∆T =<br>eIos,∆T+ePSRR+eCMRR<br>2+ eBext<br>2+ eS,∆T<br>2+ eNL<br>2|0.79%|1.00%|


**9.2 Typical Application**







In many applications, power must be converted from AC sources for use in DC circuitry. Some type of controlled
power factor correction (PFC) stage is typically needed to improve power transfer efficiency. Faster and faster
power switches are being used in modern PFC stages to reduce overall size and to improve power transfer
efficiency. Often, the PFC stage of AC to DC converters is connected directly to AC power grids. A primary
challenge to sensing in PFC stages is that the current sensor is subjected to large voltage spikes coming
from the high-voltage (HV) power grid along with large transients coming from high speed power switches
during charge transfer. Inherent isolation in the TMCS1133 construction helps overcome these challenges by
providing high levels of isolation between the HV current sensing nodes and low-voltage control circuitry, with
high common-mode transient immunity (CMTI). Figure 9-2 shows the use of the TMCS1133 measuring phase
currents in a common AC to DC converter stage.


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


_**9.2.1 Design Requirements**_



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)


**Figure 9-2. AC to DC Converter Current Sensing**



For a 3-phase current sensing application, make sure to provide linear sensing across the expected current
range, and make sure that the device remains within working thermal constraints. A single TMCS1133 can
be used to measure current in each phase if necessary. For this example, consider a nominal supply of 5V
but a minimum of 4.9V to include for some supply variation. Maximum output swings are defined according to
TMCS1133 specifications, and a full-scale current measurement of ±20A is required.


**Table 9-3. Example Application Design Requirements**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|VS,nom|5V|
|VS,min|4.9V|
|IIN,FS|±20A|



_**9.2.2 Detailed Design Procedure**_


The primary design parameter for using the TMCS1133 is the optimum sensitivity variant based on the required
measured current levels and the selected supply voltage. Positive and negative currents are measured in
this in-line phase current application example, therefore select a bidirectional variant. The TMCS1133 has a
precision internal reference voltage that determines the zero current output voltage, VOUT,0A.

The internal reference voltage on TMCS1133AxA variants, with zero current output voltage VOUT,0A = 2.5V is
intended for bidirectional current measurements when used with 5V power supplies. The internal reference
voltage on TMCS1133BxA variants, with zero current output voltage VOUT,0A = 1.65V is intended for bidirectional
current measurements when used with 3.3V power supplies. Further consideration of noise and integration with
an ADC can be explored, but is beyond the scope of this application design example. The TMCS1133 output
voltage VOUT is proportional to the input current IIN as defined by Equation 30 with output offset set by VOUT,0A.


VOUT = IIN × S + VOUT, 0A (30)


Design of the sensing solution focuses on maximizing the sensitivity of the device while maintaining linear
measurement over the expected current input range. The TMCS1133 has a linear measurable current range that
is constrained by either the positive swing to supply or negative swing to ground. To account for the operating
margin, consider the previously defined minimum possible supply voltage VS,min = 4.9V. With the previous
parameters, the maximum linear output voltage VOUT,max is defined by Equation 31 and the minimum linear
output voltage VOUT,min is defined by Equation 32.


VOUT, max = VS, min −100mV (31)


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 31


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


VOUT, min = 100mV (32)


Design parameters for this example application are shown in Table 9-4 along with the calculated output range.


**Table 9-4. Example Application Design Parameters**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|VOUT,max|4.8V|
|VOUT,0A|2.5V|
|VOUT,max – VOUT,0A|2.3V|



These design parameters result in a maximum positive linear output voltage swing of ±2.3V about VOUT,0A =
2.5V. To determine which sensitivity variant of the TMCS1133 most fully uses this linear range, use Equation 33
to calculate the maximum current range for a bidirectional current ±IIN,max.



IIN, max =





where


 - S is the sensitivity of the relevant AxA variant.


Table 9-5 shows the calculation for each gain variant of the TMCS1133 with the appropriate sensitivities.


**Table 9-5. Maximum Full-Scale Current Ranges With 2.3V Positive Output Swing**

|VARIANT|SENSITIVITY|I<br>IN,max|
|---|---|---|
|TMCS1133A1A|25mV/A|±92A|
|TMCS1133A2A|50mV/A|±46A|
|TMCS1133A3A|75mV/A|±30.6A|
|TMCS1133A4A|100mV/A|±23A|
|TMCS1133A5A|150mV/A|±15.3A|



In general, the highest sensitivity variant is selected to provide the lowest maximum input current range that is
larger than the desired full-scale current range. For the design parameters in this example, the TMCS1133A4A
with sensitivity of 100mV/A is the proper selection because the maximum ±23A linear measurable range is larger
than the desired ±20A full-scale current range.


_**9.2.3 Application Curve**_


To illustrate high levels of isolation achievable between noisy high-voltage current sensing nodes and lowvoltage precision current measurement and control circuitry, Figure 9-3 shows the output signal from the
TMCS1133 in a noisy in-phase PWM motor control example. In this example with a large induction motor under
no load, no PWM edge interference is seen on the current sensor output with high-voltage PWM switching on
the current sensor input, as is often pronounced on many current sensors.


32 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)


**Figure 9-3. Inline Motor Current-Sense Input and Output Signals**



**9.3 Power Supply Recommendations**


The TMCS1133 only requires a power supply (VS) on the low-voltage isolated side, which powers the analog
circuitry independent of the isolated current input. VS determines the full-scale output range of the analog
output VOUT, and can be supplied with any voltage between 3V and 5.5V. To filter noise in the power-supply
path, place a low-ESR decoupling capacitor of 0.1µF between VS and GND pins as close as possible to the
supply and ground pins of the device. More decoupling capacitance can be added to compensate for noisy or
high-impedance power supplies. When used in extremely noisy environments, ferrite beads can be added close
to the supply pin as shown in Figure 9-4 to target and suppress high-frequency noise coupled on to system
supply.



**Supply**










|1|VS<br>VS<br>IN +<br>VOC<br>OC<br>VOUT<br>NC<br>IN<br>ALERT<br>GND|F.B.<br>10<br>9<br>0.1µF<br>8<br>7<br>6<br>5<br>4<br>3|
|---|---|---|
||||
|**2**|**2**|**2**|
||||
||||



**Figure 9-4. Power Supply Noise Filtering**


The TMCS1133 power supply VS can be sequenced independently of current flowing through the input.
However, there is a power-on delay between VS reaching the recommended operating voltage and the analog
output validation. During this power-on time, the output voltage VOUT can transition between GND and VS as the
output transfers from a high impedance reset state to the active drive state. If this behavior must be avoided,
then provide a stable supply voltage VS for longer than the power-on time prior to applying input current.

**9.4 Layout**

_**9.4.1 Layout Guidelines**_


The TMCS1133 is specified for a continuous current handling capability on the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_ which uses
4oz copper planes. This current capability is fundamentally limited by the maximum device junction temperature
and the thermal environment, primarily the PCB layout and design. To maximize current-handling capability and
thermal stability of the device, take care with PCB layout and construction to optimize the thermal capability.
Efforts to improve the thermal performance beyond the design and construction of the _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_ can


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 33


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


|TMCS1133<br>SBOSAG0D – OCTOBER 2023 – REVISE|D JUNE 2025|
|---|---|
|result in increased continuous<br>improving thermal performanc<br>•<br>Use large copper planes fo<br>•<br>Use heavier copper PCB c<br>•<br>Place thermal via_farms_ ar<br>•<br>Provide airflow across the<br>**_9.4.2 Layout Example_**<br>An example layout, shown in<br>targeted for thermal and ma<br>terminal connectors to the de|-current~~ capa~~bility due t~~o~~ higher h~~ea~~t tr~~ansfe~~r to the<br> eofthe PCB include:<br>  r both input current path and isolated power planes a<br>  onstruction.<br> ound the isolated current input.<br>  surface of the PCB.<br> Figure 9-5, is~~f~~r~~om~~ the _T_~~_MCS1133xEVM User's _~~_G_<br>  g~~netic~~ ~~char~~ac~~teristics of ~~thi~~s ~~l~~ayout, wh~~i~~chprovide~~s <br>  vi~~ce i~~np~~u~~t ~~p~~in~~s wh~~ile large cop~~per pla~~nes en~~hance~~t~~he~~|
|result in increased continuous<br>improving thermal performanc<br>•<br>Use large copper planes fo<br>•<br>Use heavier copper PCB c<br>•<br>Place thermal via_farms_ ar<br>•<br>Provide airflow across the<br>**_9.4.2 Layout Example_**<br>An example layout, shown in<br>targeted for thermal and ma<br>terminal connectors to the de||


**Figure 9-5. Recommended Board Layout**


**10 Device and Documentation Support**

**10.1 Device Nomenclature**


For orderable part numbers of _TMCS1133_ devices in the _SOIC_ package types, see the Package Option
[Addendum of this document, ti.com, or contact your TI sales representative.](http://www.ti.com)


For additional description of the device nomenclature markings on the die, see the _[Silicon Errata](https://www.ti.com/lit/pdf/SPRZxxx)_ .


**10.2 Device Support**

_**10.2.1 Development Support**_


For development tool support see the following:

 - Texas Instruments, _[TMCS1133xEVM](https://www.ti.com/lit/pdf/SBAU423)_


**10.3 Documentation Support**

_**10.3.1 Related Documentation**_


For related documentation see the following:

 - Texas Instruments, _[TMCS1133xEVM User's Guide](https://www.ti.com/lit/pdf/SBAU423)_

 - Texas Instruments, _[Isolation Glossary](https://www.ti.com/lit/pdf/SLLA353)_, application note


34 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[www.ti.com](https://www.ti.com)**


**10.4 Receiving Notification of Documentation Updates**



**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0)



To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Notifications_ to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.


**10.5 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**10.6 Trademarks**
TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.
**10.7 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**10.8 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**11 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision C (February 2025) to Revision D (June 2025)** **Page**

 - Updated the number formatting for tables, figures, and cross-references throughout the document ............... 1

 - Updated the VIORM in the Insulation Specifications section from 1344V to 1697V peak ................................ 5

 - Updated the reinforced isolation working voltage in the Insulation Specifications section from 600V to 950V
RMS ...................................................................................................................................................................5

 - Updated the reinforced isolation working voltage in the Insulation Specifications section from 849V to 1343V
DC ..................................................................................................................................................................... 5

 - Updated the basic isolation working voltage in the Insulation Specifications section from 950V to 1200V
RMS ...................................................................................................................................................................5

 - Added Power Ratings to the _Specifications_ .......................................................................................................5

 - Added Safety-Related Certification to the _Specifications_ .................................................................................. 5

 - Added Safety Limiting Values to the _Specifications_ ...........................................................................................5

 - Added the Input-Referred Noise Density vs Frequency graph to the _Typical Characteristics_ ......................... 10

 - Added the Insulation Characteristics Curves to the _Typical Characteristics_ ....................................................10

 - Added the Input Isolation section to _Feature Description_ for clarification.........................................................21


**Changes from Revision B (March 2024) to Revision C (February 2025)** **Page**

 - Updated the number formatting for tables, figures, and cross-references throughout the document ............... 1

 - Added the TMCS1133x9A variant device...........................................................................................................1

 - Updated typical hysteresis specification on variants TMCS1133x7A and TMCS1133x9A to better reflect actual
performance........................................................................................................................................................8


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ 35


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


**[TMCS1133](https://www.ti.com/product/TMCS1133)**
[SBOSAG0D – OCTOBER 2023 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBOSAG0) **[www.ti.com](https://www.ti.com)**


**Changes from Revision A (March 2024) to Revision B (August 2024)** **Page**

 - Updated the number formatting for tables, figures, and cross-references throughout the document ............... 1


**Changes from Revision * (October 2024) to Revision A (March 2024)** **Page**

 - Updated the number formatting for tables, figures, and cross-references throughout the document ............... 1


**12 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


36 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSAG0D&partnum=TMCS1133)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TMCS1133](https://www.ti.com/product/tmcs1133?qgpn=tmcs1133)_


## **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Jan-2026


**PACKAGING INFORMATION**





















Addendum-Page 1


## **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Jan-2026





















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
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 2


## **PACKAGE OPTION ADDENDUM**

www.ti.com 9-Jan-2026


**[OTHER QUALIFIED VERSIONS OF TMCS1133 :]**

- [[Automotive : ][TMCS1133-Q1]](http://focus.ti.com/docs/prod/folders/print/tmcs1133-q1.html)


[NOTE: Qualified Version Definitions:]

    - [Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects]


Addendum-Page 3


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


