### ~~**VSC8514-11 Datasheet**~~
# **Quad-Port 10/100/1000BASE-T PHY with QSGMII MAC VSC8514-11**

### **_Quad-Port 10/100/1000BASE-T PHY with_** **_QSGMII MAC_**


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 ii


## **Table of Contents**

1 Product Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1


1.1 Key Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1

1.2 Block Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


2 Functional Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4


2.1 SerDes MAC Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 PHY Addressing and Port Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.3 Cat5 Twisted Pair Media Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2.4 Reference Clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.5 Ethernet Inline-Powered Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.6 IEEE 802.3af Power Over Ethernet Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.7 ActiPHY Power Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.8 Serial Management Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

2.9 LED Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

2.10 GPIO Pins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

2.11 Testing Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

2.12 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24


3 Registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


3.1 Register and Bit Conventions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

3.2 IEEE 802.3 and Main Registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

3.3 Extended Page 1 Registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

3.4 Extended Page 2 Registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

3.5 Extended Page 3 Registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

3.6 General Purpose Registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

3.7 Clause 45 Registers to Support Energy Efficient Ethernet and 802.3bf . . . . . . . . . . . . . . . . . . . . . . . . 62


4 Electrical Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65


4.1 DC Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

4.2 AC Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

4.3 Operating Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

4.4 Stress Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75


5 Pin Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76


5.1 Pin Identifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

5.2 Pin Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

5.3 Pins by Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77


6 Package Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82


6.1 Package Drawing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82

6.2 Thermal Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

6.3 Moisture Sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84


7 Design Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85


8 Ordering Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86


**VMDS-10446** **VSC8514-11** **Datasheet** **Revision 4.0** **iii**


9 Revision History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87


9.1 Revision 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 iv


Key Features

## **1 Product Overview**


The VSC8514-11 device is a low-power Gigabit Ethernet transceiver with copper media interfaces. It has
a low electromagnetic interference (EMI) line driver, and integrated line-side termination resistors that
conserve both power and printed circuit board (PCB) space.


The VSC8514-11 device includes Microsemi’s EcoEthernet™ 2.0 technology that supports Energy
Efficient Ethernet and power saving features to reduce power based on link state and cable reach.


The VSC8514-11 device uses Microsemi’s mixed signal and digital signal processing (DSP) architecture
to ensure robust performance even under less-than-favorable environmental conditions. It supports both
half-duplex and full-duplex 10BASE-T, 100BASE-TX, and 1000BASE-T communication speeds over
Category 5 (Cat5) unshielded twisted pair (UTP) cable at distances greater than 100 m, displaying
excellent tolerance to NEXT, FEXT, echo, and other types of ambient environmental and system
electronic noise.


The following illustration shows a high-level, general view of a typical VSC8514-11 application.


_**Figure 1 •**_ **Copper Transceiver Application Diagram**


1.0 V 2.5 V


1x QSGMII


1x QSGMII 4-Port Copper Media 4× RJ-45

#### **1.1 Key Features**

|Col1|Col2|
|---|---|
|**VSC8514**<br>4-Port Copper Media<br>QSGMII<br>MAC Interface|**VSC8514**<br>4-Port Copper Media<br>QSGMII<br>MAC Interface|



This section lists the main features and benefits of the VSC8514-11 device.

##### **1.1.1 Superior PHY and Interface Technology**


           - Four integrated 10/100/1000BASE-T Ethernet copper transceivers (IEEE 802.3ab-compliant)
with VeriPHY™ cable diagnostics


           - QSGMII SerDes MAC interface


           - Patented line driver with low EMI voltage mode and integrated line side termination resistors


           - HP Auto-MDIX support and forced MDI/MDIX option


           - Jumbo frame support up to 16 kB with programmable synchronization FIFOs


           - IEEE 802.3bf register support for standardized access to information on data delay between the
MDI and xMII interface for a given PHY

##### **1.1.2 Energy Efficiency**


           - EcoEthernet™ 2.0 green energy efficiency with ActiPHY™, PerfectReach™, and IEEE 802.3az
Energy Efficient Ethernet


           - Fully optimized power consumption for all link speeds


           - Integrated LED brightness control


           - Clause 45 registers to support IEEE 802.3az Energy Efficient Ethernet and IEEE 802.3bf


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 1


Key Features


##### **1.1.3 Key Specifications**


   - 1.0 V and 2.5 V power supplies


   - 3.3 V-tolerant 2.5 V inputs (single-ended and bi-directional TTL/CMOS I/Os)


   - Compliant with IEEE 802.3 (10BASE-T, 100BASE-TX, and 1000BASE-T)


   - QSGMII v1.3 and IEEE 1149.1 JTAG boundary scan


   - Devices support operating temperatures of –40 °C ambient to 125 °C junction or 0 °C ambient to
125 °C junction


   - Available in 12 mm x 12 mm, 138-pin, multi-row plastic QFN package


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 2


Block Diagram

#### **1.2 Block Diagram**


The following illustration shows the primary functional blocks of the VSC8514-11 device.


_**Figure 2 •**_ **Block Diagram**



P0_D[3:0]N
P0_D[3:0]P
P1_D[3:0]N
P1_D[3:0]P
P2_D[3:0]N
P2_D[3:0]P
P3_D[3:0]N
P3_D[3:0]P









TDP_0
TDN_0


RDP_0
RDN_0


COMA_MODE
NRESET

MDC

MDIO

MDINT
PHYADD[4:2]









REFCLK_P/N
REFCLK_SEL0
REFCLK_SEL1
REF_FILT_A
REF_REXT_A
SerDes_Rext_[1:0]



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 3


SerDes MAC Interface

## **2 Functional Descriptions**


This section provides detailed information about the functionality of the VSC8514-11 device, including
available configurations, operational features, and testing functionality. It includes descriptions of the
various device interfaces and their configuration. With the information in this section, the device setup
parameters can be determined for configuring the VSC8514-11 device for use in a particular application.

#### **2.1 SerDes MAC Interface**


The VSC8514-11 SerDes MAC interface performs data serialization and deserialization functions using
an integrated enhanced SerDes operating in QSGMII mode. The termination resistor is integrated into
the enhanced SerDes block in the device but does not include integrated AC decoupling capacitors.

##### **2.1.1 QSGMII MAC**


The VSC8514-11 device supports a QSGMII MAC to convey two ports of network data and port speed
between 10BASE-T, 100BASE-TX, and 1000BASE-T data rates and operates in both half-duplex and
full-duplex at all port speeds. The MAC interface protocol for each port within QSGMII can be either
1000BASE-X or SGMII, if the QSGMII MAC that the VSC8514-11 is connecting to supports this
functionality. The device also supports SGMII MAC-side autonegotiation on each individual port, enabled
through register 16E3, bit 7, of that port.


_**Figure 3 •**_ **QSGMII MAC Interface**
















|TxP<br>TxN<br>QSGMII MAC<br>RxP<br>RxN|Col2|
|---|---|
|**QSGMII MAC**<br>TxP<br>TxN<br>RxN<br>RxP||
|**QSGMII MAC**<br>TxP<br>TxN<br>RxN<br>RxP|100W|


|0.1 µF|TxP<br>PHY<br>100 Ω Port_0<br>TxN PHY QSGMII<br>Port_1<br>MUX<br>RxP PHY<br>Port_2<br>100 Ω<br>PHY<br>RxN Port_3|
|---|---|
|0.1 µF|0.1 µF|
|0.1 µF|0.1 µF|
|0.1 µF|RxN<br>100Ω|
|||


#### **2.2 PHY Addressing and Port Mapping**

The VSC8514-11 device includes three external PHY address pins, PHYADD[4:2], to allow control of
multiple PHY devices on a system board sharing a common management bus. These pins set the most
significant bits of the PHY address port map. The lower two bits of the address for each port are derived
from the physical address of the port (0 to 1) and the setting of the PHY address reversal bit in register
20E1, bit 9.


The VSC8514-11 device also includes one 5 GHz enhanced SerDes macro operating in QSGMII mode.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 4


Cat5 Twisted Pair Media Interface

#### **2.3 Cat5 Twisted Pair Media Interface**


The VSC8514-11 twisted pair interface is compliant with IEEE 802.3-2008 and the IEEE 802.3az
standard for Energy Efficient Ethernet.

##### **2.3.1 Voltage Mode Line Driver**


The VSC8514-11 device uses a patented voltage mode line driver that allows it to fully integrate the
series termination resistors, which are required to connect the PHY’s Cat5 interface to an external 1:1
transformer. Also, the interface does not require the user to place an external voltage on the center tap of
the magnetic. The following illustration shows the connections.


_**Figure 4 •**_ **Cat5 Media Interface**





|PHY Port_n|P0_D[3:0]N|Col3|Transformer|1|Col6|Col7|Col8|RJ-45<br>A+<br>A–<br>B+<br>B–<br>C+<br>C–<br>D+<br>D–|
|---|---|---|---|---|---|---|---|---|
|**PHY Portn_**|P0_D[3:0]P<br>0.1µF|P0_D[3:0]P<br>0.1µF|P0_D[3:0]P<br>0.1µF|2|2|2|2|2|
|**PHY Portn_**|P0_D[3:0]P<br>0.1µF|P0_D[3:0]P<br>0.1µF|P0_D[3:0]P<br>0.1µF||||||
|**PHY Portn_**|P1_D[3:0]N||||||3|3|
|**PHY Portn_**|P1_D[3:0]P|0.1µF|0.1µF||||6|6|
|**PHY Portn_**|P1_D[3:0]P|0.1µF|0.1µF||||||
|**PHY Portn_**|P2_D[3:0]N||||||4|4|
|**PHY Portn_**|P2_D[3:0]P|0.1µF|0.1µF||||5|5|
|**PHY Portn_**|P2_D[3:0]P|0.1µF|0.1µF||||||
|**PHY Portn_**|P3_D[3:0]N||||||7|7|
|**PHY Portn_**|P3_D[3:0]P|0.1µF|0.1µF||||8|8|
|**PHY Portn_**|P3_D[3:0]P|0.1µF|0.1µF||||||


75 Ω


75 Ω


75 Ω



1000 pF,
2 kV


##### **2.3.2 Cat5 Autonegotiation and Parallel Detection**

The VSC8514-11 supports twisted pair autonegotiation, as defined by IEEE 802.3-2008 Clause 28 and
IEEE 802.3az. The autonegotiation process evaluates the advertised capabilities of the local PHY and its
link partner to determine the best possible operating mode. In particular, autonegotiation can determine
speed, duplex configuration, and master or slave operating modes for 1000BASE-TX. Autonegotiation
also enables a connected MAC to communicate with its link partner MAC through the VSC8514-11 using
optional next pages to set attributes that may not otherwise be defined by the IEEE standard.


If the Category 5 (Cat5) link partner does not support autonegotiation, the VSC8514-11 automatically
uses parallel detection to select the appropriate link speed.


Autonegotiation is disabled by clearing register 0, bit 12. When autonegotiation is disabled, the state of
register bits 0.6, 0.13, and 0.8 determine the device operating speed and duplex mode.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 5


Cat5 Twisted Pair Media Interface


**Note** While 10BASE-T and 100BASE-TX do not require autonegotiation, IEEE 802.3-2008 Clause 40
has defined 1000BASE-T to require autonegotiation.

##### **2.3.3 1000BASE-T Forced Mode Support**


The VSC8514-11 provides support for a 1000BASE-T forced test mode. In this mode, the PHY can be
forced into 1000BASE-T mode and does not require manual setting of master/slave at the two ends of
the link. This mode is for test purposes only, and should not be used in normal operation. To configure a
PHY in this mode, set register 17E2, bit 5 = 1 and register 0, bits 6 and 13 = 10.

##### **2.3.4 Automatic Crossover and Polarity Detection**


For trouble-free configuration and management of Ethernet links, the VSC8514-11 includes a robust
automatic crossover detection feature for all three speeds on the twisted pair interface (10BASE-T,
100BASE-T, and 1000BASE T). Known as HP Auto-MDIX, the function is fully compliant with Clause 40
of IEEE 802.3-2008.


Additionally, the device detects and corrects polarity errors on all MDI pairs — a useful capability that
exceeds the requirements of the standard.


Both HP Auto-MDIX detection and polarity correction are enabled in the device by default. Default
settings can be changed using device register bits 18.5:4. Status bits for each of these functions are
located in register 28.


**Note** The VSC8514-11 can be configured to perform HP Auto-MDIX, even when autonegotiation is
disabled and the link is forced into 10/100 speeds. To enable this feature, set register 18.7 to 0. To use
the feature, also set register 0.12 to 0.


The HP Auto-MDIX algorithm successfully detects, corrects, and operates with any of the MDI wiring pair
combinations listed in the following table.


_**Table 1 •**_ **Supported MDI Pair Combinations**


**1, 2** **3, 6** **4, 5** **7, 8** **Mode**


A B C D Normal MDI


B A D C Normal MDI-X


A B D C Normal MDI with pair swap on C and D pair


B A C D Normal MDI-X with pair swap on C and D pair

##### **2.3.5 Manual MDI/MDIX Setting**


As an alternative to HP Auto-MDIX detection, the PHY can be forced to be MDI or MDI-X using register
19E1, bits 3:2. Setting these bits to 10 forces MDI and setting 11 forces MDI-X. Leaving the bits 00
enables the HP Auto-MDIX setting to be based on register 18, bits 7 and 5.

##### **2.3.6 Link Speed Downshift**


For operation in cabling environments that are incompatible with 1000BASE-T, the VSC8514-11 provides
an automatic link speed downshift option. When enabled, the device automatically changes its
1000BASE-T autonegotiation advertisement to the next slower speed after a set number of failed
attempts at 1000BASE-T. No reset is required to get out of this state when a subsequent link partner with
1000BASE-T support is connected. This feature is useful in setting up in networks using older cable
installations that include only pairs A and B, and not pairs C and D.


To configure and monitor link speed downshifting, set register 20E1, bits 4:1. For more information, see
Table 45 on page 3-44.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 6


Reference Clock

##### **2.3.7 Energy Efficient Ethernet**


The VSC8514-11 supports the IEEE 802.3az Energy Efficient Ethernet standard to provide a method for
reducing power consumption on an Ethernet link during times of low utilization. It uses low-power idles
(LPI) to achieve this objective.


_**Figure 5 •**_ **Low-Power Idle Operation**



~~Active~~



~~Low Power Idle~~



~~Active~~



~~T~~ s ~~T~~ q ~~T~~ r


Using LPI, the usage model for the link is to transmit data as fast as possible and then return to a lowpower idle state. Energy is saved on the link by cycling between active and low-power idle states. During
LPI, power is reduced by turning off unused circuits and using this method, energy use scales with
bandwidth utilization. The VSC8514-11 uses LPI to optimize power dissipation in 100BASE-TX and
1000BASE-T modes of operation.


In addition, the IEEE 802.3az standard defines a 10BASE-Te mode that reduces transmit signal
amplitude from 5 V p-p to approximately 3.3 V p-p . This mode reduces power consumption in 10 Mbps link
speed and fully interoperates with legacy 10BASE-T compliant PHYs over 100 m Cat5 cable or better.


To configure the VSC8514-11 in 10BASE-Te mode, set register 17E2.15 to 1 for each port. Additional
energy efficient Ethernet features are controlled through Clause 45 registers. For more information, see
"Clause 45 Registers to Support Energy Efficient Ethernet and 802.3bf" on page 3-62.

#### **2.4 Reference Clock**


The device reference clock supports 125 MHz and 156.25 MHz compliant clock signals. The clock signal
must be capacitively coupled and LVDS complaint.

##### **2.4.1 Configuring the Reference Clock**


The REFCLK_SEL1 and REFCLK_SEL0 pins configure the reference clock speed. The following table
shows the functionality and associated reference clock frequency.


_**Table 2 •**_ **REFCLK Frequency Selection**


**REFCLK_SEL1** **REFCLK_SEL0** **Frequency**


0 0 125 MHz


1 0 156.25 MHz

#### **2.5 Ethernet Inline-Powered Devices**


The VSC8514-11 can detect legacy inline-powered devices in Ethernet network applications. Inlinepowered detection capability is useful in systems that enable IP phones and other devices (such as
wireless access points) to receive power directly from their Ethernet cable, similar to office digital phones
receiving power from a private branch exchange (PBX) office switch over telephone cabling. This type of
setup eliminates the need for an external power supply and enables the inline-powered device to remain
active during a power outage, assuming that the Ethernet switch is connected to an uninterrupted power
supply, battery, back-up power generator, or other uninterruptable power source.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 7


Ethernet Inline-Powered Devices


For more information about legacy inline-powered device detection, visit the Cisco Web site at
www.cisco.com. The following illustration shows an example of an inline-powered Ethernet switch
application.


_**Figure 6 •**_ **Inline-Powered Ethernet Switch Diagram**




















|Transformer|Col2|
|---|---|
|||
|RJ-45<br>I/F|RJ-45<br>I/F|









The following procedure describes the process that an Ethernet switch must perform to process inlinepower requests made by a link partner that is, in turn, capable of receiving inline-power:


1. Enable the inline-powered device detection mode on each VSC8514-11 PHY using its serial
management interface. Set register bit 23E1.10 to 1.


2. Ensure that the VSC8514-11 autonegotiation enable bit (register 0.12) is also set to 1. In the
application, the device sends a special fast link pulse signal to the link partner. Reading register
bit 23E1.9:8 returns 00 during the search for devices that require power over Ethernet (PoE).


3. The VSC8514-11 PHY monitors its inputs for the fast link pulse signal looped back by the link
partner. A link partner capable of receiving PoE loops back the fast link pulses when the link
partner is powered down. This is reported when VSC8514-11 register bit 23E1.9:8 reads back 01.
It can also be verified as an inline-power detection interrupt by reading VSC8514-11 register
bit 26.9, which should be a 1, and which is subsequently cleared and the interrupt de-asserted
after the read. When a link partner device does not loop back the fast link pulse after a specific
time, VSC8514-11 register bit 23E1.9:8 automatically resets to 10.


4. If the VSC8514-11 PHY reports that the link partner requires PoE, the Ethernet switch must
enable inline-power on this port, independent of the PHY.


5. The PHY automatically disables inline-powered device detection when the VSC8514-11 register
bits 23E1.9:8 automatically reset to 10, and then automatically changes to its normal
autonegotiation process. A link is then autonegotiated and established when the link status bit is
set (register bit 1.2 is set to 1).


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 8


IEEE 802.3af Power Over Ethernet Support


6. In the event of a link failure (indicated when VSC8514-11 register bit 1.2 reads 0), it is
recommended that the inline-power be disabled to the inline-powered device, independent of the
PHY. The VSC8514-11 PHY disables its normal autonegotiation process and re-enables its inlinepowered device detection mode.

#### **2.6 IEEE 802.3af Power Over Ethernet Support**


The VSC8514-11 device is compatible with designs that are intended for use in systems that supply
power to data terminal equipment (DTE) by means of the MDI or twisted pair cable, as described in IEEE
802.3af Clause 33.

#### **2.7 ActiPHY Power Management**


In addition to the IEEE-specified power-down control bit (device register bit 0.11), the VSC8514-11
device also includes an ActiPHY power management mode for each PHY. This mode enables support for
power-sensitive applications. It utilizes a signal-detect function that monitors the media interface for the
presence of a link to determine when to automatically power-down the PHY. The PHY wakes up at a
programmable interval and attempts to wake up the link partner PHY by sending a burst of fast link pulse
over copper media.


The ActiPHY power management mode in the VSC8514-11 is enabled on a per-port basis during normal
operation at any time by setting register bit 28.6 to 1.


The following operating states are possible when ActiPHY mode is enabled:


           - Low-power state


           - Link partner wake-up state


           - Normal operating state (link-up state)


The VSC8514-11 switches between the low-power state and link partner wake-up state at a
programmable rate (the default is two seconds) until signal energy has been detected on the media
interface pins. When signal energy is detected, the PHY enters the normal operating state. If the PHY is
in its normal operating state and the link fails, the PHY returns to the low-power state after the expiration
of the link status time-out timer. After reset, the PHY enters the low-power state.


When autonegotiation is enabled in the PHY, the ActiPHY state machine operates as described.


When autonegotiation is disabled and the link is forced to use 10BASE-T or 100BASE-TX modes while
the PHY is in its low-power state, the PHY continues to transition between the low-power and link partner
wake-up states until signal energy is detected on the media pins. At that time, the PHY transitions to the
normal operating state and stays in that state even when the link is dropped.


When autonegotiation is disabled while the PHY is in the normal operation state, the PHY stays in that
state when the link is dropped and does not transition back to the low-power state.


The following illustration shows the relationship between ActiPHY states and timers.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 9


Serial Management Interface


_**Figure 7 •**_ **ActiPHY State Diagram**








##### **2.7.1 Low-Power State**

In the low-power state, all major digital blocks are powered down. However, the SMI interface (MDC,
MDIO, and MDINT) functionality is provided.


In this state, the PHY monitors the media interface pins for signal energy. The PHY comes out of lowpower state and transitions to the normal operating state when signal energy is detected on the media.
This happens when the PHY is connected to one of the following:


           - Autonegotiation-capable link partner


           - Another PHY in enhanced ActiPHY link partner wake-up state


In the absence of signal energy on the media pins, the PHY periodically transitions from low-power state
to link partner wake-up state, based on the programmable sleep timer (register bits 20E1.14:13). The
actual sleep time duration is randomized from –80 ms to 60 ms to avoid two linked PHYs in ActiPHY
mode entering a lock-up state during operation.

##### **2.7.2 Link Partner Wake-Up State**


In the link partner wake-up state, the PHY attempts to wake up the link partner. Up to three complete fast
link pulse bursts are sent on alternating pairs A and B of the Cat5 media for a duration based on the
wake-up timer, which is set using register bits 20E1.12:11.


In this state, SMI interface (MDC, MDIO, and MDINT) functionality is provided.


After sending signal energy on the relevant media, the PHY returns to the low-power state.

##### **2.7.3 Normal Operating State**


In the normal operating state, the PHY establishes a link with a link partner. When the media is
unplugged or the link partner is powered down, the PHY waits for the duration of the programmable link
status time-out timer, which is set using register bit 28.7 and bit 28.2. It then enters the low-power state.

#### **2.8 Serial Management Interface**


The VSC8514-11 device includes an IEEE 802.3-compliant serial management interface (SMI) that is
controlled by its MDC, MDIO, and MDINT pins. The SMI provides access to device control and status
registers. The register set that controls the SMI consists of 32 16-bit registers, including all required


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 10


Serial Management Interface


IEEE-specified registers. Also, there are additional pages of registers accessible using device register
31.


