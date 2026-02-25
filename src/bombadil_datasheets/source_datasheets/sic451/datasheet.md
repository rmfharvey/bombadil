## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

## **4.5 V to 20 V Input, 15 A, 25 A, 40 A** **microBuck [®] DC/DC Converter With PMBus Interface**



**LINKS TO ADDITIONAL RESOURCES**



Design Tool Evaluation

Boards



Design Tools



**DESCRIPTION**

The SiC45x is a PMBus 1.3 compliant non-isolated DC/DC
buck regulator with integrated MOSFETs. It is capable of
supplying up to 40 A (SiC450) continuous output current. Its
output voltage is digitally adjustable from 0.3 V to 12 V from
a 4.5 V to 20 V input with switching frequencies up to
1.5 MHz.
SiC45x architecture delivers ultrafast transient response
with minimum output capacitance and tight regulation over
a broad load range. The device has integrated internal
compensation and is stable with any type of output
capacitor. The device incorporates a power saving scheme
that significantly increases light load efficiency.
The SiC45x allows power block configuration programs to
be stored in non volatile memory (NVM). Various operation
parameters can all be locally stored and used to determine
fault behavior. Operation is firmware based and is field
upgradable Pinstrap option is also available for default
configuration without PMBus.
The SiC45x is available in lead (Pb)-free power enhanced
MLP 5 mm x 7 mm package.


**TYPICAL APPLICATION CIRCUIT**



**FEATURES**

- Versatile

 - Single supply operation from 4.5 V to 20 V
input voltage

 - Scalable solution with continuous output
current of 40 A (SiC450), 25 A (SiC451), 15
A (SiC453)

- Continuous current of SiC451 by VOUT range 

 - 30 A at VOUT < 2.5 V 

 - 25 A at VOUT  2.5 V

 - Adjustable output voltage from 0.3 V to 12 V

 - Built in 5 V regulator for internal circuits and driver
supply

 - 1 % output voltage accuracy over temperature

 - 0.5 % output accuracy at VOUT = 3.3 V / 1.8 V, TA = 25 °C

 - Ultrafast transient response

- Highly efficient

 - 98 % peak efficiency

 - Optional power save mode

- Highly configurable

 - PMBus 1.3 compliant with 1 MHz bus speed

 - Internal NVM

 - VOUT adjustability and reading resolution of 2 mV

 - Supports over 50 PMBus commands

 - Supports in phase or 180° out of phase synchronization

 - Output voltage source and sink capability

- Robust and reliable

 - PVIN, VOUT, IIN and IOUT and temperature reporting

 - Over current protection in pulse-by-pulse mode

 - Output over and under voltage protection

 - Over temperature protection with hysteresis

 - Differential output remote sensing


**APPLICATIONS**

- Server, cloud, and infrastructure

- Networking, telecom, storage applications

- Distributed point of load power architectures

- DDR memory


Axis Title















10000


1000


100


10







**Fig. 1 - Typical Application Circuit**



|96<br>94<br>(%)<br>92<br>Efficiency<br>line<br>90<br>2nd<br>88<br>-<br>86 eff<br>84<br>82<br>80<br>0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)|||||||||
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)|||||||||
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)||||2.|5 Vo|3.3|Vo|5 Vo|
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)|||||||||
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)||||||VIN <br>~~F~~|= 12 V<br>~~ = 600~~|<br>~~  kHz~~|
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)||||||sw|||
|80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br><br>0<br>2nd line<br>eff - Efficiency (%)|||||||||
|powerictechsup|powerictechsup|powerictechsup|powerictechsup|powerictechsup|powerictechsup|powerictechsup|powerictechsup|powerictechsup|


THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**PIN CONFIGURATION**



PVIN 34


PGND 33


PGND 32


SW 31



10 NC
11 VSEN12 VSEN+

13 PGOOD
14 ADDR
15 VSET

16 AGND
17 RT / SYNC
18 SALRT



**Fig. 3 - Pin Configuration - Bottom View**

|PIN DESCRIPTION|Col2|Col3|
|---|---|---|
|**PIN NUMBER**|**SYMBOL**|**DESCRIPTION**|
|1, 2, 3, 34|PVIN|Input voltage for power stage|
|4|PHASE|Phase node, return path of high side gate driver|
|5|GH|High side MOSFET gate monitor|
|6|BOOT|Bootstrap voltage for high side gate driver (referenced to PH)|
|7, 16|AGND|Analog signal return ground|
|8|NC|Not used in Vishay device|
|9|NC|Not used in Vishay device|
|10|NC|Not used in Vishay device|
|11|VSEN-|Remote sense amplifier negative input connect to output ground|
|12|VSEN+|Remote sense amplifier positive input connect to output|
|13|PGOOD|Power good; open-drain output indicating VOUT is within set limits. Connect a pull up resistor typically<br>10 k to VDD|
|14|ADDR|PMBus address programming pin|
|15|VSET|Output voltage set point by connecting a resistor from VSET to AGND|
|17|RT/SYNC|Clock synchronization pin. Frequency can be set by connecting a resistor to AGND.<br>Pending on master / salve configuration, a clock can be send / receive via the pin|
|18|SALRT|PMBus alert. Connect to external host interface if desired|
|19|SDA|PMBus data. Connect to external host interface|
|20|SCL|PMBus clock. Connect to external host interface|
|21|EN|Enable pin. Active high 5 V logic level input|
|22|VDD|Internal 5 V circuits supply voltage. VDD is a LDO output, connect a 1 μF decoupling capacitor to AGND|
|23|VIN|Internal driver supply voltage|
|24|PVCC|Supply voltage for internal gate drive. PVCC is a LDO output. Connect a 4.7 μF decoupling capacitor to<br>PGND|
|25|GL|Low side MOSFET gate monitor|
|26 to 31|SW|Switch node|
|32, 33|PGND|Power ground. Common return for internal MOSFETs|


|ORDERING INFORMATION|Col2|Col3|Col4|
|---|---|---|---|
|**PART NUMBER**|**PART MARKING**|**MAXIMUM CURRENT**|**PACKAGE**|
|SiC450ED-T1-GE3|SiC450|40 A|PowerPAK MLP34-57|
|SiC450EVB|Reference board|Reference board|Reference board|
|SiC451ED-T1-GE3|SiC451|25 A|PowerPAK MLP34-57|
|SiC451EVB|Reference board|Reference board|Reference board|
|SiC453ED-T1-GE3|SiC453|15 A|PowerPAK MLP34-57|
|SiC453EVB|Reference board|Reference board|Reference board|



S23-1166-Rev. D, 25-Dec-2023 **2** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**PART MARKING INFORMATION**


= **pin 1 indicator**





**P/N** **=** **part number code**


= **Siliconix logo**


= **ESD symbol**


**F** **=** **assembly factory code**


**Y** **=** **year code**


**WW   =** **week code**


**LL** **=** **lot code**









|ABSOLUTE MAXIMUM RATINGS (T = 25 °C, unless otherwise noted)<br>A|Col2|Col3|Col4|
|---|---|---|---|
|**ELECTRICAL PARAMETER**|**CONDITIONS**|**LIMITS**|**UNIT**|
|PVIN, VIN|Reference to PGND|-0.3 to +28|V|
|Switching FETs break down voltage|Drain to source|+28|+28|
|SW / PH|Reference to PGND|-0.3 to +28|-0.3 to +28|
|SW / PH (AC)|Reference to PGND (100 ns)|-8 to +33|-8 to +33|
|BOOT||-0.3 to VPH + PVCC|-0.3 to VPH + PVCC|
|BOOT to SW||-0.3 to +6|-0.3 to +6|
|Drive supply voltage (PVCC)||-0.3 to +6|-0.3 to +6|
|Bias supply voltage (VDD)||-0.3 to +6|-0.3 to +6|
|AGND to PGND||-0.3 to +0.3|-0.3 to +0.3|
|All other pins|Reference to AGND|-0.3 to VDD + 0.3|-0.3 to VDD + 0.3|
|**Temperature**|**Temperature**|**Temperature**|**Temperature**|
|Junction temperature||-40 to +150|°C|
|Storage temperature||-65 to +150|-65 to +150|
|**Power Dissipation**|**Power Dissipation**|**Power Dissipation**|**Power Dissipation**|
|Junction-to-ambient thermal impedance (RthJA)||24|°C/W|
|Thermal resistance from junction to case (RthJ-C)||4.5|4.5|
|Thermal resistance from junction to PCB (RthJ-PCB)||5|5|
|**ESD Protection**|**ESD Protection**|**ESD Protection**|**ESD Protection**|
|Electrostatic discharge protection|HBM<br>CDM|2|kV|
|Electrostatic discharge protection|HBM<br>CDM|750|V|


_Stresses beyond those listed under “Absolute Maximum Ratings” may cause permanent damage to the device. These are stress ratings only, and functional operation_
_of the device at these or any other conditions beyond those indicated in the operational sections of the specifications is not implied. Exposure to absolute maximum_
_rating / conditions for extended periods may affect device reliability._







|RECOMMENDED OPERATING CONDITIONS (all voltages referenced to GND = 0 V)|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**ELECTRICAL PARAMETER**|**MIN.**|**TYP.**|**MAX.**|**UNIT**|
|PVIN, VIN|4.5|-|20|V|
|Logic pins|0|-|5.5|5.5|
|VOUT|0.3|-|12|12|
|Drive supply voltage (PVCC)|4.75|5|5.25|5.25|
|Bias supply voltage (VDD)|4.75|5|5.25|5.25|
|**Temperature**|**Temperature**|**Temperature**|**Temperature**|**Temperature**|
|Recommended ambient temperature|-40 to +85|-40 to +85|-40 to +85|°C|
|Operating junction temperature|-40 to +125|-40 to +125|-40 to +125|-40 to +125|


S23-1166-Rev. D, 25-Dec-2023 **3** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix













|ELECTRICAL SPECIFICATIONS (PV = 12 V, T = -40 °C to +125 °C, unless otherwise specified)<br>IN J|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PARAMETER**|**SYMBOL**|**TEST CONDITIONS**|**LIMITS**|**LIMITS**|**LIMITS**|**UNIT**|
|**PARAMETER**|**SYMBOL**|**TEST CONDITIONS**|** MIN.**|**TYP.**|**MAX.**|**MAX.**|
|**Power Supplies**|**Power Supplies**|**Power Supplies**|**Power Supplies**|**Power Supplies**|**Power Supplies**|**Power Supplies**|
|PVIN, VIN|PVIN, VIN||4.5|-|20|V|
|VIN_ON, default|VIN_ON|Default setting|-|10|-|-|
|VIN_OFF, default|VIN_OFF|Default setting|-|9|-|-|
|PVCC supply|VPVCC|VIN = 4.5 V to 20 V|4.5|5|5.5|5.5|
|VDD supply|VDD|Logic supply voltage|4.5|5|5.5|5.5|
|PVCC UVLO threshold|VPVCC_UVLO_TH||3.4|3.6|3.8|3.8|
|PVCC UVLO hysteresis|VPVCC_UVLO_HYS||-|300|-|mV|
|Input current|IVIN|TJ = 25 °C, non-switching, no load, VOUT > VSET|-|3.5|6|mA|
|Shutdown current|IVIN_SDN|EN = 0 V, IPVCC + IPVDD + IPVIN|-|2.5|6|6|
|**PVIN Monitoring**|**PVIN Monitoring**|**PVIN Monitoring**|**PVIN Monitoring**|**PVIN Monitoring**|**PVIN Monitoring**|**PVIN Monitoring**|
|PVIN monitor accuracy|VPVIN_MON_ACC||-|3|-|%|
|PVIN min. monitor resolution|VPVIN_MON_RSO||-|70|-|mV|
|PVIN monitor full scale|VPVIN_MON_SCL||-|-|28|V|
|PVIN read frequency|tPVIN_RSP||-|78|-|Hz|
|**IIN Fault Response Time**|**IIN Fault Response Time**|**IIN Fault Response Time**|**IIN Fault Response Time**|**IIN Fault Response Time**|**IIN Fault Response Time**|**IIN Fault Response Time**|
|IIN fault response time|tIIN_RSP|IIN_OC_WARN|-|78|-|Hz|
|**Pin (Input power)**|**Pin (Input power)**|**Pin (Input power)**|**Pin (Input power)**|**Pin (Input power)**|**Pin (Input power)**|**Pin (Input power)**|
|Pin sense accuracy|PPVIN_SNS_ACC|5 W to 160 W|-|5|-|%|
|Pin sense resolution|PPVIN_SNS_RSO||-|0.5|-|W|
|**Output Voltage**|**Output Voltage**|**Output Voltage**|**Output Voltage**|**Output Voltage**|**Output Voltage**|**Output Voltage**|
|VOUT default set-point|VOUT|VSET resistor = OPEN or SHORT|-|0.6|-|V|
|VOUT set-point accuracy|VOUT_ACC|Measured asV (VSEN+ - VSEN-)|-1|-|1|%|
|VOUT set-point accuracy|VOUT_ACC|Measured asV (VSEN+ - VSEN-), VIN = 12 V,<br>VO = 3.3 V and TA = 25 °C|-0.5|-|+0.5|+0.5|
|VOUT set-point accuracy|VOUT_ACC|Measured asV (VSEN+ - VSEN-), VIN = 12 V,<br>VO = 1.8 V and TA = 25 °C|-0.5|-|+0.5|+0.5|
|VOUT set-point range|VOUT_RNG||0.3|-|12|V|
|VOUT set-point resolution|VOUT_RSO||-|2|-|mV|
|Line regulation|VOUT_REG||-|1|-|%|
|Load regulation|VOUT_REG||-|1|-|-|
|VOUT min. monitor resolution|VOUT_MON_RSO|VOUT scale loop = 1|-|5|-|mV|
|VOUT start up delay range|tS_DLY_RNG|From PVIN valid until 1st PWM pulse|-|0|-|ms|
|VSEN+ common mode range|VVSNS_RNG||-0.2|-|12|V|
|VSEN- common mode range|VVSNS_RNG||-200|-|200|mV|
|VOUT read conversion frequency|tVOUT_RSP||-|78|-|Hz|
|**Controller and Timing**|**Controller and Timing**|**Controller and Timing**|**Controller and Timing**|**Controller and Timing**|**Controller and Timing**|**Controller and Timing**|
|Minimum on-time|tON_MIN||-|50|-|ns|
|Minimum off-time|tOFF_MIN||-|250|-|-|
|tON accuracy|tON_ACC||-10|-|10|%|
|Frequency, default|fSW||540|600|660|kHz|
|Frequency setting range|fSW_RNG|CCM mode|300|-|1500|1500|


S23-1166-Rev. D, 25-Dec-2023 **4** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

























|ELECTRICAL SPECIFICATIONS (PV = 12 V, T = -40 °C to +125 °C, unless otherwise specified)<br>IN J|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PARAMETER**|**SYMBOL**|**TEST CONDITIONS**|**LIMITS**|**LIMITS**|**LIMITS**|**UNIT**|
|**PARAMETER**|**SYMBOL**|**TEST CONDITIONS**|** MIN.**|**TYP.**|**MAX.**|**MAX.**|
|**VOUT Soft Start / Soft Stop**|**VOUT Soft Start / Soft Stop**|**VOUT Soft Start / Soft Stop**|**VOUT Soft Start / Soft Stop**|**VOUT Soft Start / Soft Stop**|**VOUT Soft Start / Soft Stop**|**VOUT Soft Start / Soft Stop**|
|tON rise, default|tON_RISE|From VOUT = 0 V to VOUT set point|-|5|-|ms|
|tON rise, setting range|tON_RNG||0|-|127|127|
|tOFF fall, default|tSSP||-|5|-|-|
|tOFF fall, setting range|tSSP,RNG||0|-|127|127|
|tON delay, default|tON_DLY|From VOUT = 0 V to VOUT set point|-|0|-|-|
|tON delay, setting range|tON_DLY,RNG||0|-|127|127|
|tOFF delay, default|tOFF_DLY||-|0|-|-|
|tOFF delay, setting range|tOFF_DLY,RNG||0|-|127|127|
|tON max. fault limit, default|tmax_FLT||-|20|-|-|
|tON max. fault limit, setting range|tmax_FLT,RNG||0|-|127|127|
|**Enable**|**Enable**|**Enable**|**Enable**|**Enable**|**Enable**|**Enable**|
|EN pull down resistance|REN||-|5|-|M|
|**RT/SYNC**|**RT/SYNC**|**RT/SYNC**|**RT/SYNC**|**RT/SYNC**|**RT/SYNC**|**RT/SYNC**|
|Logic high level|VRT/SYNC_HI||2|-|-|V|
|Logic low level|VRT/SYNC_LO||-|-|0.8|0.8|
|Input minimum pulse width|tIN Pulse_min||-|100|-|ns|
|Sync switching|FSYNC||300|-|1500|kHz|
|**Power Good**|**Power Good**|**Power Good**|**Power Good**|**Power Good**|**Power Good**|**Power Good**|
|Power good output rising<br>threshold|VFB_RISING_TH|Default value respect to<br>VOUT default setting = 0.6 V|-|90|-|%|
|Power good output falling<br>threshold|VFB_FALLING_TH|VFB_FALLING_TH|-|85|-|-|
|Power good hysteresis|VFB_HYST||-|5|-|-|
|Power good on resistance|RPG||-|5.5|-||
|Power good delay time (rising)|tPG_RISE_DLY||-|25|-|μs|
|Power good delay time (falling)|tPG_FALL_DLY||-|100|-|-|
|**Temperature Monitor and Temperature Shutdown**|**Temperature Monitor and Temperature Shutdown**|**Temperature Monitor and Temperature Shutdown**|**Temperature Monitor and Temperature Shutdown**|**Temperature Monitor and Temperature Shutdown**|**Temperature Monitor and Temperature Shutdown**|**Temperature Monitor and Temperature Shutdown**|
|Monitoring resolution|TMON_RSO||-|1|-|°C|
|Monitoring range|TMON_RNG||-40|-|+150|+150|
|Monitoring accuracy|TMON_ACC||-5|-|+5|+5|
|Thermal shutdown|TSD||-|125|-|-|
|Thermal shutdown hysteresis|TSD_HYS||-|35|-|-|
|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|**Digital Inputs** **(ADDR, SALRT, SCLK, SDA, EN)**|
|Input high threshold|VIH||2|-|-|V|
|Input low threshold|VIL||-|-|0.8|0.8|
|Input hysteresis|VHYST||-|0.1|-|-|
|Pin capacitance|CPIN||-|5|-|pF|
|**Fault Protections**|**Fault Protections**|**Fault Protections**|**Fault Protections**|**Fault Protections**|**Fault Protections**|**Fault Protections**|
|Valley current limit, default|IOCP|SiC450 (40 A), TJ = -40 °C to +85 °C|-|56|-|A|
|Valley current limit, default|IOCP|SiC451 (25 A), TJ = -40 °C to +85 °C|-|35|-|-|
|Valley current limit, default|IOCP|SiC453 (15 A), TJ = -40 °C to +85 °C|-|21|-|-|
|Output OVP threshold, default|VOVP|VOUT with respect to VSET|-|115|-|%|
|Output UVP threshold, default|VUVP|VUVP|-|80|-|-|


