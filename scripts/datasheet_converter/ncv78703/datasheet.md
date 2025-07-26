# Multiphase Booster LED Driver for Automotive Front Lighting NCV78703

The NCV78703 is a single−chip and high efficient booster for smart
Power ballast and LED Driver designed for automotive front lighting
applications like high beam, low beam, DRL (daytime running light),
turn indicator, fog light, static cornering, etc. The NCV78703 is in
particular designed for high current LEDs and with NCV78723 (dual
channel buck)/713 (single channel) provides a complete solution to
drive multiple LED strings of up−to 60 V. It includes a current−mode
voltage boost controller which also acts as an input filter with a
minimum of external components. The available output voltage can be
customized. Two devices NCV78703 can be combined and the booster

circuits can operate together to function as a multiphase booster
(2−phase, 3−phase, 4−phase, 5−phase, 6−phase) in order to further
optimize the filtering effect of the booster and lower the total
application BOM cost for higher power. Thanks to the SPI
programmability, one single hardware configuration can support
various application platforms.

**Features**
##### • Single Chip • Multiphase Booster • High Overall Efficiency • Minimum of External Components • Active Input Filter with Low Current Ripple from Battery • Integrated Boost Controller • Programmable Input Current Limitation • High Operating Frequencies to Reduce Inductor Sizes • PCB Trace for Current Sense Shunt Resistor is Possible • Low EMC Emission • SPI Interface for Dynamic Control of System Parameters • Fail Save Operating (FSO) Mode, Stand−Alone Mode • Integrated Failure Diagnostic

**Typical Applications** • High Beam • Low Beam • DRL • Position or Park Light • Turn Indicator • Fog • Static Cornering


1 24

**QFNW24**

**MW SUFFIX**

**CASE 484AE**


**DATA SHEET**

**[www.onsemi.com](http://www.onsemi.com/)**

1 24

**QFNW24**

**MW SUFFIX**

**CASE 484AF**

|Col1|Col2|
|---|---|


**MARKING DIAGRAM**

N703−1

FALYW

�

Case 484AE

N78703−0

FAWLYYWW

�

Case 484AF

N703 = Specific Device Code
or N78703

F = Fab Indicator

A = Assembly Location
L or WL = Wafer Lot

Y or YY = Year

W or WW = Work Week

� = Pb−Free Package

**ORDERING INFORMATION**

See detailed ordering and shipping information on page 34 of
this data sheet.


© Semiconductor Components Industries, LLC, 2016 **1** Publication Order Number:
**February, 2024 − Rev. 1** **NCV78703/D**


-----

V_Batt

(after rev. pol. prot.)


C_BST_IN

C_BC2

C_BC1 R_BC1

##### **NCV78703**

**TYPICAL APPLICATION SCHEMATIC**

Vboost


V CC of MCU

R_SDO


C_BB

C_DRIVE

C_DD


� C


R_SENSE3

Phase 3

|VGATE 1 IBSTSENSE 1+ COMP IBSTSENSE 1− ON Semiconductor LED driver VBB 3 phase booster VDRIVE NCV78703 VGATE 2 IBSTSENSE 2+ VDD IBSTSENSE 2− ENABLE1,3 BSTSYNC/TST/TST1 FSO/ENABLE2 VGATE 3 SPI_SCLK/TST2 SPI_SDI IBSTSENSE 3+ SPI_SDO SPI_SCS IBSTSENSE 3− GND GNDP|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||


**Figure 1. Typical Application Schematic**


PWR GND

Sig GND


**Table 1. EXTERNAL COMPONENTS**

|Component|Function|Typ. Value|Unit|
|---|---|---|---|
|L1, L2, L3|Booster regulator coil|10|H |
|T1, T2, T3|Booster regulator switching transistor|e.g. NTD6416ANL||
|D1, D2, D3|Booster regulator diode|e.g. MBR5H100MFS||
|R_SENSE1, R_SENSE2, R_SENSE3|Booster regulator current sensing resistor|10|m|
|C_BST|Booster regulator output capacitor|0.44|F/W |
|C_BB|V decoupling capacitance (Note 1) BB|1|F |
|C_VDRIVE|Capacitor for V regulator DRIVE|1|F |
|C_VDRIVE_ESR|ESR of V capacitor DRIVE|max. 200|m|
|C_DD|V decoupling capacitor DD|1|F |
|C_DD_ESR|ESR of V capacitor DD|max. 200|m|
|R_SDO|SPI pull−up resistor|1|k|
|C_BC1|Booster compensation network|See Booster Compensator Model section||
|C_BC2|Booster compensation network|See Booster Compensator Model section||
|R_BC1|Booster compensation network|See Booster Compensator Model section||
|RD1|Booster output voltage feedback divider (Note 2)|107|k|
|RD2|Booster output voltage feedback divider (Note 2)|3.24|k|



1. The value represents a potential initial startup value on a generic application. The actual size of the boost capacitor depends on the
application defined requirements (such as power level, operating ranges, number of phases) and transient performances with respect to the
rest of BOM. Please refer to application notes and tools provided by **onsemi** for further guidance. The chosen value must be validated in
the application.
2. Proposed values. Divider ratio (BSTDIV_RATIO) has to be 34.

**[www.onsemi.com](http://www.onsemi.com/)**

**2**


-----

##### **NCV78703**

VBB

BSTSYNC,

TST1/TST2

GND GNDP

**Figure 2. Block Diagram**

**[www.onsemi.com](http://www.onsemi.com/)**

**3**


VBOOSTDIV

Comp

VGATE 1

IBSTSENSE 1+

IBSTSENSE 1−

VGATE 2

IBSTSENSE 2+

IBSTSENSE 2−

VGATE 3

IBSTSENSE 3+

IBSTSENSE 3−

|Booster LDR Error DIV amplifier LDR Vref Vdrive Bandgap Vref PWM Predriver POR Bias Current control sense CMP TSD Vdrive Digital OSC PWM Predriver OTP Current sense CMP 5V tolerant input Vdrive 5V tolerant input / OD output PWM Predriver Current sense CMP|Col2|Col3|
|---|---|---|
||||


-----

|24|Col2|23|Col4|22|Col6|21|Col8|20|Col10|19|
|---|---|---|---|---|---|---|---|---|---|---|

|7|Col2|8|Col4|9|Col6|10|Col8|11|Col10|12|
|---|---|---|---|---|---|---|---|---|---|---|


**Table 2. PIN DESCRIPTION**

##### **NCV78703**

**PACKAGE AND PIN DESCRIPTION**

24 23 22 21 20 19

7 8 9 10 11 12

**Figure 3. Pin Connections – QFNW24 5x5 and QFNW24 4x4**

**[www.onsemi.com](http://www.onsemi.com/)**

**4**

|Pin No. QFNW24|Pin Name|Description|I/O Type|
|---|---|---|---|
|1|ENABLE3|ENABLE3 input|MV in|
|2|VGATE1|Booster MOSFET gate pre−driver|MV out|
|3|VGATE2|Booster MOSFET gate pre−driver|MV out|
|4|VGATE3|Booster MOSFET gate pre−driver|MV out|
|5|IBSTSENSE3+|Coil3 current positive feedback input|MV in|
|6|IBSTSENSE3−|Coil3 current negative feedback input|MV in|
|7|GNDP|Power ground|Ground|
|8|IBSTSENSE1+|Coil1 current positive feedback input|MV in|
|9|IBSTSENSE1−|Coil1 current negative feedback input|MV in|
|10|IBSTSENSE2+|Coil2 current positive feedback input|MV in|
|11|IBSTSENSE2−|Coil2 current negative feedback input|MV in|
|12|FSO/ENABLE2|FSO/ENABLE2 input|MV in|
|13|SCLK/TST2|SPI clock / TST2 IO|MV in|
|14|CSB/SCS|SPI chip select (chip select bar)|MV in|
|15|SDI|SPI data input|MV in|
|16|SDO|SPI data output – pull up|MV open−drain|
|17|BSTSYNC/TST/TST1|External clock for the boost regulator/ TM entry/ TST1 IO|HV in|
|18|ENABLE1|ENABLE1 input|MV in|
|19|VBOOSTDIV|Booster high voltage feedback input|HV in|
|20|COMP|Compensation for the Boost regulator|LV in/out|
|21|GND|Ground|Ground|
|22|VDD|3 V logic supply|LV supply|
|23|VDRIVE|10 V supply|MV supply|
|24|VBB|Battery supply|HV supply|


-----

##### **NCV78703**

|Table 3. ABSOLUTE MAXIMUM RATINGS|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Characteristic|Symbol|Min|Max|Unit|
|Battery supply voltage (Note 4)|V BB|−0.3|36 (Note 3)|V|
|Logic supply voltage (Note 5)|V DD|−0.3|3.6|V|
|Gate driver supply voltage (Note 6)|V DRIVE|−0.3|12|V|
|Input current sense voltage (Note 7)|IBSTSENSEPx, IBSTSENSENx|−1.0|12|V|
|Medium voltage IO pins (Note 8)|IOMV|−0.3|6.5|V|
|Storage Temperature (Note 9)|T STRG|−50|150|C °|
|Electrostatic Discharge on Component Level (Note 10) Human Body Model Charge Device Model|V ESD_HBM V ESD_CDM|−2 −500|+2 +500|kV V|


Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality
should not be assumed, damage may occur and reliability may be affected.
3. Absolute maximum rating for VBB is 40 V for limited time < 0.5 s
4. Absolute maximum rating for pins: VBB, BSTSYNC/TST/TST1, VBOOSTDIV
5. Absolute maximum rating for pins: VDD, COMP
6. Absolute maximum rating for pins: VDRIVE, VGATE1, VGATE2, VGATE3
7. Absolute maximum rating for pins: IBSTSENSE1+, IBSTSENSE1−, IBSTSENSE2+, IBSTSENSE2−, IBSTSENSE3+, IBSTSENSE3−
8. Absolute maximum rating for pins: SCLK/TST2, CSB, SDI, SDO, ENABLE1, FSO/ENABLE2, ENABLE3
9. For limited time up to 100 hours. Otherwise the max storage temperature is 85 ° C.
10.This device series incorporates ESD protection and is tested by the following methods:
ESD Human Body Model tested per EIA/JESD22−A114
ESD Charge Device Model tested per ESD−STM5.3.1−1999
Latch−up Current Maximum Rating: � 100 mA per JEDEC standard: JESD78

Operating ranges define the limits for functional operation conditions; hence the Customer must contact
operation and parametric characteristics of the device. A ON Semiconductor in order to mutually agree in writing on
mission profile (Note 11) is a substantial part of the the allowed missions profile(s) in the application.

|Table 4. RECOMMENDED OPERATING RANGES|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Characteristic|Symbol|Min|Typ|Max|Unit|
|Battery supply voltage (Note 12 and 13)|V BB|5||30|V|
|Logic supply voltage (Note 14)|V DD|3.1||3.5|V|
|VDD current load|I DD|||50|mA|
|Medium voltage IO pins|IOMV|0||5|V|
|Input current sense voltage|IBSTSENSEPx, IBSTSENSENx|−0.1||1|V|
|Functional operating junction temperature range (Note 15)|T JF|−45||155|C °|
|Parametric operating junction temperature range (Note 16)|T JP|−40||150|C °|



Functional operation above the stresses listed in the Recommended Operating Ranges is not implied. Extended exposure to stresses beyond
the Recommended Operating Ranges limits may affect device reliability.
11. A mission profile describes the application specific conditions such as, but not limited to, the cumulative operating conditions over life time,
the system power dissipation, the system’s environmental conditions, the thermal design of the customer’s system, the modes, in which the
device is operated by the customer, etc. No more than 100 cumulated hours in life time above T tw .
12.Minimum V BB for OTP memory programming is 15.8 V.
13.VDRIVE is supplied from VBB, it must be verified that VDRIVE voltage is appropriate for the external FETs.
14.VBB > 5 V
15.The circuit functionality is not guaranteed outside the functional operating junction temperature range. Also please note that the device is
verified on bench for operation up to 170 ° C but that the production test guarantees 155 ° C only.
16.The parametric characteristics of the circuit are not guaranteed outside the Parametric operating junction temperature range.

|Table 5. THERMAL RESISTANCE|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Characteristic|Package|Symbol|Min|Typ|Max|Unit|
|Thermal Resistance Junction to Exposed Pad (Note 17)|QFNW24 4x4|Rthjp||2.82||C/W °|



17.Includes also typical solder thickness under the Exposed Pad (EP). Thermal resistance junction to PCB Top Layer.

**[www.onsemi.com](http://www.onsemi.com/)**

**5**


-----

##### **NCV78703**

**ELECTRICAL CHARACTERISTICS**

Note: All Min and Max parameters are guaranteed over full battery voltage (5 V; 30 V) and junction temperature (T JP ) range
(−40°C; 150°C), unless otherwise specified.

**Table 6. TEMPERATURE MEASUREMENTS**

**Table 7. VDRIVE: 10 V SUPPLY FOR BOOST FET GATE DRIVER CIRCUIT**

18.The VDRIVE voltage drop between VDRIVE and VBB has to be sufficient (min. 0.5 V).
19.Both of these conditions have to be fulfilled otherwise SPI status bit VDRIVE_NOK is set.
20.Relative threshold to typical value of VDRIVE_VSETPOINT settings.

**[www.onsemi.com](http://www.onsemi.com/)**

**6**

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Thermal Shutdown|TSD||165|170|175|C °|
|Thermal Warning|TW||155|160|165|C °|
|Thermal Output|TEMP7|ADC_TEMP_THR[2:0] = 111|140|150|160|C °|
|Thermal Output|TEMP6|ADC_TEMP_THR[2:0] = 110|130|140|150|C °|
|Thermal Output|TEMP5|ADC_TEMP_THR[2:0] = 101|120|130|140|C °|
|Thermal Output|TEMP4|ADC_TEMP_THR[2:0] = 100|110|120|130|C °|
|Thermal Output|TEMP3|ADC_TEMP_THR[2:0] = 011|100|110|120|C °|
|Thermal Output|TEMP2|ADC_TEMP_THR[2:0] = 010|90|100|110|C °|
|Thermal Output|TEMP1|ADC_TEMP_THR[2:0] = 001|80|90|100|C °|
|Thermal Output|TEMP0|ADC_TEMP_THR[2:0] = 000|70|80|90|C °|
|Thermal Output Hysteresis|TEMP_HYST|||3||C °|

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDRIVE reg. voltage from VBB (Note 18)|VDRV_15|[VDRIVE_VSETPOINT = 1111], Vbb − VDRIVE > 0.5 V @IDRIVE = 90 mA|9.7|10.1|10.7|V|
|VDRIVE reg. voltage from VBB (Note 18)|VDRV_00|[VDRIVE_VSETPOINT = 0000], Vbb − VDRIVE > 0.5 V @IDRIVE = 90 mA|4.8|5|5.3|V|
|VDRIVE increase per code (Note 18)|VDRV |Linear increase, 4 bits||0.34||V|
|DC output current consumption|VDRV_ILIM||0||90|mA|
|Output current limitation|VDRV_BB_IL||90||500|mA|
|Output overload condition for VDRIVE_NOK detection (Note 19)|VDRIVE_NOK_ILOAD||95|||mA|
|Minimum VBB−VDRIVE sufficient voltage (Note 19)|VDRIVE_NOK_VBBLOW||0.5|||V|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[7]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 111]|83|87|91|%|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[6]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 110]|79|83|87|%|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[5]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 101]|75|79|84|%|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[4]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 100]|71|75|79|%|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[3]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 011]|63|67|71|%|


-----

##### **NCV78703**

**Table 7. VDRIVE: 10 V SUPPLY FOR BOOST FET GATE DRIVER CIRCUIT**

18.The VDRIVE voltage drop between VDRIVE and VBB has to be sufficient (min. 0.5 V).
19.Both of these conditions have to be fulfilled otherwise SPI status bit VDRIVE_NOK is set.
20.Relative threshold to typical value of VDRIVE_VSETPOINT settings.

**Table 8. VDD: 3 V LOW VOLTAGE ANALOG AND DIGITAL SUPPLY**

**Table 9. POR: POWER−ON RESET CIRCUIT**

**Table 11. OSC10M: SYSTEM OSCILLATOR CLOCK**

21.All parameters are guaranteed for recommended external Vboost resistor divider (Rdiv) ratio 34 with ± 1% tolerance.
22.Higher levels are valid if BST_VLIMTH value 2 or 3 (BOOST_VLIMTHx[1] = 1) is selected at least on one channel.

**[www.onsemi.com](http://www.onsemi.com/)**

**7**

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[2]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 010]|54|58|62|%|
|VDRIVE UV detection threshold (Note 20)|VDRV_UV_[1]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 001]|46|50|54|%|
|VDRIVE UV detection threshold|VDRV_UV_[0]|Relative threshold to actual VDRIVE_VSETPOINT {VDRIVE_UV_THR = 000]||0||%|
|VDRIVE UV detection delay|VDRV_UV_DL||5||35|s |

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VDD regulator output voltage|V DD|Vbb > 5 V|3.135||3.465|V|
|DC output current consumption|VDD_IOUT|Vbb > 5 V, including 10 mA self current consumption|||50|mA|
|Output current limitation|VDD_ILIM||60||350|mA|

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|POR Toggle level on VDD rising|POR3V_H||2.55||3.05|V|
|POR Toggle level on VDD falling|POR3V_L||2.3||2.8|V|
|POR Hysteresis|POR3V_HYST|||0.15||V|
|POR threshold on VBB, VBB rising|POR_VBB_H|Applicable only during startup (VBB is rising)|3.8||4.3|V|

