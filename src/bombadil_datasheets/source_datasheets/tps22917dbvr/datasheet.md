**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)

## **TPS22917x 1 V–5.5-V, 2-A, 80-mΩ Ultra-Low Leakage Load Switch**



**1 Features**


- Input operating voltage range (V IN ): 1 V to 5.5 V

- Maximum continuous current (I MAX ): 2 A

- On-resistance (R ON ):
– 5 V IN = 80 mΩ (typical)
– 1.8 V IN = 120 mΩ (typical)
– 1 V IN = 220 mΩ (typical)

- Ultra-low power consumption:

–
ON state (I Q ): 0.5 µA (typical)
– OFF state (I SD ): 10 nA (typical)

- Smart ON pin pulldown (R PD ):
– ON ≥ VIH (I ON ): 10 nA (maximum)
– ON ≤ VIL (R PD ): 750 kΩ (typical)

- Adjustable turn ON limits inrush current (t ON ):
– 5-V t ON = 100 μs at 72 mV/μs (C T = open)
– 5-V t ON = 4000 μs at 2.3 mV/μs (C T = 1000 pF)

- Adjustable output discharge and fall time:

–
Optional QOD resistance ≥ 150 Ω (internal)

- Always-ON true Reverse Current Blocking (RCB):
– Activation current (I RCB ): –500 mA (typical)

–
Reverse leakage (I IN,RCB ): –1 µA (maximum)


**2 Applications**


- Industrial systems

- Set top box

- Blood glucose meters

- Electronic point of sale



**3 Description**


The TPS22917x device is a small, single channel load
switch using a low leakage P-Channel MOSFET for
minimum power loss. Advanced gate control design
supports operating voltages as low as 1 V with
minimal increase in ON-Resistance and power loss.


The Rise and Fall times can be independently
adjusted with external components for system level
optimizations. The timing capacitor (C T ) and turn
on time can be adjusted to manage inrush current
without adding unnecessary system delays. The
output discharge resistance (QOD) can be used to
adjust the output fall time. Connect the QOD pin
directly to the output for a fastest fall time or leave
it open for the slowest fall time.


The switch ON state is controlled by a digital input
that can interface directly with low-voltage control
signals. The TPS22917 uses active high enable logic,
while the TPS22917L uses active low. When power is
first applied, a Smart Pulldown is used to keep the ON
pin from floating until system sequencing is complete.
After the ON pin is deliberately driven high (≥V IH ),
the Smart Pulldown (R PD ) is disconnected to prevent
unnecessary power loss.


The TPS22917x device is available in a leaded
SOT-23 package (DBV) which allows visual inspection
of solder joints. The device is characterized for
operation over a temperature range of –40°C to
125°C.


**Device Information** [(1) ]

|PART NUMBER|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|TPS22917x|SOT-23 (6)|2.90 mm × 1.60 mm|



(1) For all available packages, see the orderable addendum at
the end of the data sheet.



R L

















Copyright © 2018, Texas Instruments Incorporated


**Simplified Schematic**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Revision History** .............................................................. 2
**5 Device Comparison Table** ...............................................3
**6 Pin Configuration and Functions** ...................................4
**7 Specifications** .................................................................. 5

7.1 Absolute Maximum Ratings........................................ 5
7.2 ESD Ratings............................................................... 5
7.3 Recommended Operating Conditions.........................5
7.4 Thermal Information....................................................5

7.5 Electrical Characteristics.............................................6
7.6 Switching Characteristics............................................7
7.7 Typical Characteristics................................................ 8
**8 Parameter Measurement Information** .......................... 13

8.1 Test Circuit and Timing Waveforms Diagrams.......... 13
**9 Detailed Description** ......................................................14

9.1 Overview................................................................... 14

9.2 Functional Block Diagram......................................... 14



9.3 Feature Description...................................................15
9.4 Full-Time Reverse Current Blocking......................... 16
9.5 Device Functional Modes..........................................16

**10 Application and Implementation** ................................ 17

10.1 Application Information........................................... 17
10.2 Typical Application.................................................. 17
**11 Power Supply Recommendations** ..............................19
**12 Layout** ...........................................................................20

12.1 Layout Guidelines................................................... 20
12.2 Layout Example...................................................... 20
12.3 Thermal Considerations..........................................20
**13 Device and Documentation Support** ..........................21

13.1 Receiving Notification of Documentation Updates..21
13.2 Support Resources................................................. 21
13.3 Trademarks............................................................. 21
13.4 Electrostatic Discharge Caution..............................21
13.5 Glossary..................................................................21
**14 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 21



**4 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision A (February 2018) to Revision B (December 2021)** **Page**

 - Updated the numbering format for tables, figures, and cross-references throughout the document..................1

 - Added TPS22917L orderable to the data sheet................................................................................................. 1


**Changes from Revision * (September 2017) to Revision A (February 2018)** **Page**

 - Changed product status from Advanced Information to Production Data ..........................................................1


2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**5 Device Comparison Table**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



|Device|ON Pin Logic|
|---|---|
|TPS22917|Active High|
|TPS22917L|Active Low|


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 3


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**6 Pin Configuration and Functions**

|Col1|Col2|1 6<br>2 5<br>3 4|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||



**Figure 6-1. DBV Package 6-Pin SOT-23 Top View**


**Table 6-1. Pin Functions**







