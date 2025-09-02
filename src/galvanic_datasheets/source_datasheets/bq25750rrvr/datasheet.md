**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)
## **BQ25750: Standalone/I [2] C Controlled, 1- to 14-Cell Bidirectional Buck-Boost Battery** **Charge Controller with Direct Power Path Control**



**1 Features**


- Wide input voltage operating range: 4.2 V to 70 V

- Wide battery voltage operating range: up-to 70 V
with multi-chemistry support:

–
1- to 14-cell Li-ion charge profile
– 1- to 16-cell LiFePO 4 charge profile

- Synchronous buck-boost charge controller with
NFET drivers

–
Adjustable switching frequency from 200 kHz to
600 kHz

–
Optional synchronization to external clock

–
Integrated loop compensation with soft start

–
Optional gate driver supply input for optimized
efficiency

- Bidirectional converter operation (Reverse Mode)
supporting USB-PD Extended Power Range (EPR)

–
Adjustable input voltage (VAC) regulation from
3.3 V to 65 V with 20-mV/step

–
Adjustable input current regulation (R AC_SNS )
from 400 mA to 20 A with 50-mA/step using
5-mΩ resistor

- Direct power path management for highest
efficiency to power system

–
System power selection from adapter or battery

–
Dynamic power management
– All N-channel FET drivers

- High accuracy

–
±0.5% charge voltage regulation

–
±3% charge current regulation

–
±3% input current regulation

- I [2] C controlled for optimal system performance with
resistor-programmable option

–
Hardware adjustable input and output current
limits

- Integrated 16-bit ADC for voltage, current, and
temperature monitoring

- Low battery quiescent current

- High safety integration

–
Adjustable input overvoltage and undervoltage
protection

–
Battery overvoltage and overcurrent protection

–
Charging safety timer

–
Battery short protection
– Thermal shutdown

- Status outputs

–
Adapter present status (PG)

–
Charger operation status

- Package

–
36-pin 5 mm × 6 mm QFN



**2 Applications**