|Table 10. OTP MEMORY|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|Min. VBB for OTP zapping|VBB_OTP||15.8|||V|
|VBB range for OTP_FAIL flag during OTP programming|VBB_OTP_L||13.2|14.1|15|V|

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|System oscillator frequency|FOSC10M||7|10|13|MHz|

|Table 12. BOOSTER (Note 21)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|Booster overvoltage shutdown|BST_OV_127|[BOOST_OVERVOLTSD_THR =1111111], DC level|63.8|65.85|67.9|V|
|Booster overvoltage shutdown|BST_OV_022|[BOOST_OVERVOLTSD_THR =0010110], DC level|11|11.5|12|V|
|Booster overvoltage shutdown increase per code|BST_OV |Linear increase, 7 bits||0.518|0.718|V|


-----

##### **NCV78703**

21.All parameters are guaranteed for recommended external Vboost resistor divider (Rdiv) ratio 34 with ± 1% tolerance.
22.Higher levels are valid if BST_VLIMTH value 2 or 3 (BOOST_VLIMTHx[1] = 1) is selected at least on one channel.

**[www.onsemi.com](http://www.onsemi.com/)**

**8**

|Table 12. BOOSTER (Note 21)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|Booster overvoltage re−activation|BST_RA_3|[BOOST_OV_REACT =11], V to the Vboost reg. overvoltage protec- tion, DC level|−1.9|−1.5|−1.1|V|
|Booster overvoltage re−activation|BST_RA_0|[BOOST_OV_REACT =00], V to the Vboost reg. overvoltage protec- tion, DC level||0||V|
|Booster overvoltage re−activa- tion decrease per code|BST_RA |Linear decrease, 2 bits, DC level|−0.6|−0.5||V|
|Booster undervoltage protection (external divider fail state detec- tion)|BST_EA_UV||3.45|3.95|4.45|V|
|Booster undervoltage protection (external divider fail state detec- tion) hysteresis|BST_EA_UV_HYST|||0.6||V|
|Booster regulation level|BST_REG_125|[BOOST_VSETPOINT =1111101], DC level|62.8|64.8|66.8|V|
|Booster regulation level|BST_REG_022|[BOOST_VSETPOINT =0010110], DC level|10.8|11.5|12.2|V|
|Booster regulation level increase per code|BST_REG |Linear increase, 7 bits||0.518|0.718|V|
|Transconductance gain of Error amplifier|BST_EA_GM3|[BOOST_OTA_GAIN =11], seen from VBOOST, DC value|63|90|117|S |
|Transconductance gain of Error amplifier|BST_EA_GM2|[BOOST_OTA_GAIN =10], seen from VBOOST, DC value|42|60|78|S |
|Transconductance gain of Error amplifier|BST_EA_GM1|[BOOST_OTA_GAIN =01], seen from VBOOST, DC value|21|30|39|S |
|Transconductance gain of Error amplifier|BST_EA_GM0|[BOOST_OTA_GAIN =00], high impedance||0||S |
|EA max output current|EA_IOUT_POS||150|||A |
|EA min output current|EA_IOUT_NEG||||−150|A |
|Output leakage current in tri−state|EA_ILEAK|Output in tri−state (EA_GM0)|−1||1|A |
|EA output resistance|EA_ROUT|||2.0||M|
|EA max output voltage_3|COMP_CLH_3|BOOST_SLPCTRL[2]=1, OR of all BOOST_VLIMTHx[1]=1|2.1|2.26||V|
|EA max output voltage_2|COMP_CLH_2|BOOST_SLPCTRL[2]=1, OR of all BOOST_VLIMTHx[1]=0||1.98||V|
|EA max output voltage_1|COMP_CLH_1|BOOST_SLPCTRL[2]=0, OR of all BOOST_VLIMTHx[1]=1||1.64||V|
|EA max output voltage_0|COMP_CLH_0|BOOST_SLPCTRL[2]=0, OR of all BOOST_VLIMTHx[1]=0||1.35||V|
|EA min output voltage|COMP_CLL||||0.4|V|
|Booster VOOSTDIV pin input pull up current|BST_EA_DIV_INI|Pull current source towards to VDD voltage|0.4|0.8|1.4|A |
|Division of COMP on the Current comparator input|COMP_DIV_15|[P_DISTRIBUTIONx =01111], signed, see Power Distribution sec- tion and Table 19 for details||20|||
|Division of COMP on the current comparator input|COMP_DIV_0|[P_DISTRIBUTIONx =00000], signed, see Power Distribution sec- tion and Table 19 for details||6.81|||
|Division of COMP on the current comparator input|COMP_DIV_−16|[P_DISTRIBUTIONx =11111], signed, see Power Distribution sec- tion and Table 19 for details||4|||


-----

##### **NCV78703**

21.All parameters are guaranteed for recommended external Vboost resistor divider (Rdiv) ratio 34 with ± 1% tolerance.
22.Higher levels are valid if BST_VLIMTH value 2 or 3 (BOOST_VLIMTHx[1] = 1) is selected at least on one channel.

**[www.onsemi.com](http://www.onsemi.com/)**

**9**

|Table 12. BOOSTER (Note 21)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|Voltage shift on COMP on Cur- rent comparator input|COMP_VSF|||+0.5||V|
|Booster skip cycle for low cur- rents (Note 22)|BST_SKCL_3|[BOOST_SKCL =11], Booster dis- abled for lower V(COMP)||0.7/0.8||V|
|Booster skip cycle for low cur- rents (Note 22)|BST_SKCL_2|[BOOST_SKCL =10], Booster dis- abled for lower V(COMP)||0.625/0.7||V|
|Booster skip cycle for low cur- rents (Note 22)|BST_SKCL_1|[BOOST_SKCL =01], Booster dis- abled for lower V(COMP)||0.55/0.6||V|
|VGATE comparator to start BST_TOFF time|BST_VGATE_THR_1|[VBOOST_VGATE_THR = 1]||1.2||V|
|VGATE comparator to start BST_TOFF time|BST_VGATE_THR_0|[VBOOST_VGATE_THR = 0]||0.4||V|
|Booster minimum OFF time|BST_TOFF_7|[VBOOST_TOFF_SET = 111], time from VGATE below VBOOST_VGATE_THR|780|1200|1620|ns|
|Booster minimum OFF time|BST_TOFF_6|VBOOST_TOFF_SET = 110], time from VGATE below VBOOST_VGATE_THR|300|460|620|ns|
|Booster minimum OFF time|BST_TOFF_5|VBOOST_TOFF_SET = 101], time from VGATE below VBOOST_VGATE_THR|260|400|540|ns|
|Booster minimum OFF time|BST_TOFF_4|VBOOST_TOFF_SET = 100], time from VGATE below VBOOST_VGATE_THR|220|340|460|ns|
|Booster minimum OFF time|BST_TOFF_3|VBOOST_TOFF_SET = 011], time from VGATE below VBOOST_VGATE_THR|180|280|380|ns|
|Booster minimum OFF time|BST_TOFF_2|VBOOST_TOFF_SET = 010], time from VGATE below VBOOST_VGATE_THR|140|220|300|ns|
|Booster minimum OFF time|BST_TOFF_1|VBOOST_TOFF_SET = 001], time from VGATE below VBOOST_VGATE_THR|100|160|220|ns|
|Booster minimum OFF time|BST_TOFF_0|VBOOST_TOFF_SET = 000], time from VGATE below VBOOST_VGATE_THR|60|100|140|ns|
|Booster minimum ON time|BST_TON_7|[VBOOST_TON_SET =111], time from internal signal for VGATE drive|330|530|730|ns|
|Booster minimum ON time|BST_TON_6|[VBOOST_TON_SET =110], time from internal signal for VGATE drive|300|480|660|ns|
|Booster minimum ON time|BST_TON_5|[VBOOST_TON_SET =101], time from internal signal for VGATE drive|270|430|590|ns|
|Booster minimum ON time|BST_TON_4|[VBOOST_TON_SET =100], time from internal signal for VGATE drive|240|380|520|ns|
|Booster minimum ON time|BST_TON_3|[VBOOST_TON_SET =011], time from internal signal for VGATE drive|210|330|450|ns|
|Booster minimum ON time|BST_TON_2|[VBOOST_TON_SET =010], time from internal signal for VGATE drive|180|280|380|ns|
|Booster minimum ON time|BST_TON_1|[VBOOST_TON_SET =001], time from internal signal for VGATE drive|150|230|310|ns|
|Booster minimum ON time|BST_TON_0|[VBOOST_TON_SET =000], time from internal signal for VGATE drive|120|180|240|ns|


-----

##### **NCV78703**

**Table 13. BOOSTER – CURRENT REGULATION AND LIMITATION**

**Table 14. BOOSTER – PRE−DRIVER**

**Table 15. 5 V TOLERANT DIGITAL INPUTS (SCLK/TST2, CSB, SDI, BSTSYNC/TST/TST1, ENABLE1, FSO/ENABLE2,**

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Current comparator for Imax de- tection|BST_VLIMTHx_3|[BOOST_VLIMTHx =11], DC level of threshold voltage|95|100|105|mV|
|Current comparator for Imax de- tection|BST_VLIMTHx_2|[BOOST_VLIMTHx =10], DC level of threshold voltage|75|80|85|mV|
|Current comparator for Imax de- tection|BST_VLIMTHx_1|[BOOST_VLIMTHx =01], DC level of threshold voltage|57|62.5|67|mV|
|Current comparator for Imax de- tection|BST_VLIMTHx_0|[BOOST_VLIMTHx =00], DC level of threshold voltage|45|50|55|mV|
|Current comparator for Vboost regulation, offset voltage|BST_OFFS||−10||10|mV|
|Booster slope compensation|BST_SLPCTRL_7|BOOST_SLPCTRL =111], see Power Distribution section||290 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_6|BOOST_SLPCTRL =110], see Power Distribution section||190 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_5|BOOST_SLPCTRL =101], see Power Distribution section||120 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_4|BOOST_SLPCTRL =100], see Power Distribution section||85 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_3|BOOST_SLPCTRL =011], see Power Distribution section||50 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_2|BOOST_SLPCTRL =010], see Power Distribution section||35 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_1|BOOST_SLPCTRL =001], see Power Distribution section||17 / COMP_DIV||mV/ s |
|Booster slope compensation|BST_SLPCTRL_0|BOOST_SLPCTRL =000], see Power Distribution section||0||mV/ s |
|Sense voltage common mode range|CMVSENSE|Over full operating range|−0.1||1|V|


|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|High−side switch impedance|RONHI|t = 25 C °||4.2|||
|High−side switch impedance|RONHI|t = 150 C °||6|7||
|Low−side switch impedance|RONLO|t = 25 C °||4.2|||
|Low−side switch impedance|RONLO|t = 150 C °||6|7||
|Pull down resistor on VGATEx|RPDOWN|||10||k|


