###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)
### **DP83TG720S-Q1 1000BASE-T1 Automotive Ethernet PHY with SGMII and RGMII**

###### **1 Features** • IEEE802.3bp 1000BASE-T1 compliant • Open Alliance TC12 Interoperability and EMC compliant – Interoperability tested with OA/IEEE compliant PHYs – EMC immunity Class-IV compliant for UTP (unshielded twisted pair) • Integrated LPF on MDI pins • MAC Interfaces: RGMII and SGMII • Supported I/O voltages: 3.3V, 2.5V, and 1.8V • Pin compatible with TI's 100BASE-T1 PHY – Single board design for 100BASE-T1 and 1000BASE-T1 with required BOM change • Power savings features: – Standby and sleep – Local and remote wake-up • Diagnostic tool kit – High accuracy temperature monitor – Voltage monitor – ESD event monitor – Data throughput calculator: inbuilt MAC packet generator, counter and error checker – Link quality monitoring – Cable open and short fault detection – Loopback modes • 25MHz clock output source • VQFN, wettable flank packaging • AEC-Q100 Qualified – Inbuilt ESD protection : IEC61000-4-2 ESD : ±8 kV contact discharge – Device temperature grade 1: –40°C to +125°C ambient operating temperature **2 Applications** • Telematics control unit (TCU, TBOX) • Gateway and Body Control Module (BCM) • ADAS: LIDAR, RADAR, Front Camera

###### **3 Description** The DP83TG720S-Q1 device is an IEEE 802.3bp and Open Alliance compliant automotive Ethernet physical layer transceiver. The device provides all physical layer functions needed to transmit and receive data over unshielded/shielded single twisted-pair cables. The device provides xMII flexibility with support for RGMII and SGMII MAC interfaces. DP83TG720 is compliant to Open Alliance EMC and interoperable specifications over unshielded twisted cable. DP83TG720 is front print compatible to TI's 100BASE-T1 PHY enabling design scalability with single board for both speeds. This device offers the Diagnostic Tool Kit, with an extensive list of real- time monitoring tools, debug tools and test modes. Within the tool kit is the first integrated electrostatic discharge (ESD) monitoring tool. The device is capable of counting ESD events on both the xMII and MDI as well as providing real-time monitoring through the use of a programmable interrupt. Additionally, the DP83TG720S-Q1 includes a data generator and checker tool to generate customizable MAC packets and check the errors on incoming packets. This enables system level datapath tests/optimizations without dependency on MAC. **Device Information**

(1) For all available packages, see the orderable addendum at
the end of the data sheet.
(2) The package size (length × width) is a nominal value and
includes pins, where applicable.

CM

Termination

|PART NUMBER|PACKAGE (1)|BODY SIZE (NOM) (2)|
|---|---|---|
|DP83TG720S-Q1|VQFN (36)|6.00mm × 6.00mm|

|CPU/MPU MAC|RGMII SGMII|DP83TG720S-Q1 1000 Mbps Ethernet PHY|
|---|---|---|


25-MHz

Clock Source


Status

LEDs


GND
###### **Simplified Schematic**

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Table of Contents**

###### 1 Features ............................................................................1 2 Applications ..................................................................... 1 3 Description .......................................................................1 4 Pin Configuration and Functions ...................................3 Pin Functions.................................................................... 4 4.1 Pin States....................................................................6 4.2 Pin Power Domain...................................................... 9 5 Specifications ................................................................ 10 5.1 Absolute Maximum Ratings...................................... 10 5.2 ESD Ratings............................................................. 10 5.3 Recommended Operating Conditions....................... 11 5.4 Thermal Information.................................................. 11 5.5 Electrical Characteristics...........................................11 5.6 Timing Requirements................................................ 15 5.7 Timing Diagrams....................................................... 19 5.8 LED Drive Characteristics.........................................23 6 Detailed Description ......................................................24 6.1 Overview................................................................... 24 6.2 Functional Block Diagram......................................... 25 6.3 Feature Description...................................................26

###### 6.4 Device Functional Modes..........................................38 6.5 Programming............................................................ 53 6.6 Register Maps...........................................................57 7 Application and Implementation ................................ 167 7.1 Application Information........................................... 167 7.2 Typical Applications................................................ 167 7.3 Power Supply Recommendations...........................167 7.4 Compatibility with TI's 100BT1 PHY ...................... 170 7.5 Layout..................................................................... 171 8 Device and Documentation Support ..........................174 8.1 Receiving Notification of Documentation Updates..174 8.2 Support Resources................................................. 174 8.3 Trademarks............................................................. 174 8.4 Electrostatic Discharge Caution..............................174 8.5 Glossary..................................................................174 9 Revision History .......................................................... 174 **10 Mechanical, Packaging, and Orderable ** Information .................................................................. 176 10.1 Package Option Addendum.................................. 176


2 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **4 Pin Configuration and Functions**

TX_CLK 28

TX_CTRL 29

TX_D3 30

TX_D2 31

TX_D1 / TX_P 32

TX_D0 / TX_M 33

VDDIO 34

LED_0 / GPIO_0 35

MDIO 36 **Figure 4-1. RHA Package** **36-Pin VQFN** **Top View **

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

18 DNC

17 DNC

16 CLKOUT / GPIO_2

15 RX_CTRL

14 STRAP_1

13 TRD_M

12 TRD_P

11 VDDA

10 INH


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 3

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Pin Functions**

|Col1|Col2|Col3|Table 4-1. Pin Functions|
|---|---|---|---|
|PIN||STATE(1)|DESCRIPTION (2)|
|NAME|NO.|||
|MAC INTERFACE||||
|RX_D3 RX_M|23|S, PD, O|Receive Data: Symbols received on the cable are decoded and transmitted out of these pins synchronous to the rising edge of RX_CLK. Valid data is contained when RX_DV(decoded from RX_CTL) is asserted. A nibble, RX_D[3:0], is transmitted in RGMII mode. RX_M / RX_P: Differential SGMII Data Output. These pins transmit data from the PHY to the MAC.|
|RX_D2 RX_P|24|||
|RX_D1|25|||
|RX_D0|26|||
|RX_CLK|27|O|Receive Clock: In RGMII mode, PHY provides this 125MHz clock to MAC. Unused in SGMII mode|
|RX_CTRL|15|S, PD, O|RGMII Receive Control: Receive control combines receive data valid indication and receive error indication into a single signal. RX_DV is presented on the rising edge of RX_CLK and RX_ER is presented on the falling edge of RX_CLK. Used only as strap in SGMII mode|
|TX_CLK|28|I|Transmit Clock: In RGMII mode, MAC provides this 125MHz clock to PHY. Unused in SGMII mode|
|TX_CTRL|29|I|RGMII Transmit Control: Transmit control combines transmit enable and transmit error indication into a single signal. TX_EN is presented prior to the rising edge of TX_CLK; TX_ER is presented on the falling edge of TX_CLK. Unused in SGMII mode|
|TX_D3|30|I|Transmit Data: In RGMII mode, the transmit data nibble, TX_D[3:0], is received from the MAC . TX_M / TX_P: Differential SGMII Data Input. These pins receive data that is transmitted from the MAC to the PHY.|
|TX_D2|31|||
|TX_D1 TX_P|32|||
|TX_D0 TX_M|33|||
|SERIAL MANAGEMENT INTERFACE||||
|MDC|1|I|Management Data Clock: Synchronous clock to the MDIO serial management input and output data.|
|MDIO|36|OD, IO|Management Data Input/Output: Bidirectional management data signal that is sourced by either the management station or the PHY. This pin requires an external pull-up resistor (recommended value = 2.2kΩ) .|
|CONTROL INTERFACE||||
|INT|2|PU, OD, O|Interrupt: Active-LOW output, which is asserted LOW when an interrupt condition occurs. This pin has a weak internal pullup. Register access is necessary to enable various interrupt triggers. Once an interrupt event flag is set, register access is required to clear the interrupt event on this pin. This pin can be configured as an Active-HIGH output using register[0x0011]. To capture the interrupt source reliably, status from interrupt registers x12, x13, x18 is recommended to be read after interrupt is asserted on int_n pin.|
|RESET|3|PU, I|RESET: Active-LOW input, which initializes or reinitializes the DP83TG720S-Q1. Asserting this pin LOW for at least 10μs forces a reset process to occur. All internal registers reinitialize to the default states as specified for each bit in the Register Map section. All bootstrap pins are resampled upon deassertion of reset.|
|INH|10|PMOS OD|INH: Active-HIGH PMOS open-drain output. When the PHY enters the sleep state, PHY releases the INH pin to allow an external pull-down resistor (recommended value = 10kΩ) to pull the line to ground. When in any other state, the INH pin drives a HIGH state to the VSLEEP rail.|
|WAKE|8|PD, I|WAKE: Active-HIGH (this pin works on VSLEEP domain) pulse on wake-up pin wakes up the PHY from the sleep state. For pulse width, refer to timing section. This pin can be directly tied to the VSLEEP rail when the sleep state is not used or left float.|



4 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Col1|Col2|Col3|Table 4-1. Pin Functions (continued)|
|---|---|---|---|
|PIN||STATE(1)|DESCRIPTION (2)|
|NAME|NO.|||
|STRP_1|14|I|Strap 1: This pin is for strapping PHY_AD bits.|
|CLOCK INTERFACE||||
|XI|5|I|Reference Clock Input: Reference clock 25MHz ±100ppm-tolerance crystal or oscillator input. The device supports either an external crystal resonator connected across pins XI and XO, or an external CMOS-level oscillator connected to pin XI only and XO left floating.|
|XO|4|O|Reference Clock Output: XO pin is used for crystal only. This pin is left floating when a CMOS-level oscillator is connected to XI.|
|LED/GPIO INTERFACE||||
|LED_0 / GPIO_0|35|S, PD, IO|LED_0: Link Status|
|LED_1 / GPIO_1|6|S, PD, IO|LED_1: Link Status and BLINK for TX/RX Activity|
|CLKOUT / GPIO_2|16|IO|Clock Output: 25MHz reference clock(buffered replication of XI) by default. If not used, clock output can be disabled by writing register 0x0453 = 0x0006.|
|MEDIUM DEPENDENT INTERFACE||||
|TRD_M|13|IO|Differential Transmit and Receive: Bidirectional differential signaling configured for 1000BASE-T1 operation, IEEE 802.3bp compliant.|
|TRD_P|12|||
|POWER AND GROUND CONNECTIONS||||
|VDDA3P3|11|SUPPLY|Core Supply: 3.3V. Refer to power supply recommendations for decoupling network.|
|VDDIO|22, 34|SUPPLY|IO Supply: 1.8V, 2.5V, or 3.3V. Refer to power supply recommendations for decoupling network.|
|VDD1P0|9, 21|SUPPLY|Core Supply: 1.0V. Refer to power supply recommendations for decoupling network.|
|VSLEEP|7|SUPPLY|Sleep Supply: 3.3V. Refer to power supply recommendations for decoupling network. This pin shall be tied to VDDA3P3 if sleep functionality is not used.|
|GROUND|DAP|GROUND|Ground|
|DO NOT CONNECT||||
|DNC|17, 18, 19, 20|DNC|DNC: Do Not Connect (test structures connected to these pins and must be kept floating to avoid damage or wrong mode entry of PHY)|


(1) Type: I = Input
O = Output
IO = Input/Output
OD = Open Drain
PD = Internal Pulldown

PU = Internal Pullup
S = Strap: Configuration pin (all configuration pins have weak internal pullups or pulldowns)
(2) When pins are unused, follow the recommended connection requirements provided in the table above. The pins which do not have
required termination can be left floating.

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 5

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **4.1 Pin States**

(1) Type: I = Input
O = Output
IO = Input/Output
OD = Open Drain
PD = Internal pulldown
PU = Internal pullup

|Col1|Table 4-2. Pin States -|Col3|Col4|RGMII|Col6|Col7|
|---|---|---|---|---|---|---|
|PIN NAME|POWER-UP / RESET|||NORMAL OPERATION - RGMII|||
||PIN STATE(1)|PULL TYPE|PULL VALUE (kΩ)|PIN STATE (1)|PULL TYPE|PULL VALUE (kΩ)|
|MDC|I|none|-|I|none|-|
|INT_N|I|PU|9|OD|PU|9|
|RESET_N|I|PU|9|I|PU|9|
|XO|O|none|-|O|none|-|
|XI|I|none|-|I|none|-|
|LED_1|I|PD|9|O|none|-|
|WAKE|I|PD|50|I|PD|50|
|STRP_1|I|PD|6.3|I|none|-|
|INH|PMOS,OD,O|none|-|PMOS OD, O|none|-|
|RX_CTRL|I|PD|6.3|O|none|-|
|CLKOUT/GPIO_2|O|none|-|O|none|-|
|RX_D3|I|PD|9|O|none|-|
|RX_D2|I|PD|9|O|none|-|
|RX_D1|I|PD|9|O|none|-|
|RX_D0|I|PD|9|O|none|-|
|RX_CLK|I|PD|9|O|none|-|
|TX_CLK|I|none|-|I|none|-|
|TX_CTRL|I|none|-|I|none|-|
|TX_D3|I|none|-|I|none|-|
|TX_D2|I|none|-|I|none|-|
|TX_D1|I|none|-|I|none|-|
|TX_D0|I|none|-|I|none|-|
|LED_0|I|PD|9|O|none|-|
|MDIO|I|none|-|IO|none|-|



6 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

(1) Type: I = Input
O = Output
IO = Input/Output
OD = Open Drain
PD = Internal pulldown
PU = Internal pullup
Hi-Z = High Impedence

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **Table 4-3. Pin States - SGMII**

|PIN NAME|POWER-UP / RESET|Col3|Col4|NORMAL OPERATION - SGMII|Col6|Col7|
|---|---|---|---|---|---|---|
||PIN STATE (1)|PULL TYPE|PULL VALUE (kΩ)|PIN STATE (1)|PULL TYPE|PULL VALUE (kΩ)|
|MDC|I|none|-|I|none|-|
|INT_N|I|PU|9|OD|PU|9|
|RESET_N|I|PU|9|I|PU|9|
|XO|O|none|-|O|none|-|
|XI|I|none|-|I|none|-|
|LED_1|I|PD|9|O|none|-|
|WAKE|I|PD|50|I|PD|50|
|STRP_1|I|PD|6.3|I|none|-|
|INH|PMOS,OD,O|none|-|PMOS OD, O|none|-|
|RX_CTRL|I|PD|6.3|I|PD|6.3|
|CLKOUT/GPIO_2|O|none|-|O|none|-|
|RX_D3|I|PD|9|O|none|-|
|RX_D2|I|PD|9|O|none|-|
|RX_D1|I|PD|9|Hi-Z|PD|9|
|RX_D0|I|PD|9|Hi-Z|PD|9|
|RX_CLK|I|PD|9|Hi-Z|PD|9|
|TX_CLK|I|none|-|Hi-Z|none|-|
|TX_CTRL|I|none|-|Hi-Z|none|-|
|TX_D3|I|none|-|Hi-Z|none|-|
|TX_D2|I|none|-|Hi-Z|none|-|
|TX_D1|I|none|-|I|none|-|
|TX_D0|I|none|-|I|none|-|
|LED_0|I|PD|9|O|none|-|
|MDIO|I|none|-|IO|none|-|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 7

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Table 4-4. Pin States - Slee p and Isolate**

(1) Type: I = Input
O = Output
IO = Input/Output
OD = Open Drain
PD = Internal pulldown
PU = Internal pullup
Hi-Z = High Impedence
Float = IO is not powered and hence pin is not biased by the PHY
(2) PD only for Rgmii's isolate mode. **Note** For sleep mode entry vdda, vddio and vdd1p0 are supposed to be powered-down. See figure Re q uired Implementation of Sleep Mode for further details.

|PIN NAME|MAC ISOLATE|Col3|Col4|SLEEP|Col6|Col7|
|---|---|---|---|---|---|---|
||PIN STATE (1)|PULL TYPE|PULL VALUE (kΩ)|PIN STATE (1)|PULL TYPE|PULL VALUE (kΩ)|
|MDC|I|none|-|Float|none|-|
|INT_N|O|PU|9|Float|none|-|
|RESET_N|I|PU|9|Float|none|-|
|XO|O|none|-|Float|none|-|
|XI|I|none|-|Float|none|-|
|LED_1|O|none|-|Float|none|-|
|WAKE|I|PD|50|I|none|50|
|STRP_1|I|none|-|Float|none|-|
|INH|PMOS,OD,O|none|-|PMOS OD, O|none|-|
|RX_CTRL|I|PD|6.3|Float|none|-|
|CLKOUT/GPIO_2|O|none|-|Float|none|-|
|RX_D3|I|PD/none(2)|9|Float|none|-|
|RX_D2|I|PD/none(2)|9|Float|none|-|
|RX_D1|I|PD|9|Float|none|-|
|RX_D0|I|PD|9|Float|none|-|
|RX_CLK|I|PD|9|Float|none|-|
|TX_CLK|I|none|-|Float|none|-|
|TX_CTRL|I|none|-|Float|none|-|
|TX_D3|I|none|-|Float|none|-|
|TX_D2|I|none|-|Float|none|-|
|TX_D1|I|none|-|Float|none|-|
|TX_D0|I|none|-|Float|none|-|
|LED_0|O|none|-|Float|none|-|
|MDIO|IO|none|-|Float|none|-|



8 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **4.2 Pin Power Domain**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Col1|Table 4-5. Pin Power Domain Table|Col3|
|---|---|---|
|Pin|RGMII Mode|SGMII Mode|
|MDC|VDDIO|VDDIO|
|INT_N|VDDIO|VDDIO|
|RESET_N|VDDIO|VDDIO|
|XI|VDDIO|VDDIO|
|XO|VDDIO|VDDIO|
|LED_1|VDDIO|VDDIO|
|WAKE|VSLEEP|VSLEEP|
|STRP_1|VDDIO|VDDIO|
|INH|VSLEEP|VSLEEP|
|RX_CTRL|VDDIO|VDDIO|
|CLKOUT/GPIO_2|VDDIO|VDDIO|
|RX_D3|VDDIO|VDDA|
|RX_D2|VDDIO|VDDA|
|RX_D1|VDDIO|VDDIO|
|RX_D0|VDDIO|VDDIO|
|RX_CLK|VDDIO|VDDIO|
|TX_CLK|VDDIO|VDDIO|
|TX_CTRL|VDDIO|VDDIO|
|TX_D3|VDDIO|VDDIO|
|TX_D2|VDDIO|VDDIO|
|TX_D1|VDDIO|VDDA|
|TX_D0|VDDIO|VDDA|
|LED_0|VDDIO|VDDIO|
|MDIO|VDDIO|VDDIO|
|TRD_P|VDDA|VDDA|
|TRD_M|VDDA|VDDA|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 9

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **5 Specifications** **5.1 Absolute Maximum Ratings** over operating free-air temperature range (unless otherwise noted) [(1)]

(1) Stresses beyond those listed under *Absolute Maximum Rating* can cause permanent damage to the device. These are stress
ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under
*Recommended Operating Condition* . Exposure to absolute-maximum-rated conditions for extended periods can affect device reliability.

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.

|Col1|Col2|MIN TYP MAX|UNIT|
|---|---|---|---|
|Supply Voltage|VDDA3P3|-0.5 4|V|
|Supply Voltage|VDD1P0|-0.5 1.4|V|
|Supply Voltage|VDDIO (3.3V)|-0.5 4|V|
|Supply Voltage|VDDIO (2.5V)|-0.5 2.9|V|
|Supply Voltage|VDDIO (1.8V)|-0.5 2.2|V|
|Supply Voltage|V SLEEP|-0.5 4|V|
|MDI Pins|TRD_M, TRD_P|-0.5 4|V|
|LVCMOS/ LVTTL Input Voltage|MDC, RESET, XI, LED_1, STRP_1, RX_CTRL, CLKOUT, RX_D[3:0], TX_CLK, TX_CTRL, TX_D[3:0], LED_0, MDIO|-0.5 VDDIO + 0.3|V|
|LVCMOS/ LVTTL Input Voltage|WAKE|-0.5 V + 0.3 SLEEP|V|
|LVCMOS/ LVTTL Output Voltage|INT, LED_1, RX_CTRL, CLKOUT, RX_D[3:0], RX_CLK, LED_0, MDIO|-0.5 VDDIO + 0.3|V|
|LVCMOS/ LVTTL Output Voltage|INH|VSLEEP + -0.5 0.3|V|
|T J|Junction Temperature|150|°C|
|T stg|Storage temperature|-65 150|°C|


|5.2 ESD Ratings|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||VALUE|UNIT|
|V (ESD)|Electrostatic discharge|Human body model (HBM), per AEC Q100-002(1)|All pins|±2000|V|
|V (ESD)|Electrostatic discharge|Human body model (HBM), per AEC Q100-002(1)|TRD_M, TRD_P|±8000|V|
|V (ESD)|Electrostatic discharge|Charged device model (CDM), per AEC Q100-011|All pins|±500|V|
|V (ESD)|Electrostatic discharge|IEC 61000-4-2 contact discharge|TRD_M, TRD_P|±8000|V|



10 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.3 Recommended Operating Conditions** over operating free-air temperature range (unless otherwise noted)

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Col1|Col2|MIN NOM MAX|UNIT|
|---|---|---|---|
|VDDIO|IO Supply Voltage, 1.8V operation|1.62 1.8 1.98|V|
||IO Supply Voltage, 2.5V operation|2.25 2.5 2.75||
||IO Supply Voltage, 3.3V operation|2.97 3.3 3.63||
|VDDA3P3|Core Supply Voltage, 3.3V|2.97 3.3 3.63|V|
|VDD1P0|Core Supply Voltage, 1.0V|0.95 1 1.1|V|
|V SLEEP|Sleep Supply Voltage, 3.3V|2.97 3.3 3.63|V|
|T A|Ambient temperature|–40 125|°C|

|5.4 Thermal Information|Col2|Col3|Col4|
|---|---|---|---|
|THERMAL METRIC(1)||DP83TG720|UNIT|
|||RHA (VQFN)||
|||36 PINS||
|R θJA|Junction-to-ambient thermal resistance|32.5|°C/W|
|R θJC(top)|Junction-to-case (top) thermal resistance|22.2|°C/W|
|R θJB|Junction-to-board thermal resistance|13.3|°C/W|
|Ψ JT|Junction-to-top characterization parameter|0.3|°C/W|
|Ψ JB|Junction-to-board characterization parameter|13.3|°C/W|
|R θJC(bot)|Junction-to-case (bottom) thermal resistance|3.2|°C/W|


