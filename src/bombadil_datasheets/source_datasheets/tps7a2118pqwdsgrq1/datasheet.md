**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)

## **TPS7A21-Q1 Automotive, 500mA, Low-Noise, Low-I Q, High-PSRR LDO**



**1 Features**


- AEC-Q100 qualified for automotive applications:

–
Temperature grade 1: –40°C to +125°C

–
Junction temperature: –40°C to +150°C

- Very low I Q : 6.5μA

- Input voltage range: 2.0V to 6.0V

- Output voltage range: 0.8V to 5.5V (50mV steps)

- High PSRR: 91dB at 1kHz

- Low output voltage noise: 7.7μV RMS

- Low dropout:
– 265mV (maximum) at 500mA (2.5V V OUT )

- Smart EN pulldown

- Output voltage tolerance: ±1% over temperature

- Supports a wide range of ceramic capacitors:

–
1µF to 200µF

- Package:

– 3mm × 3mm wettable flank VSON

– 2mm × 2mm wettable flank WSON

– 2mm × 2mm WSON


**2 Applications**


- [DAS cameras and radar](https://www.ti.com/applications/automotive/adas/overview.html)

- [Automotive infotainment](https://www.ti.com/applications/automotive/infotainment-cluster/overview.html)

- Telematics systems

- Navigation systems



**3 Description**


The TPS7A21-Q1 is a small, low-dropout (LDO)
linear voltage regulator that sources 500mA of output
current. The device provides low noise, high PSRR,
and excellent load and line transient performance
to meet the requirements of RF and other sensitive
analog circuits in automotive applications. Innovative
design techniques result in low-noise performance
without the addition of an external noise bypass
capacitor. The TPS7A21-Q1 low quiescent current
is a good choice for low-power systems. The 2.0V
to 6.0V input voltage range and 0.8V to 5.5V
output voltage range support a variety of system
requirements.


An internal soft-start circuit helps control inrush
current, thus minimizing the input voltage drop during
start-up. The LDO is stable with small ceramic
capacitors, allowing for a small overall design size.


A smart enable input circuit with an internally
controlled pulldown resistor keeps the LDO disabled
even when the EN pin is unconnected. This circuit
also helps eliminate external components that are
otherwise required to pull down the EN input.


**Package Information**









INPUT


1 µF


ENABLE




|PART NUMBER|PACKAGE(1)|PACKAGE SIZE(2)|
|---|---|---|
|TPS7A21-Q1|DRB (Wettable flank<br>VSON, 8)|3mm × 3mm|
|TPS7A21-Q1|DSG (Wettable flank<br>WSON, 8)|2mm × 2mm|
|TPS7A21-Q1|DSG (WSON, 8)|2mm × 2mm|





(1) For more information, see the _Mechanical, Packaging, and_
_Orderable Information_ .
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.





**Simplified Application Schematic**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Pin Configuration and Functions** ...................................3
**5 Specifications** .................................................................. 4

5.1 Absolute Maximum Ratings........................................ 4
5.2 ESD Ratings............................................................... 4
5.3 Recommended Operating Conditions.........................4
5.4 Thermal Information....................................................5

5.5 Electrical Characteristics.............................................5
5.6 Typical Characteristics................................................ 7
**6 Detailed Description** ......................................................14

6.1 Overview................................................................... 14

6.2 Functional Block Diagram......................................... 14
6.3 Feature Description...................................................15
6.4 Device Functional Modes..........................................17



**7 Applications and Implementation** ................................ 18

7.1 Application Information............................................. 18
7.2 Typical Application.................................................... 21
7.3 Power Supply Recommendations.............................23
7.4 Layout....................................................................... 23
**8 Device and Documentation Support** ............................25

8.1 Device Support......................................................... 25
8.2 Documentation Support............................................ 25
8.3 Receiving Notification of Documentation Updates....25
8.4 Support Resources................................................... 25
8.5 Trademarks............................................................... 25
8.6 Electrostatic Discharge Caution................................25
8.7 Glossary....................................................................25
**9 Revision History** ............................................................ 26
**10 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 26



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**4 Pin Configuration and Functions**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)





Not to scale


**Figure 4-1. DRB Package, 8-Pin Fixed VSON (Top View)**







OUT


OUT


NC


GND











GND


EN


IN


IN





IN


IN


NC


EN







NC


NC


OUT


OUT



Not to scale

**Figure 4-2. DSG Package (DSG0008B), 8-Pin Fixed**

**WSON (Top View)**



Not to scale

**Figure 4-3. DSG Package (DSG0008A), 8-Pin Fixed**

**WSON C Version (Top View)**



**Table 4-1. Pin Functions**



















|PIN|Col2|Col3|Col4|TYPE(1)|DESCRIPTION|
|---|---|---|---|---|---|
|**NAME**|**DRB**|**DSG0008B**|**DSG0008A**<br>**(C Version)**|**DSG0008A**<br>**(C Version)**|**DSG0008A**<br>**(C Version)**|
|EN|5|5|2|I|Enable pin. Drive EN greater than VEN(HI) to turn on the regulator.<br>Drive EN less than VEN(LO) to put the low-dropout regulator (LDO)<br>into shutdown mode.|
|GND|4|4|1|—|Ground pin.|
|IN|8|7, 8|3, 4|I|Input pin. For best transient response and to minimize input<br>impedance, use the recommended value or larger ceramic capacitor<br>from IN to ground as listed in the_Recommended Operating_<br>_Conditions_ table and the_Input and Output Capacitor Requirements_<br>section. Place the input capacitor as close to the output of the device<br>as possible.|
|NC|2, 3, 6, 7|3, 6|7, 8|—|No internal connection. Ground this pin for better thermal<br>performance.|
|OUT|1|1, 2|5, 6|O|Regulated output voltage pin. Connect a low-equivalent series<br>resistance (ESR) capacitor to this pin. For best transient response,<br>use the nominal recommended value or larger capacitor from OUT to<br>GND. An internal pulldown resistor prevents a charge from remaining<br>on OUT when the regulator is in shutdown mode (VEN < VEN (LOW)).|
|Thermal Pad|Thermal Pad|Thermal Pad|Thermal Pad|Thermal Pad|The thermal pad is electrically connected to the GND node. Connect<br>to the GND plane for improved thermal performance.|


(1) I = input, O = output, NC = no connect.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 3


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**5 Specifications**


**5.1 Absolute Maximum Ratings**
over operating free-air temperature range (unless otherwise noted) [(1)] [(3)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|VIN|Input voltage|–0.3<br>6.5|V|
|VOUT|Output voltage|–0.3<br>Lesser of VIN + 0.3, or 6.5|V|
|VEN|Enable input voltage|–0.3<br>6.5|V|
||Maximum output current(3)|Internally limited|A|
|TJ|Operating junction temperature|-40<br>150|°C|
|Tstg|Storage temperature|–65<br>150|°C|



(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute maximum ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If briefly operating outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not
sustain damage, but it may not be fully functional. Operating the device in this manner may affect device reliability, functionality,
performance, and shorten the device lifetime.
(2) All voltages are with respect to the GND pin.
(3) Internal thermal shutdown circuitry helps protect the device from permanent damage.


**5.2 ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)|Electrostatic discharge|Charged-device model (CDM), per JEDEC specification JESD22-C101(2)|±750|±750|



(1) JEDEC document JEP155 states that 500V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250V CDM allows safe manufacturing with a standard ESD control process.


**5.3 Recommended Operating Conditions**
over the operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VIN|Input supply voltage|2.0<br>6.0|V|
|VEN|Enable input voltage|0<br>6.0|V|
|VOUT|Nominal output voltage range|0.8<br>5.5|V|
|IOUT|Output current|0<br>500|mA|
|CIN|Input capacitor(2)|1|µF|
|COUT|Output capacitor(3)|1<br>200|µF|
|ESR|Output capacitor effective series resistance|100|mΩ|
|TJ|Operating junction temperature|–40<br>150|°C|



(1) All voltages are with respect to the GND pin.
(2) An input capacitor is not required for LDO stability. However, an input capacitor with an effective value of 0.47μF minimum
is recommended to counteract the effect of source resistance and inductance, which in some cases causes symptoms of systemlevel instability such as ringing or oscillation, especially in the presence of load transients.
(3) Effective output capacitance of 0.4μF minimum and 200μF maximum over all temperature and voltage conditions is required for
stability with ESR values as high as 100mΩ. If the ESR is reduced to 20mΩ or lower, stable operation is achieved with effective output
capacitance as low as 0.3μF.


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**5.4 Thermal Information**





**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



|THERMAL METRIC(1)|Col2|TPS7A21-Q1|Col4|UNIT|
|---|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**DRB**<br>**(VSON)**|**DSG**<br>**(WSON)**|**DSG**<br>**(WSON)**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**8 PINS**|**8 PINS**|**8 PINS**|
|RθJA|Junction-to-ambient thermal resistance|58.9|77.7|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|76.3|109.0|°C/W|
|RθJB|Junction-to-board thermal resistance|31.8|44.5|°C/W|
|ψJT|Junction-to-top characterization parameter|6.3|7.2|°C/W|
|ψJB|Junction-to-board characterization parameter|31.8|44.5|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|13.3|17.0|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics and An](https://www.ti.com/lit/an/spra953c/spra953c.pdf?ts=1670537024185&ref_url=https%253A%252F%252Fwww.ti.com%252Fsitesearch%252Fen-us%252Fdocs%252Funiversalsearch.tsp%253FlangPref%253Den-US%2526searchTerm%253Dsemiconductor%2Band%2Bic%2Bpackage%2Bthermal%2Bmetrics%2526nr%253D10693)
[empirical analysis of the impact of board layout on LDO thermal performance application notes.](https://www.ti.com/lit/an/slvae85/slvae85.pdf)


**5.5 Electrical Characteristics**


specified over operating temperature range (T J = –40℃ to +150℃), V IN = V OUT(NOM) + 0.3V or 2V, whichever is greater, V EN
= 1.0V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF (unless otherwise noted); all typical values are at T J = 25℃









































|PARAMETER|Col2|TEST CONDITIONS|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|ΔVOUT|Output voltage tolerance|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>1mA < IOUT ≤ 500mA,<br>VOUT ≥ 3.3V|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>1mA < IOUT ≤ 500mA,<br>VOUT ≥ 3.3V|–2.25<br>1.5|%|
|ΔVOUT|Output voltage tolerance|VIN = (VOUT(NOM) + 0.3 V) to 6.0V,<br>1mA < IOUT ≤ 500mA,<br>2.8V ≤ VOUT < 3.3V|VIN = (VOUT(NOM) + 0.3 V) to 6.0V,<br>1mA < IOUT ≤ 500mA,<br>2.8V ≤ VOUT < 3.3V|–2.5<br>1.5|–2.5<br>1.5|
|ΔVOUT|Output voltage tolerance|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>IOUT = 1mA<br>VOUT ≥ 2.8V|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>IOUT = 1mA<br>VOUT ≥ 2.8V|–1<br>1|–1<br>1|
|ΔVOUT|Output voltage tolerance|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>1mA < IOUT ≤ 500mA,<br>VOUT < 2.8V|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>1mA < IOUT ≤ 500mA,<br>VOUT < 2.8V|–70<br>50|mV|
|ΔVOUT|Output voltage tolerance|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>IOUT = 1mA<br>VOUT < 2.8V|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>IOUT = 1mA<br>VOUT < 2.8V|–50<br>50|–50<br>50|
|ΔVOUT|Line regulation|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>IOUT = 1mA|VIN = (VOUT(NOM) + 0.3V) to 6.0V,<br>IOUT = 1mA|0.03|%/V|
|ΔVOUT|Load regulation|IOUT= 1mA to 500mA|IOUT= 1mA to 500mA|0.003|%/mA|
|IGND|Quiescent current|VEN = VIN, VIN = 6.0V,<br>IOUT = 0mA|TJ = 25°C|6.5<br>9|µA|
|IGND|Quiescent current|VEN = VIN, VIN = 6.0V,<br>IOUT = 0mA|TJ = –40°C to 85°C|11|11|
|IGND|Quiescent current|VEN = VIN, VIN = 6.0V,<br>IOUT = 0mA|TJ = –40°C to 125°C|15|15|
|IGND|Quiescent current|VEN = VIN, VIN = 6.0V,<br>IOUT = 0mA|TJ = –40°C to 150°C|18|18|
|IGND|Quiescent current|VEN = VIN, VIN = 6.0V, IOUT = 500mA|VEN = VIN, VIN = 6.0V, IOUT = 500mA|2300<br>3500|2300<br>3500|
|ISHTDWN|Shutdown current|VEN = 0V (disabled), VIN = 6.0V, TJ = 25°C|VEN = 0V (disabled), VIN = 6.0V, TJ = 25°C|0.15<br>1|µA|
|ISHTDWN|Shutdown current|VEN = 0V (disabled), VIN = 6.0V, TJ = –40°C to 150°C|VEN = 0V (disabled), VIN = 6.0V, TJ = –40°C to 150°C|10|10|
|IQ(DO)|Quiescent current in dropout|VIN ≤ VOUT(NOM), IOUT = 0mA|VIN ≤ VOUT(NOM), IOUT = 0mA|7<br>15|µA|
|VDO|Dropout voltage|IOUT = 500mA,<br>VOUT = 95% ×<br>VOUT(NOM)|0.8V ≤ VOUT < 1.0V(1)|825|mV|
|VDO|Dropout voltage|IOUT = 500mA,<br>VOUT = 95% ×<br>VOUT(NOM)|1.0V ≤ VOUT < 1.2V(1)|605|605|
|VDO|Dropout voltage|IOUT = 500mA,<br>VOUT = 95% ×<br>VOUT(NOM)|1.2V ≤ VOUT < 1.5V(1)|470|470|
|VDO|Dropout voltage|IOUT = 500mA,<br>VOUT = 95% ×<br>VOUT(NOM)|1.5V ≤ VOUT < 2.5V|355|355|
|VDO|Dropout voltage|IOUT = 500mA,<br>VOUT = 95% ×<br>VOUT(NOM)|2.5V ≤ VOUT ≤ 5.5V|265|265|
|ICL|Output current limit|VOUT = 0.9 × VOUT(NOM)|VOUT = 0.9 × VOUT(NOM)|650<br>1060<br>1500|mA|
|ISC|Short-circuit current limit|VOUT = 0 V|VOUT = 0 V|325|mA|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 5


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**5.5 Electrical Characteristics (continued)**


specified over operating temperature range (T J = –40℃ to +150℃), V IN = V OUT(NOM) + 0.3V or 2V, whichever is greater, V EN
= 1.0V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF (unless otherwise noted); all typical values are at T J = 25℃































|PARAMETER|Col2|TEST CONDITIONS|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|PSRR|Power-supply rejection ratio|IOUT = 20mA,<br>VIN = VOUT + 1.0 V|f = 100Hz|90|dB|
|PSRR|Power-supply rejection ratio|IOUT = 20mA,<br>VIN = VOUT + 1.0 V|f = 1kHz|91|91|
|PSRR|Power-supply rejection ratio|IOUT = 20mA,<br>VIN = VOUT + 1.0 V|f = 10kHz|71|71|
|PSRR|Power-supply rejection ratio|IOUT = 20mA,<br>VIN = VOUT + 1.0 V|f = 100kHz|61|61|
|PSRR|Power-supply rejection ratio|IOUT = 20mA,<br>VIN = VOUT + 1.0 V|f = 1MHz|50|50|
|PSRR|Power-supply rejection ratio|IOUT = 500mA,<br>VIN = VOUT + 1.0 V|f = 100Hz|65|65|
|PSRR|Power-supply rejection ratio|IOUT = 500mA,<br>VIN = VOUT + 1.0 V|f = 1kHz|85|85|
|PSRR|Power-supply rejection ratio|IOUT = 500mA,<br>VIN = VOUT + 1.0 V|f = 10kHz|79|79|
|PSRR|Power-supply rejection ratio|IOUT = 500mA,<br>VIN = VOUT + 1.0 V|f = 100kHz|44|44|
|PSRR|Power-supply rejection ratio|IOUT = 500mA,<br>VIN = VOUT + 1.0 V|f = 1MHz|50|50|
|VN|Output noise voltage|BW = 10Hz to<br>100kHz,<br>VOUT = 2.8V|IOUT = 500mA|7.7|µVRMS|
|VN|Output noise voltage|BW = 10Hz to<br>100kHz,<br>VOUT = 2.8V|IOUT = 1mA|10|10|
|RPULLDOWN|Output automatic discharge<br>pulldown resistance|VIN = 2V, VEN < VIL (output disabled)|VIN = 2V, VEN < VIL (output disabled)|150|Ω|
|TSD|Thermal shutdown rising|TJ rising|TJ rising|165|°C|
|TSD|Thermal shutdown falling|TJ falling|TJ falling|140|140|
|VEN(LOW)|Low input threshold|VIN = 2.0V to 6.0V,<br>VEN falling until the output is disabled|VIN = 2.0V to 6.0V,<br>VEN falling until the output is disabled|0.3|V|
|VEN(HI)|High input threshold|VIN = 2.0V to 6.0V,<br>VENrising until the output is enabled|VIN = 2.0V to 6.0V,<br>VENrising until the output is enabled|0.9|V|
|VUVLO|UVLO threshold|VIN rising|VIN rising|1.11<br>1.32<br>1.63|V|
|VUVLO|UVLO threshold|VIN falling|VIN falling|1.05<br>1.27<br>1.57|1.05<br>1.27<br>1.57|
|VUVLO(HYST)|UVLO hysteresis|||50|mV|
|IEN|EN pin leakage current|VEN = 6.0V and VIN = 6.0V|VEN = 6.0V and VIN = 6.0V|100<br>300|nA|
|REN(PULL-<br>DOWN)|Smart enable pulldown resistor|||440|kΩ|
|tON|Turnon time|From VEN > VIH to VOUT = 95% of VOUT(NOM)|From VEN > VIH to VOUT = 95% of VOUT(NOM)|120<br>200<br>280|µs|


(1) Dropout voltages for V OUT values below or very near the UVLO threshold are not measured directly. Values shown are verified by
simulation.


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)






















|Col1|-55 °|TJ<br>C|85 °|C|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||~~-40 °~~<br>0 °C<br>25 °C||~~125~~<br>150|~~°C~~<br>°C|||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


|Col1|Col2|Col3|Col4|TJ|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||-55°<br>||0°C<br>||85°C<br>||150°||||
||~~-40°~~||~~25°C~~||~~125°~~||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||








|V = 1V<br>EN<br>Figure 5-1. Output Voltage Accuracy vs I<br>OUT|V = 1V<br>EN<br>Figure 5-2. Output Voltage Accuracy vs I<br>OUT|
|---|---|
|VEN = 1V<br>**Figure 5-3. Output Voltage Accuracy vs VIN**|VEN = 1V<br>**Figure 5-4. Line Regulation vs VIN**|
|Output Current (mA)<br>Change in Output Voltage (mV)<br>0<br>50<br>100<br>150<br>200<br>250<br>300<br>350<br>400<br>450<br>500<br>0<br>2<br>4<br>6<br>8<br>10<br>12<br>Load<br>TJ<br>-55 °C<br>~~-40 °C~~<br>0 °C<br>25 °C<br>85 °C<br>~~125 °C~~<br>150 °C<br>VEN = 1V<br>**Figure 5-5. Load Regulation vs IOUT**|Output Current (mA)<br>Dropout Voltage (mV)<br>0<br>50<br>100<br>150<br>200<br>250<br>300<br>350<br>400<br>450<br>500<br>50<br>60<br>70<br>80<br>90<br>100<br>110<br>120<br>130<br>140<br>150<br>160<br>TJ<br>-55°C<br>~~-40°C~~<br>0°C<br>~~25°C~~<br>85°C<br>~~125°C~~<br>150°C<br>VEN = 1V<br>**Figure 5-6. Dropout Voltage vs IOUT**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 7


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (continued)**


at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)












|Col1|-55°C|Col3|0°C|TJ|85°C|Col7|150°|C|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||~~-40°~~||~~25°C~~||~~125°~~||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||








|-5|5°C|TJ<br>-40°C|0°C|2|5°C|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||


|85<br>TJ<br>-55°C 0°C 85°C 150°C<br>80 -40°C 25°C 125°C<br>(mV)<br>75<br>Voltage<br>70<br>Dropout<br>65<br>60<br>55<br>0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2<br>Output Current (mA)<br>V = 1V<br>EN<br>Figure 5-7. Dropout Voltage vs I<br>OUT|V = V<br>EN IN<br>Figure 5-8. I vs V<br>Q IN|
|---|---|
|VEN = 1V<br>**Figure 5-9. IQ vs VIN**|VEN = 1V<br>**Figure 5-10. IGND vs IOUT**|
|VEN = 1V<br>**Figure 5-11. IGND vs IOUT**|Input Voltage (V)<br>Quiescent Current in Shutdown (nA)<br>1.8<br>2.4<br>3<br>3.6<br>4.2<br>4.8<br>5.4<br>6<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>TJ<br>~~-55°C~~<br>~~-40°C~~<br>~~0°C~~<br>~~25°C~~<br>VEN = 0V, IOUT = 0mA<br>**Figure 5-12. Shutdown Current vs VIN**|



8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (continued)**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)