S23-1166-Rev. D, 25-Dec-2023 **5** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



|ELECTRICAL SPECIFICATIONS (PV = 12 V, T = -40 °C to +125 °C, unless otherwise specified)<br>IN J|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**PARAMETER**|**SYMBOL**|**TEST CONDITIONS**|**LIMITS**|**LIMITS**|**LIMITS**|**UNIT**|
|**PARAMETER**|**SYMBOL**|**TEST CONDITIONS**|** MIN.**|**TYP.**|**MAX.**|**MAX.**|
|**Telemetry**|**Telemetry**|**Telemetry**|**Telemetry**|**Telemetry**|**Telemetry**|**Telemetry**|
|VIN|VIN|Load current, 20 % to 100 %<br>(TA = -40 °C to +125 °C)|-3|-|3|%|
|IIN|IIN|20 % of load current (TA = 25 °C)|-15|-|15|15|
|IIN|IIN|50 % of load current (TA = 25 °C)|-6|-|6|6|
|IIN|IIN|100 % of load current (TA = 25 °C)|-5|-|5|5|
|PIN|PIN|20 % of load current (TA = 25 °C)|-9|-|9|9|
|PIN|PIN|50 % of load current (TA = 25 °C)|-4|-|4|4|
|PIN|PIN|100 % of load current (TA = 25 °C)|-3|-|3|3|
|VOUT|VOUT|2 V < VOUT < 5.5 V, load current, 20 % to 100 %<br>(TA = -40 °C to +125 °C)|-1.5|-|1.5|1.5|
|VOUT|VOUT|0.5 V < VOUT < 2 V, load current, 20 % to 100 %<br>(TA = -40 °C to +125 °C)|-2|-|2|2|
|IOUT|IOUT|20 % of load current (TA = 25 °C)|-12|-|12|12|
|IOUT|IOUT|50 % of load current (TA = 25 °C)|-4|-|4|4|
|IOUT|IOUT|100 % of load current (TA = 25 °C)|-3|-|3|3|
|POUT|POUT|20 % of load current (TA = 25 °C)|-9|-|9|9|
|POUT|POUT|50 % of load current (TA = 25 °C)|-4|-|4|4|
|POUT|POUT|100 % of load current (TA = 25 °C)|-3|-|3|3|


**FUNCTIONAL BLOCK DIAGRAM**







V IN



EN



PVIN


BOOT



PVCC

VDD


RT / SYNC


VSEN+


VSEN

VSET


ADDR


SALRT


SCLK


SDA

























SW


PGND














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
||||
||||
||||
||||
||||



P  / PIN OUT







calculation



PGOOD


**Fig. 4 - Functional Block Diagram**


S23-1166-Rev. D, 25-Dec-2023 **6** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**OPERATIONAL DESCRIPTION**


**Device Overview**



SiC45x is a high efficiency synchronous buck regulator
capable of delivering up to 25 A continuous current. The
device has programmable switching frequency of 300 kHz
to 1.5 MHz. The control scheme delivers fast transient
response and minimizes external components. Thanks to
the internal current ramp information, no high ESR output
bulk or virtual ESR network is required for the loop stability.
This device also incorporates a power saving feature by
enabling diode emulation mode and frequency fold back as
the load decreases.


In addition, a built in PLL allows in phase or 180° out of
phase synchronization under master / slave configuration.


SiC45x has a full set of protection and monitoring features
with response that can be set with PMBus:


- Over current protection in pulse-by-pulse mode


- Output over voltage protection


- Output under voltage protection


- Over temperature protection with hysteresis


- Dedicated enable pin for easy power sequencing


- Power good open drain output


This device is available in MLP34-57 package to deliver high
power density and minimize PCB area.


**PWM Control Mechanism**


SiC45x employs a voltage - mode COT control mechanism.
During steady-state operation, feedback voltage is
compared with internal reference and the amplified error
signal (VCOMP) is generated in the internal comp node. An
internally generated ramp signal and VCOMP are fed into a
comparator. Once VRAMP crosses VCOMP, a single shot
on-time pulse is generated for a fixed time, programmed by
the external Rfsw. During the on-time pulse, the high side
MOSFET will be turned on. Once the on-time pulse expires,
the low side MOSFET will be turned on after a
break-before-make period. The low side MOSFET will be on
for duration of minimum off-time pulse until VRAMP crosses
VCOMP. The cycle is then repeated.


Fig. 5 illustrates the basic block diagram for VM-COT
architecture. In this architecture the following is achieved:


- The reference of a basic ripple control regulator is
replaced with a high again error amplifier loop


- This establishes two parallel voltage regulating feedback
paths, a fast and slow path


- Fast path is the ripple injection which ensures rapid
correction of the transient perturbation


- Slow path is the error amplifier loop which ensures the DC
component of the output voltage follows the internal
accurate reference voltage



**Fig. 5 - VM-COT Block Diagram**


All components for RAMP signal generation and error
amplifier compensation required for the control loop are
internal to the IC, see Fig. 5. In order for the device to cover
a wide range of VOUT operation, the internal RAMP signal
components are automatically selected depending on the
VOUT voltage and switching frequency. The error amplifier
internal compensation consists of a resistor in series with a
capacitor (RCOMP, CCOMP).


Fig. 6 demonstrates the basic operational waveforms:


Basic operational waveforms


VCOMP


PWM Fixed on-time


**Fig. 6 - VM-COT Operational Principle**


**Light Load Condition**


To improve efficiency at light-load condition, SiC45x
provide a set of innovative implementations to eliminate LS
recirculating current and switching losses. The internal zero
crossing detector monitors SW node voltage to determine
when inductor current starts to flow negatively. In power
saving mode, as soon as inductor valley current crosses
zero, the device deploys diode emulation mode by turning
off low side MOSFET. If load further decreases, switching
frequency is reduced proportional to load condition to save
switching losses while keeping output ripple within



PVIN

















S23-1166-Rev. D, 25-Dec-2023 **7** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



tolerance. The switching frequency is set by the controller to
maintain regulation. In the standard power save mode, there
is no minimum switching frequency. If ultrasonic mode is
selected via PMBus, the minimum switching frequency that
the regulator will reduce to is > 20 kHz as the part avoids
switching frequencies in the audible range.


**Power Stage**


SiC45x integrates a high performance power stage with a
4 m  n-channel high side MOSFET and a 1.4 m  n-channel
low side MOSFET. The MOSFETs are optimized to achieve
up to 96 % efficiency.


The power input voltage (PVIN) can go up to 20 V and down
as low as 4.5 V. The output voltage must always be less than
the input voltage.


**Sequencing of Input / Output Supplies**


SiC45x has no sequencing requirements on any of its
input / output, PVIN, PVCC, VIN, VDD and EN. VIN is internal
supply voltage and is used to implement on time of COT
control. VIN shall be directly connected to PVIN.


**EN**


The SiC45x has an EN pin to turn the part on and off. Driving
this pin high enables the device, while grounding it turns it
off.


There are no sequencing requirements with respect to
input / output supplies.


**Output Overcurrent Protection (OCP)**


SiC45x has pulse-by-pulse overcurrent (OC) limit control.
The inductor valley current is monitored during low-side (LS)
FET turn-on period through RDS(on) sensing. After a
pre-defined blanking time, the valley current is compared
with an internal OCP threshold named
IOUT_OC_FAULT_LIMIT, which can be programmed via
PMBus. Once monitored valley current is larger than
IOUT_OC_FAULT_LIMIT, a pulse-by-pulse over-current
limit is broken, high-side (HS) turn-on pulse is skipped and
LS FET is kept on until the inductor valley current returns
below OCP limit as illustrated by Fig. 7.


An equation is given in (1) to calculate
IOUT_OC_FAULT_LIMIT from steady-state value of DC load
current when OCP happens.


IOUT_OC_FAULT_LIMIT =



IOUT_OCP -  ----------------------------------------------------------PV2  INL–  VPVOUTIN   fVSWOUT



(1)



SiC45x also provides secondary level OCP protection. If the
pulse-by-pulse overcurrent limit is persistently broken for
more than a specific number of consecutive switching
pulses in a row, secondary level OC fault is recognized and
both HS and LS MOSFETs are turned off. The device
continues restart attempt in a delay time until the OC fault
condition no longer exists.


The consecutive switching pulse in a row, the delay time,
and other types of fault responses can be programmed via
PMBus (see PMBus command section). The default number
is 128 for counting consecutive switching pulse in a row.
The default delay time is 20 ms.


The OCP is enabled immediately after VDD passes UVLO
level.


Iload


GH


**Fig. 7 - Over-Current Protection Illustration**


**Power Good**


Power good is an open-drain output. Pull PGOOD pin high up
to 5 V through a 10K resistor to use this signal.


- PGOOD rising threshold and falling threshold are adjustable
by using VOUT_PGOOD_ON (5Eh) and
VOUT_PGOOD_OFF (5Fh) commands


- PGOOD signal also goes low when output voltage is above
a threshold voltage (VOFL)


**Output Undervoltage Protection (UVP)**


UVP is implemented by monitoring the output voltage. If the
output voltage drops below a threshold voltage
VOUT_UV_FAULT_LIMIT (VUFL), the output-undervoltage (UV)
fault condition is recognized and both the HS and LS
MOSFETs are turned off. The device continues restart
attempt in a delay time until the UV condition no longer
exists.


The VUFL and the delay time can be programmed via PMBus
(see PMBus command section). The default value of VUFL is
20 % less than the target VOUT. The default delay time is
20 ms.


The UVP is only active after the completion of soft-start
sequence.



where: IOUT_OC_FAULT_LIMIT is the OCP threshold to be
programmed via PMBus; IOUT_OCP is the steady-state value
of DC load current when pulse-by-pulse OC event happens;
PVIN is the input voltage for power stage; VOUT is the output
voltage for power stage; L is inductance of power inductor;
and fSW is switching frequency for power stage.



S23-1166-Rev. D, 25-Dec-2023 **8** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



**Output-Overvoltage Protection (OVP)**


OVP is implemented by monitoring the output voltage. If the
output voltage is above a threshold voltage
VOUT_OV_FAULT_LIMIT (VOFL), the output-overvoltage (OV) fault
condition is recognized and both the HS and LS MOSFETs
are turned off. The device restarts when the OV fault
condition no longer exists.


The UVFL can be programmed via PMBus (see PMBus
command section). The default value of VOFL is 15 % more
than the target VOUT.

The OVP is enabled immediately after VDD passes UVLO
level.


**Input-Overvoltage Protection (VIN-OVP)**

VIN-OVP is implemented by monitoring the input voltage.
When the input voltage is pulled above a threshold voltage
VIN_OV_FAULT_LIMIT (VIN-OFL), the input-overvoltage (VIN-OV)
fault condition is recognized and both the HS and LS
MOSFETs are turned off. When the input voltage is pulled
below the VIN-OFL, the VIN-OV fault condition no longer exists
and the device restarts.


The VIN-OFL can be programmed via PMBus (see PMBus
command section). The default value of VIN-OFL is 15 V.

The VIN-OVP is enabled immediately after VDD passes UVLO
level.


**Input-Undervoltage Protection (VIN-UVP)**

VIN-UVP is implemented by monitoring the input voltage.
When the input voltage is pulled below a threshold VIN_OFF,
the input-undervoltage (VIN-UV) fault condition is recognized
and both the HS and LS MOSFETs are turned off. When the
input voltage is pulled above a threshold VIN_ON, the VIN-UV
fault condition no longer exists and the device restarts.


The VIN-OFF and VIN_ON can be programmed via PMBus (see
PMBus command section). The default value of VIN-OFF is
9 V. The default value of VIN_ON is 10 V.

The VIN-UVP is enabled immediately after VDD passes  UVLO
level.


**tON-MAX. Protection (tMP)**


SiC45x has power up time limit control. When the device
does not power up the output voltage above the VUFL in a
time interval longer than tON_MAX_FAULT_LIMIT (tMFL), the
tON-MAX. (tM) fault condition is recognized and both the HS
and LS MOSFETs are turned off. The device continues
restart attempt after the shutdown in a delay time until the tM
fault no longer exists.


The tMFL and delay time can be programmed via PMBus (see
PMBus command section). The default value of tMFL is
20 ms. The default delay time is 20 ms.


The tMP is enabled immediately after VDD passes UVLO level.



**Overtemperature Protection (OTP)**


SiC45x has internal thermal monitor block to support device
temperature control. When the device temperature rises
above OT_FAULT_LIMIT (OFL), the overtemperature (OT)
fault condition is recognized and both the HS and LS
MOSFETs are turned off. When OT fault condition no longer
exists, the device restarts.


The OFL can be programmed via PMBus (see PMBus
command section). The default value of OFL is 125 °C.


The OTP is enabled immediately after VDD passes UVLO
level.


**Pre-Bias Start-Up**


VOUT is monitored through differential output voltage sense
pins Vsen+ and Vsen-. If the sensed voltage is higher than
VSET, control logic prevents HS and LS FET from switching
to avoid negative output voltage spike and excessive
current sinking through LS FET.


**Fig. 8 - Pre-Bias Start-Up**


**Output Voltage Setting**


Connecting a resistor from VSET to AGND will set output
voltage (VOUT), eight VOUT related warning and fault voltage
limits, and the value of VOUT_SCALE_LOOP as listed in the
“VOUT_SCALE_LOOP look up” table. See below 2 tables for
the list of supported output voltage (VOUT) set by the VSET
resistor value and related warning and fault limits.


In case the output voltage is set by PMBUS, the VSET pin
needs to be shorted to AGND or left open. If so, the output
voltage can be set with resolution of 1.953 mV and the
related warning and fault limits can also be set
independently.


If a different voltage other than one listed in the “OUTPUT
VOLTAGE SETTINGS“ table is required without PMBUS, a
resistor divider can be used between output voltage sense
point, VSEN+ and VSEN- pins. Output voltage will be less
accurate with this method. Contact Vishay to know how.



S23-1166-Rev. D, 25-Dec-2023 **9** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix





**RT/SYNC PIN and Mode of Switching Configuration**


The SiC45x has an RT / SYNC pin. This pin can be used to
set the switching frequency and to send or receive a clock
signal for synchronization between a master and slave.
SiC45x will inject less than 1 mA DC current across the
RT/SYNC pin to the ground during initial power up process,
and connecting a resistor from the RT/SYNC pin to ground
will be used to set the switching frequency according to the
table listed below. The following table shows the supported
frequency settings by the RT resistor value. Please do not
leave the setting resistor open or short, or contact Vishay for
technical support. The frequency set by the external resistor
can be overridden by a PMBus command with resolution
50 kHz (see PMBus command table).

|FREQUENCY SETTINGS|Col2|
|---|---|
|**RT RESISTOR (k****)**|**FREQUENCY (kHz)**|
|0.845|300|
|1.30|400|
|1.78|500|
|2.32|550|
|2.87|600|
|3.48|650|
|4.12|700|
|4.75|750|
|5.49|800|
|6.19|850|
|6.98|900|
|7.87|950|
|8.87|1000|
|10|1250|
|11|1500|



SiC45x supports four modes of switching configuration,
including standalone mode, master mode, slave mode in
phase, and slave mode 180° out of phase. The master mode
is default one of switching configuration and user can
override it to be either standalone mode, slave mode in
phase, or slave mode 180° out of phase by PMBus
command INTERLEAVE (see PMBus command table).


|OUTPUT VOLTAGE SETTINGS|Col2|
|---|---|
|**VSET RESISTOR (k****) **|**VOUT (V)**|
|0.845|0.60|
|1.30|0.90|
|1.78|0.95|
|2.32|1.00|
|2.87|1.05|
|3.48|1.20|
|4.12|1.25|
|4.75|1.50|
|5.49|1.80|
|6.19|2.10|
|6.98|2.50|
|7.87|3.30|
|8.87|5.00|
|11.0|12.00|


|VOUT RELATED WARNINGS<br>AND FAULTS|VOLTAGE LEVEL|
|---|---|
|POWER_GOOD_ON|90 % VOUT|
|POWER_GOOD_OFF|85 % VOUT|
|VOUT_OV_FAULT_LIMIT|115 % VOUT|
|VOUT_OV_WARN_LIMIT|110 % VOUT|
|VOUT_UV_WARN_LIMIT|90 % VOUT|
|VOUT_UV_FAULT_LIMIT|80 % VOUT|
|VOUT_MARGIN_LOW|95 % VOUT|
|VOUT_MARGIN_HIGH|105 % VOUT|