(1) [For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application](http://www.ti.com/lit/SPRA953)
report.
###### **5.5 Electrical Characteristics** Over operating free-air temperature range (unless otherwise noted) [(1)]

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|DC CHARACTERISTICS|||||
|XI|||||
|V IH|High-level Input Voltage||1.3|V|
|V IL|Low-level Input Voltage||0.5|V|
|WAKE pin|WAKE pin|WAKE pin|WAKE WAKE WAKE pin pin pin|WAKE pin|
|V IH|High-level Input Voltage|V = 3.3V ± 10% SLEEP|2|V|
|V IL|Low-level Input Voltage|V = 3.3V ± 10% SLEEP|0.8|V|
|INH pin|INH pin|INH pin|INH pin INH pin INH pin|INH pin|
|V OH|High-level Output Voltage|I = -2mA, V = 3.3V ± 10% OH SLEEP|2.4|V|
|3.3V VDDIO (2)|||||
|V OH|High-level Output Voltage|I = -2mA, VDDIO = 3.3V ± 10% OH|2.4|V|
|V OL|Low-level Output Voltage|I = 2mA, VDDIO = 3.3V ± 10% OL|0.4|V|
|V IH|High-level Input Voltage|VDDIO = 3.3V ± 10%|2|V|
|V IL|Low-level Input Voltage|VDDIO = 3.3V ± 10%|0.8|V|
|2.5V VDDIO (2)|||||
|V OH|High-level Output Voltage|I = -2mA, VDDIO = 2.5V ± 10% OH|2|V|
|V OL|Low-level Output Voltage|I = 2mA, VDDIO = 2.5V ± 10% OL|0.4|V|
|V IH|High-level Input Voltage|VDDIO = 2.5V ± 10%|1.7|V|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 11

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **5.5 Electrical Characteristics (continued)** Over operating free-air temperature range (unless otherwise noted) [(1)]

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|V IL|Low-level Input Voltage|VDDIO = 2.5V ± 10%|0.7|V|
|1.8V VDDIO (2)|||||
|V OH|High-level Output Voltage|I = -2mA, VDDIO = 1.8V ± 10% OH|VDDIO – 0.45|V|
|V OL|Low-level Output Voltage|I = 2mA, VDDIO = 1.8V ± 10% OL|0.45|V|
|V IH|High-level Input Voltage|VDDIO = 1.8V ± 10%|0.7 * VDDIO|V|
|V IL|Low-level Input Voltage|VDDIO = 1.8V ± 10%|0.3 * VDDIO|V|
|I IH|Input High Current (MDIO)|VIN = VCC, -40°C to 125°C|-5 5|µA|
|I IH|Input High Current (RGMII Input pin,MDC)|VIN = VCC, -40°C to 125°C|-20 20|µA|
|I OZ|Input High Current (MDIO)|VIN swept from 0V till VCC, -40°C to 125°C|-40 40|µA|
|I IL|Input Low Current (RGMII Input pin, MDC, MDIO)|VIN = GND, -40°C to 125°C|-40 5|µA|
|I OZL||INH|6|µA|
|I OZ|Tri-state Output Current (5)|VIN swept from 0V till VCC, -40°C to 125°C|-40 10|µA|
|I OZ|Tri-state Output Current (6)|VIN swept from 0V till VCC, -40°C to 125°C|-60 60|µA|
|C IN|Input Capacitance|LVCMOS/LVTTL pins (3)|2|pF|
|C IN|Input Capacitance|LVCMOS/LVTTL pins (4)|4|pF|
|||XI|1|pF|
|C OUT|Output Capacitance|LVCMOS/LVTTL pins (3)|2|pF|
|C OUT|Output Capacitance|LVCMOS/LVTTL pins (4)|4|pF|
|||XO|1|pF|
|R pull-up|Integrated Pull-Up Resistance|INT, RESET|6.5 9 12.5|kΩ|
|R pull-down|Integrated Pull-Down Resistance|STRP_1, RX_CTRL|4.725 6.3 7.875|kΩ|
|R pull-down|Integrated Pull-Down Resistance|LED_1, RX_D[3:0], RX_CLK, LED_0|7.3 9 13|kΩ|
|||WAKE|35 50 62.5|kΩ|
|R pull-down|Integrated Pull-Up Resistance when Active|INH|106|Ω|
|R series|Integrated MAC Series Termination Resistor ( Default)|RX_D[3:0], RX_CTRL, and RX_CLK|24 42 52|Ω|
|Rseries|Integrated MAC Series Terminatin Resistor (with register<0x0456> = 0x0148)|RX_D[3:0], RX_CTRL, and RX_CLK|30 52 65|Ω|
|Rseries|Integrated MAC Series Terminatin Resistor (with register<0x0456> = 0x0168)|RX_D[3:0], RX_CTRL, and RX_CLK|40 70 84|Ω|
|CURRENT CONSUMPTION, SLEEP MODE|||||
|I SLEEP|Sleep Supply Current|V SLEEP|485 840|µA|
|CURRENT CONSUMPTION, RESET ASSERTED|||||
|I DDIO|IO Supply Current, VDDIO = 1.8V|VDDIO|4 9|mA|
|I DDIO|IO Supply Current, VDDIO = 2.5V|VDDIO|5 12|mA|
|I DDIO|IO Supply Current, VDDIO = 3.3V|VDDIO|6.5 15|mA|
|I DDA3P3|Core Supply Current, 3.3V|VDDA3P3|5 8|mA|



12 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.5 Electrical Characteristics (continued)** Over operating free-air temperature range (unless otherwise noted) [(1)]

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|I DD1P0|Core Supply Current, 1.0V|VDD1P0|30 110|mA|
|CURRENT CONSUMPTION, STANDBY|||||
|I DDIO|IO Supply Current, VDDIO = 1.8V|VDDIO|4 11|mA|
|I DDIO|IO Supply Current, VDDIO = 2.5V|VDDIO|6 13|mA|
|I DDIO|IO Supply Current, VDDIO = 3.3V|VDDIO|8 15|mA|
|I DDA3P3|Core Supply Current, 3.3V|VDDA3P3|16 18|mA|
|I DD1P0|Core Supply Current, 1.0V|VDD1P0|33 112|mA|
|CURRENT CONSUMPTION, ACTIVE MODE, Voltage: +/- 10%, Traffic : 100%,Packet Size: 1518, Content : Random|||||
|I DDIO|IO Supply Current, VDDIO = 1.8V|RGMII|20 25|mA|
|I DDIO|IO Supply Current, VDDIO = 2.5V|RGMII|26 30|mA|
|I DDIO|IO Supply Current, VDDIO = 3.3V|RGMII|33 40|mA|
|I DDIO|IO Supply Current, VDDIO = 1.8V|SGMII|3.5 5|mA|
|I DDIO|IO Supply Current, VDDIO = 2.5V|SGMII|5 7|mA|
|I DDIO|IO Supply Current, VDDIO = 3.3V|SGMII|6.5 8|mA|
|I DDA3P3|Core Supply Current, 3.3V|RGMII|85 89|mA|
|I DD1P0|Core Supply Current, 1.0V|RGMII|177 250|mA|
|I DDA3P3|Core Supply Current, 3.3V|SGMII|95 100|mA|
|I DD1P0|Core Supply Current, 1.0V|SGMII|200 260|mA|
|I SLEEP|Sleep Supply Current|V SLEEP = 3.3V +/- 10%|1000 1500|µA|
|MDI CHARACTERISTICS|||||
|V OD-MDI|Output Differential Voltage|R = 100 Ω L(diff)|1.3|V|
|R MDI-DIFF|Integrated Differential MDI Termination (Active State)|TRD_P, TRD_M|100|Ω|
|R MDI-DIFF|Integrated Differential MDI Termination (Sleep State)|TRD_P, TRD_M|100|Ω|
|SGMII DRIVER DC SPECIFICATIONS|||||
|V OD-SGMII|Output Differential Voltage|R = 100 Ω L(diff)|150 400|mV|
|R OUT-DIFF|Integrated Differential Output Termination|RX_P, RX_M|78 100 130|Ω|
|SGMII RECEIVER DC SPECIFICATIONS|||||
|V IDTH|Input Differential Threshold||100|mV|
|R IN-DIFF|Integrated Differential Input Termination|TX_P, TX_M|82 100 121|Ω|
|BOOTSTRAP DC CHARACTERISTICS|||||
|2 level straps|||||
|Vbsl_1v8|Bootstrap Threshold|Mode 1, VDDIO = 1.8V ± 10%, 2-level|0.35*VD 0 DIO|V|
|Vbsh_1v 8|Bootstrap Threshold|Mode 2, VDDIO = 1.8V ± 10%, 2-level|1.175 VDDIO|V|
|Vbsl_2v5|Bootstrap Threshold|Mode 1, VDDIO = 2.5V ± 10%, 2-level|0 0.7|V|
|Vbsh_2v 5|Bootstrap Threshold|Mode 2, VDDIO = 2.5V ± 10%, 2-level|1.175 VDDIO|V|
|Vbsl_3v3|Bootstrap Threshold|Mode 1, VDDIO = 3.3V ± 10%, 2-level|0 0.7|V|
|Vbsh_3v 3|Bootstrap Threshold|Mode 2, VDDIO = 3.3V ± 10%, 2-level|1.175 VDDIO|V|
|3 level straps|||||


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 13

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **5.5 Electrical Characteristics (continued)** Over operating free-air temperature range (unless otherwise noted) [(1)]

(1) Verified by production test, characterization or design
(2) For pins: LED_1, STRP _ 1, RX_CTRL, CLKOUT, RX_D[3:0], RX_CLK, LED_0
(3) For pins: MDC, INT, RESET, LED_1, STRP_1, RX_CTRL, CLKOUT, RX_D0, RX_D1, RX_CLK, TX_CLK, TX_CTRL, TX_D2, TX_D3,
LED_0, and MDIO
(4) For pins: TX_D0, TX_D1, RX_D2, and RX_D3
(5) For pins : LED_1, RX_D[3:0], RX_CLK, LED_0
(6) For pins : STRP_1 and RX_CTRL

|PARAMETER|Col2|TEST CONDITIONS|MIN TYP MAX|UNIT|
|---|---|---|---|---|
|V bs1_1V8|Bootstrap Threshold|Mode 1, VDDIO = 1.8V ± 10%, 3-level|0.35 * 0 VDDIO|V|
|V bs2_1V8|Bootstrap Threshold|Mode 2, VDDIO = 1.8V ± 10%, 3-level|0.40 * 0.75 * VDDIO VDDIO|V|
|V bs3_1V8|Bootstrap Threshold|Mode 3, VDDIO = 1.8V ± 10%, 3-level|0.84 * VDDIO VDDIO|V|
|V bs1_2V5|Bootstrap Threshold|Mode 1, VDDIO = 2.5V ± 10%, 3-level|0.19 * 0 VDDIO|V|
|V bs2_2V5|Bootstrap Threshold|Mode 2, VDDIO = 2.5V ± 10%, 3-level|0.27 * 0.41 * VDDIO VDDIO|V|
|V bs3_2V5|Bootstrap Threshold|Mode 3, VDDIO = 2.5V ± 10%, 3-level|0.58 * VDDIO VDDIO|V|
|V bs1_3V3|Bootstrap Threshold|Mode 1, VDDIO = 3.3V ± 10%, 3-level|0.18 * 0 VDDIO|V|
|V bs2_3V3|Bootstrap Threshold|Mode 2, VDDIO = 3.3V ± 10%, 3-level|0.22 * 0.42 * VDDIO VDDIO|V|
|V bs3_3V3|Bootstrap Threshold|Mode 3, VDDIO = 3.3V ± 10%, 3-level|0.46 * VDDIO VDDIO|V|
|Temperature Sensor|||||
||Temperature Sensor Resolution (LSB)|-40℃ to 125℃|1.5|℃|
||Temperature Sensor Accuracy ( Voltage and Temperature Variation on single part)|-40℃ to 125℃|-7.5 7.5|℃|
||Temperature Sensor Accuracy ( Voltage, Temperature and Part-to-Part variation)|-40℃ to 125℃|-21.5 20|℃|
||Temperature Sensor Range||-40 140|℃|
|Voltage Sensor|||||
||VDDA3P3 Sensor Range||2.66 3.3 3.96|V|
||VDDA3P3 Sensor Resolution (LSB)|-40℃ to 125℃|8.6|mV|
||VDDA3P3 Sensor Accuracy ( Voltage and Temperature Variation)|-40℃ to 125℃|8.6|mV|
||VDDA3P3 Sensor Accuracy Part-to-Part|-40℃ to 125℃|-68.8 68.8|mV|
||VDD1P0 Sensor Range||0.8 1.2|V|
||VDD1P0 Sensor Resolution (LSB)|-40℃ to 125℃|2.8|mV|
||VDD1P0 Sensor Accuracy ( Voltage and Temperature Variation)|-40℃ to 125℃|2.8|mV|
||VDD1P0 Sensor Accuracy Part-to-Part|-40℃ to 125℃|-22.4 22.4|mV|
||VDDIO Sensor Range||1.44 3.8|V|
||VDDIO Sensor Resolution (LSB)|-40℃ to 125℃|15.4|mV|
||VDDIO Sensor Accuracy ( Voltage and Temperature Variation)|-40℃ to 125℃|15.4|mV|
||VDDIO Sensor Accuracy Part-to-Part|-40℃ to 125℃|-78 78|mV|



14 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.6 Timing Requirements**

(1)

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|PARAMETER|Col2|TEST CONDITIONS|MIN NOM MAX|UNIT|
|---|---|---|---|---|
|POWER-UP TIMING|||||
|T5.1|VDDA3P3 Duration(2)|0% to 100% (+/- 10% VDDA3P3)|0.5 40|ms|
|T5.2|VDD1P0 Duration(2)|0% to 100% (+/- 10% VDD1P0)|0.1 40|ms|
|T5.2|VDDIO Duration(2)|VDDIO = 1.8V|0.1 40|ms|
|T5.2|VDDIO Duration(2)|VDDIO = 2.5V|0.1 40|ms|
|T5.2|VDDIO Duration(2)|VDDIO = 3.3V|0.1 40|ms|
|T5.2|V (2) SLEEP Duration|0% to 100% (+/- 10% V ) SLEEP|0.1 40|ms|
|T5.3|Crystal stabilization-time post power-up (from last power rail ramp to 100%)||1500|µs|
|T5.4|Osillator stabilization-time post power-up ( from last power rail ramp to 100%)(3)||20|ms|
|T5.5|Post power-up stabilization-time prior to MDC preamble for register access||65|ms|
|T5.6|Hardware configuration latch-in time from power-up||60|ms|
|T5.7|Hardware configuration pins transition to functional mode from latch-in completion||110|ns|
|T5.8|PAM3 IDLE Stream from power-up (Master Mode)||60|ms|
|RESET TIMING (RESET_N)|||||
|T6.1|RESET pulse width||5|µs|
|T6.2|Post reset stabilization-time prior to MDC preamble for register access||1|ms|
|T6.3|Hardware configuration latch-in time from reset||2|µs|
|T6.4|Hardware configuration pins transition to functional mode from latch-in completion||1.5|µs|
|T6.5|PAM3 IDLE Stream from reset (Master Mode)||1500|µs|
|SMI TIMING|||||
|T4.1|MDC to MDIO (Output) Delay Time (25 pF load)||0 6 10|ns|
|T4.2|MDIO (Input) to MDC Setup Time||10|ns|
|T4.3|MDIO (Input) to MDC Hold Time||10|ns|
||MDC Frequency ( 25 pF load)||2.5 20|MHz|
|RECEIVE LATENCY TIMING|||||
||SSD symbol on MDI to Rising edge of RGMII RX_CLK with assertion of RX_CTRL||8|µs|
||SSD symbol on MDI to Rising edge of RGMII RX_CLK with assertion of RX_CTRL (RS-FEC bypass mode)||400|ns|
||SSD symbol on MDI to first symbol of SGMII||9|µs|
||SSD symbol on MDI to first symbol of SGMII (RS-FEC bypass mode)||450|ns|
|TRANSMIT LATENCY TIMING|||||
||RGMII Rising edge TX_CLK with assertion TX_CTRL to SSD symbol on MDI||0.8|µs|
||RGMII Rising edge TX_CLK with assertion TX_CTRL to SSD symbol on MDI (RS-FEC bypass mode)||600|ns|
||First symbol of SGMII to SSD symbol on MDI||0.9|µs|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 15

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **5.6 Timing Requirements (continued)**

(1)

|PARAMETER|Col2|TEST CONDITIONS|MIN NOM MAX|UNIT|
|---|---|---|---|---|
||First symbol of SGMII to SSD symbol on MDI (RS-FEC bypass mode)||700|ns|
|25MHz OSCILLATOR REQUIREMENTS|||||
||Frequency (XI)||25|MHz|
||Frequency Tolerance and Stability Over temperature and aging||–100 100|ppm|
||Rise / Fall Time (10% - 90%)(6)||8|ns|
||Jitter (RMS)|Integrated upto 5MHz|1|ps|
||Duty Cycle||40 50 60|%|
|RGMII TIMING|||||
|T setupR|TX_D[3:0], TX_CTRL Setup to TX_CLK|on PHY pins|1 2|ns|
|T holdR|TX_D[3:0], TX_CTRL Hold from TX_CLK (5)|on PHY pins|1 2|ns|
|T skewT|RX_D[3:0], RX_CTRL Delay from RX_CLK (Align Mode Enabled)|On PHY Pins|-500 0 500|ps|
|T skewT (Shift)|RX_D[3:0], RX_CTRL Delay from RX_CLK (Shift Mode Enabled, default)(4)|On PHY Pins|2.190 2.650 2.970|ns|
|T cyc|Clock Cycle Duration|RX_CLK|7.2 8 8.8|ns|
|T cyc|Clock Cycle Duration|TX_CLK|7.2 8 8.8|ns|
|Duty_G|Duty Cycle|RX_CLK|45 50 55|%|
|Duty_G|Duty Cycle|TX_CLK|45 50 55|%|
|Tr|Rise Time (20% - 80%)|CL=Ctrace=5pF|0.75|ns|
|Tf|Fall Time (20% - 80%)|C = 5pF L=Ctrace|0.75|ns|
|RGMII RX Shift Mode Delays|DLL DLL_RX_DELAY_CTRL_SL=0(4)||0.330 0.650 0.970|ns|
||DLL DLL_RX_DELAY_CTRL_SL=1(4)||0.580 0.900 1.220|ns|
||DLL DLL_RX_DELAY_CTRL_SL=2(4)||0.830 1.150 1470|ns|
||DLL DLL_RX_DELAY_CTRL_SL=3(4)||1.000 1.400 1.720|ns|
||DLL DLL_RX_DELAY_CTRL_SL=4(4)||1.230 1.650 1.970|ns|
||DLL DLL_RX_DELAY_CTRL_SL=5(4)||1.490 1.990 2.220|ns|
||DLL DLL_RX_DELAY_CTRL_SL=6(4)||1.690 2.150 2.470|ns|
||DLL DLL_RX_DELAY_CTRL_SL=7(4)||1.960 2.400 2.730|ns|
||DLL DLL_RX_DELAY_CTRL_SL=8(4)||2.180 2.650 2.970|ns|
||DLL DLL_RX_DELAY_CTRL_SL=9(4)||2.490 2.900 3.220|ns|
|RGMII Shift TX Mode Delays|||||
||DLL DLL_TX_DELAY_CTRL_SL=1(4) (8)||0.08 0.25 0.38|ns|
||DLL DLL_TX_DELAY_CTRL_SL=2(4) (8)||0.27 0.49 0.67|ns|
||DLL DLL_TX_DELAY_CTRL_SL=3(4) (8)||0.51 0.73 0.91|ns|
||DLL DLL_TX_DELAY_CTRL_SL=4(4) (8)||0.75 0.97 1.15|ns|
||DLL DLL_TX_DELAY_CTRL_SL=5(4) (8)||0.94 1.21 1.44|ns|
||DLL DLL_TX_DELAY_CTRL_SL=6(4) (8)||1.18 1.45 1.68|ns|
||DLL DLL_TX_DELAY_CTRL_SL=7(4) (8)||1.37 1.69 1.98|ns|



16 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.6 Timing Requirements (continued)**

(1)

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|PARAMETER|Col2|TEST CONDITIONS|MIN NOM MAX|UNIT|
|---|---|---|---|---|
||DLL DLL_TX_DELAY_CTRL_SL=8(4) (8)||1.61 1.93 2.22|ns|
||DLL DLL_TX_DELAY_CTRL_SL=9(4) (8)||1.85 2.17 2.46|ns|
||DLL DLL_TX_DELAY_CTRL_SL=10(4) (8)||2.04 2.42 2.75|ns|
||DLL DLL_TX_DELAY_CTRL_SL=11(4) (8)||2.28 2.65 2.99|ns|
||DLL DLL_TX_DELAY_CTRL_SL=12(4) (8)||2.52 2.9 3.23|ns|
|SGMII TRANSMITTER AC TIMING|||||
||Clock signal duty cycle at 625MHz||48 52|%|
|T rise|Vod Rise Time||100 200|ps|
|T fall|Vod Fall Time||100 200|ps|
|Jitter|Output jitter||200 320 (7)|ps|
|25MHz CRYSTAL REQUIREMENTS|||||
||Frequency||25|MHz|
||Frequency Tolerance and Stability Over temperature and aging||–100 100|ppm|
||Equivalent Series Resistance||100|Ω|
|OUTPUT CLOCK TIMING (CLKOUT)|||||
||Frequency||25|MHz|
||Duty Cycle ( With crystal attached)||45 55|%|
||Rise / Fall Time (10% - 90%)||2.5|ns|
||Jitter (RMS) (Slave Mode, MAC Iinterface : SGMII)||5|ps|
||Jitter (RMS) (Master Mode, MAC Iinterface : SGMII)||2.4|ps|
||Jitter (RMS) (Slave Mode, MAC Interface : RGMII)||11|ps|
||Jitter (RMS) (Master Mode, MAC Interface : RGMII)||15|ps|
|Sleep Entry and Wake-Up|||||
||WAKE LOW to Sleep Entry; INH Transition LOW|Normal Mode, MDI_Energy = FALSE sleep_en = TRUE|64 85|us|
||sleep_en = True to Sleep Entry; INH Transition LOW (master mode)|Normal Mode, WAKE = LOW, MDI_Energy = FALSE|5 85|us|
||sleep_en = True to Sleep Entry; INH Transition LOW (slave mode)|Normal Mode, WAKE = LOW, MDI_Energy = FALSE|5000|us|
||MDI Energy Loss to Sleep Entry; INH Transition LOW|Normal Mode, WAKE = LOW, sleep_en = TRUE|5|ms|
||Local Wake-Up Pulse Duration (on Wake pin)|Sleep Mode, WAKE pin|80|µs|
||Send-S/Send-T pattern duration for wake up from MDI|Sleep Mode, Slave|1.25|ms|
||Local Wake-Up; INH Transition HIGH|Sleep Mode, rising edge of WAKE pin to rising edge of INH|85|us|
||Tolerable differential noise level on MDI for PHY to stay in sleep mode|Sleep Mode|200|mV pk-pk|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 17

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **5.6 Timing Requirements (continued)**

(1)

(1) Verified by production test or characterization or design.
(2) No supply sequencing constraint across power rails
(3) In case OSC clock is delayed, additional reset is needed post Osc clock stablisation
(4) Refer register[0x0430] for programmability of RX and TX delay codes
(5) PHY provides internal delays on TX_CLK to TX_D[3:0] to add additional skew upto 2ns. Refer to register[0x0430] for programmability
(6) Max rise/fall time of 8ns is supported for duty cycle of 40% to 55%. Max rise/fall time of 6ns is supported for duty cycle of 40% to 60%
(7) Additional register configuration available to reduce this max number to 300ps (if required)
(8) Data for 1.8V VDDIO.

|PARAMETER|Col2|TEST CONDITIONS|MIN NOM MAX|UNIT|
|---|---|---|---|---|
||Link-partner's VOD for valid wake-up (for 5m cable)|Sleep Mode|840|mV pk-pk|



18 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.7 Timing Diagrams**

XI (crystal)

XI (oscillator)

VDDA

|ms|Col2|
|---|---|
|||
|||
|||
|||



V DDIO / V DD1P0 / Vsleep

Latch-in

Active

I/O Pins

+1

PAM3

0

(Master)

-1

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Col1|T5.2|Col3|
|---|---|---|
||T5.2||
||tT5.5t tT5.6t tT5.7t||
||||
||||
||||
||||
||||
||||

###### **Figure 5-1. Power Up Timing**

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 19

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)**

V VDD

XI


tT6.1t


Hardware
RESET_N

MDC

Bootstrap
Latch-in


tT6.2t


tT6.3t


Active
tT6.4t
I/O Pins


tT6.5t


PAM3
(Master)


+1

0

-1

TX_CLK

TX_D[3:0]

###### **Figure 5-2. Reset Timing**


|tTcyct Thold(shift)|Col2|Col3|
|---|---|---|
|Valid Data Valid Data||Valid Data|
|Tsetup(shift) TX_ER TX_EN TX_ER TX_EN|||

###### **Figure 5-3. RGMII Transmit Timing (Internal Delay Enabled)**

20 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

T hold(align)


TX_CLK

TX_D[3:0]


tT cyc t

T setup(align)

|Valid Data Valid Data|Col2|Valid Data|
|---|---|---|


|TX_EN TX_ER|TX_EN|TX_ER|
|---|---|---|

###### **Figure 5-4. RGMII Transmit Timing (Internal Delay Disabled)**

tT cyc t

RX_CLK

T skew(shift)

|Valid Data Valid Data|V|alid Data|
|---|---|---|
||||
|RX_DV RX_ER RX_DV|RX_E|R RX_DV| **Figure 5-5. RGMII Receive Timing (Internal Delay Enabled)**

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 21

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)**

tT cyc t

RX_CLK

T skew(align)

|Valid Data|Col2|Col3|Valid Data|
|---|---|---|---|
|||||
|RX_DV RX_ER|||RX_DV| **Figure 5-6. RGMII Receive Timing (Internal Delay Disabled)**

MDC

tT4.1t **Figure 5-7. Serial Management Timing**

|Col1|Col2|Valid Data|Col4|
|---|---|---|---|


|Col1|Valid Data|
|---|---|



22 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **5.8 LED Drive Characteristics**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)


**Figure 5-8. LED V vs I for 3.3V VDDIO**

**Figure 5-9. LED V vs I for 2.5V VDDIO**

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 23

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6 Detailed Description** **6.1 Overview** The DP83TG720S-Q1 is a 1000BASE-T1 automotive Ethernet Physical Layer transceiver. It is IEEE 802.3bp compliant and AEC-Q100 qualified for automotive applications. This device is specifically designed to operate at 1Gbps speed while meeting stringent automotive EMC requirements. The DP83TG720S-Q1 transmits PAM3 ternary symbols at 750-MBd over unshielded/shielded single-twisted pair cable. It is designed for RGMII or SGMII support in a single 36-pin VQFN wettable flank package.

24 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.2 Functional Block Diagram**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **Figure 6-1. DP83TG720S-Q1 Functional Block Diagram**

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 25

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.3 Feature Description** ***6.3.1 Diagnostic Tool Kit*** The DP83TG720S-Q1 diagnostic tool kit provides mechanisms for monitoring normal operation, device-level debugging, system-level debugging, fault detection, and compliance testing. This tool kit includes a built-in self-test with PRBS data, various loopback modes, Signal Quality Indicator (SQI), Time Domain Reflectometry (TDR), voltage monitor, temperature monitor, electrostatic discharge monitor, and IEEE 802.3bp test modes. **6.3.1.1 Signal Quality Indicator** When the DP83TG720S-Q1 is active, the Signal Quality Indicator can be used to determine the quality of link based on SNR readings made by the device. SQI is derived based on the calculated SNR value and is presented as 8 level indication, where level of 5 provides a BER better than 10 [-10] . **Note** Refer to DP83TG720: Configuring for Open Alliance Specification Compliance application note for details on using SQI register for Open Alliance TC12 SQI tests. **6.3.1.2 Time Domain Reflectometry** Time domain reflectometry helps detecting and estimating the location of OPEN and SHORT faults along a cable. TDR is activated by setting bit[15] = 'b1 in the register[0x001E]. When TDR diagnostic process gets completed successfully, Bit[1:0] of register[0x001E] becomes 'b10. After this status change, TDR results can be read in the register of following table. **Table 6-1. TDR Result Re g isters : 0x030F** **Note**

|Register Bits|Description|
|---|---|
|[1:0]|• 01 = TDR Activation • 10 = TDR On • 00,11 = TDR Not Available|
|[3:2]|Reserved|
|[7:4]|• 0011 = Short • 0110 = Open • 0101 = Noise • 0111 = Cable OK • 1000 = Test in progress; initial value with TDR ON • 1101 = Test not possible (for example, noise, active link) • Other values are not valid|
|[13:8]|• Fault distance = Value in decimal of [13:8] • 'b111111 = Resolution not possible/out of distance|
|[15:14]|Reserved| TDR must not be run if the link is already active. Running TDR on active line can make TDR fail and also can result in disruption of link. Refer to DP83TG720: Configuring for Open Alliance Specification Compliance application note for detailed procedure of running TDR.

26 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.3.1.3 Built-In Self-Test For Datapath** The DP83TG720S-Q1 incorporates a data-path’s Built-In-Self-Test (BIST) to check the PHY level and system level data-paths. BIST has following integrated features which make the system level data transfer tests (through-put etc) and diagnostics possible without relying on MAC or external data generator hardware/software. 1. Loopback modes 2. Data generator a. Customizable MAC packets generator. b. Transmitted packet counter. c. PRBS stream generator. 3. Data checker a. Received MAC packets error checker. b. Received packet counter: Counts total packets received and packets received with errors. c. PRBS lock and PRBS error checker. ***6.3.1.3.1 Loopback Modes*** **Figure 6-2. All Loopbacks**

|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---| There are several loopback options within the DP83TG720S-Q1. Enabling different loopback modes enables/ bypass different data-paths according to system verification requirements. Different loopbacks can be enabled along-side following data generation options : a. Inbuilt data-generator b. External data-generator (on Ethernet cable or MAC side) Following diagrams illustrate data-flow during different loopback options : **Figure 6-3. Analog Loopback With Inbuilt Data-Gen**

|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 27

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Figure 6-4. Analog Loopback With External Data-Gen** **Figure 6-5. Digital Loopback With Inbuilt Data-Gen** **Figure 6-6. Digital Loopback With External Data-Gen** **Figure 6-7. PCS Loopback With Inbuilt Data-Gen** **Figure 6-8. PCS Loopback With External Data-Gen**

|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|


|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|


|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|


|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|


|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|



28 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Figure 6-9. xMII Loopback With External Data-Gen** **Figure 6-10. xMII Reverse Loopback With External Data-Gen**

|MAC|Col2|DIGITAL MII PCS AFE Data Data Generator Checker|MDI|
|---|---|---|---|

|MAC|Col2|DIGITAL PCS AFE Data Data MII Generator Checker|MDI|
|---|---|---|---|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 29

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** ***6.3.1.3.2 Data Generator*** Data generator can be programmed to generate either user defined MAC packets or PRBS stream. Following parameters of generated MAC packets can be configured (refer to registers<0x061B>,register<0x061A> and register<0x0624> for required configuration): • Packet Length • Inter-packet gap • Defined number of packets to be sent or continuous transmission • Packet data-type: Incremental/Fixed/PRBS • Number of valid bytes per packet

30 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) ***6.3.1.3.3 Programming Datapath BIST*** The following register settings enable different loopbacks, data generation and data checker procedures. **Table 6-2. Data p ath BIST Pro g rammin g**

|Col1|Loopback Mode|To enable loopback mode|To enable data generator and checker: MAC packets|To check in- coming MAC packets status|To enable data generator and checker: PRBS stream|To check in- coming PRBS status: PRBS stream|Other care- abouts|
|---|---|---|---|---|---|---|---|
|1|Analog loopback|write : reg[0x0016]=0x 0108 write : reg[0x0405]=0x 2800|write : reg[0x0624]=0x 55BF write : reg[0x0619]=0x 1555|read : reg[0x063C] for (15:0) of total received packets count. read : reg[0x063D] for (31:16) of total received packets count. read : reg[0x063E] for Packets received with CRC errors|write : reg[0x0624]=0x55 BF write : reg[0x0619]=0x05 57|Step 1: write : reg[0x0620](1) = 1'b1 Step 2 : read : reg[0x0620] (7:0) = Number of error bytes received. read : reg[0x0620] (8) (1 indicates PRBS data is coming in and checker is locked)|Disconnect the cable/link-partner. Generated data will be going to MAC side, to disable MAC side : write : reg[0x0000]=0x05 40|
|2|Digital loopback|write : reg[0x0016] = 0x0104 write : reg[0x0800] [11]=1|write : reg[0x0624]=0x 55BF write : reg[0x0619]=0x 1555|read : reg[0x063C] = [15:0] of total received packets count. read : reg[0x063D]= [31:16] of total received packets count. read : reg<0x063E> -> Packets received with CRC errors|write : reg[0x0624]=0x55 BF write : reg[0x0619]=0x05 57|Step 1 : write : reg[0x0620][1] = 1'b1 Step 2 : read : reg[0x0620] [7:0] = Number of error bytes received. read : reg[0x0620] [8] (1 indicates PRBS data is coming in and checker is locked)|Generated data will be going to Cu cable side, to disable this transmission : write : reg[0x041F] = 0x1000 Generated data will be going to MAC side, to disable MAC side : write : reg[0x0000]=0x05 40|
|3|PCS loopback|write : reg<0x0016> = 0x0101|write : reg[0x0624]=0x 55BF write : reg[0x0619]=0x 1555|read : reg[0x063C]= [15:0] of total received packets count. read : reg[0x063D]= [31:16] of total received packets count. read : reg[0x063E]= Packets received with CRC errors|write : reg[0x0624]=0x55 BF write : reg[0x0619]=0x05 57|Step 1 : write : reg[0x0620][1] = 1'b1 Step 2 : read : reg[0x0620] [7:0] = Number of error bytes received. read : reg[0x0620] [8] (1 indicates PRBS data is coming in and checker is locked)|Generated data will be going to Cu cable side, to disable this transmission : write : reg[0x041F] = 0x1000 Generated data will be going to MAC side, to disable MAC side : write : reg[0x0000]=0x05 40|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 31

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Table 6-2. Data p ath BIST Pro g rammin g ( continued )**