|8|5°C|TJ<br>125°C|150|°C|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||


|Col1|T|J|Col4|Col5|
|---|---|---|---|---|
||~~-55°C~~<br>-40°C<br>~~0°C~~<br>25°C|~~85~~<br>12|~~C~~<br>°C|~~150°C~~|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||




















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||T<br>|J<br>||||
|||~~-5~~<br>-4|~~°C~~<br>°C||~~5°C~~<br>5°C||~~15~~|~~°C~~|
|||0°|C||125°|C|||


|3000<br>TJ<br>85°C 125°C 150°C (nA)<br>2500<br>Shutdown<br>2000<br>in<br>1500 Current<br>1000<br>Quiescent<br>500<br>0<br>1.8 2.4 3 3.6 4.2 4.8 5.4 6<br>Input Voltage (V)<br>V = 0V, I = 0mA<br>EN OUT<br>Figure 5-13. Shutdown Current vs V<br>IN|5<br>TJ<br>4.5 -55°C 0°C 85°C 150°C<br>-40°C 25°C 125°C<br>4<br>3.5 (V)<br>3 Voltage<br>2.5<br>2 Output<br>1.5<br>1<br>0.5<br>0<br>0 200 400 600 800 1000 1200 1400<br>Output Current (mA)<br>V = 1V<br>EN<br>Figure 5-14. Foldback Current Limit|
|---|---|
|<br>**Figure 5-15. Enable Logic Threshold vs Temperature**|VEN - VIN (V)<br>Enable Pin Leakage Current (nA)<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>6<br>0<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>3500<br>4000<br>4500<br>5000<br>TJ<br>~~-55°C~~<br>-40°C<br>0°C<br>~~25°C~~<br>85°C<br>125°C<br>~~150°C~~<br>VEN = 6V, IOUT = 0mA<br>**Figure 5-16. Enable Pin Leakage Current vs VEN – VIN**|
|VEN = 0.3V<br>**Figure 5-17. Smart Enable Pulldown Resistor vs Temperature**<br>**and VIN**|VEN = 0.3V<br>**Figure 5-18. Output Pulldown Resistance vs**<br>**Temperature and VIN**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 9


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (continued)**