Energy efficient Ethernet control registers are available through the SMI using Clause 45 registers and
Clause 22 register access in registers 13 through 14. For information about available register settings,
see Table 24 on page 3-33 and Table 72 on page 3-62.


The SMI is a synchronous serial interface with input data to the VSC8514-11 on the MDIO pin that is
clocked on the rising edge of the MDC pin. The output data is sent on the MDIO pin on the rising edge of
the MDC signal. The interface can be clocked at a rate from 0 MHz to 12.5 MHz, depending on the total
load on MDIO. An external 2-k Ω pull-up resistor is required on the MDIO pin.

##### **2.8.1 SMI Frames**


Data is transferred over the SMI using 32-bit frames with an optional, arbitrary-length preamble. Before
the first frame can be sent, at least two clock pulses on MDC must be provided with the MDIO signal at
logic one to initialize the SMI state machine. The following illustrations show the SMI frame format for
read and write operations.


_**Figure 8 •**_ **SMI Read Frame**


Station manager drives MDIO PHY drives MDIO


MDC


MDIO


|Col1|Col2|Z|1|0|Col6|1|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|R0|Z|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Z|1|0|1|1|1|||||||||||||||||||||||||||||||
||Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|0|Z|Z|
||Z|Z|Z|Z|Z|Z|0|A4|A3|A2|A1|A0|R4|R3|R2|R1|R1|R1|0|D15|D14|D13|D12|D11|D10|D9|D8|D7|D6|D5|D4|D3|D2|D<br>D1|D<br>D1|D<br>D1|D<br>D1|



Idle [Preamble] SFD Read
(optional)



PHY Address Register Address TA Register Data Idle
to PHY from PHY



MDC


MDIO



_**Figure 9 •**_ **SMI Write Frame**


Station manager drives MDIO (PHY tri-states MDIO during the entire sequence)


|Col1|Col2|Z|1|0|1|0|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|1|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Z|1|0|1|0|1|||||||||||||||||||||||||||||||
||Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|Z|0|Z|Z|
||Z|Z|Z|Z|Z|Z|Z|A4|A3|A2|A1|A0|R4|R3|R2|R1|R1|R1|0|D15|D14|D13|D12|D11|D10|D9|D8|D7|D6|D5|D4|D3|D2|D<br>D1|D<br>D1|D<br>D1|D<br>D1|



Idle [Preamble] SFD Write
(optional)



PHY Address Register Address TA Register Data Idle
to PHY to PHY



The following list defines the terms used in the SMI read and write timing diagrams.


   - **Idle** During idle, the MDIO node goes to a high-impedance state. This allows an external pull-up
resistor to pull the MDIO node up to a logical 1 state. Because the idle mode does not contain any
transitions on MDIO, the number of bits is undefined during idle.


   - **Preamble** By default, preambles are not expected or required. The preamble is a string of ones.
If it exists, the preamble must be at least 1 bit; otherwise, it can be of an arbitrary length.


   - **Start of Frame Delimiter (SFD)** A pattern of 01 indicates the start of frame. If the pattern is not
01, all following bits are ignored until the next preamble pattern is detected.


   - **Read or Write Opcode** A pattern of 10 indicates a read. A 01 pattern indicates a write. If the bits
are not either 01 or 10, all following bits are ignored until the next preamble pattern is detected.


   - **PHY Address** The particular VSC8514-11 device responds to a message frame only when the
received PHY address matches its physical address. The physical address is 5 bits long (4:0).


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 11


LED Interface


           - **Register Address** The next five bits are the register address.


           - **Turnaround** The two bits used to avoid signal contention when a read operation is performed on
the MDIO are called the turnaround (TA) bits. During read operations, the VSC8514-11 device
drives the second TA bit, a logical 0.


           - **Data** The 16-bits read from or written to the device are considered the data or data stream.

When data is read from a PHY, it is valid at the output from one rising edge of MDC to the next
rising edge of MDC. When data is written to the PHY, it must be valid around the rising edge of
MDC.


           - **Idle** The sequence is repeated.

##### **2.8.2 SMI Interrupt**


The SMI includes an output interrupt signal, MDINT, for signaling the station manager when certain
events occur in the VSC8514-11.


When a PHY generates an interrupt, the MDINT pin is asserted if the interrupt pin enable bit (MII register
25.15) is set. The MDINT pin can be configured for open-drain (active-low) by tying the pin to a pull-up
resistor and to VDDIO. The following illustration shows this configuration.


_**Figure 10 •**_ **MDINT Configured as an Open-Drain (Active-Low) Pin**



VDDMDIO



External Pull-up
Resistor at the
Station Manager
for Open-drain
(Active-low Mode)


MDINT
(to the Station
Manager)








#### **2.9 LED Interface**

The LED interface supports the following configurations: direct drive, basic serial LED mode, and
enhanced serial LED mode. The polarity of the LED outputs is programmable and can be changed using
register 17E2, bits 13:10. The default polarity is active low.


Direct drive mode provides four LED signals per port, LED0_[0:3] through LED3_[0:3]. The mode and
function of each LED signal can be configured independently. When serial LED mode is enabled, the
direct drive pins not used by the serial LED interface remain available.


In basic serial LED mode, all signals that can be displayed on LEDs are sent as LED_Data and
LED_CLK for external processing.


In enhanced serial LED mode, up to four LED signals per port can be sent as LED_Data, LED_CLK,
LED_LD, and LED_Pulse. The following sections provide detailed information about the various LED
modes.


**Note** LED number is listed using the convention, LED<LED#>_<Port#>.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 12


LED Interface


The following table shows the bit 9 settings for register 14G that are used to control the LED behavior for
all the LEDs in VSC8514-11.


_**Table 3 •**_ **LED Drive State**


**Setting** **Active** **Not Active**


14G[9: 1] (default) Ground Tristate


14G[9: 0] (alternate setting) Ground Vdd

##### **2.9.1 LED Modes**


Each LED pin can be configured to display different status information that can be selected by setting the
LED mode in register 29. The default LED state is active low but can be changed by modifying the value
in register 17E2, bits 13:10. The blink/pulse stretch is dependent on the LED behavior setting in register
30.


The following table provides a summary of the LED modes and functions. The modes listed are
equivalent to the setting used in register 29 to configure each LED pin.


_**Table 4 •**_ **LED Mode and Function Summary**


**Mode** **Function Name** **LED State and Description**


0 Link/Activity 1: No link in any speed on any media interface.


0: Valid link at any speed on any media interface.


Blink or pulse-stretch = Valid link at any speed on any media
interface with activity present.


1 Link1000/Activity 1: No link in 1000BASE-T.


0: Valid 1000BASE-T.


Blink or pulse-stretch = Valid 1000BASE-T link with activity
present.


2 Link100/Activity 1: No link in 100BASE-TX.


0: Valid 100BASE-TX.


Blink or pulse-stretch = Valid 100BASE-TX link with activity
present.


3 Link10/Activity 1: No link in 10BASE-T.


0: Valid 10BASE-T link.


Blink or pulse-stretch = Valid 10BASE-T link with activity
present.


4 Link100/1000/Activity 1: No link in 100BASE-TX or 1000BASE-T.


0: Valid 100BASE-TX or 1000BASE-T link. Blink or pulsestretch = Valid 100BASE-TX or 1000BASE-T link with activity
present.


5 Link10/1000/Activity 1: No link in 10BASE-T or 1000BASE-T.


0: Valid 10BASE-T or 1000BASE-T link.


Blink or pulse-stretch = Valid 10BASE-T or 1000BASE-T link
with activity present.


6 Link10/100/Activity 1: No link in 10BASE-T or 100BASE-TX.


0: Valid 10BASE-T or 100BASE-TX, link.


Blink or pulse-stretch = Valid 10BASE-T or 100BASE-TX link
with activity present.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 13


LED Interface


_**Table 4 •**_ **LED Mode and Function Summary** _**(continued)**_


**Mode** **Function Name** **LED State and Description**


7 Reserved Reserved


8 Duplex/Collision 1: Link established in half-duplex mode, or no link established.


0: Link established in full-duplex mode.


Blink or pulse-stretch = Link established in half-duplex mode
but collisions are present.


9 Collision 1: No collision detected.


Blink or pulse-stretch = Collision detected.


10 Activity 1: No activity present.


Blink or pulse-stretch = Activity present (becomes TX activity
present when register bit 30.14 is set to 1).


11 Reserved Reserved


12 Autonegotiation Fault 1: No autonegotiation fault present.


0: Autonegotiation fault occurred.


13 Serial Mode Serial stream. See "Basic Serial LED Mode" on page 2-14.
Only relevant on PHY port 0. Reserved in others.


14 Force LED Off 1: De-asserts the LED [(1)] .


15 Force LED On 0: Asserts the LED [(1)] .


_1. Setting this mode suppresses LED blinking after reset._

##### **2.9.2 Basic Serial LED Mode**


The VSC8514-11 can be configured so that access to all its LED signals is available using two pins. This
option is enabled by setting LED0 on PHY0 to serial LED mode in register 29, bits 3:0 to 0xD. When
serial LED mode is enabled, the LED0_0 pin becomes the serial data pin, and the LED1_0 pin becomes
the serial clock pin. All other LED pins can still be configured normally. The serial LED mode clocks the
48 LED status bits on the rising edge of the serial clock.


The LED behavior settings can also be used in serial LED mode. The controls are used on a per-PHY
basis, where the LED combine and LED blink or pulse-stretch setting of LED0_n for each PHY is used to
control the behavior of each bit of the serial LED stream for each corresponding PHY. To configure LED
behavior, set device register 30.


The following table shows the 48-bit serial output bitstream of each LED signal. The individual signals
can be clocked in the following order.


_**Table 5 •**_ **LED Serial Bitstream Order**


**Output** **PHY0** **PHY1** **PHY2** **PHY3**


Link/activity 1 13 25 37


Link1000/activity 2 14 26 38


Link100/activity 3 15 27 39


Link10/activity 4 16 28 40


Reserved 5 17 29 41


Duplex/collision 6 18 30 42


Collision 7 19 31 43


Activity 8 20 32 44


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 14


LED Interface


_**Table 5 •**_ **LED Serial Bitstream Order** _**(continued)**_


**Output** **PHY0** **PHY1** **PHY2** **PHY3**


Reserved 9 21 33 45


Tx activity 10 22 34 46


Rx activity 11 23 35 47


Autonegotiation fault 12 24

##### **2.9.3 Extended LED Modes**


In addition to the LED modes in register 29, extended LED modes are enabled on the LED0_[3:0] pins
when the corresponding register 19E1, bits 15 to 12 are set to 1. Each of these bits enables extended
modes on a specific LED pin, and these extended modes are shown in the following table. For example,
LED0 = mode 17 means that register 19E1 bit 12 = 1 and register 29 bits 3 to 0 = 0001.


The following table provides a summary of the extended LED modes and functions.


_**Table 6 •**_ **Extended LED Mode and Function Summary**


**Mode** **Function Name** **LED State and Description**


16 Link1000BASE-X Activity 1: No link in 1000BASE-X.


0: Valid 1000BASE-X link.


17 Link100BASE-FX Activity 1: No link in 100BASE-FX.


0: Valid 100BASE-FX link.


18 1000BASE-X Activity 1: No 1000BASE-X activity present.


Blink or pulse-stretch = 1000BASE-X activity present.


19 100BASE-FX Activity 1: No 100BASE-FX activity present.


Blink or pulse-stretch = 100BASE-FX activity present.


20 Force LED Off 1: De-asserts the LED.


21 Force LED On 0: Asserts the LED. LED pulsing is disabled in this mode.


22 Reserved Reserved

##### **2.9.4 LED Port Swapping**


For additional hardware configurations, the VSC8514-11 can have its LED port order swapped. This is a
useful feature to help simplify PCB layout design. Register 25G bit 0 controls the LED port swapping
mode.

##### **2.9.5 LED Behavior**


Several LED behaviors can be programmed into the VSC8514-11. Use the settings in register 30 and
19E1 to program LED behavior, which includes the following:


_**2.9.5.1**_ _**LED Combine**_

Enables an LED to display the status for a combination of primary and secondary modes. This can be
enabled or disabled for each LED pin. For example, a copper link running in 1000BASE-T mode and
activity present can be displayed with one LED by configuring an LED pin to Link1000/Activity mode. The
LED asserts when linked to a 1000BASE-T partner and also blinks or performs pulse-stretch when
activity is either transmitted by the PHY or received by the Link Partner. When disabled, the combine
feature only provides status of the selected primary function. In this example, only Link1000 asserts the
LED, and the secondary mode, activity, does not display when the combine feature is disabled.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 15


GPIO Pins


_**2.9.5.2**_ _**LED Blink or Pulse-Stretch**_

This behavior is used for activity and collision indication. This can be uniquely configured for each LED
pin. Activity and collision events can occur randomly and intermittently throughout the link-up period.
Blink is a 50% duty cycle oscillation of asserting and de-asserting an LED pin. Pulse-stretch guarantees
that an LED is asserted and de-asserted for a specific period of time when activity is either present or not
present. These rates can also be configured using a register setting.


_**2.9.5.3**_ _**Rate of LED Blink or Pulse-Stretch**_

This behavior controls the LED blink rate or pulse-stretch length when blink/pulse-stretch is enabled on
an LED pin. The blink rate, which alternates between a high and low voltage level at a 50% duty cycle,
can be set to 2.5 Hz, 5 Hz, 10 Hz, or 20 Hz. For pulse-stretch, the rate can be set to 50 ms, 100 ms,
200 ms, or 400 ms. The blink rate selection for PHY0 globally sets the rate used for all LED pins on all
PHY ports.


**2.9.5.3.1** **LED Pulsing Enable**
To provide additional power savings, the LEDs (when asserted) can be pulsed at 5 kHz, 20% duty cycle.


**2.9.5.3.2** **LED Blink After Reset**

The LEDs will blink for one second after power-up and after any time all resets have been de-asserted.
This can be disabled through register 19E1, bit 11 = 0.


**2.9.5.3.3** **Pulse Programmable Control**
These bits add the ability to width and frequency of LED pulses. This feature facilitates power reduction
options.

#### **2.10 GPIO Pins**


The VSC8514-11 provides 15 multiplexed general purpose input/output (GPIO) pins. All device GPIO
pins and their behavior are controlled using registers. The following table shows an overview of the
register controls for GPIO pins. For more information, see "General Purpose Registers" on page 3-55.


_**Table 7 •**_ **Register Bits for GPIO Control and Status**


**GPIO Pin** **GPIO_ctrl** **GPIO Input** **GPIO Output** **GPIO Output Enable**


GPIO0 13G[1:0] 15G.0 16G.0 17G.0


GPIO1 13G[3:2] 15G.1 16G.1 17G.1


GPIO2 13G[5:4] 15G.2 16G.2 17G.2


GPIO3 13G[7:6] 15G.3 16G.3 17G.3


GPIO4 13G[9:8] 15G.4 16G.4 17G.4


GPIO5 13G[11:10] 15G.5 16G.5 17G.5


GPIO6 13G[13:12] 15G.6 16G.6 17G.6


GPIO7 13G[15:14] 15G.7 16G.7 17G.7


GPIO8 14G[1:0] 15G.8 16G.8 17G.8


GPIO9 14G[3:2] 15G.9 16G.9 17G.9


GPIO10 14G[5:4] 15G.10 16G.10 17G.10


GPIO11 14G[7:6] 15G.11 16G.11 17G.11


GPIO12 14G[15:14] 15G.12 16G.12 17G.12


GPIO13 14G[15:14] 15G.13 16G.13 17G.13


GPIO14 14G[15:14] 15G.14 16G.14 17G.14


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 16


Testing Features

#### **2.11 Testing Features**


The VSC8514-11 device includes several testing features designed to facilitate performing system-level
debugging and in-system production testing. This section describes the available features.

##### **2.11.1 Ethernet Packet Generator**


The Ethernet packet generator (EPG) can be used at each of the 10/100/1000BASE-T speed settings for
copper Cat5 media to isolate problems between the MAC and the VSC8514-11, or between a locally
connected PHY and its remote link partner. Enabling the EPG feature disables all MAC interface transmit
pins and selects the EPG as the source for all data transmitted onto the twisted pair interface.


**Important** The EPG is intended for use with laboratory or in-system testing equipment only. Do not use
the EPG testing feature when the VSC8514-11 is connected to a live network.


To enable the VSC8514-11 EPG feature, set the device register bit 29E1.15 to 1.


When the EPG is enabled, packet loss occurs during transmission of packets from the MAC to the PHY.
However, the PHY receive output pins to the MAC are still active when the EPG is enabled. When it is
necessary to disable the MAC receive pins as well, set the register bit 0.10 to 1.


When the device register bit 29E1.14 is set to 1, the PHY begins transmitting Ethernet packets based on
the settings in registers 29E1 and 30E1. These registers set:


           - Source and destination addresses for each packet


           - Packet size


           - Interpacket gap


           - FCS state


           - Transmit duration


           - Payload pattern


When register bit 29E1.13 is set to 0, register bit 29E1.14 is cleared automatically after 30,000,000
packets are transmitted.

##### **2.11.2 CRC Counters**


Two sets of cyclical redundancy check (CRC) counters are available in all PHYs in VSC8514-11. One set
monitors traffic on the copper interface, and the other set monitors traffic on the SerDes interface.


The device CRC counters operate in the 10/100/1000BASE-T mode as follows:


           - After receiving a packet on the media interface, register bit 15 in register 18E1 is set and cleared
after being read.


           - The packet then is counted by either the good CRC counter or the bad CRC counter.


           - Both CRC counters are also automatically cleared when read.


           - The good CRC counter’s highest value is 9,999 packets. After this value is reached, the counter
clears on the 10,000 [th] packet and continues to count additional packets beyond that value.


           - The bad CRC counter stops counting when it reaches its maximum counter limit of 255 packets.


**2.11.2.0.1** **Copper Interface CRC Counters**
Two separate CRC counters are available between the copper interface PCSs and SerDes MAC
interface. There is a 14-bit good CRC counter available through register bits 18E1.13:0 and a separate
8-bit bad CRC counter available in register bits 23E1.7:0.

##### **2.11.3 Far-End Loopback**


The far-end loopback testing feature is enabled by setting register bit 23.3 to 1. When enabled, it forces
incoming data from a link partner on the current media interface into the MAC interface of the PHY where
it is retransmitted to the link partner on the media interface as shown in the following illustration. In


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 17


Testing Features


addition, the incoming data also appears on the receive data pins of the MAC interface. Data present on
the transmit data pins of the MAC interface is ignored when using this testing feature.


_**Figure 11 •**_ **Far-End Loopback Diagram**












|Link Partner|RX<br>TX|PHY_port_n|RXD<br>TXD|MAC|
|---|---|---|---|---|
|Link Partner|TX<br>RX||||


##### **2.11.4 Near-End Loopback**

When the near-end loopback testing feature is enabled, transmitted data (TXD) is looped back in the
PCS block onto the receive data signals (RXD), as shown in the following illustration. When using this
testing feature, no data is transmitted over the network. To enable near-end loopback, set the device
register bit 0.14 to 1.


_**Figure 12 •**_ **Near-End Loopback Diagram**












##### **2.11.5 Connector Loopback**

The connector loopback testing feature allows the twisted pair interface to be looped back externally.
When using this feature, the PHY must be connected to a loopback connector or a loopback cable.
Connect pair A to pair B, and pair C to pair D, as shown in the following illustration. The connector
loopback feature functions at all available interface speeds.


_**Figure 13 •**_ **Connector Loopback Diagram**











When using the connector loopback testing feature, the device autonegotiation, speed, and duplex
configuration is set using device registers 0, 4, and 9.


For 1000BASE-T connector loopback, additional writes are required in the following order:


1. Enable the 1000BASE-T connector loopback. Set register bit 24.0 to 1.


2. Disable pair swap correction. Set register bit 18.5 to 1.

##### **2.11.6 SerDes Loopbacks**


For test purposes, the SerDes and SerDes macro interfaces provides several data loops. The following
illustration shows the SerDes loopbacks.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 18


Testing Features


_**Figure 14 •**_ **Data Loops of the SerDes Macro**
















|IB<br>TCE|Col2|Col3|
|---|---|---|
|IB<br>~~TCE~~||~~TCE~~|
||||


|Col1|Col2|Col3|
|---|---|---|
|bidi-loop||RCPLL|
||||




|Col1|Col2|20|
|---|---|---|
||||
||||
||||
||||
||||
||||
||||
||||



_**2.11.6.1**_ _**QSGMII Mode**_

When the MAC interface is configured in QSGMII mode, write the following 16-bit value to register 18G:


Bits 15:12 0x9


Bits 11:8: Port address (0x0)


Bits 7:4: Loopback type
0x0: No loopback
0x2: Input loopback
0x4: Facility loopback
0x8: Equipment loopback


Bits 3:0: 0x2


**Note** Loopback configuration affects all ports associated with a QSGMII. Individual port loopback within
a QSGMII is not possible.


**2.11.6.1.1** **Facility Loop**
The recovered and de-multiplexer deserializer data output is looped back to the serializer data input and
replaces the data delivered by the digital core. This test loop provides the possibility to test the complete
analog macro data path from outside including input buffer, clock and data recovery, serialization and
output buffer. The data received by the input buffer must be transmitted by the output buffer after some
delay.


Additional configuration of the enhanced SerDes macro is required when selecting facility loopback
mode. Run the “set = 1” option when entering facility loopback mode and the “set = 0” option when
exiting facility loopback mode. Execute this additional configuration after running the command to
enable/disable facility loopback mode.

```
PhyWrite(PhyBaseAddr, 31, 0x0010);

PhyWrite(PhyBaseAddr, 18, 0x8013);

PhyWrite(PhyBaseAddr, 18, 0xd7cb);

```

VMDS-10446 VSC8514-11 Datasheet Revision 4.0 19


Testing Features

```
      PhyWrite(PhyBaseAddr, 18, 0x8007);

      tmp1 = PhyRead(PhyBaseAddr, 18);

      tmp2 = tmp1 & 0x0ff0;

      if (set)
      tmp3 = tmp2 | 0x0100;

      else

      tmp3 = tmp2 & 0x0ef0;
      tmp4 = tmp3 | 0x8006;
      PhyWrite(PhyBaseAddr, 18, tmp4);

      PhyWrite(PhyBaseAddr, 18, 0x9c40);
      // PhyBaseAddr is the 5-bit base address of the internal PHYs.
      // The upper 3 bits are set by the PHYADD[4:2] pins and the
      // lower 2 bits are 0.

```

**2.11.6.1.2** **Equipment Loop**
The 1-bit data stream at the serializer output is looped back to the deserializer and replaces the received
data stream from the input buffer. This test loop provides the possibility to verify the digital data path
internally. The transmit data goes through the serialization, the clock and data recovery, and
deserialization before the data is fed back to the digital core.