|Col1|Loopback Mode|To enable loopback mode|To enable data generator and checker: MAC packets|To check in- coming MAC packets status|To enable data generator and checker: PRBS stream|To check in- coming PRBS status: PRBS stream|Other care- abouts|
|---|---|---|---|---|---|---|---|
|4|RGMII loopback|write : reg<0x0000> = 0x4140|Data is generated externally at Rgmii TX pins Write : reg[0x0619]= 0x1004|Data can be verified at Rgmii RX pins. Packet errors can additionaly be checked internally by : read : reg[0x063C]= [15:0] of total received packets count. read : reg[0x063D] = [31:16] of total received packets count. read : reg[0x063E]= Packets received with CRC errors|Data is generated externally at Rgmii Tx pins.|Not applicable as data is external. PRBS stream checker works only with internal data generator.|Generated data will be going to Cu cable side, to disable this transmission : write : reg[0x041F] = 0x1000|
|5|SGMII loopback|write : reg[0x0000] = 0x4140|Data is generated externally at Sgmii TX pins Write : reg[0x0619] = 0x1114|Data can be verified at Sgmii RX pins. Packet errors can additionaly be checked internally by : read : reg[0x063C]= [15:0] of total received packets count. read : reg[0x063D] = [31:16] of total received packets count. read : reg[0x063E] = Packets received with CRC errors|Data is generated externally at Sgmii Tx pins.|Not applicable as data is external. PRBS stream checker works only with internal data generator.|Generated data will be going to Cu cable side, to disable this transmission : write : reg[0x041F] = 0x1000|
|6|RGMII Reverse loopback|write : reg[0x0016] = 0x0010|write : reg[0x0624]=0x 55BF write : reg[0x0619]=0x 1555|read : reg[0x063C] = [15:0] of total received packets count. read : reg[0x063D] = [31:16] of total received packets count. read : reg[0x063E] = Packets received with CRC errors|write : reg[0x0624]=0x55 BF write : reg[0x0619]=0x05 57|Step 1 : write : reg[0x0620][1] = 1'b1 Step 2 : read : reg[0x0620] [7:0] = Number of error bytes received. read : reg[0x0620] [8] (1 indicates PRBS data is coming in and checker is locked)|Generated data will be going to Cu cable side, to disable this transmission : write : reg[0x041F] = 0x1000|



32 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Table 6-2. Data p ath BIST Pro g rammin g ( continued )**

|Col1|Loopback Mode|To enable loopback mode|To enable data generator and checker: MAC packets|To check in- coming MAC packets status|To enable data generator and checker: PRBS stream|To check in- coming PRBS status: PRBS stream|Other care- abouts|
|---|---|---|---|---|---|---|---|
|7|SGMII Reverse loopback|write : reg[0x042C] = 0x0010|write : reg[0x0624]=0x 55BF write : reg[0x0619]=0x 1555|read : reg[0x063C] for [15:0] of total received packets count. read : reg[0x063D] for [31:16] of total received packets count. read : reg[0x063E] for Packets received with CRC errors|write : reg[0x0624]=0x55 BF write : reg[0x0619]=0x05 57|Step 1 : write : reg[0x0620][1] = 1'b1 Step 2 : read : reg[0x0620] [7:0] for Number of error bytes received. read : reg[0x0620] [8] (1 indicates PRBS data is coming in and checker is locked)|Generated data will be going to Cu cable side, to disable this transmission : write : reg[0x041F] = 0x1000|

###### **Note** Different MAC packet parameters can be further configured with register[0x061B] and register[0x0624]

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 33

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.3.1.4 Temperature and Voltage Sensing** Temperature sensor of PHY can be used to give the indication of the temperature of the system and reading can be taken on the fly by reading the temperature sensor output register. Voltage sensor senses the voltage of all the supply pins: vdda, vddio and vdd1p0. Each pins active voltage can be sensed by reading the corresponding voltage sensor output register. All sensors are always active and monitor state machine polls the value of each sensor periodically. Monitor state machine can be further programmed to give higher priority/sampling time to one sensor over another by using MONITOR_CTRL_3 register. Following software sequence can be used to read out any sensor's output: • Step1 : Program register[0x0467] = 0x6004 ; Initial configuration of monitors • Step 2 : Program register [0x046A] = 0x00A6 and then register [0x046A]=0x00A3; Refresh the monitors • Step 3 : Program register[0x0468] to select the corresponding sensor to be polled and read register [0x047B] [14:7] for selected sensor's output code. • Step 4 : Feed the values of read sensor's output code (in decimal) in following equations to get the sensor's output value in decimals. Refer to Sensor Select Table for required value of constants to be used in equations : – vdda_value = 3.3 + (vdda_output_code - vdda_output_mean_code)*slope_vdda_sensor – vdd1p0_value = 1.0 + (vdd1p0_output_code - vdd1p0_ouput_mean_code)*slope_vdd1p0_sensor – vddio_calculated = 3.3 + (vddio_ouput_code - vddio_output_mean_code)*slope_vddio_sensor – temperature_calculated = 25 + (temperature_output_code - temperature_output_mean_code)*slope_temperature_sensor **Table 6-3. Sensor Select Table** **Table 6-4. Sensor's Constant Values** **Note** Accuracy of temperature sensor can be maximized (7.5degreeC), if customer can sample "tem p erature_output_code" at 25C and use it as "temperature_output_mean_code".

|Register[0x0468]|Sensor Selected To Read-out|
|---|---|
|0x1920|VDDA Voltage Sensor|
|0x2920|VDD1P0 Voltage Sensor|
|0x3920|VDDIO Voltage Sensor|
|0x4920|Temperature Sensor|


|Constant|Value (in decimal)|
|---|---|
|vdda_output_mean_code|128|
|slope_vdda3p3_sensor|8.63014e-3|
|vdd1p0_output_mean_code|93|
|slope_vdd1p0_sensor|2.85714e-3|
|vddio_output_mean_code|224|
|slope_vddio_sensor|15.686e-3|
|temperature_output_mean_code|161|
|slope_temperature_sensor|1|



34 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.3.1.5 Electrostatic Discharge Sensing** Electrostatic discharge is a serious issue for electronic circuits and if not properly mitigated can create short-term issues (signal integrity, link drops, packet loss) as well as long-term reliability faults. The DP83TG720S-Q1 has robust integrated ESD circuitry and offers an ESD sensing architecture. ESD events can be detected on MDI pins for further analysis and debug. The ESD sensing tool is useful for both prototyping and end-applications. Additionally, the DP83TG720S-Q1 provides an interrupt status flag; when an ESD event is logged in the register<0x0442>. Hardware and software resets are ignored by the ESDS register to prevent unwarranted clearing. **Table 6-5. ESD Sensin g : Interru p t Settin g and Count Readin g**

|Function|Required Read/Write|
|---|---|
|Interrupt Enable|• Write register<0x0012>[3] = 1|
|ESD Event Counter|• Read register<0x0442>[14:9] • Value in decimal indicates the ESD strikes since power-up.|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 35

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** ***6.3.2 Compliance Test Modes*** The six test modes for the DP83TG720S-Q1 are compliant to IEEE 802.3bp, Sub-clause 97.5.2. Supported test modes allow testing of the transmitter waveform Power Spectral Density (PSD) mask, distortion, MDI Master jitter, MDI Slave jitter, droop, transmitter frequency, frequency tolerance, BER monitoring, return loss, and mode conversion. Any of the three GPIOs can be used to output TX_TCLK for MDI Slave jitter measurement. **6.3.2.1 Test Mode 1** Test mode 1 tests the transmitter clock jitter when linked to a partner. In test mode 1, the DP83TG720S-Q1 PHYs are connected over link segment defined in section 97.6 within IEEE 802.3bp. TX_TCLK125 is a divided clock derived from TX_TCLK, which is one sixth the frequency. **6.3.2.2 Test Mode 2** Test mode 2 tests the transmitter MDI Master mode jitter. In test mode 2, the DP83TG720S-Q1 transmits a continuous pattern of three {+1} symbols followed by three {-1} symbols. The transmitted symbols are timed from the 750MHz source, which results in a 125MHz signal. **6.3.2.3 Test Mode 4** Test mode 4 tests the transmitter distortion. In test mode 4, the DP83TG720S-Q1 will transmit the sequence of symbols generated by Equation 1: g(x) = 1 + x [9] + x [11] (1) The bit sequences, x0n and x1n, are generated from combinations of the scrambler in accordance to and : 'x0 n = Scr n [0] (2) x1 n = Scr n [1] ^ Scr n [4] (3) x2 n = Scr n [1] ^ Scr n [5] (4) Example streams of the 3-bit nibbles are shown in Table 6-6. **Table 6-6. Transmitter Test Mode 4 S y mbol Ma pp in g** **6.3.2.4 Test Mode 5** Test mode 5 tests the transmitter PSD mask. In test mode 5, the DP83TG720S-Q1 will transmit normal Inter- Frame IDLE PAM3 symbols. **6.3.2.5 Test Mode 6**

|x2n|x1n|x0n|T1n|T0n|
|---|---|---|---|---|
|0|0|0|-1|-1|
|0|0|1|0|-1|
|0|1|0|-1|0|
|0|1|1|-1|+1|
|1|0|0|+1|0|
|1|0|1|+1|-1|
|1|1|0|+1|+1|
|1|1|1|0|+1| Test mode 6 tests the transmitter droop. In test mode 6, the DP83TG720S-Q1 transmits fifteen {+1} symbols followed by fifteen {-1} symbols with symbol transmission at 750MHz. This 25MHz pattern is repeated continuously until the test mode is disabled.

36 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.3.2.6 Test Mode 7**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### Test mode 7 enabled bit error rate measurement on a link segment. This mode uses zero data pattern on the MDI to check BER by comparing an expected zero data pattern to any non-zero bit received. Error checking is performed after FEC and 80B/81B decoding. **Table 6-7. Test Mode Re g ister Settin g**

|MMD|Register|Value|Test Mode|
|---|---|---|---|
|MMD1|0x0904|0x2000|Test Mode 1 : Tx_Tclk 125MHz is routed to clkout pin.|
|MMD1|0x0904|0x4000|Test Mode 2|
|MMD1|0x0904|0x8000|Test Mode 4 : Tx_Tclk 125MHz is routed to clkout pin.|
|MMD1F|0x0453|0x0019||
|MMD1|0x0904|0xA000|Test Mode 5|
|MMD1|0x0904|0xC000|Test Mode 6|
|MMD1|0x0904|0xE000|Test Mode 7|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 37

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.4 Device Functional Modes**

RESET_N = LOW
and Power-on **Figure 6-11. PHY Operation State Diagram** ***6.4.1 Power Down***

|State Change #3|Col2|
|---|---|
|State Change #3 Normal PHY Enabled State Change #4 Sleep State State Change #1 Change #2 Standby PHY Disabled RESET_N = HIGH and POR = complete Power-on Power-off Reset Power-off From any state PHY Disabled PHY Disabled|Sleep|
|Reset PHY Disabled|| When VDDA3P3 or VDDIO or VDD1P0 is below the POR threshold, the DP83TG720S-Q1 is in a power-down state. All digital IOs will remain in high impedance state and analog blocks are disabled. PMA termination is not present when in power-down. ***6.4.2 Reset*** Reset is activated upon power-up, when RESET_N is pulled LOW (for the minimum reset pulse time) or if hardware reset is initiated by setting bit[15] in the register[0x001F]. • Digital state machine restarts after reset and all the register settings are cleared to the boot-up state. • 25MHz clock on clkout pin will remain active during reset state also. • MDI/PMA will not have termination during reset state. **Note** Straps are re-latched only with pin reset and not by hardware reset through register (register [0x001F] = x8000.

38 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) ***6.4.3 Standby*** The device (MDI Master mode or MDI Slave mode) automatically enters into standby post power-up and reset so long that the device is bootstrapped for managed operation. In standby, all PHY functions are operational except for PCS and PMA blocks. Link establishment is not possible in standby and data cannot be transmitted or received. SMI functions are operational and register configurations are maintained. If the device is configured for autonomous operation through bootstrap setting, the PHY automatically switches to normal operation once powered on and reset complete. ***6.4.4 Normal*** Normal mode can be entered from either autonomous or managed operation. When in autonomous operation, the PHY will automatically try to establish link with a valid Link Partner once powered on. In managed operation, SMI access is required to allow the device to exit standby; commands issued through the SMI allow the device to exit standby and enables both the PCS and PMA blocks. All device features are operational in normal mode. Autonomous operation can be enabled through SMI access by setting bit[6] in register 0x18B. ***6.4.5 Sleep*** Once in sleep mode, all PHY blocks are disabled except for energy detection. All register configurations are lost in sleep mode. No link can be established, data cannot be transmitted or received and SMI access is not available when in sleep mode. To use sleep mode of PHY refer to implementation highlighted in following figure.

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 39

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)**


VDDIO

0 / GPIO_0

MDIO


###### Vsleep source = 3.3V; Always on : Sleep or Functional mode

###### **Figure 6-12. Required Implementation for Sleep Mode** **Note** Phy does not go into sleep mode if supply sources are not disabled as per above figure.

40 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) ***6.4.6 State Transitions*** **6.4.6.1 State Transition #1 - Standby to Normal** Autonomous Operation: The PHY will automatically transition to Normal state upon POR completion. Managed Operation: The PHY will transition to Normal state out of Standby only after writing register <0x018C> = 0x001. **6.4.6.2 State Transition #2 - Normal to Standby** The PHY can be forced back into Standby when in Normal state by writing register <0x018C> = 0x0010. **6.4.6.3 State Transition #3 - Normal to Sleep** Sleep state can be entered either locally (pin/register-write) or by remote link-partner. Local sleep entry for Master mode phy : • Step 1 : Write bit[7] = 'b1 of register[0x018B]. • Step 2 : Write reg0x042F = 0x0007, reg0x041E = 0x0100 • Step 3: Make "wake" pin low and hold it low for sleep mode. Local sleep entry for Slave mode phy : • Step 1 : Write bit[8] = 'b0 of register[0x018B] register. • Step 2 : Write bit[7] = 'b1 of register[0x018B] register. • Step 3 : Write reg0x042F = 0x0007, reg0x041E = 0x0100 • Step 4: Make "wake" pin low and hold it low for sleep mode. Remote sleep entry for Master mode phy : • Master can be put to sleep remotely by slave PHY provided the below instructions when the device is already linked-up with the link partner. • Step 1: Write bit[8] = 'b1 of register [0x018B] register and bit[7] = 'b1 of register[0x018B] register. • Step 2: Make "wake" pin low • Step 3: Phy will go into sleep mode with loss of energy on Line Remote sleep entry for Slave mode phy : • Step 1 : Write bit[7] = 'b1 of register[0x018B] register. • Step 2 : Make "wake" pin low. • Step 3: Phy will go into sleep mode with loss of energy on line (when master will go quite : no data, no send-s).This can be achieved by putting link-partner in managed mode (where device is not allowed to start link-up sequence). **Note** Phy will go into sleep mode only if power supplies are disconnected using INH signal as shown in figure Required Implementation for Sleep Mode . **6.4.6.4 State Transition #4 - Sleep to Normal** Sleep state can be exited either locally (pin/register-write) or by remote link-partner. **Local Sleep Exit** Local sleep exit for Master mode PHY by : • Making "wake" pin high (3.3V). Local sleep exit for Slave mode PHY by : • Making "wake" pin high (3.3V).

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 41

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Remote Sleep Exit** Device can be made to exit the sleep mode by link-partner by either of the following : 1. Remote sleep exit using Send-S symbols from link-partner. 2. Remote sleep exit using Send-T symbols from link-partner Details of these procedures are in the following table :

|Col1|Col2|Table 6-8. Remote Sleep Exit Procedures|Col4|
|---|---|---|---|
|Method|Device Mode|Procedure|Required Link-partner Cabability|
|Using Send-S|Master|Step 1 : Start IEEE defined Send-S pattern from link-partner for atleast 1.25ms. Step 2 : Put link-partner in the normal mode to start the link-up. Note : Link-partner with low VOD can limit the remote wake-up upto a maximum of 5m cable.|Link-partner needs to have a mode to send Send-S pattern on demand in Slave mode also. One possible way is : Step 1 : Put link-partner in master mode for atleast 1.25ms. Step 2 : Put link-partner in normal mode to start the link- up|
||Slave|Step 1 : Start IEEE defined Send-S pattern from link-partner for atleast 1.25ms. Step 2 : Put link-partner in the normal mode to start the link-up. Note : Link-partner with low VOD can limit the remote wake-up upto a maximum of 5m cable. Note : To keep the slave mode DP83TG720 in sleep mode, link- partner can be put in managed mode (where device is not allowed to start link-up sequence).|Any IEEE compliant link- partner works, as master mode link-partner is supposed to send Send-S signals to start the link-up|



42 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Table 6-8. Remote Slee p Exit Procedures ( continued )**

|Method|Device Mode|Procedure|Required Link-partner Cabability|
|---|---|---|---|
|Using Send-T|Master|Step 1 : Enable Send-T pattern on link-partner for atleast 1.25ms. Step 2 : Put link-partner in the normal mode to start the link-up.|Link-partner needs to have a mode to send Send-T pattern on demand. Swing during Send-T mode at pins of link-partner must be greater than 0.92V for remote wake-up over 15m cable. Link-partner with lower VOD can limit the remote wake-up to 5m cable. DP83T720 as link-partner can do the required with following steps : Step 1 : Enable Send-T pattern on DP83TG720 link-partner : write reg[0x0405]=0x7400; reg[0x0509]=0x4007 and reg[0x0576]=0x0500 Step 2 : After 100ms disable send-T pattern on DP83TG720 link-partner : write reg[0x0405]=x5800; reg[0x0509]=0x4005 and reg[0x0576]=0x0000|
||Slave|Step 1 : Enable Send-T pattern on link-partner for atleast 1.25ms. Step 2 : Put link-partner in the normal mode to start the link-up.|Link-partner needs to have a mode to send Send-T pattern on demand. Swing during Send-T mode at pins of link-partner must be greater than 0.92V for remote wake-up over 15m cable. Link-partner with lower VOD can limit the remote wake-up to 5m cable. DP83T720 as link-partner can do the required with following steps : Step 1 : Enable Send-T pattern on DP83TG720 link-partner : write reg[0x0405]=0x7400; reg[0x0509]=0x4007 and reg[0x0576]=0x0500 Step 2 : After 100ms disable send-T pattern on DP83TG720 link-partner : write reg[0x0405]=x5800; reg[0x0509]=0x4005 and reg[0x0576]=0x0000|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 43

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** ***6.4.7 Media Dependent Interface*** **6.4.7.1 MDI Master and MDI Slave Configuration** MDI Master and MDI Slave are configured using either hardware bootstraps or through register access. LED_0 controls the MDI Master and MDI Slave bootstrap configuration. By default, MDI Slave mode is configured because there is an internal pulldown resistor on LED_0 pin. If MDI Master mode configuration through hardware bootstrap is preferred, an external pullup resistor is required. Additionally, bit[14] in the PMA_CTRL2 egister controls the MDI Master and MDI Slave configuration. When this bit is set, MDI Master mode is enabled. **6.4.7.2 Auto-Polarity Detection and Correction** During the link training process, the DP83TG720S-Q1 as MDI receiver is able to detect polarity reversal and automatically correct for the error. Both master and slave detects can do the required correction in the receiver polarity. Auto-Polarity Correction cannot be disabled on DP83TG720S-Q1

44 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) ***6.4.8 MAC Interfaces*** **6.4.8.1 Reduced Gigabit Media Independent Interface** The DP83TG720S-Q1 also supports Reduced Gigabit Media Independent Interface (RGMII) as specified by RGMII version 2.0. RGMII is designed to reduce the number of pins required to connect MAC and PHY. To accomplish this goal, the control signals are multiplexed. Both rising and falling edges of the clock are used to sample the control signal pin on transmit and receive paths. For 1Gbps operation, RX_CLK and TX_CLK operate at 125MHz. The RGMII signals are summarized in Table 6-9: **Table 6-9. RGMII Si g nals**

|Col1|Col2|
|---|---|
|25-MHz Crystal or CMOS-level Oscillator|| **Figure 6-13. RGMII Connections**

|FUNCTION|PINS|
|---|---|
|Data Signals|TX_D[3:0]|
||RX_D[3:0]|
|Control Signals|TX_CTRL|
||RX_CTRL|
|Clock Signals|TX_CLK|
||RX_CLK|


|PHY|TX_CLK TX_CTRL TX_D[3:0] RX_CLK RX_CTRL RX_D[3:0]|MAC|
|---|---|---|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 45

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Table 6-10. RGMII Transmit Encodin g** **Table 6-11. RGMII Receive Encodin g**

|TX_CTRL (POSITIVE EDGE)|TX_CTRL (NEGATIVE EDGE)|TX_D[3:0]|DESCRIPTION|
|---|---|---|---|
|0|0|0000 through 1111|Normal Inter-Frame|
|0|1|0000 through 1111|Reserved|
|1|0|0000 through 1111|Normal Data Transmission|
|1|1|0000 through 1111|Transmit Error Propagation|


|RX_CTRL (POSITIVE EDGE)|RX_CTRL (NEGATIVE EDGE)|RX_D[3:0]|DESCRIPTION|
|---|---|---|---|
|0|0|0000 through 1111|Normal Inter-Frame|
|0|1|0000 through 1101|Reserved|
|0|1|1110|False Carrier Indication|
|0|1|1111|Reserved|
|1|0|0000 through 1111|Normal Data Reception|
|1|1|0000 through 1111|Data Reception with Errors| The DP83TG720S-Q1 supports in-band status indication to help simplify link status detection. Inter-frame signals on RX_D[3:0] pins as specified in Table 6-12. **Table 6-12. RGMII In-Band Status**

|RX_CTRL|RX_D3|RX_D[2:1]|RX_D0|
|---|---|---|---|
|0 Note: In-band status is only valid when RX_CTRL is low|Duplex Status: 0 = Half-Duplex 1 = Full-Duplex|RX_CLK Clock Speed: 00 = 2.5MHz 01 = 25MHz 10 = 125MHz 11 = Reserved|Link Status: 0 = Link not established 1 = Valid link established| RGMII MAC Interface for Gigabit Ethernet has stringent timing requirements to meet system level performance. To meet these timing requirements and to operate with different MACs over RGMII, the following requirements must be taken into consideration when designing PCB. TI recommends to check board level signal integrity by using the DP83TG720 IBIS model. **RGMII-TX Requirements** • RGMII TX signals routed with controlled impedance of 50Ohm +/-15%. • Max routing length limited to 5inches for better signal integrity performance. • Figure 6-14 shows a RGMII interface requirements for TX* signals. MAC RGMII driver output impedance of 50Ohm+/-20%. • Skew for all RGMII TX signals at TP2, in Figure 6-14, less than ±500ps. • Signal Integrity at TP1 and TP2, in Figure 6-14, can be verified with IBIS model simulation, that the following requirements are met: – At TP2, signal meeting rise/fall time of 1ns (20-80%) of signal amplitude. – Rise/fall time is monotonic between VIH/VIL level at TP2.

46 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Figure 6-14. RGMII TX Requirements**

|MAC RGMII TX|Trace characteristics: Zo = 50Ÿ(±15%) TP2 Max. length < 5inch TP1|PHY RGMII TX|
|---|---|---| **RGMII-RX Requirements** • RGMII RX signals routed with controlled impedance of 50Ohm +/-15%. • Max routing length limited to 5inch for better signal integrity performance. • No damping resistors added at TP3/TP4, in Figure 6-15, as that can impact signal integrity of RX signals. • Figure 6-15 shows a RGMII interface requirements for RX* signals. MAC RGMII driver output impedance is 50Ohm+/-20%. • Signal Integrity at TP3 and TP4, in Figure 6-15, can be verified with IBIS model simulation, that the following requirements are met: – At TP4, signal meeting rise/fall time of 1ns (20-80%) of signal amplitude. – Rise/fall time is monotonic between VIH/VIL level at TP4. **Figure 6-15. RGMII RX Requirements** **Note**

|PHY RGMII RX|Trace characteristics: Zo = 50Ÿ(±15%) TP4 Max. length < 5inch TP3|MAC RGMII RX|
|---|---|---| 1. We recommend routing RGMII on buried traces to minimize EMC emissions. 2. Buried traces connected with via placement as close as possible to the PHY and MAC.

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 47

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.4.8.2 Serial Gigabit Media Independent Interface** The Serial Gigabit Media Independent Interface (SGMII) provides a means for data transfer between MAC and PHY with significantly less signal pins (4 pins) compared to RGMII (12 pins). SGMII uses low-voltage differential signaling (LVDS) to reduce emissions and improve signal quality. The DP83TG720S-Q1 SGMII is capable of operating in 4-wire mode. In 4-wire operation, two differential pairs are used to transmit and receive data. Clock and data recovery are performed in the MAC and in the PHY in the case of the RX and TX directions, respectively. SGMII Auto-Negotitation can be disabled by setting bit[0] = 0b0 in the SGMII Configuration Register (SGMIICTL, address 0x608). The SGMII signals are summarized in Table 6-13. **Table 6-13. SGMII Si g nals** **Figure 6-16. SGMII Connections**

|FUNCTION|PINS|
|---|---|
|Data Signals|TX_M, TX_P|
||RX_M, RX_P| SGMII MAC Interface for Gigabit Ethernet has stringent signal integrity requirements to meet system level performance. The following requirements must be into consideration when designing PCB. TI recommends to check board level signal integrity by using the DP83TG720 IBIS model. **SGMII Signals Guidelines** • Sgmii Tx and Rx signals routed on board with controlled differential impedance of 100ohms +/- 5%. • Maximum routing length limited to 5inch for better signal integrity. • Mismatch in routing length of p and n limited to 5mils. • AC-coupling caps on rx lines placed close to rx_p and rx_m pins of PHY. • AC-coupling caps on tx lines placed close to tx_p and tx_m pins of MAC. • Signal integrity checked only at the pins of the receiver (PHY or MAC) using the high speed differential probe.

48 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### • At PHY's TX_M and TX_P following eye mask is met :

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **Figure 6-17. Sgmii PHY Receiver Mask Requirement**

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 49

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** ***6.4.9 Serial Management Interface*** The Serial Management Interface provides access to the DP83TG720S-Q1 internal register space for status information and configuration. The SMI is compatible with IEEE 802.3 clause 22. The implemented register set consists of the registers required by the IEEE 802.3 plus several others to provide additional visibility and controllability of the DP83TG720S-Q1. The SMI includes the management clock (MDC) and the management input and output data pin (MDIO). MDC is sourced by the external management entity, also called Station (STA). MDC is not expected to be continuous, and can be turned off by the external management entity when the bus is idle. MDIO is sourced by the external management entity and by the PHY. The data on the MDIO pin is latched on the rising edge of the MDC. MDIO pin requires a pullup resistor (2.2kΩ), which pulls MDIO high during IDLE and turnaround. Up to 9 DP83TG720S-Q1 PHYs can share a common SMI bus. To distinguish between the PHYs, a 3-bit address is used. During power-up-reset, the DP83TG720S-Q1 latches the PHY_AD configuration pins to determine its address. The management entity must not start an SMI transaction in the first cycle after power-up-reset. To maintain valid operation, the SMI bus must remain inactive at least one MDC cycle after hard reset is deasserted. In normal MDIO transactions, the register address is taken directly from the management-frame reg_addr field, thus allowing direct access to 32 16-bit registers (including those defined in IEEE 802.3 and vendor specific). The data field is used for both reading and writing. The Start code is indicated by a <01> pattern. This pattern makes sure that the MDIO line transitions from the default idle line state. Turnaround is defined as an idle bit time inserted between the Register Address field and the Data field. To avoid contention during a read transaction, no device can actively drive the MDIO signal during the first bit of turnaround. The addressed DP83TG720S-Q1 drives the MDIO with a zero for the second bit of turnaround and follows this with the required data. For write transactions, the station-management entity writes data to the addressed DP83TG720S-Q1, thus eliminating the requirement for MDIO Turnaround. The turnaround time is filled by the management entity by inserting <10>. **6.4.9.1 Direct Register Access** Direct register access can be used for the first 31 registers (0x0h through 0x1Fh). **6.4.9.2 Extended Register Space Access**

|Col1|Table 6-14. SMI Protocol Structure|
|---|---|
|SMI PROTOCOL|<idle> <start> <op code> <device address> <reg address> <turnaround> <data> <idle>|
|Read Operation|<idle><01><10><AAAAA><RRRRR><Z0><XXXX XXXX XXXX XXXX><idle>|
|Write Operation|<idle><01><01><AAAAA><RRRRR><10><XXXX XXXX XXXX XXXX><idle>| The DP83TG720S-Q1 SMI function supports read and write access to the extended register set using registers REGCR (0x000Dh) and ADDAR (0x000Eh) and the MDIO Manageable Device (MMD) indirect method defined in IEEE 802.3ah Draft for Clause 22 for accessing the Clause 45 extended register set. **Note** Registers with addresses above 0x001F require indirect access. For indirect access, a sequence of register writes must be followed. The MMD value defines the Device Address (DEVAD) of the register set. The DEVAD must be configured in the register 0x000D (REGCR) bits [4:0] for indirect access The DP83TG720S-Q1 supports 4 MMD device addresses. The 4 MMD register spaces are: 1. MMD1F (Vendor specific registers): DEVAD [4:0] = ‘11111’ 2. MMD1 (IEEE 802.3az defined registers): DEVAD [4:0] = ‘00001’