at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)






|V = 1V<br>EN<br>Figure 5-19. V UVLO Threshold vs Temperature<br>IN|V = 0V to 4.3V, slew rate = 1V/μs, I = 500mA<br>IN OUT<br>Figure 5-20. Start-Up With V Before V<br>EN IN|
|---|---|
|VIN = 0V to 4.3V, slew rate = 1V/μs, IOUT = 0mA<br>**Figure 5-21. Start-Up With VEN After VIN**|VIN = 0V to 4.3V, slew rate = 1V/μs, IOUT = 500mA<br>**Figure 5-22. Start-Up With VEN After VIN**|
|VIN = 0V to 4.3V, slew rate = 1V/μs, IOUT = 500mA<br> <br>**Figure 5-23. Start-Up With VEN = VIN**|VIN = 4.3V, VEN = 0V to 4.3V, slew rate = 1V/μs,<br>IOUT = 0mA, COUT = 1μF<br>**Figure 5-24. Start-Up Inrush Current**|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (continued)**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)










|V = 4.3V, V = 0V to 4.3V, slew rate = 1V/μs,<br>IN EN<br>I = 0mA, C = 10μF<br>OUT OUT<br>Figure 5-25. Start-Up Inrush Current|V = V to V = 95% of V, I = 0mA<br>EN EN(HI) OUT OUT(NOM) OUT<br>Figure 5-26. Start-Up Turn-On Time vs Temperature|
|---|---|
|Time (µs)<br>AC-Coupled Output Voltage (mV)<br>Input Voltage (V)<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>-3<br>-2<br>-2<br>-1<br>-1<br>0<br>0<br>1<br>1<br>2<br>2<br>3<br>3<br>4<br>4<br>5<br>5<br>6<br>~~V~~OUT<br>VIN<br>VEN = VIN, tr = tf = 5μs, IOUT = 500mA<br>**Figure 5-27. Line Transient From 3.6V to 4.6V**|Time (µs)<br>AC-Coupled Output Voltage (mV)<br>Input Voltage (V)<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>-3<br>-2<br>-2<br>-1<br>-1<br>0<br>0<br>1<br>1<br>2<br>2<br>3<br>3<br>4<br>4<br>5<br>5<br>6<br>~~V~~OUT<br>VIN<br>VEN = VIN, tr = tf = 5μs, IOUT = 1mA<br>**Figure 5-28. Line Transient From 3.6V to 4.6V**|
|VEN = VIN, tr = tf = 1μs<br>**Figure 5-29. Load Transient From 1mA to 500mA**|VEN = VIN, tr = tf = 200ns<br>**Figure 5-30. Load Transient From 1mA to 500mA**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 11


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (continued)**


