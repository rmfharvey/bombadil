## LTC4372/LTC4373 Low Quiescent Current Ideal Diode Controller

### **FEATURES DESCRIPTION**



n
**Reduces Power Dissipation by Replacing a Power**
**Schottky Diode**



n
**Low Quiescent Current: 5µA Operating**



n
**Wide Operating Voltage Range: 2.5V to 80V**



n
**Reverse Supply Protection to –28V**



n
**No TVS Input Clamps Required**



n
High Side External N-Channel MOSFET Drive



n
Drives Back-to-Back MOSFETs for Inrush Control and
Load Switching



The LTC [®] [4372/LTC4373 are positive high voltage ideal](https://www.analog.com/LTC4373?doc=LTC4372-4373.pdf)
diode controllers that drive an external N-channel MOSFET
to replace a Schottky diode. They control the forward voltage drop across the MOSFET to ensure current delivery
or current transfer from one path to the other even at
light loads.

A 5µA operating current achieves high efficiency for intermittent load applications or always-on backup power supplies. If a power source fails or is shorted, a fast turnoff minimizes reverse current transients. The LTC4372/
LTC4373 control back-to-back N-channel MOSFETs for
inrush current control and load switching.

The LTC4372’s SHDN pin keeps the MOSFET off and
reduces the quiescent current to 3.5µA. The LTC4373 has
a UV pin for undervoltage monitoring while the UVOUT
pin provides hysteresis adjustment and status information. During undervoltage, the back-to-back MOSFETs are
cut off and quiescent current reduces to 0.5μA.


All registered trademarks and trademarks are the property of their respective owners.


**Power Dissipation vs Load Current**

10



n
Shutdown Input for ON/OFF Control



n
Fast Reverse Current Turn-Off within 1.5µs



n
8-Lead MSOP and 3mm × 3mm DFN Packages


### **APPLICATIONS**



n
Automotive Battery Protection



n
Redundant Power Supplies



n
Portable Instrumentation


n
Solar Powered Systems



n
Energy Harvesting Applications



n
Supply Holdup


### **TYPICAL APPLICATION**

**12V, 20A Reverse Battery Protection**



BSC026N08NS5 VOUT


20A



8


6


4


2


0







BSC026N08NS5


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|SCHOT|TKY DIODE|(SBG2040CT|)||
|||P<br>|OWER<br>||
|||~~S~~|~~AVED~~||
||MOSFET (B|SC026N08N|S5)|S5)|



0 5 10 15
CURRENT (A)



















20


43723 TA01b



