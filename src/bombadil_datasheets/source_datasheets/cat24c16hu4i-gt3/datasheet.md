**[Share Feedback](https://cx.onsemi.com/jfe/form/SV_2co9s03RTjSwGHQ?tdid=CAT24C01/D&tdt=DATASHEET&palcodes=CA)**
Your Opinion Matters



**DATA SHEET**
**[www.onsemi.com](http://www.onsemi.com/)**


# EEPROM Serial 2/4/8/16�Kb I [2] C CAT24C02, CAT24C04, CAT24C08, CAT24C16

**Description**
The CAT24C02/04/08/16 are 2−Kb, 4−Kb, 8−Kb and 16−Kb
respectively I [2] C Serial EEPROM devices organized internally as
16/32/64 and 128 pages respectively of 16 bytes each. All devices
support both the Standard (100 kHz) as well as Fast (400 kHz) I [2] C
protocol.
Data is written by providing a starting address, then loading 1 to 16
contiguous bytes into a Page Write Buffer, and then writing all data to
non−volatile memory in one internal write cycle. Data is read by
providing a starting address and then shifting out data serially while
automatically incrementing the internal address count.
External address pins make it possible to address up to eight
CAT24C02, four CAT24C04, two CAT24C08 and one CAT24C16
device on the same bus.


**Features**

- Supports Standard and Fast I [2] C Protocol

- 1.7 V to 5.5 V Supply Voltage Range

- 16−Byte Page Write Buffer

- Hardware Write Protection for Entire Memory

- Schmitt Triggers and Noise Suppression Filters on I [2] C Bus Inputs
(SCL and SDA)

- Low power CMOS Technology

- More than 1,000,000 Program/Erase Cycles

- 100 Year Data Retention

- Industrial and Extended Temperature Range

- These Devices are Pb−Free, Halogen Free/BFR Free and are RoHS
Compliant


This document contains information on some products that are still under development.
**onsemi** reserves the right to change or discontinue these products without notice.



**TSSOP−8**
**Y SUFFIX**
**CASE 948AL**



**UDFN8−EP**
**HU4 SUFFIX**
**CASE 517AZ**


**TSOT−23**
**TD SUFFIX**
**CASE 419AE**



**SOIC−8**
**W SUFFIX**
**CASE 751BD**


**WLCSP−5****
**C5A SUFFIX**
**CASE 567DD**



**WLCSP−4****
**C4A SUFFIX**
**CASE 567DC**


**WLCSP−4****
**C4U SUFFIX**
**CASE 567NX**



** WLCSP are available for the CAT24C04,
CAT24C08 and CAT24C16 only.

For serial EEPROM in the US8 package, please
consult the N24C02 datasheet


**ORDERING INFORMATION**

See detailed ordering and shipping information in the package
dimensions section on page 10 of this data sheet.



© Semiconductor Components Industries, LLC, 2016 **1** Publication Order Number:
**July, 2022 − Rev. 36** **CAT24C01/D**


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PIN CONFIGURATIONS AND MARKING INFORMATION**



SDA


VCC

WP

SCL

SDA



SCL


A2, A1, A0


WP



VCC

|Col1|CAT2|4Cxx|Col4|
|---|---|---|---|
|||||
|||||



VSS


**Figure 1. Functional Symbol**



**Table 1. PIN FUNCTION**

|Pin Name†|Function|
|---|---|
|A0, A1, A2|Device Address Input|
|SDA|Serial Data Input/Output|
|SCL|Serial Clock Input|
|WP|Write Protect Input|
|VCC|Power Supply|
|VSS|Ground|
|NC|No Connect|



†The exposed pad for the UDFN packages can be left floating or
connected to Ground.



**CAT24C__**
**16 / 08 / 04 / 02**
NC / NC / NC / A0



1 2 Pin 1 1 2 3





Pin 1





/ NC / A /



NC / NC



A1 / A1



A


B


C



/ A2 / A2 / A2



/ A / A /



NC





VSS




|Col1|Col2|1 8<br>2 7<br>3 6<br>4 5|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||



**SOIC (W), TSSOP (Y),**
**UDFN−EP (HU4) (Top View)**



**WLCSP−4***** **WLCSP−5*****
**(Top Views)**

*** WLCSP are available for the CAT24C04,
CAT24C08 and CAT24C16 only.


**TOP MARKING FOR WLCSP**

**(Ball Down)**



WP


VCC





Pin 1









Pin 1





VSS


SDA




|Col1|Col2|1 5<br>2<br>3 4|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||



**TSOT−23 (TD) (Top View)**



**WLCSP−4** **WLCSP−4** **WLCSP−5**
**(C4A)** **(C4U)**


X = Specific Device
X = Code
4 or R = 24C04
8 or T = 24C08
6 or V = 24C16

Y = Production Year (Last Digit)
M = Production Month (1−9, O, N, D)
W = Production Week



**www.onsemi.com**

**2**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**Table 2. ABSOLUTE MAXIMUM RATINGS**

|Parameters|Ratings|Units|
|---|---|---|
|Storage Temperature|−65 to +150|°C|
|Voltage on any pin with respect to Ground (Note 1)|−0.5 to +6.5|V|



Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality
should not be assumed, damage may occur and reliability may be affected.
1. During input transitions, voltage undershoot on any pin should not exceed −1 V for more than 20 ns. Voltage overshoot on pins A0, A1, A2
and WP should not exceed VCC + 1 V for more than 20 ns, while voltage on the I [2] C bus pins, SCL and SDA, should not exceed the absolute
maximum ratings, irrespective of VCC.


**Table 3. RELIABILITY CHARACTERISTICS** (Note 2)

|Symbol|Parameter|Min|Units|
|---|---|---|---|
|NEND (Note 3)|Endurance|1,000,000|Program / Erase Cycles|
|TDR|Data Retention|100|Years|



2. These parameters are tested initially and after a design or process change that affects the parameter according to appropriate AEC−Q100
and JEDEC test methods.
3. Page Mode, VCC = 5 V, 25 ° C.


**Table 4. D.C. OPERATING CHARACTERISTICS**
(VCC = 1.8 V to 5.5 V, TA = −40 ° C to +125 ° C and VCC = 1.7 V to 5.5 V, TA = −40 ° C to +85 ° C, unless otherwise specified.)












|Symbol|Parameter|Test Conditions|Col4|Min|Max|Units|
|---|---|---|---|---|---|---|
|ICCR|Read Current|Read, fSCL = 400 kHz|||1|mA|
|ICCW|Write Current|Write, fSCL = 400 kHz|||2|mA|
|ISB|Standby Current|All I/O Pins at GND or VCC|TA = −40°C to +85°C<br>VCC ≤ 3.3 V||1|A|
|ISB|Standby Current|All I/O Pins at GND or VCC|TA = −40°C to +85°C<br>VCC > 3.3 V||3|3|
|ISB|Standby Current|All I/O Pins at GND or VCC|TA = −40°C to +125°C||5|5|
|IL|I/O Pin Leakage|Pin at GND or VCC|||2|A|
|VIL|Input Low Voltage|||−0.5|0.3 x VCC|V|
|VIH|Input High Voltage|A0, A1, A2 and WP||0.7 x VCC|VCC + 0.5|V|
|VIH|Input High Voltage|SCL and SDA||0.7 x VCC|5.5|5.5|
|VOL|Output Low<br>Voltage|VCC > 2.5 V, IOL = 3 mA|||0.4|0.4|
|VOL|Output Low<br>Voltage|VCC < 2.5 V, IOL = 1 mA|||0.2|0.2|



Product parametric performance is indicated in the Electrical Characteristics for the listed test conditions, unless otherwise noted. Product
performance may not be indicated by the Electrical Characteristics if operated under different conditions.



**www.onsemi.com**

**3**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**Table 5. PIN IMPEDANCE CHARACTERISTICS**
(VCC = 1.8 V to 5.5 V, TA = −40 ° C to +125 ° C and VCC = 1.7 V to 5.5 V, TA = −40 ° C to +85 ° C, unless otherwise specified.)






|Symbol|Parameter|Conditions|Max|Units|
|---|---|---|---|---|
|CIN(Note 4)|SDA Pin Capacitance|VIN = 0 V, f = 1.0 MHz, VCC = 5.0 V|8|pF|
|CIN(Note 4)|Other Pins|Other Pins|6|pF|
|IWP (Note 5)|WP Input Current|VIN < VIH, VCC = 5.5 V|130|A|
|IWP (Note 5)|WP Input Current|VIN < VIH, VCC = 3.3 V|120|120|
|IWP (Note 5)|WP Input Current|VIN < VIH, VCC = 1.7 V|80|80|
|IWP (Note 5)|WP Input Current|VIN > VIH|2|2|
|IA (Note 5)|Address Input Current<br> (A0, A1, A2)<br> Product Rev H: CAT24C02<br> Product Rev K: CAT24C04,<br> CAT24C08, CAT24C16|VIN < VIH, VCC = 5.5 V|50|A|
|IA (Note 5)|Address Input Current<br> (A0, A1, A2)<br> Product Rev H: CAT24C02<br> Product Rev K: CAT24C04,<br> CAT24C08, CAT24C16|VIN < VIH, VCC = 3.3 V|35|35|
|IA (Note 5)|Address Input Current<br> (A0, A1, A2)<br> Product Rev H: CAT24C02<br> Product Rev K: CAT24C04,<br> CAT24C08, CAT24C16|VIN < VIH, VCC = 1.7 V|25|25|
|IA (Note 5)|Address Input Current<br> (A0, A1, A2)<br> Product Rev H: CAT24C02<br> Product Rev K: CAT24C04,<br> CAT24C08, CAT24C16|VIN > VIH|2|2|



4. These parameters are tested initially and after a design or process change that affects the parameter according to appropriate AEC−Q100
and JEDEC test methods.
5. When not driven, the WP, A0, A1 and A2 pins are pulled down to GND internally. For improved noise immunity, the internal pull−down is
relatively strong; therefore the external driver must be able to supply the pull−down current when attempting to drive the input HIGH. To
conserve power, as the input level exceeds the trip point of the CMOS input buffer (~ 0.5 x VCC), the strong pull−down reverts to a weak
current source.


**Table 6. A.C. CHARACTERISTICS**
(Note 6) (VCC = 1.8 V to 5.5 V, TA = −40 ° C to +125 ° C and VCC = 1.7 V to 5.5 V, TA = −40 ° C to +85 ° C, unless otherwise specified.)







|Symbol|Parameter|Standard|Col4|Fast|Col6|Units|
|---|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Min**|**Max**|**Min**|**Max**|**Max**|
|FSCL|Clock Frequency||100||400|kHz|
|tHD:STA|START Condition Hold Time|4||0.6||s|
|tLOW|Low Period of SCL Clock|4.7||1.3||s|
|tHIGH|High Period of SCL Clock|4||0.6||s|
|tSU:STA|START Condition Setup Time|4.7||0.6||s|
|tHD:DAT|Data In Hold Time|0||0||s|
|tSU:DAT|Data In Setup Time|250||100||ns|
|tR|SDA and SCL Rise Time||1000||300|ns|
|tF (Note 6)|SDA and SCL Fall Time||300||300|ns|
|tSU:STO|STOP Condition Setup Time|4||0.6||s|
|tBUF|Bus Free Time Between STOP and START|4.7||1.3||s|
|tAA|SCL Low to Data Out Valid||3.5||0.9|s|
|tDH|Data Out Hold Time|100||100||ns|
|Ti (Note 6)|Noise Pulse Filtered at SCL and SDA Inputs||100||100|ns|
|tSU:WP|WP Setup Time|0||0||s|
|tHD:WP|WP Hold Time|2.5||2.5||s|
|tWR|Write Cycle Time||5||5|ms|
|tPU (Notes 7, 8)|Power−up to Ready Mode||1||1|ms|


6. Test conditions according to “AC Test Conditions” table.
7. Tested initially and after a design or process change that affects this parameter.
8. tPU is the delay between the time VCC is stable and the device is ready to accept commands.



**www.onsemi.com**

**4**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**Table 7. A.C. TEST CONDITIONS**


|Input Drive Levels|0.2 x V to 0.8 x V<br>CC CC|
|---|---|
|Input Rise and Fall Time| 50 ns|
|Input Reference Levels|0.3 x VCC, 0.7 x VCC|
|Output Reference Level|0.5 x VCC|
|Output Test Load|Current Source IOL = 3 mA (VCC  2.5 V); IOL = 1 mA (VCC< 2.5 V); CL = 100 pF|



**Power−On Reset (POR)**
Each CAT24Cxx* incorporates Power−On Reset (POR)
circuitry which protects the internal logic against powering
up in the wrong state.
A CAT24Cxx device will power up into Standby mode
after VCC exceeds the POR trigger level and will power
down into Reset mode when VCC drops below the POR
trigger level. This bi−directional POR feature protects the
device against ‘brown−out’ failure following a temporary
loss of power.
_*For common features, the CAT24C02/04/08/16 will be_
_referred to as CAT24Cxx._


**Pin Description**
**SCL** : The Serial Clock input pin accepts the Serial Clock
generated by the Master.
**SDA** : The Serial Data I/O pin receives input data and
transmits data stored in EEPROM. In transmit mode, this pin
is open drain. Data is acquired on the positive edge, and is
delivered on the negative edge of SCL.
**A0, A1 and A2** : The Address inputs set the device address
when cascading multiple devices. When not driven, these
pins are pulled LOW internally.
**WP** : The Write Protect input pin inhibits all write
operations, when pulled HIGH. When not driven, this pin is
pulled LOW internally.


**Functional Description**
The CAT24Cxx supports the Inter−Integrated Circuit
(I [2] C) Bus data transmission protocol, which defines a device
that sends data to the bus as a transmitter and a device
receiving data as a receiver. Data flow is controlled by a
Master device, which generates the serial clock and all
START and STOP conditions. The CAT24Cxx acts as a
Slave device. Master and Slave alternate as either
transmitter or receiver.


**I** **[2]** **C Bus Protocol**
The I [2] C bus consists of two ‘wires’, SCL and SDA. The
two wires are connected to the VCC supply via pull−up
resistors. Master and Slave devices connect to the 2−wire
bus via their respective SCL and SDA pins. The transmitting
device pulls down the SDA line to ‘transmit’ a ‘0’ and
releases it to ‘transmit’ a ‘1’.
Data transfer may be initiated only when the bus is not
busy (see AC Characteristics).



During data transfer, the SDA line must remain stable
while the SCL line is high. An SDA transition while SCL is
high will be interpreted as a START or STOP condition
(Figure 2). The START condition precedes all commands. It
consists of a HIGH to LOW transition on SDA while SCL
is HIGH. The START acts as a ‘wake−up’ call to all
receivers. Absent a START, a Slave will not respond to
commands. The STOP condition completes all commands.
It consists of a LOW to HIGH transition on SDA while SCL
is HIGH.
_**NOTE:**_ _The I/O pins of CAT24Cxx do not obstruct the SCL_
_and SDA lines if the VCC supply is switched off. During_
_power−up, the SCL and SDA pins (connected with pull−up_
_resistors to VCC) will follow the VCC monotonically from_
_VSS (0 V) to nominal VCC value, regardless of pull−up_
_resistor value. The delta between the VCC and the_
_instantaneous voltage levels during power ramping will be_
_determined by the relation between bus time constant_
_(determined by pull−up resistance and bus capacitance) and_
_actual VCC ramp rate._


**Device Addressing**
The Master initiates data transfer by creating a START
condition on the bus. The Master then broadcasts an 8−bit
serial Slave address. For normal Read/Write operations, the
first 4 bits of the Slave address are fixed at 1010 (Ah). The
next 3 bits are used as programmable address bits when
cascading multiple devices and/or as internal address bits.
The last bit of the slave address, R/W, specifies whether a
Read (1) or Write (0) operation is to be performed. The 3
address space extension bits are assigned as illustrated in
Figure 3. A2, A1 and A0 must match the state of the external
address pins, and a10, a9 and a8 are internal address bits.


**Acknowledge**
After processing the Slave address, the Slave responds
with an acknowledge (ACK) by pulling down the SDA line
during the 9th clock cycle (Figure 4). The Slave will also
acknowledge the address byte and every data byte presented
in Write mode. In Read mode the Slave shifts out a data byte,
and then releases the SDA line during the 9 [th] clock cycle. As
long as the Master acknowledges the data, the Slave will
continue transmitting. The Master terminates the session by
not acknowledging the last data byte (NoACK) and by
issuing a STOP condition. Bus timing is illustrated in
Figure 5.



**www.onsemi.com**

**5**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**



SCL


SDA


SCL FROM
MASTER


FROM RECEIVER


SCL


SDA IN


SDA OUT






|Col1|START|Col3|
|---|---|---|
|CONDITION|CONDITION|CONDITION|


|Col1|STOP|Col3|
|---|---|---|
|CONDITION|CONDITION|CONDITION|





**Figure 2. Start/Stop Timing**


**Figure 3. Slave Address Bits**

|B|US RELEASE DELAY (TRANSMITTER)<br>1 8|Col3|9|Col5|Col6|Col7|B<br>(R|
|---|---|---|---|---|---|---|---|
|B<br> <br> <br>|1<br>8<br>US RELEASE DELAY (TRANSMITTER)|||||||
|B<br> <br> <br>|1<br>8<br>US RELEASE DELAY (TRANSMITTER)|||||||
|||||||||
||ACK DELAY ( tAA)|||AC|AC|AC|AC|



**Figure 4. Acknowledge Timing**








|tHIGH|Col2|Col3|
|---|---|---|
|tHD:DAT<br>tHIGH<br>tLOW<br>tHD:SDA|tLOW||
|tHD:DAT<br>tHIGH<br>tLOW<br>tHD:SDA|tLOW||
|tHD:DAT<br>tHIGH<br>tLOW<br>tHD:SDA|||





**Figure 5. Bus Timing**


**www.onsemi.com**

**6**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**WRITE OPERATIONS**



**Byte Write**
In Byte Write mode, the Master sends the START
condition and the Slave address with the R/W bit set to zero
to the Slave. After the Slave generates an acknowledge, the
Master sends the byte address that is to be written into the
address pointer of the CAT24Cxx. After receiving another
acknowledge from the Slave, the Master transmits the data
byte to be written into the addressed memory location. The
CAT24Cxx device will acknowledge the data byte and the
Master generates the STOP condition, at which time the
device begins its internal Write cycle to nonvolatile memory
(Figure 6). While this internal cycle is in progress (tWR), the
SDA output will be tri−stated and the CAT24Cxx will not
respond to any request from the Master device (Figure 7).


**Page Write**
The CAT24Cxx writes up to 16 bytes of data in a single
write cycle, using the Page Write operation (Figure 8). The
Page Write operation is initiated in the same manner as the
Byte Write operation, however instead of terminating after
the data byte is transmitted, the Master is allowed to send up
to fifteen additional bytes. After each byte has been
transmitted the CAT24Cxx will respond with an
acknowledge and internally increments the four low order
address bits. The high order bits that define the page address
remain unchanged. If the Master transmits more than sixteen
bytes prior to sending the STOP condition, the address
counter ‘wraps around’ to the beginning of page and
previously transmitted data will be overwritten. Once all



sixteen bytes are received and the STOP condition has been
sent by the Master, the internal Write cycle begins. At this
point all received data is written to the CAT24Cxx in a single
write cycle.


**Acknowledge Polling**
The acknowledge (ACK) polling routine can be used to
take advantage of the typical write cycle time. Once the stop
condition is issued to indicate the end of the host’s write
operation, the CAT24Cxx initiates the internal write cycle.
The ACK polling can be initiated immediately. This
involves issuing the start condition followed by the slave
address for a write operation. If the CAT24Cxx is still busy
with the write operation, NoACK will be returned. If the
CAT24Cxx has completed the internal write operation, an
ACK will be returned and the host can then proceed with the
next read or write operation.


**Hardware Write Protection**
With the WP pin held HIGH, the entire memory is
protected against Write operations. If the WP pin is left
floating or is grounded, it has no impact on the operation of
the CAT24Cxx. The state of the WP pin is strobed on the last
falling edge of SCL immediately preceding the first data
byte (Figure 9). If the WP pin is HIGH during the strobe
interval, the CAT24Cxx will not acknowledge the data byte
and the Write request will be rejected.


**Delivery State**
The CAT24Cxx is shipped erased, i.e., all bytes are FFh.



BUS ACTIVITY:


MASTER


SLAVE



S
T
A
R
T



A
C
K



A
C
K



ADDRESS DATA
SLAVE BYTE BYTE
ADDRESS

a7 − a0 d7 − d0



S
T
O
P



A
C
K



**Figure 6. Byte Write Sequence**


**www.onsemi.com**

**7**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**



SCL


SDA


BUS ACTIVITY:


MASTER


SLAVE





DATA DATA DATA

ADDRESS BYTE BYTE BYTE
BYTE n n+1 n+P



STOP
CONDITION


**Figure 7. Write Cycle Timing**



START ADDRESS
CONDITION



S
T
A
R



SLAVE
ADDRESS



S
T
O



A
C
K



A
C
K



A
C
K



A
C
K


**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)



n = 1
P - 15


SCL


SDA


WP



**Figure 8. Page Write Sequence**


ADDRESS DATA
BYTE BYTE

|1 8 9|Col2|Col3|Col4|
|---|---|---|---|
|a7<br>a0<br>tSU:WP|a7<br>a0<br>tSU:WP|a7<br>a0<br>tSU:WP|a7<br>a0<br>tSU:WP|
|a7<br>a0<br>tSU:WP|a7<br>a0<br>tSU:WP|||
|a7<br>a0<br>tSU:WP||||
|||||
|||||



**Figure 9. WP Timing**


**www.onsemi.com**

**8**



A
C
K


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**READ OPERATIONS**



**Immediate Read**
Upon receiving a Slave address with the R/W bit set to ‘1’,
the CAT24Cxx will interpret this as a request for data
residing at the current byte address in memory. The
CAT24Cxx will acknowledge the Slave address, will
immediately shift out the data residing at the current address,
and will then wait for the Master to respond. If the Master
does not acknowledge the data (NoACK) and then follows
up with a STOP condition (Figure 10), the CAT24Cxx
returns to Standby mode.


**Selective Read**
Selective Read operations allow the Master device to
select at random any memory location for a read operation.
The Master device first performs a ‘dummy’ write operation
by sending the START condition, slave address and byte



address of the location it wishes to read. After the
CAT24Cxx acknowledges the byte address, the Master
device resends the START condition and the slave address,
this time with the R/W bit set to one. The CAT24Cxx then
responds with its acknowledge and sends the requested data
byte. The Master device does not acknowledge the data
(NoACK) but will generate a STOP condition (Figure 11).


**Sequential Read**
If during a Read session, the Master acknowledges the 1 [st]

data byte, then the CAT24Cxx will continue transmitting
data residing at subsequent locations until the Master
responds with a NoACK, followed by a STOP (Figure 12).
In contrast to Page Write, during Sequential Read the
address count will automatically increment to and then
wrap−around at end of memory (rather than end of page).



S
T
O
P



BUS ACTIVITY:


MASTER


SLAVE



S
T
A
R
T



A
C
K



DATA
BYTE



SLAVE
ADDRESS



N
O


A
C
K



SCL





DATA OUT NO ACK STOP


**Figure 10. Immediate Read Sequence and Timing**



S
T
O
P



SLAVE ADDRESS

ADDRESS BYTE


A
C
K



BUS ACTIVITY:


MASTER


SLAVE


BUS ACTIVITY:



S
T
A
R
T



S
T
A
R
T


A
C
K



SLAVE
ADDRESS



N
O


A
C
K



DATA
BYTE



**Figure 11. Selective Read Sequence**



A
C
K


A
C



S
T
O



N
O


A
C
K



A
C



A
C



MASTER


SLAVE



SLAVE
ADDRESS



C
K



DATA
BYTE
n



DATA
BYTE
n+1



DATA
BYTE
n+2



DATA
BYTE
n+x


**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)



**Figure 12. Sequential Read Sequence**


**www.onsemi.com**

**9**


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**Ordering Information**

**CAT24C02 Ordering Information** (Notes 10, 11)













|Device Order Number|Specific<br>Device Marking|Package<br>Type|Temperature<br>Range (Note 9)|Lead<br>Finish|Shipping|
|---|---|---|---|---|---|
|CAT24C02TDI−GT3A|C1|TSOT−23−5|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|


**CAT24C04 Ordering Information**













|Device Order Number|Specific<br>Device Marking|Package<br>Type|Temperature<br>Range (Note 9)|Lead<br>Finish|Shipping|
|---|---|---|---|---|---|
|CAT24C04WI−GT3|24C04K|SOIC−8|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C04YI−GT3|C04K|TSSOP−8|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C04C4UTR|R|WLCSP−4|Industrial|N/A|(Notes 12 and 13)|
|CAT24C04C4ATR|4|WLCSP−4|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C04C5ATR|4|WLCSP−5|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C04TDI−GT3|C2|TSOT−23−5|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C04HU4I−GT3|C2U|UDFN8−EP|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|


**CAT24C08 Ordering Information**













|Device Order Number|Specific<br>Device Marking|Package<br>Type|Temperature<br>Range (Note 9)|Lead<br>Finish|Shipping|
|---|---|---|---|---|---|
|CAT24C08WI−GT3|24C08K|SOIC−8|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C08YI−GT3|C08K|TSSOP−8|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C08C4UTR|T|WLCSP−4|Industrial|N/A|(Notes 12 and 13)|
|CAT24C08C4ATR|8|WLCSP−4|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C08C4CTR**|8|WLCSP−4|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C08C5ATR|8|WLCSP−5|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C08TDI−GT3|C3|TSOT−23−5|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C08HU4I−GT3|C3U|UDFN8−EP|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|


**CAT24C16 Ordering Information**













|Device Order Number|Specific<br>Device Marking|Package<br>Type|Temperature<br>Range (Note 9)|Lead<br>Finish|Shipping|
|---|---|---|---|---|---|
|CAT24C16WI−GT3|24C16K|SOIC−8|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C16YI−GT3|C16K|TSSOP−8|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C16C4UTR|6|WLCSP−4|Industrial|N/A|(Notes 12 and 13)|
|CAT24C16C4ATR|6|WLCSP−4|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C16C5ATR|6|WLCSP−5|Industrial|N/A|Tape & Reel, 5,000 Units / Reel|
|CAT24C16TDI−GT3|C4|TSOT−23−5|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C16HU4I−GT3|C4U|UDFN8−EP|Industrial|NiPdAu|Tape & Reel, 3,000 Units / Reel|
|CAT24C16HU4E−GT3 (Note 17)|C4E|UDFN8−EP|Extended|NiPdAu|Tape & Reel, 3,000 Units / Reel|


9. Industrial temperature range is −40 ° C to +85 ° C and Extended temperature range is −40 ° C to +125 ° C.
10. **Part numbers ending with “A” for the CAT24C02 are for Gresham (Product Rev H) only die.**
11. The CAT24C02 “non−A” Device Order Numbers use Gresham die (Rev H) for date codes, starting August 1st, 2012. Therefore the Specific
Device Marking for these OPNs reflect Rev H die.
12.Contact local sales office for availability.
13.CAUTION: The EEPROM devices delivered in WLCSP must never be exposed to ultraviolet light. When exposed to ultraviolet light the
EEPROM cells lose their stored data.
14.All packages are RoHS−compliant (Lead−free, Halogen−free).
15.For information on tape and reel specifications, including part orientation and tape sizes, please refer to our Tape and Reel Packaging
Specifications Brochure, BRD8011/D.
16.For detailed information and a breakdown of device nomenclature and numbering systems, please see the **onsemi** Device Nomenclature
[document, TND310/D, available at www.onsemi.com](http://www.onsemi.com)
17.In Development
** CAT24C08C4CTR is a backside coated version. Contact factory for other densities.



**www.onsemi.com**

**10**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**SOIC 8, 150 mils**
CASE 751BD
ISSUE O












|Col1|Col2|E1 E|
|---|---|---|
||||
||||



PIN # 1
IDENTIFICATION


**TOP VIEW**






|SYMBOL|MIN|NOM|MAX|
|---|---|---|---|
|A|1.35||1.75|
|A1|0.10||0.25|
|b|0.33||0.51|
|c|0.19||0.25|
|D|4.80||5.00|
|E|5.80||6.20|
|E1|3.80||4.00|
|e|1.27 BSC|1.27 BSC|1.27 BSC|
|h|0.25||0.50|
|L|0.40||1.27|
|θ|0º||8º|








|D|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||A<br>A1|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||


|h|Col2|
|---|---|
|h<br>θ<br>L<br>|h<br>θ<br>L<br>|
|||
|||



**SIDE VIEW** **END VIEW**


**Notes:**

(1) All dimensions are in millimeters. Angles in degrees.
(2) Complies with JEDEC MS-012.


**www.onsemi.com**

**11**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**TSSOP8, 4.4x3**
CASE 948AL
ISSUE A


**www.onsemi.com**

**12**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**TSOT−23, 5 LEAD**
CASE 419AE
ISSUE O




|Col1|D|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||e<br>D|e<br>D|e<br>D|e<br>D|e<br>D|e<br>D|e<br>D||
||e<br>D||||||||
||e<br>D||||||||
||||||||||
||||||||||
||||||||||



|SYMBOL|MIN|NOM|MAX|
|---|---|---|---|
|A|||1.00|
|A1|0.01|0.05|0.10|
|A2|0.80|0.87|0.90|
|b|0.30||0.45|
|c|0.12|0.15|0.20|
|D|2.90 BSC|2.90 BSC|2.90 BSC|
|E|2.80 BSC|2.80 BSC|2.80 BSC|
|E1|1.60 BSC|1.60 BSC|1.60 BSC|
|e|0.95 TYP|0.95 TYP|0.95 TYP|
|L|0.30|<br>0.40|0.50|
|L1|0.60 REF|0.60 REF|0.60 REF|
|L2|0.25 BSC|0.25 BSC|0.25 BSC|
|θ|0º||8º|


c L2



**TOP VIEW**


















|A2<br>b A1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|A2<br>A1<br>b<br>|||||
|A2<br>A1<br>b<br>|||||
|A2<br>A1<br>b<br>|||||
|A2<br>A1<br>b<br>|||b|A1|



|<br>L1|Col2|
|---|---|
|L1<br>||
|||


**SIDE VIEW** **END VIEW**


**Notes:**

(1) All dimensions are in millimeters. Angles in degrees.
(2) Complies with JEDEC MO-193.


**www.onsemi.com**

**13**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**UDFN8, 2x3 EXTENDED PAD**
CASE 517AZ
ISSUE A







**L**



NOTES:
1. DIMENSIONING AND TOLERANCING PER
ASME Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DIMENSION b APPLIES TO PLATED
TERMINAL AND IS MEASURED BETWEEN
0.15 AND 0.25MM FROM THE TERMINAL TIP.
4. COPLANARITY APPLIES TO THE EXPOSED
PAD AS WELL AS THE TERMINALS.


|Col1|0.10|C|
|---|---|---|
||||

















**L**


**L1**

**DETAIL A**

**ALTERNATE**
**CONSTRUCTIONS**


**EXPOSED Cu** **MOLD CMPD**


|ÉÉÉ A3|Col2|Col3|É A3|
|---|---|---|---|
|ÉÉÉ<br>ÉÉÉ<br>ÇÇÇ<br>|ÉÉÉ<br>ÉÉÉ<br>ÇÇÇ<br>|ÉÉÉ<br>ÉÉÉ<br>ÇÇÇ<br>||
|ÉÉÉ<br>ÉÉÉ<br>ÇÇÇ<br>|ÉÉÉ<br>ÉÉÉ<br>ÇÇÇ<br>|É<br>Ç|É<br>Ç|
|||||



**DETAIL B**

**ALTERNATE**
**CONSTRUCTIONS**




|DIM|MILLIMETERS|Col3|
|---|---|---|
|**DIM**|**MIN**|**MAX**|
|**A**|0.45|0.55|
|**A1**|0.00|0.05|
|**A3**|0.13 REF|0.13 REF|
|**b**<br><br>|0.20<br>0.30<br> <br>|0.20<br>0.30<br> <br>|
|**D**<br>**D2**<br>|2.00 BSC<br>1.35<br>1.45<br>|2.00 BSC<br>1.35<br>1.45<br>|
|**E**<br>|3.00 BSC<br><br>|3.00 BSC<br><br>|
|**E2**|1.25|1.35|
|**e**<br>|0.50 BSC<br><br>|0.50 BSC<br><br>|
|**L**<br>**L1**|0.25<br>−−−|0.35<br>0.15|



|D A B<br>E<br>PIN ONE ÇÇ<br>FERENCE<br>ÇÇ<br>0.10 C<br>ÇÇ<br>0.10 C TOP VIEW<br>DETAIL B<br>A<br>0.10 C A3|Col2|Col3|Col4|
|---|---|---|---|
||0.10|C|C|
|||||
||0.08|C|C|


**SIDE VIEW** **C** **SEATINGPLANE**



**RECOMMENDED**

**SOLDERING FOOTPRINT***



**NOTE 4**



**SIDE VIEW**



**C**



**DETAIL A**





8X 0.68






|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|||||





DIMENSIONS: MILLIMETERS







1


0.50


|D2 L<br>1 4<br>E2<br>8 5<br>8Xb<br>e 0.10 M C A B<br>BOTTOM VIEW 0.05 M C NOTE|D2|L<br>4<br>E2<br>8Xb|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**BOTTOM VIEW**<br>**L**<br>**D2**<br>**E2**<br>**NOTE**<br>**b**<br>**8X**<br>0.10<br>C<br>0.05<br>C<br>A B<br>1<br>4<br>~~8~~<br>**e**<br>~~5~~<br>M<br>M|||||||
|**BOTTOM VIEW**<br>**L**<br>**D2**<br>**E2**<br>**NOTE**<br>**b**<br>**8X**<br>0.10<br>C<br>0.05<br>C<br>A B<br>1<br>4<br>~~8~~<br>**e**<br>~~5~~<br>M<br>M|||||||
|**BOTTOM VIEW**<br>**L**<br>**D2**<br>**E2**<br>**NOTE**<br>**b**<br>**8X**<br>0.10<br>C<br>0.05<br>C<br>A B<br>1<br>4<br>~~8~~<br>**e**<br>~~5~~<br>M<br>M|||0.10<br>M|C|A|B|
|**BOTTOM VIEW**<br>**L**<br>**D2**<br>**E2**<br>**NOTE**<br>**b**<br>**8X**<br>0.10<br>C<br>0.05<br>C<br>A B<br>1<br>4<br>~~8~~<br>**e**<br>~~5~~<br>M<br>M|||0.05<br>M|C|**NOTE**|**NOTE**|


|Col1|Col2|Col3|
|---|---|---|
||||



*For additional information on our Pb−Free strategy and soldering
details, please download the ON Semiconductor Soldering and
Mounting Techniques Reference Manual, SOLDERRM/D.



**www.onsemi.com**

**14**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**WLCSP4, 0.84x0.86**
CASE 567NX
ISSUE A



**PIN A1**
**REFERENCE**





|È<br>È|E|A B|
|---|---|---|
|È<br>È|È<br>|**D**|
|È<br>È|È|È|


**TOP VIEW**







**BACKSIDE COAT**


**SEATING**
**PLANE**

**NOTE 3**





NOTES:
1. DIMENSIONING AND TOLERANCING PER ASME
Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DATUM C, THE SEATING PLANE, IS DEFINED BY
THE SPHERICAL CROWNS OF THE CONTACT
BALLS.
4. COPLANARITY APPLIES TO SPHERICAL CROWNS
OF THE CONTACT BALLS.
5. DIMENSION b IS MEASURED AT THE MAXIMUM
CONTACT BALL DIAMETER PARALLEL TO DATUM C.


|DETAIL A<br>A<br>0.05 C|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||0.05|C|C|C|
||||||
||0.05|C|C|C|













**NOTE 4**


|DIM|MILLIMETERS|Col3|Col4|
|---|---|---|---|
|**DIM**|**MIN**|**NOM**|**MAX**|
|**A**|−−−|−−−|0.30|
|**A1**|0.08|0.10|0.12|
|**A2**<br>|0.15 REF<br> <br>|0.15 REF<br> <br>|0.15 REF<br> <br>|
|**A3**|0.025 REF|0.025 REF|0.025 REF|
|**b**<br>|0.16<br>|0.18<br>|<br>0.20|
|**D**<br><br>|0.82<br>|0.84<br>|0.86<br>|
|**E**|0.84|0.86|0.88|
|**e**|0.40 BSC<br><br><br>|0.40 BSC<br><br><br>|0.40 BSC<br><br><br>|







**C**

**SIDE VIEW**













**RECOMMENDED**

**SOLDERING FOOTPRINT***






|Col1|0.05|C|A|B|
|---|---|---|---|---|
||0.03|C|C|C|



|4X b<br>0.05 C A B<br>B<br>0.03 C NOTE 5<br>A|Col2|Col3|
|---|---|---|
|**4X**<br>**b**<br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||
|**4X**<br>**b**<br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||
|**4X**<br>**b**<br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||
|**4X**<br>**b**<br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||


**BOTTOM VIEW**



0.18



0.40






|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||



DIMENSIONS: MILLIMETERS

*For additional information on our Pb−Free strategy and soldering
details, please download the **onsemi** Soldering and Mounting
Techniques Reference Manual, SOLDERRM/D.



**www.onsemi.com**

**15**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**WLCSP4, 0.84x0.86**
CASE 567DC
ISSUE F


|È|E|A B|
|---|---|---|
|È|È|**D**|
|È|||



**BACKSIDE COAT**



**PIN A1**
**REFERENCE**



**TOP VIEW**



NOTES:
1. DIMENSIONING AND TOLERANCING PER ASME
Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DATUM C, THE SEATING PLANE, IS DEFINED BY
THE SPHERICAL CROWNS OF THE CONTACT
BALLS.
4. COPLANARITY APPLIES TO SPHERICAL CROWNS
OF THE CONTACT BALLS.
5. DIMENSION b IS MEASURED AT THE MAXIMUM
CONTACT BALL DIAMETER PARALLEL TO DATUM C.





















|DETAIL A<br>A<br>0.05 C|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||0.05|C|C|C|
||||||
||0.05|C|C|C|
||||||


**NOTE 4**


|DIM|MILLIMETERS|Col3|Col4|
|---|---|---|---|
|**DIM**|**MIN**|**NOM**|**MAX**|
|**A**|−−−|−−−|0.38|
|**A1**|0.08|0.10|0.12|
|**A2**|0.23 REF<br>|0.23 REF<br>|0.23 REF<br>|
|**A3**|<br>0.025 REF|<br>0.025 REF|<br>0.025 REF|
|**b**<br>|0.16<br>|0.18<br>|<br>0.20|
|**D**<br><br>|0.82<br>|0.84<br>|0.86<br>|
|**E**|0.84|0.86|0.88|
|**e**|0.40 BSC<br><br><br>|0.40 BSC<br><br><br>|0.40 BSC<br><br><br>|





**SIDE VIEW**



**SEATING**
**PLANE**

**NOTE 3**



**RECOMMENDED**

**SOLDERING FOOTPRINT***

A1 PACKAGE
OUTLINE














|Col1|0.05|C|A|B|
|---|---|---|---|---|
||0.03|C|C|C|



|4X b<br>0.05 C A B<br>B<br>0.03 C NOTE 5<br>A|Col2|e<br>e|
|---|---|---|
|**4X**<br>**b**<br><br><br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||
|**4X**<br>**b**<br><br><br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||
|**4X**<br>**b**<br><br><br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||
|**4X**<br>**b**<br><br><br>**B**<br>**A**<br>**NOTE 5**<br>A<br>0.05<br>B<br>C<br>0.03 C|||


**BOTTOM VIEW**



0.18



0.40






|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||



DIMENSIONS: MILLIMETERS

*For additional information on our Pb−Free strategy and soldering
details, please download the ON Semiconductor Soldering and
Mounting Techniques Reference Manual, SOLDERRM/D.



**www.onsemi.com**

**16**



**[Share Feedback](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)**
[Your Opinion Matters](https://www.onsemi.com/support/technical-document-feedback/?tdid=CAT24C01-D&tdt=Datasheet)


**CAT24C02, CAT24C04, CAT24C08, CAT24C16**


**PACKAGE DIMENSIONS**


**WLCSP5, 0.86x0.84**
CASE 567DD
ISSUE D



NOTES:
1. DIMENSIONING AND TOLERANCING PER ASME
Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DATUM C, THE SEATING PLANE, IS DEFINED BY THE
SPHERICAL CROWNS OF THE CONTACT BALLS.
4. COPLANARITY APPLIES TO SPHERICAL CROWNS
OF THE CONTACT BALLS.
5. DIMENSION b IS MEASURED AT THE MAXIMUM CONTACT BALL DIAMETER PARALLEL TO DATUM C.


|Col1|E<br>È|Col3|A B|
|---|---|---|---|
||||**D**|
|||||





**PIN A1**
**REFERENCE**



**TOP VIEW**














|0.05 C|Col2|Col3|Col4|A<br>A2|Col6|Col7|
|---|---|---|---|---|---|---|
||0.05|C|C|C|C|C|
||||||||
||0.05|C|C|C|**C**|**C**|
||||||||
|||||||**C**|


|DIM|MILLIMETERS|Col3|Col4|
|---|---|---|---|
|**DIM**<br>|**MIN**<br><br>|**NOM**<br><br>|**MAX**<br>|
|**A**|−−−|−−−|0.39|
|**A1**|0.10|0.12|0.14|
|**A2**|0.23 REF<br>|0.23 REF<br>|0.23 REF<br>|
|**b**<br>|0.14<br>|0.16<br>|<br>0.18|
|**D**<br>|0.84|0.86|0.88|
|**E**<br>|<br><br>0.82|<br><br>0.84|<br><br>0.86|
|**e**|0.30 BSC|0.30 BSC|0.30 BSC|
|**e1**|<br>0.52 BSC|<br>0.52 BSC|<br>0.52 BSC|







**5X**









**SEATING**
**PLANE**









**RECOMMENDED**

**SOLDERING FOOTPRINT***


OUTLINE








|Col1|0.05|C|A|B|
|---|---|---|---|---|
||0.03|C|C|C|


|e<br>5X b e1<br>0.05 C A B<br>C<br>0.03 C NOTE 4 B<br>A|Col2|Col3|Col4|Col5|e|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**e**<br>**5X**<br>**b**<br><br><br>**C**<br>**A**<br>**e1**<br>**NOTE 4**<br> <br>**B**<br><br>A<br>0.05<br>B<br>C<br>0.03 C|**e**<br>**5X**<br>**b**<br><br><br>**C**<br>**A**<br>**e1**<br>**NOTE 4**<br> <br>**B**<br><br>A<br>0.05<br>B<br>C<br>0.03 C||||**e**||**1**|
|**e**<br>**5X**<br>**b**<br><br><br>**C**<br>**A**<br>**e1**<br>**NOTE 4**<br> <br>**B**<br><br>A<br>0.05<br>B<br>C<br>0.03 C||||||||
|**e**<br>**5X**<br>**b**<br><br><br>**C**<br>**A**<br>**e1**<br>**NOTE 4**<br> <br>**B**<br><br>A<br>0.05<br>B<br>C<br>0.03 C||||||||
|**e**<br>**5X**<br>**b**<br><br><br>**C**<br>**A**<br>**e1**<br>**NOTE 4**<br> <br>**B**<br><br>A<br>0.05<br>B<br>C<br>0.03 C||||||||
|**e**<br>**5X**<br>**b**<br><br><br>**C**<br>**A**<br>**e1**<br>**NOTE 4**<br> <br>**B**<br><br>A<br>0.05<br>B<br>C<br>0.03 C||||||||





**REFERENCE**



**BOTTOM VIEW**



5X



0.52




|Col1|A1|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||



DIMENSIONS: MILLIMETERS

*For additional information on our Pb−Free strategy and soldering
details, please download the ON Semiconductor Soldering and
Mounting Techniques Reference Manual, SOLDERRM/D.





**PUBLICATION ORDERING INFORMATION**



**LITERATURE FULFILLMENT** :
**Email Requests to:** orderlit@onsemi.com


**onsemi Website:** www.onsemi.com


 


**TECHNICAL SUPPORT**
**North American Technical Support:**
Voice Mail: 1 800−282−9855 Toll Free USA/Canada
Phone: 011 421 33 790 2910


**www.onsemi.com**

**17**



**Europe, Middle East and Africa Technical Support:**
Phone: 00421 33 790 2910
For additional information, please contact your local Sales Representative