|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**NO.**|**NAME**|**NAME**|**NAME**|
|1|VIN|I|Switch input|
|2|GND|—|Device ground|
|3|ON|I|Active high switch control input. Do not leave floating.|
|4|CT|O|Switch slew rate control. Connect capacitor from this pin to VIN to increase output slew<br>rate and turn-on time. Can be left floating for fastest timing.|
|5|QOD|O|Quick Output Discharge pin. This functionality can be enabled in one of three ways.<br>•<br>Placing an external resistor between VOUT and QOD<br>•<br>Tying QOD directly to VOUT and using the internal resistor value (RPD)<br>•<br>Disabling QOD by leaving pin floating<br>See the_Fall Time (tFALL) and Quick Output Discharge (QOD)_ section for more<br>information.|
|6|VOUT|O|Switch output|


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**7 Specifications**
**7.1 Absolute Maximum Ratings**


Over operating free-air temperature range (unless otherwise noted) [(1)]



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



|Col1|MIN MAX|UNIT|
|---|---|---|
|VIN<br>Input voltage|–0.3<br>6|V|
|VOUT<br>Output voltage|–0.3<br>6|V|
|VON<br>Enable voltage|–0.3<br>6|V|
|VQOD<br>QOD pin voltage|–0.3<br>6|V|
|IMAX<br>Maximum continuous switch current|2|A|
|IPLS<br>Maximum pulsed switch current, pulse < 300-µs, 2% duty cycle|2.5|A|
|TJ,MAX<br>Maximum junction temperature|125|°C|
|TSTG<br>Storage temperature|–65<br>150|°C|
|TLEAD<br>Maximum Lead temperature (10-s soldering time)|300|°C|


(1) Stresses beyond those listed under _Absolute Maximum Ratings_ may cause permanent damage to the device. These are stress
ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under
_Recommended Operating Conditions_ . Exposure to absolute-maximum-rated conditions for extended periods may affect device
reliability.


**7.2 ESD Ratings**






|Col1|Col2|VALUE|UNIT|
|---|---|---|---|
|V(ESD)<br>Electrostatic discharge|Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1)|±2000|V|
|V(ESD)<br>Electrostatic discharge|Charged-device model (CDM), per JEDEC specification JESD22-<br>C101(2)|±500|±500|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. Manufacturing with
less than 500-V HBM is possible with the necessary precautions. Pins listed as ±2000 V may actually have higher performance.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. Manufacturing with
less than 250-V CDM is possible with the necessary precautions. Pins listed as ±500 V may actually have higher performance.


**7.3 Recommended Operating Conditions**


Over operating free-air temperature range (unless otherwise noted)

|Col1|MIN MAX|UNIT|
|---|---|---|
|VIN<br>Input voltage|1<br>5.5|V|
|VOUT<br>Output voltage|0<br>5.5|V|
|VIH<br>High-level input voltage, ON|1<br>5.5|V|
|VIL<br>Low-level input voltage, ON|0<br>0.35|V|
|VQOD<br>QOD Pin Voltage|0<br>5.5|V|
|VCT<br>Timing Capacitor Voltage Rating|7|V|



**7.4 Thermal Information**







|Thermal Parameters(1)|TPS22917|UNIT|
|---|---|---|
|**Thermal Parameters**(1)|**DBV (SOT-23)**|**DBV (SOT-23)**|
|**Thermal Parameters**(1)|**6 PINS**|**6 PINS**|
|θJA<br>Junction-to-ambient thermal resistance|183|°C/W|
|θJCtop<br>Junction-to-case (top) thermal resistance|152|°C/W|
|θJB<br>Junction-to-board thermal resistance|34|°C/W|
|ψJT<br>Junction-to-top characterization parameter|37|°C/W|
|ψJB<br>Junction-to-board characterization parameter|33|°C/W|