50 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### 3. MMD3 (IEEE 802.3az defined registers): DEVAD [4:0] = ‘00011’ 4. MMD3 (IEEE 802.3az defined registers): DEVAD [4:0] = ‘00111’

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **Table 6-15. MMD Re g ister S p ace Division** **Note** For MMD1/3/7, most significant nibble of the register address is used to denote the respective MMD space. This should be ignored during actual register access operation. For example to access register 0x1904 use 0x0904 as the re g ister address and x01 as the MMD.

|MMD Register Space|Register Address Range|
|---|---|
|MMD1F|0x000 - 0x0EFD|
|MMD1|0x1000 - 0x1904|
|MMD3|0x3000 - 0x390D|
|MMD7|0x7000 - 0x7200| The following sections describe how to perform operations on the extended register set using register REGCR and ADDAR. ***6.4.9.2.1 Write Operation (No Post Increment)*** To write a register in the extened register set:

|Instruction|Example: Set reg 0x0170 = 0C50|
|---|---|
|1. Write the value 0x001F (address function field = 00, DEVAD = 31) to register REGCR (0x0D).|Write register 0x0D to value 0x001F|
|2. Write the desired register address to register ADDAR (0x0E).|Write register 0x0E to value 0x0170|
|3. Write the value 0x401F (data, no post increment function field = 01, DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x401F|
|4. Write the content of the desired extended register set register to register ADDAR.|Write register 0x0E to value 0x0C50| Subsequent writes to register ADDAR (step 4) continue to rewrite the register selected by the value in the address register. **Note** Steps ( 1) and (2) can be skipped if the address register was previously configured. ***6.4.9.2.2 Read Operation (No Post Increment)*** To read a register in the extended register set:

|Instruction|Example: Read 0x0170|
|---|---|
|1. Write the value 0x001F (address function field = 00, DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x001F|
|2. Write the desired register address to register ADDAR.|Write register 0x0E to value 0x0170|
|3. Write the value 0x401F (data, no post increment function field = 01, DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x401F|
|4. Read the content of the desired extended register set register to register ADDAR.|Read register 0x0E|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 51

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** Subsequent reads from register ADDAR (step 4) continue reading the register selected by the value in the address register. **Note** Ste p s (1 ) and (2) can be skipped if the address register was previously configured. ***6.4.9.2.3 Write Operation (Post Increment)*** To write a register in the extended register set and automatically increment the address register to the next higher value following the write operation:

|Instruction|Example: Set reg 0x0170 = 0C50 & reg 0x0171 = 0x0011|
|---|---|
|1. Write the value 0x001F (address function field = 00, DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x001F|
|2. Write the register address from register ADDAR.|Write register 0x0E to value 0x0170|
|3. Write the value 0x801F (data, post increment on reads and writes function field = 10, DEVAD = 31) or the value 0xC01F (data, post increment on writes function field = 11. DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x801F|
|4. Write the content of the desired extended register set register to register ADDAR.|Write register 0x0E to value 0x0C50|
|5. Subsequent writes to register ADDAR (step 4) writes the next higher addressed data register selected by the value of the address register; the address register is incremented after each access.|Write register 0x0E to value 0x0011| Step 4 Writes register 0x0170 to 0x0C50 and because post increment is enabled, Step 5 writes register 0x0171 to 0x0011. ***6.4.9.2.4 Read Operation (Post Increment)*** To read a register in the extended register set and automatically increment the address register to the next higher value following the read operation: Step 4 Reads register 0x0170 and because post increment is enabled, Step 5 reads register 0x0171.

|Instruction|Example: Read register 0x0170 & 0x0171|
|---|---|
|1. Write the value 0x001F (address function field = 00, DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x001F|
|2. Write the desired register address to register ADDAR.|Write register 0x0E to value 0x0170|
|3. Write the value 0x801F (data, post increment on reads and writes function field = 10, DEVAD = 31) to register REGCR.|Write register 0x0D to value 0x801F|
|4. Read the content of the desired extended register set register to register ADDAR.|Read register 0x0E|
|5. Subsequent reads to register ADDAR (step 4) reads the next higher addressed data register selected by the value of the address register; the address register is incremented after each access.|Read register 0x0E|



52 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.5 Programming** ***6.5.1 Strap Configuration*** The DP83TG720S-Q1 uses functional pins as strap options to place the device into specific modes of operation. The values of these pins are sampled at power up and hardware reset (through either the RESET_N pin or register access). The strap pins support 2-levels and 3-levels, which are described in greater detail below. Configuration of the device is done through strapping or through serial management interface. **Note** • Strap pins are functional pins after reset is deasserted and must not be connected directly to VCC or GND. • Pull up strap resistors are sufficient to enter different strap modes. • Pull down strap resistor can have application for LED pin straps. Refer to LED Configuration section.

VDDIO

|RH|Rpull-down|
|---|---| **Figure 6-18. Strap Circuit** **Table 6-16. Recommended 3-level Stra p Resistor Ratios** 1. 10% resistor accuracy 2. 1% resistor accuracy **Table 6-17. Recommended 2-level Stra p Resistor** 1. 10% resistor accuracy 2. To gain more margin in customer application for 1.8V VDDIO, either 2.1K+/-10% pull-up can be used or resistor accuracy of 2.49K resistor can be limited to 1%.

|MODE|Recommended RH (kΩ) 1 for VDDIO = 3.3V|Recommended RH (kΩ) 2 for VDDIO = 2.5V|Recommended RH (kΩ) 1 for VDDIO = 1.8V|
|---|---|---|---|
|1|OPEN|OPEN|OPEN|
|2|13|12|4|
|3|4.5|2|0.8|


|MODE|Recommended RH (kΩ) 1 2|
|---|---|
|1|OPEN|
|2|2.49|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 53

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** The following table describes the DP83TG720S-Q1 configuration bootstraps: **Table 6-18. 2-level Bootstra p s**

|PIN NAME|PIN NO.|STRAP MODE|STRAP FUNCTION|DESCRIPTION|
|---|---|---|---|---|
|RX_D0|26|1 (default)|MAC[0] = 0|MAC Interface Selection [0]. Refer to Table 6-19 for full description.|
|||2|MAC[0] = 1||
|RX_D1|25|1 (default)|MAC[1] = 0|MAC Interface Selection [1]. Refer to Table 6-19 for full description.|
|||2|MAC[1] = 1||
|RX_D2|24|1 (default)|MAC[2] = 0|MAC Interface Selection [2]. Refer to Table 6-19 for full description.|
|||2|MAC[2] = 1||
|LED_0|35|1 (default)|MS = 0|MDI Master Slave Select. MS = 0 Slave MS = 1 Master|
|||2|MS = 1||
|LED_1|6|1 (default)|AUTO = 0|Autonomous Disable AUTO = 0 Autonomous AUTO = 1 Managed|
|||2|AUTO = 1||



54 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Table 6-19. MAC Interface Selection Bootstra p s** **Table 6-20. 3-Level Bootstra p : PHY Address**

|MAC[2]|MAC[1]|MAC[0]|DESCRIPTION|
|---|---|---|---|
|0|0|0|SGMII (4-wire)|
|0|0|1|RESERVED|
|0|1|0|RESERVED|
|0|1|1|RESERVED|
|1|0|0|RGMII (Align Mode)|
|1|0|1|RGMII (TX Shift Mode)|
|1|1|0|RGMII (TX and RX Shift Mode)|
|1|1|1|RGMII (RX Shift Mode)|

|PHY_AD[3:0]|RX_CTRL STRAP MODE|STRP_1 STRAP MODE|DESCRIPTION|
|---|---|---|---|
|0000|1|1|PHY Address: 0x0000 (0)|
|0001|-|-|RESERVED|
|0010|-|-|RESERVED|
|0011|-|-|RESERVED|
|0100|2|1|PHY Address: 0x0004 (4)|
|0101|3|1|PHY Address: 0x0005 (5)|
|0110|-|-|RESERVED|
|0111|-|-|RESERVED|
|1000|1|2|PHY Address: 0x0008 (8)|
|1001|-|-|RESERVED|
|1010|1|3|PHY Address: 0x000A (10)|
|1011|-|-|RESERVED|
|1100|2|2|PHY Address: 0x000C (12)|
|1101|3|2|PHY Address: 0x000D (13)|
|1110|2|3|PHY Address: 0x000E (14)|
|1111|3|3|PHY Address: 0x000F (15)|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 55

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** ***6.5.2 LED Configuration*** The DP83TG720S-Q1 supports up to three configurable Light Emitting Diode (LED) pins: LED_0, LED_1, and LED_2 (CLKOUT). Several functions can be multiplexed onto the LEDs for different modes of operation. LED operations are selected using registers 0x0450 and 0x0451. **Note** CLKOUT has 25MHz clock output as default. If required, it can be configured to LED2 using register 0x0453. Because the LED output pins are also used as strap pins, external components required for strapping and the user must consider the LED usage to avoid contention. Specifically, when the LED outputs are used to drive LEDs directly, the active state of each output driver is dependent on the logic level sampled by the corresponding input upon power up or hardware reset. Figure 6-19 shows the two proper ways of connecting LEDs directly to the DP83TG720S-Q1.

Pull-Down

VDDIO


D1


R CL

###### **Figure 6-19. Example Strap Connections** ***6.5.3 PHY Address Configuration*** The DP83TG720S-Q1 can be set to respond to any of 9 possible PHY addresses through bootstrap pins. The PHY address is latched into the device upon power-up or hardware reset. Each DP83TG720S-Q1 or port sharing PHY on the serial management bus in the system must have a unique PHY address. The DP83TG720S- Q1 supports PHY address as described in Table 6-20. By default, the DP83TG720S-Q1 will latch to a PHY address of 0 ([0000]). This address can be changed by adding pullup resistors to bootstrap pins found in Table 6-18.

56 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6 Register Maps** ***6.6.1 Register Access Summary*** There are two different methods for accessing registers within the field. Direct register access method is only allowed for the first 31 registers (0x0h through 0x1Fh) of MMD1F register space. Registers beyond 0x1Fh must be accessed by use of the Indirect Method (Extended Register Space) described in Section 6.4.9.2 . **Table 6-21. MMD Re g ister S p ace Division** **Table 6-22. Re g ister Access Summar y**

|MMD REGISTER SPACE|REGISTER ADDRESS RANGE|
|---|---|
|MMD1F|0x000 - 0x0EFD|
|MMD1|0x1000 - 0x1904|
|MMD3|0x3000 - 0x390D|
|MMD7|0x7000 - 0x7200|


|REGISTER FIELD|REGISTER ACCESS METHODS|
|---|---|
|0x0h through 0x1Fh|Direct Access|
||Indirect Access, MMD1F = '11111' Example: to read register 0x17h in MMD1F field with no post increment Step 1) write 0x1Fh to register 0xDh Step 2) write 0x17h to register 0xEh Step 3) write 0x401Fh to register 0xDh Step 4) read register 0xEh|
|MMD1F Field 0x20h - 0xFFFh|Indirect Access, MMD1F = '11111' Example: to read register 0x462h in MMD1F field with no post increment Step 1) write 0x1Fh to register 0xDh Step 2) write 0x462h to register 0xEh Step 3) write 0x401Fh to register 0xDh Step 4) read register 0xEh|
|MMD1 Field 0x0000h - 0x0FFFh|Indirect Access, MMD1 = '00001' Example: to read register 0x7h in MMD1 field with no post increment Step 1) write 0x1h to register 0xDh Step 2) write 0x7h to register 0xEh Step 3) write 0x4001h to register 0xDh Step 4) read register 0xEh|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 57

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** ***6.6.2 DP83TG720 Registers*** Table 6-23 lists the memory-mapped registers for the DP83TG720 registers. All register offset addresses not listed in Table 6-23 should be considered as reserved locations and the register contents should not be modified. **Table 6-23. DP83TG720 Re g isters**

**Offset** **Acronym** **Register Name** **Section**

0h BMCR Section 6.6.2.1

1h BMSR Section 6.6.2.2

2h PHYID1 Section 6.6.2.3

3h PHYID2 Section 6.6.2.4

Dh REGCR Section 6.6.2.5

Eh ADDAR Section 6.6.2.6

10h MII_REG_10 Section 6.6.2.7

11h MII_REG_11 Section 6.6.2.8

12h MII_REG_12 Section 6.6.2.9

13h MII_REG_13 Section 6.6.2.10

16h MII_REG_16 Section 6.6.2.11

18h MII_REG_18 Section 6.6.2.12

19h MII_REG_19 Section 6.6.2.13

1Eh MII_REG_1E Section 6.6.2.14

1Fh MII_REG_1F Section 6.6.2.15

180h LSR Section 6.6.2.16

18Bh LPS_CFG2 Section 6.6.2.17

18Ch LPS_CFG3 Section 6.6.2.18

18Eh LPS_STATUS Section 6.6.2.19

30Fh TDR_TC12 Section 6.6.2.20

405h A2D_REG_05 Section 6.6.2.21

41Eh A2D_REG_30 Section 6.6.2.22

428h A2D_REG_40 Section 6.6.2.23

429h A2D_REG_41 Section 6.6.2.24

42Ch A2D_REG_44 Section 6.6.2.25

42Fh A2D_REG_47 Section 6.6.2.26

430h A2D_REG_48 Section 6.6.2.27

442h A2D_REG_66 Section 6.6.2.28

450h LEDS_CFG_1 Section 6.6.2.29

451h LEDS_CFG_2 Section 6.6.2.30

452h IO_MUX_CFG_1 Section 6.6.2.31

453h IO_MUX_CFG_2 Section 6.6.2.32

456h IO_CONTROL_3 Section 6.6.2.33

45Dh SOR_VECTOR_1 Section 6.6.2.34

45Eh SOR_VECTOR_2 Section 6.6.2.35

468h MONITOR_CTRL2 Section 6.6.2.36

46Ah MONITOR_CTRL4 Section 6.6.2.37

47Bh MONITOR_STAT1 Section 6.6.2.38

510h RS_DECODER Section 6.6.2.39

52Bh TRAINING_RX_STATUS_7 Section 6.6.2.40

543h LINK_QUAL_1 Section 6.6.2.41

544h LINK_QUAL_2 Section 6.6.2.42

58 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Table 6-23. DP83TG720 Re g isters ( continued )**

**Offset** **Acronym** **Register Name** **Section**

545h LINK_DOWN_LATCH_STAT Section 6.6.2.43

547h LINK_QUAL_3 Section 6.6.2.44

548h LINK_QUAL_4 Section 6.6.2.45

552h RS_DECODER_FRAME_STAT_2 Section 6.6.2.46

553h RS_DECODER_FRAME_STAT_3 Section 6.6.2.47

600h RGMII_CTRL Section 6.6.2.48

601h RGMII_FIFO_STATUS Section 6.6.2.49

602h RGMII_DELAY_CTRL Section 6.6.2.50

608h SGMII_CTRL_1 Section 6.6.2.51

60Ah SGMII_STATUS Section 6.6.2.52

60Ch SGMII_CTRL_2 Section 6.6.2.53

60Dh SGMII_FIFO_STATUS Section 6.6.2.54

618h PRBS_STATUS_1 Section 6.6.2.55

619h PRBS_CTRL_1 Section 6.6.2.56

61Ah PRBS_CTRL_2 Section 6.6.2.57

61Bh PRBS_CTRL_3 Section 6.6.2.58

61Ch PRBS_STATUS_2 Section 6.6.2.59

61Dh PRBS_STATUS_3 Section 6.6.2.60

61Eh PRBS_STATUS_4 Section 6.6.2.61

620h PRBS_STATUS_6 Section 6.6.2.62

622h PRBS_STATUS_8 Section 6.6.2.63

623h PRBS_STATUS_9 Section 6.6.2.64

624h PRBS_CTRL_4 Section 6.6.2.65

625h PRBS_CTRL_5 Section 6.6.2.66

626h PRBS_CTRL_6 Section 6.6.2.67

627h PRBS_CTRL_7 Section 6.6.2.68

628h PRBS_CTRL_8 Section 6.6.2.69

629h PRBS_CTRL_9 Section 6.6.2.70

62Ah PRBS_CTRL_10 Section 6.6.2.71

638h CRC_STATUS Section 6.6.2.72

639h PKT_STAT_1 Section 6.6.2.73

63Ah PKT_STAT_2 Section 6.6.2.74

63Bh PKT_STAT_3 Section 6.6.2.75

63Ch PKT_STAT_4 Section 6.6.2.76

63Dh PKT_STAT_5 Section 6.6.2.77

63Eh PKT_STAT_6 Section 6.6.2.78

871h SQI_REG_1 Section 6.6.2.79

874h DSP_REG_74 Section 6.6.2.80

875h DSP_REG_75 Section 6.6.2.81

1000h PMA_PMD_CONTROL_1 Section 6.6.2.82

1007h PMA_PMD_CONTROL_2 Section 6.6.2.83

1009h PMA_PMD_TRANSMIT_DISABL Section 6.6.2.84
E

100Bh PMA_PMD_EXTENDED_ABILIT Section 6.6.2.85
Y2

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 59

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Table 6-23. DP83TG720 Re g isters ( continued )**

**Offset** **Acronym** **Register Name** **Section**

1012h PMA_PMD_EXTENDED_ABILIT Section 6.6.2.86
Y

1834h PMA_PMD_CONTROL Section 6.6.2.87

1900h PMA_CONTROL Section 6.6.2.88

1901h PMA_STATUS Section 6.6.2.89

1902h TRAINING Section 6.6.2.90

1903h LP_TRAINING Section 6.6.2.91

1904h TEST_MODE_CONTROL Section 6.6.2.92

3900h PCS_CONTROL Section 6.6.2.93

3901h PCS_STATUS Section 6.6.2.94

3902h PCS_STATUS_2 Section 6.6.2.95

3904h OAM_TRANSMIT Section 6.6.2.96

3905h OAM_TX_MESSAGE_1 Section 6.6.2.97

3906h OAM_TX_MESSAGE_2 Section 6.6.2.98

3907h OAM_TX_MESSAGE_3 Section 6.6.2.99

3908h OAM_TX_MESSAGE_4 Section 6.6.2.100

3909h OAM_RECEIVE Section 6.6.2.101

390Ah OAM_RX_MESSAGE_1 Section 6.6.2.102

390Bh OAM_RX_MESSAGE_2 Section 6.6.2.103

390Ch OAM_RX_MESSAGE_3 Section 6.6.2.104

390Dh OAM_RX_MESSAGE_4 Section 6.6.2.105

7200h AN_CFG Section 6.6.2.106 Complex bit access types are encoded to fit into small table cells. Table 6-24 shows the codes that are used for access types in this section. **Table 6-24. DP83TG720 Access T yp e Codes**

|Access Type|Code|Description|
|---|---|---|
|Read Type|||
|R|R|Read|
|Write Type|||
|W|W|Write|
|W0C|W 0C|Write 0 to clear|
|W0S|W 0S|Write 0 to set|
|WMC|W|Write|
|WMC,0|W|Write|
|WMC,1|W|Write|
|WSC|W|Write|
|WSC,0|W|Write|
|Reset or Default Value|||
|-n||Value after reset or the default value|



60 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.1 BMCR Register (Offset = 0h) [Reset = 0140h] ** BMCR is shown in Figure 6-20 and described in Table 6-25. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-20. BMCR Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|mii_reset|loopback|RESERVED|RESERVED|power_down|isolate|RESERVED|RESERVED|
|R/WMC-0h R/W-0h R-0h R-0h R/W-0h R/W-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|speed_sel_msb|RESERVED|RESERVED|||||
|R-0h R-1h R-0h R-0h||||||||

###### **Table 6-25. BMCR Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|mii_reset|R/WMC|0h|1b = Digital in reset and all MII regs (0x0 - 0xF) reset to default 0b = No reset|
|14|loopback|R/W|0h|1b = MII loopback 0b = No MII loopback|
|13|RESERVED|R|0h|Reserved|
|12|RESERVED|R|0h|Reserved|
|11|power_down|R/W|0h|1b = Power down via register or pin 0b = Normal mode|
|10|isolate|R/W|0h|1b = MAC isolate mode (No output to MAC from the PHY) 0b = Normal Mode|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|speed_sel_msb|R|1h|0b= Reserved 1b= 1000 Mb/s|
|5|RESERVED|R|0h|Reserved|
|4-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 61

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.2 BMSR Register (Offset = 1h) [Reset = 0141h] ** BMSR is shown in Figure 6-21 and described in Table 6-26. Return to the Summary Table. **Table 6-26. BMSR Re g ister Field Descri p tions**

|Figure 6-21. BMSR Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|extended_statu s|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h R-1h||||||||
|7 6 5 4 3 2 1 0||||||||
|unidirectional_a bility|preamble_supre ssion|aneg_complete|remote_fault|aneg_ability|link_status|jabber_detect|extended_capa bility|
|R-0h R-1h R-0h R/W0C-0h R-0h R/W0S-0h R/W0C-0h R-1h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|RESERVED|R|0h|Reserved|
|13|RESERVED|R|0h|Reserved|
|12|RESERVED|R|0h|Reserved|
|11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|extended_status|R|1h|1b = Extended status information in Register 15 0b = No extended status information in Register 15|
|7|unidirectional_ability|R|0h|Reserved|
|6|preamble_supression|R|1h|1b = PHY accepts management frames with preamble suppressed. 0b = PHY does not accept management frames with preamble suppressed|
|5|aneg_complete|R|0h|Reserved|
|4|remote_fault|R/W0C|0h|Reserved|
|3|aneg_ability|R|0h|Reserved|
|2|link_status|R/W0S|0h|1b = link is up 0b = link down|
|1|jabber_detect|R/W0C|0h|Reserved|
|0|extended_capability|R|1h|1b = extended register capabilities 0b = basic register set capabilities only|



62 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.3 PHYID1 Register (Offset = 2h) [Reset = 2000h] ** PHYID1 is shown in Figure 6-22 and described in Table 6-27. Return to the Summary Table. **Fi g ure 6-22. PHYID1 Re g ister**

15 14 13 12 11 10 9 8

oui_21_16

R-2000h


7 6 5 4 3 2 1 0


oui_21_16

R-2000h
###### **Table 6-27. PHYID1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|oui_21_16|R|2000h|Unique identifier for the part|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 63

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.4 PHYID2 Register (Offset = 3h) [Reset = A284h] ** PHYID2 is shown in Figure 6-23 and described in Table 6-28. Return to the Summary Table. **Table 6-28. PHYID2 Re g ister Field Descri p tions**

|Figure 6-23. PHYID2 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|oui_5_0||model_number|
|R-28h R-28h|||
|7 6 5 4 3 2 1 0|||
|model_number|rev_number||
|R-28h R-4h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-10|oui_5_0|R|28h|Unique identifier for the part|
|9-4|model_number|R|28h|Unique identifier for the part|
|3-0|rev_number|R|4h|Unique identifier for the part|



64 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.5 REGCR Register (Offset = Dh) [Reset = 0000h] ** REGCR is shown in Figure 6-24 and described in Table 6-29. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-24. REGCR Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|Extended Register Command|RESERVED||
|R/W-0h R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED||DEVAD|
|R-0h R/W-0h|||

###### **Table 6-29. REGCR Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-14|Extended Register Command|R/W|0h|00b = Address 01b = Data, no post increment 10b = Data, post increment on read and write 11b = Data, post increment on write only|
|13-5|RESERVED|R|0h|Reserved|
|4-0|DEVAD|R/W|0h|MMD field for indirect register access|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 65

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.6 ADDAR Register (Offset = Eh) [Reset = 0000h] ** ADDAR is shown in Figure 6-25 and described in Table 6-30. Return to the Summary Table. **Fi g ure 6-25. ADDAR Re g ister**

15 14 13 12 11 10 9 8

Address/Data

R/W-0h


7 6 5 4 3 2 1 0


Address/Data

R/W-0h
###### **Table 6-30. ADDAR Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|Address/Data|R/W|0h|Address Data field for indirect register access|



66 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.7 MII_REG_10 Register (Offset = 10h) [Reset = 0004h] ** MII_REG_10 is shown in Figure 6-26 and described in Table 6-31. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-26. MII_REG_10 Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED|||RESERVED|descr_lock_bit|RESERVED|
|R-0h R-0h R/W0S-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|mii_int_bit|RESERVED|mii_loopback|duplex_mode_e nv|RESERVED|link_status_bit|
|R-0h R-0h R-0h R-1h R-0h R-0h||||||

###### **Table 6-31. MII _ REG _ 10 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|descr_lock_bit|R/W0S|0h|1b = Descrambler is locked 0b = Descrmabler is unlocked atleast once|
|8|RESERVED|R|0h|Reserved|
|7|mii_int_bit|R|0h|1b = Interrupt pin had been set 0b = Interrupts pin not set Cleared on Read|
|6-4|RESERVED|R|0h|Reserved|
|3|mii_loopback|R|0h|1b = MII loopback 0b = No MII loopback|
|2|duplex_mode_env|R|1h|1b = Full duplex 0b = Half duplex|
|1|RESERVED|R|0h|Reserved|
|0|link_status_bit|R|0h|1b = link is up 0b = link had been down|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 67

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.8 MII_REG_11 Register (Offset = 11h) [Reset = 000Bh] ** MII_REG_11 is shown in Figure 6-27 and described in Table 6-32. Return to the Summary Table. **Table 6-32. MII _ REG _ 11 Re g ister Field Descri p tions**

|Figure 6-27. MII_REG_11 Register|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||||
|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h|||||||
|7 6 5 4 3 2 1 0|||||||
|RESERVED|RESERVED|RESERVED|int_polarity|force_interrupt|int_en|RESERVED|
|R-0h R-0h R-0h R/W-1h R/W-0h R/W-1h R-0h|||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|RESERVED|R|0h|Reserved|
|13-12|RESERVED|R|0h|Reserved|
|11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5-4|RESERVED|R|0h|Reserved|
|3|int_polarity|R/W|1h|1b = Active low 0b = Active high|
|2|force_interrupt|R/W|0h|1b = Force interrupt pin 0b = Do not force interrupt pin|
|1|int_en|R/W|1h|1b = Enable interrupts 0b = Disable interrupts|
|0|RESERVED|R|0h|Reserved|



68 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.9 MII_REG_12 Register (Offset = 12h) [Reset = 0000h] ** MII_REG_12 is shown in Figure 6-28 and described in Table 6-33. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-28. MII_REG_12 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED|energy_det_int|link_int|RESERVED|esd_int|ms_train_done_ int|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|energy_det_int_ en|link_int_en|RESERVED|esd_int_en|ms_train_done_ int_en|RESERVED|RESERVED|
|R-0h R/W-0h R/W-0h R-0h R/W-0h R/W-0h R-0h R-0h||||||||

###### **Table 6-33. MII _ REG _ 12 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|energy_det_int|R|0h|Energy det change interrupt status|
|13|link_int|R|0h|Link status change interrupt status|
|12|RESERVED|R|0h|Reserved|
|11|esd_int|R|0h|ESD fault detected interrupt status|
|10|ms_train_done_int|R|0h|Training done interrupt status|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|energy_det_int_en|R/W|0h|Energy det change interrupt enable|
|5|link_int_en|R/W|0h|Link status change interrupt enable|
|4|RESERVED|R|0h|Reserved|
|3|esd_int_en|R/W|0h|ESD fault detected interrupt enable|
|2|ms_train_done_int_en|R/W|0h|Training done interrupt enable|
|1|RESERVED|R|0h|Reserved|
|0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 69

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.10 MII_REG_13 Register (Offset = 13h) [Reset = 0000h] ** MII_REG_13 is shown in Figure 6-29 and described in Table 6-34. Return to the Summary Table. **Table 6-34. MII _ REG _ 13 Re g ister Field Descri p tions**

|Figure 6-29. MII_REG_13 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|under_volt_int|over_volt_int|RESERVED|RESERVED|over_temp_int|RESERVED|pol_change_int|RESERVED|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|under_volt_int_ en|over_volt_int_e n|RESERVED|RESERVED|over_temp_int_ en|RESERVED|pol_change_int _en|RESERVED|
|R/W-0h R/W-0h R-0h R-0h R/W-0h R-0h R/W-0h R-0h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|under_volt_int|R|0h|Under volt interrupt status|
|14|over_volt_int|R|0h|Over volt interrupt status|
|13|RESERVED|R|0h|Reserved|
|12|RESERVED|R|0h|Reserved|
|11|over_temp_int|R|0h|Over temp interrupt status|
|10|RESERVED|R|0h|Reserved|
|9|pol_change_int|R|0h|Data polarity change interrupt status|
|8|RESERVED|R|0h|Reserved|
|7|under_volt_int_en|R/W|0h|Under volt interrupt enable|
|6|over_volt_int_en|R/W|0h|Over volt interrupt enable|
|5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3|over_temp_int_en|R/W|0h|Over temp interrupt enable|
|2|RESERVED|R|0h|Reserved|
|1|pol_change_int_en|R/W|0h|Data Polarity change interrupt enable|
|0|RESERVED|R|0h|Reserved|