**2.11.6.1.3** **Input Loop**
The received 1-bit data stream of the input buffer is looped back asynchronously to the output buffer. This
test loop provides the possibility to test only the analog parts of the QSGMII interface because only the
input and output buffer are part of this loop.

##### **2.11.7 VeriPHY Cable Diagnostics**


The VSC8514-11 device includes a comprehensive suite of cable diagnostic functions that are available
using SMI reads and writes. These functions enable a variety of status and cable operating conditions to
be accessed and checked. The VeriPHY suite has the ability to identify the cable length and operating
conditions and to isolate a variety of common faults that can occur on the Cat5 twisted pair cabling.


**Note** When a link is established on the twisted pair interface in the 1000BASE-T mode, VeriPHY can
run without disrupting the link or disrupting any data transfer. However, when a link is established in
100BASE-TX or 10BASE-T modes, VeriPHY causes the link to drop while the diagnostics are running.
After diagnostics are finished, the link is re-established.


The following diagnostic functions are part of the VeriPHY suite:


           - Detecting coupling between cable pairs


           - Detecting cable pair termination


           - Determining cable length


           - Mean square error noise


_**2.11.7.1**_ _**Coupling Between Cable Pairs**_
Shorted wires, improper termination, or high crosstalk resulting from an incorrect wire map can cause
error conditions such as anomalous coupling between cable pairs. These conditions can prevent the
device from establishing a link in any speed.


_**2.11.7.2**_ _**Cable Pair Termination**_

Proper termination of Cat5 cable requires a 100 Ω differential impedance between the positive and
negative cable terminals. IEEE 802.3 allows for a termination of 115 Ω maximum and 85 Ω minimum. If
the termination falls outside of this range, it is reported by the VeriPHY diagnostics as an anomalous
termination. The diagnostics can also determine the presence of an open or shorted cable pair.


_**2.11.7.3**_ _**Cable Length**_
When the Cat5 cable in an installation is properly terminated, VeriPHY reports the approximate cable
length in meters. If there is a cable fault, the distance to the fault is reported. Cable length is reliable to
120 m.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 20


Testing Features


_**2.11.7.4**_ _**Mean Square Error Noise**_
The average absolute error can be read out when either a 100BASE-TX or 1000BASE-T link is
established. In the case of 1000BASE-T link, there are two average absolute error terms, one for each
twisted pair over which signal is received. Use the following script to read average absolute error for
100BASE-TX:

```
      PhyWrite(<phy>, 31, 0x52b5);

      PhyWrite(<phy>, 16, 0xa3c0);

      PhyRead(<phy>, 16);

      tmp17 = PhyRead(<phy>, 17);

      tmp18 = PhyRead(<phy>, 18);
      mse = (tmp18 << 4) | (tmp17 >> 12);
      PhyWrite(<phy>, 31, 0);
```

The returned average absolute error is in units of 1/2,048 and can be found in the mse variable.

```
      PhyWrite(<phy>, 31, 0x52b5);

      PhyWrite(<phy>, 16, 0xa3c0);

      PhyRead(<phy>, 16);

      tmp17 = PhyRead(<phy>, 17);

      tmp18 = PhyRead(<phy>, 18);
      mseA = (tmp18 << 4) | (tmp17 >> 12);
      mseB = tmp17 & 0x0fff;

      PhyWrite(<phy>, 16, 0xa3c2);

      PhyRead(<phy>, 16);

      tmp17 = PhyRead(<phy>, 17);

      tmp18 = PhyRead(<phy>, 18);
      mseC = (tmp18 << 4) | (tmp17 >> 12);
      mseD = tmp17 & 0x0fff;

      PhyWrite(<phy>, 31, 0);
```

The returned average absolute error is in units of 1/2,048 and can be found in the mseA, mseB, mseC,
and mseD variables for each twisted pair.

##### **2.11.8 JTAG Boundary Scan**


The VSC8514-11 supports the test access port (TAP) and boundary scan architecture described in
IEEE 1149.1. The device includes an IEEE 1149.1-compliant test interface, referred to as a JTAG TAP
interface.


The JTAG boundary scan logic on the VSC8514-11, accessed using its TAP interface, consists of a
boundary scan register and other logic control blocks. The TAP controller includes all IEEE-required
signals (TMS, TCK, TDI, and TDO), in addition to the optional asynchronous reset signal TRST. The
following illustration shows the TAP and boundary scan architecture.


**Important** When JTAG is not in use, the TRST pin must be tied to ground with a pull-down resistor for
normal operation.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 21


Testing Features


_**Figure 15 •**_ **Test Access Port and Boundary Scan Architecture**













TDI


TMS


NTRST


TCK









After a TAP reset, the device identification register is serially connected between TDI and TDO by
default. The TAP instruction register is loaded from a shift register when a new instruction is shifted in, or
if there is no new instruction in the shift register, a default value of 6'b100100 (IDCODE) is loaded. Using
this method, there is always a valid code in the instruction register, and the problem of toggling
instruction bits during a shift is avoided. Unused codes are mapped to the BYPASS instruction.

##### **2.11.9 JTAG Instruction Codes**


The following table shows the supported JTAG instruction codes.


_**Table 8 •**_ **JTAG Instruction Codes**


**Instruction Code** **Description**


BYPASS The bypass register contains a single shift-register stage and is used to provide
a minimum-length serial path (one TCK clock period) between TDI and TDO to
bypass the device when no test operation is required.


CLAMP Allows the state of the signals driven from the component pins to be
determined from the boundary scan register while the bypass register is
selected as the serial path between TDI and TDO. While the CLAMP
instruction is selected, the signals driven from the component pins do not
change.


EXTEST Allows tests of the off-chip circuitry and board-level interconnections by
sampling input pins and loading data onto output pins. Outputs are driven by
the contents of the boundary scan cells, which have to be updated with valid
values, with the PRELOAD instruction, prior to the EXTEST instruction.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 22


Testing Features


_**Table 8 •**_ **JTAG Instruction Codes** _**(continued)**_


**Instruction Code** **Description**


HIGHZ Places the component in a state in which all of its system logic outputs are
placed in a high-impedance state. In this state, an in-circuit test system can
drive signals onto the connections normally driven by a component output
without incurring a risk of damage to the component. This makes it possible to
use a board where not all of the components are compatible with the
IEEE 1149.1 standard.


IDCODE Provides the version number (bits 31:28), device family ID (bits 27:12), and the
manufacturer identity (bits 11:1) to be serially read from the device.


SAMPLE/PRELOAD Allows a snapshot of inputs and outputs during normal system operation to be
taken and examined. It also allows data values to be loaded into the boundary
scan cells prior to the selection of other boundary scan test instructions.


USERCODE Provides the version number (bits 31:28), part number (bits 27:12), and the
manufacturer identity (bits 11:1) to be serially read from the device.


The following table provides information about the USERCODE binary values stored in the device JTAG
register.


_**Table 9 •**_ **USERCODE JTAG Device Identification Register Descriptions**


**Description** **Device Version** **Family ID** **Manufacturing Identity** **LSB**


Bit field 31–28 27–12 11–1 0


Binary value 0000 1000 0101 0001 0100 000 0111 0100 1


The following table provides information about the location and IEEE compliance of the JTAG instruction
codes used in the VSC8514-11. Instructions not explicitly listed in the table are reserved. For more
information about these IEEE specifications, visit the IEEE Web site at www.IEEE.org.


_**Table 10 •**_ **JTAG Instruction Code IEEE Compliance**


**Instruction** **Code** **Selected Register** **Register Width** **IEEE 1149.1**


EXTEST 6'b000000 Boundary Scan 161 Mandatory


SAMPLE/PRELOAD 6'b000001 Boundary Scan 161 Mandatory


IDCODE 6'b100100 Device Identification 32 Optional


USERCODE 6'b100101 Device Identification 32 Optional


CLAMP 6'b000010 Bypass Register 1 Optional


HIGHZ 6'b000101 Bypass Register 1 Optional


BYPASS 6'b111111 Bypass Register 1 Mandatory

##### **2.11.10 Boundary Scan Register Cell Order**


All inputs and outputs are observed in the boundary scan register cells. All outputs are additionally driven
by the contents of boundary scan register cells. Bidirectional pins have all three related boundary scan
register cells: input, output, and control.


The complete boundary scan cell order is available as a BSDL file on the Microsemi Web site.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 23


Configuration

#### **2.12 Configuration**


The VSC8514-11 can be configured by setting internal memory registers using the management
interface. To configure the device, perform the following steps:


1. COMA_MODE active, drive high.


2. Apply power.


3. Apply RefClk.


4. Release reset, drive high. Power and clock must be stable before releasing reset.


5. Wait 120 ms, minimum.


6. Apply patch from PHY_API.


7. Configure register 19G for MAC mode (to access register 19G, register 31 must be 0x10). Read
register 19G. Set bits 15:14, MAC configuration, to 01:
Write new register 19G.


8. Configure register 18G for MAC on all 4 PHYs write:
QSGMII: 0x80E0
Read register 18G until bit 15 equals 0.


9. Configure register 23 for MAC and Media mode (to access register 23, register 31 must be 0).
Read register 23. Set bits 10:8 to 000:
Write new register 23.


10. Software reset. Read register 0 (to access register 0, register 31 must be 0). Set bit 15 to 1.
Write new register 0.


11. Read register 0 until bit 15 equals 0.


12. Release the COMA_MODE pin, drive low.

##### **2.12.1 Initialization**


The COMA_MODE pin provides an optional feature that may be used to control when the PHYs become
active. The typical usage is to keep the PHYs from becoming active before they have been fully
initialized. For more information, see "Configuration" on page 2-24. Alternatively the COMA_MODE pin
may be connected low (ground) so that the PHYs are fully active once out of reset.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 24


## **3 Registers**

This section provides information about how to configure the VSC8514-11 device using its internal
memory registers and the management interface. The registers marked reserved and factory test should
not be read or written to, because doing so may produce undesired effects.


The default value documented for registers is based on the value at reset; however, in some cases, that
value may change immediately after reset.


The access type for each register is shown using the following abbreviations:


           - RO: Read Only


           - ROCR: Read Only, Clear on Read


           - RO/LH: Read Only, Latch High


           - RO/LL: Read Only, Latch Low


           - RW: Read and Write


           - RWSC: Read Write Self Clearing


The VSC8514-11 device uses several different types of registers:


           - IEEE Clause 22 device registers with addresses from 0 to 31


           - Three pages of extended registers with addresses from 16E1–30E1, 16E2–30E2, and 16E3–
30E3


           - General-purpose registers with addresses from 0G to 30G


           - IEEE Clause 45 devices registers accessible through the Clause 22 registers 13 and 14 to
support IEEE 802.3az energy efficient Ethernet registers


The following illustration shows the relationship between the device registers and their address spaces.


_**Figure 16 •**_ **Register Space Diagram**



0

1

2

3

.

.

13.

14

15


16

17

18

19

.

.

.

.

30.


31



































_**Reserved Registers**_


For main registers 16–31, extended registers 16E1–30E1, 16E2–30E2, 16E3–30E3, and general
purpose registers 0G–30G, any bits marked as Reserved should be processed as read-only and their
states as undefined.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 25


Register and Bit Conventions


_**Reserved Bits**_


In writing to registers with reserved bits, use a read-modify-then-write technique, where the entire
register is read but only the intended bits to be changed are modified. Reserved bits cannot be changed
and their read state cannot be considered static or unchanging.

#### **3.1 Register and Bit Conventions**


Registers are referred to by their address and bit number in decimal notation. A range of bits is indicated
with a colon. For example, a reference to address 26, bits 15 through 14 is shown as 26.15:14.


A register with an E and a number attached (example 27E1) means it is a register contained within
extended register page number 1. A register with a G attached (example 13G) means it is a GPIO page
register.


Bit numbering follows the IEEE standard with bit 15 being the most significant bit and bit 0 being the least
significant bit.

#### **3.2 IEEE 802.3 and Main Registers**


In the VSC8514-11 device, the page space of the standard registers consists of the IEEE 802.3 standard
registers and the Microsemi standard registers. The following table lists the names of the registers
associated with the addresses as specified by IEEE 802.3.


_**Table 11 •**_ **IEEE 802.3 Registers**


**Address** **Name**


0 Mode Control


1 Mode Status


2 PHY Identifier 1


3 PHY Identifier 2


4 Autonegotiation Advertisement


5 Autonegotiation Link Partner Ability


6 Autonegotiation Expansion


7 Autonegotiation Next-Page Transmit


8 Autonegotiation Link Partner Next-Page Receive


9 1000BASE-T Control


10 1000BASE-T Status


11–12 Reserved


13 Clause 45 Access Registers from IEEE 802.3
Table 22-6 and 22.24.3.11-12 and Annex 22D


14 Clause 45 Access Registers from IEEE 802.3
Table 22-6 and 22.24.3.11-12 and Annex 22D


15 1000BASE-T Status Extension 1


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 26


IEEE 802.3 and Main Registers


The following table lists the names of the registers in the main page space of the device. These registers
are accessible only when register address 31 is set to 0x0000.


_**Table 12 •**_ **Main Registers**


**Address** **Name**


16 100BASE-TX status extension


17 1000BASE-T status extension 2


18 Bypass control


19 Error Counter 1


20 Error Counter 2


21 Error Counter 3


22 Extended control and status


23 Extended PHY control 1


24 Extended PHY control 2


25 Interrupt mask


26 Interrupt status


27 Reserved


28 Auxiliary control and status


29 LED mode select


30 LED behavior


31 Extended register page access

##### **3.2.1 Mode Control**


The device register at memory address 0 controls several aspects of VSC8514-11 functionality. The
following table shows the available bit settings in this register and what they control.


_**Table 13 •**_ **Mode Control, Address 0 (0x00)**


**Bit** **Name** **Access Description** **Default**



15 Software reset R/W Self-clearing. Restores all serial management
interface (SMI) registers to default state,
except for sticky and super-sticky bits.


1: Reset asserted.


0: Reset de-asserted. Wait [X] after setting this
bit to initiate another SMI register access.


14 Loopback R/W 1: Loopback enabled.


0: Loopback disabled. When loop back is
enabled, the device functions at the current
speed setting and with the current duplex
mode setting (bits 6, 8, and 13 of this register).


13 Forced speed selection R/W Least significant bit. MSB is bit 6.
LSB

00: 10 Mbps.


01: 100 Mbps.


10: 1000 Mbps.


11: Reserved.



0


0


0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 27


IEEE 802.3 and Main Registers


_**Table 13 •**_ **Mode Control, Address 0 (0x00)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



12 Autonegotiation enable R/W 1: Autonegotiation enabled.


0: Autonegotiation disabled.



1



11 Power-down R/W 1: Power-down enabled. 0


10 Isolate R/W 1: Disable MAC interface outputs and ignore 0
MAC interface inputs.



9 Restart autonegotiation R/W Self-clearing bit.


1: Restart autonegotiation on media interface.


8 Duplex R/W 1: Full-duplex.


0: Half-duplex.



0


0



7 Collision test enable R/W 1: Collision test enabled. 0



6 Forced speed selection R/W Most significant bit. LSB is bit 13. [(1)]
MSB

00: 10 Mbps.


01: 100 Mbps.


10: 1000 Mbps.


11: Reserved.



10



5 Reserved RO Reserved 0


4:0 Reserved Reserved. 00000


_1. Before selecting the 1000 Mbps forced speed mode, manually configure the PHY as master or_
_slave by setting bit 11 in register 9 (1000BASE-T Control). Each time the link drops, the PHY_
_needs to be powered down manually to enable it to link up again using the master/slave setting_
_specified in register 9.11._

##### **3.2.2 Mode Status**


The register at address 1 in the device main registers space allows you to read the currently enabled
mode setting. The following table shows possible readouts of this register.


_**Table 14 •**_ **Mode Status, Address 1 (0x01)**


**Bit** **Name** **Access Description** **Default**


15 100BASE-T4 capability RO 1: 100BASE-T4 capable. 0


14 100BASE-TX FDX capability RO 1: 100BASE-TX FDX capable. 1


13 100BASE-TX HDX capability RO 1: 100BASE-TX HDX capable. 1


12 10BASE-T FDX capability RO 1: 10BASE-T FDX capable. 1


11 10BASE-T HDX capability RO 1: 10BASE-T HDX capable. 1


10 100BASE-T2 FDX capability RO 1: 100BASE-T2 FDX capable. 0


9 100BASE-T2 HDX capability RO 1: 100BASE-T2 HDX capable. 0


8 Extended status enable RO 1: Extended status information present in 1
register 15.


7 Reserved RO Reserved. 1



6 Preamble suppression RO 1: MF preamble can be suppressed.
capability 0: MF required.



1



5 Autonegotiation complete RO 1: Autonegotiation complete. 0


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 28


IEEE 802.3 and Main Registers


_**Table 14 •**_ **Mode Status, Address 1 (0x01)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



4 Remote fault RO Latches high.


1: Far-end fault detected.



0



3 Autonegotiation capability RO 1: Autonegotiation capable. 1



2 Link status RO Latches low.


1: Link is up.


1 Jabber detect RO Latches high.


1: Jabber condition detected.



0


0



0 Extended capability RO 1: Extended register capable. 1

##### **3.2.3 Device Identification**


All 16 bits in both register 2 and register 3 in the VSC8514-11 device are used to provide information
associated with aspects of the device identification. The following tables list the expected readouts.


_**Table 15 •**_ **Identifier 1, Address 2 (0x02)**


**Bit** **Name** **Access Description** **Default**


15:0 Organizationally unique identifier RO OUI most significant bits (3:18) 0×0007
(OUI)


_**Table 16 •**_ **Identifier 2, Address 3 (0x03)**


**Bit** **Name** **Access Description** **Default**


15:10 OUI RO OUI least significant bits (19:24) 000001


9:4 Microsemi model number RO VSC8514 (0x27) 100111


3:0 Device revision number RO Revision A 0000

##### **3.2.4 Autonegotiation Advertisement**


The bits in address 4 in the main registers space control the VSC8514-11 ability to notify other devices of
the status of its autonegotiation feature. The following table shows the available settings and readouts.


_**Table 17 •**_ **Device Autonegotiation Advertisement, Address 4 (0x04)**


**Bit** **Name** **Access Description** **Default**


15 Next page transmission request R/W 1: Request enabled 0


14 Reserved RO Reserved 0


13 Transmit remote fault R/W 1: Enabled 0


12 Reserved R/W Reserved 0


11 Advertise asymmetric pause R/W 1: Advertises asymmetric pause 0


10 Advertise symmetric pause R/W 1: Advertises symmetric pause 0


9 Advertise100BASE-T4 R/W 1: Advertises 100BASE-T4 0


8 Advertise100BASE-TX FDX R/W 1: Advertise 100BASE-TX FDX 1


7 Advertise100BASE-TX HDX R/W 1: Advertises 100BASE-TX HDX 1


6 Advertise10BASE-T FDX R/W 1: Advertises 10BASE-T FDX 1


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 29


IEEE 802.3 and Main Registers


_**Table 17 •**_ **Device Autonegotiation Advertisement, Address 4 (0x04)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


5 Advertise10BASE-T HDX R/W 1: Advertises 10BASE-T HDX 1


4:0 Advertise selector R/W 00001

##### **3.2.5 Link Partner Autonegotiation Capability**


The bits in main register 5 can be used to determine if the Cat5 link partner (LP) used with the
VSC8514-11 device is compatible with the autonegotiation functionality.


_**Table 18 •**_ **Autonegotiation Link Partner Ability, Address 5 (0x05)**


**Bit** **Name** **Access Description** **Default**


15 LP next page transmission request RO 1: Requested 0


14 LP acknowledge RO 1: Acknowledge 0


13 LP remote fault RO 1: Remote fault 0


12 Reserved RO Reserved 0


11 LP advertise asymmetric pause RO 1: Capable of asymmetric pause 0


10 LP advertise symmetric pause RO 1: Capable of symmetric pause 0


9 LP advertise 100BASE-T4 RO 1: Capable of 100BASE-T4 0


8 LP advertise 100BASE-TX FDX RO 1: Capable of 100BASE-TX FDX 0


7 LP advertise 100BASE-TX HDX RO 1: Capable of 100BASE-TX HDX 0


6 LP advertise 10BASE-T FDX RO 1: Capable of 10BASE-T FDX 0


5 LP advertise 10BASE-T HDX RO 1: Capable of 10BASE-T HDX 0


4:0 LP advertise selector RO 00000

##### **3.2.6 Autonegotiation Expansion**


The bits in main register 6 work together with those in register 5 to indicate the status of the LP
autonegotiation functioning. The following table shows the available settings and readouts.


_**Table 19 •**_ **Autonegotiation Expansion, Address 6 (0x06)**


**Bit** **Name** **Access Description** **Default**


15:5 Reserved RO Reserved. All zeros



4 Parallel detection fault RO This bit latches high.


1: Parallel detection fault.



0



3 LP next page capable RO 1: LP is next page capable. 0


2 Local PHY next page capable RO 1: Local PHY is next page capable. 1



1 Page received RO This bit latches low.


1: New page is received.



0



0 LP is autonegotiation capable RO 1: LP is capable of autonegotiation. 0


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 30


IEEE 802.3 and Main Registers

##### **3.2.7 Transmit Autonegotiation Next Page**


The settings in register 7 in the main registers space provide information about the number of pages in
an autonegotiation sequence. The following table shows the settings available.


_**Table 20 •**_ **Autonegotiation Next Page Transmit, Address 7 (0x07)**


**Bit** **Name** **Access Description** **Default**


15 Next page R/W 1: More pages follow 0


14 Reserved RO Reserved 0



13 Message page R/W 1: Message page


0: Unformatted page


12 Acknowledge 2 R/W 1: Complies with request


0: Cannot comply with request



1


0



11 Toggle RO 1: Previous transmitted LCW = 0 0: 0
Previous transmitted LCW = 1


10:0 Message/unformatted code R/W 00000000001

##### **3.2.8 Autonegotiation Link Partner Next Page Receive**


The bits in register 8 of the main register space work together with register 7 to determine certain aspects
of the LP autonegotiation. The following table shows the possible readouts.


_**Table 21 •**_ **Autonegotiation LP Next Page Receive, Address 8 (0x08)**


**Bit** **Name** **Access Description** **Default**


15 LP next page RO 1: More pages follow 0


14 Acknowledge RO 1: LP acknowledge 0



13 LP message page RO 1: Message page


0: Unformatted page



0



12 LP acknowledge 2 RO 1: LP complies with request 0



11 LP toggle RO 1: Previous transmitted LCW = 0