at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)






|V = V, t = t = 1μs<br>EN IN r f<br>Figure 5-31. Load Transient From 0mA to 500mA|V = V, t = t = 200ns<br>EN IN r f<br>Figure 5-32. Load Transient From 0mA to 500mA|
|---|---|
|VEN = VIN<br>**Figure 5-33. PSRR vs Frequency and IOUT**|VEN = VIN, IOUT = 20mA<br>**Figure 5-34. PSRR vs Frequency and VIN**|
|VEN = VIN, IOUT = 500mA<br>**Figure 5-35. PSRR vs Frequency and VIN**|VEN = VIN, IOUT = 20mA<br>**Figure 5-36. PSRR vs Frequency and COUT**|



12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (continued)**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



at V IN = 3.6V, V OUT = 3.3V, I OUT = 1mA, C IN = 1µF, C OUT = 1µF, and T A = 25°C (unless otherwise noted)




























|V = V, I = 500mA<br>EN IN OUT<br>Figure 5-37. PSRR vs Frequency and C<br>OUT|2<br>1 3.6 V, RMS NV oIN ise = 6.73 VRMS<br>0.5 4.75 V, RMS Noise = 6.70 VRMS (VHz)<br>6.0 V, RMS Noise = 6.65 VRMS<br>0.2<br>0.1 Noise<br>0.05<br>Voltage<br>0.02<br>0.01 Output<br>0.005<br>0.002<br>0.001<br>10 100 1k 10k 100k 1M 10M<br>Frequency (Hz)<br>V = V, I = 20mA<br>EN IN OUT<br>Figure 5-38. Noise vs Frequency and V<br>IN|
|---|---|
|Frequency (Hz)<br>Output Voltage Noise (VHz)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>**5**<br>10<br>100<br>1k<br>10k<br>100k<br>1M<br>10M<br>~~VIN~~<br>~~3.6 V, RMS Noise = 6.90V~~RMS<br>~~4.75 V, RMS Noise = 7.32VRMS~~<br>~~6.0 V, RMS Noise = 11.54VRMS~~<br>VEN = VIN, IOUT = 500mA<br>**Figure 5-39. Noise vs Frequency and VIN**|VEN = VIN<br>**Figure 5-40. Noise vs Frequency and IOUT**|
|Frequency (Hz)<br>Output voltage Noise (VHz)<br>0.001<br>0.002<br>0.003<br>0.005<br>0.01<br>0.02<br>0.03<br>0.05<br>0.1<br>0.2<br>0.3<br>0.5<br>1<br>10<br>100<br>1k<br>10k<br>100k<br>1M<br>10M<br>~~COUT~~<br>~~0.47 µF, RMS Noise = 6.63VRMS~~<br>~~1.0 µF, RMS Noise = 6.71V~~RMS<br>~~10 µF, RMS Noise = 7.20V~~RMS<br>200 uF, RMS Noise = 7.69VRMS<br>VEN = VIN, IOUT = 20mA<br>**Figure 5-41. Noise vs Frequency and COUT**|Frequency (Hz)<br>Output voltage Noise (VHz)<br>0.001<br>0.002<br>0.003<br>0.005<br>0.01<br>0.02<br>0.03<br>0.05<br>0.1<br>0.2<br>0.3<br>0.5<br>1<br>10<br>100<br>1k<br>10k<br>100k<br>1M<br>10M<br>~~COUT~~<br>~~0.47 µF, RMS Noise = 6.84VRMS~~<br>~~1.0 µF, RMS Noise = 6.96V~~RMS<br>~~10 µF, RMS Noise = 7.16V~~RMS<br>200 uF, RMS Noise = 8.74VRMS<br>VEN = VIN, IOUT = 500mA<br>**Figure 5-42. Noise vs Frequency and COUT**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 13


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**6 Detailed Description**


