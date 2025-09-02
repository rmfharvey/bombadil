Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

#### **Future Technology** Devices International Ltd . **FT231X**

###### **USB to FULL HANDSHAKE UART IC**



The FT231X is a USB to serial UART interface with
full modem control and the following advanced
features:


- Single chip USB to asynchronous serial data
transfer interface.


- Entire USB protocol handled on the chip. No
USB specific firmware programming required.


- Fully integrated 2048 byte multi-timeprogrammable (MTP) memory, storing device
descriptors and CBUS I/O configuration.


- Fully integrated clock generation with no
external crystal required plus optional clock
output selection enabling a glue-less interface
to external MCU or FPGA.


- Data transfer rates from 300 baud to 3 Mbaud
(RS422, RS485, and RS232) at TTL levels.


- 512 byte receive buffer and 512 byte transmit
buffer utilising buffer smoothing technology to
allow for high data throughput.


- FTDI’s royalty-free Virtual Com Port (VCP)
and Direct (D2XX) drivers eliminate the
requirement for USB driver development in
most cases.


- Configurable CBUS I/O pins.


- Transmit and receive LED drive signals.


- UART interface support for 7 or 8 data bits, 1
or 2 stop bits and odd / even / mark / space
no parity.


- Synchronous and asynchronous bit bang
interface options with RD# and WR# strobes.




- USB Battery Charger Detection. Allows for USB
peripheral devices to detect the presence of a
higher power source to enable improved
charging.


- Device supplied pre-programmed with unique
USB serial number.


- USB Power Configurations; supports buspowered, self-powered and bus-powered with
power switching.


- Integrated +3.3V level converter for USB I/O.


- True 3.3V CMOS drive output and TTL input;
Operates down to 1V8 with external pull-ups.
Tolerant of 5V input.


- Configurable I/O pin output drive strength; 4
mA(min) and 16 mA(max).


- Integrated power-on-reset circuit.


- Fully integrated AVCC supply filtering - no
external filtering required.


- UART signal inversion option.


- + 5V Single Supply Operation.


- Internal 3V3/1V8 LDO regulators.


Low operating and USB suspend current; 8mA
(active-typ) and 125µA (suspend-typ).


- UHCI/OHCI/EHCI host controller compatible.


- USB 2.0 Full Speed capable.


- Extended operating temperature range; -40 to
85⁰C.


- Available in compact, Pb-free, 20 Pin SSOP and
QFN packages (both RoHS compliant).



Neither the whole nor any part of the information contained in, or the product described in this manual, may be adapted, or reproduced
in any material or electronic form without the prior written consent of the copyright holder. This product and its documentation are
supplied on an as-is basis and no warranty as to their suitability for any particular purpose is either made or implied. Future Technology
Devices International Ltd will not accept any claim for damages howsoever arising as a result of use or failure of this product. Your
statutory rights are not affected. This product or any variant of it is not intended for use in any medical appliance, device, or system in
which the failure of the product might reasonably be expected to result in personal injury. This document provides preliminary
information that may be subject to change without notice. No freedom to use patents or other intellectual property rights is implied by
the publication of this document. Future Technology Devices International Ltd, Unit 1, 2 Seaward Place, Centurion Business Park,
Glasgow, G41 1HH, United Kingdom.


Copyright © Future Technology Devices International Limited 1


###### **1 Typical Applications**


- USB to RS232/RS422/RS485 Converters.


- Upgrading Legacy Peripherals to USB.


- Utilising USB to add system modularity.


- Incorporate USB interface to enable PC
transfers for development system
communication.


- Cellular and Cordless Phone USB data transfer

cables and interfaces.


- Interfacing MCU/PLD/FPGA based designs to
add USB connectivity.


- USB Audio and Low Bandwidth Video data

transfer.


- USB Smart Card Readers.


- USB Instrumentation.


**1.1** **Driver Support**



Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


- USB Industrial Control.


- USB MP3 Player Interface.


- USB FLASH Card Reader and Writers.


- Set Top Box PC - USB interface.


- USB Digital Camera Interface.


- USB Hardware Modems.


- USB Wireless Modems.


- USB Bar Code Readers.


- USB dongle implementations for Software/
Hardware Encryption and Wireless Modules.


- Detection of dedicated battery charger ports for
high current charging of batteries in portable
devices.



**Royalty free VIRTUAL COM PORT (VCP) and D2XX Direct Drivers** are available for the following
Operating Systems (OS):


  - Windows


  - Linux


  - Mac


  - Android (J2xx / D2xx only)


See the following website link for the full driver support list including OS versions and legacy OS.