0: Previous transmitted LCW = 1



0



10:0 LP message/unformatted code RO All zeros

##### **3.2.9 1000BASE-T Control**


The VSC8514-11 device's 1000BASE-T functionality is controlled by the bits in register 9 of the main
register space. The following table shows the settings and readouts available.


_**Table 22 •**_ **1000BASE-T Control, Address 9 (0x09)**


**Bit** **Name** **Access Description** **Default**



15:13 Transmitter test mode R/W 000: Normal


001: Mode 1: Transmit waveform test


010: Mode 2: Transmit jitter test as master


011: Mode 3: Transmit jitter test as slave


100: Mode 4: Transmitter distortion test


101–111: Reserved



000



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 31


IEEE 802.3 and Main Registers


_**Table 22 •**_ **1000BASE-T Control, Address 9 (0x09)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


12 Master/slave manual R/W 1: Master/slave manual configuration enabled 0
configuration



11 Master/slave value R/W This register is only valid when bit 9.12 is set
to 1.


1: Configure PHY as master during
negotiation


0: Configure PHY as slave during negotiation


10 Port type R/W 1: Multi-port device


0: Single-port device



0


1



9 1000BASE-T FDX R/W 1: PHY is 1000BASE-T FDX capable 1
capability


8 1000BASE-T HDX R/W 1: PHY is 1000BASE-T HDX capable 1
capability


7:0 Reserved R/W Reserved 0x00


**Note** Transmitter test mode (bits 15:13) operates in the manner described in IEEE 802.3 section
40.6.1.1.2. When using any of the transmitter test modes, the automatic media sense feature must be
disabled. For more information, see "Extended PHY Control Set 2" on page 3-38.

##### **3.2.10 1000BASE-T Status**


The bits in register 10 of the main register space can be read to obtain the status of the 1000BASE-T
communications enabled in the device. The following table shows the readouts.


_**Table 23 •**_ **1000BASE-T Status, Address 10 (0x0A)**


**Bit** **Name** **Access Description** **Default**



15 Master/slave RO This bit latches high.
configuration fault 1: Master/slave configuration fault detected


0: No master/slave configuration fault detected


14 Master/slave RO 1: Local PHY configuration resolved to master
configuration resolution 0: Local PHY configuration resolved to slave



0


1



13 Local receiver status RO 1: Local receiver is operating normally 0


12 Remote receiver status RO 1: Remote receiver OK 0


11 LP 1000BASE-T FDX RO 1: LP 1000BASE-T FDX capable 0
capability


10 LP 1000BASE-T HDX RO 1: LP 1000BASE-T HDX capable 0
capability


9:8 Reserved RO Reserved 00


7:0 Idle error count RO Self-clearing register 0x00


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 32


IEEE 802.3 and Main Registers

##### **3.2.11 MMD Access Control Register**


The bits in register 13 of the main register space are a window to the EEE registers as defined in
IEEE 802.3az Clause 45.


_**Table 24 •**_ **MMD EEE Access, Address 13 (0x0D)**


**Bit** **Name** **Access Description**


15:14 Function R/W 00: Address


01: Data, no post increment


10: Data, post increment for read and write


11: Data, post increment for write only


13:5 Reserved R/W Reserved


4:0 DVAD R/W Device address as defined in IEEE 802.3az table 45–1

##### **3.2.12 MMD Address or Data Register**


The bits in register 14 of the main register space are a window to the EEE registers as defined in
IEEE 802.3az Clause 45.


_**Table 25 •**_ **MMD Address or Data Register, Address 14 (0x0E)**


**Bit** **Name** **Access Description**


15:0 Register Address/Data R/W When register 13.15:14 = 2'b00, address of register of
the device that is specified by 13.4:0. Otherwise, the
data to be written to or read from the register.

##### **3.2.13 1000BASE-T Status Extension 1**


Register 15 provides additional information about the operation of the device 1000BASE-T
communications. The following table shows the readouts available.


_**Table 26 •**_ **1000BASE-T Status Extension 1, Address 15 (0x0F)**


**Bit** **Name** **Access Description** **Default**


15:14 Reserved RO Reserved 0


13 1000BASE-T FDX capability RO 1: PHY is 1000BASE-T FDX capable 1


12 1000BASE-T HDX capability RO 1: PHY is 1000BASE-T HDX capable 1


11:0 Reserved RO Reserved 0x000

##### **3.2.14 100BASE-TX Status Extension**


Register 16 in the main registers page space of the VSC8514-11 device provides additional information
about the status of the device's 100BASE-TX operation.


_**Table 27 •**_ **100BASE-TX Status Extension, Address 16 (0x10)**


**Bit** **Name** **Access Description** **Default**


15 100BASE-TX Descrambler RO 1: Descrambler locked 0



14 100BASE-TX lock error RO Self-clearing bit.


1: Lock error detected



0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 33


IEEE 802.3 and Main Registers


_**Table 27 •**_ **100BASE-TX Status Extension, Address 16 (0x10)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



13 100BASE-TX disconnect state RO Self-clearing bit.


1: PHY 100BASE-TX link disconnect

detected



0



12 100BASE-TX current link status RO 1: PHY 100BASE-TX link active 0



11 100BASE-TX receive error RO Self-clearing bit.


1: Receive error detected


10 100BASE-TX transmit error RO Self-clearing bit.


1: Transmit error detected


9 100BASE-TX SSD error RO Self-clearing bit.


1: Start-of-stream delimiter error

detected


8 100BASE-TX ESD error RO Self-clearing bit.


1: End-of-stream delimiter error

detected


7:0 Reserved RO Reserved

##### **3.2.15 1000BASE-T Status Extension 2**



0


0


0


0



The second status extension register is at address 17 in the device main registers space. It provides
information about another set of parameters associated with 1000BASE-T communications. For
information about the first status extension register, see Table 26 on page 3-33.


_**Table 28 •**_ **1000BASE-T Status Extension 2, Address 17 (0x11)**


**Bit** **Name** **Access Description** **Default**


15 1000BASE-T descrambler RO 1: Descrambler locked. 0



14 1000BASE-T lock error RO Self-clearing bit.


1: Lock error detected


13 1000BASE-T disconnect state RO Self-clearing bit.


1: PHY 1000BASE-T link disconnect

detected



0


0



12 1000BASE-T current link RO 1: PHY 1000BASE-T link active 0

status



11 1000BASE-T receive error RO Self-clearing bit.


1: Receive error detected


10 1000BASE-T transmit error RO Self-clearing bit.


1: Transmit error detected


9 1000BASE-T SSD error RO Self-clearing bit.


1: Start-of-stream delimiter error detected


8 1000BASE-T ESD error RO Self-clearing bit.


1: End-of-stream delimiter error detected


7 1000BASE-T carrier extension RO Self-clearing bit.

error 1: Carrier extension error detected



0


0


0


0


0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 34


IEEE 802.3 and Main Registers


_**Table 28 •**_ **1000BASE-T Status Extension 2, Address 17 (0x11)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


6 Non-compliant BCM5400 RO 1: Non-compliant BCM5400 link partner 0
detected detected


5 MDI crossover error RO 1: MDI crossover error was detected 0


4:0 Reserved RO Reserved

##### **3.2.16 Bypass Control**


The bits in this register control aspects of functionality in effect when the device is disabled for the
purpose of traffic bypass. The following table shows the settings available.


_**Table 29 •**_ **Bypass Control, Address 18 (0x12)**


**Bit** **Name** **Access Description** **Default**


15 Transmit disable R/W 1: PHY transmitter disabled 0


14 4B5B encoder/decoder R/W 1: Bypass 4B/5B encoder/decoder 0


13 Scrambler R/W 1: Bypass scrambler 0


12 Descrambler R/W 1: Bypass descrambler 0


11 PCS receive R/W 1: Bypass PCS receiver 0


10 PCS transmit R/W 1: Bypass PCS transmit 0


9 LFI timer R/W 1: Bypass Link Fail Inhibit (LFI) timer 0


8 Reserved RO Reserved



7 HP Auto-MDIX at forced R/W Sticky bit.
10/100 1: Disable HP Auto-MDIX at forced 10/100


speeds


6 Non-compliant BCM5400 R/W Sticky bit.
detect disable 1: Disable non-compliant BCM5400

detection



1


0


0


0


1



5 Disable pair swap correction
(HP Auto-MDIX when
autonegotiation enabled)



R/W Sticky bit.


1: Disable the automatic pair swap
correction



4 Disable polarity correction R/W Sticky bit.


1: Disable polarity inversion correction on
each subchannel


3 Parallel detect control R/W Sticky bit.


1: Do not ignore advertised ability


0: Ignore advertised ability



2 Pulse shaping filter R/W 1: Disable pulse shaping filter 0



1 Disable automatic

1000BASE-T next page
exchange



R/W Sticky bit.


1: Disable automatic 1000BASE T next

page exchanges



0



0 Reserved RO Reserved


**Note** If bit 18.1 is set to 1 in this register, automatic exchange of next pages is disabled, and control is
returned to the user through the SMI after the base page is exchanged. The user then must send the


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 35


IEEE 802.3 and Main Registers


correct sequence of next pages to the link partner, determine the common capabilities, and force the
device into the correct configuration following the successful exchange of pages.

##### **3.2.17 Error Counter 1**


The bits in register 19 provide an error counter. The following table shows the settings available.


_**Table 30 •**_ **Extended Control and Status, Address 19 (0x13)**


**Bit** **Name** **Access Description** **Default**


15:8 Reserved RO Reserved.


7:0 100/1000BASE-TX RO 8-bit counter that saturates when it reaches 0x00

receive error counter 255. These bits are self-clearing when read.

##### **3.2.18 Error Counter 2**


The bits in register 20 provide an error counter. The following table shows the settings available.


_**Table 31 •**_ **Extended Control and Status, Address 20 (0x14)**


**Bit** **Name** **Access Description** **Default**


15:8 Reserved RO Reserved.


7:0 100/1000BASE-TX RO 8-bit counter that saturates when it reaches 0x00

false carrier counter 255. These bits are self-clearing when read.

##### **3.2.19 Error Counter 3**


The bits in register 21 provide an error counter. The following table shows the settings available.


_**Table 32 •**_ **Extended Control and Status, Address 21 (0x15)**


**Bit** **Name** **Access Description** **Default**


15:8 Reserved RO Reserved.


7:0 Copper media link RO 8-bit counter that saturates when it reaches 0x00
disconnect counter 255. These bits are self-clearing when read.

##### **3.2.20 Extended Control and Status**


The bits in register 22 provide additional device control and readouts. The following table shows the
settings available.


_**Table 33 •**_ **Extended Control and Status, Address 22 (0x16)**


**Bit** **Name** **Access Description** **Default**



15 Force 10BASE-T link high R/W Sticky bit.


1: Bypass link integrity test


0: Enable link integrity test


14 Jabber detect disable R/W Sticky bit.


1: Disable jabber detect


13 Disable 10BASE-T echo R/W Sticky bit.


1: Disable 10BASE-T echo



0


0


1



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 36


IEEE 802.3 and Main Registers


_**Table 33 •**_ **Extended Control and Status, Address 22 (0x16)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



12 Disable SQE mode R/W Sticky bit.


1: Disable SQE mode


11:10 10BASE-T squelch control R/W Sticky bit.


00: Normal squelch


01: Low squelch


10: High squelch


11: Reserved


9 Sticky reset enable R/W Super-sticky bit.


1: Enabled


8 EOF Error RO This bit is self-clearing.


1: EOF error detected


7 10BASE-T disconnect state RO This bit is self-clearing.


1: 10BASE-T link disconnect detected



1


00


1


0


0



6 10BASE-T link status RO 1: 10BASE-T link active 0


5:1 Reserved RO Reserved



0 SMI broadcast write R/W Sticky bit.


1: Enabled


The following information applies to the extended control and status bits:



0




   - When bit 22.15 is set, the link integrity state machine is bypassed and the PHY is forced into a
link pass status.


   - When bits 22.11:10 are set to 00, the squelch threshold levels are based on the IEEE standard for
10BASE-T. When set to 01, the squelch level is decreased, which can improve the bit error rate
performance on long loops. When set to 10, the squelch level is increased and can improve the
bit error rate in high-noise environments.


   - When bit 22.9 is set, all sticky register bits retain their values during a software reset. Clearing this
bit causes all sticky register bits to change to their default values upon software reset. Supersticky bits retain their values upon software reset regardless of the setting of bit 22.9.


   - When bit 22.0 is set, if a write to any PHY register (registers 0–31, including extended registers),
the same write is broadcast to all PHYs. For example, if bit 22.0 is set to 1 and a write to PHY0 is
executed (register 0 is set to 0x1040), all PHYs' register 0s are set to 0x1040. Disabling this bit
restores normal PHY write operation. Reads are still possible when this bit is set, but the value
that is read corresponds only to the particular PHY being addressed.

##### **3.2.21 Extended PHY Control Set 1**


The following table shows the settings available.


_**Table 34 •**_ **Extended PHY Control 1, Address 23 (0x17)**


**Bit** **Name** **Access Description** **Default**


15:11 Reserved R/W Reserved 0



10:8 Media operating mode R/W Super-sticky bits


000: Cat5 copper only


7:4 Reserved RO Reserved



000



3 Far-end loopback mode R/W 1: Enabled 0


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 37


IEEE 802.3 and Main Registers


_**Table 34 •**_ **Extended PHY Control 1, Address 23 (0x17)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


2:0 Reserved RO Reserved


**Note** After configuring bits 11:8 of the extended PHY control register set 1, a software reset (register 0,
bit 15) must be written to change the device operating mode. On read, these bits only indicate the actual
operating mode and not the pending operating mode setting before a software reset has taken place.

##### **3.2.22 Extended PHY Control Set 2**


The second set of extended controls is located in register 24 in the main register space for the device.
The following table shows the settings and readouts available.


_**Table 35 •**_ **Extended PHY Control 2, Address 24 (0x18)**


**Bit** **Name** **Access Description** **Default**



15:13 100BASE-TX edge R/W Sticky bit.
rate control 011: +5 edge rate (slowest)


010: +4 edge rate


001: +3 edge rate


000: +2 edge rate


111: +1 edge rate


110: Default edge rate


101: –1 edge rate


100: –2 edge rate (fastest)


12 PICMG 2.16 reduced R/W Sticky bit.
power mode 1: Enabled


11:6 Reserved RO Reserved


5:4 Jumbo packet mode R/W Sticky bit.


00: Normal IEEE 1.5 kB packet length


01: 9 kB jumbo packet length (12 kB with
60 ppm or better reference clock)


10: 12 kB jumbo packet length (16 kB with
70 ppm or better reference clock)


11: Reserved


3:1 Reserved RO Reserved



001


0


00



0 1000BASE-T R/W 1: Enabled 0

connector loopback


**Note** When bits 5:4 are set to jumbo packet mode, the default maximum packet values are based on
100 ppm driven reference clock to the device. Controlling the ppm offset between the MAC and the PHY
as specified in the bit description results in a higher jumbo packet length.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 38


IEEE 802.3 and Main Registers

##### **3.2.23 Interrupt Mask**


These bits control the device interrupt mask. The following table shows the settings available.


_**Table 36 •**_ **Interrupt Mask, Address 25 (0x19)**


**Bit** **Name** **Access Description** **Default**


15 MDINT interrupt status enable R/W Sticky bit. 1: Enabled. 0


14 Speed state change mask R/W Sticky bit. 1: Enabled. 0


13 Link state change mask R/W Sticky bit. 1: Enabled. 0


12 FDX state change mask R/W Sticky bit. 1: Enabled. 0


11 Autonegotiation error mask R/W Sticky bit. 1: Enabled. 0


10 Autonegotiation complete mask R/W Sticky bit. 1: Enabled. 0


9 Inline-powered device (PoE) detect mask R/W Sticky bit. 1: Enabled. 0


8 Symbol error interrupt mask R/W Sticky bit. 1: Enabled. 0


7 Reserved RO Reserved. 0


6 TX FIFO over/underflow interrupt mask R/W Sticky bit. 1: Enabled. 0


5 RX FIFO over/underflow interrupt mask R/W Sticky bit. 1: Enabled. 0


4 Reserved RO Reserved. 0


3 False carrier interrupt mask R/W Sticky bit. 1: Enabled. 0


2 Link speed downshift detect mask R/W Sticky bit. 1: Enabled. 0


1 Master/Slave resolution error mask R/W Sticky bit. 1: Enabled. 0


0 RX_ER interrupt mask R/W Sticky bit. 1: Enabled. 0


**Note** When bit 25.15 is set, the MDINT pin is enabled. When enabled, the state of this pin reflects the
state of bit 26.15. Clearing this bit only inhibits the MDINT pin from being asserted. Also, before enabling
this bit, read register 26 to clear any previously inactive interrupts pending that will cause bit 25.15 to be
set.

##### **3.2.24 Interrupt Status**


The status of interrupts already written to the device is available for reading from register 26 in the main
registers space. The following table shows the expected readouts.


_**Table 37 •**_ **Interrupt Status, Address 26 (0x1A)**


**Bit** **Name** **Access Description** **Default**


15 Interrupt status RO Self-clearing bit. 1: Interrupt pending. 0


14 Speed state change status RO Self-clearing bit. 1: Interrupt pending. 0


13 Link state change status RO Self-clearing bit. 1: Interrupt pending. 0


12 FDX state change status RO Self-clearing bit. 1: Interrupt pending. 0


11 Autonegotiation error status RO Self-clearing bit. 1: Interrupt pending. 0


10 Autonegotiation complete status RO Self-clearing bit. 1: Interrupt pending. 0


9 Inline-powered device detect RO Self-clearing bit. 1: Interrupt pending. 0
status


8 Symbol error status RO Self-clearing bit. 1: Interrupt pending. 0


7 Reserved RO Reserved. 0


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 39


IEEE 802.3 and Main Registers


_**Table 37 •**_ **Interrupt Status, Address 26 (0x1A)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


6 TX FIFO over/underflow detect RO Self-clearing bit. 1: Interrupt pending. 0
status


5 RX FIFO over/underflow detect RO Self-clearing bit. 1: Interrupt pending. 0
status


4 Reserved RO Reserved. 0


3 False carrier interrupt status RO Self-clearing bit. 1: Interrupt pending. 0


2 Link speed downshift detect RO Self-clearing bit. 1: Interrupt pending. 0
status


1 Master/Slave resolution error RO Self-clearing bit. 1: Interrupt pending. 0
status


0 RX_ER interrupt status RO Self-clearing bit. 1: Interrupt pending. 0


The following information applies to the interrupt status bits:


           - All set bits in this register are cleared after being read (self-clearing). If bit 26.15 is set, the cause
of the interrupt can be read by reading bits 26.14:0.


           - For bits 26.14 and 26.12, bit 0.12 must be set for this interrupt to assert.


           - For bit 26.2, bits 4.8:5 must be set for this interrupt to assert.


           - For bit 26.0, this interrupt will not occur when RX_ER is used for carrier-extension decoding of a
link partner's data transmission.

##### **3.2.25 Device Auxiliary Control and Status**


Register 28 provides control and status information for several device functions not controlled or
monitored by other device registers. The following table shows the settings available and the expected
readouts.


_**Table 38 •**_ **Auxiliary Control and Status, Address 28 (0x1C)**


**Bit** **Name** **Access Description** **Default**


15 Autonegotiation complete RO Duplicate of bit 1.5 0


14 Autonegotiation disabled RO Inverted duplicate of bit 0.12 0


13 HP Auto-MDIX crossover RO 1: HP Auto-MDIX crossover performed 0
indication internally


12 CD pair swap RO 1: CD pairs are swapped 0


11 A polarity inversion RO 1: Polarity swap on pair A 0


10 B polarity inversion RO 1: Polarity swap on pair B 0


9 C polarity inversion RO 1: Polarity swap on pair C 0


8 D polarity inversion RO 1: Polarity swap on pair D 0



7 ActiPHY link status time-out R/W Sticky bit. Bits 7 and 2 are part of the
control [1] ActiPHY Link Status time-out control. Bit 7
is the MSB.


00: 2.3 second


01: 3.3 seconds


10: 4.3 seconds


11: 5.3 seconds



0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 40


IEEE 802.3 and Main Registers


_**Table 38 •**_ **Auxiliary Control and Status, Address 28 (0x1C)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



6 ActiPHY mode enable R/W Sticky bit.


1: Enabled


5 FDX status RO 1: Full-duplex


0: Half-duplex


4:3 Speed status RO 00: Speed is 10BASE-T


01: Speed is 100BASE-TX or 100BASE-FX


10: Speed is 1000BASE-T or 1000BASE-X


11: Reserved


2 ActiPHY link status time-out R/W Sticky bit. Bits 7 and 2 are part of the
control [0] ActiPHY Link Status time-out control. Bit 7
is the MSB.


00: 2.3 second


01: 3.3 seconds


10: 4.3 seconds


11: 5.3 seconds


1:0 Media mode status RO 00: No media selected


01: Copper media selected


10: Reserved


11: Reserved

##### **3.2.26 LED Mode Select**



0


00


0


1


00



The device LED outputs are controlled using the bits in register 29 of the main register space. The
following table shows the information needed to access the functionality of each of the outputs. For more
information about LED modes, see Table 4 on page 2-13.


_**Table 39 •**_ **LED Mode Select, Address 29 (0x1D)**


**Bit** **Name** **Access Description** **Default**


15:12 LED3 mode select R/W Sticky bit. Select from LED modes 0–15. 1000


11:8 LED2 mode select R/W Sticky bit. Select from LED modes 0–15. 0000


7:4 LED1 mode select R/W Sticky bit. Select from LED modes 0–15. 0010


3:0 LED0 mode select R/W Sticky bit. Select from LED modes 0–15. 0001

##### **3.2.27 LED Behavior**


The bits in register 30 control and enable you to read the status of the pulse or blink rate of the device
LEDs. The following table shows the settings you can write to the register or read from the register.


_**Table 40 •**_ **LED Behavior, Address 30 (0x1E)**


**Bit** **Name** **Access Description** **Default**


15:13 Reserved RO Reserved


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 41


IEEE 802.3 and Main Registers


_**Table 40 •**_ **LED Behavior, Address 30 (0x1E)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



12 LED pulsing enable R/W Sticky bit


0: Normal operation


1: LEDs pulse with a 5 kHz, programmable duty
cycle when active


11:10 LED blink/pulse- R/W Sticky bit
stretch rate 00: 2.5 Hz blink rate/400 ms pulse-stretch


01: 5 Hz blink rate/200 ms pulse-stretch


10: 10 Hz blink rate/100 ms pulse-stretch


11: 20 Hz blink rate/50 ms pulse-stretch


