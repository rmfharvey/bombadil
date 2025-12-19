
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