70 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.11 MII_REG_16 Register (Offset = 16h) [Reset = 0000h] ** MII_REG_16 is shown in Figure 6-30 and described in Table 6-35. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-30. MII_REG_16 Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED||RESERVED|RESERVED|core_pwr_mode|
|R-0h R-0h R-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|loopback_mode||||
|R-0h R/W-0h|||||

###### **Table 6-35. MII _ REG _ 16 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|core_pwr_mode|R|0h|1b = Core is is normal power mode 0b = Core is in power down or sleep mode|
|7|RESERVED|R|0h|Reserved|
|6-0|loopback_mode|R/W|0h|000001b = PCS loop 000010b = RS loop 000100b = Digital loop 001000B = Analog loop 010000b = Reverse loop|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 71

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.12 MII_REG_18 Register (Offset = 18h) [Reset = 0008h] ** MII_REG_18 is shown in Figure 6-31 and described in Table 6-36. Return to the Summary Table. **Table 6-36. MII _ REG _ 18 Re g ister Field Descri p tions**

|Figure 6-31. MII_REG_18 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|ack_received_in t|tx_valid_clr_int|RESERVED|RESERVED|por_done_int|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|ack_received_in t_en|tx_valid_clr_int_ en|RESERVED|RESERVED|por_done_int_e n|RESERVED|RESERVED|RESERVED|
|R/W-0h R/W-0h R-0h R-0h R/W-1h R-0h R-0h R-0h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|ack_received_int|R|0h|Ack received interrupt status (OAM)|
|14|tx_valid_clr_int|R|0h|mr_tx_valid clear interrupt status (OAM)|
|13|RESERVED|R|0h|Reserved|
|12|RESERVED|R|0h|Reserved|
|11|por_done_int|R|0h|POR done interrupt status|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|ack_received_int_en|R/W|0h|Ack received interrupt enable (OAM)|
|6|tx_valid_clr_int_en|R/W|0h|mr_tx_valid clear interrupt enable (OAM)|
|5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3|por_done_int_en|R/W|1h|POR done interrupt enable|
|2|RESERVED|R|0h|Reserved|
|1|RESERVED|R|0h|Reserved|
|0|RESERVED|R|0h|Reserved|



72 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.13 MII_REG_19 Register (Offset = 19h) [Reset = 00XXh] ** MII_REG_19 is shown in Figure 6-32 and described in Table 6-37. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-32. MII_REG_19 Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|RESERVED||RESERVED|RESERVED|
|R-0h R-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|RESERVED|SOR_PHYADDR|||
|R-0h R-Xh||||

###### **Table 6-37. MII _ REG _ 19 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9-5|RESERVED|R|0h|Reserved|
|4-0|SOR_PHYADDR|R|X|PHY ADDRESS latched from strap|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 73

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.14 MII_REG_1E Register (Offset = 1Eh) [Reset = 0000h] ** MII_REG_1E is shown in Figure 6-33 and described in Table 6-38. Return to the Summary Table. **Table 6-38. MII _ REG _ 1E Re g ister Field Descri p tions**

|Figure 6-33. MII_REG_1E Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|tdr_start|cfg_tdr_auto_ru n|RESERVED|||
|R/WMC-0h R/W-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|||tdr_done|tdr_fail|
|R-0h R-0h R-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|tdr_start|R/WMC|0h|1b = TDR start Bit is cleared after TDR run is complete|
|14|cfg_tdr_auto_run|R/W|0h|1b = TDR start automatically on link down 0b = TDR start manually using 0x1E[15]|
|13-2|RESERVED|R|0h|Reserved|
|1|tdr_done|R|0h|TDR done status 1b = TDR done 0b = TDR on-going or not initiated|
|0|tdr_fail|R|0h|When tdr_done status is 1, this bit inidicates if TDR ran successfully 1b = TDR run failed 0b = TDR ran successfully|



74 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.15 MII_REG_1F Register (Offset = 1Fh) [Reset = 0000h] ** MII_REG_1F is shown in Figure 6-34 and described in Table 6-39. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-34. MII_REG_1F Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|sw_global_reset|digital_reset|RESERVED|RESERVED|
|R/WMC-0h R/WMC-0h R-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|RESERVED|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h||||

###### **Table 6-39. MII _ REG _ 1F Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|sw_global_reset|R/WMC|0h|Hardware reset - Reset digital + register file This bit is self clearing|
|14|digital_reset|R/WMC|0h|Soft reset - Reset only digital core This bit is self clearing|
|13|RESERVED|R|0h|Reserved|
|12-8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5|RESERVED|R|0h|Reserved|
|4-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 75

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.16 LSR Register (Offset = 180h) [Reset = 0000h] ** LSR is shown in Figure 6-35 and described in Table 6-40. Return to the Summary Table. **Table 6-40. LSR Re g ister Field Descri p tions**

|Figure 6-35. LSR Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|link_up|link_down|phy_ctrl_send_ data|link_status|RESERVED||||
|R-0h R-0h R-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|RESERVED|RESERVED|RESERVED|channel_ok|descr_sync|loc_rcvr_status|rem_rcvr_status|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h R-0h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|link_up|R|0h|Link up as defined by CnS|
|14|link_down|R|0h|Link down as defined by CnS|
|13|phy_ctrl_send_data|R|0h|Phy control in send data status|
|12|link_status|R|0h|IEEE defined Live Link status|
|11-8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3|channel_ok|R|0h|channel okay status|
|2|descr_sync|R|0h|Descrambler lock status|
|1|loc_rcvr_status|R|0h|Local receiver status|
|0|rem_rcvr_status|R|0h|Remote receiver status|



76 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.17 LPS_CFG2 Register (Offset = 18Bh) [Reset = 0000h] ** LPS_CFG2 is shown in Figure 6-36 and described in Table 6-41. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-36. LPS_CFG2 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED|||||||ed_en|
|R-0h R/W-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|sleep_en|cfg_auto_mode _en_strap|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|
|R/W-0h R/WMC,1-0h R-0h R-0h R-0h R-0h R-0h R-0h||||||||

###### **Table 6-41. LPS _ CFG2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-9|RESERVED|R|0h|Reserved|
|8|ed_en|R/W|0h|1b = Enable energy detection on MDI 0b = Disable energy detection on MDI|
|7|sleep_en|R/W|0h|1b = Allow PHY to enter sleep 0b = Do not allow PHY to enter sleep|
|6|cfg_auto_mode_en_strap|R/WMC,1|0h|LPS autonomous mode enable 1b = PHY enters normal mode on power up 0b = PHY enters standby mode on power up|
|5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3|RESERVED|R|0h|Reserved|
|2|RESERVED|R|0h|Reserved|
|1|RESERVED|R|0h|Reserved|
|0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 77

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.18 LPS_CFG3 Register (Offset = 18Ch) [Reset = 0000h] ** LPS_CFG3 is shown in Figure 6-37 and described in Table 6-42. Return to the Summary Table. **Table 6-42. LPS _ CFG3 Re g ister Field Descri p tions**

|Figure 6-37. LPS_CFG3 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED||||||||
|R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|RESERVED|RESERVED|cfg_lps_pwr_m ode_4|RESERVED|RESERVED|RESERVED|cfg_lps_pwr_m ode_0|
|R-0h R-0h R-0h R/WMC,0-0h R-0h R-0h R-0h R/WMC,0-0h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5|RESERVED|R|0h|Reserved|
|4|cfg_lps_pwr_mode_4|R/WMC,0|0h|Set to enter standby mode|
|3|RESERVED|R|0h|Reserved|
|2|RESERVED|R|0h|Reserved|
|1|RESERVED|R|0h|Reserved|
|0|cfg_lps_pwr_mode_0|R/WMC,0|0h|Set to enter normal mode|



78 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.19 LPS_STATUS Register (Offset = 18Eh) [Reset = 0000h] ** LPS_STATUS is shown in Figure 6-38 and described in Table 6-43. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-38. LPS_STATUS Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|RESERVED||
|R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED|status_lps_st|
|R-0h R-0h||

###### **Table 6-43. LPS _ STATUS Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-7|RESERVED|R|0h|Reserved|
|6-0|status_lps_st|R|0h|Observe LPS state : 0x2 = Standby mode 0x4 = Normal mode|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 79

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.20 TDR_TC12 Register (Offset = 30Fh) [Reset = 0000h] ** TDR_TC12 is shown in Figure 6-39 and described in Table 6-44. Return to the Summary Table. **Table 6-44. TDR _ TC12 Re g ister Field Descri p tions**

|Figure 6-39. TDR_TC12 Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|RESERVED|fault_loc|||
|R-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|tdr_state||RESERVED|tdr_activation|
|R-0h R-0h R-0h||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-14|RESERVED|R|0h|Reserved|
|13-8|fault_loc|R|0h|See TC12|
|7-4|tdr_state|R|0h|See TC12|
|3-2|RESERVED|R|0h|Reserved|
|1-0|tdr_activation|R|0h|See TC12|



80 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.21 A2D_REG_05 Register (Offset = 405h) [Reset = 6400h] ** A2D_REG_05 is shown in Figure 6-40 and described in Table 6-45. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-40. A2D_REG_05 Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|ld_bias_1p0v_sl|RESERVED|
|R/W-19h R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED||
|R-0h||

###### **Table 6-45. A2D _ REG _ 05 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-10|ld_bias_1p0v_sl|R/W|19h|Bits to control the DAC current of LD and hence the swing. 001010b = 400mV 001011b = 440mV 001100b = 480mV 001101b = 520mV 001110b = 560mV 001111b = 600mV 010000b = 640mV 010001b = 680mV 010010b = 720mV 010011b = 760mV 010100b = 800mV 010101b = 840mV 010110b = 880mV 010111b = 920mV 011000b = 960mV 011001b = 1000mV 011010b = 1040mV 011011b = 1080mV 011100b = 1120mV 011101b = 1160mV 011110b = 1200mV|
|9-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 81

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.22 A2D_REG_30 Register (Offset = 41Eh) [Reset = 0000h] ** A2D_REG_30 is shown in Figure 6-41 and described in Table 6-46. Return to the Summary Table. **Table 6-46. A2D _ REG _ 30 Re g ister Field Descri p tions**

|Figure 6-41. A2D_REG_30 Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED|||||spare_in_2_fro mdig_sl_force_ en|
|R-0h R/W-0h||||||
|7 6 5 4 3 2 1 0||||||
|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED||
|R-0h R-0h R-0h R-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-9|RESERVED|R|0h|Reserved|
|8|spare_in_2_fromdig_sl_for ce_en|R/W|0h|Force control enable for Reg0x042F|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3-0|RESERVED|R|0h|Reserved|



82 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.23 A2D_REG_40 Register (Offset = 428h) [Reset = 6002h] ** A2D_REG_40 is shown in Figure 6-42 and described in Table 6-47. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-42. A2D_REG_40 Register|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||||
|RESERVED|SGMII_TESTMODE|RESERVED|SGMII_SOP_S ON_SLEW_CT RL|RESERVED|RESERVED||
|R-0h R/W-3h R-0h R/W-0h R-0h R-0h|||||||
|7 6 5 4 3 2 1 0|||||||
|RESERVED|RESERVED|||||RESERVED|
|R-0h R-0h R-0h|||||||

###### **Table 6-47. A2D _ REG _ 40 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14-13|SGMII_TESTMODE|R/W|3h|00b = 1000mV Sgmii output swing 01b = 1260mV Sgmii output swing 10b = 900mV Sgmii output swing 11b = 720mV Sgmii output swing|
|12|RESERVED|R|0h|Reserved|
|11|SGMII_SOP_SON_SLEW _CTRL|R/W|0h|0b =Default output rise/fall time 1b = Slow output rise/fall time|
|10|RESERVED|R|0h|Reserved|
|9-8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6-1|RESERVED|R|0h|Reserved|
|0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 83

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.24 A2D_REG_41 Register (Offset = 429h) [Reset = 0030h] ** A2D_REG_41 is shown in Figure 6-43 and described in Table 6-48. Return to the Summary Table. **Table 6-48. A2D _ REG _ 41 Re g ister Field Descri p tions**

|Figure 6-43. A2D_REG_41 Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|RESERVED|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|RESERVED||SGMII_IO_LOO PBACK_EN|RESERVED|
|R-0h R/W-0h R-0h||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7-2|RESERVED|R|0h|Reserved|
|1|SGMII_IO_LOOPBACK_E N|R/W|0h|1b = Connects RX and TX signals internally to provide internal loopback option without external components.|
|0|RESERVED|R|0h|Reserved|



84 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.25 A2D_REG_44 Register (Offset = 42Ch) [Reset = 0000h] ** A2D_REG_44 is shown in Figure 6-44 and described in Table 6-49. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-44. A2D_REG_44 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h R-0h R-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|RESERVED|RESERVED|SGMII_DIG_LO OPBACK_EN|RESERVED|||RESERVED|
|R-0h R-0h R-0h R/W-0h R-0h R-0h||||||||

###### **Table 6-49. A2D _ REG _ 44 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|RESERVED|R|0h|Reserved|
|13|RESERVED|R|0h|Reserved|
|12|RESERVED|R|0h|Reserved|
|11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5|RESERVED|R|0h|Reserved|
|4|SGMII_DIG_LOOPBACK_ EN|R/W|0h|1b = Loops back TX data to RX before the IO|
|3-1|RESERVED|R|0h|Reserved|
|0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 85

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.26 A2D_REG_47 Register (Offset = 42Fh) [Reset = 0000h] ** A2D_REG_47 is shown in Figure 6-45 and described in Table 6-50. Return to the Summary Table. **Table 6-50. A2D _ REG _ 47 Re g ister Field Descri p tions**

|Figure 6-45. A2D_REG_47 Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED|||||
|R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|RESERVED|spare_in_2_fro mdig_sl_2|spare_in_2_fro mdig_sl_1|spare_in_2_fro mdig_sl_0|
|R-0h R-0h R/W-0h R/W-0h R/W-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-4|RESERVED|R|0h|Reserved|
|3|RESERVED|R|0h|Reserved|
|2|spare_in_2_fromdig_sl_2|R/W|0h|energy lost indication force control value|
|1|spare_in_2_fromdig_sl_1|R/W|0h|energy lost detector enable force control value|
|0|spare_in_2_fromdig_sl_0|R/W|0h|[0] - sleep enable force control value Force control enable is controlled by reg0x041E[8]|



86 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.27 A2D_REG_48 Register (Offset = 430h) [Reset = 0960h] ** A2D_REG_48 is shown in Figure 6-46 and described in Table 6-51. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-46. A2D_REG_48 Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED|RESERVED|RESERVED|RESERVED|DLL_TX_DELAY_CTRL_SL|
|R-0h R-0h R-0h R-0h R/W-9h|||||
|7 6 5 4 3 2 1 0|||||
|DLL_RX_DELAY_CTRL_SL||||RESERVED|
|R/W-6h R-0h|||||

###### **Table 6-51. A2D _ REG _ 48 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|RESERVED|R|0h|Reserved|
|13|RESERVED|R|0h|Reserved|
|12|RESERVED|R|0h|Reserved|
|11-8|DLL_TX_DELAY_CTRL_S L|R/W|9h|Refer to electrical specification for delay vs code information.|
|7-4|DLL_RX_DELAY_CTRL_ SL|R/W|6h|Refer to electrical specification for delay vs code information.|
|3-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 87

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.28 A2D_REG_66 Register (Offset = 442h) [Reset = 0000h] ** A2D_REG_66 is shown in Figure 6-47 and described in Table 6-52. Return to the Summary Table. **Table 6-52. A2D _ REG _ 66 Re g ister Field Descri p tions**

|Figure 6-47. A2D_REG_66 Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED|esd_event_count|||RESERVED|
|R-0h R-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED||RESERVED|RESERVED||
|R-0h R-0h R-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14-9|esd_event_count|R|0h|Number gives the number of esd events on the copper channel|
|8|RESERVED|R|0h|Reserved|
|7-5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3-0|RESERVED|R|0h|Reserved|



88 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.29 LEDS_CFG_1 Register (Offset = 450h) [Reset = 2610h] ** LEDS_CFG_1 is shown in Figure 6-48 and described in Table 6-53. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-48. LEDS_CFG_1 Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|RESERVED|leds_bypass_str etching|leds_blink_rate|led_2_option|
|R-0h R/W-0h R/W-2h R/W-6h||||
|7 6 5 4 3 2 1 0||||
|led_1_option|||led_0_option|
|R/W-1h R/W-0h||||