S23-1166-Rev. D, 25-Dec-2023 **10** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

The following table introduces four modes of switching configuration, recommended RT/SYNC pin connections, and content of
related PMBus command INTERLEAVE.
















|MODE OF SWITCHING CONFIGURATION, PIN CONNECTION, AND INTERLEAVE PMBus|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**MODE TYPE**|**MODE DESCRIPTION**|**SWITCHING FREQUENCY AND RECOMMENDED**<br>**RT/SYNC PIN CONNECTION**|**SWITCHING**<br>**PHASE**|**INTERLEAVE**<br>**COMMAND**|
|Standalone|Chip works individually|Cross a resistor RRT from RT / SYNC pin to ground. During<br>power up, less than 1 mA DC current will be injected into<br>resistor RRT to determine default switching frequency. The<br>default switching frequency can be overridden by PMBus<br>command. After power up, RT / SYNC pin is released and<br>connected to ground via RRT.|Self determined|0x0000|
|Master|Chip works as a master<br>chip outputting a clock<br>signal in phase with its<br>switching to drive an<br>external slave chip’s<br>switching frequency and<br>phase|Cross a resistor RRT  from RT / SYNC pin to ground. During<br>power up, less than 1 mA DC current will be injected into<br>resistor RRT to determine default switching frequency. The<br>default switching frequency can be overridden by PMBus<br>command. After power up, RT / SYNC pin outputs a 50 %<br>duty cycle pulse signal toggling between 0 and VDD, which<br>is in phase with the chip’s switching node.|Self determined|0x0100|
|Slave in phase|Chip works as a slave<br>chip receiving an external<br>clock signal and<br>synchronize its switching<br>in phase with the clock<br>signal|Cross a resistor RRT from RT / SYNC pin to ground. During<br>power up, less than 1 mA DC current will be injected into<br>resistor RRT to determine default switching frequency. The<br>default switching frequency can be overridden by PMBus<br>command. When there is an external clock signal<br>presented at the RT / SYNC pin, the switching frequency<br>will be overridden and the chip’s switching node is in<br>phase with the external clock signal. If the external clock<br>signal comes from a SiC45x working in master mode<br>switching configuration, the resistor RRT shall be same to<br>the RRT used by the master chip.|In phase with the<br>external clock, or<br>self determined<br>when individually<br>works|0x0120|
|Slave 180 ° out<br>of phase|Chip works as a slave<br>chip receiving an external<br>clock signal and<br>synchronize its switching<br>180 ° out of phase with<br>the clock signal|Cross a resistor RRT from RT / SYNC pin to ground. During<br>power up, less than 1 mA DC current will be injected into<br>resistor RRT to determine default switching frequency. The<br>default switching frequency can be overridden by PMBus<br>command. When there is an external clock signal<br>presented at the RT / SYNC pin, the switching frequency<br>will be overridden and the chip’s switching node is 180°<br>out of phase with the external clock signal. If the external<br>clock signal comes from a SiC45x working in master mode<br>switching configuration, the resistor RRT shall be same to<br>the RRT used by the master chip|180° out of phase<br>with the external<br>clock, or self<br>determined when<br>individually<br>works|0x0121|



**PMBus ADDRESS (ADDR pin)**


The SiC45x has a 7-bit register that are used to set the base
PMBus address of the device. A resistor assembled
between ADDR pin and ground sets an offset from the
default pre-configured MFR base address in the memory.
Up to 15 different offsets can be set allowing 15 SiC45x
devices with unique addresses in a single system. This
offset and therefore the device address is read by the ADC
during the initialization sequence. The table below provides
the resistor values needed to set the 15 offsets from the
base address. Please do not leave the setting resistor open
or short.




|MFR_BASE_ADDRESS|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**CONNECTION**|**ADDRESS**|**HEX**<br>**[3 : 0]**|**NVM**<br>**[6 : 4]**|**BIN**<br>**[6 : 0]**|
|0.845K|1|0|001b|0010 000b|
|1.3K|2|1|001b|0010 001b|
|1.78K|3|2|001b|0010 010b|
|2.32K|4|3|001b|0010 011b|
|2.87K|5|4|001b|0010 100b|
|3.48K|6|5|001b|0010 101b|
|4.12K|7|6|001b|0010 110b|
|4.75K|8|7|001b|0010 111b|
|5.49K|9|8|001b|0011 000b|
|6.19K|10|9|001b|0011 001b|
|6.98K|11|A|001b|0011 010b|
|7.87K|12|B|001b|0011 011b|
|8.87K|13|C|001b|0011 100b|
|10K|14|D|001b|0011 101b|
|11K|15|E|001b|0011 110b|



S23-1166-Rev. D, 25-Dec-2023 **11** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



Vishay provides another 15 options of PMBus address listed
in table of MFR_BASE_ADDRESS_2. Please contact Vishay
for technical support.




|MFR_BASE_ADDRESS_2|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**CONNECTION**|**ADDRESS**|**HEX**<br>**[3 : 0]**|**NVM**<br>**[6 : 4]**|**BIN**<br>**[6 : 0]**|
|0.845K|1|0|101b|1010 000b|
|1.3K|2|1|101b|1010 001b|
|1.78K|3|2|101b|1010 010b|
|2.32K|4|3|101b|1010 011b|
|2.87K|5|4|101b|1010 100b|
|3.48K|6|5|101b|1010 101b|
|4.12K|7|6|101b|1010 110b|
|4.75K|8|7|101b|1010 111b|
|5.49K|9|8|101b|1011 000b|
|6.19K|10|9|101b|1011 001b|
|6.98K|11|A|101b|1011 010b|
|7.87K|12|B|101b|1011 011b|
|8.87K|13|C|101b|1011 100b|
|10K|14|D|101b|1011 101b|
|11K|15|E|101b|1011 110b|









|PMBus COMMAND LIST|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ADDRESS**|**PMBus COMMAND NAME**|**TYPE**|**DATA**<br>**FORMAT**<br>**(UNITS)**|**DEFAULT**<br>**VALUE IN**<br>**NVM**|**DEFAULT**|**VALID**<br>**RANGE**|
|01h|OPERATION|R/W|Byte|88h<br>(1000,1000)|[7] 1: PMBus unit output is on<br>[6] 0: output is turned off<br>immediately and any power down<br>sequencing commads are ignored<br>[5 : 4] 00: VOUT set by<br>VOUT_COMMAND<br>[3 : 2] 10: faults caused by selecting<br>VOUT_MARGIN_HIGH or<br>VOUT_MARGIN_LOW<br>as the nominal output voltage<br>source are acted upon according to<br>the settings of the<br>VOUT_OV_FAULT_RESPONSE and<br>VOUT_IV_FAULT_RESPONSE data<br>bytes<br>[1] 0: not used<br>[0]: reserved 02h|-|
|02h|ON_OFF_CONFIGURATION|R/W|Byte|1Fh<br>(0001,1111)|[7 : 5] 000: reserved<br>[4] 1: no power up until commanded<br>by the CONTROL and OPERATION<br>[3] 1: to start, the unit requires on/off<br>portion of the OPERATION<br>command<br>[2] 1: to start, the unit requires<br>CONTROL asserted<br>[1] 1: active high to start the unit<br>[0] 1: turn off VOUT as fast as<br>possible, ignore TOFF_DELAY and<br>TOFF_FALL|-|
|03h|CLEAR_FAULTS|Write|-|-|-|-|
|10h|WRITE_PROTECT|Write|Byte|00h<br>(0000,0000)|[7 : 0]: 0000,0000:<br>allows write to all registers|-|
|15h|STORE_USER_ALL|Write|-|-|-|-|
|16h|RESTORE_USER_ALL|Write|-|-|-|-|


S23-1166-Rev. D, 25-Dec-2023 **12** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix










































|PMBus COMMAND LIST|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ADDRESS**|**PMBus COMMAND NAME**|**TYPE**|**DATA**<br>**FORMAT**<br>**(UNITS)**|**DEFAULT**<br>**VALUE IN**<br>**NVM**|**DEFAULT**|**VALID**<br>**RANGE**|
|19h|CAPABILITY|Read|Byte|D0h<br>(1101,0000)|[7] 1: packet error checking is<br>supported<br>[6 : 5] 10: maximum supported<br>bus speed is 1 MHz<br>[4] 1: the unit has SMBALERT# pin<br>and supports SMBus alert response<br>protocol<br>[3] 0: numeric data is in LINEAR11,<br>LINEAR16, or DIRECT format<br> [2] 0: AVSBUS not supported<br>[1 : 0] 00: reserved|-|
|1Bh|SMBALERT_MASK|R/W|Block|0x0000<br>(0000,0000,<br>0000,0000)|-|-|
|20h|VOUT_MODE|Read|LINEAR1<br>6 (V)|17h<br>(0001,0111)|[7 : 5] 000: the unit uses<br>LINEAR16 format for<br>VOUT related commands<br>[4 : 0] 1,0111: five bit two is<br> complement exponent<br>equals -9 for VOUT related<br>commands|-|
|21h|VOUT_COMMAND|R/W|LINEAR1<br>6 (V)|0133h<br>(0000,0001,<br>0011,0011)|0.6 V|0.3 V to 14 V,<br>1.953 mV<br>resolution|
|22h|VOUT_TRIM|R/W|LINEAR1<br>6 (V)|xxxxh<br>(xxxx,xxxx,x<br>xxx,xxxx)|This command deviates from<br>standard PMBus 1.3 specifications;<br> a factory trim value varying by<br>devices|-2 V to 2 V,<br>1.953 mV<br>resolution|
|24h|VOUT_MAX|R/W|LINEAR1<br>6 (V)|1C00h<br>(0001,1100,<br>0000,0000)|14 V|0.3 V to 14 V,<br>1.953 mV<br>resolution|
|25h|VOUT_MARGIN_HIGH|R/W|LINEAR1<br>6 (V)|0142h<br>(0000,0001,<br>0100,0010)|0.63 V|0.3 V to 14 V,<br>1.953 mV<br>resolution|
|26h|VOUT_MARGIN_LOW|R/W|LINEAR1<br>6 (V)|0123h<br>(0000,0001,<br>0010,0011)|0.57 V|0.3 V to 14 V,<br>1.953 mV<br>resolution|
|27h|VOUT_TRANSITION_RATE|R/W|LINEAR1<br>1 (mV/μs)|E002h<br>(1110,0000,<br>0000,0010)|0.125 mV/μs|0.0625<br>mV/μs to2<br>mV/μs,<br>0.0625<br>mV/μs<br>resolution|
|29h|VOUT_SCALE_LOOP|R/W|LINEAR1<br>1 (V/V)|E808h<br>(1110,1000,<br>0000,1000)|This command deviates from<br>standard PMBus 1.3 specifications;<br>1 V/V|0.125 V/V,<br>0.25 V/V,<br>0.5 V/V, 1<br>V/V|
|33h|FREQUENCY_SWITCH|R/W|LINEAR1<br>1 (kHz)|0258h<br>(0000,0010,<br>0101,1000)|600 kHz|300 kHz to<br>1500 kHz,<br>50 kHz<br>resolution|
|35h|VIN_ON|R/W|LINEAR1<br>1 (V)|F814h<br>(1111,1000,<br>0001,0100)|10 V|1 V to 80 V,<br>0.5 V<br>resolution|
|36h|VIN_OFF|R/W|LINEAR1<br>1 (V)|F812h<br>(1111, 1000,<br>0001, 0010)|9 V|1 V to 80 V,<br>0.5 V<br>resolution|



S23-1166-Rev. D, 25-Dec-2023 **13** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix






































|PMBus COMMAND LIST|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ADDRESS**|**PMBus COMMAND NAME**|**TYPE**|**DATA**<br>**FORMAT**<br>**(UNITS)**|**DEFAULT**<br>**VALUE IN**<br>**NVM**|**DEFAULT**|**VALID**<br>**RANGE**|
|37h|INTERLEAVE|R/W|Word|0100h<br>(0000,0001,<br>0000,0000)|[15 : 12] 0000: reserved<br>[11 : 8] 0001: sets unit as<br>Master or Slave<br>[7 : 4] 0000: sets unit as master<br>[3 : 0] 0000: not used|Standalone,<br>master, slave<br>in phase,<br>slave<br>180° out of<br>phase|
|40h|VOUT_OV_FAULT_LIMIT|R/W|LINEAR1<br>6 (V)|0161h<br>(0000,0001,<br>0011,0011)|0.69 V|0.3 V to 14 V,<br>1.953 mV<br>resolution|
|41h|VOUT_OV_FAULT_RESPONSE|R/W|Byte|F8h<br>(1111,1000)|The device’s output is disabled while<br>the fault is present. Operation<br>resumes and the output is enabled<br>when the fault condition no longer<br>exists. It attempts to restart<br>continuously, without limitation, until<br>it is commanded off (by the<br>CONTROL pin or OPERATION<br>command or both), bias power is<br>removed, or another fault condition<br>causes the unit to shut down|00h, 16h,<br>22h,<br>36h, C0h,<br>D6h,<br>E2h, F6h,<br>F8h|
|42h|VOUT_OV_WARN_LIMIT|R/W|LINEAR1<br>6 (V)|0151h<br>(0000,0001,<br>0101,0001)|0.66 V|0.3 V to 14 V,<br>1.953 mV<br>resolution|
|43h|VOUT_UV_WARN_LIMIT|R/W|LINEAR1<br>6 (V)|0114h<br>(0000,0001,<br>0001,0100)|0.54 V|0 V to 14 V,<br>1.953 mV<br>resolution|
|44h|VOUT_UV_FAULT_LIMIT|R/W|LINEAR1<br>6 (V)|00F5h<br>(0000,0000,<br>1111,0101)|0.48 V|0 V to 14 V,<br>1.953 mV<br>resolution|
|45h|VOUT_UV_FAULT_RESPONSE|R/W|Byte|B9h<br>(1011,1001)|The device shuts down (disables the<br>output) and attempts to restart<br>continuously, without limitation, until<br>it is commanded off (by the EN pin or<br>OPERATION command or both),<br>bias power is removed, or another<br>fault condition causes the unit to<br>shut down. 20 ms delay|00h, 16h,<br>22h, 36h,<br>B9h, C0h,<br>D6h, E2h,<br>F6h|
|46h|IOUT_OC_FAULT_LIMIT|R/W|LINEAR1<br>1 (A)|SiC450:F87<br>0h<br>(1111,1000,<br>0111,0000)<br>SiC451:<br>F846h<br>(1111,1000,<br>0100,0110)<br>SiC453:<br>F82Ah<br>(1111,1000,<br>0010,1010)|SiC450: 56 A<br>SiC451: 35 A<br>SiC453: 21 A|0 A to 127 A,<br>0.5 A<br>resolution|
|47h|IOUT_OC_FAULT_RESPONSE|R/W|Byte|A1h<br>(1010,0001)|This command deviates from<br>standard PMBus 1.3 specifications.<br>The device continues operation for<br>128 consecutive OC cycles and then<br>shut down. Waiting for 20 ms, it<br>hiccups until the fault condition no<br>longer exists|00h, 16h,<br>22h, 36h,<br>A1h, C0h,<br>D6h, E2h,<br>F6h,<br>F8h|



S23-1166-Rev. D, 25-Dec-2023 **14** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix


































|PMBus COMMAND LIST|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ADDRESS**|**PMBus COMMAND NAME**|**TYPE**|**DATA**<br>**FORMAT**<br>**(UNITS)**|**DEFAULT**<br>**VALUE IN**<br>**NVM**|**DEFAULT**|**VALID**<br>**RANGE**|
|4Ah|IOUT_OC_WARN_LIMIT|R/W|LINEAR1<br>1 (A)|SiC450:<br>F868h<br>(1111,1000,<br>0110,1000)<br>SiC451:<br>F841h<br>(1111,1000,<br>0100,0010)<br>SiC453:<br>F827h<br>(1111,1000,<br>0010,0111)|SiC450: 52 A<br>SiC451: 32.5 A<br>SiC453: 19.5 A|0 A to 127 A,<br> 0.5 A<br>resolution|
|4Fh|OT_FAULT_LIMIT|R/W|LINEAR1<br>1 (°)|007Dh<br>(0000,0000,<br>0111,1101)|125 °C|0 °C to 150<br>°C, 1 °C<br>resolution|
|50h|OT_FAULT_RESPONSE|R/W|Byte|F9h<br>(1111,1001)|The device’s output is disabled while<br>the fault is present. Operation<br>resumes and the output is enabled<br>when the fault condition no longer<br>exists. It attempts to restart<br>continuously, without limitation, until<br>it is commanded off (by the EN pin<br>or OPERATION command or both),<br>bias power is removed, or another<br>fault condition causes the unit to<br>shut down|00h, 16h,<br> 22h, 36h,<br>C0h, D6h,<br>E2h, F6h,<br>F9h|
|51h|OT_WARN_LIMIT|R/W|LINEAR1<br>1 (°)|0069h<br>(0000,0000,<br>0110,1001)|105 °C|0 °C to 150<br>°C, 1 °C<br>resolution|
|55h|VIN_OV_FAULT_LIMIT|R/W|LINEAR1<br>1 (V)|F81Eh<br>(1111,1000,<br>0001,1110)|15 V|1 V to 80 V,<br>0.5 V<br>resolution|
|56h|VIN_OV_FAULT_RESPONSE|R/W|Byte|B8h<br>(1011,1000)|This command deviates from<br>standard PMBus 1.3<br>specifications.The device’s output is<br>disabled while the fault is present.<br>Operation resumes and the output is<br>enabled when the fault condition no<br>longer exists. It does not attempt to<br>restart. The output remains disabled<br>until the fault is cleared|00h, 16h,<br>22h, 36h,<br>B8h, C0h,<br>D6h, E2h,<br>F6h|
|58h|VIN_UV_WARN_LIMIT|R/W|LINEAR1<br>1 (V)|F812h<br>(1111,1000,<br>0001,0010)|9 V|1 V to 80 V,<br>0.5 V<br>resolution|
|5Dh|IIN_OC_WARN_LIMIT|R/W|LINEAR1<br>1 (A)|F80Ah<br>(1111,1000,<br>0000,1010)|5 A|0 A to 127 A,<br>0.5 A<br>resolution|
|5Eh|POWER_GOOD_ON|R/W|LINEAR1<br>6 (V)|0114h<br>(0000,0001,<br>0001,0100)|0.54 V|0.24 V to 14<br>V, 1.953 mV<br>resolution|
|5Fh|POWER_GOOD_OFF|R/W|LINEAR1<br>6 (V)|0105h<br>(0000,0001,<br>0000,0101)|0.51 V|0.24 V to 14<br>V, 1.953 mV<br>resolution|
|60h|TON_DELAY|R/W|LINEAR1<br>1 (ms)|0000h<br>(0000,0000,<br>0000,0000)|0 ms|0 ms to<br>127 ms, 1 ms<br>resolution|
|61h|TON_RISE|R/W|LINEAR1<br>1 (ms)|0005h<br>(0000,0000,<br>0000,0101)|5 ms|0 ms to<br>127 ms, 1 ms<br>resolution|



