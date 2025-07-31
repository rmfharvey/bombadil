**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)

##### **TPS1HTC30-Q1, 30-mΩ, 6-A Single-Channel Automotive Smart High-Side Switch**



**1 Features**


- Single-channel smart high-side power switch for
24-V automotive systems with full diagnostics

- Wide operating voltage range: 6 V to 60 V

–
OVP protection: 66 V

- Low R ON : 30-mΩ typical, 55-mΩ maximum

- Low standby current: < 0.5 µA

- Low quiescent current (Iq): < 2 mA

- [Improve system level reliability through adjustable](https://www.ti.com/lit/pdf/SLVA859)
[current limiting](https://www.ti.com/lit/pdf/SLVA859)

– Current limit: 2 A –16 A

- Accurate current sensing: ±4% at 1 A

- Protection

–
Overload and short-circuit protection

–
Integrated inductive discharge clamp

–
Undervoltage lockout (UVLO) protection

–
Loss of GND, loss of supply protection

–
Reverse battery protection with external
components

- Diagnostics

–
On and off state output open-load and short-tobattery detection

–
Overload and short to ground detection
– Absolute and relative thermal shutdown

detection

- [Functional Safety-Capable](https://www.ti.com/technologies/functional-safety/overview.html)

–
[Documentation available to aid functional safety](https://www.ti.com/lit/pdf/SFFS626)
[system design](https://www.ti.com/lit/pdf/SFFS626)

- Operating junction temperature: –40 to 125°C

- Input control: 1.8-V, 3.3-V and 5-V logic compatible

- Integrated fault sense voltage scaling for ADC
protection

- Qualifications

–
AEC-Q100 qualified for automotive applications

    - Temperature grade 1: –40°C to +125°C, T A

- 14-pin thermally-enhanced TSSOP package


**2 Applications**


- [General resistive, inductive, and capacitive loads](https://www.ti.com/lit/pdf/SLVAE30)



**3 Description**


TPS1HTC30-Q1 is a single-channel, smart high-side
switch, with integrated NMOS power FET and charge
pump, designed to meet the requirements of 24-V
automotive battery systems. The low R ON (30 mΩ)
minimizes device power dissipation driving a wide
range of output load current up to 6-A DC, and the 60V DC operating range improves system robustness.


The device integrates protection features such as
thermal shutdown, output clamp, and current limit.
These features improve system robustness during
fault events such as short circuit. TPS1HTC30-Q1
implements an adjustable current limiting circuit that
improves the reliability of the system by reducing
inrush current when driving large capacitive loads
and minimizing overload current. The device also
provides an accurate load current sense that allows
for improved load diagnostics such as overload
and open-load detection enabling better predictive
maintenance.


TPS1HTC30-Q1 is available in a small 14-pin, 4.40mm × 5.0-mm HTSSOP leaded package with 0.65mm pin pitch minimizing the PCB footprint.


**Package Information**


|PART NUMBER|PACKAGE(1)|PACKAGE<br>SIZE(2)|BODY SIZE<br>(NOM)|
|---|---|---|---|
|TPS1HTC30-Q1<br>|PWP<br>(HTSSOP, 14)|6.50 mm ×<br>5.00 mm|4.40 mm ×<br>5.00 mm|













(1) For all available packages, see the orderable addendum at
the end of the data sheet.
(2) The package size (length x width) is a nominal value and
includes pins, where applicable.


24V Automotive Battery









To Inductive,
Capacitive and
Resistive Load









**Typical Application Schematic**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Revision History** .............................................................. 2
**5 Pin Configuration and Functions** ...................................3

5.1 Recommended Connections for Unused Pins............ 3
**6 Specifications** .................................................................. 4

6.1 Absolute Maximum Ratings........................................ 4
6.2 ESD Ratings............................................................... 4
6.3 Recommended Operating Conditions.........................4
6.4 Thermal Information....................................................4

6.5 Electrical Characteristics.............................................5
6.6 SNS Timing Characteristics........................................ 8
6.7 Switching Characteristics............................................8
6.8 Timing Diagrams......................................................... 9
6.9 Typical Characteristics.............................................. 11
**7 Parameter Measurement Information** .......................... 13

**8 Detailed Description** ......................................................13



8.1 Overview................................................................... 13

8.2 Functional Block Diagram......................................... 14
8.3 Feature Description...................................................14
8.4 Device Functional Modes..........................................27

**9 Application and Implementation** .................................. 28

9.1 Application Information............................................. 28
9.2 Typical Application.................................................... 28
9.3 Power Supply Recommendations.............................32
9.4 Layout....................................................................... 32
**10 Device and Documentation Support** ..........................35

10.1 Documentation Support.......................................... 35
10.2 Receiving Notification of Documentation Updates..35
10.3 Support Resources................................................. 35
10.4 Trademarks............................................................. 35
10.5 Electrostatic Discharge Caution..............................35
10.6 Glossary..................................................................35
**11 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 35



**4 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

|DATE|REVISION|NOTES|
|---|---|---|
|September 2023|*|Initial Release|



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**5 Pin Configuration and Functions**


GND


EN


DIAG_EN


FAULT


LATCH


SNS


ILIM



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



VS


VS


VS


NC


VOUT


VOUT





8 VOUT







**Figure 5-1. PWP Package, 14-Pin HTSSOP Top View**


**Table 5-1. Pin Functions**

|PWP PIN NUMBER|PIN NAME|TYPE(1)|DESCRIPTION|
|---|---|---|---|
|1|GND|Power|Ground of device. Connect to resistor- diode ground network to have<br>reverse battery protection|
|2|EN|I|Input control for channel activation, internal pulldown|
|3|DIAG_EN|I|Enable-disable pin for diagnostics, internal pulldown|
|4|~~FAULT~~|O|Open drain global fault output. Referred to~~FLT,~~ or fault pin|
|5|LATCH|I|Thermal shutdown behavior, latch off or auto retry, internal pull down|
|6|SNS|O|Output corresponding sense value based on sense ratio|
|7|ILIM|O|Adjustable current limit. Short to ground or leave floating if external<br>current limit is not used|
|11|NC|N/A|No internal connection|
|8, 9, 10|VOUT|Power|Output of high side switch, connected to load|
|12, 13,<br>14|VS|Power|Power supply|
|Thermal Pad|Pad|--|Thermal Pad, internally shorted to ground|



(1) I = input, O = output


**5.1 Recommended Connections for Unused Pins**


TPS1HTC30-Q1 is designed to provide an enhanced set of diagnostic and protection features. However, if the
system design only allows for a limited number of I/O connections, some pins can be considered as optional.


**Table 5-2. Connections for Optional Pins**












|PIN NAME|CONNECTION IF NOT USED|IMPACT IF NOT USED|
|---|---|---|
|SNS|Ground through 1-kΩ resistor|Analog sense is not available.|
|LATCH|Float or ground through RPROT<br>resistor|With LATCH unused, the device performs an auto-retry after a fault. If<br>latched behavior is desired, but the system describes limited I/O, it is<br>possible to use one microcontroller output to control the latch function of<br>several high-side channels.|
|ILIM|Float|If the ILIM pin is left floating, the device is set to the default internal current-<br>limit threshold. This is considered a fault state for the device.|
|~~FAULT~~|Float|If the~~ FAULT~~pin is unused, the system cannot read faults from the output.|
|DIAG_EN|Float or ground through RPROT<br>resistor|With DIAG_EN unused, the analog sense, open-load, and short-to-battery<br>diagnostics are not available.|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 3


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**6 Specifications**
**6.1 Absolute Maximum Ratings**
Over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|Continuous supply voltage, VS with respect to IC GND|Continuous supply voltage, VS with respect to IC GND|-0.7<br>64|V|
|Continuous output voltage, VOUTwith respect to IC GND|Continuous output voltage, VOUTwith respect to IC GND|-60<br>64|V|
|Maximum transient (< 100 us) voltage at the supply pin, VS with respect to IC GND|Maximum transient (< 100 us) voltage at the supply pin, VS with respect to IC GND|-0.7<br>81|V|
|Enable pin voltage, VEN|Enable pin voltage, VEN|–1<br>7|V|
|LATCH pin voltage, VLATCH|LATCH pin voltage, VLATCH|–1<br>7|V|
|DIAG_EN pin voltage, VDIAG_EN|DIAG_EN pin voltage, VDIAG_EN|–1<br>7|V|
|Sense pin voltage, VSNS|Sense pin voltage, VSNS|–1<br>7|V|
|~~FAULT~~ pin voltage, V~~FAULT~~|~~FAULT~~ pin voltage, V~~FAULT~~|–1<br>7|V|
|Reverse ground current, IGND|VS < 0 V|–50|mA|
|Maximum junction temperature, TJ|Maximum junction temperature, TJ|150|°C|
|Storage temperature, Tstg|Storage temperature, Tstg|–65<br>150|°C|



(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.


**6.2 ESD Ratings**









|Col1|Col2|Col3|Col4|VALUE|UNIT|
|---|---|---|---|---|---|
|VESD|Electrostatic<br>discharge|Human body model (HBM), per<br>AEC Q100-002 Classification Level H2(1)|All pins except VS and VOUT|±2000|V|
|VESD|Electrostatic<br>discharge|Human body model (HBM), per<br>AEC Q100-002 Classification Level H3A(1)|VS and VOUT with respect to<br>GND|±4000|V|
|VESD|Electrostatic<br>discharge|Charged device model (CDM), per AEC Q100-011<br>Classification Level C5|All pins|±750|V|


(1) AEC-Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.


**6.3 Recommended Operating Conditions**
over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|VS_OP_NOM|Nominal supply voltage|6.0<br>60|V|
|VEN|Enable voltage|–1<br>5.5|V|
|VLATCH|LATCH pin voltage, VLATCH|–1<br>5.5|V|
|VDIAG_EN|Diagnostic Enable voltage|–1<br>5.5|V|
|VFAULT|~~FAULT~~ pin voltage|–1<br>5.5|V|
|VSNS|Sense voltage|–1<br>5.5|V|
|TA|Operating free-air temperature|–40<br>125|°C|



(1) All operating voltage conditions are measured with respect to device GND


**6.4 Thermal Information**







|THERMAL METRIC(1) (2)|Col2|TPS1HTC30|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1) (2)|**THERMAL METRIC**(1) (2)|**PWP (HTSSOP)**|**PWP (HTSSOP)**|
|**THERMAL METRIC**(1) (2)|**THERMAL METRIC**(1) (2)|**14 PINS**|**14 PINS**|
|RθJA|Junction-to-ambient thermal resistance|31.5|°C/W|


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**6.4 Thermal Information (continued)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



|THERMAL METRIC(1) (2)|Col2|TPS1HTC30|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1) (2)|**THERMAL METRIC**(1) (2)|**PWP (HTSSOP)**|**PWP (HTSSOP)**|
|**THERMAL METRIC**(1) (2)|**THERMAL METRIC**(1) (2)|**14 PINS**|**14 PINS**|
|RθJC(top)|Junction-to-case (top) thermal resistance|23.8|°C/W|
|RθJB|Junction-to-board thermal resistance|7.4|°C/W|
|ψJT|Junction-to-top characterization parameter|0.2|°C/W|
|ψJB|Junction-to-board characterization parameter|7.3|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|1.5|°C/W|


(1) [For more information about traditional and new thermal metrics, see the SPRA953 application report.](https://www.ti.com/lit/pdf/SPRA953)
(2) The thermal parameters are based on a 4-layer PCB according to the JESD51-5 and JESD51-7 standards.


**6.5 Electrical Characteristics**


V S = 6 V to 60 V, T A = -40°C to 125°C (unless otherwise noted)
















































|PARAMETER|Col2|TEST CONDITIONS|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|**VS SUPPLY VOLTAGE AND CURRENT**|**VS SUPPLY VOLTAGE AND CURRENT**|**VS SUPPLY VOLTAGE AND CURRENT**|**VS SUPPLY VOLTAGE AND CURRENT**|**VS SUPPLY VOLTAGE AND CURRENT**|**VS SUPPLY VOLTAGE AND CURRENT**|
|ILNOM|Continuous load current|VEN = HI, TAMB = 85°C|VEN = HI, TAMB = 85°C|6|A|
|IQ, VS|VS quiescent current|VEN = HI, IOUT = 0A|VDIAG_EN = LO|1<br>1.5|mA|
|IQ, VS|VS quiescent current|VEN = HI, IOUT = 0A|VDIAG_EN = HI|1.1<br>1.9|mA|
|ISTBY, VS|Total device standby<br>current (including<br>MOSFET) with<br>diagnostics disabled|VS ≤ 60 V, VEN =<br>VDIAG_EN = LO, VOUT = 0<br>V|TJ = 85°C|0.25<br>0.7|µA|
|ISTBY, VS|Total device standby<br>current (including<br>MOSFET) with<br>diagnostics disabled|VS ≤ 60 V, VEN =<br>VDIAG_EN = LO, VOUT = 0<br>V|TJ = 150°C|0.63<br>6|µA|
|IOUT(OFF)|Output leakage current|VS ≤ 60 V, VEN =<br>VDIAG_EN = 0 V, VOUT = 0<br>V|TJ = 85°C|0.4|µA|
|IOUT(OFF)|Output leakage current|VS ≤ 60 V, VEN =<br>VDIAG_EN = 0 V, VOUT = 0<br>V|TJ = 150°C|0.2<br>12|µA|
|tSTBY|Standby mode delay time|VEN = VDIAG_EN = 0 V to standby|VEN = VDIAG_EN = 0 V to standby|20|ms|
|**VS UNDERVOLTAGE LOCKOUT (UVLO) INPUT**|**VS UNDERVOLTAGE LOCKOUT (UVLO) INPUT**|**VS UNDERVOLTAGE LOCKOUT (UVLO) INPUT**|**VS UNDERVOLTAGE LOCKOUT (UVLO) INPUT**|**VS UNDERVOLTAGE LOCKOUT (UVLO) INPUT**|**VS UNDERVOLTAGE LOCKOUT (UVLO) INPUT**|
|VS,UVLOR|VS undervoltage lockout<br>rising|Measured with respect to the GND pin of the device|Measured with respect to the GND pin of the device|5.0<br>5.4<br>5.75|V|
|VS,UVLOF|VS undervoltage lockout<br>falling|VS undervoltage lockout<br>falling|VS undervoltage lockout<br>falling|4.1<br>4.5<br>4.85|V|
|**VS OVERVOLTAGE LOCKOUT (OVLO) INPUT**|**VS OVERVOLTAGE LOCKOUT (OVLO) INPUT**|**VS OVERVOLTAGE LOCKOUT (OVLO) INPUT**|**VS OVERVOLTAGE LOCKOUT (OVLO) INPUT**|**VS OVERVOLTAGE LOCKOUT (OVLO) INPUT**|**VS OVERVOLTAGE LOCKOUT (OVLO) INPUT**|
|VS,OVPR|VS overvoltage protection<br>rising|Measured with respect<br>to the GND pin of the<br>device, VEN = HI|Measured with respect<br>to the GND pin of the<br>device|62<br>65<br>68|V|
|VS,OVPRF|VS overvoltage protection<br>recovery falling|Measured with respect<br>to the GND pin of the<br>device, VEN = HI|Measured with respect<br>to the GND pin of the<br>device|60<br>63<br>66|V|
|VS,OVPRH|VS overvoltage protection<br>threshold hysteresis|Measured with respect<br>to the GND pin of the<br>device|Measured with respect<br>to the GND pin of the<br>device|2|V|
|tVS,OVP|VS overvoltage protection<br>deglitch time|Time from triggering the OVP fault to FET turn-off|Time from triggering the OVP fault to FET turn-off|125|µs|
|**VDS CLAMP**|**VDS CLAMP**|**VDS CLAMP**|**VDS CLAMP**|**VDS CLAMP**|**VDS CLAMP**|
|VDS,Clamp|VDS clamp voltage|FET current = 10 mA|VS = 24 V|65<br>72.5<br>80|V|
|VDS,Clamp|VDS clamp voltage|FET current = 10 mA|VS = 6 V|48<br>53<br>58|V|
|**RON CHARACTERISTICS**|**RON CHARACTERISTICS**|**RON CHARACTERISTICS**|**RON CHARACTERISTICS**|**RON CHARACTERISTICS**|**RON CHARACTERISTICS**|
|RON|On-resistance<br>(Includes MOSFET and<br>package)|VS = 6 V to 60 V, 0.5 A ≤<br>IOUT≤ 6 A|TJ = 25°C|30|mΩ|
|RON|On-resistance<br>(Includes MOSFET and<br>package)|VS = 6 V to 60 V, 0.5 A ≤<br>IOUT≤ 6 A|TJ = 125°C|50|mΩ|
|RON|On-resistance<br>(Includes MOSFET and<br>package)|VS = 6 V to 60 V, 0.5 A ≤<br>IOUT≤ 6 A|TJ = 150°C|60|mΩ|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 5


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**6.5 Electrical Characteristics (continued)**


V S = 6 V to 60 V, T A = -40°C to 125°C (unless otherwise noted)




































|PARAMETER|Col2|TEST CONDITIONS|Col4|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|
|RON(REV)|On-resistance during<br>reverse polarity|VS = –24 V, IOUT= 2 A|TJ = -40°C to  150°C|30<br>60|mΩ|
|**CURRENT LIMIT CHARACTERISTICS**|**CURRENT LIMIT CHARACTERISTICS**|**CURRENT LIMIT CHARACTERISTICS**|**CURRENT LIMIT CHARACTERISTICS**|**CURRENT LIMIT CHARACTERISTICS**|**CURRENT LIMIT CHARACTERISTICS**|
|ILIM_INT|ILIMCurrent Limitation<br>level internal reference|RILIM =  Open or Out of range|RILIM =  Open or Out of range|8|A|
|ILIM_INT|ILIMCurrent Limitation<br>level internal reference|RILIM = GND|RILIM = GND|16|A|
|KCL|Current Limit Ratio||RILIM = 10 kΩ to 50 kΩ|80<br>100<br>120|A * kΩ|
|**THERMAL SHUTDOWN CHARACTERISTICS**|**THERMAL SHUTDOWN CHARACTERISTICS**|**THERMAL SHUTDOWN CHARACTERISTICS**|**THERMAL SHUTDOWN CHARACTERISTICS**|**THERMAL SHUTDOWN CHARACTERISTICS**|**THERMAL SHUTDOWN CHARACTERISTICS**|
|TABS|Thermal shutdown|||154<br>165|°C|
|TREL|Relative thermal<br>shutdown|||60|°C|
|tRETRY|Retry time|Time from fault shutdown until switch re-enable<br>(thermal shutdown).|Time from fault shutdown until switch re-enable<br>(thermal shutdown).|2|ms|
|Fault<br>Response|Fault reponse to Thermal<br>Shutdown|||Configura<br>ble via<br>Latch pin||
|THYS|Thermal shutdown<br>hysteresis|||20|°C|
|**FAULT PIN CHARACTERISTICS**|**FAULT PIN CHARACTERISTICS**|**FAULT PIN CHARACTERISTICS**|**FAULT PIN CHARACTERISTICS**|**FAULT PIN CHARACTERISTICS**|**FAULT PIN CHARACTERISTICS**|
|VFAULT|~~FAULT~~ low output voltage|~~IFAULT ~~= 2.5 mA|~~IFAULT ~~= 2.5 mA|0.5|V|
|tFAULT_FLT|Fault indication-time|VDIAG_EN = 5 V<br>Time between fault and~~FAULT~~ asserting|VDIAG_EN = 5 V<br>Time between fault and~~FAULT~~ asserting|60|µs|
|tFAULT_SNS|Fault indication-time|VDIAG_EN = 5 V<br>Time between fault and ISNS settling at VSNSFH|VDIAG_EN = 5 V<br>Time between fault and ISNS settling at VSNSFH|60|µs|
|**CURRENT SENSE CHARACTERISTICS**|**CURRENT SENSE CHARACTERISTICS**|**CURRENT SENSE CHARACTERISTICS**|**CURRENT SENSE CHARACTERISTICS**|**CURRENT SENSE CHARACTERISTICS**|**CURRENT SENSE CHARACTERISTICS**|
|KSNS1|Current sense ratio<br>IOUT / ISNS|||1300|A/A|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 6 A|4.61|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 6 A|–6<br>6|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 4 A|3.3|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 4 A|–3<br>3|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 2 A|<br>1.66<br>|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 2 A|–4<br>4|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 1 A|<br>0.833<br>|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 1 A|–4<br>4|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 500 mA|<br>0.417<br>|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 500 mA|–6<br>6|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 200 mA|0.15<br>|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 200 mA|–10<br>10|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 100 mA|<br>0.073<br>|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 100 mA|–15<br>15|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 50 mA|0.035|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 50 mA|–25<br>25|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 20 mA|0.012|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 20 mA|–40<br>40|%|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 10 mA|0.0088|mA|
|ISNSI|Current sense current<br>and accuracy|VEN = VDIAG_EN = 5 V|IOUT = 10 mA|–60<br>60|%|
|**SNS PIN CHARACTERISTICS**|**SNS PIN CHARACTERISTICS**|**SNS PIN CHARACTERISTICS**|**SNS PIN CHARACTERISTICS**|**SNS PIN CHARACTERISTICS**|**SNS PIN CHARACTERISTICS**|



6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**6.5 Electrical Characteristics (continued)**


V S = 6 V to 60 V, T A = -40°C to 125°C (unless otherwise noted)



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)





























|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|VSNSFH|VSNSfault high-level|VDIAG_EN = 5 V|4.5<br>5<br>5.77|V|
|VSNSFH|VSNSfault high-level|VDIAG_EN = VIH to 3.3 V|3.0<br>3.3<br>3.82|V|
|ISNSFLT|ISNSfault high-level|VDIAG_EN > VIH,DIAG_EN|5.3<br>6.4|mA|
|ISNSleak|ISNS leakage|VDIAG_EN = 5 V, IL = 0 mA|1.3|µA|
|VS_ISNS|VS headroom needed for<br>full current sense and<br>fault functionality|VDIAG_EN = 3.3 V|6|V|
|VS_ISNS|VS headroom needed for<br>full current sense and<br>fault functionality|VDIAG_EN = 5 V|6.5|V|
|**OPEN LOAD DETECTION CHARACTERISTICS**|**OPEN LOAD DETECTION CHARACTERISTICS**|**OPEN LOAD DETECTION CHARACTERISTICS**|**OPEN LOAD DETECTION CHARACTERISTICS**|**OPEN LOAD DETECTION CHARACTERISTICS**|
|VOL_OFF|OFF state open-load<br>(OL) detection voltage|VEN = 0 V, VDIAG_EN = 5 V|1.5<br>2<br>2.5|V|
|ROL_OFF|OFF state open-load<br>(OL) detection internal<br>pull-up resistor|VEN = 0 V, VDIAG_EN = 5 V|120<br>150<br>180|kΩ|
|tOL_OFF|OFF state open-load<br>(OL) detection deglitch<br>time|VEN = 0 V, VDIAG_EN = 5 V, When Vs – VOUT < VOL, <br>duration longer than tOL. Openload detected.|480<br>700|µs|
|tOL_OFF_1|OL_OFF and STB<br>indication-time from EN<br>falling|VEN= 5 V to 0 V, VDIAG_EN = 5 V<br>IOUT = 0 mA, VOUT = Vs - VOL|310<br>700|µs|
|tOL_OFF_2|OL and STB indication-<br>time from DIA_EN rising|VEN = 0 V, VDIAG_EN = 0 V to 5 V<br>IOUT= 0 mA, VOUT = VS - VOL|700|µs|
|**DIAG_EN PIN CHARACTERISTICS**|**DIAG_EN PIN CHARACTERISTICS**|**DIAG_EN PIN CHARACTERISTICS**|**DIAG_EN PIN CHARACTERISTICS**|**DIAG_EN PIN CHARACTERISTICS**|
|VIL, DIAG_EN|Input voltage low-level|No GND Network|0.8|V|
|VIH, DIAG_EN|Input voltage high-level|No GND Network|1.5|V|
|VIHYS,<br>DIAG_EN|Input voltage hysteresis||280|mV|
|RDIAG_EN|Internal pulldown resistor||200<br>350<br>500|kΩ|
|IIL, DIAG_EN|Input current low-level|VDIAG_EN = 0.8 V|2.2|µA|
|IIH, DIAG_EN|Input current high-level|VDIAG_EN = 5 V|14|µA|
|**EN PIN CHARACTERISTICS**|**EN PIN CHARACTERISTICS**|**EN PIN CHARACTERISTICS**|**EN PIN CHARACTERISTICS**|**EN PIN CHARACTERISTICS**|
|VIL, EN|Input voltage low-level|No GND Network|0.8|V|
|VIH, EN|Input voltage high-level|No GND Network|1.5|V|
|VIH, EN|Input voltage hysteresis||280|mV|
|REN|Internal pulldown resistor||200<br>350<br>500|kΩ|
|IIL, EN|Input current low-level|VEN = 0.8 V|2.2|µA|
|IIH, EN|Input current high-level|VEN = 5 V|14|µA|
|**LATCH PIN CHARACTERISTICS**|**LATCH PIN CHARACTERISTICS**|**LATCH PIN CHARACTERISTICS**|**LATCH PIN CHARACTERISTICS**|**LATCH PIN CHARACTERISTICS**|
|VIL, LATCH|Input voltage low-level|No GND Network|0.8|V|
|VIH, LATCH|Input voltage high-level|No GND Network|1.5|V|
|VIHYS,<br>LATCH|Input voltage hysteresis||280|mV|
|RLATCH|Internal pulldown resistor||0.7<br>1<br>1.4|MΩ|
|IIL, LATCH|Input current low-level|VDIA_EN = 0.8 V|2.2|µA|
|IIH, LATCH|Input current high-level|VDIA_EN = 5 V|14|µA|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 7


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**6.6 SNS Timing Characteristics**


V BB = 6 V to 60 V, T A = -40°C to 125°C (unless otherwise noted), parameters not tested in production











|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**SNS TIMING - CURRENT SENSE**|**SNS TIMING - CURRENT SENSE**|**SNS TIMING - CURRENT SENSE**|**SNS TIMING - CURRENT SENSE**|**SNS TIMING - CURRENT SENSE**|
|tSNSION1|Settling time from rising edge of DIAG_EN<br>50% of VDIA_ENto 90% of settled ISNS|VEN= 5 V, VDIAG_EN = 0 V to 5 V<br>RSNS = 1 kΩ, IL = 1A|30|µs|
|tSNSION1|Settling time from rising edge of DIAG_EN<br>50% of VDIA_ENto 90% of settled ISNS|VEN = 5 V, VDIAG_EN = 0 V to 5 V<br>RSNS = 1 kΩ, IL = 30 mA|60|µs|
|tSNSION2|Settling time from rising edge of EN and<br>DIAG_EN<br>50% of VDIA_ENVENto 90% of settled ISNS|VEN = VDIAG_EN = 0 V to 5 V<br>RSNS = 1 kΩ, IL = 1 A|200|µs|
|tSNSION3|Settling time from rising edge of EN with<br>DIAG_EN HI;<br>50% of VDIA_ENVENto 90% of settled ISNS|VEN = 0 V to 5 V, VDIAG_EN = 5 V<br>RSNS = 1 kΩ, IL = 1 A|200|µs|
|tSNSIOFF|Settling time from falling edge of DIAG_EN|VEN = 5 V, VDIAG_EN = 5 V to 0 V<br>RSNS = 1 kΩ, RL = 125 Ω|20|µs|
|tSETTLEH|Settling time from rising edge of load step|VEN = 5 V, VDIAG_EN = 5 V<br>RSNS = 1 kΩ, IOUT = 0.5 A to 3 A|20|µs|
|tSETTLEL|Settling time from falling edge of load step|VEN = 5 V, VDIAG_EN= 5 V<br>RSNS = 1 kΩ, IOUT = 3 A to 0.5 A|20|µs|


**6.7 Switching Characteristics**


V S = 48 V, R L = 120 Ω, T A = -40°C to 125°C (unless otherwise noted)














|Parameter|Col2|Test Conditions|Min|Typ|Max|Col7|
|---|---|---|---|---|---|---|
|**Parameter**|**Parameter**|**Test Conditions**|**Min**|**Typ**|**Max**||
|**Parameter**|**Parameter**|**Test Conditions**|**Min**|**Typ**|**Max**|**Unit**|
|tDR|Turnon delay time (from standby)|50% of EN to 20% of VOUT|30|60|82.5|µs|
|tDR|Turnon delay time (from active)|50% of EN to 20% of VOUT|30|50|72.5|µs|
|tDF|Turnoff delay time|50% of EN to 80% of VOUT|55|95|135|µs|
|SRR|VOUT rising slew rate|20% to 80% of VOUT|0.2|0.45|0.8|V/µs|
|SRF|VOUT falling slew rate|80% to 20% of VOUT|0.2|0.55|0.9|V/µs|
|fmax|Maximum PWM frequency||||750|Hz|
|tON|Turnon time|50% of EN to 80% of VOUT||125|200|µs|
|tOFF|Turnoff time|50% of EN to 20% of VOUT||145|230|µs|
|tON - tOFF|Turnon and off matching|1ms ON time switch enable pulse|–25||25|µs|
|tON - tOFF|Turnon and off matching|200-µs enable pulse<br>F = fmax|–25||25|µs|
|tOFF_pw|Minimum VOUT ON pulse width|200-µs OFFtime switch enable<br>pulse, VOUT @ 20% of VS, F = fmax|70||160|µs|
|ΔPWM|PWM accuracy - average load<br>current|300-µs enable pulse<br>F = fmax|–15||15|%|
|EON|Switching energy losses during<br>turnon|1 ms pulse, VOUT from 10% to 90%<br>of VS voltage||0.3|0.4|mJ|
|EOFF|Switching energy losses during<br>turnoff|1 ms pulse, VOUT from 10% to 90%<br>of VS voltage||0.25|0.35|mJ|



8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**6.8 Timing Diagrams**


V EN(1)


V OUT







**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)


|Col1|Col2|Col3|
|---|---|---|
|N<br>(1)|50%|50%|
|UT|tDR<br>tON<br>10%<br>90%|tDF<br>tOFF<br>90%<br>10%|
||||



Rise and fall time of V EN is 100 ns.


**Figure 6-1. Switching Characteristics Definitions**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 9


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


V EN


V DIA_EN


I OUT


I SNS




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||tSNSIOFF1|tSNSIOFF1|
||tSNSION1|tSNSION1|tSNSION2|tSNSION2|tSNSION3|tSNSION3|tSNSION3||


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||tSETTLEL|tSETTLEL|
||tSETTLEH|tSETTLEH|tSETTLEH||





V EN


V DIA_EN


I OUT


I SNS


V EN


V DIA_EN


T J


I SNS






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||tSNSTOFF|tSNSTOFF|
||tSNSTON1|tSNSTON1|tSNSTON2|tSNSTON2|tSNSTON2||



Rise and fall times of control signals are 100 ns. Control signals include: EN, DIA_EN.


**Figure 6-2. SNS Timing Characteristics Definitions**


10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**6.9 Typical Characteristics**





**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)












|Col1|6.5 V|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~8.5 V~~<br>13.5 V||||||||
||18 V<br>~~4 V~~||||||||
||27.5 V<br>||||||||
||~~36 V~~||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|0.2 A|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~0.5 A~~<br>6 A||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||~~.5~~||
|||||||||||||||||||.5|V|
||||||||||||||||||1|3.5|V|
||||||||||||||||||~~1~~<br>|~~8 V~~<br>||
|||||||||||||||||||~~4~~<br>||
|||||||||||||||||||~~7.~~<br>|~~ V~~<br>|
|||||||||||||||||||~~6~~||


|Col1|6.5 V|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~24 V~~<br>~~28 V~~||||||||
||36 V||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|6<br>1|.5 V<br>8 V|
|---|---|---|---|---|---|---|---|---|
||||||||2<br>|4 V<br>|
||||||||3|~~7.5 V~~<br>6 V|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
||||||||||||||||6|.5|V|
|||||||||||||||||||
||||||||||||||||1<br>|8 V<br>||
|||||||||||||||||||
|||||||||||||||||~~4~~<br>||
|||||||||||||||||~~7.5~~<br>|~~ V~~<br>|
|||||||||||||||||~~6~~||






|45<br>6.5 V<br>42.5 8.5 V<br>40 13.5 V<br>18 V<br>37.5 24 V (m)<br>27.5 V<br>35 36 V On-Resistance<br>32.5<br>30<br>27.5<br>25<br>22.5<br>20<br>-40 -20 0 20 40 60 80 100 120 140<br>Temperature (C)<br>I = 0. 2 A<br>OUT<br>Figure 6-3. On-Resistance (R ) vs Temperature vs VS Supply<br>ON<br>Voltage|45<br>0.2 A<br>42.5 0.5 A<br>40 6 A<br>37.5 (m)<br>35<br>On-Resistance<br>32.5<br>30<br>27.5<br>25<br>22.5<br>20<br>-40 -20 0 20 40 60 80 100 120 140<br>Temperature (C)<br>VS = 24 V<br>Figure 6-4. On-Resistance (R ) vs Temperature vs Load<br>ON<br>Current|
|---|---|
|Temperature (C)<br>Quiescent Current (mA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>0.85<br>0.86<br>0.87<br>0.88<br>0.89<br>0.9<br>0.91<br>0.92<br>0.93<br>0.94<br>0.95<br>0.96<br>0.97<br>0.98<br>0.99<br>1<br>~~6.5 V~~<br>8.5 V<br>13.5 V<br>~~18 V~~<br>~~24 V~~<br>~~27.5 V~~<br>~~36 V~~<br>VEN = 5 V<br>VDIAG_EN = 0 V<br>**Figure 6-5. Quiescent Current (IQ, VS) From VS Input Supply vs**<br>**Temperature vs VS Voltage**|Temperature (C)<br>VS Standby Current (uA)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>0.1<br>0.15<br>0.2<br>0.25<br>0.3<br>0.35<br>0.4<br>0.45<br>0.5<br>0.55<br>0.6<br>0.65<br>6.5 V<br>~~24 V~~<br>~~28 V~~<br>36 V<br>VEN = 0 V<br>VDIAG_EN = 0 V<br>**Figure 6-6. Standby Current (ISTBY, VS) From VS Input Supply vs**<br>**Temperature vs VS Voltage**|
|Temperature (C)<br>Turn-on Deltay Time (us)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>32.7<br>33<br>33.3<br>33.6<br>33.9<br>34.2<br>34.5<br>34.8<br>35.1<br>35.4<br>6.5 V<br>~~18 V~~<br>24 V<br>~~27.5 V~~<br>36 V<br>RL= 48 Ω<br> <br>**Figure 6-7. Turn-on Delay Time (tDR) vs Temperature vs VS**<br>**Voltage**|Temperature (C)<br>Turn-off Delay Time (us)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>10<br>12<br>14<br>16<br>18<br>20<br>22<br>24<br>26<br>28<br>30<br>32<br>34<br>36<br>38<br>40<br>6.5 V<br>18 V<br>~~24 V~~<br>~~27.5 V~~<br>~~36 V~~<br>RL= 48 Ω<br> <br>**Figure 6-8. Turn-off Delay Time (tDF) vs Temperature vs VS**<br>**Voltage**|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 11


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**6.9 Typical Characteristics (continued)**










|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||~~.5~~||
||||||||||||||||~~1~~<br>|~~8 V~~<br>~~4~~||
||||||||||||||||2<br>|7.5<br>~~6~~|V<br>|
|||||||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||~~.5~~<br>~~18 V~~<br>|~~V~~<br><br>|
|||||||||||||||||4<br>27.5<br>|V<br>|
|||||||||||||||||~~6~~||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||18<br>||
|||||||||||||||||~~24~~<br>||
|||||||||||||||||~~27.~~<br>|~~ V~~<br>|
|||||||||||||||||~~6~~||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||~~8~~||
|||||||||||||||||~~4~~||
|||||||||||||||||~~7.~~|~~ V~~|
|||||||||||||||||~~6~~||
|||||||||||||||||||







|72<br>68<br>64<br>60<br>56 (us)<br>52<br>Time<br>48<br>44 Turn-on<br>40<br>36 6.5 V<br>32 18 V<br>24 V<br>28<br>27.5 V<br>24 36 V<br>20<br>-40 -20 0 20 40 60 80 100 120 140<br>Temperature (C)<br>R = 48 Ω<br>L<br>Figure 6-9. Turn-on Time (t ) vs Temperature vs VS Voltage<br>ON|70<br>65<br>60<br>55 (us)<br>50<br>Time<br>45<br>Turn-off<br>40<br>35 6.5 V<br>18 V<br>30 24 V<br>25 27.5 V<br>36 V<br>20<br>-40 -20 0 20 40 60 80 100 120 140<br>Temperature (C)<br>R = 48 Ω<br>L<br>Figure 6-10. Turn-off Time (t ) vs Temperature vs VS Voltage<br>OFF|
|---|---|
|Temperature (C)<br>VOUT Rising Slew Rate (V/us)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>0.2<br>0.25<br>0.3<br>0.35<br>0.4<br>0.45<br>0.5<br>0.55<br>0.6<br>0.65<br>0.7<br>0.75<br>0.8<br>0.85<br>0.9<br>0.95<br>18 V<br>~~24 V~~<br>~~27.5 V~~<br>~~36 V~~<br>RL= 48 Ω<br> <br>**Figure 6-11. VOUT Rising Slew Rate (SRR) vs Temperature vs**<br>**VS Voltage**|Temperature (C)<br>VOUT Falling Slew Rate (V/us)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0.8<br>0.9<br>1<br>~~18 V~~<br>~~24 V~~<br>~~27.5 V~~<br>~~36 V~~<br>RL= 48 Ω<br> <br>**Figure 6-12. VOUT Rising Slew Rate (SRF) vs Temperature vs**<br>**VS Voltage**|
|Temperature (C)<br>Current Sense Ratio - KSNS1 (A/A)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>1280<br>1300<br>1320<br>1340<br>1360<br>1380<br>1400<br>1420<br>1440<br>1460<br>1480<br>~~IOUT~~<br>~~0.1 A~~<br>~~0.2 A~~<br>~~1 A~~<br>~~2 A~~<br>~~4 A~~<br>~~6 A~~<br>~~7 A~~<br>VS = 24 V<br> <br>**Figure 6-13. Current Sense Ratio (KSNS) vs Temperature vs Load Current**|Temperature (C)<br>Current Sense Ratio - KSNS1 (A/A)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>140<br>1280<br>1300<br>1320<br>1340<br>1360<br>1380<br>1400<br>1420<br>1440<br>1460<br>1480<br>~~IOUT~~<br>~~0.1 A~~<br>~~0.2 A~~<br>~~1 A~~<br>~~2 A~~<br>~~4 A~~<br>~~6 A~~<br>~~7 A~~<br>VS = 24 V<br> <br>**Figure 6-13. Current Sense Ratio (KSNS) vs Temperature vs Load Current**|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||~~IO~~|~~UT~~<br>||
|||||||||||||||||~~0.1~~<br>|~~ A~~<br>|
|||||||||||||||||~~0.2~~|~~ A~~|
|||||||||||||||||~~1~~||
|||||||||||||||||~~2~~||
|||||||||||||||||||
|||||||||||||||||~~4~~<br>||
|||||||||||||||||~~6~~<br>||
|||||||||||||||||~~7 A~~||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||


12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**7 Parameter Measurement Information**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



















**Figure 7-1. Parameter Definitions**


**8 Detailed Description**

**8.1 Overview**


The TPS1HTC30-Q1 is a automotive, single-channel, fully-protected, high-side power switch with an integrated
NMOS power FET and charge pump rated to 60-V DC tolerance. Full diagnostics and high-accuracy currentsense features enable intelligent control of the load. Low logic high threshold, V IH, of 1.5 V on the input pins
allow use of MCUs down to 1.8 V. A programmable current-limit function greatly improves the reliability of
the whole system. The device diagnostic reporting has two pins to support both digital status and analog
current-sense output, for multiplexing the MCU analog or digital interface among devices.


The digital status report is implemented with an open-drain structure on the fault pin. When a fault condition
occurs, the pin is pulled down to GND. An external pullup is required to match the microcontroller supply level.
High-accuracy current sensing allows a better real-time monitoring effect and more-accurate diagnostics without
further calibration. A current mirror is used to source 1 / K SNS of the load current, which is reflected as voltage
on the SNS pin. K SNS is a constant value across temperature and supply voltage. The SNS pin can also report a
fault by forcing a voltage of V SNSFH that scales with the diagnostic enable voltage so that the max voltage seen
by the system ADC is within an acceptable value. This removes the need for an external Zener diode or resistor
divider on the SNS pin.


The external high-accuracy current limit allows setting the current limit value by application. The external highaccuracy current limit highly improves the reliability of the system by clamping the inrush current effectively
under start-up or short-circuit conditions. Also, the external high-accuracy current limit can save system costs by
reducing PCB trace, connector size, and the preceding power-stage capacity. An internal current limit can also
be implemented in this device. The lower value of the external or internal current-limit value is applied.


An active drain to source voltage clamp is built in to address switching off the energy of inductive loads, such
as relays, solenoids, pumps, motors, and so forth. During the inductive switching-off cycle, both the energy
of the power supply (E BAT ) and the load (E LOAD ) are dissipated on the high-side power switch itself. With the
benefits of process technology and excellent IC layout, the TPS1HTC30-Q1 device can achieve excellent energy
dissipation capacity, which can help save the need of using external free-wheeling circuitry in most cases.


The TPS1HTC30-Q1 device can be used as a high-side power switch for a wide variety of resistive, inductive,
and capacitive loads, including the low-wattage bulbs, LEDs, relays, solenoids, and heaters.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 13


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**8.2 Functional Block Diagram**








|Col1|V<br>Cl|S<br>amp|
|---|---|---|
||||






|Current Limit|Col2|
|---|---|
|Current Limit<br>Thermal<br>Shutdown<br>Fault|Current Limit<br>Thermal<br>Shutdown<br>Fault|
|Current Limit<br>Thermal<br>Shutdown<br>Fault||
|Indication|Indication|













|RSNS|Col2|TPS1HTC30-Q1 Off-State<br>VS Open Load<br>Detection<br>Internal VS OV/UV VDS<br>LDO Clamp Detection Clamp<br>Gate Driver<br>EN Reverse FET<br>Turnon<br>VOUT<br>Current Limit<br>ILIM<br>LATCH Thermal<br>Shutdown<br>FAULT Fault<br>Indication<br>SNS<br>Voltage Current<br>Scaling Sense<br>Open Load<br>DIAG_EN Detection<br>GND|Col4|
|---|---|---|---|
|RSNS|RSNS|**TPS1HTC30-Q1**<br>Gate Driver<br>Reverse FET<br>Turnon<br>Current Limit<br>Thermal<br>Shutdown<br>EN<br>FAULT<br>ILIM<br>SNS<br>VOUT<br>VS<br>VDS<br>Clamp<br>Fault<br>Indication<br>DIAG_EN<br>GND<br>Current<br>Sense<br>Open Load<br>Detection<br>Voltage<br>Scaling<br>Off-State<br>Open Load<br>Detection<br>VS<br>Clamp<br>OV/UV<br>Detection<br>Internal<br>LDO<br>LATCH||
|RSNS||||


**8.3 Feature Description**


**8.3.1 Accurate Current Sense**


The high-accuracy current-sense function is internally implemented, which allows real-time monitoring and
more-accurate diagnostics without further calibration. A current mirror is used to source 1 / K SNS of the load
current, flowing out to the external resistor between the SNS pin and GND, and reflected as voltage on the SNS
pin.


K SNS is the ratio of the output current and the sense current. The accuracy values of K SNS quoted in the
electrical characteristics do take into consideration temperature and supply voltage. Each device was internally
calibrated while in production, so post-calibration by users is not required in most cases.


The maximum voltage out on the SNS pin is clamped to V SNSFH, which is the fault voltage level. To make
sure that this voltage is not higher than the system can tolerate, TI has correlated the voltage coming in on
the DIAG_EN pin with the maximum voltage out on the SNS pin. If DIAG_EN is between V IH and 3.3 V, the
maximum output on the SNS pin is approximately 3.3 V. However, if the voltage at DIAG_EN is above 3.3 V,
then the fault SNS voltage, V SNSFH, tracks that voltage up to 5 V. Tracking is done because the GPIO voltage
output that is powering the diagnostics through DIAG_EN is close to the maximum acceptable ADC voltage
within the same microcontroller. Therefore, the sense resistor value, R SNS, can be chosen to maximize the
range of currents needed to be measured by the system. The R SNS value must be chosen based on application
need. The maximum usable R SNS value is bounded by the ADC minimum acceptable voltage, V ADC,min, for the
smallest load current needed to be measured by the system, I LOAD,min . The minimum acceptable R SNS value has
to ensure the V SNS voltage is below the V SNSFH value so that the system can determine faults. This difference
between the maximum readable current through the SNS pin, I LOAD,max × R SNS, and the V SNSFH is called the
headroom voltage, V HR . The headroom voltage is determined by the system but is important so that there is a
difference between the maximum readable current and a fault condition. Therefore, the minimum R SNS value has
to be the V SNSFH minus the V HR times the sense current ratio, K SNS divided by the maximum load current the
system must measure, I LOAD,max . Use the following equation to see the boundary equation.


(V SNSFH – V HR ) × K SNS / I LOAD,max ≤ R SNS ≤ V ADC,min × K SNS / I LOAD,min (1)


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



Current Sense

Voltage

ADC Full Scale Range, V ADC,max


Max Measurable Current


Max Nominal Current


Open Load Current, V ADC,min





|V|Col2|Col3|Col4|
|---|---|---|---|
|VSNSFH|VSNSFH|VSNSFH|VSNSFH|
|Headroom, VHR|Headroom, VHR|Headroom, VHR||
|Over Current|Over Current|Over Current||
|Normal<br>1<br>RSNS|Normal<br>1<br>RSNS|||
|||||


Sense Current



**Figure 8-1. Voltage Indication on the Current-Sense Pin**


The maximum current the system wants to read, I LOAD,max, must be below the current-limit threshold because
after the current-limit threshold is tripped the V SNS value goes to V SNSFH . Additionally, currents being measured
can be up to the maximum ILIM value but the current sense output accuracy is not specified above the maximum
rated value in the Current Sense Characteristics.


VBAT


|Col1|Col2|
|---|---|
|V|B|

















**Figure 8-2. Current-Sense and Current-Limit Block Diagram**


Because this scheme adapts based on the voltage coming in from the MCU, there is no need to have a Zener
diode on the SNS pin to protect from high voltages.


**8.3.2 Programmable Current Limit**


A high-accuracy current limit allows higher reliability, which protects the power supply during short circuit or
power up. Also, a high-accuracy current limit can save system costs by reducing PCB traces, connector size,
and the capacity of the preceding power stage.


Current limit offers protection from over-stressing to the load and integrated power FET. Current limit holds the
current at the set value, and pulls up the SNS pin to V SNSFH and asserts the FAULT pin as diagnostic reports.
The three current-limit thresholds are:


 - External programmable current limit -- An external resistor, R ILIM is used to set the channel current limit.
When the current through the device exceeds I LIM_REG (current limit threshold), a closed loop steps in
immediately. V GS voltage regulates accordingly, leading to the V DS voltage regulation. When the closed loop
is set up, the current is clamped at the set value. The external programmable current limit provides the
capability to set the current-limit value by application.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 15


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


Additionally this value can be dynamically changed by changing the resistance on the ILIM pin. This can be
seen in the Applications Section.

 - Internal current limit: I LIM pin shorted to ground -- If the external current limit is out of range on the lower
end or the I LIM pin is shorted to ground, the internal current limit is fixed. To use the internal current limit for
large-current applications, tie the I LIM pin directly to the device GND.

 - Internal current limit: I LIM_REG pin open -- If the external resistor is out of range on the higher end or the ILIM
pin is open, the current limit reverts to half the nominal current limit range. This level is still above the nominal
operation for the device to operate in DC steady state but is low enough that if a pin fault occurs and the R ILIM
opens up, the current does not default to the highest rating and put additional stress on the power supply.


Both the internal current limit (I lim,nom ) and external programmable current limit are always active when V S is
powered and EN is high. The lower value one (of I LIM and the external programmable current limit) is applied as
the actual current limit. The typical deglitch time for the current limit to assert is 2.5 µs.


Note that if a GND network is used (which leads to the level shift between the device GND and board GND), the
ILIM pin must be connected with device GND. Calculate R LIM with Equation 2.


R LIM_REG = K CL / I LIM_REG (2)


For better protection from a hard short-to-GND condition (when V S and input are high and a short to GND
happens suddenly), an open-loop fast-response behavior is set to turn off the channel, before the current-limit
closed loop is set up. With this fast response, the device can achieve better inrush-suppression performance.


For more information about the current limiting feature, see _Section 8.3.5.1_ .


_**8.3.2.1 Capacitive Charging**_


Figure 8-3 shows the typical set up for a capacitive load application and the internal blocks that function when
the device is used. Note that all capacitive loads have an associated "load" in parallel with the capacitor that is
described as a resistive load but in reality it can be inductive or resistive.


VBAT











R ILIM





**Figure 8-3. Capacitive Charging Circuit**


The first thing to check is that the nominal DC current, I NOM, is acceptable for the TPS1HTC30-Q1 device.
This can easily be done by taking the R θJA from the Thermal Information and multiplying the R ON of the
TPS1HTC30-Q1 and the INOM with it, add the ambient temperature and if that value is below the thermal
shutdown value, then the device can operate with that load current. For an example of this calculation see the
Section 9.2.


The second key care about for this application is to make sure that the capacitive load can be charged up
completely without the device hitting thermal shutdown. This is because if the device hits thermal shutdown


16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



during the charging, the resistive nature of the load in parallel with the capacitor starts to discharge the capacitor
over the duration the TPS1HTC30-Q1 is off. Note that there are some applications with high enough load
impedance that the TPS1HTC30-Q1 hitting thermal shutdown and trying again is acceptable; however, for the
majority of applications the system must be designed so that the TPS1HTC30-Q1 does not hit thermal shutdown
while charging the capacitor.


With the current clamping feature of the TPS1HTC30-Q1, capacitors can be charged up at a lower inrush current
than other high current limit switches. This lower inrush current means that the capacitor takes a little longer to
charge all the way up.


For more information about capacitive charging with high side switches, see the _[How to Drive Resistive,](https://www.ti.com/lit/pdf/SLVAE30)_
_[Inductive, Capacitive, and Lighting Loads](https://www.ti.com/lit/pdf/SLVAE30)_ application note. This application note has information about the
thermal modeling available along with quick ways to estimate if a high side switch is able to charge a capacitor to
a given voltage.


**8.3.3 Inductive-Load Switching-Off Clamp**


When an inductive load is switching off, the output voltage is pulled down to negative, due to the inductance
characteristics. The power FET can break down if the voltage is not clamped during the current decay period. To
protect the power FET in this situation, an internal drain to gate clamp, namely the V DS,clamp is used to clamp the
voltage between the drain and source of the device.


9 DS,clamp 9 BAT ± 9 OUT (3)


During the current-decay period (T DECAY ), the power FET is turned on for inductive energy dissipation. Both the
energy of the power supply (E BAT ) and the load (E LOAD ) are dissipated on the high-side power switch itself, which
is called E HSD . If resistance is in series with inductance, some of the load energy is dissipated in the resistance.


( HSD ( BAT � ( LOAD ( BAT � ( L ± ( R (4)


From the high-side power switch view, E HSD equals the integration value during the current decay period.


T DECAY
### E HSD ³ 0 V DS,clamp u I OUT (t)dt (5)



u ln §¨¨© R u I OUT( V MAXOUT) � V OUT - ¸¸¹ (6)






|RuI <br>OUT(MAX)|Col2|Col3|V<br>OUT|
|---|---|---|---|
||OUT<br>V|||



u V BAT R� 2 V OUT u ª««¬5 u, OUT(MAX) ± 9 OUT OQ §¨¨© R u I OUT( V MAXOUT) � V OUT - ¸¸¹º»»¼ (7)



( HSD / u V BAT R� 2 V OUT u ««5 u, OUT(MAX) ± 9 OUT OQ §¨¨ R u I OUT( V MAX) � V



HSD / u BAT R 2 OUT u ««5 u, OUT(MAX) ± 9 OUT OQ ¨¨© OUT( V MAXOUT) OUT


|RuI <br>OUT(MAX)|Col2|Col3|V<br>OUT|
|---|---|---|---|
||OUT<br>V|||



When R approximately equals 0, E HSD can be given simply as:


1 2 V BAT � V OUT
E HSD 2 u L u I OUT(MAX) R 2 (8)


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 17


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


VS







INPUT


VOUT


IOUT



**Figure 8-4. Driving Inductive Load**


|Col1|Col2|Col3|
|---|---|---|
||||
|VIN(BAT)|||
||||
|||VDS, clamp<br>EHSD|
||||
||||
||||



t DECAY


**Figure 8-5. Inductive-Load Switching-Off Diagram**


As discussed previously, when switching off, battery energy and load energy are dissipated on the high-side
power switch, which leads to the large thermal variation. For each high-side power switch, the upper limit of
the maximum safe power dissipation depends on the device intrinsic capacity, ambient temperature, and board
dissipation condition.


**8.3.4 Inductive Load Demagnetization**


When switching off an inductive load, the inductor can impose a negative voltage on the output of the switch.
The TPS1HTC30 includes voltage clamps between VS and VOUT to limit the voltage across the FETs and
demagnetize load inductance if there is any. The negative voltage applied at the OUT pin drives the discharge of
inductor current. Figure 8-6 shows the device discharging a 400-mH load.


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



**Figure 8-6. TPS1HTC30 Inductive Discharge (400 mH)**


The maximum acceptable load inductance is a function of the energy dissipated in the device and therefore the
load current and the inductive load. The maximum energy and the load inductance the device can withstand for
one pulse inductive dissipation at 125°C is shown in Figure 8-7. The device can withstand 50% of this energy
for one million inductive repetitive pulses with a >4-Hz repetitive pulse. If the application parameters exceed this
device limit, use a protection device like a freewheeling diode to dissipate the energy stored in the inductor.



1500

1300

1200

1100

1000

900

800

700

600

500

400

300

200

100

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|VS|= 3|6 V|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||



1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16



Current (A)


**Figure 8-7. TPS1HTC30 Inductive Load Discharge Energy Capability at 125°C**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 19


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**8.3.5 Full Protections and Diagnostics**


Current Sensing is active when DIAG_EN enabled. When DIAG_EN is low, current sense is disabled. The SNS
output is in high-impedance mode.

**Table 8-1. DIAG_EN Logic Table**





|DIAG_EN|EN Condition|Protections and Diagnostics|
|---|---|---|
|HIGH|HIGH|See Fault Table|
|HIGH|LOW|LOW|
|LOW|HIGH|Diagnostics disabled,~~FAULT~~and SNS<br>output set to high impedance. Protection<br>is normal.|
|LOW|LOW|LOW|


**Table 8-2. DIAG_EN=HIGH Status Table**





















|Conditions|EN|VOUT|FAULT|SNS|Behavior|Recovery|
|---|---|---|---|---|---|---|
|Normal|L|L|Hi-Z|0|Normal||
|Normal|H|H|Hi-Z|ILoad/ KSNS|Normal||
|Overcurrent|H|VS -<br>ILIM*RLOA<br>D|L|VSNSFH|Holds the current at the current<br>limit until thermal shutdown||
|Overvoltage|H|H →L|L|VSNSFH|Channel turns off if VS > VS,OVPR, <br>turns back on if VS < VS,OVPRF||
|STG, Relative<br>Thermal Shutdown,<br>Absolute Thermal<br>Shutdown|H|H→L|L|VSNSFH|Shuts down when devices hits<br>relative or absolute thermal<br>shutdown|Auto retries when<br>THYS is met and time<br>has been longer than<br>tRETRY amount of time|
|Open load|H|H|Hi-Z|ILoad / KSNS =<br>approximately 0|Normal behavior, user can judge<br>if it is an open load or not||
|Open load|L|H|L|VSNSFH|Internal pullup resistor is active. If<br>VS – VOUT < VOL then fault active|Clears when fault<br>goes away|
|Reverse Polarity|x|x|x|x|Channel turns on to lower power<br>dissipation. Current into ground<br>pin is limited by external ground<br>network||


_**8.3.5.1 Short-Circuit and Overload Protection**_



TPS1HTC30-Q1 provides output short-circuit protection to make sure that the device prevents current flow in the
event of a low impedance path to GND, removing the risk of damage or significant supply droop. The device
is specified to protect against short-circuit events regardless of the state of the ILIM pins and with up to 60-V
supply at 125°C.


Figure 8-8 shows the behavior of TPS1HTC30-Q1 when a short-circuit occurs and the device is in the on-state
and already outputting current. When the internal pass FET is fully enabled, the current clamping settling time is
slower so to make sure overshoot is limited, the device implements a fast trip level at a level I OVCR . When this
fast trip threshold is hit, the device immediately shuts off for a short period of time before quickly re-enabling and
clamping the current to I CL level after a brief transient overshoot to the higher peak current (I CL_ENPS ) level. The
device then keeps the current clamped at the regulation current limit until the thermal shutdown temperature is
hit and the device safely shuts off.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



Current (A)


I OVCR


I CL_ENPS


I CL

|Col1|Col2|Col3|
|---|---|---|
||||
||Thermal Shutdown|tRETRY|



**Figure 8-8. On-State Short-Circuit Behavior**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)


Time (s)



Overload Behavior shows the behavior of the TPS1HTC30-Q1 when there is a small change in impedance that
sends the load current above the I CL threshold. The current rises to I CL_LINPK above the regulation level. Then
the current limit regulation loop kicks in and the current drops to the I CL value.


Current (A)


I CL_ENPS


I CL_LINPK


I CL


I NOM


Time (s)

|Col1|Col2|
|---|---|
|||
|Thermal Shutdown|tRETRY<br>|



**Figure 8-9. Overload Behavior**


In all of these cases, the internal thermal shutdown is safe to hit repetitively. There is no device risk or lifetime
reliability concerns from repeatedly hitting this thermal shutdown level.


_**8.3.5.2 Open-Load Detection**_


When the main channel is enabled faults are diagnosed by reading the voltage on the SNS pin and judged by
the user.


In the off state, if a load is connected, the output voltage is pulled to 0V. In the case of an open load, the output
voltage is close to the supply voltage, V S – V OUT < V ol,off . The FLT pin goes low to indicate the fault to the MCU,
and the SNS pin is pulled up to V SNSFH . There is always a leakage current I ol,off present on the output, due to the
internal logic control path or external humidity, corrosion, and so forth. Thus, TI implemented an internal pullup
resistor to offset the leakage current. This pullup current must be less than the output load current to avoid false
detection in the normal operation mode. To reduce the standby current, TI implimented a switch in series with the
pullup resistor controlled by the DIAG_EN pin. The pull up resistor value is R pu = 150 kΩ.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 21


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


VS

















**Figure 8-10. Open-Load Detection Circuit**


_**8.3.5.3 Thermal Protection Behavior**_


The thermal protection behavior can be split up into three categories of events that can happen. Figure 8-11
shows each of these categories.


1. **Relative thermal shutdown** : The device is enabled into an overcurrent event. The DIAG_EN pin is high so
that diagnostics can be monitored on SNS and FLT (however, DIAG_EN being high is not necessary for all
protection features to function). The output current rises up to the I ILIM level and the FLT goes low while the
SNS goes to V SNSFH . With this large amount of current going through, the junction temperature of the FET
increases rapidly with respect to the controller temperature. When the power FET temperature rises T REL
amount above the controller junction temperature ΔT = T FET – T CON   - T REL, the device shuts down. The
faults are continually shown on SNS and FLT and the part waits for the t RETRY timer to expire. When t RETRY
timer expires, because the LATCH pin is low and EN is still high, the device comes back on into this I ILIM
condition.
2. **Absolute thermal shutdown** : The device is still enabled in an overcurrent event with DIAG_EN high and
LATCH still low. However, in this case the junction temperature rises up and hits an absolute reference
temperature, T ABS, and then shuts down. The device does not recover until both T J < T ABS – T hys and the
t RETRY timer has expired.
3. **Latch-off mode** : The device is enabled into an overcurrent event. The DIAG_EN pin is high so that
diagnostics can be monitored on SNS and FLT. The output current rises up to the I ILIM level and the FLT
goes low while the SNS goes to V SNSFH . If the part shuts down due to a thermal fault, either relative thermal
shutdown or absolute thermal shutdown, the device does not enable the channel until either the LATCH pin
OR the EN pin is toggled.


22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


DIAG_EN


Junction

Temperature



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



|_EN|1 2 3|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_EN|**1**<br>**2**<br>**3**||||||||||||||||||||||
|CH|||||||||||||||||||||||
|CH|||||||||||||||||||||||
|EN|||||||||||||||||||||||
|EN|||||||||||||||||||||||
|tion<br>ure<br>ABS|||||||||TABS||||||||tRETRY|||tRETRY|||
|tion<br>ure<br>ABS|||||||THYS||||||||||||||||
|tion<br>ure<br>ABS|||||||||tRETRY|||tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|
|tion<br>ure<br>ABS|TREL|TREL|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|tRETRY|
|tion<br>ure<br>ABS|TREL|TREL|||||||||||||||||||||
|tput<br>rent|||||||||||||||||||||||
|tput<br>rent|||ILIM||||||||||||||||||||
|SNS|||VSNSFH||||||||||||||||||||
|SNS|||||||||||||||||||||||
|FLT|||||||||||||||||||||||
|FLT|||||||||||||||||||||||
||||||||||||||||||||||||


**Figure 8-11. Thermal Behavior**









_**8.3.5.4 Overvoltage (OVP) Protection**_


The device monitors the supply voltage V S to prevent unpredicted behaviors in the event that the supply voltage
is too high. When the supply increases beyond V S,OVPR, the output stage is shut down automatically. When the
supply falls below V S,OVPF, the device turns on. The TPS1HTC30-Q1 integrates a deglitcher to avoid immediate
output shutoff from OVP due to short transient events brought about by inductive load oscillations.


_**8.3.5.5 UVLO Protection**_


The device monitors the supply voltage V S to prevent unpredicted behaviors in the event that the supply voltage
is too low. When the supply voltage falls down to V UVLOF, the output stage is shut down automatically. When
the supply rises up to V UVLOR, the device turns on. If an overcurrent event trips the UVLO threshold, the device
shuts off and comes back on into a current limit normally.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 23


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


_**8.3.5.6 Reverse Polarity Protection**_


**Method 1:** Blocking diode connected with V S . Both the device and load are protected when in reverse polarity.





|B<br>5<br>MCU UT<br>d|Col2|
|---|---|
|MCU|MCU|
|MCU||
|||


**Figure 8-12. Reverse Protection With Blocking Diode**



**Method 2 (GND network protection):** Only the high-side device is protected under this connection. The
load reverse loop is limited by the load itself. Note when reverse polarity happens, the continuous reverse
current through the power FET must be less than I rev . Of the three types of ground pin networks, TI strongly
recommends type 3 (the resistor and diode in parallel). No matter what types of connection are between the
device GND and the board GND, if a GND voltage shift happens, make sure the following proper connections for
the normal operation:


 - TI recommends to leave floating.

 - Connect the current limit programmable resistor to the device GND.


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)










|VBAT 2<br>T = R × R<br>B<br>5<br>MCU UT<br>d<br>RGND D<br>GND|Col2|
|---|---|
|MCU|MCU|
|MCU||
|||



**Figure 8-13. Reverse Protection With GND Network**


 - **Type 1 (resistor):** The higher resistor value contributes to a better current limit effect during the reverse
battery event or negative ISO pulses. However, the higher resistor leads to higher GND shift during normal
operation mode. Also, consider the resistor power dissipation.



R GND d V GNDshift
I nom



� ±9 CC �
� ±, GND �



(9)


(10)



� ±9

R GND t
±,



CC
GND t

� ±, GND



where


– V GNDshift is the maximum value for the GND shift, determined by the HSS and microcontroller. TI suggests
a value ≤ 0.6 V.

– I nom is the nominal operating current.
– –V CC is the maximum reverse voltage seen on the battery line.
– –I GND is the maximum reverse current the ground pin can withstand, which is available in the _Absolute_
_Maximum Ratings_ .


If multiple high-side power switches are used, the resistor can be shared among devices.

 - **Type 2 (diode):** A diode is needed to block the reverse voltage, which also brings a ground shift (≈ 600 mV).
However, an inductive load is not acceptable to avoid an abnormal status when switching off.

 - **Type 3 (resistor and diode in parallel (recommended)):** A peak negative spike can occur when the
inductive load is switching off, which can damage the HSD or the diode. So, TI recommends a resistor
in parallel with the diode when driving an inductive load. The recommended selection are 1-kΩ resistor in
parallel with an I F   - 100-mA diode. If multiple high-side switches are used, the resistor and diode can be
shared among devices.


_**8.3.5.7 Protection for MCU I/Os**_


In many conditions, such as the negative ISO pulse, or the loss of battery with an inductive load, a negative
potential on the device GND pin can damage the MCU I/O pins [more likely, the internal circuitry connected to
the pins]. Therefore, the serial resistors between MCU and HSS are required.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 25


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


Also, for proper protection against loss of GND, TI recommends 5 kΩ resistance for the RPROT resistors.
















|5 V|Col2|
|---|---|
|||
|||
|||
|||


|Smart High Side Switch<br>5 k EN VBB<br>5 V<br>5 k<br>FLT<br>Reverse FET<br>5 k<br>LATCH Turn On<br>5 k VOUT<br>MCU DIAG_EN<br>5 k<br>SNS<br>Load<br>ILIM<br>GND<br>R GND D GND|Col2|Col3|
|---|---|---|
|MCU|MCU|MCU|
|MCU|||
|MCU|||
||||



**Figure 8-14. MCU IO Protections**


**8.3.6 Diagnostic Enable Function**


The diagnostic enable pin, DIAG_EN, offers multiplexing of the microcontroller diagnostic input for current sense
or digital status, by sharing the same sense resistor and ADC line or I/O port among multiple devices.


In addition, during the output-off period, the diagnostic disable function lowers the current consumption for
the standby condition. The three working modes in the device are normal mode, standby mode, and standby
mode with diagnostic. If off-state power saving is required in the system, the standby current is <500 nA with
DIAG_EN low. If the off-state diagnostic is required in the system, the typical standby current is around 1 mA
with DIAG_EN high.


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**8.4 Device Functional Modes**


**8.4.1 Working Mode**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



The three working modes in the device are normal mode, standby mode, and standby mode with diagnostic.
If an off-state power saving is required in the system, the standby current is less than 500 nA with EN and
DIAG_EN low. If an off-state diagnostic is required in the system, the typical standby current is around 1.2 mA
with DIAG_EN high. Note that to enter standby mode requires IN low and t > t STBY . t STBY is the standby-mode
deglitch time, which is used to avoid false triggering or interfere with PWM switching. Figure 8-15 shows a
work-mode state-machine state diagram.

















**Figure 8-15. Work-Mode State Machine**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 27


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**9 Application and Implementation**


**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**9.1 Application Information**


The following discussion notes how to implement the device in a typical application with recommended external
components.


**9.2 Typical Application**


Figure 9-1 shows an example of how to design the external circuitry parameters.





















**Figure 9-1. Typical Application Circuitry**


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**9.2.1 Design Requirements**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



|Component|Description|Purpose|
|---|---|---|
|TVS|SMBJ60CA (optional)|Filter voltage transients coming from battery (ISO7637-2)|
|CVS|220 nF (optional)|Better EMI performance|
|CIC|100 nF|Minimal amount of capacitance on input for EMI mitigation|
|CBULK|10 uF (optional)|There to hold the rail for the LDO; however, helps to filter voltage<br>transients on supply rail. Not a requirement.|
|RPROT|10k|Protection resistor for microcontroller and device I/O pins|
|RILIM|7k – 70k|Set current limit threshold|
|RSNS|1k|Translate the sense current into sense voltage.|
|CFILTER|100 nF|Coupled with RPROT on the SNS line creates a low pass filter to<br>filter out noise going into the ADC of the MCU|
|CVOUT|22 nF|Improves EMI performance, filtering of voltage transients|
|RGND|1 kΩ|Stabilize GND potential during turn-off of inductive load|
|DGND|MSX1PJ|Keeps GND close to system ground during normal operation|


**9.2.2 Detailed Design Procedure**


To keep maximum voltage on the SNS pin at an acceptable range for the system, use the following equation to
calculate the R SNS . To achieve better current sense accuracy. A 1% accuracy or better resistor is preferred.


(V SNSFH – V HR ) × K SNS / I LOAD,max ≤ R SNS ≤ V ADC,min × K SNS / I LOAD,min (11)


**Table 9-1. Typical Application**

|Parameter|Value|
|---|---|
|VDIAG_EN|5 V|
|ILOAD,max|6 A|
|ILOAD,min|20 mA|
|VADC,min|5 mV|
|VHR|1 V|



For this application, an RSNS value of approximately 1 kΩ can be chosen to satisfy the equation requirements.


(5 V – 1 V) × 1300 / 6 A ≤ ≅1 kΩ ≤ 5 mV × 1300 / 20 mA (12)


In other applications, more emphasis can be put on the lower end measurable values which increases RSNS.
Likewise, if the higher currents are of more interest the RSNS can be decreased.


Having the maximum SNS voltage scale with the DIAG_EN voltage removes the need for a Zener diode on the
SNS pin going to the ADC.


To set the programmable current limit value at 5 A, use the following equation to calculate the R LIM .


R LIM = K CL / I LIM = 100 / 5 = 20 kΩ (13)


TI recommends R PROT = 10 kΩ to ensure the current going into the digital pins (EN, DIAG_EN, LATCH) is
limited.


TI recommends a 1-kΩ resistor and 600-V, 0.2-A diode for the GND network.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 29


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


_**9.2.2.1 Dynamically Changing Current Limit**_


The current limit threshold can be changed dynamically by altering the resistance going from the current limit
pin to the ground of the device on the fly. This alteration allows the system to have a different current limit for
start-up, when there can be significant inrush current, and during normal operation. The way this is commonly
done is by putting two resistors in parallel on the ILIM pin and having a switch to enable or disable one of the
resistors. This set-up can be seen in Figure 9-2. Alternatively, a digital potentiometer can be used to adjust the
impedance on the ILIM pin on the fly. Care must be taken so that the capacitance on the ILIM pin is below
approximately 100 pF to keep the current regulation loop stable. The most common application where this
feature is useful is capacitive loads.


VBAT







I LIM2 =

















**Figure 9-2. Dynamic Changing Current Limit Setup**


In a capacitive charging case, the initial current to charge the capacitor is the inrush current. Depending on
the system requirements, dynamically changing the current limit can help either charge up a capacitor faster or
charge up a larger capacitor. To allow a higher inrush level of current through in the beginning, the switch can be
closed making the current limit be according to the equation below.


I LIM2 = K CL (R ILIM1 + R ILIM2 ) / (R ILIM1 × R ILIM2 ) (14)


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



When the inrush event is over and the output voltage is charged up, the switch opens and the current limit is just
the R ILIM1 equivalent level. This timing can be seen in Figure 9-3.


V OUT (V)


V BB

V BB               - V DS


Current (A)



I ILIM2


I ILIM1


I NOM






|Time (s)<br>t (A)<br>Voltage<br>Current<br>dt<br>Time (s)|Col2|
|---|---|
|||
|||
|t (A)||
|||
|||
|~~dt~~||
|||



t SW


**Figure 9-3. Capacitive Charging Changing Current Limit**


Alternatively, if the switch is open, the current limit starts out at a lower value and then the switch can be closed
when the capacitance gets charged up. This lower current limit level allows higher value capacitance to be
charged up. The timing diagram can be seen in Figure 9-4.


V OUT (V)


V BB

V BB               - V DS





Current (A)


I ILIM2


I NOM


I ILIM1







t SW


**Figure 9-4. Large Capacitive Charging Changing Current Limit**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 31


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


**9.2.3 Application Curves**


Figure 9-5 shows a test example of initial short-circuit inrush-current limit. Test conditions: V S = 36 V, input is
from low to high, load is short-to-GND, external current limit is 5 A.


Figure 9-6 shows a test example of a discharging a 400 mH inductor. Test conditions: V S = 24 V, input is high to
low, load is 400 mH.


**Figure 9-6. 400-mH Inductive Load Driving**


**Figure 9-5. Initial Short-to-GND Waveform**


**9.3 Power Supply Recommendations**


The device is qualified for both automotive and industrial applications. The normal power supply connection is a
24-V automotive system. The supply voltage must be within the range specified in the Recommended Operating
Conditions.


**Table 9-2. Voltage Operating Ranges**













|VS Voltage Range|Note|
|---|---|
|6 V to 10 V|Extended lower 24-V automotive battery operation such as cold crank and start-stop. Device<br>is fully functional and protected but some parametrics such as RON, current sense accuracy,<br>current limit accuracy and timing parameters can deviate from specifications. Check the<br>individual specifications in the Electrical Characteristics to confirm the voltage range it is<br>applicable for.|
|10 V to 32 V|Nominal 24-V automotive battery voltage range. All parametric specifications apply and the<br>device is fully functional and protected.|
|32 V to 60 V|Extended upper 24-V automotive battery operation such as double battery. Device is fully<br>functional and protected but some parametrics such as timing parameters can deviate from<br>specifications. Check the individual specifications in the Electrical Characteristics to confirm<br>the voltage range it is applicable for.|
|60 V|Load dump voltage. Device is operational and lets the pulse pass through without being<br>damaged and is fully protect against short circuits.|


**9.4 Layout**


**9.4.1 Layout Guidelines**


To prevent thermal shutdown, T J must be less than 150°C. If the output current is very high, the power
dissipation can be large. The HTSSOP package has good thermal impedance. However, the PCB layout is
very important. Good PCB design can optimize heat transfer, which is absolutely essential for the long-term
reliability of the device.


 - Maximize the copper coverage on the PCB to increase the thermal conductivity of the board. The major
heat-flow path from the package to the ambient is through the copper on the PCB. Maximum copper is


32 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



extremely important when there are not any heat sinks attached to the PCB on the other side of the board
opposite the package.

 - Add as many thermal vias as possible directly under the package ground pad to optimize the thermal
conductivity of the board.

 - Make sure all thermal vias are either be plated shut or plugged and capped on both sides of the board to
prevent solder voids. To make sure of reliability and performance, the solder coverage must be at least 85%.


**9.4.2 Layout Example**

_**9.4.2.1 Without a GND Network**_


Without a GND network, tie the thermal pad directly to the board GND copper for better thermal performance.
























|Col1|FAULT|Col3|Col4|
|---|---|---|---|
||FAULT|||


















|Col1|1 14<br>2 13<br>3 12<br>Thermal<br>4 11<br>Pad<br>5 10<br>6 9<br>7 8|Col3|
|---|---|---|
||||



**Figure 9-7. Layout Without a GND Network**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 33


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**
[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4) **[www.ti.com](https://www.ti.com)**


_**9.4.2.2 With a GND Network**_


With a GND network, tie the thermal pad with a single trace through the GND network to the board GND copper.
















|Col1|RGND<br>DGND|Col3|Col4|Col5|Col6|Col7|Col8|S_IC CVS|Col10|
|---|---|---|---|---|---|---|---|---|---|
||RGND<br>DGND|RGND<br>DGND|RGND<br>DGND|||CV|CV|CV|CV|
||RGND<br>DGND|RGND<br>DGND|G|G||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||



**Figure 9-8. Layout With a GND Network**


_**9.4.2.3 Thermal Considerations**_


This device possesses thermal shutdown (TABS) circuitry as a protection from overheating. For continuous
normal operation, the junction temperature must not exceed the thermal-shutdown trip point. If the junction
temperature exceeds the thermal-shutdown trip point, the output turns off. When the junction temperature falls
below the thermal-shutdown trip point, the output turns on again.


Calculate the power dissipated by the device according to Equation 15.


P T = I OUT [2] × R DSON + V S × I NOM (15)


where


 - P T = Total power dissipation of the device


After determining the power dissipated by the device, calculate the junction temperature from the ambient
temperature and the device thermal impedance.


T J = T A + R θJA × P T (16)


For more information, please see _[How to Drive Resistive, Inductive, Capacitive, and Lighting Loads](https://www.ti.com/lit/pdf/SLVAE30)_ application
note.


34 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


**[www.ti.com](https://www.ti.com)**


**10 Device and Documentation Support**
**10.1 Documentation Support**


**10.1.1 Related Documentation**



**[TPS1HTC30-Q1](https://www.ti.com/product/TPS1HTC30-Q1)**

[SLVSGL4 – SEPTEMBER 2023](https://www.ti.com/lit/pdf/SLVSGL4)



Texas Instruments, _[How to Drive Resistive, Inductive, Capacitive, and Lighting Loads](https://www.ti.com/lit/pdf/SLVAE30)_ application note


**10.2 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Subscribe to updates_ to register and receive a weekly digest of any product information that has changed. For
change details, review the revision history included in any revised document.


**10.3 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**10.4 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

**10.5 Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**10.6 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**11 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSGL4&partnum=TPS1HTC30-Q1)_ 35


Product Folder Links: _[TPS1HTC30-Q1](https://www.ti.com/product/tps1htc30-q1?qgpn=tps1htc30-q1)_


###### **PACKAGE OPTION ADDENDUM**

www.ti.com 23-May-2025


**PACKAGING INFORMATION**





















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
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 1


##### **GENERIC PACKAGE VIEW**

#### **PWP 14 PowerPAD TSSOP - 1.2 mm max height**

**4.4 x 5.0, 0.65 mm pitch** PLASTIC SMALL OUTLINE


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4224995/A


www.ti.com


##### **PACKAGE OUTLINE**

#### PWP0014J SCALE 2.400 PowerPAD   TSSOP - 1.2 mm max hei TM ght

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


##### **EXAMPLE BOARD LAYOUT**

#### PWP0014J PowerPAD   TSSOP - 1.2 mm max hei TM ght

PLASTIC SMALL OUTLINE





























NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
8. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
numbers SLMA002 (www.ti.com/lit/slma002) and SLMA004 (www.ti.com/lit/slma004).
9. Size of metal pad may vary due to creepage requirement.


www.ti.com


##### **EXAMPLE STENCIL DESIGN**

#### PWP0014J PowerPAD   TSSOP - 1.2 mm max hei TM ght

PLASTIC SMALL OUTLINE




















|STENCIL<br>THICKNESS|SOLDER STENCIL<br>OPENING|
|---|---|
|0.1|3.29 X 3.73|
|0.125|2.94 X 3.34 (SHOWN)|
|0.15|2.69 X 3.05|
|0.175|2.49 X 2.82|





NOTES: (continued)

10. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
11. Board assembly site may have different recommendations for stencil design.


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