[Document Feedback](https://form.analog.com/Form_Pages/feedback/documentfeedback.aspx?doc=LTC4372-4373.pdf&product=LTC4372%20LTC4373&Rev=A) [For more information www.analog.com](https://www.analog.com)


# 1 Rev. A


## LTC4372/LTC4373
### **ABSOLUTE MAXIMUM RATINGS**

**(Notes 1, 2)**

IN, SOURCE................................................–28V to 100V
OUT **.** .............................................................–2V to 100V
IN – OUT ..................................................–100V to 100V
IN – SOURCE................................................–1V to 100V
SOURCE – OUT **.** .......................................–100V to 100V
GATE – SOURCE (Note 3)........................... –0.3V to 10V
SHDN, UV, 2UPU, UVOUT......................... –0.3V to 100V
INTVCC.......................................................... –0.3V to 6V



Operating Ambient Temperature Range
LTC4372C, LTC4373C **.** ............................. 0°C to 70°C
LTC4372I, LTC4373I.............................–40°C to 85°C
LTC4372H, LTC4373H........................ –40°C to 125°C
Storage Temperature Range...................–65°C to 150°C
Lead Temperature (Soldering, 10 Sec)
MSOP Package..................................................300°C




















































|PIN CONFIGURATION|Col2|
|---|---|
|LTC4372<br>TOP VIEW<br>DD PACKAGE<br>8-LEAD (3mm × 3mm) PLASTIC DFN<br>TJMAX = 150°C,θJA = 43°C/W<br>EXPOSED PAD (PIN 9) PCB CONNECTION TO GND IS OPTIONAL<br>5<br>6<br>7<br>8<br>9<br>4<br>3<br>2<br>1<br>OUT<br>GATE<br>SOURCE<br>IN<br>SHDN<br>2UPU<br>GND<br>INTVCC|LTC4372<br>1<br>2<br>3<br>4<br>OUT<br>GATE<br>SOURCE<br>IN<br>8<br>7<br>6<br>5<br>SHDN<br>2UPU<br>GND<br>INTVCC<br>TOP VIEW<br>MS8 PACKAGE<br>8-LEAD PLASTIC MSOP<br>TJMAX = 150°C,θJA = 163°C/W|
|LTC4373<br>TOP VIEW<br>DD PACKAGE<br>8-LEAD (3mm × 3mm) PLASTIC DFN<br>TJMAX = 150°C,θJA = 43°C/W<br>EXPOSED PAD (PIN 9) PCB CONNECTION TO GND IS OPTIONAL<br>5<br>6<br>7<br>8<br>9<br>4<br>3<br>2<br>1<br>OUT<br>GATE<br>SOURCE<br>IN<br>UV<br>UVOUT<br>GND<br>INTVCC|LTC4373<br>1<br>2<br>3<br>4<br>OUT<br>GATE<br>SOURCE<br>IN<br>8<br>7<br>6<br>5<br>UV<br>UVOUT<br>GND<br>INTVCC<br>TOP VIEW<br>MS8 PACKAGE<br>8-LEAD PLASTIC MSOP<br>TJMAX = 150°C,θJA = 163°C/W|


# ~~2~~



[For more information www.analog.com](https://www.analog.com)



Rev. A


## LTC4372/LTC4373
### **ORDER INFORMATION**

|TUBE|TAPE AND REEL|PART MARKING*|PACKAGE DESCRIPTION|TEMPERATURE RANGE|
|---|---|---|---|---|
|LTC4372CDD#PBF|LTC4372CDD#TRPBF|LHGR|8-Lead (3mm × 3mm) Plastic DFN|0°C to 70°C|
|LTC4372IDD#PBF|LTC4372IDD#TRPBF|LHGR|8-Lead (3mm × 3mm) Plastic DFN|–40°C to 85°C|
|LTC4372HDD#PBF|LTC4372HDD#TRPBF|LHGR|8-Lead (3mm × 3mm) Plastic DFN|–40°C to 125°C|
|LTC4372CMS8#PBF|LTC4372CMS8#TRPBF|LTHGS|8-Lead Plastic MSOP|0°C to 70°C|
|LTC4372IMS8#PBF|LTC4372IMS8#TRPBF|LTHGS|8-Lead Plastic MSOP|–40°C to 85°C|
|LTC4372HMS8#PBF|LTC4372HMS8#TRPBF|LTHGS|8-Lead Plastic MSOP|–40°C to 125°C|
|LTC4373CDD#PBF|LTC4373CDD#TRPBF|LHMQ|8-Lead (3mm × 3mm) Plastic DFN|0°C to 70°C|
|LTC4373IDD#PBF|LTC4373IDD#TRPBF|LHMQ|8-Lead (3mm × 3mm) Plastic DFN|–40°C to 85°C|
|LTC4373HDD#PBF|LTC4373HDD#TRPBF|LHMQ|8-Lead (3mm × 3mm) Plastic DFN|–40°C to 125°C|
|LTC4373CMS8#PBF|LTC4373CMS8#TRPBF|LTHMR|8-Lead Plastic MSOP|0°C to 70°C|
|LTC4373IMS8#PBF|LTC4373IMS8#TRPBF|LTHMR|8-Lead Plastic MSOP|–40°C to 85°C|
|LTC4373HMS8#PBF|LTC4373HMS8#TRPBF|LTHMR|8-Lead Plastic MSOP|–40°C to 125°C|



Contact the factory for parts specified with wider operating temperature ranges.
[Tape and reel specifications. Some packages are available in 500 unit reels through designated sales channels with #TRMPBF suffix.](https://www.analog.com/media/en/package-pcb-resources/package/tape-reel-rev-n.pdf)

### ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the full operating

**temperature range, otherwise specifications are at TA = 25°C. IN = SOURCE =12V, SHDN = 0V, UV = 2V unless otherwise noted.**




























|SYMBOL|PARAMETER|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
|VIN|Input Supply Voltage Range||l|2.5<br>80|V|
|VIN(UVL)|Input Supply Undervoltage Lockout|IN Rising|l|1.9<br>2.1<br>2.45|V|
|∆VIN(HYST)|Input Supply Undervoltage Lockout Hysteresis|||80|mV|
|VINTVCC|Internal Regulator Voltage|IINTVCC = 0 to –10µA|l|2.5<br>3.5<br>4.5|V|
|IQ|Total Supply Current<br> <br>IQ = IIN + ISOURCE + IOUT|Diode Control: IGATE = –0.1µA<br> <br> <br>Single or Back-to-Back MOSFETs (Note 4)<br> <br> <br> <br>(C-Grade, I-Grade)<br> <br> <br> <br>(H-Grade)<br>Shutdown: SHDN = 2V, UV = 0V<br> <br> <br>Single MOSFET<br> <br> <br>Back-to-Back MOSFETs<br>Reverse Current: ∆VSD = –0.1V, IN = 12V<br> <br> <br>Single MOSFET<br> <br> <br>Back-to-Back MOSFETs|<br> <br>l <br>l<br> <br>l <br>l<br> <br>l <br>l|<br> <br>5 <br>5<br> <br> <br>10<br>20<br> <br> <br>3.5<br>0.5<br> <br>10<br>2.5<br> <br>20<br>10<br> <br>30<br>20|<br> <br>µA<br>µA<br> <br>µA<br>µA<br> <br>µA<br>µA|
|IOUT|OUT Current|IN – OUT = 4V<br>IN – OUT = –4V|l <br>l|–0.5<br>1.8<br>–10<br>5|µA<br>µA|
|INEG|IN + SOURCE Current During<br>Reverse Battery|IN = SOURCE = –24V, OUT = 24V|l|–1<br>–5|mA|
|IOUT(NEG)|OUT Current During Reverse Battery|IN = SOURCE = –24V, OUT = 24V|l|0.3<br>0.5|mA|
|∆VSD(T)|Source-Drain Threshold (IN-OUT)|Low to High. Activates IGATE(UP)|l|20<br>30<br>45|mV|
|∆VGATE(H)|Maximum GATE Drive (GATE-SOURCE)|IN ≤ 5V, ∆VSD = 0.1V, IGATE = 0, –1µA<br>IN > 5V, ∆VSD= 0.1V, IGATE = 0, –1µA|l <br>l|4.5<br>10<br>6.5<br>11.7<br>10<br>16|V <br>V|
|IGATE(UP)|GATE Pull-Up Current|GATE = IN, ∆VSD= 0.1V|l|–15<br>–20<br>–25|µA|



[For more information www.analog.com](https://www.analog.com)


# 3 Rev. A


## LTC4372/LTC4373
### ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the full operating

**temperature range, otherwise specifications are at TA = 25°C. IN = SOURCE =12V, SHDN = 0V, UV = 2V unless otherwise noted.**




















|SYMBOL|PARAMETER|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
|IGATE(DOWN)|GATE Pull-Down Current|Shutdown: SHDN = 2V, UV = 0V, ∆VGATE = 5V<br>Reverse Current: ∆VSD= –0.1V, ∆VGATE = 5V<br>Reverse Battery: IN = SOURCE = –7V, GATE = –3V|l<br>l<br>l|0.5<br>70<br>70<br>1<br>130<br>130<br>3<br>230<br>230|mA<br>mA<br>mA|
|VGATE(NEG)|GND-GATE clamp|IGATE = 10mA (Note 3)|l|–28<br>–32<br>–35|V|
|VSOURCE(TH)|Reverse SOURCE Threshold for GATE Off|GATE = 0V (Note 5)|l|–0.9<br>–1.8<br>–2.7|V|
|<br>tOFF|<br>Gate Turn-Off Delay Time|ΔVSD= Step 0.1V to –0.8V, CGATE= 0pF, ΔVGATE<1V|l|0.5<br>1.5|µs|
|tON|Gate Turn-On Delay Time|IN = 12V, SOURCE = OUT = 0V, ΔVGATE > 4.5V,<br>CGATE = 0pF, SHDN = 2V to 0V, UV = 0V to 1.25V|l|100<br>500<br>1200|µs|




|LTC4372|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|I2UPU|2UPU Pull-Up Current||l|–1<br>–2<br>–3|µA|
|VSHDN|SHDN Threshold|SHDN Falling|l|1<br>1.2<br>1.4|V|
|VSHDN(HYST)|SHDN Threshold Hysteresis||l|2<br>15<br>40|mV|
|<br>ISHDN|<br>SHDN Leakage Current|SHDN = 1.2V|l|±1<br>±50|nA|














|LTC4373|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|VUV|UV Threshold|UV Falling|l|1.174<br>1.191<br>1.208|V|
|VUV(HYST)|UV Threshold Hysteresis||l|2<br>15<br>40|mV|
|IUV(LK)|UV Leakage Current|UV = 1.2V|l|±1<br>±50|nA|
|IUVOUT(LK)|UVOUT Leakage Current|UV = 2V,UVOUT= 1.2V<br> <br>(C-Grade, I-Grade)<br> <br>(H-Grade)|<br>l <br>l|<br>±1<br>±1<br> <br>±50<br>±200|<br>nA<br>nA|
|RUVOUT#|UVOUT Output Low Resistance|I = 2mA|l|140<br>500|Ω|
|tUV|Under Voltage Detect toUVOUT Assert Low|UV = Step 1.25V to 1.1V|l|10<br>50<br>300|µs|



**Note 1:** Stresses beyond those listed under Absolute Maximum Ratings
may cause permanent damage to the device. Exposure to any Absolute
Maximum Rating condition for extended periods may affect device
reliability and lifetime.
**Note 2:** All currents into device pins are positive; all currents out of
device pins are negative. All voltages are referenced to GND unless
otherwise specified.
**Note 3:** An internal clamp limits the GATE pin to a minimum of 10V above
SOURCE or 100V above GND. A second internal clamp limits the GATE pin
to a minimum of 28V below GND. Driving this pin to voltages beyond the
clamp may damage the device.



**Note 4:** When testing the single MOSFET configuration, IN is connected to
SOURCE. When testing the back-to-back MOSFET configuration, SOURCE
is left unconnected.
**Note 5:** SOURCE ≤ –1.8V triggers a 130mA pull-down current from GATE
to SOURCE. An internal clamp limits the GATE pin to a minimum of 28V
below GND. Driving SOURCE to voltages beyond the clamp may damage
the device.


Rev. A


# ~~4~~



[For more information www.analog.com](https://www.analog.com)


## LTC4372/LTC4373
### **TYPICAL PERFORMANCE CHARACTERISTICS TA = 25°C. IN = SOURCE = 12V, SHDN = 0V,**

**UV = 2V unless otherwise noted.**



6.0


5.5


5.0


4.5



**Total Supply Current** **Total Supply Current vs**
**Total Supply Current vs VIN** **vs Load Current** **Temperature**





40





8



7


6


5


4


3





4.0

|NFET =<br>CLOAD =<br>IGATE =|IPB107N<br>10µF, IL<br>–0.1µA|20N<br>OAD|3G<br>= 50mA|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||

0 10 20 30 40 50 60 70 80
VIN (V)

43723 G01



2

|NFET<br>CLOA<br>I|= IPB1<br>D = 10µ<br>= –0.1|07N20<br>F<br>µA|N3G|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|~~GATE~~|||||||
||||||||
||||||||
||||||||
||||||||

1µ 10µ 100µ 1m 10m 100m 1 10
ILOAD (A)

43723 G02



30


20


10


0

|NFET<br>CLOA<br>IGATE|= IPB<br>D = 10<br>= –0.|107N<br>µF, IL<br>1µA|20N3<br>OAD =1|G<br>00mA|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||

–50 –25 0 25 50 75 100 125 150
TEMPERATURE (°C)

43723 G03



**Total Supply Current** **Total Supply Current (Shutdown)** **Total Supply Current (Shutdown)**
**vs GATE Leakage** **vs VIN** **vs Temperature**





1k


100


10


1
0.01 0.1 1 10 100
–IGATE (µA)

43723 G4



0.60





0.55


0.50


0.45


0.40

|SHDN<br>BACK|= 2V,<br>-TO-B|UV =<br>ACK|0V<br>MOSFE|Ts|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||

0 10 20 30 40 50 60 70 80
VIN (V)

43723 G05



8


7


6


5


4


3


2


1



0

|SHD<br>BACK|N = 2V,<br>-TO-B|UV =<br>ACK|0V<br>MOSF|ETs|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

–50 –25 0 25 50 75 100 125 150
TEMPERATURE (°C)

43723 G06



**IN Current** **SOURCE Current** **OUT Current**



60


50


40


30


20


10



3.0


2.5


2.0


1.5


1.0


0.5


0


–0.5







12


10


8


6


4


2





0

|IN = SO|URCE|Col3|Col4|Col5|OUT = 1<br>OUT = 7|2V<br>5V|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||

0 10 20 30 40 50 60 70 80
VIN (V)

43723 G07



0

|IN = S|OUR|CE|Col4|Col5|O<br>O|UT = 1<br>UT = 7|2V<br>5V|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

0 10 20 30 40 50 60 70 80
VSOURCE (V)

43723 G08


[For more information www.analog.com](https://www.analog.com)



–1.0

|Col1|Col2|Col3|Col4|IN =|SOUR|CE = 1|2V|
|---|---|---|---|---|---|---|---|
|||||||||
|||||~~IN =~~|~~ OUR~~|~~ E =~~|~~  5V~~|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

0 10 20 30 40 50 60 70 80
VOUT (V)

43723 G09


# 5 Rev. A


## LTC4372/LTC4373
### **TYPICAL PERFORMANCE CHARACTERISTICS TA = 25°C. IN = SOURCE = 12V, SHDN = 0V,**

**UV = 2V unless otherwise noted.**


**Pin Current at Shutdown** **Pin Current at Negative Input** **OUT Current at Negative Input**



10


1


0.1


0.01



300


250


200


150


100


50







–1000


–800


–600


–400


–200





0.001

|Col1|Col2|Col3|Col4|Col5|ISOUR|CE|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
||||||~~IIN~~|||
|||||||||
|||||||||
|||||||||
||||||~~IOU~~|||
|||||||||
|||||||||
|||||||||
|||||||||
|||||~~SHD~~|~~N = 2V/~~|~~ UV =~~|~~  0V~~|

0 10 20 30 40 50 60 70 80
VOLTAGE (V)

43723 G10



0

|IN = S|OURCE,|OUT = 5|0V|Col5|Col6|
|---|---|---|---|---|---|
||||II|N||
|||||||
||||ISOUR|CE||
|||||||

0 –5 –10 –15 –20 –25 –30
VIN (V)

43723 G11



0

|IN = S<br>OUT =|OURCE<br>50V|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||

0 –5 –10 –15 –20 –25 –30
VIN (V)

43723 G12



**GATE Current** **∆VGATE (Average)** **GATE Turn-Off Time**
**vs Forward Voltage Drop** **vs GATE Leakage** **vs GATE Capacitance**



–25


–20


–15


–10


–5


0









1000


750


500


250



5

|IN =<br>GATE|SOUR<br>= SO|CE =<br>URC|12<br>E +|V<br>3V|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|~~∆V~~|~~ HIGH~~|~~ TO~~|~~  LO~~|||||||
|~~SD~~||||||||||
|||||||||||
|||||∆|∆|VSD L|OW T|O HI|GH|
|||||||||||

–5 0 5 10 15 20 25 30 35 40
∆VSD (mV)

43723 G13



16


14


12


10


8


6


4


2



0

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|~~IN = S~~|~~ OURCE =~~|~~  5V~~|||
||||||
||||||
|IN = S|OURCE =|2.5V|||
||||||
||||||
||||||

0 –5 –10 –15 –20 –25
IGATE (µA)

43723 G14



0

|IN = SOU<br>∆VSD = 5|RCE = 12<br>0mV STE|V<br>P TO –0.8|V|Col5|
|---|---|---|---|---|
||||||
||||||
||||||

0 2 4 6 8 10
CGATE (nF)

43723 G15



3


2


1



**GATE Turn-Off Time** **UV Threshold**
**vs Forward Overdrive** **vs Temperature** **Load Current vs VFWD**



1.21


1.20


1.19



10





1.22







8


6


4


2



0

|Col1|∆VSD = 5|0mV STE|P TO FIN|AL ∆VSD|
|---|---|---|---|---|
||||||
||||||

0 –0.2 –0.4 –0.6 –0.8 –1
FINAL ∆VSD (V)

43723 G16



1.18

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|~~V~~U|V~~ LOW~~|~~ TO H~~|~~  IGH~~|||||
|VUV|HIGH|TO L|OW|||||
|||||||||

–50 –25 0 25 50 75 100 125 150
TEMPERATURE (°C)

43723 G17


[For more information www.analog.com](https://www.analog.com)



0

|Col1|FDMS861|01 S|i4190ADY|
|---|---|---|---|
|||||
|||IPB107N2|0N3G|
|||||
|||||

0 25 50 75 100
∆VSD (mV)

43723 G18


Rev. A


# ~~6~~


### **PIN FUNCTIONS**

**Exposed Pad (DD Package Only) :** Exposed pad may be
left open or connected to device ground.

**GATE:** MOSFET Gate Drive Output. The LTC4372/LTC4373
control the gate of the MOSFET to maintain the voltage
drop between 0mV to 30mV using a pulsed control
method. If reverse current flows, a fast pull-down circuit connects GATE to SOURCE within 0.5μs, turning off
the MOSFET.

**GND:** Device Ground.

**IN:** Voltage Sense and Supply Voltage. IN is the anode of
the ideal diode. The voltage sensed at this pin is used to
control the MOSFET gate for forward voltage regulation
and reverse current turn-off. The positive supply input
ranges from 2.5V to 80V for normal operation. It can go
below GND by up to 28V during a reverse battery condition without damaging the part.

**INTVCC:** Internal 3V Supply Decoupling Output. Connect
a 0.1μF or larger capacitor to this pin. An external load of
less than 10µA can be connected at this pin.

**OUT:** MOSFET Drain Voltage Sense. OUT is the cathode
of the ideal diode and the common output when multiple
LTC4372/LTC4373’s are configured as an ideal diode-OR.
It connects to the drain of the N-channel MOSFET. The
voltage sensed at this pin is used to control the MOSFET


## LTC4372/LTC4373

gate for forward voltage regulation and reverse current
turn-off. OUT is used as the supply to hold the MOSFET
off when IN is not available (below UVLO). Connect a 10µF
or larger capacitor to this pin.

**SHDN (LTC4372):** Shutdown Control Input. The LTC4372
can be shut down to a low current mode by pulling SHDN
above 1.215V. Connect to GND if unused.

**SOURCE:** MOSFET Source Connection. SOURCE is the
return path of the GATE fast pull-down. Connect this
pin as close as possible to the source of the external
N-channel MOSFET.

**2UPU (LTC4372):** 2μA Pull-Up Output. This pin has a
2μA pull-up to INTVCC. It can be connected to SHDN to
facilitate on/off control of the LTC4372 by a microcontroller’s open-drain output. If unused, leave open or connect
to INTVCC.

**UVOUT (LTC4373):** UV Status Output. Open Drain output
that pulls low when UV goes below 1.191V (VUV) and goes
high impedance when UV exceeds 1.191V. UVOUT can be
used to adjust hysteresis for the UV monitor. This pin may
be left open or connected to GND if unused.

**UV (LTC4373):** Undervoltage Detection Input. The
LTC4373 goes into a low current shutdown mode when
UV is below 1.191V. Connect to INTVCC if unused.



[For more information www.analog.com](https://www.analog.com)


# 7 Rev. A


## LTC4372/LTC4373






















|Col1|I|
|---|---|
|||
|||
|||
|||
|||


|AGRAM|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|SHDN<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>2UPU<br>2μA<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4372**<br>1.2V<br>30mV<br>30mV<br>IN<br>+<br>–<br>+–<br>+–<br>–<br>+<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>SHDN<br>COMP|SHDN<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>2UPU<br>2μA<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4372**<br>1.2V<br>30mV<br>30mV<br>IN<br>+<br>–<br>+–<br>+–<br>–<br>+<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>SHDN<br>COMP|||||||||||||
|SHDN<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>2UPU<br>2μA<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4372**<br>1.2V<br>30mV<br>30mV<br>IN<br>+<br>–<br>+–<br>+–<br>–<br>+<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>SHDN<br>COMP|SHDN<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>2UPU<br>2μA<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4372**<br>1.2V<br>30mV<br>30mV<br>IN<br>+<br>–<br>+–<br>+–<br>–<br>+<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>SHDN<br>COMP|||||||||||||
|SHDN<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>2UPU<br>2μA<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4372**<br>1.2V<br>30mV<br>30mV<br>IN<br>+<br>–<br>+–<br>+–<br>–<br>+<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>SHDN<br>COMP|SHDN<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>2UPU<br>2μA<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4372**<br>1.2V<br>30mV<br>30mV<br>IN<br>+<br>–<br>+–<br>+–<br>–<br>+<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>SHDN<br>COMP|||||||||||||








































|Col1|I|
|---|---|
|||
|||
|||
|||
|||








|IN SOURCE GATE OUT<br>LTC4373 11.7V<br>32V<br>–<br>CHARGE<br>NEGATIVE PUMP<br>COMP f = 2MHz<br>–1.8V +<br>IN<br>HYST-<br>REVERSE ERETIC<br>CURRENT GATE DRIVER<br>– + + –<br>+ +<br>– 30mV – 30mV<br>INTVCC<br>INTVCC<br>REGULATOR<br>UV 1.191V + U COV MP<br>–<br>UVOUT<br>+ 1.191V<br>C1<br>–<br>GND|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1.191V<br>1.191V<br>+<br>–<br>–<br>+<br> <br>UV<br>COMP<br>UVOUT<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>UV<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4373**<br>30mV<br>30mV<br>IN<br>+–<br>+–<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>+<br>–<br>C1|1.191V<br>1.191V<br>+<br>–<br>–<br>+<br>UV<br>COMP<br>UVOUT<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>UV<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4373**<br>30mV<br>30mV<br>IN<br>+–<br>+–<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>+<br>–<br>C1|||||||||||||
|1.191V<br>1.191V<br>+<br>–<br>–<br>+<br> <br>UV<br>COMP<br>UVOUT<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>UV<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4373**<br>30mV<br>30mV<br>IN<br>+–<br>+–<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>+<br>–<br>C1|1.191V<br>1.191V<br>+<br>–<br>–<br>+<br>UV<br>COMP<br>UVOUT<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>UV<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4373**<br>30mV<br>30mV<br>IN<br>+–<br>+–<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>+<br>–<br>C1|||||||||||||
|1.191V<br>1.191V<br>+<br>–<br>–<br>+<br> <br>UV<br>COMP<br>UVOUT<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>UV<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4373**<br>30mV<br>30mV<br>IN<br>+–<br>+–<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>+<br>–<br>C1|1.191V<br>1.191V<br>+<br>–<br>–<br>+<br>UV<br>COMP<br>UVOUT<br>GND<br>OUT<br>GATE<br>SOURCE<br>IN<br>CHARGE<br>PUMP<br>f = 2MHz<br>INTVCC<br>UV<br>32V<br>–1.8V<br>11.7V<br>INTVCC<br>REGULATOR<br>**LTC4373**<br>30mV<br>30mV<br>IN<br>+–<br>+–<br>–<br>+<br>–<br>+<br>REVERSE<br>HYST-<br>ERETIC<br>GATE DRIVER<br>CURRENT<br>NEGATIVE<br>COMP<br>+<br>–<br>C1|||||||||||||


# ~~8~~



Rev. A



[For more information www.analog.com](https://www.analog.com)


### **OPERATION**

Blocking diodes are commonly placed in series with supply inputs for ORing redundant supplies and protecting
against supply reversal. The LTC4372/LTC4373 replace
the diodes such as in portable equipment and automotive applications with N-channel MOSFETs acting as ideal
diodes. The forward voltage drop reduces as shown in
Figure 1, a feature that is readily appreciated at low input
voltages where headroom is tight.


20



15


10


5


0

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||MOSFET<br>||||
|~~(BSC~~|~~026N08N~~|~~S5)~~|||
||SC<br>|HOTTKY<br>~~SBG204~~|DIODE<br>~~CT)~~||
||||||

0.0



0.1 0.2 0.3 0.4 0.5



VOLTAGE (V)



43723 F01



**Figure 1. Forward Voltage Drop Comparison Between MOSFET**
**and Schottky Diode**


As a result of this lower forward voltage drop, there is a
dramatic reduction in power loss achieved in a practical
application as shown in the Typical Application curve on
Page 1. This represents significant savings in board area
by greatly reducing heat sinking requirements of the pass
device. In addition to these two desirable properties, the
LTC4372/LTC4373 feature a low operating current (5µA)
and shutdown current (0.5µA). This increases efficiency
in applications where the ideal diode is used for intermittent loads or always on standby channels, making the
LTC4372/LTC4373 suitable for battery powered applications in the portable instrumentation, automotive and
renewable energy fields.


## LTC4372/LTC4373

The source of the external MOSFET is connected to IN
and SOURCE while its drain is connected to OUT. The
LTC4372/LTC4373 control the gate of the MOSFET to
regulate the voltage drop across the pass transistor to
less than 30mV.

In the event of a rapid drop in input voltage, such as an
input short-circuit fault or negative-going voltage spike,
reverse current temporarily flows through the MOSFET.
This current is provided by any load capacitance and
by other supplies or batteries that feed the output in
diode-OR applications. The reverse current comparator
quickly responds to this condition by turning the MOSFET
off in 500ns. This fast turn-off prevents the reverse current from ramping up to a damaging level, thus minimizing the disturbance to the output bus.

IN, SOURCE and GATE are protected against reverse
inputs of up to –28V. The negative comparator detects
negative input potentials at SOURCE and quickly connects
GATE to SOURCE, turning off the MOSFET and isolating
the load from the negative input.

For the LTC4372, driving SHDN high pulls the MOSFET
gate down to SOURCE with a 1mA pull-down. IQ reduces
to 0.5μA for a back-to-back MOSFET configuration and
GATE is held low with a 3μA pull-down to GND. When
SHDN goes low, the LTC4372 ramps GATE up to turn on
the external MOSFET. 2UPU has a 2μA pull-up to INTVCC
which can be connected to SHDN to facilitate on/off control by a microcontroller’s open-drain output.

The LTC4373 can monitor the input voltage via an external resistive voltage divider to UV. When UV goes below
1.191V, GATE pulls down to SOURCE with a 1mA pulldown and UVOUT pulls low. IQ reduces to 0.5μA for a
back-to-back MOSFET configuration and GATE is held low
with a 3μA pull down to GND. When UV recovers above
VUV + VUV(HYST), the LTC4373 ramps GATE up to turn on
the external MOSFET. An optional resistor can be connected between UV and UVOUT to configure an external
hysteresis to override VUV(HYST).



[For more information www.analog.com](https://www.analog.com)


# 9 Rev. A


## LTC4372/LTC4373
### **APPLICATIONS INFORMATION**

The LTC4372/LTC4373 operate from 2.5V to 80V and
withstands an absolute maximum range of –28V to 100V
without damage. In automotive applications the LTC4372/
LTC4373 can operate through load dump, cold crank and
two-battery jump starts, and survive reverse battery connections while protecting the load.

A 12V/20A ideal diode application is shown in Figure 2.
The following sections cover power-on, ideal diode operation, shutdown and various faults that the LTC4372/
LTC4373 detect and act upon.





Figure 5 shows a typical OUT ripple at an ILOAD of 16A for
the circuit shown in Figure 2.








|Col1|Col2|Col3|Col4|IN|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||~~O~~|~~T~~|||||||
|||||||||||
|||||||||||
||||~~G~~|~~TE~~||||||
|||||IN||||||



VOUT
12V
20A



VIN



IGATE(LEAKAGE) = 100nA

**Figure 3. Regulating ΔVSD at Low ILOAD = 1µA**







M1





















12V

IN, OUT
20mV/DIV



|Col1|Col2|Col3|Col4|IN|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||O|UT|||||||
|||||||||||
|||||||||||
||||GA|TE||||||
|||||||||||
|||||IN||||||


5ms/DIV



**Figure 2. 12V/20A Ideal Diode with Reverse Input Protection**


**Power-On and Ideal Diode Operation**

When power is applied, the initial load current flows
through the body diode of the MOSFET M1. When IN
exceeds the UVLO level of 2.1V and SHDN is low or UV is
high, the LTC4372/LTC4373 begin operation. An internal
charge pump asserts a 20µA pull-up on GATE to enhance
the MOSFET. To achieve a low supply current, the LTC4372/
LTC4373 employ a pulsed control style of operation where
the internal charge pump is not always on. Instead, the
charge pump periodically wakes up to recharge GATE after
it droops from leakage to keep ∆VSD ≤ 30mV. This pulsed
control creates a voltage ripple at OUT even with a stable
DC load. The amplitude of this ripple is dependent on gate
leakage, GATE capacitance, the load condition and the size
of the bypass capacitance at OUT. At low load or no-load
condition, this ripple can increase to 30mVPK–PK. Figure 3
shows a typical OUT ripple at an ultralight ILOAD of 1µA
for the circuit shown in Figure 2.

With a moderate DC load, the ripple amplitude is about
10mVpk-pk. Figure 4 shows a typical OUT ripple at a moderate ILOAD of 2A for the circuit shown in Figure 2.



IN, GATE
5V/DIV

12V



43723 F04



IGATE(LEAKAGE) = 100nA

**Figure 4. Regulating ΔVSD at Moderate ILOAD = 2A**



12V

IN, OUT
20mV/DIV





|Col1|Col2|Col3|Col4|IN|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||OU|T|||||||
|||||||||||
|||||||||||
||||~~G~~|~~TE~~||||||
|||||||||||
|||||IN||||||


10ms/DIV



IN, GATE
5V/DIV

12V



43723 F05



IGATE(LEAKAGE) = 100nA

**Figure 5. Regulating ΔVGATE at High ILOAD = 16A**


# ~~10~~



Rev. A



[For more information www.analog.com](https://www.analog.com)


### **APPLICATIONS INFORMATION**

As the load current increases, GATE is driven higher and
higher until a point is reached where ∆VGATE reaches
the maximum overdrive that the internal charge pump is
capable of (∆VGATE(H)) but ∆VSD is still above 30mV. In
this situation, the internal charge pump will periodically
turn on to recharge GATE as needed to keep ∆VGATE
between ∆VGATE(H) and ∆VGATE(H) – 0.7V. ∆VSD is then
equal to RDS(ON) • ILOAD. There is now insignificant
ripple on OUT as the 0.7Vpk-pk ripple on ∆VGATE has
little effect on the MOSFET RON.


**Achieving Low Average IQ**

To lower average IQ in diode control mode when GATE
is high, the LTC4372/LTC4373 operate by turning on
the charge pump periodically. When in charge pump
sleep mode, the IQ is 3.5μA. Once the charge pump is
turned on to deliver a current pulse to GATE, IQ goes up
to 300μA. The average IQ will depend on how often the
charge pump is turned on and this is affected by GATE
leakage, GATE capacitance, OUT bypass capacitance and
ILOAD. To achieve the lowest possible average IQ, minimize GATE leakage and ensure that GATE has a moderate
capacitance (>1nF). If the CGS of the MOSFET does not
already exceed this, add a 1nF capacitor between GATE
and SOURCE. CLOAD may be placed nearer to the load but
an OUT bypass capacitance of at least 10μF low ESR and
ESL electrolytic or ceramic is required close to the drain
pin of MOSFET M1 (see Figure 6a). Average IQ for Diode
Control mode can be estimated by Equation 1.


## LTC4372/LTC4373

Gate drive is compatible with 4.5V logic-level MOSFETs
over the entire operating range of 2.5V to 80V. In applications with supply voltages above 5V, standard 10V threshold MOSFETs may be used. An internal clamp limits the
gate drive to 16V maximum between GATE and SOURCE.

The maximum allowable drain-source voltage, BVDSS,
must be higher than the power supply voltage. If the input
is grounded, the full supply voltage will appear across the
MOSFET. If a reverse battery is possible and the output
is held up by a charged capacitor, battery or power supply, then the sum of the input and output voltages will
appear across the MOSFET and BVDSS must be higher
than VOUT+|VIN|.

The MOSFET’s on-resistance, RDS(ON), directly affects
the forward voltage drop and power dissipation during a
heavy load. Desired forward voltage drop (VFWD) should
be less than that of a diode for reduced power dissipation; 50mV is a good starting point. Since the LTC4372/
LTC4373 drop at least 30mV across the MOSFET, a very
low RDS(ON) may be wasted. Choose a MOSFET using
Equation 2.



RDS(ON) < [V][FWD]
ILOAD



(2)



AVERAGEIQ = 3.5 +



IGATE(LEAKAGE)
IGATE(UP)




- 300µA



(1)



The resulting power dissipation is shown in Equation 3.

Pd = ILOAD [2 ] - RDS(ON) (3)


**Input Short-Circuit Faults**

Input short-circuits that cause reverse current to flow can
occur in many ways. Some examples include PCB traces
getting accidentally shorted or bypass capacitors in the
upstream power supply failing shorted. The LTC4372/
LTC4373 utilize the external MOSFETs to add rugged input
short-circuit protection without using large TVS clamps
or capacitors.

Figure 6a models a low impedance input short with a
switch. When the short-circuit switch closes, reverse current builds up in LIN, LOUT and M1 in the direction shown.
The LTC4372/LTC4373 detect the reverse current quickly
and activate the internal 130mA GATE to SOURCE pulldown current to turn M1 off. The reverse current build up



The Typical Performance Characteristics section shows
relationship of IQ with IGATE(LEAKAGE) and ILOAD.


**MOSFET Selection**

The LTC4372/LTC4373 drive N-channel MOSFETs to
conduct the load current. The important characteristics of the MOSFET are the gate threshold voltage
VGS(TH), the maximum drain-source voltage BVDSS and
on-resistance RDS(ON).



[For more information www.analog.com](https://www.analog.com)


# 11 Rev. A


## LTC4372/LTC4373
### **APPLICATIONS INFORMATION**

REVERSE CURRENT



LS
SOURCE
PARASITIC
INDUCTANCE



LS LIN
SOURCE INPUT
PARASITIC PARASITIC
INDUCTANCE INDUCTANCE





|Col1|G|ATE|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||IN||||||||
|||GND||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||


COUT = 10μF



LOUT
OUTPUT
PARASITIC
INDUCTANCE



M1





















500ns/DIV



43723 F06b







**(a)** **(b)**

**Figure 6. Reverse Recovery Produces Inductive Spikes at IN, SOURCE and OUT. The Polarity of**
**Inductive Spike is Shown Across Parasitic Inductances**



in LIN and LOUT is interrupted and this causes IN to spike
negative and OUT to spike positive. At OUT, COUT clamps
the positive going spike caused by LOUT and commutates
I(LOUT) to zero. At IN, the internal GND – GATE clamp
asserts and holds GATE to 32V below GND, this causes M1
to turn back on as IN/SOURCE undershoots below GATE.
The current in LIN is diverted by M1 to COUT and safely
commutates to zero as shown in the short-circuit transient
of Figure 6b. If these transients cause too large of a ∆V at
OUT, increase the capacitance of COUT or add a TVS D1.

If a low source resistance power supply drives VIN, large
currents can build up in LS during the short-circuit.
When the short-circuit goes away, I(LS) can cause IN and
SOURCE to spike positive until it is held by M1 body diode
to COUT. This fast slew rate at SOURCE can cause a large
shoot-through current to flow into the part from SOURCE
to GND potentially causing damage. Adding an external
RGND will limit this current to a safe level.

For applications where IN **≤** 13.2V, a 0805 size 100Ω for
RGND is sufficient. For applications where IN > 13.2V, a
larger value RGND, 1k, is necessary. To keep GND from
going too negative when the GND – GATE clamp turns
on, a fast recovery diode like the 1N4148W is placed in
parallel with the 1k RGND.

For back-to-back MOSFET applications where SOURCE
is not driven by VIN, RGND is not needed. RGND can also
be omitted for a single MOSFET application driven by a



power supply with a large source impedance. VIN collapses during the short-circuit and cannot build up current in LS. SOURCE will not see fast slew rates when the
short-circuit goes away.

Using the external MOSFETs to commutate the parasitic
inductor currents during an input short-circuit is feasible
with input voltages up to 33V. This ensures that during
the transient, the IN – OUT Absolute Maximum Voltage of
±100V is not exceeded. During the short-circuit transient,
the MOSFET VDS sees |VGND|+|VGATE(NEG)|+VTH(M1)+VOUT.
Choose the MOSFET BVDSS accordingly. For other techniques to protect the LTC4372/LTC4373 during input
short-circuits see the Design Examples section.


**Reverse Input Protection**

Negative voltages at IN can also occur if a battery
is plugged in backwards or a negative supply is inadvertently connected. Figure 7 shows the waveforms when the
application circuit in Figure 2 is hot plugged to –24V. Due
to the parasitic inductance in between input and IN/
SOURCE, the voltages at the pins can ring significantly
below –24V. Similar to the input short-circuit situation,
the GND – GATE clamp causes M1 to divert the current
in the parasitic inductances to COUT. The GND – GATE
clamp limits the maximum DC negative voltage that the
Figure 2 application can handle to –28V.


Rev. A


# ~~12~~



[For more information www.analog.com](https://www.analog.com)


### **APPLICATIONS INFORMATION**

I(M1)
2A/DIV


SOURCE
20V/DIV


GATE
20V/DIV


VGATE-SOURCE
10V/DIV



50ms/DIV

**(a)**


50ms/DIV


IGATEA(LEAKAGE)= IGATEB(LEAKAGE) =100nA

**(b)**


## LTC4372/LTC4373





OUT
1V/DIV



43723 F09a


43723 F09b



1μs/DIV



43723 F07



**Figure 7. LTC4372/LTC4373 Handling Reverse Input**


**Paralleling Supplies**

Multiple LTC4372/LTC4373’s can be used to combine the
outputs of two or more supplies for redundancy or for
droop sharing, as shown in Figure 8. For redundant supplies, the supply with the highest output voltage sources
most or all of the load current. Figure 9a and Figure 9b
show the load transition between the two redundant
power supplies.

Depending on INA and INB’s supply impedances,
slew rates and the transient response of the LTC4372/
LTC4373, a transient reverse current might flow into lower



5V

INA, INB
50mV/DIV


GATEA,
GATEB
2V/DIV

5V


I(M1A)
0.5A/DIV

0A


I(M1B)
0.5A/DIV

0A


5V

OUT
50mV/DIV



INA



M1A
Si4190ADY





POWER
SUPPLY
A


POWER
SUPPLY
B













**Figure 9. Load Transition of Redundant Power Supplies**


supply (INA) from the supply ramping higher (INB). The
reverse current may cause INA to rise, with the amount
of voltage rise dependent on the input supply's impedance. The safest course of action is to use capacitors on
the input supply whose voltage rating is higher than the
highest voltage in the system, or to consider protecting
these capacitors with a TVS, for example.

If the higher supply’s input is shorted to ground while
delivering load current, the flow of current temporarily
reverses and flows backwards through the higher supply’s MOSFET. The LTC4372/LTC4372 sense this reverse
current and activate a fast pull-down to quickly turn off
the MOSFET.

If all the load current was supplied by the channel that suffered the short, the output will fall until the body diode of the
next MOSFET conducts. Meanwhile, the LTC4372/LTC4372
charge the MOSFET gate with 20μA until the forward drop

















**Figure 8. Redundant Power Supplies**



COUT
100µF



[For more information www.analog.com](https://www.analog.com)


# 13 Rev. A


## LTC4372/LTC4373
### **APPLICATIONS INFORMATION**

is reduced to 30mV. If this supply was sharing load current at the time of the fault, its associated ORing MOSFET
was already servoed to less than 30mV drop. In this case,
the LTC4372/LTC4372 will simply drive the MOSFET gate
higher to maintain a drop of 30mV at full load.

Load sharing can be accomplished if both power supply output voltages and source impedances are nearly
equal. The 30mV regulation technique allows load sharing
between outputs. The degree of sharing is a function of
MOSFET RDS(ON), the source impedance of the supplies
and their initial output voltages.


**Using the LTC4372’s SHDN and 2UPU**

When SHDN goes high, the LTC4372 enters shutdown
and asserts a 1mA pull-down between GATE and SOURCE
to turn off the external MOSFET. It also turns off most of
the internal circuitry, reducing IIN to 0.5μA. GATE is held
low with a 3μA pull-down to GND. If IN and SOURCE are
connected together, IQ = 3.0μA + 0.5μA = 3.5μA.

Shutting down the part does not interrupt forward current
flow as a path is still present through M1’s body diode. A
second MOSFET may be added to block the forward path (see
Figure 10). In this case, GATE and SOURCE are pulled to GND
during shutdown. The 3μA pull-down on GATE is pinched off
and IQ = 0.5μA. With back-to-back MOSFETs, SHDN serves
as an on/off control for the forward path, as well as enabling
the diode function. When SHDN is driven low, the LTC4372
exits shutdown and re-enters ideal diode operation.



If ∆VDS ≤ 30mV, the LTC4372/LTC4373 stay activated but
holds M1 and M2 off until the input exceeds the output by
30mV. In this way normal diode behavior of the circuit is
preserved, but with soft starting when the diode turns on.

When SHDN is driven high or UV driven low, GATE pulls
the MOSFET gates down quickly to SOURCE with a 1mA
pull-down. Both forward and reverse paths are cut off and
IQ is reduced to 0.5μA.


**Configuring LTC4373’s UV and UVOUT for Voltage**
**Monitoring**

With back-to-back MOSFETs, the LTC4373 can implement voltage monitoring at IN. Connect a resistive voltage
divider between IN and ground to bias UV. UV has a high
to low threshold of 1.191V with 15mV of hysteresis. The
UV hysteresis is around 1.3% referred to VUV.

Rev. A



If SHDN is not needed, connect it to GND. SHDN may
be driven with a 3.3V or 5V logic signal. It can also be
driven with an open-drain or collector output with SHDN
tied to 2UPU. 2UPU provides an internal pull up current
of 2μA to INTVCC. For higher pull-up currents, connect a
resistor from SHDN to INTVCC (capable of supplying up
to 10μA) or IN.


**Load Switching and Inrush Control**

By adding a second MOSFET as shown in Figure 10, the
LTC4372/LTC4373 can be used to control power flow in
the forward direction while retaining ideal diode behavior in the reverse direction. The body diodes of M1 and
M2 prohibit current flow when the MOSFETs are off. M1
serves as the ideal diode while M2 acts as a switch to
control forward power flow. ON/OFF control is provided
by SHDN or UV. C2 and R2 may be added to further reduce
inrush current. While C2 and R2 may be omitted if soft
starting is not needed. R1 is necessary to prevent MOSFET
parasitic oscillations and must be placed close to M2.

When SHDN is driven low or UV driven high and
∆VDS > 30mV, GATE sources 20μA and gradually charges
C2, pulling up both MOSFET gates. M2 operates as a
source follower as shown in Equation 4.



IINRUSH= [C][OUT]

C2 [• 20µA]



(4)







24V

10µF



VOUT
24V
10A



D3
SMAJ28A
28V









D2
SMAJ33A
33V


|M2 BSC026N08NS5|M1 BSC026N08NS5|
|---|---|
|R1<br>10Ω|R2<br>1k<br>C2<br>10nF|
|R1<br>10Ω||

















**Figure 10. 24V Load Switch and Ideal Diode with Inrush Control**
**and Reverse Input Protection**


# ~~14~~



[For more information www.analog.com](https://www.analog.com)


### **APPLICATIONS INFORMATION**

When UV ramps high to low, the LTC4373 enters undervoltage mode and asserts a 1mA pull-down between GATE
and SOURCE to turn off the external MOSFETs. It also turns
off most of the internal circuitry, reducing IQ to 0.5μA.
When UV ramps low to high, the LTC4373 exits undervoltage mode and goes back into ideal diode operation.

Figure 11 demonstrates how UV can be used to monitor
IN. For the UV pin, the maximum input leakage current
is 50nA. For a maximum error of 1% due to leakage currents, the resistive voltage divider current IRVD should be
at least 100 times the sum of the leakage currents, or 5μA.
The IN Undervoltage threshold (VH2L) is used to calculate
the value of R4, R5 and Undervoltage Recovery threshold
(VL2H) as shown in Equation 5.


## LTC4372/LTC4373

Obtain R4 and R5 from Equation 5 and calculate R6 using
Equation 6.



VH2L = VUV • [R4] [+] [R5]

R4

VL2H = VUV • [R5] [+] [Rpa]
Rpa



(6)



VH2L = VUV • [R4] [+] [R5]



R4



VL2H = V( UV + VUV(HYST)) [• ][R4] [+] [R5]



(5)



R4



For applications that require a higher and more accurate
hysteresis, UVOUT can be used to program an external
hysteresis to override the default hysteresis. Comparator
C1 in the Block Diagram controls an internal 140Ω switch
pulling down on UVOUT. When UV ramps below 1.191V
and trips C1, the switch pulls UVOUT low. When UV ramps
above 1.191V and un-trips C1, the switch turns off and
UVOUT goes high impedance. By connecting R6 between
UV and UVOUT, R4 and R5 implements VH2L and VL2H.


VIN



whereRpa = R4 //R6 = [R4 •R6]

R4 + R6

As long as the external hysteresis to be implemented
exceeds 5% of VH2L, Equation 6 can disregard the default
UV hysteresis without affecting accuracy.

With UVOUT connected to the resistive voltage divider, the
leakage current error needs to be re-visited. For the UVOUT
pin, the maximum input leakage current below 85°C is 50nA.
While IN ramps high to low, the resistive voltage divider sees
the leakage currents from both UV and UVOUT. This gives a
total of 100nA of leakage currents. With 5μA through R4 and
R5, this will add 2% inaccuracy to VH2L. While IN ramps low
to high, UVOUT is pulled low. The resistive voltage divider
sees only the 50nA of leakage current from UV. With 5μA
through R4 and R5, this will add 1% inaccuracy to VL2H. To
lower the leakage current error, increase IRVD.


**Layout Considerations**

Connect IN, SOURCE and OUT as close as possible to
the MOSFET source and drain pins. Keep the drain and
source traces to the MOSFET wide and short to minimize resistive losses as shown in Figure 12. Place COUT
close to the drain pin of MOSFET and keep the trace from
LTC4372/LTC4373 GATE pin to MOSFET gate short and
thin to minimize parasitic inductance and capacitance.
This practice will reduce the chance of MOSFET parasitic
oscillations. Place any surge suppressors and necessary
transient protection components close to the LTC4372/
LTC4373 using short lead lengths.

For the DFN package, pin spacing may be a concern at
voltages greater than 30V. Check creepage and clearance
guidelines to determine if this is an issue. To increase the
effective pin spacing between high voltage and ground
pins, leave the exposed pad connection open. Use
no-clean flux to minimize PCB contamination.















**Figure 11. Configuration for Monitoring IN**



[For more information www.analog.com](https://www.analog.com)


# 15 Rev. A


## LTC4372/LTC4373
### **APPLICATIONS INFORMATION**









VIN


GND







and ground to clamp IN and SOURCE when they spike negative. During the input short-circuit transient, D2 diverts the
reverse recovery current in the input parasitic inductances
to ground while COUT does the same for the output parasitic inductances. The 100V, FDMS86101 with RDS(ON) =
8mΩ(max) can handle both the 5A load current as well as
the input short-circuit voltage transients.


|1 S<br>2 S<br>3 S<br>4 G|D<br>MOSFET D<br>D<br>D|Col3|
|---|---|---|
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET|8|
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET||
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET|7|
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET||
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET|6|
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET||
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET|5|
|S<br>S<br>S<br>G<br>1<br>2<br>3<br>4|D<br>D<br>D<br>D<br>MOSFET||





GATE







VIN = 48V



M1
FDMS86101



VOUT
48V
5A







|Col1|S D<br>S D<br>MOSFET<br>S D<br>G D|Col3|
|---|---|---|
|1|1|8|
||||
|2|2|7|
||||
|3|3|6|
||||
|4|4|5|
||||


GATE























COUT



IN, SOURCE



OUT



GND





43723 F12

|4|2 3|1|
|---|---|---|
|LTC4372<br>MS8|LTC4372<br>MS8|LTC4372<br>MS8|
|5<br>|6<br>7|8|



**Figure 12. Layout, MS8 and DD8 Package**


**Design Examples**

The following design example demonstrates the considerations involved in selecting components for a 12V system with 20A maximum load current (see Figure 2). First,
choose the N-channel MOSFET. The 80V BSC026N08NS5
with RDS(ON) = 2.6mΩ(max) offers a good solution. The
maximum voltage drop across is:

ΔVSD = 20A • 2.6mΩ = 52mV

The maximum power dissipation in the MOSFET is:

P = 20A • 52mV = 1.04W

During input short-circuit voltage transients, using the
GND – GATE clamp to hold GATE should keep IN, SOURCE,
GATE and OUT within their Absolute Maximum Ratings. If
there is a problem with SOURCE to GND shoot through
current during input short-circuits, add a RGND of 100Ω.

Figure 13 shows a high voltage application. For the 48V
system, using the GND – GATE clamp to hold GATE during
input short-circuit voltage transients can exceed IN – OUT’s
–100V absolute maximum voltage. D2 is added between IN



**Figure 13. 48V Ideal Diode without Reverse Input Protection**


Figure 14 shows a high voltage application with reverse
battery protection. To handle a potential worst-case
situation of –48V at the input side and 48V at the output side, the BVDSS of the external MOSFET must be
greater than 48V + 48V = 96V with allowance. Choose
the 200V, IPB107N20N3G in the TO-263 package with
RDS(ON) = 10.7mΩ(max).

When IN is –48V and OUTPUT is 48V, D3 breaks down
and clamps IN – GND at about –6V. The MOSFET is held
off and isolates the load from the negative input. D1 and
R7 clamps OUT – GND to about 70V. The combination of
D1, D2, D3 and R7 clamps IN – OUT to about 76V.

During an input short-circuit, M1 drain spikes positive
and IN spikes negative. D2, D3 and D4 commutates the
reverse recovery current in the input parasitic inductances
while COUT does the same for the output parasitic inductances. D1, D2, D3, D4, R7 and R8 clamp IN, SOURCE,
OUT and GND to within their Absolute Maximum Ratings.

During normal ideal diode operation with GATE high, D4,
C3 and C4 help to handle IQ pulsating between 300μA
(charging GATE) and 3.5μA (charge pump sleep mode)
while D1, D2 and D3 draw no current.


Rev. A


# ~~16~~



[For more information www.analog.com](https://www.analog.com)


### **APPLICATIONS INFORMATION**



M1
IPB107N20N3G


## LTC4372/LTC4373

VOUT
48V
5A

































**Figure 14. 48V Ideal Diode with Reverse Input Protection**


[For more information www.analog.com](https://www.analog.com)


# 17 Rev. A


## LTC4372/LTC4373
### **APPLICATIONS INFORMATION**







OUTPUT





VIN
12V
WITHSTANDS
–28V TO 60V DC

# ~~18~~































|Col1|D5* SMAJ60A 60V|QUIESCENT CURRENT < 22µA FOR I-GRADE TEMPERATURE|
|---|---|---|
||M1<br>FDMS86101|M2<br>IRLR2908<br>RSNS<br>20mΩ|
|D1<br>SMAJ60A<br>60V<br>COUT<br>10µF<br>IN<br>2UPU<br>INTVCC<br>GND<br>SOURCE<br>LTC4372<br>GATE<br>OUT<br>R2<br>33Ω<br>CL<br>22µF<br>CTMR<br>220nF<br>C3<br>47nF<br>C2<br>4.7µF<br>R1<br>10k<br>RDRN<br>100k<br>R3<br>10Ω<br>DRN<br>VCC<br>ON<br>GND<br>TMR<br>SEL<br>43723 F15<br>SOURCE<br>LTC4380-2<br>GATE<br>OUT<br>SNS<br>SHDN<br>RGND<br>1k<br>C1<br>100nF<br>D4<br>1N4148W|D1<br>SMAJ60A<br>60V<br>COUT<br>10µF<br>IN<br>2UPU<br>INTVCC<br>GND<br>SOURCE<br>LTC4372<br>GATE<br>OUT<br>R2<br>33Ω<br>CL<br>22µF<br>CTMR<br>220nF<br>C3<br>47nF<br>C2<br>4.7µF<br>R1<br>10k<br>RDRN<br>100k<br>R3<br>10Ω<br>DRN<br>VCC<br>ON<br>GND<br>TMR<br>SEL<br>43723 F15<br>SOURCE<br>LTC4380-2<br>GATE<br>OUT<br>SNS<br>SHDN<br>RGND<br>1k<br>C1<br>100nF<br>D4<br>1N4148W|D1<br>SMAJ60A<br>60V<br>COUT<br>10µF<br>IN<br>2UPU<br>INTVCC<br>GND<br>SOURCE<br>LTC4372<br>GATE<br>OUT<br>R2<br>33Ω<br>CL<br>22µF<br>CTMR<br>220nF<br>C3<br>47nF<br>C2<br>4.7µF<br>R1<br>10k<br>RDRN<br>100k<br>R3<br>10Ω<br>DRN<br>VCC<br>ON<br>GND<br>TMR<br>SEL<br>43723 F15<br>SOURCE<br>LTC4380-2<br>GATE<br>OUT<br>SNS<br>SHDN<br>RGND<br>1k<br>C1<br>100nF<br>D4<br>1N4148W|


*D5 IS NEEDED TO CLAMP TRANSIENTS IN CASE INPUT SHORT-CIRCUIT OCCURS AT VIN > 33V

|Col1|Col2|
|---|---|
|RGND<br>1k|RGND<br>1k|



**Figure 15. Micropower 12V Surge Stopper with Ideal Diode**



M1
BSC026N08NS5





VOUT
12V
10A



















**Figure 16. 12V Ideal Diode with Shutdown ICC of 0.5μA (Nominal)**


[For more information www.analog.com](https://www.analog.com)



Rev. A


### **PACKAGE DESCRIPTION**



**DD Package**
**8-Lead Plastic DFN (3mm** × **3mm)**
(Reference LTC DWG # 05-08-1698 Rev C)


|±0.05 1.65 ±0.05<br>2.10 ±0.05 (2 SIDES)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|0.70 ±|
|---|---|---|---|---|---|---|---|---|---|---|
|1.65±0.05<br>(2 SIDES)<br>2.10±0.05<br> ±0.05|||||||||||
|1.65±0.05<br>(2 SIDES)<br>2.10±0.05<br> ±0.05|||||||||||
|1.65±0.05<br>(2 SIDES)<br>2.10±0.05<br> ±0.05|||||||||||
|0.25±0.05|0.25±0.05||||||||||



RECOMMENDED SOLDER PAD PITCH AND DIMENSIONS
APPLY SOLDER MASK TO AREAS THAT ARE NOT SOLDERED




## LTC4372/LTC4373







PIN 1
TOP MARK
(NOTE 6)




|Col1|Col2|Col3|3.00 ±<br>(4 SID|
|---|---|---|---|
|||||






|0.40 ± R = 0.125 TYP|Col2|Col3|Col4|0.40 ±|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|<br> ±0.10<br> IDES)<br> <br>TYP<br>2.38±0.10<br>1<br>4<br>8<br>5<br>(DD8<br>0.25±0.05<br>0.50 BSC|<br> ±0.10<br> IDES)<br> <br>TYP<br>2.38±0.10<br>1<br>4<br>8<br>5<br>(DD8<br>0.25±0.05<br>0.50 BSC|<br> ±0.10<br> IDES)<br> <br>TYP<br>2.38±0.10<br>1<br>4<br>8<br>5<br>(DD8<br>0.25±0.05<br>0.50 BSC|<br> ±0.10<br> IDES)<br> <br>TYP<br>2.38±0.10<br>1<br>4<br>8<br>5<br>(DD8<br>0.25±0.05<br>0.50 BSC|<br>8|<br>8|<br>8|<br>8|<br>8|
|<br> ±0.10<br> IDES)<br> <br>TYP<br>2.38±0.10<br>1<br>4<br>8<br>5<br>(DD8<br>0.25±0.05<br>0.50 BSC|||||||||
|±0.10<br> IDES)|||||||||
|±0.10<br> IDES)|||||||||
|0.25|||||||||
|0.25|||||||||
|0.25||2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|2.38±0.10<br>1<br>4<br> ±0.05<br>0.5|



0.00 – 0.05



BOTTOM VIEW—EXPOSED PAD



NOTE:
1. DRAWING TO BE MADE A JEDEC PACKAGE OUTLINE M0-229 VARIATION OF (WEED-1)
2. DRAWING NOT TO SCALE
3. ALL DIMENSIONS ARE IN MILLIMETERS
4. DIMENSIONS OF EXPOSED PAD ON BOTTOM OF PACKAGE DO NOT INCLUDE
MOLD FLASH. MOLD FLASH, IF PRESENT, SHALL NOT EXCEED 0.15mm ON ANY SIDE
5. EXPOSED PAD SHALL BE SOLDER PLATED
6. SHADED AREA IS ONLY A REFERENCE FOR PIN 1 LOCATION
ON TOP AND BOTTOM OF PACKAGE


[For more information www.analog.com](https://www.analog.com)


# 19 Rev. A


## LTC4372/LTC4373
### **PACKAGE DESCRIPTION**

|5.10 (.201) MIN|Col2|
|---|---|
|0.42 ± 0.038<br>||
|0.42 ± 0.038<br>||



TYP



**MS8 Package**
**8-Lead Plastic MSOP**
(Reference LTC DWG # 05-08-1660 Rev G)


0.889 ±0.127
(.035 ±.005)



BSC



(.118 ±.004)
(NOTE 4)


0.86
(.034)
REF



RECOMMENDED SOLDER PAD LAYOUT



|3.00 ±0.102|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|8<br>7<br>6 5|8<br>7<br>6 5|8<br>7<br>6 5|8<br>7<br>6 5|8<br>7<br>6 5|8<br>7<br>6 5|8<br>7<br>6 5|8<br>7<br>6 5|
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||
|4.90 ±0.152<br>(.193 ±.006)<br>3.00 ±0.102<br>~~(.118 ±.004)~~<br>(NOTE 3)|||||||||


1.10
(.043)
MAX


|0.254 DE|Col2|
|---|---|
|(.010)|(.010)|
|||
|||





1 2 3 4





DETAIL “A”


SEATING
PLANE



GAUGE PLANE



BSC



NOTE:

BSC

1. DIMENSIONS IN MILLIMETER/(INCH)
2. DRAWING NOT TO SCALE
3. DIMENSION DOES NOT INCLUDE MOLD FLASH, PROTRUSIONS OR GATE BURRS.
MOLD FLASH, PROTRUSIONS OR GATE BURRS SHALL NOT EXCEED 0.152mm (.006") PER SIDE
4. DIMENSION DOES NOT INCLUDE INTERLEAD FLASH OR PROTRUSIONS.
INTERLEAD FLASH OR PROTRUSIONS SHALL NOT EXCEED 0.152mm (.006") PER SIDE
5. LEAD COPLANARITY (BOTTOM OF LEADS AFTER FORMING) SHALL BE 0.102mm (.004") MAX


# ~~20~~



Rev. A



[For more information www.analog.com](https://www.analog.com)


## LTC4372/LTC4373
### **REVISION HISTORY**



|REV|DATE|DESCRIPTION|PAGE NUMBER|
|---|---|---|---|
|A|12/21|Revised bullets and SHDN pin description.<br>Revised Paralleling Supplies section.<br>Revised Equations 5 and 6.<br>Added new application.|1<br>13<br>15<br>18|


Information furnished by Analog Devices is believed to be accurate and reliable. However, no responsibility is assumed by Analog
Devices for its use, nor for any infringements of patents or other rights of third parties that may result from its use. Specifications
[subject to change without notice. No license is granted by implicatior otherwise under any patent or patent rights of Analog Devices.For more informati](https://www.analog.com) **on** [www.analog.com](https://www.analog.com)


# 21 Rev. A




## LTC4372/LTC4373
### **TYPICAL APPLICATION**





VIN
28V



UNDERVOLTAGE CUTOFF = 24V

28V
10A







COUT
100µF






|M2 BSC026N08NS5|M1 BSC026N08NS5|
|---|---|
|R1<br>10Ω||
|R1<br>10Ω||





























**Figure 17. 28V Supply with Voltage Monitoring and Backup Channel**

### **RELATED PARTS**


|PART NUMBER|DESCRIPTION|COMMENTS|
|---|---|---|
|LTC4352|Ideal Diode Controller|Controls N-Channel MOSFET, 0V to 18V Operation|
|LTC4353|Dual Ideal Diode Controller|Controls Two N-Channel MOSFETs, 0V to 18V Operation|
|LTC4355|High Voltage Diode-OR Controller and Monitor|Controls Two N-Channel MOSFETs, 0.4μs Turn-Off, 80V Operation|
|LTC4357|High Voltage Ideal Diode Controller|Controls N-Channel MOSFET, 0.5μs Turn-Off, 80V Operation|
|LTC4358|5A Ideal Diode|Internal N-Channel MOSFET, 9V to 26.5V Operation|
|LTC4359|Ideal Diode Controller with Reverse Input Protection|Controls N-Channel MOSFET, 4V to 80V Operation, –40V Reverse Input|
|LTC4364|Surge Stopper with Ideal Diode|4V to 80V Operation, –40V Reverse Input, –20V Reverse Output|
|LTC4371|Dual Negative Voltage Ideal Diode-OR Controller and Monitor|Controls Two MOSFETs, 220ns Turn-Off, Withstands > ±300V Transients|
|LTC4376|7A Ideal Diode with Reverse Input Protection|Internal N-Channel MOSFET, 4V to 40V Operation, –40V Reverse Input|


# ~~22~~



Rev. A


12/21
[www.analog.com](https://www.analog.com)

[For more information www.analog.com](https://www.analog.com)  ANALOG DEVICES, INC. 2020-2021