S23-1166-Rev. D, 25-Dec-2023 **15** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

















|PMBus COMMAND LIST|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ADDRESS**|**PMBus COMMAND NAME**|**TYPE**|**DATA**<br>**FORMAT**<br>**(UNITS)**|**DEFAULT**<br>**VALUE IN**<br>**NVM**|**DEFAULT**|**VALID**<br>**RANGE**|
|62h|TON_MAX_FAULT_LIMIT|R/W|LINEAR1<br>1 (mS)|0014h<br>(0000,0000,<br>0001,0100)|20 ms|0 ms to<br>127 ms, 1 ms<br>resolution|
|63h|TON_MAX_FAULT_RESPONS<br>E|R/W|Byte|B9h<br>(1011,1001)|The device shuts down (disables the<br>output). It attempts to restart<br>continuously, without limitation, until<br>it is commanded off (by the EN pin or<br>OPERATION command or both),<br>bias power is removed, or another<br>fault condition causes the unit to<br>shut down. 20 ms delay|80h, 83h,<br>86h, 88h,<br> 89h, 8Ah,<br>8Bh, B9h|
|64h|TOFF_DELAY|R/W|LINEAR1<br>1 (ms)|0000h<br>(0000,0000,<br>0000,0000)|0 ms|0 ms to<br>127 ms, 1 ms<br>resolution|
|65h|TOFF_FALL|R/W|LINEAR1<br>1 (ms)|0005h<br>(0000,0000,<br>0000,0101)|5 ms|0 ms to<br>127 ms, 1 ms<br>resolution|
|66h|TOFF_MAX_WARN_LIMIT|R/W|LINEAR1<br>1 (ms)|003Ch<br>(0000,0000,<br>0011,1100)|60 ms|0 ms to<br>127 ms, 1 ms<br>resolution|
|78h|STATUS_BYTE|Read|Byte|00h<br>(0000,0000)|No faults|-|
|79h|STATUS_WORD|Read|Word|0000h<br>(0000,0000,<br>0000,0000)|No faults|-|
|7Ah|STATUS_VOUT|Read|Byte|00h<br>(0000,0000)|No faults|-|
|7Bh|STATUS_IOUT|Read|Byte|00h<br>(0000,0000)|No faults|-|
|7Ch|STATUS_INPUT|Read|Byte|00h<br>(0000,0000)|No faults|-|
|7Dh|STATUS_TEMPERATURE|Read|Byte|00h<br>(0000,0000)|No faults|-|
|7Eh|STATUS_CML|Read|Byte|00h<br>(0000,0000)|No faults|-|
|80h|STATUS_MFR_SPECIFIC|Read|Byte|00h<br>(0000,0000)|No faults|-|
|88h|READ_VIN|Read|LINEAR1<br>1 (V)|n/a|n/a|0 V to 80 V|
|89h|READ_IIN|Read|ULINEAR<br>11 (A)|n/a|n/a|exp:<br>(-4) to (-16)|
|8Bh|READ_VOUT|Read|LINEAR1<br>6 (V)|n/a|n/a|0 V to 48 V|
|8Ch|READ_IOUT|Read|ULINEAR<br>11 (A)|n/a|n/a|exp:<br>(-4 ) to (-10)|
|8Dh|READ_TEMPERATURE|Read|LINEAR1<br>1 (°)|n/a|n/a|(-50)° to 150°|
|94h|READ_DUTY_CYCLE|Read|LINEAR1<br>1 (%)|n/a|n/a|0 % to 100<br>%|
|96h|READ_POUT|Read|ULINEAR<br>11 (W)|n/a|n/a|exp:<br>(-4) to (-16)|
|97h|READ_PIN|Read|ULINEAR<br>11 (W)|n/a|n/a|exp:<br>(-4) to (-16)|
|98h|PMBUS_REVISION|Read|Byte|33h<br>(0011,0011)|[7 :4] 0011: part I revision 1.3<br>[3 : 0] 0011: part II revision 1.3||


S23-1166-Rev. D, 25-Dec-2023 **16** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix







|PMBus COMMAND LIST|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**ADDRESS**|**PMBus COMMAND NAME**|**TYPE**|**DATA**<br>**FORMAT**<br>**(UNITS)**|**DEFAULT**<br>**VALUE IN**<br>**NVM**|**DEFAULT**|**VALID**<br>**RANGE**|
|9Eh|MFR_SERIAL|R/W|Block|n/a|For user to store customized<br>information||
|ADh|IC_DEVICE_ID|R/W|Block|0000h|-||
|D7h|MFR_BASE_ADDRESS|Pins program|7-bit|10h|-||
|E2h|MFR_BASE_ADDRESS_2|Pins program|7-bit|50h|-||


**PMBus COMMAND DETAILS**


**OPERATION (01h)**


The OPERATION command sets the operational state of the regulator. It is used for the following functions:


- Turn the regulator output on and off in conjunction with the input from EN signal


- Set the output voltage with upper or lower margins


- Select the fault handling behavior when fault is caused by margining state

|COMMAND|OPERATION|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|On/off|Off B|Margin|Margin|MRGNFLT|MRGNFLT|Nouse|RSV|
|Default (88h)|1|0|0|0|1|0|0|0|



**Bit Description (default setting in bold)**







|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|7|On/off|0b|Output is disabled|
|7|On/off|**1b**|**Output is enabled**|
|6|Off B|**0b**|**Output is turned off immediately and power off sequence commands ignored**|
|6|Off B|1b|Regulator turns off following the TOFF_DELAY and TOFF_FALL command|
|5 : 4|Margin|**00b**|**Output voltage is set by the PMBus VOUT_COMMAND data**|
|5 : 4|Margin|01b|Output voltage is set by the PMBus VOUT_MARGIN_LOW data|
|5 : 4|Margin|10b|Output voltage is set by the PMBus VOUT_MARGIN_HIGH data|
|5 : 4|Margin|11b|Not supported|
|3 : 2|MRGNFLT|00b|Not supported|
|3 : 2|MRGNFLT|01b|Faults caused by selecting VOUT_MARGIN_HIGH or VOUT_MARGIN_LOW as the nominal<br>output voltage source are ignored|
|3 : 2|MRGNFLT|**10b**|**Faults caused by selecting VOUT_MARGIN_HIGH or VOUT_MARGIN_LOW as the**<br>**nominal output voltage source are acted upon according to the settings of the**<br>**VOUT_OV_FAULT_RESPONSE and VOUT_UV_FAULT_RESPONSE**|
|3 : 2|MRGNFLT|11b|Not supported|
|1|Nouse|x|Not used|
|0|RSV|x|Reserved|


**ON_OFF_CONFIGURATION (02h)**


The ON_OFF_CONFIG command configures the combination of EN pin input and PMBus commands needed to turn the unit
on and off. This includes how the unit responds when power is applied.

|COMMAND|ON/OFF_CONFIGURATION|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|RSV|RSV|RSV|PU|CMD|EN|ENPOL|Off B1|
|Default (1Fh)|0|0|0|1|1|1|1|1|



S23-1166-Rev. D, 25-Dec-2023 **17** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Bit Description (default setting in bold)**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|7 : 5|RSV|000b|Reserved|
|4|PU|0b|Regulator powers up any time power is present regardless of state of the EN pin|
|4|PU|**1b**|**Regulator does not power up until commanded by the CONTROLEN**<br>**pin and OPERATION command**|
|3|CMD|0b|Regulator ignores the “on” bit in the OPERATION command|
|3|CMD|**1b**|**Regulator responds the “on” bit in the OPERATION command**|
|2|EN|0b|Regulator ignores the EN pin. Power conversion is controlled only by the OPERATION<br>command|
|2|EN|**1b**|**Regulator requires the EN pin to be asserted to start the unit**|
|1|ENPOL|0b|EN signal is active low|
|1|ENPOL|**1b**|**EN signal is active high**|
|0|OFFB1|0b|Regulator turns off following the tOFF_DELAY and tOFF_FALL command when EN signal is used<br>to turn off|
|0|OFFB1|**1b**|**Regulator turns off immediately**|



**CLEAR_FAULTS (03h)**


The CLEAR_FAULTS command is used to clear any fault bits that have been set. This command clears all bits in all status
registers simultaneously. At the same time, the device negates (clears, releases) its SALRT ALERT# signal output if the device
is asserting the SALRT ALERT# signal.


**WRITE_PROTECT (10h)**


The WRITE_PROTECT command is used to control writing to the PMBus device. The intent of this command is to provide
protection against accidental changes. This command is not intended to provide protection against deliberate or malicious
changes to a device’s configuration or operation.

|COMMAND|WRITE_PROTECT|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|WTPRT|WTPRT|WTPRT|Nouse|Nouse|Nouse|Nouse|Nouse|
|Default (00h)|0|0|0|0|0|0|0|0|



**Bit Description (default setting in bold)**







|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|7 : 5|WTPRT|**000b**|**Enable writes to all commands**|
|7 : 5|WTPRT|100b|Disable all writes except to the WRITE_PROTECT command|
|7 : 5|WTPRT|010b|Disable all writes except to the WRITE_PROTECT and OPERATION commands|
|7 : 5|WTPRT|001b|Disable all writes except to the WRITE_PROTECT, OPERATION, ON_OFF_CONFIG and<br>VOUT_COMMAND commands|
|4 : 0|Nouse|00000b|Not used|


**STORE_USER_ALL (15h)**


The STORE_USER_ALL command instructs the PMBus device to copy the entire contents of the operating memory to the
matching locations in the non-volatile User Store memory. Any items in operating memory that do not have matching locations
in the User Store are ignored.


**RESTORE_USER_ALL (16h)**


The RESTORE_USER_ALL command instructs the PMBus device to copy the entire contents of the nonvolatile user store
memory (NVM) to the matching locations in the operating memory. The values in the operating memory are overwritten by the
value retrieved from the user store. This feature is protected by the EEPROM_PASSWORD (DBh) command, see the section
below for more information. Any items in user store that do not have matching locations in the operating memory are ignored,
see the summary table for details.


S23-1166-Rev. D, 25-Dec-2023 **18** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**CAPABILITY (19h)**


The CAPABILITY command provides a way for a host system to determine some key capabilities of the PMBus device.


This is a read only register.

|COMMAND|WRITE_PROTECT|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|PEC|SPD|SPD|ALRT|NFMT|AVS|RSV|RSV|
|Default (D0h)|1|1|0|1|0|0|0|0|



**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|7|PEC|1b|Packet error checking is supported|
|6 : 5|SPD|10b|Maximum supported bus speed is 1 MHz|
|4|ALRT|1b|The unit has ALERT# pin and supports PMBus alert response protocol|
|3|NFMT|0b|Numeric data is in LINEAR11, LINEAR16, or DIRECT format|
|2|AVS|0b|AVSBUS not supported|
|1 : 0|RSV|00b|Reserved|



**SMBALERT_MASK (1Bh)**


The SMBALERT_MASK command may be used to prevent a warning or fault condition from asserting the SMBALERT# signal.
The command format used to block a status bit or bits from causing the SMBALERT# signal to be asserted is shown in Fig. 9.
The bits in the mask byte align with the bits in the corresponding status register. For example, if the STATUS_TEMPERATURE
command code were sent with the mask byte 01000000b, then an over temperature warning OT_WARNING (overtemperature
warning) condition would be blocked from asserting SMBALERT#.


7 1 1 8 1 8 1 8 1















**Fig. 9 - SMBALSER_MASK Command Packet Format**


The command format used by the host to determine the SMALER_MASK setting for a given status register is shown in Fig. 10.


7 1 1 8 1 8 1 8 1



















7 1 1 8 1 8 1















**Fig. 10 - Retrieving the SMBALSER_MASK Setting for a Given Status Register**


**VOUT_MODE (20h)**


The PMBus specification dictates that the data word for the VOUT_MODE command is one byte that consists of a 3-bit mode and
5-bit exponent parameter, as shown below. The 3-bit mode sets whether the device uses the linear or direct modes for output
voltage related commands. The 5-bit parameter sets the exponent value for the linear data mode. The mode and exponent
parameters are fixed and do not permit the user to change the values.


This is a read only register

|COMMAND|WRITE_PROTECT|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|Mode|Mode|Mode|EXP|EXP|EXP|EXP|EXP|
|Default (D0h)|0|0|0|1|0|1|1|1|



S23-1166-Rev. D, 25-Dec-2023 **19** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|7 : 5|Mode|000b|The unit uses ULINEAR16 format for VOUT related commands|
|4 : 0|EXP|10111b|5-bit two’s complement binary integer equals -9 for VOUT related commands|



**VOUT_COMMAND (21h)**


The VOUT_COMMAND is used to directly set the output voltage using the ULINEAR16 format, which is a 16-bit unsigned
integer. This is a read and write register. The output voltage, in volts, is calculated from the equation:

VOUT_SET = VOUT_COMMAND x 2 [N]


Where:


VOUT_SET is the set output voltage in volt


VOUT_COMMAND is the 16-bit unsigned binary integer specified in the command


N is a 5-bit two’s complement binary integer specified in VOUT mode [4 : 0]

|COMMAND|VOUT COMMAND|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|7|6|5|4|3|2|1|0|
|Function|Data byte high|Data byte high|Data byte high|Data byte high|Data byte high|Data byte high|Data byte high|Data byte high|Data byte low|Data byte low|Data byte low|Data byte low|Data byte low|Data byte low|Data byte low|Data byte low|
|Default (133h)|0|0|0|0|0|0|0|1|0|0|1|1|0|0|1|1|



**Bit Description**

|BITS|FORMAT|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|0133h|VOUT_COMMAND is specified as 307 x 2-9 = 0.6 V|



The output voltage’s range is 0.3 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0133h equivalent
to 0.6 V.


**VOUT_TRIM (22h)**


The VOUT_TRIM command is used to apply a fixed offset voltage to the output voltage command value. This is a read and write
register. The VOUT_TRIM has two data bytes formatted as a two’s complement binary integer (SLINEAR16 format). It is most
typically used by the end user to trim the output voltage at the time the PMBus device is assembled into the end user’s system.


The VOUT_TRIM command deviates from standard PMBus 1.3 specifications, at which it requires adding an integer calculating
from the expected offset voltage and the VOUT_SCALE_LOOP to VOUT_TRIM’s NVM register default store value varying by
devices. The effect of this command on the output voltage, in volts, is calculated from the equation:


 V  2 [N]
 Voltage = ------------------------------------------------------- **-**
VOUT_SCALE_LOOP


Where:

 voltage is the fixed offset voltage to the output voltage in volt

 V is the 16-bit two’s complement integer specified in VOUT_TRIM


VOUT_SCALE_LOOP is the dimensionless scale factor specified in VOUT_SCALE_LOOP command


N is a 5-bit two’s complement binary integer specified in VOUT_MODE [4:0].

|COMMAND|VOUT TRIM|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit position|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|Function|sign|data|data|data|data|data|data|data|data|data|data|data|data|data|data|data|
|Default (0000h)|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



S23-1166-Rev. D, 25-Dec-2023 **20** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Bit Description**

|BITS|FORMAT|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|0000h|V is 0 V|



The offset voltage’s range is -2 V to 2 V, resolution is 1.953 mV, and its NVM register default store value is a factory trim value
varying by devices. The users need to calculate a 16-bit two’s complement integer number following the above equation and
add the number to the factory trim value, so as to achieve the expected offset voltage to the output voltage.


**VOUT_MAX (24h)**


The VOUT_MAX command sets an upper limit on the output voltage the unit can command regardless of any other commands
or combinations. The intent of this command is to provide a safeguard against a user accidentally setting the output voltage to
a possibly destructive level rather than to be the primary output overvoltage protection. This is a read and write register.


The VOUT_MAX uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the VOUT_MAX
command.


**Bit Description**

|BITS|FORMAT|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|1C00h|The VOUT_MAX is specified as 14 V|



The VOUT_MAX range is 0.3 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 1C00h equivalent to
14 V.


**VOUT_MARGIN_HIGH (25h)**


The VOUT_MARGIN_HIGH command loads the unit with the voltage to which the output is to be changed when the
OPERATION command is set to “margin high”. This is a read and write register.


The VOUT_MARGIN_HIGH uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the
VOUT_MODE command.


**Bit Description**

|BITS|FORMAT|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|0142h|The VOUT_MARGIN_HIGH is specified as 0.63 V|



The VOUT_MARGIN_HIGH range is 0.3 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0142h
equivalent to 0.63 V.


