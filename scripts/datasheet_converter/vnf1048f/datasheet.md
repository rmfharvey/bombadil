# **VNF1048F**
### Datasheet
## High-side switch controller with intelligent fuse protection for 12 V, 24 V and 48 V automotive applications

**QFN32L Epad**

|Features|Col2|Col3|
|---|---|---|
|Maximum transient supply voltage|VS|70 V|
|Operating voltage range|VS|6 V to 60 V|
|Operating voltage range (extended)|VS|6 V to 70 V|
|Standby current (max.)|IS_Q|70 µA|
|SPI I/O supply voltage|VSPI|3 V to 5.5 V|
|SPI standby current (max.)|I_STBY|5 µA|


**Product status link**



- AEC-Q100 qualified

- General

–
High-side switch control IC with eFuse protection for 12 V, 24 V, and
48 V automotive applications

–
SPI secondary interface for host control

–
32-bit ST-SPI interface compatible with 3.3 V and 5 V CMOS level

–
2 stage charge pump

–
Gate drive for an external MOSFET in high-side configuration

–
High precision uni-directional digital current sense via SPI through an
external high-side shunt resistor

–
Input for an NTC resistor to monitor the external MOSFET temperature

–
Very low standby current

–
Robust fail-safe functionality through internal and external controls

–
SPI register lock-out by a dedicated digital input pin

–
Integrated ADC for T J, VNTC, VOUT, and VDS conversion

- Protections

–
Battery undervoltage shutdown

–
External MOSFET desaturation shutdown configurable via SPI

–
Hard short circuit latch-off configurable via SPI

–
Current vs time latch-off configurable via SPI (fuse-emulation)

–
Device overtemperature shutdown

–
External MOSFET overtemperature shutdown

- Intelligent high current fuse replacement for automotive applications

- Especially, intended for automotive power distribution applications
### **Description**