- [Cordless power and garden tools](https://www.ti.com/solution/cordless-power-tool)

- [Solar backup charger](https://www.ti.com/solution/solar-charge-controller)

- [Energy storage systems](https://www.ti.com/applications/industrial/grid-infrastructure/energy-storage-systems/overview.html)

- [Drone](https://www.ti.com/solution/battery-pack-non-military-drone)

- [Ultrasound](https://www.ti.com/solution/ultrasound-scanner)

- [X-ray systems](https://www.ti.com/solution/x-ray-systems)

- [Electronic hospital beds and bed control](https://www.ti.com/solution/electronic-hospital-bed-control)

- [Multiparameter patient monitors](https://www.ti.com/solution/multiparameter-patient-monitor)


**3 Description**


The BQ25750 is a wide input voltage, switched-mode
buck-boost Li-Ion, Li-polymer, or LiFePO 4 battery
charge controller with direct power path control.
The device offers high-efficiency battery charging
over a wide voltage range with accurate charge
current and charge voltage regulation, in addition to
automatic charge preconditioning, termination, and
charge status indication. The device integrates all
the loop compensation for the buck-boost converter,
thereby providing a high density solution with ease of
use. In reverse mode, the device draws power from
the battery and regulates the SYS terminal voltage.


**Package Information**






|PART<br>NUMBER|PACKAGE(1)|PACKAGE<br>SIZE(2)|BODY SIZE<br>(NOM)|
|---|---|---|---|
|BQ25750<br>|RRV (VQFN 36)<br>6<br>|.0 mm × 5.0<br>mm<br><br>|6.0 mm × 5.0<br>mm|



(1) For all available packages, see Section 14.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.



























|OPTIONAL|SYSTEM<br>+CSYS<br>OPTIONAL|Col3|Col4|Col5|
|---|---|---|---|---|
|ICHG<br>ACP<br>BATDRV<br>SRP<br>SRN<br>HIDRV2<br>LODRV2<br>HIDRV1<br>LODRV1<br>ACDRV<br>PGND<br>VAC<br>ACN<br>SW1<br>SW2<br>SYS<br>TS<br>Host<br>I2C<br>FB<br>ILIM_HIZ<br>BQ25750<br>REGN<br>BATSRC|ICHG<br>ACP<br>BATDRV<br>SRP<br>SRN<br>HIDRV2<br>LODRV2<br>HIDRV1<br>LODRV1<br>ACDRV<br>PGND<br>VAC<br>ACN<br>SW1<br>SW2<br>SYS<br>TS<br>Host<br>I2C<br>FB<br>ILIM_HIZ<br>BQ25750<br>REGN<br>BATSRC|||BATTERY|
|Host|Host|Host|Host|Host|
|Host|Host||||
|Host|Host||||


**Simplified Schematic**



An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table of Contents**



**1 Features** ............................................................................1

**2 Applications** ..................................................................... 1
**3 Description** .......................................................................1
**4 Description (continued)** .................................................. 3
**5 Device Comparison** ......................................................... 4
**6 Pin Configuration and Functions** ...................................5
**7 Specifications** .................................................................. 8

7.1 Absolute Maximum Ratings........................................ 8
7.2 ESD Ratings............................................................... 8
7.3 Recommended Operating Conditions.........................8
7.4 Thermal Information....................................................9

7.5 Electrical Characteristics...........................................10

7.6 Timing Requirements................................................ 16
7.7 Typical Characteristics (BQ25750)........................... 17
**8 Detailed Description** ......................................................20

8.1 Overview................................................................... 20

8.2 Functional Block Diagram......................................... 21
8.3 Feature Description...................................................22
8.4 Device Functional Modes..........................................38



8.5 BQ25750 Registers...................................................40
**9 Application and Implementation** .................................. 62

9.1 Application Information............................................. 62
9.2 Typical Applications.................................................. 62
**10 Power Supply Recommendations** ..............................73
**11 Layout** ........................................................................... 74

11.1 Layout Guidelines................................................... 74
11.2 Layout Example...................................................... 75
**12 Device and Documentation Support** ..........................77

12.1 Device Support....................................................... 77
12.2 Receiving Notification of Documentation Updates..77
12.3 Support Resources................................................. 77
12.4 Trademarks............................................................. 77
12.5 Electrostatic Discharge Caution..............................77
12.6 Glossary..................................................................77
**13 Revision History** .......................................................... 77
**14 Mechanical, Packaging, and Orderable**

**Information** .................................................................... 78



2 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**4 Description (continued)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



Besides the I [2] C host-controlled charging mode, the device also supports standalone charging mode via resistor
programmable limits. Input current, charge current and charge voltage regulation targets can be set via the
ILIM_HIZ, ICHG and FB pins, respectively.


The device has three status pins (STAT1, STAT2, and PG) to indicate the charging status and input voltage
status. These pins can be used to drive LEDs or communicate with a host processor. If needed, these pins can
also be used as general purpose indicators and their status controlled directly by the I2C interface. The INT pin
immediately notifies host when the device status changes, including faults.


The device also provides an analog-to-digital converter (ADC) for monitoring input current, charge current and
input/battery/system/thermistor voltages.


The device comes with a 36-pin 5.0 mm × 6.0 mm QFN package with 0.5 mm pin pitch.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 3


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**5 Device Comparison**

|PART NUMBER|BQ25750|BQ25756E|BQ25756|
|---|---|---|---|
|Key Feature|Li-Ion, LFP|Li-Ion, LFP|Li-Ion, LFP|
|Charger Topology|Buck-Boost|Buck-Boost|Buck-Boost|
|Power Topology|Direct Power-Path|Non Power-Path|Non Power-Path|
|I2C Address|0X6B|0X6A|0X6B|
|Default Charge Profile|Li-Ion (trickle, precharge, CC, CV)|Li-Ion (trickle, precharge, CC, CV)|Li-Ion (trickle, precharge, CC, CV)|
|Configuration|I2C + Standalone|I2C + Standalone|I2C + Standalone|
|Operating VIN|4.2V → 70V|4.2V → 36V|4.2V → 70V|
|Pin Count|36|36|36|
|Package|5X6 QFN|5X6 QFN|5X6 QFN|
|TS Pin Function|JEITA profile|JEITA profile|JEITA profile|



4 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**6 Pin Configuration and Functions**


FSW_ ACOV ACUV VAC SYS ACDRV ACP ACN
SYNC







**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


SW1


HIDRV1


BTST1


LODRV1


REGN


DRV_SUP


PGND


LODRV2


BTST2


HIDRV2



SCL


SDA


INT


STAT1


STAT2


PG


CE


TS


ICHG


ILIM_HIZ





BAT BAT
FBG FB SRN SRP
DRV SRC



PGND



SW2



**Figure 6-1. BQ25750, RRV Package 36-Pin VQFN Top View**


**Table 6-1. Pin Functions**






|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|
|SCL|1|I|**I2C Interface Clock –** Connect SCL to the logic rail through a 10-kΩ resistor.|
|SDA|2|IO|**I2C Interface Data –** Connect SDA to the logic rail through a 10-kΩ resistor.|
|~~INT~~|3|O|**Open Drain Interrupt Output –** Connect the~~INT~~ pin to a logic rail via 10-kΩ resistor. The~~INT~~ pin sends<br>an active low, 256-μs pulse to host to report the charger device status and faults.|
|STAT1|4|O|**Open Drain Charge Status 1 Output –** STAT1 and STAT2 indicate various charger operations, see<br>Table 8-6. Connect to the pull up rail via 10-kΩ resistor. The STAT1, STAT2 pin functions can be<br>disabled when DIS_STAT_PINS bit is set to 1. When disabled, this pin can be used as a general<br>purpose indicator via the FORCE_STAT1_ON bit.|
|STAT2|5|O|**Open Drain Charge Status 2 Output –** STAT1 and STAT2 indicate various charger operations, see<br>Table 8-6. Connect to the pull up rail via 10-kΩ resistor. The STAT1, STAT2 pin functions can be<br>disabled when DIS_STAT_PINS bit is set to 1. When disabled, this pin can be used as a general<br>purpose indicator via the FORCE_STAT2_ON bit.|
|~~PG~~|6|O|**Open Drain Active Low Power Good Indicator –** Connect to the pull up rail via 10-kΩ resistor. LOW<br>indicates a good input source if VAC is within the programmed ACUV / ACOV operating window. The<br>~~PG~~ pin function can be disabled when DIS_PG_PIN bit is set to 1. When disabled, this pin can be used<br>as a general purpose indicator via the FORCE_STAT3_ON bit.|
|~~CE~~|7|IO|**Active Low Charge Enable Pin –** Battery charging is enabled whenEN_CHG bit is 1 and~~CE~~ pin is<br>LOW.~~ CE~~pin must be pulled HIGH or LOW, do not leave floating. The~~CE~~pin function can be disabled<br>when DIS_CE_PIN bit is set to 1. When disabled, this pin can be used as a general purpose indicator<br>via the FORCE_STAT4_ON bit.|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 5


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 6-1. Pin Functions (continued)**



















|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|
|TS|8|I|**Temperature Qualification Voltage Input –** Connect a negative temperature coefficient thermistor.<br>Program temperature window with a resistor divider from REGN to TS to PGND. Charge suspends<br>when TS pin voltage is out of range. Recommend 103AT-2 10-kΩ thermistor.|
|ICHG|9|I|**Charge Current Limit Setting –** ICHG pin sets the maximum charge current, and can be used to<br>monitor the charge current. A programming resistor to PGND is used to set the charge current limit as<br>ICHG = KICHG / RICHG. When the device is under charge current regulation, the voltage at ICHG pin is<br>VREF_ICHG. When ICHG pin voltage is less than VREF_ICHG, the actual charge current can be calculated<br>as: IBAT = KICHG x VICHG / ( RICHG x VREF_ICHG). The actual charge current limit is the lower of the limits<br>set by ICHG pin or the ICHG_REG register bits. This pin function can be disabled when EN_ICHG_PIN<br>bit is 0. If ICHG pin is not used, this pin should be pulled to PGND, do not leave floating.|
|ILIM_HIZ|10|I|**Input Current Limit Setting and HIZ Mode Control Pin –** ILIM_HIZ pin sets the maximum input<br>current limit, can be used to monitor the input current and can be pulled HIGH to force device into<br>HIZ mode. A programming resistor to PGND is used to set the input current limit as ILIM = KILIM /<br>RILIM. When the device is under input current regulation, the voltage at ILIM_HIZ pin is VREF_ILIM. When<br>ILIM_HIZ pin voltage is less than VREF_ILIM, the actual input current can be calculated as: IAC = KILIM<br>x VILIM / ( RILIM x VREF_ILIM). The actual input current limit is the lower of the limits set by ILIM_HIZ<br>pin or the IAC_DPM register bits. This pin function can be disabled when EN_ILIM_HIZ_PIN bit is 0. If<br>ILIM_HIZ pin is not used, this pin should be pulled to PGND, do not leave floating.|
|FBG|11|I|**Voltage Feedback Divider Return –** Connect to the bottom of battery feedback resistor. When<br>charging, this pin is driven to PGND internally. When input voltage is outside of the ACUV / ACOV<br>operating window, this pin is high-impedance, minimizing battery leakage current.|
|FB|12|I|**Charge Voltage Analog Feedback Adjustment –** Connect the output of a resistive voltage divider<br>from the battery terminals to this node to adjust the output battery regulation voltage.|
|SRN|13|I|**Charge Current-Sense Resistor, Negative Input –** A 0.47-μF ceramic capacitor is placed from SRN to<br>SRP to provide differential-mode filtering. An optional 0.1-μF ceramic capacitor is placed from the SRN<br>pin to PGND for common-mode filtering.|
|SRP|14|I|**Charge Current-Sense Resistor, Positive Input –** A 0.47-μF ceramic capacitor is placed from SRN<br>to SRP to provide differential-mode filtering. A 0.1-μF ceramic capacitor is placed from the SRP pin to<br>PGND for common-mode filtering.|
|BATDRV|15|O|**N-Channel Battery FET Gate Drive –** Connect directly to the BATFET gate. Pin drives the gate with<br>10 V relative to BATSRC to turn on BATFET when the input voltage is outside of the ACUV / ACOV<br>operating window. An optional capacitor from BATDRV to BATSRC can be used to slow down the turn<br>on transition.|
|BATSRC|16|I|**N-Channel Battery FET Source –** Connect directly to the BATFETs common source.|
|PGND|17|I|Tie this pin directly to PGND.|
|SW2|18|P|**Boost Side Half Bridge Switching Node –** Connect to the source of boost HS FET and the drain of<br>boost LS FET. Connect the inductor between SW1 and SW2.|
|HIDRV2|19|O|**Boost Side High-Side Gate Driver –** Connect to the boost high-side N-channel MOSFET gate.|
|BTST2|20|P|**Boost Side High-Side Power MOSFET Gate Driver Power Supply –** Connect a capacitor between<br>BTST2 and SW2 to provide bias to the high-side MOSFET gate driver.|
|LODRV2|21|O|**Boost Side Low-Side Gate Driver –** Connect to the boost low-side N-channel MOSFET gate.|
|PGND|22|P|**Power Ground Return –** The high current ground connection for the low-side gate drivers.|
|DRV_SUP|23|P|**Charger Gate Drive Supply Input –** Voltage on this pin is used to drive the gates of buck-boost<br>converter switching FET. Connect a 4.7-μF ceramic capacitor from DRV_SUP to power ground. REGN<br>LDO voltage can be used as the gate driver supply for all switching FETs by connecting REGN to<br>DRV_SUP pin. In high-voltage applications, it is possible to directly provide the DRV_SUP voltage with<br>an external supply up to 12 V to achieve higher switching efficiency. SeeSection 8.3.3.2 for more<br>details.|
|REGN|24|P|**Charger Internal Linear Regulator Output –** Connect a 4.7-μF ceramic capacitor from REGN to<br>power ground. REGN LDO voltage can be used as the gate driver supply for all switching FETs by<br>connecting REGN to DRV_SUP pin. In high-voltage applications, it is possible to directly provide the<br>DRV_SUP voltage with an external supply up to 12 V to achieve higher switching efficiency. See<br>Section 8.3.3.2 for more details.|
|LODRV1|25|O|**Buck Side Low-Side Gate Driver –** Connect to the buck low-side N-channel MOSFET gate.|
|BTST1|26|P|**Buck Side High-Side Power MOSFET Gate Driver Power Supply –** Connect a capacitor between<br>BTST1 and SW1 to provide bias to the high-side MOSFET gate driver.|


6 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 6-1. Pin Functions (continued)**














|PIN|Col2|I/O|DESCRIPTION|
|---|---|---|---|
|**NAME**|**NO.**|**NO.**|**NO.**|
|HIDRV1|27|O|**Buck Side High-Side Gate Driver –** Connect to the buck high-side N-channel MOSFET gate.|
|SW1|28|P|**Buck Side Half Bridge Switching Node –** Connect to the source of buck HS FET and the drain of<br>buck LS FET. Connect the inductor between SW1 and SW2.|
|ACN|29|I|**Adapter Current-Sense Resistor, Negative Input –** A 0.47-μF ceramic capacitor is placed from ACN<br>to ACP to provide differential-mode filtering. An optional 0.1-μF ceramic capacitor is placed from the<br>ACN pin to PGND for common-mode filtering.|
|ACP|30|I|**Adapter Current-Sense Resistor, Positive Input –** A 0.47-μF ceramic capacitor is placed from ACN<br>to ACP to provide differential-mode filtering. A 0.1-μF ceramic capacitor is placed from the ACP pin to<br>PGND for common-mode filtering|
|ACDRV|31|O|**N-Channel Input FET Gate Drive –** Connect directly to the back-to-back input FETs (ACFETs) gates.<br>Pin drives the gate with 10V to turn on ACFETs when the input voltage is inside of the ACUV / ACOV<br>operating window. If input voltage is outside the valid operating window, this pin pulls to PGND to turn<br>off the FETs. Connect a 15-V Zener diode from ACDRV to the common source of the ACFETs.|
|SYS|32|I|**System voltage sense point –** Sense point for system voltage. If VAC is outside of the ACUV / ACOV<br>operating window, the BATFET will only turn on once the SYS voltage falls below battery voltage<br>(ideal-diode turn on). When Reverse Mode is enabled, this pin voltage is regulated to VSYS_REV.|
|VAC|33|P|**Input Voltage Detection and Power –** VAC is the input bias to power the IC. Connect a 1-µF capacitor<br>from pin to PGND.|
|ACUV|34|I|**Input Undervoltage Comparator –** Connect a resistor divider from VAC to PGND to program the<br>undervoltage protection. When this pin falls below VREF_ACUV, the device stops charging, disables<br>the ACFETs and enables the BATFET. The hardware limit for input voltage regulation reference is<br>VACUV_DPM. The actual input voltage regulation is the higher of the pin-programmed value and the<br>VAC_DPM register value. If ACUV programming is not used, pull this pin to VAC, do not leave floating.|
|ACOV|35|I|**Input Overvoltage Comparator –** Connect a resistor divider from VAC to PGND to program the<br>overvoltage protection. When this pin rises above VREF_ACOV, the device stops charging, disables the<br>ACFETs and enables the BATFET. If ACOV programming is not used, pull this pin to PGND, do not<br>leave floating.|
|FSW_SYNC|36|I|**Switching Frequency and Synchronization Input –** An external resistor is connected to the<br>FSW_SYNC pin and PGND to set the nominal switching frequency. This pin can also be used to<br>synchronize the PWM controller to an external clock with 200-kHz to 600-kHz frequency.|
|Thermal Pad|37|-|**Exposed pad beneath the IC –** Always solder the thermal pad to the board, and have vias on the<br>thermal pad plane star-connecting to PGND and ground plane for high-current power converter. It also<br>serves as a thermal pad to dissipate the heat.|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 7


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**7 Specifications**

**7.1 Absolute Maximum Ratings**


over operating free-air temperature range (unless otherwise noted) [(1)]

|Col1|Col2|MIN MAX|UNIT|
|---|---|---|---|
|Voltage|VAC, ACUV, ACOV, ACP, ACN, SYS, ACDRV, BATDRV, BATSRC,<br>SRP, SRN, FB, FBG|–0.3<br>85|V|
|Voltage|SW1, SW2|–2<br>85|V|
|Voltage|SW1, SW2 (40ns transient)|–4<br>85|V|
|Voltage|~~PG~~|–0.3<br>40|V|
|Voltage|BATDRV with respect to BATSRC|–0.3<br>12|V|
|Voltage|BTST1, HIDRV1 with respect to SW1|–0.3<br>14|V|
|Voltage|BTST2, HIDRV2 with respect to SW2|–0.3<br>14|V|
|Voltage|DRV_SUP, LODRV1, LODRV2|–0.3<br>14|V|
|Voltage|ACP with respect to ACN, SRP with respect to SRN|–0.3<br>0.3|V|
|Voltage|~~CE,~~ FSW_SYNC, ICHG, ILIM_HIZ,~~ INT~~, REGN, SCL, SDA, MODE,<br>STAT1, STAT2, TS|–0.3<br>6|V|
|Output Sink<br>Current|~~CE, PG~~, STAT1, STAT2|5|mA|
|TJ|Junction temperature|–40<br>150|°C|
|Tstg|Storage temperature|–65<br>150|°C|



(1) Stresses beyond those listed under _Absolute Maximum Rating_ may cause permanent damage to the device. These are stress
ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated
under _Recommended Operating Condition_ . Exposure to absolute-maximum-rated conditions for extended periods may affect device
reliability.


**7.2 ESD Ratings**






|Col1|Col2|Col3|VALUE|UNIT|
|---|---|---|---|---|
|V(ESD)|Electrostatic discharge|Human body model (HBM), per ANSI/ESDA/<br>JEDEC JS-001, all pins(1)|±2000|V|
|V(ESD)|Electrostatic discharge|Charged device model (CDM), per ANSI/ESDA/<br>JEDEC JS-002, all pins(2)|±500|±500|



(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.


**7.3 Recommended Operating Conditions**


over operating free-air temperature range (unless otherwise noted)

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VAC|Input voltage|4.2<br>70|V|
|VBAT|Battery voltage|0<br>70|V|
|VDRV_SUP|DRV_SUP pin direct drive voltage range|4.0<br>12|V|
|FSW|Switching Frequency|200<br>600|kHz|
|TJ|Junction temperature|–40<br>125|°C|
|TA|Ambient temperature|–40<br>105|°C|
|CVAC|VAC capacitor|1|µF|
|CIN|Buck-boost input capacitance (minimum value after derating)|160|µF|
|COUT|Buck-boost output capacitance (minimum value after derating)|160|µF|
|CREGN|REGN capacitor (nominal value before derating)|4.7|µF|
|CDRV_SUP|DRV_SUP capacitor (nominal value before derating)|4.7|µF|



8 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**7.3 Recommended Operating Conditions (continued)**


over operating free-air temperature range (unless otherwise noted)



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|L|Switched Inductor|2.2<br>15|µH|
|RDCR|Inductor DC resistance|1.75<br>60|mΩ|
|RAC_SNS|Input current sense resistor|0(1)<br>2<br>10|mΩ|
|RBAT_SNS|Battery current sense resistor|5|mΩ|
|RICHG|ICHG programming pulldown resistor|0.0(2)<br>100|kΩ|
|RILIM_HIZ|ILIM_HIZ programming pulldown resistor|0.0(3)<br>50|kΩ|


(1) When R AC_SNS is 0mΩ, input current limit function is disabled
(2) When R ICHG is pulled to GND, the hardware charge current limit is disabled, actual charge current is controlled by the ICHG_REG
register setting
(3) When R ILIM_HIZ is pulled to GND, the hardware input current limit is disabled, actual input current is controlled by the IAC_DPM register
setting


**7.4 Thermal Information**







|THERMAL METRIC(1)|Col2|BQ25750|UNIT|
|---|---|---|---|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**RRV**|**RRV**|
|**THERMAL METRIC**(1)|**THERMAL METRIC**(1)|**36 PINS**|**36 PINS**|
|RθJA|Junction-to-ambient thermal resistance (JEDEC(1))|29.4|°C/W|
|RθJC(top)|Junction-to-case (top) thermal resistance|18.8|°C/W|
|RθJB|Junction-to-board thermal resistance|9.9|°C/W|
|ΨJT|Junction-to-top characterization parameter|0.2|°C/W|
|ΨJB|Junction-to-board characterization parameter|9.8|°C/W|
|RθJC(bot)|Junction-to-case (bottom) thermal resistance|2.5|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
report.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 9


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics**


VAC = ACP = ACN = SYS = SRP = SRN = 28V, T J = -40°C to +125°C, and T J = 25°C for typical values (unless otherwise
noted)


































|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|**QUIESCENT CURRENTS**|**QUIESCENT CURRENTS**|**QUIESCENT CURRENTS**|**QUIESCENT CURRENTS**|**QUIESCENT CURRENTS**|
|ISD_BAT|Shutdown battery current with<br>BATFET off (ISRN + ISRP)|VBAT= 28V, VAC = 0V, ADC_EN = 0,<br>FORCE_BATFET_OFF = 1, TJ < 105 °C|10|µA|
|IQ_BAT|Quiescent battery current with<br>BATFET on (ISRN + ISRP)|VBAT= 28V, VAC = 0V, ADC_EN = 0, TJ <<br>105 °C|17|µA|
|IQ_BAT|Quiescent battery current with<br>BATFET on (ISRN + ISRP)|VBAT= 28V, VAC = 0V, ADC_EN = 1, TJ <<br>105 °C|500<br>700|µA|
|IHIZ_VAC|HIZ input current (IVAC)|EN_HIZ = 1|10<br>30|µA|
|IQ_VAC|Quiescent input current (IVAC)|Not switching|0.75<br>1|mA|
|IQ_REV|Quiescent battery current in Reverse<br>mode (ISRN + ISRP)|Not switching|0.75<br>1|mA|
|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|
|VVAC_OP|VAC operating range||4.2<br>70|V|
|VVAC_OK|VAC converter enable threshold|VAC rising, no battery|4.2|V|
|VVAC_OKZ|VAC converter disable threshold|VAC falling, no battery|3.5|V|
|VREF_ACUV|ACUV comparator threshold to enter<br>VAC_UVP|VACUV falling|1.095<br>1.1<br>1.106|V|
|VREF_ACUV_HYS|ACUV comparator threshold<br>hysteresis|VACUV rising|50|mV|
|VVAC_INT_OV|VAC internal threshold to enter<br>VAC_OVP|IN rising|72<br>74<br>76|V|
|VVAC_INT_OVZ|VAC internal thresholds to exit<br>VAC_OVP|IN falling|69<br>71<br>73|V|
|VREF_ACOV|ACOV comparator threshold to enter<br>VAC_OVP|VACOV rising|1.184<br>1.2<br>1.206|V|
|VREF_ACOV_HYS|ACOV comparator threshold<br>hysteresis|VACOV falling|50|mV|
|VSRN_OK|Battery voltage to enable BATFET|VSRN rising, no input|3.1|V|
|VSRN_OKZ|Battery voltage to disable BATFET|VSRN falling, no input|2.15<br>2.5|V|
|**CHARGE VOLTAGE REGULATION**|**CHARGE VOLTAGE REGULATION**|**CHARGE VOLTAGE REGULATION**|**CHARGE VOLTAGE REGULATION**|**CHARGE VOLTAGE REGULATION**|
|VVFB_RANGE|Feedback voltage range||1.504<br>1.566|V|
|VVFB_NOM|Nominal feedback voltage|VFB_REG = 0x10|1.536|V|
|VVFB_ACC|Feedback voltage regulation accuracy|TJ = 0°C to 85°C|–0.5<br>0.5|%|
|VVFB_ACC|Feedback voltage regulation accuracy|TJ = -40°C to 125°C|–0.7<br>0.7|%|
|RFBG|FBG resistance to PGND|IFBG = 1mA|33<br>55|Ω|
|**FAST CHARGECURRENT REGULATION**|**FAST CHARGECURRENT REGULATION**|**FAST CHARGECURRENT REGULATION**|**FAST CHARGECURRENT REGULATION**|**FAST CHARGECURRENT REGULATION**|
|ICHG_REG_RANGE|Charge current regulation range||0.4<br>20|A|
|ICHG_REG_ACC|I2C setting charge current regulation<br>accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ICHG_REG = 0x012C|15|A|
|ICHG_REG_ACC|I2C setting charge current regulation<br>accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ICHG_REG = 0x012C|–3<br>3|%|
|ICHG_REG_ACC|I2C setting charge current regulation<br>accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ICHG_REG = 0x0064|5|A|
|ICHG_REG_ACC|I2C setting charge current regulation<br>accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ICHG_REG = 0x0064|–3<br>3|%|
|ICHG_REG_ACC|I2C setting charge current regulation<br>accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ICHG_REG = 0x0028|2|A|
|ICHG_REG_ACC|I2C setting charge current regulation<br>accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ICHG_REG = 0x0028|–5<br>5|%|
|KICHG|Hardware charge current limit set<br>factor (Amperes of charge current per<br>kΩ on ICHG pin)|RBAT_SNS = 5mΩ, RICHG = 10kΩ, 5kΩ, and<br>3.33kΩ|48<br>50<br>52|A x<br>kΩ|



10 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics (continued)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



VAC = ACP = ACN = SYS = SRP = SRN = 28V, T J = -40°C to +125°C, and T J = 25°C for typical values (unless otherwise
noted)


















































|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|VREF_ICHG|ICHG pin voltage when ICHG pin is in<br>regulation||2.0|V|
|**PRE-CHARGE CURRENT REGULATION**|**PRE-CHARGE CURRENT REGULATION**|**PRE-CHARGE CURRENT REGULATION**|**PRE-CHARGE CURRENT REGULATION**|**PRE-CHARGE CURRENT REGULATION**|
|IPRECHG_RANGE|Precharge current regulation range|VFB < VBAT_LOWV * VVFB_REG|0.25<br>10|A|
|IPRECHG_ACC|I2C setting precharge current<br>accuracy|RBAT_SNS = 5mΩ, VFB < VBAT_LOWV *<br>VVFB_REG. IPRECHG = 0x003C|3.0|A|
|IPRECHG_ACC|I2C setting precharge current<br>accuracy|RBAT_SNS = 5mΩ, VFB < VBAT_LOWV *<br>VVFB_REG. IPRECHG = 0x003C|–4<br>4|%|
|IPRECHG_ACC|I2C setting precharge current<br>accuracy|RBAT_SNS = 5mΩ, VFB < VBAT_LOWV *<br>VVFB_REG. IPRECHG[1:0] = 0x0014|1.0|A|
|IPRECHG_ACC|I2C setting precharge current<br>accuracy|RBAT_SNS = 5mΩ, VFB < VBAT_LOWV *<br>VVFB_REG. IPRECHG[1:0] = 0x0014|–10<br>10|%|
|IPRECHG_ACC|I2C setting precharge current<br>accuracy|RBAT_SNS = 5mΩ, VFB < VBAT_LOWV *<br>VVFB_REG. IPRECHG[1:0] = 0x000A|0.50|A|
|IPRECHG_ACC|I2C setting precharge current<br>accuracy|RBAT_SNS = 5mΩ, VFB < VBAT_LOWV *<br>VVFB_REG. IPRECHG[1:0] = 0x000A|–30<br>30|%|
|**CHARGE TERMINATION**|**CHARGE TERMINATION**|**CHARGE TERMINATION**|**CHARGE TERMINATION**|**CHARGE TERMINATION**|
|ITERM_RANGE|Termination current range|VFB = VVFB_REG|0.25<br>10|A|
|ITERM_ACC|Termination current accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V,<br>55V. ITERM = 0x001E|1.5|A|
|ITERM_ACC|Termination current accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V,<br>55V. ITERM = 0x001E|–7<br>7|%|
|ITERM_ACC|Termination current accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ITERM = 0x000A|0.50|A|
|ITERM_ACC|Termination current accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ITERM = 0x000A|–20<br>20|%|
|ITERM_ACC|Termination current accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ITERM = 0x0005|0.250|A|
|ITERM_ACC|Termination current accuracy|RBAT_SNS = 5mΩ, VBAT = 12V, 36V, 55V.<br>ITERM = 0x0005|–50<br>50|%|
|**BATTERY VOLTAGE COMPARATORS**|**BATTERY VOLTAGE COMPARATORS**|**BATTERY VOLTAGE COMPARATORS**|**BATTERY VOLTAGE COMPARATORS**|**BATTERY VOLTAGE COMPARATORS**|
|VBAT_SHORT|Trickle charge to pre-charge transition|VSRN rising|2.8<br>3<br>3.2|V|
|VBAT_SHORT|Pre-charge to trickle charge transition|VSRN falling|2.2<br>2.4<br>2.6|V|
|VBAT_LOWV|Pre-charge to fast-charge transition|VFB rising, as percentage of VFB_REG, <br>VBAT_LOWV[2:0] = 3|69.0<br>71.7<br>73.8|%|
|VBAT_LOWV|Pre-charge to fast-charge transition|VFB rising, as percentage of VFB_REG, <br>VBAT_LOWV[2:0] = 2|64.3<br>66.7<br>69.0|%|
|VBAT_LOWV|Pre-charge to fast-charge transition|VFB rising, as percentage of VFB_REG, <br>VBAT_LOWV[2:0] = 1|52<br>55<br>58|%|
|VBAT_LOWV|Pre-charge to fast-charge transition|VFB rising, as percentage of VFB_REG, <br>VBAT_LOWV[2:0] = 0|27<br>30<br>33|%|
|VBAT_LOWV_HYS|BAT_LOWV hysteresis||5|%|
|VRECHG|Battery recharge threshold for Li-Ion<br>and LiFePO4|VFB falling, as percentage of VFB_REG, <br>VRECHG[1:0] = 3|97.6|%|
|VRECHG|Battery recharge threshold for Li-Ion<br>and LiFePO4|VFB falling, as percentage of VFB_REG, <br>VRECHG[1:0] = 2|95.2|%|
|VRECHG|Battery recharge threshold for Li-Ion<br>and LiFePO4|VFB falling, as percentage of VFB_REG, <br>VRECHG[1:0] = 1|94.3|%|
|VRECHG|Battery recharge threshold for Li-Ion<br>and LiFePO4|VFB falling, as percentage of VFB_REG, <br>VRECHG[1:0] = 0|93.0|%|
|**INPUT CURRENT REGULATION**|**INPUT CURRENT REGULATION**|**INPUT CURRENT REGULATION**|**INPUT CURRENT REGULATION**|**INPUT CURRENT REGULATION**|
|IIREG_DPM_ACC|I2C setting input current regulation<br>accuracy in forward mode|RAC_SNS = 2mΩ, IAC_DPM = 0x00A0|20|A|
|IIREG_DPM_ACC|I2C setting input current regulation<br>accuracy in forward mode|RAC_SNS = 2mΩ, IAC_DPM = 0x00A0|–3<br>3|%|
|IIREG_DPM_ACC|I2C setting input current regulation<br>accuracy in forward mode|RAC_SNS = 2mΩ, IAC_DPM = 0x0050|10|A|
|IIREG_DPM_ACC|I2C setting input current regulation<br>accuracy in forward mode|RAC_SNS = 2mΩ, IAC_DPM = 0x0050|–4<br>4|%|
|IIREG_DPM_ACC|I2C setting input current regulation<br>accuracy in forward mode|RAC_SNS = 2mΩ, IAC_DPM = 0x0028|5.0|A|
|IIREG_DPM_ACC|I2C setting input current regulation<br>accuracy in forward mode|RAC_SNS = 2mΩ, IAC_DPM = 0x0028|–7<br>7|%|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 11


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics (continued)**


VAC = ACP = ACN = SYS = SRP = SRN = 28V, T J = -40°C to +125°C, and T J = 25°C for typical values (unless otherwise
noted)






























|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|KILIM|Hardware input current limit set factor<br>(Amperes of input current per kΩ on<br>ILIM_HIZ pin)|RAC_SNS = 2mΩ, RILIM = 5kΩ, 2.5kΩ, and<br>1.67kΩ|48<br>50<br>52|A x<br>kΩ|
|VREF_ILIM_HIZ|ILIM_HIZ pin voltage when ILIM_HIZ<br>pin is in regulation||2.0|V|
|VIH_ILIM_HIZ|ILIM_HIZ input high threshold to enter<br>HIZ mode|VILIM_HIZ rising|3.7|V|
|**INPUT VOLTAGE REGULATION**|**INPUT VOLTAGE REGULATION**|**INPUT VOLTAGE REGULATION**|**INPUT VOLTAGE REGULATION**|**INPUT VOLTAGE REGULATION**|
|VVREG_DPM_RANGE|Input voltage DPM regulation range||4.2<br>65|V|
|VVREG_DPM_ACC|I2C setting input voltage regulation<br>accuracy|VAC_DPM = 0x076C|38|V|
|VVREG_DPM_ACC|I2C setting input voltage regulation<br>accuracy|VAC_DPM = 0x076C|–2<br>2|%|
|VVREG_DPM_ACC|I2C setting input voltage regulation<br>accuracy in forward mode|VAC_DPM = 0x04E2|25|V|
|VVREG_DPM_ACC|I2C setting input voltage regulation<br>accuracy in forward mode|VAC_DPM = 0x04E2|–2<br>2|%|
|VVREG_DPM_ACC|I2C setting input voltage regulation<br>accuracy in forward mode|VAC_DPM = 0x03B6|19|V|
|VVREG_DPM_ACC|I2C setting input voltage regulation<br>accuracy in forward mode|VAC_DPM = 0x03B6|–2<br>2|%|
|VACUV_DPM|ACUV pin voltage when in VDPM<br>regulation||1.198<br>1.210<br>1.222|V|
|**REVERSE MODE VOLTAGE REGULATION**|**REVERSE MODE VOLTAGE REGULATION**|**REVERSE MODE VOLTAGE REGULATION**|**REVERSE MODE VOLTAGE REGULATION**|**REVERSE MODE VOLTAGE REGULATION**|
|VREV_RANGE|SYS Voltage regulation range in<br>Reverse mode||3.3<br>65|V|
|VREV_ACC|Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x0960|48|V|
|VREV_ACC|Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x0960|–2<br>2|%|
|VREV_ACC|Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x0578|28|V|
|VREV_ACC|Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x0578|–2<br>2|%|
|VREV_ACC|VAC Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x02EE|15|V|
|VREV_ACC|VAC Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x02EE|–2<br>2|%|
|VREV_ACC|VAC Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x00FA|5|V|
|VREV_ACC|VAC Voltage regulation accuracy in<br>Reverse mode|VSYS_REV = 0x00FA|–2<br>2|%|
|**REVERSE MODE CURRENT REGULATION**|**REVERSE MODE CURRENT REGULATION**|**REVERSE MODE CURRENT REGULATION**|**REVERSE MODE CURRENT REGULATION**|**REVERSE MODE CURRENT REGULATION**|
|IIREV_ACC|Input current regulation accuracy in<br>Reverse mode|RAC_SNS = 2mΩ, IAC_REV = 0x00A0|20|A|
|IIREV_ACC|Input current regulation accuracy in<br>Reverse mode|RAC_SNS = 2mΩ, IAC_REV = 0x00A0|–3.5<br>3.5|%|
|IIREV_ACC|Input current regulation accuracy in<br>Reverse mode|RAC_SNS = 2mΩ, IAC_REV = 0x0028|5.0|A|
|IIREV_ACC|Input current regulation accuracy in<br>Reverse mode|RAC_SNS = 2mΩ, IAC_REV = 0x0028|–5.5<br>5.5|%|
|**CHARGE MODE BATTERY-PACK NTC MONITOR**|**CHARGE MODE BATTERY-PACK NTC MONITOR**|**CHARGE MODE BATTERY-PACK NTC MONITOR**|**CHARGE MODE BATTERY-PACK NTC MONITOR**|**CHARGE MODE BATTERY-PACK NTC MONITOR**|
|VT1_RISE|TS pin voltage rising T1 threshold,<br>charge suspended above this voltage.|As Percentage to REGN, TS_T1=0°C w/<br>103AT|72.75<br>73.25<br>73.85|%|
|VT1_FALL|TS pin voltage falling T1 threshold,<br>charge re-enabled below this voltage.|As Percentage to REGN, TS_T1=0°C w/<br>103AT|71.5<br>72<br>72.5|%|
|VT2_RISE|TS pin voltage rising T2 threshold,<br>charge back to reduced ICHG above<br>this voltage|As Percentage to REGN, TS_T2=10°C w/<br>103AT|67.75<br>68.25<br>68.75|%|
|VT2_FALL|TS pin voltage falling T2 threshold.<br>Charge back to normal below this<br>voltage|As Percentage to REGN, TS_T2=10°C w/<br>103AT|66.45<br>66.95<br>67.45|%|
|VT3_FALL|TS pin voltage falling T3 threshold,<br>charge to ICHG and reduced VFB_REG<br>below this voltage.|As Percentage to REGN, TS_T3=45°C w/<br>103AT|44.25<br>44.75<br>45.25|%|



12 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics (continued)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



VAC = ACP = ACN = SYS = SRP = SRN = 28V, T J = -40°C to +125°C, and T J = 25°C for typical values (unless otherwise
noted)








































|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|VT3_RISE|TS pin voltage rising T3 threshold.<br>Charge back to normal above this<br>voltage.|As Percentage to REGN, TS_T3=45°C w/<br>103AT|45.55<br>46.05<br>46.55|%|
|VT5_FALL|TS pin voltage falling T5 threshold,<br>charge suspended below this voltage|As Percentage to REGN, TS_T5=60°C w/<br>103AT|33.875<br>34.375<br>34.875|%|
|VT5_RISE|TS pin voltage rising T5 threshold.<br>Charge back to ICHG and reduced<br>VFB_REG above this voltage.|As Percentage to REGN, TS_T5=60°C w/<br>103AT|35<br>35.5<br>36|%|
|**REVERSE MODE BATTERY-PACK NTC MONITOR**|**REVERSE MODE BATTERY-PACK NTC MONITOR**|**REVERSE MODE BATTERY-PACK NTC MONITOR**|**REVERSE MODE BATTERY-PACK NTC MONITOR**|**REVERSE MODE BATTERY-PACK NTC MONITOR**|
|VBCOLD_RISE|TS pin voltage rising TCOLD<br>threshold. Reverse mode suspended<br>above this voltage|As Percentage to REGN (BCOLD = –20°C<br>w/ 103AT)|79.45<br>80.0<br>80.55|%|
|VBCOLD_RISE|TS pin voltage rising TCOLD<br>threshold. Reverse mode suspended<br>above this voltage|As Percentage to REGN (BCOLD = –10°C<br>w/ 103AT)|76.65<br>77.15<br>77.65|%|
|VBCOLD_FALL|TCOLD comparator falling threshold.|As Percentage to REGN (–20°C w/ 103AT)|78.2<br>78.7<br>79.2|%|
|VBCOLD_FALL|TCOLD comparator falling threshold.|As Percentage to REGN (–10°C w/ 103AT)|75.5<br>75.6<br>76.5|%|
|VBHOT_FALL|TS pin voltage falling THOT<br>threshold. Reverse mode suspends<br>below this voltage|As Percentage to REGN, (BHOT = 55°C w/<br>103AT)|37.2<br>37.7<br>38.2|%|
|VBHOT_FALL|TS pin voltage falling THOT<br>threshold. Reverse mode suspends<br>below this voltage|As Percentage to REGN, (BHOT = 60°C w/<br>103AT)|33.875<br>34.375<br>34.875|%|
|VBHOT_FALL|TS pin voltage falling THOT<br>threshold. Reverse mode suspends<br>below this voltage|As Percentage to REGN, (BHOT 65°C w/<br>103AT)|30.75<br>31.25<br>31.75|%|
|VBHOT_RISE|TS pin voltage rising THOT threshold.<br>Reverse mode allowed above this<br>voltage|As Percentage to REGN, (BHOT = 55°C w/<br>103AT)|38.5<br>39.0<br>39.95|%|
|VBHOT_RISE|TS pin voltage rising THOT threshold.<br>Reverse mode allowed above this<br>voltage|As Percentage to REGN, (BHOT = 60°C w/<br>103AT)|35<br>35.5<br>36|%|
|VBHOT_RISE|TS pin voltage rising THOT threshold.<br>Reverse mode allowed above this<br>voltage|As Percentage to REGN, (BHOT 65°C w/<br>103AT)|32.0<br>32.5<br>33.0|%|
|**BATTERY CHARGER PROTECTION**|**BATTERY CHARGER PROTECTION**|**BATTERY CHARGER PROTECTION**|**BATTERY CHARGER PROTECTION**|**BATTERY CHARGER PROTECTION**|
|VBAT_OV|Battery overvoltage threshold|VFB rising, as percentage of VFB_REG|102.5<br>104<br>105.5|%|
|VBAT_OVZ|Battery overvoltage falling threshold|VFB falling, as percentage of VFB_REG|100.5<br>102<br>103.5|%|
|VICHG_OC|Battery charge over-current threshold|VSRP- VSRN rising|120<br>170|mV|
|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|**THERMAL SHUTDOWN**|
|TSHUT|Thermal shutdown rising threshold|Temperature increasing|150|°C|
|TSHUT|Thermal shutdown falling threshold|Temperature decreasing|135|°C|
|**REGN REGULATOR AND GATE DRIVE SUPPLY (DRV_SUP)**|**REGN REGULATOR AND GATE DRIVE SUPPLY (DRV_SUP)**|**REGN REGULATOR AND GATE DRIVE SUPPLY (DRV_SUP)**|**REGN REGULATOR AND GATE DRIVE SUPPLY (DRV_SUP)**|**REGN REGULATOR AND GATE DRIVE SUPPLY (DRV_SUP)**|
|VREGN|REGN LDO output voltage|IREGN = 20mA|4.8<br>5<br>5.2|V|
|VREGN|REGN LDO output voltage|VAC = 5V, IREGN = 20mA|4.35<br>4.6|V|
|IREGN|REGN LDO current limit|VREGN = 4.5V|70|mA|
|VREGN_OK|REGN OK threshold to allow<br>switching|REGN rising|3.55|V|
|VDRV_UVPZ|DRV_SUP under-voltage threshold to<br>allow switching|DRV_SUP rising|3.7|V|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 13


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics (continued)**


VAC = ACP = ACN = SYS = SRP = SRN = 28V, T J = -40°C to +125°C, and T J = 25°C for typical values (unless otherwise
noted)
































|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|VDRV_OVP|DRV_SUP over-voltage threshold to<br>disable switching|DRV_SUP rising|12.8<br>13.2<br>13.6|V|
|**POWER-PATH MANAGER**|**POWER-PATH MANAGER**|**POWER-PATH MANAGER**|**POWER-PATH MANAGER**|**POWER-PATH MANAGER**|
|VACDRV_REG|ACFET drive voltage|VACDRV - VVAC, IACDRV = 10µA|10|V|
|IACDRV_ON|ACFET charge pump current limit|VACDRV - VVAC = 5V|40|µA|
|IACDRV_OFF|ACFET turnoff current||3|mA|
|VBATDRV_REG|BATFET drive voltage|VBATDRV - VBATSRC, VAC = 0V, IBATDRV =<br>10µA|10|V|
|IBATDRV_REG|BATFET charge pump current limit|VBATDRV - VBATSRC = 5V, VAC = 0V|40|µA|
|IBATDRV_OFF|BATFET turnoff current||400|µA|
|IAC_LOAD|VAC discharge load current||16|mA|
|IBAT_LOAD|Battery (SRN) discharge load current||16|mA|
|**SWITCHING FREQUENCY AND SYNC**|**SWITCHING FREQUENCY AND SYNC**|**SWITCHING FREQUENCY AND SYNC**|**SWITCHING FREQUENCY AND SYNC**|**SWITCHING FREQUENCY AND SYNC**|
|fSW|Switching Frequency|RFSW_SYNC = 133kΩ|212<br>250<br>288|kHz|
|fSW|Switching Frequency|RFSW_SYNC = 50kΩ|425<br>500<br>575|kHz|
|VIH_SYNC|FSW_SYNC input high threshold||1.3|V|
|VIL_SYNC|FSW_SYNC input low threshold||0.4|V|
|PWSYNC|FSW_SYNC input pulse width||80|ns|
|**PWM DRIVERS**|**PWM DRIVERS**|**PWM DRIVERS**|**PWM DRIVERS**|**PWM DRIVERS**|
|RHIDRV1_ON|Buck side high-side turnon resistance|VBTST1 - VSW1 = 5V|3.4|Ω|
|RHIDRV1_OFF|Buck side high-side turnoff resistance|VBTST1 - VSW1 = 5V|1.0|Ω|
|VBTST1_REFRESH|Bootstrap refresh comparator<br>threshold voltage|BTST1 falling, VBTST1 - VSW1 when low-side<br>refresh pulse is requested|2.7<br>3.1<br>3.9|V|
|RLODRV1_ON|Buck side low-side turnon resistance|VREGN = 5V|3.4|Ω|
|RLODRV1_OFF|Buck side low-side turnoff resistance|VREGN = 5V|1.0|Ω|
|tDT1|Buck side dead time, both edges||45|ns|
|RHIDRV2_ON|Boost side high-side turnon<br>resistance|VBTST2 - VSW2 = 5V|3.4|Ω|
|RHIDRV2_OFF|Boost side high-side turnoff<br>resistance|VBTST2 - VSW2 = 5V|1.0|Ω|
|VBTST2_REFRESH|Bootstrap refresh comparator<br>threshold voltage|BTST2 falling, VBTST2 - VSW2when low-side<br>refresh pulse is requested|2.7<br>3.1<br>3.9|V|
|RLODRV2_ON|Boost side low-side turnon resistance|VREGN = 5V|3.4|Ω|
|RLODRV2_OFF|Boost side low-side turnoff resistance|VREGN = 5V|1.0|Ω|
|tDT2|Boost side dead time, both edges||45|ns|
|**ANALOG-TO-DIGITAL CONVERTER (ADC)**|**ANALOG-TO-DIGITAL CONVERTER (ADC)**|**ANALOG-TO-DIGITAL CONVERTER (ADC)**|**ANALOG-TO-DIGITAL CONVERTER (ADC)**|**ANALOG-TO-DIGITAL CONVERTER (ADC)**|
|tADC_CONV|Conversion-time, each measurement|ADC_SAMPLE[1:0] = 00|24|ms|
|tADC_CONV|Conversion-time, each measurement|ADC_SAMPLE[1:0] = 01|12|ms|
|tADC_CONV|Conversion-time, each measurement|ADC_SAMPLE[1:0] = 10|6|ms|
|ADCRES|Effective resolution|ADC_SAMPLE[1:0] = 00|14<br>15|bits|
|ADCRES|Effective resolution|ADC_SAMPLE[1:0] = 01|13<br>14|bits|
|ADCRES|Effective resolution|ADC_SAMPLE[1:0] = 10|12<br>13|bits|
|**ADC MEASUREMENT RANGE AND LSB**|**ADC MEASUREMENT RANGE AND LSB**|**ADC MEASUREMENT RANGE AND LSB**|**ADC MEASUREMENT RANGE AND LSB**|**ADC MEASUREMENT RANGE AND LSB**|
|IAC_ADC|Input current ADC reading (positive or<br>negative)|Range with 2mΩ RAC_SNS|–50000<br>50000|mA|
|IAC_ADC|Input current ADC reading (positive or<br>negative)|LSB with 2mΩ RAC_SNS|2|mA|



14 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**7.5 Electrical Characteristics (continued)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



VAC = ACP = ACN = SYS = SRP = SRN = 28V, T J = -40°C to +125°C, and T J = 25°C for typical values (unless otherwise
noted)







|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|IBAT_ADC|Battery current ADC reading (positive<br>or negative)|Range with 5mΩ RBAT_SNS|–20000<br>20000|mA|
|IBAT_ADC|Battery current ADC reading (positive<br>or negative)|LSB with 5mΩ RBAT_SNS|2|mA|
|VAC_ADC|Input voltage ADC reading|Range|0<br>65534|mV|
|VAC_ADC|Input voltage ADC reading|LSB|2|mV|
|VBAT_ADC|Battery voltage ADC reading|Range|0<br>65534|mV|
|VBAT_ADC|Battery voltage ADC reading|LSB|2|mV|
|VSYS_ADC|System voltage ADC reading|Range|0<br>65534|mV|
|VSYS_ADC|System voltage ADC reading|LSB|2|mV|
|TSADC|TS voltage ADC reading, as<br>percentage of REGN|Range|0<br>99.9|%|
|TSADC|TS voltage ADC reading, as<br>percentage of REGN|LSB|0.098|%|
|VFB_ADC|FB voltage ADC reading|Range|0<br>2047|mV|
|VFB_ADC|FB voltage ADC reading|LSB|1|mV|
|**I2C INTERFACE (SCL, SDA)**|**I2C INTERFACE (SCL, SDA)**|**I2C INTERFACE (SCL, SDA)**|**I2C INTERFACE (SCL, SDA)**|**I2C INTERFACE (SCL, SDA)**|
|VIH|Input high threshold level||1.3|V|
|VIL|Input low threshold level||0.4|V|
|VOL|Output low threshold level|Sink current = 5mA|0.4|V|
|IIN_BIAS|High-level leakage current|Pull up rail 3.3V|1|µA|
|**LOGIC I/O PIN**~~**(CE**~~**,**~~** PG**~~**, STAT1, STAT2)**|**LOGIC I/O PIN**~~**(CE**~~**,**~~** PG**~~**, STAT1, STAT2)**|**LOGIC I/O PIN**~~**(CE**~~**,**~~** PG**~~**, STAT1, STAT2)**|**LOGIC I/O PIN**~~**(CE**~~**,**~~** PG**~~**, STAT1, STAT2)**|**LOGIC I/O PIN**~~**(CE**~~**,**~~** PG**~~**, STAT1, STAT2)**|
|VIH|Input high threshold level (~~CE~~)||1.3|V|
|VOL|Output low threshold level (~~CE,~~ ~~PG~~, <br>STAT1, STAT2)|Sink current = 5mA|0.4|V|
|VIL|Input low threshold level (~~CE~~)||0.4|V|
|IOUT_BIAS|High-level leakage current (~~CE, PG~~, <br>STAT1, STAT2)|Pull up rail 3.3V|1|µA|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 15


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**7.6 Timing Requirements**







|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|**VAC / BAT POWER UP**|
|tACOV_DGL|Enter ACOV deglitch time, ACOV rising|100|µs|
|tACOVZ_DGL|Exit ACOV deglitch time, ACOV falling|12|ms|
|tACUV_DGL|Enter ACUV deglitch time, ACUV falling|100|µs|
|tACUVZ_DGL|Exit ACUV deglitch time, ACUV rising|12|ms|
|**BATTERY CHARGER**|**BATTERY CHARGER**|**BATTERY CHARGER**|**BATTERY CHARGER**|
|tTERM_DGL|Deglitch time for charge termination, VSRP - VSRN<br>falling|220|ms|
|tRECHG_DGL|Deglitch time for recharge threshold, VFB falling|200|ms|
|tPRECHG|Pre-charge safety timer accuracy|1.7<br>2<br>2.3|hr|
|tSAFETY|Fast-charge safety timer accuracy, CHG_TMR = 8hr|6.8<br>8<br>9.2|hr|
|tTOPOFF|Top-off timer accuracy, TOPOFF_TMR = 30 min|25.5<br>30<br>34.5|min|
|tCV_TIMER|CV timer accuracy, CV_TMR = 10hr|8.5<br>10<br>11.5|hr|
|**BATTERY-PACK NTC MONITOR**|**BATTERY-PACK NTC MONITOR**|**BATTERY-PACK NTC MONITOR**|**BATTERY-PACK NTC MONITOR**|
|tTS_DGL|Deglitch time for TS threshold crossing|25|ms|
|**MPPT TIMERS**|**MPPT TIMERS**|**MPPT TIMERS**|**MPPT TIMERS**|
|tFULL_SWEEP|Full Panel Sweep timer accuracy, FULL_SWEEP_TMR<br>= 10 min|8.5<br>10<br>11.5|min|
|**I2C INTERFACE**|**I2C INTERFACE**|**I2C INTERFACE**|**I2C INTERFACE**|
|fSCL|SCL clock frequency|1000|kHZ|
|**DIGITAL CLOCK AND WATCHDOG**|**DIGITAL CLOCK AND WATCHDOG**|**DIGITAL CLOCK AND WATCHDOG**|**DIGITAL CLOCK AND WATCHDOG**|
|tLP_WDT|I2C Watchdog reset time (EN_HIZ = 1,<br>WATCHDOG[1:0] = 160s)|100<br>160|s|
|tWDT|I2C Watchdog reset time (EN_HIZ = 0,<br>WATCHDOG[1:0] = 160s)|130<br>160|s|


16 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**7.7 Typical Characteristics (BQ25750)**


C VAC = 160 µF, C OUT = 160 µF, _f_ _SW_ = 250 kHz, L = 10 μH, T A = 25°C (unless otherwise specified)



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||||||~~5V~~|
|||||||||~~IN~~<br>15VIN<br>|
|||||||||~~20V~~IN<br>24VIN<br>|
|||||||||36VIN<br>48V|
|||||||||~~IN~~<br>60VIN|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
|||||||||||~~V~~|
|||||||||||~~IN~~<br>15VIN<br>|
|||||||||||~~0V~~IN<br>24VIN<br>|
|||||||||||6VIN<br>8V|
|||||||||||~~IN~~<br>60VIN|














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
|||||||||~~5V~~|
|||||||||~~IN~~<br>15VIN<br>|
|||||||||~~20V~~IN<br>24VIN<br>|
|||||||||36VIN<br>48V~~IN~~|
|||||||||60VIN|


|Col1|Col2|Col3|Col4|Col5|Col6|20Vin,|29.2Vb|at|
|---|---|---|---|---|---|---|---|---|
|||||||~~28Vin,~~<br>36Vin,|~~29.2Vb~~<br>29.2Vb|~~at~~<br>t|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||



|100<br>98<br>96<br>94<br>(%)<br>92<br>Efficiency<br>90<br>88 5VIN<br>15VIN<br>86 20VIN<br>24VIN<br>84<br>36VIN<br>82 48VIN<br>60VIN<br>80<br>0 2 4 6 8 10 12 14<br>Charging Current (A)<br>VBAT = 20 V<br>Figure 7-1. Charge Efficiency vs Charge Current (5s battery<br>configuration)|100<br>98<br>96<br>94<br>(%)<br>92<br>Efficiency<br>90<br>88 5VIN<br>15VIN<br>86 20VIN<br>24VIN<br>84<br>36VIN<br>82 48VIN<br>60VIN<br>80<br>0 1 2 3 4 5 6 7 8 9 10<br>Charging Current (A)<br>VBAT = 28 V<br>Figure 7-2. Charge Efficiency vs Charge Current (7s battery<br>configuration)|
|---|---|
|Charging Current (A)<br>Efficiency (%)<br>0.5<br>1<br>1.5<br>2<br>2.5<br>3<br>3.5<br>4<br>4.5<br>5<br>80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br>98<br>100<br>~~5VIN~~<br>15VIN<br>~~20V~~IN<br>24VIN<br>36VIN<br>48V~~IN~~<br>60VIN<br>VBAT = 38 V<br>**Figure 7-3. Charge Efficiency vs Charge Current (10s battery**<br>**configuration)**|Temperature (C)<br>Accuracy (%)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>-0.5<br>-0.4<br>-0.3<br>-0.2<br>-0.1<br>0<br>0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>20Vin, 29.2Vbat<br>~~28Vin, 29.2Vbat~~<br>36Vin, 29.2Vbat<br>**Figure 7-4. Charge Voltage Accuracy vs Temperature**|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 17


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**7.7 Typical Characteristics (BQ25750) (continued)**


C VAC = 160 µF, C OUT = 160 µF, _f_ _SW_ = 250 kHz, L = 10 μH, T A = 25°C (unless otherwise specified)










|Col1|Col2|Col3|Col4|Col5|Col6|Col7|20Vin|, 27Vba|t|
|---|---|---|---|---|---|---|---|---|---|
||||||||~~28Vi~~<br>36Vi|~~, 27Vba~~<br>, 27Vb|~~t~~<br>t|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||


|IQ_BAT|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|~~IQ_VAC~~||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||












|Col1|Col2|Col3|Col4|Col5|Col6|Col7|VINP<br>VINP|M = 19<br>M = 34|V<br>V|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|20Vin|, 28Vba|t|
|---|---|---|---|---|---|---|---|---|---|
||||||||~~28Vin~~<br>36Vin|~~, 28Vba~~<br>, 28Vb|~~t~~<br>t|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||||||||||5V<br>|SYS_<br>|REV<br>|
||||||||||~~9V~~<br>15<br>|SYS_<br>VSYS<br>|REV<br>_REV<br>|
||||||||||20<br>36|VSYS<br>V|_REV<br>|
||||||||||48|~~SYS~~<br>VSYS|~~_REV~~<br>_REV|


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
|||||||||5V<br>|SYS_<br>|REV<br>|
|||||||||~~9V~~<br>15<br>|SYS_<br>VSYS<br>|REV<br>_REV<br>|
|||||||||20<br>36|VSYS<br>V|_REV<br>|
|||||||||48|~~SYS~~<br>VSYS|~~_REV~~<br>_REV|


|5<br>20Vin, 27Vbat<br>4 28Vin, 27Vbat<br>3 36Vin, 27Vbat<br>2<br>(%)<br>1<br>Accuracy<br>0<br>-1<br>-2<br>-3<br>-4<br>-5<br>-40 -25 -10 5 20 35 50 65 80<br>Temperature (C)<br>ICHG = 5 A<br>Figure 7-5. Charge Current Accuracy vs Temperature|0.50<br>IQ_BAT<br>0.45 IQ_VAC<br>0.40<br>0.35<br>(mA)<br>0.30<br>0.25 Current<br>0.20<br>0.15<br>0.10<br>0.05<br>0.00<br>-40 -20 0 20 40 60 80 100 120<br>Temperature (C)<br>IQ_BAT: VAC = 0 V IQ_VAC: VAC = 20 V EN_HIZ = 1<br>Figure 7-6. Battery and Input Quiescent Current vs Temperature<br>with VBAT = 28 V|
|---|---|
|Temperature (C)<br>Accuracy (%)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>-2<br>-1<br>0<br>1<br>2<br>VINPM = 19V<br>VINPM = 34V<br>VBAT = 28 V<br>**Figure 7-7. Input Voltage (VAC_DPM) Regulation Accuracy vs**<br>**Temperature**|Temperature (C)<br>Accuracy (%)<br>-40<br>-25<br>-10<br>5<br>20<br>35<br>50<br>65<br>80<br>-5<br>-4<br>-3<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>5<br>20Vin, 28Vbat<br>~~28Vin, 28Vbat~~<br>36Vin, 28Vbat<br>IAC_DPM = 3 A<br>**Figure 7-8. Input Current (IAC_DPM) Regulation Accuracy vs**<br>**Temperature**|
|Reverse Mode Output Power (W)<br>Efficiency (%)<br>0<br>20<br>40<br>60<br>80<br>100 120 140 160 180 200 220 240<br>80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br>98<br>100<br>5VSYS_REV<br>~~9V~~SYS_REV<br>15VSYS_REV<br>20VSYS_REV<br>36V~~SYS_REV~~<br>48VSYS_REV<br>VBAT = 20 V<br>**Figure 7-9. Reverse Mode Efficiency (5s battery configuration)**|Reverse Mode Output Power (W)<br>Efficiency (%)<br>0<br>20<br>40<br>60<br>80<br>100 120 140 160 180 200 220 240<br>80<br>82<br>84<br>86<br>88<br>90<br>92<br>94<br>96<br>98<br>100<br>5VSYS_REV<br>~~9V~~SYS_REV<br>15VSYS_REV<br>20VSYS_REV<br>36V~~SYS_REV~~<br>48VSYS_REV<br>VBAT = 28 V<br>**Figure 7-10. Reverse Mode Efficiency (7s battery configuration)**|



18 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**7.7 Typical Characteristics (BQ25750) (continued)**


C VAC = 160 µF, C OUT = 160 µF, _f_ _SW_ = 250 kHz, L = 10 μH, T A = 25°C (unless otherwise specified)



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



100


98


96


94


92


90


88


86


84


82





3


2



80

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
|||||||||5V<br>|SYS_<br>|REV<br>|
|||||||||~~9V~~<br>15<br>|SYS_<br>VSYS<br>|REV<br>_REV<br>|
|||||||||20<br>36|VSYS<br>V|_REV<br>|
|||||||||48|~~SYS~~<br>VSYS|~~_REV~~<br>_REV|



0 20 40 60 80 100 120 140 160 180 200 220 240

Reverse Mode Output Power (W)


VBAT = 38 V


**Figure 7-11. Reverse Mode Efficiency (10s battery**



1


0


-1


-2


-3

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|1<br>2|9VBAT<br>7VBAT|
|---|---|---|---|---|---|---|---|---|---|
|||||||||~~3~~|~~8V~~BAT|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||



5 10 15 20 25 30 35 40 45 50

Reverse Mode Regulation Voltage Setting (V)


**Figure 7-12. Reverse Mode Output Voltage Accuracy vs**

**VAC_REV Setting**



**configuration)**


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 19


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**8 Detailed Description**

**8.1 Overview**


The BQ25750 is a wide input voltage, Li-Ion, Li-polymer, and LiFePO 4 switched-mode buck-boost battery
charge controller with direct power path control. The device offers high-efficiency battery charging over a wide
voltage range with accurate and programmable charge current and charge voltage regulation, in addition to
automatic charge preconditioning, termination, and charge status indication. The device integrates all the loop
compensation and 5-V gate drivers for the buck-boost converter, thereby providing a high density solution
with ease of use. The switching frequency of the device can be programmed or forced to follow an external
clock frequency via the FSW_SYNC pin. While switching under light-load the device offers an optional Pulse
Frequency Modulation (PFM) mode to increase efficiency. The charger has a digital state machine that advances
the charger's states as the converter analog feedback loops hand off control to each other. It also manages the
fault protection comparators. The loops regulate and comparators compare against reference values in the I [2] C
registers, unless clamped by external resistors.


Besides the I [2] C host-controlled charging mode, the device also supports autonomous charging mode via resistor
programmable limits. Input current, charge current and charge voltage regulation targets can be changed via
the ILIM_HIZ, ICHG, and FB pins, respectively. The device can complete a charging cycle without any software
intervention. Charging function is controlled via the CE pin.


For Li-Ion and LiFePO 4 chemistries, the device checks battery voltage and charges the battery in different
phases accordingly: trickle charging, pre-charging, constant current (CC) charging and constant voltage (CV)
charging. At the end of the charging cycle, the charger automatically terminates when the charge current is
below the termination current limit in the constant voltage phase. When the full battery falls below the recharge
threshold, the charger automatically starts a new charge cycle.


The input operating window is programmed via the ACUV and ACOV pins. When the input voltage is outside
the programmed window, the device automatically stops the charger, transitions to power the system load from
the battery, and the PG pin pulls HIGH. In the absence of an input source, the device can power the system
load from battery through BATFET or via reverse power flow, discharging the battery through the buck-boost
converter to generate a programmable, regulated voltage on system which is above or below the battery voltage.


The charger provides various safety features for battery charging and system operation, including battery
temperature negative thermistor (NTC) monitoring, charge timers and over-voltage/over-current protections on
battery and input. The thermal shutdown prevents charging when the junction temperature exceeds the T SHUT
limit.


The device has three status pins (STAT1, STAT2, and PG) to indicate the charging status and input voltage
status. These pins can be used to drive LEDs or communicate with a host processor. If needed, these pins can
also be used as general purpose indicators and their status controlled directly by the I [2] C interface. In addition,
the CE pin can also be used as a general purpose indicator. The INT pin immediately notifies host when the
device status changes, including faults.


The device also provides a 16-bit analog-to-digital converter (ADC) for monitoring input current, charge current
and input/battery/system/thermistor voltages (IAC, IBAT, VAC, VBAT, VSYS, TS).


The device comes with a 36-pin 5-mm × 6-mm QFN package with 0.5-mm pin pitch.


20 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**8.2 Functional Block Diagram**


VAC



ACOV


ACUV


ILIM_HIZ


ICHG


SRP


SRN


ACP


ACN


FB


SYS


SCL


SDA


INT


CE


PG


STAT2


STAT1


FBG











**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


ACDRV


BATDRV


BATSRC


REGN





























DRV_SUP


BTST1


HIDRV1


SW1


LODRV1





































BTST2


HIDRV2


SW2


LODRV2


MODE


PGND














|Col1|Col2|CHARGE<br>CONTROL|
|---|---|---|
||STATUS<br>PIN|STATUS<br>PIN|




|Col1|VACDRV_REG<br>VSRN<br>VACOV<br>+ VAC_OVP EN_ACFET VAC<br>VREF_ACOV<br>EN_BATFET POWER-PATH<br>MANAGER VBATDRV_REG<br>VACUV R LE DG ON REGN<br>VAC_UVP<br>VREF_ACUV HIZ_MODE<br>+<br>IAC IBAT BQ25750<br>VILIM_HIZ<br>VICHG REGN VDRV_SUP<br>VO,REF<br>+ IBAT VICHG<br>– – VFB<br>+ BAT_OVP<br>– ICHG_REG VREF_ICHG VBAT_OV<br>+ +<br>IBAT<br>+ IAC VILIM_HIZ + BAT_OCP<br>– – VICHG_OC<br>– IAC_DPM VREF_ILIM_HIZ DRV_SUP<br>+ + VDRV_SUP<br>+ DRV_OVP<br>VDRV_OVP<br>VFB VACUV<br>– –<br>VDRV_SUP<br>VFB_REG VACUV_DPM DRV_UVP BUCK-BOOST<br>+ + VDRV_UVP CONTROLLER<br>+<br>VSYS VAC<br>+ + VSYS + SYS_OVP<br>VSYS_REV VAC_DPM VSYS_REV_OV<br>– –<br>HIZ_MODE<br>VFB_REG<br>EN_CHARGE DRV_SUP<br>ICHG_REG<br>EN_PFM<br>IAC_DPM<br>EN_REVERSE<br>VV S IA AYC CS_ __D RRP EEM VV DR AE CF C CO ON NVE TRR OTE LR E EN N_ _A BC ATF FE ET<br>T<br>VV AR CE UF V_ _I DC PH MG V TSILI HM_ UH TIZ + I TC S_ HUT TJ<br>CLK<br>VREF_ILIM_HIZ OSCILLATOR<br>SYNC_DET<br>IAC<br>IBAT<br>ADC VAC<br>VBAT<br>I2C VSYS<br>VTS<br>VFB_REG<br>VRECHG <br>RECHRG +<br>VFB<br>IBAT<br>TERMINATION +<br>ITERM<br>CHARGE VBAT_LOWV<br>BAT_LOWV +<br>CONTROL VFB<br>STATUS BAT_SHORT + VBAT_SHORT<br>PIN BATTERY|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
|||||
||VBAT<br>TS_SUSPEND<br><br>CNTRL<br><br>THERMISTOR<br>SENSI~~N~~G<br>VTS|VBAT<br>TS_SUSPEND<br><br>CNTRL<br><br>THERMISTOR<br>SENSI~~N~~G<br>VTS||



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 21


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**8.3 Feature Description**


**8.3.1 Device Power-On-Reset**


The internal bias circuits are powered from either VAC or SRN. When VAC rises above V VAC_OK, the ACFET
driver is active and charging is allowed. When BAT rises above 3 V, the BATFET driver is active, and reverse
mode operation is allowed.


A POR occurs when one of these supplies rises above its corresponding V OK level, while the other supply is
below its corresponding V OK level. After the POR, I [2] C interface is ready for communication and all the registers
are reset to default value. The host can access all the registers after POR.


**8.3.2 Device Power-Up From Battery Without Input Source**


If only battery is present and the voltage is above V SRN_OK threshold, the BATFET turns on and connects battery
to system. The REGN LDO stays off to minimize the quiescent current. The N-type driver allows for use of
low R DS,ON external BATFET, minimizing the conduction loss. The low quiescent current on BAT maximizes the
battery run time. The ADC can be used to monitor discharge current through SRP and SRN pins. The BATFET
can be forced to turn off via the FORCE_BATFET_OFF register bit.


**8.3.3 Device Power Up from Input Source**


When a valid input source (V VAC_OK < VAC and VAC within the ACUV and ACOV operating window) is detected,
the ACFET turns on to connect the input to the system, and the PG pin pulls LOW. If charging is enabled, the
device proceeds to enable the REGN LDO and power up the buck-boost converter.


_**8.3.3.1 VAC Operating Window Programming (ACUV and ACOV)**_


The VAC operating window can be programmed via the ACUV and ACOV pins using a three-resistor divider
from VAC to PGND as shown in Figure 8-1.

|be programmed via the ACUV gure 8-1.|Col2|and ACOV|
|---|---|---|
|INPUT|INPUT|VAC<br>ACUV<br>ACOV|
|INPUT|RAC1|RAC1|
|INPUT|RAC2|RAC2|



**Figure 8-1. ACUV and ACOV Programming**


When V ACUV falls and reaches V ACUV_DPM, the device enters input voltage regulation, thereby reducing the
charge current. V ACUV continues falling below V REF_ACUV, the device automatically stops the converter, turns off
the ACFET, turns on the BATFET and the PG pin pulls high.


**System Note:** if VAC_DPM register is programmed to a value higher than POR, the device regulates the
VAC voltage to the higher of VAC_DPM register or V ACUV_DPM pin voltage. Refer to Section 8.3.5.1.2 for more
information.


When V ACOV rises above V REF_ACOV, the device automatically stops the converter, turns off the ACFET, turns on
the BATFET and the PG pin pulls high.


The following equations govern the relationship between the resistor divider and the target operating voltage
window programmed by ACOV and ACUV pins:



V ACOV_TARGET = V REF_ACOV ×


V ACUV_TARGET = V REF_ACUV ×



RAC1 + RAC2 + RAC3
(1)
RAC3


RAC1 + RAC2 + RAC3
(2)
RAC2 + RAC3



22 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



If unused, tie ACUV to VAC and ACOV to PGND in order to apply the internal VAC operating window (V VAC_OP ).


_**8.3.3.2 REGN Regulator (REGN LDO)**_


The REGN LDO regulator provides a regulated bias supply for the IC and the TS external resistors. Additionally,
REGN voltage can be used to drive the buck-boost switching FETs directly by tying the DRV_SUP pin to REGN.
The pull-up rail of PG, STAT1, and STAT2 can be connected to REGN as well. The REGN LDO is enabled when
below conditions are valid:

1. VAC voltage above V VAC_OK and charge is enabled in forward mode.
2. BAT voltage above 3 V in Reverse mode and Reverse Mode is enabled (EN_REV = 1)


At high input voltages and/or large gate drive requirements, the power loss from gate driving via the REGN LDO
can be excessive. This power for the gate drivers can be provided externally by directly driving the DRV_SUP
pin with a high efficiency supply ranging from 4.5 V to 12 V. This supply should be able to provide at least 50 mA
or more as required to drive the switching FET gate charge.


The power dissipation for driving the gates via the REGN LDO is: P REGN =( VAC −V REGN) × Q G( TOT) 1,2, 3,4 × f SW,
where _Q_ _G(TOT)1,2,3,4_ is the sum of the total gate charge for all switching FETs and _f_ _SW_ is the programmed
switching frequency. The Safe Operating Area (SOA) below is based on a 1-W power loss limit.


80


70


60


50


40


30


20


10


0

0 10 20 30 40 50 60 70 80 90 100

Q G(TOT)1,2,3,4 x f SW (mA)


**Figure 8-2. REGN LDO Safe Operating Area (SOA)**


_**8.3.3.3 Compensation-Free Buck-Boost Converter Operation**_


The device integrates all the loop compensation, thereby providing a high density solution with ease of use. At
startup, the device toggles the SW node for about 40 ms to determine the correct compensation values for a
given set of passives. If the battery is above VBAT_LOWV, then SW2 is toggled. SW1 is toggled otherwise.


The charger employs a synchronous buck-boost converter that allows charging from a wide range of input
voltage sources. The charger operates in buck, buck-boost or boost mode. The converter can operate
uninterruptedly and continuously across the three operation modes. During buck-boost mode, the converter
alternates a SW1 pulse with a SW2 pulse, with effective switching frequency interleaved among these pulses for
highest efficiency operation.


During boost mode operation, the HS FET is forced to turn on for 225 ns in each switching cycle to ensure
inductor energy is delivered to the output, effectively limiting the maximum boosting ratio. For example, when
device is configured to switch at 500 kHz, the switching period is 2 μs, yielding a duty cycle limit of (1 - 0.225
μs/2 μs) = 88.75%. Given a 5-V input, this translates to a maximum 44-V output assuming 100% efficiency. The
true output will be lower than this ideal limit. At lower switching frequencies, the maximum duty cycle increases,
making the limitation less significant.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 23


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-1. Switching MOSFET Operation**







|MODE|BUCK|BUCK-BOOST|BOOST|
|---|---|---|---|
|HS BUCK FET|Switching at_fSW_|Switching (_fSW_ interleaved<br>between SW1 and SW2)|ON|
|LS BUCK FET|Switching at_fSW_|Switching (_fSW_ interleaved<br>between SW1 and SW2)|OFF|
|LS BOOST FET|OFF|Switching (_fSW_ interleaved<br>between SW1 and SW2)|Switching at_fSW_|
|HS BOOST FET|ON|Switching (_fSW_ interleaved<br>between SW1 and SW2)|Switching at_fSW_|


**8.3.3.3.1 Light-Load Operation**


In order to improve converter light-load efficiency, the device switches to Pulse Frequency Modulation (PFM)
control at light load when the EN_PFM bit is set to 1. The effective switching frequency will decrease accordingly
when output load decreases.


EN_PFM bit is automatically cleared to 0 every time the converter starts and a valid SYNC clock input is
detected on the FSW_SYNC pin, thereby ensuring fixed frequency operation regardless of output current. The
bit can be overwritten to 1 to allow PFM after startup even when SYNC signal is present.


Light-load PFM mode can be disabled by clearing the EN_PFM bit. In this case, the device switches in PWM
mode at a fixed switching frequency. It is recommended to disable PFM mode (EN_PFM = 0) when termination
is enabled and set lower than 2 A.


_**8.3.3.4 Switching Frequency and Synchronization (FSW_SYNC)**_


The device switching frequency can be programmed between 200 kHz to 600 kHz using a resistor from the
FSW_SYNC pin to PGND. The R FSW resistor is related to the nominal switching frequency ( _f_ _SW_ ) by the equation:


1
R FSW = (3)


This pin must be pulled to PGND using a R FSW, do not leave floating. In addition to programming the nominal
switching frequency, the FSW_SYNC pin can also be used to synchronize the internal oscillator to an external
clock signal. The synchronization feature works over the same range as the switching frequency: 200-kHz to
600-kHz range.

**Table 8-2. Common R** **FSW** **and Switching Frequency Values**

|R (kΩ)<br>FSW|SWITCHING FREQUENCY (kHz)|
|---|---|
|200|200|
|133|250|
|100|300|
|80|350|
|66.67|400|
|57.1|450|
|50|500|
|44.4|550|
|40|600|



_**8.3.3.5 Device HIZ Mode**_


When a valid input supply is present, it is possible to force the device into HIZ Mode which disables switching,
disables REGN LDO, turns off the ACFET, turns on the BATFET. The system load is provided by the battery in


24 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



this mode. The device draws less than I HIZ_VAC from the input supply in this mode. The charger enters HIZ Mode
when EN_HIZ bit is set to 1 or the ILIM_HIZ pin is pulled above V IH_ILIM_HIZ (refer to Section 8.3.5.1.1.1).


If the device is operating in reverse mode with the converter turned on, and the device enters HIZ mode
(EN_HIZ bit is set to 1 or ILIM_HIZ pin is pulled above V IH_ILIM_HIZ ), switching stops and the system load is
provided by the battery through the BATFETs. Once HIZ mode condition is cleared by the host, the device
resumes reverse mode operation, powering the system through the converter with the BATFET off.


The device exits HIZ Mode when the EN_HIZ bit is cleared to 0 and the ILIM_HIZ pin is pulled below 0.4 V.


**8.3.4 Battery Charging Management**


The device charges 1-cell up-to 14-cell Li-Ion batteries and 1-cell up-to 16-cell LiFePO 4 batteries. The charge
cycle is autonomous and requires no host interaction.


_**8.3.4.1 Autonomous Charging Cycle**_


When battery charging is enabled (EN_CHG bit =1 and CE pin is LOW), the device autonomously completes
a charging cycle without host involvement. The device charging parameters can be set by hardware through
the FB pin to set regulation voltage and the ICHG pin to set charging current. The host can always control the
charging operation and optimize the charging parameters by writing to the corresponding registers through I [2] C.


**Table 8-3. Li-Ion & LiFePO** **4** **Charging Parameter Default Settings**

|PARAMETER|VALUE|
|---|---|
|Charge Stages|Precharge → Fast Charge (CC) → Taper Charge (CV) →<br>Termination → Recharge|
|FB Voltage Regulation Target (VFB_REG)|1.536 V|
|Battery Low Voltage (VBAT_LOWV )|66.7% x VFB_REG = 1.0245 V|
|Recharge Voltage (VRECHG)|97.6% x VFB_REG =1.4991 V|
|Charging Current HW Limit (ICHG pin)|ICHG = KICHG / RICHG|
|Pre-Charge Current HW Limit (ICHG pin)|20% x ICHG|
|Termination Current HW Limit (ICHG pin)|10% x ICHG|
|CV Timer|Disabled|
|NTC Temperature Profile|JEITA|
|Safety Timer|12 hours|



A new charge cycle starts when the following conditions are valid:

 - VAC is within the ACUV and ACOV operating window

 - Device is not in HIZ mode (EN_HIZ = 0 and ILIM_HIZ pin voltage is below V IH_ILIM_HIZ )

 - REGN is above V
REGN_OK

 - Battery charging is enabled (EN_CHG = 1 and CE pin is LOW )

 - No thermistor fault on TS

 - No safety timer fault


For lithium-ion battery charging, the charger device automatically terminates the charging cycle when the
charging current is below termination threshold, charge voltage is above recharge threshold, and device is
not in DPM mode. When a full battery voltage is discharged below recharge threshold (threshold selectable via
VRECHG[1:0] bits), the device automatically starts a new charging cycle. After the charge is done, toggle either
CE pin or EN_CHG bit can initiate a new charging cycle. In addition, the device offers a dedicated CV timer to
stop the charging after a programmable period (CV_TMR bits) in CV mode, regardless of the charge current
value.


The status register (CHARGE_STAT) indicates the different charging phases as:

 - 000 – Not Charging

 - 001 – Trickle Charge (VFB < V BAT_SHORT )

 - 010 – Pre-charge (V BAT_SHORT < VFB < V BAT_LOWV )


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 25


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


 - 011 – Fast-charge (CC mode)

 - 100 – Taper Charge (CV mode)

 - 101 – Reserved

 - 110 – Top-off Timer Active Charging

 - 111 – Charge Termination Done


When the charger transitions to any of these states, including when charge cycle is completed, an INT pulse is
asserted to notify the host.


Supercapacitors do not require Trickle Charge or Pre-charge regions when their voltage is low. For
supercapacitor charging, setting the EN_PRECHG bit to 0 can disable both of these charging regions. In this
case, the charger outputs ICHG current as long as the feedback voltage (V FB ) is below VFB_REG. The following
settings are recommended for supercapacitor charging:

 - EN_PRECHG = 0

 - EN_TERM = 0

 - EN_CHG_TMR = 0


**8.3.4.1.1 Charge Current Programming (ICHG pin and ICHG_REG)**


There are two distinct thresholds to limit the charge current (if both are enabled, the lowest limit of these will
apply):
1. ICHG pin pull down resistor (hardware control)
2. ICHG_REG register bits (host software control)


To set the maximum charge current using the ICHG pin, a pull-down resistor to PGND is used. It is required to
use a 5-mΩ R BAT_SNS sense resistor. The charge current limit is controlled by:



I CHG_MAX =



KICHG
(4)
RICHG



The precharge current limit is defined as I PRECHG_MAX = 20% x I CHG_MAX, and the termination current is I TERM =
10% x I .
CHG_MAX


The actual charge current limit is the lower value between ICHG pin setting and I [2] C register setting
(ICHG_REG). For example, if the register setting is 10 A (0xC8), and ICHG pin has a 10-kΩ resistor (K ICHG
= 50 A-kΩ) to ground for 5 A, the actual charge current limit is 5 A. The device regulates ICHG pin at V REF_ICHG .
If ICHG pin voltage exceeds V REF_ICHG, the device enters charge current regulation.


The ICHG pin can also be used to monitor charge current when device is not in charge current regulation. When
not in charge current regulation, the voltage on ICHG pin (V ICHG ) is proportional to the actual charging current.
ICHG pin can be used to monitor battery current with the following relationship:



I BAT =



KICHG × VICHG
(5)
RICHG × VREF_ICHG



For example, if ICHG pin is set with 10-kΩ resistor, and the ICHG voltage 1.0V, the actual charge current is
between 2.4 A to 2.6 A (based on K ICHG specified).


If ICHG pin is shorted to PGND, the charge current limit is set by the ICHG_REG register. If hardware charge
current limit function is not needed, it is recommended to short this pin to PGND. The ICHG pin function can be
disabled by setting the EN_ICHG_PIN bit to 0 (recommended when pin is shorted to PGND). When the pin is
disabled, charge current limit and monitoring functions via ICHG pin are not available.


To set the maximum charge current using the ICHG_REG register bits, write to the ICHG_REG register bits.
The charge current limit range is from 400 mA to 20,000 mA with 50 mA/step. The default ICHG_REG is set to
maximum code, allowing ICHG pin to limit the current in hardware.


26 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


_**8.3.4.2 Li-Ion Battery Charging Profile**_



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



The device charges the battery in five phases: trickle charge, pre-charge, constant current, constant voltage, and
top-off trickle charging (optional). At the beginning of a charging cycle, the device checks the battery voltage and
regulates current/voltage accordingly.


**Table 8-4. Recommended Li-Ion Charge Settings**

|PARAMETER|I2C REGISTER BITS|VALUE|EQUIVALENT PER 4.2-V<br>CHARGE (V)|
|---|---|---|---|
|Battery Low Voltage|VBAT_LOWV|0x3 = 71.4% x VFB_REG|3.0 V|
|Recharge Voltage|VRECHG|0x3 = 97.6% x VFB_REG|4.1 V|



If the charger device is in DPM regulation during charging, the actual charging current will be less than the
programmed value. In this case, termination is temporarily disabled and the charging safety timer is counted at



Charge Voltage
V FB_REG

V RECHG


Charge Current
ICHG


V BATLOWV


V BAT_SHORT


IPRECHG


ITERM
I BAT_SHORT












|as explained in Charging Safety Timer.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|Battery Voltage|Battery Voltage|Battery Voltage|Battery Voltage|
|Charge Current<br>Trickle Charge<br>Pre-charge<br>Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>001<br>010<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>111<br>Precharge Timer<br>(2hrs)<br>Safety Timer<br>CHG_TMR[1:0]<br>100<br>Safety Timer<br>Auto-<br>Recharge<br>CV|Charge Current<br>Trickle Charge<br>Pre-charge<br>Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>001<br>010<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>111<br>Precharge Timer<br>(2hrs)<br>Safety Timer<br>CHG_TMR[1:0]<br>100<br>Safety Timer<br>Auto-<br>Recharge<br>CV|Charge Current<br>Trickle Charge<br>Pre-charge<br>Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>001<br>010<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>111<br>Precharge Timer<br>(2hrs)<br>Safety Timer<br>CHG_TMR[1:0]<br>100<br>Safety Timer<br>Auto-<br>Recharge<br>CV|Charge Current<br>Trickle Charge<br>Pre-charge<br>Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>001<br>010<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>111<br>Precharge Timer<br>(2hrs)<br>Safety Timer<br>CHG_TMR[1:0]<br>100<br>Safety Timer<br>Auto-<br>Recharge<br>CV|
|Trickle Charge<br>Pre-charge<br>001<br>010<br>Precharge Timer<br>(2hrs)|Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>Safety Timer<br>CHG_TMR[1:0]|||
|Trickle Charge<br>Pre-charge<br>001<br>010<br>Precharge Timer<br>(2hrs)|Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>Safety Timer<br>CHG_TMR[1:0]|111|100|
|Trickle Charge<br>Pre-charge<br>001<br>010<br>Precharge Timer<br>(2hrs)|Fast-Charge<br>CC<br>Top-off Timer<br>(optional)<br>011<br>110<br>Taper-Charge<br>CV<br>100<br>Safety Timer<br>CHG_TMR[1:0]||Safety Timer|



**Figure 8-3. Typical Li-Ion Battery Charging Profile**


_**8.3.4.3 LiFePO**_ _**4**_ _**Battery Charging Profile**_


The device charges the battery in five phases: trickle charge, pre-charge, constant current, constant voltage, and
top-off trickle charging (optional). At the beginning of a charging cycle, the device checks the battery voltage and
regulates current/voltage accordingly.


**Table 8-5. Recommended LiFePO** **4** **Charge Settings**

|PARAMETER|I2C REGISTER BITS|VALUE|EQUIVALENT PER 3.6-V<br>CHARGE (V)|
|---|---|---|---|
|Battery Low Voltage|VBAT_LOWV|0x1 = 55% x VFB_REG|1.98 V|
|Recharge Voltage|VRECHG|0x0 = 93% x VFB_REG|3.35 V|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 27


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


If the charger device is in DPM regulation during charging, the actual charging current will be less than the
programmed value. In this case, termination is temporarily disabled and the charging safety timer is counted at
half the clock rate, as explained in Charging Safety Timer. The typical charging cycle for LiFePO 4 follows the
same profile as Typical Li-Ion Battery Charging Profile.


_**8.3.4.4 Charging Termination for Li-ion and LiFePO**_ _**4**_


The device terminates a charge cycle when the battery voltage is above recharge threshold, and the current is
below termination current. The termination current threshold is controlled by the lower option between 10% x
ICHG pin setting or the ITERM register setting.


In standalone applications using the ICHG pin to program the current, the termination threshold is set at 10% of
the ICHG pin value (10-A ICHG pin programming results in 1-A termination).


In host-controlled applications, the termination current can be programmed using the ITERM register bits. The
ICHG pin can still be used to set a hardware limit for the charge current.


After the charging cycle is completed, the buck-boost converter turns off. The ACFET stays on to power the
system. When termination occurs, the status register CHARGE_STAT is set to 111, and an INT pulse is asserted
to the host. Termination is temporarily disabled when the charger device is in input current, or input voltage
regulation. Termination can be permanently disabled by writing 0 to EN_TERM.


At low termination currents, due to the comparator offset, the actual termination current may be up to 20% higher
than the termination target. In order to compensate for comparator offset, a programmable top-off timer (default
disabled) can be applied after termination is detected. The top-off timer follows safety timer constraints, such that
if safety timer is suspended, so is the top-off timer. Similarly, if safety timer is doubled, so is the top-off timer.
CHARGE_STAT reports whether the top off timer is active via the 110 code. Once the Top-Off timer expires, the
CHARGE_STAT register is set to 111 and an INT pulse is asserted to the host.


_**8.3.4.5 Charging Safety Timer**_


The device has built-in safety timer to prevent extended charging cycle due to abnormal battery conditions. The
user can program fast charge safety timer through I [2] C (CHG_TMR bits). When safety timer expires, the fault
register CHG_TMR_STAT bit is set to 1, and an INT pulse is asserted to the host. The safety timer feature can
be disabled by clearing EN_CHG_TMR bit.


During input voltage or input current regulation, the safety timer counts at half clock rate as the actual charge
current is likely to be below the programmed setting. For example, if the charger is in input current regulation
(IAC_DPM_STAT=1) throughout the whole charging cycle, and the safety timer is set to 5 hours, then the timer
will expire in 10 hours. The timer also counts at half clock rate for TS pin events which reduce charge current
(refer to JEITA Guideline Compliance in Charge Mode section). This half clock rate feature can be disabled by
setting EN_TMR2X = 0.


During faults which disable charging, timer is suspended. Once the fault goes away, safety timer resumes. If
the charging cycle is stopped and started again, the timer gets reset (toggle CE pin or EN_CHG bit restarts the
timer).


The pre-charge safety timer is a fixed 2 hour counter that runs when VBAT < V BAT_LOWV . The pre-charge safety
timer is disabled when EN_PRECHG bit is 0.


_**8.3.4.6 Thermistor Qualification**_


The charger device provides a single thermistor input for battery temperature monitor.


**8.3.4.6.1 JEITA Guideline Compliance in Charge Mode**


To improve the safety of charging Li-ion batteries, JEITA guideline was released on April 20, 2007. The guideline
emphasized the importance of avoiding a high charge current and high charge voltage at certain low and high
temperature ranges.


28 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



To initiate a charge cycle, the voltage on TS pin must be within the VT1 to VT5 thresholds. If TS voltage exceeds
the T1 to T5 range, the controller suspends charging and waits until the battery temperature is within the T1 to
T5 range.


At cool temperature, T1 to T2, JEITA recommends the charge current to be reduced to half of the charge current
or lower. The device allows charge current in the cool temperature region to be progrramed to 20%, 40% or
100% of the charge current at T2 to T3 or charge suspend, which is controlled by the register bits JEITA_ISETC.
If charge current is reduced in the cool temperature region, the safety timer counts at half clock rate when
EN_TMR2X = 1.


At warm temperature, T3 to T5, JEITA recommends charge voltage less than 4.1 V / cell. The device provides
the programmability of the charge voltage at T3-T5, to be with a voltage offset less than charge voltage at T2 to
T3 or charge suspend, which is controlled by the register bits JEITA_VSET.


The charger also provides flexible voltage/current settings beyond the JEITA requirements. The charge current
setting at warm temperature T3 to T5 can be configured to be 40%, or 100% of the programmed charge current
or charge suspend, which is programmed by the register bit JEITA_ISETH. If charge current is reduced in the
JEITA warm region, the safety timer counts at half clock rate when EN_TMR2X = 1.


The default charging profile for JEITA is shown in the figure below, in which the blue line is the default setting
and the red dash line is the programmable options.





V FB_REG


97.6%


94.3%



|Col1|VSET = 11<br>VSET = 10<br>VSET = 01<br>VSET = 00|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||||||VSET = 10|VSET = 10|VSET = 10|
||||||||||
|||||||VSET = 01|VSET = 01|VSET = 01|
|||||||VSET = 00|VSET = 00|VSET = 00|
||||||||||


T1 T2 T3 T5
0°C 10°C TS Temperature 45°C 60°C



100%


80%


60%


40%


20%



|Col1|ISETC=11|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|ISETC=00<br>ISETC=01<br>ISETC=10<br>ISETC=11<br>ISETH=0<br>ISETH=1|
||ISETC=10|ISETH=0|ISETH=0|ISETH=0|ISETH=0|ISETH=0|ISETH=0|ISETH=0|
||||||||||
||||||||||
||ISETC=01|ISETC=01|ISETC=01|ISETC=01|ISETC=01|ISETC=01|ISETC=01|ISETC=01|
|ISETC=00|ISETC=00|ISETC=00|ISETC=00|ISETC=00|ISETC=00|ISETC=00|ISETC=00|ISETC=00|
|ISETC=00|ISETC=00||||||||


T1 T2 T3 T5
0°C 10°C TS Temperature 45°C 60°C





**Figure 8-4. TS Charging Values**







Assuming a 103AT NTC thermistor on the battery pack as shown above, the value of RT1 and RT2 can be
determined by:



RT2 =


RT1 =




1
VT1 [−1]

1 1
RT2 [+] RTHCOLD



(6)


(7)



Select 0°C to 60°C range for Li-ion or Li-polymer battery:


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 29


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


RTH T1 = 27.28 kΩ


RTH T5 = 3.02 kΩ


RT1 = 5.24 kΩ


RT2 = 30.31 kΩ


The device also offers programmability for all the thresholds via the TS Charging Threshold Control register
(REG0x1B). This flexibility can help to change the charger's operating window in software.


The JEITA profile can be disabled by clearing the EN_JEITA register bit. In this case, the device still limits the
charging window from T1 to T5, but no special charge profile is employed within the Cool (T1 to T2) or Warm (T3
to T5) regions.


The NTC monitoring window can be disabled by clearing the EN_TS register bit. In this case, the TS pin voltage
is ignored, and the device always reports normal TS status. If EN_TS is set to 0, TS pin can be floated or
connected to PGND.


**8.3.4.6.2 Cold/Hot Temperature Window in Reverse Mode**


For battery protection during reverse or auto-reverse mode operation, the device monitors the battery
temperature to be within the VBCOLD to VBHOT thresholds. When temperature is outside of the thresholds,
the reverse mode is shut off and device returns to powering the system from the battery. In addition, EN_REV,
EN_AUTO_REV and REVERSE_STAT bits are cleared to 0 and corresponding TS_STAT is reported (TS Cold or
TS Hot). The temperature protection in reverse mode can be completely disabled by clearing the EN_TS bit to 0.


Temperature Range for Reverse Mode

VREGN


Reverse Mode Suspended


V BCOLDx


(±10°C / ±20°C)


Reverse Mode Enable


V BHOTx


(55°C / 60°C / 65°C)


Reverse Mode Suspended


GND


**Figure 8-5. TS Pin Thermistor Sense Threshold in Reverse Mode**


**8.3.5 Power Path Management**


The device accommodates a wide range of input sources from 4.2 V up to 70 V. The device provides dynamic
power management and automatic power path selection to supply the system (SYS) from input source (VAC), or
battery (BAT).


_**8.3.5.1 Dynamic Power Management: Input Voltage and Input Current Regulation**_


The device features Dynamic Power Management (DPM), which continuously monitors the input current and
input voltage. When input source is over-loaded, either the current exceeds the input current limit (lower of
IAC_DPM or ILIM_HIZ pin setting), or the voltage falls below the input voltage limit (higher of VAC_DPM or
ACUV pin setting, V ACUV_DPM ). The device then reduces the charge current until the input current falls below the
input current limit and the input voltage rises above the input voltage limit.


When the charge current is reduced to zero, but the input source is still overloaded, the input voltage continues
to drop. Once the input voltage drops below the ACUV limit (V ACUV < V REF_ACUV ), the charger stops switching
and the device automatically transitions to Battery Only Mode so that the system is supported by the battery.


30 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**8.3.5.1.1 Input Current Regulation**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



The total input current is a function of the system supply current and the battery charging current. System current
normally fluctuates as portions of the systems are powered up or down. Without DPM, the source must be able
to supply the maximum system current and the maximum charger input current simultaneously. By using DPM,
the battery charger reduces the charging current when the input current exceeds the input current limit set by
the lower of IAC_DPM register bits, or ILIM_HIZ pin. This allows the current capability of the input source to be
lowered, reducing system cost.


There are two thresholds to limit the input current (if both are enabled, the lower limit of these two will apply):
1. IAC_DPM register bits (host software control)
2. ILIM_HIZ pull down resistor (hardware control)


To set the maximum current using the IAC_DPM register bits, write to the IAC_DPM register bits. When using a
2-mΩ resistor, the input current limit range is from 1 A to 50 A with 125 mA/step. The default IAC_DPM is set to
maximum code, allowing ILIM_HIZ pin to limit the current in hardware.


To set the maximum current using the ILIM_HIZ pin, refer to Section 8.3.5.1.1.1.


Although both limits are referenced to a 2-mΩ sense resistor, other values can also be used. A larger sense
resistor provides a larger sense voltage and higher regulation accuracy, but at the expense of higher conduction
loss. For example, using a 5-mΩ resistor yields programmability from 400 mA to 20 A with 50 mA/step.


_**8.3.5.1.1.1 ILIM_HIZ Pin**_


To set the maximum input current using the ILIM_HIZ pin, a pull-down resistor to PGND is used. When using a
2-mΩ R AC_SNS resistor, the input current limit is controlled by: I AC_MAX = K ILIM / R ILIM_HIZ .


The actual input current limit is the lower value between ILIM_HIZ pin setting and register setting (IAC_DPM).
For example, if the register setting is 20 A, and ILIM_HIZ pin has a 5-kΩ resistor (K ILIM = 50 A-kΩ) to ground
for 10 A, the actual input current limit is 10 A. ILIM_HIZ pin can be used to set the input current limit
when EN_ILIM_HIZ_PIN bit is set to 1. The device regulates the pin at V REF_ILIM_HIZ . If pin voltage exceeds
V REF_ILIM_HIZ, the device enters input current regulation. Entering input current regulation through the pin sets
the IAC_DPM_STAT and FLAG bits, and produces an interrupt to host. The interrupt can be masked via the
IAC_DPM_MASK bit.


The ILIM_HIZ pin can also be used to monitor input current. When not in input current regulation, the voltage on
ILIM_HIZ pin (V ILIM_HIZ ) is proportional to the input current. Pin voltage can be used to monitor input current with
the following relationship: IAC = K ILIM x V ILIM_HIZ / (R ILIM_HIZ x V REF_ILIM_HIZ ).


For example, if the pin is set with 5-kΩ resistor, and the pin voltage is 1.0 V, the actual input current is between
4.8 A to 5.2 A (based on K ILIM specified).


If ILIM_HIZ pin is shorted, the input current limit is set by the IAC_DPM register. If hardware input current limit
function is not needed, it is recommended to short this pin to GND. If ILIM_HIZ pin is pulled above V IH_ILIM_HIZ,
the device enters HIZ mode (refer to Section 8.3.3.5). The ILIM_HIZ pin function can be disabled by setting the
EN_ILIM_HIZ_PIN bit to 0. When the pin is disabled, input current limit and monitoring functions as well as HIZ
mode control via the pin are not available.


**8.3.5.1.2 Input Voltage Regulation**


In addition to input current regulation, the device also offers input voltage regulation to limit the input power. This
is especially useful when dealing with input sources such as solar panels, where the operating voltage must be
controlled to extract the maximum power. Alternatively, if the input source current limitation is not known, input
voltage regulation can be used to limit the power draw from the input source. By using input voltage regulation,
the battery charger reduces the charging current when the input voltage falls below the input voltage limit set by
the higher of VAC_DPM register bits, or ACUV pin.


There are two thresholds to limit the input voltage (the higher limit of these will apply)
1. VAC_DPM register bits (host software control)
2. ACUV pin falling threshold (hardware control)


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 31


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


To set the minimum input voltage using the VAC_DPM register bits, write the desired value directly to the
VAC_DPM register bits. The default VAC_DPM is set to minimum code, allowing ACUV pin to limit the input
voltage in hardware.


To set the minimum input voltage using the ACUV pin, refer to Section 8.3.3.1.


_**8.3.5.1.2.1 Max Power Point Tracking (MPPT) for Solar PV Panel**_


When EN_MPPT bit is 1, the device provides a maximum power point tracking (MPPT) algorithm for solar PV
panel input sources. The Input Power Maximizer algorithm finds and tracks the maximum power point by full
panel sweep.


The full panel sweep is used to find the input operating voltage which delivers the maximum charge current
to the battery. Before running a full panel sweep, the device momentarily enters HIZ mode to measure input
source open-circuit voltage (V OC ). The device proceeds to reduce the input voltage regulation target, measuring
the charge current output at each setting. The VAC_DPM register is used to program the minimum voltage
to exit the full panel sweep. After the sweep is complete, the device updates the VAC_MPP register to the
input voltage regulation value producing the maximum charge current. The device then waits for a period of
FULL_SWEEP_TMR[1:0] before performing a new full panel sweep. A full panel sweep can be forced at any
time by setting the FORCE_SWEEP bit to 1. Note that EN_MPPT = 1 is required for FORCE_SWEEP to work.
The FORCE_SWEEP bit is automatically cleared to 0 after the full panel sweep is completed. Note that the
device uses the internal ADC to determine the charge current at each step of the full panel sweep, therefore
writes to the IBAT_ADC_DIS bit are ignored while MPPT is enabled (EN_MPPT = 1).


Note that when the system is directly connected to the input supply, the device cannot limit the system load.
Therefore, the MPPT algorithm may not find and track the true MPP under all conditions. To enable MPPT
operation, it is recommended to connect the system load directly in parallel to the battery pack.


**8.3.6 Reverse Mode Power Direction**


The device supports buck-boost reverse power direction to deliver power from the battery to the system when
the adapter is not present. During this mode of operation, the ACFET and BATFET both remain off. The reverse
mode output voltage regulation is set in VSYS_REV register bits. The reverse mode also offers output current
regulation via the R AC_SNS resistor. This parameter is controlled by the IAC_REV register bits. The reverse mode
operation can be enabled if the following conditions are valid:

1. SRN above 3 V.
2. DRV_SUP voltage within valid operating window (V DRV_UVP < V DRV < V DRV_OVP .
3. VAC outside the ACOV / ACUV operating window, or V VAC < V VAC_OK, or V VAC - V VAC_INT_OV
4. Reverse mode operation is enabled (EN_REV = 1)
5. Voltage at TS (thermistor) pin is within range configured by Reverse Temperature Monitor as configured by
BHOT and BCOLD register bits


While the reverse mode is active, the device sets the REVERSE_STAT bit to 1. Host can disable the reverse
operation at any time by setting EN_REV bit to 0. The device disables the converter, and turns the BATFET on to
connect the battery directly to the system.


The charger also monitors and regulates the battery discharging current in reverse mode. When the battery
discharge current rises above the IBAT_REV register setting, the charger reduces the reverse mode power flow
to limit the discharge current.


Once a valid VAC voltage is detected for forward operation, the device automatically disables reverse mode
(EN_REV = 0), turns on the ACFETs and proceeds to charge the battery if enabled.


_**8.3.6.1 Auto Reverse Mode**_


In some applications, a regulated system voltage is required when the adapter power is removed. The BQ25750
integrates an auto-reverse function which provides a regulated system voltage using the buck-boost converter in
reverse direction once the input power is removed.


32 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



When enabled by setting the AUTO_REV register bit to 1, Auto Reverse mode can be used to provide a
regulated system voltage immediately after the input power is removed. The device transitions to reverse mode
with the BATFET off and the converter on when the input falls below the ACUV threshold.







V SYS_REV

V AC_DPM


(CC Mode) Reg

|Col1|VAC VSYS|Col3|Col4|Col5|
|---|---|---|---|---|
|DPM<br>AT<br>REV<br>CUV|VBAT||||
|DPM<br>AT<br>REV<br>CUV|VBAT||||
|DPM<br>AT<br>REV<br>CUV|VBAT||||
|DPM<br>AT<br>REV<br>CUV|||||
|DPM<br>AT<br>REV<br>CUV|||||
|DPM<br>AT<br>REV<br>CUV|||||
||Battery Charging|VAC_DPM<br>||SYS_REV Regulation<br>(Buck from BAT to SYS)|



Reverse

Mode ON


**Figure 8-6. Auto Reverse Mode if BAT > VSYS_REV When VAC is Removed**


While the Auto reverse mode is active, the device sets the REVERSE_STAT bit to 1. Host can disable the Auto
reverse operation at any time by setting EN_AUTO_REV = 0 and EN_REV = 0. The device then disables the
converter, and turns the BATFET on to connect the battery directly to the system.


**8.3.7 Integrated 16-Bit ADC for Monitoring**


The device includes a 16-bit ADC to monitor critical system information based on the device’s modes of
operation. The ADC is allowed to operate if either the V VAC >V VAC_OK or VBAT>V REGN_OK is valid. The ADC_EN
bit provides the ability to enable and disable the ADC to conserve power. The ADC_RATE bit allows continuous
conversion or one-shot behavior. After a one-shot conversion finishes, the ADC_EN bit is cleared, and must be
re-asserted to start a new conversion.


The ADC_SAMPLE bits control the resolution and sample speed of the ADC. By default, ADC channels will be
converted in one-shot or continuous conversion mode unless disabled in the ADC Function Disable register. If
an ADC parameter is disabled by setting the corresponding bit, then the read-back value in the corresponding
register will be from the last valid ADC conversion or the default POR value (all zeros if no conversions have
taken place). If an ADC parameter is disabled in the middle of an ADC measurement cycle, the device will finish
the conversion of that parameter, but will not convert the parameter starting the next conversion cycle. If all
channels are disabled in one-shot conversion mode, the ADC_EN bit is cleared.


The ADC_DONE_STAT and ADC_DONE_FLAG bits signal when a conversion is complete in one-shot mode
only. This event produces an INT pulse, which can be masked with ADC_DONE_MASK. During continuous
conversion mode, the ADC_DONE_STAT bit has no meaning and will be '0'. The ADC_DONE_FLAG bit will
remain unchanged in continuous conversion mode.


ADC conversion operates independently of the faults present in the device. ADC conversion will continue even
after a fault has occurred (such as one that causes the power stage to be disabled), and the host must set


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 33


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


ADC_EN = ‘0’ to disable the ADC. ADC readings are only valid for DC states and not for transients. When host
writes ADC_EN = 0, the ADC stops immediately, and ADC measurement values correspond to last valid ADC
reading.


If the host wants to exit ADC more gracefully, it is possible to do either of the following:
1. Write ADC_RATE to one-shot, and the ADC will stop at the end of a complete cycle of conversions, or
2. Disable all ADC conversion channels, and the ADC will stop at the end of the current measurement.


When system load is powered from the battery (input source is removed, or device in HIZ mode), enabling the
ADC automatically powers up REGN and increases the quiescent current. To keep the battery leakage low, it is
recommended to duty cycle or completely disable the ADC.


**8.3.8 Status Outputs (PG, STAT1, STAT2, and INT)**

_**8.3.8.1 Power Good Indicator (PG)**_


The PG_STAT bit goes HIGH and the PG pin pulls LOW to indicate a good input source when a valid VAC
voltage is detected. The PG pin can drive an LED. All conditions must be met to indicate power good:
1. V VAC_OK < V VAC < V VAC_INT_OV
2. V ACUV - V REF_ACUV
3. V ACOV < V REF_ACOV
4. Device not in HIZ mode


The PG pin can be disabled via the DIS_PG_PIN bit. When disabled, this pin can be controlled to pull LOW
using the FORCE_STAT3_ON bit.


_**8.3.8.2 Charging Status Indicator (STAT1, STAT2 Pins)**_


The device indicates charging state on the open drain STAT1 and STAT2 pins. The STAT1, STAT2 pins can drive
LEDs.


**Table 8-6. STAT1, STAT2 Pin State**

|CHARGING STATE|STAT1|STAT2|
|---|---|---|
|Charge in progress (including recharge)|ON|OFF|
|Charge done|OFF|ON|
|Charging fault detected (TS out of range, safety timer fault,<br>etc.)|ON|ON|
|Charge disabled (EN_CHG = 0, or~~CE~~pin high)|OFF|OFF|



The STAT1, STAT2 pin function can be disabled via the DIS_STAT_PINS bit. When disabled, these pins can
be controlled to independently pull LOW using the FORCE_STAT1_ON and FORCE_STAT2_ON bits. The STAT
pins are not affected by the Reverse mode and remain OFF during this mode.


_**8.3.8.3 Interrupt to Host (INT)**_


In some applications, the host does not always monitor the charger operation. The INT pin notifies the system
host on the device operation. By default, the following events will generate an active-low, 256-µs INT pulse.


1. Valid input source conditions detected (see conditions for PG pin)
2. Valid input source conditions removed (see conditions for PG pin)
3. Entering IAC_DPM regulation through register or ILIM_HIZ pin
4. Entering VAC_DPM regulation through register or ACUV pin
5. I [2] C Watchdog timer expired
6. Charger status changes state (CHARGE_STAT value change), including Charge Complete
7. TS_STAT changes state (TS_STAT value change)
8. Junction temperature shutdown (TSHUT)
9. Battery overvoltage detected (BATOVP)
10. Charge safety timer expired (including pre-charge or CV timer expiration)
11. A rising edge on any of the *_STAT bits


34 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



Each one of these INT sources can be masked off to prevent INT pulses from being sent out when they occur.
Three bits exist for each one of these events:

 - The STAT bit holds the _current status_ of each INT source

 - The FLAG bit holds information on which source produced an INT, regardless of the current status

 - The MASK bit is used to prevent the device from sending out INT for each particular event


When one of the above conditions occurs (a rising edge on any of the *_STAT bits), the device sends out an
INT pulse and keeps track of which source generated the INT via the FLAG registers. The FLAG register bits are
automatically reset to zero after the host reads them, and a new edge on STAT bit is required to re-assert the
FLAG.


IAC_DPM_STAT


IAC_DPM_FLAG


TS_STAT


TS_FLAG


/INT


I2C Flag Read


**Figure 8-7. INT Generation Behavior Example**


**8.3.9 Serial Interface**


The device uses I [2] C compatible interface for flexible charging parameter programming and instantaneous device
status reporting. I [2] C is a bi-directional 2-wire serial interface. Only two open-drain bus lines are required: a
serial data line (SDA), and a serial clock line (SCL). Devices can be considered as controllers or targets when
performing data transfers. A controller is a device which initiates a data transfer on the bus and generates the
clock signals to permit that transfer. At that time, any device addressed is considered a target.


The device operates as a target device with address 0x6B, receiving control inputs from the controller device like
a micro-controller or digital signal processor through the registers defined in the Register Map. Registers read
outside those defined in the map, return 0xFF. The I [2] C interface supports standard mode (up to 100 kbits/s), fast
mode (up to 400 kbits/s), and fast mode plus (up to 1 Mbit/s). When the bus is free, both lines are HIGH. The
SDA and SCL pins are open drain and must be connected to the positive supply voltage via a current source or
pull-up resistor.


**System Note:** All 16-bit registers are defined as Little Endian, with the most-significant byte allocated to the
higher address. 16-bit register writes must be done sequentially and are recommended to be programmed using
multi-write approach described in the Section 8.3.9.7.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 35


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


_**8.3.9.1 Data Validity**_


The data on the SDA line must be stable during the HIGH period of the clock. The HIGH or LOW state of the
data line can only change when the clock signal on SCL line is LOW. One clock pulse is generated for each data
bit transferred.


SDA


SCL

data allowed


**Figure 8-8. Bit Transfers on the I** **[2]** **C Bus**


_**8.3.9.2 START and STOP Conditions**_


All transactions begin with a START (S) and are terminated with a STOP (P). A HIGH to LOW transition on the
SDA line while SCL is HIGH defines a START condition. A LOW to HIGH transition on the SDA line when the

SCL is HIGH defines a STOP condition.


START and STOP conditions are always generated by the controller. The bus is considered busy after the
START condition, and free after the STOP condition. When timeout condition is met, for example START
condition is active for more than 2 seconds and there is no STOP condition triggered, the charger I [2] C
communication will automatically reset and communication lines are free for another transmission.



SDA


SCL

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||||||S|
|||||||
|||||||



_**8.3.9.3 Byte Format**_



SDA


SCL



START (S) STOP (P)


**Figure 8-9. START and STOP Conditions on the I** **[2]** **C Bus**



Every byte on the SDA line must be 8 bits long. The number of bytes to be transmitted per transfer is
unrestricted. Each byte has to be followed by an ACKNOWLEDGE (ACK) bit. Data is transferred with the
Most Significant Bit (MSB) first. If a target cannot receive or transmit another complete byte of data until it
has performed some other function, it can hold the SCL line low to force the controller into a wait state (clock
stretching). Data transfer then continues when the target is ready for another byte of data and releases the SCL
line.


36 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**





**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)





|Col1|Col2|Acknowledgement signal from target Acknowledgement signal from target|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|1<br>2<br>7<br>8<br>9<br>MSB<br>signal from target<br>1<br>2<br>8<br>9<br>|||
|DA|DA|DA|||||||||
|DA|DA|DA|||||||P or Sr|P or Sr|
|CL|S or Sr||||||||||


STOP or

Repeated
START







ACK



START or

Repeated
START



ACK



**Figure 8-10. Data Transfer on the I** **[2]** **C Bus**


_**8.3.9.4 Acknowledge (ACK) and Not Acknowledge (NACK)**_


The ACK signaling takes place after byte. The ACK bit allows the target to signal the controller that the byte was
successfully received and another byte may be sent. All clock pulses, including the acknowledge 9 [th] clock pulse,
are generated by the controller.


The controller releases the SDA line during the acknowledge clock pulse so the target can pull the SDA line
LOW and it remains stable LOW during the HIGH period of this 9 [th] clock pulse.


A NACK is signaled when the SDA line remains HIGH during the 9 [th] clock pulse. The controller can then
generate either a STOP to abort the transfer or a repeated START to start a new transfer.


_**8.3.9.5 Target Address and Data Direction Bit**_


After the START signal, a target address is sent. This address is 7 bits long, followed by the 8 bit as a data
direction bit (bit R/ W). A zero indicates a transmission (WRITE) and a one indicates a request for data (READ).
The device 7-bit address is defined as 1101 011' (0x6B) by default.


SDA







SCL




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|A|||||||||||||||||
||||1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|1-7<br>8<br>9<br>1-7<br>8<br>9<br>1-7<br>8<br>9|||
|L|S|S|S|S|S|S|S|S|S|S|S|S|S|S|P||



ACK



START



ADDRESS R/W ACK DATA ACK DATA ACK



ACK



**Figure 8-11. Complete Data Transfer on the I** **[2]** **C Bus**


_**8.3.9.6 Single Write and Read**_


**Figure 8-12. Single Write**



STOP







**Figure 8-13. Single Read**


If the register address is not defined, the charger IC sends back NACK and returns to the idle state.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 37


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


_**8.3.9.7 Multi-Write and Multi-Read**_


The charger device supports multi-read and multi-write of all registers.





**Figure 8-14. Multi-Write**







**Figure 8-15. Multi-Read**


**8.4 Device Functional Modes**


**8.4.1 Host Mode and Default Mode**





The device is a host controlled charger, but it can operate in default mode without host management. In default
mode, the device can be used as an autonomous charger with no host or while host is in sleep mode. When the
charger is in default mode, WD_STAT bit becomes HIGH, WD_FLAG is set to 1, and a INT is asserted low to
alert the host (unless masked by WD_MASK). The WD_FLAG bit would read as a '1' upon the first read and then
'0' upon subsequent reads. When the charger is in host mode, WD_STAT bit is LOW.


After power-on-reset, the device starts in default mode with watchdog timer expired. All the registers are in the
default settings.


In default mode, the device keeps charging the battery with default 2-hour pre-charging safety timer and the
12-hour fast charging safety timer. At the end of the 2-hour or 12-hour timer expiration, the charging is stopped if
termination has not been detected.


A write to any I [2] C register transitions the charger from default mode to host mode, and initiates the watchdog
timer. All the device parameters can be programmed by the host. To keep the device in host mode, the host has
to reset the watchdog timer by writing 1 to WD_RST bit before the watchdog timer expires (WD_STAT bit is set),
or disable watchdog timer by setting WATCHDOG bits = 00.


When the watchdog timer is expired, the device returns to default mode and select registers are reset to default
values as detailed in the Register Map section. The Watchdog timer will be reset on any write if the watchdog
timer has expired. When watchdog timer expires, WD_STAT and WD_FLAG is set to 1, and /INT is asserted low
to alert the host (unless masked by WD_MASK).


38 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**8.4.2 Register Bit Reset**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)

























**Figure 8-16. Watchdog Timer Flow Chart**



Beside the register reset by the watchdog timer in the default mode, the register and the timer could be reset
to the default value by writing the REG_RST bit to 1. The register bits which can be reset by the REG_RST
bit, are noted in the Register Map section. After the register reset, the REG_RST bit will go back from 1 to 0
automatically.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 39


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**8.5 BQ25750 Registers**


Table 8-7 lists the memory-mapped registers for the BQ25750 registers. All register offset addresses not listed in
Table 8-7 should be considered as reserved locations and the register contents should not be modified.


**Table 8-7. BQ25750 Registers**


**Address** **Acronym** **Register Name** **Section**


0x0 REG0x00_Charge_Voltage_Limit Charge Voltage Limit Go


0x2 REG0x02_Charge_Current_Limit Charge Current Limit Go


0x6 REG0x06_Input_Current_DPM_Limit Input Current DPM Limit Go


0x8 REG0x08_Input_Voltage_DPM_Limit Input Voltage DPM Limit Go


0xA REG0x0A_Reverse_Mode_Input_Current_Limit Reverse Mode Input Current Limit Go


0xC REG0x0C_Reverse_Mode_System_Voltage_Limit Reverse Mode System Voltage Limit Go


0x10 REG0x10_Precharge_Current_Limit Precharge Current Limit Go


0x12 REG0x12_Termination_Current_Limit Termination Current Limit Go


0x14 REG0x14_Precharge_and_Termination_Control Precharge and Termination Control Go


0x15 REG0x15_Timer_Control Timer Control Go


0x16 REG0x16_Three-Stage_Charge_Control Three-Stage Charge Control Go


0x17 REG0x17_Charger_Control Charger Control Go


0x18 REG0x18_Pin_Control Pin Control Go


0x19 REG0x19_Power_Path_and_Reverse_Mode_Control Power Path and Reverse Mode Control Go


0x1A REG0x1A_MPPT_Control MPPT Control Go


0x1B REG0x1B_TS_Charging_Threshold_Control TS Charging Threshold Control Go


0x1C REG0x1C_TS_Charging_Region_Behavior_Control TS Charging Region Behavior Control Go


0x1D REG0x1D_TS_Reverse_Mode_Threshold_Control TS Reverse Mode Threshold Control Go


0x1E REG0x1E_Reverse_Undervoltage_Control Reverse Undervoltage Control Go


0x1F REG0x1F_VAC_Max_Power_Point_Detected VAC Max Power Point Detected Go


0x21 REG0x21_Charger_Status_1 Charger Status 1 Go


0x22 REG0x22_Charger_Status_2 Charger Status 2 Go


0x23 REG0x23_Charger_Status_3 Charger Status 3 Go


0x24 REG0x24_Fault_Status Fault Status Go


0x25 REG0x25_Charger_Flag_1 Charger Flag 1 Go


0x26 REG0x26_Charger_Flag_2 Charger Flag 2 Go


0x27 REG0x27_Fault_Flag Fault Flag Go


0x28 REG0x28_Charger_Mask_1 Charger Mask 1 Go


0x29 REG0x29_Charger_Mask_2 Charger Mask 2 Go


0x2A REG0x2A_Fault_Mask Fault Mask Go


0x2B REG0x2B_ADC_Control ADC Control Go


0x2C REG0x2C_ADC_Channel_Control ADC Channel Control Go


0x2D REG0x2D_IAC_ADC IAC ADC Go


0x2F REG0x2F_IBAT_ADC IBAT ADC Go


0x31 REG0x31_VAC_ADC VAC ADC Go


0x33 REG0x33_VBAT_ADC VBAT ADC Go


0x35 REG0x35_VSYS_ADC VSYS ADC Go


0x37 REG0x37_TS_ADC TS ADC Go


0x39 REG0x39_VFB_ADC VFB ADC Go


0x3B REG0x3B_Gate_Driver_Strength_Control Gate Driver Strength Control Go


0x3C REG0x3C_Gate_Driver_Dead_Time_Control Gate Driver Dead Time Control Go


40 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 8-7. BQ25750 Registers (continued)**





Complex bit access types are encoded to fit into small table cells. Table 8-8 shows the codes that are used for
access types in this section.


**Table 8-8. BQ25750 Access Type Codes**

|Access Type|Code|Description|
|---|---|---|
|Read Type|Read Type|Read Type|
|R|R|Read|
|Write Type|Write Type|Write Type|
|W|W|Write|
|Reset or Default Value|Reset or Default Value|Reset or Default Value|
|-_n_||Value after reset or the default<br>value|



**8.5.1 REG0x00_Charge_Voltage_Limit Register (Address = 0x0) [Reset = 0x0010]**


REG0x00_Charge_Voltage_Limit is shown in Table 8-9.


Return to the Summary Table.


I2C REG0x01=[15:8], I2C REG0x00=[7:0]


**Table 8-9. REG0x00_Charge_Voltage_Limit Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:5|RESERVED|R|0x0||Reserved|
|4:0|VFB_REG|R/W|0x10|Reset by:<br>REG_RESET|FB Voltage Regulation Limit:<br>POR: 1536mV (10h)<br>Range: 1504mV-1566mV (0h-1Fh)<br>Bit Step: 2mV<br>Offset: 1504mV|



**8.5.2 REG0x02_Charge_Current_Limit Register (Address = 0x2) [Reset = 0x0640]**


REG0x02_Charge_Current_Limit is shown in Table 8-10.


Return to the Summary Table.


I2C REG0x03=[15:8], I2C REG0x02=[7:0]


**Table 8-10. REG0x02_Charge_Current_Limit Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:11|RESERVED|R|0x0||Reserved|
|10:2|ICHG_REG|R/W|0x190|Reset by:<br>REG_RESET<br>WATCHDOG|Fast Charge Current Regulation Limit with 5mΩ<br>RBAT_SNS:<br>Actual charge current is the lower of ICHG_REG and<br>ICHG pin<br>POR: 20000mA (190h)<br>Range: 400mA-20000mA (8h-190h)<br>Clamped Low<br>Clamped High<br>Bit Step: 50mA|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 41


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-10. REG0x02_Charge_Current_Limit Register Field Descriptions (continued)**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|1:0|RESERVED|R|0x0||Reserved|



**8.5.3 REG0x06_Input_Current_DPM_Limit Register (Address = 0x6) [Reset = 0x0640]**


REG0x06_Input_Current_DPM_Limit is shown in Table 8-11.


Return to the Summary Table.


I2C REG0x07=[15:8], I2C REG0x06=[7:0]


**Table 8-11. REG0x06_Input_Current_DPM_Limit Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:11|RESERVED|R|0x0||Reserved|
|10:2|IAC_DPM|R/W|0x190|Reset by:<br>REG_RESET|Input Current DPM Regulation Limit with 2mΩ<br>RAC_SNS:<br>Actual input current limit is the lower of IAC_DPM and<br>ILIM_HIZ pin<br>POR: 50000mA (190h)<br>Range: 1000mA-50000mA (8h-190h)<br>Clamped Low<br>Clamped High<br>Bit Step: 125mA|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.4 REG0x08_Input_Voltage_DPM_Limit Register (Address = 0x8) [Reset = 0x0348]**


REG0x08_Input_Voltage_DPM_Limit is shown in Table 8-12.


Return to the Summary Table.


I2C REG0x09=[15:8], I2C REG0x08=[7:0]


**Table 8-12. REG0x08_Input_Voltage_DPM_Limit Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:14|RESERVED|R|0x0||Reserved|
|13:2|VAC_DPM|R/W|0xD2|Reset by:<br>REG_RESET|Input Voltage Regulation Limit:<br>Note if EN_MPPT = 1, the Full Sweep method will use<br>this limit as the lower search window for Full Panel<br>Sweep<br>POR: 4200mV (D2h)<br>Range: 4200mV-65000mV (D2h-CB2h)<br>Clamped Low<br>Clamped High<br>Bit Step: 20mV|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.5 REG0x0A_Reverse_Mode_Input_Current_Limit Register (Address = 0xA) [Reset = 0x0640]**


REG0x0A_Reverse_Mode_Input_Current_Limit is shown in Table 8-13.


Return to the Summary Table.


I2C REG0x0B=[15:8], I2C REG0x0A=[7:0]


42 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


**Table 8-13. REG0x0A_Reverse_Mode_Input_Current_Limit Register Field Descriptions**









|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:11|RESERVED|R|0x0||Reserved|
|10:2|IAC_REV|R/W|0x190|Reset by:<br>REG_RESET|Input Current Regulation in Reverse Mode with 2mΩ<br>RAC_SNS:<br>POR: 50000mA (190h)<br>Range: 1000mA-50000mA (8h-190h)<br>Clamped Low<br>Clamped High<br>Bit Step: 125mA|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.6 REG0x0C_Reverse_Mode_System_Voltage_Limit Register (Address = 0xC) [Reset = 0x03E8]**


REG0x0C_Reverse_Mode_System_Voltage_Limit is shown in Table 8-14.


Return to the Summary Table.


I2C REG0x0D=[15:8], I2C REG0x0C=[7:0]


**Table 8-14. REG0x0C_Reverse_Mode_System_Voltage_Limit Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:14|RESERVED|R|0x0||Reserved|
|13:2|VSYS_REV|R/W|0xFA|Reset by:<br>REG_RESET|System Voltage Regulation in Reverse Mode:<br>POR: 5000mV (FAh)<br>Range: 3300mV-65000mV (A5h-CB2h)<br>Clamped Low<br>Clamped High<br>Bit Step: 20mV|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.7 REG0x10_Precharge_Current_Limit Register (Address = 0x10) [Reset = 0x0140]**


REG0x10_Precharge_Current_Limit is shown in Table 8-15.


Return to the Summary Table.


I2C REG0x11=[15:8], I2C REG0x10=[7:0]


**Table 8-15. REG0x10_Precharge_Current_Limit Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:10|RESERVED|R|0x0||Reserved|
|9:2|IPRECHG|R/W|0x50|Actual pre-charge current<br>is the lower of IPRECHG<br>and ICHG pin<br>Reset by:<br>REG_RESET|Pre-charge current regulation limit with 5mΩ<br>RBAT_SNS:<br>POR: 4000mA (50h)<br>Range: 250mA-10000mA (5h-C8h)<br>Clamped Low<br>Clamped High<br>Bit Step: 50mA|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.8 REG0x12_Termination_Current_Limit Register (Address = 0x12) [Reset = 0x00A0]**


REG0x12_Termination_Current_Limit is shown in Table 8-16.


Return to the Summary Table.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 43


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


I2C REG0x13=[15:8], I2C REG0x12=[7:0]


**Table 8-16. REG0x12_Termination_Current_Limit Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:10|RESERVED|R|0x0||Reserved|
|9:2|ITERM|R/W|0x28|Actual termination current<br>is the lower of ITERM and<br>ICHG pin if both functions<br>enabled<br>Reset by:<br>REG_RESET|Termination Current Threshold with 5mΩ RBAT_SNS:<br>POR: 2000mA (28h)<br>Range: 250mA-10000mA (5h-C8h)<br>Clamped Low<br>Clamped High<br>Bit Step: 50mA|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.9 REG0x14_Precharge_and_Termination_Control Register (Address = 0x14) [Reset = 0x0F]**


REG0x14_Precharge_and_Termination_Control is shown in Table 8-17.


Return to the Summary Table.


**Table 8-17. REG0x14_Precharge_and_Termination_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:4|RESERVED|R|0x0||Reserved|
|3|EN_TERM|R/W|0x1|Reset by:<br>REG_RESET|Enable termination control<br>0b = Disable<br>1b = Enable|
|2:1|VBAT_LOWV|R/W|0x3|Reset by:<br>REG_RESET|Battery threshold for PRECHG to FASTCHG transition,<br>as percentage of VFB_REG:<br>00b = 30% x VFB_REG<br>01b = 55% x VFB_REG<br>10b = 66.7% x VFB_REG<br>11b = 71.4% x VFB_REG|
|0|EN_PRECHG|R/W|0x1|Reset by:<br>REG_RESET|Enable pre-charge and trickle charge functions:<br>0b = Disable<br>1b = Enable|



**8.5.10 REG0x15_Timer_Control Register (Address = 0x15) [Reset = 0x1D]**


REG0x15_Timer_Control is shown in Table 8-18.


Return to the Summary Table.


**Table 8-18. REG0x15_Timer_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|TOPOFF_TMR|R/W|0x0|Reset by:<br>REG_RESET|Top-off timer control:<br>00b = Disable<br>01b = 15 mins<br>10b = 30 mins<br>11b = 45 mins|
|5:4|WATCHDOG|R/W|0x1|Reset by:<br>REG_RESET|Watchdog timer control:<br>00b = Disable<br>01b = 40s<br>10b = 80s<br>11b = 160s|
|3|EN_CHG_TMR|R/W|0x1|Reset by:<br>REG_RESET<br>WATCHDOG|Enable charge safety timer:<br>0b = Disable<br>1b = Enable|



44 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


**Table 8-18. REG0x15_Timer_Control Register Field Descriptions (continued)**








|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|2:1|CHG_TMR|R/W|0x2|Reset by:<br>REG_RESET|Charge safety timer setting:<br>00b = 5hr<br>01b = 8hr<br>10b = 12hr<br>11b = 24hr|
|0|EN_TMR2X|R/W|0x1|Reset by:<br>REG_RESET|Charge safety timer speed in DPM:<br>0b = Timer always counts normally<br>1b = Timer slowed by 2x during input DPM|



**8.5.11 REG0x16_Three-Stage_Charge_Control Register (Address = 0x16) [Reset = 0x00]**


REG0x16_Three-Stage_Charge_Control is shown in Table 8-19.


Return to the Summary Table.


**Table 8-19. REG0x16_Three-Stage_Charge_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|RESERVED|R|0x0||Reserved|
|5|RESERVED|R|0x0||Reserved|
|4|RESERVED|R|0x0||Reserved|
|3:0|CV_TMR|R/W|0x0|Reset by:<br>REG_RESET<br>WATCHDOG|CV timer setting:<br>0000b = disable<br>0001b = 1hr<br>0010b = 2hr<br>... = ...<br>1110b = 14hr<br>1111b = 15hr|



**8.5.12 REG0x17_Charger_Control Register (Address = 0x17) [Reset = 0xC9]**


REG0x17_Charger_Control is shown in Table 8-20.


Return to the Summary Table.


**Table 8-20. REG0x17_Charger_Control Register Field Descriptions**










|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|VRECHG|R/W|0x3|Reset by:<br>REG_RESET|Battery auto-recharge threshold, as percentage of<br>VFB_REG:<br>00b = 93.0% x VFB_REG<br>01b = 94.3% x VFB_REG<br>10b = 95.2% x VFB_REG<br>11b = 97.6% x VFB_REG|
|5|WD_RST|R/W|0x0|Reset by:<br>REG_RESET|I2C Watchdog timer reset control:<br>0b = Normal<br>1b = Reset (bit goes back to 0 after timer reset)|
|4|DIS_CE_PIN|R/W|0x0|Reset by:<br>REG_RESET|/CE pin function disable:<br>0b = /CE pin enabled<br>1b = /CE pin disabled|
|3|EN_CHG_BIT_RES<br>ET_BEHAVIOR|R/W|0x1|Reset by:<br>REG_RESET|Controls the EN_CHG bit behavior when WATCHDOG<br>expires:<br>0b = EN_CHG bit resets to 0<br>1b = EN_CHG bit resets to 1|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 45


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-20. REG0x17_Charger_Control Register Field Descriptions (continued)**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|2|EN_HIZ|R/W|0x0|Reset by:<br>REG_RESET<br>WATCHDOG<br>Adapter Plug In|HIZ mode enable:<br>0b = Disable<br>1b = Enable|
|1|EN_IBAT_LOAD|R/W|0x0|Sinks current from SRN<br>to GND. Recommend<br>to disable IBAT ADC<br>(IBAT_ADC_DIS = 1)<br>while this bit is active.<br>Reset by:<br>REG_RESET<br>WATCHDOG|Battery Load (IBAT_LOAD) Enable:<br>0b = Disabled<br>1b = Enabled|
|0|EN_CHG|R/W|0x1|Reset by:<br>REG_RESET<br>WATCHDOG|Charge enable control:<br>0b = Disable<br>1b = Enable|



**8.5.13 REG0x18_Pin_Control Register (Address = 0x18) [Reset = 0xC0]**


REG0x18_Pin_Control is shown in Table 8-21.


Return to the Summary Table.


**Table 8-21. REG0x18_Pin_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|EN_ICHG_PIN|R/W|0x1|Reset by:<br>REG_RESET<br>WATCHDOG|ICHG pin function enable:<br>0b = ICHG pin disabled<br>1b = ICHG pin enabled|
|6|EN_ILIM_HIZ_PIN|R/W|0x1|Reset by:<br>REG_RESET<br>WATCHDOG|ILIM_HIZ pin function enable:<br>0b = ILIM_HIZ pin disabled<br>1b = ILIM_HIZ pin enabled|
|5|DIS_PG_PIN|R/W|0x0|Reset by:<br>REG_RESET|PG pin function disable:<br>0b = PG pin enabled<br>1b = PG pin disabled|
|4|DIS_STAT_PINS|R/W|0x0|Reset by:<br>REG_RESET|STAT1, STAT2 pin function disable:<br>0b = STAT pins enabled<br>1b = STAT pins disabled|
|3|FORCE_STAT4_ON|R/W|0x0|Reset by:<br>REG_RESET|CE_STAT4 pin override:<br>Can only be forced on if DIS_CE_PIN = 1<br>0b = CE_STAT4 open-drain off<br>1b = CE_STAT4 pulls LOW|
|2|FORCE_STAT3_ON|R/W|0x0|Reset by:<br>REG_RESET|PG_STAT3 pin override:<br>Can only be forced on if DIS_PG_PIN = 1<br>0b = PG_STAT3 open-drain off<br>1b = PG_STAT3 pulls LOW|
|1|FORCE_STAT2_ON|R/W|0x0|Reset by:<br>REG_RESET|STAT2 pin override:<br>Can only be forced on if DIS_STAT_PINS = 1<br>0b = STAT2 open-drain off<br>1b = STAT2 pulls LOW|
|0|FORCE_STAT1_ON|R/W|0x0|Reset by:<br>REG_RESET|STAT1 pin override:<br>Can only be forced on if DIS_STAT_PINS = 1<br>0b = STAT1 open-drain off<br>1b = STAT1 pulls LOW|



46 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**8.5.14 REG0x19_Power_Path_and_Reverse_Mode_Control Register (Address = 0x19) [Reset = 0x20]**


REG0x19_Power_Path_and_Reverse_Mode_Control is shown in Table 8-22.


Return to the Summary Table.


**Table 8-22. REG0x19_Power_Path_and_Reverse_Mode_Control Register Field Descriptions**












|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|REG_RST|R/W|0x0|Reset by:<br>REG_RESET|Register reset to default values:<br>0b = Not reset<br>1b = Reset (bit goes back to 0 after register reset)|
|6|EN_IAC_LOAD|R/W|0x0|Reset by:<br>REG_RESET<br>WATCHDOG|VAC Load (IAC_LOAD) Enable:<br>0b = Disabled<br>1b = Enabled|
|5|EN_PFM|R/W|0x1|It is recommended to<br>disable PFM when ITERM<br>< 2A<br>Reset by:<br>REG_RESET|Enable PFM mode in light-load:<br>Note this bit is reset upon a valid SYNC signal<br>detection on FSW_SYNC pin. Host can set this bit<br>back to 1 to force PFM operation even with a valid<br>SYNC input<br>0b = Disable (Fixed-frequency DCM operation)<br>1b = Enable (PFM operation)|
|4|FORCE_BATFET_O<br>FF|R/W|0x0|Reset by:<br>REG_RESET<br>Adapter Plug In|Force BATFET off control:<br>0b = Allow normal BATFET operation<br>1b = Force BATFET off|
|3|PWRPATH_REDUC<br>E_VDRV|R/W|0x0|Reset by:<br>REG_RESET<br>WATCHDOG|Power-Path (ACFET, BATFET) Drive Voltage Select:<br>0b = 10V<br>1b = 7V|
|2|EN_BATFET_IDEAL<br>_DIODE|R/W|0x0|Reset by:<br>REG_RESET|Enable BATFET ideal diode turn-on mode:<br>Note: Only recommended for single BATFET<br>0b = Disable<br>1b = Enable|
|1|EN_AUTO_REV|R/W|0x0|To exit reverse mode, it<br>is recommended to clear<br>both EN_AUTO_REV and<br>EN_REV bits<br>Reset by:<br>REG_RESET<br>WATCHDOG|Auto Reverse Mode to regulate SYS when VBAT <<br>VSYS_REV register:<br>0b = Disable Auto Reverse<br>1b = Enable Auto Reverse|
|0|EN_REV|R/W|0x0|To exit reverse mode, it<br>is recommended to clear<br>both EN_AUTO_REV and<br>EN_REV bits<br>Reset by:<br>REG_RESET<br>WATCHDOG<br>Adapter Plug In|Reverse Mode control:<br>0b = Disable<br>1b = Enable|



**8.5.15 REG0x1A_MPPT_Control Register (Address = 0x1A) [Reset = 0x20]**


REG0x1A_MPPT_Control is shown in Table 8-23.


Return to the Summary Table.


**Table 8-23. REG0x1A_MPPT_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|FORCE_SWEEP|R/W|0x0|Reset by:<br>REG_RESET|Force Full Panel Sweep and reset MPPT timers:<br>0b = Normal<br>1b = Start Full Panel Sweep (bit goes back to 0 after<br>Full Panel Sweep complete)|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 47


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-23. REG0x1A_MPPT_Control Register Field Descriptions (continued)**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|6:3|RESERVED|R|0x0||Reserved|
|2:1|FULL_SWEEP_TMR|R/W|0x0|Reset by:<br>REG_RESET|Full Panel Sweep timer control:<br>00b = 3 min<br>01b = 10 min<br>10b = 15 min<br>11b = 20 min|
|0|EN_MPPT|R/W|0x0|When MPPT is enabled,<br>the ADC is controlled<br>by the device, writes to<br>REG2A are ignored<br>Reset by:<br>REG_RESET|MPPT algorithm control:<br>0b = Disable MPPT<br>1b = Enable MPPT|



**8.5.16 REG0x1B_TS_Charging_Threshold_Control Register (Address = 0x1B) [Reset = 0x96]**


REG0x1B_TS_Charging_Threshold_Control is shown in Table 8-24.


Return to the Summary Table.


**Table 8-24. REG0x1B_TS_Charging_Threshold_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|TS_T5|R/W|0x2|Reset by:<br>REG_RESET|TS T5 (HOT) threshold control:<br>00b = 41.2% (50C)<br>01b = 37.7% (55C)<br>10b = 34.375% (60C)<br>11b = 31.25%(65C)|
|5:4|TS_T3|R/W|0x1|Reset by:<br>REG_RESET|JEITA TS T3 (WARM) threshold control:<br>00b = 48.4% (40C)<br>01b = 44.8% (45C)<br>10b = 41.2% (50C)<br>11b = 37.7% (55C)|
|3:2|TS_T2|R/W|0x1|Reset by:<br>REG_RESET|JEITA TS T2 (COOL) threshold control:<br>00b = 71.1% (5C)<br>01b = 68.4% (10C)<br>10b = 65.5% (15C)<br>11b = 62.4% (20C)|
|1:0|TS_T1|R/W|0x2|Reset by:<br>REG_RESET|TS T1 (COLD) threshold control:<br>00b = 77.15% (-10C)<br>01b = 75.32% (-5C)<br>10b = 73.25% (0C)<br>11b = 71.1% (5C)|



**8.5.17 REG0x1C_TS_Charging_Region_Behavior_Control Register (Address = 0x1C) [Reset = 0x57]**


REG0x1C_TS_Charging_Region_Behavior_Control is shown in Table 8-25.


Return to the Summary Table.


**Table 8-25. REG0x1C_TS_Charging_Region_Behavior_Control Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|RESERVED|R|0x0||Reserved|



48 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 8-25. REG0x1C_TS_Charging_Region_Behavior_Control Register Field Descriptions (continued)**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|6:5|JEITA_VSET|R/W|0x2|Reset by:<br>REG_RESET|JEITA Warm (T3 < TS < T5) regulation voltage setting,<br>as percentage of VFB_REG:<br>00b = Charge Suspend<br>01b = 94.3% x VFB_REG<br>10b = 97.6% x VFB_REG<br>11b = 100% x VFB_REG|
|4|JEITA_ISETH|R/W|0x1|Reset by:<br>REG_RESET|JEITA Warm (T3 < TS < T5) regulation current setting,<br>as percentage of ICHG_REG:<br>0b = 40% x ICHG_REG<br>1b = 100% x ICHG_REG|
|3:2|JEITA_ISETC|R/W|0x1|Reset by:<br>REG_RESET|JEITA Cool (T1 < TS < T2) regulation current setting,<br>as percentage of ICHG_REG:<br>00b = Charge Suspend<br>01b = 20% x ICHG_REG<br>10b = 40% x ICHG_REG<br>11b = 100% x ICHG_REG|
|1|EN_JEITA|R/W|0x1|EN_VREG_TEMP_COMP<br>and EN_JEITA cannot be<br>set to 1 at the same time.<br>Reset by:<br>REG_RESET|JEITA profile control:<br>0b = Disabled (COLD/HOT control only)<br>1b = Enabled (COLD/COOL/WARM/HOT control)|
|0|EN_TS|R/W|0x1|Reset by:<br>REG_RESET|TS pin function control (applies to forward charging<br>and reverse discharging modes):<br>0b = Disabled (ignore TS pin)<br>1b = Enabled|



**8.5.18 REG0x1D_TS_Reverse_Mode_Threshold_Control Register (Address = 0x1D) [Reset = 0x40]**


REG0x1D_TS_Reverse_Mode_Threshold_Control is shown in Table 8-26.


Return to the Summary Table.


**Table 8-26. REG0x1D_TS_Reverse_Mode_Threshold_Control Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|BHOT|R/W|0x1|Reset by:<br>REG_RESET|Reverse Mode TS HOT temperature threshold control:<br>00b = 37.7% (55C)<br>01b = 34.2% (60C)<br>10b = 31.25%(65C)<br>11b = Disable|
|5|BCOLD|R/W|0x0|Reset by:<br>REG_RESET|Reverse Mode TS COLD temperature threshold<br>control:<br>0b = 77.15% (-10C)<br>1b = 80% (-20C)|
|4:0|RESERVED|R|0x0||Reserved|


**8.5.19 REG0x1E_Reverse_Undervoltage_Control Register (Address = 0x1E) [Reset = 0x00]**


REG0x1E_Reverse_Undervoltage_Control is shown in Table 8-27.


Return to the Summary Table.


**Table 8-27. REG0x1E_Reverse_Undervoltage_Control Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|RESERVED|R|0x0||Reserved|
|6|RESERVED|R|0x0||Reserved|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 49


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-27. REG0x1E_Reverse_Undervoltage_Control Register Field Descriptions (continued)**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|5|SYSREV_UV|R/W|0x0|Reset by:<br>REG_RESET|Reverse Mode System UVP:<br>0b = 80% of VSYS_REV target<br>1b = Fixed at 3.3V|
|4|RESERVED|R|0x0||Reserved|
|3|RESERVED|R|0x0||Reserved|
|2|RESERVED|R|0x0||Reserved|
|1|RESERVED|R|0x0||Reserved|
|0|RESERVED|R|0x0||Reserved|


**8.5.20 REG0x1F_VAC_Max_Power_Point_Detected Register (Address = 0x1F) [Reset = 0x0000]**


REG0x1F_VAC_Max_Power_Point_Detected is shown in Table 8-28.


Return to the Summary Table.


I2C REG0x20=[15:8], I2C REG0x1F=[7:0]


**Table 8-28. REG0x1F_VAC_Max_Power_Point_Detected Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:14|RESERVED|R|0x0||Reserved|
|13:2|VAC_MPP|R|0x0||Input Voltage for Max Power Point detected:<br>POR: 0mV (0h)<br>Range: 0mV-60000mV (0h-BB8h)<br>Clamped High<br>Bit Step: 20mV|
|1:0|RESERVED|R|0x0||Reserved|



**8.5.21 REG0x21_Charger_Status_1 Register (Address = 0x21) [Reset = 0x00]**


REG0x21_Charger_Status_1 is shown in Table 8-29.


Return to the Summary Table.


**Table 8-29. REG0x21_Charger_Status_1 Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|ADC_DONE_STAT|R|0x0||ADC conversion status (in one-shot mode only):<br>0b = Conversion not complete<br>1b = Conversion complete|
|6|IAC_DPM_STAT|R|0x0||Input Current regulation status:<br>0b = Normal<br>1b = In Input Current regulation (ILIM pin or IAC_DPM)|
|5|VAC_DPM_STAT|R|0x0||Input Voltage regulation status:<br>0b = Normal<br>1b = In Input Voltage regulation (VAC_DPM or<br>VSYS_REV)|
|4|RESERVED|R|0x0||Reserved|
|3|WD_STAT|R|0x0||I2C Watchdog timer status:<br>0b = Normal<br>1b = WD timer expired|



50 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


**Table 8-29. REG0x21_Charger_Status_1 Register Field Descriptions (continued)**



|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|2:0|CHARGE_STAT|R|0x0||Charge cycle status:<br>000b = Not charging<br>001b = Trickle Charge (VBAT < VBAT_SHORT)<br>010b = Pre-Charge (VBAT < VBAT_LOWV)<br>011b = Fast Charge (CC mode)<br>100b = Taper Charge (CV mode)<br>101b = Reserved<br>110b = Top-off Timer Charge<br>111b = Charge Termination Done|


**8.5.22 REG0x22_Charger_Status_2 Register (Address = 0x22) [Reset = 0x00]**


REG0x22_Charger_Status_2 is shown in Table 8-30.


Return to the Summary Table.


**Table 8-30. REG0x22_Charger_Status_2 Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|PG_STAT|R|0x0||Input Power Good status:<br>0b = Not Power Good<br>1b = Power Good|
|6:4|TS_STAT|R|0x0||TS (Battery NTC) status:<br>000b = Normal<br>001b = TS Warm<br>010b = TS Cool<br>011b = TS Cold<br>100b = TS Hot|
|3:2|RESERVED|R|0x0||Reserved|
|1:0|MPPT_STAT|R|0x0||Max Power Point Tracking Algorithm status:<br>00b = MPPT Disabled<br>01b = MPPT Enabled, But Not Running<br>10b = Full Panel Sweep In Progress<br>11b = Max Power Voltage Detected|



**8.5.23 REG0x23_Charger_Status_3 Register (Address = 0x23) [Reset = 0x00]**


REG0x23_Charger_Status_3 is shown in Table 8-31.


Return to the Summary Table.


**Table 8-31. REG0x23_Charger_Status_3 Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|RESERVED|R|0x0||Reserved|
|5:4|FSW_SYNC_STAT|R|0x0||FSW_SYNC pin status:<br>00b = Normal, no external clock detected<br>01b = Valid ext. clock detected<br>10b = Pin fault (frequency out-of-range)<br>11b = Reserved|
|3|CV_TMR_STAT|R|0x0||CV Timer status:<br>0b = Normal<br>1b = CV Timer Expired|
|2|REVERSE_STAT|R|0x0||Converter Reverse Mode status:<br>0b = Reverse Mode off<br>1b = Reverse Mode On|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 51


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-31. REG0x23_Charger_Status_3 Register Field Descriptions (continued)**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|1|ACFET_STAT|R|0x0||ACFET driver status:<br>0b = ACFET off<br>1b = ACFET on|
|0|BATFET_STAT|R|0x0||BATFET driver status:<br>0b = BATFET off<br>1b = BATFET on|



**8.5.24 REG0x24_Fault_Status Register (Address = 0x24) [Reset = 0x00]**


REG0x24_Fault_Status is shown in Table 8-32.


Return to the Summary Table.


**Table 8-32. REG0x24_Fault_Status Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|VAC_UV_STAT|R|0x0||Input under-voltage status:<br>0b = Input Normal<br>1b = Device in Input under-voltage protection|
|6|VAC_OV_STAT|R|0x0||Input over-voltage status:<br>0b = Input Normal<br>1b = Device in Input over-voltage protection|
|5|IBAT_OCP_STAT|R|0x0||Battery over-current status:<br>0b = Battery current normal<br>1b = Battery over-current detected|
|4|VBAT_OV_STAT|R|0x0||Battery over-voltage status:<br>0b = Normal<br>1b = Device in Battery over-voltage protection|
|3|TSHUT_STAT|R|0x0||Thermal shutdown status:<br>0b = Normal<br>1b = Device in thermal shutdown protection|
|2|CHG_TMR_STAT|R|0x0||Charge safety timer status:<br>0b = Normal<br>1b = Charge safety timer expired|
|1|DRV_OKZ_STAT|R|0x0|In battery-only mode with<br>ADC disabled, this bit<br>always reads '1'|DRV_SUP pin voltage status:<br>0b = Normal<br>1b = DRV_SUP pin voltage is out of valid range|
|0|RESERVED|R|0x0||Reserved|


**8.5.25 REG0x25_Charger_Flag_1 Register (Address = 0x25) [Reset = 0x00]**


REG0x25_Charger_Flag_1 is shown in Table 8-33.


Return to the Summary Table.


**Table 8-33. REG0x25_Charger_Flag_1 Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|ADC_DONE_FLAG|R|0x0||ADC conversion INT flag (in one-shot mode only):<br>Note: always reads 0 in continuous mode<br>Access: R (ClearOnRead)<br>0b = Conversion not complete<br>1b = Conversion complete|



52 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


**Table 8-33. REG0x25_Charger_Flag_1 Register Field Descriptions (continued)**



|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|6|IAC_DPM_FLAG|R|0x0||Input Current regulation INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Device entered Input Current regulation|
|5|VAC_DPM_FLAG|R|0x0||Input Voltage regulation INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Device entered Input Voltage regulation|
|4|RESERVED|R|0x0||Reserved|
|3|WD_FLAG|R|0x0||I2C Watchdog timer INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = WD_STAT rising edge detected|
|2|RESERVED|R|0x0||Reserved|
|1|CV_TMR_FLAG|R|0x0||CV timer INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = CV timer expired rising edge detected|
|0|CHARGE_FLAG|R|0x0||Charge cycle INT flag:<br>Access: R (ClearOnRead)<br>0b = Not charging<br>1b = CHARGE_STAT[2:0] bits changed (transition to<br>any state)|


**8.5.26 REG0x26_Charger_Flag_2 Register (Address = 0x26) [Reset = 0x00]**


REG0x26_Charger_Flag_2 is shown in Table 8-34.


Return to the Summary Table.


**Table 8-34. REG0x26_Charger_Flag_2 Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|PG_FLAG|R|0x0||Input Power Good INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = PG signal toggle detected|
|6|ACFET_FLAG|R|0x0||ACFET driver INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = ACFET signal toggle detected|
|5|BATFET_FLAG|R|0x0||BATFET driver INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = BATFET signal toggle detected|
|4|TS_FLAG|R|0x0||TS (Battery NTC) INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = TS_STAT[2:0] bits changed (transitioned to any<br>state)|
|3|REVERSE_FLAG|R|0x0||Reverse Mode INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Reverse Mode toggle detected|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 53


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-34. REG0x26_Charger_Flag_2 Register Field Descriptions (continued)**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|2|RESERVED|R|0x0||Reserved|
|1|FSW_SYNC_FLAG|R|0x0||FSW_SYNC pin signal INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = FSW_SYNC status changed|
|0|MPPT_FLAG|R|0x0||Max Power Point Tracking INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = MPPT_STAT[1:0] bits changed (transitioned to<br>any state)|



**8.5.27 REG0x27_Fault_Flag Register (Address = 0x27) [Reset = 0x00]**


REG0x27_Fault_Flag is shown in Table 8-35.


Return to the Summary Table.


**Table 8-35. REG0x27_Fault_Flag Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|VAC_UV_FLAG|R|0x0||Input under-voltage INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Entered input under-voltage fault|
|6|VAC_OV_FLAG|R|0x0||Input over-voltage INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Entered Input over-voltage fault|
|5|IBAT_OCP_FLAG|R|0x0||Battery over-current INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Entered Battery over-current fault|
|4|VBAT_OV_FLAG|R|0x0||Battery over-voltage INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Entered battery over-voltage fault|
|3|TSHUT_FLAG|R|0x0||Thermal shutdown INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Entered TSHUT fault|
|2|CHG_TMR_FLAG|R|0x0||Charge safety timer INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = Charge Safety timer expired rising edge detected|
|1|DRV_OKZ_FLAG|R|0x0||DRV_SUP pin voltage INT flag:<br>Access: R (ClearOnRead)<br>0b = Normal<br>1b = DRV_SUP pin fault detected|
|0|RESERVED|R|0x0||Reserved|



**8.5.28 REG0x28_Charger_Mask_1 Register (Address = 0x28) [Reset = 0x00]**


REG0x28_Charger_Mask_1 is shown in Table 8-36.


54 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


Return to the Summary Table.



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 8-36. REG0x28_Charger_Mask_1 Register Field Descriptions**


















|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|ADC_DONE_MASK|R/W|0x0|Reset by:<br>REG_RESET|ADC conversion INT mask (in one-shot mode only):<br>0b = ADC_DONE produces INT pulse<br>1b = ADC_DONE does not produce INT pulse|
|6|IAC_DPM_MASK|R/W|0x0|Reset by:<br>REG_RESET|Input Current regulation INT mask:<br>0b = IAC_DPM_FLAG produces INT pulse<br>1b = IAC_DPM_FLAG does not produce INT pulse|
|5|VAC_DPM_MASK|R/W|0x0|Reset by:<br>REG_RESET|Input Voltage regulation INT mask:<br>0b = VAC_DPM_FLAG produces INT pulse<br>1b = VAC_DPM_FLAG does not produce INT pulse|
|4|RESERVED|R|0x0||Reserved|
|3|WD_MASK|R/W|0x0|Reset by:<br>REG_RESET|I2C Watchdog timer INT mask:<br>0b = WD expiration produces INT pulse<br>1b = WD expiration does not produce INT pulse|
|2|RESERVED|R|0x0||Reserved|
|1|CV_TMR_MASK|R/W|0x0|Reset by:<br>REG_RESET|CV timer INT mask:<br>0b = CV Timer expired rising edge produces INT pulse<br>1b = CV Timer expired rising edge does not produce<br>INT pulse|
|0|CHARGE_MASK|R/W|0x0|Reset by:<br>REG_RESET|Charge cycle INT mask:<br>0b = CHARGE_STAT change produces INT pulse<br>1b = CHARGE_STAT change does not produces INT<br>pulse|



**8.5.29 REG0x29_Charger_Mask_2 Register (Address = 0x29) [Reset = 0x00]**


REG0x29_Charger_Mask_2 is shown in Table 8-37.


Return to the Summary Table.


**Table 8-37. REG0x29_Charger_Mask_2 Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|PG_MASK|R/W|0x0|Reset by:<br>REG_RESET|Input Power Good INT mask:<br>0b = PG toggle produces INT pulse<br>1b = PG toggle does not produce INT pulse|
|6|ACFET_MASK|R/W|0x0|Reset by:<br>REG_RESET|ACFET driver INT mask:<br>0b = ACFET toggle produces INT pulse<br>1b = ACFET toggle does not produce INT pulse|
|5|BATFET_MASK|R/W|0x0|Reset by:<br>REG_RESET|BATFET driver INT mask:<br>0b = BATFET toggle produces INT pulse<br>1b = BATFET toggle does not produce INT pulse|
|4|TS_MASK|R/W|0x0|Reset by:<br>REG_RESET|TS (Battery NTC) INT mask:<br>0b = TS_STAT change produces INT pulse<br>1b = TS_STAT change does not produce INT pulse|
|3|REVERSE_MASK|R/W|0x0|Reset by:<br>REG_RESET|Reverse Mode INT mask:<br>0b = REVERSE_STAT toggle produces INT pulse<br>1b = REVERSE_STAT toggle does no produce INT<br>pulse|
|2|RESERVED|R|0x0||Reserved|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 55


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-37. REG0x29_Charger_Mask_2 Register Field Descriptions (continued)**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|1|FSW_SYNC_MASK|R/W|0x0|Reset by:<br>REG_RESET|FSW_SYNC pin signal INT mask:<br>0b = FSW_SYNC status change produces INT pulse<br>1b = FSW_SYNC status change does not produce INT<br>pulse|
|0|MPPT_MASK|R/W|0x0|Reset by:<br>REG_RESET|Max Power Point Tracking INT mask:<br>0b = MPPT_STAT rising edge produces INT pulse<br>1b = MPPT_STAT rising edge does no produce INT<br>pulse|



**8.5.30 REG0x2A_Fault_Mask Register (Address = 0x2A) [Reset = 0x00]**


REG0x2A_Fault_Mask is shown in Table 8-38.


Return to the Summary Table.


**Table 8-38. REG0x2A_Fault_Mask Register Field Descriptions**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|VAC_UV_MASK|R/W|0x0|Reset by:<br>REG_RESET|Input under-voltage INT mask:<br>0b = Input under-voltage event produces INT pulse<br>1b = Input under-voltage event does not produce INT<br>pulse|
|6|VAC_OV_MASK|R/W|0x0|Reset by:<br>REG_RESET|Input over-voltage INT mask:<br>0b = Input over-voltage event produces INT pulse<br>1b = Input over-voltage event does not produce INT<br>pulse|
|5|IBAT_OCP_MASK|R/W|0x0|Reset by:<br>REG_RESET|Battery over-current INT mask:<br>0b = Battery over-current event produces INT pulse<br>1b = Battery over-current event does not produce INT<br>pulse|
|4|VBAT_OV_MASK|R/W|0x0|Reset by:<br>REG_RESET|Battery over-voltage INT mask:<br>0b = Battery over-voltage event produces INT pulse<br>1b = Battery over-voltage event does not produce INT<br>pulse|
|3|TSHUT_MASK|R/W|0x0|Reset by:<br>REG_RESET|Thermal shutdown INT mask:<br>0b = TSHUT event produces INT pulse<br>1b = TSHUT event does not produce INT pulse|
|2|CHG_TMR_MASK|R/W|0x0|Reset by:<br>REG_RESET|Charge safety timer INT mask:<br>0b = Timer expired rising edge produces INT pulse<br>1b = Timer expired rising edge does not produce INT<br>pulse|
|1|DRV_OKZ_MASK|R/W|0x0|Reset by:<br>REG_RESET|DRV_SUP pin voltage INT mask:<br>0b = DRV_SUP pin fault produces INT pulse<br>1b = DRV_SUP pin fault does not produce INT pulse|
|0|RESERVED|R|0x0||Reserved|


**8.5.31 REG0x2B_ADC_Control Register (Address = 0x2B) [Reset = 0x60]**


REG0x2B_ADC_Control is shown in Table 8-39.


Return to the Summary Table.


56 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**Table 8-39. REG0x2B_ADC_Control Register Field Descriptions**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|ADC_EN|R/W|0x0|When<br>EN_VREG_TEMP_COMP<br>= 1, the ADC will<br>be automatically enabled,<br>regardless of the status of<br>ADC_EN<br>Reset by:<br>REG_RESET<br>WATCHDOG|ADC control:<br>0b = Disable ADC<br>1b = Enable ADC|
|6|ADC_RATE|R/W|0x1|Reset by:<br>REG_RESET|ADC conversion rate control:<br>0b = Continuous conversion<br>1b = One-shot conversion|
|5:4|ADC_SAMPLE|R/W|0x2|Reset by:<br>REG_RESET|ADC sample speed:<br>00b = 15 bit effective resolution<br>01b = 14 bit effective resolution<br>10b = 13 bit effective resolution<br>11b = Reserved|
|3|ADC_AVG|R/W|0x0|Reset by:<br>REG_RESET|ADC average control:<br>0b = Single value<br>1b = Running average|
|2|ADC_AVG_INIT|R/W|0x0|Reset by:<br>REG_RESET|ADC average initial value control:<br>0b = Start average using existing register value<br>1b = Start average using new ADC conversion|
|1:0|RESERVED|R|0x0||Reserved|


**8.5.32 REG0x2C_ADC_Channel_Control Register (Address = 0x2C) [Reset = 0x02]**


REG0x2C_ADC_Channel_Control is shown in Table 8-40.


Return to the Summary Table.


**Table 8-40. REG0x2C_ADC_Channel_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|IAC_ADC_DIS|R/W|0x0|Reset by:<br>REG_RESET|IAC ADC control<br>0b = Enable<br>1b = Disable|
|6|IBAT_ADC_DIS|R/W|0x0|Recommend to disable<br>IBAT ADC channel when<br>EN_IBAT_LOAD bit is 1<br>Reset by:<br>REG_RESET|IBAT ADC control<br>0b = Enable<br>1b = Disable|
|5|VAC_ADC_DIS|R/W|0x0|Reset by:<br>REG_RESET|VAC ADC control<br>0b = Enable<br>1b = Disable|
|4|VBAT_ADC_DIS|R/W|0x0|Reset by:<br>REG_RESET|VBAT ADC control<br>0b = Enable<br>1b = Disable|
|3|VSYS_ADC_DIS|R/W|0x0|Reset by:<br>REG_RESET|VSYS ADC control<br>0b = Enable<br>1b = Disable|
|2|TS_ADC_DIS|R/W|0x0|Reset by:<br>REG_RESET|TS ADC control<br>0b = Enable<br>1b = Disable|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 57


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-40. REG0x2C_ADC_Channel_Control Register Field Descriptions (continued)**







|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|1|VFB_ADC_DIS|R/W|0x1|Reset by:<br>REG_RESET|VFB ADC control<br>Recommend to disable this channel when charging is<br>enabled<br>0b = Enable<br>1b = Disable|
|0|RESERVED|R|0x0||Reserved|


**8.5.33 REG0x2D_IAC_ADC Register (Address = 0x2D) [Reset = 0x0000]**


REG0x2D_IAC_ADC is shown in Table 8-41.


Return to the Summary Table.


I2C REG0x2E=[15:8], I2C REG0x2D=[7:0]


**Table 8-41. REG0x2D_IAC_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|IAC_ADC|R|0x0||IAC ADC reading with 2mΩ RAC_SNS:<br>Reported as 2s complement<br>POR: 0mA (0h)<br>Format: 2s Complement<br>Range: -50000mA-50000mA (9E58h-61A8h)<br>Clamped Low<br>Clamped High<br>Bit Step: 2mA|



**8.5.34 REG0x2F_IBAT_ADC Register (Address = 0x2F) [Reset = 0x0000]**


REG0x2F_IBAT_ADC is shown in Table 8-42.


Return to the Summary Table.


I2C REG0x30=[15:8], I2C REG0x2F=[7:0]


**Table 8-42. REG0x2F_IBAT_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|IBAT_ADC|R|0x0||IBAT ADC reading with 5mΩ RBAT_SNS:<br>Reported as 2s complement<br>POR: 0mA (0h)<br>Format: 2s Complement<br>Range: -20000mA-20000mA (D8F0h-2710h)<br>Clamped Low<br>Clamped High<br>Bit Step: 2mA|



**8.5.35 REG0x31_VAC_ADC Register (Address = 0x31) [Reset = 0x0000]**


REG0x31_VAC_ADC is shown in Table 8-43.


Return to the Summary Table.


I2C REG0x32=[15:8], I2C REG0x31=[7:0]


58 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 8-43. REG0x31_VAC_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|VAC_ADC|R|0x0||VAC ADC reading:<br>Reported as unsigned integer<br>POR: 0mV (0h)<br>Format: 2s Complement<br>Range: 0mV-65534mV (0h-7FFFh)<br>Clamped Low<br>Bit Step: 2mV|



**8.5.36 REG0x33_VBAT_ADC Register (Address = 0x33) [Reset = 0x0000]**


REG0x33_VBAT_ADC is shown in Table 8-44.


Return to the Summary Table.


I2C REG0x34=[15:8], I2C REG0x33=[7:0]


**Table 8-44. REG0x33_VBAT_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|VBAT_ADC|R|0x0||VBAT ADC reading:<br>Reported as unsigned integer<br>POR: 0mV (0h)<br>Format: 2s Complement<br>Range: 0mV-65534mV (0h-7FFFh)<br>Clamped Low<br>Bit Step: 2mV|



**8.5.37 REG0x35_VSYS_ADC Register (Address = 0x35) [Reset = 0x0000]**


REG0x35_VSYS_ADC is shown in Table 8-45.


Return to the Summary Table.


I2C REG0x36=[15:8], I2C REG0x35=[7:0]


**Table 8-45. REG0x35_VSYS_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|VSYS_ADC|R|0x0||VSYS ADC reading:<br>Reported as unsigned integer<br>POR: 0mV (0h)<br>Format: 2s Complement<br>Range: 0mV-65534mV (0h-7FFFh)<br>Clamped Low<br>Bit Step: 2mV|



**8.5.38 REG0x37_TS_ADC Register (Address = 0x37) [Reset = 0x0000]**


REG0x37_TS_ADC is shown in Table 8-46.


Return to the Summary Table.


I2C REG0x38=[15:8], I2C REG0x37=[7:0]


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 59


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Table 8-46. REG0x37_TS_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|TS_ADC|R|0x0||TS ADC reading as percentage of REGN:<br>Reported as unsigned integer<br>POR: 0%(0h)<br>Range: 0% - 99.90234375% (0h-3FFh)<br>Clamped High<br>Bit Step: 0.09765625%|



**8.5.39 REG0x39_VFB_ADC Register (Address = 0x39) [Reset = 0x0000]**


REG0x39_VFB_ADC is shown in Table 8-47.


Return to the Summary Table.


I2C REG0x3A=[15:8], I2C REG0x39=[7:0]


**Table 8-47. REG0x39_VFB_ADC Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|15:0|VFB_ADC|R|0x0||VFB ADC reading:<br>POR: 0mV (0h)<br>Range: 0mV-2047mV (0h-7FFh)<br>Clamped High<br>Bit Step: 1mV|



**8.5.40 REG0x3B_Gate_Driver_Strength_Control Register (Address = 0x3B) [Reset = 0x00]**


REG0x3B_Gate_Driver_Strength_Control is shown in Table 8-48.


Return to the Summary Table.


**Table 8-48. REG0x3B_Gate_Driver_Strength_Control Register Field Descriptions**






|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|BOOST_HS_DRV|R/W|0x0|Reset by:<br>REG_RESET|Boost High Side FET Gate Driver Strength:<br>00b = Fastest<br>01b = Faster<br>10b = Slower<br>11b = Slowest|
|5:4|BUCK_HS_DRV|R/W|0x0|Reset by:<br>REG_RESET|Buck High Side FET Gate Driver Strength:<br>00b = Fastest<br>01b = Faster<br>10b = Slower<br>11b = Slowest|
|3:2|BOOST_LS_DRV|R/W|0x0|Reset by:<br>REG_RESET|Boost Low Side FET Gate Driver Strength:<br>00b = Fastest<br>01b = Faster<br>10b = Slower<br>11b = Slowest|
|1:0|BUCK_LS_DRV|R/W|0x0|Reset by:<br>REG_RESET|Buck Low Side FET Gate Driver Strength:<br>00b = Fastest<br>01b = Faster<br>10b = Slower<br>11b = Slowest|



60 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**8.5.41 REG0x3C_Gate_Driver_Dead_Time_Control Register (Address = 0x3C) [Reset = 0x00]**


REG0x3C_Gate_Driver_Dead_Time_Control is shown in Table 8-49.


Return to the Summary Table.


**Table 8-49. REG0x3C_Gate_Driver_Dead_Time_Control Register Field Descriptions**










|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:4|RESERVED|R|0x0||Reserved|
|3:2|BOOST_DEAD_TIM<br>E|R/W|0x0|Reset by:<br>REG_RESET|Boost Side FETs Dead Time Control:<br>00b = 45ns<br>01b = 75ns<br>10b = 105ns<br>11b = 135ns|
|1:0|BUCK_DEAD_TIME|R/W|0x0|Reset by:<br>REG_RESET|Buck Side FETs Dead Time Control:<br>00b = 45ns<br>01b = 75ns<br>10b = 105ns<br>11b = 135ns|



**8.5.42 REG0x3D_Part_Information Register (Address = 0x3D) [Reset = 0x02]**


REG0x3D_Part_Information is shown in Table 8-50.


Return to the Summary Table.


**Table 8-50. REG0x3D_Part_Information Register Field Descriptions**

|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7|RESERVED|R|0x0||Reserved|
|6:3|PART_NUM|R|0x0||Part Number:<br>000 - BQ25750|
|2:0|DEV_REV|R|0x2||Device Revision:|



**8.5.43 REG0x62_Reverse_Mode_Battery_Discharge_Current Register (Address = 0x62) [Reset = 0x02]**


REG0x62_Reverse_Mode_Battery_Discharge_Current is shown in Table 8-51.


Return to the Summary Table.


**Table 8-51. REG0x62_Reverse_Mode_Battery_Discharge_Current Register Field Descriptions**















|Bit|Field|Type|Reset|Notes|Description|
|---|---|---|---|---|---|
|7:6|IBAT_REV|R/W|0x0|Reset by:<br>REG_RESET|Reverse mode battery discharge current limit:<br>00b = 20A<br>01b = 15A<br>10b = 10A<br>11b = 5A|
|5:2|RESERVED|R|0x0||Reserved|
|1|EN_CONV_FAST_T<br>RANSIENT|R/W|0x1|Reset by:<br>REG_RESET|Enable converter fast transient response in reverse<br>mode only -<br>0b = Disable<br>1b = Enable|
|0|RESERVED|R|0x0||Reserved|


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 61


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**9 Application and Implementation**


**Note**


Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TI’s customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.


**9.1 Application Information**


The BQ25750 battery charger is ideal for high current charging (up-to 20 A) and can charge multi-chemistry
battery packs consisting of single cells or multiple cells in series up-to 70 V. The BQ25750EVM evaluation
module is a complete charge module for evaluating the device performance. The application curves were taken
using the BQ25750EVM.


**9.2 Typical Applications**


**9.2.1 Typical Application**


The device can be configured for direct power path applications, where the input source can be used to power
both system as well as charge the battery. When the input source falls outside the VAC operating window
programmed through ACUV and ACOV, the battery is automatically connected to the system. Figure 9-1 shows
a typical schematic when using the device as a 14S Li-Ion charger from a 48V input. The charging parameters
are programmed via the I [2] C registers.



Q1 Q2



48Vin

2m � SYS



2m �






|Q3<br>Q4|Col2|
|---|---|
|Q3<br>Q4||







































|Col1|Col2|HIDRV1 SW1 SW2 HIDRV2<br>BTST1 LODRV1 LODRV2 BTST2<br>ACN SYS<br>ACP BATSRC<br>ACDRV BATDRV<br>VAC<br>ACUV SRP<br>SRN<br>ACOV FB<br>DRV_SUP<br>REGN<br>TS<br>CE<br>INT ILIM_HIZ<br>SDA ICHG<br>SCL FSW_SYNC<br>PG<br>STAT1 PGND<br>STAT2 BQ25750|
|---|---|---|
|Host|Host|Host|
|Host|||
|Host|||
|Host|||
|Host|||
|Host|||
|Host|||
|Host|||


PGND AGND









**Figure 9-1. BQ25750: I** **[2]** **C Controlled, 48 VAC with 14-S Li-Ion Battery, 10-A Charge Current and 350-kHz**

**Switching Frequency**


62 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 9-1. Recommended Part Numbers:**

|COMPONENT|VALUE|RECOMMENDED PART NO.|
|---|---|---|
|Q1, Q2|80V, 2.6mΩ|AONS6276|
|Q3, Q4|80V, 2.6mΩ|AONS6276|
|Q5, Q6, Q7, Q8|80V, 6.5mΩ|SiR880BDP|
|L1|10uH|IHLP6767GZ-01|



_**9.2.1.1 Design Requirements**_


For this design example, use the parameters shown in the table below.


**Table 9-2. Design Parameters**

|PARAMETER|VALUE|
|---|---|
|Input voltage operating range (VAC)|40V to 56V|
|Input current limit (IAC)|12 A|
|Fast-charge current limit (ICHG)|10 A|
|Battery Charge Voltage (VBAT_REG)|58.8V|
|Switching frequency|350 kHz|



_**9.2.1.2 Detailed Design Procedure**_


**9.2.1.2.1 ACUV / ACOV Input Voltage Operating Window Programming**


The input voltage operating window is programmed by an ACUV / ACOV window with a resistor divider from
VAC to GND. The top resistor, RAC1 is typically selected as 1,000 kΩ to minimize the input voltage leakage
current. Assuming the desired trip-points for under-voltage and over-voltage protection are labeled V VACUVP and
V VACOVP, the resistor divider required can be calculated as follows. The internal reference for the over-voltage
threshold (VREF_ACOV) is 1.2 V. The internal reference for the under-voltage threshold (VREF_ACUV) is 1.1 V.

|INPUT|Col2|VAC<br>ACUV<br>ACOV|
|---|---|---|
|INPUT|RAC1|RAC1|
|INPUT|RAC2|RAC2|



**Figure 9-2. ACUV and ACOV Resistor Divider**



V VACOVP =


V VACUVP =



(8)
RAC3


(9)
RAC2 + RAC3



Solving this system of equations and finding the nearest 0.1% resistor value for the desired trip-points as 40 V
and 56 V for undervoltage and overvoltage yields:


R AC2 = 6.26 kΩ


R AC3 = 22.1 kΩ


The resulting overvoltage trip point can be calculated as:


V VACOVP = 1.2 V (1,000 kΩ + 6.26 kΩ + 22.1 kΩ) / (22.1 kΩ) = 55.8 V


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 63


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


Similarly, the V VACUVP can be calculated as: 39.9 V


Note that in addition to programming the input undervoltage threshold, the ACUV pin also programs a hardware
input voltage regulation limit when the pin voltage reaches the reference (V ACUV_DPM, typically 1.2 V). When the
input voltage reaches this threshold, the charger will reduce charge current to regulate the ACUV pin to the 1.2 V
reference. For the above example, the hardware ACUV_DPM level can be calculated as:


ACUV_DPM = 1.2 V (1,000 kΩ + 6.26 kΩ + 22.1 kΩ) / (6.26 kΩ + 22.1 kΩ) = 43.5 V


For the default device operating window of 4.2 V to 60 V, the ACUV can be pulled up directly to VAC, while the
ACOV can be pulled directly to GND.


**9.2.1.2.2 Charge Voltage Selection**


The battery regulation voltage is programmed using a resistor divider to the FB pin. The default internal voltage
reference is 1.536 V, and can be changed via the VFB_REG register bits. The top of the resistor divider is
selected to be 249 kΩ.


R TOP = 249 kΩ


The bottom resistor can be calculated as:



R BOT = R TOP ×



VFB
VBATREG −VFB [+ R] [FBG] (10)



where

 - V FB is the target feedback voltage programmed through I [2] C (default 1.536 V),

 - V BATREG is the desired battery regulation target (58.8 V in this example)

 - R FBG is the internal FBG pull-down resistor (33 Ω)


R = 6.712 kΩ.
FB_BOT


Choosing the nearest 0.1% resistor value, gives R FB_BOT = 6.65 kΩ, for a nominal charge voltage of 58.75 V.
Further fine-tuning of the regulation voltage can be achieved by changing the internal feedback reference.


It is recommended to use 0.1% accurate resistors to maximize the charge voltage accuracy.


**9.2.1.2.3 Switching Frequency Selection**


The switching frequency is set by a resistor connected from the FSW_SYNC pin to PGND. The RFSW resistor
required to set the desired frequency is calculated using Equation 3 or Table 8-2. A 0.1% standard resistor of 80
kΩ is selected to set _f_ _SW_ = 350 kHz.


**9.2.1.2.4 Inductor Selection**


Higher switching frequency allows the use of smaller inductor and capacitor values. Inductor saturation current
should be higher than the inductor current (I L ) plus half the ripple current (I RIPPLE ):


I SAT ≥I L + [1] 2 [I] [RIPPLE] (11)


The inductor ripple current in buck operation depends on input voltage (V AC ), duty cycle (D BUCK = V BAT /V AC ),
switching frequency (f SW ) and inductance (L):



I RIPPLE_BUCK =



(12)
fSW × L



During boost operation, the duty cycle is: D BOOST = 1 – (V AC /V BAT ). The inductor ripple current is:



I RIPPLE_BOOST =



VAC × DBOOST
(13)
fSW × L



64 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



The maximum inductor ripple current happens with D = 0.5 or close to 0.5. Ripple calculations should be
analyzed for both forward and reverse operating modes if applicable.


Usually inductor ripple is designed in the range of (20 – 40%) maximum inductor current (in either forward or
reverse mode) as a trade-off between inductor size and efficiency for a practical design.


**9.2.1.2.5 Input (VAC / SYS) Capacitor**


Input capacitor should have enough ripple current rating to absorb input switching ripple current. The worst case
RMS ripple current is half of the output when duty cycle is 0.5 in forward buck mode, or reverse boost mode. If
the converter does not operate at 50% duty cycle, then the worst case capacitor RMS current occurs where the
duty cycle is closest to 50% and can be estimated by Equation 14:


I CIN = I CHG × D ×( 1 −D) (14)


A combination of ceramic and bulk capacitors should be used to provide a short path for high di/dt current
and to reduce the voltage ripple. Ceramic capacitors should be placed close to the switching half-bridge. Given
total bulk input capacitance, it is recommended to distribute equally on either side of R AC_SNS . The complete
schematic is a good starting point for input capacitor for typical applications.


**9.2.1.2.6 Output (VBAT) Capacitor**


In forward boost mode or reverse buck mode, the output capacitor conducts high ripple current. The output
capacitor RMS ripple current is given by where the minimum VAC corresponds to the maximum capacitor
current.



I CBAT = I BAT



VBAT
VAC [−1] (15)



58V
In this case, the highest ripple occurs with highest V BAT and lowest V AC : I CBAT = 10A 40V [−1 = 6.9A] [ . A 5-mΩ ]

output capacitor ESR causes an output voltage ripple of 74 mV as given by:



ΔV RIPPLE( ESR) = I BAT ×



VBAT
VAC, min [× ESR] (16)



A 140-μF output capacitor causes a capacitive ripple voltage of 66 mV as given by:



ΔV RIPPLE( CBAT) = I BAT ×(



(17)
CBAT × fSW



A combination of ceramic and bulk capacitors should be used to provide low ESR and high ripple current
capacity. Ceramic capacitors should be placed close to the switching half-bridge. Given total bulk output
capacitance, it is recommended to distribute equally on either side of R BAT_SNS . The complete schematic is
a good starting point for C BAT for typical applications.


**9.2.1.2.7 Sense Resistor (R** **AC_SNS** **and R** **BAT_SNS** **) and Current Programming**


The battery current sense resistor between SRP and SRN is fixed at 5 mΩ; using a different value is not
recommended. The input current sense resistor between ACP and ACN is typically 2 mΩ, but can be increased
to achieve better accuracy at lower sensed currents. In USB-PD EPR applications, a 5-mΩ sense resistor is
recommended to achieve programmability in 50 mA/step. In addition, if input current limit function is not desired,
ACP and ACN may be shorted together. For both of these sense resistors, a filter network is recommended as
shown in the Typical Application.


For both the input current and the output current, the limits may be programmed using the I [2] C interface or an
external programming resistor on ILIM_HIZ and ICHG pins, respectively.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 65


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**

|PARAMETER|FORMULA|VALUE|
|---|---|---|
|Input Current Hardware Limit|RILIM_HIZ = KILIM / 15 A|3.3 kΩ for 15 A with 2-mΩ RAC_SNS|
|Input Current Software Limit|IAC_DPM = 12 A|REG06 = 0x0180 (12 A with 2-mΩ RAC_SNS)|
|Charge Current Hardware Limit|RICHG = KICHG / 12 A|4.2 kΩ for 15 A with 5-mΩ RBAT_SNS|
|Charge Current Software Limit|ICHG = 15 A|REG02 = 0x04B0 (15 A)|



The default input sense resistor (R AC_SNS ) is 2 mΩ, and the register allows for a range of up-to 50-A input
current limit. If lower currents are desired, it is possible to use a higher resistor, such as 5 mΩ. In this case, the
IAC_DPM register value should be multiplied by a factor of 2/5 to program the correct current. For example, if
a 5-mΩ R AC_SNS is used, and the register is programmed to a value of 0x60, the true maximum current across
the R AC_SNS will be: 12A * 2/5 = 4.8 A. Similarly, the K ILIM parameter used to set the ILIM_HIZ pull-down resistor
should be scaled by 2/5. For example, with a 5-mΩ R AC_SNS resistor, a 6-A current limit would be achieved as:
R ILIM = K ILIM - (2/5) / 6A = 3.3 kΩ.


**9.2.1.2.8 Power MOSFETs Selection**


Four external N-channel MOSFETs are used for a synchronous switching buck-boost battery charger. The gate
drivers are integrated into the IC with 5 V of gate drive voltage. An external gate drive voltage can be provided
directly into the DRV_SUP pin for increased efficiency.


Figure-of-merit (FOM) is usually used for selecting proper MOSFET based on a tradeoff between the conduction
loss and switching loss. For the top side MOSFET, FOM is defined as the product of a MOSFET's on-resistance,
R DS(ON), and the gate-to-drain charge, Q GD . For the bottom side MOSFET, FOM is defined as the product of the
MOSFET's on-resistance, R DS(ON), and the total gate charge, Q G .


FOM top = R DS(on)  - Q GD ; FOM bottom = R DS(on)  - Q G (18)


The lower the FOM value, the lower the total power loss. Usually lower R DS(ON) has higher cost with the same
package size.


The top-side MOSFET loss includes conduction loss and switching loss. Taking buck mode operation as
an example the power loss is a function of duty cycle (D=V OUT /V IN ), charging current (I CHG ), MOSFET's onresistance (R DS(ON)_top ), input voltage (V IN ), switching frequency (f S ), turn-on time (t on ) and turn-off time (t off ):


P top =P con_top +P sw_top (19)


P con_top =D · I L_RMS [2]  - R DS(on)_top ; (20)


I L_RMS [2] =I L_DC [2] +I ripple [2] /12 (21)


 - I L_DC is the average inductor DC current;

 - I ripple is the inductor current ripple peak-to-peak value;


P sw_top =P IV_top +P Qoss_top +P Gate_top ; (22)


The first item P con_top represents the conduction loss which is straight forward. The second term P sw_top
represents the multiple switching loss items in top MOSFET including voltage and current overlap losses
(P IV_top ), MOSFET parasitic output capacitance loss (P Qoss_top ) and gate drive loss (P Gate_top ). To calculate
voltage and current overlap losses (P IV_top ):


P IV_top =0.5x V IN  - I valley  - t on  - f S +0.5x V IN  - I peak  - t off  - f S (23)


I valley =I L_DC     - 0.5 · I ripple (inductor current valley value); (24)


I peak =I L_DC + 0.5 · I ripple (inductor current peak value); (25)


 - t on is the MOSFET turn-on time that V DS falling time from V IN to almost zero (MOSFET turn on conduction
voltage);

 - t off is the MOSFET turn-off time that I DS falling time from I peak to zero;


66 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


The MOSFET turn-on and turn-off times are given by:



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



t on = Q SW, t off = Q SW
I on I off (26)


where Q sw is the switching charge, I on is the turn-on gate driving current, and I off is the turn-off gate driving
current. If the switching charge is not given in MOSFET datasheet, it can be estimated by gate-to-drain charge
(Q GD ) and gate-to-source charge (Q GS ):


Q sw =Q GD +Q GS (27)


Gate driving current can be estimated by REGN voltage (V REGN ), MOSFET plateau voltage (V plt ), total turn-on
gate resistance (R on ), and turn-off gate resistance (R off ) of the gate driver:


I on = V REGN    - V plt, I off = V plt
R on R off (28)


To calculate top MOSFET parasitic output capacitance loss (P Qoss_top ):


P Qoss_top =0.5 · V IN  - Q oss  - f S (29)


 - Q oss is the MOSFET parasitic output charge which can be found in MOSFET datasheet. It is recommended
to limit the total switch node capacitance C SW (nF) < 160/VIN; for example, for a 60-V application, it is
recommended to keep the total C SW < 2.67 nF


To calculate top MOSFET gate drive loss (P Gate_top ):


P Gate_top =V IN  - Q Gate_top  - f S (30)


 - Q Gate_top is the top MOSFET gate charge which can be found in MOSFET datasheet;

 - Note here V IN is used instead of real gate drive voltage because the gate drive is generated based on LDO
from V IN, the total gate drive related loss are all considered when V IN is used for gate drive loss calculation.

 - Alternatively, gate drive voltage can be supplied directly by external high efficiency supply into the DRV_SUP
pin. In this case, the power loss to drive the gates becomes: P Gate_top =V DRV_SUP   - Q Gate_top   - f S


The bottom-side MOSFET loss also includes conduction loss and switching loss:


P bottom =P con_bottom +P sw_bottom (31)


P con_bottom =(1 - D) · I L_RMS [2]  - R DS(on)_bottom ; (32)


P sw_bottom =P RR_bottom +P Dead_bottom +P Gate_bottom ; (33)


The first item P con_bottom represents the conduction loss which is straight forward. The second term P sw_bottom
represents the multiple switching loss items in bottom MOSFET including reverse recovery losses (P RR_bottom ),
Dead time body diode conduction loss (P Dead_bottom ) and gate drive loss (P Gate_bottom ). The detail calculation can
be found below:


P RR_bottom =V IN  - Q rr  - f S (34)


 - Q rr is the bottom MOSFET reverse recovery charge which can be found in MOSFET data sheet;


P Dead_bottom =V F  - I valley  - f S  - t dead_rise +V F  - I peak  - f S  - t dead_fall (35)


 - V F is the body diode forward conduction voltage drop;

 - t dead_rise is the SW rising edge deadtime between top and bottom MOSFETs which is around 45 ns;

 - t dead_fall is the SW falling edge deadtime between top and bottom MOSFETs which is around 45 ns;


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 67


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


P Gate_bottom can follow the same method as top MOSFET gate drive loss calculation approach.


Power-path FETs for providing power to SYS from either VAC or VBAT are selected as N-channel MOSFETs.
The gate drivers are integrated into the IC with 10 V of gate drive voltage; however, the gate drive voltage can be
reduced to 7 V using the PWRPATH_REDUCE_VDRV register bit if desired.


**9.2.1.2.9 ACFETs and BATFETs Selection**


Four external N-channel MOSFETs are used for power path transfer. Two on the VAC side called ACFETs and
two on the VBAT side called BATFETs.


The proper trade off for selecting these MOSFETs depends on the SOA characteristics. All four FETs follow the
same trend hence the same FET can be used at all four places. It is essential to select a MOSFET that offers
close to 10A Drain Current at 30V V DS at DC and also has the capability to offer 100A Drain Current at 30V
V DS at 10 μs without breaking. Furthermore, the SOA characteristics should be such that the maximum junction
temperature should be at least 125°C. The FETs selected for this application are AONS6276 and can withstand
a voltage swing of up-to 30V from VAC to VBAT and vice-versa.


**9.2.1.2.10 Converter Fast Transient Response**


The device integrates all the loop compensation, thereby providing a high density solution with ease of use. For
faster transient reponse in reverse operating mode, the EN_CONV_FAST_TRANSIENT bit can be set to 1. If
device is not used in reverse boost mode operation, this section can be disregarded.


When the converter is operating in boost mode, the non-continuous inductor current flow to the load results in a
right-half plane (RHP) zero. The RHP zero location is:



RHPz =



VIN, boost
IIN, boost



1
2πL (36)



For good phase margin, the unity gain bandwidth (UGBW) of the converter should be about 1/3 of the RHPz.
The boost output capacitor ( _C_ _load_ ), and the converter transient parameters ( _R_ _1_, _gm_ _1_ ) need to be scaled to move
the location of the UGBW of the converter.





1 ≈ (







(37)



The device adjusts _Adiv_, _gm_ _1_ and _R_ _1_ based on the output voltage and the EN_CONV_FAST_TRANSIENT bit
setting per the table below. During some boost case scenarios, the _C_ _load_ needs to be adjusted to limit the
converter bandwidth.







|BOOST OUTPUT<br>VOLTAGE|Adiv|C<br>1|EN_CONV_FAST_TRANSIENT = 0|Col5|EN_CONV_FAST_TRANSIENT = 1|Col7|
|---|---|---|---|---|---|---|
|**BOOST OUTPUT**<br>**VOLTAGE**|**_Adiv_**|**_C1_**|**_gm1_**|**_R1_**|**_gm1_**|**_R1_**|
|≤8 V|1/5|75 pF|0.4 μ|600 kΩ|2 μ|1.3 MΩ|
|8 V to 16 V|1/10|75 pF|0.47 μ|1 MΩ|2 μ|1.8 MΩ|
|16 V to 32 V|1/20|75 pF|0.67 μ|2.8 MΩ|2 μ|2.8 MΩ|
|>32 V|1/40|75 pF|2 μ|2.8 MΩ|2 μ|2.8 MΩ|


As an example, assume the device operates in reverse boost mode from a 5V supply to provide a 7V boost
output voltage with load up-to 5A and 10μH inductor. The RHPz is approximately located at:



RHPz =



VIN, boost
IIN, boost



1
2πL [= 11.4kHz] (38)



For best stability, the UGBW of the converter should be limited to 1/3 of the RHP zero, or 3.8kHz. If
EN_CONV_FAST_TRANSIENT = 1, the equation becomes:


68 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**






|0.2 × 2μ ( jω × 1.3MΩ × 75pF + 1 5V<br>jω × 75pF[ 5A × 50m][|1|
|---|---|
|0.2 × 2μ jω × 1.3MΩ × 75pF + 1<br>jω × 75pF<br>5V<br>5A × 50m|1 + jω~~C~~load ~~× 1.4~~<br>~~2~~|



Solving the above for _C_ _load_ gives ≥674 μF capacitor requirement.


Conversely, if EN_CONV_FAST_TRANSIENT = 0, the UGBW equation becomes:



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)


(39)


(40)









Solving the above for _C_ _load_ gives ≥51 μF capacitor requirement. However, the minimum recommended capacitor
for converter stability is 80 μF, so this minimum value should be used.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 69


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


_**9.2.1.3 Application Curves**_


C VAC = 160 µF, C OUT = 160 µF, V VAC = 20 V, V BAT = 29.4 V (unless otherwise specified)






|VAC = 20 V VBAT = 20 V ICHG = 5 A<br>Figure 9-3. VAC Plug-In Power Up with 5-A ICHG|VAC = 20 V → 0 V VBAT = 20 V ICHG = 5 A<br>Figure 9-4. VAC Un-plug Power Down with 5-A<br>ICHG|
|---|---|
|VAC = 20 V<br>VBAT = 24 V<br>ICHG = 5 A<br>**Figure 9-5. Charge Enable via I2C with 5-A ICHG**|VAC = 20 V<br>VBAT = 24 V<br>ICHG = 5 A<br>**Figure 9-6. Charge Disable via I2C with 5-A ICHG**|
|VAC = 20 V<br>VBAT = 24 V<br>ICHG = 5 A<br>**Figure 9-7. Charge Enable via**~~** CE**~~** Pin with 5-A**<br>**ICHG**|VAC = 20 V<br>VBAT = 24 V<br>ICHG = 5 A<br>**Figure 9-8. Charge Disable via**~~**CE**~~** Pin with 5-A**<br>**ICHG**|



70 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)








|VAC = 24 V VBAT = 20 V ICHG = 5 A<br>Figure 9-9. Buck Switching Waveform|VAC = 24 V VOUT = 28 V ICHG = 5 A<br>Figure 9-10. Boost Switching Waveform|
|---|---|
|VAC = 24 V<br>VBAT = 24 V<br>ICHG = 5 A<br>**Figure 9-11. Buck-Boost Switching Waveform**|VOC = 30 V<br>ISC = 3.5 A<br>VBAT = 24 V<br>EN_CHG = 0 → 1<br>**Figure 9-12. Max Power Point Tracking (MPPT) Full**<br>**Panel Sweep**|
|VBAT = 24 V<br>VAC_REV = 20 V<br>ILOAD = 4 A<br>**Figure 9-13. Reverse Mode Power Up with 4-A**<br>**Load**|VBAT = 24 V<br>VAC_REV = 20 V<br>ILOAD = 4 A<br>**Figure 9-14. Reverse Mode Power Down with 4-A**<br>**Load**|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 71


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**







|VBAT = 28 V VAC_REV = 5 V ILOAD = 0.5 A → 4.5 A<br>Figure 9-15. Reverse Mode Buck Transient<br>Reponse|VBAT = 28 V VAC_REV = 28 V ILOAD = 0.5 A → 4.5 A<br>Figure 9-16. Reverse Mode Buck-Boost Transient<br>Reponse|
|---|---|
|VBAT = 28 V<br>VAC_REV = 48 V<br>ILOAD = 0.5 A → 4.5 A<br>**Figure 9-17. Reverse Mode Boost Transient Reponse**|VBAT = 28 V<br>VAC_REV = 48 V<br>ILOAD = 0.5 A → 4.5 A<br>**Figure 9-17. Reverse Mode Boost Transient Reponse**|


72 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**10 Power Supply Recommendations**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



The power supply for the device is any DC voltage source within the specified input range. The supply should
also be capable of supplying sufficient current based on the programmed input current limit. The input supply
should be bypassed with a combination of electrolytic and ceramic capacitors to avoid ringing due to the
parasitic impedance of the connecting cables.


When device is operating in the reverse direction, the supply at the OUTPUT should follow the same
recommendations as the input supply mentioned above.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 73


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**11 Layout**
**11.1 Layout Guidelines**


Proper layout of the components to minimize high frequency current path loops is important to prevent electrical
and magnetic field radiation and high frequency resonant problems. Here is a PCB layout priority list for proper
layout.

**Table 11-1. PCB Layout Guidelines**
























|COMPONENTS|FUNCTION|IMPACT|GUIDELINES|
|---|---|---|---|
|Buck high side FET,<br>Buck low side FET, input<br>capacitors|Buck input loop|High frequency noise,<br>ripple, efficiency|This path forms a high frequency switching loop due<br>to the pulsating current at the input of the buck. Place<br>components on the same side of the board. Minimize<br>loop area to reduce parasitic inductance. Maximize<br>trace width to reduce parasitic resistance. Place input<br>ceramic capacitors close to the switching FETs.|
|Boost low side FET, boost<br>high side FET, output<br>capacitors|Boost output loop|High frequency noise,<br>ripple, efficiency|This path forms a high frequency switching loop due to<br>the pulsating current at the output of the boost. Place<br>components on the same side of the board. Minimize<br>loop area to reduce parasitic inductance. Maximize<br>trace width to reduce parasitic resistance. Place output<br>ceramic capacitors close to the switching FETs.|
|Sense resistors, switching<br>FETs, inductor|Current path|Efficiency|The current path from input to output through the<br>power stage and sense resistors has low impedance.<br>Pay attention to via resistance if they are not on the<br>same side. The number of vias can be estimated as<br>1- to 2-A per via for a 10-mil via with 1 oz. copper<br>thickness.|
|Switching FETs, inductor|Power stage|Thermal, efficiency|The switching FETs and inductor are the components<br>with highest power loss. Allow enough copper area<br>for heat dissipation. Multiple thermal vias can be used<br>to connect more copper layers together and dissipate<br>more heat.|
|DRV_SUP, BTST1, BTST2<br>capacitors|Switching FET gate drive|High frequency noise,<br>parasitic ringing, gate<br>drive integrity|The DRV_SUP capacitor is used to supply the power<br>to drive the low side FETs. The BTST capacitors are<br>used to drive the high side FETs. It is recommended to<br>place the capacitors as close as possible to the IC.|
|LODRV1, LODRV2|Low side gate drive|High frequency noise,<br>parasitic ringing, gate<br>drive integrity|LODRV1 and LODRV2 supplies the gate drive current<br>to turn on the low side FETs. The return of LODRV1<br>and LODRV2 is PGND. As current take the path of<br>least impedance, a ground plane close to the low side<br>gate drive traces is recommended. Minimize gate drive<br>length and aim for at least 20-mil gate drive trace<br>width.|
|HIDRV1, HIDRV2, SW1<br>(pin trace), SW2 (pin<br>trace)|High side gate drive|High frequency noise,<br>parasitic ringing, gate<br>drive integrity|HIDRV1 and HIDRV2 supplies the gate drive current<br>to turn on the high side FETs. The return of HIDRV1<br>and HIDRV2 are SW1 and SW2, respectively. Route<br>HIDRV1/SW1 and HIDRV2/SW2 pair next to each<br>other to reduce gate drive parasitic inductance.<br>Minimize gate drive length and aim for at least 20-mil<br>gate drive trace width.|



74 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



**Table 11-1. PCB Layout Guidelines (continued)**















|COMPONENTS|FUNCTION|IMPACT|GUIDELINES|
|---|---|---|---|
|Current limit resistors,<br>FSW_SYNC resistor|IC programmable settings|Regulation accuracy,<br>switching integrity|Pin voltage determines the settings for input current<br>limit, output current limit and switching frequency.<br>Ground noise on these could lead to inacuracy.<br>Minimize ground return from these resistors to the IC<br>ground pin.|
|Input (ACP, ACN) and<br>output (SRP, SRN) current<br>sense|Current regulation|Regulation accuracy|Use Kelvin-sensing technique for input and output<br>current sense resistors. Connect the current sense<br>traces to the center of the pads, and run current sense<br>traces as differential pairs, away from switching nodes.|
|Input (ACUV), and output<br>(FB, VO_SNS) voltage<br>sensing|Voltage sense and<br>regulation|Regulation accuracy|ACUV divider sets internal input voltage regulation in<br>forward mode (VACUV_DPM). FB divider sets battery<br>voltage regulation in forward mode (VFB_ACC). Route<br>the top of the divider point to the target regulation<br>location. Avoid routing close to high power switching<br>nodes.|
|Bypass capacitors|Noise filter|Noise immunity|Place lowest value capacitors closest to the IC.|


**11.2 Layout Example**


Based on the above layout guidelines, the buck-boost PCB layout example top view is shown below including all
the key power components.


**Figure 11-1. PCB Layout Reference Example Top View**


For both input and output current sensing resistors, differential sensing and routing method are suggested and
highlighted in figure below. Use wide trace for gate drive traces, minimum 20-mil trace width. Connect all analog
grounds to a dedicated low-impedance copper plane, which is tied to the power ground underneath the IC
exposed pad.


Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 75


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**Figure 11-2. PCB Layout Gate Drive and Current Sensing Signal Layer Routing**


76 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[www.ti.com](https://www.ti.com)**


**12 Device and Documentation Support**
**12.1 Device Support**


**12.1.1 Third-Party Products Disclaimer**



**[BQ25750](https://www.ti.com/product/BQ25750)**

[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3)



TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT

CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES

OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER
ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.


**12.2 Receiving Notification of Documentation Updates**


To receive notification of documentation updates, navigate to the device product folder on [ti.com. Click on](https://www.ti.com)
_Notifications_ to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.


**12.3 Support Resources**


TI E2E [™] [support forums are an engineer's go-to source for fast, verified answers and design help — straight](https://e2e.ti.com)
from the experts. Search existing answers or ask your own question to get the quick design help you need.


Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
[not necessarily reflect TI's views; see TI's Terms of Use.](https://www.ti.com/corp/docs/legal/termsofuse.shtml)


**12.4 Trademarks**

TI E2E [™] is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

**12.5 Electrostatic Discharge Caution**


This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.


ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.


**12.6 Glossary**


[TI Glossary](https://www.ti.com/lit/pdf/SLYZ022) This glossary lists and explains terms, acronyms, and definitions.


**13 Revision History**

|DATE|REVISION|NOTES|
|---|---|---|
|December 2023|*|Initial release|



Copyright © 2023 Texas Instruments Incorporated _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ 77


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


**[BQ25750](https://www.ti.com/product/BQ25750)**
[SLUSDY3 – DECEMBER 2023](https://www.ti.com/lit/pdf/SLUSDY3) **[www.ti.com](https://www.ti.com)**


**14 Mechanical, Packaging, and Orderable Information**


The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.


78 _[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SLUSDY3&partnum=BQ25750)_ Copyright © 2023 Texas Instruments Incorporated


Product Folder Links: _[BQ25750](https://www.ti.com/product/bq25750?qgpn=bq25750)_


### **PACKAGE OPTION ADDENDUM**

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


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 10-Dec-2023


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
|BQ25750RRVR|VQFN|RRV|36|3000|330.0|12.4|5.3|6.3|1.15|8.0|12.0|Q1|


Pack Materials-Page 1


### **PACKAGE MATERIALS INFORMATION**

www.ti.com 10-Dec-2023





*All dimensions are nominal

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|BQ25750RRVR|VQFN|RRV|36|3000|367.0|367.0|35.0|



Pack Materials-Page 2


## **GENERIC PACKAGE VIEW**

# **RRV 36 VQFN - 1 mm max height**

**5 x 6, 0.5 mm pitch** PLASTIC QUAD FLATPACK - NO LEAD


This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.


4229484/A


www.ti.com


## **PACKAGE OUTLINE** **RRV0036A VQFN - 1 mm max height**

PLASTIC QUAD FLATPACK-NO LEAD
















|11|Col2|18|
|---|---|---|
|||37|
|||37|
||||


|0.3 0.2|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|0.1<br>|C<br>|C<br>|A<br>|B|
|0.05|0.05|C|C|C|



















NOTES:


1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for optimal thermal and mechanical performance.


**www.ti.com**


## **EXAMPLE BOARD LAYOUT** **RRV0036A VQFN - 1 mm max height**

PLASTIC QUAD FLATPACK-NO LEAD


|Col1|Col2|36|
|---|---|---|
||||
||||
||||
||||





























NOTES: (continued)


4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271) .
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.


**www.ti.com**


## **EXAMPLE STENCIL DESIGN** **RRV0036A VQFN - 1 mm max height**

PLASTIC QUAD FLATPACK-NO LEAD


|Col1|29|
|---|---|
|||
|||














|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||37|37|||||||
||||37|37|||||||
||||37|37|||||||
||||37|37|||||||
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
||||||||||||



NOTES: (continued)


6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.


**www.ti.com**


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


