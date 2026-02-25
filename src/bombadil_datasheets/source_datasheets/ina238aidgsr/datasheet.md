**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)
## **INA238 85V, 16-Bit, High-Precision Power Monitor With I [2] C Interface**



**1 Features**


- High-resolution, 16-bit delta-sigma ADC

- Current monitoring accuracy:

  - Offset voltage: ±5µV (maximum)

  - Offset drift: ±0.02µV/°C (maximum)

  - Gain error: ±0.1% (maximum)

  - Gain error drift: ±25ppm/°C (maximum)

  - Common mode rejection: 140dB (minimum)

- Power monitoring accuracy:

  - 0.7% full scale, –40°C to +125°C (maximum)

- Fast alert response: 75μs

- Wide common-mode range: –0.3V to +85V

- Bus voltage sense input: 0V to 85V

- Shunt full-scale differential range:
±163.84mV / ±40.96mV

- Input bias current: 2.5nA (maximum)

- Temperature sensor: ±1°C (maximum at 25°C)

- Programmable conversion time and averaging

- 2.94MHz high-speed I [2] C interface with 16 pinselectable addresses

- Operates from a 2.7V to 5.5V supply:

  - Operational current: 640µA (typical)

  - Shutdown current: 5µA (maximum)


**2 Applications**