**6.1 Overview**


Designed to meet the needs of sensitive RF and analog circuits, the TPS7A21-Q1 provides low noise, high
PSRR, low quiescent current, and excellent line and load transient response. The TPS7A21-Q1 achieves
excellent noise performance without the need for a separate noise filter capacitor.


The TPS7A21-Q1 is designed to operate properly with a single 1µF input capacitor and a single 1µF ceramic
output capacitor. Make sure the effective output capacitance is at least 0.4µF across all operating voltage and
temperature conditions.


**6.2 Functional Block Diagram**


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**6.3 Feature Description**


_**6.3.1 Smart Enable (EN)**_



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



The enable pin (EN) is active high. The output is enabled when the voltage applied to EN is greater than V EN(HI)
and disabled when the applied voltage is less than V EN(LOW) . If external control of the output voltage is not
needed, connect EN to IN. This device has a smart enable circuit to reduce quiescent current. When the voltage
on the enable pin is driven above V EN(HI), the output is enabled and the smart enable internal pulldown resistor
(R EN(PULLDOWN) ) is disconnected. When the enable pin is floating, the R EN(PULLDOWN) is connected and pulls the
enable pin low to disable the output. In addition to reducing quiescent current, the smart pulldown helps make
sure that the logic level is correct even when EN is driven from a source that has limited current drive capability.
The R value is listed in the _Electrical Characteristics_ table.
EN(PULLDOWN)


_**6.3.2 Low Output Noise**_


Any internal noise at the TPS7A21-Q1 reference voltage is reduced by a first-order, low-pass RC filter before
being passed to the output buffer stage. The low-pass RC filter has a –3dB cutoff frequency of approximately
0.1Hz. During start-up, the filter resistor is bypassed to reduce output rise time. The filter begins normal
operation after the output voltage reaches the nominal value.


_**6.3.3 Active Discharge**_


The regulator has an internal metal-oxide-semiconductor field-effect transistor (MOSFET) that connects a
pulldown resistor between the output and ground pins when the device is disabled to actively discharge the
output voltage. Make sure the voltage on IN is high enough to turn on the pulldown MOSFET. When V IN is too
low to provide sufficient V GS on the pulldown MOSFET, the pulldown circuit is not active. The active discharge
circuit is activated by the enable pin, or by the voltage on IN falling below the undervoltage lockout (UVLO)
threshold.


Do not rely on the active discharge circuit for discharging a large amount of output capacitance after the
input supply collapses. Reverse current potentially flows from the output to the input. This reverse current flow
potentially causes damage to the device. Limit any such transient reverse current to no more than 5% of the
device rated current.


_**6.3.4 Dropout Voltage**_


Dropout voltage (V DO ) is defined as the input voltage minus the output voltage (V IN – V OUT ) at the rated output
current (I RATED ), when the pass transistor is fully on. I RATED is the maximum I OUT listed in the _Recommended_
_Operating Conditions_ table. The pass transistor is in the ohmic or triode region of operation, and acts as a
switch. The dropout voltage indirectly specifies a minimum input voltage greater than the nominal programmed
output voltage at which the output voltage is expected to stay in regulation. If the input voltage falls to less than
the value required to support output regulation, then the output voltage falls as well.


For a CMOS regulator, the dropout voltage is determined by the drain-source, on-state resistance (R DS(ON) ) of
the pass transistor. Therefore, if the linear regulator operates at less than the rated current, the dropout voltage
for that current scales accordingly. Equation 1 calculates the R DS(ON) of the device.


R = V DO
DS(ON) I RATED (1)


_**6.3.5 Foldback Current Limit**_


The TPS7A21-Q1 has an internal current limit circuit that protects the regulator during transient high-load current
faults or shorting events. The current limit is a hybrid brick-wall foldback scheme. The current limit transitions
from a brick-wall scheme to a foldback scheme at the foldback voltage (V FOLDBACK ).


In a high-load current fault with the output voltage above V FOLDBACK, the brick-wall scheme limits the output
current to the current limit (I CL ). When the output voltage drops below V FOLDBACK, a foldback current limit
activates that scales back the current when the output voltage approaches GND. When the output is shorted, the


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 15


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


device supplies a typical current called the _short-circuit current limit_ (I SC ). I CL and I SC are listed in the _Electrical_
_Characteristics_ table.


The output voltage is not regulated when the device is in current limit. When a current limit event occurs, the
regulator begins to heat up because of the increase in power dissipation. When the device is in brick-wall
current limit, the pass transistor dissipates power [(V IN – V OUT ) × I CL ]. When the output is shorted and the output
voltage is less than V FOLDBACK, the pass transistor dissipates power [(V IN – V OUT ) × I SC ]. If thermal shutdown
is triggered, the device turns off. After the device cools down, the internal thermal shutdown circuit turns the
device back on. If the output current fault condition persists, the device cycles between current limit and thermal
shutdown. For more information on current limits, see the _[Know Your Limits](https://www.ti.com/lit/pdf/snva736)_ application note.


Figure 6-1 shows a diagram of the foldback current limit.


V OUT


Brickwall


V OUT(NOM)


V FOLDBACK



0 V

|Bri|Col2|Col3|Col4|
|---|---|---|---|
|Br<br>Foldback|Br<br>Foldback|Br<br>Foldback|Br<br>Foldback|
|||||



0 mA


_**6.3.6 Undervoltage Lockout**_



I OUT



I SC I RATED I CL


**Figure 6-1. Foldback Current Limit**



An independent undervoltage lockout (UVLO) circuit monitors the input voltage, allowing a controlled and
consistent turn on and turn off of the output voltage. If the input voltage drops during load transients (when
the device output is enabled), the UVLO has built-in hysteresis to prevent unwanted turn off.


_**6.3.7 Thermal Overload Protection (T**_ _**SD**_ _**)**_


Thermal shutdown disables the output when the junction temperature T J rises to the shutdown temperature
threshold T SD . The thermal shutdown circuit hysteresis requires the temperature to fall to a lower temperature
before turning on again. The thermal time constant of the semiconductor die is fairly short. Thus, the device
cycles on and off when thermal shutdown is reached until power dissipation is reduced.


High power dissipation occurs during start up from large V IN – V OUT voltage drops across the device or from
high inrush currents charging large output capacitors. Under some conditions, the thermal shutdown protection
disables the device before start up completes.


For reliable operation, limit the junction temperature to the maximum listed in the _Recommended Operating_
_Conditions_ table. Operation above this maximum temperature causes the regulator to exceed operational
specifications.


16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



Although the thermal shutdown circuitry is designed to protect against temporary thermal overload conditions,
this circuitry is not intended to replace proper thermal design. Continuously running the regulator into thermal
shutdown or above the maximum recommended junction temperature reduces long-term reliability.


**6.4 Device Functional Modes**


_**6.4.1 Device Functional Mode Comparison**_


Table 6-1 shows the conditions that lead to the different modes of operation. See the _Electrical Characteristics_
table for parameter values.


**Table 6-1. Device Functional Mode Comparison**



|OPERATING MODE|PARAMETER|Col3|Col4|Col5|
|---|---|---|---|---|
|**OPERATING MODE**|**VIN**|**VEN**|**IOUT**|**TJ**|
|Normal operation|VIN > VOUT(nom) + VDO and VIN > VIN(min)|VEN ≥ VEN(HI)|IOUT < IOUT(max)|TJ < TSD(shutdown)|
|Dropout operation|VIN(min) < VIN < VOUT(nom) + VDO|VEN ≥ VEN(HI)|IOUT < IOUT(max)|TJ < TSD(shutdown)|
|Disabled<br>(any true condition<br>disables the device)|VIN < VUVLO|VEN ≤ VEN(LOW)|Not applicable|TJ ≥ TSD(shutdown)|


_**6.4.2 Normal Operation**_





The device regulates to the nominal output voltage when the following conditions are met:


 - The input voltage is greater than the nominal output voltage plus the dropout voltage (V OUT(nom) + V DO )

 - The output current is less than the current limit (I OUT < I CL )

 - The device junction temperature is less than the thermal shutdown temperature (T J < T SD )

 - The enable voltage has previously exceeded the enable rising threshold voltage and has not yet decreased
to less than the enable falling threshold


_**6.4.3 Dropout Operation**_


If the input voltage is lower than the nominal output voltage plus the specified dropout voltage, but all other
conditions are met for normal operation, the device operates in dropout mode. In this mode, the output voltage
tracks the input voltage. During this mode, the transient performance of the device becomes significantly
degraded because the pass transistor is in the ohmic or triode region, and acts as a switch. Line or load
transients in dropout result in large output-voltage deviations.


When the device is in a steady dropout state (defined as when the device is in dropout, V IN < V OUT(NOM) + V DO,
directly after being in a normal regulation state, but _not_ during start up), the pass transistor is driven into the
ohmic or triode region. When the input voltage returns to a value greater than or equal to the nominal output
voltage plus the dropout voltage (V OUT(NOM) + V DO ), the output voltage overshoots for a short period of time
while the device pulls the pass transistor back into the linear region.


For output currents less than approximately 200mA, the slope of the dropout voltage curve is lower than for
higher currents. This slope helps maintain better performance when the LDO is in dropout.


_**6.4.4 Disabled**_


Shut down the output of the device by forcing the enable pin voltage to less than V EN(LOW) ). When disabled,
the pass transistor is turned off, internal circuits are shut down, and the output voltage is actively discharged to
ground by an internal discharge circuit from the output to ground.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 17


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**7 Applications and Implementation**


