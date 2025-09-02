**Description**



**Pin Assignments**



The AP22652, AP22653, AP22652A, and AP22653A are single
channel, precision-adjustable, current-limited switches optimized for

applications that require precision current limiting, or to provide up to

2.1A of continuous load current during heavy loads/short circuits.

These devices offer a programmable current-limit threshold between

125mA and 2665mA (typ) via an external resistor. Current-limit

accuracy ±10% can be achieved at high current-limit settings. The rise

and fall times are controlled to minimize current surges during turn

on/off.

The devices have fast short-circuit response time for improved overall

system robustness. They provide a complete protection solution for

applications subject to heavy capacitive loads and the prospect of short

circuit, offering reverse-current blocking and limiting, overcurrent,

overtemperature, and short-circuit protection, as well as controlled rise

time and undervoltage lockout functionality. A 6ms deglitch capability

on the open-drain flag output prevents false overcurrent reporting and

does not require any external components.

The AP22652 and AP22653 limit the output current to a safe level when

the output current exceeds current-limit threshold.

The AP22652A and AP22653A provide latch-off function during

overcurrent or reverse-voltage conditions.

All devices are available in the SOT26 (Type A1) and W-DFN2020-6

(Type A1) packages.


**Applications**


- Set-top boxes

- LCD TVs & monitors

- Residential gateways

- Laptops, desktops, servers, e-readers, printers, docking stations,

HUBs



**SOT26 (Type A1)**


**Features**


- Up to 2.1A Maximum Load Current

- Accurate Adjustable Current Limit, 125mA to 2665mA

- ±7% Accurate Adjustable Current Limit, 1.735A with R LIM = 15kΩ


- Constant-Current (AP22652/53) During Overcurrent

- Output Latch-Off (AP22652A/53A) at Overcurrent

- Fast Short-Circuit Response Time: 5µs (typ)

- Reverse Current Blocking During Shutdown and Reverse Current

Limiting During Enable

- Operating Range: 3.0V to 5.5V

- Built-In Soft-Start with 0.5ms Typical Rise Time

- Overcurrent, and Thermal Protection

- Fault Report (FAULT) with Blanking Time

- ESD Protection: 2kV HBM, 500V CDM

- 15kV ESD Protection per IEC61000-4-2 (With External Capacitance)

- UL Recognized, File Number E322375, Vol. 1

- IEC60950-1 CB Scheme Certified

- Active-Low (AP22652/52A) or Active-High (AP22653/53A) Enable

- Ambient Temperature Range: -40ºC to +85°C

- SOT26 (Type A1) and W-DFN2020-6 (Type A1) Packages:

Available in “Green” Molding Compound (No Br, Sb)

- **Totally Lead-Free & Fully RoHS Compliant (Notes 1 & 2)**

- **Halogen and Antimony Free. “Green” Device (Note 3)**

- **An automotive-compliant part is available under separate**