The blink rate selection for PHY0 globally sets
the rate used for all LED pins on all PHY ports


9 Reserved RO Reserved


8 LED3 pulse- R/W Sticky bit
stretch/blink select 1: Pulse-stretch


0: Blink


7 LED2 pulse- R/W Sticky bit
stretch/blink select 1: Pulse-stretch


0: Blink


6 LED1 pulse- R/W Sticky bit
stretch/blink select 1: Pulse-stretch


0: Blink


5 LED0 pulse- R/W Sticky bit
stretch/blink select 1: Pulse-stretch


0: Blink


4:2 Reserved RO Reserved


3 LED3 combine R/W Sticky bit
feature disable 0: Combine enabled (link/activity,

duplex/collision)


1: Disable combination (link only, duplex only)


2 LED2 combine R/W Sticky bit
feature disable 0: Combine enabled (link/activity,

duplex/collision)


1: Disable combination (link only, duplex only)


1 LED1 combine R/W Sticky bit
feature disable 0: Combine enabled (link/activity,

duplex/collision)


1: Disable combination (link only, duplex only)


0 LED0 combine R/W Sticky bit
feature disable 0: Combine enabled (link/activity,

duplex/collision)


1: Disable combination (link only, duplex only)


**Note** Bits 30.11:10 are active only in port 0 and affect the behavior of LEDs for all the ports.



0


01


0


0


0


0


0


0


0


0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 42


Extended Page 1 Registers

##### **3.2.28 Extended Page Access**


To provide functionality beyond the IEEE 802.3-specified registers and main device registers, the
VSC8514-11 device includes an extended set of registers that provide an additional 15 register spaces.


The register at address 31 controls the access to the extended registers for the VSC8514-11 device.
Accessing the GPIO page register space is similar to accessing the extended page registers. The
following table shows the settings available.


_**Table 41 •**_ **Extended/GPIO Register Page Access, Address 31 (0x1F)**


**Bit** **Name** **Access Description** **Default**



15:0 Extended/GPIO page R/W 0x0000: Register 16–30 accesses main register
register access space. Writing 0x0000 to register 31 restores the
main register access.


0x0001: Registers 16–30 access extended
register space 1


0x0002: Registers 16–30 access extended
register space 2


0x0003: Registers 16–30 access extended
register space 3


0x0010: Registers 0–30 access GPIO register

space

#### **3.3 Extended Page 1 Registers**



0x0000



To access the extended page 1 registers (16E1–30E1), enable extended register access by writing
0x0001 to register 31. Writing 0x0000 to register 31 restores the main register access.


When extended page 1 register access is enabled, reads and writes to registers 16–30 affect the
extended registers 16E1–30E1 instead of those same registers in the IEEE-specified register space.
Registers 0–15 are not affected by the state of the extended page register access.


_**Table 42 •**_ **Extended Registers Page 1 Space**


**Address** **Name**


16E1 Reserved


17E1 Reserved


18E1 Cu Media CRC good counter


19E1 Extended mode control


20E1 Extended PHY control 3 (ActiPHY)


21E1–22E1 Reserved


23E1 Extended PHY control 4 (PoE and CRC error counter)


24E1 VeriPHY 1


25E1 VeriPHY 2


26E1 VeriPHY 3


27E1–28E1 Reserved


29E1 Ethernet packet generator (EPG) 1


30E1 EPG 2


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 43


Extended Page 1 Registers

##### **3.3.1 Cu Media CRC Good Counter**


Register 18E1 makes it possible to read the contents of the CRC good counter for packets that are
received on the Cu media interface; the number of CRC routines that have executed successfully. The
following table shows the expected readouts.


_**Table 43 •**_ **Cu Media CRC Good Counter, Address 18E1 (0x12)**


**Bit** **Name** **Access Description** **Default**



15 Packet since last read RO Self-clearing bit.


1: Packet received since last read.


14 Reserved RO Reserved.


13:0 Cu Media CRC good RO Self-clearing bit. Counter containing the
counter contents number of packets with valid CRCs modulo
10,000; this counter does not saturate and
will roll over to zero on the next good packet
received after 9,999.

##### **3.3.2 Extended Mode Control**



0


0x000



Register 19E1 controls the LED and other chip modes. The following table shows the settings available.


_**Table 44 •**_ **Extended Mode Control, Address 19E1 (0x13)**


**Bit** **Name** **Access Description** **Default**


15:12 Reserved RO Reserved 0



11 LED Reset Blink Suppress R/W 1: Blink LEDs after COMA_MODE is
de-asserted


0: Suppress LED blink after
COMA_MODE is de-asserted



0



10:4 Reserved RO Reserved 0



3:2 Force MDI crossover R/W 00: Normal HP Auto-MDIX operation


01: Reserved


10: Copper media forced to MDI


11: Copper media forced MDI-X


1:0 Reserved RO Reserved

##### **3.3.3 ActiPHY Control**



00



Register 20E1 controls the device ActiPHY sleep timer, its wake-up timer, and its link speed downshifting
feature. The following table shows the settings available.


_**Table 45 •**_ **Extended PHY Control 3, Address 20E1 (0x14)**


**Bit** **Name** **Access Description** **Default**


15 Disable carrier extension R/W 1: Disable carrier extension in 1

SGMII/1000BASE-T copper links


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 44


Extended Page 1 Registers


_**Table 45 •**_ **Extended PHY Control 3, Address 20E1 (0x14)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



14:13 ActiPHY sleep timer R/W Sticky bit.


00: 1 second


01: 2 seconds


10: 3 seconds


11: 4 seconds


12:11 ActiPHY wake-up timer R/W Sticky bit.


00: 160 ms


01: 400 ms


10: 800 ms


11: 2 seconds


10 Reserved RO Reserved


9 PHY address reversal R/W Reverse PHY address


Enabling causes physical PHY 0 to have
address of 3, PHY 1 address of 2, PHY 2
address of 1, and PHY 3 address of 0.
Changing this bit to 1 should initially be
done from PHY 0 and changing to 0 from
PHY3


1: Enabled


0: Disabled


8 Reserved RO Valid only on PHY0


7:6 Media mode status RO 00: No media selected


01: Copper media selected


10: Reserved


11: Reserved


5 Enable 10BASE-T no R/W Sticky bit.
preamble mode 1: 10BASE-T will assert RX_DV indication

when data is presented to the receiver even
without a preamble preceding it


4 Enable link speed R/W Sticky bit.
autodownshift feature 1: Enable auto link speed downshift from

1000BASE-T


3:2 Link speed auto downshift R/W Sticky bit.
control 00: Downshift after 2 failed 1000BASE-T


autonegotiation attempts


01: Downshift after 3 failed 1000BASE-T

autonegotiation attempts


10: Downshift after 4 failed 1000BASE-T

autonegotiation attempts


11: Downshift after 5 failed 1000BASE-T

autonegotiation attempts


1 Link speed auto downshift RO 0: No downshift
status 1: Downshift is required or has occurred


0 Reserved RO Reserved



01


00


0


00


0


0


01


0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 45


Extended Page 1 Registers

##### **3.3.4 PoE and Miscellaneous Functionality**


The register at address 23E1 controls various aspects of inline-powering and the CRC error counter in
the VSC8514-11 device.


_**Table 46 •**_ **Extended PHY Control 4, Address 23E1 (0x17)**


**Bit** **Name** **Access Description** **Default**


15:11 PHY address RO PHY address; latched on reset



10 Inline-powered device R/W Sticky bit.
detection 1: Enabled


9:8 Inline-powered device RO Only valid when bit 10 is set.
detection status 00: Searching for devices


01: Device found; requires inline-power


10: Device found; does not require inline
power


11: Reserved


7:0 Cu Media CRC error RO Self-clearing bit
counter



0


00



RC error counter for packets received on the Cu media interface. The value saturates at 0xFF and
subsequently clears when read and restarts count 0x00.

##### **3.3.5 VeriPHY Control 1**


Register 24E1 in the extended register space provides control over the device VeriPHY diagnostics
features. There are three separate VeriPHY control registers. The following table shows the settings
available and describes the expected readouts.


_**Table 47 •**_ **VeriPHY Control Register 1, Address 24E1 (0x18)**


**Bit** **Name** **Access Description** **Default**



15 VeriPHY trigger R/W Self-clearing bit.


1: Triggers the VeriPHY algorithm and clears
when VeriPHY has completed. Settings in
registers 24E–26E become valid after this bit
clears.



0



14 VeriPHY valid RO 1: VeriPHY results in registers 24E–26E are 0
valid.


13:8 Pair A (1, 2) distance RO Loop length or distance to anomaly for pair A (1, 0x00
2).


7:6 Reserved RO Reserved.


5:0 Pair B (3, 6) distance RO Loop length or distance to anomaly for pair B (3, 0x00
6).


**Note** The resolution of the 6-bit length field is 3 meters.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 46


Extended Page 1 Registers

##### **3.3.6 VeriPHY Control 2**


The register at address 25E1 consists of the second of the three device registers that provide control
over VeriPHY diagnostics features. The following table shows the expected readouts.


_**Table 48 •**_ **VeriPHY Control Register 2, Address 25E1 (0x19)**


**Bit** **Name** **Access Description** **Default**


15:14 Reserved RO Reserved


13:8 Pair C (4, 5) distance RO Loop length or distance to anomaly for pair C 0x00
(4, 5)


7:6 Reserved RO Reserved


5:0 Pair D (7, 8) distance RO Loop length or distance to anomaly for pair D 0x00
(7, 8)


**Note** The resolution of the 6-bit length field is 3 meters.

##### **3.3.7 VeriPHY Control 3**


The register at address 26E1 consists of the third of the three device registers that provide control over
VeriPHY diagnostics features. Specifically, this register provides information about the termination status
(fault condition) for all link partner pairs. The following table shows the expected readouts.


_**Table 49 •**_ **VeriPHY Control Register 3, Address 26E1 (0x1A)**


**Bit** **Name** **Access Description** **Default**


15:12 Pair A (1, 2) termination status RO Termination fault for pair A (1, 2) 0x00


11:8 Pair B (3, 6) termination status RO Termination fault for pair B (3, 4) 0x00


7:4 Pair C (4, 5) termination status RO Termination fault for pair C (4, 5) 0x00


3:0 Pair D (7, 8) termination status RO Termination fault for pair D (7, 8) 0x00


The following table shows the meanings for the various fault codes.


_**Table 50 •**_ **VeriPHY Control Register 3 Fault Codes**


**Code** **Denotes**


0000 Correctly terminated pair


0001 Open pair


0010 Shorted pair


0100 Abnormal termination


1000 Cross-pair short to pair A


1001 Cross-pair short to pair B


1010 Cross-pair short to pair C


1011 Cross-pair short to pair D


1100 Abnormal cross-pair coupling with pair A


1101 Abnormal cross-pair coupling with pair B


1110 Abnormal cross-pair coupling with pair C


1111 Abnormal cross-pair coupling with pair D


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 47


Extended Page 1 Registers

##### **3.3.8 Ethernet Packet Generator Control 1**


The EPG control register provides access to and control of various aspects of the EPG testing feature.
There are two separate EPG control registers. The following table shows the settings available in the first
register.


_**Table 51 •**_ **EPG Control Register 1, Address 29E1 (0x1D)**


**Bit** **Name** **Access Description** **Default**


15 EPG enable R/W 1: Enable EPG 0


14 EPG run or stop R/W 1: Run EPG 0



13 Transmission duration R/W 1: Continuous (sends in 10,000-packet
increments)


0: Send 30,000,000 packets and stop


12:11 Packet length R/W 00: 125 bytes


01: 64 bytes


10: 1518 bytes


11: 10,000 bytes (jumbo packet)


10 Interpacket gap R/W 1: 8,192 ns


0: 96 ns



0


0


0



9:6 Destination address R/W Lowest nibble of the 6-byte destination 0001
address


5:2 Source address R/W Lowest nibble of the 6-byte destination 0000
address



1 Payload type R/W 1: Randomly generated payload pattern


0: Fixed based on payload pattern



0


0



0 Bad frame check

sequence (FCS)
generation



R/W 1: Generate packets with bad FCS


0: Generate packets with good FCS



The following information applies to the EPG control number 1:


   - Do not run the EPG when the VSC8514-11 is device connected to a live network.


   - bit 29E1.13 (continuous EPG mode control): When enabled, this mode causes the device to send
continuous packets. When disabled, the device continues to send packets only until it reaches the
next 10,000-packet increment mark. It then ceases to send packets.


   - The 6-byte destination address in bits 9:6 is assigned one of 16 addresses in the range of 0xFF
FF FF FF FF F0 through 0xFF FF FF FF FF FF.


   - The 6-byte source address in bits 5:2 is assigned one of 16 addresses in the range of 0xFF FF FF
FF FF F0 through 0xFF FF FF FF FF FF.


   - If any of bits 13:0 are changed while the EPG is running (bit 14 is set to 1), bit 14 must be cleared
and then set back to 1 for the change to take effect and to restart the EPG.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 48


Extended Page 2 Registers

##### **3.3.9 Ethernet Packet Generator Control 2**


Register 30E1 consists of the second set of bits that provide access to and control over the various
aspects of the EPG testing feature. The following table shows the settings available.


_**Table 52 •**_ **EPG Control Register 2, Address 30E1 (0x1E)**


**Bit** **Name** **Access Description** **Default**


15:0 EPG packet payload R/W Data pattern repeated in the payload of 0x00
packets generated by the EPG


**Note** If any of bits 15:0 in this register are changed while the EPG is running (bit 14 of register 29E1 is
set to 1), that bit (29E1.14) must first be cleared and then set back to 1 for the change to take effect and
to restart the EPG.

#### **3.4 Extended Page 2 Registers**


To access the extended page 2 registers (16E2–30E2), enable extended register access by writing
0x0002 to register 31. For more information, see Table 41 on page 3-43.


When extended page 2 register access is enabled, reads and writes to registers 16–30 affect the
extended registers 16E2–30E2 instead of those same registers in the IEEE-specified register space.
Registers 0–15 are not affected by the state of the extended page register access.


Writing 0x0000 to register 31 restores the main register access.


The following table lists the addresses and register names in the extended register page 2 space. These
registers are accessible only when the device register 31 is set to 0x0002.


_**Table 53 •**_ **Extended Registers Page 2 Space**


**Address** **Name**


16E2 Cu PMD Transmit Control


17E2 EEE Control


18E2-30E2 Reserved

##### **3.4.1 Cu PMD Transmit Control**


The register at address 16E2 consists of the bits that provide control over the amplitude settings for the
transmit side Cu PMD interface. These bits provide the ability to make small adjustments in the signal
amplitude to compensate for minor variations in the magnetics from different vendors. Extreme caution
must be exercised when changing these settings from the default values as they have a direct impact on


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 49


Extended Page 2 Registers


the signal quality. Changing these settings also affects the linearity and harmonic distortion of the
transmitted signals. For help with changing these values, contact your Microsemi representative.


_**Table 54 •**_ **Cu PMD Transmit Control, Address 16E2 (0x10)**


**Bit** **Name** **Access Description** **Default**



15:12 1000BASE-T signal R/W 1000BASE-T signal amplitude
amplitude trim [(1)] 1111: -1.7%


1110: -2.6%


1101: -3.5%


1100: -4.4%


1011: -5.3%


1010: -7%


1001: -8.8%


1000: -10.6%


0111: 5.5%


0110: 4.6%


0101: 3.7%


0100: 2.8%


0011: 1.9%


0010: 1%


0001: 0.1%


0000: -0.8%


11:8 100BASE-TX signal R/W 100BASE-TX signal amplitude
amplitude trim [(2)] 1111: -1.7%


1110: -2.6%


1101: -3.5%


1100: -4.4%


1011: -5.3%


1010: -7%


1001: -8.8%


1000: -10.6%


0111 5.5%


0110: 4.6%


0101: 3.7%


0100: 2.8%


0011: 1.9%


0010: 1%


0001: 0.1%


0000: -0.8%



0000


0010



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 50


Extended Page 2 Registers


_**Table 54 •**_ **Cu PMD Transmit Control, Address 16E2 (0x10)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**



7:4 10BASE-T signal R/W 10BASE-T signal amplitude
amplitude trim [(3)] 1111: -7%


1110: -7.9%


1101: -8.8%


1100: -9.7%


1011: -10.6%


1010: -11.5%


1001: -12.4%


1000: -13.3%


0111: 0%


0110: -0.7%


0101: -1.6%


0100: -2.5%


0011: -3.4%


0010: -4.3%


0001: -5.2%


0000: -6.1%


3:0 10BASE-Te signal R/W 10BASE-Te signal amplitude
amplitude trim 1111: -30.45%


1110: -31.1%


1101: -31.75%


1100: -32.4%


1011: -33.05%


1010: -33.7%


1001: -34.35%


1000: -35%


0111: -25.25%


0110: -25.9%


0101: -26.55%


0100: -27.2%


0011: -27.85%


0010: -28.5%


0001: -29.15%


0000: -29.8%



1011


1110



_1. Changes to 1000BASE-T amplitude may result in side effects and hide issues due to a_
_questionable board design._

_2. Adjust 100BASE-TX to specific magnetics._

_3. Amplitude limited by VCC(2.5 V)._


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 51


Extended Page 3 Registers

##### **3.4.2 EEE Control**


The register at address 17E2 consists of the bits that provide additional control over the chip behavior in
energy efficient Ethernet (IEEE 802.3az) mode for debug and to allow interoperation with legacy MACs
that do not support IEEE 802.3az.


_**Table 55 •**_ **EEE Control, Address 17E2 (0x11)**


**Bit** **Name** **Access Description** **Default**


15 Enable 10BASE-Te R/W Enable energy efficient (IEEE 802.3az) 0
10BASE-Te operating mode.


14 Reserved RO Reserved. 0


13:10 Invert LED polarity R/W Invert polarity of LED[3:0]_[1:0] signals. Default 0000
is to drive an active low signal on the LED pins.


9:6 Reserved RO Reserved.



5 Enable 1000BASE-T R/W 1: Enable 1000BASE-T force mode to allow PHY

force mode to link-up in 1000BASE-T mode without forcing
master/slave when register 0, bit 6 and 13 are
set to 2’b10.


4 Force transmit LPI R/W 1: Enable the EPG to transmit LPI on the MDI

instead of normal idles when receiving normal
idles from the MAC.


0: Transmit idles being received from the MAC.


3 Inhibit 100BASE-TX R/W 1: Disable transmission of EEE LPI on transmit

transmit EEE LPI path MDI in 100BASE-TX mode when receiving
LPI from MAC.


2 Inhibit 100BASE-TX R/W 1: Disable transmission of EEE LPI on receive

receive EEE LPI path MAC interface in 100BASE-TX mode when
receiving LPI from the MDI.


1 Inhibit 1000BASE-T R/W 1: Disable transmission of EEE LPI on transmit

transmit EEE LPI path MDI in 1000BASE-T mode when receiving
LPI from MAC.


0 Inhibit 1000BASE-T R/W 1: Disable transmission of EEE LPI on receive

receive EEE LPI path MAC interface in 1000BASE-T mode when
receiving LPI from the MDI.

#### **3.5 Extended Page 3 Registers**



0


0


0


0


0


0



To access the extended page 3 registers (16E3–30E3), enable extended register access by writing
0x0003 to register 31. For more information, see Table 41 on page 3-43.


When extended page 3 register access is enabled, reads and writes to registers 16–30 affect the
extended registers 16E3–30E3 instead of those same registers in the IEEE-specified register space.
Registers 0–15 are not affected by the state of the extended page register access.


Writing 0x0000 to register 31 restores the main register access.


The following table lists the addresses and register names in the extended register page 3 space. These
registers are accessible only when the device register 31 is set to 0x0003.


_**Table 56 •**_ **Extended Registers Page 3 Space**


**Address** **Name**


16E3 MAC SerDes PCS Control


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 52


Extended Page 3 Registers


_**Table 56 •**_ **Extended Registers Page 3 Space** _**(continued)**_


**Address** **Name**


17E3 MAC SerDes PCS Status


18E3 MAC SerDes Clause 37 Advertised Ability


19E3 MAC SerDes Clause 37 Link Partner Ability


20E3 MAC SerDes Status


21E3–30E3 Reserved

##### **3.5.1 MAC SerDes PCS Control**


The register at address 16E3 consists of the bits that provide access to and control over MAC SerDes
PCS block. The following table shows the settings available.


_**Table 57 •**_ **MAC SerDes PCS Control, Address 16E3 (0x10)**


**Bit** **Name** **Access Description** **Default**



15 MAC interface disable R/W Sticky bit.


1: 1000BASE-X MAC interface disable when

media link down.


14 MAC interface restart R/W Sticky bit.


1: 1000BASE-X MAC interface restart on

media link change.


13 MAC interface PD enable R/W Sticky bit.


1: MAC interface autonegotiation parallel
detect enable.


12 MAC interface R/W Self-clearing bit.
autonegotiation restart 1: Restart MAC interface autonegotiation.



0


0


0


0



11 Force advertised ability R/W 1: Force 16-bit advertised ability from register 0
18E3.



10:8 SGMII preamble control R/W 000: No effect on the start of packet.


001: If both the first two nibbles of the 10/100

packet are not 0x5, a byte of 0x55 must be
prefixed to the output, otherwise there will be
no effect on the start of packet.


010: If both the first two nibbles of the 10/100

packet are not 0x5, a byte of 0x55 must be
prefixed to the output. An additional byte of
0x55 must be prefixed to the output if the
next two nibbles are also not 0x5.


011–111: Reserved.



001



7 MAC SerDes R/W 1: MAC SerDes ANEG enable. 0

autonegotiation enable


6 SerDes polarity at input of R/W 1: Invert polarity of signal received at input of 0
MAC MAC.


5 SerDes polarity at output R/W 1: Invert polarity of signal at output of MAC.
of MAC


4:0 Reserved RO Reserved.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 53


Extended Page 3 Registers

##### **3.5.2 MAC SerDes PCS Status**


The register at address 17E3 consists of the bits that provide status from the MAC SerDes PCS block.
The following table shows the settings available.


_**Table 58 •**_ **MAC SerDes PCS Status, Address 17E3 (0x11)**


**Bit** **Name** **Access Description**


15:12 Reserved RO Reserved


11 MAC interface LP autonegotiation RO 1: MAC interface link partner autonegotiation
restart restart request occurred


10 Reserved RO Reserved


9:8 MAC remote fault RO 01, 10, and 11: Remote fault detected from
MAC


00: No remote fault detected from MAC


7 Asymmetric pause advertisement RO 1: Asymmetric pause advertised by MAC


6 Symmetric pause advertisement RO 1: Symmetric pause advertised by MAC