**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**7.1 Application Information**


_**7.1.1 Recommended Capacitor Types**_


The device is designed to be stable using low equivalent series resistance (ESR) ceramic capacitors at
the input and output. Multilayer ceramic capacitors have become the industry standard for many types of
applications and are recommended, but use good judgment. Ceramic capacitors that employ X7R-, X5R-,
and C0G-rated dielectric materials provide good capacitive stability across temperature, whereas the use of
Y5V-rated capacitors is discouraged because of large variations in capacitance.


Regardless of the ceramic capacitor type selected, the effective capacitance varies with operating voltage
and temperature. Consult the manufacturer data sheet to verify performance. Generally, expect the effective
capacitance to decrease by as much as 50%. The input and output capacitors recommended in the
_Recommended Operating Conditions_ table account for an effective capacitance of approximately 50% of the
nominal value.


_**7.1.2 Input and Output Capacitor Requirements**_


Although the LDO is stable without an input capacitor, good design practice is to connect a capacitor from IN
to GND, with a value at least equal to the nominal value specified in the _Recommended Operating Conditions_
table. The input capacitor counteracts reactive input sources and improves transient response, input ripple, and
PSRR, and is recommended if the source impedance is greater than 0.5Ω. When the source resistance and
inductance are sufficiently high, the overall system is susceptible to instability (including ringing and sustained
oscillation) and other performance degradation if there is insufficient capacitance between IN and GND. A
capacitor with a value greater than the minimum is necessary if there are large fast-rise-time load or line
transients or if the LDO is located more than a few centimeters from the input power source.


An output capacitor of an appropriate value helps provide stability and improve dynamic performance. Use an
output capacitor within the range specified in the _Recommended Operating Conditions_ table.


_**7.1.3 Load Transient Response**_


The load-step transient response is the output voltage response by the LDO to a step in load current, whereby
output voltage regulation is maintained. There are two key transitions during a load transient response: the
transition from a light to a heavy load and the transition from a heavy to a light load. The regions shown in Figure
7-1 are broken down as follows. Regions A, E, and H are where the output voltage is in a steady state.


~~tAt~~ ~~tCt~~ ~~tDt~~ ~~tEt~~ ~~tGt~~ ~~tHt~~

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|B|B|B|F|F|F||



**Figure 7-1. Load Transient Waveform**


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


During transitions from a light load to a heavy load, the:



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)




 - Initial voltage dip is a result of the depletion of the output capacitor charge and parasitic impedance to the
output capacitor (region B)

 - Recovery from the dip results from the LDO increasing the sourcing current, and leads to output voltage
regulation (region C)


During transitions from a heavy load to a light load, the:


 - Initial voltage rise results from the LDO sourcing a large current, and leads to the output capacitor charge to
increase (region F)

 - Recovery from the rise results from the LDO decreasing the sourcing current in combination with the load
discharging the output capacitor (region G)


A larger output capacitance reduces the peaks during a load transient but slows down the response time of the
device. A larger DC load also reduces the peaks because the amplitude of the transition is lowered and a higher
current discharge path is provided for the output capacitor.


_**7.1.4 Undervoltage Lockout (UVLO) Operation**_


The UVLO circuit makes sure that the device remains disabled before the input supply reaches the minimum
operational voltage range, and makes sure that the device shuts down when the input supply collapses. Figure
7-2 shows the UVLO circuit response to various input voltage events. The diagram is separated into the
following parts:


 - Region A: The device does not start until the input reaches the UVLO rising threshold.

 - Region B: Normal operation, regulating device.

 - Region C: Brownout event above the UVLO falling threshold (UVLO rising threshold – UVLO hysteresis). The
output falls out of regulation but the device remains enabled.

 - Region D: Normal operation, regulating device.

 - Region E: Brownout event below the UVLO falling threshold. The device is disabled in most cases and the
output falls because of the load and active discharge circuit. The device is re-enabled when the UVLO rising
threshold is reached by the input voltage and a normal start-up follows.

 - Region F: Normal operation followed by the input falling to the UVLO falling threshold.

 - Region G: The device is disabled when the input voltage falls below the UVLO falling threshold to 0V. The
output falls because of the load and active discharge circuit.


UVLO Rising Threshold


UVLO Hysteresis


V IN



V OUT






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||C<br>~~tBt~~|||~~tEt~~|~~tFt~~|~~tGt~~|
||C<br>~~tBt~~||~~tDt~~|~~tDt~~|~~tDt~~|~~tDt~~|
|~~tAt~~|~~tAt~~|~~tAt~~|~~tAt~~|~~tAt~~|~~tAt~~|~~tAt~~|



**Figure 7-2. Typical UVLO Operation**


_**7.1.5 Power Dissipation (P**_ _**D**_ _**)**_


Circuit reliability demands that proper consideration be given to device power dissipation, location of the circuit
on the printed circuit board (PCB), and correct sizing of the thermal plane. Make sure the PCB area around the
regulator is as free as possible of other heat-generating devices that cause added thermal stresses.


As a first-order approximation, power dissipation in the regulator depends on the input-to-output voltage
difference and load conditions. Use Equation 2 to approximate P D :


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 19


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