|ENABLE3)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|High−level input voltage|VINHI|SDI, BSTSYNC, CSB and SCLK/TST2|2|||V|
|Low−level input voltage|VINLO|SDI, BSTSYNC, CSB and SCLK/TST2|||0.8|V|
|Pull resistance (Note 23)|Rpull|SDI, BSTSYNC, CSB and SCLK/TST2|40||160|k|
|High−level input voltage|ENA_VINHI|ENABLE1, FSO/ENABLE2, ENABLE3|2.35|||V|
|Low−level input voltage|ENA_VINLO|ENABLE1, FSO/ENABLE2, ENABLE3|||0.7|V|
|Pull resistance (Notes 23 and 24)|ENA_Rpull|ENABLE1, FSO/ENABLE2, ENABLE3|20||400|k|



23.Internal pull down resistor (Rpd) for SDI, ENABLE1, FSO/ENABLE2, ENABLE3, BSTSYNC and SCLK/TST2, pull up resistor (Rpu) for CSB
to VDD.
24.VDD > POR3V_H; ENA_Rpull > 20 k � when VDD = 0 V to 3.5 V

**[www.onsemi.com](http://www.onsemi.com/)**

**10**


-----

##### **NCV78703**

**Table 16. 5 V TOLERANT OPEN−DRAIN DIGITAL OUTPUT (SDO)**

|Characteristic|Symbol|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Low−voltage output voltage|VOUTLO|Iout = −10 mA (current flows into the pin)|||0.4|V|
|Equivalent output resistance|RDSON|Lowside switch||20|40||
|SDO pin leakage current|SDO_ILEAK||||2|A |
|SDO pin capacitance (Note 25)|SDO_C||||10|pF|
|CLK to SDO propagation delay|SDO_DL|Low−side switch activation/deactivation time; @1 k to 5 V, 100 pF to GND, for falling edge V(SDO) goes below 0.5 V|||60|ns|



25.Guaranteed by bench measurement, not tested in production.

|Table 17. SPI INTERFACE|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Characteristic|Symbol|Min|Typ|Max|Unit|
|CSB setup time|t CSS|0.5|||s |
|CSB hold time|t CSH|0.25|||s |
|SCLK low time|t WL|0.5|||s |
|SCLK high time|t WH|0.5|||s |
|Data−in (DIN) setup time, valid data before rising edge of CLK|t SU|0.25|||s |
|Data−in (DIN) hold time, hold data after rising edge of CLK|t H|0.275|||s |
|Output (DOUT) disable time (Note 26)|t DIS|0.07||0.32|s |
|Output (DOUT) valid (Note 26)|t V1→0|||0.32|s |
|Output (DOUT) valid (Note 27)|t V0→1|||0.32 + t(RC)|s |
|Output (DOUT) hold time (Note 26)|t HO|0.07|||s |
|CSB high time|t CS|1|||s |



26.SDO low–side switch activation time
27.Time depends on the SDO load and pull–up resistor

**Figure 4. SPI Communication Timing**

**[www.onsemi.com](http://www.onsemi.com/)**

**11**


|CS VIH edIn git eia il s dta ot ne to cf S reC L ,K ta cf ate nr bC eS lB wfa olli rn hg s ’ a i o igh CSB VIL tCSS tWH tWL tCSH VIH SCLK VIL tSU tH VIH DIN DIN 15 DIN14 DIN 13 DIN1 DIN0 VIL tV tHO tDIS VIH DOUT DOUT 15 DOUT 14 DOUT 13 DOUT 1 DOUT 0 HI−Z HI−Z V|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||


-----

##### **NCV78703**

**Typical Characteristics**

**Figure 5. Typical temperature dependency of VGATE high and low side switch impedances**

**DETAILED OPERATING DESCRIPTION**

**Supply Concept in General**
Low operating voltages become more and more required due to the growing use of start stop systems. In order to respond
to this necessity, the NCV78703 is designed to support power−up starting from VBB = 5 V.

**Figure 6. Cranking Pulse (ISO7637−1): System has to be fully functional (Grade A) from Vs = 5 V to 28 V**


**VDRIVE Supply**
The VDRIVE supply voltage represents the power for the
complete booster pre−driver block which generates the
VGATE, used to switch the booster MOSFETs. The voltage
is programmable via SPI in 16 different values (register
VDRIVE_VSETPOINT[3:0], ranging from a minimum of
5 V typical to 10.1 V typical: see Table 7). This feature
allows having the best switching losses vs. resistive losses
trade off, according to the MOSFET selection in the


application, also versus the minimum required battery
voltage.
VDRIVE supply takes its energy from VBB battery
voltage. Minimal VDRIVE regulator voltage drop is about
0.5 V. To ensure that booster can be operated close to
minimal VBB battery voltage, logic level MOSFETs should
be considered. By efficiency reasons, it is important to select
MOSFETs with low gate charge. External MOSFETs are


**[www.onsemi.com](http://www.onsemi.com/)**

**12**


-----

##### **NCV78703**


controlled by the integrated pre−driver with slope control to
reduce EMC emissions.

VDRIVE Undervoltage Lockout safety mechanism
monitors sufficient voltage for MOSFETs and protects them
by switching off the booster when VDRIVE voltage is too
low. During initial 150 μs after POR the detection is disabled
to ensure that normal operating mode is entered. Detection
level is set by VDRIVE_UV_THR[2:0] register relatively to
used VDRIVE voltage. Detection thresholds are
summarized in Table 7. When VDRIVE_UV_THR[2:0] =
0, function is disabled.

**VDD Supply**
The VDD supply is the low voltage digital and analog
supply for the chip and derives energy from VBB. Due to the
low dropout regulator design, VDD is guaranteed already
from low VBB voltages.
The Power−On−Reset circuit (POR) monitors the VDD
and VBB voltages to control the out−of−reset condition at
power−up. At least one ENABLE input is required to be in
logic ‘1’ to enable the VDD regulator and leave reset state.
When SPI register VDD_ENA is set to ‘1’, VDD regulator
stays enabled and chip stays in normal mode, even if all
ENABLEx (x = 1, 2) inputs are set to logic ‘0’. When SPI
register VDD_ENA is set to ‘0’ and all ENABLEx inputs are
set to logic ‘0’, chip enters the reset state and VDD regulator
is switched off.

VDD regulator is dimensioned to supply up to 8
NCV78713/NCV78723 buck devices.

**Internal Clock Generation – OSC10M**

An internal RC clock named OSC10M is used to run all

the digital functions in the chip. The clock is trimmed in the
factory prior to delivery. Its accuracy is guaranteed under
full operating conditions and is independent from external
component selection (refer to Table 11 for details). All
timings depend on OSC10M accuracy.

**Boost Regulator**

**General**

The booster stage provides the required voltage source for
the LED string voltages out of the available battery voltage.
Moreover, it filters out the variations in the battery input
current in case of LED strings PWM dimming.
For nominal loads, the boost controller will regulate in
*continuous mode* of operation, thus maximizing the system
power efficiency at the same time having the lowest possible


input ripple current (with “continuous mode” it is meant that
the supply current does not go to zero while the load is
activated). Only in case of very low loads or low dimming
duty cycle values, *discontinuous mode* can occur: this means
the supply current can swing from zero when the load is off,
to the required peak value when the load is on, while keeping
the required input average current through the cycle. In such
situations, the total efficiency ratio may be lower than the
theoretical optimal. However, as also the total losses will at
the same time be lower, there will be no impact on the
thermal design.
On top of the using phases available in the device, the
device can be combined with more NCV78702/NCV78703
devices in the application to gain even more phases. More
details about the multichip−multiphase mode can be found
in the dedicated section.

**Booster Regulation Principles**
The NCV78703 features a *current−mode* voltage boost
controller, which regulates the VBOOST line used by the
buck converters. The regulation loop principle is shown in
the following picture. The loop compares the reference
voltage (BOOST_VSETPOINT) with the actual measured
voltage at the VBOOST pin, thus generating an error signal
which is treated internally by the error trans−conductance
amplifier (block A1). This amplifier transforms the error
voltage into current by means of the trans−conductance gain
Gm. The amplifier’s output current is then fed into the
external compensation network impedance (A2), so that it
originates a voltage at the VCOMP pin, this last used as a
reference by the current control block (B).
The current controller regulates the duty cycle as a
consequence of the VCOMP reference, the sensed inductor
peak current via the external resistor R SENSE and the slope
compensation used. The power converter (block C)
represents the circuit formed by the boost converter
externals (inductor, capacitors, MOSFET and forward
diode). The load power (usually the LED power going via
the buck converters) is applied to the converter. The
controlled variable is the boost voltage, measured directly at
the device VBOOST pin with a unity gain feedback
(block F). The picture highlights as block G all the elements
contained inside the device. The regulation parameters are
flexibly set by a series of SPI commands. A detailed internal
boost controller block diagram is presented in the next
section.


**[www.onsemi.com](http://www.onsemi.com/)**

**13**


-----

##### **NCV78703**

**Figure 7. NCV78703 Boost Control Loop – Principle Block Diagram**


**Boost Controller Detailed Internal Block Diagram**
A detailed NCV78703 boost controller block diagram is
provided in this section. The main signals involved are
indicated, with a particular highlight on the SPI
programmable parameters.


The blocks referring to the principle block diagram are
also indicated. In addition, the protection specific blocks can
be found (see dedicated sections for details).

C_BC2


L


D



RD1 RD2

|Col1|Col2|Col3|Col4|
|---|---|---|---|


**Figure 8. Boost Controller Internal Detailed Block Diagram**

**[www.onsemi.com](http://www.onsemi.com/)**

**14**


-----

BOOSTx_SYNC [1,2,3]

BOOSTx_SYNC [1,2,3]

Ireg or Imax cmp [1,2,3]

BOOST_TOFF [1,2,3]

BOOST_TON [1,2,3]

VGATE_LOW [1,2,3]

##### **NCV78703**

**Figure 9. Boost Controller Internal Waveforms**

|C [1,2,3]|Col2|Col3|Col4|Col5|Col6|GATE reset|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|[1,2,3]|||||||||
|p [1,2,3]|Pulse masked during min TON n TOFF Min Min TON OFF time by IREG comp. & TOFF gen ON time by IREG /IMAX comp.|||Pulse masked during min TON TOFF M Min TON /IMAX OFF time b erator & VGATE c ON time by BOOST _SYN signal||in TOFF Min TON y BOOST _SYN si g. omp. & TOFF gen. ON time by TON generator|||
|Mi|||||||||
||||||||||
|FF [1,2,3]|||||||||
||||||||||
||||||||T _SYN s TOFF ge ime by T||
|N [1,2,3] E [1,2,3]|||OFF time by IREG omp. & TOFF gen .|/IMAX erator||y BOOS omp. & ON t||i g. n. ON generator|
||||||||||
||||||||||
||||||||||
|W [1,2,3]|||||||||


**Booster Regulator Setpoint (BOOST_VSETPOINT)**
The booster voltage VBOOST is regulated around the
target programmable by the 7−bit SPI setting
BOOST_VSETPOINT[6:0], ranging from a minimum of
11.5 V to a maximum of typical 64.8 V (please refer to
Table 12 for details). Due to the step−up only characteristic
of any boost converter, the boost voltage cannot obviously
be lower than the supply battery voltage provided. Therefore
a target of 11.5 V would be used only for systems that require
the activation of the booster in case of battery drops below
the nominal level. At power−up, the booster is disabled and
the setpoint is per default the minimum (all zeroes).

**Booster Overvoltage Shutdown Protection**
An integrated comparator monitors VBOOST in order to
protect the external booster components from overvoltage.
When the voltage rises above the threshold defined by the
BOOST_OVERVOLTSD_THR[6:0], ranging from a
minimum 11.5 V to a maximum of typical 65.85 V (please
refer to Table 12 for details), the MOSFET gate is
switched−off at least for the current PWM cycle and at the
same time, the boost overvoltage flag in the status register
will be set (BOOST_OV = ‘1’), together with the


BOOSTx_STATUS flags equal to zero. The PWM runs
again as from the moment the VBOOST will fall below the
reactivation hysteresis defined by the
BOOST_OV_REACT[1:0] SPI parameter. Therefore,
depending on the voltage drop and the PWM frequency, it
might be that more than one cycle will be skipped. A
graphical interpretation of the protection levels is given in
the figure below, followed by a summary table (Table 18).
###### [V]

Boost overvoltage shutdown

(BOOST_OVERVOLTSD_THR)

Boost overvoltage reactivation

(BOOST_OVERVOLTSD_THR - BOOST_OV_REACT)

BOOST_VSETPOINT

**Figure 10. Booster voltage protection levels with**
**respect to the setpoint**


**Table 18. BOOST OVERVOLTAGE PROTECTION LEVES AND RELATED DIAGNOSTIC**

**[www.onsemi.com](http://www.onsemi.com/)**

**15**

|Case|Condition|PWM gate control|SPI flags|Col5|
|---|---|---|---|---|
||||BOOSTx_STATUS|BOOST_OV|
|A|V < BOOST_VSETPOINT BOOST|Normal (not disabled)|1|0|
|B|V > BOOST_OVERVOLTSD_THR BOOST|Disabled until case ‘C’|0|1 (latched)|
|C|V < BOOST_OVERVOLTSD_THR − BOOST BOOST_OV_REACT|Re−enables the PWM, normal mode resumed if from case ‘B’|1|1 (latched, if read in this condition, it will go back to ‘0’|


-----

##### **NCV78703**


**Booster Current Regulation Loop**
The peak−current level of the booster is set by the voltage
of the compensation pin COMP, which is output of the
trans−conductance error amplifier, “block B” of Figure 7.
This reference voltage is fed to the current comparator via
a divider (divider ratio of which can be set by Power sharing
function for each phase independently, see “Power
Distribution” section for more details. The comparator
compares this reference voltage with voltage V SENSE sensed
on the external sense resistor R SENSE, connected to the pins
IBSTSENSE1/2/3+ and IBSTSENSE1/2/3−. The sense
voltage is created by the booster inductor coil current when

D x

V IN1


the MOSFET is switched on and is summed up to an
additional offset of +0.5 V (see COMP_VSF in Table 12)
and on top of that, a slope compensation voltage ramp is
added. The slope compensation is programmable by SPI via
the BOOST_SLPCTRL[2:0] register and can also be
disabled. Due to the offset, current can start flowing in the
circuit when V COMP - COMP_VSF.
When booster is active, voltage at COMP pin is clamped
to voltage between 0.4 V (see Table 12) and 1.35 V to 2.26 V
depending on BOOST_VLIMTHx and BOOST_SLPCTRL
settings (see Table 13) to ensure quicker reaction of the
system to load changes.

V COMP


**Figure 11. Booster Peak Current Regulator Involved in the Current Control Loop**


**Booster Current Limitation Protection**

On top of the normal current regulation loop comparator,
an additional comparator clamps the maximum physical
current that can flow in the booster input circuit while the
MOSFET is driven. The aim is to protect all the external
components involved (boost inductor from saturation, boost
diode and boost MOSFET from overcurrent, etc...). The
protection is active PWM cycle−by−cycle and switches off
the MOSFET gate when V SENSE reaches its maximum
threshold defined by the BOOST_VLIMTHx[1:0] register
(see Table 13 for more details). Therefore, the maximum
allowed peak current will be defined by the ratio I PEAK_MAX
= BOOST_VLIMTHx[1:0]/R SENSE . The maximum current
must be set in order to allow the total desired booster power
for the lowest battery voltage. Warning: setting the current
limit too low may generate unwanted system behavior as
uncontrolled de−rating of the LED light due to insufficient

power.

**Booster PWM Internal Generation**

Internally generated booster PWM signal is used only in
FSO modes. When FSO mode is entered, booster PWM


source is switched automatically from the external
BSTSYNC pin to the internally generated signal, which is
derived from the internal oscillator OSC10M. A selection of

the frequencies is enabled by the register
FSO_BST_FREQ[2:0], ranging from typical 200 kHz to
typical 1 MHz (Table 22).

**Booster PWM External Generation**

In normal operation mode the booster PWM is taken
directly from the BSTSYNC device pin. Maximum
frequency at the BSTSYNC pin is 1 MHz. There is no actual
limitation in the resolution, apart from the system clock for
the sampling and a debounce of two clock cycles on the
signal edges. The gate PWM is synchronized with either the
rising or falling edge of the external signal depending on the
BOOST_SRCINV bit value. The default POR value is “0”
and corresponds to synchronization to the rising edge.
BOOST_SRCINV equals “1” selects falling edge
synchronization. Thanks to the possibility to invert external
clock in the chip by SPI, up to 6−phase systems with shifted
clock are supported with only 1 external clock.


**[www.onsemi.com](http://www.onsemi.com/)**

**16**


-----

BSTSYNC p in


Debounce


BOOST1_SYNC


PWM internal generation
(FSO mode)


Normal / FSO mode

##### **NCV78703**

SPI TSD

SPI TW

BOOST2_SYNC_INT

BOOST3_SYNC_INT

BOOST1_EN (SPI)

BOOST_SRCINV (SPI) (SPI)

**Figure 12. Generation of BOOSTx_SYNC**


BOOST_DIV3/DIV2 = `0'

|STSYNC input|DIV BY 2|BOOST1_SYNC|
|---|---|---|
|||BOOST2_SYNC|
|||BOOST3_SYNC|



BSTSYNC input

BOOST1_SYNC_INT

BOOST2_SYNC_INT

Disabled

BOOST3_SYNC_INT

BOOST_DIV3/DIV2 = `1'

|STSYNC input|DIV BY 3|BOOST1_SYNC|
|---|---|---|
|||BOOST2_SYNC|
|||BOOST3_SYNC|



BSTSYNC input

BOOST1_SYNC_INT

BOOST2_SYNC_INT


BOOST3_SYNC_INT


**Figure 13. PWM Generation (2−phase and 3−phase)**

**[www.onsemi.com](http://www.onsemi.com/)**

**17**


-----

##### **NCV78703**


**Booster PWM Min TOFF and Min TON Protection**

As additional protection, the PWM duty cycle is
constrained between a minimum and a maximum, defined
per means of two parameters available in the device.
The PWM *minimum on−time* is programmable via
VBOOST_TON_SET[2:0]: its purpose is to guarantee a
minimum activation interval for the booster MOSFET gate,
to insure full drive of the component and avoiding switching
in the linear region. Please note that this does not imply that
the PWM is always running even when not required by the
control loop, but means that whenever the MOSFET should
be activated, then its on time would be at least the one
specified. At the contrary when no duty cycle at all is
required, then it will be zero.
The PWM *minimum off−time* is set via the parameter
VBOOST_TOFF_SET[2:0]: this parameter is limiting the
maximum duty cycle that can be used in the regulation loop
for a defined period T PWM :

T T
##### � PWM � OFFMIN �
Duty MAX � T

PWM

The main aim of a maximum duty cycle is preventing
MOSFET shoot−through in cases the (transient) duty cycle
would get too close to 100% of the MOSFET real switch−off
characteristics. In addition, as a secondary effect, a limit on
the duty cycle may also be exploited to minimize the inrush
current when the load is activated. Warning : a wrong setting
of the duty cycle constraints may result in unwanted system
behavior. In particular, a too big
VBOOST_TOFF_SET[2:0] may prevent the system to
regulate the VBOOST with low battery voltages (VBAT).
This can be explained by the simplified formula for booster
steady state continuous mode:

V V
V BOOST � (1 � BAT Duty) [�] [Duty] [ �] [1] [ �] V BOOST BAT

So in order to reach a desired V BOOST for a defined supply
voltage, a certain duty cycle must be guaranteed.

Vin i L Vds D Vout

Cout


RD2


**Booster Compensator Model**
A linear model of the booster controller compensator
(block “A” Figure 7) is provided in this section. The
protection mechanisms around are not taken into account. A
type “2” network is taken into account at the VCOMP pin.
The equivalent circuit is shown below:

V COMP (t)

R 1

G m e(t) R OUT R P C P

C 1

**Figure 14. Booster Compensator Circuit with Type**
**“2” Network**

In the Figure, e(t) represents the control error, equals to the
difference BOOST_VSETPOINT(t) − V BOOST (t). “G m ” is
the trans−conductance error amplifier gain, while “R OUT ” is
the amplifier internal output resistance. The values of these
two parameters can be found in Table 12 in this datasheet. By
solving the circuit in Laplace domain the following error to
V COMP transfer function is obtained:

H COMP � V COMP e(s)(s) �

� G m R T � 1 s � 1
###### � 1 � P s [2] � [�] � P � � 1P [�] s � 1

The explanation of the parameters stated in the equation
above follows:

R � R
R P OUT
T � R R
P � OUT
� 1 � R 1 C 1

� P � R T C P � 1P � [�] R 1 � R T [�] C 1

This transfer function model can be used for closed loop
stability calculations.


OTA


**Figure 15. Voltage Divider and Compensation Network**

**[www.onsemi.com](http://www.onsemi.com/)**

**18**


-----

##### **NCV78703**


**Booster PWM Skip Cycles**
In case of light booster load, it may be useful to reduce the
number of effective PWM cycles in order to get a decrease
of the input current inrush bursts and a less oscillating boost
voltage. This can be obtained by using the “skip cycles”
feature, programmable by SPI via BOOST_SKCL[1:0] (see
Table 12 and SPI map). BOOST_SKCL[1:0] = ‘00’ means
skip cycle disabled.
The selection defines the VCOMP voltage threshold
below which the PWM is stopped, thus avoiding V BOOST
oscillations in a larger voltage window.

**Booster Multiphase Mode Principles**
The NCV78703 device supports three booster phases,
which are connected together to the same VBOOST node,
sharing the boost capacitor block. Multiphase mode shows
to be a cost effective solution in case of mid to high power
systems, where bigger external BOM components would be
required to bear the total power in one phase only with the
same performances and total board size. In particular, the
boost inductor could become a critical item for very high
power levels, to guarantee the required minimum saturation
current and RMS heating current.
Another advantage is the benefit from EMC point of view,
due to the reduction in ripple current per phase and ripple
voltage on the module input capacitor and boost capacitor.
The picture below shows the (very) ideal case of 50% duty
cycle, the ripple of the total module current (I Lmp_sum =
I L1mp + I L2mp ) is reduced to zero. The equivalent single
phase current (I Lsp ) is provided as a graphical comparison.

**I** **Lsp**

**I** **Lmp_sum**

**I** **L1mp** **I** **L2mp**

**t**

**Figure 16. Booster Single Phase vs. Multiphase**
**Example**

**Booster Multichip Connection Diagram and**
**Programming**
For high−power systems more NCV78702 and
NCV78703 devices can be combined to gain even more
synchronized booster phases.


This section describes the steps both from hardware and
SPI programming point of view to operate in multichip
mode. Example of physical connection of two devices is
provided in this section. From a hardware point of view, it
is assumed that in multiphase mode (N boosters), each stage
has the same external components. The following features
have to be considered as well:

1. The compensation pin (COMP) of all boosters is
connected together to the same compensation
network, to equalize the power distribution of each
booster (booster phases work with the equal peak
current). For the best noise rejection, the
compensation network area has to be surrounded
by the GND plane.
2. Boosters are synchronized by using shared
external clock, generated by MCU or external
logic, according to the user−defined control
strategy. The generic number of lines needed is
equivalent to the number of devices. When two
chips are combined, the slave device shall have
BOOST_SRCINV bit at ‘1’ (clock polarity
internal inversion active), whereas the master
device will keep the BOOST_SRCINV bit at ‘0’
(= no inversion, default).
3. Only the master device’s error amplifier OTA must
be active, while the other (slave) devices must
have all their own OTA blocks disabled
(BOOST_OTA_GAIN[1:0] = ‘00’). Master device
should have the register
BOOST_MULTI_PHASE_MD[1:0] set to ‘01’
(Multiphase Mode − MASTER), this will ensure
that Error Amplifier of this device drives COMP
signal which is shared between all devices. Other
(slave) devices should have
BOOST_MULTI_PHASE_MD[1:0] set to ‘10’
(Multiphase Mode − SLAVE), meaning that
COMP pin is used only to sense the voltage.
4. Overvoltage settings of master and slave devices
should be set to the same level. Each device senses

boost voltage via VBOOSTDIV pin and reacts to the
overvoltage situation independently. See also
“Booster overvoltage shutdown protection” for more
details on the protection mechanism and threshold.


**[www.onsemi.com](http://www.onsemi.com/)**

**19**


-----

##### **NCV78703**


V_Batt

(after rev. pol. prot.)

C_BC2


C_BST_IN


C_BC1 R_BC1

V C C of MCU

R_SDO


Vboost


C_BB

C_DRIVE


C_DD


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


|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||


**Figure 17. Booster Multichip Connection Example**

**[www.onsemi.com](http://www.onsemi.com/)**

**20**


-----

##### **NCV78703**


**Booster Enable and Disable Control**

By means of FSO_ENABLE_SEL SPI registers, function
of FSO/ENABLE2 pin can be selected.
When FSO_ENABLE_SEL = ‘0’, FSO function is
enabled (FSO mode can be entered by falling edge on this
pin). In this case each phase of the booster can be
enabled/disabled by corresponding BOOSTx_EN bit. The
enable signal is the transition from ‘0’ to ‘1’, the disable
function is vice−versa.

When FSO_ENABLE_SEL = ‘1’, ENABLE function is
enabled (independent control of booster phases). When the
independent control of the phases is chosen, a booster x is
activated only when SPI bit BOOSTx_EN is ‘1’ and
corresponding debounced ENABLEx pin is in logic ‘1’.
When BOOSTx_EN = ‘0’, the corresponding channel is
off and its GATE drive is disabled. Please note that even

when all phases are off, the error amplifier is not shut off
automatically and to avoid voltage generation on the
VCOMP pin the G m gain must be put to zero as well.

**Power Distribution**

Current peak regulation level I PEAK in current regulation
loop can be modified by changing of division ratio of the
internal voltage divider in range from 4 to 20 (see COMP_DIV

**Table 19. POWER DISTRIBUTION**


parameter in Table 12 and Table 19) for each phase
individually by SPI registers P_DISTRIBUTIONx[4:0].
The same internal divider is also in path of slope
compensation, internal slope has to be translated into
corresponding slope on sensing resistor R SENSE according
to Table 13 and Table 19.

Power distribution feature allows setting of the ratio
between peak values of the currents in the individual booster
channels. This can serve to:
##### • balance power sharing between booster phases which

can differ because of external components tolerances
and device specification; • set different power levels to the individual phases

without changing external components (R SENSE ).
Because peak value of the current I PEAK is modified by
power distribution setting, the average current I AVERAGE
and corresponding power P have to be computed by the
following formulas when operated in continuous mode:

I AVERAGE = I PEAK – I RIPPLE /2, P = I AVERAGE - V BAT .
Individual intermediate values of COMP_DIV are
computed according to the following equation:

1
COMP_DIV �
1
20 [�] [15] [�] [P] [_] [DISTRIBUTION] 155 [[] [4:0] [](] [si] [g] [ned] [)]

|P_DISTRIBUTIONx[4:0] unsigned|Col2|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P_DISTRIBUTIONx[4:0] signed||-16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 4.00 4.11 4.22 4.34 4.46 4.59 4.73 4.88 5.04 5.21 5.39 5.59 5.79 6.02 6.26 6.53||||||||||||||||
|COMP_DIV_ratio||||||||||||||||||
||Internal slope [mV/us]|||||||||||||||||
|Slope_Comp_0 (mV/us @ Rsense)|0|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|
|Slope_Comp_1 (mV/us @ Rsense)|17|4.25|4.14|4.03|3.92|3.81|3.70|3.59|3.48|3.37|3.26|3.15|3.04|2.94|2.82|2.72|2.60|
|Slope_Comp_2 (mV/us @ Rsense)|35|8.75|8.52|8.29|8.06|7.85|7.63|7.40|7.17|6.94|6.72|6.49|6.26|6.04|5.81|5.59|5.36|
|Slope_Comp_3 (mV/us @ Rsense)|50|12.50|12.17|11.85|11.52|11.21|10.89|10.57|10.25|9.92|9.60|9.28|8.94|8.64|8.31|7.99|7.66|
|Slope_Comp_4 (mV/us @ Rsense)|85|21.25|20.68|20.14|19.59|19.06|18.52|17.97|17.42|16.87|16.31|15.77|15.21|14.68|14.12|13.58|13.02|
|Slope_Comp_5 (mV/us @ Rsense)|120|30.00|29.20|28.44|27.65|26.91|26.14|25.37|24.59|23.81|23.03|22.26|21.47|20.73|19.93|19.17|18.38|
|Slope_Comp_6 (mV/us @ Rsense)|190|47.50|46.23|45.02|43.78|42.60|41.39|40.17|38.93|37.70|36.47|35.25|33.99|32.82|31.56|30.35|29.10|
|Slope_Comp_7 (mV/us @ Rsense)|290|72.50|70.56|68.72|66.82|65.02|63.18|61.31|59.43|57.54|55.66|53.80|51.88|50.09|48.17|46.33|44.41|
|||||||||||||||||||
|P_DISTRIBUTIONx[4:0] unsigned||0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 6.81 7.13 7.47 7.85 8.27 8.73 9.25 9.84 10.51 11.27 12.16 13.19 14.42 15.90 17.71 20.00||2|3|4|5|6|7|8|9|10|11|12|13|14|15|
|P_DISTRIBUTIONx[4:0] signed||||||||||||||||||
|COMP_DIV_ratio||||||||||||||||||
||Internal slope [mV/us]|0.00 0.00 2.50 2.38 5.14 4.91 7.34 7.01 12.48 11.92 17.62 16.83 27.90 26.65 42.58 40.67||||||||||||||||
|Slope_Comp_0 (mV/us @ Rsense)|0|||0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.00|
|Slope_Comp_1 (mV/us @ Rsense)|17|||2.28|2.17|2.06|1.95|1.84|1.73|1.62|1.51|1.40|1.29|1.18|1.07|0.96|0.85|
|Slope_Comp_2 (mV/us @ Rsense)|35|||4.69|4.46|4.23|4.01|3.78|3.56|3.33|3.11|2.88|2.65|2.43|2.20|1.98|1.75|
|Slope_Comp_3 (mV/us @ Rsense)|50|||6.69|6.37|6.05|5.73|5.41|5.08|4.76|4.44|4.11|3.79|3.47|3.14|2.82|2.50|
|Slope_Comp_4 (mV/us @ Rsense)|85|||11.38|10.83|10.28|9.74|9.19|8.64|8.09|7.54|6.99|6.44|5.89|5.35|4.80|4.25|
|Slope_Comp_5 (mV/us @ Rsense)|120|||16.06|15.29|14.51|13.75|12.97|12.20|11.42|10.65|9.87|9.10|8.32|7.55|6.78|6.00|
|Slope_Comp_6 (mV/us @ Rsense)|190|||25.44|24.20|22.97|21.76|20.54|19.31|18.08|16.86|15.63|14.40|13.18|11.95|10.73|9.50|
|Slope_Comp_7 (mV/us @ Rsense)|290|||38.82|36.94|35.07|33.22|31.35|29.47|27.59|25.73|23.85|21.99|20.11|18.24|16.37|14.50|


**[www.onsemi.com](http://www.onsemi.com/)**

**21**


-----

##### **NCV78703**


**Diagnostics**
The NCV78703 features a wide range of embedded
diagnostic features. Their description follows.

**Diagnostic Description**
##### • Thermal Warning: this mechanism detects a junction

temperature which is in principle close, but lower, to
the chip maximum allowed, thus providing the
information that some action (power de−rating) is
required to prevent overheating that would cause
Thermal Shutdown. The thermal warning flag (TW) is
given in status register 0x0A and is latched. Thermal
warning threshold is typically 160°C (see Table 6). • Thermal Shutdown: this safety mechanism intends to

protect the device from damage caused by overheating,
by disabling the booster channels. The diagnostic is
displayed per means of the TSD bit in status register
0x0A (latched). Once occurred, the thermal shutdown
condition is exited when the temperature drops below
the thermal warning level, thus providing hysteresis for
thermal shutdown recovery process. Booster channels
are re−enabled automatically if
TSD_AUT_RCVR_EN = 1, respectively can be
re−enabled by rising edge on BOOSTx_EN if
TSD_AUT_RCVR_EN = 0. The application thermal
design should be made as such to avoid the thermal
shutdown in the worst case conditions. The thermal

shutdown level is not user programmable and is factory
trimmed to typically 170°C (see Table 6). • Temperature output: allows to observe temperature of

the chip by the means of the adjustable threshold
ADC_TEMP_THR[2:0] (see Table 6). When
temperature exceeds the threshold, status flag
TEMP_OUT is set. • SPI Error: in case of SPI communication errors the

SPIERR bit in status register 0x0A is set. The bit is
latched. For more details, please refer to section “SPI
protocol: framing and parity error”. • HW reset: the out of reset condition is reported

through the HWR bit (latched). This bit is set only at
each Power On Reset (POR) and indicates the device is
ready to operate. • Booster Overvoltage Shutdown: Whenever the boost

overvoltage detection triggers in the control loop, the


BOOST_OV flag (latched, register 0x0A) is set and
booster is switched off. The booster is automatically
activated when voltage falls below the hysteresis
defined by Booster overvoltage re−activation parameter
in Table 12.
##### • Booster Undervoltage Protection: when voltage at

booster divider pin VBOOSTDIV drops below
BST_EA_UV level (see Table 12) because of external
divider failure, the VBSTDIV_UV flag (latched, 0x0B)
is displayed and booster is switched off to protect
external components from the overvoltage. • VDRIVE Out of Regulation: correct work of

VDRIVE regulator is monitored by checking
VBB – VDRIVE voltage difference which has to be at
least 0.5 V and by checking current drawn from the
regulator. If one or both conditions are not met,
VDRIVE_NOK flag is displayed (latched, 0x0B). • VDRIVE Undervoltage Lockout: this safety

mechanism monitors sufficient voltage for MOSFETs
and protects them by switching off the booster when
VDRIVE voltage is too low. During initial 150 �s after
POR the detection is disabled to ensure that normal

operating mode is entered. Detection level is set by
VDRIVE_UV_THR[2:0] register relatively to used
VDRIVE voltage (set by VDRIVE_VSETPOINT[3:0]
register). Detection thresholds are summarized in
Table 7. When VDRIVE_UV_THR[2:0] = 0, function
is disabled. • Booster status: the physical activation of the booster

phase is displayed by the BOOSTx_STATUS flag
(non−latched, 0x0A). Please note this is different from
the BOOSTx_EN control bit, which reports instead the
*willing* to activate the booster. See also section ”Booster
Enable Control”. • Enable pin status: the actual logic status read at

ENABLEx pin is reported by the flag
ENABLEx_STATUS (non−latched, 0x0B). Thanks to
this diagnostic, the MCU can check proper logic level
on the pin.

A short summary table of the main diagnostic bits related to
the LED outputs follows.


**[www.onsemi.com](http://www.onsemi.com/)**

**22**


-----

**Table 20. DIAGNOSTIC SUMMARY**

|Diagnose|Col2|Detection level|Booster Output|Latched|
|---|---|---|---|---|
|Flag|Description||||
|TW|Thermal Warning|Factory trimmed|No change|Yes|
|TSD|Thermal Shutdown|Factory trimmed|Disabled. Re−enabled by rising edge on BOOSTx_EN after Tj < TW and TSD flag was cleared. Re−enabled automatically when TSD_AUT_RCVR_EN bit is set (in FSO/SA modes always).|Yes|
|TEMP_OUT|Temperature Output|See Diagnostic section|No change|Yes|
|SPIERR|SPI error|See SPI section|No change|Yes|
|BOOST_OV|Overvoltage Shutdown|See Electrical Characteristics|Disabled. Re−enabled automatically below BOOST_RA threshold.|Yes|
|VBSTDIV_UV|Undervoltage Protection|See Electrical Characteristics|Disabled. Re−enabled by rising edge on BOOSTx_EN when VBOOSTDIV > BST_EA_UV|Yes|
|VDRIVE_NOK|VDRIVE Out of regulation|See Electrical Characteristics|No change|Yes|
|VDRIVE_UV *|VDRIVE UV Lockout|See Diagnostic section. Depends on SPI VDRIVE_VSETPOINT[3:0] and VDRIVE_UV_THR[2:0] settings.|Disabled. Re−enabled by rising edge on BOOSTx_EN after VDRIVE_UV condition disappears.|Yes|
|HWR|HW Reset|Set after POR|No change|Yes|



*The flag not available in SPI map

**Table 21. TSD RECOVERY OVERVIEW**

|FSO_ENABLE_SEL SPI bit|TSD_AUT_RCVR_EN SPI bit|ENABLEx pin|BOOSTx_EN SPI bit|BOOSTERx status after TSD disappear|
|---|---|---|---|---|
|0|0|x|0|Disabled|
|0|0|x|1|Disabled|
|0|0|x|0 1 →|Enabled|
|0|1|x|0|Disabled|
|0|1|x|1|Enabled|
|1|0|0|0|Disabled|
|1|0|0|1|Disabled|
|1|0|1|0|Disabled|
|1|0|1|1|Disabled|
|1|0|0 1 →|1|Disabled|
|1|0|1|0 1 →|Enabled|
|1|1|0|0|Disabled|
|1|1|0|1|Disabled|
|1|1|1|0|Disabled|
|1|1|1|1|Enabled|



NOTE: 0 → 1 … rising edge (after TW disappeared)

##### **NCV78703**

**[www.onsemi.com](http://www.onsemi.com/)**

**23**


-----

##### **NCV78703**


**Functional Mode Description**

**Reset**

POR always causes asynchronous reset − transition to
reset state. The Power−On−Reset circuit (POR) monitors the
VDD and VBB voltages to control the out−of−reset
condition at power−up. Chip will leave the reset state and
VDD regulator will be enabled when VBB > POR_VBB_H
and VDD > POR3V_H and at least one ENABLE input is in
logic ‘1’.
When SPI register VDD_ENA is set to ‘1’, VDD regulator
stays enabled and chip stays in normal mode, even if all
ENABLE inputs are set to logic ‘0’. When SPI register
VDD_ENA is set to ‘0’ and all ENABLE inputs are set to
logic ‘0’, chip enters the reset state and VDD regulator is
switched off, current consumption from VBB is less than
1 μA (for T J = 30°C).

**Init and Normal mode**

Normal mode is entered through Init state after internal
delay of 150 μs. In Init state, OTP refresh is performed. If
OTP bits for FSO_MD[2:0] register and *OTP Lock Bit* are
programmed, transition to FSO/SA mode is possible.
Device is fully started 500 μs after rising edge on
ENABLE pin.

**FSO/Stand−Alone mode**
FSO (Fail−Safe Operation)/Stand−Alone modes can be
used for two main purposes:
##### • Default power−up operation of the chip ( Stand−Alone

functionality without external microcontroller or
preloading of the registers with default content for
default operation before microcontroller starts sending
SPI commands for chip settings) • Fail−Safe functionality (chip functionality definition in

fail−safe mode when the external microcontroller

functionality is not guaranteed)

FSO/stand−alone function is controlled according to
Table 24. Entrance into FSO/Stand−alone mode is possible
only after costumer OTP zapping when *OTP Lock Bit* is set.
FSO/ENABLE2 pin serves to enter/exit FSO mode when
SPI bit FSO_ENABLE_SEL = “0” (meaning that function
of the pin is “FSO”). If FSO_ENABLE_SEL = “1”, FSO
mode cannot be entered. Independent control of booster
phases (FSO_ENABLE_SEL = ‘1’) is not available in FSO
mode. When FSO_ENABLE_SEL is changed in FSO mode
from ‘0’ to ‘1’, the FSO mode is immediately exited.
Actual value of SPI register FSO_MD[2:0] (preloaded
from OTP only at power−up) is used for entrance into FSO
mode and all FSO related functions are then controlled

according to it.
When FSO mode is entered, SPI status bit FSO is set. It is
clear by read flag.


When FSO/Stand−Alone mode is activated, content of the
following SPI registers is preloaded from OTP memory:

BOOST_SKCL[1:0]

BOOST_OTA_GAIN[1:0]

VDRIVE_VSETPOINT[3:0]

VBOOST_VGATE_THR

BOOST_VLIMTH1[1:0]

BOOST_VLIMTH2[1:0]

BOOST_OV_REACT[1:0]

BOOST_SLPCTRL[2:0]

BOOST_OVERVOLTSD_THR[6:0]

BOOST_SRCINV

BOOST_MULTI_PHASE_MD[1:0]

BOOST_VSETPOINT[6:0]

FSO_BST_FREQ[2:0]

BOOST1_EN

BOOST2_EN

VDD_ENA

FSO_ENABLE_SEL

VBOOST_TOFF_SET[2:0]

VBOOST_TON_SET[2:0]

P_DISTRIBUTION1[4:0]

P_DISTRIBUTION2[4:0]

VDRIVE _ UV _ THR [ 2:0 ]

In FSO (entered via falling edge on FSO/ENABLE2 pin)
or Stand−Alone modes, internal booster PWM source with
50% duty cycle is used as booster frequency. Frequency at
which booster runs is determined by value in
FSO_BST_FREQ[2:0] register. Values which can be
selected are shown in the following table.

**Table 22. BOOSTER FREQUENCY IN FSO MODES**

TSD_AUT_RCVR_EN is kept high ‘1’ in FSO or

|FSO_BST_FREQ[2:0]|Booster freq. [kHz]|
|---|---|
|0x0|200|
|0x1|294.1|
|0x2|416.7|
|0x3|500|
|0x4|625|
|0x5|714.3|
|0x6|833|
|0x7|1000|

Stand−Alone modes, allowing automatic recovery when
thermal shutdown occurs. TSD_AUT_RCVR_EN is loaded
from OTP only when FSO_MD[2:0] = 1.
BOOSTx_EN bits are kept high ‘1’ in FSO modes
(entered via falling edge on FSO pin), enabling booster
phases. If BOOSTx_EN values preloaded from OTP’s are
and remain ‘0’, corresponding booster phases will be
disabled when FSO mode is exited.


**[www.onsemi.com](http://www.onsemi.com/)**

**24**


-----

**Table 23. FSO MODES OVERVIEW**

|FSO_MD[2:0]|FSO entered after startup|FSO entered after falling edge on FSO pin|SPI ctrl. regis- ters loaded with “00” after POR|SPI ctrl. registers loaded with values from cus- tomer OTPs after POR|SPI registers update in FSO enabled|OTP programming needed|
|---|---|---|---|---|---|---|
|0|N|N|Y|N|N|N|
|1|N|N|N|Y|N|Y|
|2|N|Y|Y|N|N|Y|
|3|N|Y|Y|N|Y|Y|
|4|N|Y|N|Y|N|Y|
|5|N|Y|N|Y|Y|Y|
|6|Y|N|N|Y|N|Y|
|7|Y|Y*|N|Y|Y|Y|



*after proper FSO_MD[2:0] register update

**Table 24. FSO MODES DESCRIPTION**

##### **NCV78703**

**[www.onsemi.com](http://www.onsemi.com/)**

**25**

|FSO_MD[2:0]|Description|
|---|---|
|000 = 0 b|FSO mode disabled, registers are loaded with safe value = 0x00h after POR, default After the reset, control registers are loaded with 0x00h value. • Entrance into FSO mode is not possible •|
|001 = 1 b|FSO mode disabled, registers are loaded with data from OTP memory after POR After the reset, control registers are loaded with data stored in OTP memory (device’s OTP memory has to be pro- g•rammed, OTP Lock Bit has to be set). It reduces number of SPI transfers needed to configure the device after the reset. Entrance into FSO mode is not possible •|
|010 = 2 b|FSO entered after falling edge on FSO pin, registers are loaded with safe value = 0x00h after POR After FSO mode activation, control registers are loaded with data stored in OTP memory. • SPI register update (SPI write/read operation) in FSO mode is disabled (SPI write operation is blocked; • clearing of SPI registers is blocked; SPIERR flag is set in case of invalid SPI frame). FSO/ENABLE2 pin serves to enter/exit FSO mode (when SPI bit FSO_ENABLE_SEL = 0). • Internal booster PWM source will be selected as the booster frequency after activation of FSO mode. •|
|011 = 3 b|FSO entered after falling edge on FSO pin, registers are loaded with safe value = 0x00h after POR After FSO mode activation, control registers are loaded with data stored in OTP memory. • SPI register update (SPI write/read operation) in FSO mode is enabled • FSO mode can be exited by writing FSO_MD[2:0] = 000 or 001 • FSO/ENABLE2 pin serves to enter/exit FSO mode (when SPI bit FSO_ENABLE_SEL = 0). • If SPI bit FSO_ENABLE_SEL is written with ‘1’ in FSO mode, the FSO mode is immediately exited. • Internal booster PWM source will be selected as the booster frequency after activation of FSO mode. •|
|100 = 4 b|FSO entered after falling edge on FSO pin, registers are loaded with data from OTP memory after POR After FSO mode activation, control registers are loaded with data stored in OTP memory. • SPI register update (SPI write/read operation) in FSO mode is disabled (SPI write operation is blocked; • clearing of SPI registers is blocked; SPIERR flag is set in case of invalid SPI frame). FSO/ENABLE2 pin serves to enter/exit FSO mode (when SPI bit FSO_ENABLE_SEL = 0). • Internal booster PWM source will be selected as the booster frequency after activation of FSO mode. •|
|101 = 5 b|FSO entered after falling edge on FSO pin, registers are loaded with data from OTP memory after POR After FSO mode activation, control registers are loaded with data stored in OTP memory. • SPI register update (SPI write/read operation) in FSO mode is enabled • FSO mode can be exited by writing FSO_MD[2:0] = 000 or 001 • FSO/ENABLE2 pin serves to enter/exit FSO mode (when SPI bit FSO_ENABLE_SEL = 0). • If SPI bit FSO_ENABLE_SEL is written with ‘1’ in FSO mode, the FSO mode is immediately exited. • Internal booster PWM source will be selected as the booster frequency after activation of FSO mode. •|
|110 = 6 b|SA (stand−alone)/FSO entered after POR, registers are loaded with data from OTP memory After SA/FSO mode activation, control registers are loaded with data from OTP memory • SPI register update (SPI write/read operation) in SA/FSO mode is disabled (SPI write operation is blocked; • clearing of SPI registers is blocked; SPIERR flag is set in case of invalid SPI frame). Internal booster PWM source will be selected as the booster frequency. •|
|111 = 7 b|SA (stand−alone)/FSO entered after POR, registers are loaded with data from OTP memory After SA/FSO mode activation, control registers are loaded with data from OTP memory • SPI register update (SPI write/read operation) in SA/FSO mode is enabled • FSO mode can be exited by writing FSO_MD[2:0] = 000 or 001 • If SPI bit FSO_ENABLE_SEL is written with ‘1’ in FSO mode, the FSO mode is immediately exited. • Internal booster PWM source will be selected as the booster frequency. •|


-----

##### **NCV78703**


**SPI Interface**

**General**
The serial peripheral interface (SPI) is used to allow
an external microcontroller (MCU) to communicate
with the device. NCV78703 acts always as a slave and it
cannot initiate any transmission. The operation of the device
is configured and controlled by means of SPI registers,
which are observable for read and/or write from the master.

The NCV78703 SPI transfer size is 16 bits.

During an SPI transfer, the data is simultaneously
transmitted (shifted out serially) and received (shifted in
serially). A serial clock line (SCLK) synchronizes shifting
and sampling of the information on the two serial data lines:
SDO and SDI. The SDO signal is the output from the Slave
(NCV78703), and the SDI signal is the output from the
Master.


A slave or chip select line (CSB) allows individual
selection of a slave SPI device in a time multiplexed
multiple−slave system.
The CSB line is active low. If an NCV78703 is not

selected, SDO is in high impedance state and it does not
interfere with SPI bus activities. Since the NCV78703

always clocks data out on the falling edge and samples data
in on rising edge of clock, the MCU SPI port must be
configured to match this operation.
The implemented SPI allows connection to multiple
slaves by means of star connection (CSB per slave) or by
means of daisy chain.
An SPI star connection requires a bus = (3 + N) total lines,
where N is the number of Slaves used, the SPI frame length
is 16 bits per communication.


**Figure 18. SPI Star vs. Daisy Chain Connection**


**SPI Daisy chain mode**
SPI daisy chain connection bus width is always four lines
independently on the number of slaves. However, the SPI
transfer frame length will be a multiple of the base frame
length so N x 16 bits per communication: the data will be
interpreted and read in by the devices at the moment the CSB
rises.

A diagram showing the data transfer between devices in
daisy chain connection is given further: CMDx represents
the 16−bit command frame on the data input line transmitted
by the Master, shifting via the chips’ shift registers through
the daisy chain. The chips interpret the command once the
chip select line rises.


**Figure 19. SPI Daisy Chain Data Shift Between**
**Slaves. The symbol ‘x’ represents the previous**
**content of the SPI shift register buffer.**


**[www.onsemi.com](http://www.onsemi.com/)**

**26**


-----

##### **NCV78703**


The NCV78703 default power up communication mode
is “star”. In order to enable daisy chain mode, a multiple of
16 bits clock cycles must be sent to the devices, while the
SDI line is left to zero.

Note: to come back to star mode the NOP register (address
0x0000) must be written with all ones, with the proper data
parity bit and parity framing bit: see SPI protocol for details
about parity and write operation.

**SPI Transfer Format**
Two types of SPI commands (to SDI pin of NCV78703)
from the micro controller can be distinguished: “Write to a
control register” and “Read from register (control or
status)”.

The frame protocol for the *write operation* :

|High Write; CMD = ‘1’|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Low C SDI MAAAA PDDDDDDDDDD 3 2 1 0 9 8 7 6 5 4 3 2 1 0 D Low S C P AAAADDDDDDDDDD DO EI M 3 2 1 0 9 8 7 6 5 4 3 2 1 0 R R D HIG||||||||||||||||||
||C M D|A 3|A 2|A 1|A 0|P|D 9|D 8|D 7|D 6|D 5|D 4|D 3|D 2|D 1|D 0||
|DO|S P I E R R|C M D|A 3|A 2|A 1|A 0|D 9|D 8|D 7|D 6|D 5|D 4|D 3|D 2|D 1|D 0||
|CLK|S P I E R R|C M D|A 4|A 3|A 2|A 1|A 0|P0P|1|VTV S VB D UI|O T P F A I L|F S O|T E M P O U T|B O O S T O V|T S D|T W|Low|
|||||||||||||||||||



P = not(CMD xor A3 xor A2 xor A1 xor A0 xor D9 xor D8 xor D7 xor
D6 xor D5 xor D4 xor D3 xor D2 xor D1 xor D0)

**Figure 20. SPI Write Frame**

Referring to the previous picture, the write frame coming
from the master (into the SDI) is composed from the
following fields:
##### • Bit[15] (MSB): CMD bit = 1 for write operation, • Bits[14:11]: 4 bits WRITE ADDRESS field, • Bit[10]: frame parity bit. It is ODD parity formed by

the negated XOR of all other bits in the frame, • Bits[9:0]: 10 bit DATA to write

Device in the same time replies to the master (on the SDO): • If the previous command was a write and no SPI error

had occurred, a copy of the command, address and data
written fields, • If the previous command was a read, the response

frame summarizes the address used and an overall


diagnostic check (copy of the main detected errors, see
Figure 20 and Figure 21 for details),
##### • In case of previous SPI error or after power−on−reset,

only the MSB bit will be 1, followed by zeros.

If parity bit in the frame is wrong, device will not perform
command and <SPI> flag will be set.
The frame protocol for the *read operation* :

**Read; CMD =** **‘** **0** **’**

H igh

Low ***BOOSTFAIL = BOOSTOV or VBSTDIVUV***

***−>*** ***immediate value of STATUS BITS;***

***Dedicated SPI READ Command of the***

|C M D|A 4|A 3|A 2|A 1|A 0|P|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|S P I E R R|T E M P O U T|OOB S ATF LI|T S D|T W|F S O|D 9|D 8|D 7|D 6|D 5|D 4|D 3|D 2|D 1|D 0|



SCLK Low

P = not(CMD xor A4 xor A3 xor A2 xor A1 xor A0)

**Figure 21. SPI Read Frame**

Referring to the previous picture, the read frame coming
from the master (into the SDI) is composed from the
following fields: • Bit[15] (MSB): CMD bit = 0 for read operation, • Bits[14:10]: 5 bits READ ADDRESS field, • Bit[10]: frame parity bit. It is ODD parity formed by

the negated XOR of all other bits in the frame, • Bits [8:0]: 9 bits zeroes field.

Device in the same frame provides to the master (on the
SDO) data from the required address (in frame response),
thus achieving the lowest communication latency.

**SPI Framing and Parity Error**
SPI communication framing error is detected by the
NCV78703 in the following situations: • Not an integer multiple of 16 CLK pulses are received

during the active−low CSB signal; • LSB bits (8..0) of a read command are not all zero; • SPI parity errors, either on write or read operation.

Once an SPI error occurs, the <SPI> flag can be reset only
by reading the status register in which it is contained (using
in the read frame the right communication parity bit).


**[www.onsemi.com](http://www.onsemi.com/)**

**27**


-----

##### **NCV78703**

**Table 25. NCV78703 SPI ADDRESS MAP**

**Table 26. BIT DEFINITION**

**REGISTER 0x00 (CR): NOP Register, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x01 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x02 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x03 (CR): Booster Settings, Reset Value (POR) = 0001111111** **2**

**REGISTER 0x04 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x05 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**[www.onsemi.com](http://www.onsemi.com/)**

**28**

|ADDR|R/W|bit9|bit8|bit7|bit6|bit5|bit4|bit3|bit2|bit1|bit0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0x00|NA|NOP register (read/write operation ignored)||||||||||
|0x01|R/W|BOOST_ DIV3/DIV2|VBOOST_VGATE_ THR|VDRIVE_VSETPOINT[3:0]||||BOOST_OTA_GAIN[1:0]||BOOST_SKCL[1:0]||
|0x02|R/W|0x0|BOOST_SLPCTRL[2:0]|||BOOST_VLIMTH3[1:0]||BOOST_VLIMTH2[1:0]||BOOST_VLIMTH1[1:0]||
|0x03|R/W|BOOST_MULTI_PHASE_MD[1:0]||BOOST_SRCINV|BOOST_OVERVOLTSD_THR[6:0]|||||||
|0x04|R/W|FSO_BST_FREQ[2:0]|||BOOST_VSETPOINT[6:0]|||||||
|0x05|R/W|TSD_AUT_ RCVR_EN|ADC_TEMP_THR[2:0]|||FSO_MD[2:0]|||BOOST3_EN|BOOST2_EN|BOOST1_EN|
|0x06|R/W|BOOST_OV_REACT[1:0]||VBOOST_TON_SET[2:0]|||VBOOST_TOFF_SET[2:0]|||FSO_ENABLE _SEL|VDD_ENA|
|0x07|R/W|P_DISTRIBUTION2[4:0]|||||P_DISTRIBUTION1[4:0]|||||
|0x08|R/W|0x0||VDRIVE_UV_THR[2:0]|||P_DISTRIBUTION3[4:0]|||||
|0x09|R/W|0x0|||OTP_BIAS_H|OTP_BIAS_L|OTP_ADDR[2:0]|||OTP_OPERATION[1:0]||
|0x0A|R|HWR|ODD PARITY|BOOST3_ STATUS|BOOST2_ STATUS|BOOST1_ STATUS|BOOST_OV|TEMP_OUT|SPIERR|TSD|TW|
|0x0B|R|0x0|ODD PARITY|ENABLE3_ STATUS|ENABLE2_ STATUS|ENABLE1_ STATUS|VDRIVE_NOK|VBSTDIV_UV|OTP_ACTIVE|OTP_FAIL|FSO|
|0x0C|R|OTP_DATA[9:0]||||||||||
|0x0D|R|0x0||REVID[7:0]||||||||
|OTHER|R|0x0||||||||||

|Symbol|MAP position|Description|
|---|---|---|

|NOP|Bits [9:0] – ADDR_0x00|NOP register (read/write operation ignored)|
|---|---|---|

|BOOST_DIV3/DIV2|Bit 9 – ADDR_0x01|Two or Three Phases Selection|
|---|---|---|
|VBOOST_VGATE_THR|Bit 8 – ADDR_0x01|Adjustment of Gate Threshold Voltage for Booster Transistor|
|VDRIVE_VSETPOINT[3:0]|Bits [7:4] – ADDR_0x01|VDRIVE Voltage|
|BOOST_OTA_GAIN[1:0]|Bits [3:2] – ADDR_0x01|Error Amplifier Gain|
|BOOST_SKCL[1:0]|Bits [1:0] – ADDR_0x01|Booster Skip Cycle Settings|

|BOOST_SLPCTRL[2:0]|Bits [8:6] – ADDR_0x02|Booster Slope Control|
|---|---|---|
|BOOST_VLIMTH3[1:0]|Bits [5:4] – ADDR_0x02|Booster phase Current Limitation|
|BOOST_VLIMTH2[1:0]|Bits [3:2] – ADDR_0x02|Booster phase Current Limitation|
|BOOST_VLIMTH1[1:0]|Bits [1:0] – ADDR_0x02|Booster phase Current Limitation|

|BOOST_MULTI_PHASE_MD[1:0]|Bits [9:8] – ADDR_0x03|Stand Alone /Master/Slave Selection|
|---|---|---|
|BOOST_SRCINV|Bit 7 – ADDR_0x03|Booster Clock Inversion|
|BOOST_OVERVOLTSD_THR[6:0]|Bits [6:0] – ADDR_0x03|Booster Overvoltage Threshold|

|FSO_BST_FREQ[2:0]|Bits [9:7] – ADDR_0x04|Booster Frequency|
|---|---|---|
|BOOST_VSETPOINT[6:0]|Bits [6:0] – ADDR_0x04|Booster Voltage Setpoint|

|TSD_AUT_RCVR_EN|Bit 9 – ADDR_0x05|Thermal Shutdown Automatic Recovery|
|---|---|---|
|ADC_TEMP_THR[2:0]|Bits [8:6] – ADDR_0x05|Temperature Output Threshold|


-----

##### **NCV78703**

**Table 26. BIT DEFINITION**

**REGISTER 0x05 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x06 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x07 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x08 (CR): Booster Settings, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x09 (CR): OTP Operations, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x0A (SR): Booster Status, Reset Value (POR) = 1x000xxxxx** **2**

**REGISTER 0x0B (SR): Booster Status, Reset Value (POR) = 0xxxxxx00x** **2**

**[www.onsemi.com](http://www.onsemi.com/)**

**29**

|Symbol|MAP position|Description|
|---|---|---|

|FSO_MD[2:0]|Bits [5:3] – ADDR_0x05|Fail Safe Operation Mode Selection|
|---|---|---|
|BOOST3_EN|Bit 2 – ADDR_0x05|Booster Phase 3 Enable|
|BOOST2_EN|Bit 1 – ADDR_0x05|Booster Phase 2 Enable|
|BOOST1_EN|Bit 0 – ADDR_0x05|Booster Phase 1 Enable|

|BOOST_OV_REACT[1:0]|Bits [9:8] – ADDR_0x06|Booster Overvoltage Reaction|
|---|---|---|
|VBOOST_TON_SET[2:0]|Bits [7:5] – ADDR_0x06|Booster Minimal TON|
|VBOOST_TOFF_SET[2:0]|Bits [4:2] – ADDR_0x06|Booster Minimal TOFF|
|FSO_ENABLE_SEL|Bit 1 – ADDR_0x06|Function of FSO/ENABLE2 Pin|
|VDD_ENA|Bit 0 – ADDR_0x06|VDD Active without Enable Pin|

|P_DISTRIBUTION2[4:0]|Bits [9:5] – ADDR_0x07|Power Distribution phase 2|
|---|---|---|
|P_DISTRIBUTION1[4:0]|Bits [4:0] – ADDR_0x07|Power Distribution phase 1|

|VDRIVE_UV_THR[2:0]|Bits [9:5] – ADDR_0x08|VDRIVE Undervoltage Threshold|
|---|---|---|
|P_DISTRIBUTION3[4:0]|Bits [4:0] – ADDR_0x08|Power Distribution phase 3|

|OTP_BIAS_H|Bit 6 – ADDR_0x09|OTP bias high|
|---|---|---|
|OTP_BIAS_L|Bit 5 – ADDR_0x09|OTP bias low|
|OTP_ADDR[2:0]|Bits [4:2] – ADDR_0x09|OTP Address|
|OTP_OPERATION[1:0]|Bits [1:0] – ADDR_0x09|OTP Operation|

|HWR|Bit 9 – ADDR_0x0A|Hardware Reset Flag|
|---|---|---|
|ODD PARITY|Bit 8 – ADDR_0x0A|Odd Parity over Data|
|BOOST3_STATUS|Bit 7 – ADDR_0x0A|Booster Phase 3 Status|
|BOOST2_STATUS|Bit 6 – ADDR_0x0A|Booster Phase 2 Status|
|BOOST1_STATUS|Bit 5 – ADDR_0x0A|Booster Phase 1 Status|
|BOOST_OV|Bit 4 – ADDR_0x0A|Booster Overvoltage Flag|
|TEMP_OUT|Bit 3 – ADDR_0x0A|Temperature Output|
|SPIERR|Bit 2 – ADDR_0x0A|SPI Error|
|TSD|Bit 1 – ADDR_0x0A|Thermal Shutdown|
|TW|Bit 0 – ADDR_0x0A|Thermal Warning|

|ODD PARITY|Bit 8 – ADDR_0x0B|Odd Parity over Data|
|---|---|---|
|ENABLE3_STATUS|Bit 7 – ADDR_0x0B|Enable Pin 3 Status|
|ENABLE2_STATUS|Bit 6 – ADDR_0x0B|Enable Pin 2 Status|
|ENABLE1_STATUS|Bit 5 – ADDR_0x0B|Enable Pin 1 Status|
|VDRIVE_NOK|Bit 4 – ADDR_0x0B|VDRIVE Voltage Not OK|
|VBSTDIV_UV|Bit 3 – ADDR_0x0B|VBOOST Divider Undervoltage Flag|
|OTP_ACTIVE|Bit 2 – ADDR_0x0B|OTP Active Flag|
|OTP_FAIL|Bit 1 – ADDR_0x0B|OTP Fail Flag|


-----

##### **NCV78703**

**Table 26. BIT DEFINITION**

**REGISTER 0x0B (SR): Booster Status, Reset Value (POR) = 0xxxxxx00x** **2**

**REGISTER 0x0C (SR): OTP Data, Reset Value (POR) = 0000000000** **2**

**REGISTER 0x0D (SR): Revision ID, Reset Value (POR) = 00xxxxxxxx** **2**

POR values of status registers are shown in situation that FSO mode is not entered after POR. All latched flags are “cleared

|Symbol|MAP position|Description|
|---|---|---|


|FSO|Bit 0 – ADDR_0x0B|Fail Safe Operation Mode Active Flag|
|---|---|---|


|OTP_DATA[9:0]|Bits [9:0] – ADDR_0x0C|OTP Data Register|
|---|---|---|


|REVID[7:0]|Bits [7:0] – ADDR_0x0D|Revision ID|
|---|---|---|

by read”. ‘x’ means that value after reset is defined during reset phase (diagnostics) or is trimmed during manufacturing process.
SPI register SPI_REVID[7:0] is used to track the silicon version, following encoding mechanism is used: • SPI_REVID[7] : 0 for NCV78703 • SPI_REVID[6:4] : Full Mask Version <0 to 7> • SPI_REVID[3:0] : Metal Tune <0 to 15>

REVID[7:0] for N78703−0 and N703−1 devices is 21hex (NCV78703 = 0, Full Mask Version = 2, Metal Tune = 1)

**[www.onsemi.com](http://www.onsemi.com/)**

**30**


-----

##### **NCV78703**


**OTP Memory**

**Description**
The OTP (Once Time Programmable) memory contains
75 bits which bear the most important application dependant
parameters and is user programmable via SPI interface. The
programming of these bits is typically done at the end of the
module manufacturing line.
OTP memory serves to store configuration data for
Fail−Safe or Stand−Alone functionality or default
configuration of the chip after power−up.
The OTP bits can be programmed only once, this is
ensured by dedicated *OTP Lock Bit* which is set during
programming.

**Table 27. OTP MAP**

The OTP bits addressed by SPI register OTP_ADDR[2:0]

|OTP bits|Connection to SPI register|
|---|---|
|OTP[1:0]|BOOST_SKCL[1:0]|
|OTP[3:2]|BOOST_OTA_GAN[1:0]|
|OTP[7:4]|VDRIVE_VSETPOINT[3:0]|
|OTP[8]|VBOOST_VGATE_THR|
|OTP[9]|SPARE = ‘0’|
|OTP[11:10]|BOOST_VLIMTH1[1:0]|
|OTP[13:12]|BOOST_VLIMTH2[1:0]|
|OTP[15:14]|SPARE[1:0]= ‘00’|
|OTP[17:16]|BOOST_OV_REACT[1:0]|
|OTP[20:18]|BOOST_SLPCTRL[2:0]|
|OTP[27:21]|BOOST_OVERVOLTSD_THR[6:0]|
|OTP[28]|BOOST_SRCINV|
|OTP[30:29]|BOOST_MULTI_PHASE_MD[1:0]|
|OTP[37:31]|BOOST_VSETPOINT[6:0]|
|OTP[40:38]|FSO_BST_FREQ[2:0]|
|OTP[41]|BOOST1_EN|
|OTP[42]|BOOST2_EN|
|OTP[43]|SPARE =’0’|
|OTP[46:44]|FSO_MD[2:0]|
|OTP[47]|TSD_AUT_RCVR_EN|
|OTP[48]|VDD_ENA|
|OTP[49]|FSO_ENABLE_SEL|
|OTP[52:50]|VBOOST_TOFF_SET[2:0]|
|OTP[55:53]|VBOOST_TON_SET[2:0]|
|OTP[60:56]|P_DISTRIBUTION1[4:0]|
|OTP[65:61]|P_DISTRIBUTION2[4:0]|
|OTP[70:66]|SPARE[4:0]=’00000’|
|OTP[73:71]|VDRIVE_UV[2:0]|
|OTP[74]|OTP Lock Bit|

are accessible (read only) in the SPI register
OTP_DATA[9:0] after OTP Refresh operation
(OTP_OPERATION[1:0] = 0x1) in the following way:


OTP_ADDR[2:0] = 0x0: OTP_DATA[9:0] = OTP[9:0]

OTP_ADDR[2:0] = 0x1: OTP_DATA[9:0] = OTP[19:10]

OTP_ADDR[2:0] = 0x2: OTP_DATA[9:0] = OTP[29:20]

OTP_ADDR[2:0] = 0x3: OTP_DATA[9:0] = OTP[39:30]

OTP_ADDR[2:0] = 0x4: OTP_DATA[9:0] = OTP[49:40]

OTP_ADDR[2:0] = 0x5: OTP_DATA[9:0] = OTP[59:50]

OTP_ADDR[2:0] = 0x6: OTP_DATA[9:0] = OTP[69:60]

OTP_ADDR[2:0] = 0x7: OTP_DATA[9:0] = {0000 &
OTP[74:70]}

**OTP Operations**
The NCV78703 supports following operations with OTP

memory:
##### • OTP_OPERATION[1:0] = 0x0 or 0x3:

**NOP** (no operation), • OTP_OPERATION[1:0] = 0x1:

**OTP Refresh** – refresh of the whole OTP memory
(75 bits). Data addressed by SPI register
OTP_ADDR[2:0] are available in SPI register
OTP_DATA[9:0] after the end of OTP Refresh
operation. Duration of OTP Refresh operation should
be 46 μs measured from CSB rising edge. • OTP_OPERATION[1:0] = 0x2:

**OTP Zap** – data from SPI register (those listed in
Table 27) and *OTP Lock Bit* are programmed into OTP
memory. OTP Zap operation is allowed to be
performed only once − when *OTP Lock Bit* is
unprogrammed. Duration of OTP Zap operation should
be 15 ms measured from CSB rising edge.

SPI status bit OTP_ACTIVE is set to “log. 1” when an OTP
operation is in progress.

**OTP Programming Procedure**
Following procedure should be applied to program OTP

memory: • VBB voltage has to be higher than 15.8 V with current

capability at least 50 mA. The user has to insure that
the right voltage is available in the application. Remark:
Lower VBB voltage does not prevent OTP zapping. • SPI registers listed in Table 27 have to be written with

required content. • Content of the SPI registers (those listed in Table 27) is

programmed into the OTP memory by
OTP_OPERATION[1:0] = 0x2 SPI write command.
*OTP Lock Bit* is programmed automatically at the same
time to prevent any further OTP programming.

**OTP Programming Verification**
OTP_FAIL bit in the SPI status register is set when VBB
under−voltage (VBB < VBB_OTP_L) is detected during
OTP Zap operation. It is clear by read flag.
The OTP_BIAS_H and OTP_BIAS_L registers are used
to check proper OTP programming. After OTP
programming, the OTP content has to be the same as


**[www.onsemi.com](http://www.onsemi.com/)**

**31**


-----

##### **NCV78703**


programmed when OTP is read with OTP_BIAS_H = 1 and
OTP_BIAS_L = 1.
Following procedure should be applied to verify OTP

content:
##### • VDD voltage has to be kept in range for normal mode

operation. • Write SPI registers OTP_BIAS_L = 1 and

OTP_BIAS_H = 0 • Write SPI register OTP_OPERATION[1:0] = 0x1 (OTP

Refresh) for all OTP_ADDR[2:0] values and check
corresponding OTP_DATA[9:0] content which has to
match with previously programmed data • Write SPI registers OTP_BIAS_L = 0 and

OTP_BIAS_H = 1

V_Batt

(after rev. pol. Prot.)

##### • Write SPI register OTP_OPERATION[1:0] = 0x1 (OTP

Refresh) for all OTP_ADDR[2:0] values and check
corresponding OTP_DATA[9:0] content which has to
match with previously programmed data • Programming is considered as successful when no

mismatch is observed and OTP_FAIL flag is not set.

**PCB Layout Recommendations**
This section contains instructions for the NCV78703 PCB

layout application design. Although this guide does not
claim to be exhaustive, these directions can help the
developer to reduce application noise impact and insuring
the best system operation. All important areas are
highlighted in the following picture:

Vboost


|Col1|Col2|Col3|Col4|
|---|---|---|---|
||R_SENSE1|||
|||||
|||||
||R_SENSE2|||


**Figure 22. NCV78703 Application Critical PCB Areas**

**PCB Layout: Booster Current Sensing – Area (A1, A2)** possible to each other, trying to have the same
The booster current sensing circuit used both by the loop length. The number of vias along the measurement
regulation and the current limitation mechanism, relies on a path should be minimized;
low voltage comparator, which triggers with respect to the 6. Place R_SENSE1/2 sufficiently close to the
sense voltage across the external resistors R_SENSE1/2. In MOSFET source terminal;
order to maximize power efficiency (=minimum losses on 7. The MOSFET’s dissipation area should be stretched
the sense resistor), the threshold voltage is rather low, with in a direction away from the sense resistor to
a maximum setting of 100 mV typical. This area may be minimize resistivity changes due to heating;
affected by the MOSFET switching noise if no specific care 8. If the current sense measurement tracks are
is taken. The following recommendations are given: interrupted by series resistors or jumpers (once as
5. Use a four terminals current sense method as a maximum) their value should be matched and
depicted in the figure below. The measurement low ohmic (pair of 0 � to 47 � max) to avoid
PCB tracks should run in parallel and as close as errors due to the comparator input bias currents.

**[www.onsemi.com](http://www.onsemi.com/)**

**32**


-----

##### **NCV78703**


However, in case of high application noise, a PCB
re−layout without RC filters is always
recommended.

9. Avoid using the board GND as one of the
measurement terminals as this would also

introduce errors.

**Figure 23. Four Wires Method for Booster Current**
**Sensing Circuit**

**PCB Layout: Booster Compensation Network – Area (B)**
The compensation network must be placed very close to
the chip to avoid noise capturing. Its ground has to be
connected directly to the chip ground pin to avoid noise
coming from other portions of the PCB ground. In addition
a ground ring shall provide extra shielding ground around.

**PCB Layout: VBOOST Resistor Divider – Area (C)**
The VBOOST resistor divider has to be connected
directly to the chip BOOST feedback (VBOOSTDIV) pin
and ground pin with separate PCB tracks to avoid coupling
of the ground shift on the PCB into the chip.

**PCB Layout: VGATE Signals – Area (D)**
It has to be ensured that VGATE signals do not interfere
with other signals like COMP or input of the IMAX or IREG
comparators.


**PCB Layout: VDD Connections – Area (E)**
The VDD decoupling capacitor has to be connected
directly to the VDD and ground pins with separate PCB
tracks to avoid coupling of the ground shift on the PCB into
the chip.
VDD connection from the NCV78703 to the NCV787x3

buck devices should be shielded with surrounding PCB
GND.

**PCB Layout: GND Connections – Area (F)**
The NCV78703 GND and GNDP pins must be connected
together. It is suggested to perform this connection directly
close to the device, behaving also as the cross−junction
between the signal GND (all low power related functions)
and the power GNDP (ground of VGATE driver). The
device exposed pad should be connected to the GND plane
for dissipation purposes.

**PCB Layout: Additional EMC Recommendations on**
**Loops**
It is suggested in general to have a good metal connection
to the ground and to keep it as continuous as possible, not
interrupted by resistors or jumpers.
In additions, PCB loops for power lines should be
minimized. A simplified application schematic is shown in
the next figure to better focus on the theoretical explanation.
When a DC voltage is applied to the VBB, at the left side of
the boost inductor L_BOOST, a DC voltage also appears on
the right side of L_BUCK and on the C_BUCK. However,
due to the switching operation (boost and buck), the applied
voltage generates AC currents flowing through the red area
(1). These currents also create time variable voltages in the
area marked in green (2). In order to minimize the radiation
due to the AC currents in area 1, the tracks’ length between
L_BOOST and the pair L_BUCK plus C_BUCK must be
kept low. At the contrary, if long tracks would be used, a
bigger parasitic capacitance in area 2 would be created, thus
increasing the coupled EMC noise level.


**Figure 24. PCB AC Current Lines (1) and AC Voltage Nodes (2)**

**[www.onsemi.com](http://www.onsemi.com/)**

**33**


-----

##### **NCV78703**

**Table 28. ORDERING INFORMATION**

|Device|Marking|Package*|Shipping†|
|---|---|---|---|
|NCV78703MW0AR2G|N78703−0|QFNW24 5 5 with Step−cut Wettable Flank × (Pb-Free)|5000 / Tape & Reel|
|NCV78703MW1AR2G|N703−1|QFNW24 4 4 with Step−cut Wettable Flank × (Pb-Free)|2500 / Tape & Reel|



*For additional information on our Pb−Free strategy
and soldering details, please download the
**onsemi** Soldering and Mounting
Techniques Reference Manual, SOLDERRM/D.

- or information on tape and reel specifications, including part orientation and tape sizes, please refer to our Tape and Reel Packaging
Specifications Brochure, BRD8011/D.

**[www.onsemi.com](http://www.onsemi.com/)**

**34**


-----

1 24

**SCALE 2:1**

**PIN ONE**
**LOCATION**

##### MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**

**QFNW24 4x4, 0.5P**
CASE 484AE

ISSUE A

DATE 07 AUG 2018



**L3**


**L3**


NOTES:
1. DIMENSIONING AND TOLERANCING PER
ASME Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DIMENSION b APPLIES TO PLATED
TERMINAL AND IS MEASURED BETWEEN
0.15 AND 0.30 MM FROM THE TERMINAL TIP.
4. COPLANARITY APPLIES TO THE EXPOSED
PAD AS WELL AS THE TERMINALS.

**GENERIC**

|DIM|MILLIMETERS|Col3|Col4|
|---|---|---|---|
||MIN|NOM|MAX|
|A|0.80|0.85|0.90|
|A1|−−−|−−−|0.05|
|A3|0.20 REF|||
|A4|0.10|−−−|−−−|
|b|0.20|0.25|0.30|
|D|3.90|4.00|4.10|
|D2|2.70|2.80|2.90|
|E|3.90|4.00|4.10|
|E2|2.70|2.80|2.90|
|e|0.50 BSC|||
|K|0.20|−−−|−−−|
|L|0.35|0.40|0.45|
|L3|0.00|0.05|0.10|


**MARKING DIAGRAM***

XXXXXX

XXXXXX

ALYW �

�

XXXXXX = Specific Device Code
A = Assembly Location
L = Wafer Lot

Y = Year

W = Work Week

� = Pb−Free Package

|A|Col2|Col3|
|---|---|---|
||||
||||



(Note: Microdot may be in either location)

*This information is generic. Please refer to
device data sheet for actual part marking.
Pb−Free indicator, “G” or microdot “ � ”, may
or may not be present. Some products may
not follow the Generic Marking.


**L**


**TOP VIEW**

|D ÉÉ ÉÉ ÉÉ|A B É É É E|
|---|---|



**NOTE 4** **SIDE VIEW** **A1**


**L**

**ALTERNATE**
**CONSTRUCTION**
**DETAIL A**

**EXPOSED**

**COPPER**

**PLATING**

**ALTERNATE**
**CONSTRUCTION**

**DETAIL B**

|A4|Col2|
|---|---|



**SURFACES**

**SECTION C−C**


|Col1|Col2|Col3|DETAIL B|Col5|
|---|---|---|---|---|
||0.10|C|||
|C|||||
||0.08|C|||


**C**


**DETAIL A**


**K**


**A1**
**A4**

**SEATING**
**PLANE**



**D2**

**24X** **L**

**13**

**E2**


**BOTTOM VIEW**

|4X b|Col2|Col3|Col4|
|---|---|---|---|
|0.10|C|A|B|
|0.05|C|NOT||



**RECOMMENDED**
**SOLDERING FOOTPRINT**

24X

2.90 0.71

2.90 4.72

24X

0.50 0.27

PITCH

|1|Col2|
|---|---|
|2.90||
|0.50||


DIMENSIONS: MILLIMETERS

|DOCUMENT NUMB|ER: 98AON17722G|Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped “CONTROLLED COPY” in red.|Col4|
|---|---|---|---|
|DESCRIPT|ION: QFNW24 4x4, 0.5P||PAGE 1 OF 1|


© Semiconductor Components Industries, LLC, 2018 www.onsemi.com


-----

1 24

**SCALE 2:1**

**PIN ONE**
**LOCATION**


**D**

**TOP VIEW**

**DETAIL B**

##### MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**

**QFNW24 5x5, 0.65P**
CASE 484AF

ISSUE A

DATE 07 AUG 2018


**L3**


NOTES:
1. DIMENSIONING AND TOLERANCING PER
ASME Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DIMENSION b APPLIES TO PLATED
TERMINAL AND IS MEASURED BETWEEN
0.15 AND 0.30 MM FROM THE TERMINAL TIP.
4. COPLANARITY APPLIES TO THE EXPOSED
PAD AS WELL AS THE TERMINALS.


**L**


**L3**

**L**

**ALTERNATE**
**CONSTRUCTION**
**DETAIL A**

**EXPOSED**

**COPPER**


**E**


|A|Col2|Col3|
|---|---|---|
||||
||||


~~0~~ . ~~08~~ C **CC** **A3** **A** **A4** **DETAIL B** **CONSTRUCTIONALTERNATE** **E2Ee** 4.903.40 0.65 BSC5.003.50 5.103.60

**NOTE 4** **SIDE VIEW** **A1** **C** **SEATINGPLANE** **K** 0.35 REF

|DIM|MILLIMETERS|Col3|Col4|
|---|---|---|---|
||MIN|NOM|MAX|
|A|0.80|0.85|0.90|
|A1|−−−|−−−|0.05|
|A3|0.20 REF|||
|A4|0.10|−−−|−−−|
|b|0.25|0.30|0.35|
|D|4.90|5.00|5.10|
|D2|3.40|3.50|3.60|
|E|4.90|5.00|5.10|
|E2|3.40|3.50|3.60|
|e|0.65 BSC|||
|K|0.35 REF|||
|L L3|0.30 0.40 0.50 0.05 REF|||



**D2** **GENERIC**

|10 M C|A|B|
|---|---|---|



~~0~~ . ~~10~~ ~~M~~ C ~~A~~ ~~B~~ **PLATED** **L3**

|A4|Col2|
|---|---|
|||
||L3|


**SURFACES**

**SECTION C−C**

XXXXXXXX

**E2** XXXXXXXX

**K** AWLYYWW �

�

|SEATING PLANE A A3 C E VIEW A1 A4 A1|Col2|Col3|Col4|
|---|---|---|---|
|0.10 M C A B D2 24X L 0.10 M C A B||||
||C|A|B|
|13||||



**24** **19**

**e/2** 0.10 M C A B XXXXXX = Specific Device Code

**BOTTOM VIEW** 0.05 M C **NOTE 3** A = Assembly Location

WL = Wafer Lot

|24X b|Col2|Col3|
|---|---|---|
|0.10 M|C|A|
|0.05 M|C||



**RECOMMENDED** YY = Year
**SOLDERING FOOTPRINT** WW = Work Week

5.30 � = Pb−Free Package

3.66 24X (Note: Microdot may be in either location)

0.62

*This information is generic. Please refer to

1 device data sheet for actual part marking.

Pb−Free indicator, “G” or microdot “ � ”,
may or may not be present. Some products
may not follow the Generic Marking.

|5.30 3.66 1|Col2|
|---|---|
|||
|||
|0.65||


PITCH


24X

0.40

DIMENSIONS: MILLIMETERS

|DOCUMENT NUM|BER: 98AON30093G|Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped “CONTROLLED COPY” in red.|Col4|
|---|---|---|---|
|DESCRIPT|ION: QFNW24 5x5, 0.65P||PAGE 1 OF 1|


© Semiconductor Components Industries, LLC, 2017 www.onsemi.com


-----

**onsemi**,, and other names, marks, and brands are registered and/or common law trademarks of Semiconductor Components Industries, LLC dba “ **onsemi** ” or its affiliates
and/or subsidiaries in the United States and/or other countries. **onsemi** owns the rights to a number of patents, trademarks, copyrights, trade secrets, and other intellectual property.
A listing of **onsemi** ’s product/patent coverage may be accessed at [www.onsemi.com/site/pdf/Patent](https://www.onsemi.com/site/pdf/Patent-Marking.pdf) − Marking.pdf . **onsemi** reserves the right to make changes at any time to any
products or information herein, without notice. The information herein is provided “as−is” and **onsemi** makes no warranty, representation or guarantee regarding the accuracy of the
information, product features, availability, functionality, or suitability of its products for any particular purpose, nor does **onsemi** assume any liability arising out of the application or use
of any product or circuit, and specifically disclaims any and all liability, including without limitation special, consequential or incidental damages. Buyer is responsible for its products
and applications using prov ~~ided~~ b ~~y~~ **onsem** ~~**i**~~ . ~~“~~ Ty **onsemi** ~~p~~ i ~~c~~ a ~~l”~~ p products, including compliance with all laws, regulations and safety requirements or standards, regardless of any support or applications information ~~ar~~ ameters ~~w~~ h ~~i~~ ch ~~m~~ ay be provid ~~e~~ d in **onsemi** data sheets and/or specifications can and do vary in different applications and actual performance may
vary over time. All operating parameters, including “Typicals” must be validated for each customer application by customer’s technical experts. **onsemi** does not convey any license
under any of its intellectual property rights nor the rights of others. **onsemi** products are not designed, intended, or authorized for use as a critical component in life support systems
or any FDA Class 3 medical devices or medical devices with a same or similar classification in a foreign jurisdiction or any devices intended for implantation in the human body. Should
Buyer purchase or use **onsemi** products for any such unintended or unauthorized application, Buyer shall indemnify and hold **onsemi** and its officers, employees, subsidiaries, affiliates,
and distributors harmless against all claims, costs, damages, and expenses, and reasonable attorney fees arising out of, directly or indirectly, any claim of personal injury or death
associated with such unintended or unauthorized use, even if such claim alleges that **onsemi** was negligent regarding the design or manufacture of the part. **onsemi** is an Equal
Opportunity/Affirmative Action Employer. This literature is subject to all applicable copyright laws and is not for resale in any manner.


**ADDITIONAL INFORMATION**

**TECHNICAL PUBLICATIONS** :
**Technical Library:** [www.onsemi.com/design/resources/technical](https://www.onsemi.com/design/resources/technical-documentation) − documentation
**onsemi Website:** [www.onsemi.com](https://www.onsemi.com/)




**ONLINE SUPPORT** : [www.onsemi.com/support](https://www.onsemi.com/support?utm_source=techdocs&utm_medium=pdf)
**For additional information, please contact your local Sales Representative at**
[www.onsemi.com/support/sales](https://www.onsemi.com/support/sales)


-----