- [DC/DC converters and power inverters](https://www.ti.com/solution/automotive-dc-dc-converter)

- [Industrial battery packs](https://www.ti.com/solution/energy-storage-battery-packs-with-bms)

- [Power-over-ethernet (PoE)](https://www.ti.com/power-management/power-over-ethernet-poe/overview.html)

- [Telecom equipment](https://www.ti.com/applications/communications-equipment/overview.html)

- [Enterprise servers](https://www.ti.com/solution/rack-server)



**3 Description**


The INA238 is an ultra-precise digital power monitor
with a 16-bit delta-sigma ADC specifically designed
for current-sensing applications. The device can
measure a full-scale differential input of ±163.84mV
or ±40.96mV across a resistive shunt sense element
with common-mode voltage support from –0.3V to
+85V.


The INA238 reports current, bus voltage, temperature,
and power, all while performing the needed
calculations in the background. The integrated
temperature sensor is ±1°C accurate for die
temperature measurement and is useful in monitoring
the system ambient temperature.


The low offset and gain drift design of the INA238
allows the device to be used in precise systems
that do not undergo multi-temperature calibration
during manufacturing. Further, the very low offset
voltage and noise allow for use in A to kA sensing
applications and provide a wide dynamic range
without significant power dissipation losses on the
sensing shunt element. The low input bias current
of the device permits the use of larger currentsense resistors, thus providing accurate current
measurements in the micro-amp range.


The device allows for selectable ADC conversion
times from 50µs to 4.12ms as well as sample
averaging from 1x to 1024x, which further helps
reduce the noise of the measured data.


**Package Information**

|PART NUMBER|PACKAGE(1)|PACKAGE SIZE(2)|
|---|---|---|
|INA238|DGS (VSSOP, 10)|3.00mm × 4.90mm|



(1) For more information, see Section 10.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.


VS







IN+


IN

VBUS



SCL


SDA


A0


A1


ALERT








|Voltage|Current|
|---|---|
|Power|Temp|









GND


**Simplified Block Diagram**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1
**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Pin Configuration and Functions** ...................................3
**5 Specifications** .................................................................. 3

5.1 Absolute Maximum Ratings........................................ 3
5.2 ESD Ratings............................................................... 4
5.3 Recommended Operating Conditions.........................4
5.4 Thermal Information....................................................4
5.5 Electrical Characteristics.............................................5
5.6 Timing Requirements (I [2] C)......................................... 7
5.7 Timing Diagram ..........................................................7
5.8 Typical Characteristics................................................ 8
**6 Detailed Description** ......................................................12

6.1 Overview................................................................... 12
6.2 Functional Block Diagram......................................... 12
6.3 Feature Description...................................................12



6.4 Device Functional Modes..........................................17
6.5 Programming............................................................ 18
6.6 Register Maps...........................................................21
**7 Application and Implementation** .................................. 29

7.1 Application Information............................................. 29
7.2 Typical Application.................................................... 33
7.3 Power Supply Recommendations.............................36
7.4 Layout....................................................................... 36
**8 Device and Documentation Support** ............................38

8.1 Receiving Notification of Documentation Updates....38
8.2 Support Resources................................................... 38
8.3 Trademarks............................................................... 38
8.4 Electrostatic Discharge Caution................................38
8.5 Glossary....................................................................38
**9 Revision History** ............................................................ 38
**10 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 38



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**4 Pin Configuration and Functions**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



Not to scale


**Figure 4-1. DGS Package 10-Pin VSSOP Top View**


**Table 4-1. Pin Functions**



|PIN|Col2|TYPE|DESCRIPTION|
|---|---|---|---|
|**NO.**|**NAME**|**NAME**|**NAME**|
|1|A1|Digital input|I2C address pin. Connect to GND, SCL, SDA, or VS.|
|2|A0|Digital input|I2C address pin. Connect to GND, SCL, SDA, or VS.|
|3|ALERT|Digital output|Open-drain alert output, default state is active low.|
|4|SDA|Digital input/output|Open-drain bidirectional I2C data.|
|5|SCL|Digital input|I2C clock input.|
|6|VS|Power supply|Power supply, 2.7V to 5.5V.|
|7|GND|Ground|Ground.|
|8|VBUS|Analog input|Bus voltage input.|
|9|IN–|Analog input|Negative input to the device. For high-side applications, connect to load side of sense resistor. For<br>low-side applications, connect to ground side of sense resistor.|
|10|IN+|Analog input|Positive input to the device. For high-side applications, connect to power supply side of sense<br>resistor. For low-side applications, connect to load side of sense resistor.|


**5 Specifications**


**5.1 Absolute Maximum Ratings**
over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|VS|Supply voltage|6|V|
|VIN+, VIN–(2)|Differential (VIN+) – (VIN–)|–40<br>40|V|
|VIN+, VIN–(2)|Common-mode|–0.3<br>85|V|
|VVBUS||–0.3<br>85|V|
|VALERT|ALERT|–0.3<br>VS + 0.3|V|
|VIO|SDA, SCL|–0.3<br>6|V|
|IIN|Input current into any pin|5|mA|
|IOUT|Digital output current|10|mA|
|TJ|Junction temperature|150|°C|
|Tstg|Storage temperature|–65<br>150|°C|



(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
(2) VIN+ and VIN– are the voltages at the IN+ and IN– pins, respectively.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 3


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**5.2 ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all<br>pins(1)|±2000|V|
|V(ESD)|Electrostatic discharge|Charged device model (CDM), per JEDEC specification JESD22-<br>C101, all pins(2)|±1000|±1000|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**5.3 Recommended Operating Conditions**
over operating free-air temperature range (unless otherwise noted)

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VCM|Common-mode input range|–0.3<br>85|V|
|VS|Operating supply range|2.7<br>5.5|V|
|TA|Ambient temperature|–40<br>125|°C|



**5.4 Thermal Information**







|THERMAL METRIC(1)|Col2|INA238|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**DGS**|**DGS**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**10 PINS**|**10 PINS**|
|RθJA|Junction-to-ambient thermal resistance|177.6|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|66.4|°C/W|
|RθJB|Junction-to-board thermal resistance|99.5|°C/W|
|ΨJT|Junction-to-top characterization parameter|9.7|°C/W|
|YJB|Junction-to-board characterization parameter|97.6|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|N/A|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
note.


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**5.5 Electrical Characteristics**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



at TA = 25 °C, VS = 3.3V, VSENSE = VIN+ – VIN– = 0V, VCM = VIN– = 48V (unless otherwise noted)






















|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**INPUT**|**INPUT**|**INPUT**|**INPUT**|**INPUT**|
|VCM|Common-mode input range|TA = –40°C to +125°C|–0.3<br>85|V|
|VVBUS|Bus voltage input range||0<br>85|V|
|CMRR|Common-mode rejection|–0.3V < VCM < 85V, TA = –40°C to +125°C|140<br>160|dB|
|VDIFF|Shunt voltage input range|TA = –40°C to +125°C, ADCRANGE = 0|–163.84<br>163.84|mV|
|VDIFF|Shunt voltage input range|TA = –40°C to +125°C, ADCRANGE = 1|–40.96<br>40.96|mV|
|Vos|Shunt offset voltage|VCM = 48V|±1.5<br>±5|µV|
|Vos|Shunt offset voltage|VCM= 0V|±1.5<br>±5|µV|
|dVos/dT|Shunt offset voltage drift|TA = –40°C to +125°C|±2<br>±20|nV/°C|
|PSRR|Shunt offset voltage vs power supply|VS = 2.7V to 5.5V, TA = –40°C to +125°C|±0.1<br>±1|µV/V|
|Vos_bus|VBUS offset voltage|VBUS = 20mV|±1<br>±5|mV|
|dVos/dT|VBUS offset voltage drift|TA = –40°C to +125°C|±4<br>±40|µV/°C|
|PSRR|VBUS offset voltage vs power supply|VS = 2.7V to 5.5V|±1.1|mV/V|
|IB|Input bias current|Either input, IN+ or IN–, VCM = 85V|0.1<br>2.5|nA|
|ZVBUS|VBUS pin input impedance|Active mode|0.8<br>1<br>1.2|MΩ|
|IVBUS|VBUS pin leakage current|Shutdown mode, VBUS = 85V|10|nA|
|RDIFF|Input differential impedance|Active mode, VIN+ – VIN– < 164mV|92|kΩ|
|**DC ACCURACY**|**DC ACCURACY**|**DC ACCURACY**|**DC ACCURACY**|**DC ACCURACY**|
|GSERR|Shunt voltage gain error||±0.01<br>±0.1|%|
|GS_DRFT|Shunt voltage gain error drift||±25|ppm/°C|
|GBERR|VBUS voltage gain error||±0.01<br>±0.1|%|
|GB_DRFT|VBUS voltage gain error drift||±25|ppm/°C|
|PTME|Power total measurment error (TME)|TA = –40°C to +125°C, at full scale|±0.7|%|
||ADC resolution||16|Bits|
||1 LSB step size|Shunt voltage, ADCRANGE = 0|5|µV|
||1 LSB step size|Shunt voltage, ADCRANGE = 1|1.25|µV|
||1 LSB step size|Bus voltage|3.125|mV|
||1 LSB step size|Temperature|125|m°C|
|TCT|ADC conversion-time(1)|Conversion time field = 0h|50|µs|
|TCT|ADC conversion-time(1)|Conversion time field = 1h|84|84|
|TCT|ADC conversion-time(1)|Conversion time field = 2h|150|150|
|TCT|ADC conversion-time(1)|Conversion time field = 3h|280|280|
|TCT|ADC conversion-time(1)|Conversion time field = 4h|540|540|
|TCT|ADC conversion-time(1)|Conversion time field = 5h|1052|1052|
|TCT|ADC conversion-time(1)|Conversion time field = 6h|2074|2074|
|TCT|ADC conversion-time(1)|Conversion time field = 7h|4120|4120|
|INL|Integral Non-Linearity||±2|m%|
|DNL|Differential Non-Linearity||0.2|LSB|
|**CLOCK SOURCE**|**CLOCK SOURCE**|**CLOCK SOURCE**|**CLOCK SOURCE**|**CLOCK SOURCE**|
|FOSC|Internal oscillator frequency||1|MHz|
|FOSC_TOL|Internal oscillator frequency tolerance|TA = 25°C|±0.5|%|
|FOSC_TOL|Internal oscillator frequency tolerance|TA = –40°C to +125°C|±1|%|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 5


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**5.5 Electrical Characteristics (continued)**

at TA = 25 °C, VS = 3.3V, VSENSE = VIN+ – VIN– = 0V, VCM = VIN– = 48V (unless otherwise noted)



















|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**TEMPERATURE SENSOR**|**TEMPERATURE SENSOR**|**TEMPERATURE SENSOR**|**TEMPERATURE SENSOR**|**TEMPERATURE SENSOR**|
||Measurement range||–40<br>+125|°C|
||Temperature accuracy|TA = 25°C|±0.15<br>±1|°C|
||Temperature accuracy|TA = –40°C to +125°C|±0.2<br>±2|°C|
|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|
|VS|Supply voltage||2.7<br>5.5|V|
|IQ|Quiescent current|VSENSE = 0V|640<br>750|µA|
|IQ|Quiescent current|VSENSE = 0V, TA = –40°C to +125°C|1.1|mA|
|IQSD|Quiescent current, shutdown|Shutdown mode|2.8<br>5|µA|
|TPOR|Device start-up time|Power-up (NPOR)|300|µs|
|TPOR|Device start-up time|From shutdown mode|60|60|
|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|
|VIH|Logic input level, high|SDA, SCL|1.2<br>5.5|V|
|VIL|Logic input level, low||GND<br>0.4|V|
|VOL|Logic output level, low|IOL = 3mA|GND<br>0.4|V|
|IIO_LEAK|Digital leakage input current|0 ≤ VIN ≤ VS|–1<br>1|µA|


(1) Subject to oscillator accuracy and drift


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**5.6 Timing Requirements (I** **[2]** **C)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)









|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|I2C BUS (FAST MODE)|I2C BUS (FAST MODE)|I2C BUS (FAST MODE)|I2C BUS (FAST MODE)|
|F(SCL)|I2C clock frequency|1<br>400|kHz|
|t(BUF)|Bus free time between STOP and START conditions|600|ns|
|t(HDSTA)|Hold time after a repeated START condition. After this period, the first<br>clock is generated.|100|ns|
|t(SUSTA)|Repeated START condition setup time|100|ns|
|t(SUSTO)|STOP condition setup time|100|ns|
|t(HDDAT)|Data hold time|10<br>900|ns|
|t(SUDAT)|Data setup time|100|ns|
|t(LOW)|SCL clock low period|1300|ns|
|t(HIGH)|SCL clock high period|600|ns|
|tF|Data fall time|300|ns|
|tF|Clock fall time|300|ns|
|tR|Clock rise time|300|ns|
|I2C BUS (HIGH-SPEED MODE)|I2C BUS (HIGH-SPEED MODE)|I2C BUS (HIGH-SPEED MODE)|I2C BUS (HIGH-SPEED MODE)|
|F(SCL)|I2C clock frequency|10<br>2940|kHz|
|t(BUF)|Bus free time between STOP and START conditions|160|ns|
|t(HDSTA)|Hold time after a repeated START condition. After this period, the first<br>clock is generated.|100|ns|
|t(SUSTA)|Repeated START condition setup time|100|ns|
|t(SUSTO)|STOP condition setup time|100|ns|
|t(HDDAT)|Data hold time|10<br>125|ns|
|t(SUDAT)|Data setup time|20|ns|
|t(LOW)|SCL clock low period|200|ns|
|t(HIGH)|SCL clock high period|60|ns|
|tF|Data fall time|80|ns|
|tF|Clock fall time|40|ns|
|tR|Clock rise time|40|ns|


**5.7 Timing Diagram**


SCL


SDA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||tR<br>tF<br>t(HDSTA)<br>t(HDDAT)<br>t(SUDAT)<br>t(HIGH)<br>t(SUSTA)||||
|||||||||
|||t(BUF)|t(BUF)|t(BUF)|t(BUF)|t(BUF)|t(BUF)|
|||||||||
||P|P|S|S|S|S|S|



**Figure 5-1. I** **[2]** **C Timing Diagram**

|Col1|Col2|
|---|---|
|||
||t(|
|P|P|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 7


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**5.8 Typical Characteristics**


at TA = 25 °C, VVS = 3.3 V, VCM = 48 V, VSENSE = 0, and VVBUS = 48 V (unless otherwise noted)












|Population<br>-5 -4 -3 -2 -1 0 1 2 3 4 5<br>Shunt Offset Voltage (PV)<br>V = 48 V<br>CM<br>Figure 5-2. Shunt Input Offset Voltage Production Distribution|Population<br>-5 -4 -3 -2 -1 0 1 2 3 4 5<br>Shunt Offset Voltage (PV)<br>V = 0 V<br>CM<br>Figure 5-3. Shunt Input Offset Voltage Production Distribution|
|---|---|
|**Figure 5-4. Shunt Input Offset Voltage vs Temperature**|**Figure 5-5. Common-Mode Rejection Ratio Production**<br>**Distribution**|
|.<br>**Figure 5-6. Shunt Input Common-Mode Rejection Ratio vs**<br>**Temperature**|VCM = 24 V<br>**Figure 5-7. Shunt Input Gain Error Production Distribution**|



8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**5.8 Typical Characteristics (continued)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



at TA = 25 °C, VVS = 3.3 V, VCM = 48 V, VSENSE = 0, and VVBUS = 48 V (unless otherwise noted)









|V = 24 V<br>CM<br>Figure 5-8. Shunt Input Gain Error vs Temperature|.<br>Figure 5-9. Shunt Input Gain Error vs Common-Mode Voltage|
|---|---|
|Bus Offset Voltage (mV)<br>Population<br>-5<br>-4<br>-3<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>5<br>VVBUS = 20 mV<br>**Figure 5-10. Bus Input Offset Voltage Production Distribution**|VVBUS = 20 mV<br>**Figure 5-11. Bus Input Offset Voltage vs Temperature**|
|**Figure 5-12. Bus Input Gain Error Production Distribution**|**Figure 5-13. Bus Input Gain Error vs Temperature**|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 9


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**5.8 Typical Characteristics (continued)**


at TA = 25 °C, VVS = 3.3 V, VCM = 48 V, VSENSE = 0, and VVBUS = 48 V (unless otherwise noted)

|Figure 5-14. Input Bias Current vs Differential Input Voltage|Figure 5-15. Input Bias Current (IB+ or IB–) vs Common-Mode<br>Voltage|
|---|---|
|**Figure 5-16. Input Bias Current vs Temperature**|**Figure 5-17. Input Bias Current vs Temperature, Shutdown**|
|**Figure 5-18. Active IQ vs Temperature**|**Figure 5-19. Active IQ vs Supply Voltage**|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**5.8 Typical Characteristics (continued)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



at TA = 25 °C, VVS = 3.3 V, VCM = 48 V, VSENSE = 0, and VVBUS = 48 V (unless otherwise noted)










|Col1|Col2|Col3|Col4|Col5|Col6|Continuo|us|I2C|W|rite C|om|m|ands|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||Idl|e S|DA,|Cl|ockin|g S|CL|||
||||||||||||||||
||||||||||||||||
||||||||||||||||



|Figure 5-20. Shutdown I vs Supply Voltage<br>Q|Figure 5-21. Shutdown I vs Temperature<br>Q|
|---|---|
|Frequency (kHz)<br>Quiescent Current (PA)<br>1<br>10<br>100<br>1000<br>3000<br>600<br>620<br>640<br>660<br>680<br>Continuous I2C Write Commands<br>Idle SDA, Clocking SCL<br>**Figure 5-22. Active IQ vs Clock Frequency**|Frequency (kHz)<br>Quiescent Current - Shutdown (PA)<br>1<br>10<br>100<br>1000<br>3000<br>0<br>30<br>60<br>90<br>120<br>150<br>**Figure 5-23. Shutdown IQ vs Clock Frequency**|
|**Figure 5-24. Internal Clock Frequency vs Power Supply**|**Figure 5-25. Internal Clock Frequency vs Temperature**|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 11


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**6 Detailed Description**

**6.1 Overview**

The INA238 device is a digital current sense amplifier with an I [2] C digital interface. The device measures shunt
voltage, bus voltage and internal temperature while calculating current, power necessary for accurate decision
making in precisely controlled systems. Programmable registers allow flexible configuration for measurement
precision as well as continuous or triggered operation. Detailed register information is found in Section 6.6.


**6.2 Functional Block Diagram**


VS







IN+


IN

VBUS


**6.3 Feature Description**



SCL


SDA


A0


A1


ALERT










|Voltage|Current|
|---|---|
|Power|Temp|









GND



_**6.3.1 Versatile High Voltage Measurement Capability**_


The INA238 operates off a 2.7 V to 5.5 V supply but can measure voltage and current on rails as high as 85
V. The current is measured by sensing the voltage drop across a external shunt resistor at the IN+ and IN–
pins. The input stage of the INA238 is designed such that the input common-mode voltage can be higher than
the device supply voltage, VS. The supported common-mode voltage range at the input pins is –0.3 V to +85
V, which makes the device well suited for both high-side and low-side current measurements. There are no
special considerations for power-supply sequencing because the common-mode input range and device supply
voltage are independent of each other; therefore, the bus voltage can be present with the supply voltage off, and
vice-versa without damaging the device.


The device also measures the bus supply voltage through the VBUS pin and temperature through the integrated
temperature sensor. The differential shunt voltage is measured between the IN+ and IN– pins, while the bus
voltage is measured with respect to device ground. Monitored bus voltages can range from 0 V to 85 V, while
monitored temperatures can range from -40 ºC to +125 ºC.


Shunt voltage, bus voltage, and temperature measurements are multiplexed internally to a single ADC as shown
in Figure 6-1.





VBUS


IN+


IN








**Figure 6-1. High-Voltage Input Multiplexer**


12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


_**6.3.2 Power Calculation**_



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



The current and power are calculated after a shunt voltage and bus voltage measurement as shown in Figure
6-2. Power is calculated based on the previous current calculation and the latest bus voltage measurement. If
the value loaded into the SHUNT_CAL register is zero, the power value reported is also zero. The current and
power values are considered intermediate results (unless the averaging is set to 1) and are stored in an internal
accumulation register. Following every measured sample, the newly-calculated values for current and power are
appended to this accumulation register until all of the samples have been measured and averaged. After all
of the samples have been measured and the corresponding current and power calculations have been made,
the accumulated average for each of these parameters is then loaded to the corresponding output registers
where they can then be read. These calculations are performed in the background and do not add to the overall
conversion time.


Current Limit Detect Following Bus and Power Limit Detect
Every Shunt Voltage Conversion Following Every Bus Voltage Conversion


P P P P P P P P P P P P P P P P


**Power Average**


**Bus Voltage Average**


**Shunt Voltage Average**


**Figure 6-2. Power Calculation Scheme**


_**6.3.3 Low Bias Current**_


The INA238 features very low input bias current which provides several benefits. The low input bias current of
the INA238 reduces the current consumed by the device in both active and shutdown state. Another benefit of
low bias current is the ability to use input filters to reject high-frequency noise before the signal is converted to
digital data. In traditional digital current-sense amplifiers, the addition of input filters comes at the cost of reduced
accuracy. However, as a result of the low bias current, the reduction in accuracy due to input filters is minimized.
An additional benefit of low bias current is the ability to use a larger shunt resistor to accurately sense smaller
currents. Use of a larger value for the shunt resistor allows the device to accurately monitor currents in the
sub-mA range.


The bias current in the INA238 is the smallest when the sensed current is zero. As the current starts to increase,
the differential voltage drop across the shunt resistor increases which results in an increase in the bias current
as shown in Figure 5-14.


_**6.3.4 High-Precision Delta-Sigma ADC**_


The integrated ADC is a high-performance, low-offset, low-drift, delta-sigma ADC designed to support
bidirectional current flow at the shunt voltage measurement channel. The measured inputs are selected through
the high-voltage input multiplexer to the ADC inputs as shown in Figure 6-1. The ADC architecture enables
lower drift measurement across temperature and consistent offset measurements across the common-mode
voltage, temperature, and power supply variations. A low-offset ADC is preferred in current sensing applications
to provide a near 0-V offset voltage that maximizes the useful dynamic range of the system.


The INA238 can measure the shunt voltage, bus voltage, and die temperature, or a combination of any based
on the selected MODE bits setting in the ADC_CONFIG register. This permits selecting modes to convert
only the shunt voltage or bus voltage to further allow the user to configure the monitoring function to fit the
specific application requirements. When no averaging is selected, once an ADC conversion is completed, the
converted values are independently updated in the corresponding registers where they can be read through


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 13


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


the digital interface at the time of conversion end. The conversion time for shunt voltage, bus voltage, and
temperature inputs are set independently from 50 µs to 4.12ms depending on the values programmed in the
ADC_CONFIG register. Enabled measurement inputs are converted sequentially so the total time to convert
all inputs depends on the conversion time for each input and the number of inputs enabled. When averaging
is used, the intermediate values are subsequently stored in an averaging accumulator, and the conversion
sequence repeats until the number of averages is reached. After all of the averaging has been completed, the
final values are updated in the corresponding registers that can then be read. These values remain in the data
output registers until they are replaced by the next fully completed conversion results. In this case, reading the
data output registers does not affect a conversion in progress.


The ADC has two conversion modes—continuous and triggered—set by the MODE bits in ADC_CONFIG
register. In continuous-conversion mode, the ADC continuously converts the input measurements and update
the output registers as described above in an indefinite loop. In triggered-conversion mode, the ADC converts
the input measurements as described above, after which the ADC goes into shutdown mode until another
single-shot trigger is generated by writing to the MODE bits. Writing the MODE bits interrupts and restart
triggered or continuous conversions that are in progress. Although the device can be read at any time, and
the data from the last conversion remains available, the Conversion Ready flag (CNVRF bit in DIAG_ALRT
register) is provided to help coordinate triggered conversions. This bit is set after all conversions and averaging
is completed.


The Conversion Ready flag (CNVRF) clears under these conditions:


 - Writing to the ADC_CONFIG register (except for selecting shutdown mode); or

 - Reading the DIAG_ALRT Register


While the INA238 device is used in either one of the conversion modes, a dedicated digital engine is calculating
the current and power values in the background as described in Section 6.3.2. All of the calculations are
performed in the background and do not contribute to conversion time.


For applications that must synchronize with other components in the system, the INA238 conversion can be
delayed by programming the CONVDLY bits in CONFIG register in the range between 0 (no delay) and 510
ms. The resolution in programming the conversion delay is 2 ms. The conversion delay is set to 0 by default.
Conversion delay can assist in measurement synchronization when multiple external devices are used for
voltage or current monitoring purposes. In applications where an time aligned voltage and current measurements
are needed, two devices can be used with the current measurement delayed such that the external voltage and
current measurements occurs at approximately the same time. Keep in mind that even though the internal time
base for the ADC is precise, synchronization is lost over time due to internal and external time base mismatch.


**6.3.4.1 Low Latency Digital Filter**


The device integrates a low-pass digital filter that performs both decimation and filtering on the ADC output data,
which helps with noise reduction. The digital filter is automatically adjusted for the different output data rates
and always settles within one conversion cycle. The user has the flexibility to choose different output conversion
time periods TCT from 50 µs to 4.12 ms. With this configuration the first amplitude notch appears at a frequency
which is determined by the selected conversion time period and defined as fNOTCH= 1 / TCT. This means that the
filter cut-off frequency scales proportionally with the data output rate as described. Figure 6-3 shows the filter
response when the 1.052 ms conversion time period is selected.


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



0


−10


−20


−30


−40


−50


−60



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)


1 10 100 1k 10k 100k
Frequency (Hz) G001


Conversion time = 1.052 ms, single
conversion only



**Figure 6-3. ADC Frequency Response**


**6.3.4.2 Flexible Conversion Times and Averaging**


ADC conversion times for shunt voltage, bus voltage and temperature can be set independently from 50 μs to
4.12 ms. The flexibility in conversion time allows for robust operation in a variety of noisy environments. The
device also allows for programmable averaging times from a single conversion all the way to an average of
1024 conversions. The amount of averaging selected applies uniformly to all active measurement inputs. The
ADC_CONFIG register shown in Table 6-6 provides additional details on the supported conversion times and
averaging modes. The INA238 effective resolution of the ADC can be increased by increasing the conversion
time and increasing the number of averages. Figure 6-4 and Figure 6-5 shown below illustrate the effect of
conversion time and averaging on a constant input signal.


**Figure 6-4. Noise vs. Conversion Time (Averaging = 1)**


**Figure 6-5. Noise vs. Conversion Time (Averaging = 128)**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 15


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


Settings for the conversion time and number of conversions averaged impact the effective measurement
resolution. For more detailed information on how averaging reduces noise and increases the effective number of
bits (ENOB) see Section 7.1.3.


_**6.3.5 Integrated Precision Oscillator**_


The internal timebase of the device is provided by an internal oscillator that is trimmed to less than 0.5%
tolerance at room temperature. The precision oscillator is the timing source for ADC conversions. The digital
filter response varies with conversion time; therefore, the precise clock verifies that the filter response and
notch frequency consistency across temperature. On power up, the internal oscillator and ADC take roughly
300 µs to reach <1% error stability. Once the clock stabilizes, the ADC data output is accurate to the electrical
specifications provided in Section 5.


_**6.3.6 Multi-Alert Monitoring and Fault Detection**_


The INA238 includes a multipurpose, open-drain ALERT output pin that can be used to report multiple
diagnostics or as an indicator that the ADC conversion is complete when the device is operating in both
triggered and continuous conversion mode. The diagnostics listed in Table 6-1 are constantly monitored and can
be reported through the ALERT pin whenever the monitored output value crosses the associated out-of-range
threshold.


**Table 6-1. ALERT Diagnostics Description**















|INA238 DIAGNOSTIC|STATUS BIT IN DIAG_ALRT REGISTER<br>(RO)|OUT-OF-RANGE<br>THRESHOLD<br>REGISTER (R/W)|REGISTER DEFAULT<br>VALUE|
|---|---|---|---|
|Shunt Under Voltage Limit|SHNTUL|SUVL|0x8000 h<br>(two's complement)|
|Shunt Over Voltage Limit|SHNTOL|SOVL|0x7FFF h<br>(two's complement)|
|Bus Voltage Over-Limit|BUSOL|BOVL|0x7FFF h<br>(two's complement,<br>positive values only)|
|Bus Voltage Under-Limit|BUSUL|BUVL|0x0000 h<br>(two's complement,<br>positive values only)|
|Temperature Over-Limit|TMPOL|TEMP_LIMIT|0xFFFF h<br>(two's complement,<br>positive values only)|
|Power Over-Limit|POL|PWR_LIMIT|0x7FFF h<br>(two's complement)|


A read of the DIAG_ALRT register is used to determine which diagnostic has triggered the ALERT pin. This
register, shown in Table 6-13, is also used to monitor other associated diagnostics as well as configure some
ALERT pin functions.


 - Alert latch enable — In case the ALERT pin is triggered, this function holds the value of the pin even after
all diagnostic conditions have cleared. A read of the DIAG_ALRT register resets the status of the ALERT pin.
This function is enabled by setting the ALATCH bit.

 - Conversion ready enable — Enables the ALERT pin to assert when an ADC conversion has completed and
output values are ready to be read through the digital interface. This function is enabled by setting the CNVR
bit. The conversion completed events can also be read through the CNVRF bit regardless of the CNVR bit
setting.

 - Alert comparison on averaged output — Allows the out-of-range threshold value to be compared to the
averaged data values produced by the ADC. This helps to additionally remove noise from the output data
when compared to the out-of-range threshold to avoid false alerts due to noise. However, the diagnostic is
delayed due to the time needed for averaging. This function is enabled by setting the SLOWALERT bit.


16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)




 - Alert polarity — Allows the device to invert the active state of the ALERT pin. Note that the ALERT pin is an
open-drain output that must be pulled-up by a resistor. The ALERT pin is active-low by default and can be
configured for active high function using the APOL control bit.


Other diagnostic functions that are not reported by the ALERT pin but are available by reading the DIAG_ALRT
register:

 - Math overflow — Indicated by the MATHOF bit, reports when an arithmetic operation has caused an internal
register overflow.

 - Memory status — Indicated by the MEMSTAT bit, monitors the health of the device non-volatile trim memory.
This bit must always read '1' when the device is operating properly.


When the ALERT pin is configured to report the ADC conversion complete event, the ALERT pin becomes a
multipurpose reporting output. Figure 6-6 shows an example where the device reports ADC conversion complete
events while the INA238 device is subject to shunt over voltage (over current) event, bus under voltage event,
over temperature event and over power-limit event.



Shunt Voltage


Bus Voltage


Temperature


Power


ALERT
_(ALATCH = 0)_
_(APOL = 0)_
_(CNVR = 1)_


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||Shunt Over Voltage Threshold|Shunt Over Voltage Threshold|Shunt Over Voltage Threshold|Shunt Over Voltage Threshold|Shunt Over Voltage Threshold|
|||||||||
||||Bus Under Voltage Threshold|||||
|||||||||
||||Over Temp Threshold|||||
|||||||||
||||Power Over Limit Threshold|||||
|||||||||



BUV BUV SOV
SET CLEAR SET





SOV
&
BUV
SET



BUV
&
OT
&
OP
SET



SOV BUV
CLEAR &
OT
SET




_**- No diag. error -**_
_**Conversion Complete**_
_**Reported**_


**6.4 Device Functional Modes**

_**6.4.1 Shutdown Mode**_



**Figure 6-6. Multi-Alert Configuration**



In addition to the two conversion modes (continuous and triggered), the device also has a shutdown mode
(selected by the MODE bits in ADC_CONFIG register) that reduces the quiescent current to less than 5 µA and
turns off current into the device inputs, reducing the impact of supply drain when the device is not being used.
The registers of the device can be written to and read from while the device is in shutdown mode. The device
remains in shutdown mode until another triggered conversion command or continuous conversion command is
received.


The device can be triggered to perform conversions while in shutdown mode. When a conversion is triggered,
the ADC starts conversion; once conversion completes the device returns to the shutdown state.


Note that the shutdown current is specified with an inactive communications bus. Active clock and data activity
increases the current consumption as a function of the bus frequency as shown in Figure 5-23.


_**6.4.2 Power-On Reset**_


Power-on reset (POR) is asserted when VS drops below 1.26V (typical) at which all of the registers are reset to
the default values. A manual device reset can be initiated by setting the RST bit in the CONFIG register. The


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 17


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


default power-up register values are shown in the reset column for each register description. Links to the register
descriptions are shown in Section 6.6.


**6.5 Programming**

_**6.5.1 I**_ _**[2]**_ _**C Serial Interface**_

The INA238 operates only as a secondary device on both the SMBus and I [2] C interfaces. Connections to the
bus are made through the open-drain SDA and SCL lines. The SDA and SCL pins feature integrated spike
suppression filters and Schmitt triggers to minimize the effects of input spikes and bus noise. Although the
device integrates spike suppression into the digital I/O lines, proper layout techniques help minimize the amount
of coupling into the communication lines. This noise introduction can occur from capacitive coupling signal edges
between the two communication lines themselves or from other switching noise sources present in the system.
Routing traces in parallel with ground in between layers on a printed-circuit board (PCB) typically reduces the
effects of coupling between the communication lines. Shielded communication lines reduce the possibility of
unintended noise coupling into the digital I/O lines that can be incorrectly interpreted as start or stop commands.


The INA238 supports the transmission protocol for fast mode (1 kHz to 400 kHz) and high-speed mode (1 kHz to
2.94 MHz). All data bytes are transmitted most significant byte first and follow the SMBus 3.0 transfer protocol.


To communicate with the INA238, the main device must first address secondary devices through a secondary
device address byte. The secondary device address byte consists of seven address bits and a direction bit that
indicates whether the action is to be a read or write operation.


The device has two address pins, A0 and A1. Table 6-2 lists the pin logic levels for each of the 16 possible
addresses. The device samples the state of pins A0 and A1 on every bus communication. Establish the pin
states before any activity on the interface occurs. When connecting the SDA pin to either A0 or A1 to set the
device address, additional hold time of 100 ns is needed on the MSB of the I2C address to verify the correct
device addressing.


**Table 6-2. Address Pins and Secondary Device Addresses**

|A1|A0|Secondary Device Address|
|---|---|---|
|GND|GND|1000000|
|GND|VS|1000001|
|GND|SDA|1000010|
|GND|SCL|1000011|
|VS|GND|1000100|
|VS|VS|1000101|
|VS|SDA|1000110|
|VS|SCL|1000111|
|SDA|GND|1001000|
|SDA|VS|1001001|
|SDA|SDA|1001010|
|SDA|SCL|1001011|
|SCL|GND|1001100|
|SCL|VS|1001101|
|SCL|SDA|1001110|
|SCL|SCL|1001111|



**6.5.1.1 Writing to and Reading Through the I** **[2]** **C Serial Interface**


Accessing a specific register on the INA238 is accomplished by writing the appropriate value to the register
pointer. Refer to Section 6.6 for a complete list of registers and corresponding addresses. The value for the
register pointer (as shown in Figure 6-9) is the first byte transferred after the secondary device address byte with
the R ~~/W~~ bit low. Every write operation to the device requires a value for the register pointer.


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



Writing to a register begins with the first byte transmitted by the main device. This byte is the secondary
device address, with the R/ ~~W~~ bit low. The device then acknowledges receipt of a valid address. The next
byte transmitted by the main device is the address of the register to be accessed. This register address value
updates the register pointer to the desired internal device register. The next two bytes are written to the register
addressed by the register pointer. The device acknowledges receipt of each data byte. The main device can
terminate data transfer by generating a start or stop condition.


When reading from the device, the last value stored in the register pointer by a write operation determines which
register is read during a read operation. To change the register pointer for a read operation, a new value must
be written to the register pointer. This write is accomplished by issuing a secondary device address byte with
the R/ ~~W~~ bit low, followed by the register pointer byte. No additional data are required. The main device then
generates a start condition and sends the address byte for the secondary device with the R/ ~~W~~ bit high to initiate
the read command. The next byte is transmitted by the secondary device and is the most significant byte of the
register indicated by the register pointer. This byte is followed by an _Acknowledge_ from the main device; then
the secondary device transmits the least significant byte. The main device may or may not acknowledge receipt
of the second data byte. The main device can terminate data transfer by generating a _Not-Acknowledge_ after
receiving any data byte, or generating a start or stop condition. If repeated reads from the same register are
desired, continually sending the register pointer bytes is not necessary; the device retains the register pointer
value until the value is changed by the next write operation.


Figure 6-7 shows the write operation timing diagram. Figure 6-8 shows the read operation timing diagram. These
diagrams are shown for reading/writing to 16 bit registers.


Register bytes are sent most-significant byte first, followed by the least significant byte.



1


D7 D6 D5 D4 D3 D2 D1 D0



9



9 1 9


D15 D14 D13 D12 D11 D10 D9 D8



SCL


SDA



1 9 1


1 0 0 A3 A2 A1 A0 R/W P7 P6 P5 P4 P3 P2 P1 P0



ACK By Stop By
**Target** Controller



Start By ACK By ACK By
Controller **Target** **Target**


(1)



ACK By
**Target**



A. The value of the Secondary Device Address byte is determined by the settings of the A0 and A1 pins. Refer to Table 6-2.
B. The device does not support packet error checking (PEC) or perform clock stretching.


**Figure 6-7. Timing Diagram for Write Word Format**



1 9 1 9



1 9



SCL


SDA









(3)



Start By ACK By From ACK By
Controller **Target** **Target** Controller



From No ACK By
**Target** Controller



No ACK By Stop



(2)



Frame 3 Data LSByte



Frame 1 Two-Wire Target Address Byte





(2)



A. The value of the Secondary Device Address byte is determined by the settings of the A0 and A1 pins. Refer to Table 6-2.
B. Read data is from the last register pointer location. If a new register is desired, the register pointer must be updated. See Figure 6-9.
C. ACK by the main device can also be sent.
D. The device does not support packet error checking (PEC) or perform clock stretching.


**Figure 6-8. Timing Diagram for Read Word Format**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 19


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


1 9 1 9



SCL


SDA







Start By ACK By ACK By
Controller **Target** **Target**



(1)



Frame 2 Register Pointer Byte



Frame 1 Two-Wire Target Address Byte



A. The value of the Secondary Device Address Byte is determined by the settings of the A0 and A1 pins. Refer to Table 6-2.


**Figure 6-9. Typical Register Pointer Set**


**6.5.1.2 High-Speed I** **[2]** **C Mode**


When the bus is idle, both the SDA and SCL lines are pulled high by the pullup resistors. The main device
generates a start condition followed by a valid serial byte containing high-speed (HS) main device code
_00001XXX_ . This transmission is made in fast (400 kHz) or standard (100 kHz) (F/S) mode at no more than
400 kHz. The device does not acknowledge the HS main device code, but does recognize code and switches
the internal filters to support 2.94-MHz operation.


The main device then generates a repeated start condition (a repeated start condition has the same timing
as the start condition). After this repeated start condition, the protocol is the same as F/S mode, except that
transmission speeds up to 2.94 MHz are allowed. Instead of using a stop condition, use repeated start conditions
to maintain the bus in HS-mode. A stop condition ends the HS-mode and switches all the internal filters of the
device to support the F/S mode.


**6.5.1.3 SMBus Alert Response**


The INA238 is designed to respond to the SMBus Alert Response address. The SMBus Alert Response provides
a quick fault identification for simple secondary devices. When an Alert occurs, the main device can broadcast
the Alert Response secondary device address (0001 100) with the Read/Write bit set high. Following this Alert
Response, any secondary device that generates an alert identifies itself by acknowledging the Alert Response
and sending the address on the bus.

The Alert Response can activate several different target devices simultaneously, similar to the I [2] C General Call.
If more than one target attempts to respond, bus arbitration rules apply. The losing device does not generate an
Acknowledge and continues to hold the Alert line low until that device wins arbitration.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**6.6 Register Maps**

_**6.6.1 INA238 Registers**_



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



Table 6-3 lists the INA238 registers. All register locations not listed in Table 6-3 must be considered as reserved
locations and the register contents must not be modified.


**Table 6-3. INA238 Registers**











Complex bit access types are encoded to fit into small table cells. Table 6-4 shows the codes that are used for
access types in this section.


**Table 6-4. INA238 Access Type Codes**

|Access Type|Code|Description|
|---|---|---|
|Read Type|Read Type|Read Type|
|R|R|Read|
|Write Type|Write Type|Write Type|
|W|W|Write|
|Reset or Default Value|Reset or Default Value|Reset or Default Value|
|-_n_||Value after reset or the default<br>value|



**6.6.1.1 Configuration (CONFIG) Register (Address = 0h) [reset = 0h]**


The CONFIG register is shown in Table 6-5.


Return to the Summary Table.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 21


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**Table 6-5. CONFIG Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RST|R/W|0h|Reset Bit. Setting this bit to '1' generates a system reset that is the<br>same as power-on reset.<br>Resets all registers to default values.<br>0h = Normal Operation<br>1h = System Reset sets registers to default values<br>This bit self-clears.|
|14|RESERVED|R/W|0h|Reserved. Always reads 0.|
|13-6|CONVDLY|R/W|0h|Sets the Delay for initial ADC conversion in steps of 2 ms.<br>0h = 0 s<br>1h = 2 ms<br>FFh = 510 ms|
|5|RESERVED|R/W|0h|Reserved. Always reads 0.|
|4|ADCRANGE|R/W|0h|Shunt full scale range selection across IN+ and IN–.<br>0h = ±163.84 mV<br>1h = ± 40.96 mV|
|3-0|RESERVED|R|0h|Reserved. Always reads 0.|



**6.6.1.2 ADC Configuration (ADC_CONFIG) Register (Address = 1h) [reset = FB68h]**


The ADC_CONFIG register is shown in Table 6-6.


Return to the Summary Table.


**Table 6-6. ADC_CONFIG Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-12|MODE|R/W|Fh|The user can set the MODE bits for continuous or triggered mode on<br>bus voltage, shunt voltage or temperature measurement.<br>0h = Shutdown<br>1h = Triggered bus voltage, single shot<br>2h = Triggered shunt voltage, single shot<br>3h = Triggered shunt voltage and bus voltage, single shot<br>4h = Triggered temperature, single shot<br>5h = Triggered temperature and bus voltage, single shot<br>6h = Triggered temperature and shunt voltage, single shot<br>7h = Triggered bus voltage, shunt voltage and temperature, single<br>shot<br>8h = Shutdown<br>9h = Continuous bus voltage only<br>Ah = Continuous shunt voltage only<br>Bh = Continuous shunt and bus voltage<br>Ch = Continuous temperature only<br>Dh = Continuous bus voltage and temperature<br>Eh = Continuous temperature and shunt voltage<br>Fh = Continuous bus voltage, shunt voltage and temperature|



22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)


**Table 6-6. ADC_CONFIG Register Field Descriptions (continued)**



|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|11-9|VBUSCT|R/W|5h|Sets the conversion time of the bus voltage measurement:<br>0h = 50 µs<br>1h = 84 µs<br>2h = 150 µs<br>3h = 280 µs<br>4h = 540 µs<br>5h = 1052 µs<br>6h = 2074 µs<br>7h = 4120 µs|
|8-6|VSHCT|R/W|5h|Sets the conversion time of the shunt voltage measurement:<br>0h = 50 µs<br>1h = 84 µs<br>2h = 150 µs<br>3h = 280 µs<br>4h = 540 µs<br>5h = 1052 µs<br>6h = 2074 µs<br>7h = 4120 µs|
|5-3|VTCT|R/W|5h|Sets the conversion time of the temperature measurement:<br>0h = 50 µs<br>1h = 84 µs<br>2h = 150 µs<br>3h = 280 µs<br>4h = 540 µs<br>5h = 1052 µs<br>6h = 2074 µs<br>7h = 4120 µs|
|2-0|AVG|R/W|0h|Selects ADC sample averaging count. The averaging setting applies<br>to all active inputs.<br>When >0h, the output registers are updated after the averaging has<br>completed.<br>0h = 1<br>1h = 4<br>2h = 16<br>3h = 64<br>4h = 128<br>5h = 256<br>6h = 512<br>7h = 1024|


**6.6.1.3 Shunt Calibration (SHUNT_CAL) Register (Address = 2h) [reset = 1000h]**


The SHUNT_CAL register is shown in Table 6-7.


Return to the Summary Table.


**Table 6-7. SHUNT_CAL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved. Always reads 0.|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 23


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**Table 6-7. SHUNT_CAL Register Field Descriptions (continued)**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|14-0|SHUNT_CAL|R/W|1000h|The register provides the device with a conversion constant value<br>that represents shunt resistance used to calculate current value in<br>Amperes.<br>This also sets the resolution for theCURRENT register.<br>Value calculation underSection 7.1.2.|



**6.6.1.4 Shunt Voltage Measurement (VSHUNT) Register (Address = 4h) [reset = 0h]**


The VSHUNT register is shown in Table 6-8.


Return to the Summary Table.


**Table 6-8. VSHUNT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|VSHUNT|R|0h|Differential voltage measured across the shunt output. Two's<br>complement value.<br>Conversion factor:<br>5 µV/LSB whenADCRANGE = 0<br>1.25 µV/LSB whenADCRANGE = 1|



**6.6.1.5 Bus Voltage Measurement (VBUS) Register (Address = 5h) [reset = 0h]**


The VBUS register is shown in Table 6-9.


Return to the Summary Table.


**Table 6-9. VBUS Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|VBUS|R|0h|Bus voltage output. Two's complement value, however always<br>positive.<br>Conversion factor: 3.125 mV/LSB|



**6.6.1.6 Temperature Measurement (DIETEMP) Register (Address = 6h) [reset = 0h]**


The DIETEMP register is shown in Table 6-10.


Return to the Summary Table.


**Table 6-10. DIETEMP Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-4|DIETEMP|R|0h|Internal die temperature measurement. Two's complement value.<br>Conversion factor: 125 m°C/LSB|
|3-0|RESERVED|R|0h|Reserved. Always reads 0.|



**6.6.1.7 Current Result (CURRENT) Register (Address = 7h) [reset = 0h]**


The CURRENT register is shown in Table 6-11.


Return to the Summary Table.


**Table 6-11. CURRENT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|CURRENT|R|0h|Calculated current output in Amperes. Two's complement value.<br>Value description underSection 7.1.2.|



24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**6.6.1.8 Power Result (POWER) Register (Address = 8h) [reset = 0h]**


The POWER register is shown in Table 6-12.


Return to the Summary Table.



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



**Table 6-12. POWER Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|23-0|POWER|R|0h|Calculated power output.<br>Output value in watts.<br>Unsigned representation. Positive value.<br>Value description underSection 7.1.2.|



**6.6.1.9 Diagnostic Flags and Alert (DIAG_ALRT) Register (Address = Bh) [reset = 0001h]**


The DIAG_ALRT register is shown in Table 6-13.


Return to the Summary Table.


**Table 6-13. DIAG_ALRT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|ALATCH|R/W|0h|When the Alert Latch Enable bit is set to Transparent mode, the<br>Alert pin and Flag bit reset to the idle state when the fault has been<br>cleared.<br>When the Alert Latch Enable bit is set to Latch mode, the Alert pin<br>and Alert Flag bit remain active following a fault until the DIAG_ALRT<br>Register has been read.<br>0h = Transparent<br>1h = Latched|
|14|CNVR|R/W|0h|Setting this bit high configures the Alert pin to be asserted when<br>the Conversion Ready Flag (bit 1) is asserted, indicating that a<br>conversion cycle has completed.<br>0h = Disable conversion ready flag on ALERT pin<br>1h = Enables conversion ready flag on ALERT pin|
|13|SLOWALERT|R/W|0h|When enabled, ALERT function is asserted on the completed<br>averaged value.<br>This gives the flexibility to delay the ALERT until after the averaged<br>value.<br>0h = ALERT comparison on non-averaged (ADC) value<br>1h = ALERT comparison on averaged value|
|12|APOL|R/W|0h|Alert Polarity bit sets the Alert pin polarity.<br>0h = Normal (Active-low, open-drain)<br>1h = Inverted (active-high, open-drain )|
|11-10|RESERVED|R|0h|Reserved. Always read 0.|
|9|MATHOF|R|0h|This bit is set to 1 if an arithmetic operation resulted in an overflow<br>error.<br>The bit indicates that current and power data can be invalid.<br>0h = Normal<br>1h = Overflow<br>Must be manually cleared by triggering another conversion.|
|8|RESERVED|R|0h|Reserved. Always read 0.|
|7|TMPOL|R|0h|This bit is set to 1 if the temperature measurement exceeds the<br>threshold limit in the temperature over-limit register.<br>0h = Normal<br>1h = Over Temp Event<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register.|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 25


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**Table 6-13. DIAG_ALRT Register Field Descriptions (continued)**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|6|SHNTOL|R|0h|This bit is set to 1 if the shunt voltage measurement exceeds the<br>threshold limit in the shunt over-limit register.<br>0h = Normal<br>1h = Over Shunt Voltage Event<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register.|
|5|SHNTUL|R|0h|This bit is set to 1 if the shunt voltage measurement falls below the<br>threshold limit in the shunt under-limit register.<br>0h = Normal<br>1h = Under Shunt Voltage Event<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register.|
|4|BUSOL|R|0h|This bit is set to 1 if the bus voltage measurement exceeds the<br>threshold limit in the bus over-limit register.<br>0h = Normal<br>1h = Bus Over-Limit Event<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register.|
|3|BUSUL|R|0h|This bit is set to 1 if the bus voltage measurement falls below the<br>threshold limit in the bus under-limit register.<br>0h = Normal<br>1h = Bus Under-Limit Event<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register.|
|2|POL|R|0h|This bit is set to 1 if the power measurement exceeds the threshold<br>limit in the power limit register.<br>0h = Normal<br>1h = Power Over-Limit Event<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register.|
|1|CNVRF|R|0h|This bit is set to 1 if the conversion is completed.<br>0h = Normal<br>1h = Conversion is complete<br>When ALATCH =1 this bit is cleared by reading or writing to this<br>register, or starting a new triggered conversion.|
|0|MEMSTAT|R|1h|This bit is set to 0 if a checksum error is detected in the device trim<br>memory space.<br>0h = Memory Checksum Error<br>1h = Normal Operation|



**6.6.1.10 Shunt Overvoltage Threshold (SOVL) Register (Address = Ch) [reset = 7FFFh]**


If negative values are entered in this register, then a shunt voltage measurement of 0 V trips this alarm. When
using negative values for the shunt under and overvoltage thresholds be aware that the over voltage threshold
must be set to the larger (that is, less negative) of the two values. The SOVL register is shown in Table 6-14.


Return to the Summary Table.


**Table 6-14. SOVL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|SOVL|R/W|7FFFh|Sets the threshold for comparison of the value to detect Shunt<br>Overvoltage (overcurrent protection). Two's complement value.<br>Conversion Factor: 5 µV/LSB whenADCRANGE = 0<br>1.25 µV/LSB whenADCRANGE = 1.|



26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



**6.6.1.11 Shunt Undervoltage Threshold (SUVL) Register (Address = Dh) [reset = 8000h]**


The SUVL register is shown in Table 6-15.


Return to the Summary Table.


**Table 6-15. SUVL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|SUVL|R/W|8000h|Sets the threshold for comparison of the value to detect Shunt<br>Undervoltage (undercurrent protection). Two's complement value.<br>Conversion Factor: 5 µV/LSB whenADCRANGE = 0<br>1.25 µV/LSB whenADCRANGE = 1.|



**6.6.1.12 Bus Overvoltage Threshold (BOVL) Register (Address = Eh) [reset = 7FFFh]**


The BOVL register is shown in Table 6-16.


Return to the Summary Table.


**Table 6-16. BOVL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|Reserved|R|0h|Reserved. Always reads 0.|
|14-0|BOVL|R/W|7FFFh|Sets the threshold for comparison of the value to detect Bus<br>Overvoltage (overvoltage protection). Unsigned representation,<br>positive value only. Conversion factor: 3.125 mV/LSB.|



**6.6.1.13 Bus Undervoltage Threshold (BUVL) Register (Address = Fh) [reset = 0h]**


The BUVL register is shown in Table 6-17.


Return to the Summary Table.


**Table 6-17. BUVL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|Reserved|R|0h|Reserved. Always reads 0.|
|14-0|BUVL|R/W|0h|Sets the threshold for comparison of the value to detect Bus<br>Undervoltage (undervoltage protection). Unsigned representation,<br>positive value only. Conversion factor: 3.125 mV/LSB.|



**6.6.1.14 Temperature Over-Limit Threshold (TEMP_LIMIT) Register (Address = 10h) [reset = 7FFFh]**


The TEMP_LIMIT register is shown in Table 6-18.


Return to the Summary Table.


**Table 6-18. TEMP_LIMIT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-4|TOL|R/W|7FFh|Sets the threshold for comparison of the value to detect over<br>temperature measurements. Two's complement value.<br>The value entered in this field compares directly against the value<br>from the DIETEMP register to determine if an over temperature<br>condition exists. Conversion factor: 125 m°C/LSB.|
|3-0|Reserved|R|0|Reserved, always reads 0|



**6.6.1.15 Power Over-Limit Threshold (PWR_LIMIT) Register (Address = 11h) [reset = FFFFh]**


The PWR_LIMIT register is shown in Table 6-19.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 27


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


Return to the Summary Table.


**Table 6-19. PWR_LIMIT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|POL|R/W|FFFFh|Sets the threshold for comparison of the value to detect power over-<br>limit measurements. Unsigned representation, positive value only.<br>The value entered in this field compares directly against the value<br>from the POWER register to determine if an over power condition<br>exists. Conversion factor: 256 × Power LSB.|



**6.6.1.16 Manufacturer ID (MANUFACTURER_ID) Register (Address = 3Eh) [reset = 5449h]**


The MANUFACTURER_ID register is shown in Table 6-20.


Return to the Summary Table.


**Table 6-20. MANUFACTURER_ID Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|MANFID|R|5449h|Reads back TI in ASCII.|



**6.6.1.17 Device ID (DEVICE_ID) Register (Address = 3Fh) [reset = 2381h]**


The DEVICE_ID register is shown in Table 6-21.


Return to the Summary Table.


**Table 6-21. DEVICE_ID Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-4|DIEID|R|238h|Stores the device identification bits.|
|3-0|REV_ID|R|1h|Device revision identification.|



28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


**7 Application and Implementation**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**7.1 Application Information**

_**7.1.1 Device Measurement Range and Resolution**_


The INA238 device supports two input ranges for the shunt voltage measurement. The supported full scale
differential input across the IN+ and IN– pins can be either ±163.84 mV or ±40.96 mV depending on the
ADCRANGE bit in CONFIG register. The range for the bus voltage measurement is from 0 V to 85 V. The
internal die temperature sensor range extends from –256 °C to +256 °C but is limited by the package to –40 °C
to 125 °C.


Table 7-1 provides a description of full scale voltage on shunt, bus, and temperature measurements, along with
the associated step size.


**Table 7-1. ADC Full Scale Values**







|PARAMETER|FULL SCALE VALUE|RESOLUTION|
|---|---|---|
|Shunt voltage|±163.84 mV (ADCRANGE = 0)|5 µV/LSB|
|Shunt voltage|±40.96 mV (ADCRANGE = 1)|1.25 µV/LSB|
|Bus voltage|0 V to 85 V|3.125 mV/LSB|
|Temperature|–40 °C to +125 °C|125 m°C/LSB|


The device shunt voltage measurements, bus voltage, and temperature measurements can be read through the
VSHUNT, VBUS, and DIETEMP registers, respectively. The digital output in VSHUNT and VBUS registers is
16-bits. The shunt voltage measurement can be positive or negative due to bidirectional currents in the system;
therefore the data value in VSHUNT can be positive or negative. The VBUS data value is always positive. The
output data can be directly converted into voltage by multiplying the digital value by the respective resolution
size. The digital output in the DIETEMP register is 12-bit and can be directly converted to °C by multiplying by
the above resolution size. This output value can also be positive or negative.


Furthermore, the device provides the flexibility to report calculated current in Amperes, power in Watts as
described in Section 7.1.2.


_**7.1.2 Current and Power Calculations**_


For the INA238 device to report current values in Ampere units, a constant conversion value must be written
in the SHUNT_CAL register that is dependent on the maximum measured current and the shunt resistance
used in the application. The SHUNT_CAL register is calculated based on the first equation in this section.
The term CURRENT_LSB is the LSB step size for the CURRENT register where the current in Amperes is
stored. The value of CURRENT_LSB is based on the maximum expected current as shown in the second
equation in this section. This value directly defines the resolution of the CURRENT register. While the smallest
CURRENT_LSB value yields highest resolution, selecting a higher round-number (no higher than 8x) value for
the CURRENT_LSB is common for simplifying the conversion of the CURRENT.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 29


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


The RSHUNT term is the resistance value of the external shunt used to develop the differential voltage across
the IN+ and IN– pins. Use the following equation for ADCRANGE = 0. For ADCRANGE = 1, the value of
SHUNT_CAL must be multiplied by 4.


SHUNT_CAL = 819.2 × 10 [6] × CURENT_LSB × RSHUNT (1)


where

 - 819.2 × 10 [6] is an internal fixed value used to verify that scaling is maintained properly.

 - the value of SHUNT_CAL must be multiplied by 4 for ADCRANGE = 1.


Current_LSB = [Maximum Expected Current] (2)

2 [15]


Note that the current is calculated following a shunt voltage measurement based on the value set in the
SHUNT_CAL register. If the value loaded into the SHUNT_CAL register is zero, the current value reported
through the CURRENT register is also zero.


After programming the SHUNT_CAL register with the calculated value, the measured current in Amperes can be
read from the CURRENT register. The final value is scaled by CURRENT_LSB and calculated in the following
equation:


Current A = CURRENT_LSB × CURRENT (3)


where


 - CURRENT is the value read from the CURRENT register


The power value can be read from the POWER register as a 24-bit value and converted to Watts by using the
following equation:


Power W = 0.2 × CURRENT_LSB × POWER (4)


where


 - POWER is the value read from the POWER register.

 - CURRENT_LSB is the lsb size of the current calculation as defined by Equation 2.


For a design example using these equations refer to Section 7.2.2.


_**7.1.3 ADC Output Data Rate and Noise Performance**_


The INA238 noise performance and effective resolution depend on the ADC conversion time. The device
also supports digital averaging which can further help decrease digital noise. The flexibility of the device to
select ADC conversion time and data averaging offers increased signal-to-noise ratio and achieves the highest
dynamic range with lowest offset. The profile of the noise at lower signals levels is dominated by the system
noise that is comprised mainly of 1/f noise or white noise. The INA238 effective resolution of the ADC can be
increased by increasing the conversion time and increasing the number of averages.


Table 7-2 summarizes the output data rate conversion settings supported by the device. The fastest conversion
setting is 50 µs. Typical noise-free resolution is represented as Effective Number of Bits (ENOB) based on
device measured data. The ENOB is calculated based on noise peak-to-peak values, which verifies that full
noise distribution is taken into consideration.


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)


**Table 7-2. INA238 Noise Performance**







































|ADC CONVERSION<br>TIME PERIOD [µs]|OUTPUT SAMPLE<br>AVERAGING [SAMPLES]|OUTPUT SAMPLE PERIOD<br>[ms]|NOISE-FREE ENOB<br>(±163.84-mV)<br>(ADCRANGE = 0)|NOISE-FREE ENOB<br>(±40.96-mV)<br>(ADCRANGE = 1)|
|---|---|---|---|---|
|50|1|0.05|12.5|9.9|
|84|84|0.084|12.7|10.5|
|150|150|0.15|13.4|11.4|
|280|280|0.28|13.7|12.2|
|540|540|0.54|14.1|12.4|
|1052|1052|1.052|14.1|12.7|
|2074|2074|2.074|15.7|13.1|
|4120|4120|4.12|15.7|13.4|
|50|4|0.2|12.7|10.6|
|84|84|0.336|13.7|11.4|
|150|150|0.6|14.1|12.2|
|280|280|1.12|14.7|12.7|
|540|540|2.16|15.7|13.4|
|1052|1052|4.208|15.7|14.1|
|2074|2074|8.296|15.7|14.7|
|4120|4120|16.48|15.7|14.7|
|50|16|0.8|13.7|11.5|
|84|84|1.344|15.7|12.7|
|150|150|2.4|15.7|13.4|
|280|280|4.48|15.7|13.7|
|540|540|8.64|15.7|14.1|
|1052|1052|16.832|15.7|14.7|
|2074|2074|33.184|15.7|15.7|
|4120|4120|65.92|16.0|15.7|
|50|64|3.2|15.7|12.5|
|84|84|5.376|15.7|13.7|
|150|150|9.6|15.7|14.7|
|280|280|17.92|15.7|14.7|
|540|540|34.56|16.0|14.7|
|1052|1052|67.328|16.0|15.7|
|2074|2074|132.736|16.0|15.7|
|4120|4120|263.68|16.0|15.7|
|50|128|6.4|15.7|13.1|
|84|84|10.752|15.7|14.1|
|150|150|19.2|15.7|14.7|
|280|280|35.84|16.0|15.7|
|540|540|69.12|16.0|15.7|
|1052|1052|134.656|16.0|15.7|
|2074|2074|265.472|16.0|15.7|
|4120|4120|527.36|16.0|16.0|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 31


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**Table 7-2. INA238 Noise Performance (continued)**





























|ADC CONVERSION<br>TIME PERIOD [µs]|OUTPUT SAMPLE<br>AVERAGING [SAMPLES]|OUTPUT SAMPLE PERIOD<br>[ms]|NOISE-FREE ENOB<br>(±163.84-mV)<br>(ADCRANGE = 0)|NOISE-FREE ENOB<br>(±40.96-mV)<br>(ADCRANGE = 1)|
|---|---|---|---|---|
|50|256|12.8|15.7|13.7|
|84|84|21.504|15.7|14.7|
|150|150|38.4|15.7|15.7|
|280|280|71.68|16.0|15.7|
|540|540|138.24|16.0|15.7|
|1052|1052|269.312|16.0|16.0|
|2074|2074|530.944|16.0|16.0|
|4120|4120|1054.72|16.0|16.0|
|50|512|25.6|15.7|14.1|
|84|84|43|16.0|15.7|
|150|150|76.8|16.0|15.7|
|280|280|143.36|16.0|15.7|
|540|540|276.48|16.0|15.7|
|1052|1052|538.624|16.0|16.0|
|2074|2074|1061.888|16.0|16.0|
|4120|4120|2109.44|16.0|16.0|
|50|1024|51.2|15.7|14.7|
|84|84|86.016|15.7|15.7|
|150|150|153.6|16.0|16.0|
|280|280|286.72|16.0|16.0|
|540|540|552.96|16.0|16.0|
|1052|1052|1077.248|16.0|16.0|
|2074|2074|2123.776|16.0|16.0|
|4120|4120|4218.88|16.0|16.0|


_**7.1.4 Input Filtering Considerations**_


As previously discussed, INA238 offers several options for noise filtering by allowing the user to select the
conversion times and number of averages independently in the ADC_CONFIG register. The conversion times
can be set independently for the shunt voltage and bus voltage measurements to allow added flexibility in
monitoring of the power-supply bus.


The internal ADC has good inherent noise rejection; however, the transients that occur at or very close to the
sampling rate harmonics can cause problems. Because these signals are at 1 MHz and higher, the signals can
be managed by incorporating filtering at the input of the device. Filtering high frequency signals enables the use
of low-value series resistors on the filter with negligible effects on measurement accuracy. For best results, filter
using the lowest possible series resistance (typically 100 Ω or less) and a ceramic capacitor. Recommended
values for this capacitor are between 0.1 µF and 1 µF. Figure 7-1 shows the device with a filter added at the
input.


Overload conditions are another consideration for the device inputs. The device inputs are specified to tolerate
±40 V differential across the IN+ and IN– pins. A large differential scenario can be a short to ground on the load
side of the shunt. This type of event can result in full power-supply voltage across the shunt (as long the power
supply or energy storage capacitors support the voltage). Removing a short to ground can result in inductive
kickbacks that can exceed the 40-V differential or 85-V common-mode absolute maximum rating of the device.
Inductive kickback voltages are best controlled by Zener-type transient-absorbing devices (commonly called
_transzorbs_ ) combined with sufficient energy storage capacitance. See the _[Transient Robustness for Current](https://www.ti.com/lit/pdf/TIDU473)_


32 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



_[Shunt Monitors](https://www.ti.com/lit/pdf/TIDU473)_ reference design which describes a high-side current shunt monitor used to measure the voltage
developed across a current-sensing resistor when current passes through the resistor.


In applications that do not have large energy storage, electrolytic capacitors on one or both sides of the shunt,
an input overstress condition can result from an excessive dV/dt of the voltage applied to the input. A hard
physical short is the most likely cause of this event. This problem occurs because an excessive dV/dt can
activate the ESD protection in the device in systems where large currents are available. Testing demonstrates
that the addition of 10-Ω resistors in series with each input of the device sufficiently protects the inputs against
this dV/dt failure up to the 40-V maximum differential voltage rating of the device. Selecting these resistors in the
range noted has minimal effect on accuracy.





















**Figure 7-1. Input Filtering**


Do not use values greater than 100Ω for RFILTER. A resistor higher than 100Ω can degrade gain error and
increase non-linearity.


**7.2 Typical Application**


The low offset voltage and low input bias current of the INA238 allow accurate monitoring of a wide range of
currents. To accurately monitor currents with high resolution, select the value of the shunt resistor so that the
resulting sense voltage is close to the maximum allowable differential input voltage range (either ±163.84 mV
or ±40.96 mV, depending on register settings). The circuit for monitoring currents in a high-side configuration is
shown in Figure 7-2.


VS = 2.7V± 5.5V VS















_To_















**Figure 7-2. INA238 High-Side Sensing Application Diagram**


_**7.2.1 Design Requirements**_


The INA238 measures the voltage developed across a current-sensing resistor (RSHUNT) when current passes
through the device. The device also measures the bus supply voltage and calculates power when calibrated.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 33


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


The device also comes with alert capability, where the alert pin can be programmed to respond to a user-defined
event or a conversion ready notification.


The design requirements for the circuit shown in Figure 7-2 are listed in Table 7-3.


**Table 7-3. Design Parameters**

|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|Power-supply voltage (VS)|5 V|
|Bus supply rail (VCM)|48 V|
|Bus supply rail over voltage fault threshold|52 V|
|Average Current|6 A|
|Overcurrent fault threshold (IMAX)|10 A|
|ADC Range Selection (VSENSE_MAX)|±163.84 mV|
|Temperature|25 ºC|



_**7.2.2 Detailed Design Procedure**_

**7.2.2.1 Select the Shunt Resistor**


Using values from Table 7-3, the maximum value of the shunt resistor is calculated based on the value of
the maximum current to be sensed (IMAX) and the maximum allowable sense voltage (VSENSE_MAX) for the
chosen ADC range. When operating at the maximum current, the differential input voltage must not exceed the
maximum full scale range of the device, VSENSE_MAX. Using Equation 5 for the given design parameters, the
maximum value for RSHUNT is calculated to be 16.38 mΩ. The closest standard resistor value that is smaller than
the maximum calculated value is 16.2 mΩ. Also keep in mind that RSHUNT must be able to handle the power
dissipated across the resistor in the maximum load condition.



RSHUNT <



VSENSE_MAX ~~I~~ MAX (5)



**7.2.2.2 Configure the Device**


The first step to program the INA238 is to properly set the device and ADC configuration registers. On initial
power up the CONFIG and ADC_CONFIG registers are set to the reset values as shown in Table 6-5 and
Table 6-6. In this default power on state the device is set to measured on the ±163.84 mV range with the ADC
continuously converting the shunt voltage, bus voltage, and temperature. If the default power up conditions do
not meet the design requirements, these registers needs to be set properly after each VS power cycle event.


**7.2.2.3 Program the Shunt Calibration Register**


The shunt calibration register needs to be correctly programmed at each VS power up for the device to properly
report any result based on current. The first step in properly setting this register is to calculate the LSB value for
the current by using Equation 2. Applying this equation with the maximum expected current of 10 A results in an
LSB size of 305.1758 μA. Applying Equation 1 to the CURRENT_LSB and selected value for the shunt resistor
results in a shunt calibration register setting of 4050d (FD2h). Failure to set the value of the shunt calibration
register results in a zero value for any result based on current.


**7.2.2.4 Set Desired Fault Thresholds**


Fault thresholds are set by programming the desired trip threshold into the corresponding fault register. The list
of supported fault registers is shown in Table 6-1.


An over current threshold is set by programming the shunt over voltage limit register (SOVL). The voltage that
needs to be programmed into this register is calculated by multiplying the over current threshold by the shunt
resistor. In this example the over current threshold is 10 A and the value of the current sense resistor is 16.2 mΩ,
which give a shunt voltage limit of 162 mV. Once the shunt voltage limit is known, the value for the shunt over
voltage limit register is calculated by dividing the shunt voltage limit by the shunt voltage LSB size.


In this example, the calculated value of the shunt over voltage limit register is 162 mV / 5 μV = 32400d (7E90h).


34 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**



**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)



An over voltage fault threshold on the bus voltage is set by programming the bus over voltage limit register
(BOVL). In this example the desired over voltage threshold is 52 V. The value that needs to be programmed into
this register is calculated by dividing the target threshold voltage by the bus voltage fault limit LSB value of 3.125
mV. For this example, the target value for the BOVL register is 52 V / 3.125 mV = 16640d (4100h).


When setting the power over-limit value, the LSB size used to calculate the value needed in the limit registers
are 256 times greater than the power LSB. This is because the power register is a 24 bits in length while the
power fault limit register is 16 bits.


Values stored in the alert limit registers are set to the default values after VS power cycle events and need to be
reprogrammed each time power is applied.


**7.2.2.5 Calculate Returned Values**


Parametric values are calculated by multiplying the returned value by the LSB value. Table 7-4 below shows the
returned values for this application example assuming the design requirements shown in Table 7-3.


**Table 7-4. Calculating Returned Values**

|PARAMETER|Returned Value|LSB Value|Calculated Value|
|---|---|---|---|
|Shunt voltage (V)|19440d|5 µV/LSB|0.0972 V|
|Current (A)|19660d|10 A/215 = 305.176 µA/LSB|5.9997 A|
|Bus voltage (V)|15360d|3.125 mV/LSB|48 V|
|Power (W)|4718604d|Current LSB x 0.2 = 61.035156 µW/LSB|288 W|
|Temperature (°C)|200d|125 m°C/LSB|25°C|



Shunt Voltage, Current, Bus Voltage (positive only), and Temperature return values in two's complement format.
In two's complement format a negative value in binary is represented by having a 1 in the most significant bit
of the returned value. These values can be converted to decimal by first inverting all the bits and adding 1 to
obtain the unsigned binary value. This value must then be converted to decimal with the negative sign applied.
For example, assume a shunt voltage reading returns 1011 0100 0001 0000. This is a negative value due to the
MSB having a value of one. Inverting the bits and adding one results in 0100 1011 1111 0000 (19440d) which
from the shunt voltage example in Table 7-4 correlates to a voltage of 97.2 mV. Since the returned value is
negative the measured shunt voltage value is -97.2 mV.


_**7.2.3 Application Curves**_


Figure 7-3 and Figure 7-4 show the ALERT pin response to a bus overvoltage fault with a conversion time of
50 μs, averaging set to 1, and the SLOWALERT bit set to 0 for bus only conversions. For these scope shots,
persistence is enabled on the ALERT channel to show the variation in the alert response for many sequential
fault events. If the magnitude of the fault is sufficient the ALERT response can be as fast as one quarter of the
ADC conversion time as shown in Figure 7-3. For fault conditions that are just exceeding the limit threshold, the
response time for the ALERT pin can vary from approximately 0.5 to 1.5 conversion cycles as shown in Figure
7-4. Variation in the alert response exists because the external fault event is not synchronized to the internal
ADC conversion start. Also the ADC is constantly sampling to get a result, so the response time for fault events
starting from zero is slower than fault events starting from values near the set fault threshold. Because the timing
of the alert can be difficult to predict, in applications where the alert timing is critical, expect an alert response
equal to 1.5 times the ADC conversion time for bus voltage or shunt voltage only conversions.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 35


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**











**7.3 Power Supply Recommendations**





The input circuitry of the device can accurately measure signals on common-mode voltages beyond the powersupply voltage, VS. For example, the voltage applied to the VS power supply terminal can be 5 V, whereas the
load power-supply voltage being monitored (the common-mode voltage) can be as high as 85 V. Note that the
device can also withstand the full 0 V to 85 V range at the input terminals, regardless of whether the device has
power applied or not. Avoid applications where the GND pin is disconnected while device is actively powered.


Place the required power-supply bypass capacitors as close as possible to the supply and ground terminals of
the device. A typical value for this supply bypass capacitor is 0.1 µF. Applications with noisy or high-impedance
power supplies can require additional decoupling capacitors to reject power-supply noise.


**7.4 Layout**

_**7.4.1 Layout Guidelines**_


Connect the input pins (IN+ and IN–) to the sensing resistor using a Kelvin connection or a 4-wire connection.
This connection technique verifies that only the current-sensing resistor impedance is sensed between the input
pins. Poor routing of the current-sensing resistor commonly results in additional resistance present between
the input pins. Given the very low ohmic value of the current-sensing resistor, any additional high-current
carrying impedance causes significant measurement errors. Place the power-supply bypass capacitor as close
as possible to the supply and ground pins.


36 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[www.ti.com](https://www.ti.com)**


_**7.4.2 Layout Example**_


Alert output
(2)


I [2] C
interface











**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025)


Via to Ground Plane


Via to Power Plane





(1) Connect the VBUS pin to the voltage powering the load for load power calculations..
(2) Can be left floating if unused.


**Figure 7-5. INA238 Layout Example**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ 37


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


**[INA238](https://www.ti.com/product/INA238)**
[SLYS025B – JANUARY 2021 – REVISED MAY 2025](https://www.ti.com/lit/pdf/SLYS025) **[www.ti.com](https://www.ti.com)**


**8 Device and Documentation Support**

**8.1 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Notifications_ to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.


**8.2 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**8.3 Trademarks**
TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.
**8.4 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**8.5 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**9 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision A (May 2022) to Revision B (May 2025)** **Page**

 - Updated the numbering format for tables, figures, and cross-references throughout the document................. 1

 - Updated equation to calculate notch frequency in _Low Latency Digital Filter_ ................................................. 14

 - Changed bits 0-7 in DIAG_ALRT Register table from R/W to R...................................................................... 21


**Changes from Revision * (January 2021) to Revision A (May 2022)** **Page**

 - Updated the numbering format for tables, figures, and cross-references throughout the document................. 1

 - Updated the figures and equations throughput the document to align with the commercial data sheet............ 1

 - Changed the Shunt Calibration (SHUNT_CAL) register 14-0 bit name from CURRLSB to SHUNT_CAL.......21

 - Changed the Device ID (DEVICE_ID) register reset value.............................................................................. 21

 - Changed the TOL 15-4 bit reset value from 7FF0h to 7FFh ........................................................................... 21

 - Changed the equation definition list in _Current Calculation_ section................................................................. 29


**10 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


38 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLYS025B&partnum=INA238)_ Copyright © 2025 Texas Instruments Incorporated


Product Folder Links: _[INA238](https://www.ti.com/product/ina238?qgpn=ina238)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 31-Dec-2025


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

**[OTHER QUALIFIED VERSIONS OF INA238 :]**

- [[Automotive : ][INA238-Q1]](http://focus.ti.com/docs/prod/folders/print/ina238-q1.html)


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 31-Dec-2025


[NOTE: Qualified Version Definitions:]

    - [Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects]


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 1-Jan-2026


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
|INA238AIDGSR|VSSOP|DGS|10|2500|330.0|12.4|5.25|3.35|1.25|8.0|12.0|Q1|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 1-Jan-2026





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|INA238AIDGSR|VSSOP|DGS|10|2500|366.0|364.0|50.0|



Pack Materials-Page 2


## **PACKAGE OUTLINE**
# DGS0010A SCALE 3.200 VSSOP - 1.1 mm max height

SMALL OUTLINE PACKAGE























NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-187, variation BA.


www.ti.com


## **EXAMPLE BOARD LAYOUT**
# **DGS0010A VSSOP - 1.1 mm max height**

SMALL OUTLINE PACKAGE

















NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com




## **EXAMPLE STENCIL DESIGN**
# **DGS0010A VSSOP - 1.1 mm max height**

SMALL OUTLINE PACKAGE















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