[https://ftdichip.com/drivers/](https://ftdichip.com/drivers/)


**Virtual COM Port (VCP)** drivers cause the USB device to appear as an additional COM port available to
the PC. Application software can access the USB device in the same way as it would access a standard
COM port.


**D2XX Direct Drivers** allow direct access to the USB device through a DLL. Application software can
access the USB device through a series of DLL function calls. The functions available are listed in the
[D2XX Programmer's Guide](https://ftdichip.com/document/programming-guides/) [document which is available from the Documents](https://ftdichip.com/document/programming-guides/) section of our website.


Please also refer to the [Installation Guides webpage for details on how to install the drivers.](https://ftdichip.com/document/installation-guides/)

**1.2** **Part Numbers**

|Part Number|Package|
|---|---|
|FT231XQ-x|20 Pin QFN|
|FT231XS-x|20 Pin SSOP|



**Note:** Packing codes for x is:

- R: Taped and Reel, (SSOP is 2,000pcs per reel, QFN is 5,000pcs per reel).

- U: Tube packing, 58pcs per tube (SSOP only)

- T: Tray packing, 490pcs per tray (QFN only)

For example: FT231XQ-R is 5,000pcs taped and reel packing.


Copyright © Future Technology Devices International Limited 2


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**1.3** **USB Compliant**

The FT231X is fully compliant with the USB 2.0 specification and has been given the USB-IF Test-ID (TID)
40001464 (Rev D).


Copyright © Future Technology Devices International Limited 3


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


###### **2 FT231X Block Diagram**

VCC



3V3OUT

















USBDP


USBDM


GND





TXD
RXD
RTS#
CTS#
DTR#

DSR#
DCD#
RI#


CBUS0
CBUS1
CBUS2
CBUS3































**Figure 2.1 FT231X Block Diagram**

For a description of each function, please refer to Section 4.


Copyright © Future Technology Devices International Limited 4


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **Table of Contents**


**1** **Typical Applications ..................................................................... 2**


**1.1** **Driver Support ................................................................................... 2**


**1.2** **Part Numbers..................................................................................... 2**


**1.3** **USB Compliant ................................................................................... 3**


**2** **FT231X Block Diagram ................................................................. 4**


**3** **Device Pin Out and Signal Description ......................................... 7**


**3.1** **20-LD QFN Package .......................................................................... 7**


3.1.1 QFN Package PinOut Description .................................................................................. 7


**3.2** **20-LD SSOP Package......................................................................... 8**


3.2.1 SSOP Package PinOut Description................................................................................. 9


**3.3** **CBUS Signal Options ........................................................................ 10**


**4** **Function Description .................................................................. 11**


**4.1** **Key Features .................................................................................... 11**


**4.2** **Functional Block Descriptions .......................................................... 11**


**5** **Devices Characteristics and Ratings .......................................... 14**


**5.1** **Absolute Maximum Ratings.............................................................. 14**


**5.2** **ESD and Latch-up Specifications ...................................................... 14**


**5.3** **DC Characteristics............................................................................ 14**


**5.4** **MTP Memory Reliability Characteristics ........................................... 18**


**5.5** **Internal Clock Characteristics .......................................................... 18**


**6** **USB Power Configurations ......................................................... 19**


**6.1** **USB Bus Powered Configuration ..................................................... 19**


**6.2** **Self Powered Configuration ............................................................. 20**


**6.3** **USB Bus Powered with Power Switching Configuration ................... 21**


**7** **Application Examples ................................................................. 22**


**7.1** **USB to RS232 Converter .................................................................. 22**


**7.2** **USB to RS485 Coverter .................................................................... 23**


**7.3** **USB to RS422 Converter .................................................................. 24**


**7.4** **USB Battery Charging Detection ...................................................... 25**


**7.5** **LED Interface ................................................................................... 27**


**8** **Internal MTP Memory Configuration .......................................... 29**


**8.1** **Default Values ................................................................................. 29**


**8.2** **Methods of Programming the MTP Memory ...................................... 30**


8.2.1 Programming the MTP memory over USB .................................................................... 30


**8.3** **Memory Map .................................................................................... 30**


Copyright © Future Technology Devices International Limited 5


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**9** **Package Parameters .................................................................. 32**


**9.1** **SSOP-20 Package Mechanical Dimensions ....................................... 32**


**9.2** **SSOP-20 Package Markings ............................................................. 33**


**9.3** **QFN-20 Package Mechanical Dimensions ......................................... 34**


**9.4** **QFN-20 Package Markings ............................................................... 35**


**9.5** **Solder Reflow Profile ....................................................................... 36**


**10** **Contact Information .................................................................. 37**


**Appendix A – References ................................................................... 38**


**Document/Web References ....................................................................... 38**


**Acronyms and Abbreviations ..................................................................... 38**


**Appendix B – List of Figures and Tables ............................................. 39**


**List of Figures ............................................................................................ 39**


**List of Tables ............................................................................................. 39**


**Appendix C – Revision History ........................................................... 41**


Copyright © Future Technology Devices International Limited 6


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **3 Device Pin Out and Signal Description**


**3.1** **20-LD QFN Package**

























**Figure 3.1 QFN Schematic Symbol**

**3.1.1** **QFN Package PinOut Description**

**Note:** # denotes an active low signal.
















|Pin No.|Name|Type|Description|
|---|---|---|---|
|12|**<br>VCC|POWER<br>Input|5 V or 3V3 supply to IC|
|20|VCCIO|POWER<br>Input|1V8 – 3V3 supply for the IO cells|
|10|**<br>3V3OUT|POWER<br>Output|3V3 output at 50mA. May be used to power VCCIO.<br>When VCC is 3V3; pin 10 is an input pin and should be<br>connected to pin 12.|
|3, 13|GND|POWER<br>Input|0V Ground input.|



**Table 3.1 Power and Ground**

*Pin 21 on the symbol is the pad under the centre of the chip package and should be connected to GND
** If VCC is 3V3 then 3V3OUT must also be driven with 3V3 input

|Pin No.|Name|Type|Description|
|---|---|---|---|
|9|USBDM|INPUT|USB Data Signal Minus.|
|8|USBDP|INPUT|USB Data Signal Plus.|
|11|RESET#|INPUT|Reset input (active low).|



**Table 3.2 Common Function pins**


Copyright © Future Technology Devices International Limited 7


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261







|Pin No.|Name|Type|Description|
|---|---|---|---|
|17|TXD|Output|Transmit Asynchronous Data Output.|
|1|RXD|Input|Receiving Asynchronous Data Input.|
|19|RTS#|Output|Request to Send Control Output / Handshake Signal.|
|6|CTS#|Input|Clear To Send Control Input / Handshake Signal.|
|18|DTR#|Output|Data Terminal Ready Control Output / Handshake<br>Signal.|
|4|DSR#|Input|Data Set Ready Control Input / Handshake Signal.|
|5|DCD#|Input|Data Carrier Detect Control Input.|
|2|RI#|Input|Ring Indicator input for remote wake up.|
|15|CBUS0|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is TXDEN. See CBUS Signal Options,<br>Table 3.7.|
|14|CBUS1|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is TXLED#. See CBUS Signal Options,<br>Table 3.7.|
|7|CBUS2|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is RXLED#. See CBUS Signal Options,<br>Table 3.7.|
|16|CBUS3|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is SLEEP#. See CBUS Signal Options,<br>Table 3.7.|


**Table 3.3 UART Interface and CBUS Group**

**Note:**

When used in Input Mode, the input pins are pulled to VCCIO via internal 75kΩ (approx.) resistors. These
pins can be programmed to gently pull low during USB suspend (PWREN# = “1”) by setting an option in
the MTP memory.

**3.2** **20-LD SSOP Package**













**Figure 3.2 SSOP Schematic Symbol**


Copyright © Future Technology Devices International Limited 8


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**3.2.1** **SSOP Package PinOut Description**

**Note:** # denotes an active low signal.
















|Pin No.|Name|Type|Description|
|---|---|---|---|
|15|**<br>VCC|POWER<br>Input|5 V or 3V3 supply to IC|
|3|VCCIO|POWER<br>Input|1V8 – 3V3 supply for the IO cells|
|13|**<br>3V3OUT|POWER<br>Output|3V3 output at 50mA. May be used to power VCCIO.<br>When VCC is 3V3, pin 13 is an input pin.<br>|
|6, 16|GND|POWER<br>Input|0V Ground input.|



**Table 3.4 Power and Ground**

** If VCC is 3V3 then 3V3OUT must also be driven with 3V3 input.

|Pin No.|Name|Type|Description|
|---|---|---|---|
|12|USBDM|INPUT|USB Data Signal Minus.|
|11|USBDP|INPUT|USB Data Signal Plus.|
|14|RESET#|INPUT|Reset input (active low).|



**Table 3.5 Common Function pins**







|Pin No.|Name|Type|Description|
|---|---|---|---|
|20|TXD|Output|Transmit Asynchronous Data Output.|
|4|RXD|Input|Receiving Asynchronous Data Input.|
|2|RTS#|Output|Request to Send Control Output / Handshake Signal.|
|9|CTS#|Input|Clear To Send Control Input / Handshake Signal.|
|1|DTR#|Output|Data Terminal Ready Control Output / Handshake<br>Signal.|
|7|DSR#|Input|Data Set Ready Control Input / Handshake Signal.|
|8|DCD#|Input|Data Carrier Detect Control Input.|
|5|RI#|Input|Ring Indicator input for remote wake up.|
|18|CBUS0|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is TXDEN. See CBUS Signal Options,<br>Table 3.7.|
|17|CBUS1|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is TXLED#. See CBUS Signal Options,<br>Table 3.7.|
|10|CBUS2|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is RXLED#. See CBUS Signal Options,<br>Table 3.7.|
|19|CBUS3|I/O|Configurable CBUS I/O Pin. Function of this pin is<br>configured in the device MTP memory. The default<br>configuration is SLEEP#. See CBUS Signal Options,<br>Table 3.7.|


**Table 3.6 UART Interface and CBUS Group**

**Notes:**

When used in Input Mode, the input pins are pulled to VCCIO via internal 75kΩ (approx.) resistors. These
pins can be programmed to gently pull low during USB suspend (PWREN# = “1”) by setting an option in
the MTP memory.


Copyright © Future Technology Devices International Limited 9


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**3.3** **CBUS Signal Options**

The following options can be configured on the CBUS I/O pins. CBUS signal options are common to both
package versions of the FT231X. These options can be configured in the internal MTP memory using the
[software utility FT_PROG. The default configuration is described in Section](https://ftdichip.com/utilities/#ft_prog) 8.















|CBUS Signal<br>Option|Available On CBUS Pin|Description|
|---|---|---|
|TRI-STATE|CBUS0, CBUS1, CBUS2, CBUS3|IO Pad is tri-stated|
|DRIVE 1|CBUS0, CBUS1, CBUS2, CBUS3|Output a constant 1|
|DRIVE 0|CBUS0, CBUS1, CBUS2, CBUS3|Output a constant 0|
|TXDEN|CBUS0, CBUS1, CBUS2, CBUS3|Enable transmit data for RS485|
|PWREN#|CBUS0, CBUS1, CBUS2, CBUS3|Output is low after the device has been<br>configured by USB, then high during USB<br>suspend mode. This output can be used to<br>control power to external logic P-Channel logic<br>level MOSFET switch. Enable the interface pull-<br>down option when using the PWREN# in this<br>way.|
|TXLED#|CBUS0, CBUS1, CBUS2, CBUS3|Transmit data LED drive – pulses low when<br>data is being transmitted on the TxD pin of the<br>UART. See Section 7.5 for more details.|
|RXLED#|CBUS0, CBUS1, CBUS2, CBUS3|Receive data LED drive – pulses low when data<br>is being received on the RxD pin of the UART.<br>See Section 7.5 for more details.|
|TX&RXLED#|CBUS0, CBUS1, CBUS2, CBUS3|LED drive – pulses low when transmitting or<br>receiving data via USB. See Section 7.5 for<br>more details.|
|SLEEP#|CBUS0, CBUS1, CBUS2, CBUS3|Goes low during USB suspend mode. Typically<br>used to power down an external TTL to RS232<br>level converter IC in USB to RS232 converter<br>designs.|
|CLK24MHz|CBUS0, CBUS1, CBUS2, CBUS3|24 MHz Clock output.*|
|CLK12MHz|CBUS0, CBUS1, CBUS2, CBUS3|12 MHz Clock output.*|
|CLK6MHz|CBUS0, CBUS1, CBUS2, CBUS3|6 MHz Clock output.*|
|GPIO|CBUS0, CBUS1, CBUS2, CBUS3|CBUS bit bang mode option. Allows up to 4 of<br>the CBUS pins to be used as general purpose<br>I/O. Configured individually for CBUS0, CBUS1,<br>CBUS2 and CBUS3 in the internal MTP memory.<br>A separate application note, AN232R-01,<br>available from FTDI website<br>(www.ftdichip.com) describes in more detail<br>how to use CBUS bit bang mode.|
|BCD Charger|CBUS0, CBUS1, CBUS2, CBUS3|Battery Charge Detect, indicates when the<br>device is connected to a dedicated battery<br>charger. Active high output.|
|BCD Charger#|CBUS0, CBUS1, CBUS2, CBUS3|Inverse of BCD Charger|
|BitBang_WR#|CBUS0, CBUS1, CBUS2, CBUS3|Synchronous and asynchronous bit bang mode<br>WR# strobe output.|
|BitBang_RD#|CBUS0, CBUS1, CBUS2, CBUS3|Synchronous and asynchronous bit bang mode<br>RD# strobe output.|
|VBUS_Sense|CBUS0, CBUS1, CBUS2, CBUS3|Input to detect when VBUS is present.|
|Time Stamp|CBUS0, CBUS1, CBUS2, CBUS3|Toggle signal which changes state each time a<br>USB SOF is received|
|Keep_Awake#|CBUS0, CBUS1, CBUS2, CBUS3|Prevents the device from entering suspend<br>state when unplugged.|


**Table 3.7 CBUS Configuration Control**


*When in USB suspend mode the outputs clocks are also suspended.


Copyright © Future Technology Devices International Limited 10


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **4 Function Description**


The FT231X is a USB to full handshake serial UART interface device which simplifies USB implementations
and reduces external component count by fully integrating an MTP memory, and an integrated clock
circuit which requires no external crystal. It has been designed to operate efficiently with USB host
controllers by using as little bandwidth as possible when compared to the total USB bandwidth available.

**4.1** **Key Features**

**Functional Integration.** Fully integrated MTP memory, clock generation, AVCC filtering, Power-OnReset (POR) and LDO regulators.

**Configurable CBUS I/O Pin Options.** The fully integrated MTP memory allows configuration of the
Control Bus (CBUS) functionality and drive strength selection. There are 4 configurable CBUS I/O pins.
These configurable options are detailed in Section 3.3.

The CBUS lines can be configured with any one of these output options by setting bits in the internal MTP
memory. The device is shipped with the most commonly used pin definitions pre-programmed – see
Section 8 for details.

**Asynchronous Bit Bang Mode with RD# and WR# Strobes.** The FT231X supports FTDI’s previous
chip generation bit-bang mode. In bit-bang mode, the eight UART lines can be switched from the regular
interface mode to an 8-bit general purpose I/O port. Data packets can be sent to the device and they will
be sequentially sent to the interface at a rate controlled by an internal timer (equivalent to the baud rate
pre-scalar). In the FT231X device this mode has been enhanced by outputting the internal RD# and
WR# strobes signals which can be used to allow external logic to be clocked by accesses to the bit-bang
[I/O bus. This option will be described more fully in a separate application note available from FTDI](http://www.ftdichip.com/)
[website (www.ftdichip.com).](http://www.ftdichip.com/)

**Synchronous Bit Bang Mode.** The FT231X supports synchronous bit bang mode. This mode differs from
asynchronous bit bang mode in that the interface pins are only read when the device is written to. This
makes it easier for the controlling program to measure the response to an output stimulus as the data
[returned is synchronous to the output data. An application note, AN232R-01](https://ftdichip.com/document/application-notes/) describes this feature.

**Source Power and Power Consumption** . The FT231X is capable of operating at a voltage supply
between +3.3V and +5.25V with a nominal operational mode current of 8mA and a nominal USB suspend
mode current of 125µA. This allows greater margin for peripheral designs to meet the USB suspend mode
current limit of 2.5mA. An integrated level converter within the UART interface allows the FT231X to
interface to UART logic running at +1.8V to +3.3V (5V tolerant).

**4.2** **Functional Block Descriptions**

The following paragraphs detail each function within the FT231X. Please refer to the block diagram shown
in Figure 2.1.

**Internal MTP Memory.** The internal MTP memory in the FT231X is used to store USB Vendor ID (VID),
Product ID (PID), device serial number, product description string and various other USB configuration
descriptors. The internal MTP memory is also used to configure the CBUS pin functions. The FT231X is
supplied with the internal MTP memory pre-programmed as described in Section 8. A user area of the
internal MTP memory is available to system designers to allow storing additional data from the user
application over USB. The internal MTP memory descriptors can be programmed in circuit, over USB
without any additional voltage requirement. The descriptors can be programmed using the FTDI utility
[software called FT_PROG.](https://ftdichip.com/utilities/#ft_prog)

**+3.3V LDO Regulator.** The +3.3V LDO regulator generates the +3.3V reference voltage for driving the
USB transceiver cell output buffers. It requires an external decoupling capacitor to be attached to the
3V3OUT regulator output pin. It also provides +3.3V power to the 1.5kΩ internal pull up resistor on
USBDP. The main function of the LDO is to power the USB Transceiver and the Reset Generator Cells
rather than to power external logic. However, it can be used to supply external circuitry requiring a
+3.3V nominal supply with a maximum current of 50mA.

**+1.8V LDO Regulator.** The +1.8V LDO regulator generates the +1.8V reference voltage for internal use
driving the IC core functions of the serial interface engine and USB protocol engine.


Copyright © Future Technology Devices International Limited 11


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**USB Transceiver.** The USB Transceiver Cell provides the USB 1.1 / USB 2.0 full-speed physical interface
to the USB cable. The output drivers provide +3.3V level slew rate control signalling, whilst a differential
input receiver and two single ended input receivers provide USB data in, Single-Ended-0 (SE0) and USB
reset detection conditions respectfully. This function also incorporates a 1.5kΩ pull up resistor on USBDP.
The block also detects when connected to a USB power supply which will not enumerate the device but
still supply power and may be used for battery charging.

**USB DPLL.** The USB DPLL cell locks on to the incoming NRZI USB data and generates recovered clock
and data signals for the Serial Interface Engine (SIE) block.

**Internal 12MHz Oscillator.** The Internal 12MHz Oscillator cell generates a 12MHz reference clock. This
provides an input to the x4 Clock Multiplier function. The 12MHz Oscillator is also used as the reference
clock for the SIE, USB Protocol Engine and UART FIFO controller blocks.

**Clock Multiplier / Divider.** The Clock Multiplier / Divider takes the 12MHz input from the Internal
Oscillator function and generates the 48MHz, 24MHz, 12MHz and 6MHz reference clock signals. The 48Mz
clock reference is used by the USB DPLL and the Baud Rate Generator blocks.

**Serial Interface Engine (SIE).** The Serial Interface Engine (SIE) block performs the parallel to serial
and serial to parallel conversion of the USB data. In accordance with the USB 2.0 specification, it
performs bit stuffing/un-stuffing and CRC5/CRC16 generation. It also verifies the CRC on the USB data
stream.

**USB Protocol Engine.** The USB Protocol Engine manages the data stream from the device USB control
endpoint. It handles the low-level USB protocol requests generated by the USB host controller and the
commands for controlling the functional parameters of the UART in accordance with the USB 2.0
specification chapter 9.

**FIFO RX Buffer (512 bytes).** Data sent from the USB host controller to the UART via the USB data OUT
endpoint is stored in the FIFO RX (receive) buffer. Data is removed from the buffer to the UART transmit
register under control of the UART FIFO controller. (Rx relative to the USB interface).

**FIFO TX Buffer (512 bytes).** Data from the UART receive register is stored in the TX buffer. The USB
host controller removes data from the FIFO TX Buffer by sending a USB request for data from the device
data IN endpoint. (Tx relative to the USB interface).

**UART FIFO Controller.** The UART FIFO controller handles the transfer of data between the FIFO RX and
TX buffers and the UART transmit and receive registers.

**UART Controller with Programmable Signal Inversion and High Drive.** Together with the UART
FIFO Controller the UART Controller handles the transfer of data between the FIFO RX and FIFO TX
buffers and the UART transmit and receive registers. It performs asynchronous 7 or 8 bit parallel to serial
and serial to parallel conversion of the data on the RS232 (or RS422 or RS485) interface.

Control signals supported by UART mode include RTS, CTS, DSR, DTR, DCD and RI. The UART Controller
also provides a transmitter enable control signal pin option (TXDEN) to assist with interfacing to RS485
transceivers. RTS/CTS, DSR/DTR and X ON / X OFF handshaking options are also supported. Handshaking
is handled in hardware to ensure fast response times. The UART interface also supports the RS232
BREAK setting and detection conditions.

Additionally, the UART signals can each be individually inverted and have a configurable high drive
strength capability. Both these features are configurable in the MTP memory.

**Baud Rate Generator.** The Baud Rate Generator provides a 16x clock input to the UART Controller from
the 48MHz reference clock. It consists of a 14-bit pre-scalar and 3 register bits which provide fine tuning
of the baud rate (used to divide by a number plus a fraction or “sub-integer”). This determines the baud
rate of the UART, which is programmable from 183 baud to 3 Mbaud.

The FT231X supports all standard baud rates and non-standard baud rates from 183 baud up to 3 Mbaud.
Achievable non-standard baud rates are calculated as follows –

Baud Rate = 3000000 / (n + _x_ )


Copyright © Future Technology Devices International Limited 12


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


where ‘n’ can be any integer between 2 and 16,384 (= 2 [14] ) and ‘ _x’_ can be a sub-integer of the value 0,
0.125, 0.25, 0.375, 0.5, 0.625, 0.75, or 0.875. When n = 1, _x_ = 0, i.e. baud rate divisors with values
between 1 and 2 are not possible.

This gives achievable baud rates in the range 183.1 baud to 3,000,000 baud. When a non-standard baud
rate is required simply pass the required baud rate value to the driver as normal, and the FTDI driver will
[calculate the required divisor, and set the baud rate. Refer to the application note AN232B-05](https://ftdichip.com/document/application-notes/) for more
details.

**RESET Generator.** The integrated Reset Generator Cell provides a reliable power-on reset to the device
internal circuitry at power up. The RESET# input pin allows an external device to reset the FT231X.
RESET# can be tied to VCCIO.


Copyright © Future Technology Devices International Limited 13


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **5 Devices Characteristics and Ratings**


**5.1** **Absolute Maximum Ratings**

The absolute maximum ratings for the FT231X devices are as follows. These are in accordance with the
Absolute Maximum Rating System (IEC 60134). Exceeding these may cause permanent damage to the
device.









|Parameter|Value|Unit|Conditions|
|---|---|---|---|
|Storage Temperature|-65°C to 150°C|Degrees C||
|Floor Life (Out of Bag) At Factory Ambient<br>(30°C / 60% Relative Humidity)|168 Hours<br>(IPC/JEDEC J-<br>STD-033A MSL<br>Level 3<br>Compliant)*|Hours||
|Ambient Operating Temperature (Power<br>Applied)|-40°C to 85°C|Degrees C||
|MTTF/MTBF FT231XS|9,185,671|Hours|60% Confidence<br>Level.<br>FIT = 108.87|
|MTTF/MTBF FT231XQ|9,185,671|Hours|Hours|
|VCC Supply Voltage|-0.3 to +5.5|V||
|VCCIO IO Voltage|-0.3 to +4.0|V||
|DC Input Voltage – USBDP and USBDM|-0.5 to +3.63|V||
|DC Input Voltage – High Impedance<br>Bi-directional (powered from VCCIO)|-0.3 to +5.8|V||
|DC Output Current – Outputs|22|mA||
|ESD Charge Device Mode (CDM)|500|V|Class III|
|ESD Human Body Mode (HDM)|2000|V|Class 2|


**Table 5.1 Absolute Maximum Ratings**

- If devices are stored out of the packaging beyond this time limit the devices should be baked before
use. The devices should be ramped up to a temperature of +125°C and baked for up to 17 hours.

**5.2** **ESD and Latch-up Specifications**

|Description|Specification|
|---|---|
|Human Body Mode (HBM)|> ± 2kV|
|Machine mode (MM)|> ± 200V|
|Charged Device Mode (CDM)|> ± 500V|
|Latch-up|> ± 200mA|



**Table 5.2 ESD and Latch-Up Specifications**

**5.3** **DC Characteristics**

DC Characteristics (Ambient Temperature = -40°C to +85°C)






|Col1|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|Col9|
|---|---|---|---|---|---|---|---|---|
||VCC|VCC Operating<br>Supply Voltage|2.97|5|5.5|V|Normal<br>Operation|Normal<br>Operation|
||VCC2|VCCIO Operating<br>Supply Voltage|1.62|---|3.63|V|||
||Icc1|Operating Supply<br>Current|8|8|8.4|mA|Normal<br>Operation|Normal<br>Operation|
||Icc2|Operating Supply<br>Current||125||μA|USB Suspend|USB Suspend|
||3V3|3.3V regulator<br>output|2.97|3.3|3.63|V|VCC must be<br>greater than<br>3V3 otherwise<br>3V3OUT is an<br>input which<br>must be driven|VCC must be<br>greater than<br>3V3 otherwise<br>3V3OUT is an<br>input which<br>must be driven|



Copyright © Future Technology Devices International Limited 14


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

|Col1|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||with 3.3V|with 3.3V|



**Table 5.3 Operating Voltage and Current**


Copyright © Future Technology Devices International Limited 15


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261











































|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|
|---|---|---|---|---|---|---|
|Voh|Output Voltage<br>High|2.97|VCCIO|VCCIO|V|Ioh = +/-2mA<br>I/O Drive<br>strength* = 4mA|
|Voh|Output Voltage<br>High|2.97|VCCIO|VCCIO|V|I/O Drive<br>strength* = 8mA|
|Voh|Output Voltage<br>High|2.97|VCCIO|VCCIO|V|I/O Drive<br>strength* =<br>12mA|
|Voh|Output Voltage<br>High|2.97|VCCIO|VCCIO|V|I/O Drive<br>strength* =<br>16mA|
|Vol|Output Voltage<br>Low||0|0.4|V|Iol = +/-2mA<br>I/O Drive<br>strength* = 4mA|
|Vol|Output Voltage<br>Low||0|0.4|V|I/O Drive<br>strength* = 8mA|
|Vol|Output Voltage<br>Low||0|0.4|V|I/O Drive<br>strength* =<br>12mA|
|Vol|Output Voltage<br>Low||0|0.4|V|I/O Drive<br>strength* =<br>16mA|
|Vil|Input low<br>Switching<br>Threshold|||0.8|V|LVTTL|
|Vih|Input High<br>Switching<br>Threshold|2.0|||V|LVTTL|
|Vt|Switching<br>Threshold||1.49||V|LVTTL|
|Vt-|Schmitt trigger<br>negative going<br>threshold voltage||1.15||V||
|Vt+|Schmitt trigger<br>positive going<br>threshold voltage||1.64||V||
|Rpu|Input pull-up<br>resistance|40|75|190|KΩ|Vin = 0|
|Rpd|Input pull-down<br>resistance|40|75|190|KΩ|Vin =VCCIO|
|Iin|Input Leakage<br>Current|-10|+/-1|10|μA|Vin = 0|
|Ioz|Tri-state output<br>leakage current|-10|+/-1|10|μA|Vin = 5.5V or 0|


**Table 5.4 I/O Pin Characteristics VCCIO = +3.3V (except USB PHY pins)**

- The I/O drive strength and slow slew-rate are configurable in the MTP memory.


Copyright © Future Technology Devices International Limited 16


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261































|Col1|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|Col9|
|---|---|---|---|---|---|---|---|---|
||Voh|Output Voltage High|2.25|VCCIO|VCCIO|V|Ioh = +/-2mA<br>I/O Drive<br>strength* = 4mA|Ioh = +/-2mA<br>I/O Drive<br>strength* = 4mA|
||Voh|Output Voltage High|2.25|VCCIO|VCCIO|V|I/O Drive<br>strength* = 8mA|I/O Drive<br>strength* = 8mA|
||Voh|Output Voltage High|2.25|VCCIO|VCCIO|V|I/O Drive<br>strength* = 12mA|I/O Drive<br>strength* = 12mA|
||Voh|Output Voltage High|2.25|VCCIO|VCCIO|V|I/O Drive<br>strength* = 16mA|I/O Drive<br>strength* = 16mA|
||Vol|Output Voltage Low||0|0.4|V|Iol = +/-2mA<br>I/O Drive<br>strength* = 4mA|Iol = +/-2mA<br>I/O Drive<br>strength* = 4mA|
||Vol|Output Voltage Low||0|0.4|V|I/O Drive<br>strength* = 8mA|I/O Drive<br>strength* = 8mA|
||Vol|Output Voltage Low||0|0.4|V|I/O Drive<br>strength* = 12mA|I/O Drive<br>strength* = 12mA|
||Vol|Output Voltage Low||0|0.4|V|I/O Drive<br>strength* = 16mA|I/O Drive<br>strength* = 16mA|
||Vil|Input low Switching<br>Threshold|||0.8|V|LVTTL|LVTTL|
||Vih|Input High Switching<br>Threshold|1.2|||V|LVTTL|LVTTL|
||Vt|Switching Threshold||1.1||V|LVTTL|LVTTL|
||Vt-|Schmitt trigger<br>negative going<br>threshold voltage||0.8||V|||
||Vt+|Schmitt trigger<br>positive going<br>threshold voltage||1.2||V|||
||Rpu|Input pull-up<br>resistance|40|75|190|KΩ|Vin = 0|Vin = 0|
||Rpd|Input pull-down<br>resistance|40|75|190|KΩ|Vin =VCCIO|Vin =VCCIO|
||Iin|Input Leakage<br>Current|-10|+/-1|10|μA|Vin = 0|Vin = 0|
||Ioz|Tri-state output<br>leakage current|-10|+/-1|10|μA|Vin = 5.5V or 0|Vin = 5.5V or 0|


**Table 5.5 I/O Pin Characteristics VCCIO = +2.5V (except USB PHY pins)**

- The I/O drive strength and slow slew-rate are configurable in the MTP memory.

















|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|
|---|---|---|---|---|---|---|
|Voh|Output Voltage High|1.62|VCCIO|VCCIO|V|Ioh = +/-2mA<br>I/O Drive<br>strength* = 4mA|
|Voh|Output Voltage High|1.62|VCCIO|VCCIO|V|I/O Drive<br>strength* = 8mA|
|Voh|Output Voltage High|1.62|VCCIO|VCCIO|V|I/O Drive<br>strength* = 12mA|
|Voh|Output Voltage High|1.62|VCCIO|VCCIO|V|I/O Drive<br>strength* = 16mA|
|Vol|Output Voltage Low||0|0.4|V|Iol = +/-2mA<br>I/O Drive<br>strength* = 4mA|
|Vol|Output Voltage Low||0|0.4|V|I/O Drive<br>strength* = 8mA|
|Vol|Output Voltage Low||0|0.4|V|I/O Drive<br>strength* = 12mA|
|Vol|Output Voltage Low||0|0.4|V|I/O Drive<br>strength* = 16mA|
|Vil|Input low Switching|||0.77|V|LVTTL|


Copyright © Future Technology Devices International Limited 17


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261















|Col1|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|Col9|
|---|---|---|---|---|---|---|---|---|
|||Threshold|||||||
||Vih|Input High Switching<br>Threshold|1.6|||V|LVTTL|LVTTL|
||Vt|Switching Threshold||0.77||V|LVTTL|LVTTL|
||Vt-|Schmitt trigger<br>negative going<br>threshold voltage||0.557||V|||
||Vt+|Schmitt trigger<br>positive going<br>threshold voltage||0.893||V|||
||Rpu|Input pull-up<br>resistance|40|75|190|KΩ|Vin = 0|Vin = 0|
||Rpd|Input pull-down<br>resistance|40|75|190|KΩ|Vin =VCCIO|Vin =VCCIO|
||Iin|Input Leakage<br>Current|-10|+/-1|10|μA|Vin = 0|Vin = 0|
||Ioz|Tri-state output<br>leakage current|-10|+/-1|10|μA|Vin = 5.5V or 0|Vin = 5.5V or 0|


**Table 5.6 I/O Pin Characteristics VCCIO = +1.8V (except USB PHY pins)**

- The I/O drive strength and slow slew-rate are configurable in the MTP memory.

|Parameter|Description|Minimum|Typical|Maximum|Units|Conditions|
|---|---|---|---|---|---|---|
|Voh|Output Voltage High|3V3OUT-<br>0.2|||V||
|Vol|Output Voltage Low|||0.2|V||
|Vil|Input low Switching<br>Threshold||-|0.8|V||
|Vih|Input High Switching<br>Threshold|2.0|-||V||



**Table 5.7 USB I/O Pin (USBDP, USBDM) Characteristics**

**5.4** **MTP Memory Reliability Characteristics**

The internal 2048 Byte MTP memory has the following reliability characteristics:

|Parameter|Value|Unit|
|---|---|---|
|Data Retention|10|Years|
|Write Cycle|2,000|Cycles|
|Read Cycle|Unlimited|Cycles|



**Table 5.8 MTP Memory Characteristics**


**Note:** Performing X-ray inspection as part of manufacturing process could potentially corrupt the MTP
content. Avoid X-ray directly on the IC as part of the manufacturing process if possible, or conduct your
own evaluation and risk assessment.


**5.5** **Internal Clock Characteristics**

The internal Clock Oscillator has the following characteristics:

|Parameter|Value|Col3|Col4|Unit|
|---|---|---|---|---|
|**Parameter**|Minimum|Typical|Maximum|Maximum|
|Frequency of Operation<br>(see Note 1)|11.98|12.00|12.02|MHz|
|Clock Period|83.19|83.33|83.47|ns|
|Duty Cycle|45|50|55|%|



**Table 5.9 Internal Clock Characteristics**

**Note:** Equivalent to +/-1667ppm.


Copyright © Future Technology Devices International Limited 18


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **6 USB Power Configurations**


The following sections illustrate possible USB power configurations for the FT231X. The illustrations have
omitted pin numbers for ease of understanding since the pins differ between the FT231XS and FT231XQ
package options.

All USB power configurations illustrated apply to both package options for the FT231X device. Please refer
to Section 9 for the package option pin-out and signal descriptions.

**6.1** **USB Bus Powered Configuration**



















**Figure 6.1 Bus Powered Configuration**

Figure 6.1 Illustrates the FT231X in a typical USB bus powered design configuration. A USB bus powered
device gets its power from the USB bus. Basic rules for USB bus power devices are as follows –


i) On plug-in to USB, the device should draw no more current than 100mA.
ii) In USB Suspend mode the device should draw no more than 2.5mA.
iii) A bus powered high power USB device (one that draws more than 100mA) should use one of
the CBUS pins configured as PWREN# and use it to keep the current below 100mA on plug-in
and 2.5mA on USB suspend.
iv) A device that consumes more than 100mA cannot be plugged into a USB bus powered hub.
v) No device can draw more than 500mA from the USB bus.

The power descriptors in the internal MTP memory of the FT231X should be programmed to match the
current drawn by the device.

A ferrite bead is connected in series with the USB power supply to reduce EMI noise from the FT231X and
associated circuitry being radiated down the USB cable to the USB host. The value of the Ferrite Bead
depends on the total current drawn by the application. A suitable range of Ferrite Beads is available from
[Laird Technologies (http://www.lairdtech.com), for example Laird Technologies Part # MI0805K400R-10.](http://www.lairdtech.com/)

**Note:** If using PWREN# (available using the CBUS) the pin should be pulled to VCCIO using a 10kΩ
resistor.


Copyright © Future Technology Devices International Limited 19


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261



**6.2** **Self Powered Configuration**



























**Figure 6.2 Self-Powered Configuration**

Figure 6.2 illustrates the FT231X in a typical USB self-powered configuration. A USB self-powered device
gets its power from its own power supply, VCC, and does not draw current from the USB bus. The basic
rules for USB self-powered devices are as follows –


i) A self-powered device should not force current down the USB bus when the USB host or hub
controller is powered down.
ii) A self-powered device can use as much current as it needs during normal operation and USB
suspend as it has its own power supply.
iii) A self-powered device can be used with any USB host, a bus powered USB hub or a selfpowered USB hub.

The power descriptor in the internal MTP memory of the FT231X should be programmed to a value of
zero (self-powered).

To comply with the first requirement above, the USB bus power (pin 1) is used to control the
VBUS_Sense pin of the FT231X device. When the USB host or hub is powered up an internal 1.5kΩ
resistor on USBDP is pulled up to +3.3V, thus identifying the device as a full speed device to the USB
host or hub. When the USB host or hub is powered off, VBUS_Sense pin will be low and the FT231X is
held in a suspend state. In this state the internal 1.5kΩ resistor is not pulled up to any power supply
(hub or host is powered down), so no current flows down USBDP via the 1.5kΩ pull-up resistor. Failure to
do this may cause some USB host or hub controllers to power up erratically.


Figure 6.2 illustrates a self-powered design which has a +3.3V to +5.25V supply.


**Note:**

When the FT231X is in reset, the UART interface I/O pins are tri-stated. Input pins have internal 200kΩ
pull-up resistors to VCCIO, so they will gently pull high unless driven by some external logic.


Copyright © Future Technology Devices International Limited 20


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**6.3** **USB Bus Powered with Power Switching Configuration**


P Channel Power


MOSFET





























**Figure 6.3 Bus Powered with Power Switching Configuration**

A requirement of USB bus powered applications is when in USB suspend mode, the application draws a
total current of less than 2.5mA. This requirement includes external logic. Some external logic has the
ability to power itself down into a low current state by monitoring the PWREN# signal. For external logic
that cannot power itself down in this way, the FT231X provides a simple but effective method of turning
off power during the USB suspend mode.

Figure 6.3 shows an example of using a discrete P-Channel MOSFET to control the power to external
logic. A suitable device to do this is an International Rectifier (www.irf.com) IRLML6402, or equivalent. It
is recommended that a “soft start” circuit consisting of a 1kΩ series resistor and a 0.1μF capacitor is used
to limit the current surge when the MOSFET turns on. Without the “soft start” circuit it is possible that the
transient power surge, caused when the MOSFET switches on, will reset the FT231X or the USB host/hub
controller. The “soft start” circuit example shown in Figure 6.3 powers up with a slew rate of
approximaely12.5V/ms. Thus, supply voltage to external logic transitions from GND to +5V in
approximately 400 microseconds.

As an alternative to the MOSFET, a dedicated power switch IC with inbuilt “soft start” can be used. A
suitable power switch IC for such an application is the Micrel MIC2025-2BM or equivalent.

With power switching controlled designs the following should be noted:


i) The external logic to which the power is being switched should have its own reset circuitry to
automatically reset the logic when power is re-applied when moving out of suspend mode.
ii) Set the Pull-down on Suspend option in the internal FT231X MTP memory.
iii) One of the CBUS Pins should be configured as PWREN# in the internal FT231X MTP memory and

used to switch the power supply to the external circuitry. This should be pulled high through a 10
kΩ resistor.
iv) For USB high-power bus powered applications (one that consumes greater than 100mA, and up

to 500mA of current from the USB bus), the power consumption of the application must be set in
the Max Power field in the internal FT231X MTP memory. A high-power bus powered application
uses the descriptor in the internal FT231X MTP memory to inform the system of its power
requirements.
v) PWREN# gets its VCC from VCCIO. For designs using 3V3 logic, ensure VCCIO is not powered

