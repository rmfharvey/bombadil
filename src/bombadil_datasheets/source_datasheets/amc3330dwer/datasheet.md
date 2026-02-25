**1 Features**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)
## **AMC3330 Precision, ±1V Input, Reinforced Isolated Amplifier** **With Integrated DC/DC Converter**


**3 Description**




- 3.3V or 5V single supply operation with integrated
DC/DC converter

- ±1V input voltage range optimized for voltage
measurements with high input impedance

- Fixed gain: 2.0

- Low DC errors:

  - Gain error: ±0.2% (max)

  - Gain drift: ±45ppm/°C (max)

  - Offset error: ±0.3mV (max)

  - Offset drift: ±4µV/°C (max)

  - Nonlinearity: ±0.02% (max)

- High CMTI: 85kV/µs (min)

- System-level diagnostic features

- Safety-related certifications:

  - 6000VPK reinforced isolation per DIN EN IEC
60747-17 (VDE 0884-17)

  - 4250VRMS isolation for 1 minute per UL1577

- Meets CISPR-11 and CISPR-25 EMI standards


**2 Applications**


- Isolated voltage sensing in:

  - [Motor drives](http://www.ti.com/applications/industrial/motor-drives/overview.html)

  - [Photovoltaic inverters](http://www.ti.com/applications/industrial/grid-infrastructure/overview.html)

  - [Power delivery systems](http://www.ti.com/applications/industrial/power-delivery/overview.html)

  - [EV charging infrastructure](https://www.ti.com/applications/industrial/energy-infrastructure/ev-charging/)

  - [Battery energy storage systems](https://www.ti.com/solution/battery-energy-storage-system)



The AMC3330 is a precision, isolated amplifier with
a fully integrated, isolated DC/DC converter that
allows single-supply operation from the low-side of
the device. The reinforced capacitive isolation barrier
is certified according to DIN EN IEC 60747-17 (VDE
0884-17) and UL1577 and separates sections of
the system that operate on different common-mode
voltage levels and protects low-voltage domains from
damage.


The input of the AMC3330 is optimized for
direct connection to high-impedance, voltage-signal
sources such as a resistor-divider network to
sense high-voltage signals. The integrated isolated
DC/DC converter allows measurement of non-groundreferenced signals and makes the device a unique
solution for noisy, space-constrained applications.


The excellent performance of the device supports
accurate voltage monitoring and control. The
integrated DC/DC converter fault-detection and
diagnostic output pin of the AMC3330 simplify
system-level design and diagnostics.


The AMC3330 is specified over the temperature
range of –40°C to +125°C.


**Package Information**

|PART NUMBER|PACKAGE(1)|PACKAGE SIZE(2)|
|---|---|---|
|AMC3330|DWE (SOIC, 16)|10.3mm × 10.3mm|



(1) For more information, see the _Mechanical, Packaging, and_
_Orderable Information_ .
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.




















|Col1|DCDC_OUT|Col3|Col4|Col5|
|---|---|---|---|---|
||DCDC_HGND|||Isolated<br>Power|
|HLDO_IN<br>HLDO_OUT<br>NC|HLDO_IN||||
|HLDO_IN<br>HLDO_OUT<br>NC|HLDO_IN||||
|INP|INP||||
|INN|INN|INN|INN|INN|


|330|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|
|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|||DCDC_GND<br>DIAG|DCDC_GND<br>DIAG|DCDC_GND<br>DIAG||
|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|||DIAG|DIAG|DIAG|DIAG|
|Isolated<br>Power|Isolated<br>Power|Isolated<br>Power|||LDO_OUT||||
|Isolated<br>Power|Isolated<br>Power||||VDD||||
|Isolated<br>Power|Isolated<br>Power||||OUTP||||
||||||OUTN<br>||||


|DCDC_OUT<br>DCDC_HGND<br>HLDO_IN<br>NC<br>HLDO_OUT<br>+1.0 V INP<br>0 V –1.0 V INN<br>HGND|Col2|AMC3330<br>Isolated Isolated<br>Power Power<br>Isolation<br>Reinforced|(3.3 V or 5 V)<br>DCDC_IN<br>DCDC_GND<br>DIAG To MCU (optional)<br>LDO_OUT<br>VDD<br>OUTP<br>OUTN VCMout ±2.05 V ADC<br>GND|
|---|---|---|---|
|||||



**Application Example**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


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
5.5 Power Ratings.............................................................5
5.6 Insulation Specifications............................................. 6
5.7 Safety-Related Certifications ..................................... 7
5.8 Safety Limiting Values.................................................7
5.9 Electrical Characteristics.............................................8
5.10 Switching Characteristics..........................................9
5.11 Timing Diagram....................................................... 10
5.12 Insulation Characteristics Curves............................11
5.13 Typical Characteristics............................................ 12
**6 Detailed Description** ......................................................18

6.1 Overview................................................................... 18



6.2 Functional Block Diagram......................................... 18
6.3 Feature Description...................................................18
6.4 Device Functional Modes..........................................22
**7 Application and Implementation** .................................. 23

7.1 Application Information............................................. 23
7.2 Typical Application.................................................... 23
7.3 Best Design Practices...............................................27
7.4 Power Supply Recommendations.............................27
7.5 Layout....................................................................... 29
**8 Device and Documentation Support** ............................30

8.1 Device Support......................................................... 30
8.2 Documentation Support............................................ 30
8.3 Receiving Notification of Documentation Updates....30
8.4 Support Resources................................................... 30
8.5 Trademarks............................................................... 30
8.6 Electrostatic Discharge Caution................................30
8.7 Glossary....................................................................30
**9 Revision History** ............................................................ 31
**10 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 31



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**4 Pin Configuration and Functions**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



Not to scale


**Figure 4-1. DWE Package, 16-Pin SOIC (Top View)**


**Table 4-1. Pin Functions**



|PIN|Col2|TYPE|DESCRIPTION|
|---|---|---|---|
|**NO.**|**NAME**|**NAME**|**NAME**|
|1|DCDC_OUT|Power|High-side output of the isolated DC/DC converter; connect this pin to the HLDO_IN pin.(1)|
|2|DCDC_HGND|Power Ground|High-side ground reference for the isolated DC/DC converter; connect this pin to the HGND pin.|
|3|HLDO_IN|Power|Input of the high-side low-dropout (LDO) regulator; connect this pin to the DCDC_OUT pin.(1)|
|4|NC|—|No internal connection. Connect this pin to the high-side ground or leave this pin unconnected<br>(floating).|
|5|HLDO_OUT|Power|Output of the high-side LDO.(1)|
|6|INP|Analog Input|Noninverting analog input.|
|7|INN|Analog Input|Inverting analog input. Connect this pin to HGND.|
|8|HGND|Signal Ground|High-side analog ground; connect this pin to the DCDC_HGND pin.|
|9|GND|Signal Ground|Low-side analog ground; connect this pin to the DCDC_GND pin.|
|10|OUTN|Analog Output|Inverting analog output.|
|11|OUTP|Analog Output|Noninverting analog output.|
|12|VDD|Power|Low-side power supply.(1)|
|13|LDO_OUT|Power|Output of the low-side LDO; connect this pin to the DCDC_IN pin.(1)|
|14|DIAG|Digital Output|Active-low, open-drain status indicator output; connect this pin to the pullup supply (for example,<br>VDD) using a resistor or leave this pin floating if not used.|
|15|DCDC_GND|Power Ground|Low-side ground reference for the isolated DC/DC converter; connect this pin to the GND pin.|
|16|DCDC_IN|Power|Low-side input of the isolated DC/DC converter; connect this pin to the LDO_OUT pin.(1)|


(1) See the _Power Supply Recommendations_ section for power-supply decouplng recommendations.


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 3


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**5 Specifications**

**5.1 Absolute Maximum Ratings**
see [(1)]






|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|Power-supply voltage|VDD to GND|–0.3<br>6.5|V|
|Analog input voltage|INP, INN|HGND – 6<br>VHLDOout + 0.5|V|
|Analog output voltage|OUTP, OUTN|GND – 0.5<br>VDD + 0.5|V|
|Digital output voltage|DIAG|GND – 0.5<br>6.5|V|
|Input current|Continuous, any pin except power-supply pins|–10<br>10|mA|
|Temperature|Junction, TJ|150|°C|
|Temperature|Storage, Tstg|–65<br>150|–65<br>150|



(1) Operation outside the _Absolute Maximum Ratings_ may cause permanent device damage. _Absolute Maximum Ratings_ do not imply
functional operation of the device at these or any other conditions beyond those listed under _Recommended Operating Conditions_ .
If used outside the _Recommended Operating Conditions_ but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime


**5.2 ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)|Electrostatic discharge|Charged-device model (CDM), per per ANSI/ESDA/JEDEC JS-002(2)|±1000|±1000|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**5.3 Recommended Operating Conditions**
over operating ambient temperature range (unless otherwise noted)











|Col1|Col2|Col3|MIN NOM MAX|UNIT|
|---|---|---|---|---|
|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|
|VDD|Low-side supply voltage|VDD to GND|3.0<br>3.3<br>5.5|V|
|**ANALOG INPUT**|**ANALOG INPUT**|**ANALOG INPUT**|**ANALOG INPUT**|**ANALOG INPUT**|
|VClipping|Differential input voltage before clipping output|VIN = VINP – VINN|±1.25|V|
|VFSR|Specified linear differential full-scale voltage|VIN = VINP – VINN|–1<br>1|V|
||Absolute common-mode input voltage(1)|(VINP + VINN) / 2 to HGND|–2<br>3|V|
|VCM|Operating common-mode input voltage|(VINP + VINN) / 2 to HGND,<br>VINP = VINN|–1.4<br>1.6|V|
|VCM|Operating common-mode input voltage|(VINP + VINN) / 2 to HGND,<br>|VINP – VINN| = 1.0 V(2)|–0.925<br>0.725|–0.925<br>0.725|
|VCM|Operating common-mode input voltage|(VINP + VINN) / 2 to HGND,<br>|VINP – VINN| = 1.25 V|–0.8<br>0.6|–0.8<br>0.6|
|**ANALOG OUTPUT**|**ANALOG OUTPUT**|**ANALOG OUTPUT**|**ANALOG OUTPUT**|**ANALOG OUTPUT**|
|CLOAD|Capacitive load|On OUTP or OUTN to GND2,<br>Without any series resistance|500|pF|
|CLOAD|Capacitive load|OUTP to OUTN, Without any series<br>resistance|250|pF|
|RLOAD|Resistive load|On OUTP or OUTN to GND2|10<br>1|kΩ|
|**DIGITAL OUTPUT**|**DIGITAL OUTPUT**|**DIGITAL OUTPUT**|**DIGITAL OUTPUT**|**DIGITAL OUTPUT**|
||Pull-up supply-voltage for DIAG pin||0<br>VDD|V|
|**TEMPERATURE RANGE**|**TEMPERATURE RANGE**|**TEMPERATURE RANGE**|**TEMPERATURE RANGE**|**TEMPERATURE RANGE**|
|TA|Operating ambient temperature||–40<br>25<br>125|°C|


(1) Steady-state voltage supported by the device in case of a system failure. See specified common-mode input voltage VCM for normal
operation. Observe analog input voltage range as specified in the _Absolute Maximum Ratings_ table.
(2) Linear response.


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**5.4 Thermal Information**





**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



|THERMAL METRIC(1)|Col2|AMC3330|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**DWE (SOIC)**|**DWE (SOIC)**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**16 PINS**|**16 PINS**|
|RθJA|Junction-to-ambient thermal resistance|73.5|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|31|°C/W|
|RθJB|Junction-to-board thermal resistance|44|°C/W|
|ψJT|Junction-to-top characterization parameter|16.7|°C/W|
|ψJB|Junction-to-board characterization parameter|42.8|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|n/a|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
report.


**5.5 Power Ratings**






|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|PD|Maximum power dissipation|VDD = 5.5 V|236.5|mW|
|PD|Maximum power dissipation|VDD = 3.6 V|155|155|



Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 5


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**5.6 Insulation Specifications**
over operating ambient temperature range (unless otherwise noted)

































|PARAMETER|Col2|TEST CONDITIONS|VALUE|UNIT|
|---|---|---|---|---|
|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|**GENERAL**|
|CLR|External clearance(1)|Shortest pin-to-pin distance through air|≥ 8|mm|
|CPG|External creepage(1)|Shortest pin-to-pin distance across the package surface|≥ 8|mm|
|DTI|Distance through insulation|Minimum internal gap (internal clearance - capacitive signal<br>isolation)|≥ 21|µm|
|DTI|Distance through insulation|Minimum internal gap (internal clearance - transformer power<br>isolation)|≥ 120|µm|
|CTI|Comparative tracking index|DIN EN 60112 (VDE 0303-11); IEC 60112|≥ 600|V|
||Material group|According to IEC 60664-1|I||
||Overvoltage category<br>per IEC 60664-1|Rated mains voltage ≤ 600VRMS|I-III||
||Overvoltage category<br>per IEC 60664-1|Rated mains voltage ≤ 1000VRMS|I-II|I-II|
|**DIN EN IEC 60747-17 (VDE 0884-17)**|**DIN EN IEC 60747-17 (VDE 0884-17)**|**DIN EN IEC 60747-17 (VDE 0884-17)**|**DIN EN IEC 60747-17 (VDE 0884-17)**|**DIN EN IEC 60747-17 (VDE 0884-17)**|
|VIORM|Maximum repetitive peak<br>isolation voltage|At AC voltage|1700|VPK|
|VIOWM|Maximum-rated isolation<br>working voltage|At AC voltage (sine wave)|1200|VRMS|
|VIOWM|Maximum-rated isolation<br>working voltage|At DC voltage|1700|VDC|
|VIOTM|Maximum transient<br>isolation voltage|VTEST = VIOTM, t = 60s (qualification test),<br>VTEST = 1.2 × VIOTM, t = 1s (100% production test)|6000|VPK|
|VIMP|Maximum impulse voltage(2)|Tested in air, 1.2/50µs waveform per IEC 62368-1|7700|VPK|
|VIOSM|Maximum surge<br>isolation voltage(3)|Tested in oil (qualification test),<br>1.2/50µs waveform per IEC 62368-1|10000|VPK|
|qpd|Apparent charge(4)|Method a, after input/output safety test subgroups 2 and 3,<br>Vpd(ini) = VIOTM, tini = 60s, Vpd(m) = 1.2 × VIORM, tm = 10s|≤ 5|pC|
|qpd|Apparent charge(4)|Method a, after environmental tests subgroup 1,<br>Vpd(ini) = VIOTM, tini = 60s, Vpd(m) = 1.6 × VIORM, tm = 10 s|≤ 5|≤ 5|
|qpd|Apparent charge(4)|Method b1, at preconditioning (type test) and routine test,<br>Vpd(ini) = 1.2 x VIOTM, tini = 1s, Vpd(m) = 1.875 × VIORM, tm = 1s|≤ 5|≤ 5|
|qpd|Apparent charge(4)|Method b2, at routine test (100% production)(6),<br>Vpd(ini) = Vpd(m) = 1.2 x VIOTM, tini = tm = 1s|≤ 5|≤ 5|
|CIO|Barrier capacitance,<br>input to output(5)|VIO = 0.5 VPP at 1MHz|~4.5|pF|
|RIO|Insulation resistance,<br>input to output(5)|VIO = 500 V at TA = 25°C|> 1012|Ω|
|RIO|Insulation resistance,<br>input to output(5)|VIO = 500 V at 100°C ≤ TA ≤ 125°C|> 1011|> 1011|
|RIO|Insulation resistance,<br>input to output(5)|VIO = 500 V at TS = 150°C|> 109|> 109|
||Pollution degree||2||
||Climatic category||40/125/21||
|**UL1577**|**UL1577**|**UL1577**|**UL1577**|**UL1577**|
|VISO|Withstand isolation voltage|VTEST = VISO, t = 60s (qualification test),<br>VTEST = 1.2 × VISO, t = 1s (100% production test)|4250|VRMS|


(1) Apply creepage and clearance requirements according to the specific equipment isolation standards of an application.Maintain the
creepage and clearance distance of a board design to make sure that the mounting pads of the isolator on the printed circuit board
(PCB) do not reduce this distance. Creepage and clearance on a PCB become equal in certain cases. Techniques such as inserting
grooves, ribs, or both on a PCB are used to help increase these specifications.
(2) Testing is carried out in air to determine the surge immunity of the package.
(3) Testing is carried in oil to determine the intrinsic surge immunity of the isolation barrier.
(4) Apparent charge is electrical discharge caused by a partial discharge (pd).
(5) All pins on each side of the barrier are tied together, creating a two-pin device.
(6) Either method b1 or b2 is used in production.


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**5.7 Safety-Related Certifications**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)









|VDE|UL|
|---|---|
|DIN EN IEC 60747-17 (VDE 0884-17),<br>EN IEC 60747-17,<br>DIN EN IEC 62368-1 (VDE 0868-1),<br>EN IEC 62368-1,<br>IEC 62368-1 Clause : 5.4.3 ; 5.4.4.4 ; 5.4.9|Recognized under 1577 component recognition and<br>CSA component acceptance NO 5 programs|
|Reinforced insulation|Single protection|
|Certificate number: 40040142|File number: E181974|


**5.8 Safety Limiting Values**
Safety limiting [(1)] intends to minimize potential damage to the isolation barrier upon failure of input or output circuitry. A
failure of the I/O can allow low resistance to ground or the supply and, without current limiting, dissipate sufficient power to
over-heat the die and damage the isolation barrier potentially leading to secondary system failures.







|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|IS|Safety input, output, or supply current|RθJA = 73.5°C/W, VDD = 5.5 V,<br>TJ = 150°C, TA = 25°C|309|mA|
|IS|Safety input, output, or supply current|RθJA = 73.5°C/W, VDD = 3.6 V,<br>TJ = 150°C, TA = 25°C|472|472|
|PS|Safety input, output, or total power|RθJA = 73.5°C/W,<br>TJ = 150°C, TA = 25°C|1700|mW|
|TS|Maximum safety temperature||150|°C|


(1) The maximum safety temperature, TS, has the same value as the maximum junction temperature, TJ, specified for the device. The IS
and PS parameters represent the safety current and safety power, respectively. Do not exceed the maximum limits of IS and PS. These
limits vary with the ambient temperature, TA.
The junction-to-air thermal resistance, RθJA, in the _Thermal Information_ table is that of a device installed on a high-K test board for
leaded surface-mount packages. Use these equations to calculate the value for each parameter:
TJ = TA + RθJA × P, where P is the power dissipated in the device.
TJ(max) = TS = TA + RθJA × PS, where TJ(max) is the maximum junction temperature.
PS = IS × VDDmax, where VDDmax is the maximum low-side voltage.


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 7


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**5.9 Electrical Characteristics**

minimum and maximum specifications apply from TA = –40°C to +125°C, VDD = 3.0 V to 5.5 V, INP = –1 V to +1 V, and INN





















|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**ANALOG INPUT**|**ANALOG INPUT**|**ANALOG INPUT**|**ANALOG INPUT**|**ANALOG INPUT**|
|RIN|Single-ended input resistance|INN = HGND|0.1<br>0.8|GΩ|
|RIND|Differential input resistance||0.1<br>1.2|0.1<br>1.2|
|IIB|Input bias current|INP = INN = HGND, IIB = (IIBP +<br>IIBN) / 2|–10<br>2.5<br>10|nA|
|TCIIB|Input bias current drift||–14|pA/°C|
|IIO|Input offset current|IIO = IINP – IINN; INP = INN = HGND|–10<br>-0.8<br>10|nA|
|CIN|Single-ended input capacitance|INN = HGND, fIN = 310 kHz|2|pF|
|CIND|Differential input capacitance|fIN = 310 kHz|2|2|
|**ANALOG OUTPUT**|**ANALOG OUTPUT**|**ANALOG OUTPUT**|**ANALOG OUTPUT**|**ANALOG OUTPUT**|
||Nominal gain||2|V/V|
|VCMout|Common-mode output voltage||1.39<br>1.44<br>1.49|V|
|VCLIPout|Clipping differential output voltage|VOUT = (VOUTP– VOUTN);<br>|VIN| = |VINP– VINN| > VClipping|±2.49|V|
|VFailsafe|Failsafe differential output voltage|V+ = (VOUTP– VOUTN); VDCDCout ≤<br>VDCDCUV or VHLDOout ≤ VHLDOUV|–2.57<br>–2.5|V|
|BWOUT|Output bandwidth||300<br>375|kHz|
|ROUT|Output resistance|On OUTP or OUTN|0.2|Ω|
||Output short-circuit current|On OUTP or OUTN, sourcing or<br>sinking, INP = INN = HGND, outputs<br>shorted to either GND or VDD|14|mA|
|CMTI|Common-mode transient immunity||HGND – GND| = 2 kV|85<br>135|kV/µs|
|**ACCURACY**|**ACCURACY**|**ACCURACY**|**ACCURACY**|**ACCURACY**|
|VOS|Input offset voltage(1) (2)|TA = 25°C, INP = INN = HGND|–0.3<br>±0.05<br>0.3|mV|
|TCVOS|Input offset drift(1) (2) (4)||–4<br>±1<br>4|µV/°C|
|EG|Gain error|TA = 25°C|–0.2%<br>–0.08%<br>0.2%||
|TCEG|Gain error drift(1) (5)||–45<br>±7<br>45|ppm/°C|
||Nonlinearity||–0.02%<br>0.01%<br>0.02%||
||Nonlinearity drift||0.4|ppm/°C|
|SNR|Signal-to-noise ratio|VIN = 2 VPP, fIN = 1 kHz,<br>BW = 10 kHz, 10 kHz filter|81<br>85|dB|
|SNR|Signal-to-noise ratio|VIN = 2 VPP, fIN = 10 kHz,<br>BW = 100 kHz, 1 MHz filter|72|72|
|THD|Total harmonic distortion(3)|VIN = 2 Vpp, fIN = 10 kHz,<br>BW = 100 kHz|–84|dB|
||Output noise|INP = INN = HGND, fIN = 0 Hz,<br>BW = 100 kHz|250|µVRMS|
|CMRR|Common-mode rejection ratio|fIN = 0 Hz, VCM min ≤ VCM ≤ VCM max|–100|dB|
|CMRR|Common-mode rejection ratio|fIN = 10 kHz, VCM min ≤ VCM ≤ VCM<br>max|–86|–86|
|PSRR|Power-supply rejection ratio|VDD from 3.0 V to 5.5 V, at dc, input<br>referred|–98|dB|
|PSRR|Power-supply rejection ratio|INP = INN = HGND, VDD from 3.0<br>V to 5.5 V, 10 kHz / 100 mV ripple,<br>input referred|–86|–86|
|**DIGITAL OUTPUT ( DIAG)**|**DIGITAL OUTPUT ( DIAG)**|**DIGITAL OUTPUT ( DIAG)**|**DIGITAL OUTPUT ( DIAG)**|**DIGITAL OUTPUT ( DIAG)**|
|VOL|Low-level output voltage|ISINK= 4 mA|80<br>250|mV|


8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**5.9 Electrical Characteristics (continued)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



minimum and maximum specifications apply from TA = –40°C to +125°C, VDD = 3.0 V to 5.5 V, INP = –1 V to +1 V, and INN



















|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|ILKG|Open-drain output leakage current|VDD = 5V|5<br>100|nA|
|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|
|IDD|Low-side supply current|No external load on HLDO|28.5<br>41|mA|
|IDD|Low-side supply current|1 mA external load on HLDO|30.5<br>43|mA|
|VDDUV|VDD analog undervoltage detection<br>threshold|VDD rising|2.9|V|
|VDDUV|VDD analog undervoltage detection<br>threshold|VDD falling|2.8|2.8|
|VDDPOR|VDD digital reset threshold|VDD rising|2.5|V|
|VDDPOR|VDD digital reset threshold|VDD falling|2.4|2.4|
|VDCDC_OUT|DC/DC output voltage|DCDC_OUT to HGND|3.1<br>3.5<br>4.65|V|
|VDCDCUV|DC/DC output undervoltage<br>detection threshold voltage|DCDC output falling|2.1<br>2.25|V|
|VHLDO_OUT|High-side LDO output voltage|HLDO to HGND, up to 1 mA external<br>load|3<br>3.2<br>3.4|V|
|VHLDOUV|High-side LDO output undervoltage<br>detection threshold voltage|HLDO output falling|2.4<br>2.6|V|
|IH|High-side supply current for auxiliary<br>circuitry|3 V ≤ VDD < 4.5 V, load connected<br>from HLDO_OUT to HGND, non-<br>switching|1|mA|
|IH|High-side supply current for auxiliary<br>circuitry|4.5 V ≤ VDD ≤ 5.5 V, load connected<br>from HLDO_OUT to HGND, non-<br>switching|4.3|4.3|
|tAS|Analog settling time|VDD step to 3.0 V, to OUTP and<br>OUTN valid, 0.1% settling|0.6<br>1.1|ms|


(1) The typical value includes one standard deviation ("sigma") at nominal operating conditons.
(2) This parameter is input referred.
(3) THD is the ratio of the rms sum of the amplitues of first five higher harmonics to the amplitude of the fundamental.
(4) Offset error temperature drift is calculated using the box method, as described by the following equation:
_TCVOS = (VOS,MAX - VOS,MIN) / TempRange_ where VOS,MAX and VOS,MIN refer to the maximum and minimum VOS values measured
within the temperature range (–40 to 125℃).
(5) Gain error temperature drift is calculated using the box method, as described by the following equation:
_TCEG (ppm) = ((EG,MAX - EG,MIN) / TempRange) x 10_ _[4]_ where EG,MAX and EG,MIN refer to the maximum and minimum EG values (in %)
measured within the temperature range (–40 to 125℃).


**5.10 Switching Characteristics**
over operating ambient temperature range (unless otherwise noted)

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|tr|Output signal rise time||1.3|µs|
|tf|Output signal fall time||1.3|µs|
||VINx to VOUTx signal delay (50% – 10%)|Unfiltered output|1.2<br>1.3|µs|
||VINx to VOUTx signal delay (50% – 50%)|Unfiltered output|1.6<br>2.1|µs|
||VINx to VOUTx signal delay (50% – 90%)|Unfiltered output|2.2<br>2.6|µs|



Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 9


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


1 V



INP - INN


OUTN


OUTP







0


± 1 V


VCMout


|am|Col2|
|---|---|
|||
|tf<br>tr|tf<br>tr|
|||
|||
|||



**Figure 5-1. Rise, Fall, and Delay Time Waveforms**


10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)


|Col1|Col2|Col3|Col4|VDD<br>VDD|= 3.6 V<br>= 5.5 V|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||

























|5.12 Insulation Characteristics Curves|Col2|
|---|---|
|TA (°C)<br>IS (mA)<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>0<br>100<br>200<br>300<br>400<br>500<br>D001<br>VDD = 3.6 V<br>VDD = 5.5 V<br> <br>**Figure 5-2. Thermal Derating Curve for Safety-**<br>**Limiting Current per VDE**|TA (°C)<br>PS (mW)<br>0<br>25<br>50<br>75<br>100<br>125<br>150<br>0<br>200<br>400<br>600<br>800<br>1000<br>1200<br>1400<br>1600<br>1800<br>D002<br> <br>**Figure 5-3. Thermal Derating Curve for Safety-**<br>**Limiting Power per VDE**|
|1.E+01<br>1.E+02<br>1.E+03<br>1.E+04<br>1.E+05<br>1.E+06<br>1.E+07<br>1.E+08<br>1.E+09<br>1.E+10<br>1.E+11<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>3500<br>4000<br>4500<br>5000<br>5500<br>6000<br>6500<br>Time to Fail (sec)<br>Applied Voltage (VRMS)<br>**Working Isolation Voltage = 1200 VRMS**<br>**Projected Insulation Lifetime = 76 Yrs**<br>**TA upto 150oC**<br>**Applied Voltage Frequency = 60 Hz**<br>**TDDB Line (< 1 ppm Fail Rate)**<br>20 %<br>87.5%<br>76 Yrs<br>143 Yrs<br>**VDE Safety Margin Zone**<br>**Operating Zone**<br>**Figure 5-4. Reinforced Isolation Capacitor Lifetime Projection**|1.E+01<br>1.E+02<br>1.E+03<br>1.E+04<br>1.E+05<br>1.E+06<br>1.E+07<br>1.E+08<br>1.E+09<br>1.E+10<br>1.E+11<br>500<br>1000<br>1500<br>2000<br>2500<br>3000<br>3500<br>4000<br>4500<br>5000<br>5500<br>6000<br>6500<br>Time to Fail (sec)<br>Applied Voltage (VRMS)<br>**Working Isolation Voltage = 1200 VRMS**<br>**Projected Insulation Lifetime = 76 Yrs**<br>**TA upto 150oC**<br>**Applied Voltage Frequency = 60 Hz**<br>**TDDB Line (< 1 ppm Fail Rate)**<br>20 %<br>87.5%<br>76 Yrs<br>143 Yrs<br>**VDE Safety Margin Zone**<br>**Operating Zone**<br>**Figure 5-4. Reinforced Isolation Capacitor Lifetime Projection**|


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 11


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**5.13 Typical Characteristics**


at VDD = 3.3 V, INP = –1 V to 1 V, INN = HGND = 0V, and fIN = 10 kHz (unless otherwise noted)




















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|VO|UTN|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||~~V~~O|UTP|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||






















|10<br>8<br>6<br>4<br>2<br>(nA)<br>0<br>IIB<br>-2<br>-4<br>-6<br>-8<br>-10<br>-1.4 -1 -0.6 -0.2 0.2 0.6 1 1.4<br>VCM (V)<br>D003<br>Figure 5-5. Input Bias Current vs Common-Mode Input Voltage|10<br>8<br>6<br>4<br>2<br>(nA)<br>0<br>IIB<br>-2<br>-4<br>-6<br>-8<br>-10<br>3 3.5 4 4.5 5 5.5<br>VDD (V)<br>D004<br>Figure 5-6. Input Bias Current vs Supply Voltage|
|---|---|
|Temperature (°C)<br>IIB (nA)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110 125<br>-10<br>-8<br>-6<br>-4<br>-2<br>0<br>2<br>4<br>6<br>8<br>10<br>D005<br> <br>**Figure 5-7. Input Bias Current vs Temperature**|Differential Input Voltage (V)<br>VOUT(V)<br>-1.5<br>-1<br>-0.5<br>0<br>0.5<br>1<br>1.5<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>D006<br>VOUTN<br>~~V~~OUTP<br> <br>**Figure 5-8. Output vs Differential Input Voltage**|
|fIN (kHz)<br>Normalized Gain (dB)<br>1<br>10<br>100<br>1000<br>-40<br>-35<br>-30<br>-25<br>-20<br>-15<br>-10<br>-5<br>0<br>5<br>D007<br> <br>**Figure 5-9. Normalized Gain vs Input Frequency**|fIN (kHz)<br>Output Phase<br>1<br>10<br>100<br>1000<br>-360°<br>-315°<br>-270°<br>-225°<br>-180°<br>-135°<br>-90°<br>-45°<br>0°<br>D008<br> <br>**Figure 5-10. Output Phase vs Input Frequency**|



12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**5.13 Typical Characteristics (continued)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



at VDD = 3.3 V, INP = –1 V to 1 V, INN = HGND = 0V, and fIN = 10 kHz (unless otherwise noted)




















|Col1|Col2|Col3|Col4|Col5|Device 1<br>Device 2<br>Device 3|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Dev<br>Dev|ice 1<br>ice 2|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||~~Dev~~|~~ce 3~~|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||






|390<br>380<br>370 (kHz)<br>BW<br>360<br>350<br>340<br>3 3.5 4 4.5 5 5.5<br>VDD (V)<br>D011<br>Figure 5-11. Output Bandwidth vs Supply Voltage|390<br>380<br>370 (kHz)<br>BW<br>360<br>350<br>340<br>-40 -25 -10 5 20 35 50 65 80 95 110 125<br>Temperature (°C)<br>D012<br>Figure 5-12. Output Bandwidth vs Temperature|
|---|---|
|EG (%)<br>Devices (%)<br>0<br>10<br>20<br>30<br>40<br>50<br>-0.2<br>-0.15<br>-0.1<br>-0.05<br>0<br>0.05<br>0.1<br>0.15<br>0.2<br>D018<br> <br>**Figure 5-13. Gain Error Histogram**|VDD (V)<br>EG (%)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>-0.3<br>-0.2<br>-0.1<br>0<br>0.1<br>0.2<br>0.3<br>D020<br>Device 1<br>Device 2<br>~~Device 3~~<br> <br>**Figure 5-14. Gain Error vs Supply Voltage**|
|Temperature (°C)<br>EG (%)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110<br>125<br>-0.3<br>-0.2<br>-0.1<br>0<br>0.1<br>0.2<br>0.3<br>D021<br>Device 1<br>Device 2<br>~~Device 3~~<br> <br>**Figure 5-15. Gain Error vs Temperature**|TCEG (ppm/qC)<br>Devices (%)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>-45<br>-40<br>-35<br>-30<br>-25<br>-20<br>-15<br>-10<br>-5<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>D019<br> <br>**Figure 5-16. Gain Error Drift Histogram**|



Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 13


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**5.13 Typical Characteristics (continued)**


at VDD = 3.3 V, INP = –1 V to 1 V, INN = HGND = 0V, and fIN = 10 kHz (unless otherwise noted)










|Col1|Col2|Col3|Col4|Col5|Device 1|
|---|---|---|---|---|---|
|||||||
||||||~~Device 2~~<br>Device 3|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Dev|ice 1|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||~~Dev~~<br>Dev|~~ce 2~~<br>ice 3|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|D|evice 1|
|---|---|---|---|---|---|---|---|---|
||||||||~~D~~<br>D|~~vice 2~~<br>evice 3|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|Col2|Col3|Col4|Col5|Device 1|
|---|---|---|---|---|---|
||||||~~Device 2~~<br>Device 3|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||










|50<br>40<br>30 (%)<br>Devices<br>20<br>10<br>0<br>-0.3 -0.2 -0.1 0 0.1 0.2 0.3<br>VOS (mV) D023<br>Figure 5-17. Offset Error Histogram|100<br>Device 1<br>75 Device 2<br>Device 3<br>50<br>25<br>(PV)<br>0<br>VOS<br>-25<br>-50<br>-75<br>-100<br>3 3.5 4 4.5 5 5.5<br>VDD (V)<br>D027<br>Figure 5-18. Offset Error vs Supply Voltage|
|---|---|
|Temperature (°C)<br>VOS (PV)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110<br>125<br>-100<br>-75<br>-50<br>-25<br>0<br>25<br>50<br>75<br>100<br>D026<br>Device 1<br>~~Device 2~~<br>Device 3<br> <br>**Figure 5-19. Offset Error vs Temperature**|TCVOS (PV/qC)<br>Devices (%)<br>0<br>10<br>20<br>30<br>40<br>50<br>-4<br>-3<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>D024<br> <br>**Figure 5-20. Offset Error Drift Histogram**|
|Differential Input Volatge (V)<br>Nonlinearity (%)<br>-1<br>-0.75<br>-0.5<br>-0.25<br>0<br>0.25<br>0.5<br>0.75<br>1<br>-0.02<br>-0.015<br>-0.01<br>-0.005<br>0<br>0.005<br>0.01<br>0.015<br>0.02<br>D028<br>Device 1<br>~~Device 2~~<br>Device 3<br> <br>**Figure 5-21. Nonlinearity vs Differential Input Voltage**|VDD (V)<br>Nonlinearity (%)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>-0.02<br>-0.015<br>-0.01<br>-0.005<br>0<br>0.005<br>0.01<br>0.015<br>0.02<br>**D02**4019<br>Device 1<br>~~Device 2~~<br>Device 3<br> <br>**Figure 5-22. Nonlinearity vs Supply Voltage**|



14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**5.13 Typical Characteristics (continued)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



at VDD = 3.3 V, INP = –1 V to 1 V, INN = HGND = 0V, and fIN = 10 kHz (unless otherwise noted)












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||Devi<br>|ce 1<br>|||||||||
||~~Dev~~<br>Devi|~~ce 2~~<br>ce 3|||||||||




|evice 1|Col2|Col3|Col4|
|---|---|---|---|
|~~vice 2~~<br>evice 3||||
|||||
|||||
|||||
|||||
|||||
|||||






















|Col1|Col2|Col3|Col4|Col5|Device 1|
|---|---|---|---|---|---|
|||||||
||||||~~Device 2~~<br>Device 3|
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


|Col1|Col2|Col3|Col4|Col5|Col6|Devic|
|---|---|---|---|---|---|---|
||||||||
|||||||~~Devic~~<br>Devic|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||






















|Col1|Col2|Col3|Col4|Col5|Device 1<br>Device 2|
|---|---|---|---|---|---|
||||||~~Device 3~~|
|||||||
|||||||
|||||||
|||||||
|||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
|||||||~~Devi~~|
|||||||<br>Devic<br>Devic|














|0.02<br>0.015<br>0.01<br>(%)<br>0.005<br>Nonlinearity<br>0<br>-0.005<br>-0.01<br>Device 1<br>-0.015 Device 2<br>Device 3<br>-0.02<br>-40 -25 -10 5 20 35 50 65 80 95 110 125<br>Temperature (°C)<br>D0203410<br>Figure 5-23. Nonlinearity vs Temperature|80<br>Device 1<br>75 Device 2<br>Device 3<br>70<br>65<br>(dB)<br>60<br>SNR<br>55<br>50<br>45<br>40<br>0 0.25 0.5 0.75 1 1.25<br>|VINP - VINN| (V)<br>D032<br>Figure 5-24. Signal to Noise Ratio vs Differential Input Voltage|
|---|---|
|VDD (V)<br>SNR (dB)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>D034<br>Device 1<br>~~Device 2~~<br>Device 3<br> <br>**Figure 5-25. Signal to Noise Ratio vs Supply Voltage**|Temperature (°C)<br>SNR (dB)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110 125<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>D035<br>Device 1<br>~~Device 2~~<br>Device 3<br> <br>**Figure 5-26. Signal to Noise Ratio vs Temperature**|
|VDD (V)<br>THD (dB)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>-100<br>-95<br>-90<br>-85<br>-80<br>-75<br>-70<br>D056<br>Device 1<br>Device 2<br>~~Device 3~~<br> <br>**Figure 5-27. Total Harmonic Distortion vs Supply Voltage**|Temperature (°C)<br>THD (dB)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110<br>125<br>-100<br>-95<br>-90<br>-85<br>-80<br>-75<br>-70<br>D059<br>~~Device 1~~<br>Device 2<br>Device 3<br> <br>**Figure 5-28. Total Harmonic Distortion vs Temperature**|



Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 15


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**5.13 Typical Characteristics (continued)**


at VDD = 3.3 V, INP = –1 V to 1 V, INN = HGND = 0V, and fIN = 10 kHz (unless otherwise noted)
















|Col1|Col2|Col3|fIN = 10 kHz|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||


























|10000<br>(nV/—Hz)<br>Density<br>1000<br>Noise<br>100<br>0.01 0.1 1 10 100 1000<br>Frequency (kHz)<br>D017<br>Figure 5-29. Input-Referred Noise Density vs Frequency|0<br>-20<br>-40<br>(dB)<br>-60 CMRR<br>-80<br>-100<br>-120<br>0.01 0.1 1 10 100 1000<br>fIN (kHz)<br>D038<br>Figure 5-30. Common-Mode Rejection Ratio vs Input Frequency|
|---|---|
|Temperature (°C)<br>CMRR (dB)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110 125<br>-90<br>-88<br>-86<br>-84<br>-82<br>-80<br>D039<br>fIN = 10 kHz<br> <br>**Figure 5-31. Common-Mode Rejection Ratio vs Temperature**|Ripple Frequency (kHz)<br>PSRR (dB)<br>0.01<br>0.1<br>1<br>10<br>100<br>1000<br>-120<br>-100<br>-80<br>-60<br>-40<br>-20<br>0<br>D041<br> <br>**Figure 5-32. Power-Supply Rejection Ratio vs Ripple Frequency**|
|Temperature (°C)<br>PSRR (dB)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110<br>125<br>-120<br>-100<br>-80<br>-60<br>-40<br>-20<br>0<br>D042<br> <br>**Figure 5-33. Power-Supply Rejection Ratio vs Temperature**|VDD (V)<br>IDD (mA)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>22.5<br>25<br>27.5<br>30<br>32.5<br>D043<br> <br>**Figure 5-34. Input-Supply Current vs Supply Voltage**|



16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**5.13 Typical Characteristics (continued)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



at VDD = 3.3 V, INP = –1 V to 1 V, INN = HGND = 0V, and fIN = 10 kHz (unless otherwise noted)










































|Col1|Col2|Col3|Col4|Col5|50% - 90%|
|---|---|---|---|---|---|
||||||~~50% - 50%~~<br>50% - 10%|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|50% -|90%|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||<br>|~~0% -~~<br>50% -|~~  50%~~<br>  10%|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||














|32.5<br>30<br>(mA)<br>27.5<br>IDD<br>25<br>22.5<br>-40 -25 -10 5 20 35 50 65 80 95 110 125<br>Temperature (°C)<br>D044<br>Figure 5-35. Input-Supply Current vs Temperature|3.4<br>3.35<br>3.3<br>3.25 (V)<br>VHLDO_OUT<br>3.2<br>3.15<br>3.1<br>3.05<br>3<br>3 3.5 4 4.5 5 5.5<br>VDD (V)<br>D046<br>Figure 5-36. High-Side LDO Line Regulation|
|---|---|
|VDD (V)<br>tr / tf (Ps)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>D065<br> <br>**Figure 5-37. Output Rise And Fall Time vs Supply Voltage**|Temperature (°C)<br>tr/tf (Ps)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110<br>125<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>D066<br> <br>**Figure 5-38. Output Rise And Fall Time vs Temperature**|
|VDD (V)<br>Signal Delay (Ps)<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0.2<br>0.6<br>1<br>1.4<br>1.8<br>2.2<br>2.6<br>3<br>3.4<br>3.8<br>D67_<br>50% - 90%<br>~~50% - 50%~~<br>50% - 10%<br> <br>**Figure 5-39. VIN to VOUT Signal Delay Time vs Supply Voltage**|Temperature (°C)<br>Signal Delay (Ps)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>95<br>110<br>125<br>0.2<br>0.6<br>1<br>1.4<br>1.8<br>2.2<br>2.6<br>3<br>3.4<br>3.8<br>D68_<br>50% - 90%<br>~~50% - 50%~~<br>50% - 10%<br> <br>**Figure 5-40. VIN to VOUT Signal Delay Time vs Temperature**|



Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 17


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**6 Detailed Description**

**6.1 Overview**


The AMC3330 is a fully-differential, precision, isolated amplifier with high input impedance, and an integrated
DC/DC converter that allows the device to be supplied from a single 3.3-V or 5-V voltage supply source on
the low side. The input stage of the device drives a second-order, delta-sigma (ΔΣ) modulator. The modulator
uses an internal voltage reference and clock generator to convert the analog input signal to a digital bitstream.
The drivers (termed TX in the _Functional Block Diagram_ ) transfer the output of the modulator across the
isolation barrier that separates the high-side and low-side voltage domains. The received bitstream and clock are
synchronized and processed by a fourth-order analog filter on the low-side and presented as a differential analog
output.


The _Functional Block Diagram_ shows a block diagram of the AMC3330. The 1.2-GΩ differential input
impedance of the analog input stage supports low gain-error signal-sensing in high-voltage applications using
high-impedance resistor dividers.
The signal path is isolated by a double capacitive silicon-dioxide (SiO2) insulation barrier, whereas power
isolation uses an on-chip transformer separated by a thin-film polymer as the insulating material.


**6.2 Functional Block Diagram**



DCDC_OUT


DCDC_HGND


HLDO_IN



DCDC_IN


DCDC_GND







HLDO_OUT


INP


INN

|Col1|Rectifier|
|---|---|
||**AMC3330**<br> ûModulator<br>TX<br>RX<br>Bandgap<br>Reference<br>LDO|
|||
|||
|||



HGND

**6.3 Feature Description**

_**6.3.1 Analog Input**_



LDO_OUT











VDD


OUTP


OUTN







GND



The input stage of the AMC3330 feeds a second-order, switched-capacitor, feed-forward ΔΣ modulator. The
modulator converts the analog signal into a bitstream that is transferred over the isolation barrier, as described
in the _Isolation Channel Signal Transmission_ section. The high-impedance, and low bias-current input of the
AMC3330 makes the device suitable for isolated, high-voltage-sensing applications that typically employ highimpedance resistor dividers.


There are two restrictions on the analog input signals (INP and INN). First, if the input voltage exceeds the input
range specified in the _Absolute Maximum Ratings_ table, the input current must be limited to 10 mA because the
device input electrostatic discharge (ESD) diodes turn on. Second, the linearity and noise performance of the
device are ensured only when the differential analog input voltage remains within the specified linear full-scale
range VFSR and within the specified input common-mode voltage range VCM as specified in the _Recommended_
_Operating Conditions_ table.


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


_**6.3.2 Isolation Channel Signal Transmission**_



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



The AMC3330 uses an on-off keying (OOK) modulation scheme to transmit the modulator output-bitstream
across the capacitive SiO2-based isolation barrier. Figure 6-1 shows the block diagram of an isolation channel.
The transmitter modulates the bitstream at TX IN with an internally generated, 480-MHz carrier and sends
a burst across the isolation barrier to represent a digital _one_ and sends a _no signal_ to represent the digital
_zero_ . The receiver demodulates the signal after advanced signal conditioning and produces the output.
The symmetrical design of each isolation channel improves the common-mode transient immunity (CMTI)
performance and reduces the radiated emissions caused by the high-frequency carrier.





TX IN











RX OUT


|Col1|Transmitter<br>OOK<br>Modulation<br>TX Signal<br>Conditioning<br>Oscillator|SiO2-Based<br>Capacitive<br>Reinforced<br>Isolation<br>Barrier|Receiver<br>RX Signal Envelope<br>Conditioning Detection|Col5|
|---|---|---|---|---|
||||||
||||||



**Figure 6-1. Block Diagram of an Isolation Channel**


Figure 6-2 shows the concept of the on-off keying scheme.


TX IN


Carrier Signal Across
the Isolation Barrier


RX OUT


**Figure 6-2. OOK-Based Modulation Scheme**


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 19


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


_**6.3.3 Analog Output**_


The AMC3330 offers a differential analog output comprised of the OUTP and OUTN pins. For differential input
voltages (VINP – VINN) in the range from –1 V to 1 V, the device provides a linear response with a nominal
gain of 2. For example, for a differential input voltage of 1 V, the differential output voltage (VOUTP – VOUTN)
is 2 V. At zero input (INP shorted to INN), both pins output the same voltage, VCMout, as specified in the
_Electrical Characteristics_ table. For absolute differential input voltages greater than 1.0 V but less than 1.25 V,
the differential output voltage continues to increase in magnitude but with reduced linearity performance. The
outputs saturate as shown in Figure 6-3 if the differential input voltage exceeds the VClipping value.


Maximum input range before clipping (VClipping)


Linear input range (VFSR)


Common mode output voltage

.

|VOUTN|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|VOUTP||||||
|VOUTP||||||
|VOUTP||||||



±1.25 V 1.25 V
±1.00 V 0 1.00 V


Differential Input Voltage (VINP ± VINN)


**Figure 6-3. AMC3330 Output Behavior**


The AMC3330 provides a fail-safe output that simplifies diagnostics on system level. The fail-safe output is
active when the integrated DC/DC converter or hgh-side LDO don't deliver the required supply voltage for the
high-side of the device. Figure 6-4 and Figure 6-5 illustrate the fail-safe output of the AMC3330 that is a negative
differential output voltage value that does not occur under normal operating conditions. Use the maximum
VFAILSAFE voltage specified in the _Electrical Characteristics_ table as a reference value for the fail-safe detection
on system level.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**





**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)


**Figure 6-4. Typical Negative Clipping Output of the AMC3330**


**Figure 6-5. Typical Fail-Safe Output of the AMC3330**



Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 21


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


_**6.3.4 Isolated DC/DC Converter**_


The AMC3330 offers a fully integrated isolated DC/DC converter that includes the following components
illustrated in the _Functional Block Diagram_ :

 - Low-dropout regulator (LDO) on the low-side to stabilize the supply voltage VDD that drives the low-side of
the DC/DC converter

 - Low-side full-bridge inverter and drivers

 - Laminate-based, air-core transformer for high immunity to magnetic fields

 - High-side full-bridge rectifier

 - High-side LDO to stabilize the output voltage of the DC/DC converter for high analog performance of the
signal path


The DC/DC converter uses a spread-spectrum clock generation technique to reduce the spectral density of
the electromagnetic radiation. The resonator frequency is synchronous to the operation of the ΔΣ modulator to
minimize interference with data transmission and support the high analog performance of the device.


The architecture of the DC/DC converter is optimized to drive the high-side circuitry of the AMC3330 and can
source up to 1 mA of additional current (IH) for an optional auxiliary circuit such as an active filter, pre-amplifier,
or comparator.


_**6.3.5 Diagnostic Output and Fail-Safe Behavior**_


The open-drain DIAG pin can be monitored to confirm the device is operational, and the output voltage is valid.
During power-up, the DIAG pin is actively held low until the high-side supply is in regulation and the device
operates properly. The DIAG pin is actively pulled low if:


 - The low-side does not receive data from the high-side (for example, because of a loss of power on the
high-side). The amplifier outputs are driven to negative full-scale.

 - The high-side DC/DC output voltage (DCDC_OUT) or the high-side LDO output voltage (HLDO_OUT) drop
below their respective undervoltage detection thresholds VDCDCUV and VHLDOUV as sepecified in the _Electrical_
_Characteristics_ table. In this case, the low-side may still receive data from the high-side but the data may not
be valid. The amplifier outputs are driven to negative full-scale.


During normal operation, the DIAG pin is in a high-impedance state. Connect the DIAG pin to a pull-up supply
through a resistor or leave open if not used.


**6.4 Device Functional Modes**


The AMC3330 is operational when the power supply VDD is applied, as specified in the _Recommended_
_Operating Conditions_ table.


22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**7 Application and Implementation**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**7.1 Application Information**


The low input bias current, AC and DC errors, and temperature drift make the AMC3330 a high-performance
solution for applications where voltage measurement with high common-mode levels is required.


**7.2 Typical Application**


Isolated amplifiers are widely used for voltage measurements in high-voltage applications that must be isolated
from a low-voltage domain. Typical applications are AC line voltage measurements at the input of a power
factor correction (PFC) stage or the output of a solar inverter. Other applications are DC measurements at the
output of a PFC stage or DC/DC converter, or phase voltage measurements in motor and servo drives. The
AMC3330 integrates an isolated power supply for the high-voltage side and therefore is particularly easy to use
in applications that do not have a high-side supply readily available or where a high-side supply is referenced to
a different ground potential than the signal to be measured.


Figure 7-1 depicts a simplified schematic of the AMC3330 in a solar inverter where the AC phase voltage on the
grid-side must be measured. At that location in the system, there is no supply readily available for powering the
isolated amplifier. The integrated isolated power supply, together with its bipolar input voltage range, makes the
[AMC3330 ideally suited for AC line-voltage sensing. In this example, phase current is sensed by the AMC3301](https://www.ti.com/product/AMC3301)
across a shunt resistor on the grid-side of an LCL filter where there is also no suitable supply available for
powering the isolated amplifier. The integrated power supply of the AMC3301 eliminates that problem and
enables current sensing at optimal locations for the system.


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 23


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**







to grid (L1)




















|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
||100 nF<br>1 nF<br>100 nF|100 nF<br>1 nF<br>100 nF|100 nF<br>1 nF<br>100 nF|
||100 nF<br>1 nF<br>100 nF|||
|||||
|||||

















to MCU


















|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||100 nF<br>1 nF<br>100 nF|100 nF<br>1 nF<br>100 nF|100 nF<br>1 nF<br>100 nF|100 nF<br>1 nF<br>100 nF|
||100 nF<br>1 nF<br>100 nF||||
||||||
||||||



**Figure 7-1. The AMC3330 in a Solar Inverter Application**


_**7.2.1 Design Requirements**_


Table 7-1 lists the parameters for this typical application.


**Table 7-1. Design Requirements**

|PARAMETER|VALUE|
|---|---|
|Low-side supply voltage|3.3 V or 5 V|
|Voltage drop across the sensing resistor for a linear response|1 V (maximum)|
|Current through the resistive divider, ICROSS|100 µA (maximum)|



_**7.2.2 Detailed Design Procedure**_


Use Ohm's Law to calculate the minimum total resistance of the resistive divider to limit the cross current to the
desired value ( RTOTAL = VLx / ICROSS ) and the required sense resistor value to be connected to the AMC3330
input: RSNS = VFSR / ICROSS.

Consider the following two restrictions to choose the proper value of the sense resistor RSNS:

 - The voltage drop on RSNS caused by the nominal voltage range of the system must not exceed the
recommended input voltage range: VSNS ≤ VFSR

 - The voltage drop on RSNS caused by the maximum allowed system overvoltage must not exceed the input
voltage that causes a clipping output: VSNS ≤ VClipping


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



Table 7-2 lists examples of nominal E96-series (1% accuracy) resistor values for systems using 120-V and
230-V AC line voltages.


**Table 7-2. Resistor Value Examples**

|PARAMETER|120-V LINE VOLTAGE<br>RMS|230-V LINE VOLTAGE<br>RMS|
|---|---|---|
|Peak voltage|170 V|325 V|
|Resistive divider resistors RL11, RL12|845 kΩ|1.62 MΩ|
|Sense resistor RSNS|10 kΩ|10 kΩ|
|Current through resistive divider ICROSS|100 µA|100 µA|
|Resulting voltage drop on sense resistor VSNS|1.00 V|1.00 V|



**7.2.2.1 Input Filter Design**


TI recommends placing an RC filter in front of the isolated amplifier to improve signal-to-noise performance of
the signal path. Design the input filter such that:


 - The cutoff frequency of the filter is at least one order of magnitude lower than the sampling frequency
(20 MHz) of the internal ΔΣ modulator

 - The input bias current does not generate significant voltage drop across the DC impedance of the input filter

 - The impedances measured from the analog inputs are equal


Most voltage sensing applications use high-impedance resistor dividers in front of the isolated amplifier to scale
down the input voltage. In this case, a single capacitor as given in Figure 7-2 is sufficient to filter the input signal.


**AMC3330**











**Figure 7-2. Differential Input Filter**


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 25


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**7.2.2.2 Differential to Single-Ended Output Conversion**


For systems using single-ended input ADCs to convert the analog output voltage into digital, Figure 7-3 shows
[an example of a TLV6001 -based signal conversion and filter circuit. With R1 = R2 = R3 = R4, the output voltage](http://www.ti.com/product/TLV6001)
equals (VOUTP – VOUTN) + VREF. Tailor the bandwidth of this filter stage to the bandwidth requirement of the
system and use NP0-type capacitors for best performance. For most applications, R1 = R2 = R3 = R4 = 10 kΩ
and C1 = C2 = 1000 pF yields good performance.


**AMC3330**















VREF





To MCU







GND


**Figure 7-3. Connecting the AMC3330 Output to a Single-Ended Input ADC**


For more information on the general procedure to design the filtering and driving stages of SAR ADCs, see
the _[18-Bit, 1MSPS Data Acquisition Block (DAQ) Optimized for Lowest Distortion and Noise](https://www.ti.com/lit/pdf/SLAU515)_ and _[18-Bit Data](https://www.ti.com/lit/pdf/SLAU513)_
_[Acquisition Block (DAQ) Optimized for Lowest Power](https://www.ti.com/lit/pdf/SLAU513)_ [reference guides, available for download at www.ti.com.](https://www.ti.com/)


_**7.2.3 Application Curve**_


Figure 7-4 shows the typical full-scale step response of the AMC3330.







**Figure 7-4. Step Respose of the AMC3330**


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**7.3 Best Design Practices**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



Do not leave the analog inputs INP and INN of the AMC3330 unconnected (floating) when the device is powered
up on the high-side. If the device input is left floating, the bias current may generate a negative input voltage that
exceeds the specified input voltage range and the output of the device is invalid.


Connect the high-side ground (HGND) to INN, either directly or through a resistive path. A DC current path
between INN and HGND is required to define the input common-mode voltage. Take care not to exceed the input
common-mode range as specified in the _Recommended Operating Conditions_ table.


The high-side LDO sources a limited amount of current (IH) to power external circuitry. Do not overload the
high-side LDO.


The low-side LDO does not output a constant voltage and is not intended for powering any external circuitry. Do
not connect any external load to the LDO_OUT pin.


**7.4 Power Supply Recommendations**


The AMC3330 is powered from the low-side power supply (VDD) with a nominal value of 3.3 V (or 5 V). TI
recommends a low-ESR decoupling capacitor of 1 nF (C8 in Figure 7-5) placed as close as possible to the VDD
pin, followed by a 1-µF capacitor (C9) to filter this power-supply path.


The low-side of the DC/DC converter is decoupled with a low-ESR 100-nF capacitor (C4) positioned close to
the device between the DCDC_IN and DCDC_GND pins. Use a 1-µF capacitor (C2) to decouple the high-side
in addition to a low-ESR, 1-nF capacitor (C3) placed as close as possible to the device and connected to the
DCDC_OUT and DCDC_HGND pins.


For the high-side LDO, use low-ESR capacitors of 1-nF (C6), placed as close as possible to the AMC3330,
followed by a 100-nF decoupling capacitor (C5).


The ground reference for the high-side (HGND) is derived from the terminal of the sense resistor which is
connected to the negative input (INN) of the device. For best DC accuracy, use a separate trace to make this
connection but shorting HGND to INN directly at the device input is also acceptable. The high-side DC/DC
ground terminal(DCDC_HGND) is shorted to HGND directly at the device pins.







to uC (optional)


3.3 V / 5 V supply


to RC filter / ADC


to RC filter / ADC






|Col1|Col2|
|---|---|
|||
|||







**Figure 7-5. Decoupling the AMC3330**


Capacitors must provide adequate _effective_ capacitance under the applicable DC bias conditions they
experience in the application. Multilayer ceramic capacitors (MLCC) capacitors typically exhibit only a fraction
of their nominal capacitance under real-world conditions and this factor must be taken into consideration when
selecting these capacitors. This problem is especially acute in low-profile capacitors, in which the dielectric field
strength is higher than in taller components. Reputable capacitor manufacturers provide capacitance versus DC
bias curves that greatly simplify component selection.


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 27


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


The _[Best Practices to Attenuate AMC3301 Family Radiated Emissions EMI](https://www.ti.com/lit/pdf/sbaa515)_ application note is available for
[download at www.ti.com.](https://www.ti.com/)


Table 7-3 lists components suitable for use with the AMC3330. This list is not exhaustive. Other components
may exist that are equally suitable (or better), however these listed components have been validated during the
development of the AMC3330.


**Table 7-3. Recommended External Components**






|DESCRIPTION|Col2|PART NUMBER|MANUFACTURER|SIZE (EIA, L x W)|
|---|---|---|---|---|
|**VDD**|**VDD**|**VDD**|**VDD**|**VDD**|
|C8|1 nF ± 10%, X7R, 50 V|12065C102KAT2A|AVX|1206, 3.2 mm x 1.6 mm|
|C9|1 µF ± 10%, X7R, 25 V|12063C105KAT2A|AVX|1206, 3.2 mm x 1.6 mm|
|**DC/DC CONVERTER**|**DC/DC CONVERTER**|**DC/DC CONVERTER**|**DC/DC CONVERTER**|**DC/DC CONVERTER**|
|C4|100 nF ± 10%, X7R, 50 V|C0603C104K5RACAUTO|Kemet|0603, 1.6 mm x 0.8 mm|
|C3|1 nF ± 10%, X7R, 50 V|C0603C102K5RACTU|Kemet|0603, 1.6 mm x 0.8 mm|
|C2|1 µF ± 10%, X7R, 25 V|CGA3E1X7R1E105K080AC|TDK|0603, 1.6 mm x 0.8 mm|
|**HLDO**|**HLDO**|**HLDO**|**HLDO**|**HLDO**|
|C1|100 nF ± 10%, X7R, 50 V|C0603C104K5RACAUTO|Kemet|0603, 1.6 mm x 0.8 mm|
|C5|100 nF ± 5%, NP0, 50 V|C3216NP01H104J160AA|TDK|1206, 3.2 mm x 1.6 mm|
|C6|1 nF ± 10%, X7R, 50 V|12065C102KAT2A|AVX|1206, 3.2 mm x 1.6 mm|
|FERRITE BEADS|FERRITE BEADS|FERRITE BEADS|FERRITE BEADS|FERRITE BEADS|
|FB1,<br>FB2,<br>FB3|Ferrite bead(1)|74269244182|Wurth Elektronik|0402, 1.0mm × 0.5mm|
|FB1,<br>FB2,<br>FB3|Ferrite bead(1)|BLM15HD182SH1|Murata|0402, 1.0mm × 0.5mm|
|FB1,<br>FB2,<br>FB3|Ferrite bead(1)|BKH1005LM182-T|Taiyo Yuden|0402, 1.0mm × 0.5mm|



(1) No ferrite beads are used for parametric validation.


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**


**7.5 Layout**

_**7.5.1 Layout Guidelines**_



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



Figure 7-6 shows a layout recommendation with the critical placement of the decoupling capacitors. The same
component reference designators are used as in the _Power Supply Recommendations_ section. Decoupling
capacitors are placed as close as possible to the AMC3330 supply pins. For best performance, place the sense
resistor close to the INP and INN inputs of the AMC3330 and keep the layout of both connections symmetrical.


This layout is used on the AMC3330 EVM and supports CISPR-11 compliant electromagnetic radiation levels.


_**7.5.2 Layout Example**_


Clearance area, to be
kept free of any
conductive materials.















To MCU I/O (optional)


3.3-V or 5-V supply


To analog filter / ADC / MCU

To analog filter / ADC / MCU



|C2<br>C3<br>R1<br>C1<br>C5<br>INP FB1 C6 RSNS<br>C10<br>FB2<br>INN|Col2|Col3|Col4|Col5|Col6|Col7|Col8|AMC3330|Col10|Col11|C4|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C10<br>INP<br>INN<br>C3<br>C2<br>C1<br>C5<br>C6<br>FB2<br>FB1<br>RSNS<br>R1|C10<br>INP<br>INN<br>C3<br>C2<br>C1<br>C5<br>C6<br>FB2<br>FB1<br>RSNS<br>R1|||C2|||||||||||
|C10<br>INP<br>INN<br>C3<br>C2<br>C1<br>C5<br>C6<br>FB2<br>FB1<br>RSNS<br>R1|||||||||||||||
||||||||||**AMC3330**|**AMC3330**|**AMC3330**|**AMC3330**|**AMC3330**|**AMC3330**|
|||||C3|||||||||||
|R1|R1|R1|R1||||||||||C4|C4|
|R1|R1|R1|R1|C1<br>C5|C1<br>C5|||||||||VDD<br>DIAG|
||||||||||||||||
|||||C5|||||||||||
|RSNS||||C6|C6|C6|C6||||||||
||||||||||||||||
|R2|R2|R2|R2|R2|R2|R2|R2|R2|R2|R2|R2|R2|R2|R2|
||||||||||||||||
||||||||||||||||


**Figure 7-6. Recommended Layout of the AMC3330**


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 29


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34) **[www.ti.com](https://www.ti.com)**


**8 Device and Documentation Support**

**8.1 Device Support**

_**8.1.1 Device Nomenclature**_


Texas Instruments, _[Isolation Glossary](https://www.ti.com/lit/pdf/SLLA353)_


**8.2 Documentation Support**

_**8.2.1 Related Documentation**_


For related documentation see the following:

 - Texas Instruments, _[ISO72x Digital Isolator Magnetic-Field Immunity](https://www.ti.com/lit/pdf/SLLA181A)_ application note

 - Texas Instruments, _[AMC3301 Precision, ±250-mV Input, Reinforced Isolated Amplifier With Integrated DC/DC](https://www.ti.com/product/AMC3301)_
_Converter_ [data sheet](https://www.ti.com/product/AMC3301)

 - Texas Instruments, _[TLV600x Low-Power, Rail-to-Rail In/Out, 1-MHz Operational Amplifier for Cost-Sensitive](http://www.ti.com/product/TLV6001)_
_Systems_ [data sheet](http://www.ti.com/product/TLV6001)

 - Texas Instruments, _[18-Bit, 1MSPS Data Acquisition Block (DAQ) Optimized for Lowest Distortion and Noise](https://www.ti.com/lit/pdf/SLAU515)_
[reference guide](https://www.ti.com/lit/pdf/SLAU515)

 - Texas Instruments, _[18-Bit Data Acquisition Block (DAQ) Optimized for Lowest Power](https://www.ti.com/lit/pdf/SLAU513)_ reference guide


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


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ Copyright © 2024 Texas Instruments Incorporated


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


**[www.ti.com](https://www.ti.com)**



**[AMC3330](https://www.ti.com/product/AMC3330)**
[SBASA34B – JUNE 2020 – REVISED AUGUST 2024](https://www.ti.com/lit/pdf/SBASA34)



**9 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision A (October 2020) to Revision B (August 2024)** **Page**

 - Changed reinforced isolation safety-related certification from _VDE V 0884-11_ to _DIN EN IEC 60747-17 (VDE_
_0884-17)_ throughout document.......................................................................................................................... 1

 - Changed _Electricity meters_ to _EV charging infrastructure_ and _Protection relays_ to _Battery energy storage_
_systems_ in last two _Applications_ bullets..............................................................................................................1

 - Changed _Application Example_ figure................................................................................................................. 1

 - Changed Absolute Maximum Ratings: changed max for DIAG pin from 5.5 V to 6.5 V.....................................4

 - Added analog output capacitive and resistive drive capability specification.......................................................4

 - Updated Barrier capacitance specification from 3.5 pF to 4.5 pF.......................................................................6

 - Changed isolation standard from DIN VDE V 0884-11 (VDE V 0884-11) to DIN EN IEC 60747-17 (VDE
0884-17) and updated the Insulation Specifications and Safety-Related Certifications tables accordingly....... 7

 - THD footnote added........................................................................................................................................... 8

 - Added DIGITAL OUTPUT (DIAG) electrical specifications.................................................................................8

 - Added VDDUV and VDDPOR specifications.........................................................................................................8

 - Added IH specification for 4.5 V ≤ VDD ≤ 5.5 V..................................................................................................8

 - Deleted duplicate column in _Resistor Value Examples_ table............................................................................24

 - Changed _Differential Input Filter_ figure.............................................................................................................25

 - Added high-side and low-side LDO external load discussion to _Best Design Practices_ section...................... 27

 - Changed _Power Supply Recommendations_ section: Changed _Decoupling the AMC3330_ figure, added _Best_
_Practices to Attenuate AMC3301 Family Radiated Emissions EMI_ reference and added ferrite bead section to
_Recommended External Components_ table.....................................................................................................27

 - Changed OUTP, OUTN, and VDD routing in _Recommended Layout of the AMC3330_ figure..........................29


**Changes from Revision * (June 2020) to Revision A (October 2020)** **Page**

 - Changed document status from advance information to production data.......................................................... 1


**10 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


Copyright © 2024 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBASA34B&partnum=AMC3330)_ 31


Product Folder Links: _[AMC3330](https://www.ti.com/product/amc3330?qgpn=amc3330)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 6-Feb-2026


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
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 6-Feb-2026


**[OTHER QUALIFIED VERSIONS OF AMC3330 :]**

- [[Automotive : ][AMC3330-Q1]](http://focus.ti.com/docs/prod/folders/print/amc3330-q1.html)


[NOTE: Qualified Version Definitions:]

    - [Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects]


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 12-Jan-2026


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
|AMC3330DWER|SOIC|DWE|16|2000|330.0|16.4|10.75|10.7|2.7|12.0|16.0|Q1|
|AMC3330DWERG4|SOIC|DWE|16|2000|330.0|16.4|10.75|10.7|2.7|12.0|16.0|Q1|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 12-Jan-2026





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|AMC3330DWER|SOIC|DWE|16|2000|350.0|350.0|43.0|
|AMC3330DWERG4|SOIC|DWE|16|2000|350.0|350.0|43.0|



Pack Materials-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 12-Jan-2026


**TUBE**


**T - Tube**


*All dimensions are nominal

|Device|Package Name|Package Type|Pins|SPQ|L (mm)|W (mm)|T (µm)|B (mm)|
|---|---|---|---|---|---|---|---|---|
|AMC3330DWE|DWE|SO-MOD|16|40|506.98|12.7|4826|6.6|
|AMC3330DWE.A|DWE|SO-MOD|16|40|506.98|12.7|4826|6.6|
|AMC3330DWER|DWE|SO-MOD|16|2000|506.98|12.7|4826|6.6|
|AMC3330DWER.A|DWE|SO-MOD|16|2000|506.98|12.7|4826|6.6|


|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||



Pack Materials-Page 3


## **PACKAGE OUTLINE**

SOIC





























NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm, per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm, per side.
5. Reference JEDEC registration MS-013.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DWE0016A SOIC - 2.65 mm max height**

SOIC

































NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**
# **DWE0016A SOIC - 2.65 mm max height**

SOIC

































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