###### **Table 6-53. LEDS _ CFG _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|leds_bypass_stretching|R/W|0h|Bypass LED Signal Stretch|
|13-12|leds_blink_rate|R/W|2h|Blink Rate for the LED - 00b = 20Hz (50mSec) 01b = 10Hz (100mSec) 10b = 5Hz (200mSec) 11b = 2Hz (500mSec)|
|11-8|led_2_option|R/W|6h|0000b = link OK 0001b = link OK + blink on TX/RX activity 0010b = link OK + blink on TX activity 0011b = link OK + blink on RX activity 0100b = link OK + 100Base-T1 Master 0101b = link OK + 100Base-T1 Slave 0110b = TX/RX activity with stretch option 0111b = Reserved 1000b = Reserved 1001b = Link lost (remains on until register 0x1 is read) 1010b = PRBS error latch until cleared by 0x620(1) 1011b = XMII TX/RX Error with stretch option|
|7-4|led_1_option|R/W|1h|0000b = link OK 0001b = link OK + blink on TX/RX activity 0010b = link OK + blink on TX activity 0011b = link OK + blink on RX activity 0100b = link OK + 100Base-T1 Master 0101b = link OK + 100Base-T1 Slave 0110b = TX/RX activity with stretch option 0111b = Reserved 1000b = Reserved 1001b = Link lost (remains on until register 0x1 is read) 1010b = PRBS error (latch until cleared by 0x620(1) 1011b = XMII TX/RX Error with stretch option|
|3-0|led_0_option|R/W|0h|0000b = link OK 0001b = link OK + blink on TX/RX activity 0010b = link OK + blink on TX activity 0011b = link OK + blink on RX activity 0100b = link OK + 100Base-T1 Master 0101b = link OK + 100Base-T1 Slave 0110b = TX/RX activity with stretch option 0111b = Reserved 1000b = Reserved 1001b = Link lost (remains on until register 0x1 is read) 1010b = PRBS error (latch until cleared by 0x620(1) 1011b = XMII TX/RX Error with stretch option|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 89

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.30 LEDS_CFG_2 Register (Offset = 451h) [Reset = 0000h] ** LEDS_CFG_2 is shown in Figure 6-49 and described in Table 6-54. Return to the Summary Table. **Table 6-54. LEDS _ CFG _ 2 Re g ister Field Descri p tions**

|Figure 6-49. LEDS_CFG_2 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED||RESERVED||||XXXX|RESERVED|
|R-0h R-0h R-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|RESERVED|RESERVED|RESERVED|led_1_polarity|RESERVED|RESERVED|led_0_polarity|
|R-0h R-0h R-0h R-0h R/W-0h R-0h R-0h R/W-0h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-14|RESERVED|R|0h|Reserved|
|13-10|RESERVED|R|0h|Reserved|
|11-9|cfg_ieee_compl_sel|R/W|0h|Observe IEEE Compliance signals in LED_0_GPIO_0, when LED_0_GPIO_CTRL= 'h5 as follows - 000b = loc_rcvr_status 001b = rem_rcvr_status 010b = loc_snr_margin 011b = rem_phy_ready 100b = pma_watchdog_status 101b = link_sync_link_control|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3|led_1_polarity|R/W|0h|LED_1 polarity|
|2|RESERVED|R|0h|Reserved|
|1|RESERVED|R|0h|Reserved|
|0|led_0_polarity|R/W|0h|LED_0 polarity|



90 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.31 IO_MUX_CFG_1 Register (Offset = 452h) [Reset = 0000h] ** IO_MUX_CFG_1 is shown in Figure 6-50 and described in Table 6-55. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-50. IO_MUX_CFG_1 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|RESERVED|led_1_gpio_ctrl|
|R-0h R-0h R/W-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|RESERVED|led_0_gpio_ctrl|
|R-0h R-0h R/W-0h|||

###### **Table 6-55. IO _ MUX _ CFG _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-14|RESERVED|R|0h|Reserved|
|13-11|RESERVED|R|0h|Reserved|
|10-8|led_1_gpio_ctrl|R/W|0h|Controls the output of LED_1 IO - 000b = LED_1 (default: link OK + blink on TX/RX activity) 001b = Reserved 010b = RGMII data match indication 011b = Under-Voltage indication 100b = Interrupt 101b = IEEE compliance signals 110b = constant 0 111b = constant 1|
|7-6|RESERVED|R|0h|Reserved|
|5-3|RESERVED|R|0h|Reserved|
|2-0|led_0_gpio_ctrl|R/W|0h|Controls the output of LED_0 IO: 000b = LED_0 (default: LINK) 001b = Reserved 010b = RGMII data match indication 011b = Under-Voltage indication 100b = Interrupt 101b = IEEE compliance signals (see 0x451[11:9]) 110b = constant 0 111b = constant 1|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 91

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.32 IO_MUX_CFG_2 Register (Offset = 453h) [Reset = 0001h] ** IO_MUX_CFG_2 is shown in Figure 6-51 and described in Table 6-56. Return to the Summary Table. **Table 6-56. IO _ MUX _ CFG _ 2 Re g ister Field Descri p tions**

|Figure 6-51. IO_MUX_CFG_2 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|||
|R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|clk_o_clk_source|clk_o_gpio_ctrl|
|R-0h R/W-0h R/W-1h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-6|RESERVED|R|0h|Reserved|
|5-3|clk_o_clk_source|R/W|0h|Clock Observable in CLK_O pin - 000b = xi_osc_25m_1p0v_dl (25MHz crystal output - from analog) 001b = Reserved 010b = Reserved 011b = 125MHz clock 100b = 125MHz clock 101b = Reserved 110b = Reserved 111b = Reserved|
|2-0|clk_o_gpio_ctrl|R/W|1h|Controls the output of CLK_O IO - 000b = LED_2 (default: TX/RX activity with stretch option(LED_2_OPTION=0x6) 001b = Clock out (see 0x453[5:3]) 010b = RGMII data match indication 011b = Under-Voltage indication 100b = constant 0 101b = constant 0 110b = constant 0 111b = constant 1|



92 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.33 IO_CONTROL_3 Register (Offset = 456h) [Reset = 0108h] ** IO_CONTROL_3 is shown in Figure 6-52 and described in Table 6-57. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-52. IO_CONTROL_3 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED||cfg_mac_rx_impedance|
|R-0h R/W-8h|||
|7 6 5 4 3 2 1 0|||
|cfg_mac_rx_impedance|RESERVED||
|R/W-8h R-0h|||

###### **Table 6-57. IO _ CONTROL _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-10|RESERVED|R|0h|Reserved|
|9-5|cfg_mac_rx_impedance|R/W|8h|Slew Rate Control for RGMII pads - 01010b = Medium Slew (OA tr/tf compliant, max tr/tf = 1ns) 01011b = Slowest Slew (For low emissions, max tr/tf = 1.2ns) 01000b = Default mode (rgmii tr/tf compliant, max tr/tf=750ps)|
|4-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 93

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.34 SOR_VECTOR_1 Register (Offset = 45Dh) [Reset = 0000h] ** SOR_VECTOR_1 is shown in Figure 6-53 and described in Table 6-58. Return to the Summary Table. Strap Status Register: This register has information on modes selected based on straps. Any override of mode using other registers will not be reflected in this register **Table 6-58. SOR _ VECTOR _ 1 Re g ister Field Descri p tions**

|Figure 6-53. SOR_VECTOR_1 Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RGMII_TX_SHI FT|RGMII_RX_SHI FT|SGMII_EN|RGMII_EN|RESERVED|MAC_MODE|
|R-0h R-0h R-0h R-0h R-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|MAC_MODE||MAS/SLV|PHY_AD|||
|R-0h R-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RGMII_TX_SHIFT|R|0h|0x0 = TX shift disbaled 0x1 = TX shift enabled|
|14|RGMII_RX_SHIFT|R|0h|0x0 = RX shift disabled 0x1 = RX shift enabled|
|13|SGMII_EN|R|0h|0x0 = SGMII disabled 0x1 = SGMII enabled|
|12|RGMII_EN|R|0h|0x0 = RGMII disabled 0x1 = RGMII enabled|
|11-9|RESERVED|R|0h|Reserved|
|8-6|MAC_MODE|R|0h|0x0 = SGMII 0x1 = Reserved 0x2 = Reserved 0x3 = Reserved 0x4 = RGMII align 0x5 = RGMII TX shift 0x6 = RGMII TX and RX shift 0x7 = RGMII RX shift|
|5|MAS/SLV|R|0h|0x0 = Slave 0x1 = Master|
|4-0|PHY_AD|R|0h|0x0 = PHY address 0 0x4 = PHY address 4 0x5 = PHY address 5 0x8 = PHY address 8 0xA = PHY address A 0xC = PHY address C 0xD = PHY address D 0xE = PHY address E 0xF = PHY address F|



94 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.35 SOR_VECTOR_2 Register (Offset = 45Eh) [Reset = 0000h] ** SOR_VECTOR_2 is shown in Figure 6-54 and described in Table 6-59. Return to the Summary Table. Strap Status Register: This register has information on modes selected based on straps. Any override of mode using other registers will not be reflected in this register **Table 6-59. SOR _ VECTOR _ 2 Re g ister Field Descri p tions**

|Figure 6-54. SOR_VECTOR_2 Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|RESERVED||
|R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED|AUTO/ MANAGED|
|R-0h R-0h||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-1|RESERVED|R|0h|Reserved|
|0|AUTO/MANAGED|R|0h|0x0 = Autonomous mode enabled 0x1 = Managed mode enabled|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 95

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.36 MONITOR_CTRL2 Register (Offset = 468h) [Reset = 0920h] ** MONITOR_CTRL2 is shown in Figure 6-55 and described in Table 6-60. Return to the Summary Table. **Table 6-60. MONITOR _ CTRL2 Re g ister Field Descri p tions**

|Figure 6-55. MONITOR_CTRL2 Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED|cfg_rd_data||RESERVED||RESERVED|
|R-0h R/W-0h R-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|RESERVED||RESERVED||RESERVED||
|R-0h R-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14-12|cfg_rd_data|R/W|0h|Sensor select for read-out: 001b = VDDA 010b = VDD1P0 011b = VDDIO 100b = Temperature|
|11-9|RESERVED|R|0h|Reserved|
|8-6|RESERVED|R|0h|Reserved|
|5-3|RESERVED|R|0h|Reserved|
|2-0|RESERVED|R|0h|Reserved|



96 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.37 MONITOR_CTRL4 Register (Offset = 46Ah) [Reset = 0094h] ** MONITOR_CTRL4 is shown in Figure 6-56 and described in Table 6-61. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-56. MONITOR_CTRL4 Register|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||||
|RESERVED||||||RESERVED|
|R-0h R-0h|||||||
|7 6 5 4 3 2 1 0|||||||
|RESERVED|RESERVED|RESERVED|RESERVED|cfg_reset|periodic|start|
|R-0h R-0h R-0h R-0h R/W-1h R/W-0h R/WSC-0h|||||||

###### **Table 6-61. MONITOR _ CTRL4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|RESERVED|R|0h|Reserved|
|5-4|RESERVED|R|0h|Reserved|
|3|RESERVED|R|0h|Reserved|
|2|cfg_reset|R/W|1h|0b = Enable the monitor 1b = Monitor is held in reset state At any point of time, if the signal is changed to 1, the module abruptly goes to reset state|
|1|periodic|R/W|0h|0b = Monitor is enabled only when start is set for one iteration 1b = Monitor is enabled for periodic iteration|
|0|start|R/WSC|0h|Start indication for sensor monitor FSM, self clearing|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 97

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.38 MONITOR_STAT1 Register (Offset = 47Bh) [Reset = 0000h] ** MONITOR_STAT1 is shown in Figure 6-57 and described in Table 6-62. Return to the Summary Table. **Fi g ure 6-57. MONITOR _ STAT1 Re g ister**

15 14 13 12 11 10 9 8

stat_rd_data

R-0h


7 6 5 4 3 2 1 0


stat_rd_data

R-0h
###### **Table 6-62. MONITOR _ STAT1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|stat_rd_data|R|0h|Read sensor data|



98 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.39 RS_DECODER Register (Offset = 510h) [Reset = 2D50h] ** RS_DECODER is shown in Figure 6-58 and described in Table 6-63. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-58. RS_DECODER Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|cfg_rs_decoder _bypass|RESERVED|RESERVED||
|R/W-0h R-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|RESERVED|||RESERVED|
|R-0h R-0h||||

###### **Table 6-63. RS _ DECODER Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|cfg_rs_decoder_bypass|R/W|0h|Bypass RS decoder 0h = RS decoder in use 1h = Bypass RS decoder|
|14|RESERVED|R|0h|Reserved|
|13-8|RESERVED|R|0h|Reserved|
|7-1|RESERVED|R|0h|Reserved|
|0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 99

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.40 TRAINING_RX_STATUS_7 Register (Offset = 52Bh) [Reset = 0000h] ** TRAINING_RX_STATUS_7 is shown in Figure 6-59 and described in Table 6-64. Return to the Summary Table. **Table 6-64. TRAINING _ RX _ STATUS _ 7 Re g ister Field Descri p tions**

|Figure 6-59. TRAINING_RX_STATUS_7 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|rx_rvrs_pol|RESERVED|
|R-0h R-0h R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED||RESERVED|
|R-0h R-0h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-13|RESERVED|R|0h|Reserved|
|12|rx_rvrs_pol|R|0h|Received polarity 0h = Polarity decoded from received is not inverted 1h = Polarity decoded from receiver is inverted|
|11-8|RESERVED|R|0h|Reserved|
|7-4|RESERVED|R|0h|Reserved|
|3-0|RESERVED|R|0h|Reserved|



100 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.41 LINK_QUAL_1 Register (Offset = 543h) [Reset = 0000h] ** LINK_QUAL_1 is shown in Figure 6-60 and described in Table 6-65. Return to the Summary Table. **Fi g ure 6-60. LINK _ QUAL _ 1 Re g ister**

R-0h


7 6 5 4 3 2 1 0


link_training_time

R-0h
###### **Table 6-65. LINK _ QUAL _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|RESERVED|R|0h|Reserved|
|7-0|link_training_time|R|0h|Link training time in ms (TC12)|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 101

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.42 LINK_QUAL_2 Register (Offset = 544h) [Reset = 0000h] ** LINK_QUAL_2 is shown in Figure 6-61 and described in Table 6-66. Return to the Summary Table. **Fi g ure 6-61. LINK _ QUAL _ 2 Re g ister**

15 14 13 12 11 10 9 8

remote_receiver_time

R-0h


7 6 5 4 3 2 1 0


local_receiver_time

R-0h
###### **Table 6-66. LINK _ QUAL _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|remote_receiver_time|R|0h|Remote receiver time in ms (TC12)|
|7-0|local_receiver_time|R|0h|Local receiver time in ms (TC12)|



102 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.43 LINK_DOWN_LATCH_STAT Register (Offset = 545h) [Reset = 0000h] ** LINK_DOWN_LATCH_STAT is shown in Figure 6-62 and described in Table 6-67. Return to the Summary Table. **Table 6-67. LINK _ DOWN _ LATCH _ STAT Re g ister Field Descri p tions**

|Figure 6-62. LINK_DOWN_LATCH_STAT Register|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||||
|RESERVED|||||||
|R-0h|||||||
|7 6 5 4 3 2 1 0|||||||
|RESERVED|channel_ok_ll|link_fail_inhibit_ lh|send_s_sigdet_l h|hi_rfer_lh|block_lock_ll|pma_watchdog _ll|
|R-0h R/W0C-0h R/W0C-0h R/W0C-0h R/W0C-0h R/W0S-0h R/W0S-0h|||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-6|RESERVED|R|0h|Reserved|
|5|channel_ok_ll|R/W0C|0h|1b = Channel ok was never de-asserted 0b = Channel ok was de-asserted|
|4|link_fail_inhibit_lh|R/W0C|0h|1b = Link fail inhibit assertion was reported 0b = Link fail inhibit assertion was never reported|
|3|send_s_sigdet_lh|R/W0C|0h|1b = Send s sigdet assertion was reported 0b = Send s sigdet assertion was never reported|
|2|hi_rfer_lh|R/W0C|0h|1b = High ri rfer assertion was reported 0b = High ri rfer assertion was never reported|
|1|block_lock_ll|R/W0S|0h|1b = Block lock de-assertion was never reported 0b = Block lock de-assertion was never reported|
|0|pma_watchdog_ll|R/W0S|0h|1b = Low pma watchdog was never reported 0b = Low pma watchdof was reported|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 103

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.44 LINK_QUAL_3 Register (Offset = 547h) [Reset = 0000h] ** LINK_QUAL_3 is shown in Figure 6-63 and described in Table 6-68. Return to the Summary Table. **Table 6-68. LINK _ QUAL _ 3 Re g ister Field Descri p tions**

|Figure 6-63. LINK_QUAL_3 Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|link_loss_cnt|link_fail_cnt|
|R-0h R-0h||
|7 6 5 4 3 2 1 0||
|link_fail_cnt||
|R-0h||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-10|link_loss_cnt|R|0h|Link loss count since last power cycle (TC12)|
|9-0|link_fail_cnt|R|0h|Link fail without link loss count since last power cycle (TC12)|



104 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.45 LINK_QUAL_4 Register (Offset = 548h) [Reset = 0000h] ** LINK_QUAL_4 is shown in Figure 6-64 and described in Table 6-69. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-64. LINK_QUAL_4 Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|RESERVED||
|R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED|comm_ready|
|R-0h R-0h||

###### **Table 6-69. LINK _ QUAL _ 4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-1|RESERVED|R|0h|Reserved|
|0|comm_ready|R|0h|Communication ready status (TC12)|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 105

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.46 RS_DECODER_FRAME_STAT_2 Register (Offset = 552h) [Reset = 0000h] ** RS_DECODER_FRAME_STAT_2 is shown in Figure 6-65 and described in Table 6-70. Return to the Summary Table. **Fi g ure 6-65. RS _ DECODER _ FRAME _ STAT _ 2 Re g ister**

15 14 13 12 11 10 9 8

rs_dec_uncorr_frame_cnt

R-0h


7 6 5 4 3 2 1 0


rs_dec_uncorr_frame_cnt

R-0h
###### **Table 6-70. RS _ DECODER _ FRAME _ STAT _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|rs_dec_uncorr_frame_cnt|R|0h|No of uncorrectable RS frames received at RS decoder, clear on read, saturates|



106 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.47 RS_DECODER_FRAME_STAT_3 Register (Offset = 553h) [Reset = 0000h] ** RS_DECODER_FRAME_STAT_3 is shown in Figure 6-66 and described in Table 6-71. Return to the Summary Table. **Fi g ure 6-66. RS _ DECODER _ FRAME _ STAT _ 3 Re g ister**

15 14 13 12 11 10 9 8

rs_dec_err_frame_cnt

R-0h


7 6 5 4 3 2 1 0


rs_dec_err_frame_cnt

R-0h
###### **Table 6-71. RS _ DECODER _ FRAME _ STAT _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|rs_dec_err_frame_cnt|R|0h|No of erroreous RS frames received at RS decoder, clear on read, saturates|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 107

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.48 RGMII_CTRL Register (Offset = 600h) [Reset = 0120h] ** RGMII_CTRL is shown in Figure 6-67 and described in Table 6-72. Return to the Summary Table. **Table 6-72. RGMII _ CTRL Re g ister Field Descri p tions**

|Figure 6-67. RGMII_CTRL Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED||||rgmii_rx_half_full_th||
|R-0h R/W-2h||||||
|7 6 5 4 3 2 1 0||||||
|rgmii_rx_half_fu ll_th|rgmii_tx_half_full_th|rgmii_tx_if_en|invert_rgmii_txd|invert_rgmii_rxd|RESERVED|
|R/W-2h R/W-2h R/W-0h R/W-0h R/W-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-10|RESERVED|R|0h|Reserved|
|9-7|rgmii_rx_half_full_th|R/W|2h|RGMII RX sync FIFO half full threshold|
|6-4|rgmii_tx_half_full_th|R/W|2h|RGMII TX sync FIFO half full threshold|
|3|rgmii_tx_if_en|R/W|0h|RGMII enable bit Default from strap 0h = RGMII disable 1h = RGMII enable|
|2|invert_rgmii_txd|R/W|0h|Invert RGMII Tx wire order - full swap [3:0] to [0:3] 0h = Keep RGMII Tx wire order same 1h = Invert RGMII Tx wire order|
|1|invert_rgmii_rxd|R/W|0h|Invert RGMII Rx wire order - full swap [3:0] to [0:3] 0h = Keep RGMII Rx wire order same 1h = Invert RGMII Rx wire order|
|0|RESERVED|R|0h|Reserved|



108 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.49 RGMII_FIFO_STATUS Register (Offset = 601h) [Reset = 0000h] ** RGMII_FIFO_STATUS is shown in Figure 6-68 and described in Table 6-73. Return to the Summary Table. **Table 6-73. RGMII _ FIFO _ STATUS Re g ister Field Descri p tions**

|Figure 6-68. RGMII_FIFO_STATUS Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED|||||
|R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|rgmii_rx_af_full _err|rgmii_rx_af_em pty_err|rgmii_tx_af_full _err|rgmii_tx_af_em pty_err|
|R-0h R/W0C-0h R/W0C-0h R/W0C-0h R/W0C-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-4|RESERVED|R|0h|Reserved|
|3|rgmii_rx_af_full_err|R/W0C|0h|RGMII RX fifo full error 0h = No empty fifo error 1h = RGMII TX full error has been indicated|
|2|rgmii_rx_af_empty_err|R/W0C|0h|RGMII RX fifo empty error 0h = No empty fifo error 1h = RGMII RX empty error has been indicated|
|1|rgmii_tx_af_full_err|R/W0C|0h|RGMII TX fifo full error 0h = No empty fifo error 1h = RGMII TX full error has been indicated|
|0|rgmii_tx_af_empty_err|R/W0C|0h|RGMII TX fifo empty error 0h = No empty fifo error 1h = RGMII TX empty error has been indicated|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 109

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.50 RGMII_DELAY_CTRL Register (Offset = 602h) [Reset = 0000h] ** RGMII_DELAY_CTRL is shown in Figure 6-69 and described in Table 6-74. Return to the Summary Table. **Table 6-74. RGMII _ DELAY _ CTRL Re g ister Field Descri p tions**

|Figure 6-69. RGMII_DELAY_CTRL Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|||
|R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|rx_clk_sel|tx_clk_sel|
|R-0h R/W-0h R/W-0h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-2|RESERVED|R|0h|Reserved|
|1|rx_clk_sel|R/W|0h|In RGMII mode, Enable or disable the internal delay for RXD wrt RX_CLK (use this mode when RGMII_RX_CLK and RGMII_RXD are aligned). The delay magnitude can be configured by programming register 0x430[7:4] 0h = clock and data are aligned 1h = clock is delayed relative to RGMII_RX data|
|0|tx_clk_sel|R/W|0h|In RGMII mode, Enable or disable the internal delay for TXD wrt TX_CLK (use this mode when RGMII_TX_CLK and RGMII_TXD are aligned). The delay magnitude can be configured by programming register 0x430[11:8] 0h = clock and data are aligned 1h = clock is internally delayed|



110 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.51 SGMII_CTRL_1 Register (Offset = 608h) [Reset = 007Bh] ** SGMII_CTRL_1 is shown in Figure 6-70 and described in Table 6-75. Return to the Summary Table. SGMII Register: Available only on DP83TG720S-Q1

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-70. SGMII_CTRL_1 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|sgmii_tx_err_di s|cfg_align_idx_fo rce|cfg_align_idx_value||||cfg_sgmii_en|cfg_sgmii_rx_p ol_invert|
|R/W-0h R/W-0h R/W-0h R/W-0h R/W-0h||||||||
|7 6 5 4 3 2 1 0||||||||
|cfg_sgmii_tx_po l_invert|RESERVED||RESERVED|RESERVED|sgmii_autoneg_timer||mr_an_enable|
|R/W-0h R-0h R-0h R-0h R/W-1h R/W-1h||||||||

###### **Table 6-75. SGMII _ CTRL _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|sgmii_tx_err_dis|R/W|0h|1 = Disable SGMII TX Error indication 0 = Enable SGMII TX Error indication|
|14|cfg_align_idx_force|R/W|0h|Force word boundray index selection|
|13-10|cfg_align_idx_value|R/W|0h|when cfg_align_idx_force = 1 This value set the iword boundray index|
|9|cfg_sgmii_en|R/W|0h|SGMII enable bit Default from strap 0h = SGMII disable 1h = SGMII enable|
|8|cfg_sgmii_rx_pol_invert|R/W|0h|SGMII RX bus invert polarity 0h = Polarity not inverted 1h = SGMII RX bus invert polarity|
|7|cfg_sgmii_tx_pol_invert|R/W|0h|SGMII TX bus invert polarity 0h = Polarity not inverted 1h = SGMII TX bus invert polarity|
|6-5|RESERVED|R|0h|Reserved|
|4|RESERVED|R|0h|Reserved|
|3|RESERVED|R|0h|Reserved|
|2-1|sgmii_autoneg_timer|R/W|1h|Selects duration of SGMII Auto-Negotiation timer: 00: 1.6ms 01: 2us 10: 800us 11: 11ms|
|0|mr_an_enable|R/W|1h|1 = Enable SGMII Auto-Negotaition 0 = Disable SGMII Auto-Negotiation|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 111

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.52 SGMII_STATUS Register (Offset = 60Ah) [Reset = 0000h] ** SGMII_STATUS is shown in Figure 6-71 and described in Table 6-76. Return to the Summary Table. SGMII Register: Available only on DP83TG720S-Q1 **Table 6-76. SGMII _ STATUS Re g ister Field Descri p tions**

|Figure 6-71. SGMII_STATUS Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED|sgmii_page_rec eived|link_status_100 0bx|mr_an_complet e|cfg_align_en|cfg_sync_status|
|R-0h R-0h R-0h R-0h R-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|cfg_align_idx||cfg_state||||
|R-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-13|RESERVED|R|0h|Reserved|
|12|sgmii_page_received|R|0h|Indicates that a new auto neg page was received 0h = No new auto neg page received 1h = A new auto neg page received|
|11|link_status_1000bx|R|0h|sgmii link status 0h = SGMII link down 1h = SGMII link up|
|10|mr_an_complete|R|0h|sgmii autoneg complete indication 0h = SGMII autoneg not completed 1h = SGMII autoneg completed|
|9|cfg_align_en|R|0h|word boundary FSM - align indication|
|8|cfg_sync_status|R|0h|word boundary FSM - sync status indication 0h = sync not achieved 1h = sync achieved|
|7-4|cfg_align_idx|R|0h|word boundary index selection|
|3-0|cfg_state|R|0h|word boundary FSM state|



112 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.53 SGMII_CTRL_2 Register (Offset = 60Ch) [Reset = 001Bh] ** SGMII_CTRL_2 is shown in Figure 6-72 and described in Table 6-77. Return to the Summary Table. SGMII Register: Available only on DP83TG720S-Q1

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-72. SGMII_CTRL_2 Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED||||RESERVED|
|R-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|mr_restart_an|tx_half_full_th|rx_half_full_th||
|R-0h R/WSC,0-0h R/W-3h R/W-3h|||||

###### **Table 6-77. SGMII _ CTRL _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|RESERVED|R|0h|Reserved|
|6|mr_restart_an|R/WSC,0|0h|Restart sgmii autonegotiation|
|5-3|tx_half_full_th|R/W|3h|SGMII TX sync FIFO half full threshold|
|2-0|rx_half_full_th|R/W|3h|SGMII RX sync FIFO half full threshold|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 113

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.54 SGMII_FIFO_STATUS Register (Offset = 60Dh) [Reset = 0000h] ** SGMII_FIFO_STATUS is shown in Figure 6-73 and described in Table 6-78. Return to the Summary Table. SGMII Register: Available only on DP83TG720S-Q1 **Table 6-78. SGMII _ FIFO _ STATUS Re g ister Field Descri p tions**

|Figure 6-73. SGMII_FIFO_STATUS Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED|||||
|R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|sgmii_rx_af_full _err|sgmii_rx_af_em pty_err|sgmii_tx_af_full _err|sgmii_tx_af_em pty_err|
|R-0h R/W0C-0h R/W0C-0h R/W0C-0h R/W0C-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-4|RESERVED|R|0h|Reserved|
|3|sgmii_rx_af_full_err|R/W0C|0h|SGMII RX fifo full error 0h = No error indication 1h = SGMII RX fifo full error has been indicated|
|2|sgmii_rx_af_empty_err|R/W0C|0h|SGMII RX fifo empty error 0h = No error indication 1h = SGMII RX fifo empty error has been indicated|
|1|sgmii_tx_af_full_err|R/W0C|0h|SGMII TX fifo full error 0h = No error indication 1h = SGMII TX fifo full error has been indicated|
|0|sgmii_tx_af_empty_err|R/W0C|0h|SGMII TX fifo empty error 0h = No error indication 1h = SGMII TX fifo empty error has been indicated|



114 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.55 PRBS_STATUS_1 Register (Offset = 618h) [Reset = 0000h] ** PRBS_STATUS_1 is shown in Figure 6-74 and described in Table 6-79. Return to the Summary Table. **Fi g ure 6-74. PRBS _ STATUS _ 1 Re g ister**

R-0h


7 6 5 4 3 2 1 0


prbs_err_ov_cnt

R-0h
###### **Table 6-79. PRBS _ STATUS _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|RESERVED|R|0h|Reserved|
|7-0|prbs_err_ov_cnt|R|0h|Holds number of error counter overflow that received by the PRBS checker. Value in this register is locked when write is done to register prbs_status_6 bit[0] or bit[1]. Counter stops on 0xFF. Note: when PRBS counters work in single mode, overflow counter is not active|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 115

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.56 PRBS_CTRL_1 Register (Offset = 619h) [Reset = 0574h] ** PRBS_CTRL_1 is shown in Figure 6-75 and described in Table 6-80. Return to the Summary Table. **Table 6-80. PRBS _ CTRL _ 1 Re g ister Field Descri p tions**

|Figure 6-75. PRBS_CTRL_1 Register|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||||
|RESERVED||RESERVED|send_pkt|RESERVED|cfg_prbs_chk_sel|||
|R-0h R-0h R/WMC,0-0h R-0h R/W-5h||||||||
|7 6 5 4 3 2 1 0||||||||
|RESERVED|cfg_prbs_gen_sel|||cfg_prbs_cnt_m ode|cfg_prbs_chk_e nable|cfg_pkt_gen_pr bs|pkt_gen_en|
|R-0h R/W-7h R/W-0h R/W-1h R/W-0h R/W-0h||||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-14|RESERVED|R|0h|Reserved|
|13|RESERVED|R|0h|Reserved|
|12|send_pkt|R/WMC,0|0h|Enables generating MAC packet with fix/incremental data w CRC (pkt_gen_en has to be set and cfg_pkt_gen_prbs has to be clear) Cleared automatically when pkt_done is set 0h = Stop MAC packet 1h = Transmit MAC packet w CRC|
|11|RESERVED|R|0h|Reserved|
|10-8|cfg_prbs_chk_sel|R/W|5h|000 : Checker receives from RGMII TX 001 : Checker receives SGMII TX 101 : Checker receives from Cu RX|
|7|RESERVED|R|0h|Reserved|
|6-4|cfg_prbs_gen_sel|R/W|7h|000 : PRBS transmits to RGMII RX 001 : PRBS transmits to SGMII RX 101 : PRBS transmits to Cu TX|
|3|cfg_prbs_cnt_mode|R/W|0h|1 = Continuous mode, when one of the PRBS counters reaches max value, pulse is generated and counter starts counting from zero again 0 = Single mode, When one of the PRBS counters reaches max value, PRBS checker stops counting.|
|2|cfg_prbs_chk_enable|R/W|1h|Enable PRBS checker xbar (to receive data) To be enabled for counters in 0x63C, 0x63D, 0x63E to work 0h = Disable PRBS checker 1h = Enable PRBS checker|
|1|cfg_pkt_gen_prbs|R/W|0h|If set: (1) When pkt_gen_en is set, PRBS packets are generated continuously (3) When pkt_gen_en is cleared, PRBS RX checker is still enabled If cleared: (1) When pkt_gen_en is set, non - PRBS packet is generated (3) When pkt_gen_en is cleared, PRBS RX checker is disabled as well 0h = Stop PRBS packet 1h = Transmit PRBS packet|
|0|pkt_gen_en|R/W|0h|1 = Enable packet/PRBS generator 0 = Disable packet/PRBS generator|



116 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.57 PRBS_CTRL_2 Register (Offset = 61Ah) [Reset = 05DCh] ** PRBS_CTRL_2 is shown in Figure 6-76 and described in Table 6-81. Return to the Summary Table. **Fi g ure 6-76. PRBS _ CTRL _ 2 Re g ister**

15 14 13 12 11 10 9 8

cfg_pkt_len_prbs

R/W-5DCh


7 6 5 4 3 2 1 0


cfg_pkt_len_prbs

R/W-5DCh
###### **Table 6-81. PRBS _ CTRL _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|cfg_pkt_len_prbs|R/W|5DCh|Length (in bytes) of PRBS packets and MAC packets w CRC|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 117

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.58 PRBS_CTRL_3 Register (Offset = 61Bh) [Reset = 007Dh] ** PRBS_CTRL_3 is shown in Figure 6-77 and described in Table 6-82. Return to the Summary Table. **Fi g ure 6-77. PRBS _ CTRL _ 3 Re g ister**

R-0h


7 6 5 4 3 2 1 0


cfg_ipg_len

R/W-7Dh
###### **Table 6-82. PRBS _ CTRL _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|RESERVED|R|0h|Reserved|
|7-0|cfg_ipg_len|R/W|7Dh|Inter-packet gap (in bytes) between packets|



118 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.59 PRBS_STATUS_2 Register (Offset = 61Ch) [Reset = 0000h] ** PRBS_STATUS_2 is shown in Figure 6-78 and described in Table 6-83. Return to the Summary Table. **Fi g ure 6-78. PRBS _ STATUS _ 2 Re g ister**

15 14 13 12 11 10 9 8

prbs_byte_cnt

R-0h


7 6 5 4 3 2 1 0


prbs_byte_cnt

R-0h
###### **Table 6-83. PRBS _ STATUS _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|prbs_byte_cnt|R|0h|Holds number of total bytes that received by the PRBS checker. Value in this register is locked when write is done to register prbs_status_6 bit[0] or bit[1]. When PRBS Count Mode set to zero, count stops on 0xFFFF|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 119

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.60 PRBS_STATUS_3 Register (Offset = 61Dh) [Reset = 0000h] ** PRBS_STATUS_3 is shown in Figure 6-79 and described in Table 6-84. Return to the Summary Table. **Fi g ure 6-79. PRBS _ STATUS _ 3 Re g ister**

15 14 13 12 11 10 9 8

prbs_pkt_cnt_15_0

R-0h


7 6 5 4 3 2 1 0


prbs_pkt_cnt_15_0

R-0h
###### **Table 6-84. PRBS _ STATUS _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|prbs_pkt_cnt_15_0|R|0h|Bits [15:0] of number of total packets received by the PRBS checker Value in this register is locked when write is done to register prbs_status_6 bit[0] or bit[1]. When PRBS Count Mode set to zero, count stops on 0xFFFFFFFF|



120 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.61 PRBS_STATUS_4 Register (Offset = 61Eh) [Reset = 0000h] ** PRBS_STATUS_4 is shown in Figure 6-80 and described in Table 6-85. Return to the Summary Table. **Fi g ure 6-80. PRBS _ STATUS _ 4 Re g ister**

15 14 13 12 11 10 9 8

prbs_pkt_cnt_31_16

R-0h


7 6 5 4 3 2 1 0


prbs_pkt_cnt_31_16

R-0h
###### **Table 6-85. PRBS _ STATUS _ 4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|prbs_pkt_cnt_31_16|R|0h|Bits [31:16] of number of total packets received by the PRBS checker Value in this register is locked when write is done to register prbs_status_6 bit[0] or bit[1]. When PRBS Count Mode set to zero, count stops on 0xFFFFFFFF|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 121

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.62 PRBS_STATUS_6 Register (Offset = 620h) [Reset = 0000h] ** PRBS_STATUS_6 is shown in Figure 6-81 and described in Table 6-86. Return to the Summary Table. **Table 6-86. PRBS _ STATUS _ 6 Re g ister Field Descri p tions**

|Figure 6-81. PRBS_STATUS_6 Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED|pkt_done|pkt_gen_busy|prbs_pkt_ov|prbs_byte_ov|prbs_lock|
|R-0h R-0h R-0h R-0h R-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|prbs_err_cnt||||||
|R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-13|RESERVED|R|0h|Reserved|
|12|pkt_done|R|0h|Set when all MAC packets w CRC are transmitted 0h = MAC packet transmission in progress 1h = MAC packets transmission completed|
|11|pkt_gen_busy|R|0h|1 = Packet generator is in process 0 = Packet generator is not in process|
|10|prbs_pkt_ov|R|0h|If set, packet counter reached overflow Overflow is cleared when PRBS counters are cleared - done by setting bit #1 of prbs_status_6 0h = No overflow 1h = Packet counter overflow|
|9|prbs_byte_ov|R|0h|If set, bytes counter reached overflow Overflow is cleared when PRBS counters are cleared - done by setting bit #1of prbs_status_6 0h = No overflow 1h = byte counter overflow|
|8|prbs_lock|R|0h|1 = PRBS checker is locked sync) on received byte stream 0 = PRBS checker is not locked 0h = PRBS checker is not locked 1h = PRBS checker is locked sync) on received byte stream|
|7-0|prbs_err_cnt|R|0h|Holds number of errored bits received by the PRBS checker Value in this register is locked when write is done to bit[0] or bit[1] When PRBS Count Mode set to zero, count stops on 0xFF Notes: Writing bit 0 generates a lock signal for the PRBS counters. Writing bit 1 generates a lock and clear signal for the PRBS counters|



122 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.63 PRBS_STATUS_8 Register (Offset = 622h) [Reset = 0000h] ** PRBS_STATUS_8 is shown in Figure 6-82 and described in Table 6-87. Return to the Summary Table. **Fi g ure 6-82. PRBS _ STATUS _ 8 Re g ister**

15 14 13 12 11 10 9 8

pkt_err_cnt_15_0

R-0h


7 6 5 4 3 2 1 0


pkt_err_cnt_15_0

R-0h
###### **Table 6-87. PRBS _ STATUS _ 8 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pkt_err_cnt_15_0|R|0h|Bits [15:0] of number of total packets with error received by the PRBS checker Value in this register is locked when write is done to register prbs_status_6 bit[0] or bit[1]. When PRBS Count Mode set to zero, count stops on 0xFFFFFFFF|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 123

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.64 PRBS_STATUS_9 Register (Offset = 623h) [Reset = 0000h] ** PRBS_STATUS_9 is shown in Figure 6-83 and described in Table 6-88. Return to the Summary Table. **Fi g ure 6-83. PRBS _ STATUS _ 9 Re g ister**

15 14 13 12 11 10 9 8

pkt_err_cnt_31_16

R-0h


7 6 5 4 3 2 1 0


pkt_err_cnt_31_16

R-0h
###### **Table 6-88. PRBS _ STATUS _ 9 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pkt_err_cnt_31_16|R|0h|Bits [31:16] of number of total packets with error received by the PRBS checker Value in this register is locked when write is done to register prbs_status_6 bit[0] or bit[1]. When PRBS Count Mode set to zero, count stops on 0xFFFFFFFF|



124 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.65 PRBS_CTRL_4 Register (Offset = 624h) [Reset = 5511h] ** PRBS_CTRL_4 is shown in Figure 6-84 and described in Table 6-89. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-84. PRBS_CTRL_4 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|cfg_pkt_data|||
|R/W-55h|||
|7 6 5 4 3 2 1 0|||
|cfg_pkt_mode|cfg_pattern_vld_bytes|cfg_pkt_cnt|
|R/W-0h R/W-2h R/W-1h|||

###### **Table 6-89. PRBS _ CTRL _ 4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|cfg_pkt_data|R/W|55h|Fixed data to be sent in Fix data mode|
|7-6|cfg_pkt_mode|R/W|0h|0h = Incremental 1h = Fixed 2h = PRBS 3h = PRBS|
|5-3|cfg_pattern_vld_bytes|R/W|2h|Number of bytes of valid pattern in packet (Max - 6) 0h = 0 bytes 1h = 1 bytes 2h = 2 bytes 3h = 3 bytes 4h = 4 bytes 5h = 5 bytes 6h = 6 bytes 7h = 6 bytes|
|2-0|cfg_pkt_cnt|R/W|1h|000b = 1 packet 001b = 10 packets 010b = 100 packets 011b = 1000 packets 100b = 10000 packets 101b = 100000 packets 110b = 1000000 packets 111b = Continuous packets|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 125

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.66 PRBS_CTRL_5 Register (Offset = 625h) [Reset = 0000h] ** PRBS_CTRL_5 is shown in Figure 6-85 and described in Table 6-90. Return to the Summary Table. **Fi g ure 6-85. PRBS _ CTRL _ 5 Re g ister**

15 14 13 12 11 10 9 8

pattern_15_0

R/W-0h


7 6 5 4 3 2 1 0


pattern_15_0

R/W-0h
###### **Table 6-90. PRBS _ CTRL _ 5 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pattern_15_0|R/W|0h|Bits 15:0 of pattern|



126 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.67 PRBS_CTRL_6 Register (Offset = 626h) [Reset = 0000h] ** PRBS_CTRL_6 is shown in Figure 6-86 and described in Table 6-91. Return to the Summary Table. **Fi g ure 6-86. PRBS _ CTRL _ 6 Re g ister**

15 14 13 12 11 10 9 8

pattern_31_16

R/W-0h


7 6 5 4 3 2 1 0


pattern_31_16

R/W-0h
###### **Table 6-91. PRBS _ CTRL _ 6 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pattern_31_16|R/W|0h|Bits 31:16 of pattern|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 127

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.68 PRBS_CTRL_7 Register (Offset = 627h) [Reset = 0000h] ** PRBS_CTRL_7 is shown in Figure 6-87 and described in Table 6-92. Return to the Summary Table. **Fi g ure 6-87. PRBS _ CTRL _ 7 Re g ister**

15 14 13 12 11 10 9 8

pattern_47_32

R/W-0h


7 6 5 4 3 2 1 0


pattern_47_32

R/W-0h
###### **Table 6-92. PRBS _ CTRL _ 7 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pattern_47_32|R/W|0h|Bits 47:32 of pattern|



128 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.69 PRBS_CTRL_8 Register (Offset = 628h) [Reset = 0000h] ** PRBS_CTRL_8 is shown in Figure 6-88 and described in Table 6-93. Return to the Summary Table. **Fi g ure 6-88. PRBS _ CTRL _ 8 Re g ister**

15 14 13 12 11 10 9 8

pmatch_data_15_0

R/W-0h


7 6 5 4 3 2 1 0


pmatch_data_15_0

R/W-0h
###### **Table 6-93. PRBS _ CTRL _ 8 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pmatch_data_15_0|R/W|0h|Bits 15:0 of Perfect Match Data - used for DA (destination address) match|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 129

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.70 PRBS_CTRL_9 Register (Offset = 629h) [Reset = 0000h] ** PRBS_CTRL_9 is shown in Figure 6-89 and described in Table 6-94. Return to the Summary Table. **Fi g ure 6-89. PRBS _ CTRL _ 9 Re g ister**

15 14 13 12 11 10 9 8

pmatch_data_31_16

R/W-0h


7 6 5 4 3 2 1 0


pmatch_data_31_16

R/W-0h
###### **Table 6-94. PRBS _ CTRL _ 9 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pmatch_data_31_16|R/W|0h|Bits 31:16 of Perfect Match Data - used for DA (destination address) match|



130 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.71 PRBS_CTRL_10 Register (Offset = 62Ah) [Reset = 0000h] ** PRBS_CTRL_10 is shown in Figure 6-90 and described in Table 6-95. Return to the Summary Table. **Fi g ure 6-90. PRBS _ CTRL _ 10 Re g ister**

15 14 13 12 11 10 9 8

pmatch_data_47_32

R/W-0h


7 6 5 4 3 2 1 0


pmatch_data_47_32

R/W-0h
###### **Table 6-95. PRBS _ CTRL _ 10 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|pmatch_data_47_32|R/W|0h|Bits 47:32 of Perfect Match Data - used for DA (destination address) match|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 131

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.72 CRC_STATUS Register (Offset = 638h) [Reset = 0000h] ** CRC_STATUS is shown in Figure 6-91 and described in Table 6-96. Return to the Summary Table. **Table 6-96. CRC _ STATUS Re g ister Field Descri p tions**

|Figure 6-91. CRC_STATUS Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|||
|R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|rx_bad_crc|tx_bad_crc|
|R-0h R-0h R-0h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-2|RESERVED|R|0h|Reserved|
|1|rx_bad_crc|R|0h|CRC error indication in packet received on Cu RX 0h = No CRC error 1h = CRC error|
|0|tx_bad_crc|R|0h|CRC error indication in packet transmitted on Cu TX 0h = No CRC error 1h = CRC error|



132 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.73 PKT_STAT_1 Register (Offset = 639h) [Reset = 0000h] ** PKT_STAT_1 is shown in Figure 6-92 and described in Table 6-97. Return to the Summary Table. **Fi g ure 6-92. PKT _ STAT _ 1 Re g ister**

15 14 13 12 11 10 9 8

tx_pkt_cnt_15_0

R-0h


7 6 5 4 3 2 1 0


tx_pkt_cnt_15_0

R-0h
###### **Table 6-97. PKT _ STAT _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|tx_pkt_cnt_15_0|R|0h|Lower 16 bits of Tx packet counter Note : Register is cleared when 0x639, 0x63A, 0x63B are read in sequence|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 133

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.74 PKT_STAT_2 Register (Offset = 63Ah) [Reset = 0000h] ** PKT_STAT_2 is shown in Figure 6-93 and described in Table 6-98. Return to the Summary Table. **Fi g ure 6-93. PKT _ STAT _ 2 Re g ister**

15 14 13 12 11 10 9 8

tx_pkt_cnt_31_16

R-0h


7 6 5 4 3 2 1 0


tx_pkt_cnt_31_16

R-0h
###### **Table 6-98. PKT _ STAT _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|tx_pkt_cnt_31_16|R|0h|Upper 16 bits of Tx packet counter Note : Register is cleared when 0x639, 0x63A, 0x63B are read in sequence|



134 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.75 PKT_STAT_3 Register (Offset = 63Bh) [Reset = 0000h] ** PKT_STAT_3 is shown in Figure 6-94 and described in Table 6-99. Return to the Summary Table. **Fi g ure 6-94. PKT _ STAT _ 3 Re g ister**

15 14 13 12 11 10 9 8

tx_err_pkt_cnt

R-0h


7 6 5 4 3 2 1 0


tx_err_pkt_cnt

R-0h
###### **Table 6-99. PKT _ STAT _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|tx_err_pkt_cnt|R|0h|Tx packet w error (CRC error) counter Note : Register is cleared when 0x639, 0x63A, 0x63B are read in sequence|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 135

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.76 PKT_STAT_4 Register (Offset = 63Ch) [Reset = 0000h] ** PKT_STAT_4 is shown in Figure 6-95 and described in Table 6-100. Return to the Summary Table. **Fi g ure 6-95. PKT _ STAT _ 4 Re g ister**

15 14 13 12 11 10 9 8

rx_pkt_cnt_15_0

R-0h


7 6 5 4 3 2 1 0


rx_pkt_cnt_15_0

R-0h
###### **Table 6-100. PKT _ STAT _ 4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|rx_pkt_cnt_15_0|R|0h|Lower 16 bits of Rx packet counter Note : Register is cleared when 0x63C, 0x63D, 0x63E are read in sequence|



136 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.77 PKT_STAT_5 Register (Offset = 63Dh) [Reset = 0000h] ** PKT_STAT_5 is shown in Figure 6-96 and described in Table 6-101. Return to the Summary Table. **Fi g ure 6-96. PKT _ STAT _ 5 Re g ister**

15 14 13 12 11 10 9 8

rx_pkt_cnt_31_16

R-0h


7 6 5 4 3 2 1 0


rx_pkt_cnt_31_16

R-0h
###### **Table 6-101. PKT _ STAT _ 5 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|rx_pkt_cnt_31_16|R|0h|Upper 16 bits of Rx packet counter Note : Register is cleared when 0x63C, 0x63D, 0x63E are read in sequence|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 137

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.78 PKT_STAT_6 Register (Offset = 63Eh) [Reset = 0000h] ** PKT_STAT_6 is shown in Figure 6-97 and described in Table 6-102. Return to the Summary Table. **Fi g ure 6-97. PKT _ STAT _ 6 Re g ister**

15 14 13 12 11 10 9 8

rx_err_pkt_cnt

R-0h


7 6 5 4 3 2 1 0


rx_err_pkt_cnt

R-0h
###### **Table 6-102. PKT _ STAT _ 6 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|rx_err_pkt_cnt|R|0h|Rx packet w error (CRC error) counter Note : Register is cleared when 0x63C, 0x63D, 0x63E are read in sequence|



138 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.79 SQI_REG_1 Register (Offset = 871h) [Reset = 0000h] ** SQI_REG_1 is shown in Figure 6-98 and described in Table 6-103. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-98. SQI_REG_1 Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|RESERVED||||
|R-0h||||
|7 6 5 4 3 2 1 0||||
|worst_sqi_out|RESERVED|sqi_out|RESERVED|
|R-0h R-0h R-0h R-0h||||

###### **Table 6-103. SQI _ REG _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|RESERVED|R|0h|Reserved|
|7-5|worst_sqi_out|R|0h|3 bit Worst SQI since last read (see SQI mapping above) Cleared on Read|
|4|RESERVED|R|0h|Reserved|
|3-1|sqi_out|R|0h|3 bit SQI - (mse here refers to Mean Square Error 0x875[9:0]) 0b000 = MSE > 102 0b001 = 81 < MSE ≤102 0b010 = 65 < MSE ≤ 81 0b011 = 51 < MSE ≤ 65 0b100 = 41 < MSE ≤ 51 0b101 = 32 < MSE ≤ 41 0b110 = 25 < MSE ≤ 32 0b111 = MSE ≤ 25|
|0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 139

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.80 DSP_REG_74 Register (Offset = 874h) [Reset = 0000h] ** DSP_REG_74 is shown in Figure 6-99 and described in Table 6-104. Return to the Summary Table. **Fi g ure 6-99. DSP _ REG _ 74 Re g ister**

15 14 13 12 11 10 9 8

worst_peak_mse_out

R-0h


7 6 5 4 3 2 1 0


peak_mse_out

R-0h
###### **Table 6-104. DSP _ REG _ 74 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-8|worst_peak_mse_out|R|0h|Worst peak mse out since last read as per TC12 (see peak mse mapping above) Cleared on Read|
|7-0|peak_mse_out|R|0h|Peak mse as per TC12 - This value is 0.0625*averaged squared slicer error(max val = 0.015625). To get actual squared slicer error divide this value by 248.|



140 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **6.6.2.81 DSP_REG_75 Register (Offset = 875h) [Reset = 0000h] ** DSP_REG_75 is shown in Figure 6-100 and described in Table 6-105. Return to the Summary Table.

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Figure 6-100. DSP_REG_75 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|RESERVED|mse_lock|
|R-0h R-0h R-0h|||
|7 6 5 4 3 2 1 0|||
|mse_lock|||
|R-0h|||

###### **Table 6-105. DSP _ REG _ 75 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-12|RESERVED|R|0h|Reserved|
|11-10|RESERVED|R|0h|Reserved|
|9-0|mse_lock|R|0h|10 bit mse used for SQI mapping. (mse = mean square error at the receiver)|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 141

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.82 PMA_PMD_CONTROL_1 Register (Offset = 1000h) [Reset = 0000h] ** PMA_PMD_CONTROL_1 is shown in Figure 6-101 and described in Table 6-106. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-106. PMA _ PMD _ CONTROL _ 1 Re g ister Field Descri p tions**

|Figure 6-101. PMA_PMD_CONTROL_1 Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|pma_reset_2|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|RESERVED||||
|R-0h||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|pma_reset_2|R|0h|1 = PMA/PMD reset 0 = Normal operation Note - RW bit, self clearing|
|14-12|RESERVED|R|0h|Reserved|
|11|RESERVED|R|0h|Reserved|
|10-0|RESERVED|R|0h|Reserved|



142 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.83 PMA_PMD_CONTROL_2 Register (Offset = 1007h) [Reset = 003Dh] ** PMA_PMD_CONTROL_2 is shown in Figure 6-102 and described in Table 6-107. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-107. PMA _ PMD _ CONTROL _ 2 Re g ister Field Descri p tions**

|Figure 6-102. PMA_PMD_CONTROL_2 Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|RESERVED||
|R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED|cfg_pma_type_selection|
|R-0h R/W-3Dh||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-6|RESERVED|R|0h|Reserved|
|5-0|cfg_pma_type_selection|R/W|3Dh|BASE-T1 type selection for device 3Dh = BASE-T1 type selection for device|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 143

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.84 PMA_PMD_TRANSMIT_DISABLE Register (Offset = 1009h) [Reset = 0000h] ** PMA_PMD_TRANSMIT_DISABLE is shown in Figure 6-103 and described in Table 6-108. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-108. PMA _ PMD _ TRANSMIT _ DISABLE Re g ister Field Descri p tions**

|Figure 6-103. PMA_PMD_TRANSMIT_DISABLE Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|RESERVED||
|R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED|cfg_transmit_di sable_2|
|R-0h R-0h||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-1|RESERVED|R|0h|Reserved|
|0|cfg_transmit_disable_2|R|0h|1 = Transmit disable 0 = Normal operation Note - RW bit|



144 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.85 PMA_PMD_EXTENDED_ABILITY2 Register (Offset = 100Bh) [Reset = 0800h] ** PMA_PMD_EXTENDED_ABILITY2 is shown in Figure 6-104 and described in Table 6-109. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-109. PMA _ PMD _ EXTENDED _ ABILITY2 Re g ister Field Descri p tions**

|Figure 6-104. PMA_PMD_EXTENDED_ABILITY2 Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|base_t1_extend ed_abilities|RESERVED|
|R-0h R-1h R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|||
|R-0h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-12|RESERVED|R|0h|Reserved|
|11|base_t1_extended_abilitie s|R|1h|1 = PMA/PMD has BASE-T1 extended abilities listed in register 1.18 0 = PMA/PMD does not have BASE-T1 extended abilities|
|10-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 145

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.86 PMA_PMD_EXTENDED_ABILITY Register (Offset = 1012h) [Reset = 0002h] ** PMA_PMD_EXTENDED_ABILITY is shown in Figure 6-105 and described in Table 6-110. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-110. PMA _ PMD _ EXTENDED _ ABILITY Re g ister Field Descri p tions**

|Figure 6-105. PMA_PMD_EXTENDED_ABILITY Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|RESERVED|||
|R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|mr_1000_base_ t1_ability|mr_100_base_t 1_ability|
|R-0h R-1h R-0h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-2|RESERVED|R|0h|Reserved|
|1|mr_1000_base_t1_ability|R|1h|1 = PMA/PMD is able to perform 1000BASE-T1 0 = PMA/PMD is not able to perform 1000BASE-T1|
|0|mr_100_base_t1_ability|R|0h|1 = PMA/PMD is able to perform 100BASE-T1 0 = PMA/PMD is not able to perform 100BASE-T1|



146 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.87 PMA_PMD_CONTROL Register (Offset = 1834h) [Reset = 8001h] ** PMA_PMD_CONTROL is shown in Figure 6-106 and described in Table 6-111. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-111. PMA _ PMD _ CONTROL Re g ister Field Descri p tions**

|Figure 6-106. PMA_PMD_CONTROL Register|Col2|Col3|Col4|
|---|---|---|---|
|15 14 13 12 11 10 9 8||||
|RESERVED|cfg_master_sla ve_val|RESERVED||
|R-0h R/W-0h R-0h||||
|7 6 5 4 3 2 1 0||||
|RESERVED|||RESERVED|
|R-0h R-0h||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|RESERVED|R|0h|Reserved|
|14|cfg_master_slave_val|R/W|0h|1 = Configure PHY as MASTER 0 = Configure PHY as SLAVE|
|13-4|RESERVED|R|0h|Reserved|
|3-0|RESERVED|R|0h|Reserved|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 147

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.88 PMA_CONTROL Register (Offset = 1900h) [Reset = 0000h] ** PMA_CONTROL is shown in Figure 6-107 and described in Table 6-112. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-112. PMA _ CONTROL Re g ister Field Descri p tions**

|Figure 6-107. PMA_CONTROL Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|pma_reset|cfg_transmit_di sable|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED|||||
|R-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|pma_reset|R|0h|1 = PMA/PMD reset 0 = Normal operation Note - RW bit, self clearing|
|14|cfg_transmit_disable|R|0h|1 = Transmit disable 0 = Normal operation Note - RW bit|
|13-12|RESERVED|R|0h|Reserved|
|11|RESERVED|R|0h|Reserved|
|10-0|RESERVED|R|0h|Reserved|



148 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.89 PMA_STATUS Register (Offset = 1901h) [Reset = 0900h] ** PMA_STATUS is shown in Figure 6-108 and described in Table 6-113. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-113. PMA _ STATUS Re g ister Field Descri p tions**

|Figure 6-108. PMA_STATUS Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED|oam_ability|eee_ability|receive_fault_a bility|low_power_abili ty|
|R-0h R-1h R-0h R-0h R-1h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED||receive_polarity|receive_fault|pma_receive_li nk_status_ll|
|R-0h R-0h R-0h R/W0S-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-12|RESERVED|R|0h|Reserved|
|11|oam_ability|R|1h|1 = PHY has 1000BASE-T1 OAM ability 0 = PHY does not have 1000BASE-T1 OAM ability|
|10|eee_ability|R|0h|1 = PHY has EEE ability 0 = PHY does not have EEE ability|
|9|receive_fault_ability|R|0h|1 = PMA/PMD has the ability to detect a fault condition on the receive path 0 = PMA/PMD does not have the ability to detect a fault condition on the receive path|
|8|low_power_ability|R|1h|1 = PMA/PMD has low-power ability 0 = PMA/PMD does not have low-power ability|
|7-3|RESERVED|R|0h|Reserved|
|2|receive_polarity|R|0h|1 = Receive polarity is reversed 0 = Receive polarity is not reversed|
|1|receive_fault|R|0h|1 = Fault condition detected 0 = Fault condition not detected|
|0|pma_receive_link_status_l l|R/W0S|0h|1 = PMA/PMD receive link up 0 = PMA/PMD receive link down|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 149

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.90 TRAINING Register (Offset = 1902h) [Reset = 0002h] ** TRAINING is shown in Figure 6-109 and described in Table 6-114. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-114. TRAINING Re g ister Field Descri p tions**

|Figure 6-109. TRAINING Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED||cfg_training_user_fld|||
|R-0h R/W-0h|||||
|7 6 5 4 3 2 1 0|||||
|cfg_training_user_fld|RESERVED||cfg_oam_en|cfg_eee_en|
|R/W-0h R-0h R/W-1h R/W-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10-4|cfg_training_user_fld|R/W|0h|7-bit user defined field to send to the link partner|
|3-2|RESERVED|R|0h|Reserved|
|1|cfg_oam_en|R/W|1h|1 = 1000BASE-T1 OAM ability advertised to link partner 0 = 1000BASE-T1 OAM ability not advertised to link partner|
|0|cfg_eee_en|R/W|0h|1 = EEE ability advertised to link partner 0 = EEE ability not advertised to link partner|



150 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.91 LP_TRAINING Register (Offset = 1903h) [Reset = 0000h] ** LP_TRAINING is shown in Figure 6-110 and described in Table 6-115. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-115. LP _ TRAINING Re g ister Field Descri p tions**

|Figure 6-110. LP_TRAINING Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|RESERVED||lp_training_user_fld|||
|R-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|lp_training_user_fld|RESERVED||lp_oam_adv|lp_eee_adv|
|R-0h R-0h R-0h R-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10-4|lp_training_user_fld|R|0h|7-bit user defined field received from the link partner|
|3-2|RESERVED|R|0h|Reserved|
|1|lp_oam_adv|R|0h|1 = Link partner has 1000BASE-T1 OAM ability 0 = Link partner does not have 1000BASE-T1 OAM ability|
|0|lp_eee_adv|R|0h|1 = Link partner has EEE ability 0 = Link partner does not have EEE ability|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 151

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.92 TEST_MODE_CONTROL Register (Offset = 1904h) [Reset = 0000h] ** TEST_MODE_CONTROL is shown in Figure 6-111 and described in Table 6-116. Return to the Summary Table. First nibble (0x1) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-116. TEST _ MODE _ CONTROL Re g ister Field Descri p tions**

|Figure 6-111. TEST_MODE_CONTROL Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|cfg_test_mode|RESERVED|
|R/W-0h R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED||
|R-0h||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-13|cfg_test_mode|R/W|0h|111 = Test mode 7 110 = Test mode 6 101 = Test mode 5 100 = Test mode 4 011 = Reserved 010 = Test mode 2 001 = Test mode 1 000 = Normal (non-test) operation|
|12-0|RESERVED|R|0h|Reserved|



152 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.93 PCS_CONTROL Register (Offset = 3900h) [Reset = 0000h] ** PCS_CONTROL is shown in Figure 6-112 and described in Table 6-117. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-117. PCS _ CONTROL Re g ister Field Descri p tions**

|Figure 6-112. PCS_CONTROL Register|Col2|Col3|
|---|---|---|
|15 14 13 12 11 10 9 8|||
|pcs_reset|RESERVED|RESERVED|
|R-0h R-0h R-0h|||
|7 6 5 4 3 2 1 0|||
|RESERVED|||
|R-0h|||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|pcs_reset|R|0h|Note - RW bit, self clear bit 0h = Normal operation 1h = PCS reset|
|14|RESERVED|R|0h|Reserved|
|13-0|RESERVED|R|0h|Reserved|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 153

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.94 PCS_STATUS Register (Offset = 3901h) [Reset = 0000h] ** PCS_STATUS is shown in Figure 6-113 and described in Table 6-118. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-118. PCS _ STATUS Re g ister Field Descri p tions**

|Figure 6-113. PCS_STATUS Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED||RESERVED|RESERVED|RESERVED|RESERVED|
|R-0h R-0h R-0h R-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|pcs_fault|RESERVED||pcs_receive_lin k_status_ll|RESERVED||
|R-0h R-0h R/W0S-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-12|RESERVED|R|0h|Reserved|
|11|RESERVED|R|0h|Reserved|
|10|RESERVED|R|0h|Reserved|
|9|RESERVED|R|0h|Reserved|
|8|RESERVED|R|0h|Reserved|
|7|pcs_fault|R|0h|0h = No fault condition detected 1h = Fault condition detected|
|6-3|RESERVED|R|0h|Reserved|
|2|pcs_receive_link_status_ll|R/W0S|0h|0h = PCS receive link down 1h = PCS receive link up|
|1-0|RESERVED|R|0h|Reserved|



154 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.95 PCS_STATUS_2 Register (Offset = 3902h) [Reset = 0000h] ** PCS_STATUS_2 is shown in Figure 6-114 and described in Table 6-119. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-119. PCS _ STATUS _ 2 Re g ister Field Descri p tions**

|Figure 6-114. PCS_STATUS_2 Register|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8||||||
|RESERVED|||pcs_receive_lin k_status|hi_rfer|block_lock|
|R-0h R-0h R-0h R-0h||||||
|7 6 5 4 3 2 1 0||||||
|hi_rfer_lh|block_lock_ll|RESERVED||||
|R/W0C-0h R/W0S-0h R-0h||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-11|RESERVED|R|0h|Reserved|
|10|pcs_receive_link_status|R|0h|0h = PCS receive link down 1h = PCS receive link up|
|9|hi_rfer|R|0h|0h = PCS not reporting a high BER 1h = PCS reporting a high BER|
|8|block_lock|R|0h|0h = PCS not locked to received blocks 1h = PCS locked to received blocks|
|7|hi_rfer_lh|R/W0C|0h|0h = PCS has not reported a high BER 1h = PCS has reported a high BER|
|6|block_lock_ll|R/W0S|0h|0h = PCS does not have block lock 1h = PCS has block lock|
|5-0|RESERVED|R|0h|Reserved|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 155

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.96 OAM_TRANSMIT Register (Offset = 3904h) [Reset = 0000h] ** OAM_TRANSMIT is shown in Figure 6-115 and described in Table 6-120. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-120. OAM _ TRANSMIT Re g ister Field Descri p tions**

|Figure 6-115. OAM_TRANSMIT Register|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||||
|mr_tx_valid|mr_tx_toggle|mr_tx_received|mr_tx_received _toggle|mr_tx_message_num|||
|R/WMC,0-0h R-0h R-0h R-0h R/W-0h|||||||
|7 6 5 4 3 2 1 0|||||||
|RESERVED||||mr_rx_ping|mr_tx_ping|mr_tx_snr|
|R-0h R-0h R/W-0h R-0h|||||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|mr_tx_valid|R/WMC,0|0h|This bit is used to indicate message data in registers 3.2308.11:8, 3.2309, 3.2310, 3.2311, and 3.2312 are valid and ready to be loaded. This bit shall self-clear when registers are loaded by the state machine. 1 = Message data in registers are valid 0 = Message data in registers are not valid|
|14|mr_tx_toggle|R|0h|Toggle value to be transmitted with message. This bit is set by the state machine and cannot be overridden by the user.|
|13|mr_tx_received|R|0h|This bit shall self clear on read. 1 = 1000BASE-T1 OAM message received by link partner 0 = 1000BASE-T1 OAM message not received by link partner|
|12|mr_tx_received_toggle|R|0h|Toggle value of message that was received by link partner|
|11-8|mr_tx_message_num|R/W|0h|User-defined message number to send|
|7-4|RESERVED|R|0h|Reserved|
|3|mr_rx_ping|R|0h|Received PingTx value from latest good 1000BASE-T1 OAM frame received|
|2|mr_tx_ping|R/W|0h|Ping value to send to link partner|
|1-0|mr_tx_snr|R|0h|00 = PHY link is failing and shall drop link and relink within 2ms to 4ms after the end of the current 1000BASE-T1 OAM frame. 01 = LPI refresh is insufficient to maintain PHY SNR. Request link partner to exit LPI and send idles (used only when EEE is enabled). 10 = PHY SNR is marginal. 11 = PHY SNR is good.|



156 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.97 OAM_TX_MESSAGE_1 Register (Offset = 3905h) [Reset = 0000h] ** OAM_TX_MESSAGE_1 is shown in Figure 6-116 and described in Table 6-121. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-116. OAM _ TX _ MESSAGE _ 1 Re g ister**

15 14 13 12 11 10 9 8

mr_tx_message_15_0

R/W-0h


7 6 5 4 3 2 1 0


mr_tx_message_15_0

R/W-0h
###### **Table 6-121. OAM _ TX _ MESSAGE _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_tx_message_15_0|R/W|0h|Message octet 1/0. LSB transmitted first.|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 157

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.98 OAM_TX_MESSAGE_2 Register (Offset = 3906h) [Reset = 0000h] ** OAM_TX_MESSAGE_2 is shown in Figure 6-117 and described in Table 6-122. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-117. OAM _ TX _ MESSAGE _ 2 Re g ister**

15 14 13 12 11 10 9 8

mr_tx_message_31_16

R/W-0h


7 6 5 4 3 2 1 0


mr_tx_message_31_16

R/W-0h
###### **Table 6-122. OAM _ TX _ MESSAGE _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_tx_message_31_16|R/W|0h|Message octet 3/2. LSB transmitted first.|



158 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.99 OAM_TX_MESSAGE_3 Register (Offset = 3907h) [Reset = 0000h] ** OAM_TX_MESSAGE_3 is shown in Figure 6-118 and described in Table 6-123. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-118. OAM _ TX _ MESSAGE _ 3 Re g ister**

15 14 13 12 11 10 9 8

mr_tx_message_47_32

R/W-0h


7 6 5 4 3 2 1 0


mr_tx_message_47_32

R/W-0h
###### **Table 6-123. OAM _ TX _ MESSAGE _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_tx_message_47_32|R/W|0h|Message octet 5/4. LSB transmitted first.|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 159

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.100 OAM_TX_MESSAGE_4 Register (Offset = 3908h) [Reset = 0000h] ** OAM_TX_MESSAGE_4 is shown in Figure 6-119 and described in Table 6-124. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-119. OAM _ TX _ MESSAGE _ 4 Re g ister**

15 14 13 12 11 10 9 8

mr_tx_message_63_48

R/W-0h


7 6 5 4 3 2 1 0


mr_tx_message_63_48

R/W-0h
###### **Table 6-124. OAM _ TX _ MESSAGE _ 4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_tx_message_63_48|R/W|0h|Message octet 7/6. LSB transmitted first.|



160 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **6.6.2.101 OAM_RECEIVE Register (Offset = 3909h) [Reset = 0000h] ** OAM_RECEIVE is shown in Figure 6-120 and described in Table 6-125. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-125. OAM _ RECEIVE Re g ister Field Descri p tions**

|Figure 6-120. OAM_RECEIVE Register|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|15 14 13 12 11 10 9 8|||||
|mr_rx_lp_valid|mr_rx_lp_toggle|RESERVED|mr_rx_lp_message_num||
|R-0h R-0h R-0h R-0h|||||
|7 6 5 4 3 2 1 0|||||
|RESERVED||||mr_rx_lp_SNR|
|R-0h R-0h|||||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15|mr_rx_lp_valid|R|0h|This bit is used to indicate message data in registers 3.2313.11:8, 3.2314, 3.2315, 3.2316, and 3.2317 are stored and ready to be read. This bit shall self clear when register 3.2317 is read. 0h = Message data in registers are not valid 1h = Message data in registers are valid|
|14|mr_rx_lp_toggle|R|0h|Toggle value received with message Note - 0x3 added in [15:12] to differentiate|
|13-12|RESERVED|R|0h|Reserved|
|11-8|mr_rx_lp_message_num|R|0h|Message number from link partner Note - 0x3 added in [15:12] to differentiate|
|7-2|RESERVED|R|0h|Reserved|
|1-0|mr_rx_lp_SNR|R|0h|00 = Link partner link is failing and shall drop link and relink within 2ms to 4ms after the end of the current 1000BASE-T1 OAM frame. 01 = LPI refresh is insufficient to maintain link partner SNR. Link partner requests local device to exit LPI and send idles (used only when EEE is enabled). 10 = Link partner SNR is marginal. 11 = Link partner SNR is good|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 161

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.102 OAM_RX_MESSAGE_1 Register (Offset = 390Ah) [Reset = 0000h] ** OAM_RX_MESSAGE_1 is shown in Figure 6-121 and described in Table 6-126. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-121. OAM _ RX _ MESSAGE _ 1 Re g ister**

15 14 13 12 11 10 9 8

mr_rx_lp_message_15_0

R-0h


7 6 5 4 3 2 1 0


mr_rx_lp_message_15_0

R-0h
###### **Table 6-126. OAM _ RX _ MESSAGE _ 1 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_rx_lp_message_15_0|R|0h|Message octet 1/0. LSB transmitted first.|



162 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.103 OAM_RX_MESSAGE_2 Register (Offset = 390Bh) [Reset = 0000h] ** OAM_RX_MESSAGE_2 is shown in Figure 6-122 and described in Table 6-127. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-122. OAM _ RX _ MESSAGE _ 2 Re g ister**

15 14 13 12 11 10 9 8

mr_rx_lp_message_31_16

R-0h


7 6 5 4 3 2 1 0


mr_rx_lp_message_31_16

R-0h
###### **Table 6-127. OAM _ RX _ MESSAGE _ 2 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_rx_lp_message_31_16|R|0h|Message octet 3/2. LSB transmitted first.|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 163

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.104 OAM_RX_MESSAGE_3 Register (Offset = 390Ch) [Reset = 0000h] ** OAM_RX_MESSAGE_3 is shown in Figure 6-123 and described in Table 6-128. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-123. OAM _ RX _ MESSAGE _ 3 Re g ister**

15 14 13 12 11 10 9 8

mr_rx_lp_message_47_32

R-0h


7 6 5 4 3 2 1 0


mr_rx_lp_message_47_32

R-0h
###### **Table 6-128. OAM _ RX _ MESSAGE _ 3 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_rx_lp_message_47_32|R|0h|Message octet 5/4. LSB transmitted first.|



164 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **6.6.2.105 OAM_RX_MESSAGE_4 Register (Offset = 390Dh) [Reset = 0000h] ** OAM_RX_MESSAGE_4 is shown in Figure 6-124 and described in Table 6-129. Return to the Summary Table. First nibble (0x3) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Fi g ure 6-124. OAM _ RX _ MESSAGE _ 4 Re g ister**

15 14 13 12 11 10 9 8

mr_rx_lp_message_63_48

R-0h


7 6 5 4 3 2 1 0


mr_rx_lp_message_63_48

R-0h
###### **Table 6-129. OAM _ RX _ MESSAGE _ 4 Re g ister Field Descri p tions**

|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-0|mr_rx_lp_message_63_48|R|0h|Message octet 7/6. LSB transmitted first.|



Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 165

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **6.6.2.106 AN_CFG Register (Offset = 7200h) [Reset = 0000h] ** AN_CFG is shown in Figure 6-125 and described in Table 6-130. Return to the Summary Table. First nibble (0x7) in the register address is to indicate MMD register space. For register access, ignore the first nibble. **Table 6-130. AN _ CFG Re g ister Field Descri p tions**

|Figure 6-125. AN_CFG Register|Col2|
|---|---|
|15 14 13 12 11 10 9 8||
|RESERVED||
|R-0h||
|7 6 5 4 3 2 1 0||
|RESERVED|mr_main_reset|
|R-0h R/WSC-0h||


|Bit|Field|Type|Reset|Description|
|---|---|---|---|---|
|15-1|RESERVED|R|0h|Reserved|
|0|mr_main_reset|R/WSC|0h|1 = Reset link sync/autoneg Note - RW bit|



166 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**
###### **7 Application and Implementation**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### **Note** Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality. **7.1 Application Information** The DP83TG720S-Q1 is a single-port 1-Gbps Automotive Ethernet PHY. It supports IEEE 802.3bp and allows for connections to an Ethernet MAC through RGMII or SGMII. When using the device for Ethernet applications, it is necessary to meet certain requirements for normal operation. The following subsections are intended to assist in appropriate component selection and required connections. **7.2 Typical Applications**

|Col1|Col2|
|---|---|
||ESD|
||| **Figure 7-1. Typical Application (SGMII)** **Table 7-1. Recommended Com p onents for MDI Network**

|Media Access Controller|0.1 µF 0.1 µF 0.1 µF 0.1 µF VDDIO|TX_P TX_M TRD_P RX_P TRD_M RX_M DP83TG720S-Q1 MDIO MDC WAKE INT|DC CMC Blocking Automotive ESD Connector (optional) CM Termination MDI ESD Coupling Shunt GND|
|---|---|---|---| 1. 1% tolerance components are recommended for margins over spec of return loss and mode conversion. 2. CM termination resistor's size higher than 0805 helps in increasing ESD margin. **7.3 Power Supply Recommendations**

|Design Parameter|Value|
|---|---|
|DC Blocking Capacitors 1|0.1μF|
|Common-Mode Choke|Murata :DLW32MH101XT2|
|Common Mode Termination Resistors 1 2|1kΩ|
|MDI Coupling Capacitor|4.7nF|
|ESD Shunt|100kΩ| The DP83TG720S-Q1 is capable of operating with a wide range of IO supply voltages (3.3V, 2.5V, or 1.8V). No power supply sequencing is required. The recommended power supply de-coupling network is shown in following figure :

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 167

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)**