5 Full duplex advertisement RO 1: Full duplex advertised by MAC


4 Half duplex advertisement RO 1: Half duplex advertised by MAC


3 MAC interface LP autonegotiation RO 1: MAC interface link partner autonegotiation
capable capable


2 MAC interface link status RO 1: MAC interface link status connected


1 MAC interface autonegotiation RO 1: MAC interface autonegotiation complete
complete


0 MAC interface PCS signal detect RO 1: MAC interface PCS signal detect present

##### **3.5.3 MAC SerDes Clause 37 Advertised Ability**


The register at address 18E3 consists of the bits that provide access to and control over MAC SerDes
Clause 37 advertised ability. The following table shows the settings available.


_**Table 59 •**_ **MAC SerDes Clause 37 Advertised Ability, Address 18E3 (0x12)**


**Bit** **Name** **Access Description** **Default**



15:0 MAC SerDes advertised R/W Current configuration code word being
ability advertised (this register is read/write if
16E3.11 = 1)

##### **3.5.4 MAC SerDes Clause 37 Link Partner Ability**



0x0000



The register at address 19E3 consists of the bits that provide status of the MAC SerDes link partner's
Clause 37 advertised ability. The following table shows the settings available.


_**Table 60 •**_ **MAC SerDes Cl37 LP Ability, Address 19E3 (0x13)**


**Bit** **Name** **Access Description**


15:0 MAC SerDes LP ability RO Last configuration code word received from link partner


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 54


General Purpose Registers

##### **3.5.5 MAC SerDes Status**


The register at address 20E3 consists of the bits that provide access to MAC SerDes status. The
following table shows the settings available.


_**Table 61 •**_ **MAC SerDes Status, Address 20E3 (0x14)**


**Bit** **Name** **Access Description**


15 Reserved RO Reserved


14 SerDes signal detect RO Self-clearing bit. Sticky bit.


1: SerDes signal detection occurred


13 QSGMII sync status RO


12:0 Reserved RO Reserved

#### **3.6 General Purpose Registers**


Accessing the general purpose register space is similar to accessing the extended page registers. Set
register 31 to 0x0010. This sets all 32 registers to the general purpose register space.


To restore main register page access, write 0x0000 to register 31.


The following table lists the addresses and register names in the general purpose register page space.
These registers are accessible only when the device register 31 is set to 0x0010. All general purpose
register bits are super-sticky. This register space is global in nature to all four PHY’s in the VSC8514-11
device.


_**Table 62 •**_ **General Purpose Registers Page Space**


**Address** **Name**


0G–12G Reserved


13G LED/GPIO Control


14G GPIO Control 2


15G GPIO Input


16G GPIO Output


17G GPIO Output Enable


18G Micro Command


19G MAC Mode Configuration


20G Reserved


21G Reserved


22G Reserved


23G Reserved


24G Reserved


25G Enhanced LED Control


26G Reserved


27G Reserved


28G Reserved


29G Global Interrupt Status


30G Reserved


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 55


General Purpose Registers

##### **3.6.1 Reserved General Purpose Address Space**


The bits in registers 0G to 12G and 30G of the general purpose register space are reserved.

##### **3.6.2 GPIO Control**


The GPIO control bits configure the GPIO[1:0] pins. The following table shows the values that can be
written.


_**Table 63 •**_ **GPIO Control, Address 13G (0x0D)**


**Bit** **Name** **Access Description** **Default**



15:14 GPIO7 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


13:12 GPIO6 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


11:10 GPIO5 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


9:8 GPIO4 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


7:6 GPIO3 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


5:4 GPIO2 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


3:2 GPIO1 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


1:0 GPIO0 control R/W 00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G



00


00


00


00


00


00


00


00



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 56


General Purpose Registers

##### **3.6.3 GPIO Control 2**


The GPIO control 2 register configures the functionality of the COMA_MODEinput pins, and provides
control for possible GPIO pin options.


_**Table 64 •**_ **GPIO Control 2, Address 14G (0x0E)**


**Bit** **Name** **Access Description** **Default**



15:14 GPIO12 control, GPIO13
control, and GPIO14
control



R/W Control the operation of GPIO12, GPIO13,
and GPIO14 pins.


00: Reserved


01: Reserved


10: Reserved


11: GPIO12/GPIO13/GPIO14 - controlled

by MII registers 15G to 17G



00


1



13 COMA_MODE output R/W 1: COMA_MODE pin is an input.
enable (active low) 0: COMA_MODE pin is an output.



12 COMA_MODE output R/W Value to output on the COMA_MODE pin 0
data when it is configured as an output.


11 COMA_MODE input data RO Data read from the COMA_MODE pin.


10 Reserved R/W Reserved. 1



9 Tri-state enable for LEDs R/W 1: Tri-state LED output signals instead of
driving them high. this allows the signals to
be pulled above VDDIO using an external
pull-up resistor.


0: Drive LED bus output signals to high and
low values, as appropriate.



0



8 Reserved RO Reserved 0



7:6 GPIO11 control R/W GPIO11 control.


00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


5:4 GPIO10 control R/W GPIO10 control.


00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


3:2 GPIO9 control R/W GPIO9 control.


00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G


1:0 GPIO8 control R/W GPIO8 control.


00: Reserved


01: Reserved


10: Reserved


11: Controlled by MII registers 15G to 17G



00


00


00


00



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 57


General Purpose Registers

##### **3.6.4 GPIO Input**


The input register contains information about the input to the device GPIO pins. Read from this register to
access the data on the device GPIO pins. The following table shows the readout you can expect.


_**Table 65 •**_ **GPIO Input, Address 15G (0x0F)**


**Bit** **Name** **Access Description** **Default**


15 Reserved RO Reserved


14 GPIO14 R/W GPIO14 input 0


13 GPIO13 R/W GPIO13 input 0


12 GPIO12 R/W GPIO12 input 0


11 GPIO11 R/W GPIO11 input 0


10 GPIO10 R/W GPIO10 input 0


9 GPIO9 R/W GPIO9 input 0


8 GPIO8 R/W GPIO8 input 0


7 GPIO7 R/W GPIO7 input 0


6 GPIO6 R/W GPIO6 input 0


5 GPIO5 R/W GPIO5 input 0


4 GPIO4 R/W GPIO4 input 0


3 GPIO3 R/W GPIO3 input 0


2 GPIO2 R/W GPIO2 input 0


1 GPIO1 R/W GPIO1 input 0


0 GPIO0 R/W GPIO0 input 0

##### **3.6.5 GPIO Output**


The output register allows you to access and control the output from the device GPIO pins. The following
table shows the values you can write.


_**Table 66 •**_ **GPIO Output, Address 16G (0x10)**


**Bit** **Name** **Access Description** **Default**


15 Reserved RO Reserved


14 GPIO14 R/W GPIO14 output 0


13 GPIO13 R/W GPIO13 output 0


12 GPIO12 R/W GPIO12 output 0


11 GPIO11 R/W GPIO11 output 0


10 GPIO10 R/W GPIO10 output 0


9 GPIO9 R/W GPIO9 output 0


8 GPIO8 R/W GPIO8 output 0


7 GPIO7 R/W GPIO7 output 0


6 GPIO6 R/W GPIO6 output 0


5 GPIO5 R/W GPIO5 output 0


4 GPIO4 R/W GPIO4 output 0


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 58


General Purpose Registers


_**Table 66 •**_ **GPIO Output, Address 16G (0x10)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


3 GPIO3 R/W GPIO3 output 0


2 GPIO2 R/W GPIO2 output 0


1 GPIO1 R/W GPIO1 output 0


0 GPIO0 R/W GPIO0 output 0

##### **3.6.6 GPIO Pin Configuration**


Register 17G in the GPIO register space controls whether a particular GPIO pin functions as an input or
an output. The following table shows the settings available.


_**Table 67 •**_ **GPIO Input/Output Configuration, Address 17G (0x11)**


**Bit** **Name** **Access Description** **Default**


15 Reserved RO Reserved


14 GPIO14 R/W GPIO14 output enable 0


13 GPIO13 R/W GPIO13 output enable 0


12 GPIO12 R/W GPIO12 output enable 0


11 GPIO11 R/W GPIO11 output enable 0


10 GPIO10 R/W GPIO10 output enable 0


9 GPIO9 R/W GPIO9 output enable 0


8 GPIO8 R/W GPIO8 output enable 0


7 GPIO7 R/W GPIO7 output enable 0


6 GPIO6 R/W GPIO6 output enable 0


5 GPIO5 R/W GPIO5 output enable 0


4 GPIO4 R/W GPIO4 output enable 0


3 GPIO3 R/W GPIO3 output enable 0


2 GPIO2 R/W GPIO2 output enable 0


1 GPIO1 R/W GPIO1 output enable 0


0 GPIO0 R/W GPIO0 output 0

##### **3.6.7 Micro Command**


Register 18G is a command register. Bit 15 tells the internal processor to execute the command. When
bit 15 is cleared the command has completed. Software needs to wait until bit 15 = 0 before proceeding
with the next PHY register access. Bit 14 = 1 typically indicates an error condition. Use the following
steps to execute the command:


1. Write desired command


2. Check bit 15 (move existing text)


3. Check bit 14 (if set, then error)


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 59


General Purpose Registers


Commands may take up to 25 ms to complete before bit 15 changes to 0.


_**Table 68 •**_ **Micro Command Register, Address 18G**


**Command** **Setting**


Enable 4 ports MAC QSGMII 0x80E0


QSGMII transmitter control [(1)]


_1. Contact your Microsemi representative for details._

##### **3.6.8 MAC Configuration**


Register 19G in the GPIO register space controls the MAC interface mode. The following table shows the
settings available for the GPIO9 pin.


_**Table 69 •**_ **MAC Configuration Register, Address 19G (0x13)**


**Bit** **Name** **Access Description** **Default**



15:14 MAC configuration R/W Select MAC interface mode


00: Reserved


01: QSGMII


10: Reserved


11: Reserved


13:4 Reserved RO Reserved



00



3:0 Reserved RO Reserved 0xF

##### **3.6.9 Enhanced LED Control**


The following table contains the bits to control advanced functionality of the parallel and serial LED
signals.


_**Table 70 •**_ **Enhanced LED Control, Address 25G (0x19)**


**Bit** **Name** **Access Description** **Default**



15:8 LED pulsing duty cycle R/W Programmable control for LED pulsing
control duty cycle when bit 30.12 is set to 1. Valid
settings are between 0 and 198. A setting
of 0 corresponds to a 0.5% duty cycle and
198 corresponds to a 99.5% duty cycle.
Intermediate values change the duty cycle
in 0.5% increments


7 Port 1 enhanced serial LED R/W Enable the enhanced serial LED output
output enable functionality for port 1 LED pins.


1: Enhanced serial LED outputs


0: Normal function


6 Port 0 enhanced serial LED R/W Enable the enhanced serial LED output
output enable functionality for port 0 LED pins.


1: Enhanced serial LED outputs


0: Normal function



00


0


0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 60


General Purpose Registers


_**Table 70 •**_ **Enhanced LED Control, Address 25G (0x19)** _**(continued)**_


**Bit** **Name** **Access Description** **Default**


5:3 Serial LED frame rate R/W Select frame rate of serial LED stream

selection 000: 2500 Hz frame rate


001: 1000 Hz frame rate


010: 500 Hz frame rate


011: 250 Hz frame rate


100: 200 Hz frame rate


101: 125 Hz frame rate


110: 40 Hz frame rate


111: Output basic serial LED stream


See Table 5 on page 2-14.



2:1 Serial LED select R/W Select which LEDs from each PHY to

enable on the serial stream


00: Enable all four LEDs of each PHY


01: Enable LEDs 2, 1 and 0 of each PHY


10: Enable LEDs 1 and 0 of each PHY


11: Enable LED 0 of each PHY


0 LED port swapping R/W See "LED Port Swapping" on page 2-15.

##### **3.6.10 Global Interrupt Status**



00



The following table contains the interrupt status from the various sources to indicate which one caused
that last interrupt on the pin.


_**Table 71 •**_ **Global Interrupt Status, Address 29G (0x1D)**


**Bit** **Name** **Access Description**


15:4 Reserved RO Reserved


3 PHY3 interrupt source [(1)] RO PHY3 interrupt source indication


0: PHY3 caused the interrupt


1: PHY3 did not cause the interrupt


2 PHY2 interrupt source [(1)] RO PHY2 interrupt source indication


0: PHY2 caused the interrupt


1: PHY2 did not cause the interrupt



1 PHY1 interrupt source [(1)]



RO PHY1 interrupt source indication


0: PHY1 caused the interrupt


1: PHY1 did not cause the interrupt



0 PHY0 interrupt source [(1)] RO PHY0 interrupt source indication


0: PHY0 caused the interrupt


1: PHY0 did not cause the interrupt


_1. This bit is set to 1 when the corresponding PHY’s Interrupt Status register 26 (0x1A) is read._


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 61


Clause 45 Registers to Support Energy Efficient Ethernet and 802.3bf

#### **3.7 Clause 45 Registers to Support Energy Efficient** **Ethernet and 802.3bf**


This section describes the Clause 45 registers that are required to support energy efficient Ethernet.
Access to these registers is through the IEEE standard registers 13 and 14 (MMD access control and
MMD data or address registers) as described in section 4.2.11 and 4.2.12.


The following table lists the addresses and register names in the Clause 45 register page space. When
the link is down, 0 is the value returned for the x.180x addresses.


_**Table 72 •**_ **Clause 45 Registers Page Space**


**Address** **Name**


1.1801 Tx maximum delay through PHY


1.1803 Tx minimum delay through PHY


1.1805 Rx maximum delay through PHY


1.1807 Rx minimum delay through PHY


3.1 PCS status 1


3.20 EEE capability


3.22 EEE wake error counter


4.1801 Tx maximum delay through xMII (QSGMII, including FIFO variations)


4.1803 Tx minimum delay through xMII (QSGMII, including FIFO variations)


4.1805 Rx maximum delay through xMII (QSGMII, including FIFO variations)


4.1807 Rx minimum delay through xMII (QSGMII, including FIFO variations)


7.60 EEE advertisement


7.61 EEE link partner advertisement

##### **3.7.1 PCS Status 1**


The bits in the PCS Status 1 register provide a status of the EEE operation from the PCS for the link that
is currently active.


_**Table 73 •**_ **PCS Status 1, Address 3.1**


**Bit** **Name** **Access Description**


15:12 Reserved RO Reserved


11 Tx LPI received RO/LH 1: Tx PCS has received LPI


0: LPI not received


10 Rx LPI received RO/LH 1: Rx PCS has received LPI


0: LPI not received


9 Tx LPI indication RO 1: Tx PCS is currently receiving LPI


0: PCS is not currently receiving LPI


8 Rx LPI indication RO 1: Rx PCS is currently receiving LPI


0: PCS is not currently receiving LPI


7:3 Reserved RO Reserved


2 PCS receive link status RO 1: PCS receive link up


0: PCS receive link down


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 62


Clause 45 Registers to Support Energy Efficient Ethernet and 802.3bf


_**Table 73 •**_ **PCS Status 1, Address 3.1** _**(continued)**_


**Bit** **Name** **Access Description**


1:0 Reserved RO Reserved

##### **3.7.2 EEE Capability**


This register is used to indicate the capability of the PCS to support EEE functions for each PHY type.
The following table shows the bit assignments for the EEE capability register.


_**Table 74 •**_ **EEE Capability, Address 3.20**


**Bit** **Name** **Access Description**


15:3 Reserved RO Reserved


2 1000BASE-T EEE RO 1: EEE is supported for 1000BASE-T


0: EEE is not supported for 1000BASE-T


1 100BASE-TX RO 1: EEE is supported for 100BASE-TX
EEE 0: EEE is not supported for 100BASE-TX


0 Reserved RO Reserved

##### **3.7.3 EEE Wake Error Counter**


This register is used by PHY types that support EEE to count wake time faults where the PHY fails to
complete its normal wake sequence within the time required for the specific PHY type. The definition of
the fault event to be counted is defined for each PHY and can occur during a refresh or a wakeup as
defined by the PHY. This 16-bit counter is reset to all zeros when the EEE wake error counter is read or
when the PHY undergoes hardware or software reset.


_**Table 75 •**_ **EEE Wake Error Counter, Address 3.22**


**Bit** **Name** **Access Description**


15:0 Wake error counter RO Count of wake time faults for a PHY

##### **3.7.4 EEE Advertisement**


This register defines the EEE advertisement that is sent in the unformatted next page following a EEE
technology message code. The following table shows the bit assignments for the EEE advertisement
register.


_**Table 76 •**_ **EEE Advertisement, Address 7.60**


**Bit** **Name** **Access Description** **Default**


15:3 Reserved RO Reserved



2 1000BASE-T EEE R/W 1: Advertise that the 1000BASE-T has EEE

capability


0: Do not advertise that the 1000BASE-T has EEE

capability


1 100BASE-TX R/W 1: Advertise that the 100BASE-TX has EEE

EEE capability


0: Do not advertise that the 100BASE-TX has EEE

capability


0 Reserved RO Reserved



0


0



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 63


Clause 45 Registers to Support Energy Efficient Ethernet and 802.3bf

##### **3.7.5 EEE Link Partner Advertisement**


All the bits in the EEE LP Advertisement register are read only. A write to the EEE LP advertisement
register has no effect. When the AN process has been completed, this register will reflect the contents of
the link partner's EEE advertisement register. The following table shows the bit assignments for the EEE
advertisement register.


_**Table 77 •**_ **EEE Advertisement, Address 7.61**


**Bit** **Name** **Access Description**


15:3 Reserved RO Reserved


2 1000BASE-T EEE RO 1: Link partner is advertising EEE capability for 1000BASE-T


0: Link partner is not advertising EEE capability for
1000BASE-T


1 100BASE-TX RO 1: Link partner is advertising EEE capability for 100BASE-TX
EEE 0: Link partner is not advertising EEE capability for

100BASE-TX


0 Reserved RO Reserved


The following table shows the bit assignments for the 802.3bf registers. When the link is down, 0 is the
value returned. cl45reg1_1801 would be device address of 1 and register address of 1801.


_**Table 78 •**_ **802.3bf Registers**


**Register** **Name** **Function**


1.1801 cl45reg1_1801_val[15:0] Tx maximum delay through PHY (PMA/PMD/PCS)


