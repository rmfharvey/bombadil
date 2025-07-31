_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025

## **TAS6511-Q1 - 50W, 2MHz Digital Input 1-Channel Automotive Heatsink-Free Class-D** **Audio Amplifier with Current Sense and Real-time Load Diagnostics**



**1 Features**


- AEC-Q100 qualified for automotive applications
– Temperature grade 1: –40°C to +125°C, T A

- General operation

–
4.5V to 19V supply voltage, 40V load dump

–
Support for 1.8V and 3.3V I/O’s
– I [2] C control with 8 address options

–
<0.5W idle power loss at 14.4V, <5uA max
PVDD shutdown loss

- Output current sensing via I [2] S or TDM

–
No need for external circuitry

- Real-time load diagnostics

–
Monitor output conditions while playing audio

–
Open load, Shorted load, Short-to-power,
Short-to-ground detection

- Integrated DSP processing

–
Thermal monitoring and foldback

–
PVDD monitoring and foldback

–
Clip detection

–
Low Latency Path, >70% reduced signal delay
at 48kHz

- DC and AC Standby load diagnostics

- Audio inputs
– I [2] S and TDM support up to TDM16

–
Input sample rates: 16, 32, 44.1, 48, 96,
192kHz

- Audio outputs

–
384kHz to 2MHz configurable output switching
frequency

–
Up to 7A channel output current

–
30W (14.4V, 4Ω, 10% THD+N)

–
50W (14.4V, 2Ω, 10% THD+N)

- Audio Performance

–
THD+N <0.02% (4Ω, 1W, 1kHz)
– 108dB SNR

–
Output noise: 41μV RMS at 14.4V, A-weighting

- Protection

–
Output short protection

–
Speaker Guard [TM] Pro power limiter

–
Configurable overtemperature warning and
shutdown
– I [2] C temperature and supply voltage readout

–
DC offset, undervoltage and overvoltage

- Easily meet CISPR25-L5 EMC specification

–
Advanced spread-spectrum


**2 Applications**