|Pins|Phy[s Supply BOM|Col3|Board-supply min decap|
|---|---|---|---|
|34 22 21 9 11 7|10nF 100nF Ferrite 10nF 100nF >= 2.2uF 10nF 100nF >= 2.2uF Ferrite 10nF 100nF >= 2.2uF Ferrite||= vddio >=1uF vdd1p0 >=1uF vdda3p3 >=1uF vsleep >=1uF|
|||||
|||||
||10nF 100nF >= 2.2uF|||
||||| **Figure 7-2. Recommended Supply De-Coupling Network (if sleep mode is used in the application)**

168 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

|Pins|Phy[s Supply BOM|Col3|Board-supply  min decap|
|---|---|---|---|
|34 22 21 9 11 7|10nF 100nF Ferrite 10nF 100nF >= 2.2uF 10nF 100nF >= 2.2uF Ferrite 10nF 100nF >= 2.2uF Ferrite||= vddio >=1uF vdd1p0 >=1uF vdda3p3 >=1uF|
|||||
|||||
||10nF 100nF >= 2.2uF|||

###### **Figure 7-3. Recommended Supply De-Coupling Network (if sleep mode is not used in application)** **Table 7-2. Recommended Com p onents for Power Network**

|Design Parameter|Value|
|---|---|
|V DDIO|1.8V, 2.5V, or 3.3V|
|De-Coupling Capacitors V (pin 34) DDIO|10nF, 100nF|
|De-Coupling Capacitors V (pin 22) DDIO|10nF, 100nF, 2.2uF|
|Combined Ferrite Bead for VDDIO|BLM18HE102SN1|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 169

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **Table 7-2. Recommended Com p onents for Power Network ( continued )** **Note** For recommendation on LDOs for VDD1p0 and Vsleep, please refer to the DP83TC811, DP83TG730 Rollover Document application report. **7.4 Compatibility with TI's 100BT1 PHY **

|Design Parameter|Value|
|---|---|
|V DDA|3.3V|
|De-Coupling Capacitors V (pin 11) DDA|10nF, 100nF, 2.2uF|
|Ferrite Bead for V DDA|BLM18KG601SH1|
|V DD1p0|1V|
|De-Coupling Capacitors V (pin 9) DD1P0|10nF, 100nF, 2.2uF|
|De-Coupling Capacitors V (pin 21) DDA|10nF, 100nF, 2.2uF|
|Combined Ferrite Bead for V DD1P0|BLM18KG601SH1|
|V sleep|3.3V| Following table shows pin comparison between DP83TC811 and DP83TG720. Pins highlighted in bold need attention while designing a common board for both 100BT1 and 1000BT1 PHY. 100BT1 and 1000BT1 PHY's different BOM requirements can also be taken care by a common board. Details and recommendation for common board design can be found in DP83TC811, DP83TG720 Rollover Document application report. **Table 7-3. Pin Com p arison Table**

|Pin No.|DP83TC811|DP83TG720|
|---|---|---|
|1|MDC|MDC|
|2|INT_N|INT_N|
|3|RESET_N|RESET_N|
|4|XO|XO|
|5|XI|XI|
|6|LED_1|LED_1|
|7|EN|VSLEEP|
|8|WAKE|WAKE|
|9|DNC|VDD1P0|
|10|INH|INH|
|11|VDDA|VDDA|
|12|TRD_P|TRD_P|
|13|TRD_M|TRD_M|
|14|RX_ER|STRP1|
|15|RX_DV|RX_CTRL|
|16|CLKOUT|CLKOUT|
|17|TCK|DNC|
|18|TDO|DNC|
|19|TMS|DNC|
|20|TCK|DNC|
|21|DNC|VDD1P0|
|22|VDDIO|VDDIO|
|23|RX_D3|RX_D3|
|24|RX_D2|RX_D2|



170 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Table 7-3. Pin Com p arison Table ( continued )** **7.5 Layout**

|Pin No.|DP83TC811|DP83TG720|
|---|---|---|
|25|RX_D1|RX_D1|
|26|RX_D0|RX_D0|
|27|RX_CLK|RX_CLK|
|28|TXCLK|TXCLK|
|29|TX_EN|TX_CTRL|
|30|TX_D3|TX_D3|
|31|TX_D2|TX_D2|
|32|TX_D1|TX_D1|
|33|TX_D0|TX_D0|
|34|TX_ER|VDDIO|
|35|LED_0|LED_0|
|36|MDIO|MDIO| ***7.5.1 Layout Guidelines*** **7.5.1.1 Signal Traces** PCB traces are lossy and long traces can degrade signal quality. Traces must be kept short as possible. Unless mentioned otherwise, all signal traces must be 50Ω, single-ended impedance. Differential traces must be 50Ω single-ended and 100Ω differential. Impedance discontinuities cause reflections leading to emissions and signal integrity issues. Stubs must be avoided on all signal traces, especially differential signal pairs. **Figure 7-4. Differential Signal Trace Routing** Within the differential pairs, trace lengths must be run parallel to each other and matched in length. Matched lengths minimize delay differences, avoiding an increase in common mode noise and emissions. Length matching is also important for MAC interface connections. All transmit signal traces must be length matched to each other and all receive signal traces must be length matched to each other. Avoid crossover or vias on signal path traces. Vias present impedance discontinuities and be minimized when possible. Route trace pairs on the same layer. Avoid signals on different layers crossing each other without at least one return path plane between them. Differential pairs must always have a constant coupling

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 171

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** distance between them. For convenience and efficiency, TI recommends routing critical signals first (that is, MDI differential pairs, reference clock, and MAC IF traces). **7.5.1.2 Return Path** A general best practice is to have a solid return path beneath all signal traces. This return path can be a continuous ground or DC power plane. Reducing the width of the return path can potentially affect the impedance of the signal trace. This effect is more prominent when the width of the return path is comparable to the width of the signal trace. Breaks in return path between the signal traces must be avoided. A signal crossing a split plane causes unpredictable return path currents and impacts signal quality and result in emissions issues. **Figure 7-5. Power and Ground Plane Breaks** **7.5.1.3 Physical Medium Attachment** There must be no metal running beneath the common-mode choke. CMCs can inject noise into metal beneath them, which can affect the emissions and immunity performance of the system. Because the DP83TG720S-Q1 is a voltage mode line driver, no external termination resistors are required. The ESD shunt and MDI coupling capacitor must be connected to ground. Select common mode termination resistors that are 1% tolerance or better to improve differential coupling. **7.5.1.4 Metal Pour** All metal pours that are not signals or power must be tied to ground. There must be no floating metal in the system, and there must be no metal between differential traces. **7.5.1.5 PCB Layer Stacking** To meet signal integrity and performance requirements, minimum four-layer PCB is recommended. However, a six-layer PCB and above should be used when possible.

172 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **Figure 7-6. Recommended PCB Layer Stack-Up**


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 173

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **8 Device and Documentation Support** **Note** TI is transitioning to use more inclusive terminology. Some language may be different than what you would expect to see for certain technology areas. **8.1 Receiving Notification of Documentation Updates** To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Notifications to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document. **8.2 Support Resources** TI E2E [™] support forums are an engineer's go-to source for fast, verified answers and design help — straight from the experts. Search existing answers or ask your own question to get the quick design help you need. Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use. **8.3 Trademarks** TI E2E [™] is a trademark of Texas Instruments. All trademarks are the property of their respective owners. **8.4 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications. **8.5 Glossary** TI Glossary This glossary lists and explains terms, acronyms, and definitions. **9 Revision History** NOTE: Page numbers for previous revisions may differ from page numbers in the current version. **Changes from Revision E (February 2022 ) to Revision F (April 2025) Page** • Changed the order of register 0x619 and 0x624 writes .................................................................................. 31 • Changed the parameter 'slope_temperature_sensor'.......................................................................................34 • Added a statement that Auto-Polarity Correction can't be disabled on DP83TG720-Q1................................. 44 • Simplified the description of Serial Management Interface for ease of readability........................................... 50 • Changed LED_0 pin number from 1 to 35 in Table 7-18.................................................................................. 53 • Removed unused register fields from the register map....................................................................................57 **Chan g es from Revision D ( March 2021) to Revision E (February 2022) Page** • Updated the title of document.........................................................................................................................0 • Updated the Strap_1 pin state in the Pin Function table to input only. Separated the Pin states table and Pin Power domain tables.......................................................................................................................................... 4 • Updated the INH pin in power/reset to PMOS, OD, O in the Pin States table. Updated abbreviations............. 6 • Added the Pin Power Domain Table...................................................................................................................9 • SQI section updated to indicate improved number of SQI levels with updated computation method.............. 26 • Updated the link for the TDR application note..................................................................................................26

174 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)

###### • Changed the 0x0016 register value to 0x0108, 0x0104, 0x0101 for analog loopback, digital loopback, and PCS loopback...................................................................................................................................................31 • Updated the step of local and remote sleep entry............................................................................................41 • Updated the CM resistor packaging recommendation 0805.......................................................................... 167 **Changes from Revision C ( February 2021) to Revision D (March 2021) Page** • IOZ, 2 level boot-strap's Mode 2 threshold and Rpull-down min/max data sheet limits updated to give more margin to customer application.........................................................................................................................10 • Min/Max values of rgmii DLL_TX_DELAY, sleep mode timing parameters, latency parameters, reset mode power, standby mode power and sleep mode power added ........................................................................... 10 • Changed Integrated Pull-Down Resistance from 4.5kΩ to 4.725kΩ................................................................ 10 • Correction in registers to be used for enabling sleep mode entry.................................................................... 41 • Further details added to remote sleep exit procedure...................................................................................... 41 • Note added for more margins for 1.8V two level straps................................................................................... 53 **Chan g es from Revision B ( Februar y 2021) to Revision C (February 2021) Page** • Updated the Pull-down resistor value of rx_cntrl and strp_1 pins in pin-state tables. Changed from 6 K to 6.3 K to match exact value in the Specifications section .........................................................................................4 • SQI section updated to meet OA requirements................................................................................................26 • Strap circuit diagram updated to remove external pull-down........................................................................... 53 **Chan g es from Revision A ( December 2020) to Revision B (December 2020) Page** • Updated Power Supply Recommendation Note............................................................................................. 167 **Chan g es from Revision * ( September 2020) to Revision A (December 2020) Page** • Changed marketing status from Advance Information to initial release............................................................. 1

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 175

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)** **10 Mechanical, Packaging, and Orderable Information** The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left navigation. **10.1 Package Option Addendum** ***10.1.1 Packaging Information***

