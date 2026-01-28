**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)
## **INA236 48-V, 16-Bit, Ultra-Precise, Current, Voltage, and Power Monitor With an I [2] C** **Interface**



**1 Features**


- High-side or low-side current sensing

- Operates from a 1.7-V to 5.5-V power supply

- Reports current, voltage and power

- Programmable full scale range: 20mV / 80mV

- Input common mode range: –0.3 V to 48 V

- Current monitoring accuracy:

– 16-bit ADC resolution

–
0.1% gain error (maximum)

–
5-µV offset (maximum)

- Low input bias current: 10 nA (maximum)

- Configurable averaging options

- General call addressing allows conversion
synchronization among devices

- Alert limits for over and under current events

- 1.2-V compliant I [2] C, SMBus interface

- Two device address options with a 4-pin selectable
address

- DSBGA-8 Package (0.745 mm × 1.508 mm)

- SOT23-8 Package

- Operating temperature: –40°C and +125°C


**2 Applications**


- [Mobile phones](https://www.ti.com/applications/personal-electronics/mobile-phones/overview.html)

- [Smart speakers](https://www.ti.com/solution/smart-speaker)

- [Wearables](https://www.ti.com/applications/personal-electronics/wearables/overview.html)

- [Battery chargers](https://www.ti.com/power-management/battery-management/charger-ics/products.html)

- [Power management](https://www.ti.com/power-management/overview.html)

- [Battery cell monitors and balancers](https://www.ti.com/power-management/battery-management/monitors-balancers/overview.html)

- [Rack servers](https://www.ti.com/solution/rack-server)



**3 Description**


The INA236 device is a 16-bit digital current monitor
with an I [2] C/SMBus-compatible interface that is
compliant with a wide range of digital bus voltages
such as 1.2 V, 1.8 V, 3.3 V, and 5.0 V. The device
monitors the voltage across an external sense resistor
and reports values for current, bus voltage, and

power.


The INA236 features programmable ADC conversion
times and averaging. The device also has a
programmable calibration value with an internal
multiplier that enables direct readouts of current in
amperes and power in watts. The device monitors
the bus voltage present on the IN– pin and can
alert on overcurent and undercurrent conditions as

well as overvoltage and undervoltage conditions. High
input impedance while in current measurement mode
allows use of larger current sense resistors needed to
measure small value system currents.


The INA236 senses current on common-mode bus
voltages that can vary from –0.3 V to 48 V,
independent of the supply voltage. The device
operates from a single 1.7-V to 5.5-V supply, drawing
a typical supply current of 300 µA in normal operation.
The device can be placed in a low-power standby
mode where the typical operating current is 2.2 µA.


**Package Information** [(1) ]






|PART NUMBER(2)|PACKAGE|BODY SIZE (NOM)|
|---|---|---|
|INA236|DSBGA (8)|0.745 mm × 1.508 mm|
|INA236|SOT-23 (8)|1.60 mm × 2.90 mm|



(1) For all available packages, see the package option
addendum at the end of the data sheet.
(2) The INA236 is available in A and B device address options.
See Table 7-1 for address differences between the A and B

devices.


Supply Voltage
(1.7 V to 5.5 V)





High
Shunt


Low
Shunt













GND

|CBYPASS<br>us Voltage 0.1 µF<br>.3 V to 48 V)<br>TI Device<br>dh e- VS<br>nt<br>SDA<br>SCL<br>Load x Power Register<br>V I2C-, SMBus-,<br>IN+ Current Register Compatible<br>w- ADC Interface<br>d ne t IN- I Voltage Register ALERT<br>A0<br>Alert Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x||||
|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|
|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>C<br>0.1 µF<br>BYPASS<br>h-<br>de<br>nt<br>w-<br>de<br>nt<br>Load<br>Alert Register<br>VS<br>us Voltage<br>.3 V to 48 V)<br>IN-<br>**TI Device**<br>IN+<br>Power Register<br>x|Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br><br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|SCL|||||
|Loa|Loa|Loa||||||
|w-<br>de<br>nt|w-<br>de<br>nt|w-<br>de<br>nt|w-<br>de<br>nt|w-<br>de<br>nt|w-<br>de<br>nt|w-<br>de<br>nt|w-<br>de<br>nt|
|w-<br>de<br>nt|IN-||A0<br>ALERT|||||
|w-<br>de<br>nt|IN-||A0<br>ALERT|||||



**High-Side or Low-Side Sensing Application**


An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


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
6.4 Thermal Information....................................................4

6.5 Electrical Characteristics.............................................5
6.6 Timing Requirements (I [2] C)......................................... 7
6.7 Timing Diagram ..........................................................7
6.8 Typical Characteristics................................................ 8
**7 Detailed Description** ......................................................12

7.1 Overview................................................................... 12

7.2 Functional Block Diagram......................................... 12
7.3 Feature Description...................................................12


**4 Revision History**



7.4 Device Functional Modes..........................................14

7.5 Programming............................................................ 16
7.6 Register Maps...........................................................19
**8 Application and Implementation** .................................. 24

8.1 Application Information............................................. 24
8.2 Typical Application.................................................... 28
8.3 Power Supply Recommendations.............................31
8.4 Layout....................................................................... 31
**9 Device and Documentation Support** ............................33

9.1 Device Support......................................................... 33
9.2 Documentation Support............................................ 33
9.3 Receiving Notification of Documentation Updates....33
9.4 Support Resources................................................... 33
9.5 Trademarks............................................................... 33
9.6 Electrostatic Discharge Caution................................33
9.7 Glossary....................................................................33
**10 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 33



**Changes from Revision C (December 2022) to Revision D (August 2023)** **Page**

 - Changed Integral Non-Linearity typical value from ±2m% to ±1.5m%............................................................... 5

 - Added Integral Non-Linearity maximum value of ±6m%.....................................................................................5


**Changes from Revision B (May 2022) to Revision C (December 2022)** **Page**

 - Added DDF package.......................................................................................................................................... 1

 - Updated Table 7-1 to show the INA236 device options ................................................................................... 16


**Changes from Revision A (August 2021) to Revision B (May 2022)** **Page**

 - Changed Figure 6-18 .........................................................................................................................................8

 - Changed the full recovery time from power-down mode from: 40 ms to: 100 µs............................................. 15


**Changes from Revision * (May 2021) to Revision A (August 2021)** **Page**

 - Changed data sheet title from: INA236 48-V, 16-Bit, High-Precision, Current, Voltage, and Power Monitor with
an I2C Interface to: INA236 48-V, 16-Bit, Ultra-Precise, Current, Voltage, and Power Monitor with an I2C
Interface..............................................................................................................................................................1

 - Changed data sheet status from Advanced Information to Production Data......................................................1


2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**5 Pin Configuration and Functions**


1 2



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)

|Col1|1 8<br>2 7<br>3 6<br>4 5|Col3|
|---|---|---|
||||
||||
||||
||||
||||
||||
||||
||||



Not to scale

**Figure 5-2. DDF Package8-Pin SOT-23 (Top View)**



A


B


C


D





Not to scale


**Figure 5-1. YBJ Package 8-Bump DSBGA (Top**

**View)**


**Table 5-1. Pin Functions**



















|PIN|Col2|Col3|TYPE|DESCRIPTION|
|---|---|---|---|---|
|**NAME**|**DDF (SOT-23)**|**YBJ (DSBGA)**|**YBJ (DSBGA)**|**YBJ (DSBGA)**|
|A0|7|B1|Digital input|Address pin. Connect to GND, SCL, SDA, or VS.Table 7-1 lists the pin<br>settings and corresponding addresses.|
|ALERT|8|A1|Digital output|Multifunctional alert, open-drain output. This pin alerts to report fault<br>conditions or can be configured to notify host when a conversion is<br>complete.|
|GND|3|C2|Ground|Ground for both analog and digital.|
|IN–|2|B2|Analog input|Current sensing negative input. For high-side applications, connect to load<br>side of sense resistor. For low-side applications, connect to ground side of<br>sense resistor. Bus voltage measurements are made with respect to this<br>pin.|
|IN+|1|A2|Analog input|Current sensing positive input. For high-side applications, connect to bus<br>voltage side of sense resistor. For low-side applications, connect to load<br>side of sense resistor.|
|SCL|5|D1|Digital input|Serial bus clock line, open-drain input.|
|SDA|6|C1|Digital<br>input/output|Serial bus data line, open-drain input/output|
|VS|4|D2|Power Supply|Power supply, 1.7 V to 5.5 V|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 3


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**6 Specifications**
**6.1 Absolute Maximum Ratings**
over operating free-air temperature range (unless otherwise noted) [(1)]







|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|Vs|Supply Voltage|6|V|
|VIN+, VIN-|Differential (VIN+) - (VIN-)|–26<br>26|V|
|VIN+, VIN-|Common - mode|GND – 0.3<br>50|V|
|VIO|SDA, SCL, ALERT, A0|GND – 0.3<br>6|V|
||Input current into any pin|5|mA|
||Open-drain digital output current (SDA, ALERT)|10|mA|
|TA|Operating Temperature|–55<br>150|°C|
|TJ|Junction temperature|150|°C|
|Tstg|Storage temperature|–65<br>150|°C|


(1) Operation outside the _Absolute Maximum Ratings_ may cause permanent device damage. _Absolute Maximum Ratings_ do not imply
functional operation of the device at these or any other conditions beyond those listed under _Recommended Operating Conditions_ .
If used outside the _Recommended Operating Conditions_ but within the _Absolute Maximum Ratings_, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.


**6.2 ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins(1)|±2000|V|
|V(ESD)|Electrostatic discharge|Charged device model (CDM), per ANSI/ESDA/JEDEC JS-002, all<br>pins(2)|±1000|±1000|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**6.3 Recommended Operating Conditions**
over operating free-air temperature range (unless otherwise noted)

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VCM|Common-mode input range|GND – 0.3<br>48|V|
|VS|Operating supply range|1.7<br>5.5|V|
|TA|Ambient temperature|–40<br>125|°C|



**6.4 Thermal Information**







|THERMAL METRIC(1)|Col2|INA236|Col4|UNIT|
|---|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**DDF (SOT23)**|**YBJ (DSBGA)**|**YBJ (DSBGA)**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**8 PINS**|**8 PINS**|**8 PINS**|
|RθJA|Junction-to-ambient thermal resistance|146.8|62.2|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|70.5|0.5|°C/W|
|RθJB|Junction-to-board thermal resistance|67.1|20.4|°C/W|
|ΨJT|Junction-to-top characterization parameter|4.1|0.3|°C/W|
|YJB|Junction-to-board characterization parameter|66.7|20.2|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|N/A|N/A|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
report.


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



**6.5 Electrical Characteristics**

at T A = 25°C, V S = 3.3 V, V SENSE = V IN+ - V IN- = 0 mV, V IN- = V BUS = 12V (unless otherwise noted)



































|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**INPUT**|**INPUT**|**INPUT**|**INPUT**|**INPUT**|
|CMRR|Common-mode rejection|VCM = –0.3 V to 48 V, TA = –40°C to<br>125°C|136<br>150|dB|
||Shunt voltage input range|ADCRANGE = 0|–81.9175<br>81.92|mV|
||Shunt voltage input range|ADCRANGE = 1|–20.4794<br>20.48|mV|
|Vos|Shunt offset voltage|VCM = 12 V|±1<br>±5|µV|
|dVos/dT|Shunt offset voltage drift|TA = –40°C to +125°C|±5<br>±25|nV/°C|
|Vos_b|IN- bus offset Voltage||±1<br>±7.5|mV|
|dVos_b/dT|IN- bus offset voltage drift|TA = –40°C to +125°C|±10<br>±30|µV/°C|
|PSRRSHUNT|Power supply rejection ratio<br>(Current measurements)|VS = 1.7 V to 5.5 V, TA = –40°C to 125°C|±0.5<br>±2.5|µV/V|
|PSRRBUS|Power supply rejection ratio<br>(Voltage measurements)|VS = 1.7 V to 5.5 V, TA = –40°C to 125°C,<br>VIN- = 50 mV|±0.5<br>±2.5|mV/V|
|ZIN-|IN- input impedance|Bus Voltage Measurement Mode|1.05|MΩ|
|IB_SHDWN|Input Leakage|IN+, IN-, Shutdown Mode|0.1<br>5|nA|
|IB|Input bias current|IN+, IN-, Current Measurment Mode|0.1<br>10|nA|
|**DC ACCURACY**|**DC ACCURACY**|**DC ACCURACY**|**DC ACCURACY**|**DC ACCURACY**|
|RDIFF|Differential Input Impedance<br>(IN+ to IN-)|Shunt or Current Measurment<br>Modes, VIN+ - VIN- < 82 mV|140|kΩ|
||ADC Resolution|TA = –40°C to 125°C|16|Bits|
||1 LSB step size|Shunt Voltage, ADCRANGE = 0|2.5|µV|
||1 LSB step size|Shunt Voltage, ADCRANGE = 1|625|nV|
||1 LSB step size|Bus Voltage|1.6|mV|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 000|133<br>140<br>147|µs|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 001|194<br>204<br>214|µs|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 010|315<br>332<br>349|µs|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 011|559<br>588<br>617|µs|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 100|1.045<br>1.100<br>1.155|ms|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 101|2.01<br>2.116<br>2.222|ms|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 110|3.948<br>4.156<br>4.364|ms|
||ADC Conversion-time<br>(TA = –40°C to 125°C)|CT bit = 111|7.832<br>8.244<br>8.656|ms|
|GSERR|Shunt voltage gain error||±0.015<br>±0.1|%|
|GS_DRFT|Shunt voltage gain error drift|TA = –40°C to +125°C|30|ppm/°C|
|GBERR|VIN- voltage gain error||±0.015<br>±0.1|%|
|GB_DRFT|VIN- voltage gain error drift|TA = –40°C to +125°C|30|ppm/°C|
|INL|Integral Non-Linearity|ADCRANGE = 0, Linear best fit,<br>TA = –40°C to +125°C|±1.5<br>±6|m%|
|DNL|Differential Non-Linearity||±0.1|LSB|
|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|**POWER SUPPLY**|
|IQ|Quiescent current|VSENSE = 0 mV|300<br>380|µA|
|IQ|Quiescent current|IQ vs temperature, TA = –40°C to +125°C|500|µA|
|IQ|Quiescent current|Shutdown|2.2<br>3|µA|
|VPOR|Power-on reset threshold|VS falling|0.95|V|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 5


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


at T A = 25°C, V S = 3.3 V, V SENSE = V IN+ - V IN- = 0 mV, V IN- = V BUS = 12V (unless otherwise noted)

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**SMBUS**|**SMBUS**|**SMBUS**|**SMBUS**|**SMBUS**|
||SMBUS timeout||28<br>35|ms|
|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|**DIGITAL INPUT / OUTPUT**|
||Input capacitance||3|pF|
|VIH|Logic input level, high|VS = 1.7 V to 5.5 V, TA = –40°C to +125°C|0.9<br>5.5|V|
|VIL|Logic input level, low|VS = 1.7 V to 5.5 V, TA = –40°C to +125°C|0<br>0.4|V|
|VHYS|Hysteresis||130|mV|
|VOL|Logic output level, low|IOL = 3 mA, VS = 1.7 V to 5.5 V, TA =<br>–40°C to +125°C|0<br>0.3|V|
||Digital leakage input current|0 ≤ VINPUT ≤ VS|–1<br>1|µA|



6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**6.6 Timing Requirements (I** **[2]** **C)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)









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
|tR|Clock rise time (SCLK ≤ 100 kHz)|1000|ns|
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


**6.7 Timing Diagram**


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



**Figure 6-1. I** **[2]** **C Timing Diagram**

|Col1|Col2|
|---|---|
|||
||t(|
|P|P|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 7


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics**


at T A = 25°C, V VS = 3.3 V, V CM = 12 V, and V SENSE = (V IN+ – V IN– ) = 0 mV (unless otherwise noted)







|0<br>−10<br>−20<br>(dB)<br>−30 Gain<br>−40<br>−50<br>−60<br>1 10 100 1k 10k 100k<br>Frequency (Hz)<br>G001<br>.<br>Figure 6-2. Frequency Response|Figure 6-3. Shunt Input Offset Voltage Production Distribution|
|---|---|
|**Figure 6-4. Shunt Input Offset Voltage vs Temperature**|**Figure 6-5. CMRR Production Distribution**|
|**Figure 6-6. Shunt Input CMRR vs Temperature**|**Figure 6-7. Shunt Voltage Gain Error Production Distribution**|


8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics (continued)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



at T A = 25°C, V VS = 3.3 V, V CM = 12 V, and V SENSE = (V IN+ – V IN– ) = 0 mV (unless otherwise noted)






|Figure 6-8. Shunt Gain Error vs Temperature|Figure 6-9. Shunt Gain Error vs Common-Mode Voltage|
|---|---|
|**Figure 6-10. Bus Offset Voltage (VIN–) Production Distribution**|**Figure 6-11. Bus Offset Voltage (VIN–) vs Temperature**|
|**Figure 6-12. Bus Voltage (VIN–) Gain Error Production**<br>**Distribution**|**Figure 6-13. Bus Voltage (VIN–) Gain Error vs Temperature**|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 9


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics (continued)**


at T A = 25°C, V VS = 3.3 V, V CM = 12 V, and V SENSE = (V IN+ – V IN– ) = 0 mV (unless otherwise noted)

|Figure 6-14. Input Bias Current vs Differential Voltage|Figure 6-15. Input Bias Current vs Common-Mode Voltage (IB+,<br>IB–)|
|---|---|
|**Figure 6-16. Input Bias Current vs Temperature**|**Figure 6-17. Input Bias Current vs Temperature (Shutdown)**|
|**Figure 6-18. Quiescent Current vs Temperature**|**Figure 6-19. Quiescent Current vs Supply Voltage**|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**6.8 Typical Characteristics (continued)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



at T A = 25°C, V VS = 3.3 V, V CM = 12 V, and V SENSE = (V IN+ – V IN– ) = 0 mV (unless otherwise noted)

|Figure 6-20. Quiescent Current - Shutdown vs Supply Voltage|Figure 6-21. Quiescent Current - Shutdown vs Temperature|
|---|---|
|**Figure 6-22. Quiescent Current vs Clock (SCL) Frequency**|**Figure 6-23. Quiescent Current - Shutdown vs SCL Frequency**|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 11


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**7 Detailed Description**

**7.1 Overview**


The INA236 is a digital current-sense amplifier with an I [2] C- and SMBus-compatible interface. The device reports
the sensed current and features programmable out-of-range limits to issue alerts when the current is outside
the normal range of operation. The integrated analog-to-digital converter (ADC) can be set to different averaging
modes and configured for continuous-versus-triggered operation. _Device Registers_ provides detailed register
information for the INA236.


**7.2 Functional Block Diagram**


Supply Voltage
(1.7 V to 5.5 V)





Bus Voltage
(-0.3 V to 48 V)


Shunt



C BYPASS
0.1 µF









Shunt






|Col1|TI Device|
|---|---|
||Current Register<br>I2C-, SMBus-,<br>Compatible<br>Interface<br>Voltage Register<br>ADC<br>V<br>I<br>A0<br>ALERT<br>SDA<br>SCL<br>Alert Register<br>VS<br>Power Register<br>x|
|||
|||



GND


**7.3 Feature Description**


**7.3.1 Integrated Analog-to-Digital Convertor (ADC)**


The INA236 integrates a low offset 16-bit delta-sigma (ΔΣ) ADC. This ADC is multiplexed to process both
the shunt voltage and bus voltage measurements. Bus voltage measurements are made with respect to IN–
and GND. The shunt voltage measurement is a differential measurement of the voltage developed when the
load current flows through a shunt resistor as measured between the IN+ and IN– pins. The shunt voltage
measurement has an maximum offset voltage of only 5 µV and a maximum gain error of 0.1%. The low offset
voltage of the shunt voltage measurement allows for increased accuracy at light load conditions for a given shunt
resistor value. Another advantage of low offset is the ability to sense a lower voltage drop across the sense
resistor accurately, thus allowing for a lower-value shunt resistor. Lower-value shunt resistors reduce power loss
in the current-sense circuit and help improve the power efficiency of the end application.


There are no special considerations for power-supply sequencing because the bus common-mode at the IN+
and IN– pins and power-supply voltage at the vs. pin are independent of each other; therefore, the bus commonmode voltage can be present with the supply voltage off, and vice-versa.


**7.3.2 Power Calculation**


Figure 7-1 shows that the current and power are calculated after a shunt voltage and bus voltage measurement.
Power is calculated based on the previous current calculation and the latest bus voltage measurement. If the
value loaded into the calibration register is zero, the power value reported is also zero. The current and power
values are considered intermediate results (unless the averaging is set to 1) and are stored in an internal
accumulation register. Following every measured sample, the newly-calculated values for current and power are
appended to this accumulation register until all of the samples have been measured and averaged. After all


12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



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


**Figure 7-1. Power Calculation Scheme**


**7.3.3 Low Bias Current**


When performing a current measurement, the INA236 features very low input bias current which provides
several benefits. The low input bias current of the INA236 reduces the current consumed by the device in both
active and shutdown state. Another benefit of low bias current is that it allows the use of input filters to reject
high-frequency noise before the signal is converted to digital data. In traditional digital current-sense monitors,
the addition of input filters comes at the cost of reduced accuracy. However, as a result of the low bias current,
the reduction in accuracy due to input filters is minimized. An additional benefit of low bias current is the ability
to use a larger shunt resistor to accurately sense smaller currents. Use of a larger value for the shunt resistor
allows the device to accurately monitor currents in the sub-mA range.


The bias current in the INA236 is the smallest when the sensed current is zero. As the current starts to increase,
the differential voltage drop across the shunt resistor increases which results in an increase in the bias current
(see Figure 6-14).


The INA236 has low bias current only when making a current measurement, when bus voltage measurements
are made the impedance of the IN– will decrease. During bus voltage measurements the IN– pin will be
connected to an internal resistor divider with an impedance of approximately 1 MΩ. Configuring the ADC to
perform only current measurements will allow the device to always have low bias current.


**7.3.4 Low Voltage Supply and Wide Common-Mode Voltage Range**


The supply voltage range of the INA236 is 1.7 V to 5.5 V. The ability to operate at 1.7 V enables the device to be
used in 1.8-V supply rails. Even with a supply voltage of 1.7 V, the device can monitor currents on voltage rails
as high as 48 V. This wide common-mode range of operation allows the device to be used in many applications
where the common-mode voltage exceeds the supply voltage rail.


**7.3.5 ALERT Pin**


The INA236 has a single Mask/Enable register (06h) that allows the ALERT pin to be programmed to respond
to a single user-defined event or to a conversion ready notification if desired. The Mask/Enable register allows
the selection from one of the five available functions to monitor and set the conversion ready bit (CNVR, Mask/
Enable register) to control the response of the ALERT pin. Based on the function being monitored, a value would
then be entered into the Alert Limit register to set the corresponding threshold value that asserts the ALERT pin.


The ALERT pin allows for one of several available alert functions to be monitored to determine if a user-defined
threshold has been exceeded. The five alert functions that can be monitored are:

 - Shunt voltage overlimit (SOL)

 - Shunt voltage underlimit (SUL)


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 13


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


 - Bus voltage overlimit (BOL)

 - Bus voltage underlimit (BUL)

 - Power overlimit (POL)


The ALERT pin is an open-drain output. This pin is asserted when the alert function selected in the Mask/Enable
register exceeds the value programmed into the Alert Limit register. Only one of these alert functions can be
enabled and monitored at a time. If multiple alert functions are enabled, the selected function in the highest
significant bit position takes priority and responds to the Alert Limit register value. For example, if the SOL and
the SUL are both selected, the ALERT pin asserts when the Shunt Voltage Over Limit register exceeds the value
in the Alert Limit register.


The conversion-ready state of the device can also be monitored at the ALERT pin to inform the user when the
device has completed the previous conversion and is ready to begin a new conversion. The conversion ready
flag (CVRF) bit can be monitored at the ALERT pin along with one of the alert functions. If an alert function
and the CNVR bit are both enabled for monitoring at the ALERT pin, then after the ALERT pin is asserted, the
CVRF bit (D3) and the AFF bit (D4) in the Mask/Enable register must be read following the alert to determine the
source of the alert. If the conversion ready feature is not desired, and the CNVR bit is not set, the ALERT pin
only responds to an exceeded alert limit based on the alert function enabled.


If the alert function is not used, the ALERT pin can be left floating without impacting the operation of the device.


Refer to Figure 7-1 to see the relative timing of when the value in the Alert Limit register is compared to the
corresponding converted value. For example, if the alert function that is enabled is Shunt Voltage Over Limit
(SOL), following every shunt voltage conversion the value in the Alert Limit register is compared to the measured
shunt voltage to determine if the measurements have exceeded the programmed limit. The AFF bit (D4, Mask/
Enable register) asserts high any time the measured voltage exceeds the value programmed into the Alert Limit
register. In addition to the AFF bit being asserted, the ALERT pin is asserted based on the Alert Polarity bit
(APOL, D1, Mask/Enable register). If the Alert Latch is enabled, the AFF bit and ALERT pin remain asserted until
either the Configuration register is written to or the Mask/Enable register is read.


The bus voltage alert functions (BOL and BUL, Mask/Enable register) compare the measured bus voltage to
the Alert Limit register following every bus voltage conversion and assert the AFF bit and ALERT pin if the limit
threshold is exceeded.


The power overlimit alert function (POL, Mask/Enable register) is also compared to the calculated power value
following every bus voltage measurement conversion and asserts the AFF bit and ALERT pin if the limit
threshold is exceeded.


The alert function compares the programmed alert limit value to the result of each corresponding conversion.
Therefore, an alert can be issued during a conversion cycle where the averaged value of the signal does not
exceed the alert limit. Triggering an alert based on this intermediate conversion allows for out-of-range events
to be detected faster than the averaged output data registers are updated. This fast detection can be used to
create alert limits for quickly changing conditions through the use of the alert function, as well as to create limits
to longer-duration conditions through software monitoring of the averaged output values.


**7.4 Device Functional Modes**


**7.4.1 Continuous Verses Triggered Operation**


The INA236 has two operating modes, continuous and triggered, that determine how the ADC operates
after these conversions. When the INA236 is in the normal operating mode (that is, the MODE bits of the
Configuration register are set to '111'), it continuously converts a shunt voltage reading followed by a bus voltage
reading.


In triggered mode, writing any of the triggered convert modes into the Configuration register (0h) (that is, the
MODE bits of the Configuration register are set to 001) triggers a single-shot conversion. This action produces a
single set of measurements. To trigger another single-shot conversion, the Configuration register must be written
to again, even if the mode does not change.


Although the INA236 can be read at any time, and the data from the last conversion remain available, the
conversion ready flag bit (CVRF bit, Mask/Enable register) is provided to help coordinate single-shot or triggered


14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



conversions. The CVRF bit is set after all conversions, averaging, and multiplication operations are complete for
a single cycle.


The CVRF bit clears under these conditions:

1. Writing to the Configuration register, except when configuring the MODE bits for power-down mode; or
2. Reading the Mask/Enable register.


**7.4.2 Device Shutdown**


In addition to the two operating modes (continuous and triggered), the INA236 also has a power-down mode
that reduces the quiescent current and input bias current. The power-down mode reduces supply drain when
the device is not being used. Full recovery from power-down mode requires 100 µs. The device remains in
power-down mode until one of the active modes settings are written into the Configuration register.


**7.4.3 Power-On Reset**


Power-on reset (POR) is asserted when V S drops below 0.95 V (typical) at which all of the registers are reset
to their default values. The default power-up register values are shown in the reset column for each register
description. Table 7-2 provides links to the register descriptions.


**7.4.4 Averaging and Conversion Time Considerations**


The INA236 has programmable conversion times for both the shunt voltage and bus voltage measurements. The
conversion times for these measurements can be selected from as fast as 140 μs to as long as 8.244 ms. The
conversion time settings, along with the programmable averaging mode, allow the INA236 to be configured to
optimize the available timing requirements in a given application. For example, if a system requires that data
be read every 5 ms, the INA236 can be configured with the conversion times set to 588 μs and the averaging
mode set to 4. This configuration results in the data updating approximately every 4.7 ms. The INA236 can also
be configured with a different conversion time setting for the shunt and bus voltage measurements. This type of
approach is common in applications where the bus voltage tends to be relatively stable. This situation allows for
the time spent measuring the bus voltage to be reduced relative to the shunt voltage measurement. The shunt
voltage conversion time can be set to 4.156 ms with the bus voltage conversion time set to 588 μs, and the
averaging mode set to 1. This configuration also results in data updating approximately every 4.7 ms.


There are trade-offs associated with the conversion time settings and the averaging mode used. The averaging
feature can significantly improve the measurement accuracy by effectively filtering the signal. This approach
allows the INA236 to reduce noise in the measurement that may be caused by noise coupling into the signal.
A greater number of averages enables the INA236 to be more effective in reducing the noise component of the
measurement.


The conversion times selected can also have an effect on the measurement accuracy. Figure 7-2 shows
multiple conversion times to illustrate the effect of noise on the measurement. To achieve the highest accuracy
measurement possible, use a combination of the longest allowable conversion times and highest number of
averages, based on the timing requirements of the system.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 15


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**Figure 7-2. Noise vs Conversion Time**


**7.5 Programming**


**7.5.1 I** **[2]** **C Serial Interface**


The INA236 operates only as a target on both the SMBus and I [2] C interfaces. Connections to the bus are
made through the open-drain SDA and SCL lines. The SDA and SCL pins feature integrated spike suppression
filters and Schmitt triggers to minimize the effects of input spikes and bus noise. Although the device integrates
spike suppression into the digital I/O lines, proper layout techniques help minimize the amount of coupling into
the communication lines. This noise introduction could occur from capacitive coupling signal edges between
the two communication lines themselves or from other switching noise sources present in the system. Routing
traces in parallel with ground in between layers on a printed circuit board (PCB) typically reduces the effects of
coupling between the communication lines. Shielded communication lines reduce the possibility of unintended
noise coupling into the digital I/O lines that could be incorrectly interpreted as start or stop commands.


The INA236 supports the transmission protocol for fast mode up to 400 kHz and high-speed mode up to 2.94
MHz. All data bytes are transmitted most significant byte first and follow the SMBus 3.0 transfer protocol.


To communicate with the INA236, the controller must first address targets through a target address byte. The
target address byte consists of seven address bits and a direction bit that indicates whether the action is to be a
read or write operation.


The INA236 uses a single address pin, A0. Table 7-1 shows possible configurations for A0 and the
corresponding address for both the A and B versions of the device. The INA236 samples the state of the
A0 pin on every bus communication. The pin state for A0 must be established before any activity on the interface
occurs. When connecting the SDA pin to A0 to set the device address, make sure to add an additional hold time
of 100 ns on the MSB of the I2C address to ensure correct device addressing. The A and B device options,
each with four unique addresses, allows users to connect up to eight devices in a system without I [2] C address
conflicts.


**Table 7-1. Address Pins and Target Addresses**

|A0|INA236A DEVICE OPTION|INA236B DEVICE OPTION|
|---|---|---|
|GND|1000000|1001000|
|VS|1000001|1001001|
|SDA|1000010|1001010|
|SCL|1000011|1001011|



16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**7.5.2 Writing to and Reading Through the I** **[2]** **C Serial Interface**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



Accessing a specific register on the INA236 is accomplished by writing the appropriate value to the register
pointer. Refer to _Register Maps_ for a complete list of registers and corresponding addresses. The value for the
register pointer (see Figure 7-5) is the first byte transferred after the target address byte with the R/W bit low.
Every write operation to the device requires a value for the register pointer.


Writing to a register begins with the first byte transmitted by the controller. This byte is the target address,
with the R/W bit low. The device then acknowledges receipt of a valid address. The next byte transmitted by
the controller is the address of the register to be accessed. This register address value updates the register
pointer to the desired internal device register. The next two bytes are written to the register addressed by the
register pointer. The device acknowledges receipt of each data byte. The controller may terminate data transfer
by generating a start or stop condition.


When reading from the device, the last value stored in the register pointer by a write operation determines which
register is read during a read operation. To change the register pointer for a read operation, a new value must
be written to the register pointer. This write is accomplished by issuing a target address byte with the R/ W bit
low, followed by the register pointer byte. No additional data are required. The controller then generates a start
condition and sends the address byte for the target with the R/W bit high to initiate the read command. The next
byte is transmitted by the target and is the most significant byte of the register indicated by the register pointer.
This byte is followed by an _Acknowledge_ from the controller; then the target transmits the least significant byte.
The controller may or may not acknowledge receipt of the second data byte. The controller may terminate data
transfer by generating a _Not-Acknowledge_ after receiving any data byte, or generating a start or stop condition.
If repeated reads from the same register are desired, it is not necessary to continually send the register pointer
bytes; the device retains the register pointer value until it is changed by the next write operation.


Figure 7-3 shows the write operation timing diagram. Figure 7-4 shows the read operation timing diagram. These
diagrams are shown for reading/writing to 16 bit registers.


Register bytes are sent most-significant byte first, followed by the least significant byte.



1


D7 D6 D5 D4 D3 D2 D1 D0



9 1 9


D15 D14 D13 D12 D11 D10 D9 D8



9



SCL


SDA



1 9 1


1 0 0 A3 A2 A1 A0 R/W P7 P6 P5 P4 P3 P2 P1 P0



ACK By Stop By
**Target** Controller



Start By ACK By ACK By
Controller **Target** **Target**


(1)
Frame 1 Two-Wire Target Address Byte Frame 2 Register Pointer Byte



ACK By
**Target**


Frame 3 Data MSByte Frame 4 Data LSByte



A. The value of the Target Address byte is determined by the setting of the A0 address pin. Refer to Table 7-1.

B. The device does not support packet error checking (PEC) or perform clock stretching.


**Figure 7-3. Timing Diagram for Write Word Format**



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



(2)



Frame 3 Data LSByte



Frame 1 Two-Wire Target Address Byte



(1)
Frame 2 Data MSByte



A. The value of the Target Address byte is determined by the setting of the A0 address pin. Refer to Table 7-1.

B. Read data is from the last register pointer location. If a new register is desired, the register pointer must be updated. See Figure 7-5.

C. ACK by the controller can also be sent.

D. The device does not support packet error checking (PEC) or perform clock stretching.


**Figure 7-4. Timing Diagram for Read Word Format**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 17


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


1 9 1 9



SCL


SDA





���



Start By ACK By ACK By
Controller **Target** **Target**



(1)



Frame 2 Register Pointer Byte



Frame 1 Two-Wire Target Address Byte



A. The value of the Target Address byte is determined by the setting of the A0 address pin. Refer to Table 7-1.


**Figure 7-5. Typical Register Pointer Set**


**7.5.3 High-Speed I** **[2]** **C Mode**


When the bus is idle, both the SDA and SCL lines are pulled high by the pullup resistors. The controller
generates a start condition followed by a valid serial byte containing high-speed (HS) controller code _00001XXX_ .
This transmission is made in fast (400 kHz) or standard (100 kHz) (F/S) mode at no more than 400 kHz. The
device does not acknowledge the HS controller code, but does recognize it and switches its internal filters to
support 2.94-MHz operation.


The controller then generates a repeated start condition (a repeated start condition has the same timing as
the start condition). After this repeated start condition, the protocol is the same as F/S mode, except that
transmission speeds up to 2.94 MHz are allowed. Instead of using a stop condition, use repeated start conditions
to maintain the bus in HS-mode. A stop condition ends the HS-mode and switches all the internal filters of the
device to support the F/S mode.


**7.5.4 General Call Reset**


A general call reset to multiple devices is implemented by addressing the general call address 0000 000, with
the last R/W bit set to 0. This is then followed by the following data byte 0000 0110 (06h).


On receiving this 2-byte sequence, all devices designed to respond to the general call address will reset. All
INA236 devices on the bus will do a soft reset operation and return to the default power-up conditions


**7.5.5 General Call Start Byte**


A general call ADC conversion start command to multiple INA236 devices is implemented by addressing the
general call address 0000 000, with the last R/W bit set to 1. No other data bytes are required. Be aware that
other devices in the bus that use general call start commands on the bus will also trigger a start of conversion.


**7.5.6 SMBus Alert Response**


The INA236 is designed to respond to the SMBus Alert Response address. The SMBus Alert Response provides
a quick fault identification for simple targets. When an Alert occurs, the controller can broadcast the Alert
Response target address (0001 100) with the Read/Write bit set high. Following this Alert Response, any target
that generates an alert identifies itself by acknowledging the Alert Response and sending its address on the bus.


The Alert Response can activate several different target devices simultaneously, similar to the I [2] C General Call.
If more than one target attempts to respond, bus arbitration rules apply. The losing device does not generate an
Acknowledge and continues to hold the Alert line low until that device wins arbitration.


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**7.6 Register Maps**


**7.6.1 Device Registers**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



Table 7-2 lists the INA236 registers. All register locations not listed in Table 7-2 should be considered as
reserved locations and the register contents should not be modified.


**Table 7-2. INA236 Registers**

|Address|Register Name|Register Size (bits)|Reset Value|Section|
|---|---|---|---|---|
|0h|Configuration Register|16|4127h|Go|
|1h|Shunt Voltage Register|16|0000h|Go|
|2h|Bus Voltage Register|16|0000h|Go|
|3h|Power Register|16|0000h|Go|
|4h|Current Register|16|0000h|Go|
|5h|Calibration Register|16|0000h|Go|
|6h|Mask/Enable Register|16|0000h|Go|
|7h|Alert Limit Register|16|0000h|Go|
|3Eh|Manufacturer ID Register|16|5449h|Go|
|3Fh|Device ID Register|16|A080h|Go|



Complex bit access types are encoded to fit into small table cells. Table 7-3 shows the codes that are used for
access types in this section.


**Table 7-3. Device Access Type Codes**

|Access Type|Code Description|Col3|
|---|---|---|
|Read Type|Read Type|Read Type|
|R|R|Read|
|Write Type|Write Type|Write Type|
|W|W|Write|



**7.6.1.1 Configuration Register (Address = 0h) [reset = 4127h]**


The configuration register is shown in Table 7-4.


**Table 7-4. Configuration Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RST|R/W|0b|Set this bit to '1' to generate a system reset that is the same as power-<br>on reset.<br>Resets all registers to default values and then self-clears.<br>**0b = Normal Operation**<br>1b = System Reset self clears registers to default values|
|14-13|Reserved|R|10b|Reserved value always returns 10b|
|12|ADCRANGE|R/W|0b|Enables the selection of the shunt full scale input across IN+ and IN–.<br>**0b = ±81.92 mV**<br>1b = ±20.48 mV|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 19


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**Table 7-4. Configuration Register Field Descriptions (continued)**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|11-9|AVG|R/W|000b|Sets the number of ADC conversion results to be averaged. The read-<br>back registers are updated after averaging is completed.<br>**000b = 1**<br>001b = 4<br>010b = 16<br>011b = 64<br>100b = 128<br>101b = 256<br>110b = 512<br>111b = 1024|
|8-6|VBUSCT|R/W|100b|Sets the conversion time of the VBUS measurement<br>000b = 140 µs<br>001b = 204 µs<br>010b = 332 µs<br>011b = 588 µs<br>**100b = 1100 µs**<br>101b = 2116 µs<br>110b = 4156 µs<br>111b = 8244 µs|
|5-3|VSHCT|R/W|100b|Sets the conversion time of the SHUNT measurement<br>000b = 140 µs<br>001b = 204 µs<br>010b = 332 µs<br>011b = 588 µs<br>**100b = 1100 µs**<br>101b = 2116 µs<br>110b = 4156 µs<br>111b = 8244 µs|
|2-0|MODE|R/W|111b|Operating mode, modes can be selected to operate the device either in<br>Shutdown mode, continuous mode or triggered mode.<br>The mode also allows user to select mux settings to set continuous or<br>triggered mode on bus voltage, shunt voltage measurement.<br>000b = Shutdown<br>001b = Shunt Voltage triggered, single shot<br>010b = Bus Voltage triggered, single shot<br>011b = Shunt voltage and Bus voltage triggered, single shot<br>100b = Shutdown<br>101b = Continuous Shunt voltage<br>110b = Continuous Bus voltage<br>**111b = Continuous Shunt and Bus voltage**|



Return to the Summary Table.


**7.6.1.2 Shunt Voltage Register (Address = 1h) [reset = 0000h]**


The Shunt Voltage Register stores the current shunt voltage reading, V SHUNT and is show in Table 7-5. Negative
numbers are represented in two's complement format. Generate the two's complement of a negative number by
complementing the absolute value binary number and adding 1. An MSB = '1' denotes a negative number.


**Example:** For a value of V SHUNT = –80 mV:

1. Take the absolute value: 80 mV
2. Translate this number to a whole decimal number (80 mV ÷ 2.5 µV) = 32000
3. Convert this number to binary = 0111 1101 0000 0000
4. Complement the binary result = 1000 0010 1111 1111


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



5. Add '1' to the complement to create the two's complement result = 1000 0011 0000 0000 = 8300h


If averaging is enabled, this register displays the averaged value.


**Table 7-5. Shunt Voltage Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|VSHUNT|R|0000h|Differential voltage measured across the shunt output. Two's<br>complement value.|



Return to the Summary Table.


**7.6.1.3 Bus Voltage Register (Address = 2h) [reset = 0000h]**


The bus voltage register is shown in Table 7-6.


This register will only return positive values. If averaging is enabled, this register displays the averaged value.


**Table 7-6. Bus Voltage Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|Reserved|R|0b|This bit returns Zero as common mode voltage is only positive|
|14-0|VBUS|R|0000h|These bits readout the bus voltage of the system|



Return to the Summary Table.


**7.6.1.4 POWER Register (Address = 3h) [reset = 0000h]**


The power register is shown in Table 7-7.


If averaging is enabled, this register displays the averaged value. The Power Register records power in Watts by
multiplying the decimal values of the Current Register with the decimal value of the Bus Voltage Register. This is
an unsigned result.


**Table 7-7. POWER Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|POWER|R|0000h|This bit returns a calculated value of power in the system.<br>This is an unsigned result.|



Return to the Summary Table.


**7.6.1.5 CURRENT Register (Address = 4h) [reset = 0000h]**


CURRENT is shown in Table 7-8.


If averaging is enabled, this register displays the averaged value. The value of the Current Register is calculated
by multiplying the decimal value in the Shunt Voltage Register with the decimal value of the Calibration Register.


**Table 7-8. CURRENT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|CURRENT|R|0000h|Calculated current output in Amperes. Two's complement value.|



Return to the Summary Table.


**7.6.1.6 Calibration Register (Address = 5h) [reset = 0000h]**


The calibration register shown in Table 7-9 must be programmed to receive valid current and power results after
initial power up or power cycle events.


This register provides the device with the value of the shunt resistor that was present to create the measured
differential voltage. It also sets the resolution of the Current Register. Programming this register sets the
Current_LSB and the Power_LSB.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 21


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**Table 7-9. Calibration Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|Reserved|R|0h||
|14-0|SHUNT_CAL|R/W|0000h|Programmed value needed for doing the shunt voltage to current<br>conversion.|



Return to the Summary Table.


**7.6.1.7 Mask/Enable Register (Address = 6h) [reset = 0000h]**


The Mask/Enable Register is shown in Table 7-10.


**Table 7-10. Mask/Enable Register Field Descriptions**












|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|SOL (Shunt Over-limit)|R/W|0b|Setting this bit high configures the ALERT pin to be asserted if the shunt voltage<br>conversion result exceeds the value programmed in the LIMIT register|
|14|SUL (Shunt Under-limit)|R/W|0b|Setting this bit high configures the ALERT pin to be asserted if the shunt voltage<br>conversion result is below the value programmed in the LIMIT register.<br>Cannot be set if Shunt overlimit is set.|
|13|BOL (Bus Over-limit)|R/W|0b|Setting this bit high configures the ALERT pin to be asserted if the bus voltage<br>conversion result exceeds the value programmed in the LIMIT register<br>Cannot be set if Shunt overlimit or Shunt underlimit is set.|
|12|BUL (Bus Under-limit)|R/W|0b|Setting this bit high configures the ALERT pin to be asserted if the bus voltage<br>conversion result is below the value programmed in the LIMIT register<br>Cannot be set if Shunt over limit, Shunt under limit or Bus over limit is set.|
|11|POL (Power Over-limit)|R/W|0b|Setting this bit high configures the ALERT pin to be asserted if the power result<br>exceeds the value programmed in the LIMIT register<br>Cannot be set if Shunt over limit, Shunt under limit, Bus over limit or Bus under<br>limit is set.|
|10|CNVR (Conversion<br>Ready)|R/W|0b|Setting this bit high configures the ALERT pin to be asserted when the<br>Conversion Ready Flag, Bit 3, is asserted indicating that the device is ready<br>for the next conversion.<br>**0b = Disable conversion ready flag on ALERT pin**<br>1b = Enables conversion ready flag on ALERT pin|
|9-6|Reserved|R|0000b||
|5|MemError|R|0b|CRC or ECC error|
|4|AFF (Alert Function<br>Flag)|R|0b|Alert Function Flag -While only one Alert Function can be monitored at the<br>ALERT pin at a time, the Conversion Ready can also be enabled to assert the<br>ALERT pin. Reading the Alert Function Flag following an alert allows the user to<br>determine if the Alert Function was the source of the Alert.<br>When the Alert Latch Enable bit is set to Latch mode, the Alert Function Flag bit<br>clears only when the Mask/Enable Register is read. When the Alert Latch Enable<br>bit is set to Transparent mode, the Alert Function Flag bit is cleared following the<br>next conversion that does not result in an Alert condition.|
|3|CVRF (Conversion<br>Ready Flag)|R|0b|Although the device can be read at any time, and the data from the last<br>conversion is available, the Conversion Ready Flag bit is provided to help<br>coordinate one-shot or triggered conversions.<br>The Conversion Ready Flag bit is set after all conversions, averaging, and<br>multiplications are complete.<br>Conversion Ready Flag bit clears under the following conditions:<br>1.) Writing to the Configuration Register (except for Power-Down selection)<br>2.) Reading the Mask/Enable Register|



22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)


**Table 7-10. Mask/Enable Register Field Descriptions (continued)**





|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|2|OVF (Math Over-flow)|R|0b|This bit is set to '1' if an arithmetic operation resulted in an overflow error. It<br>indicates that current and power data may be invalid.|
|1|APOL (Alert Polarity)|R/W|0b|Alert Polarity bit sets the Alert pin polarity.<br>**0b = Normal (Active-low open drain)**<br>1b= Inverted (active-high )|
|0|LEN (Alert Latch<br>Enable)|R/W|0b|When the Alert Latch Enable bit is set to Transparent mode, the Alert pin and<br>Alert Function Flag (AFF) bit resets to the idle states when the fault condition has<br>been cleared.<br>When the Alert Latch Enable bit is set to Latch mode, the Alert pin and AFF bit<br>remains active following a fault until this register flag has been read.<br>This bit must be set to use the I2C Alert Response function.<br>**0b = Transparent**<br>1b = Latched Alert pin|


Return to the Summary Table.





**7.6.1.8 Alert Limit Register (Address = 7h) [reset = 0000h]**


The alert limit register is shown in Table 7-11.


**Table 7-11. Alert Limit Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|LIMIT|R/W|0000h|The Alert Limit Register contains the value used to compare to the<br>register selected in the Mask/Enable Register to determine if a limit<br>has been exceeded.<br>A two's complement value must be used for the Shunt Over Voltage<br>limit. Limit values entered should match the format of the targeted<br>register|



Return to the Summary Table.


**7.6.1.9 Manufacturer ID Register (Address = 3Eh) [reset = 5449h]**


The manufacturer ID register is shown in Table 7-12.


**Table 7-12. MANUFACTURE_ID Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|MANUFACTURE_ID|R|5449h|Reads back TI in ASCII|



Return to the Summary Table.


**7.6.1.10 Device ID Register (Address = 3Fh) [reset = A080h]**


The Device ID register is shown in Table 7-13.


**Table 7-13. DEVICE_ID Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-3|DIEID|R|A080h|Stores the device identification bits|
|3-0|Reserved|R|0h|Always read 0|



Return to the Summary Table.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 23


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**8 Application and Implementation**


**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**8.1 Application Information**


The INA236 is a current shunt monitor with an I [2] C- and SMBus-compatible interface. The device monitors
a shunt voltage drop to calculate the current and bus voltage at IN– pin to determine power. Programmable
calibration value, conversion times, and averaging (combined with an internal multiplier) enable direct readouts
of current in amperes and power in watts.


**8.1.1 Device Measurement Range and Resolution**


The INA236 device supports two input ranges for the shunt voltage measurement. The supported full scale
differential input across the IN+ and IN– pins can be either ±81.92 mV or ±20.48 mV depending on the
ADCRANGE bit in the Configuration Register (0h) register. The range for the bus voltage measurement at the
IN- pin is from 0 V to 52.42 V, but is limited by process ratings to the max operating voltage.


Table 8-1 provides a description of full scale voltage on shunt and bus voltage measurements, along with their
associated resolution.


**Table 8-1. ADC Full Scale Values**







|PARAMETER|FULL SCALE VALUE|RESOLUTION|
|---|---|---|
|Shunt voltage|±81.92 mV (ADCRANGE = 0)|2.5 µV/LSB|
|Shunt voltage|±20.48 mV (ADCRANGE = 1)|625 nV/LSB|
|Bus voltage|0 V to 52.4 V (Limit usable range to recommended operating<br>voltage)|1.6 mV/LSB|


The device shunt voltage and bus voltage measurements are read through the Shunt Voltage register (1h) and
Bus Voltage register (2h), respectively. The digital output in shunt voltage and bus voltage registers is 16 bits.
The shunt voltage measurement can be positive or negative due to bidirectional currents in the system; therefore
the data value in shunt voltage register can be positive or negative. The bus voltage register data value is always
positive. The output data can be directly converted into voltage by multiplying the digital value by its respective
resolution size.


Furthermore, the device provides the flexibility to report calculated current in Amperes, power in Watts, as
described in _Current and Power Calculations_ .


**8.1.2 Current and Power Calculations**


For the INA236 to report current values in Amperes, a constant conversion value must be written in the
calibration register that is dependent on the selected CURRENT_LSB and the shunt resistance used in the
application. The value of the calibration register is calculated based on Equation 1. The term CURRENT_LSB is
the chosen LSB step size for the CURRENT register where the current is stored. Equation 2 shows the minimum
value of CURRENT_LSB is based on the maximum expected current, and it directly defines the maximum
resolution of the CURRENT register. While the smallest CURRENT_LSB value yields highest resolution, it is
common to select a higher round-number (no higher than 8x) value for the CURRENT_LSB to simplify the
conversion of the CURRENT.


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



The R SHUNT term is the resistance value of the external shunt used to develop the differential voltage across the
IN+ and IN– pins. Use Equation 1 for ADCRANGE = 0. For ADCRANGE = 1, the value of SHUNT_CAL must be
divided by 4.


0.00512
SHUNT_CAL =

Current_LSB × R SHUNT (1)


where


 - 0.00512 is an internal fixed value used to ensure scaling is maintained properly.

 - CURRENT_LSB is a selected value for the current step size in amperes. Must be greater than or equal to
CURRENT_LSB (minimum), but less than 8 x CURRENT_LSB(minimum) to reduce resolution loss.

 - The value of SHUNT_CAL must be divided by 4 for ADCRANGE = 1.


(2)


Note that the current is calculated following a shunt voltage measurement based on the value set in the
SHUNT_CAL register. If the value loaded into the SHUNT_CAL register is zero, the current value reported
through the CURRENT register is also zero.


After programming the SHUNT_CAL register with the calculated value, the measured current in Amperes can be
read from the CURRENT register. Use Equation 3 to calculate the final value scaled by the CURRENT_LSB:


Current [A] = CURRENT_LSB x CURRENT (3)


where


 - CURRENT is the value read from the CURRENT register


The power value can be read from the POWER register as a 16-bit value. Use Equation 4 to convert the power
to Watts:


Power [W] = 32 x CURRENT_LSB x POWER (4)


where


 - POWER is the value read from the POWER register.

 - CURRENT_LSB is selected value for the lsb size of the current calculation used in Equation 1.


Refer to _Detailed Design Procedure_ for a design example using these equations.


**8.1.3 ADC Output Data Rate and Noise Performance**


The INA236 noise performance and effective resolution depend on the ADC conversion time. The device
also supports digital averaging which can further help decrease digital noise. The flexibility of the device to
select ADC conversion time and data averaging offers increased signal-to-noise ratio and achieves the highest
dynamic range with lowest offset. The profile of the noise at lower signals levels is dominated by the system
noise that is comprised mainly of 1/f noise or white noise. The effective resolution of the ADC can be increased
by increasing the conversion time and increasing the number of averages.


Table 8-2 summarizes the output data rate conversion settings supported by the device. The fastest conversion
setting is 140 µs. Typical noise-free resolution is represented as Effective Number of Bits (ENOB) based on
device measured data. The ENOB is calculated based on noise peak-to-peak values, which assures that full
noise distribution is taken into consideration.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 25


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


**Table 8-2. INA236 Noise Performance**













|ADC CONVERSION<br>TIME PERIOD [µs]|OUTPUT SAMPLE<br>AVERAGING<br>[SAMPLES]|OUTPUT SAMPLE PERIOD<br>[ms]|NOISE-FREE ENOB<br>(±81.92-mV) (ADCRANGE<br>= 0)|NOISE-FREE ENOB<br>(±20.48-mV) (ADCRANGE<br>= 1)|
|---|---|---|---|---|
|140|1|0.14|13.1|11.1|
|204|1|0.204|13.4|11.1|
|332|1|0.332|14.1|11.7|
|588|1|0.588|14.7|12.2|
|1100|1|1.1|14.7|12.5|
|2116|1|2.116|15.1|13.4|
|4156|1|4.156|15.7|14.1|
|8244|1|8.244|16.0|14.7|
|140|4|0.56|14.1|12.1|
|204|4|0.816|14.4|12.4|
|332|4|1.328|15.1|12.9|
|588|4|2.352|15.7|13.4|
|1100|4|4.4|15.7|13.7|
|2116|4|8.464|16.0|14.7|
|4156|4|16.624|16.0|14.7|
|8244|4|32.976|16.0|15.7|
|140|16|2.24|15.1|13.1|
|204|16|3.264|15.7|13.4|
|332|16|5.312|15.7|14.1|
|588|16|9.408|16.0|14.4|
|1100|16|17.6|16.0|15.1|
|2116|16|33.856|16.0|15.7|
|4156|16|66.496|16.0|15.7|
|8244|16|131.904|16.0|16.0|
|140|64|8.96|15.7|13.7|
|204|64|13.056|16.0|14.4|
|332|64|21.248|16.0|15.1|
|588|64|37.632|16.0|15.7|
|1100|64|70.4|16.0|15.7|
|2116|64|135.424|16.0|16.0|
|4156|64|265.984|16.0|16.0|
|8244|64|527.616|16.0|16.0|
|140|128|17.92|16.0|14.1|
|204|128|26.112|16.0|15.1|
|332|128|42.496|16.0|15.7|
|588|128|75.264|16.0|15.7|
|1100|128|140.8|16.0|16.0|
|2116|128|270.848|16.0|16.0|
|4156|128|531.968|16.0|16.0|
|8244|128|1055.232|16.0|16.0|
|140|256|35.84|16.0|14.7|
|204|256|52.224|16.0|15.7|
|332|256|84.992|16.0|15.7|
|588|256|150.528|16.0|16.0|


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**





**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)