**VOUT_MARGIN_LOW (26h)**


The VOUT_MARGIN_LOW command loads the unit with the voltage to which the output is to be changed when the OPERATION
command is set to margin low. This is a read and write register. 
The VOUT_MARGIN_LOW uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the
VOUT_MODE command.


**Bit Description**

|BITS|FORMAT|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|0123h|The VOUT_MARGIN_LOW is specified as 0.57 V|



The VOUT_MARGIN_LOW range is 0.3 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0123h
equivalent to 0.57 V.


**VOUT_TRANSITION_RATE (27h)**


The VOUT_TRANSITION_RATE command sets the rate in mV/μs at which the output voltage should change voltage when a
PMBus device receives either a VOUT_COMMAND or OPERATION (margin high, margin low) that causes the output voltage to
change. This commanded rate of change does not apply when the unit is commanded to turn on or to turn off. This is a read
and write register.
The VOUT_TRANSITION_RATE uses LINEAR11 format, which has two data bytes with an 11-bit two’s complement mantissa
and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of the
VOUT_TRANSITION_RATE command is constant as 5’b11100, that is, -4 in decimal. The LINEAR11 format of the two data
bytes is illustrated in table below.


S23-1166-Rev. D, 25-Dec-2023 **21** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Table - LINEAR11 Numeric Format Data Bytes**

|COMMAND|VOUT_TRANSITION_RATE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit position|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|Function|EXP|EXP|EXP|EXP|EXP|MAN|MAN|MAN|MAN|MAN|MAN|MAN|MAN|MAN|MAN|MAN|
|Default (E002h)|1|1|1|0|0|0|0|0|0|0|0|0|0|0|1|0|



**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15|EXP SGN|1b|Exponent value with negative sign|
|14 : 11|EXP|1100b|Five 5-bit two’s complement exponent equals -4 for VOUT_TRANSITION_RATE command|
|10|MAN SGN|0b|Mantissa value with positive sign|
|9 : 0|MAN DATA|00, 0000, 0010b|Eleven 11-bit two’s complement mantissa equals 2 for VOUT_TRANSITION_RATE command|



The VOUT_TRANSITION_RATE range is 0.0625 - 2 mV/μs, resolution is 0.0625 mV/μs, and its NVM register default store value
is E002h equivalent to 0.125 mV/μs. Any commands out of the valid range or with incorrect resolution will be ignored and
reported.


**VOUT_SCALE_LOOP** **(29h)**


The VOUT_SCALE_LOOP command deviates from standard PMBus 1.3 specifications. The VOUT_SCALE_LOOP command
is used to scale down both the VOUT_COMMAND and the sense differential output voltage at the unit input, so as to extend
operational range of the PMBus unit to reach the maximum output voltage 12 V without the requirement of external resistor
divider on board. This is a read and write register.
The VOUT_SCALE_LOOP uses LINEAR11 format, which has two data bytes with an 11-bit two’s complement mantissa and a
5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of the VOUT_SCALE_LOOP command
is constant as 5’b11101, that is, -3 in decimal.


The LINEAR11 format of the two data bytes is illustrated in Table “LINEAR11 Numeric Format Data Bytes”.


**Table - VOUT_SCALE_LOOP Look Up**

|SET OUTPUT VOLTAGE (V)|SCALE DOWN FACTOR (V/V)|VOUT_SCALE_LOOP BITS [15 : 0]|
|---|---|---|
|0.3 V < VOUT < 1.8 V|1.0|E808h|
|1.8 V VOUT < 3.3 V|0.5|E804h|
|3.3 V VOUT  5.0 V|0.25|E802h|
|5.0 VVOUT  12.0 V|0.125|E801h|



**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 to 0|Linear 11|E808h|The VOUT_SCALE_LOOP is specified as 1 V/V|



The VOUT_SCALE_LOOP offers four options of scale down factor: 1.0 V/V, 0.5 V/V, 0.25 V/V, and 0.125 V/V. When VOUT is set
by a resistor between VSET pin and ground, the value of VOUT_SCALE_LOOP is automatically chosen according to the
“VOUT_SCALE_LOOP look up” table. When VOUT is set by PMBus VOUT_COMMAND, the value of the VOUT_SCALE_LOOP
shall be updated according to the “VOUT_SCALE_LOOP look up” table.


The VOUT_SCALE_LOOP NVM register default store value is E808h equivalent to 1.0 V/V. Any commands out of the valid
options will be ignored and reported.


**FREQUENCY_SWITCH (33h)**


The FREQUENCY_SWITCH command sets the switching frequency, in kHz, of the PMBus unit. This is a read and write register.
The FREQUENCY_SWITCH uses LINEAR11 format, which has two data bytes with an 11-bit two’s complement mantissa and
a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of the FREQUENCY_SWITCH
command is constant as 5’b00000, that is, 0 in decimal. The LINEAR11 format of the two data bytes is illustrated in Table “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0258h|FREQUENCY_SWITCH is specified 600 kHz.|



S23-1166-Rev. D, 25-Dec-2023 **22** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

The FREQUENCY_SWITCH range is 300 kHz to 1500 kHz, resolution is 50 kHz, and its NVM register default store value is 0258h
equivalent to 600 kHz. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**VIN_ON (35h)**


The VIN_ON command sets the value of the input voltage, in volt, at which the PMBus unit should start power conversion. This
is a read and write register. The VIN_ON uses LINEAR11 format, which has two data bytes with an 11-bit two’s complement
mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of the VIN_ON
command is constant as 5’b11111, that is, -1 in decimal. The LINEAR11 format of the two data bytes is illustrated in Table “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|F814h|The VIN_ON is specified as 10 V|



The VIN_ON range is 1 V to 80 V, resolution is 0.5 V, and its NVM register default store value is F814h equivalent to 10 V. Any
commands out of the valid range or with incorrect resolution will be ignored and reported.


**VIN_OFF (36h)**


The VIN_OFF command sets the value of the input voltage, in volt, at which the PMBus unit, once operation has started, should
stop power conversion. This is a read and write register. The VIN_OFF uses LINEAR11 format, which has two data bytes with
an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement
exponent of the VIN_OFF command is constant as 5’b11111, that is, -1 in decimal. The LINEAR11 format of the two data bytes
is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|F812h|The VIN_OFF is specified as 9 V|



The VIN_OFF range is 1 V to 80 V, resolution is 0.5 V, and its NVM register default store value is F812h equivalent to 9 V. Any
commands out of the valid range or with incorrect resolution will be ignored and reported.


**INTERLEAVE (37h)**


The INTERLEAVE command deviates from standard PMBus 1.3 specifications. The INTERLEAVE command is used to sets the
mode of switching frequency and phase, at which the PMBus unit, once operation has started, should use to generate switching
frequency and phase angle. This is a read and write register.


The INTERLEAVE commands offer four modes of switching configuration: STANDALONE, MASTER, SLAVE in phase, and
SALVE 180° out of phase.
The description of all four modes and the corresponding INTERLEAVE command is listed in the table below.








|INTERLEAVE COMMAND AND MODE OF SWITCHING FREQUENCY GENERATION|Col2|Col3|
|---|---|---|
||**DESCRIPTION**|**INTERLEAVE BITS**<br>**[15 : 0]**|
|STANDALONE|The value of unit switching frequency is set by resistance of a resistor connected to RT/SYNC<br>unit designated pin. The setting value of the switching frequency will be overridden after the<br>PMBus unit receiving the PMBus command FREQUENCY_SWITCH command. The RT/SYNC pin<br>shall not be used for other purposes|0000h|
|MASTER|The value of unit switching frequency is set by resistance of a resistor connected to RT/SYNC<br>pin. The setting value of the switching frequency will be overridden after the PMBus unit receiving<br>the PMBus command FREQUENCY_SWITCH command. After inside power VDD of the unit is<br>above its under voltage level, the RT/SYNC pin will output a 50% duty cycle pulse signal in phase<br>with the switching frequency, which may be used to drive other units set as the SLAVE mode by<br>INTERLEAVE command. The RT/SYNC pin shall not be used for other purposes|0100h|
|SLAVE in phase|The value of unit switching frequency is set by resistance of a resistor connected to RT/SYNC<br>pin. The setting value of the switching frequency will be overridden after the PMBus unit receiving<br>the PMBus command FREQUENCY_SWITCH command. When an external pulse switching<br>signal is connected to the /SYNC pin, the unit will synchronize its switching frequency to the<br>external pulse switching signal with 0º phase difference. The RT/SYNC pin shall not be used for<br>other purpose|0120h|



S23-1166-Rev. D, 25-Dec-2023 **23** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



|INTERLEAVE COMMAND AND MODE OF SWITCHING FREQUENCY GENERATION|Col2|Col3|
|---|---|---|
||**DESCRIPTION**|**INTERLEAVE BITS**<br>**[15 : 0]**|
|SLAVE 180º out of<br>phase|The value of unit switching frequency is set by resistance of a resistor connected to RT/SYNC<br>pin. The setting value of the switching frequency will be overridden after the PMBus unit receiving<br>the PMBus command FREQUENCY_SWITCH command. When an external pulse switching<br>signal is connected to the /SYNC pin, the unit will synchronize its switching frequency to the<br>external pulse switching signal with 180º phase difference. The RT/SYNC pin shall not be used<br>for other purposes|0121h|


**Bit Description**







|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Linear 11|0100h|The INTERLEAVE is specified as MASTER mode|


The INTERLEAVE NVM register default store value is 0100h equivalent to MASTER mode. Any commands out of the options
will be ignored and reported.


**VOUT_OV_FAULT_LIMIT (40h)**


The VOUT_OV_FAULT_LIMIT command sets the value of the output voltage measured at the sense of output pins that causes
an output overvoltage fault. This is a read and write register.


The VOUT_OV_FAULT_LIMIT uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the
VOUT_MODE command.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Ulinear 16|0161h|The VOUT_OV_FAULT_LIMIT is specified as 0.69 V|



The VOUT_OV_FAULT_LIMIT range is 0.3 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0161h
equivalent to 0.69 V.


**VOUT_OV_FAULT_RESPONSE (41h)**


The VOUT_OV_FAULT_RESPONSE command instructs the device on what action to take in response to an output overvoltage
fault. This is a read and write register and the NVM register default store value is F8h.

|COMMAND|VOUT_OV_FAULT_RESPONSE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|OVRSP|OVRSP|OVRTY|OVRTY|OVRTY|OVDLY|OVDLY|OVDLY|
|Default (F8h)|1|1|1|1|1|0|0|0|



**Supported Commands**







|OVRSP|Col2|OVRTY|Col4|Col5|OVDLY|Col7|Col8|DESCRIPTIONS|
|---|---|---|---|---|---|---|---|---|
|1|1|1|1|1|0|0|0|The device’s output is disabled while the fault is present. Operation resumes<br>and the output is enabled when the fault condition no longer exists. It<br>attempts to restart continuously, without limitation, until it is commanded off<br>(by the CONTROL pin or OPERATION command or both), bias power is<br>removed, or another fault condition causes the unit to shut down|
|0|0|0|0|0|0|0|0|The device continues operation|
|0|0|0|1|0|1|1|0|The device continues operation|
|0|0|1|0|0|0|1|0|The device continues operation|
|0|0|1|1|0|1|1|0|The device continues operation|
|1|1|0|0|0|0|0|0|The device’s output is disabled while the fault is present. Operation resumes<br>and the output is enabled when the fault condition no longer exists|
|1|1|0|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes<br>and the output is enabled when the fault condition no longer exists|
|1|1|1|0|0|0|1|0|The device’s output is disabled while the fault is present. Operation resumes<br>and the output is enabled when the fault condition no longer exists|
|1|1|1|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes<br>and the output is enabled when the fault condition no longer exists|


S23-1166-Rev. D, 25-Dec-2023 **24** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**VOUT_OV_WARN_LIMIT (42h)**


The VOUT_OV_WARN_LIMIT command sets the value of the output voltage measured at the sense of output pins that causes
an output voltage high warning. This is a read and write register.


The VOUT_OV_WARN_LIMIT uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the
VOUT_MODE command.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Ulinear 16|0151h|The VOUT_OV_WARN_LIMIT is specified as 0.66 V|



The VOUT_OV_WARN_LIMIT range is 0.3 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0151h
equivalent to 0.66 V.


**VOUT_UV_WARN_LIMIT (43h)**


The VOUT_UV_WARN_LIMIT command sets the value of the output voltage measured at the sense of output pins that causes
an output voltage low warning. This is a read and write register.


The VOUT_UV_WARN_LIMIT uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the
VOUT_MODE command.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Ulinear 16|0114h|The VOUT_UV_WARN_LIMIT is specified as 0.54 V|



The VOUT_UV_WARN_LIMIT range is 0 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0114h
equivalent to 0.54 V.


**VOUT_UV_FAULT_LIMIT (44h)**


The VOUT_UV_FAULT_LIMIT command sets the value of the output voltage measured at the sense of output pins that causes
an output undervoltage fault. This is a read and write register.


The VOUT_UV_FAULT_LIMIT uses ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the
VOUT_MODE command.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Ulinear 16|00F5h|The VOUT_UV_FAULT_LIMIT is specified as 0.48 V|



The VOUT_UV_FAULT_LIMIT range is 0 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 00F5h
equivalent to 0.48 V.


**VOUT_UV_FAULT_RESPONSE (45h)**


The VOUT_UV_FAULT_RESPONSE command instructs the device on what action to take in response to an output undervoltage
fault. This is a read and write register and the NVM register default store value is B9h.

|COMMAND|VOUT_UV_FAULT_RESPONSE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|UVRSP|UVRSP|UVRTY|UVRTY|UVRTY|UVDLY|UVDLY|UVDLY|
|Default (B9h)|1|0|1|1|1|0|0|1|



S23-1166-Rev. D, 25-Dec-2023 **25** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Supported Commands**







|UVRSP|Col2|UVRTY|Col4|Col5|UVDLY|Col7|Col8|DESCRIPTIONS|
|---|---|---|---|---|---|---|---|---|
|1|0|1|1|1|0|0|1|The device shuts down (disables the output) and attempts to restart continuously,<br>without limitation, until it is commanded off (by the EN pin or OPERATION<br>command or both), bias power is removed, or another fault condition causes the<br>unit to shut down. 20 ms delay|
|0|0|0|0|0|0|0|0|The device continues operation|
|0|0|0|1|0|1|1|0|The device continues operation|
|0|0|1|0|0|0|1|0|The device continues operation|
|0|0|1|1|0|1|1|0|The device continues operation|
|1|1|0|0|0|0|0|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. The device does<br>not attempt to restart. The output remains disabled until the fault is cleared|
|1|1|0|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. The device does<br>not attempt to restart. The output remains disabled until the fault is cleared|
|1|1|1|0|0|0|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. The device does<br>not attempt to restart. The output remains disabled until the fault is cleared|
|1|1|1|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. The device does<br>not attempt to restart. The output remains disabled until the fault is cleared|


**IOUT_OC_FAULT_LIMIT (46h)**


The IOUT_OC_FAULT_LIMIT command sets the value of the output current, in Amperes, that causes the overcurrent detector
to indicate an overcurrent fault condition. This is a read and write register. The IOUT_OC_FAULT_LIMIT uses LINEAR11 format,
which has two data bytes with an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor).
The 5-bit two’s complement exponent of the IOUT_OC_FAULT_LIMIT command is constant as 5’b11111, that is, -1 in decimal.
The LINEAR11 format of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**






|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Linear 11|F870h|The IOUT_OC_FAULT_LIMIT is 56 A for SiC450|
|15:0|Linear 11|F846h|The IOUT_OC_FAULT_LIMIT is 35 A for SiC451|
|15:0|Linear 11|F82Ah|The IOUT_OC_FAULT_LIMIT is 21 A for SiC453|



The IOUT_OC_FAULT_LIMIT range is 0 A to 127 A, resolution is 0.5 A, and its NVM register default store value is F846h for
SiC451 equivalent to 35 A. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**IOUT_OC_FAULT_RESPONSE (47h)**


The IOUT_OC_FAULT_RESPONSE is used to set device over current protection response (OCP) when valley inductor current
is higher than IOUT_OC_FAULT_LIMIT. This is a read and write register and the NVM register default store value is A1h.

|COMMAND|IOUT_OC_FAULT_RESPONSE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|OCRSP|OCRSP|OCCYCL|OCCYCL|OCCYCL|OCDLY|OCDLY|OCDLY|
|Default (0xA1h)|1|0|1|0|0|0|0|1|



This command deviates from standard PMBus 1.3 specifications. It provides users 3-bit [5 : 3] setting to generate OC fault
based on total number of consecutive pulse-by-pulse OC counts. It also provides users 3-bit [2 : 0] delay time option between
shutdown and next restart attempt. In case of bits [5 : 3] = 111b, the device does not report OC fault and continues to operate
indefinitely while maintaining the output current at the value set by IOUT_OC_FAULT_LIMIT without regard to the output
voltage.


S23-1166-Rev. D, 25-Dec-2023 **26** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Supported Commands**

|OCRSP|Col2|OCRTY|Col4|Col5|OCDLY|Col7|Col8|DESCRIPTIONS|
|---|---|---|---|---|---|---|---|---|
|1|0|1|0|0|0|0|1|The device continues operation for 128 consecutive OC cycles and then shut down.<br>Waiting for 20 ms, it hiccups until the fault condition no longer exists|
|0|0|0|0|0|0|0|0|The device continues operation|
|0|0|0|1|0|1|1|0|The device continues operation|
|0|0|1|0|0|0|1|0|The device continues operation|
|0|0|1|1|0|1|1|0|The device continues operation|
|1|1|0|0|0|0|0|0|The device continues operation for 8 consecutive OC cycles and then shut down<br>without delay|
|1|1|0|1|0|1|1|0|The device continues operation for 32 consecutive OC cycles and then shut down<br>without delay|
|1|1|1|0|0|0|1|0|The device continues operation for 128 consecutive OC cycles and then shut down<br>without delay.|
|1|1|1|1|0|1|1|0|The device continues operation for 512 consecutive OC cycles and then shut down<br>without delay|
|1|1|1|1|1|0|0|0|The device continues operation and never shut down when OCP happens|