P D = (V IN – V OUT ) × I OUT (2)


Power dissipation is minimized, and thus greater efficiency achieved, by proper selection of the system voltage
rails. Proper selection allows the minimum input-to-output voltage differential to be obtained. The low dropout of
the TPS7A21-Q1 allows for maximum efficiency across a wide range of output voltages.


The main heat conduction path for the device is through the thermal pad on the package. As such, solder the
thermal pad to a copper pad area under the device. This pad area contains an array of plated vias that conduct
heat to any inner plane areas or to a bottom-side copper plane.


The maximum allowable junction temperature (T J ) determines the maximum power dissipation for the device.
According to Equation 3, power dissipation and junction temperature are most often related by the junction-toambient thermal resistance (R θJA ) of the combined PCB and device package and the temperature of the ambient
air (T A ).


T J = T A + (R θJA × P D ) (3)


Equation 4 rearranges Equation 3 for output current.


I OUT = (T J – T A ) / [R θJA × (V IN – V OUT )] (4)


Unfortunately, this thermal resistance (R θJA ) is highly dependent on the heat-spreading capability built into the
particular PCB design, and therefore varies according to the total copper area, copper weight, and location
of the planes. The R θJA recorded in the _Thermal Information_ table is determined by the JEDEC standard,
PCB, and copper-spreading area, and is only used as a relative measure of package thermal performance.
For a well-designed thermal layout, R θJA is actually the sum of the package junction-to-case (bottom) thermal
resistance (R θJC(bot) ) plus the thermal resistance contribution by the PCB copper.


_**7.1.6 Estimating Junction Temperature**_


The JEDEC standard now recommends the use of psi (Ψ) thermal metrics to estimate the junction temperatures
of the LDO when in-circuit on a typical PCB board application. These metrics are not strictly speaking thermal
resistances, but rather offer practical and relative means of estimating junction temperatures. These psi metrics
are determined to be significantly independent of the copper-spreading area. The key thermal metrics (Ψ JT and
Ψ JB ) are used in accordance with Equation 5 and are given in the _Thermal Information_ table.


Ψ JT : T J = T T + Ψ JT × P D and Ψ JB : T J = T B + Ψ JB × P D (5)


where:


 - P D is the power dissipated as explained in the _Power Dissipation (P_ _D_ _)_ section

 - T T is the temperature at the center-top of the device package

 - T B is the PCB surface temperature measured 1mm from the device package and centered on the package
edge


_**7.1.7 Recommended Area For Continuous Operation**_


The operational area of an LDO is limited by the dropout voltage, output current, junction temperature, and input
voltage. The recommended area for continuous operation for a linear regulator is given in Figure 7-3 and is
separated into the following parts:


 - Dropout voltage limits the minimum differential voltage between the input and the output (V IN – V OUT ) at a
given output current level. See the _Dropout Operation_ section for more details.

 - The rated output currents limits the maximum recommended output current level. Exceeding this rating
causes the device to fall out of specification.

 - The rated junction temperature limits the maximum junction temperature of the device. Exceeding this rating
causes the device to fall out of specification and reduces long-term reliability.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)



–
The shape of the slope is depicted in the third region of Figure 7-3. The slope is nonlinear because the
maximum-rated junction temperature of the LDO is controlled by the power dissipation across the LDO.
Thus, when V IN – V OUT increases the output current decreases.

 - The rated input voltage range governs both the minimum and maximum of V IN – V OUT .


Figure 7-3 shows the recommended area of operation for this device on a JEDEC-standard high-K board with a
R θJA, as given in the _Thermal Information_ table.





V IN ± V OUT (V)


**Figure 7-3. Region Description of Continuous Operation Regime**


**7.2 Typical Application**


Figure 7-4 shows the typical application circuit for the TPS7A21-Q1. If necessary for some applications, increase
the input and output capacitances above the 1µF minimum value.





INPUT


1 µF


ENABLE







|Col1|IN OUT<br>TPS7A21-Q1<br>EN<br>GND|Col3|
|---|---|---|
||||


**Figure 7-4. TPS7A21-Q1 Typical Application**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 21


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


_**7.2.1 Design Requirements**_


Table 7-1 summarizes the design requirements for the typical application circuit.


**Table 7-1. Design Parameters**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|Input voltage range|3.6V to 4.2V|
|Output voltage|3.3V|
|Output current|350mA|
|Maximum ambient temperature|125°C|



_**7.2.2 Detailed Design Procedure**_


For this design example, the 3.3V output version (TPS7A2133PQWDRBRQ1) is selected. A nominal 3.6V input
supply is assumed. Use a minimum 1.0μF input capacitor to minimize the effect of resistance and inductance
between the source and the LDO input. Use a minimum 1.0μF output capacitor for stability and good load
transient response. The dropout voltage (V DO ) is less than 150mV maximum at a 3.3V output voltage and
500mA output current, so there are no dropout issues with an input voltage of 3.6V and a maximum output
current of 350mA.


**7.2.2.1 Power Dissipation and Device Operation**


The permissible power dissipation for any package is a measure of the capability of the device to pass heat from
the power source (the junctions of the device) to the ultimate heat sink of the ambient environment. Thus, power
dissipation is dependent on the ambient temperature and the thermal resistance across the various interfaces
between the die junction and ambient air.


Equation 6 calculates the maximum allowable power dissipation for the device in a given package:


P D-MAX = ((T J-MAX – T A ) / R θJA ) (6)


Equation 7 represents the actual power being dissipated in the device:


P D = (V IN – V OUT ) × I OUT (7)


These two equations establish the relationship between the maximum power dissipation allowed resulting from
thermal consideration, the voltage drop across the device, and the continuous current capability of the device.
Use these two equations to determine the optimum operating conditions for the device in the application.


In applications where lower power dissipation (P D ) or excellent package thermal resistance (R θJA ) is present,
increase the maximum ambient temperature (T A-MAX ).


In applications where high power dissipation or poor package thermal resistance is present, derate the maximum
ambient temperature (T A-MAX ) if necessary. As given by Equation 8, T A-MAX is dependent on the maximum
operating junction temperature (T J-MAX-OP = 150°C), the maximum allowable power dissipation in the device
package in the application (P D-MAX ), and the junction-to ambient thermal resistance of the device or package in
the application (R θJA ):


T A-MAX = (T J-MAX-OP – (R θJA × P D-MAX )) (8)


Alternately, if T A-MAX is unable to be derated, do not reduce the P D value. This reduction is accomplished by
reducing V IN in the _V_ _IN_ _–V_ _OUT_ term as long as the minimum V IN is met, or by reducing the _I_ _OUT_ term, or by some
combination of the two.


22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


_**7.2.3 Application Curves**_


V IN = 0V to 4.3V, slew rate = 1V/μs, I OUT = 1mA


**Figure 7-5. Start-Up With V** **EN** **After V** **IN**


**7.3 Power Supply Recommendations**



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)


V EN = V IN, I OUT = 500mA


**Figure 7-6. PSRR vs Frequency and V** **IN**



This LDO is designed to operate from an input supply voltage range of 2.0V to 5.5V. Make sure the input supply
is well regulated and free of spurious noise. To make sure that the TPS7A21-Q1 output voltage is well regulated
and dynamic performance is optimum, set the input supply to be at least V OUT + 0.3V. A minimum capacitor
value of 1µF is required to be within 1cm of the IN pin.


**7.4 Layout**


_**7.4.1 Layout Guidelines**_