**Table 8-2. INA236 Noise Performance (continued)**









|ADC CONVERSION<br>TIME PERIOD [µs]|OUTPUT SAMPLE<br>AVERAGING<br>[SAMPLES]|OUTPUT SAMPLE PERIOD<br>[ms]|NOISE-FREE ENOB<br>(±81.92-mV) (ADCRANGE<br>= 0)|NOISE-FREE ENOB<br>(±20.48-mV) (ADCRANGE<br>= 1)|
|---|---|---|---|---|
|1100|256|281.6|16.0|16.0|
|2116|256|541.696|16.0|16.0|
|4156|256|1063.936|16.0|16.0|
|8244|256|2110.464|16.0|16.0|
|140|512|71.68|16.0|15.1|
|204|512|104.448|16.0|15.7|
|332|512|169.984|16.0|16.0|
|588|512|301.056|16.0|16.0|
|1100|512|563.2|16.0|16.0|
|2116|512|1083.392|16.0|16.0|
|4156|512|2127.872|16.0|16.0|
|8244|512|4220.928|16.0|16.0|
|140|1024|143.36|16.0|15.7|
|204|1024|208.896|16.0|16.0|
|332|1024|339.968|16.0|16.0|
|588|1024|602.112|16.0|16.0|
|1100|1024|1126.4|16.0|16.0|
|2116|1024|2166.784|16.0|16.0|
|4156|1024|4255.744|16.0|16.0|
|8244|1024|8441.856|16.0|16.0|