**IOUT_OC_WARN_LIMIT (4Ah)**


The IOUT_OC_WARN_LIMIT command sets the value of the output current, in ampere, that causes an output overcurrent
warning. This is a read and write register. The IOUT_OC_WARN_LIMIT uses LINEAR11 format, which has two data bytes with
an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement
exponent of the IOUT_OC_WARN_LIMIT command is constant as 5’b11111, that is, -1 in decimal. The LINEAR11 format of the
two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**






|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|1 5: 0|Linear 11|F868h|The IOUT_OC_WARN_LIMIT is 52 A SiC450|
|1 5: 0|Linear 11|F841h|The IOUT_OC_WARN_LIMIT is 32.5 A for SiC451|
|1 5: 0|Linear 11|F827h|The IOUT_OC_WARN_LIMIT is 19.5 A for SiC453|



The IOUT_OC_WARN_LIMIT range is 0 A to 127 A, resolution is 0.5 A, and its NVM register default store value is F841h for
SiC451 equivalent to 32.5 A. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**OT_FAULT_LIMIT (4Fh)**


The OT FAULT LIMIT command sets the temperature of the unit, in degree celsius, at which it should indicate an
overtemperature fault. This is a read and write register. The OT_FAULT_LIMIT uses LINEAR11 format, which has two data bytes
with an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement
exponent of the OT_FAULT_LIMIT command is constant as 5’b00000, that is, 0 in decimal. The LINEAR11 format of the two
data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15:0|Linear 11|007Dh|The OT_FAULT_LIMIT is specified as 125 °C|



The OT_FAULT_LIMIT range is 0 °C to 150 °C, resolution is 1 °C, and its NVM register default store value is 007Dh equivalent
to 125 °C. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**OT_FAULT_RESPONSE (50h)**


The OT_FAULT_RESPONSE command instructs the device on what action to take in response to an overtemperature fault. This
is a read and write register and the NVM register default store value is F9h.

|COMMAND|OT FAULT RESPONSE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|OTRSP|OTRSP|OTRTY|OTRTY|OTRTY|OTDLY|OTDLY|OTDLY|
|Default (F9h)|1|1|1|1|1|0|0|1|



S23-1166-Rev. D, 25-Dec-2023 **27** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Supported Commands**







|OTRSP|Col2|OTRTY|Col4|Col5|OTDLY|Col7|Col8|DESCRIPTIONS|
|---|---|---|---|---|---|---|---|---|
|1|1|1|1|1|0|0|1|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. It attempts to<br>restart continuously, without limitation, until it is commanded off (by the EN pin or<br>OPERATION command or both), bias power is removed, or another fault<br>condition causes the unit to shut down|
|0|0|0|0|0|0|0|0|The device continues operation|
|0|0|0|1|0|1|1|0|The device continues operation|
|0|0|1|0|0|0|1|0|The device continues operation|
|0|0|1|1|0|1|1|0|The device continues operation|
|1|1|0|0|0|0|0|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. It does not<br>attempt to restart. The output remains disabled until the fault is cleared|
|1|1|0|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists|
|1|1|1|0|0|0|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists|
|1|1|1|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists|


**OT_WARN_LIMIT (51h)**


The OT_WARN_LIMIT command sets the temperature of the unit, in degree celsius, at which it should indicate an
overtemperature warning alarm. This is a read and write register. The OT_WARN_LIMIT uses LINEAR11 format, which has two
data bytes with an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s
complement exponent of the OT_WARN_LIMIT command is constant as 5’b00000, that is, 0 in decimal. The LINEAR11 format
of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0069h|The OT_WARN_LIMIT is specified as 105 °C|



The OT_WARN_LIMIT range is 0 °C to 150 °C, resolution is 1 °C, and its NVM register default store value is 0069h equivalent
to 105 °C. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**VIN_OV_FAULT_LIMIT (55h)**


The VIN_OV_FAULT_LIMIT command sets the value of the input voltage, in volt, that causes an input overvoltage fault. This is
a read and write register. The VIN_OV_FAULT_LIMIT uses LINEAR11 format, which has two data bytes with an 11-bit two’s
complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of the
VIN_OV_FAULT_LIMIT command is constant as 5’b11111, that is, -1 in decimal. The LINEAR11 format of the two data bytes is
illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|F81Eh|The VIN_OV_FAULT_LIMIT is specified as 15 V|



The VIN_OV_FAULT_LIMIT range is 1 V to 80 V, resolution is 0.5 V, and its NVM register default store value is F81Eh equivalent
to 15 V. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**VIN_OV_FAULT_RESPONSE (56h)**


The VIN_OV_FAULT_RESPONSE command instructs the device on what action to take in response to an input overvoltage fault.
This is a read and write register and the NVM register default store value is B8h.

|COMMAND|VIN_OV_FAULT_RESPONSE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|VIOVRSP|VIOVRSP|VIOVRTY|VIOVRTY|VIOVRTY|VIOVDLY|VIOVDLY|VIOVDLY|
|Default (B8h)|1|0|1|1|1|0|0|0|



S23-1166-Rev. D, 25-Dec-2023 **28** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Supported Commands**

|OTRSP|Col2|OTRTY|Col4|Col5|OTDLY|Col7|Col8|DESCRIPTIONS|
|---|---|---|---|---|---|---|---|---|
|1|0|1|1|1|0|0|0|This command deviates from standard PMBus 1.3 specifications. The device’s<br>output is disabled while the fault is present. Operation resumes and the output<br>is enabled when the fault condition no longer exists. It does not attempt to<br>restart. The output remains disabled until the fault is cleared|
|0|0|0|0|0|0|0|0|The device continues operation|
|0|0|0|1|0|1|1|0|The device continues operation|
|0|0|1|0|0|0|1|0|The device continues operation|
|0|0|1|1|0|1|1|0|The device continues operation|
|1|1|0|0|0|0|0|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists. It does not<br>attempt to restart. The output remains disabled until the fault is cleared|
|1|1|0|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists|
|1|1|1|0|0|0|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists|
|1|1|1|1|0|1|1|0|The device’s output is disabled while the fault is present. Operation resumes and<br>the output is enabled when the fault condition no longer exists|



**VIN_UV_WARN_LIMIT (58h)**


The VIN_UV_WARN_LIMIT command sets the value of the input voltage, in volt, that causes an input voltage low warning. This
is a read and write register. The VIN_UV_WARN_LIMIT uses LINEAR11 format, which has two data bytes with an 11-bit two’s
complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of the
VIN_UV_WARN_LIMIT command is constant as 5’b11111, that is, -1 in decimal. The LINEAR11 format of the two data bytes is
illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|F812h|The VIN_UV_WARN_LIMIT is specified as 9 V|



The VIN_UV_WARN_LIMIT range is 1 V to 80 V, resolution is 0.5 V, and its NVM register default store value is F812h equivalent
to 9 V. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**IIN_OC_WARN_LIMIT (5Dh)**


The IIN_OC_WARN_LIMIT command sets the value of the input current, in ampere, that causes an input current overcurrent
Warning. This is a read and write register. The IIN_OC_WARN_LIMIT uses LINEAR11 format, which has two data bytes with an
11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement
exponent of the IIN_OC_WARN_LIMIT command is constant as 5’b11111, that is, -1 in decimal. The LINEAR11 format of the
two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|F80Ah|The IIN_OC_WARN_LIMIT is specified as 5 A|



The IIN_OC_WARN_LIMIT range is 0 A to 127 A, resolution is 0.5 A, and its NVM register default store value is F80Ah equivalent
to 5 A. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**POWER_GOOD_ON (5Eh)**


The POWER_GOOD_ON command sets the value of the output voltage at which an optional power good signal should be
asserted, indicating that the output voltage is valid. This is a read and write register. The POWER_GOOD_ON uses ULINEAR16
format, which is a 16-bit unsigned integer according to the setting of the VOUT_MODE command.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|0114h|The POWER_GOOD_ON is specified as 0.54 V|



The POWER_GOOD_ON range is 0.24 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0114h
equivalent to 0.54 V.


**POWER_GOOD_OFF (5Fh)**


The POWER_GOOD_OFF command sets the value of the output voltage at which an optional power good signal should be
negated, indicating that the output voltage is not valid. This is a read and write register. The POWER_GOOD_OFF uses
ULINEAR16 format, which is a 16-bit unsigned integer according to the setting of the VOUT_MODE command.


S23-1166-Rev. D, 25-Dec-2023 **29** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Ulinear 16|0105h|The POWER_GOOD_OFF is specified as 0.51 V|



The POWER_GOOD_OFF range is 0.24 V to 14 V, resolution is 1.953 mV, and its NVM register default store value is 0105h
equivalent to 0.51 V.


**TON_DELAY(60h)**


The TON_DELAY command sets the time, in millisecond, from which a start condition is received (as programmed by the
ON_OFF_CONFIG command) until the output voltage starts to rise. This is a read and write register. The TON_DELAY uses
LINEAR11 format, which has two data bytes with an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent
(scaling factor). The 5 bit two’s complement exponent of the TON_DELAY command is constant as 5’b0000, that is, 0 in
decimal. The LINEAR11 format of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0000h|The TON_DELAY is specified as 0 ms|



The TON_DELAY range is 0 ms to 127 ms, resolution is 1 ms, and its NVM register default store value is 0000h equivalent to
0 ms. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**TON_RISE (61h)**


The TON_RISE command sets the time, in millisecond, from when the output starts to rise until the voltage has entered the
regulation band. This is a read and write register. The TON_RISE uses LINEAR11 format, which has two data bytes with an 11-bit
two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement exponent of
the TON_RISE command is constant as 5’b0000, that is, 0 in decimal. The LINEAR11 format of the two data bytes is illustrated
in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0005h|The TON_RISE is specified as 5 ms|



The TON_RISE range is 0 ms to 127 ms, resolution is 1 ms, and its NVM register default store value is 0005h equivalent to
5 ms. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**TON_MAX_FAULT_LIMIT** **(62h)**


The TON_MAX_FAULT_LIMIT command sets an upper limit, in millisecond, on how long the unit can attempt to power up the
output without reaching the output undervoltage fault limit. This is a read and write register. The TON_MAX_FAULT_LIMIT uses
LINEAR11 format, which has two data bytes with an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent
(scaling factor). The 5-bit two’s complement exponent of the TON_MAX_FAULT_LIMIT command is constant as 5’b0000, that
is, 0 in decimal. The LINEAR11 format of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0014h|The TON_MAX_FAULT_LIMIT is specified as 20 ms|



The TON_MAX_FAULT_LIMIT range is 0 ms to 127 ms, resolution is 1 ms, and its NVM register default store value is 0014h
equivalent to 20 ms. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**TON_MAX_FAULT_RESPONSE (63h)**


The TON_MAX_FAULT_RESPONSE command instructs the device on what action to take in response to an input overcurrent
fault. This is a read and write register and the NVM register default store value is B9h.

|COMMAND|TON_MAX_FAULT_RESPONSE|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Bit position|7|6|5|4|3|2|1|0|
|Function|ONMXRSP|ONMXRSP|ONMXRTY|ONMXRTY|ONMXRTY|ONMXDLY|ONMXDLY|ONMXDLY|
|Default (0xB9h)|1|0|1|1|1|0|0|1|



S23-1166-Rev. D, 25-Dec-2023 **30** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**Supported Commands**







|ONMXRSP|Col2|ONMXRTY|Col4|Col5|ONMXDLY|Col7|Col8|DESCRIPTIONS|
|---|---|---|---|---|---|---|---|---|
|1|0|1|1|1|0|0|1|The device shuts down (disables the output). It attempts to restart continuously,<br>without limitation, until it is commanded off (by the EN pin or OPERATION command<br>or both), bias power is removed, or another fault condition causes the unit to shut<br>down. 20 ms delay|
|1|0|0|0|0|0|0|0|The device shuts down (disables the output). It does not attempt to restart. The<br>output remains disabled until the fault is cleared|
|1|0|0|0|0|0|1|1|The device shuts down (disables the output). It does not attempt to restart. The<br>output remains disabled until the fault is cleared|
|1|0|0|0|0|1|1|0|The device shuts down (disables the output). It does not attempt to restart. The<br>output remains disabled until the fault is cleared|
|1|0|0|0|1|0|0|0|The device shuts down (disables the output). It attempts to restart 1 time. No delay|
|1|0|0|0|1|0|0|1|The device shuts down (disables the output). It attempts to restart 1 time. 20 ms delay|
|1|0|0|0|1|0|1|0|The device shuts down (disables the output). It attempts to restart 1 time. 30 ms delay|
|1|0|0|0|1|0|1|1|The device shuts down (disables the output). It attempts to restart 1 time. 40 ms delay|


**TOFF_DELAY (64h)**


The TOFF_DELAY command sets the time, in millisecond, from when a stop condition is received until the unit stops transferring
energy to the output. This is a read and write register. The TOFF_DELAY uses LINEAR11 format, which has two data bytes with
an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit two’s complement
exponent of the TOFF_DELAY command is constant as 5’b0000, that is, 0 in decimal. The LINEAR11 format of the two data
bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0000h|The TOFF_DELAY is specified as 0 ms|



The TOFF_DELAY range is 0 ms to 127 ms, resolution is 1 ms, and its NVM register default store value is 0000h equivalent to
0 ms. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**TOFF_FALL (65h)**


The TOFF_FALL command sets the time, in millisecond, from the end of the turn-off delay time until the voltage is commanded
to zero. Note that this command can only be used with a device whose output can sink enough current to cause the output
voltage to decrease at a controlled rate. This is a read and write register. The TOFF_FALL uses LINEAR11 format, which has
two data bytes with an 11-bit two’s complement mantissa and a 5-bit two’s complement exponent (scaling factor). The 5-bit
two’s complement exponent of the TOFF_FALL command is constant as 5’b0000, that is, 0 in decimal. The LINEAR11 format
of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|0005h|The TOFF_FALL is specified as 5 ms|



The TOFF_FALL range is 0 ms to 127 ms, resolution is 1 ms, and its NVM register default store value is 0005h equivalent to
5 ms. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


**TOFF_MAX_WARN_LIMIT (66h)**


The TOFF_MAX_WARN_LIMIT command sets an upper limit, in millisecond, on how long the unit can attempt to power down
the output without reaching 12.5 % of the output voltage programmed at the time the unit is turned off. This is a read and write
register. The TOFF_MAX_WARN_LIMIT uses LINEAR11 format, which has two data bytes with an 11-bit two’s complement
mantissa and a 5-bit two’s complement exponent (scaling factor). The 5- bit two’s complement exponent of the
TOFF_MAX_WARN_LIMIT command is constant as 5’b0000, that is, 0 in decimal. The LINEAR11 format of the two data bytes
is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 : 0|Linear 11|003Ch|The TOFF_MAX_WARN_LIMIT is specified as 60 ms|



The TOFF_MAX_WARN_LIMIT range is 0 ms to 127 ms, resolution is 1 ms, and its NVM register default store value is 003Ch
equivalent to 60 ms. Any commands out of the valid range or with incorrect resolution will be ignored and reported.


S23-1166-Rev. D, 25-Dec-2023 **31** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**STATUS_BYTE (78h)**


The STATUS_BYTE command returns one byte of information with a summary of the most critical faults. The STATUS_BYTE
message content is described in the table below. This is a read register.


**Table - STATUS_BYTE Message Contents**

|BIT|STATUS BIT NAME|MEANING|
|---|---|---|
|7|BUSY|A fault was declared because the device was busy and unable to respond|
|6|OFF|This bit is asserted if the unit is not providing power to the output, regardless of the reason,<br>including simply not being enabled|
|5|VOUT_OV_FAULT|An output overvoltage fault has occurred|
|4|IOUT_UV_FAULT|An output overcurrent fault has occurred|
|3|VIN_UV_FAULT|An input undervoltage fault has occurred|
|2|Temperature|A temperature fault or warning has occurred|
|1|CML|A communications, memory or logic fault has occurred|
|0|None of the above|A fault or warning not listed in bits (7 to 1) has occurred|



**STATUS_WORD (79h)**


The STATUS_WORD command returns two bytes of information with a summary of the unit’s fault condition. Based on the
information in these bytes, the host can get more information by reading the appropriate status registers. The low byte of the
status word is the same register as the STATUS_BYTE command. The STATUS_WORD message content is described in the
following table. This is a read register.






|BYTE|BIT|STATUS BIT NAME|MEANING|
|---|---|---|---|
|Low|7|Busy|A fault was declared because the device was busy and unable to respond|
|Low|6|OFF|This bit is asserted if the unit is not providing power to the output, regardless of the<br>reason, including simply not being enabled|
|Low|5|VOUT_OV_FAULT|An output overvoltage fault has occurred|
|Low|4|IOUT_UV_FAULT|An output overcurrent fault has occurred|
|Low|3|VIN_UV_FAULT|An input undervoltage fault has occurred|
|Low|2|Temperature|A temperature fault or warning has occurred|
|Low|1|CML|A communications, memory or logic fault has occurred|
|Low|0|None of the above|A fault or warning not listed in bits [7 : 1] has occurred|
|High|7|VOUT|An output voltage fault or warning has occurred|
|High|6|IOUT / POUT|An output current or output power fault or warning has occurred|
|High|5|Input|An input voltage, input current, or input power fault or warning has occurred|
|High|4|MFR specific|A manufacturer specific fault or warning has occurred|
|High|3|PG status #|The power good signal, if present, is negated|
|High|2|Fans|Not available|
|High|1|Other|Not available|
|High|0|Unknown|Not available|