[The VNF1048F is an advanced controller for Power MOSFET in high-side](https://www.st.com/en/product/VNF1048F?ecmp=tt9470_gl_link_feb2019&rt=ds&id=DS13084)
configuration, designed for the implementation of an intelligent high-side switch for 12
V, 24 V, and 48 V automotive applications. The control IC is interfaced to a host
microcontroller through a 3.3 V and 5 V CMOS-compatible SPI interface and
provides protection and diagnostics to the system.


[VNF1048F](https://www.st.com/en/product/VNF1048F?ecmp=tt9470_gl_link_feb2019&rt=ds&id=DS13084)

|Product summary|Col2|
|---|---|
|Order code|VNF1048FTR|
|Package|QFN32L|
|Packing|Tape and reel|


**DS13084** - **Rev 8** - **November 2023**
For further information contact your local STMicroelectronics sales office.


www.st.com


-----

## **1 Block diagram and pin description**

**Figure 1. Block diagram**

Vs

CP

CP2P

CP1P

CP1M

V3V3

VSPI

CSN

SCK

DIAG

HWLO

GND

### **VNF1048F**

**Block diagram and pin description**

HS_GATE

OUT

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
|Gate Driver HS|||||
||||||
||||||
||||||
||||||
||||||

|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||||
||||
||||
||||
||||
|||24-bit SPI|
||||
||||
||||
||||
||||
||||
||||
||||


GADG021120231259GT

**Figure 2. Device pin connection diagram (top through view - not in scale)**


VSPI

CSN

SDI

SDO

SCK

DIAG

TEST1

TEST2


HS_GATE

OUT

NC

ISNS_P

ISNS_N

NTC

NTC_M

NC


*Note:* *TAB connection must be to ground. TAB is not intended as device reference ground (dedicated pin shall be*
*used).*

**DS13084** - **Rev 8** **page 2/49**


-----

### **VNF1048F**

**Block diagram and pin description**

|Col1|Col2|Table 1. Pin functions|
|---|---|---|
|Pin #|Name|Function|
|TAB|GND|TAB connection must be to ground. TAB is not intended as device reference ground (dedicated pin shall be used).|
|1|VSPI|DC supply input for the SPI interface. 3.3 V and 5 V compatible.|
|2|CSN|Chip select not (active low) for SPI communication. It is the selection pin of the device. CMOS compatible input.|
|3|SDI|Serial data input for SPI communication. Data is transferred serially into the device on the SCK rising edge.|
|4|SDO|Serial data output for SPI communication. Data is transferred serially out of the device on the SCK falling edge.|
|5|SCK|Serial clock for SPI communication. It is a CMOS compatible input.|
|6|DIAG|Open-drain logic output. Diagnostic feedback. DIAG = '0' if (SR1.WAKEUPM = '1') or (GSB.DIAGS = '1') or (GSB.DE = '1') else '1'|
|7|TEST1|Test mode pin 1- must be connected to the ground.|
|8|TEST2|Test mode pin 2- must be connected to the ground.|
|9|NC|Not connected pin.|
|10|HWLO|Active high input pin compatible with 3.3 V and 5 V CMOS; it causes transitions to states where the registers are locked from writing.|
|11|NC|Not connected pin.|
|12|V3V3|Output of the 3.3 V internal LDO voltage regulator (logic and I/O supply). Connect a low ESR capacitor (1 μF) close to this pin.|
|13|GND|Ground connection.|
|14-17|NC|Not connected pin.|
|18|NTC_M|Negative input pin for external NTC resistor.|
|19|NTC|Positive input pin for external NTC resistor.|
|20|ISNS_N|Current sense amplifier negative input.|
|21|ISNS_P|Current sense amplifier positive input.|
|22|NC|Not connected pin.|
|23|OUT|External FET source connection.|
|24|HS_GATE|Output of the gate driver for the external FET.|
|25|VS|Input supply pin. Connect to the 12 V, 24 V, 48 V battery voltage.|
|26|NC|Not connected pin.|
|27|CP|Charge pump output.|
|28|CP2P|Charge pump–Positive terminal of the flying capacitor C . P2|
|29|CP2M|Charge pump–Negative terminal of the flying capacitor C . P2|
|30|CP1P|Charge pump–Positive terminal of the flying capacitor C . P1|
|31|CP1M|Charge pump–Negative terminal of the flying capacitor C . P1|
|32|NC|Not connected pin.|



**DS13084** - **Rev 8** **page 3/49**


-----

### **VNF1048F**

**Electrical specification**
## **2 Electrical specification**
### **2.1 Absolute maximum ratings**

Stressing the device above the rating listed in Table 2 may cause permanent damage to the device. These are
stress ratings only and operation of the device at these or any other conditions above those indicated in the
operating sections of this specification is not implied. Exposure to the conditions in the table below for extended
periods may affect device reliability.

**Table 2. Absolute maximum ratings**

*1.* *All pins except corners.*

*2.* *Corner pins.*

|Symbol|Parameter|Value|Unit|
|---|---|---|---|
|V S|DC supply voltage|-0.3 to 70|V|
|-I GND|DC reverse ground pin current|200|mA|
|V SPI|DC input voltage|-0.3 to 5.5|V|
|V 3V3|DC output voltage|-0.3 to 4.6|V|
|V, V, V CSN SDI SCK|SPI pins DC input voltage|-0.3 to 5.5|V|
|V SDO|SPI pins DC output voltage|-0.3 to V + 0.3 SPI|V|
|V HWLO|DC input voltage|-0.3 to 5.5|V|
|V DIAG|DC output voltage|-0.3 to V_SPI + 0.3|V|
|I DIAG|DC Input current|Internally limited if V < 3.3 V S|mA|
|V ISNS_P|DC input voltage|V - 0.3 to V + 0.3 S S|V|
|V ISNS_N|DC input voltage|V - 3.3 to V + 0.3 if V > 3.3 V S S S|V|
|||-0.3 to V + 0.3 if V < 3.3 V S S||
|V HS_GATE|DC output voltage|V - 0.3 V to V + 20 V if V < V - 20 V OUT OUT OUT CP|V|
|||V - 0.3 V to V + 0.3 V OUT CP||
|V OUT|DC output voltage|-2 to V + 3 S|V|
|V transient OUT|Transient output voltage|-10 to V + 3 for 10 µs max. S|V|
|V NTC|DC input voltage|-0.3 to V + 0.3 if V < 3.3 V S S|V|
|||V - 3.3 to V + 0.3 S S|V|
|V NTC_M|DC input voltage|-0.3 to V + 0.3 if V < 3.3 V S S|V|
|||V - 3.3 to V + 0.3 S S|V|
|V CP|DC input voltage|V -0.3 to V + 20 S S|V|
|V CP1P|DC input voltage|V - 0.3 to V + 20 S S|V|
|V CP2P|DC input voltage|V - 0.6 to V + 20 S S|V|
|V, V CP1M CP2M|DC input voltage|-0.3 to V + 0.3 S|V|
|V ESD|Electrostatic discharge (JEDEC 22A-114F)|2000|V|
||Charge device model (CDM-AEC-Q100-011)|±500(1)||
|||±750(2)||
|T J|Operating junction temperature range|-40 to 150|°C|
|T stg|Storage temperature range|-55 to 150|°C|



**DS13084** - **Rev 8** **page 4/49**


-----

### **VNF1048F**

**Electrical specification**

### **2.2 Thermal data**

*1.* *Device mounted on two-layer 2s0p PCB with 2 cm² heatsink copper trace*

|Col1|Table 3. Thermal data|Col3|Col4|
|---|---|---|---|
|Symbol|Parameter|Typ. value|Unit|
|R thJA|Thermal resistance, junction-to-ambient (JEDEC JESD 51-5) (1)|56|°C/W|
||Thermal resistance, junction-to-ambient (JEDEC JESD 51-7)|26|| **2.3 Main electrical characteristics**

6 V < V S < 60 V; -40 °C < T J < 150 °C, unless otherwise specified.

All typical values refer to V S = 48 V; T J = 25 °C, unless otherwise specified.

|Col1|Table 4. Supply|specification|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|V S|Operating supply voltage||6|48|60|V|
|V S_EXT|Extended operating supply voltage|100 ms max. duration|6||70|V|
|V S_USD|Undervoltage shutdown||4.5|||V|
|V S_USD_RES|Undervoltage shutdown reset||||6|V|
|V S_USD_HYS|Undervoltage shutdown hysteresis|||0.1||V|
|t VS_USD|Undervoltage shutdown filtering time.|||33||µs|
|V SPI|SPI I/Os supply voltage||3.0||5.5|V|
|I SPI|SPI supply current during frame communication||||3|mA|
|I SPI_STBY|SPI supply current in standby state||||5|µA|
|I S(ON)|Supply current (includes logic)|f = 1 Hz, Q = 250 nC, PWM G V = 48 V, OUT = V (1) S S||8|11|mA|
|||f = 1 Hz, Q = 250 nC, PWM G V = 48 V, OUT = V S S||12||mA|
|I OUT|Output current|V = 48 V, standby mode, S OUT = GND, bypass switch OFF|||250|μA|
|||V = 13 V, standby mode, S OUT = GND, bypass switch OFF|||75|μA|
|||V = 48 V, unlocked mode, S OUT = GND, bypass switch OFF|||1.3|mA|
|||V = 13 V, unlocked mode, S OUT = GND, bypass switch OFF|||1.15|mA|
|I S_Q|Vs quiescent current (includes logic)– independently from bypass switch condition|V = 48 V, T = 25 °C, OUT = V S J S|||80|µA|
|||V = 48 V, T = 25 °C, OUT = GND S J|||310|µA|
|||V = 13 V, T = 25 °C, OUT = V S J S|||70|µA|
|||V = 13 V, T = 25 °C, OUT = GND S J|||130|µA|
|V S_POR_ON|Power-on reset threshold. Device leaves the reset mode|||2.5||V|
|V S_POR_OFF|Power-on shutdown threshold. Device enters reset mode|||2.3||V|
|V S_POR_HYST|Power-on reset hysteresis|||0.2||V|


**DS13084** - **Rev 8** **page 5/49**


-----

### **VNF1048F**

**Electrical specification**

*1.* *Measured in test mode with the charge pump off.*

**Table 5. SPI logic inputs (CSN, SCK, and SDI) specification**

**Table 6. SPI logic outputs (SDO) specification**

**Table 7. HWLO logic input pin specification**

**Table 8. DIAG logic output pin specification**

**Table 9. Device thermal shutdown**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|t PWON|Time from power-on to standby|V >V, S S_POR_ON V3V3 external capacitor 1 μF|||500|μs|


|ID|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|---|
|2.1|I IL|Low level input current (SCK and SDI)|V = 0.3 * V IL SPI|0.5||5|µA|
|||Low level input current (CSN)||-0.5|||µA|
|2.2|I IH|High level input current (SCK and SDI)|V = 0.7 * V IL SPI|0.5||5|µA|
|||High level input current (CSN)||-0.5|||µA|
|2.3|V IL|Low level input voltage||||0.3 * V SPI|V|
|2.4|V IH|High level input voltage||0.7 * V SPI|||V|
|2.5|V I_HYST|Input hysteresis voltage|||0.4||V|
|2.6|V ICL|SCK and SDI clamping voltage|||V SPI + 0.6||V|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V OL|Low level output voltage||||0.2 * V SPI|V|
|V OH|High level output voltage||0.8 * V SPI|||V|
|I LO|Output leakage current||-10||10|µA|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|I IL|Low level input current||0.5||1|µA|
|I IH|High level input current||10|||µA|
|V IL|Low level input voltage||||0.9|V|
|V IH|High level input voltage||2.1|||V|
|V I_HYST|Input hysteresis voltage|||0.4||V|
|t HWLO|HWLO filtering time|||33||µs|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V DIAG_PD|DIAG pin open-drain pulls down voltage||||0.2|V|
|I DIAG_PD|DIAG pin open-drain input current|V = V DIAG DIAG_PD|||1|mA|
|I DIAG_LKG|DIAG pin open-drain leakage current|V = V = 5.5 V DIAG SPI|0||1|µA|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|T TSD|Junction temperature thermal shutdown threshold||160|175|190|°C|



**DS13084** - **Rev 8** **page 6/49**


-----

### **VNF1048F**

**Electrical specification**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|T TSD_HYS|Junction temperature thermal shutdown hysteresis|||15||°C|
|T J_ADC_CONV|Junction temperature ADC full scale range resolution|T [9:0] = J_ADC (T + 72) * 3 J|0||1023||
|T J_ADC_RATE|Junction temperature ADC sample rate|||10||kSamples/s|


**Table 10. ST-SPI timings specification**

**Table 11. Charge pump specification**

**Table 12. External FET gate driver specification**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|f C|SPI clock frequency||||8|MHz|
|t WHCH|CSN low timeout|V = 3.3 V, SPI ext R < 1 kΩ PROT|30||70|ms|
|t WDTB|Watchdog toggle bit timeout.WD_TIME configuration:|00|-10%|50|+10%|ms|
|||01||100|||
|||10||150|||
|||11||200|||
|t STBY_OUT|Minimum time during which CSN must be toggled low to go out of STDBY mode||20||100|µs|

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V CP_6V|Charge pump output voltage|V = 6V S|V + 7 S|V + 11 S||V|
|V CP_10V|Charge pump output voltage|V > 10 V S|V + 13.5 S|V + 14.5 S|V + 15.5 S|V|
|V CP_LOW_H|Charge pump output undervoltage high threshold|Ramp up on V CP|V + 5.5 S|V + 6 S|V + 6.5 S|V|
|V CP_LOW_L|Charge pump output undervoltage low threshold|Ramp down on V CP|V + 5.1 S|V + 5.6 S|V + 6.2 S|V|
|V CP_LOW_hyst|Charge pump output undervoltage hysteresis|||0.4||V|
|f CP|Charge pump frequency||-5%|400|+5%|kHz|
|t CP_RISE|Charge pump low (CP_LOW diagnostic) rising edge filtering time||-5%|60|+5%|µs|
|t CP_FALL|Charge pump low (CP_LOW diagnostic) falling edge filtering time||-10%|2.3|+10%|µs|

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V GSON_6V|Gate-On voltage|V = 6 V, I = 50 µA S G|6|||V|
|V GSON_10V|Gate-On voltage|V > 10 V, I = 50 µA S G|12||15|V|
|V GSOFF|Gate-Off voltage||||0.5|V|
|V GSMAX|Maximum gate voltage (internally limited)||||20|V|
|t ON|Gate turn-on|V = 0.5 V to V = 10 V GS GS C = 80 nF GATE|||4|µs|
|t OFF|Gate turn-off|Full V to V < 0.5, GS GS C = 80 nF GATE|||2.6|µs|


**DS13084** - **Rev 8** **page 7/49**


-----

### **VNF1048F**

**Electrical specification**

**Table 13. Current sense amplifier with integrated ADC**

**Table 14. External FET VDS protection**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V GS_UVLO_6V|Gate undervoltage lockout|V = 6 V S|5|||V|
|V GS_UVLO_10V|Gate undervoltage lockout|V >10 V S|8.5|||V|
|V G_UVLO_BLK|Gate undervoltage lockout blanking|Enable at charge pump startup if external FET turn-on is required, and applied after CP_LOW expiration (falling edge)|-6%|100|+6%|µs|
|V G_UVLO_DEGLITCH|Gate undervoltage lockout deglitch filtering time||-15%|8|+15%|µs|
|Q GMAX|Maximum gate charge|V = 10 V GS|||800|nC|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V SENSE_CM|Common-mode input voltage range||0||70|V|
|V SENSE_FSR|Differential input voltage full scale range||0||160|mV|
|I _SENSE_P|CSA positive input current|||400||μA|
|I _SENSE_N|CSA negative input current|||560||μA|
|V SENSE_ADC_CONV|Current sense ADC full scale range resolution|V [12:0] = SENSE_ADC min((V /160 * 8192), 8191) SENSE|0||8191||
|V SENSE_REFRESH|Current sense ADC sample rate|||2.4||kSample/s|
|V SENSE_ACC_6mV|Digital current sense accuracy|6 mV < V < 10 mV SENSE_DIFF|-10||+10|%|
|V SENSE_ACC_10mV||V = 10 mV SENSE_DIFF|-5||+5|%|
|V SENSE_ACC_20mV||V > 20 mV SENSE_DIFF|-3||+3|%|
|V SENSE_ACC_1.8mV||1.8 mV < V < 6 mV SENSE_DIFF|-17||+17|%|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V DS_THRS_RANGE|V monitor threshold range DS 31 steps adjustable through SPI||300||1800|mV|
|V DS_THRS_STEP|V monitor threshold step DS|||50||mV|
|V DS_THRS_0|V monitor thresholds DS|||300||mV|
|V DS_THRS_ 1||||350|||
|V DS_THRS_2||||400|||
|V DS_THRS_3||||450|||
|V DS_THRS_ 4||||500|||
|V DS_THRS_ 5||||550|||
|V DS_THRS_ 6||||600|||
|V DS_THRS_ 7||||650|||
|V DS_THRS_ 8||||700|||
|V DS_THRS_ 9||||750|||
|V DS_THRS_ 10||||800|||
|V DS_THRS_ 11||||850|||



**DS13084** - **Rev 8** **page 8/49**


-----

### **VNF1048F**

**Electrical specification**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V DS_THRS_ 12|V monitor thresholds DS|||900||mV|
|V DS_THRS_13||||950|||
|V DS_THRS_14||||1000|||
|V DS_THRS_15||||1050|||
|V DS_THRS_16||||1100|||
|V DS_THRS_17||||1150|||
|V DS_THRS_18||||1200|||
|V DS_THRS_19||||1250|||
|V DS_THRS_20||||1300|||
|V DS_THRS_21||||1350|||
|V DS_THRS_22||||1400|||
|V DS_THRS_23||||1450|||
|V DS_THRS_24||||1500|||
|V DS_THRS_25||||1550|||
|V DS_THRS_26||||1600|||
|V DS_THRS_27||||1650|||
|V DS_THRS_28||||1700|||
|V DS_THRS_29||||1750|||
|V DS_THRS_30||||1800|||
|V DS_THRS_ACC|V monitor threshold accuracy DS||-5||5|%|
|V DS_DEGLITCH|V monitor shut-off deglitch time DS||-25%|5|+25%|µs|
|V DS_DELAY|V monitor shut-off delay time DS||||5|µs|
|V DS_BLK|V monitor shut-off blanking time DS|At high-side external FET startup|-10%|960|+10%|µs|
|V DS_ADC_CONV|VDS monitor ADC full scale range resolution|V [9:0] = DS_ADC min((V - V )/2 SENSE_N OUT * 1024, 957)|0||957||
|V DS_ADC_RATE|VDS monitor ADC sample rate|||0.9||MSample/s|


|Col1|Table 15. Hard short circuit|protection|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|V HSC_THRS_RANGE|Hard short circuit protection threshold range 16 steps adjustable through SPI||20||160|mV|
|V HSC_THRS_0|Hard short circuit protection thresholds|||20||mV|
|V HSC_THRS_1||||23|||
|V HSC_THRS_2||||26.4|||
|V HSC_THRS_3||||30.3|||
|V HSC_THRS_4||||34.8|||
|V HSC_THRS_5||||40|||
|V HSC_THRS_6||||45.9|||



**DS13084** - **Rev 8** **page 9/49**


-----

### **VNF1048F**

**Electrical specification**

**Table 16. Overcurrent protection**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V HSC_THRS_7|Hard short circuit protection thresholds|||52.8||mV|
|V HSC_THRS_8||||60.6|||
|V HSC_THRS_9||||69.6|||
|V HSC_THRS_10||||80|||
|V HSC_THRS_11||||91.9|||
|V HSC_THRS_12||||105.6|||
|V HSC_THRS_13||||121.3|||
|V HSC_THRS_14||||139.3|||
|V HSC_THRS_15||||160.00|||
|V HSC_THRS_ACC|Hard short circuit protection threshold accuracy||-5||5|%|
|V HSC_DELAY|Hard short circuit protection delay time||||5|µs|
|V HSC_ADC_CONV|Hard short circuit protection ADC full range resolution|V [9:0] = HSC_ADC min((V / SENSE 160*1024), 1023)|0||1023||
|V HSC_ADC_RATE|Hard short circuit ADC sample rate|||0.9||MSample/s|


|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V OC_THRS_RANGE|Overcurrent protection threshold range 32 steps adjustable through SPI||6||90|mV|
|V OC_THRS_0|Overcurrent protection thresholds||-12%|6|+12%|mV|
|V OC_THRS_1||||7.2|||
|V OC_THRS_2||||8.7|||
|V OC_THRS_3|||-7%|10.4|+7%||
|V OC_THRS_4||||11.8|||
|V OC_THRS_5||||13|||
|V OC_THRS_6||||13.8|||
|V OC_THRS_7||||14.8|||
|V OC_THRS_8||||15.8|||
|V OC_THRS_9||||16.8|||
|V OC_THRS_10||||17.9|||
|V OC_THRS_11||||19.1|||
|V OC_THRS_12||||20.4|||
|V OC_THRS_13|||-5%|21.8|+5%||
|V OC_THRS_14||||23.3|||
|V OC_THRS_15||||24.8|||
|V OC_THRS_16||||26.5|||
|V OC_THRS_17||||28.2|||
|V OC_THRS_18||||30.1|||



**DS13084** - **Rev 8** **page 10/49**


-----

### **VNF1048F**

**Electrical specification**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V OC_THRS_19|Overcurrent protection thresholds||-5%|32.2|+5%|mV|
|V OC_THRS_20||||34.3|||
|V OC_THRS_21||||36.6|||
|V OC_THRS_22||||39.1|||
|V OC_THRS_23||||41.7|||
|V OC_THRS_24||||44.5|||
|V OC_THRS_25||||47.5|||
|V OC_THRS_26||||50.6|||
|V OC_THRS_27||||54|||
|V OC_THRS_28||||61.3|||
|V OC_THRS_29||||69.5|||
|V OC_THRS_30||||78.8|||
|V OC_THRS_31||||89.3|||
|i-time_tol_t|I-t tolerance on time step (y axis)||(t-10%) - 32||(t+10%) +32|µs|
|t I_SAMPLING|Shunt current sampling time||-10%|61|+10%|µs|



*Note:* *Overcurrent protection is based on the same 10-bit ADC used for hard short protection.*

**Table 17. External FET thermal shutdown via NTC input**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V NTC_FSR|NTC input voltage full scale range||VSENSE_N - 1.2||VSENSE_N|V|
|V NTC_M|NTC_M output voltage|||VSENSE_N – 1.2||V|
|V NTC _ACC|NTC input voltage threshold accuracy||-3||3|mV|
|V NTC_THRS_0|External FET thermal shutdown NTC input voltage thresholds|||110.92||mV|
|V NTC_THRS_1||||98.76|||
|V NTC_THRS_2||||88.07|||
|V NTC_THRS_3||||78.66|||
|V NTC_THRS_4||||70.38|||
|V NTC_THRS_5||||63.08|||
|V NTC_THRS_6||||56.64|||
|V NTC_THRS_7||||50.95|||
|V NTC_THRS_8||||45.92|||
|V NTC_THRS_9||||41.46|||
|V NTC_THRS_10||||37.50|||
|V NTC_THRS_11||||37.50|||
|V NTC_THRS_12||||37.50|||
|V NTC_THRS_13||||37.50|||



**DS13084** - **Rev 8** **page 11/49**


-----

### **VNF1048F**

**Electrical specification**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V NTC_THRS_14|External FET thermal shutdown NTC input voltage thresholds|||37.50||mV|
|V NTC_THRS_15||||37.50|||
|V NTC_DEGLITCH|External FET thermal shutdown deglitch time||10||500|µs|
|V NTC_ADC_CONV|External FET thermal shutdown ADC full range resolution|V [9:0] = NTC_ADC min(((V - SENSE_N V )/1.2 * NTC 1024), 1023)|0||1023||
|V NTC_ADC_RATE|External FET thermal shutdown ADC sample rate|||4.9||kSample/s|


*Note:* *•* *VNTC = VBG * RNTC/(RT_REF + RNTC)*

*•* *RNTC = B57232V5103F360 (10 kΩ at 25 °C)*

*•* *RT-REF = 10 kΩ ±1%*

**Figure 3. NTC bridge**

**Table 18. Bypass switch**

|VNTC|ISNS_N R VBG NTC - + To ADC NTC_M BIAS R VNTC GND|
|---|---|

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|V DS_BYPASS_SAT|Bypass switch VDS saturation protection threshold||1||2|V|
|I BYPASS_SAT|Bypass switch saturation current|V - V = S OUT V DS_BYPASS_SAT|100|||mA|
|R DS(ON)_BYPASS|Bypass switch on state resistance||4|7|10|Ω|
|t ON_BYPOFF|Output turn-on time on bypass-sutthing off||||100|µs|
|t BYPASS_STA_DEGLITCH|Bypass switch saturation diagnostic deglitch filtering time||4||5|µs|


**DS13084** - **Rev 8** **page 12/49**


-----

### **VNF1048F**

**Electrical specification**

|Col1|Table|19. VOUT A-to-D conversion|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|V OUT_ADC_CONV|V ADC full range resolution OUT|V [9:0] = min(V /(51*1.2)*1024, OUT_ADC OUT 1023)|0||1023||
|V OUT_ADC_RATE|V ADC sample rate OUT|||4.9||kSample/s|


**DS13084** - **Rev 8** **page 13/49**


-----

### **VNF1048F**

**eFuse function**
## **3 eFuse function**

Protection of wire harness and PCB can be performed by defining an ideal time to fuse curve as a result of a
maximum power dissipation over the time in the wire or copper PCB traces themselves. This function can
guarantee that the insulation of wires and PCB are subject to a limited temperature and time budget that is below
the reliability specified values. Not respecting such specified limits can lead to the formation of a conducting path
by carbonization across the organic insulation materials and therefore local hot spot can conduct to sparking and
fire ignition.

The VNF1048F embeds the ST proprietary eFuse functionality for the implementation of a robust and flexible
overcurrent protection mechanism. The eFuse functionality features an intelligent circuit breaking aimed at
protecting PCB traces, connectors and wire harness from overheating, with no impact on load transients like
inrush currents and capacitance charging.

This function is set by two parameters called I NOM and t NOM . The value of I NOM corresponds to the maximum
continuous current while t NOM will determine a current versus time-to-fuse curve when load current is higher than
I NOM . The expression of current versus time-to-fuse is approximated by an optimized stepwise function, which can
be adjusted in a range between the wire I [2] -t limit on one side and load transient characteristics on the other side.
The value of t NOM corresponds to the first step up of the curve. The current time curve is always active in
combination with very fast overcurrent protection that will be triggered when the current reaches a defined
threshold for hard short circuit condition.

When the current in the load is pulse wide modulated the eFuse function calculates the mean square root of the
current. Mean square root of the current is also calculated when switching on/off the power switch during normal
operation or after a switch off due to short circuit/overload condition. So if for example the circuit is broken due to
an overload and after a while the circuit is activated again, the eFuse keeps in memory the previous condition and
still avoids that maximum I RMS is higher than I NOM .

VIP-Fuse is programmed via SPI as follows:

         - VOC_THRS sets I NOM = VOC_THRS/R SENSE

         - VHSC_THRS sets hard short circuit current = VHSC_THRS/R SENSE

         - T_NOM sets t NOM from 1 to 511 s

No intervention occurs for VSENSE < VOC_THRS, whilst an immediate shut-off occurs for VSENSE >
VHSC_THRS.

The eFuse functionality operating range is defined between VOC_THRS and VHSC_THRS. In that range, the
circuit breaking profile is defined by the stepwise function reported in Figure 4. The number of steps is
consequential to the selection of VOC_THRS and VHSC_THRS, the maximum being 15, when VOC_THRS = 6
mV and VHSC_THRS = 160 mV. This corresponds to a 1:26.67 ratio between the maximum allowed continuous
current and hard short circuit.

The Figure 5 shows the I [2] -t curve when VOC_THRS = 26.5 mV and VHSC_THRS = 105.60 mV. The number of
steps is reduced to 9 accordingly.

**DS13084** - **Rev 8** **page 14/49**


-----

### **VNF1048F**

**eFuse function**

**Figure 4. eFuse I** **[2]** **-t typical curve (VOC_thrs minimum - VHSC_thrs maximum)**

**Figure 5. eFuse I** **[2]** **-t typical curve (generic thresholds)**

**DS13084** - **Rev 8** **page 15/49**


-----

### **VNF1048F**

**Self-test**
## **4 Self-test**

The following sections describe how the device supports the execution of the in-application tests, needed to verify
the proper behavior of the hardware diagnostic verification during product lifetime. Configuration, control, and
check for each of the tests are performed in close relationship with the microcontroller, through SPI interface
communication.

Activities related to self-test are possible in a specific device state (self-test) in order to distinguish it from
operating modes (standby, wake-up, unlocked and locked modes), allowing to manage differently diagnostic faults
according to the hardware feature under test.

**Self-test control interface**

The initialization of the self-test sequence (selection of the self-test, start and stop command) is done through the
control register 1 (CR#1). Results are accessible through the status register 5 (SR#5), status register 6 (SR#6)
and status register 7 (SR#7).
### **4.1 Current sense self-test**

The purpose of the current sense self-test is to verify the proper behavior of the full current sense chain, from the
analog input to the digital output.

Starting from the unlocked state, the current sense self-test is activated through a dedicated SPI frame. The
duration of this test is around 10 µs; the first 5 µs are intended to convert the value of the voltage across the
R SENSE .

Once the self-test is started, an internal current generator provides a current sink able to produce an additional
voltage drop of 100 mV at the input pin of the internal comparator.

The result of the self-test is the difference between this converted value and the value already stored in SR#8
(HSHT), corresponding to the normal measurement performed during operation; such result is stored in SR#7
together with the self-test status.

The transition from self-test state to unlocked state is automatically guaranteed after the test is completed (around
10 µs) or if the test is stopped through S_T_STOP = 1 (self-test aborted).

The transition from the self-test state to the locked state occurs in case of watchdog timeout or HWLO = 1 (selftest aborted).

**DS13084** - **Rev 8** **page 16/49**


-----

**Figure 6. Current sense self-test flow sequence**

### **VNF1048F**

**Self-test**

CR#1 → S_T_CFG = --1

CR#2 → OVC_THR = <user option>

CR#2 → HSHT_THR = <user option>

**T** **S_T_ACTIVE** time duration

During T S_T_ACTIVE and T S_T_WAIT
timeframes, fast and slow

trip protections are
inhibited, whilst all other

protections are active

T S_T_WAIT time duration


CURRENT SENSE SELF-TEST Current sense

T S_T_ACTIVE = 5 μs Self-test
T S_T_WAIT = 5 μs Configuration

Current sense CR#1 → S_T_CFG = --1

Configuration CR#2 → HSHT_THR = <user option>

|Col1|Current sense Self-test Configuration|Col3|
|---|---|---|
||||



S_T_START = 1 Self-test

WD Timeout **SELF-TEST CONFIGURATION**

OR Turn-on pull-down current generator to produce

LOCKED SELF-TEST STATE

(Selftest aborted, **T** **S_T_ACTIVE** time duration

|SELF-TEST CONFIGURATION Turn-on pull-down current generator to produce additional voltage drop of 100 mV on current sense amplifier inputs|Col2|
|---|---|
|||


state transition **A/D CONVERSIONS AND DELTA MEASURES**

|A/D CONVERSIONS AND DELTA MEASURES Perform current sense SAR A/D conversions Compute difference between self-test measures and last user measure available in status register SR#8 Store data result, self-test status and fault emulation check in status register SR#7|Col2|
|---|---|
|||
|SELF-TEST CLOSURE Turn-off pull-down current generator to restore normal drop on current sense amplifier inputs No current sense A/D conversions during this timeframe||
|||



TEST COMPLETED Current sense

UNLOCKED STATE Self-test

|1144|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### **4.2 External FET V DS detection self-test**

The purpose of the external FET V DS detection self-test is to verify the proper behavior of the complete V DS
monitor chain (sense/process/detection), from the analog input to the digital output.

Starting from the unlocked state, the V DS detection self-test is activated through a dedicated SPI frame. The
duration of this test is around 10 μs; the first 5 μs are intended to convert the value of the voltage across the drain
and source terminals of the external FET, the remaining 5 µs are required to bring back the analog circuitry to
normal configuration.

Once the self-test is started, an internal current generator provides a current sink able to produce an additional
voltage offset of 100 mV on V DS monitor circuit inputs, to distinguish self-test execution from normal operation. In
order to guarantee proper data conversions, special care must be taken to avoid V DS ADC saturation by keeping
the overall V DS sensed by the monitor circuit below the maximum scale range (V DS_ADC_CONV ).

V DS detection self-test result is the difference between the converted value obtained during self-test execution
and the value already stored in SR#4 (V DS field), corresponding to the normal measurement performed during
operation; such delta measure result is stored in SR#5 (S_T_VDS field) together with the self-test status.

**DS13084** - **Rev 8** **page 17/49**


-----

### **VNF1048F**

**Self-test**

During self-test execution it is also possible to emulate the external FET V DS fault condition by playing with
programmable thresholds available through register CR#2 (VDS_THR field); fault emulation result is stored in
SR#5 (S_T_VDS_MAX1 bit field).

To be noted that diagnostic fault for normal operation (VDS_MAX, SR#1) is inhibited during execution, while all
the others are kept enabled.

The transition from self-test state to unlocked state is automatically guaranteed after the test is completed (around
10 μs) or if the test is stopped through S_T_STOP = 1 (self-test aborted).

The transition from the self-test state to the locked state can occur in case of watchdog timeout or HWLO = 1
(self-test aborted).

**Figure 7. VDS monitor self-test flow sequence**

VDS MONITOR SELF-TEST

T S_T_ACTIVE = 5 μs Ext FET VDS Monitor
T S_T_WAIT = 5 μs Self-test configuration


UNLOCKED STATE


CR#1 → S_T_CFG = -1
CR#2 → VDS_THR = <user option>

**T** **S_T_ACTIVE** time duration

During T S_T_ACTIVE and T S_T_WAIT
timeframes, V DS protection

is inhibited, whilst all
other protections are

active

T S_T_WAIT time duration

|Col1|VDS Monitor Self-test Configuration|Col3|
|---|---|---|
||||


S_T_START = 1 Self-test

WD Timeout **SELF-TEST CONFIGURATION**

OR Turn-on pull-down current generator to produce

LOCKED SELF-TEST STATE

(Selftest aborted, **T** **S_T_ACTIVE** time duration

|SELF-TEST CONFIGURATION Turn-on pull-down current generator to produce additional voltage offset of 100mV on VDS Monitor inputs|Col2|
|---|---|
|||


state transition **A/D CONVERSIONS & DELTA MEASURES**

expiration) last user measure available in Status Register SR#4

|A/D CONVERSIONS & DELTA MEASURES Perform VDS SAR A/D conversions Compute difference between Selftest measures and last user measure available in Status Register SR#4 Store data result, selftest status and fault emulation check in Status Register SR#5|Col2|
|---|---|
|||


|SELF-TEST CLOSURE Turn-off pull-down current generator to restore normal voltage drop on VDS Monitor inputs No VDS A/D conversions during this timeframe|Col2|
|---|---|
|||



TEST COMPLETED Ext FET VDS Monitor

UNLOCKED STATE Self-test

|1133|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|

### **4.3 External FET stuck-on self-test**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|0|
|---|---|---|---|---|---|---|---|



The purpose of this self-test is to verify the proper turn-off of the external power switch, by monitoring its V DS

behavior in time.

**DS13084** - **Rev 8** **page 18/49**


-----

### **VNF1048F**

**Self-test**

Starting from the unlocked State, the external FET stuck-on self-test is activated through a dedicated SPI frame
(CR#1, S_T_START & S_T_CFG fields).

At execution start the external FET is automatically turned-off, regardless of its status during previous operations,
then continuous AtoD conversions of V DS voltage, sensed across external power switch terminals, are performed
in order to allow the user to monitor V DS evolution in time.

Data conversion values are made available through dedicated register SR#6 (S_T_STUCK field); in addition, a
specific bit informs the user if the data have been updated with a new measure or are still relative to the previous
one (UPDT_S_T_STUCK bit). Status of self-test execution is available in the same register.

Self-test completion can be controlled directly by sending the S_T_STOP command (CR#1, bit 8) or by setting the
programmable V DS threshold (CR#2, VDS_THR field): in this case, self-test is stopped automatically as soon as
the external FET V DS overcomes the previously mentioned threshold and a specific bit is set to flag this situation
(SR#6, S_T_VDS_MAX2 bit). In both cases, device FSM performs the transition from self-test to unlocked state.

To be noted that the diagnostic fault for normal operation (VDS_MAX, SR#1) is inhibited during execution, while
all the others are kept enabled; bypass switch control is left to the user.

The transition from the self-test state to the locked state can occur in case of watchdog timeout or HWLO = 1
(self-test aborted).

**Figure 8. External FET stuck-on self-test - flow sequence for entry**


EXTERNAL FET STUCK-ON SELF-TEST

WD Timeout

OR

HWLO = 1

(Selftest aborted)


UNLOCKED STATE

External FET = ‘OUTCTL’

BYPASS = ‘BYPASSCTL”


External FET

Stuck-on self-test

Configuration

Y


CR#1 → S_T_CFG = 1-
CR#2 → VDS_THR = <user option>

During Selftest

DS execution, VDS

protection is inhibited

|Col1|External FET Stuck-on Self-test Configuration|Col3|Col4|
|---|---|---|---|
|||||

|Col1|SELF-TEST CONFIGURATION Turn OFF the External FET|Col3|
|---|---|---|
||||
||CONTINUOUS A/D CONVERSIONS Perform continuous A/D conversion of VDS Store the result in Status Register SR#6||


S_T_STOP = 1

(Selftest completed)


S_T_START = 1

TEST COMPLETED

|1144|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|


**DS13084** - **Rev 8** **page 19/49**


-----

### **VNF1048F**

**Protections**
## **5 Protections**
### **5.1 Battery undervoltage shutdown**

The device is able to operate down to V S = 6 V, with the charge pump still active. If the battery supply voltage V S
falls below the undervoltage shutdown threshold, the device enters in battery undervoltage mode. The current
sense diagnostic is not available. The charge pump, the output stage and the bypass switch are off regardless of
the SPI status.

If V S rises above the threshold (V S_USD + V S_USD_hys ) the device returns to the last mode.

An undervoltage flag is set in the SPI register when V S < V S_USD, and automatically reset when
V S     - V S_USD + V S_USD_hys . **5.2 Device overtemperature shutdown**

The device temperature is internally monitored. An overtemperature shut-down of the device occurs when T J
exceeds T TSD . The charge pump, the output stage and the bypass switch are off. A fault indication is given via

SPI.

The device restarts when T J decreases below T TSD        - T TSD_HYS .

V TJ is converted by a dedicated ADC converter. The converted result is stored in the Status register and can be

read via SPI. **5.3 External MOSFET overtemperature shutdown**

The external MOSFET temperature is monitored through a 10 kΩ NTC thermistor with one terminal connected to
the Drain of the MOSFET, in order to allow optimal component placement.

R NTC is part of a V BG (V BG = V SenseN     - V NTC_M ; typ. 1.2 V) voltage divider through NTC and NTC_M pins:

VBG × RNTC

V NTC = RT_REF + RNTC (1)

V NTC is converted by a dedicated ADC converter. The converted result is stored in the Status register and can be

read via SPI.

An overtemperature shutdown of the MOSFET occurs when V NTC voltage decreases under a preset threshold.
The threshold can be set via SPI in the range from 100 °C to 150 °C in steps of 5 °C. In this case both output
stages and bypass switch are turned off.

The MOSFET and the bypass switch are re-armed via SPI by clearing latched fault NTC_OVT bit.

This protection is not active in case of external MOSFET in OFF state. **5.4 External MOSFET desaturation shutdown**

The external MOSFET drain-source voltage is monitored by the Control IC. A desaturation shutdown of the
MOSFET occurs when the VDS exceeds the preset threshold. In this case both output stage and bypass switch
are turned off. The threshold can be set via SPI in the range 0.3 V to 1.80 V in steps of 50 mV (default = 300 mV).

The MOSFET and bypass switch are re-armed via SPI by clearing latched fault VDS_MAX bit.

V DS is converted by a dedicated ADC converter. The converted result is stored in the Status register and can be

read via SPI.

This protection is not active in case of external MOSFET in OFF state.

**DS13084** - **Rev 8** **page 20/49**


-----

### **VNF1048F**

**Protections** **5.5 Hard short circuit latch-off**

The external MOSFET drain-source current is monitored by the control IC through the current sense amplifier,
which reads the voltage drop across a high-side shunt resistor. A hard short circuit shutdown of the MOSFET
occurs when the current sense voltage exceeds the preset threshold. In this case, both output stage and bypass
switch are turned off. The threshold can be set via SPI in the range from 20 mV to 160 mV.

The MOSFET is re-armed via SPI by clearing the HSHT latched fault bit.

V HSHT is converted by a dedicated ADC converter. The converted result is stored in the status register and can be

read via SPI.

This protection is not active in case the external MOSFET is in OFF state. **5.6 Current vs time latch-off**

The external MOSFET drain-source current is monitored by the control IC through the current sense amplifier,
which reads the voltage drop across a high-side shunt resistor. The overload detection circuitry emulates the
response of a traditional fuse. An overcurrent shutdown of the MOSFET occurs when the current sense voltage
exceeds the preset threshold for longer than the preset time. In this case, both output stages and bypass switch
are turned off. The threshold can be set via SPI in the range 6 mV to 90 mV, while the nominal trip time can be
programmed in the range from 1 s to 511 s.

The MOSFET is re-armed via SPI by clearing the FUSE_LATCH latched fault bit. This protection is not active in
case the external MOSFET is in OFF state.

In case of hard short protection event occurrence, reported by the HSHT flag bit, the FUSE_LATCH bit is set as
well. **5.7 Low current bypass desaturation shutdown**

Internal bypass switch VDS voltage (VS - VOUT) is monitored by the IC, to protect the switch from load current
sink changes.

A desaturation shutdown of the bypass occurs when its VDS exceeds a fixed threshold (~1.3 V); in this situation,
the bypass switch is turned off while the external FET is turned on through the HS_GATE output, directly by the
hardware, regardless of their software controlled bit status, in order to protect the bypass and provide the
requested current capability to the connected load.

This represents the so-called AUTO-ON event and it is flagged by bit #4 (AUTOON) of the global status byte that
corresponds to the BYPASS_SAT flag of status Register #1.

Bypass switch can be re-armed through SPI control by clearing the BYPASS_SAT fault latched bit.

This protection is not active in case the bypass switch is in OFF state.

A particular case is represented by standby wake-up event occurrence, with FSM state transition to wake up
state, due to bypass switch desaturation: only in this situation, in addition to the previously mentioned actions on
the bypass switch and external FET, the device signals, by driving the DIAG pin low, that it has been woken up by
the hardware event (load current increase), in order to allow host control to take proper actions.

It is important to notice that the bypass switch cannot be used to charge any type of load, even those requesting
small currents capability: on the contrary, it shall be used to keep powered application loads, previously charged
by external FET, when they switch to low-power consumption modes (that is, standby).

**DS13084** - **Rev 8** **page 21/49**


-----

### **VNF1048F**

**SPI functional description**
## **6 SPI functional description**
### **6.1 SPI Communication**

The SPI communication is based on the “ST-SPI Specification”.

The device operates in Slave mode on a bus configuration through CSN, SDI, SDO and SCK signal lines, with 32
bits SPI frames.

A SPI Master device (Host Microcontroller) initiates the communication.

The SPI Master device must be configured in the following mode:

CPOL = 0, CPHA = 0

Input data are shifted into SDI, MSB first while output data are shifted out on SDO, MSB first.

**Figure 9. SPI functional diagram**
##### CSN SCK µC VNF1048F SDI SPI Master Slave SDO CSN SCK

|Col1|Col2|
|---|---|
|||
|||
|||


|BUS master SPI interface with CPOL = 0 CPHA = 0 CS1 CS2|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||



**DS13084** - **Rev 8** **page 22/49**


-----

### **VNF1048F**

**SPI functional description** **6.2 Signal description**

**Serial clock SCK**

This input signal provides the timing of the serial interface. Data present at Serial Data Input (SDI) are latched on
the rising edge of Serial Clock (SCK). Data on Serial Data Output (SDO) change after the falling edge of Serial
Clock (SCK).

**Serial data input SDI**

This input signal is used to transfer data serially into the device. It receives data to be written. Values are sampled
on the rising edge of Serial Clock (SCK).

**Serial data output SDO**

This output signal is used to transfer data serially out of the device. Data are shifted out on the falling edge of
Serial Clock (SCK).

**Chip select CSN**

The communication interface is deselected, when this input signal is logically high. A falling edge on CSN enables
and starts the communication while a rising edge finishes the communication and the sent command is executed
when a valid frame was sent. During communication start and stop the Serial Clock (SCK) has to be logically low. **6.3 SPI protocol**

SDI format during each communication frame starts with a command byte. It begins with two bits of operating
code (OC1, OC0) which specify the type of operation (read, write, read and clear status, read device information)
and it is followed by a 6-bit address (A5 : A0). The command byte is followed by three input data bytes: (D23 :
D16), (D15 : D8) and (D7 : D0).

**Table 24. Global status byte**

SDO format during each communication frame starts with a specific byte called Global Status Byte (see GSB byte for more
details on bit0 - bit7 ) . This b y te is followed b y three out p ut data b y tes ( D23 : D16 ), ( D15 : D8 ) and ( D7 : D0 ) .

|Col1|Table 20. Command byte|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|OC1|OC0|A5|A4|A3|A2|A1|A0|


|Col1|Table 21. Input data byte 1|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|D23|D22|D21|D20|D19|D18|D17|D16|


|Col1|Table 22. Input data byte 2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|D15|D14|D13|D12|D11|D10|D9|D8|


|Col1|Table 23. Input data byte 3|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|D7|D6|D5|D4|D3|D2|D1|D0|


|MSB|Col2|Col3|Col4|Col5|Col6|Col7|LSB|
|---|---|---|---|---|---|---|---|
|bit7|bit6|bit5|bit4|bit3|bit2|bit1|bit0|



**DS13084** - **Rev 8** **page 23/49**


-----

### **VNF1048F**

**SPI functional description**

|Col1|Table 25. Output data byte 1|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|D23|D22|D21|D20|D19|D18|D17|D16|


|Col1|Table 26. Output data byte 2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|D15|D14|D13|D12|D11|D10|D9|D8|


|Col1|Table 27. Output data byte 3|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|MSB|||||||LSB|
|D7|D6|D5|D4|D3|D2|D1|D0| **6.4 Operating code definition**

The SPI interface features four different addressing modes which are listed in Table 28.

|Col1|Col2|Table 28. Operating codes|
|---|---|---|
|OC1|OC0|Meaning|
|0|0|Write operation|
|0|1|Read operation|
|1|0|Read and clear status operation|
|1|1|Read device information| **6.5 Write mode**

The write mode of the device allows to write the content of the input data byte into the addressed register (see list
of registers in Table 33. RAM memory map). Incoming data are sampled on the rising edge of the serial clock
(SCK), MSB first.

During the same sequence outgoing data are shifted out MSB first on the falling edge of the CSN pin and
subsequent bits on the falling edge of the serial clock (SCK). The first byte corresponds to the Global Status Byte,
second, third and forth bytes to the previous content of the addressed register. Unused bits will be always read as
0.

**Figure 10. SPI write operation**

CSN

SDI

|Col1|Command Byte|Col3|Col4|Data (24 bits) MSB LSB|Col6|
|---|---|---|---|---|---|
||0|0|MSB Address LSB|||


|Col1|Global Status Byte (8 bits) MSB LSB|Data (previous content of register) MSB LSB|Col4|
|---|---|---|---|



*GADG1010171330PS*

**DS13084** - **Rev 8** **page 24/49**


-----

### **VNF1048F**

**SPI functional description** **6.6 Read mode**

The read mode of the device allows to read and to check the state of any registers.

Incoming data are sampled on the rising edge of the serial clock (SCK), MSB first.

Outgoing data are shifted out MSB first on the falling edge of the CSN pin and others on the falling edge of the
serial clock (SCK). The first byte corresponds to the Global Status Byte, second, third and forth byte to the
content of the addressed register.Unused bits will be always read as 0.

In order to avoid inconsistency between the Global Status byte and the Status register, the Status register
contents are frozen during SPI communication.

**Figure 11. SPI read operation**

CSN

|Col1|Command Byte|Col3|Col4|Don’t care (24 bits) MSB LSB|Col6|
|---|---|---|---|---|---|
||0|1|MSB Address LSB|||


|Col1|Global Status Byte (8bit) MSB LSB|Data (24 bits) MSB LSB|Col4|
|---|---|---|---|



*GADG1010171333PS* **6.7 Read and clear status command**

The read and clear status operation is used to clear the content of the addressed status register (see
Table 33. RAM memory map). A read and clear status operation with address 0x3Fh clears all Status registers
simultaneously.

Incoming data are sampled on the rising edge of the serial clock (SCK), MSB first. The command byte allows to
determine which register content is read and the payload bits set to 1 into the data byte determine the bits into the
register which have to be cleared.

Outgoing data are shifted out MSB first on the falling edge of the CSN pin and others on the falling edge of the
serial clock (SCK). The first byte corresponds to the Global Status byte, second, third and forth byte to the content
of the addressed register. Unused bits will be always read as 0.

In order to avoid inconsistency between the Global Status byte and the Status register, the Status register
contents are frozen during SPI communication.

**Figure 12. SPI read and clear operation**


CSN

SDI

SDO


Read and clear status

|Col1|operation|Col3|
|---|---|---|

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|Command byte|||Data byte (24 bits) MSB LSB|
|1|0|MSB Address LSB||
|||||

|Col1|Col2|Global Status byte (8 bits) MSB LS|Data byte BMSB (24 bits) LSB|Col5|Col6|
|---|---|---|---|---|---|


*GADG1010171505PS*

**DS13084** - **Rev 8** **page 25/49**


-----

### **VNF1048F**

**SPI functional description** **6.8 SPI device information**

Specific information can be read but not modified during this mode.

Incoming data are sampled on the rising edge of the serial clock (SCK), MSB first. The command byte allows to
determine which information is read, whilst the other three data bytes are "don’t care".

Outgoing data are shifted out MSB first on the falling edge of the CSN pin and others on the falling edge of the
serial clock (SCK). The first byte corresponds to the Global Status byte, second byte to the content of the
addressed register, third and forth bytes are 0x00.

**Figure 13. SPI read device information**


Read and clear status

|Col1|operation|Col3|
|---|---|---|


|Col1|Col2|Global Status byte (8 bits) MSB LSB|Data byte MSB (24 bits) LSB|Col5|Col6|
|---|---|---|---|---|---|



*GADG1010171521PS*
### **6.9 Special commands**

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|Command byte|||Don’t care (24 bits) MSB LSB|
|1|1|MSB Address LSB||
|||||



**0xFF — SWReset: sets all control registers to default and clears all status register**

An Opcode ‘11’ (read device information) addressed at ‘111111’ forces a Software Reset of the device, second,
third and forth bytes are "don't care" provided that at least one bit is zero.

*Note:* *In the case of an OpCode '11' at address '111111' with data field equal to '1111111111111111' the SPI frame is*
*recognized as a frame error and SPIE bit of GSB is set.*

**Table 29. 0xFF: (SW_Reset)**

*1.* *X: do not care*

**0xBF — clear all status registers (RAM access)**

When an OpCode ‘10’ (read and clear operation) at address b’111111 is performed.

|Bit 7|Bit 6|Bit 5|Bit 4|Bit 3|Bit 2|Bit 1|Bit 0|
|---|---|---|---|---|---|---|---|
|Command||||||||
|OC1|OC0|Address||||||
|1|1|1|1|1|1|1|1|
|DATA1|X(1)|X|X|X|X|X|X|
||0|0|0|0|0|0|0|
|DATA2|X|X|X|X|X|X|X|
||0|0|0|0|0|0|0|
|DATA3|X|X|X|X|X|X|X|
||0|0|0|0|0|0|0|



**DS13084** - **Rev 8** **page 26/49**


-----

### **VNF1048F**

**SPI functional description**

**Table 30. Clear all status registers (RAM access)**

*1.* *X: do not care*

|Bit 7|Bit 6|Bit 5|Bit 4|Bit 3|Bit 2|Bit 1|Bit 0|
|---|---|---|---|---|---|---|---|
|Command||||||||
|OC1|OC0|Address||||||
|1|0|1|1|1|1|1|1|
|DATA1|X(1)|X|X|X|X|X|X|
||0|0|0|0|0|0|0|
|DATA2|X|X|X|X|X|X|X|
||0|0|0|0|0|0|0|
|DATA3|X|X|X|X|X|X|X|
||0|0|0|0|0|0|0| **6.10 Global status byte**

As per the **STMicroelectronics SPI 4.1** specification, the device features an in-frame response mechanism.

A global status byte is transmitted to the SPI master on the SDO line while the command byte is received on the
SDI line.

The global status byte reports the global status of the device:

|Table 31. Global status byte|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Global status byte|||||||||
|Bit|MSB|30|29|28|27|26|25|LSB|
|Name|GSBN|RSTB|SPIE|AUTOON|DIAGS|DE|OVC|FS|


|Col1|Col2|Table 32. Global status byte - bit description|
|---|---|---|
|Bit #|Name|Description|
|31|GSBN|Global status bit NOT This bit is a NOR combination of the remaining bits of this register: GSBN = NOT (RSTB or SPIE or AUTOON or DIAGS or DE or OVC or FS) This bit can also be used as global status flag without starting a complete communication frame as it is present directly after pulling CSN low.|
|30|RSTB|Reset bit The RSTB indicates a device hardware reset. This bit is set in power-on mode. All internal control registers are set to default and kept in that state until the bit is automatically cleared by the first valid SPI communication.|
|29|SPIE|SPI error The SPIE is a logical OR combination of errors related to a wrong SPI communication: SDI stuck-at fault, SPI frame length ≠ 32-bit (wrong number of clock pulses while CSN is low), parity check error|
|28|AUTOON|AUTOON The AUTOON indicates the automatic turn-on of the external FET due to low-current bypass desaturation (BYPASS_SAT = 1) when its VDS exceeds the fixed threshold (~1.3 V). This bit is also set by a transition from wake up to unlocked mode. AUTOON = BYPASS_SAT|
|27|DIAGS|Diagnostic signal bit The DIAGS is a logical OR combination of all faults, which cause the external FET to be switched off|



**DS13084** - **Rev 8** **page 27/49**


-----

### **VNF1048F**

**SPI functional description**

|Bit #|Name|Description|
|---|---|---|
|||DIAGS = VS_UV or HSHT or VDS_MAX or FUSE_LATCH or DEV_OVT or NTC_OVT or VGS_LOW or DIS_OUT_FAULT or CS_UV|
|26|DE|Device error bit The DE is a logical OR combination of errors related to device specific blocks: charge pump output undervoltage, NVM download failure, oscillator failure DE = CP_LOW or NVM_FAIL or OSC_FAIL|
|25|OVC|Overcurrent bit The OVC is a ‘realtime’ bit indicating an overcurrent event (VIP-fuse counter running)|
|24|FS|Fail-safe If the FS bit is set, the device was forced into a safe state. This bit is set in the fail-safe state (SR#1.FAILSAFE_ST = 1) FS = FAILSAFE_ST| **6.11 Address map**

**Table 33. RAM memory map**

|Address|Name|Access type|Content|
|---|---|---|---|
|01h|Control Register 1|R/W|CR#1: 1st Control Register (CONTROLS)|
|02h|Control Register 2|R/W|CR#2: 2nd Control Register (CONFIG 1)|
|03h|Control Register 3|R/W|CR#3: 3rd Control Register (CONFIG 2)|
|…|…|…|…|
|11h|Status register 1|R/C|SR#1: 1st status register (DIAGNOSTICS + PROTECTIONS)|
|12h|Status register 2|R|SR#2: 2nd status register (CURRENT SENSE)|
|13h|Status register 3|R|SR#3: 3rd status register (NTC + TJ)|
|14h|Status register 4|R|SR#4: 4th status register (VOUT + VDS)|
|15h|Status register 5|R/C|SR#5: 5th status register (SELFTEST VDS)|
|16h|Status register 6|R/C|SR#6: 6th status register (SELFTEST STUCK ON)|
|17h|Status register 7|R/C|SR#7: 7th status register (SELFTEST CURRENT SENSE)|
|18h|Status register 8|R|SR#8: 8th status register (HSHT)|
|…|…|…|…|
|21h|Reserved|||
|22h|Reserved|||



**DS13084** - **Rev 8** **page 28/49**


-----

### **VNF1048F**

**SPI functional description**

|Address|Name|Access type|Content|
|---|---|---|---|
|…|…|…||
|31h|Reserved|||
|32h|Reserved|||
|33h|Reserved|||
|34h|Reserved|||
|…|…|…||
|3Fh|Advanced operation code|C|A R&C operation to this address causes all clearable status registers to be cleared|

### **6.12 ROM memory map**

|Col1|Col2|Table 34. ROM memory map|Col4|Col5|
|---|---|---|---|---|
|Address|Name|Description|Access|Content|
|00h|Company code|STMicroelectronics company code|Read only|00h|
|01h|Device family|Product family code|Read only|01h|
|02h|Product code 1|First product letter code|Read only|55h|
|03h|Product code 2|Second product letter code|Read only|52h|
|04h|Product code 3|Third product letter code|Read only|05h|
|05h|Product code 4|Fourth product letter code|Read only|4Ah|
|0Ah|Silicon version|AD silicon version|Read only|02h|
|10h|SPI Mode|Bit7 = 0, burst read is disabled, SPI data length = 32bit Bit6, DL2 = 0 Bit5, DL1 = 1 Bit4, DL0 = 1 Bit3, SPI8 =0: 8-bit frame option not available Bit2 =0: Parity check is used Bit1, S1=0 Bit0, S0=1|Read only|31h|
|11h|WD Type 1|A WD is implemented Bit7, WD1 =0 Bit6, WD0 =1 WD period 5ms = 10*ms -> WT[5:0] = 0xA Bit5, WT5 = 0 Bit4, WT4 = 0 Bit3, WT3 = 1 Bit2, WT2 = 0 Bit1, WT1 = 1 Bit0, WT0 = 0|Read only|4Ah|
|13h|WD bit pos. 1|Bit7,WB1 = 0 Bit6,WB2 = 1 WBA[5-0], Bit[5-0] = address of the config. register, where the WD bit is located = 03h = 000011b|Read only|43h|


**DS13084** - **Rev 8** **page 29/49**


-----

### **VNF1048F**

**SPI functional description**

|Address|Name|Description|Access|Content|
|---|---|---|---|---|
|14h|WD bit pos. 2|Bit7,WB1 = 1 Bit6,WB0 = 1 Bit position of the WD bit within the corresponding configuration register = 01d = 000001b|Read only|C1h|
|3Fh|Advanced Operation Code|Access to this address provokes a SW reset (all control registers are set to their default values; in addition, all clearable status registers are cleared too). Note: data field should not be “all ones”, otherwise an “SDI stuck at” error occurs.|Read only|00h|

### **6.13 Control registers**


**Table 35. CR#1: control register 1 (read/write); address 01h**

|Bit|Default|Name|Description|
|---|---|---|---|
|23 ÷ 12||Unused||
|11|0|GOSTBY|GOSTBY can be set to 1 only if UNLOCK = 1; trying to set this bit to 1 when UNLOCK = 0 will have no effects and it maintains its previous value. GOSTBY can be reset to 0 also when UNLOCK = 0. To send a GOToStandby sequence it is necessary to send two consecutive SPI frames, as follows: 1st SPI writes operation to set UNLOCK bit to 1 2nd SPI write operation to set GOSTBY bit to 1 and EN bit to 0. A transition to standby state causes GOSTBY to be reset to 0.|
|10|0|EN|EN can be set to 1 only if UNLOCK = 1; trying to set this bit to 1 when UNLOCK = 0 will have no effects and it maintains its previous value. EN can be reset to 0 also when UNLOCK = 0. To send a GOToUnlocked sequence it is necessary to send two consecutive SPI frames as follows: 1st SPI writes operation to set UNLOCK bit to 1 2nd SPI write operation to set GOSTBY bit to 0 and EN bit to 1. A transition to unlocked state causes EN to be set to 1. A transition to locked state causes EN to be reset to 0.|
|9|0|S_T_START|When it is set to 1, starts selected self-test. If current state is unlocked and S_T_CFG is not 000, then setting this bit causes a transition to self-test state. This bit is automatically reset.|
|8|0|S_T_STOP|When it is set to 1, stops execution of selected self-test. This bit is automatically reset.|
|7 ÷ 5|000|S_T_CFG|Self-test selection: 000: No selection 001: Current sense 010: VDS detection 100: Power switch stuck-on 011: Current sense + VDS detection 101: Current sense + power switch stuck-on 110: VDS detection + power switch stuck-on|


**DS13084** - **Rev 8** **page 30/49**


-----

### **VNF1048F**

**SPI functional description**

**Table 36. CR#2: control register 2 (read/write); address 02h**

**Table 37. CR#3: control register 3 (read/write); address 03h**

|Bit|Default|Name|Description|
|---|---|---|---|
||||111: Current sense + VDS detection + power switch stuck-on|
|4|0|OUTCTL|Enables high-side through SPI 1: HS gate driver commanded on 0: HS gate driver commanded off|
|3|0|BYPASSCTL|Enables low current bypass through SPI 1: LCB commanded on 0: LCB commanded off|
|2||Unused||
|1|0|WD_TRIG|Mirror of WD_TRIG bit|
|0|0|Parity bit|Odd parity bit check|


|Bit|Default|Name|Description|
|---|---|---|---|
|23 ÷ 16|00000000|T_NOM|Configures the value of nominal time, required for the fuse emulation: t (s) = NOM b{T_NOM(7:0), 1} T_NOM = 00000000 → t (s) = b000000001 = 1s min NOM T_NOM = 11111111 → t (s) = b111111111 = 511s max NOM Nominal time corresponds to the trip time obtained when current is equal to the nominal overcurrent threshold (OVC_THR).|
|15 ÷ 11|00000|OVC _THR|Configures the value of nominal overcurrent threshold. The threshold can be set in the range 6 mV to 90 mV See Table 16|
|10 ÷ 7|0000|HSHT_THR|Configures a threshold for hard short circuit latch-off. The threshold can be set in the range from 20 mV to 160 mV. See Table 15|
|6 ÷ 2|00000|VDS_THR|Configures a threshold for external MOSFET desaturation shutdown. The threshold can be set in the range from 0.3 V to 1.80 V in steps of 50 mV (default = 300 mV). Configuration 0x1F is reserved.|
|1|0|WD_TRIG|Mirror of WD_TRIG bit|
|0||Parity bit|Odd parity bit check|


|Bit|Default|Name|Description|
|---|---|---|---|
|23 ÷ 10||unused||
|9|0|UNLOCK|0: bits GOSTBY, EN cannot be set to 1 but can be reset; 1: bits GOSTBY, EN can be set to 1, but only with the next valid SPI frame. When UNLOCK = 1, it is automatically reset with the next valid SPI frame.|
|8 ÷ 5|0000|NTC_THR|Configures a threshold for external MOSFET overtemperature shutdown via NTC. The threshold can be set in the range 37.50 to 110.92. See Table 17|
|4 ÷ 3|00|WD_TIME|Watchdog time selection: 00: t = 50ms WD 01: t = 100ms WD 10: t = 150ms WD|



**DS13084** - **Rev 8** **page 31/49**


-----

### **VNF1048F**

**SPI functional description**

|Bit|Default|Name|Description|
|---|---|---|---|
||||11: t = 200ms WD|
|2|0|DIS_OUT_MODE|Outputs status in locked state: 0: leave output and bypass as they are (default) 1: shut off output and bypass|
|1|0|WD_TRIG|In order to keep device in unlocked mode, this bit must be cyclically toggled within a period equal to t to refresh the watchdog. WD|
|0||Parity bit|Odd parity bit check| **6.14 Status registers**

**Table 38. SR#1: status register 1; address 11h**

|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23 ÷ 19||Unused|||
|18|0|DIS_OUT_FAULT|Disable output fault: a transition to locked mode state causes this bit to be set to 1, but only when DIS_OUT_MODE = 1. When DIS_OUT_FAULT = 1, both high-side and bypass are switched off.|R/C|
|17|0|SELFTEST|Self-test state flag bit|R|
|16|0|OUTST|High-side gate driver status bit 1: HS gate driver turned on 0: HS gate driver turned off|R|
|15|0|BYPASS_ST|Low current bypass status bit 1: LCB turned on 0: LCB turned off|R|
|14|0|WAKEUPM|Wake up mode flag bit|R|
|13|0|LOCKEDM|Locked mode flag bit|R|
|12|0|HWLO_ST|HWLO mirror bit: provides the logical level of HWLO pin after having applied a symmetrical filter on both its rising and falling edges (filtering time is tHWLO)|R|
|11|0|VS_UV|V undervoltage “real-time” bit S 0: V >V + V S USD S_USD_HYS 1: V ≤ V if the battery supply voltage VS falls below the undervoltage S S_USD shutdown threshold, then the external MOSFET, the charge pump and the bypass switch are switched off.|R|
|10|0|HSHT|Hard short circuit latch-off: a hard short circuit shutdown of the MOSFET (HSHT = 1) and the bypass switch occurs when the current sense voltage exceeds the preset threshold. The MOSFET and the bypass switch are re-armed via SPI.|R/C|
|9|0|VDS_MAX|External MOSFET desaturation shutdown: a desaturation shutdown of the MOSFET (VDS_MAX = 1) and the bypass switch occurs if the VDS exceeds the preset threshold when HS is in on-state after V time. DS_DEGLITCH The MOSFET and the bypass switch are re-armed via SPI.|R/C|
|8|0|BYPASS_SAT|Low current bypass desaturation shutdown: a desaturation shutdown of the Low current bypass (BYPASS_SAT = 1) occurs if the VDS exceeds the fixed threshold when HS is in off-state and bypass is in on-state. When BYPASS_SAT = 1, external MOSFET is automatically commanded on, independently of OUTCTL bit value.|R/C|



**DS13084** - **Rev 8** **page 32/49**


-----

### **VNF1048F**

**SPI functional description**

**Table 39. SR#2: status register 2; address 12h**

|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
||||The Low current bypass is rearmed via SPI. A transition to wake-up mode causes this bit to be set to 1.||
|7|0|FUSE_LATCH|Current vs time latch-off: an overcurrent shutdown of the MOSFET (FUSE_LATCH = 1) and the bypass switch occurs when the current sense voltage exceeds the preset threshold for longer than the preset time (I2-t curve emulating a traditional fuse). The MOSFET and bypass switch are rearmed via SPI.|R/C|
|6|0|OVC|Overcurrent warning: an overcurrent warning (OVC = 1) occurs even when average current sense value evaluated in a time interval equal to t I_SAMPLING (time basis used by fuse emulation algorithm) exceeds current threshold programmed through OVC_THR. This is a “real-time” bit OVC bit keeps memory of the previous events: once this bit is set, it will be reset automatically after a time depending on current level previously reached and on the related timings. Moreover, after a FUSE_LATCH bit setting, OVC will be automatically reset in a time interval proportional to the TNOM value previously programmed (provided that in the meantime FUSE_LATCH is not cleared, high-side restarts and current is again above OVC_THR). Resetting FUSE_LATCH bit when OVC bit is still set to 1 is possible, but in this case user can expect that trip time will be lower than expected.|R|
|5|0|DEV_OVT|Overtemperature shutdown (“real-time” bit). When DEV_OVT = 1, the MOSFET, the charge pump and the bypass switch are turned off.|R|
|4|0|NTC_OVT|External MOS overtemperature: this bit is latched when NTC is lower than NTC_THR. When NTC_OVT = 1 both external MOS and bypass switch are turned off. The MOSFET and the bypass switch are rearmed via SPI.|R/C|
|3|0|VGS_LOW|This bit is set in on-state when VGS falls below UV threshold (V ) GS_UVLO_10V for more than V . When this bit is set, external FET is G_UVLO_DEGLITCH switched off.|R/C|
|2|0|CP_LOW|This bit is set when V falls below V threshold for more than CP CP_LOW t . When this bit is set, external FET driver is disabled. This is a “real- CP_RISE time” bit.|R|
|1|0|WD_FAIL|Watchdog failure bit: 0: Watchdog OK; 1: Watchdog failure in unlocked / self-test states When this bit is set, device goes to locked state. To go back to the unlocked mode through the GoToUnlocked sequence this bit must be cleared.|R/C|
|0|0|Parity bit|Odd parity bit check||


|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23 ÷ 15||Unused|||
|14 ÷ 2|0000000000000|CURR_SENSE|13 bit ADC conversion related to current sense amplifier, ranging from 0 V to 160 mV; unidirectional current through an external sense resistor.|R|
|1|0|UPDT_CURR|Updated status bit. This bit is set when value is updated and cleared when register is read.|R|
|0||Parity bit|Odd parity bit check||



**DS13084** - **Rev 8** **page 33/49**


-----

### **VNF1048F**

**SPI functional description**

**Table 40. SR#3: status register 3; address 13h**

**Table 41. SR#4: status register 4; address 14h**

**Table 42. SR#5: status register 5; address 15h**

**Table 43. SR#6: status register 6; address 16h**

|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23||Unused|||
|22 ÷ 13|0000000000|TJ|10 bit ADC conversion related to TJ (device temperature)|R|
|12|0|UPDT_TJ|Updated status bit. This bit is set when value is updated and cleared when register is read.|R|
|11 ÷ 2|0000000000|NTC|10 bit ADC conversion related to NTC (external MOSFET temperature sensing through an external NTC resistor)|R|
|1|0|UPDT_NTC|Updated status bit. This bit is set when value is updated and cleared when register is read.|R|
|0||Parity bit|Odd parity bit check||


|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23 ÷ 12||Unused|||
|22 ÷ 13|0000000000|VDS|10 bit ADC conversion of the voltage across HS switch (VS-OUT). This register is not refreshed during VDS self-test execution.|R|
|12|0|UPDT_VDS|Updated status bit. This bit is set when value is updated and cleared when register is read.|R|
|11 ÷ 2|0000000000|VOUT|10 bit ADC conversion of the OUT pin|R|
|1|0|UPDT_VOUT|Updated status bit. This bit is set when value is updated and cleared when register is read.|R|
|0||Parity bit|Odd parity bit check||


|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23 ÷ 14||Unused|||
|13||S_T_VDS_MAX1|This bit is set if VDS_THR is reached during VDS self-test.|R/C|
|12 ÷ 3|0000000000|S_T_VDS|Difference between 10 bit ADC conversion of the VDS, performed during VDS self-test and content of VDS register latched during self- test execution.|R/C|
|2 ÷ 1|00|S_T_VDS_STATUS|Status of VDS self-test 00: IDLE: self-test not started 01: RUN: self-test execution in progress 10: END: self-test completed successfully (consistent data available on dedicated registers) 11: ABORT: self-test aborted (watchdog timeout, HWLO, S_T_STOP when not required)|R/C|
|0||Parity bit|Odd parity bit check||


|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23 ÷ 15||Unused|||
|14|0|UPDT_S_T_STUCK|Updated status bit. This bit is set when value is updated and cleared when register is read.|R/C|
|13|0|S_T_VDS _MAX2|This bit is set if VDS_THR is reached during STUCK ON self-test.|R/C|



**DS13084** - **Rev 8** **page 34/49**


-----

### **VNF1048F**

**SPI functional description**

**Table 45. SR#8: status register 8; address 18h**

|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|12 ÷ 3|0000000000|S_T_STUCK|10 bit ADC conversion of the VDS, performed during STUCK ON self-test|R/C|
|2 ÷ 1|00|S_T_STUCK_STATUS|Status of STUCK _ON self-test 00: IDLE: self-test not started 01: RUN: self-test execution in progress 10: END: self-test completed successfully (consistent data available on dedicated registers) 11: ABORT: self-test aborted (watchdog timeout, HWLO, S_T_STOP when not required)|R/C|
|0||Parity bit|Odd parity bit check||


|Col1|Col2|Table 44.|SR#7: status register 7; address 17h|Col5|
|---|---|---|---|---|
|Bit|Default|Name|Description|Access|
|23 ÷ 15||Unused|||
|14|0|S_T_HSHT|This bit is set if HSHT_THR is reached during CURRENT SENSE self-test.|R/C|
|13|0|S_T_OVC|This bit is set if OVC_THR is reached during CURRENT SENSE self- test.|R/C|
|12 ÷ 3|0000000000|S_T_CURR|Difference between 10 bit ADC conversion of the CURRENT SENSE, performed during CURRENT SENSE self-test and content of HSHT_SAR register latched during self-test execution.|R/C|
|2 ÷ 1|00|S_T_CURR_STATUS|Status of CURRENT SENSE self-test 00: IDLE: self-test not started 01: RUN: self-test execution in progress 10: END: self-test completed successfully (consistent data available on dedicated registers) 11: ABORT: self-test aborted (watchdog timeout, HWLO, S_T_STOP when not required)|R/C|
|0||Parity bit|Odd parity bit check||


|Bit|Default|Name|Description|Access|
|---|---|---|---|---|
|23 ÷ 12||Unused|||
|11 ÷ 2|0000000000|HSHT_SAR|10 bit ADC SAR fast conversion related to current sense amplifier, ranging from 0 V to 160 mV; unidirectional current through an external sense resistor. This register is not refreshed during current sense self-test execution.|R|
|1|00|UPDT_HSHT|Updated status bit. This bit is set when value is updated and cleared when register is read.|R|
|0||Parity bit|Odd parity bit check||



**DS13084** - **Rev 8** **page 35/49**


-----

### **VNF1048F**

**SPI functional description** **6.15 Timeout watchdog**

In order to serve the timeout watchdog, the relevant WD_TRIG bit (Watchdog Trigger bit) must be toggled within a
given timeout window.

**Figure 14. Timeout watchdog**

**DS13084** - **Rev 8** **page 36/49**


-----

### **VNF1048F**

**Operating modes**

## **7 Operating modes**
### **7.1 State diagram**

V S < V S_POR_OFF


**Figure 15. State diagram**


Notes:

When there are more then one possibletransitions out of one state, priority number is indicated in brackets for each transition.

(*) Transition to wakeup sets 'BYPASS_SAT' status bit to 1.
(**) Transition to unlocked sets "EN' bit to 1.
(***) Transition to locked resets "EN" bit to 1 and sets 'DIS_OUT_FAULT' to 1 only if 'DIS_OUT_MODE' = 1.
### **7.2 Power-on mode**

The power-on mode is the device reset state at V S power-on, due to device startup or power-on reset conditions.
At power-on, the registers are loaded with the default values and the RSTB is set to 1.

External FET, BYPASS switch, and charge pump are in the OFF state.

**DS13084** - **Rev 8** **page 37/49**


-----

### **VNF1048F**

**Operating modes** **7.3 Standby mode**

In standby mode, the device is in quiescent power consumption and operates under the following conditions:

         - High current path through external FETs is off

         - Protections for the external FETs are disabled

         - All diagnostics are disabled, but BYPASS switch saturation is monitored, if BYPASS switch is in ON state
during standby mode, in order to detect potential desaturation

         - Low-current bypass can be ON or OFF according to the ‘BYPASSCTL’ bit

         - The device is self-protected

         - Charge pump is OFF

The standby mode characteristics are:

         - VSPI and VS low consumption

         - SPI inactive

         - Registers are frozen (powered but with the clock stopped) allowing to keep either previous configuration, in
case of transition from unlocked state, or default reset configuration, in case of transition from power-on
state

The standby mode is reached in case of power-on state transition from unlocked mode through the following SPI
frame sequence:

1. Frame #1 to set UNLOCK bit in CR#3

2. Frame #2 to reset EN and set GOSTBY in CR#1

Exit from standby mode occurs in any of the following cases:

         - CSN Low for a time t > t
STBY_OUT

Or

         - BYPASS switch in ON state and desaturation event occurrence **7.4 Wake-up mode**

The device enters in wake-up mode from standby when the V S       - V OUT       - V DS_BYPASS_SAT .

In wake-up mode, the device fuse functionality is armed and the device operates under the following conditions:

         - High current path through external FETs is ON

         - Protections for the external FETs are enabled

         - Low-current bypass is OFF

         - All diagnostics are enabled

         - Control registers are locked to write operations

         - The device is self-protected

         - SPI is active

         - Charge pump is ON **7.5 Unlocked mode**

In unlocked mode, the device fuse functionality is armed and SPI communication is allowed. The device operates
under the following conditions:

         - High current path through external FETs can be ON or OFF, depending on the SPI setting

         - Protections for the external FETs are enabled

         - All diagnostics are enabled

         - Low-current bypass can be ON or OFF, depending on the SPI setting

         - The device is self-protected

         - SPI is active

         - Charge pump is ON

**DS13084** - **Rev 8** **page 38/49**


-----

### **VNF1048F**

**Operating modes** **7.6 Locked mode**

In locked mode, the device fuse functionality is armed. The device operates under the following conditions:

         - External FETs status is defined by 'OUTCTL' and 'DIS_OUT_MODE' control bits

         - Protections for the external FETs are enabled

         - All diagnostics are enabled

         - Low-current bypass is defined by 'BYPASSCTL' and 'DIS_OUT_MODE' control bits

         - The device is self-protected

         - SPI is active, all registers can be read, control registers are locked to write operations

         - Charge pump is ON **7.7 Self-test mode**

See Section 4 Self-test in this document.

**DS13084** - **Rev 8** **page 39/49**


-----

## **8 Application information**


**Figure 16. Application diagram**

### **VNF1048F**

**Application information**

R SENSE

External FET

|VBAT|Col2|Col3|
|---|---|---|
|C P C VS1 C V VS2 BAT C P2 CP VS CP2P ISNS_P CP2M C P1 VREG CP1P CP1M ISNS_N R NTC VSPI VNF1048F R PU HS_GATE R PROT R DIAG GB R PROT4 OUT HOST SPI MICRO R PROT NTC HWLO R T_REF V3V3 TEST1 GND TEST2 NTC_M C 3V3|||
|VREG|||
||||
|HOST MICRO|||
||||
||||
||||


SAFETY LOGIC

##### R PROT NTC HWLO R T_REF LOAD

V3V3 TEST1 GND TEST2 NTC_M C 3V3

**Table 46. Component value**

|Reference|Value|
|---|---|
|C VS1|20 μF|
|C VS2|100 nF|
|C P1|470 nF|
|C P2|470 nF|
|C P|470 nF|
|R PU|4.7 kΩ|
|C 3V3|1 μF|
|R GB|47 kΩ|
|R T_REF|10 kΩ|
|R SENSE|1 mΩ|


**DS13084** - **Rev 8** **page 40/49**


-----

### **VNF1048F**

**Package information**
## **9 Package information**

[In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages,](https://www.st.com/ecopack)
depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product
[status are available at: www.st.com. ECOPACK is an ST trademark.](http://www.st.com)
### **9.1 QFN32L Epad (5.0x5.0x1.0 mm) package information**

**Figure 17. QFN32L Epad (5.0x5.0x1.0 mm) package outline**

**DS13084** - **Rev 8** **page 41/49**


-----

### **VNF1048F**

**Package information**

**Table 47. QFN32L Epad (5.0x5.0x1.0 mm) package mechanical data**

|Symbol|Dimension in mm|Col3|Col4|
|---|---|---|---|
||Min.|Typ.|Max.|
|A|0.80|0.90|1.00|
|A1|0||0.05|
|A2||0.2 REF||
|A3|0.1|||
|D|5.00 BSC|||
|D2|3.40|3.50|3.60|
|E|5.00 BSC|||
|E2|3.40|3.50|3.60|
|e1|0.5 BSC|||
|k|0.20|||
|L1|||0.05|
|La|0.40|0.50|0.60|
|bA|0.20|0.25|0.30|
|h||0.19 REF||
|h1||0.19 REF||
|LB|0.45|0.50|0.55|
|bB|0.20|0.25|0.30|
|N|32|||
|R1|||0.1|
|Tolerance of form and position||||
|aaa|0.15|||
|bbb|0.10|||
|ccc|0.10|||
|ddd|0.05|||
|eee|0.08|||
|fff|0.10|||



**DS13084** - **Rev 8** **page 42/49**


-----

### **VNF1048F**

### **Revision history**

|Col1|Col2|Table 48. Document revision history|
|---|---|---|
|Date|Revision|Changes|
|16-Oct-2019|1|Initial release.|
|05-Aug-2020|2|Updated: -Section 9.1 QFN32L 5x5 package information -Table 4. Supply specification (also added ID 1.11) - Table 5. SPI logic inputs (CSN, SCK and SDI) specification - Table 7. HWLO logic input pin specification - Table 9. Device Thermal shutdown (added ID 2.21 and 2.22) - Table 10. ST-SPI Specification: Timings - Table 11. Charge Pump Specification - Table 12. External FET Gate Driver Specification - Table 13. Current sense amplifier with integrated ADC - Table 14. External FET VDS Protection (also removed VDS_THRS_31, added ID 7.8 and 7.9) - Table 15. Hard Short Circuit protection (added ID 8.5 and 8.6) - Table 16. Overcurrent protection (added note) - Table 17. External FET Thermal Shutdown via NTC input (added ID 10.6 and 10.7) - Table 18. Bypass switch (removed tS_T_WAIT parameter) - Figure 1. Block diagram - Figure 16. Application diagram (also added note) Added: - Section 5.7 Low Current Bypass desaturation shutdown - Section 6.15 Timeout Watchdog - Table 19. VOUT A-to-D Conversion - Figure 5. eFuse I2-t curve (generic thresholds) Minor text changes in: - Section 5.6 Current vs time latch-off - Section 6.10 Global Status Byte - Section 7.3 Stand-by mode - Table 1. Pin functions - Table 2. Absolute maximum rating - Table 36. CR#2: Control Register 2 (read/write); Address 02h (ID 13.20)|
|22-Sep-2020|3|Updated: - Order Code - Table 4. Supply specification (ID 1.10, 1.11 and 1.12) - Table 7. HWLO logic input pin specification (ID 2.10) - Table 13. Current sense amplifier with integrated ADC (ID, removed ISENSE_DIFF parameter) - Table 15. Hard Short Circuit protection (added ID 8.2) - Table 16. Overcurrent protection (added ID 9.2)|
|13-Jul-2021|4|Updated: - Features in cover page - Section 2 Electrical specification|


**DS13084** - **Rev 8** **page 43/49**


-----

### **VNF1048F**

|Date|Revision|Changes|
|---|---|---|
|||- Section 3 eFuse function - Section 4.2 External FET VDS Detection Self Test - Section 5.4 External MOSFET desaturation shutdown - Section 6.14 Status Registers - Section 7 Operating modes - Figure 16. Application diagram|
|06-May-2022|5|Updated : • Features in cover page • Figure 2. Configuration diagram (top view) • Table 2. Absolute maximum rating • Table 4. Supply specification • Table 13. Current sense amplifier with integrated ADC • Section 4.1 Current Sense Self Test • Figure 6. Current sense self test flow sequence • Section 4.2 External FET VDS Detection Self Test • Figure 7. VDS monitor self test flow sequence • Figure 8. External FET Stuck-on self test - flow sequence for entry • Section 5.1 Battery under-voltage shutdown • Table 34. ROM Memory Map (ID 12.2) Minor text changes.|
|27-May-2022|6|Modified Table 2. Absolute maximum ratings. Modified Figure 14. Timeout watchdog. Minor text changes.|
|14-Jul-2023|7|Updated Table 2. Absolute maximum ratings. Minor text changes.|
|17-Nov-2023|8|Updated Package silhouette on cover page. Updated Section 1 Block diagram and pin description. Removed column "ID" in all tables of Section 2.3 Main electrical characteristics. Updated Figure 6, Figure 7 and Figure 8. Updated Section 5.3 External MOSFET overtemperature shutdown. Updated Section 6.12 ROM memory map and Section 6.14 Status registers. Updated Section 7 Operating modes. Minor text changes.|


**DS13084** - **Rev 8** **page 44/49**


-----

### **VNF1048F**

**Contents**
## **Contents**
### **1 Block diagram and pin description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2** **2 Electrical specification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4**
#### 2.1 Absolute maximum ratings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.2 Thermal data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.3 Main electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
### **3 eFuse function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .14** **4 Self-test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16**
#### 4.1 Current sense self-test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16 4.2 External FET V DS detection self-test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .17 4.3 External FET stuck-on self-test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .18
### **5 Protections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20**
#### 5.1 Battery undervoltage shutdown. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20 5.2 Device overtemperature shutdown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20 5.3 External MOSFET overtemperature shutdown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 5.4 External MOSFET desaturation shutdown. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20 5.5 Hard short circuit latch-off . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21 5.6 Current vs time latch-off . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21 5.7 Low current bypass desaturation shutdown. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21
### **6 SPI functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .22**
#### 6.1 SPI Communication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .22 6.2 Signal description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23 6.3 SPI protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23 6.4 Operating code definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .24 6.5 Write mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .24 6.6 Read mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .25 6.7 Read and clear status command. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .25 6.8 SPI device information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26 6.9 Special commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26 6.10 Global status byte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .27 6.11 Address map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .28 6.12 ROM memory map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29 6.13 Control registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .30 6.14 Status registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32 6.15 Timeout watchdog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .36

**DS13084** - **Rev 8** **page 45/49**


-----

### **VNF1048F**

**Contents** **7 Operating modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37**
#### 7.1 State diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37 7.2 Power-on mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37 7.3 Standby mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .38 7.4 Wake-up mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .38 7.5 Unlocked mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .38 7.6 Locked mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .39 7.7 Self-test mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .39
### **8 Application information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .40** **9 Package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .41**
#### 9.1 QFN32L Epad (5.0x5.0x1.0 mm) package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
### **Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .43**

**DS13084** - **Rev 8** **page 46/49**


-----

### **VNF1048F**

**List of tables**
## **List of tables**

**Table 1.** Pin functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

**Table 2.** Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

**Table 3.** Thermal data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

**Table 4.** Supply specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
**Table 5.** SPI logic inputs (CSN, SCK, and SDI) specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
**Table 6.** SPI logic outputs (SDO) specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
**Table 7.** HWLO logic input pin specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
**Table 8.** DIAG logic output pin specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

**Table 9.** Device thermal shutdown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

**Table 10.** ST-SPI timings specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
**Table 11.** Charge pump specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
**Table 12.** External FET gate driver specification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
**Table 13.** Current sense amplifier with integrated ADC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
**Table 14.** External FET VDS protection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
**Table 15.** Hard short circuit protection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
**Table 16.** Overcurrent protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
**Table 17.** External FET thermal shutdown via NTC input. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
**Table 18.** Bypass switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
**Table 19.** V OUT A-to-D conversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

**Table 20.** Command byte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
**Table 21.** Input data byte 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
**Table 22.** Input data byte 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
**Table 23.** Input data byte 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
**Table 24.** Global status byte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
**Table 25.** Output data byte 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
**Table 26.** Output data byte 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
**Table 27.** Output data byte 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
**Table 28.** Operating codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
**Table 29.** 0xFF: (SW_Reset) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
**Table 30.** Clear all status registers (RAM access). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
**Table 31.** Global status byte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
**Table 32.** Global status byte - bit description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
**Table 33.** RAM memory map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
**Table 34.** ROM memory map. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
**Table 35.** CR#1: control register 1 (read/write); address 01h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
**Table 36.** CR#2: control register 2 (read/write); address 02h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
**Table 37.** CR#3: control register 3 (read/write); address 03h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
**Table 38.** SR#1: status register 1; address 11h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
**Table 39.** SR#2: status register 2; address 12h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
**Table 40.** SR#3: status register 3; address 13h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
**Table 41.** SR#4: status register 4; address 14h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
**Table 42.** SR#5: status register 5; address 15h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
**Table 43.** SR#6: status register 6; address 16h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
**Table 44.** SR#7: status register 7; address 17h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
**Table 45.** SR#8: status register 8; address 18h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
**Table 46.** Component value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
**Table 47.** QFN32L Epad (5.0x5.0x1.0 mm) package mechanical data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
**Table 48.** Document revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

**DS13084** - **Rev 8** **page 47/49**


-----

### **VNF1048F**

**List of figures**
## **List of figures**

**Figure 1.** Block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
**Figure 2.** Device pin connection diagram (top through view - not in scale) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
**Figure 3.** NTC bridge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

**Figure 4.** eFuse I [2] -t typical curve (VOC_thrs minimum - VHSC_thrs maximum) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

**Figure 5.** eFuse I [2] -t typical curve (generic thresholds) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
**Figure 6.** Current sense self-test flow sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
**Figure 7.** VDS monitor self-test flow sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
**Figure 8.** External FET stuck-on self-test - flow sequence for entry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
**Figure 9.** SPI functional diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
**Figure 10.** SPI write operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
**Figure 11.** SPI read operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
**Figure 12.** SPI read and clear operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
**Figure 13.** SPI read device information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
**Figure 14.** Timeout watchdog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
**Figure 15.** State diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
**Figure 16.** Application diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
**Figure 17.** QFN32L Epad (5.0x5.0x1.0 mm) package outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

**DS13084** - **Rev 8** **page 48/49**


-----

### **VNF1048F**

**IMPORTANT NOTICE – READ CAREFULLY**

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST
products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST
products are sold pursuant to ST’s terms and conditions of sale in place at the time of order acknowledgment.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of
purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

[ST and the ST logo are trademarks of ST. For additional information about ST trademarks, refer to www.st.com/trademarks. All other product or service names](http://www.st.com/trademarks)
are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2023 STMicroelectronics – All rights reserved

**DS13084** - **Rev 8** **page 49/49**


-----