(1) The marketing status values are defined as follows:
**ACTIVE:** Product device recommended for new designs.
**LIFEBUY:** TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
**NRND:** Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using
this part in a new design.
**PRE_PROD** Unannounced device, not in production, not available for mass market, nor on the web, samples not available.
**PREVIEW:** Device has been announced but is not in production. Samples may or may not be available.
**OBSOLETE:** TI has discontinued the production of the device.

space
(2) Eco Plan - The planned eco-friendly classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS & no Sb/Br) - please
[check http://www.ti.com/productcontent for the latest availability information and additional product content details.](http://www.ti.com/productcontent)
**TBD:** The Pb-Free/Green conversion plan has not been defined.
**Pb-Free (RoHS):** TI's terms "Lead-Free" or "Pb-Free" mean semiconductor products that are compatible with the current RoHS
requirements for all 6 substances, including the requirement that lead not exceed 0.1% by weight in homogeneous materials. Where
designed to be soldered at high temperatures, TI Pb-Free products are suitable for use in specified lead-free processes.
**Pb-Free (RoHS Exempt):** This component has a RoHS exemption for either 1) lead-based flip-chip solder bumps used between the

|Orderable Device|Status (1)|Packag e Type|Packag e Drawing|Pins|Packag e Qty|Eco Plan (2)|Lead/Ball Finish(4)|MSL Peak Temp (3)|Op Temp (°C)|Device Marking(5) (6)|
|---|---|---|---|---|---|---|---|---|---|---|
|PDP83TG720SWCST Q1|EARLY SAMPL E|VQFN|RHA|36|250|RoHS|NiPdAu|MSL3-260C|-40 to 125||
|DP83TG720SWRHAT Q1|ACTIV E|VQFN|RHA|36|250|RoHS|NiPdAu|MSL3-260C|-40 to 125|720S|
|DP83TG720SWRHAR Q1|ACTIV E|VQFN|RHA|36|2500|RoHS|NiPdAu|MSL3-260C|-40 to 125|720S|

die and package, or 2) lead-based die adhesive used between the die and leadframe. The component is otherwise considered Pb-Free
(RoHS compatible) as defined above.
**Green (RoHS & no Sb/Br)** : TI defines "Green" to mean Pb-Free (RoHS compatible), and free of Bromine (Br) and Antimony (Sb)
based flame retardants (Br or Sb do not exceed 0.1% by weight in homogeneous material)

space
(3) MSL, Peak Temp. -- The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder
temperature.

space
(4) Lead/Ball Finish - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line.
Lead/Ball Finish values may wrap to two lines if the finish value exceeds the maximum column width.

space
(5) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device

space
(6) Multiple Device markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will
appear on a device. If a line is indented then it is a continuation of the previous line and the two combined represent the entire Device
Marking for that device.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI
bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information.
Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers
consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to
Customer on an annual basis.

176 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

**[www.ti.com](https://www.ti.com)** [SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) ***10.1.2 Tape and Reel Information***

**REEL DIMENSIONS** **TAPE DIMENSIONS**

Reel

Diameter

|Col1|A0 Cavity|
|---|---|
|A0|Dimension designed to accommodate the component width|
|B0|Dimension designed to accommodate the component length|
|K0|Dimension designed to accommodate the component thickness|
|W|Overall width of the carrier tape|
|P1|Pitch between successive cavity centers|



Reel Width (W1)

|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||W B0|
||||||||
||||||||
|vity|||A0||||



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

|Device|Package Type|Package Drawing|Pins|SPQ|Reel Diameter (mm)|Reel Width W1 (mm)|A0 (mm)|B0 (mm)|K0 (mm)|P1 (mm)|W (mm)|Pin1 Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PDP83TG720SWCSTQ 1|VQFN|RHA|36|250|Call TI|Call TI|Call TI|Call TI|Call TI|Call TI|Call TI|Call TI|
|DP83TG720SWRHATQ 1|VQFN|RHA|36|250|180|16.4|6.3|6.3|1.1|12|16|Q2|
|DP83TG720SWRHARQ 1|VQFN|RHA|36|2500|330|16.4|6.3|6.3|1.1|12|16|Q2|


Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 177

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)**

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|DP83TG720SWRHATQ1|VQFN|RHA|36|250|210|185|35|
|DP83TG720SWRHARQ1|VQFN|RHA|36|2500|367|367|35|



178 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)
##### **PACKAGE OUTLINE**

##### RHA0036A SCALE 2 . 000 VQFN - 1 mm max hei g ht

PLASTIC QUAD FLATPACK - NO LEAD

NOTES:

|Col1|0.08 C|
|---|---|


|10|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||37|A A|
|||||
|||||


|0.31 0.19|Col2|Col3|
|---|---|---|
|0.1|C A|B|
|0.05|||



1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.

www.ti.com

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 179

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604) **[www.ti.com](https://www.ti.com)**
##### **EXAMPLE BOARD LAYOUT** **RHA0036A VQFN - 1 mm max hei g ht**

PLASTIC QUAD FLATPACK - NO LEAD

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|37|||||
||||||
||||||
||||||
||||||


~~M~~ ETAL UNDER
SOLDER MASK


36X (0.6)

36X (0.25)

32X (0.5)


1


~~S~~ EE SOLDER MASK
DETAIL

27


SYMM

(R0.05) TYP

( 0.2) TYP
VIA

9

0.07 MAX
ALL AROUND

EXPOSED METAL


( 3.7)

SYMM

36 28

37

10 18

(0.625) TYP

(1.6) TYP

(5.8)

LAND PATTERN EXAMPLE

EXPOSED METAL SHOWN

SCALE: 15X

0.07 MIN
ALL AROUND

~~M~~ ETAL EDGE


~~S~~ OLDER MASK
OPENING


(1.6)
TYP

(0.625)
TYP

19


(5.8)


EXPOSED SOLDER MASK
METAL OPENING


NON SOLDER MASK
DEFINED SOLDER MASK DEFINED
(PREFERRED)

SOLDER MASK DETAILS


4225089/A 06/2019


NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.

www.ti.com

180 *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* Copyright © 2025 Texas Instruments Incorporated

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

**[www.ti.com](https://www.ti.com)**

###### **DP83TG720S-Q1**

[SNLS604F – SEPTEMBER 2020 – REVISED APRIL 2025](https://www.ti.com/lit/pdf/SNLS604)
##### **EXAMPLE STENCIL DESIGN**

##### **RHA0036A VQFN - 1 mm max hei g ht**

PLASTIC QUAD FLATPACK - NO LEAD

NOTES: (continued)

|37|Col2|Col3|Col4|
|---|---|---|---|
|||||
||37|||
|||||



6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.

www.ti.com

Copyright © 2025 Texas Instruments Incorporated *[Submit Document Feedback](https://www.ti.com/feedbackform/techdocfeedback?litnum=SNLS604F&partnum=DP83TG720S-Q1)* 181

Product Folder Links: *[DP83TG720S-Q1](https://www.ti.com/product/dp83tg720s-q1?qgpn=dp83tg720s-q1)*


-----

#### **PACKAGE OPTION ADDENDUM**

www.ti.com 14-Aug-2024
###### **PACKAGING INFORMATION**


**Orderable Device** **Status**


**Package Type Package**


**Op Temp (°C)** **Device Marking**

(4/5)



**Eco Plan**

(2)


**MSL Peak Temp**

(3)


DP83TG720SWRHARQ1 ACTIVE VQFN RHA 36 2500 RoHS & Green NIPDAU Level-3-260C-168 HR -40 to 125 720S

DP83TG720SWRHATQ1 ACTIVE VQFN RHA 36 250 RoHS & Green NIPDAU Level-3-260C-168 HR -40 to 125 720S

**(1)** The marketing status values are defined as follows:
**ACTIVE:** Product device recommended for new designs.
**LIFEBUY:** TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
**NRND:** Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
**PREVIEW:** Device has been announced but is not in production. Samples may or may not be available.
**OBSOLETE:** TI has discontinued the production of the device.

**(2)** **RoHS:** TI defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substance
do not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may
reference these types of products as "Pb-Free".
**RoHS Exempt:** TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.
**Green:** TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based
flame retardants must also meet the <=1000ppm threshold requirement.

**(3)** MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

**(4)** There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

**(5)** Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation
of the previous line and the two combined represent the entire Device Marking for that device.

**(6)** Lead finish/Ball material - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two
lines if the finish value exceeds the maximum column width.

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information
provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and
continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals.
TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 1


-----

#### **PACKAGE OPTION ADDENDUM**

www.ti.com 14-Aug-2024

Addendum-Page 2


-----

#### **PACKAGE MATERIALS INFORMATION**

www.ti.com 3-Apr-2025
###### **TAPE AND REEL INFORMATION**


**REEL DIMENSIONS**

*All dimensions are nominal


**TAPE DIMENSIONS**

Reel Width (W1)

|K0|Col2|P1|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||||W B0|
||||||||
||||||||
|vity|||A0||||


|A0|Dimension designed to accommodate the component width A0 Cavity|
|---|---|
|A0|Dimension designed to accommodate the component width|
|B0|Dimension designed to accommodate the component length|
|K0|Dimension designed to accommodate the component thickness|
|W|Overall width of the carrier tape|
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

Pack Materials-Page 1

|Device|Package Type|Package Drawing|Pins|SPQ|Reel Diameter (mm)|Reel Width W1 (mm)|A0 (mm)|B0 (mm)|K0 (mm)|P1 (mm)|W (mm)|Pin1 Quadrant|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|DP83TG720SWRHARQ1|VQFN|RHA|36|2500|330.0|16.4|6.3|6.3|1.1|12.0|16.0|Q2|
|DP83TG720SWRHATQ1|VQFN|RHA|36|250|180.0|16.4|6.3|6.3|1.1|12.0|16.0|Q2|


-----

#### **PACKAGE MATERIALS INFORMATION**

www.ti.com 3-Apr-2025

*All dimensions are nominal

Pack Materials-Page 2

|Device|Package Type|Package Drawing|Pins|SPQ|Length (mm)|Width (mm)|Height (mm)|
|---|---|---|---|---|---|---|---|
|DP83TG720SWRHARQ1|VQFN|RHA|36|2500|367.0|367.0|35.0|
|DP83TG720SWRHATQ1|VQFN|RHA|36|250|210.0|185.0|35.0|


-----

### **GENERIC PACKAGE VIEW**
## **RHA 36 VQFN - 1 mm max hei g ht**
###### 6 x 6, 0.5 mm pitch PLASTIC QUAD FLATPACK - NO LEAD This image is a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

4228438/A www.ti.com


-----

### **PACKAGE OUTLINE**
## **RHA0036A VQFN - 1 mm max hei g ht**

~~SCALE~~ ~~2~~ . ~~000~~

PLASTIC QUAD FLATPACK - NO LEAD

NOTES:

|Col1|0.08 C|
|---|---|


|0.31 0.19|Col2|Col3|Col4|
|---|---|---|---|
|0.1|C|A|B|
|0.05||||


1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
###### www.ti.com


-----

### **EXAMPLE BOARD LAYOUT**
## **RHA0036A VQFN - 1 mm max hei g ht**

PLASTIC QUAD FLATPACK - NO LEAD

NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.
###### www.ti.com


-----

### **EXAMPLE STENCIL DESIGN**
## **RHA0036A VQFN - 1 mm max hei g ht**

PLASTIC QUAD FLATPACK - NO LEAD

NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
###### www.ti.com


-----

###### **IMPORTANT NOTICE AND DISCLAIMER**

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


-----