1.1803 cl45reg1_1803_val[15:0] Tx minimum delay through PHY (PMA/PMD/PCS


1.1805 cl45reg1_1805_val[15:0] Rx maximum delay through PHY (PMA/PMD/PCS)


1.1807 cl45reg1_1807_val[15:0] Rx minimum delay through PHY (PMA/PMD/PCS)


4.1801 cl45reg4_1801_val[15:0] Tx maximum delay through xMII (QSGMII, including
FIFO variations)


4.1803 cl45reg4_1803_val[15:0] Tx minimum delay through xMII (QSGMII, including
FIFO variations)


4.1805 cl45reg4_1805_val[15:0] Rx maximum delay through xMII (QSGMII, including
FIFO variations)


4.1807 cl45reg4_1807_val[15:0] Rx minimum delay through xMII (QSGMII, including
FIFO variations)


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 64


DC Characteristics

## **4 Electrical Specifications**


This section provides the DC characteristics, AC characteristics, recommended operating conditions,
and stress ratings for the VSC8514-11 device.

#### **4.1 DC Characteristics**


This section contains the DC specifications for the VSC8514-11 device.

##### **4.1.1 VDD25 and VDDMDIO (2.5 V)**


The following table shows the DC specifications for the pins referenced to V VDD25 and V VDDMDIO when it
is set to 2.5 V. The specifications listed in the following table are valid only when V VDD1 = 1.0 V,
V VDD1A = 1.0 V and V VDD25A = 2.5 V.


_**Table 79 •**_ **VDD25 and VDDMDIO**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit** **Condition**


Output high voltage, V OH_TTL 2.0 2.8 V I OH = –1 mA
LVTTL


Output high voltage, open V OH_OD 2.0 2.8 V I OH = –100 µA
drain


Output low voltage V OL –0.3 0.4 V I OL = 4 mA


Input high voltage V IH 1.85 3.3 V Except SMI pins


Input high voltage V IH 1.88 3.3 V SMI pins


Input low voltage V IL –0.3 0.7 V


Input leakage current I ILEAK –32 32 µA Internal resistor included
(except GPIO, LED, and
COMA_MODE)


Input leakage current I ILEAK –76 32 µA Internal resistor included
(GPIO, LED, and
COMA_MODE)


Output leakage current I OLEAK –32 32 µA Internal resistor included
(except GPIO, LED, and
COMA_MODE)


Output leakage current I OLEAK –76 32 µA Internal resistor included
(GPIO, LED, and
COMA_MODE)


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 65


DC Characteristics

##### **4.1.2 VDDMDIO (1.2 V)**


The following table shows the DC specifications for the pins referenced to V VDDMDIO when it is set to
1.2 V. The specifications listed in the following table are valid only when V VDD1 = 1.0 V, V VDD1A = 1.0 V,
V VDD25 = 2.5 V, V VDD25A = 2.5 V, and V VDDMDIO = 1.2 V.


_**Table 80 •**_ **VDDMDIO**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit Condition**


Output high voltage, V OH 1.0 1.5 V I OH = –100 µA
open drain


Output low voltage, open V OL –0.3 0.25 V I OL = 4 mA
drain


Input high voltage V IH 0.9 1.5 V


Input low voltage V IL –0.3 0.36 V


Input leakage current I ILEAK –32 32 µA Internal resistor included


Output leakage current I OLEAK –32 32 µA Internal resistor included

##### **4.1.3 LED and GPIO**


The following table shows the DC specifications for the LED and GPIO pins.


_**Table 81 •**_ **LED and GPIO**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit** **Condition**


Output high voltage for V OH 1.7 2.8 V V VDD25 = 2.5 V
LED pins, LVTTL I OH = –24 mA


Output low voltage for V OL –0.3 0.6 V V VDD25 = 2.5 V
LED pins, LVTTL I OL = 24 mA


Output high voltage for V OH 1.7 2.8 V V VDD25 = 2.5 V
GPIO pins, LVTTL I OH = –12 mA


Output low voltage for V OL –0.3 0.6 V V VDD25 = 2.5 V
GPIO pins, LVTTL I OL = 12 mA

##### **4.1.4 Internal Pull-Up or Pull-Down Resistors**


Internal pull-up or pull-down resistors are specified in the following table. For more information about
signals with internal pull-up or pull-down resistors, see "Pins by Function" on page 5-77.


All internal pull-up resistors are connected to their respective I/O supply.


_**Table 82 •**_ **Internal Pull-Up or Pull-Down Resistors**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit**


Internal pull-up resistor (GPIO, LED, R PU1 33 53 90 k Ω
and COMA_MODE)


Internal pull-up resistor, all others R PU2 96 120 144 k Ω


Internal pull-down resistor R PD 96 120 144 k Ω


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 66


DC Characteristics

##### **4.1.5 Reference Clock**


The following table shows the DC specifications for a differential reference clock input signal.


_**Table 83 •**_ **Reference Clock**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit**


Input voltage range V IP,V IN –25 1260 mV



Input differential voltage V ID 150 [(1)]



1000 mV



Input common-mode voltage V ICM 0 1200 [(2)]



mV



Differential input impedance R I 100 Ω


_1. To meet jitter specifications, the minimum input differential voltage must be 400 mV._


_2. The maximum common-mode voltage is provided without a differential signal. The_
_common-mode voltage is only limited by the maximum and minimum input voltage range_
_and the input signal’s differential amplitude._

##### **4.1.6 Enhanced SerDes Interface (QSGMII)**


All DC specifications for the enhanced SerDes interface are compliant with QSGMII Specification
Revision 1.3 and meet or exceed the requirements in the standard. They are also compliant with OIFCEI-02.0 requirements where applicable.


The following table shows the DC specifications for the enhanced SerDes driver.


_**Table 84 •**_ **QSGMII Driver**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit Condition**


Output differential peak voltage |V ODp | 400 750 mV V DD_VS = 1.0 V
R L = 100 Ω ±1%
maximum drive


Differential resistance R O 80 120 Ω V C = 1.0 V


Output current, drivers shorted to |I OSA |, 40 mA
ground |I OSB |


The following table lists the DC specifications for the enhanced SerDes receiver.


_**Table 85 •**_ **QSGMII Receiver**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit Condition**



Input voltage range, V IA
or V IB(1)



V I –25 1200 mV



Input differential |V ID | 100 1600 mV
peak-to-peak voltage


Common-mode voltage R CMV Internal mV AC coupled
CMV operation [(2)]


Common-mode voltage R CMV VDD1A – VDD1A VDD1A + mV DC coupled
100 100 operation, load
type 2 [(2)]


Receiver differential input R I 80 100 120 Ω
impedance


_1. QSGMII DC input sensitivity is less than 400 mV._


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 67


AC Characteristics


_2. Mode for common mode termination is specified by setting of configuration register. Input_
_amplitude in DC coupled mode must not exceed maximum input voltage range._

##### **4.1.7 Current Consumption**


The following tables show the typical current consumption values for the 4-port QSGMII mode. Add
significant margin above the values for sizing power supplies.


_**Table 86 •**_ **Current Consumption**


**Mode** **Typical** **Maximum** **Unit**


1 V 1 V 2.5 V 2.5 V 1 V 1 V 2.5 V 2.5 V

Digital Analog Digital Analog Digital Analog Digital Analog


Power down 75 155 10 20 225 200 10 25 mA


1000BASE-T idle 340 185 10 445 585 245 10 560 mA


1000BASE-T traffic 355 185 10 445 605 245 10 560 mA


100BASE-TX idle 150 165 10 290 325 210 10 335 mA


100BASE-TX traffic 150 165 10 290 325 210 10 335 mA


10BASE-T idle 95 162 10 110 230 200 10 125 mA


10BASE-T traffic 95 162 10 215 240 200 10 235 mA


1000BASE-T EEE 135 160 10 202 385 200 10 225 mA

LPI


100BASE-TX EEE 102 160 10 205 350 200 10 225 mA

LPI

#### **4.2 AC Characteristics**


This section provides the AC specifications for the VSC8514-11 device.

##### **4.2.1 Reference Clock**


The use of a differential reference clock source is required to meet QSGMII jitter generation
requirements.


The following table shows the AC specifications for a differential reference clock input. Performance is
guaranteed for 125 MHz and 156.25 MHz differential clocks only.


_**Table 87 •**_ **Reference Clock for QSGMII 125 MHz Differential Clock**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit Condition**



Reference clock

frequency,
REFCLK_SEL[1:0] = 00


Reference clock

frequency,
REFCLK_SEL[1:0] = 10



ƒ 125.00 MHz ±100 ppm


Jitter < 1 ps RMS


ƒ 156.25 MHz ±100 ppm



Duty cycle DC 40 50 60 %


Rise time and fall time t R, t F 1.5 ns 20% to 80%
threshold


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 68


AC Characteristics


_**Table 87 •**_ **Reference Clock for QSGMII 125 MHz Differential Clock** _**(continued)**_


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit Condition**



RefClk input RMS jitter
requirement, bandwidth
between 12 kHz and
500 kHz [(1)]


RefClk input RMS jitter
requirement, bandwidth
between 500 kHz and
15 MHz [(1)]


RefClk input RMS jitter
requirement, bandwidth
between 15 MHz and
40 MHz [(1)]


RefClk input RMS jitter
requirement, bandwidth
between 40 MHz and
80 MHz [(1)]


Jitter gain from RefClk to
SerDes output,
bandwidth between

0.1 MHz and 0.1 MHz


Jitter gain from RefClk to
SerDes output,
bandwidth between

0.1 MHz and 7 MHz


Jitter gain from RefClk to
SerDes output,
bandwidth above 7 MHz



20 ps To meet jitter
generation of 1G
output data per
IEEE 802.3z


4 ps Meets jitter
generation of 1G
output data per
IEEE 802.3z


20 ps Meets jitter
generation of 1G
output data per
IEEE 802.3z


100 ps Meets jitter
generation of 1G
output data per
IEEE 802.3z


0.3 dB


1 3 dB


1–20 × log 3–20 × log dB
(ƒ/7 MHz) (ƒ/7 MHz)



_1. Maximum RMS sinusoidal jitter allowed at the RefClk input when swept through the given_
_bandwidth._

##### **4.2.2 Enhanced SerDes Interface**


All AC specifications for the enhanced SerDes interface are compliant with QSGMII Specification
Revision 1.3 and meet or exceed the requirements in the standard. They are also compliant with the OIFCEI-02.0 requirements where applicable.


The transmit and receive eye specifications relate to the eye diagrams shown in the following illustration,
with the compliance load as defined in the test circuit.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 69


AC Characteristics


_**Figure 17 •**_ **QSGMII Transient Parameters**


Transmitter Eye Mask Receiver Eye Mask



T_Y2


T_Y1


0


–T_Y1


–T_Y2



R_Y2


R_Y1


0


–R_Y1


–R_Y2



0 T_X1 T_X2 1–T_X2 1–T_X1 1.0 0 R_X1 0.5 1–R_X1 1.0



1–T_X1



0



Time (UI)



Time (UI)



The following table provides the AC specifications for the enhanced SerDes outputs in QSGMII mode.


_**Table 88 •**_ **QSGMII Transmitter**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit** **Condition**


Signaling speed T BAUD 5.00 – 100 ppm 5.00 5.00 + Gbps
100 ppm


Differential output return RLO SDD22 –8 dB 100 MHz to 2.5 GHz
loss R L = 100 Ω ±1%


Differential output return RLO SDD22 –8 + 16.6 log dB 2.5 GHz to 5 GHz
loss (ƒ/2.5 GHz) R L = 100 Ω ±1%


Common-mode output RLO SCC22 –6 dB 100 MHz to 2.5 GHz
return loss R L = 25 Ω ±1%


Rise time and fall time t R, t F 30 130 ps 20% to 80% of register
programmable slew rate


Random jitter RJ 0.15 UI P-P


Deterministic jitter DJ 0.15 UI P-P


Duty cycle distortion DCD 0.05 UI P-P
(part of DJ)


Total jitter TJ 0.30 UI P-P


Eye mask X1 X1 0.15 UI P-P Near-end


Eye mask X2 X2 0.40 UI P-P Near-end


Eye mask Y1 Y1 200 mV Near-end


Eye mask Y2 Y2 450 mV Near-end


The following table lists the AC specifications for the enhanced SerDes inputs in QSGMII mode.


_**Table 89 •**_ **QSGMII Receiver**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit** **Condition**


Signaling speed T BAUD 5.00 – 100 ppm 5.00 5.00 + 100 ppm Gbps


Differential input return RLI SDD11 –8 dB 100 MHz to 2.5 GHz
loss


Differential input return RLI SDD11 –8 + 16.6 log dB 2.5 GHz to 5 GHz
loss (ƒ/2.5 GHz)


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 70


AC Characteristics


_**Table 89 •**_ **QSGMII Receiver**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit** **Condition**


Common-mode input RLI SCC11 –6 dB 100 MHz to 2.5 GHz
return loss


Sinusoidal jitter, SJ MAX 5 UI P-P Low sinusoidal jitter
maximum frequencies below
(baud/1667)


Sinusoidal jitter, high SJ HF 0.05 UI P-P
frequency



Deterministic jitter
(uncorrelated bounded
high-probability jitter)


Data dependant jitter
(correlated bounded
high-probability jitter)



UBHPJ 0.15 UI P-P


CBHPJ 0.30 UI P-P



Total jitter TJ 0.60 UI P-P Sinusoidal jitter excluded


Eye mask X1 R_X1 0.30 UI P-P


Eye mask Y1 R_Y1 50 mV


Eye mask Y2 R_Y2 450 mV

##### **4.2.3 Basic Serial LEDs**


This section contains the AC specifications for the basic serial LEDs.


_**Table 90 •**_ **Basic Serial LEDs**


**Parameter** **Symbol** **Typical** **Unit**


LED_CLK cycle time t CYC 1024 ns


Pause between LED port sequences t PAUSE_PORT 3072 ns


Pause between LED bit sequences t PAUSE_BIT 25.541632 ms


LED_CLK to LED_DATA t CO 1 ns


_**Figure 18 •**_ **Basic Serial LED Timing**


LED_CLK



LED_DATA




##### **4.2.4 JTAG Interface**

This section provides the AC specifications for the JTAG interface. The specifications meet or exceed the
requirements of IEEE 1149.1-2001. The JTAG receive signal requirements are requested at the pin of


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 71


AC Characteristics


the device. The JTAG_TRST signal is asynchronous to the clock, and does not have a setup or hold time
requirement.


_**Table 91 •**_ **JTAG Interface**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit Condition**


TCK frequency ƒ 10 MHz


TCK cycle time t C 100 ns


TCK high time t W(CH) 40 ns


TCK low time t 40 ns
W(CL)


Setup time to TCK rising t SU 10 ns


Hold time from TCK rising t H 10 ns


TDO valid after TCK falling t V(C) 28 ns C L = 10 pF


TDO hold time from TCK t H(TDO) 0 ns C L = 0 pF
falling



TDO disable time [(1)]



t DIS 30 ns See Figure 20 on page 4-73.



TRST time low t 30 ns
W(TL)


_1. The pin begins to float when a 300 mV change from the actual V_ _OH_ _/V_ _OL_ _level occurs._


_**Figure 19 •**_ **JTAG Interface Timing Diagram**


TCK


TDI

TMS


TDO






|Col1|Col2|Col3|Col4|t<br>c|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CH)  ~~|||||
|||~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CL)  ~~|~~ tW(CL)  ~~|~~ tW(CL)  ~~|~~ tW(CL)  ~~|
|||~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CH)  ~~|~~ tW(CL)  ~~||||
|||||||||||
|||||||||||
||tV(C)|tV(C)|tV(C)|tV(C)|tV(C)|tV(C)||||
|||||||||||
|||||||||||
||||tH(TDO)<br>tDIS|tH(TDO)<br>tDIS|tH(TDO)<br>tDIS|tH(TDO)<br>tDIS|tH(TDO)<br>tDIS|tH(TDO)<br>tDIS|tH(TDO)<br>tDIS|
|||||||||||



nTRST



|Col1|Col2|Col3|
|---|---|---|
||||
||||
||~~tW(TL)~~|~~tW(TL)~~|


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 72


AC Characteristics


_**Figure 20 •**_ **Test Circuit for TDO Disable Time**


3.3 V


From output under test





5 pF


##### **4.2.5 Serial Management Interface**

This section contains the AC specifications for the serial management interface (SMI).


_**Table 92 •**_ **Serial Management Interface**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit Condition**



MDC
frequency [(1)]



f CLK 2.5 12.5 MHz



MDC cycle time t CYC 80 400 ns


MDC time high t WH 20 50 ns


MDC time low t WL 20 50 ns


Setup to MDC t SU 10 ns
rising


Hold from MDC t H 10 ns
rising



100 ns MDC = 0: 1 MHz

t CYC × 10% [(1)] MDC = 1:



MDC rise time t R 100



MDC = 1:
MHz – f CLK maximum



MDC fall time t F 100
t CYC × 10% [(1)]


MDC to MDIO t CO 10 300 ns Time-dependant on the
valid value of the external pullup resistor on the MDIO
pin


_1. For f_ _CLK_ _above 1 MHz, the minimum rise time and fall time is in relation to the frequency of the MDC_
_clock period. For example, if f_ _CLK_ _is 2 MHz, the minimum clock rise time and fall time is 50 ns._


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 73


Operating Conditions


_**Figure 21 •**_ **Serial Management Interface Timing**


MDC



MDIO

(write)


MDIO
(read)

##### **4.2.6 Reset Timing**









This section contains the AC specifications that apply to device reset functionality. The signal applied to
the NRESET input must comply with the specifications listed in the following table.


_**Table 93 •**_ **Reset Timing**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit**


NRESET assertion time after power t W 2 ms
supplies and clock stabilize


Recovery time from reset inactive to t REC 105 ms
device fully active


NRESET pulse width t W(RL) 100 ns


Wait time between NRESET de-assert t WAIT 105 ms
and access of the SMI interface

#### **4.3 Operating Conditions**


The following table shows the recommended operating conditions for the VSC8514-11 device.


_**Table 94 •**_ **Recommended Operating Conditions**


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit**


Power supply voltage for core supply V VDD1 0.95 1.00 1.05 V


Power supply voltage for digital I/O V VDD25 2.38 2.50 2.62 V


Power supply voltage for analog circuits V VDD1A 0.95 1.00 1.05 V


Power supply voltage for analog circuits V VDD25A 2.38 2.50 2.62 V


Power supply voltage for V VDDMDIO at 1.2 V V VDDMDIO 1.14 1.20 1.26


Power supply voltage for V VDDMDIO at 2.5 V V VDDMDIO 2.38 2.50 2.62


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 74


Stress Ratings


_**Table 94 •**_ **Recommended Operating Conditions** _**(continued)**_


**Parameter** **Symbol** **Minimum** **Typical** **Maximum** **Unit**

VSC8514-11 operating temperature [(1)] T 0 125 °C

VSC8514-14 operating temperature [(1)] T –40 125 °C


_1. Minimum specification is ambient temperature, and the maximum is junction temperature._

#### **4.4 Stress Ratings**


This section contains the stress ratings for the VSC8514-11 device.


**Warning** Stresses listed in the following table may be applied to devices one at a time without causing
permanent damage. Functionality at or exceeding the values listed is not implied. Exposure to these
values for extended periods may affect device reliability.


_**Table 95 •**_ **Stress Ratings**


**Parameter** **Symbol** **Minimum** **Maximum** **Unit**


Power supply voltage for core supply V VDD1 –0.3 1.10 V


Power supply voltage for digital I/O V VDD25 –0.3 2.75 V


Power supply voltage for analog circuits V VDD1A –0.3 1.10 V


Power supply voltage for analog circuits V VDD25A –0.3 2.75 V


Power supply voltage for V VDDMDIO V VDDMDIO –0.3 2.75 V


Input voltage for GPIO and logic input pins 3.3 V


Storage temperature T S –55 125 °C


Electrostatic discharge voltage, charged V ESD_CDM –250 250 V
device model


Electrostatic discharge voltage, human body V ESD_HBM –1000 1000 V
model, REF_FILT pin



Electrostatic discharge voltage, human body V ESD_HBM See note [(1)]
model, all pins except the REF_FILT pin



V



_1. This device has completed all required testing as specified in the JEDEC standard_
_JESD22-A114, Electrostatic Discharge (ESD) Sensitivity Testing Human Body Model_
_(HBM), and complies with a Class 2 rating. The definition of Class 2 is any part that passes_
_an ESD pulse of 2000 V, but fails an ESD pulse of 4000 V._


**Warning** This device can be damaged by electrostatic discharge (ESD) voltage. Micrsosemi
recommends that all integrated circuits be handled with appropriate precautions. Failure to observe
proper handling and installation procedures may adversely affect reliability of the device.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 75


Pin Identifications

## **5 Pin Descriptions**


The VSC8514-11 device has 138 pins, which are described in this section.


The pin information is also provided as an attached Microsoft Excel file so that you can copy it
electronically. In Acrobat, double-click the attachment icon.

#### **5.1 Pin Identifications**


This section contains the pin descriptions for the VSC8514-11 device. The following table provides
notations for definitions of the various pin types.


_**Table 96 •**_ **Pin Type Symbol Definitions**


**Symbol** **Pin Type** **Description**


A Analog Analog pin.


ABIAS Analog bias Analog bias pin.


ADIFF Analog differential Analog differential signal pair.


I Input Input without on-chip pull-up or pull-down resistor.


I/O Bidirectional Bidirectional input or output signal.


NC No connect No connect pins must be left floating.


O Output Output signal.


OD Open drain Open drain output.


OS Open source Open source output.


PD Pull-down On-chip pull-down resistor to VSS.


PU Pull-up On-chip pull-up resistor to VDD_IO.

#### **5.2 Pin Diagram**


The following illustration shows the pin diagram for the VSC8514-11 device, as seen looking through the
package from the top of it. Note that the exposed pad connects to the package ground.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 76


Pins by Function


_**Figure 22 •**_ **Pin Diagram**


















































































#### **5.3 Pins by Function**

This section contains the functional pin descriptions for the VSC8514-11 device.

##### **5.3.1 Copper PHY Media**


The following table lists the copper PHY media pins.


_**Table 97 •**_ **Copper PHY Media Pins**


**Name** **Pin** **Type** **Description**


P0_D0N D30 A PHY 0 Tx/Rx channel A negative signal


P0_D0P D31 A PHY 0 Tx/Rx channel A positive signal


P0_D1N C24 A PHY 0 Tx/Rx channel B negative signal


P0_D1P C25 A PHY 0 Tx/Rx channel B positive signal


P0_D2N C23 A PHY 0 Tx/Rx channel C negative signal


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 77


Pins by Function


_**Table 97 •**_ **Copper PHY Media Pins** _**(continued)**_


**Name** **Pin** **Type** **Description**


P0_D2P D29 A PHY 0 Tx/Rx channel C positive signal


P0_D3N C21 A PHY 0 Tx/Rx channel D negative signal


P0_D3P C22 A PHY 0 Tx/Rx channel D positive signal


P1_D0N B17 A PHY 1 Tx/Rx channel A negative signal


P1_D0P B18 A PHY 1 Tx/Rx channel A positive signal


P1_D1N C28 A PHY 1 Tx/Rx channel B negative signal


P1_D1P C29 A PHY 1 Tx/Rx channel B positive signal


P1_D2N B15 A PHY 1 Tx/Rx channel C negative signal


P1_D2P B16 A PHY 1 Tx/Rx channel C positive signal


P1_D3N C26 A PHY 1 Tx/Rx channel D negative signal


P1_D3P C27 A PHY 1 Tx/Rx channel D positive signal


P2_D0N C32 A PHY 2 Tx/Rx channel A negative signal


P2_D0P C33 A PHY 2 Tx/Rx channel A positive signal


P2_D1N B19 A PHY 2 Tx/Rx channel B negative signal


P2_D1P B20 A PHY 2 Tx/Rx channel B positive signal


P2_D2N A9 A PHY 2 Tx/Rx channel C negative signal


P2_D2P A10 A PHY 2 Tx/Rx channel C positive signal


P2_D3N C30 A PHY 2 Tx/Rx channel D negative signal


P2_D3P C31 A PHY 2 Tx/Rx channel D positive signal


P3_D0N C36 A PHY 3 Tx/Rx channel A negative signal


P3_D0P C1 A PHY 3 Tx/Rx channel A positive signal


P3_D1N D34 A PHY 3 Tx/Rx channel B negative signal


P3_D1P D35 A PHY 3 Tx/Rx channel B positive signal


P3_D2N C34 A PHY 3 Tx/Rx channel C negative signal


P3_D2P C35 A PHY 3 Tx/Rx channel C positive signal


P3_D3N D32 A PHY 3 Tx/Rx channel D negative signal


P3_D3P D33 A PHY 3 Tx/Rx channel D positive signal

##### **5.3.2 GPIO**


The following table lists the general purpose input and output (GPIO) pins.


_**Table 98 •**_ **GPIO Pins**


**Name** **Pin** **Type** **Description**



GPIO[0:14] D19, C14, D20, C15,
B9, C16, D21, B10,
C17, D22, D24, D23,
C18, B11, D25



I/O, PU General purpose input/output (GPIO)



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 78


Pins by Function

##### **5.3.3 JTAG**


The following table lists the JTAG test pins.


_**Table 99 •**_ **JTAG Pins**


**Name** **Pin** **Type** **Description**


TCK B6 I, PU JTAG test clock input


TDI C9 I, PU JTAG test serial data input


TDO C8 O JTAG test serial data output


TMS A3 I, PU JTAG test mode select


TRST C7 I, PU JTAG reset


**Important** When JTAG is not in use, this pin must be tied to ground
with a pull-down resistor

##### **5.3.4 Miscellaneous**


The following table lists the miscellaneous pins.


_**Table 100 •**_ **Miscellaneous Pins**


**Name** **Pin** **Type** **Description**



O LED direct-drive outputs. All LEDs pins are active-low.
A serial LED stream can also be implemented. See
"LED Mode Select" on page 3-41.


**Note** LEDbit_port, where port = PHY port number
and bit = the particular LED for the port.


I, Reference clock input differential pair. Must be
ADIFF capacitively coupled and LVDS compliant.



LED0_PHY[0:3]


LED1_PHY[0:3]


LED2_PHY[0:3]


LED3_PHY[0:3]


REFCLK_N


REFCLK_P



E2, C3, C5, B4,


D1, B2, D5, C6,


D2, C4, B3, A2,


C2, D4, D6, D7


D12


D11



REFCLK_SEL[0:1] B8, B7 I, PD Reference clock frequency select signal for bit 0:1.


REF_FILT A7 ABIAS Reference filter connects to an external 1 µF capacitor
to analog ground.


REF_REXT A8 ABIAS Reference signal connects to an external 2 k Ω (1%)
resistor to analog ground.



RESERVED_[1:7] C12, C13,


D28, B14, B13,
C20, D27



NC Reserved signal. Leave unconnected.