**STATUS_VOUT (7Ah)**


The STATUS_VOUT command returns one byte with contents described in the following table. This is a read register.

|BIT|MEANING|
|---|---|
|7|VOUT OV fault (output overvoltage fault)|
|6|VOUT OV warning (output overvoltage warning)|
|5|VOUT UV warning (output undervoltage warning)|
|4|VOUT OV fault (output undervoltage fault)|
|3|VOUT max. min. (an attempt has been made to set the output voltage toa value higher than allowed by the VOUT max. or<br>lower than the limited allowed by the VOUT min.)|
|2|tON max. fault|
|1|tOFF max. warning|
|0|Not available|



S23-1166-Rev. D, 25-Dec-2023 **32** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**STATUS_IOUT (7Bh)**


The STATUS_IOUT command returns one byte with contents described in the following table. This is a read register.

|BIT|MEANING|
|---|---|
|7|IOUT OC fault (output overcurrent fault)|
|6|Not available|
|5|IOUT OC warning (output overcurrent warning)|
|4|Not available|
|3|Not available|
|2|Not available|
|1|Not available|
|0|Not available|



**STATUS_INPUT (7Ch)**


The STATUS_INPUT command returns one byte with contents described in the following table. This is a read register.

|BIT|MEANING|
|---|---|
|7|VIN OV fault (input overvoltage fault)|
|6|Not available|
|5|VIN UV warning (input undervoltage warning)|
|4|Not available|
|3|Unit off for insufficient input voltage|
|2|Not available|
|1|IIN OC warning (input overcurrent warning)|
|0|Not available|



**STATUS_TEMPERATURE (7Dh)**


The STATUS_TEMPERATURE command returns one byte with contents described in the following table. This is a read register.

|BIT|MEANING|
|---|---|
|7|OT fault (overtemperature fault)|
|6|OT warning (overtemperature warning)|
|5 to 0|Not available|



**STATUS_CML (7Eh)**


The STATUS_CML command returns one byte with contents described in the following table. This is a read register.

|BIT|MEANING|
|---|---|
|7|Invalid or unsupported command received|
|6|Invalid or unsupported data received|
|5|Packet error check failed|
|4|Memory fault detected|
|3|Not available|
|2|Reserved|
|1|A communication fault other than the ones listed in this table has occurred|
|0|Not available|



**STATUS_MFR Specific (80h)**


The STATUS_MFR specific command returns one byte with contents described in the following table. This is a read register.

|BIT|MEANING|
|---|---|
|7 to 4|Not available|
|3|IL master fault|
|2|YF verify fault|
|1|YF erase fault|
|0|YF PGM fault|



S23-1166-Rev. D, 25-Dec-2023 **33** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**READ_VIN (88h)**


The READ_VIN command returns the input voltage in volt. The two data bytes are encoded in LINEAR11 format. The LINEAR11
format of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format Data Bytes”. This is a read register.


**READ_IIN (89h)**


The READ_IIN command returns the input current in ampere. The two data bytes in this register are encoded in unsigned
LINEAR11 format, ULINEAR11. The ULINEAR11 has the format shown in “Table - ULINEAR11 Format”
Table - ULINEAR11 Format

|COMMAND EXAMPLE|READ_IIN|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit position|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|Function|Two’s compliment exponent, N|Two’s compliment exponent, N|Two’s compliment exponent, N|Two’s compliment exponent, N|Two’s compliment exponent, N||Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|



The relation between N, M and real-world value, X is:

X = M x 2 [N]


For example, an input current of 0.501 A will return a value of AC03h in ULINEAR11 format when READ_IIN is implemented.

|Bit position|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Data|1|0|1|0|1|1|0|0|0|0|0|0|0|0|1|1|
|Function|Two’s compliment exponent, N|Two’s compliment exponent, N|Two’s compliment exponent, N|Two’s compliment exponent, N|Two’s compliment exponent, N||Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|Integer, M|



In this case, M = 1027, N = -11 and X = 0.50146


**READ_VOUT (8Bh)**


The read VOUT command returns the actual, measured output voltage in volt. The two data bytes are encoded in ULINEAR16
format, which is a 16-bit unsigned integer according to the setting of the VOUT_MODE command. This is a read register.


**READ_IOUT (8Ch)**


The READ_IOUT command returns the measured output current in ampere. The two data bytes are encoded in ULINEAR11
format. The ULINEAR11 format of the two data bytes is illustrated in Table - “ULINEAR11 Format”. This is a read register.


**READ_TEMPERATURE (8Dh)**


The READ_TEMPERATURE command returns the measured temperature of the PMBus unit in degree celsius. The two data
bytes are encoded in LINEAR11 format. The LINEAR11 format of the two data bytes is illustrated in Table - “LINEAR11 Numeric
Format Data Bytes”. This is a read register.


**READ_DUTY_CYCLE (94h)**


The READ_DUTY_CYCLE command returns the duty of the PMBus unit’s power conversion in percent. The two data bytes are
encoded in LINEAR11 format. The LINEAR11 format of the two data bytes is illustrated in Table - “LINEAR11 Numeric Format
Data Bytes”. This is a read register.


**READ_POUT (96h)**


The READ_POUT command returns the output power in watt. The two data bytes are encoded in ULINEAR11 format. The
ULINEAR11 format of the two data bytes is illustrated in Table - “ULINEAR11 Format”. This is a read register.


**READ_PIN (97h)**


The READ_PIN command returns the input power in watt. The two data bytes are encoded in ULINEAR11 format. The
ULINEAR11 format of the two data bytes is illustrated in Table - “ULINEAR11 Format”. This is a read register.


**PMBus_REVISION (98h)**


The PMBUS_REVISION command stores or reads the revision of the PMBus to which the device is compliant. The command
has one data byte. Bits (7 to 4) indicate the revision of PMBus specification Part I to which the device is compliant. Bits (3 to 0)
indicate the revision of PMBus specification part II to which the device is compliant. The permissible values are shown in the
table below. This is a read register.


**Table - PMBUS_REVISION DATA Byte Contents**

|BITS (7 TO 4)|PART I REVISION|BIT (3 TO 0)|PART II REVISION|
|---|---|---|---|
|0000b|1.0|0000b|1.0|
|0001b|1.1|0001b|1.1|
|0010b|1.2|0010b|1.2|
|0011b|1.3|0011b|1.3|



S23-1166-Rev. D, 25-Dec-2023 **34** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**MFR_SERIAL (9Eh)**


The MFR_SERIAL command is used to store user’s customized information. This is a read and write 16-bit block register.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 to 0|Block|0000h|A block register to store user’s customized information|



**IC_DEVICE_ID (ADh)**


The IC_DEVICE_ID command is used to either set or read the type or part number of an IC embedded within a PMBus that is
used for the PMBus interface. Each manufacturer uses the format of their choice for the IC device identification. IC_DEVICE_ID
is typically only set once, at the time of manufacture.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 to 0|Block|0000h|The part number of the unit|



**EEPROM_PASSWORD (DBh)**


The EEPROM_PASSWORD command will unlock write access to the internal NVM. This command must be sent before the
STORE_USER_ALL command. Access to the NVM can be disabled by sending any other data and will be automatically disabled
on each power-cycle.


**Bit Description**

|BITS|SYMBOL|VALUE|ACTION|
|---|---|---|---|
|15 to 0|Block|1234h|Default password for unlocking access to the NVM before the STORE_USER_ALL command|



**MFR_BASE_ADDRESS (D7h) and MFR_BASE_ADDRESS_2 (E2h)**


The data in either the MFR_BASE_ADDRESS (D7h) or MFR_BASE_ADDRESS_2 (E2h) register is used along with data from
ADDR resistor and VSET setting to generate the device’s PMBUS address, which consists of 7 bits. Its most significant 3 bits
are contributed by bits 6 to 4 of either MFR_BASE_ADDRESS register or MFR_BASE_ADDRESS_2 register, and its least
significant 4 bits come from the data determined by the resistor connected to ADDR pin. When VSET pin is shorted or connected
to AGND via a resistor, MFR_BASE_ADRESS register will be used to set bits 6 - 4. MFR_BASE_ADDRESS register has a default
value of 10 h and MFR_BASE:ADDRESS_” register 50 h. Both register can be READ or WRITTEN.


Here shows 2 examples.

1. Assume VSET pin is shorted or connected to AGND via a resistor, and a 4.75 k  resistor is connected between ADDR pin and
AGND, which corresponds to an address offset of 07 h, then MFR_BASE_ADDRESS register will be used to set the PBMBUS
address, which is 17 h.


2. Assume VSET pin is floating, and a 7.87 k  resistor is connected between ADDR pin and AGND, which corresponds to an
address offset of 0 Bh, then MFR_BASE_ADRESS_2 register will be used to set the PMBUS address, which is 5 Bh.