down using the external logic. In this case use the +3V3OUT.

Please also refer to technical note [TN_162 Bus Powered with Power Switching Configuration.](https://ftdichip.com/document/technical-notes/)


Copyright © Future Technology Devices International Limited 21


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **7 Application Examples**


The following sections illustrate possible applications of the FT231X. The illustrations have omitted pin
numbers for ease of understanding since the pins differ between the FT231XS and FT231XQ package
options.

**7.1** **USB to RS232 Converter**


**Figure 7.1 Application Example showing USB to RS232 Converter**

An example of using the FT231X as a USB to RS232 converter is illustrated in Figure 7.1. In this
application, a 3V3 TTL to RS232 Level Converter IC is used on the serial UART interface of the FT231X to
convert the 3V3 levels of the FT231X to RS232 levels. This level shift can be done using line drivers from
a variety of vendors e.g. Zywyn. A useful feature on some of these devices is the SHDN# pin which can
be used to power down the device to a low quiescent current during USB suspend mode.

A suitable level shifting device is the Zywyn ZT3243F which is capable of RS232 communication at up to
1000k baud.

In example shown, the CBUS1 and CBUS2 have been configured as TXLED# and RXLED# and are being
used to drive two LEDs.


Copyright © Future Technology Devices International Limited 22


**7.2** **USB to RS485 Coverter**



Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


Vcc


































|Col1|3|Col3|
|---|---|---|
||3||
||||













**Figure 7.2 Application Example Showing USB to RS485 Converter**

An example of using the FT231X as a USB to RS485 converter is shown in Figure 7.2. In this application,
a 3V3-TTL to RS485 level converter IC is used on the serial UART interface of the FT231X to convert the

TTL levels of the FT231X to RS485 levels.

This example uses the Zywyn ZT3485 device. Equivalent devices are available from Maxim and Analogue
Devices. The ZT3485 is a RS485 device in a compact 8 pin SOP package. It has separate enables on both
the transmitter and receiver. With RS485, the transmitter is only enabled when a character is being
transmitted from the UART. The TXDEN signal CBUS pin option on the FT231X is provided for exactly this
purpose and so the transmitter enable is wired to CBUS2 which has been configured as TXDEN. Similarly,
CBUS3 has been configured as PWREN#. This signal is used to control the ZT3485’s receiver enable. The
receiver enable is active low, so it is wired to the PWREN# pin to disable the receiver when in USB
suspend mode. CBUS2 = TXDEN and CBUS3 = PWREN# are the default device configurations of the
FT231X pins.

RS485 is a multi-drop network; so many devices can communicate with each other over a two-wire cable
interface. The RS485 cable requires to be terminated at each end of the cable. A link (which provides the
120Ω termination) allows the cable to be terminated if the ZT3485 is physically positioned at either end
of the cable.

In this example the data transmitted by the FT231X is also present on the receive path of the
ZT3485.This is a common feature of RS485 and requires the application software to remove the
transmitted data from the received data stream. With the FT231X it is possible to do this entirely in
hardware by modifying the example shown in Figure 7.2 by logically OR’ing the FT231X TXDEN and the
ZT3485 receiver output and connecting the output of the OR gate to the RXD of the FT231X.

Note that the TXDEN is activated 1 bit period before the start bit. TXDEN is deactivated at the same time
as the stop bit. This is not configurable.


Copyright © Future Technology Devices International Limited 23


**7.3** **USB to RS422 Converter**



Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


Vcc

























TXDM


TXDP


RXDP


RXDM


RTSM


RTSP

CTSP


CTSM


















|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||||5<br>3|5<br>3|5<br>3|
|||||2|2|2|
||||||||
||||||||
||||5|5|5||
||||3<br>2<br>|3<br>2<br>|3<br>|3<br>|





TXDM

TXDP
RXDP

RXDM

RTSM
RTSP
CTSP
CTSM


**Figure 7.3 USB to RS422 Converter Configuration**

An example of using the FT231X as a USB to RS422 converter is shown in Figure 7.3. In this application,
two 3V3-TTL to RS422 Level Converter Ics are used on the serial UART interface of the FT231X to convert
the TTL levels of the FT231X to RS422 levels. There are many suitable level converter devices available.
This example uses Zywyn ZT3491 devices which have enables on both the transmitter and receiver.
Since the ZT3491 transmitter enable is active high, it is connected to a CBUS pin in SLEEP#
configuration. The ZT3491 receiver enable is active low and is therefore connected to a CBUS pin
PWREN# configuration. This ensures that when both the ZT3491 transmitters and receivers are enabled
then the device is active, and when the device is in USB suspend mode, the ZT3491 transmitters and
receivers are disabled. If a similar application is used, but the design is USB BUS powered, it may be
necessary to use a P-Channel logic level MOSFET (controlled by PWREN#) in the VCC line of the ZT3491
devices to ensure that the USB standby current of 2.5mA is met.

The ZT3491 is specified to transmit and receive data at a rate of up to 16 Mbaud. In this example the
maximum data rate is limited to 3 Mbaud by the FT231X.


Copyright © Future Technology Devices International Limited 24


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**7.4** **USB Battery Charging Detection**

A recent addition to the USB specification [(https://www.usb.org/) is to allow for additional charging](https://www.usb.org/)
profiles to be used for charging batteries in portable devices. These charging profiles do not enumerate
the USB port of the peripheral. The FT231X device will detect that a USB compliant dedicated charging
port (DCP) is connected. Once detected while in suspend mode, a battery charge detection signal is
provided to allow external logic to switch to charging mode as opposed to operation mode.

To use the FT231X with battery charging detection the CBUS pins must be reprogrammed to allow for the
BCD Charger output to switch the external charger circuitry on. The CBUS pins are configured in the
[internal MTP memory with the free utility FT_PROG. If the charging circuitry requires an active low signal](http://www.ftdichip.com/Support/Utilities.htm#FT_Prog)
to enable it, the CBUS pin can be programmed to BCD Charger# as an alternative.

When connected to a USB compliant dedicated charging port (DCP, as opposed to a standard USB host)
the device USB signals will be shorted together and the device suspended. The BCD charger signal will
bring the LTC4053 out of suspend and allow battery charging to start. The charge current in the example
below is 1A as defined by the resistance on the PROG pin.



VBUS 3V3OUT VBUS 3V3OUT


0.1uF 0.1uF



CN USB




|Col1|Col2|
|---|---|
|F||





VBUS 3V3OUT





GND


GND







GND


VBATT


1uF


1R

|7 8 9 10|Col2|Col3|
|---|---|---|
|7|7|7|
|7|2K2|1K5<br>NTC|



GND


|VBUS<br>D-<br>D+<br>ID<br>GND|Col2|Col3|
|---|---|---|
||||


|Col1|Col2|
|---|---|
|F<br>||



NCT


     

TB3.5mm









GND



VBUS


0.1uF


GND



GND


VBUS VBUS


~~4~~ .7uF



GND











+



GND



GND


EEPROM Setting







GND



GND



GND



1A when connected to a dedicated charger port
0A when enumerated

0A when not enumerated and not in sleep


|X-Chip Pin|Function|
|---|---|
|**CBUS0**|**BCD**|





0A when in sleep



VBUS





JUMPER-2mm JP1 2-3 NCT Disabled (Default)


|Battery Options|Col2|Col3|
|---|---|---|
|**Battery Charger Enable**|**X**|**X**|
|**Force Power Enable**<br>**De-acticate Sleep**|||
||||



SIP-3


|JP1<br>NCT Available|Col2|
|---|---|
|1-2<br>2-3|NCT Enabled<br>NCT Disabled (Defaul|



GND





**Figure 7.4 USB Battery Charging Detection (1 pin)**

Alternatively, the PWREN# And SLEEP pins may be used to control the LTC4053 such that a battery may
be charged from a standard host (low current) or from a dedicated charging port (high current). In such
a design as shown below the charge current would need to be limited to 0.4A to ensure that the USB host
power limit is not exceeded.


Copyright © Future Technology Devices International Limited 25


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6







Document No.: FT_000565 Clearance No.: FTDI# 261


VBUS 3V3OUT VBUS 3V3OUT


0.1uF 0.1uF






|Col1|Col2|
|---|---|
|||


|Col1|Col2|
|---|---|
|||



GND





VBUS 3V3OUT



GND


VBATT















GND



VBUS


0.1uF

|Col1|Col2|
|---|---|
|F<br>||



GND



VBUS VBUS


~~4~~ .7uF



GND 2 VCC BAT 9 1







TB3.5mm





NCT



+



GND


|7 8 9 10|Col2|Col3|
|---|---|---|
|7|7|7|
|6||NTC|
|6|2K2|2K2|



GND





GND





GND



GND



GND



GND



0.4A when connected to a dedicated charger port

0.4A when enumerated

0.1A when not enumerated and not in sleep mode

0A when in sleep mode



EEPROM Setting







VBUS

















JUMPER-2mm JP1 2-3 NCT Disabled (Default)


|Battery Options|Col2|
|---|---|
|**Battery Charger Enable**|**X**|
|**Force Power Enable**|**X**|
|**De-acticate Sleep**|**X**<br>|



SIP-3


|JP1<br>NCT Available|Col2|
|---|---|
|1-2<br>2-3|NCT Enabled<br>NCT Disabled (Defaul|



GND





**Figure 7.5 USB Battery Charging Detection (2 pin)**

In the example above the FT231X SLEEP pin is used to enable/disable the LTC4053, while the PWREN#
signal alters the charging current by altering the resistance on the LTC4053 PROG pin.


Copyright © Future Technology Devices International Limited 26


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


A third option shown in the example below uses the SLEEP signal from the FT231X to enable / disable the
battery charger. The BCD# and PWREN# signals are then used to alter the resistance on the PROG pin of
the LTC4053 which controls the charge current drawn from the USB connector.



VBUS 3V3OUT VBUS 3V3OUT


0.1uF 0.1uF







GND





VBUS 3V3OUT





GND


VBATT













GND



GND



VBUS


0.1uF

|Col1|Col2|
|---|---|
|F<br>||



GND



VBUS VBUS


~~4~~ .7uF



GND 2 VCC BAT 9 1







TB3.5mm





+






|7 8 9 10|Col2|
|---|---|
|7|7|
|7|2K2|


GND



GND


EEPROM Setting



GND



GND



GND







GND



GND



VBUS





**CBUS2**



**SLEEP#**









1A when connected to a dedicated charger port
0.4A when enumerated

0.1A when not enumerated and not in sleep

0A when in sleep


|X-Chip Pin|Function|
|---|---|
|**CBUS0**<br>**CBUS1**<br>|**BCD#**<br>**PWREN#**<br>|



JUMPER-2mm JP1 2-3 NCT Disabled (Default)




|Battery Options|Col2|
|---|---|
|**attery Charger Enable**<br>**orce Power Enable**|**X**|
|**e-acticate Sleep**|**X**|



SIP-3


|JP1<br>NCT Available|Col2|
|---|---|
|1-2<br>2-3|NCT Enabled<br>NCT Disabled (Default|



GND





**Figure 7.6 USB Battery Charging Detection (3 pin)**

To calculate the equivalent resistance on the LTC4053 PROG pin select a charge current, then Res =
1500V/I chg.

For more configuration options of the LTC4053 refer to - [AN_175 Battery Charger Detection over USB](https://ftdichip.com/document/application-notes/)
[with FT-X Devices](https://ftdichip.com/document/application-notes/)

**Note:** If the FT231X is connected to a standard host port such that the device is enumerated the battery
charge detection signal is inactive as the device will not be in suspend.

**7.5** **LED Interface**

Any of the CBUS I/O pins can be configured to drive an LED. The FT231X has 3 configuration options for
driving LEDs from the CBUS. These are TXLED#, RXLED#, and TX&RXLED#. Refer to Section 3.3 for
configuration options.


  TXLED# indicates data is being transmitted on the UART TxD pin

  RXLED# indicates data is being received on the RxD pin of the UART

  TX&RXLED# uses a single CBUS pin to indicate data in either direction


Copyright © Future Technology Devices International Limited 27


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


VCCIO



RX






|TX<br>270R 2<br>FT231X<br>TXLED#<br>CBUS[0...3]<br>CBUS[0...3] RXLED#|Col2|
|---|---|
|**FT231X**<br>CBUS[0...3]<br>CBUS[0...3]|**FT231X**<br>CBUS[0...3]<br>CBUS[0...3]|



**Figure 7.7 Dual LED Configuration**

An example of using the FT231X to drive LEDs is shown in Figure 7.7. In this application one of the CBUS
pins is used to indicate transmission of data (TXLED#) and another is used to indicate receiving data
(RXLED#). When data is being transmitted or received the respective pins will drive from tri-state to low
to provide indication on the LEDs of data transfer. A digital one-shot is used so that even a small
percentage of data transfer is visible to the end user.


VCCIO





**Figure 7.8 Single LED Configuration**

Another example of using the FT231X to drive LEDs is shown in Figure 7.8. In this example one of the
CBUS pins is used to indicate when data is being transmitted or received by the device (TX&RXLED). In
this configuration the FT231X will drive only a single LED.


Copyright © Future Technology Devices International Limited 28


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **8 Internal MTP Memory Configuration**


The FT231X includes an internal MTP memory which holds the USB configuration descriptors, other
configuration data for the chip and also user data areas. Following a power-on reset or a USB reset the
FT231X will scan its internal MTP memory and read the USB configuration descriptors stored there.
In many cases, the default values programmed into the MTP memory will be suitable and no reprogramming will be necessary. The defaults can be found in Section 8.1.

The MTP memory in the FT231X can be programmed over USB if the values need to be changed for a
particular application. Further details of this are provided from section 0 onwards.

Users who do not have their own USB Vendor ID but who would like to use a unique Product ID in their
design can apply to FTDI for a free block of unique PIDs. See [TN_100 USB Vendor ID/Product ID](https://ftdichip.com/document/technical-notes/)
[Guidelines](https://ftdichip.com/document/technical-notes/) for more details.

**8.1** **Default Values**

The default factory programmed values of the internal MTP memory are shown in Table 8.1.

























|Col1|Parameter|Value|Notes|Col5|
|---|---|---|---|---|
||USB Vendor ID (VID)|0403h|FTDI default VID (hex)|FTDI default VID (hex)|
||USB Product UD (PID)|6015h|FTDI default PID (hex)|FTDI default PID (hex)|
||Serial Number Enabled?|Yes|||
||Serial Number|See Note|A unique serial number is generated and<br>programmed into the MTP memory during device<br>final test.|A unique serial number is generated and<br>programmed into the MTP memory during device<br>final test.|
||Pull down I/O Pins in USB<br>Suspend|Disabled|Enabling this option will make the device pull down<br>on the UART interface lines when in USB suspend<br>mode (PWREN# is high).|Enabling this option will make the device pull down<br>on the UART interface lines when in USB suspend<br>mode (PWREN# is high).|
||Manufacturer Name|FTDI|||
||Product Description|FT231X USB UART|||
||Max Bus Power Current|90mA|||
||Power Source|Bus Powered|||
||Device Type|FT231X|||
||USB Version|0200|Returns USB 2.0 device description to the host.<br>Note: The device is a USB 2.0 Full Speed device<br>(12Mb/s) as opposed to a USB 2.0 High Speed<br>device (480Mb/s).|Returns USB 2.0 device description to the host.<br>Note: The device is a USB 2.0 Full Speed device<br>(12Mb/s) as opposed to a USB 2.0 High Speed<br>device (480Mb/s).|
||Remote Wake Up|Enabled|Taking RI# low will wake up the USB host controller<br>from suspend in approximately 20ms.|Taking RI# low will wake up the USB host controller<br>from suspend in approximately 20ms.|
||DBUS Drive Current<br>Strength|4mA|Options are 4mA, 8mA, 12mA, 16mA|Options are 4mA, 8mA, 12mA, 16mA|
||DBUS slew rate|Slow|Options are slow or fast|Options are slow or fast|
||DBUS Schmitt Trigger<br>Enable|Normal|Options are normal or Schmitt|Options are normal or Schmitt|
||CBUS Drive Current<br>Strength|4mA|Options are 4mA, 8mA, 12mA, 16mA|Options are 4mA, 8mA, 12mA, 16mA|
||CBUS slew rate|Slow|Options are slow or fast|Options are slow or fast|
||CBUS Schmitt Trigger<br>Enable|Normal|Options are normal or Schmitt|Options are normal or Schmitt|
||Load VCP Driver|Enabled**|Makes the device load the VCP driver interface for<br>the device.|Makes the device load the VCP driver interface for<br>the device.|
||CBUS0|TXDEN|Default configuration of CBUS0 – Transmit data<br>enable for RS485|Default configuration of CBUS0 – Transmit data<br>enable for RS485|
||CBUS1|TXLED#|Default configuration of CBUS1 – Transmit LED<br>drive.|Default configuration of CBUS1 – Transmit LED<br>drive.|
||CBUS2|RXLED#|Default configuration of CBUS2 – Receive LED drive.|Default configuration of CBUS2 – Receive LED drive.|
||CBUS3|SLEEP#|Default configuration of CBUS3 – SLEEP#. Logic 0<br>when the device is in suspend.|Default configuration of CBUS3 – SLEEP#. Logic 0<br>when the device is in suspend.|
||Invert TXD|Disabled|Signal on this pin becomes TXD# if enable.|Signal on this pin becomes TXD# if enable.|
||Invert RXD|Disabled|Signal on this pin becomes RXD# if enable.|Signal on this pin becomes RXD# if enable.|
||Invert RTS#|Disabled|Signal on this pin becomes RTS if enable.|Signal on this pin becomes RTS if enable.|


Copyright © Future Technology Devices International Limited 29


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

|Col1|Parameter|Value|Notes|Col5|
|---|---|---|---|---|
||Invert CTS#|Disabled|Signal on this pin becomes CTS if enable.|Signal on this pin becomes CTS if enable.|
||Invert DTR#|Disabled|Signal on this pin becomes DTR if enable.|Signal on this pin becomes DTR if enable.|
||Invert DSR#|Disabled|Signal on this pin becomes DSR if enable.|Signal on this pin becomes DSR if enable.|
||Invert DCD#|Disabled|Signal on this pin becomes DCD if enable.|Signal on this pin becomes DCD if enable.|
||Invert RI#|Disabled|Signal on this pin becomes RI if enable.|Signal on this pin becomes RI if enable.|



**Table 8.1 Default Internal MTP Memory Configuration**

**VCP disabled in Rev B silicon in error.


**Note:** The Internal MTP is protected with a checksum. This checksum can fail if the memory is
programmed incorrectly by the user, or if it’s exposed to X-Ray during PCB inspection. When a device
fails this checksum then it automatically reverts back to FTDI default settings. This is a protection
mechanism to allow the device to attempt to successfully enumerate with the USB Host. In such cases
the default VID and PID will be set as per Table 8.1 and the Product Description would read FT232EX.
[FT_PROG](https://ftdichip.com/utilities/#ft_prog) can be used to attempt to recover the memory. If recovery is not possible then please Contact
Us.


**8.2** **Methods of Programming the MTP Memory**

**8.2.1** **Programming the MTP memory over USB**

The MTP memory on all FT-X devices can be programmed over USB. This method is the same as for the
EEPROM on other FTDI devices such as the FT232R. No additional hardware, connections or programming
voltages are required. The device is simply connected to the host computer in the same way that it would
be for normal applications, and the FT_PROG utility is used to set the required options and program the
device.

The FT_PROG utility is provided free-of-charge and the user guide is also available at this link [http://www.ftdichip.com/Support/Utilities.htm#FT_Prog.](http://www.ftdichip.com/Support/Utilities.htm#FT_Prog) Additionally, D2XX commands can be used to
program the MTP memory from within user applications. For more information on the commands

'
[available, please refer to the D2XX Programmer](https://ftdichip.com/document/programming-guides/) s Guide.

**8.3** **Memory Map**

The FT-X family MTP memory has various areas which come under three main categories:


  - User Memory Area

  - Configuration Memory Area (writable)

  - Configuration Memory Area (non-writable)

|Memory Area Description|Word Address|
|---|---|
|User Memory Area 2<br>Accessible via USB|0x3FF – 0x80|
|Configuration Memory Area<br>Accessible via USB|0x7E – 0x50|
|Configuration Memory Area<br>Cannot be written|0x4E – 0x40|



Copyright © Future Technology Devices International Limited 30


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261







|Col1|Memory Area Description|Word Address|Col4|
|---|---|---|---|
||User Memory Area 1<br>Accessible via USB|0x3E – 0x12|0x3E – 0x12|
||Configuration Memory Area<br>Accessible via USB|0x10 – 0x00|0x10 – 0x00|


**Figure 8.1: Simplified memory map for the FT-X**

**User Memory Area**

The User Memory Areas are highlighted in Green on the memory map. They can be read and written via
USB on the FT231X. All locations within this range are freely programmable; no areas have special
functions and there is no checksum for the user area.

Note that the application should consider the specification for the number of write cycles in Section 5.4 if
it will be writing to the MTP memory multiple times.

**Configuration Memory Area (writable)**

This area stores the configuration data for the device, including the data which is returned to the host in
the configuration descriptors (e.g. the VID, PID and string descriptions) and values which set the
hardware configuration (the signal assigned to each CBUS pin for example).

These values can have a significant effect on the behaviour of the device. Steps must be taken to ensure
that these locations are not written to un-intentionally by an application which is intended to access only
the user area.

This area is included in a checksum which covers configuration areas of the memory, and so changing
any value can also cause this checksum to fail.

**Configuration Memory Area (non-writable)**

This is a reserved area and the application should not write to this area of memory. Any attempt to write
these locations will fail.


Copyright © Future Technology Devices International Limited 31


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **9 Package Parameters**


The FT231X is available in two different packages. The FT231XS is the SSOP-20 option and the FT231XQ
is the QFN-20 package option. The solder reflow profile for both packages is described in Section 9.5.


**9.1** **SSOP-20 Package Mechanical Dimensions**


**Figure 9.1 SSOP-20 Package Dimensions**


The FT231XS is supplied in a RoHS compliant 20 pin SSOP package. The package is lead (Pb) free and
uses a ‘green’ compound. The package is fully compliant with European Union directive 2002/95/EC.

This package is nominally 8.66mm x 3.91mm body (8.66mm x 5.99mm including pins). The pins are on a
0.635 mm pitch. The above mechanical drawing shows the SSOP-20 package.


Copyright © Future Technology Devices International Limited 32


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**9.2** **SSOP-20 Package Markings**


**Figure 9.2 SSOP-20 Package Markings**

The date code format is **YYXX** where XX = 2-digit week number, YY = 2-digit year number. This is
followed by the revision number.

The code **XXXXXXXXXXXX** is the manufacturing LOT code.


Copyright © Future Technology Devices International Limited 33


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**9.3** **QFN-20 Package Mechanical Dimensions**


**Figure 9.3 QFN-20 Package Dimensions**


The FT231XQ is supplied in a RoHS compliant leadless QFN-20 package. The package is lead (Pb) free
and uses a ‘green’ compound. The package is fully compliant with European Union directive 2002/95/EC.

This package is nominally 4.00mm x 4.00mm. The solder pads are on a 0.50mm pitch. The above
mechanical drawing shows the QFN-20 package. All dimensions are in millimetres.

The centre pad on the base of the FT231XQ is internally connected to ground.


Copyright © Future Technology Devices International Limited 34


**9.4** **QFN-20 Package Markings**


**20**


**1**



Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**15**







**6**



**10**



**Figure 9.4 QFN-20 Package Markings**

The date code format is **YYXX** where XX = 2-digit week number, YY = 2-digit year number. This is
followed by the revision number.

The code **XXXXXXX** is the manufacturing LOT code.


Copyright © Future Technology Devices International Limited 35


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


**9.5** **Solder Reflow Profile**

The FT231X is supplied in Pb free 20 LD SSOP and QFN-20 packages. The recommended solder reflow
profile for both package options is shown in Figure 9.5.





T p


T L


25



















**Figure 9.5 FT231X Solder Reflow Profile**

The recommended values for the solder reflow profile are detailed in Table 9.1. Values are shown for both
a completely Pb free solder process (i.e. the FT231X is used with Pb free solder), and for a non-Pb free
solder process (i.e. the FT231X is used with non-Pb free solder).
















|Profile Feature|Pb Free Solder<br>Process|Non-Pb Free Solder Process|
|---|---|---|
|Average Ramp Up Rate (Ts to Tp)|3°C / second Max.|3°C / Second Max.|
|Preheat<br>- Temperature Min (Ts Min.)<br>- Temperature Max (Ts Max.)<br>- Time (ts Min to ts Max)|<br>150°C<br>200°C<br>60 to 120 seconds|<br>100°C<br>150°C<br>60 to 120 seconds|
|Time Maintained Above Critical<br>Temperature TL:<br>- Temperature (TL)<br>- Time (tL)|<br>217°C<br>60 to 150 seconds|<br>183°C<br>60 to 150 seconds|
|Peak Temperature (Tp)|260°C|240°C|
|Time within 5°C of actual Peak<br>Temperature (tp)|20 to 40 seconds|20 to 40 seconds|
|Ramp Down Rate|6°C / second Max.|6°C / second Max.|
|Time for T= 25°C to Peak Temperature,<br>Tp|8 minutes Max.|6 minutes Max.|



**Table 9.1 Reflow Profile Parameter Values**


Copyright © Future Technology Devices International Limited 36


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **10 Contact Information**


**Europe, Middle East, Africa** **Americas**


Future Technology Devices International Limited Future Technology Devices International Limited (USA)
Unit 1, 2 Seaward Place, Centurion Business Park 7130 SW Fir Loop
Glasgow G41 1HH Tigard, OR 97223-8160
United Kingdom USA
Tel: +44 (0) 141 429 2777 Tel: +1 (503) 547 0988


E-mail (Sales) [sales1@ftdichip.com](mailto:sales1@ftdichip.com) E-mail (Sales) [us.sales@ftdichip.com](mailto:us.sales@ftdichip.com)
E-mail (Technical Support) [support1@ftdichip.com](mailto:support1@ftdichip.com) E-mail (Technical Support) [us.support@ftdichip.com](mailto:us.support@ftdichip.com)


**Asia Pacific** **China**


Future Technology Devices International Limited Future Technology Devices International Limited (China)
(Singapore) Room 1103, No. 666 West Huaihai Road,
1 Tai Seng Avenue, Tower A #03-06 Shanghai, 200052
Singapore 536464 China
Tel: (+65) 6841 1174 Tel: +86 21 62351596

Tel (Technical Support): +886 (0) 2 8797 1330

E-mail (Sales) [tw.sales1@ftdichip.com](mailto:tw.sales1@ftdichip.com) E-mail (Sales) [cn.sales@ftdichip.com](mailto:cn.sales@ftdichip.com)
E-mail (Technical Support) [tw.support1@ftdichip.com](mailto:tw.support1@ftdichip.com) E-mail (Technical Support) [cn.support@ftdichip.com](mailto:cn.support@ftdichip.com)


**Web Site**


[http://ftdichip.com](http://ftdichip.com/)


**Distributor and Sales Representatives**


[Please visit the Sales Network page of the FTDI Web site](http://ftdichip.com/FTSalesNetwork.htm) for the contact details of our distributor(s) and sales
representative(s) in your country.


System and equipment manufacturers and designers are responsible to ensure that their systems, and any Future Technology Devices
International Ltd (FTDI) devices incorporated in their systems, meet all applicable safety, regulatory and system-level performance
requirements. All application-related information in this document (including application descriptions, suggested FTDI devices and other
materials) is provided for reference only. While FTDI has taken care to assure it is accurate, this information is subject to customer
confirmation, and FTDI disclaims all liability for system designs and for any applications assistance provided by FTDI. Use of FTDI
devices in life support and/or safety applications is entirely at the user’s risk, and the user agrees to defend, indemnify, and hold
harmless FTDI from any and all damages, claims, suits, or expense resulting from such use. This document is subject to change without
notice. No freedom to use patents or other intellectual property rights is implied by the publication of this document. Neither the whole
nor any part of the information contained in, or the product described in this document, may be adapted, or reproduced in any material
or electronic form without the prior written consent of the copyright holder. Future Technology Devices International Ltd, Unit 1, 2
Seaward Place, Centurion Business Park, Glasgow G41 1HH, United Kingdom. Scotland Registered Company Number: SC136640


Copyright © Future Technology Devices International Limited 37


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **Appendix A – References**


**Document/Web References**

[AN232R-01 Bit Bang Modes for the FT232R and FT245R](https://ftdichip.com/document/application-notes/)


[AN232B-05 Configuring FT232R, FT2232 and FT232BM Baud Rates](https://ftdichip.com/document/application-notes/)


[AN_100 Using the FT232R/FT245R with an External Crystal or Oscillator](https://ftdichip.com/document/application-notes/)


[AN_107 Advanced Driver Options](https://ftdichip.com/document/application-notes/)


[AN_120 Aliasing VCP Baud Rates](https://ftdichip.com/document/application-notes/)


[AN_121 Accessing the EEPROM User Area of FTDI Devices](https://ftdichip.com/document/application-notes/)


[AN_126 User Guide for FT232B/R Factory Test Utility](https://ftdichip.com/document/application-notes/)


[AN_175 Battery Charger Detection over USB with FT-X Devices](https://ftdichip.com/document/application-notes/)


[TN_100 USB Vendor ID/Product ID Guidelines](https://ftdichip.com/document/technical-notes/)


[TN_162 Bus Powered with Power Switching Configuration](https://ftdichip.com/document/technical-notes/)


[https://www.analog.com/en/products/ltc4053-4.2.html](https://www.analog.com/en/products/ltc4053-4.2.html)


                          -                          -                          https://www.analog.com/media/en/reference [design](https://www.analog.com/media/en/reference-design-documentation/design-notes/dn320f.pdf) documentation/design notes/dn320f.pdf


[http://www.usb.org](http://www.usb.org/)


**Acronyms and Abbreviations**

|Terms|Description|
|---|---|
|DCP|Dedicated Charging Port|
|FIT|Failure In Time|
|FIFO|First In First Out|
|LSB|Least Significant Bit First|
|MSB|Most Significant Bit First|
|MTBF|Mean Time Between Failures|
|MTP|Multi-time Programmable memory|
|MTTF|Mean Time To Failure|
|QFN|Quad Flat Non-leaded package|
|SIE|Serial Interface Engine|
|USB|Universal Serial Bus|
|UART|Universal Asynchronous Receiver / Transmitter|



Copyright © Future Technology Devices International Limited 38


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **Appendix B – List of Figures and Tables**


**List of Figures**


Figure 2.1 FT231X Block Diagram ................................................................................................... 4


Figure 3.1 QFN Schematic Symbol .................................................................................................. 7


Figure 3.2 SSOP Schematic Symbol ................................................................................................ 8


Figure 6.1 Bus Powered Configuration ........................................................................................... 19


Figure 6.2 Self-Powered Configuration ........................................................................................... 20


Figure 6.3 Bus Powered with Power Switching Configuration ............................................................ 21


Figure 7.1 Application Example showing USB to RS232 Converter ..................................................... 22


Figure 7.2 Application Example Showing USB to RS485 Converter .................................................... 23


Figure 7.3 USB to RS422 Converter Configuration ........................................................................... 24


Figure 7.4 USB Battery Charging Detection (1 pin).......................................................................... 25


Figure 7.5 USB Battery Charging Detection (2 pin).......................................................................... 26


Figure 7.6 USB Battery Charging Detection (3 pin).......................................................................... 27


Figure 7.7 Dual LED Configuration ................................................................................................ 28


Figure 7.8 Single LED Configuration .............................................................................................. 28


Figure 8.1: Simplified memory map for the FT-X ............................................................................ 31


Figure 9.1 SSOP-20 Package Dimensions ....................................................................................... 32


Figure 9.2 SSOP-20 Package Markings .......................................................................................... 33


Figure 9.3 QFN-20 Package Dimensions ......................................................................................... 34


Figure 9.4 QFN-20 Package Markings ............................................................................................ 35


Figure 9.5 FT231X Solder Reflow Profile......................................................................................... 36


**List of Tables**


Table 3.1 Power and Ground .......................................................................................................... 7


Table 3.2 Common Function pins .................................................................................................... 7


Table 3.3 UART Interface and CBUS Group ...................................................................................... 8


Table 3.4 Power and Ground .......................................................................................................... 9


Table 3.5 Common Function pins .................................................................................................... 9


Table 3.6 UART Interface and CBUS Group ...................................................................................... 9


Table 3.7 CBUS Configuration Control ........................................................................................... 10


Table 5.1 Absolute Maximum Ratings ............................................................................................ 14


Table 5.2 ESD and Latch-Up Specifications .................................................................................... 14


Table 5.3 Operating Voltage and Current ....................................................................................... 15


Table 5.4 I/O Pin Characteristics VCCIO = +3.3V (except USB PHY pins) ........................................... 16


Table 5.5 I/O Pin Characteristics VCCIO = +2.5V (except USB PHY pins) ........................................... 17


Table 5.6 I/O Pin Characteristics VCCIO = +1.8V (except USB PHY pins) ........................................... 18


Copyright © Future Technology Devices International Limited 39


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261


Table 5.7 USB I/O Pin (USBDP, USBDM) Characteristics .................................................................. 18


Table 5.8 MTP Memory Characteristics ........................................................................................... 18


Table 5.9 Internal Clock Characteristics ......................................................................................... 18


Table 8.1 Default Internal MTP Memory Configuration ..................................................................... 30


Table 9.1 Reflow Profile Parameter Values ..................................................................................... 36


Copyright © Future Technology Devices International Limited 40


Datasheet

**FT231X USB TO FULL HANDSHAKE UART IC**


Version 1.6


Document No.: FT_000565 Clearance No.: FTDI# 261

###### **Appendix C – Revision History**


Document Title: FT231X USB to FULL HANDSHAKE UART IC


Document Reference No.: FT_000565


Clearance No.: FTDI# 261


                                  Product Page: [https://ftdichip.com/product](https://ftdichip.com/product-category/products/ic/) category/products/ic/


Document Feedback: [Send Feedback](mailto:docufeedback@ftdichip.com?subject=Document%20Feedback:%20DS_FT231X%20Version%201.6)
















|Revision|Changes|Date|
|---|---|---|
|1.0|Initial Release.|08-02-2012|
|1.1|Added USB compliance in section 1.3; Clarified MTP Reliability in<br>table 5.8; Section 8.1, added a note “VCP disabled in Rev. B Silicon<br>in error.|17-04-2012|
|1.2|Clarified IO is tolerant of 5V input; Updated TID info.|15-02-2013|
|1.3|Removed CBUS default references from Section 7.2; Updated the<br>QFN16 Dimension in section 9.3; Corrected VBUS Sense, corrected<br>FT230X reference; Updated China office address.|09-02-2015|
|1.4|Updated section 4.2 – reset can be connected to VCCIO if not used;<br>Updated section 3.3 and section 7.5 to provide additional<br>information on Tx and Rx LEDs.|21-09-2021|
|1.5|Updated Driver section.<br>Added MTTF.<br>Added statement about X-ray and MTP in section 5.4.<br>Changed Vih value in table 5.5.|10-05-2024|
|1.6|Updated minimum Voh in Table 5.7.<br>Updated MTTF/MTBF/FIT in Table 5.1.<br>Added note on memory checksum and recovery text underneath<br>Table 8.1.<br>Updated X-ray note in section 5.4.<br>Swapped TXLED and RXLED to match FT_PROG.<br>Updated Contact Information.|26-06-2025|



Copyright © Future Technology Devices International Limited 41