The dynamic performance of the TPS7A21-Q1 is dependent on the layout of the PCB. PCB layout practices that
are adequate for typical LDOs potentially degrade the PSRR, noise, or transient performance of the TPS7A21Q1.


Best performance is achieved by placing C IN and C OUT on the same side of the PCB as the TPS7A21-Q1, and
as close to the package as practical. Route the ground connections for C IN and C OUT back to the TPS7A21-Q1
ground pin using as wide and short a copper trace as practical.


Avoid connections using long trace lengths, narrow trace widths, or connections through vias. These
connections add parasitic inductances and resistance that results in inferior performance, especially during
transient conditions.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 23


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


_**7.4.2 Layout Example**_


**Figure 7-7. Typical DRB Layout**


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[www.ti.com](https://www.ti.com)**


**8 Device and Documentation Support**


**8.1 Device Support**


_**8.1.1 Device Nomenclature**_



**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**

[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437)








|PRODUCT(1) (2)|V<br>OUT|
|---|---|
|TPS7A21**xx(x)(C)PQ(W)yyyzQ1**|**xx(x)** is the nominal output voltage. For output voltages with a resolution of 100 mV, two digits<br>are used in the ordering number; otherwise, three digits are used (for example, 28 = 2.8V; 125 =<br>1.25V).<br>**C** (when present) indicates an alternate pin configuration.<br>**P** indicates an active output discharge feature. All variants of the TPS7A21 actively discharge the<br>output when the device is disabled.<br>**Q** indicates that this device is a Grade-1 device in accordance with the AEC-Q100 standard.<br>**W** (when present) indicates the package has wettable flanks.<br>**yyy** is the package designator.<br>**z** is the package quantity. R is for a 3,000 piece reel.<br>**Q1** indicates that this is an automotive grade (AEC-Q100) device.|



(1) For the most current package and ordering information see the Package Option Addendum at the end of this document, or visit the
[device product folder at www.ti.com.](https://www.ti.com)
(2) Output voltages from 0.8V to 5.5V in 50mV increments are available. Contact the factory for details and availability.


**8.2 Documentation Support**


_**8.2.1 Related Documentation**_


For related documentation see the following:

 - Texas Instruments, _[QFN/SON PCB Attachment](https://www.ti.com/lit/pdf/SLUA271)_ application report


**8.3 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Notifications_ to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.


**8.4 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**8.5 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

**8.6 Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**8.7 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ 25


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


**[TPS7A21-Q1](https://www.ti.com/product/TPS7A21-Q1)**
[SBVS437D – DECEMBER 2022 – REVISED JUNE 2025](https://www.ti.com/lit/pdf/SBVS437) **[www.ti.com](https://www.ti.com)**


**9 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision C (June 2024) to Revision D (June 2025)** **Page**

 - Changed 8-pin DSG device status from _Advance Information_ to _Production Data_ ........................................... 1


**Changes from Revision B (February 2024) to Revision C (June 2024)** **Page**

 - Changed wettable flank WSON (DGS) package from _Advance Information_ to _Production Data_ ...................... 1

 - Changed output voltage tolerance from _±1% at 1mA I_ _OUT_ to _±1% over temperature_ ....................................... 1

 - Deleted maximum output voltage tolerance discussion from _Description_ section..............................................1

 - Corrected redundant voltage tolerance conditions............................................................................................ 5

 - EN pin maximum leakage current changed from 250nA to 300nA.....................................................................5


**10 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBVS437D&partnum=TPS7A21-Q1)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[TPS7A21-Q1](https://www.ti.com/product/tps7a21-q1?qgpn=tps7a21-q1)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 16-Jun-2025


**PACKAGING INFORMATION**





















Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 16-Jun-2025





















**(1)** **Status:** [For more details on status, see our product life cycle.](https://www.ti.com/support-quality/quality-policies-procedures/product-life-cycle.html)


**(2)** **Material type:** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.


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


Addendum-Page 2


### **PACKAGE OPTION ADDENDUM**

www.ti.com 16-Jun-2025


and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

**[OTHER QUALIFIED VERSIONS OF TPS7A21-Q1 :]**

- [[Catalog : ][TPS7A21]](http://focus.ti.com/docs/prod/folders/print/tps7a21.html)


[NOTE: Qualified Version Definitions:]


    - [Catalog - TI's standard catalog product]


Addendum-Page 3


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 16-Jun-2025


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
|PS7A21105PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|S7A21105PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2109PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2110PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2110PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2112PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2112PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2115PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2115PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2118CPQDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2118PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2118PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2128PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2128PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2131PQDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2131PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 16-Jun-2025























|Device|Package<br>Type|Package<br>Drawing|Pins|SPQ|Reel<br>Diameter<br>(mm)|Reel<br>Width<br>W1 (mm)|A0<br>(mm)|B0<br>(mm)|K0<br>(mm)|P1<br>(mm)|W<br>(mm)|Pin1<br>Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TPS7A2133PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2133PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|
|TPS7A2150PQWDRBRQ1|SON|DRB|8|5000|330.0|12.4|3.3|3.3|1.1|8.0|12.0|Q2|
|TPS7A2150PQWDSGRQ1|WSON|DSG|8|3000|180.0|8.4|2.2|2.2|1.2|4.0|8.0|Q2|


Pack Materials-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 16-Jun-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|PS7A21105PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|S7A21105PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2109PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2110PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2110PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2112PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2112PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2115PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2115PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2118CPQDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2118PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2118PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2128PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2128PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2131PQDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2131PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|
|TPS7A2133PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2133PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|



Pack Materials-Page 3


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 16-Jun-2025

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TPS7A2150PQWDRBRQ1|SON|DRB|8|5000|367.0|367.0|35.0|
|TPS7A2150PQWDSGRQ1|WSON|DSG|8|3000|213.0|191.0|35.0|



Pack Materials-Page 4


## **PACKAGE OUTLINE** **DRB0008J VSON - 1 mm max height**

PLASTIC QUAD FLAT PACK- NO LEAD




















|Col1|Col2|9|
|---|---|---|
|||9|
||||


|Col1|0.1|C A|B|
|---|---|---|---|
||0.05|C|C|





NOTES:


1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for optimal thermal and mechanical performance.


**www.ti.com**


## **EXAMPLE BOARD LAYOUT** **DRB0008J VSON - 1 mm max height**

PLASTIC QUAD FLAT PACK- NO LEAD





































NOTES: (continued)


4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271) .
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.


**www.ti.com**


## **EXAMPLE STENCIL DESIGN** **DRB0008J VSON - 1 mm max height**

PLASTIC QUAD FLAT PACK- NO LEAD




















|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
||||||9|
|||||||
|||||||







NOTES: (continued)


6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


**www.ti.com**


## **GENERIC PACKAGE VIEW**

# **DSG 8 WSON - 0.8 mm max height**

**2 x 2, 0.5 mm pitch** PLASTIC SMALL OUTLINE - NO LEAD


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4224783/A


www.ti.com


## **PACKAGE OUTLINE**

# **DSG0008B WSON - 0.8 mm max height**

~~SCALE 5.500~~


PLASTIC SMALL OUTLINE - NO LEAD







































NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.


www.ti.com


## **EXAMPLE BOARD LAYOUT**

# **DSG0008B WSON - 0.8 mm max height**

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

# **DSG0008B WSON - 0.8 mm max height**

PLASTIC SMALL OUTLINE - NO LEAD





















NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


www.ti.com


## **PACKAGE OUTLINE**

# **DSG0008A WSON - 0.8 mm max height**

~~SCALE 5.500~~


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