S23-1166-Rev. D, 25-Dec-2023 **35** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC453 (15 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 11 - SiC453 Startup with VIN, t = 5 ms/div**


**Fig. 12 - SiC453 Shut Down with VIN, t = 100 ms/div**


**Fig. 13 - SiC453 Startup with EN, t = 5 ms/div**



**Fig. 14 - SiC453 Shut down with EN, t = 100 ms/div**


**Fig. 15 - SiC453 OCP**


**Fig. 16 - SiC453 UVP**



S23-1166-Rev. D, 25-Dec-2023 **36** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC453 (15 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 17 - SiC453 Load Step, 7.5 A to 15 A, 1 A/μs, t = 10 μs/div**


**Fig. 18 - SiC453 Load Step, 15 A to 7.5 A, 1 A/μs, t = 10 μs/div**


**Fig. 19 - SiC453 Load Step, 0 A to 7.5 A, 1 A/μs, t = 10 μs/div**



**Fig. 20 - SiC453 Load Step, 0 A to 7.5 A, 1 A/μs, t = 10 μs/div**


**Fig. 21 - SiC453 Load Step, 0 A to 7.5 A, 1 A/μs, t = 10 μs/div**
**Skip Mode Enabled**


**Fig. 22 - SiC453 Load Step, 7.5 A to 0 A, 1 A/μs, t = 10 μs/div**
**Skip Mode Enabled**



S23-1166-Rev. D, 25-Dec-2023 **37** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC453 (15 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 23 - SiC453 Output Ripple, 0.01 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**


**Fig. 24 - SiC453 Output Ripple, 0.01 A, t = 20 μs/div**
**DCM Mode**


**Fig. 25 - SiC453 Output Ripple, 7.5 A, t = 1 μs/div**



**Fig. 26 - SiC453 Output Ripple, 15 A, t = 1 μs/div**


**Fig. 27 - SiC453 Prebias Startup**



S23-1166-Rev. D, 25-Dec-2023 **38** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC451 (25 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 28 - SiC451 Startup with VIN, t = 5 ms/div**


**Fig. 29 - SiC451 Shut Down with VIN, t = 100 ms/div**


**Fig. 30 - SiC451 Startup with EN, t = 2 ms/div**



**Fig. 31 - SiC451 Shut down with EN, t = 100 ms/div**


**Fig. 32 - SiC451 OCP**


**Fig. 33 - SiC451 UVP**



S23-1166-Rev. D, 25-Dec-2023 **39** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC451 (25 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 34 - SiC451 Load Step, 12.5 A to 25 A, 10 A/μs, t = 10 μs/div**


**Fig. 35 - SiC451 Load Step, 25 A to 12.5 A, 1 A/μs, t = 10 μs/div**


**Fig. 36 - SiC451 Load Step, 0 A to 12.5 A, 1 A/μs, t = 10 μs/div**



**Fig. 37 - SiC451 Load Step, 12.5 A to 0 A, 1 A/μs, t = 10 μs/div**


**Fig. 38 - SiC451 Load Step, 0 A to 12.5 A, 1 A/μs, t = 10 μs/div**
**Skip Mode Enabled**


**Fig. 39 - SiC451 Load Step, 12.5 A to 0 A, 1 A/μs, t = 10 μs/div**
**Skip Mode Enabled**



S23-1166-Rev. D, 25-Dec-2023 **40** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC451 (25 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 40 - SiC451 Output Ripple, 0.01 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**


**Fig. 41 - SiC451 Output Ripple, 0.01 A, t = 2 ms/div**
**DCM Mode**


**Fig. 42 - SiC451 Output Ripple, 12.5 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**



**Fig. 43 - SiC451 Output Ripple, 25 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**


**Fig. 44 - SiC451 Prebias Startup**



S23-1166-Rev. D, 25-Dec-2023 **41** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC450 (40 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 45 - SiC450 Startup with VIN, t = 5 ms/div**


**Fig. 46 - SiC450 Shut Down with VIN, t = 100 ms/div**


**Fig. 47 - SiC450 Startup with EN, t = 5 ms/div**



**Fig. 48 - SiC450 Shut down with EN, t = 100 ms/div**


**Fig. 49 - SiC450 Overcurrent Protection Behavior, t = 10 μs**


**Fig. 50 - SiC450 Output Undervoltage Protection Behavior,**
**t = 5 μs/div**



S23-1166-Rev. D, 25-Dec-2023 **42** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC450 (40 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 51 - SiC450 Load Step, 20 A to 40 A, 1 A/μs, t = 10 μs/div**


**Fig. 52 - SiC450 Load Step, 40 A to 20 A, 10 A/μs, t = 10 μs/div**


**Fig. 53 - SiC450 Load Step, 0 A to 20 A, 1 A/μs, t = 10 μs/div**



**Fig. 54 - SiC450 Load Step, 20 A to 0 A, 1 A/μs, t = 10 μs/div**


**Fig. 55 - SiC450 Load Step, 0 A to 20 A, 1 A/μs, t = 10 μs/div**
**Skip Mode Enabled**


**Fig. 56 - SiC450 Load Step, 20 A to 0 A, 1 A/μs, t = 10 μs/div**
**Skip Mode Enabled**



S23-1166-Rev. D, 25-Dec-2023 **43** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**ELECTRICAL CHARACTERISTICS** (VIN = 12 V, VOUT = 1.2 V, fsw = 600 kHz, SiC450 (40 A), CIN = 2.2 μF x 3,
COUT = 47 μF x 12, unless otherwise noted)



**Fig. 57 - SiC450 Output Ripple, 0.01 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**


**Fig. 58 - SiC450 Output Ripple, 0.01 A, t = 50 μs/div**
**DCM Mode**


**Fig. 59 - SiC450 Output Ripple, 20 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**



**Fig. 60 - SiC450 Output Ripple, 40 A, t = 1 μs/div**
**Forced Continuous Conduction Mode**


**Fig. 61 - SiC450 Prebias Startup**



S23-1166-Rev. D, 25-Dec-2023 **44** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix

**PCB LAYOUT RECOMMENDATIONS**



**Step 1: VIN/GND Planes and Decoupling**


**Fig. 62**
1. Layout VIN and PGND planes as shown above

2. Ceramic capacitors should be placed right between VIN
and PGND, and very close to the device for best
decoupling effect


3. Difference values / packages of ceramic capacitors
should be used to cover entire decoupling spectrum
e.g. 1210 and 0603


4. Smaller capacitance value, closer to device VIN pin(s) better high frequency noise absorbing


**Step 2: VIN Pin**


**Fig. 63**
1. VIN (pin 23) is the input pin for both internal LDO and tON
block. tON time varies based on input voltage. It is
necessary to put a decouple cap close to this pin



**Step 3: VSWH Plane**



**Fig. 64**

1. Connect output inductor to SiC45x with large plane to
lower the resistance


2. If any snubber network is required, place the
components on the bottom side as shown above



S23-1166-Rev. D, 25-Dec-2023 **45** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



**Step 4: VDD/PVCC Input Filter**


**Fig. 65**
1. CVDD and CPVCC caps should be placed close to the IC
to filter noise and provide maximum instantaneous driver
current for low side MOSFET during switching cycle


**Step 5: BOOT Resistor and Capacitor Placement**


**Fig. 66**

1. These components need to be placed very close to
SiC45x, right between PHASE (pin 4) and BOOT (pin 6)


2. To reduce parasitic inductance, chip size 0402 can be
used



**Step 6: Signal Routing**





**Fig. 67**

1. Separate the small analog signal from high current path.
As shown above, the high current paths with high dv/dt,
di/dt are placed on the right side of the IC, while the
small control signals are placed on the left side of the IC.
All the components for small analog signal should be
placed closer to IC with minimum trace length


2. Pin 16 is considered as IC analog ground, which should
have single connection to power ground. The AGND
ground plane connected with pin 16 helps to keep AGND
quite and improve noise immunity


3. Vsen+ / Vsen- differential analog signal pair should layout
using minimum clearance. Also, the differential pair
should be far away from VSWH node and other signals
throughout the length of the trace. Ground shield is
highly recommended



S23-1166-Rev. D, 25-Dec-2023 **46** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix



**Step 7: Adding Thermal Relief Vias and Duplicate Power**
**Path Plane**


**Fig. 68**
1. Thermal relief Vias can be added on the VIN and PGND
pads to utilize inner layers for high current and thermal
dissipation


2. To achieve better thermal performance, additional Vias
can be put on VIN plane and PGND plane. It is also
necessary to duplicate the VIN and ground plane at
bottom layer to maximize the power dissipation
capability from PCB


3. VSWH pad is a noise source and not recommended to put
Vias on this pad


4. 8 mil drill for pads and 10 mils drill for plane can be the
optional Via size. The Vias on pad may drain solder
during assembly and cause assembly issue. Please
consult with the assembly house for guideline



**Step 8: Ground Layer**


**Fig. 69**

1. It is recommended to make the whole inner 1 layer (next
to top layer) ground plane


2. This ground plane provides shielding between noise
source on top layer and signal trace within inner layer


3. The ground plane can be broken into two section as
power ground and analogue ground



S23-1166-Rev. D, 25-Dec-2023 **47** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **SiC450, SiC451, SiC453**
### www.vishay.com Vishay Siliconix









|PRODUCT SUMMARY|Col2|Col3|Col4|
|---|---|---|---|
|Part number|SiC450|SiC451|SiC453|
|Description|4.5 V to 20 V input 40 A<br>microBUCK DC/DC converter<br>with PMBus|4.5 V to 20 V input 25 A<br>microBUCK DC/DC converter<br>with PMBus|4.5 V to 20 V input 15 A<br>microBUCK DC/DC converter<br>with PMBus|
|Input voltage min. (V)|4.5|4.5|4.5|
|Input voltage max. (V)|20|20|20|
|Output voltage min. (V)|0.3|0.3|0.3|
|Output voltage max. (V)|12|12|12|
|Continuous current (A)|40|25|15|
|Switch frequency min. (kHz)|300|300|300|
|Switch frequency max. (kHz)|1500|1500|1500|
|Pre-bias operation (yes / no)|yes|yes|yes|
|Internal bias reg. (yes / no)|yes|yes|yes|
|Compensation|internal|internal|internal|
|Enable (yes / no)|yes|yes|yes|
|PGOOD (yes / no)|yes|yes|yes|
|Over current protection|yes|yes|yes|
|Protection|OVP, OCP, UVP/SCP, OTP,<br>UVLO|OVP, OCP, UVP/SCP, OTP,<br>UVLO|OVP, OCP, UVP/SCP, OTP,<br>UVLO|
|Light load mode|yes|yes|yes|
|Peak efficiency (%)|96|96|96|
|Package type|PowerPAK MLP34-57|PowerPAK MLP34-57|PowerPAK MLP34-57|
|Package size (W, L, H) (mm)|5.0 x 7.0 x 0.75|5.0 x 7.0 x 0.75|5.0 x 7.0 x 0.75|
|Status code|1|1|1|
|Product type|microBUCK|microBUCK|microBUCK|
|Applications|Computer, industrial, networking|Computer, industrial, networking|Computer, industrial, networking|


_[Vishay Siliconix maintains worldwide manufacturing capability. Products may be manufactured at one of several qualified locations. Reliability data for Silicon](http://www.vishay.com/ppg?71911)_
_[Technology and Package Reliability represent a composite of all qualified locations. For related documents such as package / tape drawings, part marking, and](http://www.vishay.com/ppg?71911)_
_[reliability data, see](http://www.vishay.com/ppg?71911)_ _www.vishay.com/ppg?77863._


S23-1166-Rev. D, 25-Dec-2023 **48** Document Number: 77863
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **Package Information**
### www.vishay.com Vishay Siliconix

## **PowerPAK [®] MLP34-57 Case Outline**










































|2 x|Col2|2 x|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|E<br>Pin 1 index<br>2 x<br>0.10 C|E<br>Pin 1 index<br>2 x<br>0.10 C|||0.10|C|D|D|
|E<br>Pin 1 index<br>2 x<br>0.10 C|E<br>Pin 1 index<br>2 x<br>0.10 C|||0.10|C|||
|E<br>Pin 1 index<br>2 x<br>0.10 C|E<br>Pin 1 index<br>2 x<br>0.10 C|||0.10|C|||
||0.10|0.10|C|||||



Top view












|D2-1 D2-2 K4|Col2|Col3|Col4|Col5|Col6|D2-2|K4|D2-1|1|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|e4<br>e5|e6<br>|K<br>34|K9<br>14<br>1|K9<br>14<br>1|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|30|30|30|E2-<br>K<br><br>K|D2-4<br>E2-3<br>4<br>7<br>K5<br>D2<br>L3<br>8|-5|||1|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|30|30|30|E2-<br>K<br><br>K|D2-4<br>E2-3<br>4<br>7<br>K5<br>D2<br>L3<br>8|-5|||E2<br>e1<br>e2<br>2 x<br>5 x<br>b3<br>5 x<br>b2<br>e7<br>23 x<br>e|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|0.10<br>C|0.05<br>C||b1<br><br>K6|b1<br><br>K6||||E2<br>K<br>e8|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|0.10<br>C|||||||||
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|0.10<br>C|||||||||
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|0.10<br>C||||||||9|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|0.10<br>C||||||||L|
|Bottom view<br>Side view<br>0.08 C<br>A<br>A2<br>A1<br>C<br>b<br>0.10<br>C A B<br>0.05<br>C<br>b1<br><br><br>D2-4<br>D2-3<br>E2<br>E2<br>E2-3<br>E2-4<br>K<br>K2<br>L<br>e1<br>e2<br>e8<br>e11<br>e3<br>e10<br>e4<br>e5<br>e6<br>b4<br>K9<br>K10<br>0.10 C A<br>2 x<br><br>K7<br>K6<br>K5<br>D2-5<br>K1<br>K1<br>L<br>L2<br>K11<br>K12<br>K13<br>K14<br>5 x<br>b3<br>b5<br>L3<br>1<br>9<br>18<br>19<br>30<br>31<br>10<br>34<br>5 x<br>b2<br>e7<br>23 x<br>e<br>e9<br>K10<br>K8<br>(3)|30|0.10<br>C||||e9|e9|e9|K1<br>L<br>10|K1<br>L<br>10|





|DIM.|MILLIMETERS|Col3|Col4|INCHES|Col6|Col7|
|---|---|---|---|---|---|---|
|**DIM.**|**MIN.**|**NOM.**|**MAX.**|**MIN.**|**NOM.**|**MAX.**|
|A (7)|0.70|0.75|0.80|0.027|0.029|0.031|
|A1|0.00|-|0.05|0.000|-|0.002|
|A2|0.20 ref.|0.20 ref.|0.20 ref.|0.008 ref.|0.008 ref.|0.008 ref.|
|b (3)|0.20|0.25|0.30|0.008|0.010|0.012|
|b1|0.15|0.20|0.25|0.006|0.008|0.010|
|b2|0.45|0.50|0.55|0.018|0.020|0.022|
|b3|0.38|0.43|0.48|0.015|0.017|0.019|
|b4|0.25|0.30|0.35|0.010|0.012|0.014|
|b5|0.20|0.25|0.30|0.008|0.010|0.012|
|D|4.90|5.00|5.10|0.193|0.197|0.201|
|E|6.90|7.00|7.10|0.272|0.276|0.280|
|e|0.50 BSC|0.50 BSC|0.50 BSC|0.020 BSC|0.020 BSC|0.020 BSC|
|e1|1.25 BSC|1.25 BSC|1.25 BSC|0.049 BSC|0.049 BSC|0.049 BSC|
|e2|0.63 BSC|0.63 BSC|0.63 BSC|0.025 BSC|0.025 BSC|0.025 BSC|
|e3|0.75 BSC|0.75 BSC|0.75 BSC|0.030 BSC|0.030 BSC|0.030 BSC|
|e4|0.80 BSC|0.80 BSC|0.80 BSC|0.031 BSC|0.031 BSC|0.031 BSC|
|e5|1.47 BSC|1.47 BSC|1.47 BSC|0.058 BSC|0.058 BSC|0.058 BSC|
|e6|0.80 BSC|0.80 BSC|0.80 BSC|0.031 BSC|0.031 BSC|0.031 BSC|
|e7|2.50 BSC|2.50 BSC|2.50 BSC|0.098 BSC|0.098 BSC|0.098 BSC|
|e8|2.50 BSC|2.50 BSC|2.50 BSC|0.098 BSC|0.098 BSC|0.098 BSC|
|e9|4.00 BSC|4.00 BSC|4.00 BSC|0.157 BSC|0.157 BSC|0.157 BSC|
|e10|3.00 BSC|3.00 BSC|3.00 BSC|0.118 BSC|0.118 BSC|0.118 BSC|
|e11|2.00 BSC|2.00 BSC|2.00 BSC|0.079 BSC|0.079 BSC|0.079 BSC|


Revision: 06-Aug-2018 **1** Document Number: 76600
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **Package Information**
### www.vishay.com Vishay Siliconix

|DIM.|MILLIMETERS|Col3|Col4|INCHES|Col6|Col7|
|---|---|---|---|---|---|---|
|**DIM.**|**MIN.**|**NOM.**|**MAX.**|**MIN.**|**NOM.**|**MAX.**|
|D2-1|1.06|1.11|1.16|0.042|0.044|0.046|
|D2-2|1.92|1.97|2.02|0.076|0.078|0.080|
|D2-3|3.45|3.50|3.55|0.136|0.138|0.140|
|D2-4|0.55|0.60|0.65|0.022|0.024|0.026|
|D2-5|0.78|0.83|0.88|0.031|0.033|0.035|
|E2-1|3.45|3.50|3.55|0.136|0.138|0.140|
|E2-2|1.73|1.78|1.83|0.068|0.070|0.072|
|E2-3|1.94|1.99|2.04|0.076|0.078|0.080|
|E2-4|1.02|1.07|1.12|0.040|0.042|0.044|
|L|0.35|0.40|0.45|0.014|0.016|0.018|
|L2|0.25|0.30|0.35|0.010|0.012|0.014|
|L3|0.30|0.35|0.40|0.012|0.014|0.016|
|K1|0.35 ref.|0.35 ref.|0.35 ref.|0.014 ref.|0.014 ref.|0.014 ref.|
|K2|0.35 ref.|0.35 ref.|0.35 ref.|0.014 ref.|0.014 ref.|0.014 ref.|
|K3|0.63 ref.|0.63 ref.|0.63 ref.|0.025 ref.|0.025 ref.|0.025 ref.|
|K4|0.40 ref.|0.40 ref.|0.40 ref.|0.016 ref.|0.016 ref.|0.016 ref.|
|K5|0.55 ref.|0.55 ref.|0.55 ref.|0.022 ref.|0.022 ref.|0.022 ref.|
|K6|0.30 ref.|0.30 ref.|0.30 ref.|0.012 ref.|0.012 ref.|0.012 ref.|
|K7|0.76 ref.|0.76 ref.|0.76 ref.|0.030 ref.|0.030 ref.|0.030 ref.|
|K8|0.40 ref.|0.40 ref.|0.40 ref.|0.016 ref.|0.016 ref.|0.016 ref.|
|K9|0.60 BSC|0.60 BSC|0.60 BSC|0.024 BSC|0.024 BSC|0.024 BSC|
|K10|0.78 BSC|0.78 BSC|0.78 BSC|0.031 BSC|0.031 BSC|0.031 BSC|
|K11|0.50 BSC|0.50 BSC|0.50 BSC|0.020 BSC|0.020 BSC|0.020 BSC|
|K12|0.48 BSC|0.48 BSC|0.48 BSC|0.019 BSC|0.019 BSC|0.019 BSC|
|K13|0.70 BSC|0.70 BSC|0.70 BSC|0.028 BSC|0.028 BSC|0.028 BSC|
|K14|1.23 BSC|1.23 BSC|1.23 BSC|0.048 BSC|0.048 BSC|0.048 BSC|
|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|ECN: T18-0377-Rev. A, 06-Aug-2018<br>DWG: 6069|



**Notes**
(1) Use millimeters as the primary measurement
(2) Dimensioning and tolerances conform to ASME Y14.5M. - 1994
(3) Dimension b applies to plated terminal and is measured between 0.20 mm and 0.25 mm from terminal tip
(4) The pin #1 identifier must be existed on the top surface of the package by using indentation mark or other feature of package body
(5) Exact shape and size of this feature is optional
(6) Package warpage max. 0.08 mm
(7) Applied only for terminals


Revision: 06-Aug-2018 **2** Document Number: 76600
For technical questions, contact: powerictechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **PAD Pattern**
### www.vishay.com Vishay Siliconix

## **Recommended Land Pattern PowerPAK [®] MLP34-57**

34 31


10 18
























|Col1|Col2|5.00 (pkg.)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0.30|0.30|5.00 (pkg.)<br>0.80<br>1.473<br>0.80<br>0.40<br>34<br>31<br>25<br>25|5.00 (pkg.)<br>0.80<br>1.473<br>0.80<br>0.40<br>34<br>31<br>25<br>25|5.00 (pkg.)<br>0.80<br>1.473<br>0.80<br>0.40<br>34<br>31<br>25<br>25|5.00 (pkg.)<br>0.80<br>1.473<br>0.80<br>0.40<br>34<br>31<br>25<br>25|5.00 (pkg.)<br>0.80<br>1.473<br>0.80<br>0.40<br>34<br>31<br>25<br>25|5.00 (pkg.)<br>0.80<br>1.473<br>0.80<br>0.40<br>34<br>31<br>25<br>25|0.475<br>0.30|0.475<br>0.30|0.475<br>0.30|0.475<br>0.30|
|0.30|0.30|2|2|2|2|2||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|0.|0.|0.30<br>0<br>2.073<br>30<br>0.6<br>2.07<br>0.68<br>0.652<br>8<br>2.197<br>~~0~~.~~6~~95<br>.93|0.30<br>0<br>2.073<br>30<br>0.6<br>2.07<br>0.68<br>0.652<br>8<br>2.197<br>~~0~~.~~6~~95<br>.93|0.30<br>0<br>2.073<br>30<br>0.6<br>2.07<br>0.68<br>0.652<br>8<br>2.197<br>~~0~~.~~6~~95<br>.93||2.00<br>30<br>0.550|2.00<br>30<br>0.550|||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|||||||30|30|30|30|30|
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|||||||52|||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|||||||52|||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||||||||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||||||||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||||||||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||||||~~0~~.~~6~~95|~~0~~.~~6~~95|||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15|1.15|3.00<br>0.775<br>19<br>0<br>30|3.00<br>0.775<br>19<br>0<br>30|3.00<br>0.775<br>19<br>0<br>30|3.00<br>0.775<br>19<br>0<br>30|
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15|1.15|||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15|1.15|||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||70<br>|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|~~0~~.7<br><br>0.525<br>0.20<br>1.875<br>0.85<br>1.15<br><br>0.30|1.15|1.15||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||||||||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|~~0~~.|~~0~~.|~~0~~.|~~0~~.|~~0~~.|~~0~~.|~~0~~.7|0|0|0|0|
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>||||||||||||
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|0.3|0||3.60||70|~~0~~.|30|30|30|30|
|0.775<br>9<br>0.3<br>~~0~~.<br>2.50 (0.5 x 5)<br>7.00 (pkg.)<br>1.25<br>1.25<br>1<br>0.60<br>0.<br>0.55<br>0.625<br>|0.3|0||3.60||||||||
|0.30|||||||||0.30|0.30|0.30|
|0.30||||||||||||



**Note**

- Dimensions in mm


ECN: T22-0594-Rev. A, 26-Dec-2022
DWG: 3016


Revision: 26-Dec-2022 **1** Document Number: 62187
For technical questions, contact: pmostechsupport@vishay.com
THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


## **Legal Disclaimer Notice**
### www.vishay.com Vishay

## **Disclaimer**

ALL PRODUCT, PRODUCT SPECIFICATIONS AND DATA ARE SUBJECT TO CHANGE WITHOUT NOTICE TO IMPROVE
RELIABILITY, FUNCTION OR DESIGN OR OTHERWISE.


Vishay Intertechnology, Inc., its affiliates, agents, and employees, and all persons acting on its or their behalf (collectively,
“Vishay”), disclaim any and all liability for any errors, inaccuracies or incompleteness contained in any datasheet or in any other
disclosure relating to any product.


Vishay makes no warranty, representation or guarantee regarding the suitability of the products for any particular purpose or
the continuing production of any product. To the maximum extent permitted by applicable law, Vishay disclaims (i) any and all
liability arising out of the application or use of any product, (ii) any and all liability, including without limitation special,
consequential or incidental damages, and (iii) any and all implied warranties, including warranties of fitness for particular
purpose, non-infringement and merchantability.


Statements regarding the suitability of products for certain types of applications are based on Vishay's knowledge of typical
requirements that are often placed on Vishay products in generic applications. Such statements are not binding statements
about the suitability of products for a particular application. It is the customer's responsibility to validate that a particular product
with the properties described in the product specification is suitable for use in a particular application. Parameters provided in
datasheets and / or specifications may vary in different applications and performance may vary over time. All operating
parameters, including typical parameters, must be validated for each customer application by the customer's technical experts.
Product specifications do not expand or otherwise modify Vishay's terms and conditions of purchase, including but not limited
to the warranty expressed therein.


Hyperlinks included in this datasheet may direct users to third-party websites. These links are provided as a convenience and
for informational purposes only. Inclusion of these hyperlinks does not constitute an endorsement or an approval by Vishay of
any of the products, services or opinions of the corporation, organization or individual associated with the third-party website.
Vishay disclaims any and all liability and bears no responsibility for the accuracy, legality or content of the third-party website
or for that of subsequent links.


Vishay products are not designed for use in life-saving or life-sustaining applications or any application in which the failure of
the Vishay product could result in personal injury or death unless specifically qualified in writing by Vishay. Customers using or
selling Vishay products not expressly indicated for use in such applications do so at their own risk. Please contact authorized
Vishay personnel to obtain written terms and conditions regarding products designed for such applications.


No license, express or implied, by estoppel or otherwise, to any intellectual property rights is granted by this document or by
any conduct of Vishay. Product names and markings noted herein may be trademarks of their respective owners.


_**© 2026 VISHAY INTERTECHNOLOGY, INC. ALL RIGHTS RESERVED**_


Revision: 01-Jan-2026 **1** Document Number: 91000


THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE. THE PRODUCTS DESCRIBED HEREIN AND THIS DOCUMENT
ARE SUBJECT TO SPECIFIC DISCLAIMERS, SET FORTH AT www.vishay.com/doc?91000