**[datasheet (AP22653Q)](https://www.diodes.com/datasheet/download/AP22653Q.pdf)**



**(Top View)**























Notes: 1. No purposely added lead. Fully EU Directive 2002/95/EC (RoHS), 2011/65/EU (RoHS 2) & 2015/863/EU (RoHS 3) compliant.
2. See https://www.diodes.com/quality/lead-free/ for more information about Diodes Incorporated’s definitions of Halogen- and Antimony-free, "Green" and
Lead-free.
3. Halogen- and Antimony-free "Green” products are defined as those which contain <900ppm bromine, <900ppm chlorine (<1500ppm total Br + Cl) and
<1000ppm antimony compounds.



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



1 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**



**Typical Applications Circuit** (Note 4)


Note: 4. 120µF output capacitance is a requirement of USB.


**Available Options**

















|Part Number|Channel|Enable Pin (EN/EN)|Recommended Maximum<br>Continuous Load Current (A)|Current-Limit<br>Protection|Package|
|---|---|---|---|---|---|
|AP22652|1|Active Low|2.1|Constant-Current|W-DFN2020-6 (Type A1)|
|AP22653|1|Active High|Active High|Active High|W-DFN2020-6 (Type A1)|
|AP22652|1|Active Low|Active Low|Active Low|SOT26 (Type A1)|
|AP22653|1|Active High|Active High|Active High|SOT26 (Type A1)|
|AP22652A|1|Active Low|Active Low|Latch-Off|W-DFN2020-6 (Type A1)|
|AP22653A|1|Active High|Active High|Active High|W-DFN2020-6 (Type A1)|
|AP22652A|1|Active Low|Active Low|Active Low|SOT26 (Type A1)|
|AP22653A|1|Active High|Active High|Active High|SOT26 (Type A1)|


**Pin Descriptions**

















|Pin<br>Name|Pin Number|Col3|Col4|Col5|I/O|Function|
|---|---|---|---|---|---|---|
|**Pin**<br>**Name**|**AP22652W6-7**<br>**AP22652AW6-7**|**AP22653W6-7**<br>**AP22653AW6-7**|**AP22652FDZ-7**<br>**AP22652AFDZ-7**|**AP22653FDZ-7**<br>**AP22653AFDZ-7**|**AP22653FDZ-7**<br>**AP22653AFDZ-7**|**AP22653FDZ-7**<br>**AP22653AFDZ-7**|
|IN|1|1|6|6|I|Input, connect a 0.1µF or greater ceramic capacitor<br>from IN to GND as close to IC as possible.|
|GND|2|2|5|5|—|Ground, connect to external exposed pad.|
|EN|3|—|4|—|I|Enable input, logic low turns on power switch.|
|EN|—|3|—|4|I|Enable input, logic high turns on power switch.|
|FAULT|4|4|3|3|O|Active-low open-drain output, asserted during<br>overcurrent, overtemperature, or reverse-voltage<br>conditions.|
|ILIM|5|5|2|2|O|Use external resistor to set current-limit threshold;<br>recommended 10kΩ≦ RLIM ≦ 210kΩ|
|OUT|6|6|1|1|O|Voltage Output Pin, connect a 0.1μF bypass<br>capacitor and a high-value capacitor to GND, close<br>to IC. (At least 10μF in USB application.)|
|Exposed<br>Pad|—|—|Pad|Pad|—|Internal connection to GND; Connect to GND<br>externally for improved power dissipation. It should<br>not be used as electrical ground conduction path.|


October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



2 of 17


**[www.diodes.com](http://www.diodes.com/)**


**Functional Block Diagram**



**AP22652/AP22653/AP22652A/AP22653A**



IN


EN/EN


ILIM


IN


EN/EN


ILIM





















October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



3 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**


**Absolute Maximum Ratings** (@T A = +25°C, unless otherwise specified.)











|Symbol|Col2|Parameter|Ratings|Unit|
|---|---|---|---|---|
|ESD|HBM|Human Body Model ESD Protection|2|kV|
|ESD|CDM|Charged Device Model ESD Protection|500|V|
|ESD|IEC System<br>Level|Surges per IEC61000-4-2. 1999 Applied to Output<br>Terminals of EVM (Note 6)|15|kV|
|VIN, VOUT, VFAULT, <br>VILIM, <br>,<br>EN<br>V<br>EN<br>V<br>|VIN, VOUT, VFAULT, <br>VILIM, <br>,<br>EN<br>V<br>EN<br>V<br>|Voltage on IN, OUT,FAULT, ILIM, EN,EN|-0.3 to +6.0|V|
|—|—|ContinuousFAULT Sink Current|25|mA|
|—|—|ILIM Source Current|1|mA|
|ILOAD|ILOAD|Maximum Continuous Load Current|Internal Limited|A|
|TJ(MAX)|TJ(MAX)|Maximum Junction Temperature|-40 to +150|°C|
|TSTG|TSTG|Storage Temperature Range (Note 5)|-65 to +150|°C|


Notes: 5. UL Recognized Rating from -30°C to +70°C (Diodes Incorporated qualified T STG from -65°C to +150°C).
6. External capacitors need to be connected to the output, EVM board was tested with external capacitor. This level is a pass test only and not a limit.


Caution: Stresses greater than the _Absolute Maximum Ratings_ specified above can cause permanent damage to the device. These are stress ratings only;
functional operation of the device at these or any other conditions exceeding those indicated in this specification is not implied. Device reliability can be
affected by exposure to absolute maximum rating conditions for extended periods of time.
Semiconductor devices are ESD sensitive and can be damaged by exposure to ESD events. Suitable ESD precautions should be taken when
handling and transporting these devices.

**Dissipation Rating Table**
























|Board|Package|Thermal<br>Resistance<br>θJA|Thermal<br>Resistance<br>θJC|TA ≤ +25°C<br>Power Rating|Derating Factor<br>Above<br>TA = +25°C|TA = +70°C<br>Power Rating|TA = +85°C<br>Power Rating|
|---|---|---|---|---|---|---|---|
|High-K (Note 7)|SOT26<br> (Type A1)|120**°**C/W|35**°**C/W|830mW|8.3mW/**°**C|450mW|330mW|
|High-K (Note 7)|W-<br>DFN2020-6<br>(Type A1)|95**°**C/W|25**°**C/W|1050mW|10.05mW/**°**C|570mW|420mW|



Note: 7. The JEDEC high-K (2s2p) board used to derive this data was a 3inch x 3inch, multilayer board with 1oz internal power and ground planes with
2oz copper traces on top and bottom of the board.

**Recommended Operating Conditions** (@T A = +25°C, unless otherwise specified.)


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|VIN|Input Voltage|3|5.5|V|
|IOUT|Continuous Output Current (-40°C ≤ TA ≤ +85°C)|0|2.1|A|
|,<br>EN<br>V<br>EN<br>V<br>|Enable Voltage|0|5.5|V|
|VIH|High-Level Input Voltage on EN orEN|1.5|VIN|V|
|VIL|Low-Level Input Voltage on EN orEN|0|0.4|V|
|RLIM|Current-Limit Threshold Resistor Range<br>(1% Initial Tolerance)|10|210|kΩ|
|IO|ContinuousFAULT  Sink Current|0|10|mA|
|—|Input De-Coupling Capacitance, IN to GND|0.1|—|µF|
|TA|Operating Ambient Temperature|-40|+85|°C|
|TJ|Operating Junction Temperature|-40|+125|°C|



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



4 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**


**Electrical Characteristics** (@T A = +25°C, V IN = 3.0V to 5.5V, V EN = 0V or V EN = V IN, R FAULT = 10kΩ, unless otherwise specified.)































|Symbol|Parameter|Test Conditions (Note 8)|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|**Supply**<br>|**Supply**<br>|**Supply**<br>|**Supply**<br>|**Supply**<br>|**Supply**<br>|**Supply**<br>|**Supply**<br>|
|VUVLO|Input UVLO|VIN Rising|VIN Rising|— <br>|2.65|2.95|V|
|VUVLO|Input UVLO Hysteresis|VIN Decreasing|VIN Decreasing|— <br>|65|—|mV|
|ISHDN|Input Shutdown Current|VIN= 5.5V, Disabled, OUT = Open|VIN= 5.5V, Disabled, OUT = Open|— <br>|0.1|1|µA|
|IQ|Input Quiescent Current|VIN= 5.5V, Enabled, OUT = Open, RLIM = 20kΩ|VIN= 5.5V, Enabled, OUT = Open, RLIM = 20kΩ|— <br>|140|160|µA|
|IQ|Input Quiescent Current|VIN= 5.5V, Enabled, OUT = Open, RLIM = 210kΩ|VIN= 5.5V, Enabled, OUT = Open, RLIM = 210kΩ|— <br>|120|140|µA|
|IREV|Reverse Leakage Current|Disabled, VIN= 0V, VOUT= 5.5V, IREV at VIN|Disabled, VIN= 0V, VOUT= 5.5V, IREV at VIN|—|0.01|1|µA|
|**Power Switch**|**Power Switch**|**Power Switch**|**Power Switch**|**Power Switch**|**Power Switch**|**Power Switch**|**Power Switch**|
|RDS(ON)|Switch On-Resistance|SOT26 (Type A1) Package|TJ = +25°C, VIN= 5.0V|—|65|90|mΩ|
|RDS(ON)|Switch On-Resistance|SOT26 (Type A1) Package|-40°C≤ TA ≤ +85°C|—|—|135|135|
|RDS(ON)|Switch On-Resistance|W-DFN2020-6 (Type A1)<br>Package|TJ = +25°C, VIN= 5.0V|—|65|90|90|
|RDS(ON)|Switch On-Resistance|W-DFN2020-6 (Type A1)<br>Package|-40°C≤ TA ≤ +85°C|—|—|135|135|
|tR|Output Turn-On Rise Time|VIN = 5.5V, CL = 1µF, RLOAD= 100Ω. See Figure 1|VIN = 5.5V, CL = 1µF, RLOAD= 100Ω. See Figure 1|—|0.5|1.5|ms|
|tR|Output Turn-On Rise Time|VIN = 3.0V, CL = 1µF, RLOAD= 100Ω|VIN = 3.0V, CL = 1µF, RLOAD= 100Ω|—|0.3|1|ms|
|tF|Output Turn-Off Fall Time|VIN = 5.5V, CL = 1µF, RLOAD= 100Ω. See Figure 1|VIN = 5.5V, CL = 1µF, RLOAD= 100Ω. See Figure 1|0.1|—|0.5|ms|
|tF|Output Turn-Off Fall Time|VIN = 3.0V, CL = 1µF, RLOAD= 100Ω|VIN = 3.0V, CL = 1µF, RLOAD= 100Ω|0.1|—|0.5|ms|
|**Current Limit**|**Current Limit**|**Current Limit**|**Current Limit**|**Current Limit**|**Current Limit**|**Current Limit**|**Current Limit**|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 10kΩ|TA = +25°C|2478|2665|2852|mA|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 10kΩ|-40°C≤ TA ≤ +85°C|2398|2665|2931|2931|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 15kΩ|TA = +25°C|1614|1735|1856|1856|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 15kΩ|-40°C≤ TA ≤ +85°C|1561|1735|1908|1908|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 20kΩ|TA = +25°C|1196|1286|1376|1376|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 20kΩ|-40°C≤ TA ≤ +85°C|1157|1286|1414|1414|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 49.9kΩ|TA = +25°C|456|490|524|524|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 49.9kΩ|-40°C≤ TA ≤ +85°C|441|490|539|539|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIM = 210kΩ|TA = +25°C|95|125|155|155|
|ILIMIT|Current-Limit Threshold<br>(Maximum DC Output Current),<br>VIN= 5V, VOUT= 4.5V|RLIMShorted to GND|RLIMShorted to GND|40<br>|80|120<br>|120<br>|
|ISHORT|Short-Circuit Current Limit, OUT<br>Connected to GND|RLIM = 10kΩ, TA = +25°C|RLIM = 10kΩ, TA = +25°C|— <br>|700|— <br>|mA|
|ISHORT|Short-Circuit Current Limit, OUT<br>Connected to GND|RLIM = 15kΩ, TA = +25°C|RLIM = 15kΩ, TA = +25°C|— <br>|470|— <br>|— <br>|
|ISHORT|Short-Circuit Current Limit, OUT<br>Connected to GND|RLIM = 20kΩ, TA = +25°C|RLIM = 20kΩ, TA = +25°C|— <br>|350|— <br>|— <br>|
|ISHORT|Short-Circuit Current Limit, OUT<br>Connected to GND|RLIM = 49.9kΩ, TA = +25°C|RLIM = 49.9kΩ, TA = +25°C|— <br>|140|— <br>|— <br>|
|ISHORT|Short-Circuit Current Limit, OUT<br>Connected to GND|RLIM = 210kΩ, TA = +25°C|RLIM = 210kΩ, TA = +25°C|—|35|—|—|
|ISHORT|Short-Circuit Current Limit, OUT<br>Connected to GND|RLIMShorted to GND, TA = +25°C|RLIMShorted to GND, TA = +25°C|—|80|—|—|
|**Enable Pin**|**Enable Pin**|**Enable Pin**|**Enable Pin**|**Enable Pin**|**Enable Pin**|**Enable Pin**|**Enable Pin**|
|ILEAK-EN|EN Input Leakage Current|VIN = 5V, VEN= 0V and 5.5V|VIN = 5V, VEN= 0V and 5.5V|-2|—|2|µA|
|tON|Turn-On Time|CL = 1µF, RL = 100Ω. See Figure 1|CL = 1µF, RL = 100Ω. See Figure 1|—|—|4|ms|
|tOFF|Turn-Off Time|CL = 1µF, RL = 100Ω. See Figure 1|CL = 1µF, RL = 100Ω. See Figure 1|—|—|1|ms|
|**Output Discharge**|**Output Discharge**|**Output Discharge**|**Output Discharge**|**Output Discharge**|**Output Discharge**|**Output Discharge**|**Output Discharge**|
|RDIS|Discharge Resistance (Note 9)|VIN = 5V, Disabled, IOUT = 1mA|VIN = 5V, Disabled, IOUT = 1mA|—|600|—|Ω|


Notes: 8. Pulse-testing techniques maintain junction temperature close to ambient temperature; thermal effects must be taken into account separately.
9. The discharge function is active when the device is disabled (when enable is de-asserted or during power-up power-down when V IN < V UVLO ).
The discharge function offers a resistive discharge path for the external storage capacitor for limited time.



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



5 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**

|Electrical Characteristics (continued) (@TA = +25°C, VIN = 3.0V to 5.5V, VEN = 0V or VEN = VIN, RFAULT = 10kΩ, unless otherwise specified.)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|**Symbol**|**Parameter**|**Test Conditions (Note 8)**|**Min**|**Typ**|**Max**|**Unit**|
|**Reverse Voltage Protection**|**Reverse Voltage Protection**|**Reverse Voltage Protection**|**Reverse Voltage Protection**|**Reverse Voltage Protection**|**Reverse Voltage Protection**|**Reverse Voltage Protection**|
|VRVP|Reverse-Voltage Comparator Trip Point|VOUT - VIN|—|65|—|mV|
|IROCP|Reverse Current Limit|VOUT- VIN= 150mV|—|0.32|—|A|
|tTRIG|Time from Reverse-Voltage Condition to<br>MOSFET Turn Off|VIN = 5V|2|6|20|ms|
|**Fault Flag**|**Fault Flag**|**Fault Flag**|**Fault Flag**|**Fault Flag**|**Fault Flag**|**Fault Flag**|
|VOL|FAULT Output Low Voltage|IFAULT = 1mA|—|—|180|mV|
|IFOH|FAULT Off Current|VFAULT= 5.5V|—|—|1|µA|
|tBLANK|FAULT Blanking Time|Assertion or deassertion due to overcurrent and<br>overtemperature condition|2|6|20|ms|
|**Thermal Shutdown**|**Thermal Shutdown**|**Thermal Shutdown**|**Thermal Shutdown**|**Thermal Shutdown**|**Thermal Shutdown**|**Thermal Shutdown**|
|TSHDN|Thermal Shutdown Threshold|Enabled|—|+145|—|°C|
|THYS|Thermal Shutdown Hysteresis|Only for AP22652 and AP22653|—|+40|—|°C|



Note: 8. Pulse-testing techniques maintain junction temperature close to ambient temperature; thermal effects must be taken into account separately.


**Typical Performance Characteristics**



**V** **EN**











**V** **EN**







**V** **OUT**



**V** **OUT**



Figure 1. Voltage Waveforms: AP22652/52A (Left), AP22653/53A (Right)



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



6 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**



**Typical Performance Characteristics** (continued)



**1ms/div**
Figure 5. No Load to 1Ω Transient Response





**1ms/div**
Figure 2. Turn-On Delay and Rise Time


**1ms/div**
Figure 4. Device Enabled into Short-Circuit





**400µs/div**
Figure 3. Turn-Off Delay and Fall Time











**2ms/div**


Figure 6. Short-Circuit Current Limit Response


AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



**200ms/div**

Figure 7. Extended Short-Circuit into Thermal Cycles



7 of 17


**[www.diodes.com](http://www.diodes.com/)**



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.


**AP22652/AP22653/AP22652A/AP22653A**


**Typical Performance Characteristics** (continued)


**1ms/div**


Figure 8. Reverse Current Limit Response Figure 9. Reverse Current Limit vs. Temperature



Figure 10. Input Quiescent Current vs. Temperature Figure 11. Input Quiescent Current vs. Temperature


Figure 12. Switch On-Resistance vs. Temperature Figure 13. Undervoltage Lockout vs. Temperature



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



8 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**


**Application Information**


The AP22652/52A and AP22653/53A are integrated high-side power switches optimized for universal serial bus (USB) that require protection
functions. The power switches are equipped with a driver that controls the gate voltage and incorporates slew-rate limitation. This, along with the
various protection features and special functions, makes these power switches ideal for hot-swap or hot-plug applications.

**Protection Features**

**Undervoltage Lockout (UVLO)**
Whenever the input voltage falls below UVLO threshold (~2.5V), the power switch is turned off. This facilitates the design of hot-insertion systems
where it is not possible to turn off the power switch before input power is removed.

**Overcurrent and Short-Circuit Protection**

An internal sensing FET is employed to check for overcurrent conditions. Unlike current-sense resistors, sense FETs do not increase the series
resistance of the current path. When an overcurrent condition is detected, the AP22652 and AP22653 maintain a constant output current and reduce
the output voltage accordingly. Complete shutdown occurs only if the fault stays long enough to activate thermal limiting.

For AP22652A/53A, when an overcurrent condition is detected, the devices will limit the current until the overload condition is removed or the internal

deglitch time (6ms typical) is reached, and AP22652A/53A will be turned off. The AP22652A/53A will remain latched off until power is cycled or the
device enable is toggled.

The different overload conditions and the corresponding response of the AP22652/52A and AP22653/53A are outlined below:












|NO.|Conditions|Explanation|Behavior of the AP22652 and AP22653|
|---|---|---|---|
|1|Short-circuit condition at<br>startup|Output is shorted before input<br>voltage is applied or before the<br>part is enabled.|The IC senses the short circuit and immediately clamps output<br>current to a certain safe level namely ISHORT.|
|2|Short-circuit or overcurrent<br>condition|Short-circuit or overload condition<br>that occurs when the part is<br>enabled.|• At the instance the overload occurs, higher current may flow for<br>a very short period of time before the current limit function can<br>react.<br>• After the current limit function has tripped (reached the<br>overcurrent trip threshold), the device switches into current<br>limiting mode and the current is clamped at ISHORT/ILIMIT.|
|3|Gradual increase from<br>nominal operating current to<br>ILIMIT|Load increases gradually until the<br>current-limit threshold. (ITRIG)|The current rises until ILIMITor thermal limit. Once the threshold has<br>been reached, the device switches into its current limiting mode<br>and is set at ILIMIT.|














|NO.|Conditions|Explanation|Behavior of the AP22652A/53A|
|---|---|---|---|
|1|Short-circuit condition at<br>startup|Output is shorted before input<br>voltage is applied or before the<br>part is enabled|The IC senses the short circuit and immediately clamps output<br>current to a certain safe level namely ISHORT.When the internal<br>deglitch time (6ms typical) is reached and the devices will be<br>turned off.|
|2|Short-circuit or overcurrent<br>condition|Short-circuit or overload condition<br>that occurs when the part is<br>enabled.|• At the instance the overload occurs, higher current may flow for<br>a very short period of time before the current limit function can<br>react.<br>• After the current limit function has tripped (reached the<br>overcurrent trip threshold), the device switches into current<br>limiting mode and the current is clamped at ISHORT/ILIMIT. When <br>the internal deglitch time (6ms typical) is reached and the<br>devices will be turned off.|
|3|Gradual increase from<br>nominal operating current to<br>ILIMIT|Load increases gradually until the<br>current-limit threshold. (ITRIG)|The current rises until ILIMITor thermal limit. Once the threshold has<br>been reached, the device switches into its current limiting mode<br>and is set at ILIMIT. When the internal deglitch time (6ms typical) is<br>reached, the devices will be turned off.|



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



9 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**


**Application Information** (continued)


**Current-Limit Threshold Programming**
The current-limit threshold can be programmed using an external resistor. The current-limit threshold is proportional to the current sourced out of
I LIM .

The recommended 1% resistor range for R LIM is 10kΩ ≤ R LIM ≤ 210kΩ. Figure 14 includes current-limit tolerance due to variations caused by
temperature and process. This graph does not include the external resistor tolerance. The traces routing the RLIM resistor to the AP22652/52A and
AP22653/53A should be as short as possible to reduce parasitic effects on the current-limit accuracy.

To design below a maximum current-limit threshold, find the intersection of R LIM and the maximum desired load current on the I OS(max) (I LIM ) curve
and choose a value of R LIM above this value. Programming the current limit below a maximum threshold is important to avoid current limiting
upstream power supplies causing the input voltage bus to drop. The resulting minimum current-limit threshold is the intersection of the selected
value of R LIM and the I OS(min) (I LIM ) curve.

Best-Fit Current-Limit Threshold Equations (I LIMIT ):

I LIMIT_Min **[mA]** = 28955/R[kΩ] [1.075] I LIMIT_Typ **[mA]** = 30321/R[k Ω ] [1.055] I LIMIT_Max **[mA]** = 31033/R[k Ω ] [1.031 ]

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||IN=5||
|||||||||
|||||||||
|||||||||
|||||||||
|IL|IM(max|)||||||
|||||||||
|||I(t|p)|||||
|||LIM||||||
|||||||||
|ILIM(|min)|||||||



**R** **LIM** **Current-Limit Programming Resistor (kΩ)**


Figure 14. Current-Limit Threshold vs. R LIM

**Thermal Protection**
Thermal protection prevents the IC from damage when the die temperature exceeds safe margins. This mainly occurs when heavy-overload or
short-circuit faults are present for extended periods of time. The AP22652/52A and AP22653/53A implement a thermal sensing to monitor the
operating junction temperature of the power distribution switch. Once the die temperature rises to approximately +145°C, the thermal protection
feature activates as follows: The internal thermal sense circuitry turns the power switch off and the FAULT output is asserted, thus preventing the
power switch from damage. Hysteresis in the thermal sense circuit allows the device to cool down by approximately +40°C before the output is
turned back on. This built-in thermal hysteresis feature is an excellent feature, as it avoids undesirable oscillations of the thermal protection circuit.

**Reverse-Current and Reverse-Voltage Protection**
The USB specification does not allow an output device to source current back into the USB port. In a normal MOSFET switch, current will flow in
reverse direction (from the output side to the input side) when the output side voltage is higher than the input side. A reverse-current limit (ROCP)
feature is implemented in the AP22652/52A and AP22653/53A to limit such back currents. The ROCP circuit is activated when the output voltage is
higher than the input voltage. After the reverse current circuit has tripped (reached the reverse current trip threshold), the current is clamped at this
IROCP level.

In addition to ROCP, reverse overvoltage protection (ROVP) is also implemented. The ROVP circuit is activated by the reverse voltage comparator
trip point; i.e., the difference between the output voltage and the input voltage.

For AP22652/53, once ROVP is activated, FAULT assertion occurs at a de-glitch time of 6ms. Recovery from ROVP is automatic when the fault is
removed. FAULT de-assertion de-glitch time is same as the de-assertion time.

For AP22652A/53A, once ROVP is activated and when the condition exists for more than 5ms (typ), output device is disabled and shut down. This
is called the "Time from Reverse-Voltage Condition to MOSFET Turn Off". FAULT assertion occurs at a de-glitch time of 6ms after ROVP is reached.
Recovery from this fault is achieved by recycling power or toggling EN. FAULT de-assertion de-glitch time is same as the de-assertion time.



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



10 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**


**Application Information** (continued)


**Special Functions**
**Discharge Function**
When enable is de-asserted, or when the input voltage is under UVLO level, the discharge function is active. The output capacitor is discharged
through an internal NMOS that has a discharge resistance of 600Ω. Hence, the output voltage drops down to zero. The time taken for discharge is
dependent on the RC time constant of the resistance and the output capacitor.

**FAULT Response**
The FAULT open-drain output goes active low for any of following faults: overcurrent, OUT pin short-circuit, reverse-voltage condition, or thermal
shutdown. The time from when a fault condition is encountered to when the FAULT output goes low is 6ms (typ). The FAULT output remains low
until overcurrent, OUT pin short-circuit, and overtemperature conditions are removed. Connecting a heavy capacitive load to the output of the device
can cause a momentary overcurrent condition, which does not trigger the FAULT due to the 6ms deglitch timeout. This 6ms timeout is also applicable
for overcurrent recovery and overtemperature recovery. The AP22652 and AP22653 are designed to eliminate erroneous overcurrent reporting
without the need for external components, such as an RC delay network.

For the AP22652/52A and AP22653/53A when the reverse voltage condition is triggered, FAULT output goes low after 6ms (typ). This 6ms (typ)
timeout is also applicable for the recovery from reverse voltage fault. The Flag Current is always higher than Current Limit threshold to ensure
maximum loading consuming.

When the ILIM pin is shorted to GND, current-limit threshold and short-circuit current limit will be clamped at typically 100mA. When the ILIM pin is
shorted to GND, the AP22652/53 and AP22652A/53A FAULT pin will assert during current-limiting and short-circuit conditions.

For latch-off version, once Fault signal is triggered, the device will stay off until EN pin is toggled or power is restarted.

**Power Supply Considerations**
A 0.01μF to 0.1μF, X7R or X5R ceramic bypass capacitor between IN and GND, close to the device, is recommended. This limits the input voltage
drop during line transients. Placing a high-value electrolytic capacitor on the input (10μF minimum) and output pin (120µF) is recommended when
the output load is heavy. This precaution also reduces power-supply transients that may cause ringing on the input. Additionally, bypassing the
device output with a 0.1μF to 4.7μF ceramic capacitor improves the immunity of the device to short-circuit transients. This capacitor also prevents
output from going negative during turn-off due to parasitic inductance.

**Power Dissipation and Junction Temperature**
The low on-resistance of the internal MOSFET allows the small surface-mount packages to pass large current. Using the maximum operating
ambient temperature (T A ) and R DS(ON), the power dissipation can be calculated by:

P D = R DS(ON) × I [2]

Finally, calculate the junction temperature:

T J = P D x Θ JA + T A

Where:

T A = Ambient temperature °C

θ JA = Thermal resistance

P D = Total power dissipation

**Generic Hot-Plug Applications**
In many applications, it may be necessary to remove modules or PC boards while the main unit is still operating. These are considered hot-plug
applications. Such implementations require the control of current surges seen by the main power supply and the card being inserted. The most
effective way to control these surges is to limit and slowly ramp the current and voltage being applied to the card, similar to the way in which a power
supply normally turns on. Due to the controlled rise and fall times of the AP22652/52A and AP22653/53A, these devices can be used to provide a
softer startup to devices being hot-plugged into a powered system. The UVLO feature of the AP22652/52A and AP22653/53A also ensures that the
switch is off after the card has been removed, and that the switch is off during the next insertion.

**Generic Hot-Plug Applications**
By placing the AP22652/52A and AP22653/53A between the V CC input and the rest of the circuitry, the input power reaches these devices first after
insertion. The typical rise time of the switch is approximately 1ms, providing a slow voltage ramp at the output of the device. This implementation
controls system surge current and provides a hot-plugging mechanism for any device.



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



11 of 17


**[www.diodes.com](http://www.diodes.com/)**


**Ordering Information**



**AP22652/AP22653/AP22652A/AP22653A**


**AP2265 X X X - X**



2 : Active Low Blank : Non Latch-off W6 : SOT26 (Type A1) 7; 7B: 7” 7 ;-7B : Tape & Reel Tape & Reel
3 : Active High A : Latch-off FDZ : W-DFN2020-6

(Type A1)




























































|Type|Orderable Part<br>Number|Enable<br>Active|Output<br>Fault<br>Condition|Package<br>Code|Package|Part<br>Number<br>Suffix|Packing|Col9|
|---|---|---|---|---|---|---|---|---|
|**Type**|**Orderable Part**<br>**Number**|**Enable**<br>**Active**|**Output**<br>**Fault**<br>**Condition**|**Package**<br>**Code**|**Package**|**Part**<br>**Number**<br>**Suffix**|**Qty.**|**Carrier**|
|Consumer<br>Grade|AP22652W6-7|Low|Output<br>Current<br>Limits|W6|SOT26<br> (Type A1)|-7|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22652FDZ-7|AP22652FDZ-7|AP22652FDZ-7|FDZ|W-DFN2020-6<br>(Type A1)|-7; -7B|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22653W6-7|High|High|W6|SOT26<br>(Type A1)|-7|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22653FDZ-7|AP22653FDZ-7|AP22653FDZ-7|FDZ|W-DFN2020-6<br>(Type A1)|-7; -7B|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22652AW6-7|Low|Output<br>Latches<br>Off|W6|SOT26<br>(Type A1)|-7|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22652AFDZ-7|AP22652AFDZ-7|AP22652AFDZ-7|FDZ|W-DFN2020-6<br>(Type A1)|-7; -7B|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22653AW6-7|High|High|W6|SOT26<br>(Type A1)|-7|3000|7” Tape & Reel|
|Consumer<br>Grade|AP22653AFDZ-7|AP22653AFDZ-7|AP22653AFDZ-7|FDZ|W-DFN2020-6<br>(Type A1)|-7; -7B|3000|7” Tape & Reel|



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



12 of 17


**[www.diodes.com](http://www.diodes.com/)**


**Marking Information**


**(1) SOT26 (Type A1)**



**(Top View)**





**AP22652/AP22653/AP22652A/AP22653A**


XX : Identification Code

Y : Year 0~9


W : Week : A~Z : 1~26 week;

a~z : 27~52 week; z represents
52 and 53 week


X : Internal Code








|Col1|6|Col3|5|Col5|4<br>7|Col7|
|---|---|---|---|---|---|---|
|**XX Y W X**|**XX Y W X**|**XX Y W X**|**XX Y W X**|**XX Y W X**|**XX Y W X**|**XX Y W X**|
||1||2||3||





|Type|Orderable Part Number|Package|Identification Code|
|---|---|---|---|
|Consumer Grade|AP22652W6-7|SOT26 (Type A1)|FJ|
|Consumer Grade|AP22653W6-7|SOT26 (Type A1)|FK|
|Consumer Grade|AP22652AW6-7|SOT26 (Type A1)|FR|
|Consumer Grade|AP22653AW6-7|SOT26 (Type A1)|FS|


**(2) W-DFN2020-6 (Type A1)**



**(Top View)**

XX : Identification Code



Y : Year : 0~9


W : Week : A~Z : 1~26 week;



Y W X a~z : 27~52 week; z represents
52 and 53 week



X : Internal Code






|Type|Orderable Part Number|Package|Identification Code|
|---|---|---|---|
|Consumer Grade|AP22652FDZ-7|W-DFN2020-6 (Type A1)|FJ|
|Consumer Grade|AP22653FDZ-7|W-DFN2020-6 (Type A1)|FK|
|Consumer Grade|AP22652AFDZ-7|W-DFN2020-6 (Type A1)|FR|
|Consumer Grade|AP22653AFDZ-7|W-DFN2020-6 (Type A1)|FS|



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



13 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**



**Package Outline Dimensions**


Please see http://www.diodes.com/package-outlines.html for the latest version.

**(1) Package Type: SOT26 (Type A1)**








|Col1|D|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||b<br>|b<br>|b<br>|b<br>|E1|
|||||||
|||||||
|||||||
|||||||


|SOT26 (Type A1)|Col2|Col3|Col4|
|---|---|---|---|
|**Dim**|**Min**|**Max**|**Typ**|
|**A **|--|1.45|--|
|**A1**|0.00|0.15|--|
|**A2**|0.90|1.30|1.15|
|**b **|0.30|0.50|--|
|**c **|0.08|0.22|--|
|**D **|2.90 BSC|2.90 BSC|2.90 BSC|
|**E **<br>|2.80 BSC<br>|2.80 BSC<br>|2.80 BSC<br>|
|**E1**<br>**e **|1.60 BSC<br>0.95 BSC|1.60 BSC<br>0.95 BSC|1.60 BSC<br>0.95 BSC|
|**e1**|1.90 BSC|1.90 BSC|1.90 BSC|
|**L **|0.30|0.60|0.45|
|**L1**|0.60 REF|0.60 REF|0.60 REF|
|**L2**|0.25 BSC|0.25 BSC|0.25 BSC|
|**R **|0.10|--|--|
|**R1**|0.10|0.25|--|
|**θ **|0°|8°|4°|
|**θ1**|5°|15°|10°|
|**All Dimensions in mm**|**All Dimensions in mm**|**All Dimensions in mm**|**All Dimensions in mm**|







c


DETAIL 1


Seating Plane





E



DE TAIL 1


Gauge Plane


Seating Plane





~~01~~


01


|A A2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|A<br>A2||||||
|A<br>A2||||||
|||||||



**(2) Package Type: W-DFN2020-6** **(Type A1)**



C0.20x45°





|W-DFN2020-6<br>Type A1|Col2|Col3|Col4|
|---|---|---|---|
|**Dim**|**Min**|**Max**|**Typ**|
|**A **|0.70|0.80|0.75|
|**A1**|0.00|0.05|0.02|
|**A3**|0.20 REF|0.20 REF|0.20 REF|
|**b **|0.25|0.35|0.30|
|**D **|2.00 BSC|2.00 BSC|2.00 BSC|
|**D2**|1.35|1.45|1.40|
|**E **<br>|2.00 BSC<br><br><br>|2.00 BSC<br><br><br>|2.00 BSC<br><br><br>|
|**E2**|0.55|0.65|0.60|
|**e **|0.65 BSC|0.65 BSC|0.65 BSC|
|**k **|0.20|––|––|
|**L **|0.25|0.35|0.30|
|**All Dimensions in mm**|**All Dimensions in mm**|**All Dimensions in mm**|**All Dimensions in mm**|


October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



1 3 1


|Col1|D|Col3|Col4|
|---|---|---|---|
|||||
||||E|
|1||||
|1||||



e


|4 6<br>L<br>D2<br>E|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|L||||||
|||||||
|||||||
||||||E|
|||||||
|k||||||
|3||||||
|3||b<br>|e|e|e|



|Col1|Col2|Col3|A3<br>A|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|A1|A1|A1|A1|||


AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



Seating Plane



14 of 17


**[www.diodes.com](http://www.diodes.com/)**


**Suggested Pad Layout**


Please see http://www.diodes.com/package-outlines.html for the latest version.

**(1) Package Type: SOT26 (Type A1)**



**AP22652/AP22653/AP22652A/AP22653A**






|Dimensions|Value<br>(in mm)|
|---|---|
|**C **|0.950|
|**G **|1.600|
|**X **|0.700|
|**Y **|0.900|
|**Y1**|3.400|



|C C|Col2|Col3|
|---|---|---|
|G<br>Y<br><br>X<br>|G<br>Y<br><br>X<br>|G<br>Y<br><br>X<br>|
|G<br>Y<br><br>X<br>|X|X|
|G<br>Y<br><br>X<br>|X||


**(2) Package Type: W-DFN2020-6** **(Type A1)**




|X|Col2|
|---|---|
|||
|||






|Dimensions|Value<br>(in mm)|
|---|---|
|**C **<br>|0.65<br>|
|**X **|0.38|
|**X1**<br>|1.50<br>|
|**Y **<br>|0.45<br>|
|**Y1**|0.70|
|**Y2**|2.10|


|X|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Y<br>X1<br><br>Y1<br>C<br>Y|Y<br>X1<br><br>Y1<br>C<br>Y|Y<br>X1<br><br>Y1<br>C<br>Y|Y<br>X1<br><br>Y1<br>C<br>Y|Y<br>X1<br><br>Y1<br>C<br>Y|
|Y<br>X1<br><br>Y1<br>C<br>Y|||||
|X1|||||
|X1|||||
|X1|||||
|X1|||||



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



15 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**


**Mechanical Data**


**SOT26 (Type A1)**

- Moisture Sensitivity: Level 1 per J-STD-020

- Terminals: Finish – Matte Tin Plated Leads, Solderable per MIL-STD-202, Method 208

- Weight: 0.016 grams (Approximate)

**W-DFN2020-6 (Type A1)**

- Moisture Sensitivity: Level 1 per J-STD-020

- Terminals: Finish – Matte Tin Plated Leads, Solderable per MIL-STD-202, Method 208

- Weight: 0.0075 grams (Approximate)

**Pin 1 Orientation**


- Pin 1 in second quadrant for -7 (top left):


- Pin 1 in second quadrant for -7B (top right):



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



16 of 17


**[www.diodes.com](http://www.diodes.com/)**


**AP22652/AP22653/AP22652A/AP22653A**



October 2024
© 2024 Copyright Diodes Incorporated. All Rights Reserved.



AP22652/AP22653/AP22652A/AP22653A

Document number: DS41186 Rev. 4 - 2



17 of 17


**[www.diodes.com](http://www.diodes.com/)**