(1) For more information about traditional and new thermal metrics, see the _[Semiconductor and IC Package Thermal Metrics](https://www.ti.com/lit/pdf/spra953)_ application
report.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 5


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics**

Unless otherwise noted, the specification in the following table applies for all variants over the entire recommended power
supply voltage range of 1 V to 5.5 V. Typical Values are at 25°C.















|PARAMETER|Col2|TEST CONDITIONS|Col4|TJ|MIN TYP MAX|UNIT|
|---|---|---|---|---|---|---|
|**INPUT SUPPLY(VIN)**|**INPUT SUPPLY(VIN)**|**INPUT SUPPLY(VIN)**|**INPUT SUPPLY(VIN)**|**INPUT SUPPLY(VIN)**|**INPUT SUPPLY(VIN)**|**INPUT SUPPLY(VIN)**|
|IQ,VIN|VIN Quiescent current|Enabled, VOUT = Open|Enabled, VOUT = Open|–40°C to +85°C|0.5<br>1.0|µA|
|IQ,VIN|VIN Quiescent current|Enabled, VOUT = Open|Enabled, VOUT = Open|–40°C to +125°C|1.2|µA|
|ISD,VIN|VIN Shutdown current|Disabled, VOUT = GND (TPS22917)|Disabled, VOUT = GND (TPS22917)|–40°C to +85°C|<br>10<br>100|nA|
|ISD,VIN|VIN Shutdown current|Disabled, VOUT = GND (TPS22917)|Disabled, VOUT = GND (TPS22917)|–40°C to +105°C|<br>250|nA|
|ISD,VIN|VIN Shutdown current|Disabled, VOUT = GND (TPS22917L)|Disabled, VOUT = GND (TPS22917L)|–40°C to +85°C|<br>175<br>300|nA|
|ISD,VIN|VIN Shutdown current|Disabled, VOUT = GND (TPS22917L)|Disabled, VOUT = GND (TPS22917L)|–40°C to +105°C|<br>400|nA|
|**ON-RESISTANCE(RON)**|**ON-RESISTANCE(RON)**|**ON-RESISTANCE(RON)**|**ON-RESISTANCE(RON)**|**ON-RESISTANCE(RON)**|**ON-RESISTANCE(RON)**|**ON-RESISTANCE(RON)**|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 5 V|25°C|80<br>100|mΩ|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 5 V|–40°C to +85°C|120|120|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 5 V|–40°C to +105°C|130|130|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 5 V|–40°C to +125°C|140|140|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 3.6 V|25°C|90<br>110|90<br>110|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 3.6 V|–40°C to +85°C|140|140|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 3.6 V|–40°C to +105°C|150|150|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 3.6 V|–40°C to +125°C|160|160|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.8 V|25°C|120<br>150|120<br>150|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.8 V|–40°C to +85°C|175|175|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.8 V|–40°C to +105°C|185|185|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.8 V|–40°C to +125°C|200|200|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.2 V|25°C|170<br>220|170<br>220|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.2 V|–40°C to +85°C|265|265|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.2 V|–40°C to +105°C|280|280|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.2 V|–40°C to +125°C|300|300|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.0 V|25°C|220<br>300|220<br>300|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.0 V|–40°C to +85°C|<br> <br>350|<br> <br>350|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.0 V|–40°C to +105°C|<br> <br>370|<br> <br>370|
|RON|ON-Resistance|IOUT = 200 mA|VIN = 1.0 V|–40°C to +125°C|390|390|
|**ENABLE PIN(ON)**|**ENABLE PIN(ON)**|**ENABLE PIN(ON)**|**ENABLE PIN(ON)**|**ENABLE PIN(ON)**|**ENABLE PIN(ON)**|**ENABLE PIN(ON)**|
|ION|ON Pin leakage|Enabled (TPS22917)|Enabled (TPS22917)|–40°C to +125°C|–10<br>10|nA|
|ION|ON Pin leakage|Enabled (TPS22917L)|Enabled (TPS22917L)|–40°C to +125°C|–20<br>20|nA|
|RPD|Smart Pull Down Resistance|VON ≤ VIL|VON ≤ VIL|–40°C to +105°C|750|kΩ|
|**REVERSE CURRENT BLOCKING(RCB)**|**REVERSE CURRENT BLOCKING(RCB)**|**REVERSE CURRENT BLOCKING(RCB)**|**REVERSE CURRENT BLOCKING(RCB)**|**REVERSE CURRENT BLOCKING(RCB)**|**REVERSE CURRENT BLOCKING(RCB)**|**REVERSE CURRENT BLOCKING(RCB)**|
|IRCB|RCB Activation Current|Enabled, VOUT > VIN|Enabled, VOUT > VIN|–40°C to +125°C|-0.5<br>-1|A|
|tRCB|RCB Activation time|Enabled, VOUT > VIN + 200mV|Enabled, VOUT > VIN + 200mV|–40°C to +125°C|10|µs|
|VRCB|RCB Release Voltage|Enabled, VOUT > VIN|Enabled, VOUT > VIN|–40°C to +125°C|25|mV|
|IIN,RCB|VIN Reverse Leakage Current|0 V ≤ VIN + VRCB≤ VOUT ≤ 5.5 V|0 V ≤ VIN + VRCB≤ VOUT ≤ 5.5 V|–40°C to +105°C|–1|µA|
|**QUICK OUTPUT DISCHARGE(QOD)**|**QUICK OUTPUT DISCHARGE(QOD)**|**QUICK OUTPUT DISCHARGE(QOD)**|**QUICK OUTPUT DISCHARGE(QOD)**|**QUICK OUTPUT DISCHARGE(QOD)**|**QUICK OUTPUT DISCHARGE(QOD)**|**QUICK OUTPUT DISCHARGE(QOD)**|
|QOD|Output discharge resistance|Disabled|Disabled|–40°C to +105°C|150|Ω|


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**7.6 Switching Characteristics**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



Unless otherwise noted, the typical characteristics in the following table applies over the entire recommended power supply
voltage range of 1 V to 5.5 V at 25°C with a load of C L = 1 µF, R L = 10 Ω
















|PARAMETER|TEST CONDITIONS|Col3|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|tON<br>Turn ON Time|VIN = 5.0 V|CT  = Open|100|µs|
|tON<br>Turn ON Time|VIN = 5.0 V|CT  ≥ 100 pF|4|µs/pF|
|tON<br>Turn ON Time|VIN = 3.6 V|CT  = Open|120|µs|
|tON<br>Turn ON Time|VIN = 3.6 V|CT  ≥ 100 pF|3.8|µs/pF|
|tON<br>Turn ON Time|VIN = 1.8 V|CT  = Open|200|µs|
|tON<br>Turn ON Time|VIN = 1.8 V|CT  ≥ 100 pF|3.6|µs/pF|
|tON<br>Turn ON Time|VIN = 1.2 V|CT  = Open|300|µs|
|tON<br>Turn ON Time|VIN = 1.2 V|CT  ≥ 200 pF|3.4|µs/pF|
|tON<br>Turn ON Time|VIN = 1.0 V|CT  = Open|400|µs|
|tON<br>Turn ON Time|VIN = 1.0 V|CT  ≥ 400 pF|3|µs/pF|
|tR<br>Output Rise Time|VIN = 5.0 V|CT  = Open|55|µs|
|tR<br>Output Rise Time|VIN = 5.0 V|CT  ≥ 100 pF|1.8|µs/pF|
|tR<br>Output Rise Time|VIN = 3.6 V|CT  = Open|65|µs|
|tR<br>Output Rise Time|VIN = 3.6 V|CT  ≥ 100 pF|1.6|µs/pF|
|tR<br>Output Rise Time|VIN = 1.8 V|CT  = Open|100|µs|
|tR<br>Output Rise Time|VIN = 1.8 V|CT  ≥ 100 pF|1.2|µs/pF|
|tR<br>Output Rise Time|VIN = 1.2 V|CT  = Open|150|µs|
|tR<br>Output Rise Time|VIN = 1.2 V|CT  ≥ 200 pF|0.95|µs/pF|
|tR<br>Output Rise Time|VIN = 1.0 V|CT  = Open|200|µs|
|tR<br>Output Rise Time|VIN = 1.0 V|CT  ≥ 400 pF|0.6|µs/pF|
|SRON<br>Turn ON Slew Rate(1)|VIN = 5.0 V|CT  = Open|72|mV/µs|
|SRON<br>Turn ON Slew Rate(1)|VIN = 5.0 V|CT  ≥ 100 pF|2300|(mV/µs)*pF|
|SRON<br>Turn ON Slew Rate(1)|VIN = 3.6 V|CT  = Open|44|mV/µs|
|SRON<br>Turn ON Slew Rate(1)|VIN = 3.6 V|CT  ≥ 100 pF|1900|(mV/µs)*pF|
|SRON<br>Turn ON Slew Rate(1)|VIN = 1.8 V|CT  = Open|14|mV/µs|
|SRON<br>Turn ON Slew Rate(1)|VIN = 1.8 V|CT  ≥ 100 pF|1100|(mV/µs)*pF|
|SRON<br>Turn ON Slew Rate(1)|VIN = 1.2 V|CT  = Open|6.2|mV/µs|
|SRON<br>Turn ON Slew Rate(1)|VIN = 1.2 V|CT  ≥ 200 pF|1000|(mV/µs)*pF|
|SRON<br>Turn ON Slew Rate(1)|VIN = 1.0 V|CT  = Open|3.9|mV/µs|
|SRON<br>Turn ON Slew Rate(1)|VIN = 1.0 V|CT  ≥ 400 pF|1100|(mV/µs)*pF|
|tOFF<br>Turn OFF Time|||10|µs|
|tFALL<br>Output Fall Time(2)|RL = 10 Ω|CL = 1uF, RQOD  = Short|22|µs|
|tFALL<br>Output Fall Time(2)|RL = Open|CL = 10uF, RQOD  = Short|3.8|ms|
|tFALL<br>Output Fall Time(2)|RL = Open|CL = 10uF, RQOD  = 100 Ω|5.9|ms|
|tFALL<br>Output Fall Time(2)|RL = Open|CL = 220uF, RQOD  = Short|72|ms|



(1) SR ON is the fastest Slew Rate during the turn on time (t ON )
(2) Output may not discharge completely if QOD is not connected to VOUT.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 7


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**7.7 Typical Characteristics**


**7.7.1 Typical Electrical Characteristics**


The typical characteristics curves in this section apply at 25°C unless otherwise noted.














|Col1|105 qC<br>85 qC<br>25 qC|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||40qC||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||1<br>|05qC<br>|
||||||||8<br>|5qC<br>|
|||||||||5qC<br>40qC|


























|Col1|1 V|1.8|V|5 V|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~.2 V~~|~~3.6~~|~~V~~||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|85qC<br>25qC|
|---|---|---|---|---|---|---|---|---|
|||||||||~~40qC~~|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||||||||||VIH<br>VIL|










|10<br>105 qC<br>85 qC<br>8 25 qC<br>40 qC<br>6 (nA)<br>ISD,VIN<br>4<br>2<br>0<br>1 1.5 2 2.5 3 3.5 4 4.5 5 5.5<br>VIN (V)<br>D002<br>V ≤ V<br>ON IL<br>Figure 7-1. Shutdown Current (I )<br>SD|0.8<br>0.75<br>0.7<br>0.65<br>0.6 (nA)<br>0.55 IQ,VIN<br>0.5<br>0.45<br>105 qC<br>0.4 85 qC<br>0.35 25 qC<br>40 qC<br>0.3<br>1 1.5 2 2.5 3 3.5 4 4.5 5 5.5<br>VIN (V)<br>D001<br>V ≥ V<br>ON IH<br>Figure 7-2. Quiescent Current (I )<br>Q|
|---|---|
|Temperature (°C)<br>RON (m:)<br>-40<br>-20<br>0<br>20<br>40<br>60<br>80<br>100<br>120<br>50<br>75<br>100<br>125<br>150<br>175<br>200<br>225<br>250<br>275<br>D004<br>1 V<br>~~1.2 V~~<br>1.8 V<br>~~3.6 V~~<br>5 V<br>VON ≥ VIH<br>**Figure 7-3. ON-Resistance (RON)**|VIN (V)<br>QOD (:)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>140<br>160<br>180<br>200<br>220<br>240<br>260<br>D007<br>85qC<br>25qC<br>~~40qC~~<br>VON ≤ VIL<br>**Figure 7-4. Quick Output Discharge (QOD)**|
|VIN (V)<br>VON (V)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0.55<br>0.575<br>0.6<br>0.625<br>0.65<br>0.675<br>0.7<br>0.725<br>D006<br>VIH<br>VIL<br>–40°C to +105°C<br>**Figure 7-5. ON Pin Threshold**|Temperature (qC)<br>RPD (k:)<br>-50<br>0<br>50<br>100<br>150<br>650<br>700<br>750<br>800<br>850<br>900<br>950<br>1000<br>1050<br>D005<br>VON ≤ VIL<br>**Figure 7-6. ON Pin Smart Pulldown (RPD)**|



8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**7.7.2 Typical Switching Characteristics**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



The typical data in this section apply at 25°C with a load of C L = 1 μF, R L = 10 Ω, and QOD shorted to VOUT unless

otherwise noted.








|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|105°C|
|---|---|---|---|---|---|---|---|---|
|||||||||85°C<br>|
|||||||||~~25°C~~<br>~~40°C~~|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|1<br>8|05 °C<br>5 °C|
|---|---|---|---|---|---|---|---|---|
||||||||~~2~~<br>|~~5 °C~~<br>40 °C|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||










|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||~~1~~<br>8<br>|~~05qC~~<br>5qC<br>|
||||||||~~2~~<br>-4|~~qC~~<br>0qC|









|600<br>550 105°C<br>85°C<br>500 25°C<br>450 40°C<br>400<br>350<br>(V)<br>300<br>tON<br>250<br>200<br>150<br>100<br>50<br>0<br>1 1.5 2 2.5 3 3.5 4 4.5 5 5.5<br>VIN (V)<br>D009<br>Figure 7-7. Turn-On Time (CT = Open)|Figure 7-8. Turn-On at 5 V (CT = Open)|
|---|---|
|VIN (V)<br>tRISE (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>50<br>100<br>150<br>200<br>250<br>300<br>D010<br>105 °C<br>85 °C<br>~~25 °C~~<br>40 °C<br>**Figure 7-9. Rise Time (CT = Open)**|**Figure 7-10. Turn-On at 3.6 V (CT = Open)**|
|VIN (V)<br>SRON (mV/Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>D008<br>~~105qC~~<br>85qC<br>~~25qC~~<br>-40qC<br>**Figure 7-11. Slew Rate (CT = Open)**|**Figure 7-12. Turn On at 1 V (CT = Open)**|


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 9


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**








|Col1|105°C<br>85°C|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~25°C~~<br>40°C||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||1<br>|05qC<br>~~5C~~|
||||||||2<br>|~~q~~<br>5qC<br>40qC|












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|1<br>8|05 °C<br>5 °C|
|---|---|---|---|---|---|---|---|---|
||||||||~~2~~<br>|~~5 °C~~<br>40 °C|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||







|7.7.2 Typical Switching Characteristics (continued)|Col2|
|---|---|
|VIN (V)<br>tON (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>2000<br>2500<br>3000<br>3500<br>4000<br>4500<br>5000<br>D013<br>105°C<br>85°C<br>~~25°C~~<br>40°C<br>**Figure 7-13. Turn On Time (CT = 1000 pF)**|**Figure 7-14. Turn-On at 5 V (CT = 1000 pF)**|
|VIN (V)<br>tRISE (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>300<br>600<br>900<br>1200<br>1500<br>1800<br>D014<br>105qC<br>~~85qC~~<br>25qC<br>40qC<br>**Figure 7-15. Rise Time (CT = 1000 pF)**|**Figure 7-16. Turn-On at 3.6 V (CT = 1000 pF)**|
|VIN (V)<br>SRON (mV/Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>D012<br>105 °C<br>85 °C<br>~~25 °C~~<br>40 °C<br>**Figure 7-17. Slow Slew Rate (CT = 1000 pF)**|**Figure 7-18. Turn-On at 1 V (CT = 1000 pF)**|


10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)








|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||2|20 µF|
||||||||4<br>1|7 µF<br> µF|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||||||||||3 :<br>10:|


























|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||2<br>4<br>1|20 µF<br>7 µF<br> µF|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|3 :|
|---|---|---|---|---|---|---|---|---|
|||||||||~~10:~~<br>Open|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||




















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||~~2~~|~~20 µF~~|
||||||||4<br>1|7 µF<br> µF|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|3 :<br>10 :|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||














|7.7.2 Typical Switching Characteristics (continued)|Col2|
|---|---|
|VIN (V)<br>tON (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>22000<br>23000<br>24000<br>25000<br>26000<br>27000<br>28000<br>29000<br>D022<br>220 µF<br>47 µF<br>1 µF<br>RL = 10 Ω<br>**Figure 7-19. Turn-On vs Load Capacitance (CT = 10000 pF)**|VIN (V)<br>tON (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>22000<br>24000<br>26000<br>28000<br>30000<br>32000<br>34000<br>D023<br>3 :<br>10:<br>CL = 47 µF<br>**Figure 7-20. Turn-On vs Load Resistance (CT = 10000 pF)**|
|VIN (V)<br>tR (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>2000<br>4000<br>6000<br>8000<br>10000<br>12000<br>D024<br>220 µF<br>47 µF<br>1 µF<br>RL = 10 Ω<br>**Figure 7-21. Rise Time vs Load Capacitance (CT = 10000 pF)**|VIN (V)<br>tR (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>600<br>900<br>1200<br>1500<br>1800<br>2100<br>2400<br>2700<br>3000<br>3300<br>3600<br>D025<br>3 :<br>~~10:~~<br>Open<br>CL = 47 µF<br>**Figure 7-22. Rise Time vs Load Resistance (CT = 10000 pF)**|
|VIN (V)<br>SRON (mV/Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>D026<br>~~220 µF~~<br>47 µF<br>1 µF<br>RL = 10 Ω<br>**Figure 7-23. Slew Rate vs Load Capacitance (CT = 10000 pF)**|VIN (V)<br>SRON (mV/Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>**D027**<br>3 :<br>10:<br>CL = 47 µF<br>**Figure 7-24. Slew Rate vs Load Resistance (CT = 10000 pF)**|



Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 11


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**














|Col1|Col2|Col3|Col4|Col5|Col6|105°C|
|---|---|---|---|---|---|---|
|||||||~~5°C~~<br>25°C<br>~~40°C~~|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||


|Col1|10 PF<br>220 P|F|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||




















|Col1|Col2|Col3|Col4|Col5|1|05 qC|
|---|---|---|---|---|---|---|
||||||~~8~~<br>2<br>~~~~|~~5qC~~<br>5qC<br>~~40qC~~|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||


|Col1|10 uF|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||220 u|F|||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||










|7.7.2 Typical Switching Characteristics (continued)|Col2|
|---|---|
|**Figure 7-25. Turn-Off at 3.6 V**|RL = Open<br>CL = 47 μF<br>**Figure 7-26. Turn-Off at 3.6 V (Open Load)**|
|VIN (V)<br>tOFF (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>D011<br>105°C<br>~~85°C~~<br>25°C<br>~~40°C~~<br>VIN = 1 V to 5.5 V<br>**Figure 7-27. Turn-Off Time**|RQOD (:)<br>tOFF (Ps)<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>700<br>800<br>900 1000<br>0<br>5000<br>10000<br>15000<br>20000<br>25000<br>D032<br>10PF<br>220PF<br>VIN = 1 V to 5.5 V<br>RL = Open<br>**Figure 7-28. Turn-Off Time (Open Load)**|
|VIN (V)<br>tFALL (Ps)<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>5.5<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>D028<br>105qC<br>~~85qC~~<br>25qC<br>~~40qC~~<br>VIN = 1 V to 5.5 V<br>**Figure 7-29. Fall Time**|RQOD (:)<br>tFALL (Ps)<br>0<br>100<br>200<br>300<br>400<br>500<br>600<br>700<br>800<br>900 1000<br>0<br>50000<br>100000<br>150000<br>200000<br>250000<br>300000<br>350000<br>400000<br>450000<br>500000<br>550000<br>**D030**<br>10 uF<br>220 uF<br>VIN = 1 V to 5.5 V<br>RL = Open<br>**Figure 7-30. Fall Time (Open Load)**|



12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**8 Parameter Measurement Information**

**8.1 Test Circuit and Timing Waveforms Diagrams**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



R L















Copyright © 2018, Texas Instruments Incorporated


A. Rise and fall times of the control signal are 100 ns.

B. Turn-off times and fall times are dependent on the time constant at the load. For TPS22917x, the internal pull-down resistance QOD is

enabled when the switch is disabled. The time constant is (R QOD + QOD || R L ) × C L .


**Figure 8-1. Test Circuit**


**Figure 8-2. Timing Waveforms**


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 13


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**9 Detailed Description**

**9.1 Overview**


The TPS22917x device is a 5.5-V, 2-A load switch in a 6-pin SOT-23 package. To reduce voltage drop for low
voltage and high current rails, the device implements a low resistance P-channel MOSFET which reduces the
drop out voltage across the device.


The TPS22917x device has a configurable slew rate which helps reduce or eliminate power supply droop
because of large inrush currents. Furthermore, the device features a QOD pin, which allows the configuration
of the discharge rate of VOUT after the switch is disabled. During shutdown, the device has very low leakage
currents, thereby reducing unnecessary leakages for downstream modules during standby. Integrated control
logic, driver, charge pump, and output discharge FET eliminates the need for any external components which
reduces solution size and bill of materials (BOM) count.


**9.2 Functional Block Diagram**



IN


ON







OUT


CT


QOD




|Col1|Reverse<br>Current<br>Blocking<br>Control Timing<br>Driver<br>Logic Control|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||



GND


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**9.3 Feature Description**


**9.3.1 On and Off Control**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



The ON pin controls the state of the switch. The ON pin is compatible with standard GPIO logic threshold so it
can be used in a wide variety of applications. The TPS22917 is enabled when the voltage applied to the ON pin
is pulled above V IH, while the TPS22917L is enabled when the voltage is below V IL .


When power is first applied to VIN, a Smart Pulldown is used to keep the ON pin from floating until system
sequencing is complete. After the ON pin is deliberately driven high (≥V IH ), the Smart Pulldown is disconnected
to prevent unnecessary power loss. Table 9-1 shown then the ON Pin Smart Pulldown is active.


**Table 9-1. Smart-ON Pulldown**

|VON|Pulldown|
|---|---|
|≤ VIL|Connected|
|≥ VIH|Disconnected|



**9.3.2 Turn-On Time (t** **ON** **) and Adjustable Slew Rate (CT)**


A capacitor to VIN on the CT pin sets the slew rate of V OUT . The CT capacitor voltage ramps until shortly after
the switch is turned on and V OUT becomes stable.


Leaving the CT pin open results in the highest slew rate and fastest turn-on time. These values can be found
in the Switching Characteristics Table. For slower slew rates the required CT capacitor can be found using
Equation 1:


CT = (Slew Rate) ÷ SR ON (1)


where


 - Slew Rate = desired slew rate (mV/us)

 - CT = the capacitance value on the CT pin (pF)

 - SR ON = slew rate constant from table [(mV/µs) × pF]


The total turn-on time has a direct correlation to the output slew rate. The fastest turn on times (t ON ), with CT
pin open, can be found in the _Switching Characteristics_ . For slower slew rates, the resulting turn-on time can be
found with Equation 2:


Turn-On time = CT × t ON (2)


where


 - Turn-On Time = total time from enable until V OUT rises to 90% of V IN (µs)

 - CT =the capacitance value on the CT pin (pF)

 - t ON = Turn-On time constant (µs/pF)


**9.3.3 Fall Time (t** **FALL** **) and Quick Output Discharge (QOD)**


The TPS22917x device includes a QOD pin that can be configured in one of three ways:

 - QOD pin shorted to VOUT pin. Using this method, the discharge rate after the switch becomes disabled is
controlled with the value of the internal resistance QOD.

 - QOD pin connected to VOUT pin using an external resistor R QOD . After the switch becomes disabled, the
discharge rate is controlled by the value of the total discharge resistance. To adjust the total discharge
resistance, Equation 3 can be used:


R DIS = QOD + R QOD (3)


– Where:
– R DIS = total output discharge resistance (Ω)

–
QOD = internal pulldown resistance (Ω)
– R QOD = external resistance placed between the VOUT and QOD pins (Ω)


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 15


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


 - QOD pin is unused and left floating. Using this method, there is no quick output discharge functionality, and
the output remains floating after the switch is disabled.


The fall times of the device depend on many factors including the total discharge resistance (R DIS ) and the
output capacitance (C L ). To calculate the approximate fall time of V OUT use Equation 4.


t FALL = 2.2 × (R DIS || R L ) × C L (4)


Where:


 - t FALL = output fall time from 90% to 10% (μs)

 - R DIS = total QOD + R QOD resistance (Ω)

 - R L = output load resistance (Ω)

 - C L = output load capacitance (μF)


_**9.3.3.1 QOD When System Power is Removed**_


The adjustable QOD can be used to control the power down sequencing of a system even when the system
power supply is removed. When the power is removed, the input capacitor discharges at V IN . Past a certain V IN
level, the strength of the R PD is reduced. If there is still remaining charge on the output capacitor, this results in
longer fall times. For further information regarding this condition, see the _Setting Fall Time for Shutdown Power_
_Sequencing_ section.


**9.4 Full-Time Reverse Current Blocking**


In a scenario where the device is enabled and V OUT is greater than V IN there is potential for reverse current
to flow through the pass FET or the body diode. When the reverse current threshold (I RCB ) is exceeded, the
switch is disabled within t RCB . The Switch remains off and block reverse current as long as the reverse voltage
condition exists. After V OUT has dropped below the V RCB release threshold the device turns back on with slew
rate control.


**9.5 Device Functional Modes**


Table 9-2 describes the connection of the VOUT pin depending on the state of the ON pin as well as the various
QOD pin configurations.


**Table 9-2. VOUT Connection**

|ON|QOD CONFIGURATION|TPS22917 VOUT|TPS22917L VOUT|
|---|---|---|---|
|L|QOD pin connected to VOUT with RQOD|GND (via QOD + RQOD)|VIN|
|L|QOD pin tied to VOUT directly|GND (via QOD)|VIN|
|L|QOD pin left open|Floating|VIN|
|H|QOD pin connected to VOUT with RQOD|VIN|GND (via QOD + RQOD)|
|H|QOD pin tied to VOUT directly|VIN|GND (via QOD)|
|H|QOD pin left open|VIN|Floating|



16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**10 Application and Implementation**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**10.1 Application Information**


This section highlights some of the design considerations when implementing this device in various applications.


**10.2 Typical Application**


This typical application demonstrates how the TPS22917x device can be used to power downstream modules.



R L

















Copyright © 2018, Texas Instruments Incorporated


**Figure 10-1. Typical Application Schematic**


**10.2.1 Design Requirements**


For this design example, use the values listed in Table 10-1 as the design parameters:


**Table 10-1. Design Parameters**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|Input voltage (VIN )|3.6 V|
|Load current / resistance (RL)|1 kΩ|
|Load capacitance (CL)|47 µF|
|Minimum fall time (tF)|40 ms|
|Maximum inrush current (IRUSH)|150 mA|



Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 17


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**10.2.2 Detailed Design Procedure**

_**10.2.2.1 Limiting Inrush Current**_


Use Equation 5 to find the maximum slew rate value to limit inrush current for a given capacitance:


(Slew Rate) = I RUSH ÷ C L (5)


where


 - I INRUSH = maximum acceptable inrush current (mA)

 - C L = capacitance on VOUT (μF)

 - Slew Rate = Output Slew Rate during turn on (mV/μs)


After the required slew rate shown in Equation 1 can be used to find the minimum CT capacitance


CT = SR ON ÷ (Slew Rate) (6)


CT = 1900 ÷ 3.2 = 594 pF (7)


To ensure an inrush current of less than 150 mA, choose a CT value greater than 594 pF. An appropriate value
must be placed on such that the I MAX and I PLS specifications of the device are not violated.


_**10.2.2.2 Application Curves**_


**Figure 10-2. Inrush Current (CT = 470 pF)** **Figure 10-3. Inrush Current (CT = 1000 pF)**


_**10.2.2.3 Setting Fall Time for Shutdown Power Sequencing**_


Microcontrollers and processors often have a specific shutdown sequence in which power must be removed.
Using the adjustable Quick Output Discharge function of the TPS22917x, adding a load switch to each power rail
can be used to manage the power down sequencing. To determine the QOD values for each load switch, first
confirm the power down order of the device you wish to power sequence. Be sure to check if there are voltage or
timing margins that must be maintained during power down.


After the required fall time is determined, the maximum external discharge resistance (R DIS ) value can be found
using Equation 4:


t FALL = 2.2 × (R DIS || R L ) × C L (8)


R DIS = 630 Ω (9)


Equation 3 can then be used to calculate the R QOD resistance needed to acheive a particular discharge value:


R DIS = QOD + R QOD (10)


R QOD = 480 Ω (11)


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



To ensure a fall time greater than, choose an R QOD value greater than 480 Ω.


_**10.2.2.4 Application Curves**_


**Figure 10-4. Fall Time (R** **QOD** **= 100 Ω)** **Figure 10-5. Fall Time (R** **QOD** **= 1 kΩ)**


**11 Power Supply Recommendations**


The device is designed to operate with a VIN range of 1 V to 5.5 V. The VIN power supply must be well
regulated and placed as close to the device terminal as possible. The power supply must be able to withstand all
transient load current steps. In most situations, using an input capacitance (C IN ) of 1 μF is sufficient to prevent
the supply voltage from dipping when the switch is turned on. In cases where the power supply is slow to
respond to a large transient current or large load current step, additional bulk capacitance can be required on the
input.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 19


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[TPS22917](https://www.ti.com/product/TPS22917)**
[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8) **[www.ti.com](https://www.ti.com)**


**12 Layout**
**12.1 Layout Guidelines**


For best performance, all traces must be as short as possible. To be most effective, the input and output
capacitors must be placed close to the device to minimize the effects that parasitic trace inductances can have
on normal operation. Using wide traces for VIN, VOUT, and GND helps minimize the parasitic electrical effects.


**12.2 Layout Example**


**Figure 12-1. Recommended Board Layout**


**12.3 Thermal Considerations**


The maximum IC junction temperature must be restricted to 125°C under normal operating conditions. To
calculate the maximum allowable dissipation, P D(max) for a given output current and ambient temperature, use
Equation 12:


P � T J(MAX) � T A

D(MAX)

� JA (12)


where


 - P D(MAX) = maximum allowable power dissipation

 - T J(MAX) = maximum allowable junction temperature (125°C for the TPS22917x)

 - T A = ambient temperature of the device

 - θ JA = junction to air thermal impedance. Refer to the _Thermal Information_ section. This parameter is highly
dependent upon board layout.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ Copyright © 2021 Texas Instruments Incorporated


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


**[www.ti.com](https://www.ti.com)**


**13 Device and Documentation Support**
**13.1 Receiving Notification of Documentation Updates**



**[TPS22917](https://www.ti.com/product/TPS22917)**

[SLVSDW8B – SEPTEMBER 2017 – REVISED DECEMBER 2021](https://www.ti.com/lit/pdf/SLVSDW8)



To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Subscribe to updates_ to register and receive a weekly digest of any product information that has changed. For
change details, review the revision history included in any revised document.


**13.2 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**13.3 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

**13.4 Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**13.5 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**14 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


Copyright © 2021 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLVSDW8B&partnum=TPS22917)_ 21


Product Folder Links: _[TPS22917](https://www.ti.com/product/tps22917?qgpn=tps22917)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 27-Jul-2025


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


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 27-Jul-2025


**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 18-Jun-2025


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
|TPS22917DBVR|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS22917DBVRG4|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS22917DBVT|SOT-23|DBV|6|250|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS22917LDBVR|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS22917LDBVR|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|TPS22917LDBVRG4|SOT-23|DBV|6|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 18-Jun-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TPS22917DBVR|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS22917DBVRG4|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS22917DBVT|SOT-23|DBV|6|250|210.0|185.0|35.0|
|TPS22917LDBVR|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS22917LDBVR|SOT-23|DBV|6|3000|210.0|185.0|35.0|
|TPS22917LDBVRG4|SOT-23|DBV|6|3000|210.0|185.0|35.0|



Pack Materials-Page 2


## **PACKAGE OUTLINE**

# **DBV0006A SOT-23 - 1.45 mm max height**

~~SCALE 4.000~~


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