ABIAS SerDes bias pins. Connect to a 620 Ω 1% resistor.



SERDES_REXT_0


SERDES_REXT_1



D17


D18



THERMDA B1 I Thermal diode anode.


THERMDC_VSS D3 I Thermal diode cathode connected to device ground.
Temperature sensor must be chosen accordingly.

##### **5.3.5 No Connect**


The following table lists the no connect pins.


_**Table 101 •**_ **No Connect Pins**


**Name** **Pin** **Description**


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 79


Pins by Function


_**Table 101 •**_ **No Connect Pins** _**(continued)**_


NC_[1:4] A1, A4, A5, A6 Leave unconnected

##### **5.3.6 PHY Configuration**


The following table lists the PHY configuration pins.


_**Table 102 •**_ **PHY Configuration Pins**


**Name** **Pin** **Type** **Description**


COMA_MODE D8 I, PU When this pin is asserted high, all PHYs are held in a powered
down state. When de-asserted low, all PHYs are powered up
and resume normal operation. This signal is also used to
synchronize the operation of multiple chips on the same PCB
to provide visual synchronization for LEDs driven by separate
chips. [(1)]


NRESET B5 I, PD Device reset. Active low input that powers down the device and
sets all register bits to their default state.



I, PD Device SMI address bits 4:2.



PHYADD2


PHYADD3


PHYADD4



C19


B12


D26



_1. For more information, see "Initialization" on page 2-24. For information about a typical bring-up_
_example, see "Configuration" on page 2-24._

##### **5.3.7 Power Supply and Ground**


The following table lists the power supply pins and associated functional pins. All power supply pins must
be connected to their respective voltage input, even if certain functions are not used for a specific
application. No power supply sequencing is required. However, clock and power must be stable before
releasing Reset.


_**Table 103 •**_ **Power Supply and Ground Pins**


**Name** **Pin** **Description**


VDD1 E5, E7, E10, E13, E15, E17, 1.0 V digital core power supply
E19, E21, E23, E25


VDD1A E1, E11, E14, E16, E28, E30, 1.0 V analog power requiring additional PCB power
E32, E34, E36 supply filtering


VDD25 E3, E4, E6, E8, E12, E18, E20, 2.5 V general digital power supply
E22, E24, E26


VDD25A E27, E29, E31, E33, E35, E37 2.5 V general analog power supply


VDDMDIO E9 1.2 V or 2.5 V power for SMI pins


VSS_CASE Exposed pad, D9 Common device ground


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 80


Pins by Function

##### **5.3.8 QSGMII MAC Interface**


The following table lists the SerDes MAC interface pins.


_**Table 104 •**_ **SerDes MAC Interface Pins**


**Name** **Pin** **Type** **Description**



RDN_0


RDP_0


TDN_0


TDP_0



D13


D14


D15


D16



A QSGMII MAC receiver output pair


A QSGMII MAC transmitter input pair


##### **5.3.9 Serial Management Interface**

The following table lists the serial management interface (SMI) pins. The SMI pins are referenced to
VDD25 and can be set to a 2.5 V power supply.


_**Table 105 •**_ **SMI Pins**


**Name** **Pin** **Type** **Description**


MDC C11 I, PD Management data clock. A 0 MHz to 12.5 MHz reference input is used to
clock serial MDIO data into and out of the PHY.


MDINT C10 I/O, OS, Management interrupt signal. Upon reset the device configures these pins as
OD active-low (open drain). This pin can be tied together in a wired-OR
configuration with only a single pull-up resistor.


MDIO D10 I/O, OD Management data input/output pin. Serial data is written or read from this pin
bidirectionally between the PHY and station manager, synchronously on the
positive edge of MDC. One external pull-up resistor is required at the station
manager, and its value depends on the MDC clock frequency and the total
sum of the capacitive loads from the MDIO pins.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 81


Package Drawing

## **6 Package Information**


VSC8514XMK-11 and VSC8514XMK-14 are packaged in a lead-free (Pb-free), 138-pin, multi-row plastic
quad flat no-lead (QFN) package with an exposed pad, 12 mm × 12 mm body size, 0.65 mm pin pitch,
and 0.85 mm maximum height.


Lead-free products from Microsemi comply with the temperatures and profiles defined in the joint IPC
and JEDEC standard IPC/JEDEC J-STD-020. For more information, see the IPC and JEDEC standard.


This section provides the package drawing, thermal specifications, and moisture sensitivity rating for the
VSC8514 device.

#### **6.1 Package Drawing**


The following illustration shows the package drawing for the device. The drawing contains the top view,
bottom view, side view, detail views, dimensions, tolerances, and notes.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 82


Package Drawing


_**Figure 23 •**_ **Package Drawing**

|0.10 M X Y Z 0.05 M|Col2|Col3|Col4|Col5|Col6|Col7|0.10 M Z X Y Z 0.05 M|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||3<br>3||||||||
|b3|b2|b1|b|L|K|eR<br>eT|E2<br>|E|D2|D|A1|A|Reference|
|0.550|0.650|0.400|0.250|0.150|0.752||4.700||4.700||0.020||Minimu|
|0.600|0.700|0.450|0.300|0.200|0.802|0.65 BSC<br>0.65 BSC|4.800<br>|12.00 BSC|4.800|12.00 BSC|0.050||m Nominal|
|0.650|0.750|0.500|0.350|0.250|0.852||4.900||4.900||0.080|0.85|Maximum|


|D De|Col2|Col3|Col4|De|Col6|Col7|D|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|eR<br>E2<br>B13<br><br>B11<br>B12<br>B10<br>3|eR<br>E2<br>B13<br><br>B11<br>B12<br>B10<br>3|eR<br>E2<br>B13<br><br>B11<br>B12<br>B10<br>3|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L||
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|eR<br>E2<br>B13<br><br>B11<br>B12<br>B10<br>3|eR<br>E2<br>B13<br><br>B11<br>B12<br>B10<br>3|eR<br>E2<br>B13<br><br>B11<br>B12<br>B10<br>3|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|A6<br>D30<br>B14<br>C25<br>C26<br>C24<br>D29<br>etail B<br>C23<br>C22<br>C21<br>E28<br>E29<br>L<br>L|0.10 (4×) M|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|D19<br>~~D18~~<br>C14|D19<br>~~D18~~<br>C14|D20<br>~~E19~~<br><br>C15<br>E20|D25<br>D24<br>D23<br>D22<br>E21<br>E22<br>E23<br>E24<br>C19<br>C18<br>C17<br>C16<br><br>D21<br>|D25<br>D24<br>D23<br>D22<br>E21<br>E22<br>E23<br>E24<br>C19<br>C18<br>C17<br>C16<br><br>D21<br>|D27<br>E26<br><br>D26<br>E27<br><br>C20<br>E25<br>D28|D30<br>C25<br>C26<br>C24<br>D29<br>C23<br>C22<br>C21<br>E28<br>E29|D30<br>C25<br>C26<br>C24<br>D29<br>C23<br>C22<br>C21<br>E28<br>E29|D30<br>C25<br>C26<br>C24<br>D29<br>C23<br>C22<br>C21<br>E28<br>E29|D30<br>C25<br>C26<br>C24<br>D29<br>C23<br>C22<br>C21<br>E28<br>E29|D30<br>C25<br>C26<br>C24<br>D29<br>C23<br>C22<br>C21<br>E28<br>E29|D30<br>C25<br>C26<br>C24<br>D29<br>C23<br>C22<br>C21<br>E28<br>E29|Z<br>X|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|D19<br>~~D18~~<br>C14|D19<br>~~D18~~<br>C14|||||||||||Y|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|~~E18~~<br>E15<br>D15<br>~~E17~~<br>D1<br>~~D16~~<br>~~D17~~<br>E16|~~E18~~<br>E15<br>D15<br>~~E17~~<br>D1<br>~~D16~~<br>~~D17~~<br>E16|~~E18~~<br>E15<br>D15<br>~~E17~~<br>D1<br>~~D16~~<br>~~D17~~<br>E16|0.650|0.650||A7<br>B16<br>B17<br>C27<br>C30<br>B18<br>E30<br>E31<br>E32<br>E33<br>A8<br>B15<br>D31<br>C28<br>C29|A7<br>B16<br>B17<br>C27<br>C30<br>B18<br>E30<br>E31<br>E32<br>E33<br>A8<br>B15<br>D31<br>C28<br>C29|A7<br>B16<br>B17<br>C27<br>C30<br>B18<br>E30<br>E31<br>E32<br>E33<br>A8<br>B15<br>D31<br>C28<br>C29|A7<br>B16<br>B17<br>C27<br>C30<br>B18<br>E30<br>E31<br>E32<br>E33<br>A8<br>B15<br>D31<br>C28<br>C29|A7<br>B16<br>B17<br>C27<br>C30<br>B18<br>E30<br>E31<br>E32<br>E33<br>A8<br>B15<br>D31<br>C28<br>C29|D2<br>e|D2<br>e|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|~~E18~~<br>E15<br>D15<br>~~E17~~<br>D1<br>~~D16~~<br>~~D17~~<br>E16|~~E18~~<br>E15<br>D15<br>~~E17~~<br>D1<br>~~D16~~<br>~~D17~~<br>E16|~~E18~~<br>E15<br>D15<br>~~E17~~<br>D1<br>~~D16~~<br>~~D17~~<br>E16|0.650||||||||||
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|K<br>E12<br>E13<br>D13<br>C13<br>D12<br>4<br>E14|K<br>E12<br>E13<br>D13<br>C13<br>D12<br>4<br>E14|K<br>E12<br>E13<br>D13<br>C13<br>D12<br>4<br>E14|0.325|0.325|0.200|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|K<br>E12<br>E13<br>D13<br>C13<br>D12<br>4<br>E14|K<br>E12<br>E13<br>D13<br>C13<br>D12<br>4<br>E14|K<br>E12<br>E13<br>D13<br>C13<br>D12<br>4<br>E14|0.325|0.325|0.200|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|B20<br>E34<br>E35<br>E36<br>D32<br>A9<br>C31<br>B19<br>C32<br>C33<br>A10<br>D33|||||
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|D10<br>D11<br>C12<br>C|D10<br>D11<br>C12<br>C|E11<br>E10<br>B7<br><br><br><br>|K<br>D8<br>D9<br><br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D5<br>D6<br>D7<br>B3<br>B4<br>B5<br><br>C9<br>B6|K<br>D8<br>D9<br><br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D5<br>D6<br>D7<br>B3<br>B4<br>B5<br><br>C9<br>B6|E3<br>E4<br>E2<br>C3<br><br>C4<br>D3<br>B2<br>D4<br>B1<br>D2<br>C5|D1<br>E37<br>D35<br>D34<br>C34<br>C35<br>C<br>E1|D1<br>E37<br>D35<br>D34<br>C34<br>C35<br>C<br>E1|D1<br>E37<br>D35<br>D34<br>C34<br>C35<br>C<br>E1|||||
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3|B8<br>11<br>C10<br>A4|B8<br>11<br>C10<br>A4|B8<br>11<br>C10<br>A4|B8<br>11<br>C10<br>A4|B8<br>11<br>C10<br>A4|B8<br>11<br>C10<br>A4|C2|C1|36||A1|A1|A1|
|5.45<br>Pack<br>Pad<br>Pad<br>5.30<br>4.65<br>4.00<br>3.35<br>3.25<br>2.70<br>2.60<br>2.27<br>1.95<br>0.000<br>0.200<br>K<br>K<br>3.25<br>3.57<br>4.00<br>4.22<br>4.55<br>4.65<br>5.30<br>5.45<br>Pack<br>3.250<br>3.575<br>3.677<br>5.626<br>Package<br>Pad 2.<br>Pad 2.<br>5.450<br>4.976<br>4.326<br>4.225<br>3.676<br>2.925<br>2.600<br>2.275<br>1.950<br>0.000<br>4.327<br>4.977<br>5.450<br>5.627<br>Package<br>Pin A<br>D2<br>0.10 (4×) M<br>Z<br>X<br>Y<br>eR<br>E2<br>eT<br>A6<br>D30<br>B14<br>B13<br>D27<br>E26<br>A7<br>B16<br>B17<br>C25<br>C26<br>C27<br>C30<br>C24<br>D29<br>B18<br>B20<br>~~E18~~<br>E15<br>E11<br>E12<br>E10<br>E13<br>D13<br>D15<br>C13<br>etail B<br>etail D<br>D<br>C23<br>C22<br>C21<br>D26<br>D25<br>D24<br>D23<br>D22<br>E21<br>E3<br>D8<br>D9<br>B7<br>E4<br>E2<br>C3<br>C2<br>C4<br>C6<br>C7<br>C8<br>E5<br>E6<br>E7<br>A2<br>A3<br>E8<br>E9<br>D1<br>D3<br>B2<br>D4<br>D5<br>D6<br>D7<br>D10<br>B3<br>B4<br>B5<br>B8<br>E22<br>E23<br>E24<br>E27<br>E28<br>E29<br>E30<br>E31<br>E32<br>E33<br>E34<br>E35<br>E36<br>E37<br>D19<br>C20<br>C19<br>C18<br>C17<br>B11<br>B12<br>D35<br>D32<br>D34<br>C34<br>C35<br>A8<br>A9<br>L<br>L<br>A5<br>~~E17~~<br>A1<br>B1<br>D2<br>C5<br>D11<br>D12<br>C12<br>C11<br>C10<br>A4<br>C1<br>C36<br>D14<br>~~D16~~<br>~~D17~~<br>~~D18~~<br>D20<br>~~E19~~<br>C16<br>C15<br>B9<br>C14<br>E25<br>E1<br>B15<br>D31<br>C9<br>B6<br>eT<br>0.650<br>0.325<br>D28<br>C28<br>C29<br>E16<br>E14<br>C31<br>B19<br>C32<br>C33<br>A10<br>D21<br>E20<br>B10<br>D33<br>eR<br>3<br>3<br>3||||||||||||||


|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||D|D|
|||||
|X<br>Y<br>E|X<br>Y<br>E|X<br>Y<br>E|X<br>Y<br>E|



VMDS-10446 VSC8514-11 Datasheet Revision 4.0 83


|b|eta (8×|Col3|Col4|
|---|---|---|---|
||b3<br><br>×)|b3<br><br>×)|b3<br><br>×)|
|||||
|||||
|Z<br>0.05 M|Z<br>0.05 M|0.05 M|0.10 M|
|Z<br>0.05 M|Z<br>0.05 M|Z||
|Z<br>0.05 M|Z<br>0.05 M|Z|X|
|Z<br>0.05 M|Z<br>0.05 M|Z|Y|


|Detail B (106×)|Col2|Col3|
|---|---|---|
|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|
|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|||
|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|0.05 M|0.10 M|
|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|Z|Z|
|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|Z|X|
|Y<br>0.10 M Z X<br>Z<br>0.05 M<br>|Z|Y|


|eta (4×|Col2|Col3|
|---|---|---|
|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|
|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|0.05 M|0.10 M|
|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|Z<br>|Z|
|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|Z<br>|X|
|0.10 M Z X Y<br>Z<br>0.05 M<br><br>×)|Z<br>|Y|


|Col1|Col2|
|---|---|
|0.05 M|0.10 M|
|Z|Z|
|Z|X|
|Z|Y|


Thermal Specifications

#### **6.2 Thermal Specifications**


Thermal specifications for this device are based on the JEDEC JESD51 family of documents. These
documents are available on the JEDEC Web site at www.jedec.org. The thermal specifications are
modeled using a four-layer test board with two signal layers, a power plane, and a ground plane (2s2p
PCB). For more information about the thermal measurement method used for this device, see the
JESD51-1 standard.


_**Table 106 •**_ **Thermal Resistances**


**Symbol** **°C/W** **Parameter**


θ JCtop 19.7 Die junction to package case top


θ JB 7.33 Die junction to printed circuit board


θ JA 23.2 Die junction to ambient


θ JMA at 1 m/s 18.15 Die junction to moving air measured at an air speed of 1 m/s


θ JMA at 2 m/s 15.65 Die junction to moving air measured at an air speed of 2 m/s


To achieve results similar to the modeled thermal measurements, the guidelines for board design
described in the JESD51 family of publications must be applied. For information about applications using
QFN packages, see the following:


           - JESD51-2A, _Integrated Circuits Thermal Test Method Environmental Conditions, Natural_
_Convection (Still Air)_


           - JESD51-6, _Integrated Circuit Thermal Test Method Environmental Conditions, Forced Convection_
_(Moving Air)_


           - JESD51-8, _Integrated Circuit Thermal Test Method Environmental Conditions, Junction-to-Board_


           - JESD51-7, _High Effective Thermal Conductivity Test Board for Leaded Surface Mount Packages_


           - JESD51-5, _Extension of Thermal Test Board Standards for Packages with Direct Thermal_
_Attachment Mechanisms_

#### **6.3 Moisture Sensitivity**


This device is rated moisture sensitivity level 3 or better as specified in the joint IPC and JEDEC standard
IPC/JEDEC J-STD-020. For more information, see the IPC and JEDEC standard.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 84


## **7 Design Considerations**

This section provides information about design considerations for the VSC8514-11 device.


_**10BASE-T signal amplitude**_


10BASE-T signal amplitude can be lower than the minimum specified in IEEE 802.3 paragraph
14.3.1.2.1 (2.2 V) at low supply voltages.


This issue is not estimated to present any system level impact. Performance is not impaired with cables
up to 130 m with various link partners.


_**PHY0 initialization after reset from power up**_


On some devices, register 0 in PHY0 does not get initialized to the correct default state and is instead
initialized to 0x0000. This results in the PHY being forced into a 10BASE-T half-duplex configuration.


This issue is does not affect systems that use the recommended initialization sequence. For more
information, see "Configuration" on page 2-24. If the recommended initialization sequence is not used,
reset PHY0 by setting register 0, bit 15 to logic 1 after power up and hardware reset deassertion. This will
restore PHY0 to the correct default state.


_**Link performance in 100BASE-TX and 1000BASE-T modes**_


PHY ports may exhibit sub-optimal performance under certain environmental and cabling conditions
without proper initialization.


Contact Microsemi for a script that needs to be applied during system initialization.


_**Ethernet Packet Generator control register write corruption**_


Writing values to extended page 1 registers 29E1 and 30E1 of one port may corrupt contents of registers
29E1 or 30E1 in another port. This is a timing-related issue and all revision A devices are susceptible to
the problem.


Ethernet packet generator functionality is only used during lab testing, so broadcast writes can be used
to enable EPG on all ports simultaneously.


Alternatively, EPG can be enabled on a per-port basis with the limitation that EPG control updates on a
port may affect other ports of the device.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 85


## **8 Ordering Information**

The device is offered with two operating temperature ranges. The range for VSC8514XMK-11 is 0 °C
ambient to 125 °C junction. The range for VSC8514XMK-14 is –40 °C ambient to 125 °C junction.


VSC8514XMK-11 and VSC8514XMK-14 are packaged in a lead-free (Pb-free), 138-pin, multi-row plastic
quad flat no-lead (QFN) package with an exposed pad, 12 mm × 12 mm body size, 0.65 mm pin pitch,
and 0.85 mm maximum height.


Lead-free products from Microsemi comply with the temperatures and profiles defined in the joint IPC
and JEDEC standard IPC/JEDEC J-STD-020. For more information, see the IPC and JEDEC standard.


The following table lists the ordering information for the device.


_**Table 107 •**_ **Ordering Information**


**Part Order Number** **Description**


VSC8514XMK-11 Lead-free, 138-pin, multi-row plastic QFN with an exposed pad, 12 mm ×
12 mm body size, 0.65 mm pin pitch, and 0.85 mm maximum height. The
operating temperature is 0 °C ambient to 125 °C junction.


VSC8514XMK-14 Lead-free, 138-pin, multi-row plastic QFN with an exposed pad, 12 mm ×
12 mm body size, 0.65 mm pin pitch, and 0.85 mm maximum height. The
operating temperature is –40 °C ambient to 125 °C junction.


VMDS-10446 VSC8514-11 Datasheet Revision 4.0 86


## **9 Revision History**

This section describes the changes that were implemented in this document. The changes are listed by
revision, starting with the most current publication.

#### **9.1 Revision 4.0**


Revision 4.0 of this datasheet was published in August 2015. This was the first production-level
publication of the document.


**Microsemi Headquarters**
One Enterprise, Aliso Viejo,
CA 92656 USA

Within the USA: +1 (800) 713-4113
Outside the USA: +1 (949) 380-6100
Sales: +1 (949) 380-6136
Fax: +1 (949) 215-4996
[Email: sales.support@microsemi.com](mailto:sales.support@microsemi.com)
[www.microsemi.com](http://www.microsemi.com)


©2018 Microsemi, a wholly owned

subsidiary of Microchip Technology Inc. All

rights reserved. Microsemi and the

Microsemi logo are registered trademarks of

Microsemi Corporation. All other trademarks

and service marks are the property of their

respective owners.



Microsemi makes no warranty, representation, or guarantee regarding the information contained herein or the suitability of
its products and services for any particular purpose, nor does Microsemi assume any liability whatsoever arising out of the
application or use of any product or circuit. The products sold hereunder and any other products sold by Microsemi have
been subject to limited testing and should not be used in conjunction with mission-critical equipment or applications. Any
performance specifications are believed to be reliable but are not verified, and Buyer must conduct and complete all
performance and other testing of the products, alone and together with, or installed in, any end-products. Buyer shall not
rely on any data and performance specifications or parameters provided by Microsemi. It is the Buyer’s responsibility to
independently determine suitability of any products and to test and verify the same. The information provided by Microsemi
hereunder is provided “as is, where is” and with all faults, and the entire risk associated with such information is entirely
with the Buyer. Microsemi does not grant, explicitly or implicitly, to any party any patent rights, licenses, or any other IP
rights, whether with regard to such information itself or anything described by such information. Information provided in this
document is proprietary to Microsemi, and Microsemi reserves the right to make any changes to the information in this
document or to any products and services at any time without notice.


**About Microsemi**


Microsemi, a wholly owned subsidiary of Microchip Technology Inc. (Nasdaq: MCHP), offers a comprehensive portfolio of
semiconductor and system solutions for aerospace & defense, communications, data center and industrial markets.
Products include high-performance and radiation-hardened analog mixed-signal integrated circuits, FPGAs, SoCs and
ASICs; power management products; timing and synchronization devices and precise time solutions, setting the world's
standard for time; voice processing devices; RF solutions; discrete components; enterprise storage and communication
solutions, security technologies and scalable anti-tamper products; Ethernet solutions; Power-over-Ethernet ICs and
midspans; as well as custom design capabilities and services. Learn more at www.microsemi.com.


VMDS-10446. August 2015