**8.1.4 Filtering and Input Considerations**


Measuring current is often noisy and such noise can be difficult to define. The INA236 offers several options
for filtering by allowing the conversion times and number of averages to be selected independently in the
Configuration register (0h). The conversion times can be set independently for the shunt voltage and bus voltage
measurements to allow added flexibility when configuring the monitoring of the power-supply bus.


The internal ADC is based on a delta-sigma (ΔΣ) front-end with a 500-kHz (±10% maximum) sampling rate.
This architecture has good inherent noise rejection; however, transients that occur at or very close to the
sampling rate harmonics can cause problems. These signals are at 1 MHz and higher and can be managed
by incorporating filtering at the device input. The high frequency enables the use of low-value series resistors
on the filter with negligible effects on measurement accuracy. In general, filtering the device input is only
necessary if there are transients at exact harmonics of the 500 kHz (±10% maximum) sampling rate (greater
than 1 MHz). Filter using the lowest possible series resistance (typically 100 Ω or less) and a ceramic capacitor.
Recommended values for this capacitor are between 0.1 µF and 1 µF. Figure 8-1 shows the device with a filter
added at the input.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 27


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**









R FILTER











**Figure 8-1. Input Filtering**


Overload conditions are another consideration for the device inputs. The device inputs are specified to tolerate
26 V across the inputs. A large differential scenario can be a short to ground on the load side of the shunt.
This type of event can result in full power-supply voltage across the shunt (as long the power supply or energy
storage capacitors can support this voltage). Removing a short to ground can result in inductive kickbacks
that can exceed the 26-V differential and 48-V common-mode rating of the device. Inductive kickback voltages
are best controlled by Zener-type, transient-absorbing devices (commonly called _transzorbs_ ) combined with
sufficient energy storage capacitance. The _[Current Shunt Monitor with Transient Robustness Reference Design](http://www.ti.com/tool/TIDA-00302)_
describes a high-side, current-shunt monitor used to measure the voltage developed across a current-sensing
resistor and how to better protect the current-sense device from transient overvoltage conditions.


In applications that do not have large energy storage electrolytics on one or both sides of the shunt, an input
overstress condition can result from an excessive dV/dt of the voltage applied to the input. A hard physical short
is the most likely cause of this event, and the excessive dV/dt can activate the ESD protection in systems with
large currents. Testing demonstrates that the addition of 10-Ω resistors in series with each input of the device
sufficiently protects against dV/dt failures up to the 48-V rating of the device. Selecting these resistors in the
range noted has minimal effect on accuracy.


**8.2 Typical Application**


Supply Voltage (V S ):
1.7 V to 5.5 V









R SHUNT







**Figure 8-2. Typical High-Side Sensing Circuit Configuration, INA236**


**8.2.1 Design Requirements**


The INA236 measures the voltage developed across a current-sensing resistor (R SHUNT ) when current passes
through it. The device also measures the bus supply voltage and calculates power when calibrated. It also
comes with alert capability, where the alert pin can be programmed to respond to a user-defined event or a
conversion ready notification.


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


Table 8-3 lists the design requirements for the circuit shown in Figure 8-2.


**Table 8-3. Design Parameters**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



|DESIGN PARAMETER|EXAMPLE VALUE|
|---|---|
|Power-supply voltage (VS)|3.3 V|
|Bus supply rail (VCM)|12 V|
|Average Current|6 A|
|Overcurrent fault threshold|9 A|
|Maximum current monitored (IMAX)|10 A|
|ADC Range Selection (VSENSE_MAX)|±81.92 mV|


**8.2.2 Detailed Design Procedure**


This design example walks through the process of selecting the shunt resistor, programming the calibration
register, setting the correct fault thresholds, and how to properly scale returned values from the device.


_**8.2.2.1 Select the Shunt Resistor**_


Using values from Table 8-3, the maximum value of the shunt resistor is calculated based on the value of
the maximum current to be sensed (I MAX ) and the maximum allowable sense voltage (V SENSE_MAX ) for the
chosen ADC range. When operating at the maximum current, the differential input voltage must not exceed the
maximum full scale range of the device, V SENSE_MAX . Using Equation 5 for the given design parameters, the
maximum value for R SHUNT is calculated to be 8.192 mΩ. The closest standard resistor value that is smaller than
the maximum calculated value is 8.0 mΩ. Smaller resistors can be used to minimize power loss at the expense
of reduced accuracy. The shunt resistor selected must have sufficient wattage to handle the power dissipation at
maximum load at the desired operating temperature.


R SHUNT < [V] [SENSE_MAX] I MAX (5)


_**8.2.2.2 Configure the Device**_


The first step to program the INA236 is to properly set the device Configuration register (0h). On initial power up,
the configuration register is set to the reset values (see Table 7-4). In the default power on state the device is set
to measured on the ±81.92 mV range with the ADC continuously converting the shunt and bus (voltage at IN–)
voltages. If the default power up conditions do not meet the design requirements, these registers will need to be
set properly after each V S power cycle event.


_**8.2.2.3 Program the Shunt Calibration Register**_


The shunt calibration register needs to be correctly programmed at each V S power up in order for the device to
properly report any result based on current. The first step is to calculate the minimum LSB value for the current
by using Equation 2. Applying this equation with the maximum expected current of 10 A results in an minimum
LSB size of 305.17578 μA. The INA236 allows selection of the CURRENT_LSB to be up to 8 x larger than the
minimum LSB size. For this example a value of 500 μA is used. Applying Equation 1 to the Current_LSB and
selected value for the shunt resistor results in a shunt calibration register setting of 1280d (500h). Failure to set
the value of the shunt calibration register will result in a zero value for any result based on current. Programming
this register is not required for reading shunt voltage, bus voltage, or setting alert limits.


_**8.2.2.4 Set Desired Fault Thresholds**_


The INA236 has the ability to assert the Alert pin on several different fault conditions as described in _ALERT_
_Pin_ . The desired fault condition to assert the Alert pin needs to be selected by appropriately programming the
Mask/Enable Register (6h). Fault thresholds are set by programming the desired trip threshold into the Alert
Limit Register (7h).


For example, an overcurrent fault condition would be selected by setting the SOL bit in the Mask/Enable
Register to 1. The desired threshold for the over current condition would have to be programmed in the Alert
Limit Register. In this example, the over current threshold is 9.0 A and the value of the current sense resistor is


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 29


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


8.0 mΩ, which give a shunt voltage limit of 72 mV. Once the shunt voltage limit is known, the value for the shunt
over voltage limit register is calculated by dividing the shunt voltage limit by the shunt voltage LSB size.


For this case, the calculated value of the alert limit register is 72 mV / 2.5 μV = 28800d (7080h) .


Values stored in the alert limit register are set to the default values after V S power cycle events and need to be
reprogrammed each time power is applied.


_**8.2.2.5 Calculate Returned Values**_


Table 8-4 below shows the register values assuming the design requirements shown in Table 8-3. User
programmed values for the Configuration, Calibration, Mask/Enable and Alert limit registers are shown, as well
as, the returned values for shunt voltage, current, bus voltage and power. Parametric values are calculated by
multiplying the returned value by the LSB value.


**Table 8-4. Calculate Returned Values**

|Register|Contents|LSB Value|Calculated Value|
|---|---|---|---|
|Configuration (0h)|16679d (4127h)|—|—|
|Calibration (5h)|1280d (500h)|—|—|
|Mask/Enable (6h)|32768 (8000h)|—|—|
|Alert Limit (7h)|28800d (7080h)|2.5 μV/LSB|28800 × 2.5 μV = 0.072 V|
|Shunt Voltage (1h)|19200d (4B00h)|2.5 µV/LSB|19200 × 2.5 μV = 0.048 V|
|Bus Voltage (2h)|7500d (1D4Ch)|1.6 mV/LSB|7500 × 1.6 mV = 12 V|
|Current (4h)|12000d (2EE0h)|500 µA/LSB|12000 × 500 µA = 6 A|
|Power (3h)|4500d (1194h)|Current LSB x 32 = 16 mW/LSB|4500 × 16 mW = 72 W|



Shunt Voltage and Current return values in two's complement format. In two's complement format a negative
value in binary is represented by having a 1 in the most significant bit of the returned value. These values can
be converted to decimal by first inverting all the bits and adding 1 to obtain the unsigned binary value. This value
should then be converted to decimal with the negative sign applied.


**8.2.3 Application Curves**


Figure 8-3 shows the ALERT pin response to a shunt overvoltage limit of 72 mV for a conversion time (t CT )
of 140 µs and averaging set to 1. Figure 8-4 shows the response for the same limit but with the conversion
time increased to 1.1 ms. For the scope shots shown in these figures, persistence was enabled on the ALERT
channel. Figure 8-3 and Figure 8-4 show how the ALERT response time can vary depending on when the fault
condition occurs relative to the internal ADC clock of the INA236. For fault conditions that are just exceeding the
limit threshold, the response time for the ALERT pin can vary from one to two conversion cycles. As mentioned
previously, the variation is because of the timing on when the fault event occurs relative to the start time of the
internal ADC conversion cycle. For fault events that greatly exceed the limit threshold, the alert can respond in
less than one conversion cycle.











30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**8.3 Power Supply Recommendations**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



Figure 8-2 shows that the device input circuitry can accurately measure signals on common-mode voltages
beyond the power-supply voltage, V S . For example, the voltage applied to the vs. power supply pin can be 5 V,
whereas the bus power-supply voltage being monitored (the common-mode voltage) can be as high as 48 V.
The device can also withstand the full -0.3 V to 48 V range at the input pins, regardless of whether the device
has power applied or not.


Place the required power-supply bypass capacitors as close as possible to the supply and ground pins of the
device to ensure stability. A typical value for this supply bypass capacitor is 0.1 µF. Applications with noisy or
high-impedance power supplies can require additional decoupling capacitors to reject power-supply noise.


**8.4 Layout**


**8.4.1 Layout Guidelines**


Connect the input pins (IN+ and IN–) to the sensing resistor using a Kelvin connection or a 4-wire connection.
These connection techniques ensure that only the current-sensing resistor impedance is detected between
the input pins. Poor routing of the current-sensing resistor commonly results in additional resistance present
between the input pins. Given the very low ohmic value of the current-sensing resistor, any additional highcurrent carrying impedance causes significant measurement errors. Place the power-supply bypass capacitor as
close as possible to the supply and ground pins.


**8.4.2 Layout Example**


Bus Voltage





Device Address:

Connect to SDA,
SCL, VS, or GND


R PULLUP1


R PULLUP2


I [2] C Voltage:
1.2 V to 5.5 V







I [2] C Data



I [2] C Clock



Load



**Figure 8-5. INA236 Layout Example DSBGA (High Side)**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 31


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


Bus Voltage



Device Address:

Connect to SDA,
SCL, VS, or GND


R PULLUP1


R PULLUP2


I [2] C Voltage:
1.2 V to 5.5 V







I [2] C Data

















I [2] C Clock


|Col1|Col2|Col3|
|---|---|---|
||||
||||





Load



**Figure 8-6. INA236 Layout Example DDF (High Side)**


32 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**


**9 Device and Documentation Support**
**9.1 Device Support**


**9.1.1 Development Support**


For development support see the following:


_[INA234EVM and INA236EVM User's Guide](https://www.ti.com/lit/pdf/SBOU264)_ (SBOU264)


**9.2 Documentation Support**


**9.2.1 Related Documentation**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



For related documentation see the following:

 - Texas Instruments, _[Current Shunt Monitor with Transient Robustness Reference Design](https://www.ti.com/lit/pdf/TIDU473)_ (TIDU473)

 - Texas Instruments, _[INA234EVM and INA236EVM User's Guide](https://www.ti.com/lit/pdf/SBOU264)_ (SBOU264)


**9.3 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Subscribe to updates_ to register and receive a weekly digest of any product information that has changed. For
change details, review the revision history included in any revised document.


**9.4 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**9.5 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

**9.6 Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**9.7 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**10 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 33


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


34 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[www.ti.com](https://www.ti.com)**



**[INA236](https://www.ti.com/product/INA236)**

[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81)



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ 35


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


**[INA236](https://www.ti.com/product/INA236)**
[SBOSA81D – MAY 2021 – REVISED AUGUST 2023](https://www.ti.com/lit/pdf/SBOSA81) **[www.ti.com](https://www.ti.com)**


36 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SBOSA81D&partnum=INA236)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[INA236](https://www.ti.com/product/ina236?qgpn=ina236)_


### **PACKAGE OPTION ADDENDUM**

www.ti.com 24-Jul-2025


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


Addendum-Page 1


### **PACKAGE OPTION ADDENDUM**

www.ti.com 24-Jul-2025


and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Addendum-Page 2


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 8-Jul-2025


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
|INA236AIDDFR|SOT-23-<br>THIN|DDF|8|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|INA236AIYBJR|DSBGA|YBJ|8|3000|180.0|8.4|0.84|1.62|0.43|2.0|8.0|Q1|
|INA236AIYBJR|DSBGA|YBJ|8|3000|180.0|8.4|0.84|1.62|0.43|2.0|8.0|Q1|
|INA236BIDDFR|SOT-23-<br>THIN|DDF|8|3000|180.0|8.4|3.2|3.2|1.4|4.0|8.0|Q3|
|INA236BIYBJR|DSBGA|YBJ|8|3000|180.0|8.4|0.84|1.62|0.43|2.0|8.0|Q1|
|INA236BIYBJR|DSBGA|YBJ|8|3000|180.0|8.4|0.84|1.62|0.43|2.0|8.0|Q1|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 8-Jul-2025





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|INA236AIDDFR|SOT-23-THIN|DDF|8|3000|210.0|185.0|35.0|
|INA236AIYBJR|DSBGA|YBJ|8|3000|182.0|182.0|20.0|
|INA236AIYBJR|DSBGA|YBJ|8|3000|182.0|182.0|20.0|
|INA236BIDDFR|SOT-23-THIN|DDF|8|3000|210.0|185.0|35.0|
|INA236BIYBJR|DSBGA|YBJ|8|3000|182.0|182.0|20.0|
|INA236BIYBJR|DSBGA|YBJ|8|3000|182.0|182.0|20.0|



Pack Materials-Page 2


## **PACKAGE OUTLINE**

# **DDF0008A SOT-23-THIN - 1.1 mm max height**

~~SCALE 4.000~~


PLASTIC SMALL OUTLINE

















NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
exceed 0.15 mm per side.


www.ti.com


## **EXAMPLE BOARD LAYOUT**

# **DDF0008A SOT-23-THIN - 1.1 mm max height**

PLASTIC SMALL OUTLINE



















NOTES: (continued)

4. Publication IPC-7351 may have alternate designs.
5. Solder mask tolerances between and around signal pads can vary based on board fabrication site.


www.ti.com


## **EXAMPLE STENCIL DESIGN**

# **DDF0008A SOT-23-THIN - 1.1 mm max height**

PLASTIC SMALL OUTLINE












|Col1|Col2|
|---|---|
|||







NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
7. Board assembly site may have different recommendations for stencil design.


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