- [Acoustic vehicle alerting system (AVAS)](https://www.ti.com/solution/acoustic-vehicle-alerting-system-avas)

- [Emergency call (eCall)](https://www.ti.com/solution/emergency-call-ecall)




- [Automotive head unit](https://www.ti.com/solution/automotive-head-unit)

- [Telematics control unit](https://www.ti.com/solution/automotive-telematics-control-unit)

- [Automotive cluster display](https://www.ti.com/solution/automotive-cluster-display)


**3 Description**


The TAS6511-Q1 is a mono-channel, digital-input,
Class-D audio amplifier that supports 2MHz switching
frequency enabling a cost and size-optimized singlechannel audio amplifier design. The device operates
from 4.5V to 19V and delivers up to 30W (14.4V,
4Ω, 10% THD+N) and up to 50W (14.4V, 2Ω, 10%
THD+N). The device integrates DC and AC load
diagnostics to determine the status of the connected
load before enabling the output stage. Additionally,
the device can monitor the output load condition while
in PLAY mode with or without audio using real-time
load diagnostics which operates independently from
the host and audio input.


TAS6511-Q1 can monitor the output current, PVDD
voltage, and temperature of the device and can
report this data through TDM or I2S. The integrated
DSP of the TAS6511-Q1 enables advanced protection
features such as PVDD foldback, thermal foldback,
and Speaker Guard™ Pro power limiter. The DSP
also enables an additional low-latency signal path,
providing up to 70% faster signal processing at 48kHz
for time-sensitive Active Noise Cancellation (ANC)
and Road Noise Cancellation (RNC) applications.


The device is available in a small pad-down TSSOP
package, enabling a heatsink-free audio amplifier
design.


**Packaging Information**

|PART NUMBER|PACKAGE(1)|PACKAGE SIZE(2)|
|---|---|---|
|TAS6511-Q1|HTSSOP (28)|6.4mm × 9.7mm|



(1) For more information, see Mechanical, Packaging, and
Orderable Information.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.








|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|Current Sense<br>Real-Time Diagnos<br>cs|||||


|I2C<br>System µP<br>I2S /<br>TDM|TAS6511-Q1<br>Current Sense<br>Real-Time Diagnoscs<br>|Col3|
|---|---|---|
|System µP|System µP|System µP|



**Simplified Diagram**



An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Pin Configuration and Functions** ...................................3
**5 Specifications** .................................................................. 5

5.1 Absolute Maximum Ratings........................................ 5
5.2 ESD Ratings............................................................... 5
5.3 Recommended Operating Conditions.........................6
5.4 Thermal Information....................................................6

5.5 Electrical Characteristics.............................................7
5.6 Typical Characteristics (2MHz)................................. 10
5.7 Typical Characteristics (384kHz).............................. 15
**6 Parameter Measurement Information** .......................... 19

**7 Detailed Description** ......................................................20

7.1 Overview................................................................... 20

7.2 Functional Block Diagram......................................... 20
7.3 Feature Description...................................................21
**8 Device Functional Modes** ............................................. 56

8.1 Internal Reporting Signals.........................................56
8.2 Device States and Flags........................................... 57
8.3 Fault Events.............................................................. 60

**9 Programming** ................................................................. 63

9.1 I [2] C Serial Communication Bus................................. 63
9.2 I [2] C Address Selection...............................................63
9.3 I [2] C Bus Protocol....................................................... 63



9.4 Random Write........................................................... 64

9.5 Random Read...........................................................64
9.6 Sequential Read....................................................... 65
9.7 DSP Memory Book and Page................................... 65
**10 Register Maps** .............................................................. 67

10.1 page0 Registers......................................................68
**11 Application and Implementation** .............................. 165

11.1 Application Information..........................................165
11.2 Typical Application................................................ 166
11.3 Power Supply Recommendations......................... 167
11.4 Layout................................................................... 167
**12 Device and Documentation Support** ........................169

12.1 Device Support..................................................... 169
12.2 Documentation Support........................................ 169
12.3 Receiving Notification of Documentation Updates169
12.4 Support Resources............................................... 169
12.5 Trademarks........................................................... 169
12.6 Electrostatic Discharge Caution............................169
12.7 Glossary................................................................169
**13 Revision History** ........................................................ 169
**14 Mechanical, Packaging, and Orderable**

**Information** .................................................................. 170
14.1 Package Option Addendum.................................. 171
14.2 Tape and Reel Information....................................172



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



|ion|and Functions|Col3|
|---|---|---|
||1<br>28<br>2<br>27<br>3<br>26<br>4<br>25<br>5<br>24<br>6<br>23<br>7<br>22<br>8<br>21<br>9<br>20<br>10<br>19<br>11<br>18<br>12<br>17<br>13<br>16<br>14<br>15<br>Thermal<br>Pad||
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


Not to scale


**Figure 4-1. PWP (HTSSOP) Package, 28-Pin with exposed Thermal Pad Down, Top View**


**Table 4-1. Pin Functions- PWP Package**

|PIN|Col2|TYPE1|DESCRIPTION|
|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|
|AVDD_BYP|14|PWR|5V Analog supply voltage regulator bypass|
|BST_M|23|PWR|Bootstrap capacitor connection pins for high-side gate driver|
|BST_P|25|PWR|Bootstrap capacitor connection pins for high-side gate driver|
|DVDD|7|PWR|DVDD supply input|
|DVDD_BYP|5|PWR|1.5V Digital core supply bypass, derived internally from DVDD input|
|~~FAULT~~/<br>GPIO_2|10|DI/O|Configurable general purpose IO, function set by register programming. Set as~~FAULT~~by<br>default. Reports a fault (active low, open drain)|
|FSYNC|2|DI|Audio frame clock input|
|GND|6, 13, 16, 19, 24|GND|Ground|
|GPIO_1|4|DI/O|General purpose IO, function set by register programming|
|GVDD_BYP|15|PWR|5V Gate drive voltage regulator bypass|
|I2C_ADDR|12|DI|I2C address pin|
|NC|17, 18, 20, 21|NC|No internal connection|
|OUT_M|22|NO|Negative output for the channel|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 3


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**Table 4-1. Pin Functions- PWP Package (continued)**

|PIN|Col2|TYPE1|DESCRIPTION|
|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|
|OUT_P|26|PO|Positive output for the channel|
|~~PD~~|11|DI|Shuts down the device for minimal power draw (active low), 110kΩ internal pull-down<br>resistor|
|PVDD|27, 28|PWR|PVDD voltage input (can be connected to battery)|
|SCL|8|DI|I2C clock input|
|SCLK|1|DI|Audio input serial clock|
|SDA|9|DI/O|I2C data input and output|
|SDIN|3|DI|TDM or I2S data input|
|Thermal Pad|-|GND|Provides electrical and thermal connection for the device. Must be connected to GND.|



1. DI = digital input, DO = digital output, DI/O = digital input/output, GND = ground, NC = no connect, NO =
negative output, PO = positive output, PWR = power


4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**5 Specifications**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**5.1 Absolute Maximum Ratings**
over operating free-air temperature range (unless otherwise noted) [(1)]


















|Col1|Col2|Col3|MIN MAX|UNIT|
|---|---|---|---|---|
|PVDD|DC supply-voltage range relative to GND||-0.3<br>30|V|
|VMAX|Transient supply voltage: PVDD|t ≤ 400 ms exposure|-1<br>40|V|
|VRAMP|Supply-voltage ramp rate PVDD||40|V/ms|
|DVDD|DC supply voltage range relative to GND||-0.3<br>3.9|V|
|IMAX|Maximum current per pin - PVDD, GND||±5|A|
|IMAX|Maximum current per pin - OUT_P, OUT_M||±7|A|
|IMAX_PULSED|Pulsed supply current per pin - PVDD, GND|t < 1 ms|±12|A|
|IMAX_PULSED|Pulsed supply current per pin - OUT_P, OUT_M|Pulsed supply current per pin - OUT_P, OUT_M|±16.5|A|
|VLOGIC|Input voltage for logic pins - SCL, SDA,~~FAULT, PD~~, GPIOx||–0.3<br>DVDD + 0.5|V|
|VGND|Maximum voltage between GND pins||±0.3|±0.3|
|TJ|Maximum operating junction temperature range||–55<br>175|°C|
|Tstg|Storage temperature range||–55<br>150|–55<br>150|



(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.


**5.2 ESD Ratings**






|Col1|Col2|Col3|Col4|VALUE|UNIT|
|---|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human-body model (HBM), per AEC Q100-002(1)|Human-body model (HBM), per AEC Q100-002(1)|±4000|V|
|V(ESD)|Electrostatic discharge|Charged-device model (CDM), per AEC<br>Q100-011|All pins|±1500|±1500|



(1) AEC Q100-002 indicates that HBM stressing shall be in accordancewith the ANSI/ESDA/JEDEC JS-001 specification.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 5


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**5.3 Recommended Operating Conditions**



|Col1|Col2|Col3|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|PVDD|Output FET Supply Voltage Range|Relative to GND|4.5<br>14.4<br>19|V|
|DVDD|DC Logic supply|Relative to GND|1.62<br>3.6|V|
|TA|Ambient temperature||–40<br>125|°C|
|TJ|Junction temperature|An adequate thermal design is<br>required|–40<br>175|–40<br>175|
|RL|Nominal speaker load impedance|BTL Mode|PVDD/<br>(ILIM)<br>4|Ω|
|RPU_I2C|I2C pullup resistance on SDA and SCL pins||1<br>4.7<br>10|kΩ|
|CBypass|External capacitance on bypass pins|DVDD_BYP|1|µF|
|CA_GVDD|Combined external capacitance on bypass pins|GVDD_BYP, AVDD_BYP|1.1|µF|
|LO|Output filter inductance|Minimum output filter inductance<br>at ISD current levels. Applies to<br>short to ground or short to power<br>protection.|1|µH|


**5.4 Thermal Information**









|THERMAL METRIC(1)|Col2|TAS6511-Q1(2)|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**PWP(HTSSOP)**|**PWP(HTSSOP)**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**28 PINS**|**28 PINS**|
|RθJA|Junction-to-ambient thermal resistance|29.7|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|25.5|°C/W|
|RθJB|Junction-to-board thermal resistance|9.1|°C/W|
|ΨJT|Junction-to-top characterization parameter|0.6|°C/W|
|ΨJB|Junction-to-board characterization parameter|9.1|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|2.4|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](https://www.ti.com/lit/an/spra953c/spra953c.pdf?ts=1697653642570)
report, SPRA953.
(2) JEDEC standard 4 layer PCB.


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**5.5 Electrical Characteristics**

Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4 V, DVDD = 1.8 V, R L = 4 Ω, P out = 1 W/ch, ƒ out = 1
kHz, F sw = 2.048MHz, BD Modulation, AES17 Filter, reconstruction filter inductor used: 3.3µH-VCTA32252T-3R3MS6 in 4Ω,
VCMV053T-3R3MN22M in 2Ω configuration and 1µF, default I [2] C settings,see application diagram



















































|PARAMETER TEST CONDITIONS MIN TYP MAX UNIT|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**OPERATING CURRENT**|**OPERATING CURRENT**|**OPERATING CURRENT**|**OPERATING CURRENT**|**OPERATING CURRENT**|
|IDVDD|DVDD supply current|Playing, -60 dB Signal|8<br>12|mA|
|IPVDD_IDLE|PVDD idle current|Playing, no audio input, FSW = 2.048 MHz|35<br>45|35<br>45|
|IPVDD_IDLE|PVDD idle current|Playing, no audio input, FSW = 384 kHz|26|26|
|IPVDD_Shutdown|PVDD shutdown current|~~PD a~~ctive, DVDD = 0 V|2<br>5|μA|
|IDVDD_Shutdown|DVDD shutdown current|~~PDa~~ctive, DVDD = 1.8 V|0.5<br>1|0.5<br>1|
|IDVDD_Shutdown|DVDD shutdown current|~~PD a~~ctive, DVDD = 3.3 V|1<br>2|1<br>2|
|**OUTPUT POWER**|**OUTPUT POWER**|**OUTPUT POWER**|**OUTPUT POWER**|**OUTPUT POWER**|
|PO|Output power|4Ω, PVDD=14.4V, THD+N=1%,TC=75℃|21<br>23|W|
|PO|Output power|4Ω, PVDD=14.4V, THD+N=1%|24|W|
|PO|Output power|4Ω, PVDD=14.4V, THD+N=10%,TC=75℃|26<br>28|W|
|PO|Output power|4Ω, PVDD=14.4V, THD+N=10%|30|W|
|PO|Output power|2Ω, PVDD=14.4V, THD+N=1%,TC=75℃|38<br>40|W|
|PO|Output power|2Ω, PVDD=14.4V, THD+N=10%,TC=75℃|42<br>50|W|
|EFFP|Power efficiency|25 W output power RL = 4 Ω, PVDD = 14.4 V, TC =<br>25°C; (includes output filter losses)|90|%|
|**PWM OUTPUT STAGE**|**PWM OUTPUT STAGE**|**PWM OUTPUT STAGE**|**PWM OUTPUT STAGE**|**PWM OUTPUT STAGE**|
|RDS(on)|FET drain-to-source resistance|25°C, Not including bond wire and package resistance|35|mΩ|
|**AUDIO PERFORMANCE**|**AUDIO PERFORMANCE**|**AUDIO PERFORMANCE**|**AUDIO PERFORMANCE**|**AUDIO PERFORMANCE**|
|Vn|Output noise voltage|Zero input, A-weighting, Gain = 21V/FS|46|μV|
|Vn|Output noise voltage|Zero input, A-weighting, Gain = 15V/FS|41|41|
|Vn|Output noise voltage|Zero input, A-weighting, Gain = 7.5V/FS|35|35|
|Vn|Output noise voltage|Zero input, A-weighting, Gain = 3.75V/FS|33|33|
|G|Gain|Peak output voltage at full scale digital input|21|V/FS|
|THD+N|Total harmonic distortion +<br>noise|RL = 4 Ω 1W Output Power|0.02|%|
|THD+N|Total harmonic distortion +<br>noise|RL = 4 Ω 1W Output Power 20Hz to 20kHz|0.06|%|
|GVAR|Device gain variation||0.5|dB|
|FBW|Frequency response|20Hz to 20kHz, without LC filter impact or integrated<br>compensation|0.5|dB|
|FBW|Frequency response|20Hz to 40kHz, without LC filter impact or integrated<br>compensation|2|2|
|PSRR|Power-supply rejection ratio|PVDD = 14.4 Vdc + 1 VRMS, ƒ = 1 kHz|80|dB|
|GMUTE|Output attenuation|Assert~~MUTE~~and compare to amp playing 1W audio<br>into 4 Ω|120|dB|
|**LINE OUTPUT PERFROMANCE**|**LINE OUTPUT PERFROMANCE**|**LINE OUTPUT PERFROMANCE**|**LINE OUTPUT PERFROMANCE**|**LINE OUTPUT PERFROMANCE**|
|Vn_Lineout|Line Out Output noise voltage|Zero input, A-weighting, Gain set to reach full<br>amplitude|46|μV|
|THD+N_LINEOUT|Line output total harmonic<br>distortion + noise|VO = 2 VRMS, channel set to Line output mode|0.018|%|
|**DIGITAL INPUT PINS**|**DIGITAL INPUT PINS**|**DIGITAL INPUT PINS**|**DIGITAL INPUT PINS**|**DIGITAL INPUT PINS**|
|VIH|Input logic level high||70|%DVDD|
|VIL|Input logic level low|Input logic level low|30|30|
|IIH|Input logic current|VI = DVDD|15|µA|
|IIL|IIL|VI = 0|-15|-15|
|**DIGITAL OUTPUT PINS**|**DIGITAL OUTPUT PINS**|**DIGITAL OUTPUT PINS**|**DIGITAL OUTPUT PINS**|**DIGITAL OUTPUT PINS**|
|VOH|Output voltage for logic level<br>high|I = ±1 mA|90|%DVDD|
|VOL|Output voltage for logic level<br>low|Output voltage for logic level<br>low|10|10|
|VOH|Output voltage for logic level<br>high|DVDD = 3.3 V, I = ±2 mA|90|%DVDD|
|VOL|Output voltage for logic level<br>low|Output voltage for logic level<br>low|10|10|
|**BYPASS VOLTAGES**|**BYPASS VOLTAGES**|**BYPASS VOLTAGES**|**BYPASS VOLTAGES**|**BYPASS VOLTAGES**|
|VDVDD_BYP|Digital bypass pins voltage||1.5|V|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 7


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4 V, DVDD = 1.8 V, R L = 4 Ω, P out = 1 W/ch, ƒ out = 1
kHz, F sw = 2.048MHz, BD Modulation, AES17 Filter, reconstruction filter inductor used: 3.3µH-VCTA32252T-3R3MS6 in 4Ω,
VCMV053T-3R3MN22M in 2Ω configuration and 1µF, default I [2] C settings,see application diagram

































|PARAMETER TEST CONDITIONS MIN TYP MAX UNIT|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**OVERVOLTAGE (OV) PROTECTION**|**OVERVOLTAGE (OV) PROTECTION**|**OVERVOLTAGE (OV) PROTECTION**|**OVERVOLTAGE (OV) PROTECTION**|**OVERVOLTAGE (OV) PROTECTION**|
|PVDDOV_SET|PVDD overvoltage shutdown<br>set||20.3<br>22.8|V|
|PVDDOV_HYS|PVDD overvoltage recovery<br>hysteresis||0.9|V|
|**UNDERVOLTAGE (UV) PROTECTION**|**UNDERVOLTAGE (UV) PROTECTION**|**UNDERVOLTAGE (UV) PROTECTION**|**UNDERVOLTAGE (UV) PROTECTION**|**UNDERVOLTAGE (UV) PROTECTION**|
|PVDDUV_SET|PVDD undervoltage shutdown<br>set||3.5<br>4.4|V|
|PVDDUV_HYS|PVDD undervoltage recovery<br>hysteresis||0.3|V|
|DVDDUV_SET|DVDD undervoltage shutdown<br>set||1.4<br>1.59|V|
|DVDDUV_HYS|DVDD undervoltage recovery<br>hysteresis||0.1|V|
|**POWER-ON RESET (POR)**|**POWER-ON RESET (POR)**|**POWER-ON RESET (POR)**|**POWER-ON RESET (POR)**|**POWER-ON RESET (POR)**|
|VPOR_SET|DVDD power on reset set|Increasing DVDD|0.9<br>1.51|V|
|VPOR_HYS|DVDD power on reset recovery<br>hysteresis||0.25|V|
|VPOR_OFF|DVDD power off threshold|Decreasing DVDD|0.8<br>1.3|V|
|**OVERTEMPERATURE (OT) PROTECTION and Temperature Sensing**|**OVERTEMPERATURE (OT) PROTECTION and Temperature Sensing**|**OVERTEMPERATURE (OT) PROTECTION and Temperature Sensing**|**OVERTEMPERATURE (OT) PROTECTION and Temperature Sensing**|**OVERTEMPERATURE (OT) PROTECTION and Temperature Sensing**|
|OTSD|Over-temperature shutdown||170|°C|
|OTHYS|Over-temperature recovery<br>hysteresis||13|°C|
|**LOAD OVER CURRENT PROTECTION**|**LOAD OVER CURRENT PROTECTION**|**LOAD OVER CURRENT PROTECTION**|**LOAD OVER CURRENT PROTECTION**|**LOAD OVER CURRENT PROTECTION**|
|ILIM|Overcurrent cycle-by-cycle<br>limit|OC Level 1|3.0<br>3.6|A|
|ILIM|Overcurrent cycle-by-cycle<br>limit|OC Level 2|3.9<br>4.4|3.9<br>4.4|
|ILIM|Overcurrent cycle-by-cycle<br>limit|OC Level 3|5.5<br>6.3|5.5<br>6.3|
|ILIM|Overcurrent cycle-by-cycle<br>limit|OC Level 4|6.5<br>7.3|6.5<br>7.3|
|ISD|Overcurrent shutdown|OC Level 1, Any short to supply or ground|7.9<br>8.5|A|
|ISD|Overcurrent shutdown|OC Level 2, Any short to supply or ground|8.8<br>9.5|8.8<br>9.5|
|ISD|Overcurrent shutdown|OC Level 3, Any short to supply or ground|11.3<br>12.5|11.3<br>12.5|
|ISD|Overcurrent shutdown|OC Level 4, Any short to supply or ground|14<br>15|14<br>15|
|**CLICK AND POP**|**CLICK AND POP**|**CLICK AND POP**|**CLICK AND POP**|**CLICK AND POP**|
|VCP|Output click and pop voltage|ITU-R 2k filter, Hi-Z to PLAY, PLAY to Hi-Z|2.5|mV|
|**DC OFFSET**|**DC OFFSET**|**DC OFFSET**|**DC OFFSET**|**DC OFFSET**|
|VOFFSET|Output offset voltage|TC = 50°C|4<br>7|mV|
|**DC DETECT**|**DC DETECT**|**DC DETECT**|**DC DETECT**|**DC DETECT**|
|DCFAULT|Output DC fault protection||1<br>1.6<br>2|V|
|**LOAD DIAGNOSTICS**|**LOAD DIAGNOSTICS**|**LOAD DIAGNOSTICS**|**LOAD DIAGNOSTICS**|**LOAD DIAGNOSTICS**|
|S2P|Maximum resistance to detect<br>a short from OUT pin(s) to<br>PVDD||2000|Ω|
|S2G|Maximum resistance to detect<br>a short from OUT pin(s) to<br>ground||200|200|
|SL|Shorted load detection<br>tolerance||±0.5|±0.5|
|OL|Minimum impedance detected<br>as open load||58|58|
|TDC_DIAG|DC diagnostic time|no faults|155|ms|
|LO|Line output||20|kΩ|
|TLineout_DIAG|Line output diagnostic time||50|ms|
|ACIMP|AC impedance accuracy|ƒ = 18.75 kHz, RL = 4 Ω, Impedance at output pins|±0.75|Ω|
|TAC_DIAG|AC diagnostic time|ƒ = 18.75 kHz|54|ms|
|fAC|AC diagnostic test frequency|Default|18.75|kHz|


8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4 V, DVDD = 1.8 V, R L = 4 Ω, P out = 1 W/ch, ƒ out = 1
kHz, F sw = 2.048MHz, BD Modulation, AES17 Filter, reconstruction filter inductor used: 3.3µH-VCTA32252T-3R3MS6 in 4Ω,
VCMV053T-3R3MN22M in 2Ω configuration and 1µF, default I [2] C settings,see application diagram


































|PARAMETER TEST CONDITIONS MIN TYP MAX UNIT|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|ISNS_Acc|Current Sense Accuracy|fout = 20Hz to 20kHz|±10|%|
|ISNS_Acc|Current Sense Accuracy||±7|±7|
|ISNS_Acc|Current Sense Accuracy|Across Temp, -40C to 125C Ambient|±10|±10|
|ISNS_Acc|Current Sense Accuracy|fout = 20Hz to 20kHz<br>Across Temp, -40°C to 125°C Ambient|±10|±10|
|ISNS_Error|Current-sense gain error over<br>temperature|-40°C to 125°C, 4 Ω, using a 6Hz, -36dB pilot tone|±10|±10|
|THD+N|Total harmonic distortion +<br>noise||2|2|
|SNR|Signal-To-Noise Ratio|Un-Weighted, Relative to 0 dBFS|60|dB|
|DNR|Dynamic Range|Un-Weighted, Relative to 0 dBFS|63|63|
|ISNS_Lat|Current Sense Latency|Sample time from signal output till the measured<br>current is reported back on TDM|104|us|
|ZLoad_Drift|VPredict over Current Sense|Max output swing vs Max out minus 60dB|10|%|
|**I2C ADDRESS PIN**|**I2C ADDRESS PIN**|**I2C ADDRESS PIN**|**I2C ADDRESS PIN**|**I2C ADDRESS PIN**|
|tI2C_ADDR|Time delay needed for I2C <br>address set-up||300|μs|
|**I2C CONTROL PORT**|**I2C CONTROL PORT**|**I2C CONTROL PORT**|**I2C CONTROL PORT**|**I2C CONTROL PORT**|
|tBUS|Bus free time between start<br>and stop conditions||1.3|μs|
|th1|Hold Time, SCL to SDA||0|ns|
|th2|Hold Time, start condition to<br>SCL||0.6|μs|
|tSTART|I2C Startup Time After DVDD<br>Power On Reset||12|ms|
|tRISE|Rise Time, SCL and SDA||300|ns|
|tFALL|Fall Time, SCL and SDA||300|ns|
|tSU1|Setup, SDA to SCL||100|ns|
|tSU2|Setup, SCL to Start Condition||0.6|μs|
|tSU3|Setup, SCL to Stop Condition||0.6|μs|
|tW(H)|Required Pulse Duration SCL<br>"High"||0.6|μs|
|tW(L)|Required Pulse Duration SCL<br>"Low"||1.3|μs|
|**SERIAL AUDIO PORT**|**SERIAL AUDIO PORT**|**SERIAL AUDIO PORT**|**SERIAL AUDIO PORT**|**SERIAL AUDIO PORT**|
|DSCLK|Allowable input clock duty<br>cycle||45%<br>50%<br>55%||
|fS|Supported input sample rates||16<br>192|kHz|
|fSCLK|Supported SCLK frequencies||32<br>512|xFS|
|fSCLK_Max|Maximum frequency||24.576|MHz|
|tSCY|SCLK pulse cycle time||40|ns|
|tSCL|SCLK pulse-width LOW||18|ns|
|tSCH|SCLK pulse-width HIGH||18|ns|
|tSF|SCLK rising edge to FSYNC<br>edge||8|ns|
|tFS|FSYNC edge to SCLK rising<br>edge||8|ns|
|tDS|DATA set-up time||8|ns|
|ci|Input capacitance, pins SCLK,<br>FSYNC, SDIN_1, SDOUT_1,<br>GPIO_x||10|pF|
|tDH|DATA hold time||8|ns|
|TAudioLA|Audio path latency from input<br>to output|FSYNC = 44.1 kHz or 48 kHz|438|μs|
|TAudioLA|Audio path latency from input<br>to output|FSYNC = 96 kHz|219|219|
|TAudioLA|Audio path latency from input<br>to output|FSYNC = 192 kHz|110|110|
|TLLPLA|Low latency path latency from<br>input to output|FSYNC = 44.1 kHz or 48 kHz|104|104|
|TLLPLA|Low latency path latency from<br>input to output|FSYNC = 96 kHz|73|73|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 9


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (2MHz)**


Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 2.048MHz, 300kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|Col2|2||Loa|ad|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||~~2~~<br>~~4~~|~~~~|~~Lo~~<br>~~Loa~~|~~d~~<br>~~d~~|||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|2|Lo|oad|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~2~~<br>~~4~~|~~Lo~~<br> ~~Lo~~|~~ad~~<br>~~ad~~||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||














|Col1|Col2|2||Loa|ad|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||~~2~~<br>~~4~~|~~~~|~~Lo~~<br>~~Loa~~|~~d~~<br>~~d~~|||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|2<br>4|Lo<br>Lo|ad<br>ad|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||














|Col1|2<br>4|<br>|Lo<br>Lo|ad<br>ad|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||


|Col1|2<br>4|Lo<br>Lo|ad<br>ad|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||


|10<br>5 2 Load<br>4 Load<br>2<br>1<br>0.5<br>(%)<br>0.2<br>0.1 THD+N<br>0.05<br>0.02<br>0.01<br>0.005<br>0.002<br>0.001<br>20 100 1k 10k 20k<br>Frequency (Hz)<br>BD<br>Figure 5-1. THD+N vs Frequency|10<br>5 2 Load<br>4 Load<br>2<br>1<br>0.5<br>(%)<br>0.2<br>0.1 THD+N<br>0.05<br>0.02<br>0.01<br>0.005<br>0.002<br>0.001<br>20 100 1k 10k 20k<br>Frequency (Hz)<br>1SPW<br>Figure 5-2. THD+N vs Frequency|
|---|---|
|Frequency (Hz)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>20<br>100<br>1k<br>10k<br>20k<br>~~2 Load~~<br>~~4 Load~~<br>Hybrid<br>**Figure 5-3. THD+N vs Frequency**|Output Power (W)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>10m<br>100m<br>1<br>10<br>70<br>~~2 Load~~<br>~~4 Load~~<br> BD<br>**Figure 5-4. THD+N vs Output Power**|
|Output Power (W)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>10m<br>100m<br>1<br>10<br>70<br>~~2 Load~~<br>~~4 Load~~<br> 1SPW<br>**Figure 5-5. THD+N vs Output Power**|Output Power (W)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>10m<br>100m<br>1<br>10<br>70<br>~~2 Load~~<br>~~4 Load~~<br>Hybrid<br>**Figure 5-6. THD+N vs Output Power**|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


_TI Information - Selective Disclosure_



**[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (2MHz) (continued)**



**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 2.048MHz, 300kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|1|% TH|D+N|2 <br>|load|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~1~~<br>10<br>|~~ T~~<br>% T<br>|~~D+N~~<br>HD+<br>|~~4~~<br>N 2<br>|~~loa~~<br>loa<br>|d<br>|||||||||
||~~1~~|~~% T~~|~~D+~~|~~ 4~~|~~lo~~|~~d~~|~~d~~||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||


|Col1|1|% TH|D+N|2 <br>|load|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~1~~<br>10<br>|~~ TH~~<br>% T<br>|~~D+N~~<br>HD+<br>|~~4~~<br>N 2<br>|~~loa~~<br>loa<br>~~~~|d<br>|||||||||
||~~1~~|~~% T~~|~~D+~~|~~ 4~~|~~lo~~|~~d~~|~~d~~||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Ga<br>Ga|in 3.<br>in 7.|75 V/<br>5 V/F|FS<br>S|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||Ga<br>~~Ga~~|in 15<br>~~in 2~~|V/F<br>~~ V/F~~|S<br>|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Ga<br>Ga|in 3.<br>in 7.|75 V/<br>5 V/F|FS<br>S|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||Ga<br>~~Ga~~|in 15<br>~~n 2~~|V/F<br>~~ V/F~~|S<br>|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Ga<br>Ga|in 3.<br>in 7.|75 V/<br>5 V/F|FS<br>S|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||Ga<br>~~Ga~~|in 15<br>~~in 2~~|V/F<br>~~ V/F~~|S<br>|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Ga<br>Ga|in 3.<br>in 7.|75 V/<br>5 V/F|FS<br>S|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||Ga<br>~~Ga~~|in 15<br>~~n 2~~|V/F<br>~~ V/F~~|S<br>|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|80<br>1% THD+N 2 load<br>70 1% THD+N 4 load<br>10% THD+N 2 load<br>60 10% THD+N 4 load<br>(W)<br>50<br>power<br>40<br>Output<br>30<br>20<br>10<br>0<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Supply Voltage (V)<br>BD<br>Figure 5-7. Output Power vs Supply Voltage|90<br>1% THD+N 2 load<br>80 1% THD+N 4 load<br>10% THD+N 2 load<br>70 10% THD+N 4 load<br>60 (W)<br>50 power<br>40 Output<br>30<br>20<br>10<br>0<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Supply Voltage (V)<br>1SPW<br>Figure 5-8. Output Power vs Supply Voltage|
|---|---|
|Supply Voltage (V)<br>Idle channel noise (Vrms)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Gain 3.75 V/FS<br>~~Gain 7.5 V/FS~~<br>Gain 15 V/FS<br>~~Gain 21 V/FS~~<br>A-weighted<br>BD<br>**Figure 5-9. Noise vs Supply Voltage**|Supply Voltage (V)<br>Idle channel noise (Vrms)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Gain 3.75 V/FS<br>~~Gain 7.5 V/FS~~<br>Gain 15 V/FS<br>~~Gain 21 V/FS~~<br>A-weighted<br>BD<br>Spread Spectrum<br>Enabled<br>**Figure 5-10. Noise vs Supply Voltage**|
|Supply Voltage (V)<br>Idle channel noise (Vrms)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Gain 3.75 V/FS<br>~~Gain 7.5 V/FS~~<br>Gain 15 V/FS<br>~~Gain 21 V/FS~~<br>A-weighted<br>1SPW<br>**Figure 5-11. Noise vs Supply Voltage**|Supply Voltage (V)<br>Idle channel noise (Vrms)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Gain 3.75 V/FS<br>~~Gain 7.5 V/FS~~<br>Gain 15 V/FS<br>~~Gain 21 V/FS~~<br>A-weighted<br>Hybrid<br>**Figure 5-12. Noise vs Supply Voltage**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 11


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (2MHz) (continued)**


Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 2.048MHz, 300kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram










|Col1|4<br>2|L<br>L|oad<br>oad|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


|Col1|4<br>2|Col3|<br>|L<br>L|oad<br>oad|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
















|Col1|BD|M|od|e|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||1S|PW||Mode|||||
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


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||PVDD + D|VDD (Dev|ice onl|
|||||PVDD + D|VDD (Dev|ice + L|
















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||PV|DD +|DVDD (Devic|
|||||PV|DD +|DVDD (Devic|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||PVDD + D|VDD (De|ice onl|
|||||PVDD + D|VDD (Dev|ice + L|


|3<br>4 Load<br>2 2 Load<br>1<br>0 (dB)<br>Gain<br>-1<br>-2<br>-3<br>-4<br>20 100 1k 10k 20k 40k<br>Frequency (Hz)<br>BD<br>Figure 5-13. Frequency Response|3<br>4 Load<br>2 2 Load<br>1<br>0 (dB)<br>Gain<br>-1<br>-2<br>-3<br>-4<br>20 100 1k 10k 20k 40k<br>Frequency (Hz)<br>1SPW<br>Figure 5-14. Frequency Response|
|---|---|
|Frequency (Hz)<br>Gain (dB)<br>-110<br>-105<br>-100<br>-95<br>-90<br>-85<br>-80<br>-75<br>-70<br>-65<br>-60<br>-55<br>-50<br>20<br>100<br>1k<br>10k<br>20k<br>Po = Idle<br>PVDD = 14.4 +1 Vrms<br>BD Mode<br>1SPW Mode<br> <br>**Figure 5-15. PVDD PSRR vs Frequency**|Output Power (W)<br>Efficiency (%)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>BD<br>**Figure 5-16. Efficiency vs Output Power - 4Ω**|
|Output Power (W)<br>Efficiency (%)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>BD<br>**Figure 5-17. Efficiency vs Output Power - 2Ω**|Output Power (W)<br>Efficiency (%)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>1SPW<br>**Figure 5-18. Efficiency vs Output Power - 4Ω**|



12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


_TI Information - Selective Disclosure_



**[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (2MHz) (continued)**



**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 2.048MHz, 300kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||PV|DD +|DVD|(De|ice o|nly)|
|||||||PV|DD +|DVD|D (De|vice +|LC)|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||PVDD|DVDD|(Devic|only)|
||||||PVDD +|DVDD|(Device|+ LC)|














|Col1|PVD|D (D|evic|e on|ly)|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~VD~~|~~ (D~~|~~vic~~|~~ +~~|~~C)~~|||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|PVD|D (De|vice|only)|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|~~PVD~~|~~ (D~~|~~vice~~|~~ LC)~~|||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||














|Col1|PVD|D (D|evic|e on|ly)|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~VD~~|~~ (D~~|~~vic~~|~~ +~~|~~C)~~|||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|PVD|D (De|vice|only)|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|~~PVD~~|~~ (D~~|~~vice~~|~~ LC)~~|||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||


|100<br>90<br>80<br>70<br>(%)<br>60<br>Efficiency<br>50<br>40<br>30<br>20<br>10 PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>0<br>0 5 10 15 20 25 30 35 40 45 50 55<br>Output Power (W)<br>1SPW<br>Figure 5-19. Efficiency vs Output Power - 2Ω|100<br>90<br>80<br>70<br>(%)<br>60<br>Efficiency<br>50<br>40<br>30<br>20<br>10 PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>0<br>0 2 4 6 8 10 12 14 16<br>Output Power (W)<br>PVDD = 10V 1SPW<br>Figure 5-20. Efficiency vs Output Power - 4Ω, PVDD = 10V|
|---|---|
|Output Power (W)<br>Power dissipation (W)<br>0<br>2<br>4<br>6<br>8<br>10 12 14 16 18 20 22 24 26 28 30<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>PVDD (Device only)<br>~~PVDD (Device + LC)~~<br>BD<br>**Figure 5-21. Power Dissipation vs Output Power - 4Ω**|Output Power (W)<br>Power dissipation (W)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>PVDD (Device only)<br>~~PVDD (Device + LC)~~<br> BD<br>**Figure 5-22. Power Dissipation vs Output Power - 2Ω**|
|Output Power (W)<br>Power dissipation (W)<br>0<br>2<br>4<br>6<br>8<br>10 12 14 16 18 20 22 24 26 28 30<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>PVDD (Device only)<br>~~PVDD (Device + LC)~~<br> 1SPW<br>**Figure 5-23. Power Dissipation vs Output Power - 4Ω**|Output Power (W)<br>Power dissipation (W)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>PVDD (Device only)<br>~~PVDD (Device + LC)~~<br> 1SPW<br>**Figure 5-24. Power Dissipation vs Output Power - 2Ω**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 13


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**5.6 Typical Characteristics (2MHz) (continued)**


Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 2.048MHz, 300kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram








|Col1|1|SPW|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||~~D~~<br>YBRI||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||










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
|||||||||||
||~~V=14.~~|~~4V 2Load~~||||||||
||DD<br>~~V=14.~~|~~4V 4Load~~||||||||
||~~DD~~|||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||
||||||||||||||||||
||||||d<br>d||||||||||||
||2<br>4|<br>|L<br>L|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|oa<br>oa|


|3<br>2.5<br>(A)<br>current<br>2<br>1.5 shutdown<br>1<br>PVDD<br>0.5<br>0<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Supply Voltage (V)<br>Figure 5-25. Shutdown Current vs Supply Voltage|60<br>1SPW<br>55 BD<br>50 HYBRID<br>(mA)<br>45<br>40 current<br>35<br>idle<br>30<br>PVDD<br>25<br>20<br>15<br>10<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Supply Voltage (V)<br>Figure 5-26. 46 PVDD Idle Current vs Supply Voltage|
|---|---|
|IoutRMS (A)<br>THD+N (%)<br>0.02<br>0.05<br>0.1<br>0.2 0.3<br>0.50.7 1<br>2<br>3 4 5 678 10<br>0.5<br>0.7<br>1<br>2<br>3<br>4<br>5<br>7<br>10<br>**20**<br>~~PV~~DD~~=14.4V 2Load~~<br>~~PVDD=14.4V 4Load~~<br>**Figure 5-27. Current Sense THD+N vs Current**|IoutRMS (A)<br>Accuracy (%)<br>0.03 0.05<br>0.1<br>0.2 0.3<br>0.5 0.7<br>1<br>2<br>3<br>4 5 6<br>-5<br>0<br>5<br>10<br>15<br>2Load<br>4Load<br>**Figure 5-28. Current Sense Accuracy vs Current**|



14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


_TI Information - Selective Disclosure_



**[www.ti.com](https://www.ti.com)**


**5.7 Typical Characteristics (384kHz)**



**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 384kHz, 900kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|Col2|2||Loa|ad|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||~~2~~<br>~~4~~|<br> ~~~~|~~Lo~~<br>~~Loa~~|~~d~~<br>~~d~~||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


|Col1|2 Lo|oad|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||~~2 L~~<br>~~4 L~~|~~ad~~<br>~~oad~~|||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||














|Col1|Col2|2||Loa|ad|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||~~2~~<br>~~4~~|<br> ~~~~|~~Lo~~<br>~~Loa~~|~~d~~<br>~~d~~||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


|Col1|2 Lo|oad|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||~~2 L~~<br>~~4 L~~|~~oad~~<br>~~oad~~||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||














|Col1|2<br>4|<br>|Lo<br>Lo|ad<br>ad|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


|Col1|2 Lo|oad|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||~~2 L~~<br>~~4 L~~|~~oad~~<br>~~oad~~||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||


|10<br>5 2 Load<br>4 Load<br>2<br>1<br>0.5<br>(%)<br>0.2<br>0.1 THD+N<br>0.05<br>0.02<br>0.01<br>0.005<br>0.002<br>0.001<br>20 100 1k 10k 20k<br>Frequency (Hz)<br>BD<br>Figure 5-29. THD+N vs Frequency|10<br>5 2 Load<br>4 Load<br>2<br>1<br>0.5<br>(%)<br>0.2<br>0.1 THD+N<br>0.05<br>0.02<br>0.01<br>0.005<br>0.002<br>0.001<br>20 100 1k 10k 20k<br>Frequency (Hz)<br>1SPW<br>Figure 5-30. THD+N vs Frequency|
|---|---|
|Frequency (Hz)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>20<br>100<br>1k<br>10k<br>20k<br>~~2 Load~~<br>~~4 Load~~<br>Hybrid<br>**Figure 5-31. THD+N vs Frequency**|Output Power (W)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>10m<br>100m<br>1<br>10<br>70<br>~~2 Load~~<br>~~4 Load~~<br>BD<br>**Figure 5-32. THD+N vs Output Power**|
|Output Power (W)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>10m<br>100m<br>1<br>10<br>70<br>~~2 Load~~<br>~~4 Load~~<br>1SPW<br>**Figure 5-33. THD+N vs Output Power**|Output Power (W)<br>THD+N (%)<br>0.001<br>0.002<br>0.005<br>0.01<br>0.02<br>0.05<br>0.1<br>0.2<br>0.5<br>1<br>2<br>5<br>10<br>10m<br>100m<br>1<br>10<br>70<br>~~2 Load~~<br>~~4 Load~~<br>Hybrid<br>**Figure 5-34. THD+N vs Output Power**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 15


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**5.7 Typical Characteristics (384kHz) (continued)**


Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 384kHz, 900kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|1|% T|HD+N|2 |loa|d|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~1~~<br>10<br>|~~ T~~<br>% T<br>|~~D+N~~<br>HD+<br>|~~ 4~~<br>N 2<br>|~~loa~~<br>lo<br>|~~d~~<br>ad<br>||||||||
||~~1~~|~~%~~|~~HD+~~|~~ 4~~|~~lo~~|~~ad~~||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|1|% T|HD+N|2 |loa|d|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~1~~<br>10<br>|~~ T~~<br>% T<br>|~~D+N~~<br>HD+<br>|~~ 4~~<br>N 2<br>|~~loa~~<br>lo<br>|~~d~~<br>ad<br>||||||||
||~~1~~|~~%~~|~~HD+~~|~~ 4~~|~~lo~~|~~ad~~||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Ga<br>Ga|in 3.<br>in 7.|75 V/<br>5 V/F|FS<br>S|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||Ga<br>~~Ga~~|in 15<br>~~n 21~~|V/F<br>~~ V/F~~|S<br>|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Ga<br>Ga|in 3.<br>in 7.|75 V/<br>5 V/F|FS<br>S|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||Ga<br>~~Ga~~|in 15<br>~~n 21~~|V/F<br>~~ V/F~~|S<br>|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||










|Col1|Col2|2|Col4|Lo|ad|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||
|||~~4~~||~~Lo~~|~~ad~~|||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||


|Col1|Col2|2|Col4|Lo|ad|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||
|||~~4~~||~~Lo~~|~~ad~~|||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||
|||||||||||||||||||||||






|90<br>1% THD+N 2 load<br>80 1% THD+N 4 load<br>10% THD+N 2 load<br>70 10% THD+N 4 load<br>60 (W)<br>50 power<br>40 Output<br>30<br>20<br>10<br>0<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Supply Voltage (V)<br>BD<br>Figure 5-35. Output Power vs Supply Voltage|90<br>1% THD+N 2 load<br>80 1% THD+N 4 load<br>10% THD+N 2 load<br>70 10% THD+N 4 load<br>60 (W)<br>50 power<br>40 Output<br>30<br>20<br>10<br>0<br>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Supply Voltage (V)<br>1SPW<br>Figure 5-36. Output Power vs Supply Voltage|
|---|---|
|Supply Voltage (V)<br>Idle channel noise (Vrms)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Gain 3.75 V/FS<br>~~Gain 7.5 V/FS~~<br>Gain 15 V/FS<br>~~Gain 21 V/FS~~<br>A-weighted<br>1SPW<br>**Figure 5-37. Noise vs Supply Voltage**|Supply Voltage (V)<br>Idle channel noise (Vrms)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>Gain 3.75 V/FS<br>~~Gain 7.5 V/FS~~<br>Gain 15 V/FS<br>~~Gain 21 V/FS~~<br>A-weighted<br>1SPW<br>**Figure 5-38. Noise vs Supply Voltage**|
|Frequency (Hz)<br>Gain (dB)<br>-8<br>-7<br>-6<br>-5<br>-4<br>-3<br>-2<br>-1<br>0<br>1<br>2<br>3<br>20<br>100<br>1k<br>10k<br>20k<br>40k<br>2 Load<br>~~4 Load~~<br>BD<br>**Figure 5-39. Frequency Response**|Frequency (Hz)<br>Gain (dB)<br>-8<br>-7<br>-6<br>-5<br>-4<br>-3<br>-2<br>-1<br>0<br>1<br>2<br>3<br>20<br>100<br>1k<br>10k<br>20k<br>40k<br>2 Load<br>~~4 Load~~<br>1SPW<br>**Figure 5-40. Frequency Response**|



16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


_TI Information - Selective Disclosure_



**[www.ti.com](https://www.ti.com)**


**5.7 Typical Characteristics (384kHz) (continued)**



**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 384kHz, 900kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||PVDD + D|VDD (Dev|ice only)|
|||||PVDD + D|VDD (Dev|ice + LC)|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||PV|DD +|DVD|D (De|vice|nly)|
|||||||PV|DD +|DVD|D (De|vice +|LC)|














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
||||||||
|||||PVDD + D|VDD (Dev|ice only)|
|||||PVDD + D|VDD (Dev|ice + LC)|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||PV|DD +|DVD|D (De|vice|nly)|
|||||||PV|DD +|DVD|D (De|vice +|LC)|








|P|VD|D (D|evice|on|ly)|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|~~P~~|~~VD~~|~~D (D~~|~~vic~~|~~ +~~|~~C)~~|||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||


|100<br>90<br>80<br>70<br>(%)<br>60<br>Efficiency<br>50<br>40<br>30<br>20<br>10 PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>0<br>0 5 10 15 20 25 30<br>Output Power (W)<br>BD<br>Figure 5-41. Efficiency vs Output Power - 4Ω|100<br>90<br>80<br>70<br>(%)<br>60<br>Efficiency<br>50<br>40<br>30<br>20<br>10 PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br>0<br>0 5 10 15 20 25 30 35 40 45 50 55<br>Output Power (W)<br>BD<br>Figure 5-42. Efficiency vs Output Power - 2Ω|
|---|---|
|Output Power (W)<br>Efficiency (%)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br> 1SPW<br>**Figure 5-43. Efficiency vs Output Power - 4Ω**|Output Power (W)<br>Efficiency (%)<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>0<br>10<br>20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br>100<br>PVDD + DVDD (Device only)<br>PVDD + DVDD (Device + LC)<br> 1SPW<br>**Figure 5-44. Efficiency vs Output Power - 2Ω**|
|Output Power (W)<br>Power dissipation (W)<br>0<br>2<br>4<br>6<br>8<br>10 12 14 16 18 20 22 24 26 28 30<br>0<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>PVDD (Device only)<br>~~PVDD (Device + LC)~~<br>BD<br>**Figure 5-45. Power Dissipation vs Output Power - 4Ω**|BD<br>**Figure 5-46. Power Dissipation vs Output Power - 2Ω**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 17


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**5.7 Typical Characteristics (384kHz) (continued)**


Test conditions (unless otherwise noted): T C = 25°C, PVDD = 14.4V, DVDD = 1.8V, R L = 4Ω, P out = 1W/ch, ƒ out = 1kHz, F sw
= 384kHz, 900kΩ Zero frequency, AES17 Filter, reconstruction filter as described in Parameter Measurement Information,
default I2C settings, see application diagram














|Col1|P|VDD|(D|evic|e onl|y)|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~P~~|~~D~~|~~ (D~~|~~vic~~|~~ +~~|~~C)~~|||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||


|Col1|PVD|D (De|vice o|nly)|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||~~PVD~~|~~ (D~~|~~vice~~|~~ LC)~~|||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||







|4<br>PVDD (Device only)<br>3.5 PVDD (Device + LC)<br>3<br>(W)<br>2.5 dissipation<br>2<br>1.5 Power<br>1<br>0.5<br>0<br>0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30<br>Output Power (W)<br>1SPW<br>Figure 5-47. Power Dissipation vs Output Power - 4Ω|10<br>PVDD (Device only)<br>9 PVDD (Device + LC)<br>8<br>7 (W)<br>dissipation<br>6<br>5<br>4<br>Power<br>3<br>2<br>1<br>0<br>0 5 10 15 20 25 30 35 40 45 50 55<br>Output Power (W)<br>1SPW<br>Figure 5-48. Power Dissipation vs Output Power - 2Ω|
|---|---|
|Supply Voltage (V)<br>PVDD idle current (mA)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>1SPW<br>~~BD~~<br>HYBRID<br>**Figure 5-49. PVDD Idle Current vs Supply Voltage**|Supply Voltage (V)<br>PVDD idle current (mA)<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>60<br>1SPW<br>~~BD~~<br>HYBRID<br>**Figure 5-49. PVDD Idle Current vs Supply Voltage**|


|Col1|1|SPW|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||~~B~~<br>H|~~D~~<br>YBR|D||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||


18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**6 Parameter Measurement Information**


The parameters for the TAS6511-Q1 device were measured using the circuit in Section 11.4.


For measurements with 2.048MHz switching frequency the below 3.3µH inductors were used.


 - 4Ω: Cyntec VCTA32252T-3R3MS6

 - 2Ω: Cyntec VCMV053T-3R3MN22M


For measurements with 384kHz switching frequency the below 10µH inductors were used.

 - 4Ω: Cyntec VAMV06077E-100MM2

 - 2Ω: Cyntec VAMV08089A-100MM2


When enabling Real-Time Load Diagnostics with the integrated pilot tone, an analog balanced input filter must
be used to avoid misleading measurement results. An elliptic high pass filter as provided by the APx500 series
with a cutoff frequency of 20 Hz and a low-pass filter such as AES17 (20 kHz) are recommended. If the test
equipment does not support this filter type, it is recommended to turn off the Real-Time Load Diagnostics for
accurate performance measurements.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 19


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**7 Detailed Description**


**7.1 Overview**


The TAS6511-Q1 device is a mono-channel digital input Class-D audio amplifier, specifically designed for use in
the automotive industry. The ultra-efficient Class-D technology allows for reduced power consumption, reduced
PCB area, and less heat in the electrical system. The device realizes a high-fidelity audio sound system design
with smaller size, lower weight, and advanced functionality.


The core design blocks are:

 - Serial audio port

 - PLL and Clock management

 - Audio DSP subsystem

 - Pulse width modulator (PWM) with output stage feedback

 - Gate drive

 - Power FETs

 - Current Sense

 - Diagnostics including Real-Time Load Diagnostics

 - Protection

 - Power supply

 - I [2] C serial communication bus

 - Sensing


**7.2 Functional Block Diagram**











**FAULT/GPIO_2**


**SCLK**


**FSYNC**

**SDIN1**


**SDOUT/GPIO_1**





**BST_P**


**OUT_P**


**OUT_M**


**BST_M**






|Full Bridge<br>Power Stage|Col2|Col3|Col4|
|---|---|---|---|
|**Full Bridge**<br>**Power Stage**||||
|**Full Bridge**<br>**Power Stage**||||
|**Full Bridge**<br>**Power Stage**||||
|**Full Bridge**<br>**Power Stage**||||



**I2C_ADDR**








|GND DVDD AVDD_BYP / GVDD_BYP PVDD DVDD_BYP|Col2|VDD DVDD|PV D_BYP|AVDD_BYP / VDD|GND / GVDD_BYP|
|---|---|---|---|---|---|
|**Protection**<br>**LK**<br>**N1**<br>**NC**<br><br>**DA**<br>**CL**<br>**PD**<br>**_2**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br><br><br><br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>**DR**<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**_1**<br><br>**Audio DSP**<br>**Subsystem**|**Protection**<br>**LK**<br>**N1**<br>**NC**<br><br>**DA**<br>**CL**<br>**PD**<br>**_2**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br><br><br><br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>**DR**<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**_1**<br><br>**Audio DSP**<br>**Subsystem**|||||
|**Protection**<br>**LK**<br>**N1**<br>**NC**<br><br>**DA**<br>**CL**<br>**PD**<br>**_2**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br><br><br><br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>**DR**<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**_1**<br><br>**Audio DSP**<br>**Subsystem**|**Protection**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**Audio DSP**<br>**Subsystem**|**Protection**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**Audio DSP**<br>**Subsystem**|**Protection**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**Audio DSP**<br>**Subsystem**|**Protection**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**Audio DSP**<br>**Subsystem**|**Protection**<br>PLL and Clock<br>Management<br>Analog Supply<br>Regulator<br>Closed Loop Class-D Amplifier<br>Current Sense<br>Digital Core<br>Serial Audio<br>Port<br>TDM-4/TDM-8/<br>TDM-16<br>I2S<br>16kHz, 32kHz,<br>48kHz, 96kHz,<br>192kHz<br>Audio Signal Path with<br>Volume Control<br>I2C Control<br>Overtemperature<br>Overvoltage and Undervoltage<br>Overcurrent – CBC and Shutdown<br>DC Offset<br>Clip Detect<br>**Diagnostics**<br>DC Short to GND (S2G)<br>DC Short to Power (S2P)<br>DC Open Load (OL)<br>DC Shorted Load (SL)<br>AC Diagnostics<br>Real-Time Diagnostics<br>(SL, OL, S2P, S2G)<br>**Digital to**<br>**PWM**<br>Analog<br>Gain<br>Gate<br>Driver<br>**Full Bridge**<br>**Power Stage**<br>Low Latency<br>Signal Path<br>Spread<br>Spectrum<br>Digital Core<br>Supply Regulator<br>**Sensing**<br>Temperature Sensor<br>PVDD Sensor<br>8-bit ADC<br>Signal Pre- and Post-<br>conditioning<br>Dynamic gain control<br>Thermal Foldback<br>PVDD Tracking<br>Speaker GuardTM Pro<br>Power Limiter<br>Hybrid Modulation<br>**Audio DSP**<br>**Subsystem**|
|**LK**<br>**N1**<br>**NC**<br>**DA**<br>**CL**<br>**D**<br>**_2**<br>**DR**<br>**_1**||||||
|**LK**<br>**N1**<br>**NC**<br>**DA**<br>**CL**<br>**D**<br>**_2**<br>**DR**<br>**_1**||||||
|**LK**<br>**N1**<br>**NC**<br>**DA**<br>**CL**<br>**D**<br>**_2**<br>**DR**<br>**_1**||||||
|**LK**<br>**N1**<br>**NC**<br>**DA**<br>**CL**<br>**D**<br>**_2**<br>**DR**<br>**_1**||||||
|**LK**<br>**N1**<br>**NC**<br>**DA**<br>**CL**<br>**D**<br>**_2**<br>**DR**<br>**_1**||||||



**Figure 7-1. Functional Block Diagram**


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3 Feature Description**


_**7.3.1 Power Supply**_



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



The device has two power supply inputs DVDD and PVDD, which are described as follows:


**DVDD** This is a 1.8 V or 3.3 V supply that is connected at the DVDD pin and provides power to the digital
circuitry.


**PVDD** This pin is a higher voltage supply that can be connected to the vehicle battery or the regulated voltage
rail within the _Recommended Operating Conditions_ . PVDD supplies the power to the output FETs and
higher voltage analog circuits.


Several on-chip regulators are included and generate the voltages necessary for the internal circuitry. The
external pins are provided only for bypass capacitors to filter the supply and should not be used to power other
circuits.


The device reports the supplied PVDD voltage in PVDD_SENSE Register (Address = 0x74).


The device can withstand fortuitous open ground and power conditions within the absolute maximum ratings
for the device. Fortuitous open ground usually occurs when a speaker wire is shorted to ground, allowing for a
second ground path through the body diode in the output FETs.


**7.3.1.1 Power-Supply Sequence**


**7.3.1.2 Power-Up Sequence**


At power-up, the PD pin is recommended to be kept low until both power supply rails (PVDD and DVDD) are
within the Recommended Operating Conditions.


When all power rails are applied and ready, releasing the PD pin will power up the internal digital and analog
circuitry. The following state transition might take up to 6 ms in which the device powers up the analog circuitry
and ensures a proper internal boot procedure.


If DVDD is applied before PVDD and while the PD pin has been released, then a PVDD Undervoltage Fault will
be reported. POWER_FAULT_LATCHED Register (Address = 0x86) bit 1 needs to be read to be cleared after
the power-up sequence is completed.


Any time a power fault happens after the analog circuitry is powered up (PVDD ready and PD released),
TAS6511-Q1 will leave PLAY or other states and go back to the Auto Recovery (AUTOREC) state, until the
power fault disappears.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 21


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**

### PVDD DVDD



|DD<br>DD<br>PD<br>6 ms<br>150 ms<br>ate SHUTDOWN LOAD DIAG SLEEP PLAY|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|DD<br>DD<br>ate<br>SHUTDOWN<br>LOAD DIAG SLEEP<br>PLAY<br>6 ms<br>150 ms<br>~~PD~~|DD<br>DD<br>ate<br>SHUTDOWN<br>LOAD DIAG SLEEP<br>PLAY<br>6 ms<br>150 ms<br>~~PD~~|6 ms<br>150 ms|6 ms<br>150 ms|6 ms<br>150 ms|6 ms<br>150 ms|
|DD<br>DD<br>ate<br>SHUTDOWN<br>LOAD DIAG SLEEP<br>PLAY<br>6 ms<br>150 ms<br>~~PD~~|SHUTDOWN|SHUTDOWN|LOAD DIAG|SLEEP|PLAY|

### I2C

### I2S/TDM











Applying DVDD before PVDD will leads to a reported “PVDD Undervoltage Fault” which needs to be cleared


**Figure 7-2. TAS6511-Q1 Power-Up Sequence**


_**7.3.1.2.1 Quick-Start Sequence**_


In some cases a quick startup time from shutdown to audio playback is needed. For the quickest startup the DC
Load Diagnostics can be aborted. This allows the device to go into PLAY state without having to wait for DC
Load Diagnostics to finish. The below procedure can be used for a quick-start sequence.


**Note**
Aborting or bypassing the DC Diagnostics can cause the device to turn on the power stage into a fault
condition such as a shorted load drawing significant amount of current before triggering overcurrent
protection or real-time load diagnostics fault, if enabled.


1. Bring PD HIGH.
2. Wait 1ms
3. Set the LDG ABORT bit in the DC_LDG_CTRL Register (Address = 0xB0)
4. Configure the device DSP and register settings
5. Set channel to PLAY state using STATE_CTRL Register (Address = 0x03)


22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**

### PVDD

### DVDD



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025






### I2S/TDM





|PD<br>1 ms<br>>5 ms >3 ms<br>Deep<br>tate SHUTDOWN SLEEP PL<br>Sleep<br>I2C Abort DC Congure Set to<br>diagnoscs Device PLAY<br><br>DM I2S/|Col2|>5 ms|>3 ms|AY|
|---|---|---|---|---|
|tate<br>I2S/<br>Con<br>gure<br>Device<br>Set to<br>PLAY<br>DM<br>I2C<br>SHUTDOWN<br>SLEEP<br>PL<br>1 ms<br>Abort DC<br>diagnos<br>cs<br>>3 ms<br>Deep<br>Sleep<br>>5 ms<br>PD|SHUTDOWN|Deep<br>Sleep|SLEEP<br>PL|SLEEP<br>PL|
|tate<br>I2S/<br>Con<br>gure<br>Device<br>Set to<br>PLAY<br>DM<br>I2C<br>SHUTDOWN<br>SLEEP<br>PL<br>1 ms<br>Abort DC<br>diagnos<br>cs<br>>3 ms<br>Deep<br>Sleep<br>>5 ms<br>PD|SHUTDOWN|Con<br>gure<br>Device<br>Set to<br>PLAY<br>Abort DC<br>diagnos<br>cs|||
|tate<br>I2S/<br>Con<br>gure<br>Device<br>Set to<br>PLAY<br>DM<br>I2C<br>SHUTDOWN<br>SLEEP<br>PL<br>1 ms<br>Abort DC<br>diagnos<br>cs<br>>3 ms<br>Deep<br>Sleep<br>>5 ms<br>PD|SHUTDOWN|Con<br>gure<br>Device<br>Set to<br>PLAY<br>Abort DC<br>diagnos<br>cs||TDM|


**Figure 7-3. TAS6511-Q1 Quick-Start Sequence**









**7.3.1.3 Power-Down Sequence**


To power-down the device, first set the PD pin low for at least 10 ms before removing PVDD, or DVDD. After
10 ms, the power supplies can be removed. Removing PVDD first is recommended before removing the DVDD
supply.


**7.3.1.4 Device Initialization and Power-On-Reset (POR)**


The device initializes when either the system first powers up, the PD pin is pulled high, or when the DVDD
voltage falls below the POR threshold and then comes back to normal condition.


During device initialization all I [2] C registers are set to default values.


The I [2] C device address is determined from the I2C_ADDR pin. See I [2] C Address Selection for details.


After initialization, bit 7 of the of the POWER_FAULT_LATCHED Register (Address = 0x86) indicates that the
device went through a POR cycle. Reading this I [2] C register resets the fault signal. By default, this signal is
not routed to a pin but the signal can be configured accordingly by the FAULT pin in REPORT_ROUTING_2
Register (Address = 0x90) or the WARN pin if a GPIO pin is configured to the WARN function in
REPORT_ROUTING_3 Register (Address = 0x91). The pin signal is latching and can be reset by writing '1'
to the CLEAR FAULT bit 3 in RESET Register (Address = 0x01).


_**7.3.2 Serial Audio Port**_


The Serial Audio Interface can receive data in left-justified, I [2] S, or DSP mode formats. In addition, time-division
multiplexing (TDM) can be implemented to enable multichannel operation with support up to TDM16.


The pin SDIN is available for the data transfer, while any of the GPIO pins can be assigned to SDOUT if
required. Refer to GPIO Pins for more details.


**7.3.2.1 Left-Justified Timing**


Left-Justified timing uses the FSYNC pin to define when the data is being transmitted for the left channel or the
right channel. The MSB of the left channel is valid on the rising edge of the serial clock (SCLK) following the
rising edge of the audio frame clock (FSYNC). Similarly, the MSB of the right channel is valid on the rising edge
of SCLK clock following the falling edge of FSYNC. A channel offset can be configured and is identical across all


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 23


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


channels. Whether the device plays the left channel or right channel data can be configured using the I2S_CTRL
Register (Address = 0x22) bits 6 and 7.


Configuring Left-Justified Timing:
1. Set the data format to LTJ mode in bit 2-3 of AUDIO_INTERFACE_CTRL Register (Address = 0x21)
2. Set the data length in bit 2-3 the SDIN_CTRL Register (Address = 0x23)
3. Configure the optional 10-bit offset in bit 6-7 of SDIN_OFFSET_MSB Register (Address = 0x27) and
SDIN_AUDIO_OFFSET Register (Address = 0x28)



FSYNC


SCLK



~~**Left Channel**~~ ~~**Right Channel**~~



SDIN N-1 N-2 3 2 1 0

|3|2|1|0|Col5|
|---|---|---|---|---|
|3|2|1|0||



Channel 1



|3|2|1|0|Col5|
|---|---|---|---|---|
|3|2|1|0||


Channel 2



|Col1|N-1|N-2|
|---|---|---|
||||


Channel 1


|Col1|N-1|N-2|
|---|---|---|
||||


|Col1|N-1|N-2|
|---|---|---|
||||



FSYNC


SCLK



**Figure 7-4. Timing Diagram for Left-Justified Timing**














|Col1|Left Channel<br>N-1 N-2 3 2 1 0<br>Channel 1|Right Channel|Col4|N-1 N-2<br>Channe|
|---|---|---|---|---|
||||N-1 N-2<br>3<br>2<br>1<br>0<br>Channel 2|N-1 N-2<br>3<br>2<br>1<br>0<br>Channel 2|
||||||



Offset = 1 Offset = 1 Offset = 1


**Figure 7-5. Timing Diagram for Left-Justified Timing with Offset 1 = 1**


**7.3.2.2 I** **[2]** **S Mode**


I [2] S mode uses the FSYNC pin to define when the data is being transmitted for the left channel and when the
data is being transmitted for the right channel. In I [2] S mode, the MSB of the left channel is valid on the second
rising edge of the serial clock (SCLK) after the falling edge of the audio frame clock (FSYNC). Similarly the MSB
of the right channel is valid on the second rising edge of SCLK after the rising edge of FSYNC. A channel offset
can be configured and is identical for across channels. Whether the device plays the left channel or right channel
data can be configured using the I2S_CTRL Register (Address = 0x22). The device can also be configured to
use the other channel data in parallel as a low latency signal that will be internally mixed. See the Low Latency
Signal Path section of the datasheet for more information on how to use this feature.


Configuring I [2] S mode:
1. Set the data format to I [2] S in bit 2-3 of AUDIO_INTERFACE_CTRL Register (Address = 0x21)
2. Set the data length in bit 2-3 of the SDIN_CTRL Register (Address = 0x23)
3. Select left or right channel data for Audio Data in I2S_CTRL Register (Address = 0x22). The default channel
for Audio Data is left.
4. If the secondary Low Latency path will be used, enable in bit 0 of LL_EN Register (Address = 0x32) and
select left or right channel Low Latency data in I2S_CTRL Register (Address = 0x22). The default channel
for Low Latency Data is right.


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



5. Configure the optional 10-bit offset in bit 6-7 of SDIN_OFFSET_MSB Register (Address = 0x27) and
SDIN_AUDIO_OFFSET Register (Address = 0x28)



FSYNC


SCLK



~~Left Channel~~ ~~Right Channel~~



SDIN N-1 N-2 3 2 1 0


Device 1



Device 2


|Col1|N-1|N-2|
|---|---|---|
||||


|Col1|N-1|N-2|
|---|---|---|
||||



FSYNC


SCLK



**Figure 7-6. Timing Diagram for I2S Mode**


~~Left Channel~~ ~~Right Channel~~



SDIN N-1 N-2 3 2 1 0


Audio Data



|Col1|N-1|N-2|
|---|---|---|
||||


Low Latency Data



Device 1


Audio Data


|Col1|N-1|N-2|
|---|---|---|
||||



FSYNC


SCLK



**Figure 7-7. Timing Diagram for I2S Mode with Low Latency path**






|Left Channel Right Channel<br>N-1 N-2 3 2 1 0 N-1 N-2 3 2 1 0 N-1 N-2<br>Audio Data Low Latency Data Audio Data|Col2|
|---|---|
|N-1 N-2<br>3<br>2<br>1<br>0<br>Audio Data<br>N-1 N-2<br>3<br>2<br>1<br>0<br>Low Latency Data<br>N-1 N-2<br>Audio Data<br>~~Left Channel~~<br>~~Right Channel~~||
|||



Offset = 1 Offset = 1 Offset = 1


**Figure 7-8. Timing Diagram for I2S Mode with Low Latency path and Offset = 1**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 25


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**7.3.2.3 DSP Mode**


DSP mode uses the FSYNC pin to define the start of the audio data, but not to differentiate between channels.
The rising edge of the audio frame clock (FSYNC) starts the data transfer with the left channel data first and
is immediately followed by the right channel data. Each data bit is valid on the rising edge of the serial clock
(SCLK). A 10-bit channel offset can be configured for both the Audio and Low Latency Paths. DSP mode
enables the use of the Low Latency Path, and by default Audio data is first, Low Latency Data is second.


Configuring DSP mode:
1. Set the data format to DSP in bit 2-3 of AUDIO_INTERFACE_CTRL Register (Address = 0x21)
2. Set the data length in bit 2-3 of SDIN_CTRL Register (Address = 0x23)
3. Select the slot for the Audio data in AUDIO_SLOT_SELECT Register (Address = 0x33).
4. If the data steam has an offset (for example, a 1 bit offset), a 10-bit offset is available for configuration
in SDIN_OFFSET_MSB Register (Address = 0x27)(MSB) and SDIN_AUDIO_OFFSET Register (Address =
0x28) (LSB). The default offset is 0.
a. If the bit offset is applied, the same offset must be set in bit 4-5 in SDIN_OFFSET_MSB Register
(Address = 0x27) (MSB) and SDIN_LL_OFFSET Register (Address = 0x29) (LSB). The default offset is
0.


5. If the FSYNC pulse is shorter than 8 x SCLK, set AUDIO_INTERFACE_CTRL Register (Address = 0x21) bit
0-1 to "01"


FSYNC


SCLK



SDIN N-1 N-2 3 2 1 0


Device 1



|3|2|1|0|Col5|
|---|---|---|---|---|
|3|2|1|0||


Device 1


|Col1|N-1|N-2|
|---|---|---|
||||


|Col1|N-1|N-2|
|---|---|---|
||||



**Figure 7-9. Timing Diagram for DSP Mode**



Device 1



FSYNC


SCLK




|Col1|Col2|N-1 N-2 3 2 1 0 N-1 N-2 3 2 1 0<br>Device 1 Device 2|
|---|---|---|
||||
||||


|Col1|Col2|N-1 N-2<br>Device 1|
|---|---|---|
||||
||||



Offset = 1 Offset = 1


**Figure 7-10. Timing Diagram for DSP Mode with Offset = 1**


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3.2.4 TDM Mode**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



TDM mode supports 4, 8, or 16 channels of audio data through a single pin, SDIN. The data format follows the
DSP Mode.


TDM mode enables the possibility to transmit additional data besides audio for TAS6511-Q1. This includes a
secondary Low Latency path, which is disabled by default. It can be enabled in LL_EN Register (Address =
0x32). For more information on this function see Low Latency Signal Path.


**Configuring TDM mode while using the Audio Path only:**
1. Set the data format to TDM/DSP in bit 2-3 of AUDIO_INTERFACE_CTRL Register (Address = 0x21)
2. Set the data length in bit 2-3 of SDIN_CTRL Register (Address = 0x23)
3. Select the TDM slot for the Audio data in AUDIO_SLOT_SELECT Register (Address = 0x33).
4. If the TDM steam has an offset (for example, a 1 bit offset), a 10-bit offset is available for configuration
in SDIN_OFFSET_MSB Register (Address = 0x27)(MSB) and SDIN_AUDIO_OFFSET Register (Address =
0x28) (LSB). The default offset is 0.
a. If the bit offset is applied, the same offset must be set in bit 4-5 in SDIN_OFFSET_MSB Register
(Address = 0x27) (MSB) and SDIN_LL_OFFSET Register (Address = 0x29) (LSB). The default offset is
0.


5. If the FSYNC pulse is shorter than 8 x SCLK, set AUDIO_INTERFACE_CTRL Register (Address = 0x21) bit
0-1 to "01"


FSYNC


SCLK

|Slot 1|Slot 2|Slot 3|Slot 4|Slot 5|
|---|---|---|---|---|
|Audio Data|||||



**Example: Select TDM Slot 1**
Register 0x33 = 0x00: Audio Data Slot 1


**Figure 7-11. Timing Diagram for TDM Mode**


FSYNC


SCLK

|Slot 1|Slot 2|Slot 3|Slot 4|Slot 5|
|---|---|---|---|---|
|||Audio Data|||



**Example: Select TDM Slot 3**
Register 0x33 = 0x02: Audio Slot 3

|Slot M|Slot M+1|Slot 1|
|---|---|---|
|||Audio<br>Data|



**Figure 7-12. Timing Diagram for TDM mode with Slot = 3**

|Col1|N-1|
|---|---|
|||


|Col1|N-1|
|---|---|
|||


|0|Col2|
|---|---|
|0||


|0|Col2|
|---|---|
|0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 27


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


FSYNC


SCLK

|Col1|N-1 N-2 0|
|---|---|
|||
||Slot 1|



Bit Offset = 1 Bit Offset = 1

|Slot 1|Slot 2|Slot 3|Slot 4|Slot 5|
|---|---|---|---|---|
|Slot 1|Slot 2|Audio Data|Audio Data|Audio Data|



**Example: TDM Slot 3 with 1 bit offset**
Register 0x33 = 0x02: Audio Slot 3
Register 0x27 = 0x00, Register 0x28 = 0x01, Register 0x29 = 0x01: 1 bit offset


**Figure 7-13. Timing Diagram for TDM mode with Slot = 3 and Offset = 1**


**Configuring TDM mode while using the Full Featured Low Latency Path only:**


The Full Featured Low Latency Path expects Audio data in the same place as the standard audio path.


1. Set the data format to TDM/DSP in bit 2-3 of AUDIO_INTERFACE_CTRL Register (Address = 0x21)
2. Set the data length in bit 2-3 of SDIN_CTRL Register (Address = 0x23)
3. Enable the Full Featured Low Latency Audio path in bit 1 of LL_EN Register (Address = 0x32)
4. Select the TDM slot for the Full featured Low Latency Audio data in AUDIO_SLOT_SELECT Register
(Address = 0x33).
5. If the TDM steam has an offset (for example, a 1 bit offset), a 10-bit offset is available for configuration
in SDIN_OFFSET_MSB Register (Address = 0x27)(MSB) and SDIN_AUDIO_OFFSET Register (Address =
0x28) (LSB). The default offset is 0.
a. If the bit offset is applied, the same offset must be set in bit 4-5 in SDIN_OFFSET_MSB Register
(Address = 0x27) (MSB) and SDIN_LL_OFFSET Register (Address = 0x29) (LSB). The default offset is
0.


6. If the FSYNC pulse is shorter than 8 x SCLK, set AUDIO_INTERFACE_CTRL Register (Address = 0x21) bit
0-1 to "01"


The timing diagram for the Full Featured Low Latency Path follows the same configuration as the Audio Path
Only.


**Configuring TDM mode while using both Audio and Low Latency Paths:**
1. Set the data format to TDM/DSP in bit 2-3 of AUDIO_INTERFACE_CTRL Register (Address = 0x21)
2. Set the data length in bit 2-3 of SDIN_CTRL Register (Address = 0x23)
3. Enable the Low Latency path in bit 0 of LL_EN Register (Address = 0x32)
4. Select TDM slots for Audio and Low Latency Path Data in AUDIO_SLOT_SELECT Register (Address =
0x33) and LL_SLOT_SELECT Register (Address = 0x34), respectively.
a. If the default values are left unchanged (Slot 1 for AUDIO_SLOT_SELECT Register (Address = 0x33)
and Slot 1 for LL_SLOT_SELECT Register (Address = 0x34)), or are assigned to the same slot, Low
Latency Data will immediately follow the Audio Path Data to avoid overlap.


5. If the TDM stream has an offset, (for example, a 1 bit offset), a 10-bit offset is available for each applicable
channel group to determine the timing and avoid overlapping data. If an offest is used, the same offset
should be set in both data paths. The additional bit offsets can be set in:
a. **Audio Channel** Bit 6-7 in SDIN_OFFSET_MSB Register (Address = 0x27) (MSB) and
SDIN_AUDIO_OFFSET Register (Address = 0x28) (LSB). The default offset is 0.
b. **Low Latency Channel** Bit 4-5 in SDIN_OFFSET_MSB Register (Address = 0x27) (MSB) and
SDIN_LL_OFFSET Register (Address = 0x29) (LSB). The deafult offset is 0.


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



c. When both the Audio path and Low Latency Path slots are selected to be the same slot (default Slot
1) in AUDIO_SLOT_SELECT Register (Address = 0x33) and LL_SLOT_SELECT Register (Address =
0x34), and the 10-bit offset is also the same (default 0), low latency channel data will immediately follow
the audio channel data. To avoid data overlap, it is recommended to always set the same bit offset for
the Audio and Low Latency Paths.


6. If the FSYNC pulse is shorter than 8 x SCLK, set AUDIO_INTERFACE_CTRL Register (Address = 0x21) bit
0-1 to "01"


FSYNC


SCLK



|Slot 1|Slot 2|Slot 3|Slot 4|
|---|---|---|---|
|Audio Data|Low Latency Data|Low Latency Data|Low Latency Data|


|Slot M-1|Slot M|Slot 1|Slot 2|
|---|---|---|---|
|||Audio<br>Data|LL Data|


**Example: Select TDM Slot 1 for Audio Data, Slot 2 for Low Latency Data**
Register 0x33 = 0x00: Audio Slot 1
Register 0x34 = 0x01: Low Latency Slot 2

|Col1|N-1|
|---|---|
|||



**Figure 7-14. Timing Diagram for TDM Mode with Audio and Low Latency Data**


FSYNC


SCLK







|Slot 1|Slot 2|Slot 3|Slot 4|
|---|---|---|---|
|||Audio Data|Low Latency Data|


**Example: Select TDM Slot 3 for Audio Data, Slot 4 for Low Latency Data**
Register 0x33 = 0x02: Audio Slot 3
Register 0x34 = 0x03: Low Latency Slot 4

|Col1|N-1|N-2|
|---|---|---|
||||



**Figure 7-15. Timing Diagram for TDM Mode with Audio Slot = 3 and Low Latency Data Slot = 4**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 29


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


FSYNC


SCLK

|Col1|N-1 N-2 0|
|---|---|
|||
||Slot 1|



Bit Offset = 1 Bit Offset = 1

|Slot 1|Slot 2|Slot 3|Slot 4|Slot 5|
|---|---|---|---|---|
|Slot 1|Slot 2|Audio Data|Low Latency Data|Low Latency Data|



**Example: Select TDM Slot 3 for Audio Data and TDM Slot 4 for Low Latency Data, with 1 bit offset**
Register 0x33 = 0x02: Audio Slot 3
Register 0x34 = 0x03: Low Latency Data Slot 4
Register 0x27 = 0x00, Register 0x28 = 0x01, Register 0x29 = 0x01: 1 bit offset


**Figure 7-16. Timing Diagram for TDM Mode with Audio Slot = 3 and Low Latency Data Slot = 4, 1 bit**

**offset for Audio and Low Latency Path**


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3.2.5 SDOUT - Data Output**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



TAS6511-Q1 can transmit selected data in either I [2] S mode or TDM mode. The audio input serial clock (SCLK)
and audio frame clock (FSYNC) is reused, and the outgoing data has the same sampling frequency and
maximum audio frame size as the audio input signal. The word length of the SDOUT data can be configured in
the SDOUT_CTRL Register (Address = 0x25).


SDOUT requires the Serial Audio Port to operate in I [2] S or TDM mode data formats. Left-justified and DSP mode
formats are not supported.


The following data groups can be transmitted through SDOUT:

 - **Isense** - Current Sense feedback by channel

 - **Vpredict** - Output voltage estimate based on supply voltage and input signal by channel

 - **Temperature** - 8-bit device temperature reading from integrated temperature sensor

 - **PVDD Voltage** - 8-bit device PVDD sensor voltage reading


The temperature data and PVDD voltage data can be added to the SDOUT data stream by setting bit 5 of the
SDOUT_DATA Register (Address = 0x5B) to 1. When this bit is set to 1, the Isense data and Vpredict data is
16-bit else the data is set to the word length configured in SDOUT_CTRL Register (Address = 0x25).


**Note**
The availability of the data for output transmission depends on the activation of the underlying
function. Example: Isense requires Current Sense to be enabled.


**Note**
The data word length must be set to at 24-bits or greater if temperature and PVDD data is enabled, to
avoid data from truncating the LSBs.


**Note**
The phase offset between Isense and Vpredict data is configurable in the DSP.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 31


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


_**7.3.2.5.1 SDOUT - I**_ _**[2]**_ _**S Configuration**_


Using SDOUT in I [2] S mode requires the usage of one of the GPIO pins to be configured as an SDOUT pin to
transmit data. See General Purpose Output for details on how to configure a GPIO pin as SDOUT. When the
SDOUT is configured in I [2] S format the left and right channel data will be formatted as outlined in Table 7-1


**Table 7-1. SDOUT - I** **[2]** **S Configuration**

|SDOUT_DATA Register (Address = 0x5B) bit 5|Isense Data Group|Vpredict Data Group|
|---|---|---|
|0|24-bit Isense + 8-bit 0|24-bit Vpredict + 8-bit 0|
|1|16-bit Isense + 8-bit Temperature Data + 8-bit 0|16-bit Vpredict +8-bit PVDD data + 8-bit 0|



**SDOUT_DATA**
**Register**
**(Address = 0x5B)**
Bit 5 = 0



**SDOUT_DATA**
**Register**
**(Address = 0x5B)**
Bit 5 = 1







**Figure 7-17. SDOUT I** **[2]** **S Configuration**


32 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


_**7.3.2.5.2 SDOUT - TDM Configuration**_



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Transmitting data through SDOUT in TDM mode requires a minimum of one data output.


Similar to the SDIN TDM configuration, a TDM slot selection feature and an additional 10-bit offset is used
for the SDOUT data to determine the timing and avoid overlapping data. The slot selection feature selects
the TDM slot output for each data group and can be selected in ISENSE_OUTPUT_SLOT Register (Address
= 0x35) and VPREDICT_OUTPUT_SLOT Register (Address = 0x36) The additional bit offset is defined as
the number of SCLK cycles from the start (MSB) of the audio frame to the start of the data group. The bit
offset for the ISENSE data group is located in Bit 6-7 in SDOUT_OFFSET_MSB Register (Address = 0x2C)
(MSB) and ISENSE_OFFSET Register (Address = 0x2D) (LSB). The default offset is 0 bits. The bit offset for
the Vpredict data group is located in Bit 6-7 in SDOUT_OFFSET_MSB Register (Address = 0x2C) (MSB) and
VPREDICT_OFFSET Register (Address = 0x2E) (LSB). The default offset is 0 bits.


The SDOUT data consist of the Isense data, Vpredict data, Temperature data, and PVDD voltage data. The
format of the output datastream is outlined in Table 7-2. In multi-device systems the slot select can be utilized to
shift data groups to available slots and allow multiple devices to share one TDM line.


Figure 7-18 shows the format of the Isesne and Vpredict data.


**Table 7-2. SDOUT - TDM Configuration**

|SDOUT_DATA Register (Address = 0x5B) Bit 5|Isense Data Group|Vpredict Data Group|
|---|---|---|
|0|16-bit Isense + 8-bit 0|16-bit Vpredict + 8-bit 0|
|1|16-bit Isense + 8-bit Temperature Data + 8-bit 0|16-bit Vpredict +8-bit PVDD data + 8-bit 0|



Slot 1 Slot 2 Slot 3 Slot 4 Slot 5 Slot 6 Slot 7 Slot 8



SDOUT_DATA
Register
(address= 0x5B)

Bit 5 = 0



Register 0x35:

0x00

Slot 1



CH1 Isense CH1 Vpredict



Register 0x36:

0x01

Slot 2



Slot 1 Slot 2 Slot 3 Slot 4 Slot 5 Slot 6 Slot 7 Slot 8



0x2C bits [7:6]

SDOUT_DATA Register 0x2D shiand register � value TemperatureCH1 Isense +
(address= 0x5B)
Bit 5 = 1 Register 0x35:
0x00

Slot 1



CH1 Vpredict +

PVDD data


Register 0x36:

0x01

Slot 2



**Figure 7-18. TDM SDOUT Format and Configuration**


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 33


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**7.3.2.6 Device Clocking**


The TAS6511-Q1 has a flexible clocking system. Internally, the device requires several additional clocks, mostly
at related clock rates to function correctly. All of these clocks can be derived from the Serial Audio Interface.


Figure 7-19 shows the basic data flow and clock distribution.







SCLK







SDIN




|Col1|Device internal DSPCLK OSRCLK DACCLK<br>DSP<br>Audio Delta Sigma<br>(Including DAC<br>(Input) Modulator<br>interpolator)|
|---|---|
|Serial<br>Interface|Audio<br> (Input)|
|||



**Figure 7-19. Audio Flow with Respective Clocks**


The Serial Audio Interface typically has 3 connection pins which are listed as follows:

 - SCLK (Audio Serial Clock)

 - FSYNC (Frame Sync in TDM or Left/Right in I [2] S)

 - SDIN (Input Data)

 - Optional: SDOUT for outgoing data transmission.


The device has an internal PLL which uses SCLK as a reference clock and creates the higher rate clocks
required by the DSP and the DAC clock.


The TAS6511-Q1 has an audio sampling rate detection circuit that automatically senses the sampling frequency.
Common audio sampling frequencies of 16kHz, 32kHz, 44.1kHz – 48 kHz, 88.2 kHz – 96 kHz, and 192 kHz are
supported. The sampling frequency detector sets the clock for DAC and DSP automatically.


_**7.3.2.6.1 Clock Rates**_


The serial audio interface port is a 3-wire serial port with the signals SCLK, FSYNC and SDIN.


SCLK is the serial audio bit clock used to clock the serial data present on SDIN into the serial shift register of the
audio interface. Serial data is clocked into the TAS6511-Q1 device with SCLK.


The FSYNC pin is the serial audio left/right word clock or frame sync when the device is operated in TDM Mode.


SDIN is the TDM or I2S data input.


**Table 7-3. Audio Data Formats, Bit Depths and Clock Rates**






|Format|Data Bits|Maximum FSYNC Frequency<br>(kHz)|SCLK Rate (f )<br>s|
|---|---|---|---|
|I2S / LJ|32, 24, 20, 16|16 to 192|x64, x32|
|TDM|32, 24, 20, 16|16 to 48|x128, x256, x512|
|TDM|32, 24, 20, 16|96|x128, x256|
|TDM|32, 24, 20, 16|192|x128|



When a clock halt or a non-supported SCLK to FSYNC ratio is detected, the device reports the clock halt or a
non-supported SCLK to FSYNC ratio as a latched report in bit 0 of CLK_FAULT_LATCHED Register (Address =
0x8A). The latched error report clears on read.


_**7.3.2.6.2 Clock Halt Auto-recovery**_


Certain host processors halt the audio clock when no audio is playing. When the clock is halted, the device puts
the channel into the Hi-Z state and issues a latched error report in CLK_FAULT_LATCHED Register (Address
= 0x8A). The transition to Hi-Z occurs gracefully by holding the last received sample from the audio interface
and ramping down the volume. This behavior can be changed in bit 7 of AUDIO_INTERFACE_CTRL Register
(Address = 0x21). The latched error report clears once read. After audio clock recovery, the device automatically
returns to the previous state.


34 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



_**7.3.2.6.3 Sample Rate on the Fly Change**_


TAS6511-Q1 supports an on-the-fly change in the FSYNC rate. When changing FSYNC, for example from
48 kHz to 96 kHz, the host processor needs to put the FSYNC/SCLK to a halt state for at least 30 ms
before changing to the new sample rate. During this halt state, a clock error is reported. See the Clock Halt
Auto-recovery section for further details.


**7.3.2.7 Clock Error Handling**


After Power-On-Reset (POR) the device assumes that a clock error exists, but does not assert the clock error
flag until the clock error detection result is valid.


If any input clock changes are detected, the auto detect system immediately requests the device to mute, while
the auto detect continues to monitor and identify a new stable condition.


The clock error flag output to the FAULT pin can be latched or non-latched, based on the configuration in Bit 6
and 7 of the REPORT_ROUTING_5 Register (Address = 0x94).


In latched configuration, the fault can be cleared by reading the CLK_FAULT_LATCHED Register (Address =
0x8A).


_**7.3.3 Digital Audio Processing**_


TAS6511-Q1 offers advanced digital audio processing capabilities including:


 - High-Pass Filter / DC Blocking

 - Digital Volume Control

 - PVDD Foldback / AGL

 - Thermal Foldback

 - Gain Compensation Biquads

 - Hybrid Modulation

 - Real-Time Load Diagnostics

 - Clip Detect

 - Low Latency Path

 - SpeakerGuard Pro Power Limiter


The availability of specific features is dependent on the selected sampling frequency. Higher sampling
frequencies reduce the available processing time of the integrated DSP and limit the number of functions that
can operate in parallel. At all sampling frequencies, maintaining that the total processing need of the enabled
functions does not exceed the available amount of processing time.


**7.3.3.1 PVDD Foldback**


PVDD Foldback applies a smooth compression to the audio signal to maintain a consistent dynamic range while
the supply voltage (PVDD) varies. This feature helps to prevent unexpected output clipping and distortion in
systems where the audio signal would exceed the supply headroom and can also be described as Automatic
Gain Limiter (AGL).


An 8-bit ADC senses the applied PVDD voltage. This PVDD sense data provides the necessary inputs for the
DSP to calculate the amount of compression that needs to be applied to signal peaks. In addition, the PVDD
sense results can be read back via I [2] C through the PVDD_SENSE Register (Address = 0x74).


The PVDD foldback engages in two functional modes, depending on the measured value of supply voltage
(PVDD).


 - Mode 1: If PVDD voltage is greater than the maximum peak output voltage (MPOV), no action will be taken
by the PVDD sensing circuit since there is still sufficient headroom for the amplifier to reproduce the audio
signals up to 0 dBFS.

 - Mode 2: If PVDD voltage is less than MPOV, the PVDD sensing circuit will reduce gain to ensure that signals
can fit within the available PVDD voltage to avoid clipping. The attack time and time constants of the foldback
are configurable.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 35


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


PVDD Foldback can be enabled by setting bit 4 in FOLDBACK_EN Register (Address = 0x3A) to 1.



A � ack

Starts



Release

Starts



PVDD

MPOV


**7.3.3.2 High-Pass Filter**



**Figure 7-20. PVDD Foldback Example**



To protect speakers connected to the TAS6511-Q1, a 3Hz DC blocking high pass filter is built
into the audio processing path. This filter is turned on by default and be configured in bit 0 of
DC_BLOCK_SPEAKER_GUARD_EN Register (Address = 0x39)


**7.3.3.3 Analog Gain**


TAS6511-Q1 allows the user to set the analog gain for the output channel to 4 different settings.


Analog gain can be configured in ANALOG_GAIN Register (Address = 0x4A).


A gain setting of 0dB corresponds with a peak output voltage of 21V/FS at full scale digital input. TI recommends
to select the lowest possible gain for the expected PVDD operation to optimize output noise and dynamic range
performance.


The Analog Gain setting is only be changed while the device is in Hi-Z, DEEP SLEEP, or SLEEP state.


As the device enters Play state the device gradually ramps the analog gain to the desired value. The ramp
speed is configurable in ANALOG_GAIN_RAMP_CTRL Register (Address = 0x4E).


**7.3.3.4 Digital Volume Control**


The output channel has a digital-volume control with a range from 0 dB to -103 dB in 0.5 dB steps.


The volume control is set through I [2] C in the register DIG_VOL_CH1 Register (Address = 0x40).


The gain ramp-up and ramp-down rate as well as the step size in dB is programmable through I [2] C in
DIG_VOL_RAMP_CTRL Register (Address = 0x44).


_**7.3.3.4.1 Auto Mute**_


When detecting a consecutive stream of zero samples at the audio input, the device can automatically set
channel into mute. In this mode, the device continues to monitor the input signal, and, depending on the
configuration, unmute the channel at the same time when a valid non-zero signal arrives.


This auto mute feature can be enabled and configured in AUTO_MUTE_EN Register (Address = 0x47). Auto
mute is disabled by default.


The required time of consecutive zero samples before auto mute becomes active can be set in
AUTO_MUTE_TIMING Register (Address = 0x48).


**7.3.3.5 Gain Compensation Biquads**


The modulator and output LC filter of the Class-D amplifier can have an undesired influence on frequency
response linearity causing frequency drop/peaking. To help compensate for this effect and achieve a flat
response, TAS6511-Q1 offers integrated gain compensation biquads.


36 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



The biquad is configurable and is disabled by default. To enable the desired tuning, the respective coefficients
need to be written to the DSP memory.


**7.3.3.6 Low Latency Signal Path**


For time-sensitive audio signals that require a minimal processing delay, such as active noise cancellation (ANC)
or road noise cancellation (RNC), TAS6511-Q1 offers a low latency signal path. At 48 kHz sampling frequency,
this path reduces the signal delay by more than 70% between the input and output of the amplifier by minimizing
the internal signal processing.


The low latency signal path is established in parallel to the regular audio signal path. When both signal paths are
provided with input data, the two signals - audio and low latency - are internally mixed together right before the
output amplification stage. Both signals are added together and the combined signal amplitude must not exceed
the available gain range nor the voltage headroom to avoid distortion. Note that the low latency signals pass
through the device with less delay than the regular audio path signals.


The low latency signal path is disabled by default. It can be enabled in LL_EN Register (Address = 0x32), bit 0.
In TDM mode, a slot selection feature is available to configure the location of the low latency input in the TDM
stream. The slot selection can be configured in bit 0-3 of LL_SLOT_SELECT Register (Address = 0x34). See
TDM mode for more details.


In I [2] S mode the low latency data is selected in I2S_CTRL Register (Address = 0x22) bits 4-5.


**Note**
The settings in I2S_CTRL Register (Address = 0x22) bits [5:4] and [7:6] must be selected for different
audio channel source data.


The low latency signal path is only available at a sampling frequency of 48kHz or 96kHz.



Example TDM8 signal

|TDM Audio Source SDIN_1<br>(e.g. Tuner, DSP, SoC)<br>ANC/RNC<br>Noise cancellation signal|CHANNEL 1<br>+<br>Output<br>LL CHANNEL 1 Stage|OUTPUT 1|
|---|---|---|
|SDIN_1<br>TDM Audio Source<br>(e.g. Tuner, DSP, SoC)<br>ANC/RNC<br>Noise cancellation signal|+<br>Output<br>Stage<br>CHANNEL 1<br>LL CHANNEL 1||



Slot 1 2 3 4 5 6 7 8









Signal



Audio

Ch1



LL

Ch1



No

Audio

Data



No

Audio

Data



No

Audio

Data



No

Audio

Data



No

Audio

Data



No

Audio

Data



**Figure 7-21. Low Latency and Audio Signal Path**


**7.3.3.7 Full Feature Low Latency Path**


In addition to the Low Latency Signal Path, the TAS6511-Q1 integrates a Full Feature Low Latency Path. Using
the Full Feature Low Latency Path the time-sensitive audio signals, such as active noise cancellation (ANC) or
road noise cancellation (RNC), can be premixed and do not need to be separated from the non-time-senstive
audio data. The premixed audio data then processed through the DSP and then amplifed at the output stage
with a lower group delay.


The Full Feature Low Latency Path can be used in both I2S and TDM modes and is disabled by default. To
enable, use bit 1 in LL_EN Register (Address = 0x32).


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 37


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**



TDM Audio Source
(e.g. Tuner, DSP, SoC)


Example TDM4 signal


Slot 1 2 3 4



SDIN









No Audio

Data



No Audio

Data



Signal



Audio Ch1

+

ANC/RNC

Ch1



No Audio

Data


|DSP<br>Audio data<br>processed with all<br>enabled DSP Output<br>features Stage|OUTPUT 1|
|---|---|
|Output<br>Stage<br>**DSP**<br>Audio data<br>processed with all<br>enabled DSP<br>features||



**Figure 7-22. Full Feature Low Latency Audio Path**


_**7.3.4 Class-D operation and Spread Spectrum Control**_


**7.3.4.1 Modulation**


TAS6511-Q1 supports three modulation schemes: BD modulation, advanced 1SPW modulation and Hybrid
modulation. The modulation scheme can be selected in OUTPUT_CTRL Register (Address = 0x02).


_**7.3.4.1.1 BD Modulation**_


In BD modulation each output is switching from 0 volts to the supply voltage. The OUT_xP and OUT_xN are
in phase with each other with no input signal, resulting in little to no current in the speaker. The duty cycle
of OUT_xP is greater than 50% and OUT_xN is less than 50% for positive output voltages. The duty cycle
of OUT_xP is less than 50% and OUT_xN is greater than 50% for negative output voltages. In low signal
conditions, the voltage across the load sits at 0 V throughout most of the switching period, reducing the switching
current and therefore, any I [2] R losses in the load.


38 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



OUTP


OUTN


OUTP - OUTN


Speaker

Current


OUTP


OUTN



0V



OUTP - OUTN


Speaker

Current



PVDD


0V


0A



OUTP


OUTN


OUTP - OUTN



0V



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025


No Output


Positive Output


Negative Output

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||



**Figure 7-23. BD Modulation**



Speaker

Current



- PVDD


0A



_**7.3.4.1.2 Advanced 1SPW Modulation**_


Advanced 1SPW modulation alters the modulation scheme to achieve higher efficiency. In idle or low signal
conditions the outputs operate at less than 20% duty cycle, reducing losses to a minimum. When an audio
signal is applied, one output of the bridge decreases the duty cycle while the other output side increases.
The decreasing output signal rails to GND. At this point, all the audio modulation takes place through the
rising output. The result is that only one output is switching during the majority of the audio cycle. Efficiency is
improved in this mode due to the reduction of switching losses.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 39


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


OUTP


OUTN

No Output



OUTP - OUTN


Speaker

Current


OUTP - OUTN


Speaker

Current


OUTP - OUTN



0 V


OUTP


OUTN


PVDD


0 V


0 A


OUTP


OUTN


0 V


  - PVDD



Positive Output


Negative Output



Speaker

Current


_**7.3.4.1.3 Hybrid Modulation**_



0 A



**Figure 7-24. 1SPW Modulation**



Hybrid Modulation is designed for minimized power loss without compromising the high output power
performance. With Hybrid modulation, TAS6511-Q1 uses the integrated DSP to detect the input signal level
and adjusts the PWM duty cycle as well as other modulation parameters dynamically based on output power.
Hybrid modulation achieves ultra low idle current and maintains the excellent audio performance. Unlike 1SPW
or BD Modulation, Hybrid Modulation must be activated in the DSP memory before it can be used. The Hybrid
modulation configuration is dependent on the selected switching frequency, PVDD supply voltage and output
impedance.


**7.3.4.2 High-Frequency Pulse-Width Modulator (PWM)**


The PWM modulator converts the input audio data into a switched signal of varying duty cycle. The PWM
modulator is an advanced design with high bandwidth, low noise, low distortion, and excellent stability.


The output switching frequency is selectable via I [2] C in the FSW_CTRL Register (Address = 0x52).


40 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



The zero frequency resistor of the control loop is recommended to be selected to the corresponding switching
frequency using RZ_CTRL Register (Address = 0x51).


If a different PWM output phase is desired, manual phase mode in bit 7 of PWM_PHASE_CTRL Register
(Address = 0x60) can be enabled. In manual mode, the output phase can be set in 1.4 degree steps in
RAMP_PHASE_CTRL_GPO Register (Address = 0x68).


**7.3.4.3 Spread Spectrum Control**


TAS6511-Q1 applies spread spectrum control to the modulator's clock signal. Controlling the spectrum of the
clock signal translates into an optimized behavior of higher frequency signal components which are visible during
EMI testing. Spread spectrum modulation is a PWM modulation technique that reduces the peaks seen in EMI
measurements by varying the output PWM frequency, resulting in a wider spectrum but lower level.


The effectiveness of reducing the EMI noise level can be optimized through several configurable parameters:


 - Modulation scheme, configured through SS_CTRL Register (Address = 0x61)

–
Triangle
– Random

–
Triangle + Random

–
Spread Spectrum disabled by turning both schemes off

 - Spread spectrum frequency range, configured through SS_RANGE_CTRL Register (Address = 0x62).

 - Spread spectrum modulation frequency (F SS ), configured through SS_RANGE_CTRL Register (Address =
0x62).


F max


F center


F min


**Time**


**Figure 7-25. Spread-Spectrum Algorithm Diagram**


Table 7-4 shows typical spread spectrum configurations. For other PWM frequencies not listed in the table, F SS
and modulation depth are slightly different, please find more details in SS_RANGE_CTRL Register (Address =
0x62).


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 41


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**Table 7-4. Typical Spread Spectrum**











|FSW_CTRL Register<br>(Address = 0x52) Bit 0-2|SS_CTRL Register (Address<br>= 0x61) Bit 0-2|SS_RANGE_CTRL Register<br>(Address = 0x62)|Spread Spectrum|
|---|---|---|---|
|0b001: 480kHz Fsw|0b010|0x00|**Random SS, +0.39% range** (1)|
|0b001: 480kHz Fsw|0b010|0x10|Random SS, ±0.39% range|
|0b001: 480kHz Fsw|0b010|0x20|Random SS, ±1.17% range|
|0b001: 480kHz Fsw|0b010|0x30|Random SS, ±2.73% range|
|0b001: 480kHz Fsw|0b010|0x40|Random SS, ±5.86% range|
|0b001: 480kHz Fsw|0b010|0x50|Random SS, ±12.11% range|
|0b001: 480kHz Fsw|0b001|0x00|Triangle SS, 30 kHz Fss, ±9.5% range|
|0b001: 480kHz Fsw|0b001|0x01|Triangle SS, 30 kHz Fss, ±12.5% range|
|0b001: 480kHz Fsw|0b001|0x02|Triangle SS, 60 kHz Fss, ±9.5% range|
|0b001: 480kHz Fsw|0b001|0x03|Triangle SS, 60 kHz Fss, ±12.5% range|
|0b001: 480kHz Fsw|0b011|0x00|Random SS, +0.39% range<br>+ Triangle SS, 30 kHz Fss, ±9.5% range|
|0b001: 480kHz Fsw|0b011|0x01|Random SS, ±0.39% range<br>+ Triangle SS, 30 kHz Fss, ±12.5% range|
|0b001: 480kHz Fsw|0b011|0x10|Random SS, ±1.17% range<br>+ Triangle SS, 30 kHz Fss, ±9.5% range|
|0b001: 480kHz Fsw|0b011|0x11|Random SS, ±1.17% range<br>+ Triangle SS, 30 kHz Fss, ±12.5% range|
|0b001: 480kHz Fsw|0b011|**……**|**……**|
|**......**|Settings for all other FSW can be found in registers0x61 and0x62|Settings for all other FSW can be found in registers0x61 and0x62|Settings for all other FSW can be found in registers0x61 and0x62|
|0b011: 2.048MHz Fsw|0b010|0x00|Random SS, +1.67% range|
|0b011: 2.048MHz Fsw|0b010|0x10|Random SS, ±1.67% range|
|0b011: 2.048MHz Fsw|0b010|0x20|Random SS, ±5.00% range|
|0b011: 2.048MHz Fsw|0b010|0x30|Random SS, ±11.67% range|
|0b011: 2.048MHz Fsw|0b010|0x40|Random SS, ±25.00% range|
|0b011: 2.048MHz Fsw|0b010|0x50|Random SS, ±51.67% range|
|0b011: 2.048MHz Fsw|0b001|0x00|Triangle SS, 128 kHz Fss, ±6.5% range|
|0b011: 2.048MHz Fsw|0b001|0x01|Triangle SS, 128 kHz Fss, ±13.5% range|
|0b011: 2.048MHz Fsw|0b001|0x02|Triangle SS, 170 kHz Fss, ±5% range|
|0b011: 2.048MHz Fsw|0b001|0x03|Triangle SS, 170 kHz Fss, ±10% range|
|0b011: 2.048MHz Fsw|0b011|0x00|Random SS, +1.67% range<br>+ Triangle SS, 128 KHz Fss, ±6.5% range|
|0b011: 2.048MHz Fsw|0b011|0x01|Random SS, ±1.67% range<br>+ Triangle SS, 30 kHz Fss, ±13.5% range|
|0b011: 2.048MHz Fsw|0b011|0x10|Random SS, ±5.00% range<br>+ Triangle SS, 128 kHz Fss, ±6.5% range|
|0b011: 2.048MHz Fsw|0b011|0x11|Random SS, ±5.00% range<br>+ Triangle SS, 30 kHz Fss, ±13.5% range|
|0b011: 2.048MHz Fsw|0b101|0x08|**Random Period Triangle SS**<br>**1/Fss to 4/Fss** (1)|
|0b011: 2.048MHz Fsw||**……**|**……**|


(1) TI recommended spread spectrum configuration


42 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3.4.4 Gate Drive**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



The gate driver accepts the low-voltage PWM signal and level shifts it to drive a high-current, full-bridge,
power-FET stage.


The device uses proprietary techniques to optimize EMI and audio performance. The gate driver power supply
voltage, GVDD, is internally generated and a decoupling capacitor must be connected at the GVDD_BYP pin.


The full H-bridge output stages use only NMOS transistors. Therefore, bootstrap capacitors are required for the
proper operation of the high-side NMOS transistors. A 0.22µF ceramic capacitor of quality X7R or better, rated
appropriately for the applied voltages, must be connected from each output to the corresponding bootstrap input.
The bootstrap capacitors connected between the BST pins and the corresponding output function as a floating
power supply for the high-side N-channel power MOSFET gate drive circuitry. During each high-side switching
cycle, the bootstrap capacitors hold the gate-to-source voltage high, keeping the high-side MOSFETs turned on.


**7.3.4.5 Power FETs**


The BTL output channel comprises four N-channel FETs for high efficiency and maximum power transfer to
the load. These FETs are designed to handle the fast switching frequency and large voltage transients during
operation within the _Recommended Operating Conditions_ .


_**7.3.5 Load Diagnostics**_


The device incorporates both DC and AC load diagnostics which are used to determine the status of the load.
The DC-diagnostics are turned on by default.


**7.3.5.1 DC Load Diagnostics**


The DC load diagnostics are used to verify if the load is connected properly.


To support system level start up requirements of a fast time to audio:

 - The diagnostics are available as soon as the device leaves the DEEP SLEEP mode and supplies are within
the recommended operating range.

 - The diagnostics do not rely on external audio input signals or clock and sync frequencies to be available.


DC Diagnostics complete successfully and allow the channel to enter MUTE or PLAY mode if the following tests
pass on the output pins:


 - No short to ground

 - No short to power

 - No shorted load

 - No open load


When there is no fault and on completion of the diagnostics routine, the CH1 LDG RESULT bit 3 of
DC_LDG_RESULT Register (Address = 0xC2) is set. If DC load diagnostics identifies a fault, the CH1 LDG
RESULT bit 3 in register DC_LDG_RESULT Register (Address = 0xC2) stays low indicating 'DC Load Diagnostic
did not complete without faults on channel 1'. Details of the fault is reported in DC_LDG_REPORT Register
(Address = 0xC0). The channel is retested after approximately 750ms until either the fault has been eliminated
or the diagnostics function is turned off by I [2] C control.


Any of the following conditions start the DC Load Diagnostics:

 - Automatic DC load diagnostics at device initialization. Automatically at device initialization, and after the PD
pin is pulled low, after transitioning from DEEP SLEEP state to SLEEP state and under the condition that
all power supplies are within the recommended operating range, the device automatically starts DC load
diagnostics. This diagnostic can be aborted, if needed.

 - Automatic DC load diagnostics during Hi-Z or PLAY. DC diagnostics can automatically run after the channel
fault occurs during HI-Z or PLAY state.

 - Manual start of DC load diagnostics. DC diagnostics can be enabled manually to run on the channel.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 43


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


_**7.3.5.1.1 Automatic DC Load Diagnostics at Device Initialization**_


The TAS6511-Q1 supports automatic and autonomous DC load diagnostics at device start-up. When leaving
DEEP SLEEP state and under the condition that all power supplies are within the recommended operating
range, the device transitions into SLEEP state and automatically starts DC load diagnostics. Automatic DC load
diagnostics at device initialization can be aborted by setting bit 0 and bit 7 in DC_LDG_CTRL Register (Address
= 0xB0) to ‘1’ if desired. Both bits remain in this configuration until the channel transitions into Hi-Z state or PLAY
state. Afterward, the bit values can either remain or the bit values can be restored to the default of ‘0’ through a
manual change or when the device resets.


Neither I [2] C configuration nor any audio signals are necessary for the TAS6511-Q1 to perform short-to-power
(S2P), short-to-ground (S2G), open-load (OL), and shorted-load (SL) tests based on default configuration.
Systems can benefit from this autonomous operation as running the load diagnostics while bringing up the digital
part of the audio chain is possible.


A successful diagnostics without faults sets the respective bit in DC_LDG_RESULT Register (Address = 0xC2)
to 1. Once the system is ready to set the channel status to PLAY mode, no further delay is introduced. If a fault
is detected during the diagnostics, the channel re-runs the DC load diagnostics after approximately 750ms until
either the fault has been eliminated or the LDG BYPASS bit 1 in DC_LDG_CTRL Register (Address = 0xB0) is
set.


If automatic DC load diagnostics with default values is not desired, a GPIO pin configured as a STBY pin can be
held low until the device is fully configured via I [2] C.


_**7.3.5.1.2 Automatic DC load diagnostics during Hi-Z or PLAY**_


When a fault occurs while the channel is in Hi-Z or PLAY state, the device places the channel in either FAULT
state or Auto Recovery (AUTOREC) state. After the fault is resolved or cleared, the device runs automatic DC
load diagnostics on the channel and recover to the previous Hi-Z or PLAY state unless a different state was
requested through I [2] C.


This function is enabled by default through the LDG BYPASS bit 0 in DC_LDG_CTRL Register (Address =
0xB0).


If DC load diagnostics identifies a fault, the channel CH1 LDG RESULT bit 3 in DC_LDG_RESULT Register
(Address = 0xC2) stays low indicating 'DC Load Diagnostic did not complete without faults on channel 1'.
Details of the fault are reported in DC_LDG_REPORT Register (Address = 0xC0). The channel is retested after
approximately 750ms until either the fault has been eliminated or the diagnostics function is turned off by I [2] C
control.


A successful diagnostics without faults, sets the CH1 LDG RESULT bit 3 to 1.


**Note**
Automatic DC load diagnostics does not be run if a clock fault is detected


_**7.3.5.1.3 Manual start of DC load diagnostics**_


Manual DC load diagnostics can be enabled in any state after all power supplies are within the recommended
operating range and after the device has transitioned to SLEEP state for the first time. DC diagnostics can be
enabled manually by setting the I [2] C control state register to LOAD DIAG state to run on the channel. If either
the STBY pin (if configured to a GPIO pin) or a GPIO pin function set the device to SLEEP or DEEP SLEEP
state, manual DC Load diagnostics cannot be run. This doesn’t apply when the device is set to SLEEP or DEEP
SLEEP state through I [2] C control, in which manual DC Load diagnostics are available.


Procedure:

 - Make sure all power supplies are within the recommended operating range and device initialization is
complete.

 - Set channel to Hi-Z or SLEEP state in bit 4-6 STATE_CTRL Register (Address = 0x03)


44 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025




 Write any desired control parameters for DC load diagnostics in DC_LDG_CTRL Register (Address = 0xB0),
DC_LDG_TIME_CTRL Register (Address = 0xB2), DC_LDG_SL_CTRL Register (Address = 0xB3).

 - Set audio channel into Diag mode to start DC Diagnostics by setting CH1 STATE CONTROL bit 4-6 in
STATE_CTRL Register (Address = 0x03) to '001'.

 - If the diagnostics completes without faults, the CH1 LDG RESULT bit in DC_LDG_RESULT Register
(Address = 0xC2) is set to 1. Once the system is ready to set the channel status to PLAY mode, no further
delay is introduced.

–
If a fault is detected during the diagnostic routine, the fault type can be determined by reading the results
stored in DC_LDG_REPORT Register (Address = 0xC0).


_**7.3.5.1.4 Short-to-Ground**_


The Short-to-Ground (S2G) tests triggers a fault condition if there is a conductive path from output pin OUT_M
or OUT_P of the tested channel to GND with an impedance below that specified in the Electrical Characteristics
section.


_**7.3.5.1.5 Short-to-Power**_


The Short-to-Power (S2P) tests triggers a fault condition if there is a conductive path from output pin OUT_M
or OUT_P of the tested channel to a power rail with an impedance below that specified in the Electrical
Characteristics section.


_**7.3.5.1.6 Shorted-Load and Open-Load**_


The Shorted-Load (SL) test triggers a fault condition if the conductive path between the OUT_M pin and OUT_P
pin of the tested channel (i) has an impedance below the threshold set in DC_LDG_SL_CTRL Register (Address
= 0xB3). The SL test has a configurable threshold depending on the expected load to be connected.


The Open-Load (OL) test triggers a fault condition if the conductive path between the OUT_M pin and OUT_P
pin of the tested channel has an impedance higher than that specified in the Electrical Characteristics section.


OL Maximum







OL Minimum


SL Maximum


SL Minimum









|Open Load|Open Load Detected|
|---|---|
|Open Load (OL)<br>Detection Threshold|Normal or Open Load<br>May Be Detected|
|Normal Load|Play Mode|
|Shorted Load (SL)<br>Detection Threshold|Normal or Shorted Load<br>May Be Detected|
|Shorted Load|Shorted Load Detected|


**Figure 7-26. DC Load Diagnostic Reporting Thresholds**


**7.3.5.2 Line Output Diagnostics**


The device also includes an optional test to detect a line output load (LO). A line output load is a high-impedance
load that is above the open load (OL) threshold such that the DC-load diagnostics report an OL condition. If the
line output detection bit is set high, when an OL condition is detected during the DC Diagnostic test, the system
will also test if a line output load is present. The DC_LDG_LO_CTRL Register (Address = 0xB1) can be used to
configure the channel to be tested for a line output load. If the channel is configured to test for a line output load
the channel should be muted.


After the line output diagnostics runs the status is reported in the DC_LDG_RESULT Register (Address = 0xC2).


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 45


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**7.3.5.3 AC Load Diagnostics**


The AC load diagnostic is used to determine the proper connection of a capacitive coupled speaker or tweeter
when used with a passive crossover. The AC load diagnostic is controlled through I [2] C. The TAS6511-Q1
provides a required signal source to determine the AC impedance and reports the tweeter detection result back
to I [2] C registers. The I [2] C selected test frequency creates a current flow through the desired speaker for proper
detection. AC Load Diagnostics can operate without the TDM/I [2] S clocks being present.


**Note**


If a fault occurs during AC diagnostics, the AC diagnostics is stopped. AC Diagnostics is not allowed
to be performed again until the DC Diagnostics are performed. This is to make sure the fault is not a
potential hazard during AC diagnostics.


_**7.3.5.3.1 Operating Principal**_


The AC Load Diagnostic circuit of TAS6511-Q1 provides an internally generated stimulus to the load; captures
the response of the load; provides real and imaginary parts of the captured complex load impedance; and offers
a magnitude estimator and tweeter detection comparator.


_**7.3.5.3.2 Stimulus**_


The frequency of the stimulus is set in AC_LDG_FREQ_CTRL Register (Address = 0xB8). The device drives a
low level, 10 mA output current through the load which does not create any significant sound pressure levels
from the speaker.


For load impedances below 8 Ω it is recommended to the set the AC DIAG GAIN bit to '1' in AC_LDG_CTRL
Register (Address = 0xB5) to increase the reported result resolution.


_**7.3.5.3.3 Load Impedance**_


The load impedance as seen by the device is simply the ratio of the voltage across the output pins and the
current flowing through the load.


Typically the load has a frequency dependent magnitude and causes current and voltage to have a phase
shift. The TAS6511-Q1 internally captures the load impedance as a complex value consisting of a real and
imaginary part. Expressing a load impedance in magnitude and phase or in real and imaginary part is
mathematically equivalent. Both forms can be transformed into each other without loss of information. After
AC load diagnostics have finished, the real and imaginary parts of the complex impedance are available in
the AC_LDG_REPORT_CH1_R Register (Address = 0xC3) and AC_LDG_REPORT_CH1_I Register (Address =
0xC4).


_**7.3.5.3.4 Tweeter Detection**_


In most cases, it is sufficient to use the TAS6511-Q1 built-in magnitude estimator and tweeter detection report
to perform the desired tweeter detection test. If a tweeter is properly connected in the system, the magnitude
of the load impedance is close to the nominal impedance of the speaker, for example 4 Ω. Once AC load
diagnostics finished, the magnitude of the load impedance is calculated and compared against a threshold set
in TWEETER_DETECT_THRESH Register (Address = 0xB7). If the measured impedance is lower than the
set threshold, the tweeter is detected and marked accordingly in the TWEETER_REPORT Register (Address =
0xCB).


_**7.3.5.3.5 Operation**_


To perform AC load diagnostics on TAS6511-Q1:

 - Use the State Control Register (STATE_CTRL Register (Address = 0x03) to put the channel into SLEEP
state.

 - Start the AC diagnostics by marking the channel in the AC_LDG_CTRL Register (Address = 0xB5).

 - Poll the channel state from STATE_REPORT Register (Address = 0x72). Once CH1 STATUS returns to
'SLEEP' the AC load diagnostics results are ready to be read.


46 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**7.3.5.4 DC Resistance Measurement**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



The TAS6511-Q1 supports a DC Resistance Measurement of the loads connected to each channel that can be
read back to the system processor via I [2] C. To read out the DC resistance of the load connected to each channel,
DC load diagnostics must be completed. After DC load diagnostics is completed, registers DC_LDG_DCR_MSB
Register (Address = 0xC5) and DC_LDG_DCR_LSB Register (Address = 0xC6) are updated and can be read.


**7.3.5.5 Real-Time Load Diagnostics**


Real-Time Load Diagnostics (RTLDG) allows the detection of shorted load (SL), open load (OL), Short-toPower (S2P) and Short-to-Ground (S2G) conditions during audio operation of the amplifier. To monitor the
load impedance while in PLAY state TAS6511-Q1 uses its integrated current sense to measure the output
impedance by channel and compare it with configurable thresholds. An internally generated pilot tone ensures
the continuous detection of the output impedance, regardless if an external audio input signal is present. The
configurable pilot tone is by default a 6 Hz, -36 dBFs signal.


Prerequisites to run Real-Time Load Diagnostics:


 - Sampling frequency of 16 kHz, 32 kHz, 48 kHz or 96 kHz. RTLDG is not supported at 192 kHz sampling
frequency

 - Current Sense is enabled


The detection of SL/OL and S2P/S2G events during RTLDG can be enabled/disabled individually and if desired,
run in parallel. For SL/OL detection the device will compare the measured output impedance at the pilot tone
frequency against user-configurable thresholds. S2P/S2G detection is performed by comparing the sensed DC
current of OUT_xP and OUT_xM against a user-configurable current threshold.

```
 w B0 00 00      / Page switching (first 00) to page 0 (2nd 00)
 w B0 7F 00      / Change to book 0
 ### Enable Current Sense and RTLDG detection ###
 w B0 05 08      / Enable Current Sense
 w B0 5B 08      / Enable Current Sense calibration
 w B0 4E 0C      / Adjust analog gain ramp down time
 w B0 37 08      / Enable RTLDG OL/SL detection
 w B0 38 08      / Enable RTLDG S2P/S2G detection
 ### Enable Pilot Tone & Set Threshold ###
 w B0 00 00      / Page switching (first 00) to page 0 (2nd 00)
 w B0 7F 8C      / Change to book 8C. It's required to be in page 0 before changing a book
 w B0 00 22      / Go to page 22 in book 8C
 w B0 C8 00 3E BB 7E  / Pilot tone ramp down speed
 w B0 88 00 10 68 00  / Write to offset 88, 24-bit wide, set Open load threshold e.g. ~14ohm
 w B0 8C 00 01 E0 00  / Write to offset 8C, 24-bit wide, set Short load threshold e.g. ~1ohm
 w B0 00 00      / Return to page 0 of book 8C
 w B0 7F 00      / Return to book 0, page 0

```

Output clipping as well as current limiting events impact the result reporting accuracy and it is recommended
to avoid or prevent them during RTLDG operation. If Clip Detect is enabled, RTLDG results will not be updated
if Clipping occurs and is detected by the device during an update cycle. The results will be refreshed after the
next update cycle without Clipping. Note: To operate Clip Detect and RTLDG in parallel, the Clip Detect related
configuration must be completed before enabling RTLDG.


Shorted Load and Open Load register flags are reported to RTLDG_OL_SL_FAULT_LATCHED
Register (Address = 0x8B). Short-to-Power and Short-to-Ground register flags are reported to
RTLDG_S2G_S2P_FAULT_LATCHED Register (Address = 0x8C). These signals can optionally be routed
directly to I/O pins as either Fault Events or Warning Events. Refer to REPORT_ROUTING_5 Register (Address
= 0x94).


If the channel encounters an SL, OL, S2P or S2G threshold violation the channel will stop switching and move
into FAULT state. The CLEAR FAULT bit in RESET Register (Address = 0x01) must be set to '1' before the
channel can restart.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 47


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


_**7.3.6 Protection and Monitoring**_


**7.3.6.1 Overcurrent Limit (Cycle-By-Cycle)**


Under normal operation, during high level music playback, it is possible that dynamic load currents can rise
beyond the maximum load current, I LIM, of the device. In these cases, the device dynamically limits the current
into the load and operation continues without disruption and prevents undesired shutdown for transient music
events.


The channel is monitored and limited. For each of the four over current (OC) levels that can be set in
CURRENT_LIMIT_CTRL Register (Address = 0x55), there is a corresponding I LIM as shown in the Electrical
Characteristics.


If the load current limit is active for at least 25% of a 21.3 ms window, the device generates an Overcurrent Limit
Warning Even for the affected channel.


In case the load current warning event is active continuously for 170.4 ms the device generates an Overcurrent
Limit Fault Event and the channel is placed in the FAULT State. This puts the output stage in high impedance.


**Note**


If using 1.8V DVDD and driving a 2Ω load with PVDD >16V, Cycle-By-Cycle current limit should be
disabled.


**7.3.6.2 Overcurrent Shutdown**


If the output load current reaches I SD, such as during an output short to GND, then an Overcurrent Shutdown
(OCSD) event occurs, limiting the peak current and shutting down the affected channel. The time to shutdown
the channel varies depending on the severity of the short condition.


The channel is placed into the FAULT state with the output stage in Hi-Z.


Based on the configuration, a fault signal is generated, which by default generates an active low signal at the
FAULT pin.


The overcurrent limit is programmable to 4 levels and can be set in bit 0-1 of the CURRENT_LIMIT_CTRL
Register (Address = 0x55).


**7.3.6.3 Current Sense**


TAS6511-Q1 can measure the output current of the channel. This functionality is completely integrated and
requires no external components.


The channel output current measurement is performed at the rate of the sampling frequency F s . The measured
current amplitude is provided through SDOUT. For more details on the data transmission configuration see
SDOUT. Note that the current measurement and the data transmission are two separate functions and both
require proper setup before the data can be made available.


The current sense feature is disabled by default and can be enabled in ISENSE_CTRL Register (Address =
0x05).


**7.3.6.4 SpeakerGuard Pro Power Limiter**


The SpeakerGuard Pro power limiter limits the peak output voltage of the amplifier to prevent speakers from
exceeding the specified power rating. If the input signal exceeds the configured peak voltage threshold the
Speaker Guard clips the signal at the configured threshold to avoid potentially damaging the speaker. Once
the voltage limit is reached the device automatically reduces the gain at the configured attack rate until the
signal is within the voltage limit. Once the signal is within the voltage limit the device then releases the gain at
the configured release rate. The voltage limit threshold, attack rate, release rate, and max attenuation can is
configured in the DSP memory. Figure 7-27 shows the behavior of the Speaker Guard when limiting the output
voltage level.


48 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Speaker Guard is disabled by default and can be enabled by setting bit 6 in the
DC_BLOCK_SPEAKER_GUARD_EN Register (Address = 0x39).





No power
limi � ng


Signal with
Speaker Guard
Power Limi � ng


Power Limit

Threshold

|SpeakerGuard Pro A �ack Rate|SpeakerGuard Pro|
|---|---|
|r<br> <br>imit<br>old<br><br>Gain<br><br>|Release Rate|
|r<br> <br>imit<br>old<br><br>Gain<br><br>||
|r<br> <br>imit<br>old<br><br>Gain<br><br>||



**7.3.6.5 DC Detect**



Gain



**Figure 7-27. SpeakerGuard Pro-Power Limiter Example**



This circuit measures the DC offset continuously at the output of the amplifier during normal operation. If the DC
offset exceeds the DC FAULT threshold, that channel triggers a DC Fault Event and is placed in the FAULT state
and the output stage is set to high impedance.


Based on the configuration, a fault signal is generated, which by default generates an active low signal at the
FAULT Pin.


**7.3.6.6 Clip Detect**


The TAS6511-Q1 supports a configurable clip detection monitor. The DSP monitors the audio signal of the
channel and compares the magnitude of the audio signal at the input to the interpolation filters to a configurable
threshold.


Clip Detect is disabled default. Clip Detect can be enabled through bit 6 in the CLIP_DETECT_CTRL Register
(Address = 0x93)


Report registers:

 - Unlatched/Status: CLIP_WARN_STATUS Register (Address = 0x83)

 - Latched/Memory: CLIP_WARN_LATCHED Register (Address = 0x89). The latched error report clears on
read.


If configured accordingly in REPORT_ROUTING_5 Register (Address = 0x94) bit 1, the Clip Detect status can
be routed as a Warning signal.


**7.3.6.7 Temperature Protection and Monitoring**


The device monitors temperature using an integrated temperature sensor to monitor the output stage of the
channel. Based on the temperature sensor, warning and fault signals can be generated. A Thermal Gain
Foldback scheme is available that autonomously regulates audio gain and consequently limits die temperature.


The temperature of the temperature sensor is reported through an 8-bit ADC at a sampling rate of 48 kHz to
TEMP_SENSOR Register (Address = 0x75) and read through I [2] C.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 49


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**





**Figure 7-28. Abstract Temperature Sensor Locations Within the Device**


_**7.3.6.7.1 Overtemperature Shutdown**_


The temperature thresholds for OTSD is set to fixed values. Refer to Electrical Characteristics for the nominal
temperature and recovery hysteresis values.


**OTSD** : If the junction temperature rises above the OTSD threshold, the channel is placed into a protective
shutdown state and an Overtemperature Shutdown (OTSD) Event is created.

 If over-temperature auto-recovery is enabled in bit 1 of OTSD_RECOVERY_EN Register (Address = 0x8F),
the channel is put into Auto Recovery (AUTOREC) State and recover the state the channel was in before
OTSD occurred once the temperature has cooled down below respective threshold and the recovery
hysteresis.

 If over-temperature auto-recovery is disabled in bit 1 of OTSD_RECOVERY_EN Register (Address = 0x8F),
the channel is put into a FAULT state. The channel only recovers after setting the CLEAR FAULT bit in
RESET Register (Address = 0x1). This clears the faults and the channel return to the previous state.


The tolerance of the warning levels and OTSD temperatures track each other.


By default, a fault signal generates an active low signal on the FAULT Pin when an OTSD event occurs.


_**7.3.6.7.2 Overtemperature Warning**_


The temperature threshold for Overtemperature Warning (OTW) can be configured to 7 difference levels through
bit 0-2 of OTW_LEVEL Register (Address = 0x56).


During operation, if the device heats up and crosses the threshold, a Overtemperature Warning Event is
generated. While the device continues to operate, the OTW information enables higher level software to make
decisions to optimize thermal system performance.


As described in the Overtemperature Warning Event, the report can either be polled via I [2] C register or a
hardware signal can be generated by assigning a GPIO Pin for Warning Signals and enabling the OTW report
routing.


_**7.3.6.7.3 Thermal Gain Foldback**_


Thermal Gain Foldback (TGFB) is a power limiting feature to protect the TAS6511-Q1 from excessive die
temperature while maintaining audio output. Thermal foldback is disabled by default and can be enabled in bit 0
of FOLDBACK_EN Register (Address = 0x3A).


The main purpose of foldback power limiting is to keep the output stage within its safe power dissipation limit
to avoid unexpected Overtemperature Shutdown. The feature provides a smooth audio response and allows
for uninterrupted music playback when temperature limits are crossed. That means the TAS6511-Q1 does not
simply shut down, but continues to operate with considerable music output power while avoiding the trigger of
OTSD.


The DSP of TAS6511-Q1 monitors the die temperature continuously in real-time for safe operation. The device
can warn the host if the die temperature is approaching the (OTW) limits. TAS6511-Q1 still functions until the
temperature reaches the OTSD threshold, at which the amplifier is shut down.


When the temperature decreases below the foldback level, the attenuation will be held for a configurable number
of samples before the attenuation will begin releasing at the gain step rate of 0.1 dB per sample. This release
rate of the TGFB can be programmed in the DSP memory.


50 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


input signal


output signal


**7.3.6.8 Power Failures**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025


attack time


**Figure 7-29. Thermal Foldback Attack and Release**



The PVDD power supply is monitored for undervoltage and overvoltage events as described in the Power Fault
Events section. This automatically engages shutdown and protects the device. PVDD safe operating voltage
ranges can be found in the Recommended Operating Conditions table.


The device will shut down if the DVDD supply falls below V POR_OFF . The DVDD POR fault event is described in
the Power Fault Events section.


_**7.3.7 Hardware Control Pins**_


**7.3.7.1 PD Pin**


The PD pin is active low. When asserted the device goes into shutdown and the current draw is limited to a
minimum. During shut down, all internal blocks are powered off and registers initialize to their default values
during the next start-up. I [2] C is not active.


This pin has a 110 kΩ internal pull-down resistor.


**7.3.7.2 GPIO Pins**


TAS6511-Q1 offers two configurable GPIO pins. The GPIO pins can be configured as input or outputs. The
pins must be configured through I [2] C before becoming operational after Device Initialization and Power-On-Reset
(POR). By default GPIO_1 functions as an input pin and GPIO_2 functions as a FAULT pin. This can be
controlled individually for each pin through bit 6-7 of GPIO_CTRL Register (Address = 0xA0).


_**7.3.7.2.1 FAULT Pin**_


By default a GPIO pin is configured as a FAULT pin. The FAULT pin reports fault events and is active low under
any of the following conditions:

 - Overtemperature shutdown (OTSD) - Latching and non-latching

 - Overcurrent Limit and Shutdown events - Latching

 - DC Detect - Latching


Register bits are available to mask fault categories from reporting to the FAULT pin. These bits only mask the
setting of the pin and do not affect the register reporting or protection of the device. Additional fault events can
be assigned to be reported by the FAULT pin. These include:

 - Power Faults - Latching and non-latching

 - DC Load Diagnostic faults

 - Real-time Load Diagnostic reports - Latching and non-latching

 - Clock Errors - Latching and non-latching

 - Warning events


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 51


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


The related configurations are located in REPORT_ROUTING_2 Register (Address = 0x90),
REPORT_ROUTING_4 Register (Address = 0x92) and REPORT_ROUTING_5 Register (Address = 0x94).


This pin is an open-drain output with an internal 110 kΩ pull-up resistor to DVDD.


_**7.3.7.2.2 General Purpose Input**_


A General Purpose Input (GPI) pin can be configured by assigning a function to the pin through I [2] C in the related
register.


See Table 7-5 for an overview of all available input functions and the associated register in which they can be
configured.


For a GPIO pin to operate as input, the relevant register bit in GPIO_CTRL Register (Address = 0xA0) must be
set to input configuration.


**Table 7-5. General Purpose Input functional overview**







|Function|Description|Register Name and Address|
|---|---|---|
|Hi-Z|The state of the channel is set toHi-Z state|Bit 0-2 ofGPIO_INPUT_SLEEP_HIZ Register (Address = 0x9B)|
|DEEP SLEEP|The state of the channel is set toDEEP<br>SLEEP state|Bit 4-6 ofGPIO_INPUT_SLEEP_HIZ Register (Address = 0x9B)|
|SLEEP|The state of the channel is set toSLEEP<br>state|Bit 0-2 ofGPIO_INPUT_PLAY_SLEEP Register (Address = 0x9C)|
|PLAY|The state of the channel is set toPLAY<br>state|Bit 4-6 ofGPIO_INPUT_PLAY_SLEEP Register (Address = 0x9C)|
|~~MUTE~~|Mutes the device output (active low)|Bit 0-2 ofGPIO_INPUT_MUTE Register (Address = 0x9D)|
|Phase Sync|Input to sync phase with another device<br>(recipient)|Bit 0-2 ofGPIO_INPUT_SYNC Register (Address = 0x9E)|


_**7.3.7.2.3 General Purpose Output**_


A General Purpose Output (GPO) pin can be configured by writing the value of the intended output function
to the GPO pin configuration register through I [2] C. Table 7-6 lists the GPO configuration register address for all
GPIO pins.


See Table 7-7 for an overview of all available output functions and the associated register value which
determines the selected GPIO function.


In order for a GPIO pin to operate as output, the relevant register bit in GPIO_CTRL Register (Address = 0xA0)
must be set to output configuration.


**Table 7-6. General Purpose Output Configuration Register**

|GPIO Pin|GPO Configuration Register|
|---|---|
|GPIO_1|GPIO1_OUTPUT_SELECT Register (Address = 0x95)|
|GPIO_2|GPIO2_OUTPUT_SELECT Register (Address = 0x96)|



**Table 7-7. General Purpose Output Functional Overview**

|Function|Mode|Description - Match table with regmap|Register value|
|---|---|---|---|
|Low|Output Buffer|Pin continuously drives logic low output|0x00|
|Auto Mute|Open Drain|Active in response toAuto Mute on channel 1|0x06|
|SDOUT|Output Buffer|I2S / TDM data output|0x09|
|~~WARN~~|Open Drain|Active in response toWarning Events|0x0A|
|~~FAULT~~|Open Drain|Active in response toFault Events|0x0B|
|Clock Sync|Output Buffer|Output for clock sync with another device (for example, DCDC) as<br>Primary|0x0E|
|Invalid Clock|Output Buffer|Active in response to aInvalid Clock Fault Event, Clock missing or Clock<br>change|0x0F|
|High|Output Buffer|Pin continuously drives logic high output.|0x13|



52 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025


**Table 7-7. General Purpose Output Functional Overview (continued)**



|Function|Mode|Description - Match table with regmap|Register value|
|---|---|---|---|
|**All register values that are not listed in this table are RESERVED**|**All register values that are not listed in this table are RESERVED**|**All register values that are not listed in this table are RESERVED**|**All register values that are not listed in this table are RESERVED**|


GPO pin signals can be inverted by setting the relevant bit in GPIO_INVERT Register (Address = 0xA1) to 1.


_**7.3.7.2.4 STBY Pin**_


Any of the GPIO pins can be configured to function as an active low STBY pin by configuring a GPIO pin to set
the device into DEEP SLEEP state in bit 4-6 of GPIO_INPUT_SLEEP_HIZ Register (Address = 0x9B). When
asserted it sets the device into DEEP SLEEP state. In this mode the device has a reduced current while the
output pins are placed into a Hi-Z state. All internal analog bias are disabled. In DEEP SLEEP and while DVDD
is present, the I [2] C bus is active and the internal registers are active.


This pin has a 110 kΩ internal pull-down resistor.


_**7.3.7.2.5 Advanced GPIO functions**_


_**7.3.7.2.5.1 Clock Synchronization**_


TAS6511-Q1 supports multiple options for clock synchronization to improve system EMI behavior and control
supply peak current conditions.


_**7.3.7.2.5.1.1 External SYNC signal (GPIO sync)**_


Multiple TAS6511-Q1 synchronize clocks by using an externally provided sync signal.





|Col1|GPIO_x<br>TAS65xx-Q1|
|---|---|
|||


|Col1|GPIO_x<br>TAS65xx-Q1|
|---|---|
|||


.

.

.


|Sync<br>Source|Col2|Col3|
|---|---|---|
|Sync<br>Source|||
|Sync<br>Source|||


|Col1|.|
|---|---|
||GPIO_x<br>TAS65xx-Q1|
|||
|||



**Figure 7-30. External SYNC signal architecture**


Setup:
1. Set one GPIO pin to “Phase Sync" input. The selected GPIO sync pins of all applicable devices should be
connected together
2. In the PWM_PHASE_CTRL Register (Address = 0x60)
a. Set the PWM PHASE SYNC ENABLE bit 0 ito “1” to enable phase sync function
b. Set the PWM PHASE SYNC SELECT bit 1 to “0” to enable GPIO sync


3. Select the output phase settings for each device and its respective channels

   - Manual phase mode can optionally be used to select preferable output channel phase offsets across all
channels in the systems. More details can be found in High-Frequency Pulse-Width Modulator (PWM)
4. Set all channels on each synchronized device to Hi-Z state
5. Toggle the GPIO Sync source as shown in the Figure 7-31
6. Set the channel to PLAY state. It can take up to 3F sw switching cycles before the devices are switching
synchronized.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 53


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


tRise < 20ns


GPIO Sync Source


**Figure 7-31. GPIO Sync source signal**


**Note**
Spread Spectrum acts synchronized between all TAS6511-Q1 when configured with the same settings
on each device.


_**7.3.7.2.5.1.2 Synchronization through the audio serial clock (SCLK)**_


Multiple TAS6511-Q1 synchronize their clocks through the Audio Serial Clock (SCLK).





|Col1|SCLK<br>TAS65xx-Q1|
|---|---|
|||


|Col1|SCLK<br>TAS65xx-Q1|
|---|---|
|||


.

.

.


|I2S / TDM<br>Audio Input<br>Serial Clock|Col2|Col3|
|---|---|---|
|I2S / TDM<br>Audio Input<br>Serial Clock|||
|I2S / TDM<br>Audio Input<br>Serial Clock|||


|Col1|.|
|---|---|
||SCLK<br>TAS65xx-Q1|
|||
|||



**Figure 7-32. Audio serial clock (SCLK) Synchronization architecture**


Setup:
1. Halt the Audio input Serial clock (SCLK). The I [2] C communication remains enabled
2. In register PWM_PHASE_CTRL Register (Address = 0x60)
a. Set the PWM PHASE SYNC ENABLE bit 0 ito “1” to enable phase sync function
b. Set the PWM PHASE SYNC SELECT bit 1 to “1” to enable internal sync


3. Select the output phase settings for each device and its respective channels

   - Manual phase mode can optionally be used to select preferable output channel phase offsets across all
channels in the systems. More details can be found in High-Frequency Pulse-Width Modulator (PWM)
4. Set all channels on each synchronized device to Hi-Z state
5. Provide the Audio input Serial clock (SCLK) and wait a minimum of 2ms before proceeding to the next step
6. Set each channel to PLAY state


**Note**


There can be up to 1 SCLK cycle offset between the devices.


Spread Spectrum will act synchronized between all TAS6511-Q1 when configured with the same
settings on each device.


_**7.3.7.2.5.1.3 TAS6511-Q1 as clock source for external devices**_


This synchronization option allows the TAS6511-Q1 to share its clock with external system components such
as a DC-DC regulator. In this mode the device shares its internal ramp clock through the selected GPIO pin. If


54 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Spread Spectrum is enabled, this clock output will be affected and share the spread signal frequency with the
connected component. Refer to the technical documentation of the connected system components to ensure
correct sequencing for clock synchronization and avoiding unexpected system behavior.









.

.

.

.


|TAS65xx-Q1<br>(Primary)|GPIO_x|Col3|
|---|---|---|
|TAS65xx-Q1<br>(Primary)|GPIO_x||
|TAS65xx-Q1<br>(Primary)|GPIO_x||





**Figure 7-33. Clock source for external devices architecture**


Setup:
1. Select a TAS6511-Q1 to operate as Primary Clock. On this device, configure a GPIO pin as “Clock Sync”
output. Connect this pin to the clock input of all Clock secondary devices
2. In register PWM_PHASE_CTRL Register (Address = 0x60) set the PWM PHASE SYNC ENABLE bit 0 to “1”
to enable phase sync function

   - By default the GPO Clock Sync operates at the selected device output switching frequency. If the sync
should occur at a different frequency, a divider can be set before enabling the Clock sync output in
SS_CTRL Register (Address = 0x61), bit 6-7
3. The Clock Sync will ramp at a phase offset of 0 degrees in relation to the output channels. A different
phase offset can be configured in RAMP_PHASE_CTRL_GPO Register (Address = 0x68). This setting is
only available when manual phase mode is enabled in bit 7 of PWM_PHASE_CTRL Register (Address =
0x60)
4. Set the channel on each synchronized device to Hi-Z state
5. Set the channel to PLAY state


**Note**
If Spread Spectrum is enabled, it will be reflected on the SYNC signal. This mode cannot be used to
synchronize multiple TAS6511-Q1 with each other.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 55


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**8 Device Functional Modes**


**8.1 Internal Reporting Signals**


To support software driver development, the TAS6511-Q1 allows the flexible configuration of internal fault and
warning signals. These signals, where applicable, can be configured based on current device status registers or
events stored in memory registers. These signals can be configured and routed to the available GPIO pins for
signaling purposes.


_**8.1.1 Fault Signal**_


Automotive systems have a high demand on gathering device information in case of unexpected conditions. The
registers REPORT_ROUTING_2 Register (Address = 0x90), REPORT_ROUTING_4 Register (Address = 0x92)
and REPORT_ROUTING_5 Register (Address = 0x94) of the TAS6511-Q1 allow for a flexible configuration of
fault information necessary for higher level system software to effectively control the system.


The Fault Signal can be configured to be active in response to the following Fault Events:


 - Power Fault (latched or non-latched)

 - Overtemperature Shutdown (latched or non-latched)

 - DC Load Diagnostic events

 - Overcurrent limiting and shutdown (latched)

 - DC Detect (latched)

 - Channels entering the FAULT state

 - Real-Time Load Diagnostics faults (latched)

 - Clock error (latched or non-latched)


The Fault Signal, by default, gets routed to the FAULT Pin to create a HW signal. The Fault Signal can optionally
be routed to an additional GPIO pin.


There are two report bits for Fault signals:


 - GLOBAL FAULT (POWER_FAULT_STATUS Register (Address = 0x80), bit 6) - Reports any active fault in
device, regardless of fault signal configuration

 - FAULT SIGNAL (OT_FAULT Register (Address = 0x81), bit 6) - Reports active fault signals that are
configured accordingly in the fault signal configuration registers


_**8.1.2 Warning Signal**_


REPORT_ROUTING_3 Register (Address = 0x91), REPORT_ROUTING_4 Register (Address = 0x92), and
REPORT_ROUTING_5 Register (Address = 0x94) of the TAS6511-Q1 allow for a flexible configuration of
warning information necessary for higher level system software to effectively control the system.


The Warning Signal can be configured to be active in response to the following Warning Events:


 - Power Fault (latched or non-latched)

 - Overtemperature Shutdown (latched or non-latched)

 - Overtemperature Warning (latched or non-latched)

 - DC Load Diagnostic events

 - Overcurrent limiting (latched or non-latched)

 - Clip Detect (latched or non-latched)

 - Real-Time Load Diagnostics faults (latched)

 - Clock error (latched or non-latched)

 - Thermal foldback (latched or non-latched)

 - PVDD foldback (latched or non-latched)


The Warning Signal is by default not routed to a pin. TAS6511-Q1 can be configured to route warning signals
to GPIO pins to create a HW signal. Alternatively, all active Warning signals can be routed to the FAULT pin by
setting bit 0 in register REPORT_ROUTING_4 Register (Address = 0x92) to '1'.


56 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025




 - GLOBAL WARNING (POWER_FAULT_STATUS Register (Address = 0x80), bit 7) - Reports any active
warning in device, regardless of warning signal configuration with the exception of Clock Fault events.

 - WARNING SIGNAL (OT_FAULT Register (Address = 0x81), bit 7) - Reports active warning signals that are
configured accordingly in the warning signal configuration registers


**8.2 Device States and Flags**


_**8.2.1 Audio Channel States**_


The audio channel has a set of states that carefully control the set up and shut down procedure of an audio
path from source to load. These states are listed in Table 8-1. The current channel states are reported in
STATE_REPORT Register (Address = 0x72).


After the PD, is pulled high, the states can be selected by setting the CH1 STATE CONTROL bits in the
STATE_CTRL Register (Address = 0x03) or by using GPIO control if a GPIO pins is configured as a STBY Pin.


**Table 8-1. Audio Channel States**

|STATE NAME|OUTPUT FETS|DSP|OSCILLATOR|I2C|
|---|---|---|---|---|
|SHUTDOWN|Hi-Z|Stopped|Stopped|High impedance|
|DEEP SLEEP|Hi-Z|Stopped|Active|Active|
|LOAD DIAG|Hi-Z|Stopped|Active|Active|
|SLEEP|Hi-Z|Stopped|Active|Active|
|HI-Z|Hi-Z|Active|Active|Active|
|PLAY|Switching with audio|Active|Active|Active|
|FAULT|Hi-Z|Stopped|Active|Active|
|AUTOREC|Hi-Z|Stopped|Active|Active|



**8.2.1.1 SHUTDOWN State**


The device remains in shutdown when the PD pin is pulled low. All internal regulators are disabled for minimal
power consumption.


Releasing the PD pin starts the device and resets all registers to their default value.


**8.2.1.2 DEEP SLEEP State**


DEEP SLEEP puts the device in a standby state. In DEEP SLEEP, the I [2] C communication and registers as well
as the 1.5V LDO for the digital core are active. All other regulators remain deactivated to save energy.


This state is an excellent choice to configure the device through I [2] C before powering up. Unlike SHUTDOWN
state, entering or exiting DEEP SLEEP state maintains the register map and DSP memory.


**Note**

The DSP is deactivated in DEEP SLEEP.


DEEP SLEEP can be controlled through a GPIO pin (if configured to STBY) and I [2] C control in the state control
registers. Pin control supersedes I [2] C control. When the STBY pin is pulled high, the channel needs to enter this
state through I [2] C control in registers STATE_CTRL Register (Address = 0x03) for DEEP SLEEP to take effect.


By default, when leaving DEEP SLEEP state and under the condition that all power supplies are within the
recommended operating range, the device transitions into SLEEP state and automatically starts DC load
diagnostics. This load diagnostic can be bypassed by setting DC LDG BYPASS bit 0 and can be aborted through
LDG ABORT bit 7 in DC_LDG_CTRL Register (Address = 0xB0) and transition the device directly to SLEEP
state.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 57


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**8.2.1.3 LOAD DIAG State**


Diagnostic mode engages the DC Diagnostic circuitry to test for Short to Power, Short to Ground, Shorted Load
and Open Load without activating the output power stage. These tests must be completed without fault before
the Output FETs can be activated. For a more detailed description see DC Load Diagnostics.


The DC diagnostics are available as soon as the device supplies are within the Recommended Operating
Conditions. The DC diagnostics do not rely on external audio input signals or clock and sync frequencies to
be available. DC Diagnostic results are reported for the channel through the I [2] C registers DC LDG Rprt CH1
Register (Address = 0xC0).


The channel transitions to SLEEP state mode after successfully passing the diagnostic tests.


**8.2.1.4 SLEEP State**


SLEEP state activates further functional blocks in comparison to the DEEP SLEEP state, including the internal
LDO for analog circuitry and gate driver. The supply for the Digital-to-PWM conversion remains deactivated.


The channel transitions to Hi-Z state by setting the State Control register to either Hi-Z or PLAY under the
condition that no clock error is present.


**8.2.1.5 Hi-Z State**


In Hi-Z state the output driver is set to a high impedance state while all other blocks are fully functional.


The channel transitions to Section 8.2.1.6 by setting the State Control register to PLAY.


**8.2.1.6 PLAY State**


In PLAY state the device is fully operational. The output stages are active, switching and amplify the input signal.


In PLAY state, MUTE can be activated through the MUTE bit in the respective State Control Register
(STATE_CTRL Register (Address = 0x03) or a GPIO pin, if configured accordingly. The transition between
MUTE and PLAY is gradual and the volume ramp can be configured in DIG_VOL_RAMP_CTRL Register
(Address = 0x44).


Real-Time Load Diagnostics can be activated to monitor the connected load for shorts or open conditions.


**8.2.1.7 FAULT State**


FAULT state is a device-internally generated mode that cannot be manually set by the user.


If the channel of the device is in PLAY state and encounter a fault, the device may need to take protective
actions and shutdown the audio channel. The output FETs of the affected channel are turned off and the output
pins become high impedance. The reported state for the affected channel is 'FAULT'.


Possible reasons for the channel to enter this state are:

 - Overcurrent Shutdown

 - Load Current fault

 - DC fault

 - Real-Time Load Diagnostic fault

 - Channel over temperature shutdown, if configured to no auto-recovery


The following registers hold all information necessary to identify the reason for the device being in this state:

 - OT_FAULT Register (Address = 0x81)

 - CBC_FAULT_WARN_LATCHED Register (Address = 0x8D)

 - OC_DC_FAULT_LATCHED Register (Address = 0x8E)

 - RTLDG_OL_SL_FAULT_LATCHED Register (Address = 0x8B)

 - RTLDG_S2G_S2P_FAULT_LATCHED Register (Address = 0x8C)


58 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025


**Note**



If the channel is in FAULT State, the channel faults only recover after setting the CLEAR FAULT bit 3
in RESET Register (Address = 0x01).


This clears the faults and sets the affected channel into Hi-Z state.


**8.2.1.8 Auto Recovery (AUTOREC) State**


AUTOREC is a device-internally generated state that cannot be manually set by the user.


If the channel of the device are in PLAY state and encounter a fault, the device needs to take protective
actions and shutdown the audio channel. The output FETs of the affected channel are turned off and the output
pins become high impedance. Once the cause for the protective shutdown is no longer present, the device
auto-recovers and resumes back to PLAY. The reported state for the affected channel is 'AUTOREC'.


Possible reason for the channel to enter this state is:

 - Over temperature shutdown if configured to auto-recovery

 - Power failures

 - Clock Error


The following registers hold all information necessary to identify the reason for the device being in this state:

 - OT_FAULT Register (Address = 0x81)

 - POWER_FAULT_STATUS Register (Address = 0x80)

 - CLK_FAULT_LATCHED Register (Address = 0x8A)


_**8.2.2 Status and Memory Registers**_


**8.2.2.1 Status Registers**


The device reports device states and environmental information by means of status and reporting registers. The
following set of registers, at any time, hold the full set of device status:CH CBC Warn Status Register (Address =
0x85)

|Register and Address|Status Information|
|---|---|
|AUTO_MUTE_STATUS Register (Address = 0x71)|Auto Mute|
|STATE_REPORT Register (Address = 0x72)|Device Channel State Channel 1|
|POWER_FAULT_STATUS Register (Address = 0x80)|Power Faults, Global Fault, Global Warning|
|OT_FAULT Register (Address = 0x81)|Overtemperature shutdown, Fault Signal, Warning Signal|
|OTW_STATUS Register (Address = 0x82)|Temperature (OTW) Warning|
|CLIP_WARN_STATUS Register (Address = 0x83)|Clip Detect|
|CBC_WARNING_STATUS Register (Address = 0x85)|Overcurrent Limit Warning|
|DC_LDG_REPORT Register (Address = 0xC0)|DC Load Diagnostic Report CH1|
|DC_LDG_RESULT Register (Address = 0xC2)|DC Load Diagnostic Pass|
|TWEETER_REPORT Register (Address = 0xCB)|AC diagnostic tweeter detect|



Interrupt driven signaling to the controlling host device is supported by creation of events. Events can be
configured to create Warning Signal and Fault Signal.


Alternatively software can routinely read this set of registers to gather device status (polling mode).


**8.2.2.2 Memory Registers**


The device provides a set of memory registers which store latch events. This allows software drivers to properly
analyze fault situations.


The following set of memory registers is available:


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 59


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**

|Register and Address|Memory Information|
|---|---|
|POWER_FAULT_LATCHED Register (Address = 0x86)|Power Faults|
|OTSD_LATCHED Register (Address = 0x87)|Overtemperature shutdown|
|OTW_LATCHED Register (Address = 0x88)|Temperature (OTW) Warning|
|CLIP_WARN_LATCHED Register (Address = 0x89)|Clip Detect|
|CLK_FAULT_LATCHED Register (Address = 0x8A)|Clock Fault|
|RTLDG_OL_SL_FAULT_LATCHED Register (Address = 0x8B)|RTLDG Open Load and Shorted Load Faults|
|RTLDG_S2G_S2P_FAULT_LATCHED Register (Address = 0x8C)|RTLDG Short-to Power and Short-to-Ground Faults|
|CBC_FAULT_WARN_LATCHED Register (Address = 0x8D)|Overcurrent Limit Fault and Warning|
|OC_DC_FAULT_LATCHED Register (Address = 0x8E)|Overcurrent Shutdown and DC Fault|



**Note**
Memory registers only provide information to the controlling host. Reading the memory register clears
the content. The status of the device does not change by reading the memory registers.


**8.3 Fault Events**


_**8.3.1 Power Fault Events**_


Current status of power fault events is reported in POWER_FAULT_STATUS Register (Address = 0x80) and
latched events are reported in POWER_FAULT_LATCHED Register (Address = 0x86).


Power fault events are by default masked from pin reporting. This can be enabled. See FAULT pin for more
details.


**8.3.1.1 DVDD Power-On-Reset (POR)**


When DVDD falls below V POR_OFF, the device shuts down. The channel is set to SLEEP State, the DSP is
disabled and I [2] C communication terminates. When DVDD rises above V or when the device is first
POR_SET
powered and DVDD rises above V POR_SET the device initiates a Power-On-Reset routine. During this routine all
registers and device states are set to default values.


The intended behavior is that POWER_FAULT_LATCHED Register (Address = 0x86), bit 7 reports "DVDD
power on reset event stored" after power up. As DVDD POR is a transient event and is not reported in the Power
Fault Status register.


**8.3.1.2 DVDD Undervoltage Fault**


The DVDD undervoltage (UV) protection detects low voltages on the DVDD pin. In the event of a UV condition,
the device moves the channel from PLAY/HI-Z to Auto Recovery (AUTOREC) state, disable the DSP, and update
the I [2] C report registers.


Report registers:

 - Unlatched: POWER_FAULT_STATUS Register (Address = 0x80), bit 4

 - Latched: POWER_FAULT_LATCHED Register (Address = 0x86), bit 4


**Note**


POWER_FAULT_LATCHED Register (Address = 0x86), bit 4, can only be read one time while the
device remains in the fault state. Once read, the bit is cleared and not reset until the device completes
a successful startup and a new DVDD undervoltage condition occurs.


**8.3.1.3 PVDD Overvoltage Fault**


When the PVDD supply rail rises above nominal range, a PVDD Overvoltage Fault event is created and the
device enters into Auto Recovery (AUTOREC) State. Once PVDD falls back down into nominal range, the fault
event is cleared.


60 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Report registers:

 - Unlatched: POWER_FAULT_STATUS Register (Address = 0x80), bit 3

 - Latched: POWER_FAULT_LATCHED Register (Address = 0x86), bit 3


**8.3.1.4 PVDD Undervoltage Fault**


When the PVDD supply rail falls below nominal range, a PVDD Underoltage Fault event is created and the
device enters into Auto Recovery (AUTOREC) state. Once PVDD rises back up into nominal range, the fault
event is cleared.


Report registers:

 - Unlatched: POWER_FAULT_STATUS Register (Address = 0x80), bit 1

 - Latched: POWER_FAULT_LATCHED Register (Address = 0x86), bit 1


_**8.3.2 Overtemperature Shutdown (OTSD) Event**_


Section Overtemperature Shutdown describes the circumstances under which the device creates an OTSD
event as well as the configurable recovery behavior.


Report registers for Overtemperature Shutdown (OTSD) events:

 - Unlatched: OT_FAULT Register (Address = 0x81), bit 4

 - Latched: OTSD_LATCHED Register (Address = 0x87), bit 4


_**8.3.3 Overcurrent Limit Fault Event**_


Section Overcurrent Limit (Cycle-By-Cycle) describes the circumstances under which the device creates an
Overcurrent Limit Fault event. This is a transient event that only lasts for a limited time.


Report register:

 - Latched: CBC_FAULT_WARN_LATCHED Register (Address = 0x8D), bit 3


_**8.3.4 Overcurrent Shutdown Event**_


The Overcurrent protection section describes the circumstances under which the device creates an OCSD
event.


As Overrcurrent Shutdown (OCSD) Event is a transient event it is not reported in a status register. The latched
OCSD events are reported in Channel Overcurrent and DC Detection Fault Memory Register. The channel is
then placed into a FAULT State.


Report register:

 - Latched: OC_DC_FAULT_LATCHED Register (Address = 0x8E), bit 7


_**8.3.5 DC Fault Event**_


The DC Detect section describes the circumstances under which the device creates an DC Fault event.


As DC Fault Event is a transient event and is not reported in a status register. The latched DC Fault events are
reported in Overcurrent and DC Detection Fault Memory Register. The channel is placed in FAULT state.


Report register:

 - Latched: OC_DC_FAULT_LATCHED Register (Address = 0x8E), bit 3


_**8.3.6 Clock Error Event**_


The Clock Rates section describes the supported Audio Data Formats, Bit Depths, and Clock Rates. If these
conditions are violated or the clock is halted, the device reports a Clock Error Fault event and the device
gracefully transitions to the AUTOREC state. After audio clock recovery, the device automatically returns to the
previous state.


As Clock Error Event is a transient event it is not reported in a status register.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 61


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**Note**
Clock error events are detected in Hi-Z and Play Mode


Report register:

 - Latched: CLK_FAULT_LATCHED Register (Address = 0x8A), bit 0


_**8.3.7 Warning Events**_


**8.3.7.1 Overtemperature Warning Event**


The Overtemperature Warning section describes the circumstances under which the device creates a
Overtemperature Warning event.


Report registers:


 - Unlatched/Status: OTW_STATUS Register (Address = 0x82), bit 4

 - Latched/Memory: OTW_LATCHED Register (Address = 0x88), bit 4


**8.3.7.2 Overcurrent Limit Warning Event**


The Overcurrent Limit (Cycle-By-Cycle) section describes the circumstances under which the device creates an
Overcurrent Limit Warning event. This is a transient event that only lasts for a limited time.


Report register:

 - Unlatched/Status: CBC_WARNING_STATUS Register (Address = 0x85), bit 7

 - Latched/Memory: CBC_FAULT_WARN_LATCHED Register (Address = 0x8D), bit 7


**8.3.7.3 Clip Detect Warning Event**


The Clip Detect section describes the circumstances under which the device creates a Clip Detect Warning
event.


Report registers:

 - Unlatched/Status: CLIP_WARN_STATUS Register (Address = 0x83), bit 3

 - Latched/Memory: CLIP_WARN_LATCHED Register (Address = 0x89), bit 3


62 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**9 Programming**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**9.1 I** **[2]** **C Serial Communication Bus**


The device communicates with the system processor through the I [2] C serial communication bus as an I [2] C
target-only device and supports 100-kHz and 400-kHz data transfer rates for random and sequential write and
read operation. The processor can poll the device through I [2] C to determine the operating status, configure
settings, or run diagnostics.


The TAS6511-Q1 register map and DSP memory span multiple pages and books. The user should change from
page to page before writing individual registers or DSP memory. Changing from page to page is accomplished
via register 0 on each page. This register value selects the page address, from 0 to 255. All registers listed in the
TAS6511-Q1 Data sheet belong to Page 0.


For a complete list and description of all I [2] C controls, see the Register Maps section.


**9.2 I** **[2]** **C Address Selection**


TAS6511-Q1 supports eight I [2] C addresses, thus up to eight devices can be used together in a system with no
additional bus switching hardware.


The pull-up or pull-down resistor connected between the device I2C_ADDR pin and the DVDD-rail (pull-up) or
GND (pull-down) determines the I [2] C address during power up. The I2C address latches after a POR event and
is locked until the next POR event.


**Table 9-1. I** **[2]** **C Addresses**





**9.3 I** **[2]** **C Bus Protocol**


The I [2] C bus uses two signals, SDA (data) and SCL (clock), to communicate between integrated circuits in a
system. Data is transferred on the bus serially, one bit at a time. The address and data are transferred in
byte (8- bit) format with the most-significant bit (MSB) transferred first. In addition, each byte transferred on the
bus is acknowledged by the receiving device with an acknowledge bit. Each transfer operation begins with the
controller device driving a start condition on the bus and ends with the controller device driving a stop condition
on the bus. The bus uses transitions on the data terminal (SDA) while the clock is HIGH to indicate a start and
stop conditions. A HIGH-to-LOW transition on SDA indicates a start, and a LOW-to-HIGH transition indicates
a stop. Normal data bit transitions must occur within the low time of the clock period. The controller generates
the 7-bit target address and the read/write (R/W) bit to open communication with another device and then wait
for an acknowledge condition. The device holds SDA LOW during the acknowledge-clock period to indicate
an acknowledgment. When this occurs, the controller transmits the next byte of the sequence. Each device is
addressed by a unique 7-bit target address plus a R/W bit (1 byte). All compatible devices share the same
signals via a bidirectional bus using a wired-AND connection. An external pull-up resistor must be used for the
SDA and SCL signals to set the HIGH level for the bus. The number of bytes that can be transmitted between
start and stop conditions is unlimited. When the last word transfers, the controller generates a stop condition to
release the bus.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 63


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**



SDA


SCL



|Col1|Col2|R/ 8-Bit Register Data for 8-Bit Register Data for<br>7-Bit Target Address A 8-Bit Register Address (N) A A A<br>W Address (N) Address (N)|Col4|
|---|---|---|---|
|||||
|||7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0|7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0<br>7<br>6<br>5<br>4<br>3<br>2<br>1<br>0|
|||||


Start Stop


**Figure 9-1. Typical I** **[2]** **C Sequence**







SCL


SDA


**9.4 Random Write**



**Figure 9-2. SCL and SDA Timing**



As shown in Figure 9-3, a single-byte data-write transfer begins with the controller device transmitting a start
condition, followed by the I [2] C device address, and then read/write bit. The read/write bit determines the direction
of the data transfer. For a write data transfer, the read/write bit is a 0. After receiving the correct I [2] C device
address and the read/write bit, the device responds with an acknowledge bit. Next, the controller transmits
the address byte or bytes corresponding to the internal memory address being accessed. After receiving the
address byte, the device again responds with an acknowledge bit. Next, the controller device transmits the
data byte to be written to the memory address being accessed. After receiving the data byte, the device again
responds with an acknowledge bit. Finally, the controller device transmits a stop condition to complete the
single-byte data-write transfer.


Start
Condition Acknowledge Acknowledge Acknowledge


I [2] C Device Address and R/W Bit Subaddress Data Byte ConditionStop


**Figure 9-3. Random Write Transfer**


**9.5 Random Read**


As shown in Figure 9-4, a single-byte data-read transfer begins with the controller device transmitting a start
condition followed by the I [2] C device address and the read/write bit. For the data-read transfer, both a write
followed by a read are done. Initially, a write is done to transfer the address byte or bytes of the internal memory
address to be read. As a result, the read/write bit is a 0. After receiving the address and the read/write bit,
the device responds with an acknowledge bit. In addition, after sending the internal memory address byte or
bytes, the controller device transmits another start condition followed by the address and the read/write bit again.


64 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



This time the read/write bit is a 1, indicating a read transfer. After receiving the address and the read/write bit,
the device again responds with an acknowledge bit. Next, the device transmits the data byte from the memory
address being read. After receiving the data byte, the controller device transmits a not-acknowledge followed by
a stop condition to complete the single-byte data-read transfer.


Repeat Start
Condition

Start Not


I [2] C Device Address and R/W Bit Subaddress I [2] C Device Address and R/W Bit Data Byte ConditionStop


**Figure 9-4. Random Read Transfer**


**9.6 Sequential Read**


A sequential data-read transfer is identical to a single-byte data-read transfer except that multiple data bytes
are transmitted by the device to the controller device as shown in Figure 9-5. Except for the last data byte, the
controller device responds with an acknowledge bit after receiving each data byte and automatically increments
the I [2] C subaddress by one. After receiving the last data byte, the controller device transmits a not-acknowledge
followed by a stop condition to complete the transfer.


Repeat Start
Condition
Start Not


I [2] C Device Address and R/W Bit Subaddress I [2] C Device Address and R/W Bit First Data Byte Other Data Byte Last Data Byte ConditionStop


**Figure 9-5. Sequential Read Transfer**


**9.7 DSP Memory Book and Page**


The DSP memory is arranged in books, pages, and registers. Each book has several pages and each page has
several registers. As the TAS6511-Q1 register map spans several books and pages, the user must select the
correct book and page before writing individual register bits or bytes.


To change the book, the user must be on page 0x00. Register 0x7F on page 0x00 is used to change the book.
Register 0x00 of each page is used to change the page.


**Changing a book** : First write 0x00 to register 0x00 to switch to page 0. Afterward, write the desired book
number to register 0x7F on page 0.


**Changing a page inside a book** : Write the desired page number to register 0x00.


**24-bit wide registers:** When reading or writing 24-bit wide registers in the DSP memory, the sequential read/
write is recommended.


Example using 0xB0 as I [2] C address:

```
 W B0 00 00      / Page switching (1st 00) to page 0 (2nd 00)
 W B0 7F 8C      / 7F 8C = change to book 8C. It's required to be in page 0 before changing a

```

Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 65


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**

```
 book
 W B0 00 page     / Go to the desired page in book 8C
 W B0 12 00 XX XX xx  / Sequential write to register/offset 12, 4 x 8 bit
 R B0 12 04      / Sequential read register 0x12-0x15, 4 x 8 bit
 W B0 00 00      / Return to page 0 of book 8C
 W B0 7F 00      / Return to book 0, page 0

```

66 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


**10 Register Maps**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 67


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1 page0 Registers**


Table 10-1 lists the memory-mapped registers for the page0 registers. All register offset addresses not listed in
Table 10-1 should be considered as reserved locations and the register contents should not be modified.


**Table 10-1. PAGE0 Registers**


**Address** **Acronym** **Register Name** **Section**


0x01 RESET Reset Control Section 10.1.1


0x02 OUTPUT_CTRL Output Configuration Control Section 10.1.2


0x03 STATE_CTRL State Control Section 10.1.3


0x05 ISENSE_CTRL Current Sense Control Section 10.1.4


0x20 SCLK_INV_CTRL SCLK Polarity Control Section 10.1.5


0x21 AUDIO_INTERFACE_CTRL Audio Interface Control Section 10.1.6


0x22 I2S_CTRL I2S Control Section 10.1.7


0x23 SDIN_CTRL SDIN Control Section 10.1.8


0x25 SDOUT_CTRL SDOUT Control Section 10.1.9


0x27 SDIN_OFFSET_MSB SDIN Offset MSB Section 10.1.10


0x28 SDIN_AUDIO_OFFSET SDIN Audio Path Offset Section 10.1.11


0x29 SDIN_LL_OFFSET SDIN Low Latency Path Offset Section 10.1.12


0x2C SDOUT_OFFSET_MSB SDOUT Offset MSB Section 10.1.13


0x2D ISENSE_OFFSET Current Sense SDOUT Offset Section 10.1.14


0x2E VPREDICT_OFFSET Vpredict SDOUT Offset Section 10.1.15


0x32 LL_EN Low Latency Path Enable Section 10.1.16


0x33 AUDIO_SLOT_SELECT Audio Path TDM Slot Selection Section 10.1.17


0x34 LL_SLOT_SELECT Low Latency Path TDM Slot Selection Section 10.1.18


0x35 ISENSE_OUTPUT_SLOT Current Sense TDM Output Slot Selection Section 10.1.19


0x36 VPREDICT_OUTPUT_SLOT Vpredict TDM Output Slot Selection Section 10.1.20



0x37 RTLDG_EN Real-time Load Diagnostic Open Load/Shorted
Load Enable


0x38 RTLDG_S2PG_EN Real-time Load Diagnostic Short to Power/
Ground Enable



Section 10.1.21


Section 10.1.22



0x39 DC_BLOCK_SPEAKER_GUARD_EN DC Blocking and Speaker Guard Enable Section 10.1.23


0x3A FOLDBACK_EN PVDD and Thermal Foldback Enable Section 10.1.24


0x3B PAGE_AUTO_INC Page Auto Increment Section 10.1.25


0x40 DIG_VOL_CH1 Channel 1 Digital Volume Section 10.1.26


0x44 DIG_VOL_RAMP_CTRL Digital Volume Ramp Control Section 10.1.27


0x47 AUTO_MUTE_EN Auto Mute Enable Section 10.1.28


0x48 AUTO_MUTE_TIMING Auto Mute Time Section 10.1.29


0x4A ANALOG_GAIN Analog Gain Channel 1 Section 10.1.30


0x4E ANALOG_GAIN_RAMP_CTRL Analog Gain Ramp Control Section 10.1.31


0x51 RZ_CTRL Zero Frequency Control Section 10.1.32


0x52 FSW_CTRL Switching Frequency Control Section 10.1.33


0x54 CBC_CTRL CBC Control Section 10.1.34


0x55 CURRENT_LIMIT_CTRL Current Limit Control Section 10.1.35


0x56 OTW_LEVEL Overtempeature Warning Control Section 10.1.36


0x5B SDOUT_DATA SDOUT Data Selection Section 10.1.37


0x60 PWM_PHASE_CTRL PWM Phase Control Section 10.1.38


0x61 SS_CTRL Spread Spectrum Control Section 10.1.39


0x62 SS_RANGE_CTRL Spread Spectrum Range Control Section 10.1.40


68 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025


**Table 10-1. PAGE0 Registers (continued)**



**Address** **Acronym** **Register Name** **Section**


0x68 RAMP_PHASE_CTRL_GPO Switching Clock Phase Control for GPO Section 10.1.41


0x69 PWM_PHASE_M_CTRL Switching Clock Phase Control 1 Section 10.1.42


0x71 AUTO_MUTE_STATUS Auto Mute Status Section 10.1.43


0x72 STATE_REPORT Status Channel 1 Section 10.1.44


0x74 PVDD_SENSE PVDD Voltage Sense Section 10.1.45


0x75 TEMP_SENSOR Temperature Readout Section 10.1.46


0x76 FS_MON FS Monitor Section 10.1.47


0x77 SCLK_MON SCLK Monitor Section 10.1.48


0x80 POWER_FAULT_STATUS Power Fault Status Section 10.1.49


0x81 OT_FAULT Temperature (OTSD) and Fault Status Section 10.1.50


0x82 OTW_STATUS Temperature (OTW) Warning Status Section 10.1.51


0x83 CLIP_WARN_STATUS Channel Clip Detect Status Section 10.1.52


0x85 CBC_WARNING_STATUS CBC Warning Report Section 10.1.53


0x86 POWER_FAULT_LATCHED Power Fault Latched Section 10.1.54


0x87 OTSD_LATCHED Temperature (OTSD) Fault Latched Section 10.1.55


0x88 OTW_LATCHED Temperature (OTW) Warning Latched Section 10.1.56


0x89 CLIP_WARN_LATCHED Channel Clip Detect Warning Memory Section 10.1.57


0x8A CLK_FAULT_LATCHED Clock Error Latched Section 10.1.58


0x8B RTLDG_OL_SL_FAULT_LATCHED Real-Time Load Diagnostic OL/SL Latched Section 10.1.59


0x8C RTLDG_S2G_S2P_FAULT_LATCHED Real-Time Load Diagnostic S2G/S2P Latched Section 10.1.60


0x8D CBC_FAULT_WARN_LATCHED Channel Load Current Fault Latched Section 10.1.61



0x8E OC_DC_FAULT_LATCHED Channel Over Current and DC Detection Fault
Latched


0x8F OTSD_RECOVERY_EN Overtemperature Shutdown Auto-recovery
Enable



Section 10.1.62


Section 10.1.63



0x90 REPORT_ROUTING_2 Enable Faults to GPIO Section 10.1.64


0x91 REPORT_ROUTING_3 Enable Warnings to GPIO Section 10.1.65


0x92 REPORT_ROUTING_4 Enable Faults and Warnings Reported to GPIO Section 10.1.66


0x93 CLIP_DETECT_CTRL Clip Detect Control Section 10.1.67


0x94 REPORT_ROUTING_5 Enable Faults and Warnings Reported to GPIO Section 10.1.68


0x95 GPIO1_OUTPUT_SELECT Select Signals to GPIOs Section 10.1.69


0x96 GPIO2_OUTPUT_SELECT Select Signals to GPIOs Section 10.1.70


0x9B GPIO_INPUT_SLEEP_HIZ Select Signals from GPIOs Section 10.1.71


0x9C GPIO_INPUT_PLAY_SLEEP Select Signals from GPIOs Section 10.1.72


0x9D GPIO_INPUT_MUTE Select Signals from GPIOs Section 10.1.73


0x9E GPIO_INPUT_SYNC Select Signals from GPIOs Section 10.1.74


0xA0 GPIO_CTRL General GPIO Control Section 10.1.75


0xA1 GPIO_INVERT Invert GPIO Signals Section 10.1.76


0xB0 DC_LDG_CTRL DC Load Diagnostics Control Section 10.1.77


0xB1 DC_LDG_LO_CTRL DC Load Diagnostic Line-out Control Section 10.1.78


0xB2 DC_LDG_TIME_CTRL DC Load Diagnostic Timing Control Section 10.1.79


0xB3 DC_LDG_SL_CTRL DC Load Diagnostic Shorted-load Threshold Section 10.1.80


0xB5 AC_LDG_CTRL AC Load Diagnostic Control Section 10.1.81


0xB6 TWEETER_DETECT_CTRL Tweeter Detection Control Section 10.1.82


0xB7 TWEETER_DETECT_THRESH Tweeter Detection Threshold Section 10.1.83


0xB8 AC_LDG_FREQ_CTRL AC Load Diagnostic Frequency Control Section 10.1.84


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 69


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**Table 10-1. PAGE0 Registers (continued)**

















Complex bit access types are encoded to fit into small table cells. Table 10-2 shows the codes that are used for
access types in this section.


**Table 10-2. page0 Access Type Codes**

|Access Type|Code|Description|
|---|---|---|
|Read Type|Read Type|Read Type|
|R|R|Read|
|Write Type|Write Type|Write Type|
|W|W|Write|
|Reset or Default Value|Reset or Default Value|Reset or Default Value|
|-_n_||Value after reset or the default<br>value|



70 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.1 RESET Register (Address = 0x01) [Reset = 0x00]**


RESET is shown in Figure 10-1 and described in Table 10-3.


Return to the Summary Table.


Reset Control


**Figure 10-1. RESET Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|RESERVED|DEVICE<br>RESET|CLEAR FAULT|RESERVED|RESERVED|REGISTER<br>RESET|
|W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0|W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0|W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0|W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0|W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0|W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0<br>W-0x0|


**Table 10-3. RESET Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-5|RESERVED|W|0x0||
|4|DEVICE RESET|W|0x0|This bit will auto clear.<br>**0: Normal operation**<br>1: Device will be reset|
|3|CLEAR FAULT|W|0x0|This bit will auto clear.<br>**0: Normal operation**<br>1: Clear analog fault, not including load diagnostic fault|
|2|RESERVED|W|0x0|Reserved|
|1|RESERVED|W|0x0|Reserved|
|0|REGISTER RESET|W|0x0|This bit will auto clear.<br>This bit resets the mode registers back to their initial values. This<br>bit must be set only when the device is in SLEEP or DEEP SLEEP<br>mode.<br>**0: Normal operation**<br>1: Reset mode registers|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 71


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.2 OUTPUT_CTRL Register (Address = 0x02) [Reset = 0x00]**


OUTPUT_CTRL is shown in Figure 10-2 and described in Table 10-4.


Return to the Summary Table.


Output Configuration Control


**Figure 10-2. OUTPUT_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|CH1 LO MODE|RESERVED|MODULATION CTRL|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-4. OUTPUT_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 LO MODE|R/W|0x0|**0: Channel 1 is in normal / speaker mode**<br>1: Channel 1 is in line output mode|
|6-2|RESERVED|R/W|0x0||
|1-0|MODULATION CTRL|R/W|0x0|**00: BD mode**<br>01: 1SPW mode<br>10: Hybrid mode|



72 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.3 STATE_CTRL Register (Address = 0x03) [Reset = 0x20]**


STATE_CTRL is shown in Figure 10-3 and described in Table 10-5.


Return to the Summary Table.


State Control


**Figure 10-3. STATE_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|CH1 MUTE|CH1 STATE CTRL|RESERVED|
|R/W-0x0<br>R/W-0x2<br>R/W-0x0|R/W-0x0<br>R/W-0x2<br>R/W-0x0|R/W-0x0<br>R/W-0x2<br>R/W-0x0|



**Table 10-5. STATE_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 MUTE|R/W|0x0|Mute Channel 1<br>This bit issues soft mute request for channel 1. The volume will be<br>smoothly ramped down/up to avoid pop/click noise.<br>**0: Normal volume**<br>1: Mute|
|6-4|CH1 STATE CTRL|R/W|0x2|Channel 1 State Control<br>000: DEEP SLEEP<br>001: LOAD DIAG<br>**010: SLEEP**<br>011: HI-Z<br>100: PLAY|
|3-0|RESERVED|R/W|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 73


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.4 ISENSE_CTRL Register (Address = 0x05) [Reset = 0x00]**


ISENSE_CTRL is shown in Figure 10-4 and described in Table 10-6.


Return to the Summary Table.


Current Sense Control


**Figure 10-4. ISENSE_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 ISENSE<br>ENABLE|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-6. ISENSE_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3|CH1 ISENSE ENABLE|R/W|0x0|**0: Disable Current Sense Channel 1**<br>1: Enable Current Sense Channel 1|
|2-0|RESERVED|R/W|0x0||



74 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.5 SCLK_INV_CTRL Register (Address = 0x20) [Reset = 0x00]**


SCLK_INV_CTRL is shown in Figure 10-5 and described in Table 10-7.


Return to the Summary Table.


SCLK Polarity Control


**Figure 10-5. SCLK_INV_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|RESERVED|RESERVED|SCLK INV TX|SCLK INV|RESERVED|RESERVED|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-7. SCLK_INV_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0|Reserved|
|6|RESERVED|R/W|0x0|Reserved|
|5|SCLK INV TX|R/W|0x0|SCLK Polarity This bit sets the Inverted SCLK mode. In inverted<br>SCLK mode, the DAC assumes that the FSYNC and DIN edges are<br>aligned to the rising edge of the SCLK. In Normal SCLK mode, the<br>FSYNC and DIN edges are assumed to be aligned to the falling edge<br>of the SCLK.<br>**0: Normal SCLK mode**<br>1: Inverted SCLK mode|
|4|SCLK INV|R/W|0x0|SCLK Polarity<br>This bit sets the inverted SCLK mode. In inverted SCLK mode, the<br>DAC assumes that the FSYNC and DIN edges are aligned to the<br>rising edge of the SCLK. Normally they are assumed to be aligned to<br>the falling edge of the SCLK.<br>**0: Normal SCLK mode**<br>1: Inverted SCLK mode|
|3-2|RESERVED|R/W|0x0||
|1|RESERVED|R/W|0x0|Reserved|
|0|RESERVED|R/W|0x0|Reserved|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 75


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.6 AUDIO_INTERFACE_CTRL Register (Address = 0x21) [Reset = 0x00]**


AUDIO_INTERFACE_CTRL is shown in Figure 10-6 and described in Table 10-8.


Return to the Summary Table.


Audio Interface Control


**Figure 10-6. AUDIO_INTERFACE_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|LAST SAMPLE<br>HOLD|RESERVED|RESERVED|RESERVED|ASI FORMAT|FS PULSE WIDTH|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-8. AUDIO_INTERFACE_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|LAST SAMPLE HOLD|R/W|0x0|Disable Last Sample Hold<br>This bit controls whether to hold the last sample at audio interface<br>in the event of clock error. The last known good sample is held to<br>prevent errorneous samples to flow through the DAC.<br>**0: Enable last sample hold**<br>1: Disable last sample hold|
|6|RESERVED|R/W|0x0|Reserved|
|5|RESERVED|R/W|0x0||
|4|RESERVED|R/W|0x0|Reserved|
|3-2|ASI FORMAT|R/W|0x0|Data Format<br>These bits control both input and output audio interface formats for<br>DAC operation.<br>**00: I2S**<br>01: TDM/DSP<br>10: RTJ<br>11: LTJ|
|1-0|FS PULSE WIDTH|R/W|0x0|FSYNC pulse < 8 x SCLK<br>**00: High width of FSYNC in TDM/DSP mode is equal or greater**<br>**than 8 cycles of SCLK**<br>01: High width of FSYNC in TDM/DSP mode is less than 8 cycles of<br>SCLK<br>10 / 11: Reserved|



76 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.7 I2S_CTRL Register (Address = 0x22) [Reset = 0x50]**


I2S_CTRL is shown in Figure 10-7 and described in Table 10-9.


Return to the Summary Table.


I2S Control


**Figure 10-7. I2S_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|AUDIO I2S|LOW LATENCY I2S|RESERVED|
|R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x1<br>R/W-0x0|



**Table 10-9. I2S_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|AUDIO I2S|R/W|0x1|I2S Audio Left/Right Data Selection<br>Select left or right I2S data for the Audio path.<br>00: Zero data (mute)<br>**01: Left channel data**<br>10: Right channel data<br>11: Reserved|
|5-4|LOW LATENCY I2S|R/W|0x1|I2S Low Latency Left/Right Data Selection<br>Select left or right I2S data for the Low Latency path.<br>00: Zero data (mute)<br>**01: Right channel data**<br>10: Left channel data<br>11: Reserved|
|3-0|RESERVED|R/W|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 77


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.8 SDIN_CTRL Register (Address = 0x23) [Reset = 0x08]**


SDIN_CTRL is shown in Figure 10-8 and described in Table 10-10.


Return to the Summary Table.


SDIN Control


**Figure 10-8. SDIN_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|SDIN WL SELECT|RESERVED|
|R/W-0x0<br>R/W-0x2<br>R/W-0x0|R/W-0x0<br>R/W-0x2<br>R/W-0x0|R/W-0x0<br>R/W-0x2<br>R/W-0x0|



**Table 10-10. SDIN_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-2|SDIN WL SELECT|R/W|0x2|In non-TDM mode, these bits are used to control input Channel 1. In<br>TDM mode, these bits are used to control the word length of input for<br>both audio and low latency path channels.<br>00: 16 bits<br>01: 20 bits<br>**10: 24 bits**<br>11: 32 bits|
|1-0|RESERVED|R/W|0x0||



78 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.9 SDOUT_CTRL Register (Address = 0x25) [Reset = 0x08]**


SDOUT_CTRL is shown in Figure 10-9 and described in Table 10-11.


Return to the Summary Table.


SDOUT Control


**Figure 10-9. SDOUT_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|SDOUT WL SELECT|RESERVED|
|R/W-0x0<br>R/W-0x2<br>R/W-0x0|R/W-0x0<br>R/W-0x2<br>R/W-0x0|R/W-0x0<br>R/W-0x2<br>R/W-0x0|



**Table 10-11. SDOUT_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-2|SDOUT WL SELECT|R/W|0x2|I2S Word Length<br>These bits control output audio interface sample word lengths for<br>isense and vpredict output channels.<br>00: 16 bits<br>01: 20 bits<br>**10: 24 bits**<br>11: 32 bits|
|1-0|RESERVED|R/W|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 79


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.10 SDIN_OFFSET_MSB Register (Address = 0x27) [Reset = 0x00]**


SDIN_OFFSET_MSB is shown in Figure 10-10 and described in Table 10-12.


Return to the Summary Table.


SDIN Offset MSB


**Figure 10-10. SDIN_OFFSET_MSB Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|AUDIO PATH OFFSET MSB|LL PATH OFFSET MSB|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-12. SDIN_OFFSET_MSB Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|AUDIO PATH OFFSET<br>MSB|R/W|0x0|MSB for Audio Path Offset, refer to SDIN_AUDIO_OFFSET (0x28)|
|5-4|LL PATH OFFSET MSB|R/W|0x0|MSB for Low Latency Path Offset, refer to SDIN_LL_OFFSET (0x29)|
|3-0|RESERVED|R/W|0x0||


80 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.11 SDIN_AUDIO_OFFSET Register (Address = 0x28) [Reset = 0x00]**


SDIN_AUDIO_OFFSET is shown in Figure 10-11 and described in Table 10-13.


Return to the Summary Table.


SDIN Audio Path Offset


**Figure 10-11. SDIN_AUDIO_OFFSET Register**





**Table 10-13. SDIN_AUDIO_OFFSET Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|AUDIO PATH OFFSET<br>LSB|R/W|0x0|Used with AUDIO PATH OFFSET MSB in SDIN OFFSET MSB<br>register (0x27), for a total of 10 bits. Selects the offset of whole Audio<br>Path between 0 SCLK to 511 SCLK.<br>**0000000000: offset = 0 SCLK (no offset)**<br>0000000001: offset = 1 SCLK<br>0000000010: offset = 2 SCLKs<br>...<br>0111111111: offset = 511 SCLKs<br>1000000000 - 1111111111: Reserved|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 81


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.12 SDIN_LL_OFFSET Register (Address = 0x29) [Reset = 0x00]**


SDIN_LL_OFFSET is shown in Figure 10-12 and described in Table 10-14.


Return to the Summary Table.


SDIN Low Latency Path Offset


**Figure 10-12. SDIN_LL_OFFSET Register**





**Table 10-14. SDIN_LL_OFFSET Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|LOW LATENCY PATH<br>OFFSET LSB|R/W|0x0|Used with LL PATH OFFSET MSB in SDIN Offset MSB register<br>(0x27), for a total of 10 bits. Selects the offset of whole Low Latency<br>Path between 0 SCLK to 511 SCLK.<br>**0000000000: offset = 0 SCLK (no offset)**<br>0000000001: offset = 1 SCLK<br>0000000010: offset = 2 SCLKs<br>...<br>0111111111: offset = 511 SCLKs|



82 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.13 SDOUT_OFFSET_MSB Register (Address = 0x2C) [Reset = 0x00]**


SDOUT_OFFSET_MSB is shown in Figure 10-13 and described in Table 10-15.


Return to the Summary Table.


SDOUT Offset MSB


**Figure 10-13. SDOUT_OFFSET_MSB Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|ISENSE OFFSET MSB|VPREDICT OFFSET MSB|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-15. SDOUT_OFFSET_MSB Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|ISENSE OFFSET MSB|R/W|0x0|MSB for Current Sense data offset, refer to ISENSE_OFFSET<br>register (0x2D)|
|5-4|VPREDICT OFFSET MSB|R/W|0x0|MSB for Vpredict data offset, refer to VPREDICT_OFFSET register<br>(0x2E)|
|3-0|RESERVED|R/W|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 83


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.14 ISENSE_OFFSET Register (Address = 0x2D) [Reset = 0x00]**


ISENSE_OFFSET is shown in Figure 10-14 and described in Table 10-16.


Return to the Summary Table.


Current Sense SDOUT Offset


**Figure 10-14. ISENSE_OFFSET Register**





**Table 10-16. ISENSE_OFFSET Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|ISENSE OFFSET LSB|R/W|0x0|Used with ISENSE OFFSET MSB in SDOUT_OFFSET_MSB<br>register (0x2C), for a total of 10 bits. Defines the offset of Current<br>Sense data between 0 SCLK to 511 SCLKs.<br>**0000000000: offset = 0 SCLK**<br>0000000001: offset = 1 SCLK<br>0000000010: offset = 2 SCLKs<br>...<br>0111111111: offset = 511 SCLKs|



84 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.15 VPREDICT_OFFSET Register (Address = 0x2E) [Reset = 0x00]**


VPREDICT_OFFSET is shown in Figure 10-15 and described in Table 10-17.


Return to the Summary Table.


Vpredict SDOUT Offset


**Figure 10-15. VPREDICT_OFFSET Register**





**Table 10-17. VPREDICT_OFFSET Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|VPREDICT OFFSET LSB|R/W|0x0|Used with VPREDICT OFFSET MSB in SDOUT_OFFSET_MSB<br>register (0x2C), for a total of 10 bits. Defines the offset of Vpredict<br>data between 0 SCLK to 511 SCLKs.<br>**0000000000: offset = 0 SCLK**<br>0000000001: offset = 1 SCLK<br>0000000010: offset = 2 SCLKs<br>...<br>0111111111: offset = 511 SCLKs|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 85


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.16 LL_EN Register (Address = 0x32) [Reset = 0x00]**


LL_EN is shown in Figure 10-16 and described in Table 10-18.


Return to the Summary Table.


Low Latency Path Enable


**Figure 10-16. LL_EN Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|FLLP ENABLE|LLP ENABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-18. LL_EN Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R/W|0x0||
|1|FLLP ENABLE|R/W|0x0|**0: Disable Full Feature Low Latency path**<br>1: Enable Full Feature Low Latency path|
|0|LLP ENABLE|R/W|0x0|**0: Disable Low latency path**<br>1: Enable Low latency path|



86 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.17 AUDIO_SLOT_SELECT Register (Address = 0x33) [Reset = 0x00]**


AUDIO_SLOT_SELECT is shown in Figure 10-17 and described in Table 10-19.


Return to the Summary Table.


Audio Path TDM Slot Selection


**Figure 10-17. AUDIO_SLOT_SELECT Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|AUDIO PATH SLOT SELECT|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-19. AUDIO_SLOT_SELECT Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-0|AUDIO PATH SLOT<br>SELECT|R/W|0x0|TDM Slot selection<br>These bits control the offset of audio data in the audio frame for<br>input. The offset is defined as the number of TDM time slots.<br>AUDIO PATH SLOT SELECT controls the time slot assigned to audio<br>path.<br>**0000: Slot 1**<br>0001: Slot 2<br>0010: Slot 3<br>...<br>1111: Slot 16|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 87


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.18 LL_SLOT_SELECT Register (Address = 0x34) [Reset = 0x00]**


LL_SLOT_SELECT is shown in Figure 10-18 and described in Table 10-20.


Return to the Summary Table.


Low Latency Path TDM Slot Selection


**Figure 10-18. LL_SLOT_SELECT Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|LL PATH SLOT SELECT|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-20. LL_SLOT_SELECT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-0|LL PATH SLOT SELECT|R/W|0x0|TDM Slot selection<br>These bits control the offset of audio data in the audio frame for<br>input. The offset is defined as the number of TDM time slots.<br>LL PATH SLOT SELECT controls the time slot assigned to low<br>latency audio path.<br>**0000: Slot 1**<br>0001: Slot 2<br>0010: Slot 3<br>...<br>1111: Slot 16|



88 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.19 ISENSE_OUTPUT_SLOT Register (Address = 0x35) [Reset = 0x00]**


ISENSE_OUTPUT_SLOT is shown in Figure 10-19 and described in Table 10-21.


Return to the Summary Table.


Current Sense TDM Output Slot Selection


**Figure 10-19. ISENSE_OUTPUT_SLOT Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|ISENSE SLOT SELECT|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-21. ISENSE_OUTPUT_SLOT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-0|ISENSE SLOT SELECT|R/W|0x0|TDM Slot selection<br>These bits control the offset of audio data in the audio frame for<br>output. The offset is defined as the number of TDM time slots.<br>ISENSE SLOT SELECT controls the time slot of current sense<br>output data path.<br>**0000: Slot 1**<br>0001: Slot 2<br>0010: Slot 3<br>...<br>1111: Slot 16|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 89


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.20 VPREDICT_OUTPUT_SLOT Register (Address = 0x36) [Reset = 0x00]**


VPREDICT_OUTPUT_SLOT is shown in Figure 10-20 and described in Table 10-22.


Return to the Summary Table.


Vpredict TDM Output Slot Selection


**Figure 10-20. VPREDICT_OUTPUT_SLOT Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|VPREDICT SLOT SELECT|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-22. VPREDICT_OUTPUT_SLOT Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-0|VPREDICT SLOT<br>SELECT|R/W|0x0|TDM Slot selection<br>These bits control the offset of audio data in the audio frame for<br>output. The offset is defined as the number of TDM time slots.<br>VPREDICT SLOT SELECT controls the time slot of vpredict output<br>data path.<br>**0000: Slot 1**<br>0001: Slot 2<br>0010: Slot 3<br>...<br>1111: Slot 16|



90 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.21 RTLDG_EN Register (Address = 0x37) [Reset = 0x00]**


RTLDG_EN is shown in Figure 10-21 and described in Table 10-23.


Return to the Summary Table.


Real-time Load Diagnostic Open Load/Shorted Load Enable


**Figure 10-21. RTLDG_EN Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 RTLDG<br>OLSL ENABLE|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-23. RTLDG_EN Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3|CH1 RTLDG OLSL<br>ENABLE|R/W|0x0|**0: Disable Real-time load diagnostic open load/shorted load**<br>**Channel 1**<br>1: Enable Real-time load diagnostic open load/shorted load Channel<br>1|
|2-0|RESERVED|R/W|0x0||


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 91


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.22 RTLDG_S2PG_EN Register (Address = 0x38) [Reset = 0x00]**


RTLDG_S2PG_EN is shown in Figure 10-22 and described in Table 10-24.


Return to the Summary Table.


Real-time Load Diagnostic Short to Power/Ground Enable


**Figure 10-22. RTLDG_S2PG_EN Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 RTLDG<br>S2PG ENABLE|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-24. RTLDG_S2PG_EN Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3|CH1 RTLDG S2PG<br>ENABLE|R/W|0x0|**0: Disable Real-time load short to power/ground diagnostic**<br>**Channel 1**<br>1: Enable Real-time load short to power/ground diagnostic Channel 1|
|2-0|RESERVED|R/W|0x0||


92 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.23 DC_BLOCK_SPEAKER_GUARD_EN Register (Address = 0x39) [Reset = 0x00]**


DC_BLOCK_SPEAKER_GUARD_EN is shown in Figure 10-23 and described in Table 10-25.


Return to the Summary Table.


DC Blocking and Speaker Guard Enable


**Figure 10-23. DC_BLOCK_SPEAKER_GUARD_EN Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|SPEAKER<br>GUARD<br>ENABLE|RESERVED|DC BLOCK<br>BYPASS|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-25. DC_BLOCK_SPEAKER_GUARD_EN Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6|SPEAKER GUARD<br>ENABLE|R/W|0x0|**0: Disable Speaker Guard**<br>1: Enable Speaker Guard|
|5-1|RESERVED|R/W|0x0||
|0|DC BLOCK BYPASS|R/W|0x0|**0: Enable DC Blocking**<br>1: Bypass DC Blocking|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 93


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.24 FOLDBACK_EN Register (Address = 0x3A) [Reset = 0x00]**


FOLDBACK_EN is shown in Figure 10-24 and described in Table 10-26.


Return to the Summary Table.


PVDD and Thermal Foldback Enable


**Figure 10-24. FOLDBACK_EN Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|RESERVED|RESERVED|RESERVED|PVDD<br>FOLDBACK<br>ENABLE|RESERVED|RESERVED|RESERVED|THERMAL<br>FOLDBACK<br>ENABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-26. FOLDBACK_EN Register Field Descriptions**












|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0|Reserved|
|6|RESERVED|R/W|0x0|Reserved|
|5|RESERVED|R/W|0x0|Reserved|
|4|PVDD FOLDBACK<br>ENABLE|R/W|0x0|PVDD Foldback (AGL tracking)<br>**0: Disable PVDD Foldback**<br>1: Enable PVDD Foldback|
|3|RESERVED|R/W|0x0|Reserved|
|2|RESERVED|R/W|0x0|Reserved|
|1|RESERVED|R/W|0x0|Reserved|
|0|THERMAL FOLDBACK<br>ENABLE|R/W|0x0|Thermal Foldback<br>**0: Disable Thermal Foldback**<br>1: Enable Thermal Foldback|



94 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.25 PAGE_AUTO_INC Register (Address = 0x3B) [Reset = 0x00]**


PAGE_AUTO_INC is shown in Figure 10-25 and described in Table 10-27.


Return to the Summary Table.


Page Auto Increment


**Figure 10-25. PAGE_AUTO_INC Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|PAGE AUTO<br>INCREMENT<br>DISABLE|RESERVED|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-27. PAGE_AUTO_INC Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3|PAGE AUTO<br>INCREMENT DISABLE|R/W|0x0|Page auto increment disable<br>Disable page auto increment mode for non-zero books. When end of<br>page is reached it goes back to 4th address location of next page<br>when this bit is 0. When this bit is 1 the device goes to the start<br>location of the current page<br>**0: Enable Page auto increment**<br>1: Disable Page auto increment|
|2|RESERVED|R/W|0x0||
|1-0|RESERVED|R/W|0x0|Reserved|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 95


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.26 DIG_VOL_CH1 Register (Address = 0x40) [Reset = 0x30]**


DIG_VOL_CH1 is shown in Figure 10-26 and described in Table 10-28.


Return to the Summary Table.


Channel 1 Digital Volume


**Figure 10-26. DIG_VOL_CH1 Register**





**Table 10-28. DIG_VOL_CH1 Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 DIGITAL VOLUME|R/W|0x30|The digital volume is 0 dB to -103 dB in -0.5 dB steps.<br>**00110000: 0.0 dB**<br>00110001: -0.5 dB<br>...<br>11111110: -103 dB<br>11111111: Mute|



96 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.27 DIG_VOL_RAMP_CTRL Register (Address = 0x44) [Reset = 0x33]**


DIG_VOL_RAMP_CTRL is shown in Figure 10-27 and described in Table 10-29.


Return to the Summary Table.


Digital Volume Ramp Control


**Figure 10-27. DIG_VOL_RAMP_CTRL Register**











|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|DIGITAL VOLUME RAMP DOWN<br>FREQUENCY|DIGITAL VOLUME RAMP DOWN<br>STEP|DIGITAL VOLUME RAMP UP<br>FRQUENCY|DIGITAL VOLUME RAMP UP<br>STEP|
|R/W-0x0<br>R/W-0x3<br>R/W-0x0<br>R/W-0x3|R/W-0x0<br>R/W-0x3<br>R/W-0x0<br>R/W-0x3|R/W-0x0<br>R/W-0x3<br>R/W-0x0<br>R/W-0x3|R/W-0x0<br>R/W-0x3<br>R/W-0x0<br>R/W-0x3|


**Table 10-29. DIG_VOL_RAMP_CTRL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|DIGITAL VOLUME RAMP<br>DOWN FREQUENCY|R/W|0x0|These bits control the frequency of the digital volume updates when<br>the volume is ramping down.<br>**00: Update every 1 FS period**<br>01: Update every 2 FS periods<br>10: Update every 4 FS periods<br>11: Directly set the volume to zero (Instant mute)|
|5-4|DIGITAL VOLUME RAMP<br>DOWN STEP|R/W|0x3|These bits control the step of the digital volume updates when the<br>volume is ramping down.<br>00: Decrement by 4 dB for each update<br>01: Decrement by 2 dB for each update<br>10: Decrement by 1 dB for each update<br>**11: Decrement by 0.5 dB for each update**|
|3-2|DIGITAL VOLUME RAMP<br>UP FRQUENCY|R/W|0x0|These bits control the frequency of the digital volume updates when<br>the volume is ramping up.<br>**00: Update every 1 FS period**<br>01: Update every 2 FS periods<br>10: Update every 4 FS periods<br>11: Directly restore the volume (Instant unmute)|
|1-0|DIGITAL VOLUME RAMP<br>UP STEP|R/W|0x3|These bits control the step of the digital volume updates when the<br>volume is ramping up.<br>00: Increment by 4 dB for each update<br>01: Increment by 2 dB for each update<br>10: Increment by 1 dB for each update<br>**11: Increment by 0.5 dB for each update**|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 97


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.28 AUTO_MUTE_EN Register (Address = 0x47) [Reset = 0x00]**


AUTO_MUTE_EN is shown in Figure 10-28 and described in Table 10-30.


Return to the Summary Table.


Auto Mute Enable


**Figure 10-28. AUTO_MUTE_EN Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|CH1 AUTO<br>MUTE ENABLE|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-30. AUTO_MUTE_EN Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-1|RESERVED|R/W|0x0||
|0|CH1 AUTO MUTE<br>ENABLE|R/W|0x0|**0: Disable Channel 1 auto mute**<br>1: Enable Channel 1 auto mute|



98 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.29 AUTO_MUTE_TIMING Register (Address = 0x48) [Reset = 0x00]**


AUTO_MUTE_TIMING is shown in Figure 10-29 and described in Table 10-31.


Return to the Summary Table.


Auto Mute Time


**Figure 10-29. AUTO_MUTE_TIMING Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 AUTO MUTE TIMING|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-31. AUTO_MUTE_TIMING Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6-4|CH1 AUTO MUTE<br>TIMING|R/W|0x0|Auto Mute Time for Channel 1<br>These bits specify the length of consecutive zero samples at channel<br>1 before the channel can be auto muted. The times shown are for 96<br>kHz sampling rate and will scale with other rates. At 48kHz the timing<br>durations will double. At 192kHz the timing durations will be halved.<br>**000: 11.5 ms**<br>001: 53 ms<br>010: 106.5 ms<br>011: 266.5 ms<br>100: 0.535 sec<br>101: 1.065 sec<br>110: 2.665 sec<br>111: 5.33 sec|
|3-0|RESERVED|R/W|0x0||


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 99


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.30 ANALOG_GAIN Register (Address = 0x4A) [Reset = 0x00]**


ANALOG_GAIN is shown in Figure 10-30 and described in Table 10-32.


Return to the Summary Table.


Analog Gain Channel 1


**Figure 10-30. ANALOG_GAIN Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 ANALOG GAIN|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-32. ANALOG_GAIN Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R/W|0x0||
|5-4|CH1 ANALOG GAIN|R/W|0x0|Analog Gain Control<br>**00: 0 dB (21V)**<br>01: -2.9dB (15V)<br>10: -8.9dB (7.5V)<br>11: -14.9dB (3.75V)|
|3-0|RESERVED|R/W|0x0||



100 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.31 ANALOG_GAIN_RAMP_CTRL Register (Address = 0x4E) [Reset = 0x00]**


ANALOG_GAIN_RAMP_CTRL is shown in Figure 10-31 and described in Table 10-33.


Return to the Summary Table.


Analog Gain Ramp Control


**Figure 10-31. ANALOG_GAIN_RAMP_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|ANALOG GAIN RAMP STEP|ANALOG GAIN<br>RAMP DOWN<br>DISABLE|ANALOG GAIN<br>RAMP UP<br>DISABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-33. ANALOG_GAIN_RAMP_CTRL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3-2|ANALOG GAIN RAMP<br>STEP|R/W|0x0|Applies to ramp up and ramp down<br>**00: 15us/step**<br>01: 60us/step<br>10: 200us/step<br>11: 400us/step|
|1|ANALOG GAIN RAMP<br>DOWN DISABLE|R/W|0x0|**0: Enable Analog Gain ramp down**<br>1: Disable Analog Gain ramp down|
|0|ANALOG GAIN RAMP UP<br>DISABLE|R/W|0x0|**0: Enable Analog Gain ramp up**<br>1: Disable Analog Gain ramp up|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 101


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.32 RZ_CTRL Register (Address = 0x51) [Reset = 0x00]**


RZ_CTRL is shown in Figure 10-32 and described in Table 10-34.


Return to the Summary Table.


Zero Frequency Control


**Figure 10-32. RZ_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|ZERO FREQUENCY|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-34. RZ_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-3|RESERVED|R/W|0x0||
|2-0|ZERO FREQUENCY|R/W|0x0|Zero frequency control (zero resistor value)<br>**000: 300KΩ (recommended for 2.048MHz FSW, speaker mode)**<br>001: 600kΩ (recommended for all other FSW)<br>010: 750kΩ<br>011: 900kΩ (recommended for 384kHz FSW)<br>1xx: 1735kΩ (recommended for 2.048MHz FSW, lineout mode)|



102 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.33 FSW_CTRL Register (Address = 0x52) [Reset = 0x03]**


FSW_CTRL is shown in Figure 10-33 and described in Table 10-35.


Return to the Summary Table.


Switching Frequency Control


**Figure 10-33. FSW_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|PULSE<br>INJECTION|RESERVED|FSW SELECT|
|R/W-0x0<br>R/W-0x0<br>R/W-0x3|R/W-0x0<br>R/W-0x0<br>R/W-0x3|R/W-0x0<br>R/W-0x0<br>R/W-0x3|


**Table 10-35. FSW_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|PULSE INJECTION|R/W|0x0|Pulse Injection<br>**0: Disable pulse injection**<br>1: Enable pulse injection|
|6-3|RESERVED|R/W|0x0||
|2-0|FSW SELECT|R/W|0x3|Class-D Switching Frequency<br>**011: 2.048MHz**<br>000: 384kHz<br>001: 480kHz<br>010: 1.024MHz<br>100: 432kHz<br>101: 528kHz<br>110: 576kHz<br>111: 624kHz|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 103


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.34 CBC_CTRL Register (Address = 0x54) [Reset = 0x03]**


CBC_CTRL is shown in Figure 10-34 and described in Table 10-36.


Return to the Summary Table.


CBC Control


**Figure 10-34. CBC_CTRL Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|RESERVED|RESERVED|CBC HIGH<br>FSW EN|CBC FAULT<br>ENABLE|CBC WARN<br>DISABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1|


**Table 10-36. CBC_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0|Reserved|
|3|RESERVED|R/W|0x0||
|2|CBC HIGH FSW EN|R/W|0x0|Enable CBC Warn and CBC Fault detection for high fsw (1024k and<br>2048k) when CBC WARN DISABLE and CBC FAULT DISABLE are<br>set to 1.<br>**0: Disabled**<br>1: Enabled|
|1|CBC FAULT ENABLE|R/W|0x1|0: Disable CBC fault detection<br>**1: Enable CBC fault detection**|
|0|CBC WARN DISABLE|R/W|0x1|0: Disable CBC warning detection<br>**1: Enable CBC waring detection**|



104 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.35 CURRENT_LIMIT_CTRL Register (Address = 0x55) [Reset = 0x00]**


CURRENT_LIMIT_CTRL is shown in Figure 10-35 and described in Table 10-37.


Return to the Summary Table.


Current Limit Control


**Figure 10-35. CURRENT_LIMIT_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|RESERVED|CBC/OC LEVEL|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-37. CURRENT_LIMIT_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0|Reserved|
|6-2|RESERVED|R/W|0x0||
|1-0|CBC/OC LEVEL|R/W|0x0|Select the CBC and OC Current Limit level<br>**00: Level 4**<br>01: Level 3<br>10: Level 2<br>11: Level 1|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 105


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.36 OTW_LEVEL Register (Address = 0x56) [Reset = 0x00]**


OTW_LEVEL is shown in Figure 10-36 and described in Table 10-38.


Return to the Summary Table.


Overtempeature Warning Control


**Figure 10-36. OTW_LEVEL Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|OVERTEMP WARN LEVEL|
|R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0|



**Table 10-38. OTW_LEVEL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-3|RESERVED|R/W|0x0||
|2-0|OVERTEMP WARN<br>LEVEL|R/W|0x0|Select OT Warning level1~7 report to register<br>**000: NO OT Warning Level**<br>001: OT Warning Level 1 (trigger when temperature > 95C)<br>010: OT Warning Level 2 (trigger when temperature > 110C)<br>011: OT Warning Level 3 (trigger when temperature > 125C)<br>100: OT Warning Level 4 (trigger when temperature > 135C)<br>101: OT Warning Level 5 (trigger when temperature > 145C)<br>110: OT Warning Level 6 (trigger when temperature > 155C)<br>111: OT Warning Level 7 (trigger when temperature > 165C)|



106 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.37 SDOUT_DATA Register (Address = 0x5B) [Reset = 0x00]**


SDOUT_DATA is shown in Figure 10-37 and described in Table 10-39.


Return to the Summary Table.


SDOUT Data Selection


**Figure 10-37. SDOUT_DATA Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|RESERVED|TEMP PVDD<br>SDOUT EN|RESERVED|reg_isns_cal|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-39. SDOUT_DATA Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R/W|0x0||
|5|TEMP PVDD SDOUT EN|R/W|0x0|Send temperature, Isense, and Vpredict data to SDOUT<br>**0: No temperature data and PVDD data sent with Vpredict and**<br>**Isense data**<br>1: Send Temperature data and PVDD data with Vpredict and Isense<br>data|
|4|RESERVED|R/W|0x0||
|3|reg_isns_cal|R/W|0x0|Isense offset calibration enable<br>**0: Disable Isense offset calibration**<br>1: Enable Isense offset calibration|
|2-0|RESERVED|R/W|0x0|Reserved|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 107


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.38 PWM_PHASE_CTRL Register (Address = 0x60) [Reset = 0x00]**


PWM_PHASE_CTRL is shown in Figure 10-38 and described in Table 10-40.


Return to the Summary Table.


PWM Phase Control


**Figure 10-38. PWM_PHASE_CTRL Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|PWM PHASE<br>MANUAL<br>MODE ENABLE|RESERVED|RESERVED|PWM PHASE<br>SYNC SELECT|PWM PHASE<br>SYNC ENABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-40. PWM_PHASE_CTRL Register Field Descriptions**












|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|PWM PHASE MANUAL<br>MODE ENABLE|R/W|0x0|**0: Disable manual phase mode (default)**<br>1: Enable manual phase mode (Configure in 0x69)|
|6-4|RESERVED|R/W|0x0|Reserved|
|3-2|RESERVED|R/W|0x0||
|1|PWM PHASE SYNC<br>SELECT|R/W|0x0|**0: GPIO sync**<br>1: SCLK sync|
|0|PWM PHASE SYNC<br>ENABLE|R/W|0x0|**0: Disable ramp phase sync**<br>1: Enable ramp phase sync|



108 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.39 SS_CTRL Register (Address = 0x61) [Reset = 0x00]**


SS_CTRL is shown in Figure 10-39 and described in Table 10-41.


Return to the Summary Table.


Spread Spectrum Control


**Figure 10-39. SS_CTRL Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|GPO RAMP CLK DIV|RESERVED|RESERVED|RESERVED|RDM PERIOD<br>TRIANLE SS<br>ENABLE|RANDOM SS<br>ENABLE|TRIANGLE SS<br>ENABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-41. SS_CTRL Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|GPO RAMP CLK DIV|R/W|0x0|Selects GPIO output of ramp clock<br>**0: div1**<br>1: div2<br>2: div4<br>3: div8|
|5|RESERVED|R/W|0x0||
|4|RESERVED|R/W|0x0|Reserved|
|3|RESERVED|R/W|0x0||
|2|RDM PERIOD TRIANLE<br>SS ENABLE|R/W|0x0|**0: Normal triangle spread spectrum**<br>1: Triangle spread spectrum but the period of triangle spread<br>spectrum is random|
|1|RANDOM SS ENABLE|R/W|0x0|**0: Disable random spread spectrum**<br>1: Enable random SS|
|0|TRIANGLE SS ENABLE|R/W|0x0|**0: Disable triangle spread spectrum**<br>1: Enable triangle SS|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 109


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.40 SS_RANGE_CTRL Register (Address = 0x62) [Reset = 0x00]**


SS_RANGE_CTRL is shown in Figure 10-40 and described in Table 10-42.


Return to the Summary Table.


Spread Spectrum Range Control


**Figure 10-40. SS_RANGE_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|RANDOM SS RANGE|RDM PERIOD TRIANGLE SS<br>CTRL.|TRIANGLE SS RANGE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-42. SS_RANGE_CTRL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6-4|RANDOM SS RANGE|R/W|0x0|Random SS range control<br>This setting is active when Random SS mode is enabled<br>for 384kHz fsw<br>**000: SS range +0.31%**<br>001: SS range ±0.31%<br>010: SS range ±0.94%<br>011: SS range ±2.19%<br>100: SS range ±4.69%<br>101: SS range ±9.69%<br>for 480kHz fsw<br>**000: SS range +0.39%**<br>001: SS range ±0.39%<br>010: SS range ±1.17%<br>011: SS range ±2.73%<br>100: SS range ±5.86%<br>101: SS range ±12.11%<br>for 1024kHz fsw<br>**000: SS range +0.83%**<br>001: SS range ±0.83%<br>010: SS range ±2.5%<br>011: SS range ±5.83%<br>100: SS range ±12.5%<br>101: SS range ±25.83%<br>for 2048kHz fsw<br>**000: SS range +1.67%**<br>001: SS range ±1.67%<br>010: SS range ±5%<br>101: SS range ±11.67%<br>100: SS range ±25%<br>101: SS range ±51.67%|
|3-2|RDM PERIOD TRIANGLE<br>SS CTRL.|R/W|0x0|Random Period Triangle SS control<br>This setting is active when Random Period Triangle SS mode is<br>enabled<br>**00: Random triangle SS period from 1/FSS to 2/FSS**<br>01: Random triangle SS period from 1/FSS to 4/FSS<br>10: Random triangle SS period from 1/FSS to 8/FSS<br>11: Random triangle SS period from 1/FSS to 15/FSS|



110 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025


**Table 10-42. SS_RANGE_CTRL Register Field Descriptions (continued)**



|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|1-0|TRIANGLE SS RANGE|R/W|0x0|Triangle SS range control<br>This setting is active when TRIANGLE SS is enabled<br>For 384k FSW<br>**00: 24kHz FSS with 15% range(±7.5%)**<br>01: 24kHz FSS with 25% range(±12.5%)<br>10: 48kHz FSS with 15% range(±7.5%)<br>11: 48kHz FSS with 25% range(±12.5%)<br>For 480k FSW<br>**00: 30kHz Fss with 19% range(±9.5%)**<br>01: 30kHz Fss with 25% range(±12.5%)<br>10: 60kHz Fss with 19% range(±9.5%)<br>11: 60kHz Fss with 25% range(±12.5%)<br>For 1024k FSW<br>**00: 85kHz Fss with 10% range(±5%)**<br>01: 85kHz Fss with 20% range(±10%)<br>10: 128kHz Fss with 17% range(±8.5%)<br>11: 128kHz Fss with 24% range(±12%)<br>For 2048k FSW<br>**00: 128kHz Fss with 13% range(±6.5%)**<br>01: 128kHz Fss with 27% range(±13.5%)<br>10: 170kHz Fss with 10% range(±5%)<br>11: 170kHz Fss with 20% range(±10%)|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 111


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.41 RAMP_PHASE_CTRL_GPO Register (Address = 0x68) [Reset = 0x00]**


RAMP_PHASE_CTRL_GPO is shown in Figure 10-41 and described in Table 10-43.


Return to the Summary Table.


Switching Clock Phase Control for GPO


**Figure 10-41. RAMP_PHASE_CTRL_GPO Register**





**Table 10-43. RAMP_PHASE_CTRL_GPO Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|GPO PHASE CONTROL|R/W|0x0|Control phase for GPO Clock Sync. Requires bit 7 of 0x60 to be set<br>to manual mode<br>Determine phase offset: 360 deg x reg_dephase_gpo / 256<br>**0x00: 0 deg**<br>0x01: 1.4 deg<br>...<br>0x40: 90 deg<br>...<br>0xFF: 358.6 deg|



112 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.42 PWM_PHASE_M_CTRL Register (Address = 0x69) [Reset = 0x00]**


PWM_PHASE_M_CTRL is shown in Figure 10-42 and described in Table 10-44.


Return to the Summary Table.


Switching Clock Phase Control 1


**Figure 10-42. PWM_PHASE_M_CTRL Register**





**Table 10-44. PWM_PHASE_M_CTRL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 PWM PHASE<br>MANUAL CTRL|R/W|0x0|PWM PHASE MANUAL MODE EN in register 0x60 must be enabled.<br>1.4 degrees per step.<br>**0x00: 0 deg**<br>0x01: 1.4 deg<br>...<br>0x40: 90 deg<br>...<br>0xFF: 358.6 deg|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 113


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.43 AUTO_MUTE_STATUS Register (Address = 0x71) [Reset = 0x00]**


AUTO_MUTE_STATUS is shown in Figure 10-43 and described in Table 10-45.


Return to the Summary Table.


Auto Mute Status


**Figure 10-43. AUTO_MUTE_STATUS Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 AM<br>STATUS|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|


**Table 10-45. AUTO_MUTE_STATUS Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R|0x0||
|3|CH1 AM STATUS|R|0x0|This bit indicates the auto mute status for channel 1.<br>**0: Not auto muted**<br>1: Auto muted|
|2-0|RESERVED|R|0x0||



114 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.44 STATE_REPORT Register (Address = 0x72) [Reset = 0x00]**


STATE_REPORT is shown in Figure 10-44 and described in Table 10-46.


Return to the Summary Table.


Status Channel 1


**Figure 10-44. STATE_REPORT Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|CH1 STATUS|RESERVED|
|R-0x0<br>R-0x0|R-0x0<br>R-0x0|



**Table 10-46. STATE_REPORT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|CH1 STATUS|R|0x0|**000: DEEP SLEEP**<br>001: LOAD DIAG<br>010: SLEEP<br>011: HI-Z<br>100: PLAY<br>101: FAULT<br>110: AUTOREC|
|3-0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 115


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.45 PVDD_SENSE Register (Address = 0x74) [Reset = 0x00]**


PVDD_SENSE is shown in Figure 10-45 and described in Table 10-47.


Return to the Summary Table.


PVDD Voltage Sense


**Figure 10-45. PVDD_SENSE Register**





**Table 10-47. PVDD_SENSE Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|PVDD SENSE|R|0x0|Sensed PVDD voltage = Bit value x 0.19<br>0000 0000: 0V<br>0000 0001: 0.19V<br>...<br>0100 1101: 14.63V<br>...<br>1111 1111: 48.45V|



116 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.46 TEMP_SENSOR Register (Address = 0x75) [Reset = 0x00]**


TEMP_SENSOR is shown in Figure 10-46 and described in Table 10-48.


Return to the Summary Table.


Temperature Readout


**Figure 10-46. TEMP_SENSOR Register**





**Table 10-48. TEMP_SENSOR Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|TEMP SENSOR|R|0x0|Temp in Kelvin K = Bit value x 2.19<br>Temp in Celsius = Temp in Kelvin - 273.15|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 117


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.47 FS_MON Register (Address = 0x76) [Reset = 0x00]**


FS_MON is shown in Figure 10-47 and described in Table 10-49.


Return to the Summary Table.


FS Monitor


**Figure 10-47. FS_MON Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|SCLK RATIO MSB|DETECTED SAMPLE RATE|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|



**Table 10-49. FS_MON Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R|0x0||
|5-4|SCLK RATIO MSB|R|0x0|MSB for SCLK Monitor. Described in register SCLK MONITOR<br>register (0x77).|
|3-0|DETECTED SAMPLE<br>RATE|R|0x0|**0000: FS Error**<br>0100: 16KHz<br>0110: 32KHz<br>1001: 48KHz<br>1011: 96KHz<br>1101: 192KHz<br>Others Reserved|



118 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.48 SCLK_MON Register (Address = 0x77) [Reset = 0x00]**


SCLK_MON is shown in Figure 10-48 and described in Table 10-50.


Return to the Summary Table.


SCLK Monitor


**Figure 10-48. SCLK_MON Register**





**Table 10-50. SCLK_MON Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|SCLK RATIO LSB|R|0x0|Used with SCLK RATIO MSB in register 0x76, for a total of 10 bits.<br>SCLK ratio range between 32Fs to 512Fs.<br>00 0010 0000: 32Fs<br>....<br>10 0000 0000: 512Fs|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 119


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.49 POWER_FAULT_STATUS Register (Address = 0x80) [Reset = 0x00]**


POWER_FAULT_STATUS is shown in Figure 10-49 and described in Table 10-51.


Return to the Summary Table.


Power Fault Status


**Figure 10-49. POWER_FAULT_STATUS Register**















|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|GLOBAL<br>WARNING<br>STATUS|GLOBAL<br>FAULT STATUS|RESERVED|DVDD UV<br>STATUS|PVDD OV<br>STATUS|RESERVED|PVDD UV<br>STATUS|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-51. POWER_FAULT_STATUS Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|GLOBAL WARNING<br>STATUS|R|0x0|Unlatched<br>**0: No warning**<br>1: If any warning active in device, regardless of warning signal<br>configuration|
|6|GLOBAL FAULT STATUS|R|0x0|Unlatched<br>**0: No fault**<br>1: If any fault active in device, regardless of fault signal configuration|
|5|RESERVED|R|0x0|Reserved|
|4|DVDD UV STATUS|R|0x0|Unlatched<br>**0: DVDD supply voltage is above UV threshold**<br>1:DVDD supply voltage is below UV threshold|
|3|PVDD OV STATUS|R|0x0|Unlatched<br>**0: PVDD supply voltage is below OV threshold**<br>1: PVDD supply voltage is above OV threshold|
|2|RESERVED|R|0x0||
|1|PVDD UV STATUS|R|0x0|Unlatched<br>**0: PVDD supply voltage is above UV threshold**<br>1:PVDD supply voltage is below UV threshold|
|0|RESERVED|R|0x0||


120 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.50 OT_FAULT Register (Address = 0x81) [Reset = 0x00]**


OT_FAULT is shown in Figure 10-50 and described in Table 10-52.


Return to the Summary Table.


Temperature (OTSD) and Fault Status


**Figure 10-50. OT_FAULT Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|GLOBAL<br>WARNING|GLOBAL<br>FAULT|RESERVED|OTSD STATUS|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-52. OT_FAULT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|GLOBAL WARNING|R|0x0|**0: No warning**<br>1: Any warning triggered|
|6|GLOBAL FAULT|R|0x0|**0: No fault**<br>1: Any fault triggered|
|5|RESERVED|R|0x0||
|4|OTSD STATUS|R|0x0|Unlatched<br>**0: Die temperature is below OTSD threshold**<br>1: Die temperature is above OTSD threshold|
|3-0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 121


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.51 OTW_STATUS Register (Address = 0x82) [Reset = 0x00]**


OTW_STATUS is shown in Figure 10-51 and described in Table 10-53.


Return to the Summary Table.


Temperature (OTW) Warning Status


**Figure 10-51. OTW_STATUS Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|OTW STATUS|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|



**Table 10-53. OTW_STATUS Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-5|RESERVED|R|0x0||
|4|OTW STATUS|R|0x0|Unlatched<br>**0: Die temperature is below OTW threshold**<br>1: Die temperature is above OTW threshold|
|3-0|RESERVED|R|0x0||



122 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.52 CLIP_WARN_STATUS Register (Address = 0x83) [Reset = 0x00]**


CLIP_WARN_STATUS is shown in Figure 10-52 and described in Table 10-54.


Return to the Summary Table.


Channel Clip Detect Status


**Figure 10-52. CLIP_WARN_STATUS Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 CLIP<br>STATUS|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|


**Table 10-54. CLIP_WARN_STATUS Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R|0x0||
|3|CH1 CLIP STATUS|R|0x0|**0: Channel 1 clipping is not present or below clip detect**<br>**threshold**<br>1: Channel 1 clipping is above clip detect threshold|
|2-0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 123


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.53 CBC_WARNING_STATUS Register (Address = 0x85) [Reset = 0x00]**


CBC_WARNING_STATUS is shown in Figure 10-53 and described in Table 10-55.


Return to the Summary Table.


CBC Warning Report


**Figure 10-53. CBC_WARNING_STATUS Register**







|7 6 5 4 3 2 1 0|Col2|
|---|---|
|CH1 CBC<br>WARN STATUS|RESERVED|
|R-0x0<br>R-0x0|R-0x0<br>R-0x0|


**Table 10-55. CBC_WARNING_STATUS Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 CBC WARN STATUS|R|0x0|**0: Channel 1 CBC warning is not present**<br>1: Channel 1 CBC warning is present|
|6-0|RESERVED|R|0x0||



124 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.54 POWER_FAULT_LATCHED Register (Address = 0x86) [Reset = 0x00]**


POWER_FAULT_LATCHED is shown in Figure 10-54 and described in Table 10-56.


Return to the Summary Table.


Power Fault Latched


**Figure 10-54. POWER_FAULT_LATCHED Register**













|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|DVDD POR<br>STORED|RESERVED|RESERVED|DVDD UV<br>STORED|PVDD OV<br>STORED|RESERVED|PVDD UV<br>STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-56. POWER_FAULT_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|DVDD POR STORED|R|0x0|Latched<br>**0: No DVDD power on reset event stored**<br>1: DVDD power on reset event detected and stored|
|6|RESERVED|R|0x0||
|5|RESERVED|R|0x0|Reserved|
|4|DVDD UV STORED|R|0x0|Latched<br>**0: No DVDD under voltage event stored**<br>1: DVDD under voltage event detected and stored|
|3|PVDD OV STORED|R|0x0|Latched<br>**0: No PVDD over voltage event stored**<br>1: PVDD over voltage event detected and stored|
|2|RESERVED|R|0x0||
|1|PVDD UV STORED|R|0x0|Latched<br>**0: No PVDD under voltage event stored**<br>1: PVDD under voltage event detected and stored|
|0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 125


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.55 OTSD_LATCHED Register (Address = 0x87) [Reset = 0x00]**


OTSD_LATCHED is shown in Figure 10-55 and described in Table 10-57.


Return to the Summary Table.


Temperature (OTSD) Fault Latched


**Figure 10-55. OTSD_LATCHED Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|OTSD STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|



**Table 10-57. OTSD_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-5|RESERVED|R|0x0||
|4|OTSD STORED|R|0x0|Latched<br>**0: No over temperature shutdown event stored**<br>1: Over temperature shutdown event detected and stored|
|3-0|RESERVED|R|0x0||



126 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.56 OTW_LATCHED Register (Address = 0x88) [Reset = 0x00]**


OTW_LATCHED is shown in Figure 10-56 and described in Table 10-58.


Return to the Summary Table.


Temperature (OTW) Warning Latched


**Figure 10-56. OTW_LATCHED Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|OTW STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|



**Table 10-58. OTW_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-5|RESERVED|R|0x0||
|4|OTW STORED|R|0x0|Latched<br>**0: No over temperature warning event stored**<br>1: Global over temperature warning event detected and stored|
|3-0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 127


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.57 CLIP_WARN_LATCHED Register (Address = 0x89) [Reset = 0x00]**


CLIP_WARN_LATCHED is shown in Figure 10-57 and described in Table 10-59.


Return to the Summary Table.


Channel Clip Detect Warning Memory


**Figure 10-57. CLIP_WARN_LATCHED Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 CLIP<br>STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|


**Table 10-59. CLIP_WARN_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R|0x0||
|3|CH1 CLIP STORED|R|0x0|Latched<br>**0: No channel 1 clipping event stored**<br>1: Channel 1 clipping event detcted and stored|
|2-0|RESERVED|R|0x0||



128 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.58 CLK_FAULT_LATCHED Register (Address = 0x8A) [Reset = 0x00]**


CLK_FAULT_LATCHED is shown in Figure 10-58 and described in Table 10-60.


Return to the Summary Table.


Clock Error Latched


**Figure 10-58. CLK_FAULT_LATCHED Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|RESERVED|CLOCK FAULT<br>STORED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|



**Table 10-60. CLK_FAULT_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|0x0||
|1|RESERVED|R|0x0|Reserved|
|0|CLOCK FAULT STORED|R|0x0|**0: No Clock Error event stored**<br>1: Clock Error event stored|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 129


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.59 RTLDG_OL_SL_FAULT_LATCHED Register (Address = 0x8B) [Reset = 0x00]**


RTLDG_OL_SL_FAULT_LATCHED is shown in Figure 10-59 and described in Table 10-61.


Return to the Summary Table.


Real-Time Load Diagnostic OL/SL Latched


**Figure 10-59. RTLDG_OL_SL_FAULT_LATCHED Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|CH1 RTLDG SL<br>STORED|RESERVED|CH1 RTLDG<br>OL STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-61. RTLDG_OL_SL_FAULT_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 RTLDG SL STORED|R|0x0|Latched<br>**0: No shorted load condition got detected on Channel 1 during**<br>**Real-Time Load Diagnostics**<br>1: A shorted load condition got detected on Channel 1 during Real-<br>Time Load Diagnostics|
|6-4|RESERVED|R|0x0||
|3|CH1 RTLDG OL STORED|R|0x0|Latched<br>**0: No open load condition got detected on Channel 1 during**<br>**Real-Time Load Diagnostics**<br>1: An open load condition got detected on Channel 1 during Real-<br>Time Load Diagnostics|
|2-0|RESERVED|R|0x0||



130 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.60 RTLDG_S2G_S2P_FAULT_LATCHED Register (Address = 0x8C) [Reset = 0x00]**


RTLDG_S2G_S2P_FAULT_LATCHED is shown in Figure 10-60 and described in Table 10-62.


Return to the Summary Table.


Real-Time Load Diagnostic S2G/S2P Latched


**Figure 10-60. RTLDG_S2G_S2P_FAULT_LATCHED Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|CH1 RTLDG<br>S2P STORED|RESERVED|CH1 RTLDG<br>S2G STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-62. RTLDG_S2G_S2P_FAULT_LATCHED Register Field Descriptions**













|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 RTLDG S2P<br>STORED|R|0x0|Latched<br>**0: No short-to-power condition got detected on Channel 1**<br>**during Real-Time Load Diagnostics**<br>1: A short-to-power condition got detected on Channel 1 during Real-<br>Time Load Diagnostics|
|6-4|RESERVED|R|0x0||
|3|CH1 RTLDG S2G<br>STORED|R|0x0|Latched<br>**0: No short-to-ground condition got detected on Channel 1**<br>**during Real-Time Load Diagnostics**<br>1: A short-to-ground condition got detected on Channel 1 during<br>Real-Time Load Diagnostics|
|2-0|RESERVED|R|0x0||


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 131


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.61 CBC_FAULT_WARN_LATCHED Register (Address = 0x8D) [Reset = 0x00]**


CBC_FAULT_WARN_LATCHED is shown in Figure 10-61 and described in Table 10-63.


Return to the Summary Table.


Channel Load Current Fault Latched


**Figure 10-61. CBC_FAULT_WARN_LATCHED Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|CH1 CBC<br>WARN<br>STORED|RESERVED|CH1 CBC<br>FAULT<br>STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-63. CBC_FAULT_WARN_LATCHED Register Field Descriptions**













|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 CBC WARN<br>STORED|R|0x0|Latched<br>Register clears to 0x0 upon reading<br>**0: No channel 1 load current warning event stored**<br>1: Channel 1 load current warning event detected and stored|
|6-4|RESERVED|R|0x0||
|3|CH1 CBC FAULT<br>STORED|R|0x0|Register clears to 0x0 upon reading<br>For channel restart, load current fault needs to be cleared by writing<br>to register 0x30<br>**0: No channel 1 load current fault event stored**<br>1: Channel 1 load current fault event detected and stored|
|2-0|RESERVED|R|0x0||


132 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.62 OC_DC_FAULT_LATCHED Register (Address = 0x8E) [Reset = 0x00]**


OC_DC_FAULT_LATCHED is shown in Figure 10-62 and described in Table 10-64.


Return to the Summary Table.


Channel Over Current and DC Detection Fault Latched


**Figure 10-62. OC_DC_FAULT_LATCHED Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|CH1 OC FAULT<br>STORED|RESERVED|CH1 DC FAULT<br>STORED|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-64. OC_DC_FAULT_LATCHED Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 OC FAULT STORED|R|0x0|Latched<br>**0: No channel 1 over current fault event stored**<br>1: Channel 1 over current fault event detected and stored|
|6-4|RESERVED|R|0x0||
|3|CH1 DC FAULT STORED|R|0x0|Latched<br>**0: No channel 1 DC fault event stored**<br>1: Channel 1 DC fault event detected and stored|
|2-0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 133


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.63 OTSD_RECOVERY_EN Register (Address = 0x8F) [Reset = 0x00]**


OTSD_RECOVERY_EN is shown in Figure 10-63 and described in Table 10-65.


Return to the Summary Table.


Overtemperature Shutdown Auto-recovery Enable


**Figure 10-63. OTSD_RECOVERY_EN Register**







|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|OTSD AUTO<br>REC|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-65. OTSD_RECOVERY_EN Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R/W|0x0||
|1|OTSD AUTO REC|R/W|0x0|**0: Disable Overtemperature Shutdown Auto-recovery**<br>1: Enable Overtemperature Shutdown Auto-recovery|
|0|RESERVED|R/W|0x0|Reserved|



134 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.64 REPORT_ROUTING_2 Register (Address = 0x90) [Reset = 0xA2]**


REPORT_ROUTING_2 is shown in Figure 10-64 and described in Table 10-66.


Return to the Summary Table.


Enable Faults to GPIO


**Figure 10-64. REPORT_ROUTING_2 Register**















|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CBC LATCH<br>FAULT GPIO|RESERVED|OTSD LATCH<br>FAULT GPIO|POWER<br>LATCH FAULT<br>GPIO|DC LDG FAULT<br>GPIO|RESERVED|OTSD FAULT<br>GPIO|POWER FAULT<br>GPIO|
|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|R/W-0x1<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x0|


**Table 10-66. REPORT_ROUTING_2 Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CBC LATCH FAULT GPIO|R/W|0x1|0: Latching Overcurrent Limiting events are not routed to~~FAULT~~<br>**1: Latching Overcurrent Limiting events are routed to**~~** FAULT**~~|
|6|RESERVED|R/W|0x0||
|5|OTSD LATCH FAULT<br>GPIO|R/W|0x1|0: Latching Overtemperature Shutdown events are not routed to<br>~~FAULT~~<br>**1: Latching Overtemperature Shutdown events are routed to**<br>~~**FAULT**~~|
|4|POWER LATCH FAULT<br>GPIO|R/W|0x0|**0: Latching Power Fault events are not routed to** ~~**FAULT**~~ <br>1: Latching Power Fault events are routed to~~FAULT~~|
|3|DC LDG FAULT GPIO|R/W|0x0|**0: Non-Latched DC Load Diagnostic events are not routed to**<br>~~**FAULT**~~ <br>1: Non-Latched DC Load Diagnostics events are routed to~~FAULT~~|
|2|RESERVED|R/W|0x0||
|1|OTSD FAULT GPIO|R/W|0x1|0: Non-Latched Overtemperature Shutdown events are not routed to<br>~~FAULT~~<br>**1: Non-Latched Overtemperature Shutdown events are routed to**<br>~~**FAULT**~~|
|0|POWER FAULT GPIO|R/W|0x0|**0: Non-Latching Power Fault events are not routed to**~~** FAULT**~~ <br>1: Non-Latching Power Fault events are routed to~~FAULT~~|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 135


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.65 REPORT_ROUTING_3 Register (Address = 0x91) [Reset = 0x00]**


REPORT_ROUTING_3 is shown in Figure 10-65 and described in Table 10-67.


Return to the Summary Table.


Enable Warnings to GPIO


**Figure 10-65. REPORT_ROUTING_3 Register**















|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|CBC LATCH<br>WARN GPIO|RESERVED|OTSD LATCH<br>WARN GPIO|POWER<br>LATCH WARN<br>GPIO|DC LDG WARN<br>GPIO|RESERVED|OTSD WARN<br>GPIO|POWER WARN<br>GPIO|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-67. REPORT_ROUTING_3 Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CBC LATCH WARN GPIO|R/W|0x0|**0: Latching Overcurrent Limiting events are not routed to**~~** WARN**~~<br>1: Latching Overcurrent Limiting events are routed to~~WARN~~|
|6|RESERVED|R/W|0x0||
|5|OTSD LATCH WARN<br>GPIO|R/W|0x0|**0: Latching Overtemperature Shutdown events are not routed to**<br>~~**WARN**~~<br>1: Latching Overtemperature Shutdown events are routed to~~WARN~~|
|4|POWER LATCH WARN<br>GPIO|R/W|0x0|**0: Latching Power Fault events are not routed to** ~~**WARN**~~<br>1: Latching Power Fault events are routed to~~WARN~~|
|3|DC LDG WARN GPIO|R/W|0x0|**0: Non-Latched DC Load Diagnostic events are not routed to**<br>~~**WARN**~~<br>1: Non-Latched DC Load Diagnostics events are routed to~~WARN~~|
|2|RESERVED|R/W|0x0||
|1|OTSD WARN GPIO|R/W|0x0|**0: Non-Latched Overtemperature Shutdown events are not**<br>**routed to**~~** WARN**~~<br>1: Non-Latched Overtemperature Shutdown events are routed to<br>~~WARN~~|
|0|POWER WARN GPIO|R/W|0x0|**0: Non-Latching Power Fault events are not routed to**~~** WARN**~~<br>1: Non-Latching Power Fault events are routed to~~WARN~~|


136 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.66 REPORT_ROUTING_4 Register (Address = 0x92) [Reset = 0x06]**


REPORT_ROUTING_4 is shown in Figure 10-66 and described in Table 10-68.


Return to the Summary Table.


Enable Faults and Warnings Reported to GPIO


**Figure 10-66. REPORT_ROUTING_4 Register**

















|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|RESERVED|CLIP LATCH<br>WARN GPIO|OTW LATCH<br>WARN GPIO|OTW WARN<br>GPIO|PROT SD<br>FAULT GPIO|OC LATCH<br>FAULT GPIO|DC LATCH<br>FAULT GPIO|FAULT WARN<br>GPIO|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x1<br>R/W-0x1<br>R/W-0x0|


**Table 10-68. REPORT_ROUTING_4 Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0|Reserved|
|6|CLIP LATCH WARN GPIO|R/W|0x0|**0: Latching Clip Detect events are not routed to** ~~**WARN**~~<br>1: Latching Clip Detect events are routed to~~WARN~~|
|5|OTW LATCH WARN GPIO|R/W|0x0|**0: Latching Overtemperature Warning events are not routed to**<br>~~**WARN**~~<br>1: Latching Overtemperature Warning events are routed to~~WARN~~|
|4|OTW WARN GPIO|R/W|0x0|**0:Non-latched Overtemperature Warning events are not routed**<br>**to**~~** WARN**~~ <br>1: Non-latched Overtemperature Warning events are routed to<br>~~WARN~~|
|3|PROT SD FAULT GPIO|R/W|0x0|**0: If any channel enters the FAULT state it is not reported to**<br>~~**FAULT**~~ <br>1: If any channel enters the FAULT state it is reported to~~ FAULT~~|
|2|OC LATCH FAULT GPIO|R/W|0x1|0: Latching Overcurrent shutdown events are not routed to~~FAULT~~<br>**1: Latching Overcurrent shutdown events are routed to**~~** FAULT**~~|
|1|DC LATCH FAULT GPIO|R/W|0x1|0: Latching DC Detect events are not routed to ~~FAULT~~<br>**1: Latching DC Detect events are routed to**~~** FAULT**~~|
|0|FAULT WARN GPIO|R/W|0x0|**0: **~~**WARN **~~**pin signals are not routedto the**~~** FAULT**~~**pin**<br>1:~~ WARN~~ pin signals are routed to the~~FAULT~~pin|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 137


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.67 CLIP_DETECT_CTRL Register (Address = 0x93) [Reset = 0x00]**


CLIP_DETECT_CTRL is shown in Figure 10-67 and described in Table 10-69.


Return to the Summary Table.


Clip Detect Control


**Figure 10-67. CLIP_DETECT_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|CLIP DETECT<br>ENABLE|RESERVED|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-69. CLIP_DETECT_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0|Reserved|
|6|CLIP DETECT ENABLE|R/W|0x0|**0: Disable Clip detect**<br>1: Enable Clip detect|
|5-4|RESERVED|R/W|0x0|Reserved|
|3-0|RESERVED|R/W|0x0||



138 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.68 REPORT_ROUTING_5 Register (Address = 0x94) [Reset = 0x00]**


REPORT_ROUTING_5 is shown in Figure 10-68 and described in Table 10-70.


Return to the Summary Table.


Enable Faults and Warnings Reported to GPIO


**Figure 10-68. REPORT_ROUTING_5 Register**















|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|CLK FAULT<br>GPIO|CLK LATCH<br>FAULT GPIO|CBC WARN<br>FAULT GPIO|RTLDG LATCH<br>FAULT GPIO|RESERVED|CLIP WARN<br>GPIO|RTLDG LATCH<br>WARN GPIO|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-70. REPORT_ROUTING_5 Register Field Descriptions**












|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CLK FAULT GPIO|R/W|0x0|**0: Non-Latched Clock error events are not routed to**~~** FAULT**~~** and**<br>~~**WARN**~~<br>1: Non-Latched Clock error events are routed to~~FAULT~~and~~WARN~~|
|6|CLK LATCH FAULT GPIO|R/W|0x0|**0: Latched Clock error events are not routed to**~~** FAULT**~~**and**<br>~~**WARN**~~<br>1: Latched Clock error events are routed to~~FAULT~~ and~~ WARN~~|
|5|CBC WARN FAULT GPIO|R/W|0x0|**0: Unlatched CBC warning events are not routed to** ~~**WARN**~~<br>1: Unlatched CBC warning events are routed to~~WARN~~|
|4|RTLDG LATCH FAULT<br>GPIO|R/W|0x0|**0: Latched Real-time load diagnostic events are not routed to**<br>~~**FAULT**~~ <br>1: Latched Real-time load diagnostic events are routed to~~FAULT~~|
|3-2|RESERVED|R/W|0x0||
|1|CLIP WARN GPIO|R/W|0x0|**0: Non-latched Clip Detect events are not routed to** ~~**WARN**~~<br>1: Non-latched Clip Detect events are routed to~~WARN~~|
|0|RTLDG LATCH WARN<br>GPIO|R/W|0x0|**0: Latched Real-time load diagnostic events are not routed to**<br>~~**WARN**~~<br>1: Latched Real-time load diagnostic events are routed to~~WARN~~|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 139


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.69 GPIO1_OUTPUT_SELECT Register (Address = 0x95) [Reset = 0x00]**


GPIO1_OUTPUT_SELECT is shown in Figure 10-69 and described in Table 10-71.


Return to the Summary Table.


Select Signals to GPIOs


**Figure 10-69. GPIO1_OUTPUT_SELECT Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|RESERVED|GPIO1 OUTPUT|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-71. GPIO1_OUTPUT_SELECT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R/W|0x0||
|5|RESERVED|R/W|0x0|Reserved|
|4-0|GPIO1 OUTPUT|R/W|0x0|GPIO1 pin output function<br>**0x00: LOW**<br>0x06: Auto Mute Channel 1<br>0x09:SDOUT1<br>0x0A:~~WARN~~<br>0x0B:~~FAULT~~<br>0x0E: Clock sync to secondary devices(e.g.DCDC)<br>0x0F: Clock Error<br>All other values are RESERVED|



140 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.70 GPIO2_OUTPUT_SELECT Register (Address = 0x96) [Reset = 0x0B]**


GPIO2_OUTPUT_SELECT is shown in Figure 10-70 and described in Table 10-72.


Return to the Summary Table.


Select Signals to GPIOs


**Figure 10-70. GPIO2_OUTPUT_SELECT Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|RESERVED|GPIO2 OUTPUT|
|R/W-0x0<br>R/W-0x0<br>R/W-0xB|R/W-0x0<br>R/W-0x0<br>R/W-0xB|R/W-0x0<br>R/W-0x0<br>R/W-0xB|



**Table 10-72. GPIO2_OUTPUT_SELECT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|RESERVED|R/W|0x0||
|5|RESERVED|R/W|0x0|Reserved|
|4-0|GPIO2 OUTPUT|R/W|0xB|GPIO2 pin output function<br>0x00: LOW<br>0x06: Auto Mute Channel 1<br>0x09:SDOUT1<br>0x0A:~~WARN~~<br>**0x0B:**~~**FAULT**~~ <br>0x0E: Clock sync to secondary devices(e.g.DCDC)<br>0x0F: Clock Error<br>All other values are RESERVED|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 141


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.71 GPIO_INPUT_SLEEP_HIZ Register (Address = 0x9B) [Reset = 0x00]**


GPIO_INPUT_SLEEP_HIZ is shown in Figure 10-71 and described in Table 10-73.


Return to the Summary Table.


Select Signals from GPIOs


**Figure 10-71. GPIO_INPUT_SLEEP_HIZ Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|GPIO INPUT FOR DEEP SLEEP|RESERVED|GPIO INPUT FOR HI Z|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-73. GPIO_INPUT_SLEEP_HIZ Register Field Descriptions**







|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6-4|GPIO INPUT FOR DEEP<br>SLEEP|R/W|0x0|GPIO Source for DEEP SLEEP state<br>Configures the GPIO pin to set the device into DEEP SLEEP state<br>**000: N/A**<br>001: GPIO1<br>010: GPIO2<br>others: Reserved|
|3|RESERVED|R/W|0x0||
|2-0|GPIO INPUT FOR HI Z|R/W|0x0|GPIO Source for Hi-Z state<br>Configures the GPIO pin to set the device channels into Hi-Z state<br>**000: N/A**<br>001: GPIO1<br>010: GPIO2<br>others: Reserved|


142 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.72 GPIO_INPUT_PLAY_SLEEP Register (Address = 0x9C) [Reset = 0x00]**


GPIO_INPUT_PLAY_SLEEP is shown in Figure 10-72 and described in Table 10-74.


Return to the Summary Table.


Select Signals from GPIOs


**Figure 10-72. GPIO_INPUT_PLAY_SLEEP Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|GPIO INPUT PLAY|RESERVED|GPIO INPUT SLEEP|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-74. GPIO_INPUT_PLAY_SLEEP Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6-4|GPIO INPUT PLAY|R/W|0x0|GPIO Source for PLAY state<br>Configures the GPIO pin to set the device channels into PLAY state<br>**000: N/A**<br>001: GPIO1<br>010: GPIO2<br>others: Reserved|
|3|RESERVED|R/W|0x0||
|2-0|GPIO INPUT SLEEP|R/W|0x0|GPIO Source for SLEEP state<br>Configures the GPIO pin to set the device into SLEEP state<br>**000: N/A**<br>001: GPIO1<br>010: GPIO2<br>others: Reserved|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 143


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.73 GPIO_INPUT_MUTE Register (Address = 0x9D) [Reset = 0x00]**


GPIO_INPUT_MUTE is shown in Figure 10-73 and described in Table 10-75.


Return to the Summary Table.


Select Signals from GPIOs


**Figure 10-73. GPIO_INPUT_MUTE Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|RESERVED|RESERVED|GPIO INPUT MUTE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-75. GPIO_INPUT_MUTE Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6-4|RESERVED|R/W|0x0|Reserved|
|3|RESERVED|R/W|0x0||
|2-0|GPIO INPUT MUTE|R/W|0x0|GPIO Source for~~ MUTE~~<br>Configures the GPIO pin to control MUTE for all channels<br>**000: N/A**<br>001: GPIO1<br>010: GPIO2<br>others: Reserved|



144 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.74 GPIO_INPUT_SYNC Register (Address = 0x9E) [Reset = 0x00]**


GPIO_INPUT_SYNC is shown in Figure 10-74 and described in Table 10-76.


Return to the Summary Table.


Select Signals from GPIOs


**Figure 10-74. GPIO_INPUT_SYNC Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|RESERVED|RESERVED|GPIO INPUT SYNC|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-76. GPIO_INPUT_SYNC Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0|Reserved|
|6-4|RESERVED|R/W|0x0|Reserved|
|3|RESERVED|R/W|0x0||
|2-0|GPIO INPUT SYNC|R/W|0x0|GPIO Source for Phase Sync<br>Configures the GPIO pin become the input to sync phase with<br>another device in target configuration<br>**000: N/A**<br>001: GPIO1<br>010: GPIO2<br>others: Reserved|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 145


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.75 GPIO_CTRL Register (Address = 0xA0) [Reset = 0x40]**


GPIO_CTRL is shown in Figure 10-75 and described in Table 10-77.


Return to the Summary Table.


General GPIO Control


**Figure 10-75. GPIO_CTRL Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|GPIO1 IO<br>SELECT|GPIO2 IO<br>SELECT|RESERVED|GPO1 MODE|GPO2 MODE|RESERVED|
|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-77. GPIO_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|GPIO1 IO SELECT|R/W|0x0|**0: Set GPIO1 as input**<br>1: Set GPIO1 as output|
|6|GPIO2 IO SELECT|R/W|0x1|0: Set GPIO2 as input<br>**1: Set GPIO2 as output**|
|5-4|RESERVED|R/W|0x0||
|3|GPO1 MODE|R/W|0x0|Set GPIO1 as open drain. This bit only applies to GPO functions with<br>Output buffer mode and has no effect on functions that use Open<br>Drain mode by default<br>**0: Output Buffer mode**<br>1: Open drain mode|
|2|GPO2 MODE|R/W|0x0|Set GPIO2 as open drain. This bit only applies to GPO functions with<br>Output buffer mode and has no effect on functions that use Open<br>Drain mode by default<br>**0: Output Buffer mode**<br>1: Open drain mode|
|1-0|RESERVED|R/W|0x0||



146 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.76 GPIO_INVERT Register (Address = 0xA1) [Reset = 0x00]**


GPIO_INVERT is shown in Figure 10-76 and described in Table 10-78.


Return to the Summary Table.


Invert GPIO Signals


**Figure 10-76. GPIO_INVERT Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|GPO1 INV|GPO2 INV|RESERVED|GPO PU<br>DISABLE|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-78. GPIO_INVERT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|GPO1 INV|R/W|0x0|**0: GPIO1 Output signal is non-inverted**<br>1: GPIO1 Output signal is inverted|
|6|GPO2 INV|R/W|0x0|**0: GPIO2 Output signal is non-inverted**<br>1: GPIO2 Output signal is inverted|
|5-1|RESERVED|R/W|0x0||
|0|GPO PU DISABLE|R/W|0x0|**0: Enable pull-up of GP outputs in open drain**<br>1: Disable pull-up of GP outputs in open drain|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 147


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.77 DC_LDG_CTRL Register (Address = 0xB0) [Reset = 0x00]**


DC_LDG_CTRL is shown in Figure 10-77 and described in Table 10-79.


Return to the Summary Table.


DC Load Diagnostics Control


**Figure 10-77. DC_LDG_CTRL Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|LDG ABORT|LDG BUFFER WAIT TIME|RESERVED|LDG WAIT<br>BYPASS|LDG SLOL<br>DISABLE|LDG BYPASS|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-79. DC_LDG_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|LDG ABORT|R/W|0x0|**0: Normal operation**<br>1: Abort DC load diagnostic|
|6-5|LDG BUFFER WAIT TIME|R/W|0x0|**00: Buffer wait time 1ms**<br>01: Buffer wait time 2ms<br>10: Buffer wait time 5ms<br>11: Buffer wait time 10ms|
|4-3|RESERVED|R/W|0x0|Reserved|
|2|LDG WAIT BYPASS|R/W|0x0|**0: Enable the waiting loop at the end of shorted / open load**<br>**detection**<br>1: Bypass the waiting loop at the end of shorted / open load<br>detection|
|1|LDG SLOL DISABLE|R/W|0x0|**0: Shorted load and open load detection are enabled**<br>1: Shorted load, open load and line out out detection are disabled|
|0|LDG BYPASS|R/W|0x0|**0: Automatic DC diagnostic after a channel fault occurs in Hi-Z**<br>**or PLAY state**<br>1: DC diagnostic will not run automatically after a channel fault<br>occurs|



148 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.78 DC_LDG_LO_CTRL Register (Address = 0xB1) [Reset = 0x00]**


DC_LDG_LO_CTRL is shown in Figure 10-78 and described in Table 10-80.


Return to the Summary Table.


DC Load Diagnostic Line-out Control


**Figure 10-78. DC_LDG_LO_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|RESERVED|RESERVED|RESERVED|CH1 LO LDG<br>ENABLE|RESERVED|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-80. DC_LDG_LO_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|RESERVED|R/W|0x0||
|6|RESERVED|R/W|0x0|Reserved|
|5-4|RESERVED|R/W|0x0|Reserved|
|3|CH1 LO LDG ENABLE|R/W|0x0|**0: Disable DC Load Diagnostics to check for line-out load on**<br>**Channel 1**<br>1: Enable DC Load Diagnostics to check for line-out load on Channel<br>1|
|2-0|RESERVED|R/W|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 149


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.79 DC_LDG_TIME_CTRL Register (Address = 0xB2) [Reset = 0x00]**


DC_LDG_TIME_CTRL is shown in Figure 10-79 and described in Table 10-81.


Return to the Summary Table.


DC Load Diagnostic Timing Control


**Figure 10-79. DC_LDG_TIME_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|LDG RAMP SL OL|LDG SETTLING SL OL|LDG RAMP S2PG|LDG SETTLING S2PG|
|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|



**Table 10-81. DC_LDG_TIME_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-6|LDG RAMP SL OL|R/W|0x0|Ramp time, shorted load and open load diagnostics<br>**00: 10 ms**<br>01: 5 ms<br>10: 20 ms<br>11: 15 ms|
|5-4|LDG SETTLING SL OL|R/W|0x0|Settling time, shorted load and open load diagnostics<br>**00: 15 ms**<br>01: 30 ms<br>10: 10 ms<br>11: 20 ms|
|3-2|LDG RAMP S2PG|R/W|0x0|Ramp time, short to power and short to ground diagnostics<br>**00: 5 ms**<br>01: 2.5 ms<br>10: 10 ms<br>11: 15 ms|
|1-0|LDG SETTLING S2PG|R/W|0x0|Settling time, short to power and short to ground diagnostics<br>**00: 10ms**<br>01: 5 ms<br>10: 20 ms<br>11: 30 ms|



150 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.80 DC_LDG_SL_CTRL Register (Address = 0xB3) [Reset = 0x11]**


DC_LDG_SL_CTRL is shown in Figure 10-80 and described in Table 10-82.


Return to the Summary Table.


DC Load Diagnostic Shorted-load Threshold


**Figure 10-80. DC_LDG_SL_CTRL Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|CH1 DC LDG SL|RESERVED|
|R/W-0x1<br>R/W-0x1|R/W-0x1<br>R/W-0x1|



**Table 10-82. DC_LDG_SL_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|CH1 DC LDG SL|R/W|0x1|DC load diagnostic shorted-load threshold Channel 1<br>0000 : 0.5Ω<br>**0001 : 1Ω**<br>0010 : 1.5Ω<br>...<br>1001 : 5Ω|
|3-0|RESERVED|R/W|0x1||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 151


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.81 AC_LDG_CTRL Register (Address = 0xB5) [Reset = 0x10]**


AC_LDG_CTRL is shown in Figure 10-81 and described in Table 10-83.


Return to the Summary Table.


AC Load Diagnostic Control


**Figure 10-81. AC_LDG_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|RESERVED|AC DIAG GAIN|CH1 AC DIAG<br>START|RESERVED|
|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0|


**Table 10-83. AC_LDG_CTRL Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-5|RESERVED|R/W|0x0||
|4|AC DIAG GAIN|R/W|0x1|Used together with 0xB7 to select tweeter detection threshold.<br>0: Gain 1<br>**1: Gain 8**|
|3|CH1 AC DIAG START|R/W|0x0|**0: Normal operation**<br>1: Start AC diagnostic on channel 1 once channel is in Hi-Z mode|
|2-0|RESERVED|R/W|0x0||



152 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.82 TWEETER_DETECT_CTRL Register (Address = 0xB6) [Reset = 0x08]**


TWEETER_DETECT_CTRL is shown in Figure 10-82 and described in Table 10-84.


Return to the Summary Table.


Tweeter Detection Control


**Figure 10-82. TWEETER_DETECT_CTRL Register**







|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|RESERVED|RESERVED|RESERVED|TWEETWER<br>DETECT CALC<br>TYPE|TWEETER<br>DETECT<br>DISABLE|
|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|R/W-0x0<br>R/W-0x1<br>R/W-0x0<br>R/W-0x0<br>R/W-0x0|


**Table 10-84. TWEETER_DETECT_CTRL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R/W|0x0||
|3|RESERVED|R/W|0x1|Reserved|
|2|RESERVED|R/W|0x0|Reserved|
|1|TWEETWER DETECT<br>CALC TYPE|R/W|0x0|**0: AC pass/fail judgement type 2**<br>Calculate magnitude of impedance as Re(Z)+0.5*Im(Z)<br>1: AC pass/fail judgement type 1<br>Calculate magnitude of impedance as Re(Z)|
|0|TWEETER DETECT<br>DISABLE|R/W|0x0|Calculate magnitude of impedance<br>Check whether calculated result is lower than tweeter detection<br>threshold value<br>If yes, set tweeter detection bit.<br>**0: Enable Tweeter detection judgement**<br>1: Disable Tweeter detection calculation|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 153


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.83 TWEETER_DETECT_THRESH Register (Address = 0xB7) [Reset = 0x00]**


TWEETER_DETECT_THRESH is shown in Figure 10-83 and described in Table 10-85.


Return to the Summary Table.


Tweeter Detection Threshold


**Figure 10-83. TWEETER_DETECT_THRESH Register**





**Table 10-85. TWEETER_DETECT_THRESH Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|TWEETER DETECT<br>THRESHOLD|R/W|0x0|Set the reference value for AC load diagnostics pass/fail judgement.<br>If AC DIAG GAIN in AC_LDG_CTRL(0xB5) = 0: Bit value x 0.8 Ω/<br>code<br>If AC DIAG GAIN in AC_LDG_CTRL(0xB5) = 1: Bit value x 0.1 Ω/<br>code|



154 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.84 AC_LDG_FREQ_CTRL Register (Address = 0xB8) [Reset = 0xC8]**


AC_LDG_FREQ_CTRL is shown in Figure 10-84 and described in Table 10-86.


Return to the Summary Table.


AC Load Diagnostic Frequency Control


**Figure 10-84. AC_LDG_FREQ_CTRL Register**





**Table 10-86. AC_LDG_FREQ_CTRL Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|AC LDG STIMULUS<br>FREQUENCY|R/W|0xC8|Frquency = 93.75Hz * bit value<br>0000 0000: Reserved<br>0000 0001: 93.75Hz<br>0000 0010: 187.5Hz<br>0000 0011: 281.25Hz<br>....<br>**1100 1000: 18.75kHz**<br>....<br>1111 1111: 23.91kHz|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 155


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.85 DC_LDG_REPORT Register (Address = 0xC0) [Reset = 0x00]**


DC_LDG_REPORT is shown in Figure 10-85 and described in Table 10-87.


Return to the Summary Table.


DC Load Diagnostic Report


**Figure 10-85. DC_LDG_REPORT Register**

|7 6 5 4 3 2 1 0|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|CH1 S2G|CH1 S2P|CH1 OL|CH1 SL|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|



**Table 10-87. DC_LDG_REPORT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 S2G|R|0x0|**0: No short-to-GND detected on Channel 1**<br>1: Short-to-GND detected on Channel 1|
|6|CH1 S2P|R|0x0|**0: No short-to-power detected on Channel 1**<br>1: Short-to-power detected on Channel 1|
|5|CH1 OL|R|0x0|**0: No open load detected on Channel 1**<br>1: Open load detected on Channel 1|
|4|CH1 SL|R|0x0|**0: No shorted load detected on Channel 1**<br>1: Shorted load detected on Channel 1|
|3-0|RESERVED|R|0x0||



156 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.86 DC_LDG_RESULT Register (Address = 0xC2) [Reset = 0x00]**


DC_LDG_RESULT is shown in Figure 10-86 and described in Table 10-88.


Return to the Summary Table.


DC Load Diagnostic Result Report


**Figure 10-86. DC_LDG_RESULT Register**









|7 6 5 4 3 2 1 0|Col2|Col3|Col4|
|---|---|---|---|
|CH1 LO LDG<br>RESULT|RESERVED|CH1 DC LDG<br>RESULT|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0<br>R-0x0|


**Table 10-88. DC_LDG_RESULT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7|CH1 LO LDG RESULT|R|0x0|**0: Lineout load not detected on Channel 1**<br>1: Lineout load detected on Channel 1|
|6-4|RESERVED|R|0x0||
|3|CH1 DC LDG RESULT|R|0x0|**0: DC Load Diagnostic did not complete without faults on**<br>**channel 1**<br>1: DC Load Diagnostic completed without faults on channel 1|
|2-0|RESERVED|R|0x0||



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 157


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.87 AC_LDG_REPORT_CH1_R Register (Address = 0xC3) [Reset = 0x00]**


AC_LDG_REPORT_CH1_R is shown in Figure 10-87 and described in Table 10-89.


Return to the Summary Table.


AC Load Diagnostic Report Real Channel 1


**Figure 10-87. AC_LDG_REPORT_CH1_R Register**





**Table 10-89. AC_LDG_REPORT_CH1_R Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 AC IMP R|R|0x0|Register value corresponds to real part of complex impedance seen<br>at Channel 1 output<br>MSB determines the leading sign (0: positive, 1: negative)<br>0.8Ω/code if AC DIAG GAIN in 0xB5 = 0<br>0.1Ω/code if AC DIAG GAIN in 0xB5 = 1|



158 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.88 AC_LDG_REPORT_CH1_I Register (Address = 0xC4) [Reset = 0x00]**


AC_LDG_REPORT_CH1_I is shown in Figure 10-88 and described in Table 10-90.


Return to the Summary Table.


AC Load Diagnostic Report Imaginary Channel 1


**Figure 10-88. AC_LDG_REPORT_CH1_I Register**





**Table 10-90. AC_LDG_REPORT_CH1_I Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 AC IMP I|R|0x0|Register value corresponds to imaginary part of complex impedance<br>seen at Channel 1 output<br>MSB determines the leading sign (0: positive, 1: negative)<br>0.8Ω/code if AC DIAG GAIN in 0xB5 = 0<br>0.1Ω/code if AC DIAG GAIN in 0xB5 = 1|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 159


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.89 DC_LDG_DCR_MSB Register (Address = 0xC5) [Reset = 0x00]**


DC_LDG_DCR_MSB is shown in Figure 10-89 and described in Table 10-91.


Return to the Summary Table.


DC Diagnostic DC Resistance Measurement MSB


**Figure 10-89. DC_LDG_DCR_MSB Register**

|7 6 5 4 3 2 1 0|Col2|
|---|---|
|RESERVED|CH1 DC RESISTANCE MSB|
|R-0x0<br>R-0x0|R-0x0<br>R-0x0|



**Table 10-91. DC_LDG_DCR_MSB Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-2|RESERVED|R|0x0||
|1-0|CH1 DC RESISTANCE<br>MSB|R|0x0|MSB for DC Diagnostics resistance measurement, refer to<br>DC_LDG_DCR_LSB (0xC6)|



160 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.90 DC_LDG_DCR_LSB Register (Address = 0xC6) [Reset = 0x00]**


DC_LDG_DCR_LSB is shown in Figure 10-90 and described in Table 10-92.


Return to the Summary Table.


DC Diagnostic DC Resistance Measurement LSB


**Figure 10-90. DC_LDG_DCR_LSB Register**





**Table 10-92. DC_LDG_DCR_LSB Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 DC RESISTANCE<br>LSB|R|0x0|Channel 1 DC Load diagnostics resistance measurement. Combine<br>with MSB in 0xC5.<br>0.1Ω/code.|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 161


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.91 TWEETER_REPORT Register (Address = 0xCB) [Reset = 0x00]**


TWEETER_REPORT is shown in Figure 10-91 and described in Table 10-93.


Return to the Summary Table.


Tweeter Detection Report


**Figure 10-91. TWEETER_REPORT Register**

|7 6 5 4 3 2 1 0|Col2|Col3|
|---|---|---|
|RESERVED|CH1 TW DET|RESERVED|
|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|R-0x0<br>R-0x0<br>R-0x0|



**Table 10-93. TWEETER_REPORT Register Field Descriptions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-4|RESERVED|R|0x0||
|3|CH1 TW DET|R|0x0|**0: No tweeter detected on Channel 1**<br>1: Tweeter detected on Channel 1|
|2-0|RESERVED|R|0x0||



162 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**10.1.92 CH1_RTLDG_IMP_MSB Register (Address = 0xD1) [Reset = 0x00]**


CH1_RTLDG_IMP_MSB is shown in Figure 10-92 and described in Table 10-94.


Return to the Summary Table.


Real-time Load Diagnostic Channel 1 Impedance MSB


**Figure 10-92. CH1_RTLDG_IMP_MSB Register**





**Table 10-94. CH1_RTLDG_IMP_MSB Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 RTLDG IMPEDANCE<br>MSB|R|0x0|Combine with LSB in register 0xD2 for RTLDG impedance|



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 163


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**10.1.93 CH1_RTLDG_IMP_LSB Register (Address = 0xD2) [Reset = 0x00]**


CH1_RTLDG_IMP_LSB is shown in Figure 10-93 and described in Table 10-95.


Return to the Summary Table.


Real-time Load Diagnostic Channel 1 Impedance LSB


**Figure 10-93. CH1_RTLDG_IMP_LSB Register**





**Table 10-95. CH1_RTLDG_IMP_LSB Register Field Descriptions**






|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|7-0|CH1 RTLDG IMPEDANCE<br>LSB|R|0x0|Combined with MSB in 0xD1 for RTLDG impedance<br>Impedance reading is combined MSB and LSB in decimal, divided by<br>285|



164 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**11 Application and Implementation**


**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**11.1 Application Information**


The TAS6511-Q1 is a mono-channel digital input Class-D audio-amplifier design with integrated real time
Current Feedback and DSP for use in automotive head units, VESS, eCall, and external amplifier modules. The
TAS6511-Q1 incorporates the necessary functionality to perform in demanding automotive OEM applications.


_**11.1.1 AM Radio Avoidance**_


AM-radio frequency interference is avoided by setting the switching frequency of the device above the AM band.
When setting the switching frequency below the AM band, change the switching frequency to avoid the second
and third harmonic of the switching interfering with the AM band.


_**11.1.2 Reconstruction Filter Design**_


The amplifier outputs are driven by high-current LDMOS transistors in an H-bridge configuration. These
transistors are either fully off or fully on. The result is a square-wave output signal with a duty cycle that is
proportional to the amplitude of the audio signal. An LC demodulation filter is used to recover the audio signal.
The filter attenuates the high-frequency components of the output signals that are out of the audio band. The
design of the demodulation filter significantly affects the audio performance of the power amplifier. Therefore, to
meet the system THD+N requirements, the selection of the inductors used in the output filter should be carefully
considered.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 165


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**11.2 Typical Application**


_**11.2.1 BTL Application**_


Figure 11-1 shows the schematic for a typical single channel design.


PVDD

Input


PVDD


Bulk
Capacitor







































**Figure 11-1. Typical Application Schematic**


**11.2.1.1 Design Requirements**


The TAS6511-Q1 requires two power supplies compliant with the recommended operation range. The device is
designed to work with either a vehicle battery or regulated power supply such as from a backup battery.


_**11.2.1.1.1 Communication**_


All communications are through I [2] C protocol. A system controller set as the I [2] C primary can communicate with
the device through the SDA and SCL pins. The device cannot generate an I [2] C clock or initiate a transaction.
The device requires a primary host. The maximum clock speed accepted by the device is 400kHz. If multiple
TAS6511-Q1 devices are on the same I [2] C bus, the I [2] C address must be different for each device. Up to eight
TAS6511-Q1 devices can be on the same I [2] C bus.


**11.2.1.2 Detailed Design Procedure**


All communications are through I [2] C protocol. A system controller set as the I [2] C primary can communicate with
the device through the SDA and SCL pins. The device cannot generate an I [2] C clock or initiate a transaction.
The device requires a primary host. The maximum clock speed accepted by the device is 400kHz. If multiple
TAS6511-Q1 devices are on the same I [2] C bus, the I [2] C address must be different for each device. Up to eight
TAS6511-Q1 devices can be on the same I [2] C bus.


_**11.2.1.2.1 Hardware Design**_


166 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**


_**11.2.1.2.1.1 Digital Audio Input**_



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



The TAS6511-Q1 audio amplifier supports four different digital input formats which are: I [2] S, Left Justified, and
TDM/DSP mode. Depending on the format, the device can support 16, 20, 24, and 32 bit data. The supported
frequencies are 16 kHz, 32 kHz 48 kHz, 96 kHz, and 192 kHz. See the Serial Audio Port section for more details.


_**11.2.1.2.1.2 Power Supply Decoupling**_


The power supply decoupling has multiple functions. The large electrolytic capacitor is used to reduce the PVDD
voltage ripple due to the audio frequencies. The 1 µF MLCC on each group of PVDD pins is to reduce the PVDD
voltage ripple at the PWM switching frequency and the 100 nF is for EMI reduction.


The large electrolytic capacitor value is dependent on the regulation capabilities of the boost converter used. If a
battery is used with long wires, a larger value may be needed to reduce the voltage ripple in the audio band to
meet the output power requirements.


_**11.2.1.2.1.3 Bootstrap**_


The bootstrap capacitors provide the gate-drive voltage of the upper N-channel FET. These capacitors must be
sized appropriately for the system specification. A special condition can occur where the bootstrap sags if the
capacitor is not sized accordingly. The special condition is just below clipping where the PWM is slightly less
than 100% duty cycle with sustained low-frequency signals. Changing the bootstrap capacitor value to a larger
value for driving subwoofers that require frequencies below 30Hz can be necessary.


_**11.2.1.2.1.4 Reconstruction LC Filters**_


The values of the inductor and the capacitor on the LC filter is determined by the PWM frequency and the
required audio bandwidth of the amplifier. The PWM can vary from 384 kHz to 2.048 MHz. There are two groups
of PWM frequencies to determine the LC Filter. The lower frequencies from 384 kHz to 624 kHz, and the higher
frequencies, 1.024 MHz and 2.048 MHz. The lower frequency cutoff should be less than 40 kHz, where the
higher frequency cutoff can be as high as 100 kHz.


The application note [LC Filter Design and the](https://www.ti.com/lit/pdf/slaa701) [Class-D LC Filter Designer will provide the tools necessary to](https://www.ti.com/tool/LCFILTER-CALC-TOOL)
design the LC filter.


**11.3 Power Supply Recommendations**


The TAS6511-Q1 requires two power supplies. The PVDD supply is the high-current supply in the recommended
supply range. The DVDD supply is the 1.8Vdc or 3.3Vdc logic supply and must be maintained in the tolerance as
shown in the Recommended Operating Conditions.


**11.4 Layout**


_**11.4.1 Layout Guidelines**_


The TAS6511-Q1 EVM layout optimizes for thermal dissipation and EMC performance. The TAS6511-Q1 device
has a thermal pad down, and good thermal conduction and dissipation require adequate copper area. Layout
also affects EMC performance. See Section 11.2 for a typical application schematic and Section 11.4.3 for an
example layout.


**11.4.1.1 EMI Considerations**


Automotive-level EMI performance depends on both careful integrated circuit design and good system-level
design. Controlling sources of electromagnetic interference (EMI) was a major consideration in all aspects of the
design. The design has minimal parasitic inductances because of the short leads on the package which reduces
the EMI that results from current passing from the die to the system PCB. The design also incorporates circuitry
that optimizes output transitions that cause EMI.


_**11.4.1.1.1 General Guidelines**_


 - The ground connections for the capacitors in the LC filter have a direct path back to the device and also the
ground return. This direct path allows for improved common mode EMI rejection. This is on the same layer of
the pcb as the TAS6511-Q1.

 - Traces that carry large currents incorporate multiple vias to reduce the series impedance of these traces.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 167


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


 - The decoupling capacitors on PVDD, is very close to the device with the ground return close to the ground
pins.

 - A ground plane, on the same side as the device pins helps reduce EMI by providing a very-low loop
impedance for the high-frequency switching current. This plane has many vias between the ground planes on
other layers.


168 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**12 Device and Documentation Support**


TI offers an extensive line of development tools. Tools and software to evaluate the performance of the device,
generate code, and develop designs are listed below.


**12.1 Device Support**


**12.2 Documentation Support**


_**12.2.1 Related Documentation**_


**12.3 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Notifications_ to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.


**12.4 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**12.5 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

**12.6 Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**12.7 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**13 Revision History**
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.


**Changes from Revision A (December 2024) to Revision B (April 2025)** **Page**

 - Updated 14.4V, 4Ω, 10% THD+N output power to 30W.....................................................................................1

 - Deleted Supply-voltage ramp rate - PVDD Load Dump in Absolute Maximum Ratings.....................................5

 - Deleted outdated note #3 under Thermal Information........................................................................................6

 - Added additional Output power specifications....................................................................................................7

 - Changed links to reflect section names instead of section numbers throughout the document.......................21

 - Updated Vpredict description............................................................................................................................31

 - Added Mechanical, Packaging, and Orderable Information section...............................................................170


**Changes from Revision * (December 2023) to Revision A (December 2024)** **Page**

 - Updated device status to production data.......................................................................................................... 1


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 169


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**14 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


170 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



**[www.ti.com](https://www.ti.com)**


**14.1 Package Option Addendum**


**Packaging Information**



_TI Information - Selective Disclosure_








|Orderable Device|Status(1)|Package<br>Type|Package<br>Drawing|Pins|Package Qty|Eco Plan(2)|Lead/Ball<br>Finish(6)|MSL Peak<br>Temp(3)|Op Temp (°C)|Device<br>Marking(4) (5)|
|---|---|---|---|---|---|---|---|---|---|---|
|TAS6511QPWPRQ1|ACTIVE|HTSSOP|PWP|28|2000|RoHS &<br>Green|NIPDAU|Level-3-260C-<br>168 HR|-40 to 125C|TAS6511|



(1) The marketing status values are defined as follows:
**ACTIVE:** Product device recommended for new designs.
**LIFEBUY:** TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
**NRND:** Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
**PRE_PROD** Unannounced device, not in production, not available for mass market, nor on the web, samples not available.
**PREVIEW:** Device has been announced but is not in production. Samples may or may not be available.
**OBSOLETE:** TI has discontinued the production of the device.
(2) [Eco Plan - The planned eco-friendly classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS & no Sb/Br) - please check www.ti.com/productcontent for the latest](https://www.ti.com/productcontent)
availability information and additional product content details.
**TBD:** The Pb-Free/Green conversion plan has not been defined.
**Pb-Free (RoHS):** TI's terms "Lead-Free" or "Pb-Free" mean semiconductor products that are compatible with the current RoHS requirements for all 6 substances, including the
requirement that lead not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, TI Pb-Free products are suitable for use in specified
lead-free processes.
**Pb-Free (RoHS Exempt):** This component has a RoHS exemption for either 1) lead-based flip-chip solder bumps used between the die and package, or 2) lead-based die adhesive used
between the die and leadframe. The component is otherwise considered Pb-Free (RoHS compatible) as defined above.
Green (RoHS & no Sb/Br): TI defines "Green" to mean Pb-Free (RoHS compatible), and free of Bromine (Br) and Antimony (Sb) based flame retardants (Br or Sb do not exceed 0.1% by
weight in homogeneous material).
(3) MSL, Peak Temp. -- The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.
(4) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.
(5) Multiple Device markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a
continuation of the previous line and the two combined represent the entire Device Marking for that device.
(6) Lead/Ball Finish - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead/Ball Finish values may wrap to two lines if the
finish value exceeds the maximum column width.


**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on
information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties.
TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming
materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.


In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 171


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


**14.2 Tape and Reel Information**



**REEL DIMENSIONS**





|Col1|A0 Cavity|
|---|---|
|A0|Dimension designed to accommodate the component width|
|B0|Dimension designed to accommodate the component length|
|K0|Dimension designed to accommodate the component thickness|
|W|Overall width of the carrier tape|
|P1|Pitch between successive cavity centers|


Reel Width (W1)



**TAPE DIMENSIONS**


|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||B0W|
||||||||
||||||||
|vity|vity|vity|A0|A0|||







**QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE**


Sprocket Holes



|Q1|Q2|
|---|---|
|Q3|Q4|


|Q1|Q2|
|---|---|
|Q3|Q4|


Pocket Quadrants



User Direction of Feed























|Device|Package<br>Type|Package<br>Drawing|Pins|SPQ|Reel<br>Diameter<br>(mm)|Reel<br>Width W1<br>(mm)|A0<br>(mm)|B0<br>(mm)|K0<br>(mm)|P1<br>(mm)|W<br>(mm)|Pin1<br>Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TAS6511QPWPRQ1|HTSSOP|PWP|28|2000|330.0|16.4|6.9|10.2|1.8|12.0|16.0|Q1|


172 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|TAS6511QPWPRQ1|HTSSOP|PWP|28|2000|356.0|356.0|35.0|


Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 173


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


174 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


**[www.ti.com](https://www.ti.com)**



_TI Information - Selective Disclosure_


**TAS6511-Q1**

SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025



Copyright © 2025 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ 175


_TI Information - Selective Disclosure_


**TAS6511-Q1**
SLOSEA3B – DECEMBER 2023 – REVISED APRIL 2025 **[www.ti.com](https://www.ti.com)**


176 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLOSEA3B&partnum=TAS6511-Q1)_ Copyright © 2025 Texas Instruments Incorporated


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


