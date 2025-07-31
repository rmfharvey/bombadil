**Description**


The BCR420U and BCR421U monolithically integrate transistors,

diodes and resistors to function as a Constant Current Regulator

(CCR) for linear LED driving. The device regulates with a preset

10mA nominal that can be adjusted with an external resistor up to

350mA. It is designed for driving LEDs in strings and will reduce

current at increasing temperatures to self-protect. Operating as a

series linear CCR for LED string current control, it can be used in

multiple applications, as long as the maximum supply voltage to the

device is < 40V.

With the low-side control, the BCR421U has an Enable (EN) pin

which can be pulse-width modulated (PWM) up to 25kHz by a micro
controller for LED dimming.

With no need for additional external components, this CCR is fully

integrated into a 2x2x0.6mm package (U-DFN2020-6) minimizing

PCB area, off-board height, and component count.


**Applications**


Constant Current Regulation (CCR) in:

 - Edge Lighting Strips

 - Emergency Lighting

 - Signage, Advertising, Decorative and Architectural Lighting

 - Retail Lighting in Fridges, Freezer Cases and Vending Machines



**Features**


- LED Constant Current Regulator Using NPN Emitter-Follower with

Emitter Resistor to Current Limit

- I OUT – 10mA ±10% Constant Current (Preset)

- I OUT up to 350mA Adjustable with an External Resistor


(BCR421U)

- V OUT – 40V Supply Voltage

- P D up to 1.7W in U-DFN2020-6 Package


- 0.6mm Height for Low-profile Edge Lighting

- Low-Side Control Enabling PWM Input < 25kHz (BCR421U)

- Negative Temperature Coefficient (NTC) Reduces I OUT with


Increasing Temperature

- Parallel Devices to Increase Regulated Current

- **Totally Lead-Free & Fully RoHS Compliant (Notes 1 & 2)**

- **Halogen and Antimony Free. “Green” Device (Note 3)**


- **Automotive-Compliant Parts are Available Under Separate**

**[Datasheet (BCR420UFDQ/BCR421UFDQ)](http://www.diodes.com/_files/datasheets/BCR420UFDQ/BCR421UFDQ.pdf)**


**Mechanical Data**




- Case: U-DFN2020-6

- Case Material: Molded Plastic. “Green” Molding Compound.

UL Flammability Rating 94V-0

- Moisture Sensitivity: Level 1 per J-STD-020

- Terminals: Finish - NiPdAu, Solderable per MIL-STD-202, Method
208 **e4**

- Weight: 0.018 grams (Approximate)



U-DFN2020-6


Bottom View



EN OUT

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||



Internal Device


Schematic







EN


Top View



GND



Rext
(Optional)


GND



N/C


OUT



Rext




|Pin Name|Pin Function|
|---|---|
|OUT|Regulated Output Current|
|EN|Enable for Biasing<br>Transistor|
|Rext|External Resistor for<br>Adjusting Output Current|
|GND|Power Ground|
|N/C|Not connected internally|



Pin-Out



|Ordering Information (Note 4)|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|**Part Number**|**Compliance**|**Marking**|**Reel Size (inches)**|**Tape Width (mm)**|**Quantity Per Reel**|
|BCR420UFD-7|Standard|420|7|8|3,000|
|BCR421UFD-7|Standard|421|7|8|3,000|


Notes: 1. No purposely added lead. Fully EU Directive 2002/95/EC (RoHS), 2011/65/EU (RoHS 2) & 2015/863/EU (RoHS 3) compliant.
[2. See https://www.diodes.com/quality/lead-free/ for more information about Diodes Incorporated’s definitions of Halogen- and Antimony-free, "Green" and](https://www.diodes.com/quality/lead-free/)
Lead-free.
3. Halogen- and Antimony-free "Green” products are defined as those which contain <900ppm bromine, <900ppm chlorine (<1500ppm total Br + Cl) and
<1000ppm antimony compounds.
[4. For packaging details, go to our website at https://www.diodes.com/design/support/packaging/diodes-packaging/.](https://www.diodes.com/design/support/packaging/diodes-packaging/)



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



1 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**

**Marking Information**





xxx = Part Marking (See Ordering Information)
Y = Year: 0~9
W = Week: A~Z: 1~26 week;

a~z; 27~52 week; z represents
52 and 53 week



**Absolute Maximum Ratings** (Voltage relative to GND, @T A = +25°C, unless otherwise specified.)


|Characteristic|Col2|Symbol|Value|Unit|
|---|---|---|---|---|
|Enable Voltage|BCR420U|VEN|40|V|
|Enable Voltage|BCR421U|BCR421U|18|18|
|Output Current|Output Current|IOUT|500|mA|
|Output Voltage|Output Voltage|VOUT|40|V|
|Reverse Voltage Between all Terminals|Reverse Voltage Between all Terminals|VR|0.5|V|


|Thermal Characteristics (@TA = +25°C, unless otherwise specified.)|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|**Characteristic**|**Characteristic**|**Symbol**|**Value**|**Unit**|
|Power Dissipation|(Note 5)|PD|1.7|W|
|Power Dissipation|(Note 6)|(Note 6)|1.3|1.3|
|Thermal Resistance, Junction to Ambient|(Note 5)|RθJA|75|°C/W|
|Thermal Resistance, Junction to Ambient|(Note 6)|(Note 6)|100|100|
|Thermal Resistance, Junction to Lead|(Note 7)|RθJL|35|°C/W|
|Recommended Operating Junction Temperature Range|Recommended Operating Junction Temperature Range|TJ|-55 to +150|°C|
|Maximum Operating Junction and Storage Temperature Range|Maximum Operating Junction and Storage Temperature Range|TJ, TSTG|-65 to +150|-65 to +150|







|ESD Ratings (Note 8)|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|**Characteristic**|**Characteristic**|**Symbol**|**Value**|**Unit**|**JEDEC Class**|
|Electrostatic Discharge – Human Body<br>Model|BCR420U|HBM|700|V|1B|
|Electrostatic Discharge – Human Body<br>Model|BCR421U|BCR421U|1000|V|1C|
|Electrostatic Discharge – Machine Model|BCR420U|MM|300|V|B|
|Electrostatic Discharge – Machine Model|BCR421U|BCR421U|400|V|C|


Notes: 5. For a device mounted with the OUT leads on 50mm x 50mm 1oz copper that is on a single-sided 1.6mm FR-4 PCB; device is measured under still
air conditions while operating in steady-state.
6. Same as Note 5, except mounted on 25mm x 25mm 1oz copper.
7. R θJL = Thermal resistance from junction to solder-point (at the end of the OUT leads).
8. Refer to JEDEC specification JESD22-A114 and JESD22-A115 .



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



2 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


























































|Electrical Characteristics (@TA = +25°C, unless otherwise specified.)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|**Characteristic**|**Characteristic**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|**Test Condition**|
|Collector-Emitter Breakdown Voltage|Collector-Emitter Breakdown Voltage|BVCEO|40|—|—|V|IC = 1mA|
|Enable Current|BCR420U|IEN|—|1.2|—|mA|VEN= 24V|
|Enable Current|BCR421U|BCR421U|—|1.2|—|—|VEN= 3.3V|
|DC Current Gain|DC Current Gain|hFE|200|350|500|—|IC = 50mA; VCE = 1V|
|Internal Resistor|Internal Resistor|RINT|85|95|105|Ω|IRINT = 10mA|
|Bias Resistor|BCR420U|RB|—|20|—|kΩ|—|
|Bias Resistor|BCR421U|BCR421U|—|1.5|—|—|—|
|Output Current|BCR420U|IOUT|9|10|11|mA|VOUT = 1.4V; VEN = 24V|
|Output Current|BCR421U|BCR421U|9|10|11|mA|VOUT = 1.4V; VEN = 3.3V|
|Output Current at<br>REXT = 5.1Ω|BCR420U|IOUT|—|150|—|mA|VOUT > 2.0V; VEN = 24V|
|Output Current at<br>REXT = 5.1Ω|BCR421U|BCR421U|—|150|—|mA|VOUT > 2.0V; VEN = 3.3V|
|Voltage Drop (VREXT)|Voltage Drop (VREXT)|VDROP|0.85|0.95|1.05|V|IOUT = 10mA|
|Minimum Output Voltage|Minimum Output Voltage|VOUT(MIN)|—|1.4|—|V|IOUT > 18mA|
|Output Current Change<br>vs. Temperature|BCR420U|ΔIOUT/IOUT|—|-0.2|—|%/°C|VOUT > 2.0V; VEN = 24V|
|Output Current Change<br>vs. Temperature|BCR421U|BCR421U|—|-0.2|—|—|VOUT > 2.0V; VEN = 3.3V|
|Output Current Change<br>vs. Supply Voltage|BCR420U|ΔIOUT/IOUT|—|1|—|%/V|VOUT > 2.0V; VEN = 24V|
|Output Current Change<br>vs. Supply Voltage|BCR421U|BCR421U|—|1|—|—|VOUT > 2.0V; VEN = 3.3V|



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



3 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


**Typical Thermal Characteristics BCR420/1U** (@T A = +25°C, unless otherwise specified.)



2.0


1.6


1.2


0.8


0.4





0.0

|50m|m * 50mm<br>1oz Cu|Col3|Col4|
|---|---|---|---|
|50m<br>|m * 50mm<br>1oz Cu|m * 50mm<br>1oz Cu|m * 50mm<br>1oz Cu|
||25mm<br>1oz|25mm<br>1oz|* 25mm<br> Cu|
||25mm<br>1oz|25mm<br>1oz|* 25mm<br> Cu|
|||||
||||15mm * 15mm<br>1oz Cu|
|||||
|mm * 10mm<br>1oz Cu||||

0 50 100 150

Temperature (°C)
**Derating Curve**


75



|+25°C, unless otherwise specified.)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|0<br>100<br>200<br>300<br>400<br>500<br>600<br>|
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>||||||||
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>||||||||
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>||||||||
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>||||||||
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>||||||||
|0<br>100<br>200<br>300<br>400<br>500<br>600<br>||||||||


100 1000



10


1



Copper Area (mm



2 )



**Rth(JA) VS 1 oz Cu Area**







50





25


0

|50m<br>1<br>D=0.5|m * 50<br>oz Cu|mm|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|50m<br>1<br>D=0.5|||||||||||
|=0.2|||||||||||
|D=0.|1<br>D||Sing|le P|uls|e|||||
|D=0.|1<br>D||5||||||||
|D=0.|1<br>D|=0.0|=0.0|=0.0|=0.0|=0.0|=0.0|=0.0|=0.0|=0.0|
|D=0.|1<br>D||||||||||

100µ 1m 10m 100m 1 10 100 1k

Pulse Width (s)

**Transient Thermal Impedance**


150


|Single P<br>T =2<br>amb|uls<br>5°C|e|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Single P<br>T~~amb~~=2|uls<br>5°C|e|50|mm<br>|* 5<br>|0mm<br>|0mm<br>|0mm<br>|
||||||||||
||||||||||
||||||||||
|||~~25~~|~~mm~~<br>|~~* 25~~<br>|~~mm~~<br>||||
||||~~1o~~|~~z Cu~~|||||
||||||||||
|15mm<br>1o|||m||||||
|15mm<br>1o|* 1<br>z C|5m<br>u|5m<br>u|5m<br>u|5m<br>u|5m<br>u|5m<br>u|5m<br>u|
|~~ 10mm~~|||||||||
|~~ Cu~~|||||||||



100µ 1m 10m 100m 1 10 100 1k

Pulse Width (s)

**Pulse Power Dissipation**







125


100


75


50


25















100


10





0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|15mm *<br>~~1oz~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|15mm<br>~~ Cu~~|
||||||||||||
|0.5|||||||||||
|~~0.2~~|||||||||||
|||||||Sin|gle|Pul|se|se|
||||1|~~D~~|~~=0.0~~|~~5~~|||||
|||D=0.|D=0.|D=0.|||||||

100µ 1m 10m 100m 1 10 100 1k

Pulse Width (s)

**Transient Thermal Impedance**


|10mm|* 1|0m|m|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|~~1o~~|~~z C~~|~~u~~||||||||
|15mm * 15m|m|||||||||
|~~1oz Cu~~||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
||~~25~~<br>|~~m *~~<br>~~1oz~~|~~ 25~~<br>~~Cu~~|~~m~~||||||
|||||||||||
|~~Single Pulse~~<br>||~~5~~|~~0m~~|~~ *~~|~~0m~~|~~m~~||||
|~~T=25°C~~||||||||||
|~~amb~~|||~~1~~|~~oz~~|~~u~~|||||



100µ 1m 10m 100m 1 10 100 1k

Pulse Width (s)

**Pulse Power Dissipation**



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



4 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


**Typical Electrical Characteristics BCR421U** (@T A = +25°C, unless otherwise specified.)



0.20


0.16


0.12


0.08


0.04





0.20


0.15


0.10


0.05











0.000 1 2 3 4 5 6 7 8 9 10 11 12

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|V|EN|=3|.3|V|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||EX|T~~=~~|~~6.~~|~~~~||||RE|XT=|8.|2|||||||||||
|||||||||||||||REX|T=|10|||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||~~R~~E|XT~~=~~|~~15~~|~~~~||||~~R~~|EXT|~~=~~|~~30~~|~~~~|||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||R||=|op|en||||||
|||||||||||||||~~EX~~|||||||||
||||||||||||||||||||||||


V OUT (V)
# **V vs I**

**OUT** **OUT**


0.18


0.16



0.00

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||VOUT=5.4V||||||||
|||||||||||||||||
|~~ V~~OU|~~ V~~OU|T~~=1.~~|~~4V~~|||||||||||||
|~~ V~~OU|~~ V~~OU|||||||||||||||
|||||||||||||||||
|||||||||||||||||
|~~V=~~|~~V=~~|||||||||||||||
|~~V=~~|~~V=~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|~~3.3~~|
|EN|EN|||||||||||||||
|EN|EN|||||||||||||||

1 10 100

R EXT (  )
# R EXT (  ) vs I OUT



0.06


0.05


0.04


0.03









0.14


0.12


0.10


0.08



















0.06



0.02





V OUT (V) V OUT (V)
# **V vs I V vs I**

**OUT** **OUT** **OUT**





0.02


0.01









0.15


0.10


0.05











0.00


V OUT (V)

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
||||||||-|40<br>o|C|C||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||25<br>o|C|C||||||||||
||||||||~~8~~|~~5~~<br>~~oC~~|~~5~~<br>~~oC~~||||V=|3.3||
||||||||||||||~~EN~~|||
|||||||||||||||||
|||||||||||||~~R~~E|XT~~=6.~~|~~2~~||
|||||||||||||||||
|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT (V)|
|||||||||||||||||
||||||||-4|0<br>oC|0<br>oC|0<br>oC||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
||||~~25~~<br>~~o~~|~~C~~|8|8|||||||~~V~~EN|~~=3.3~~|~~V~~|
||||~~25~~<br>~~o~~|~~C~~|8|8|5<br>oC|5<br>oC|5<br>oC|5<br>oC|5<br>oC|5<br>oC|5<br>oC|5<br>oC|5<br>oC|
||||||||||||||REX|T=op|en|
|||||||||||||||||
|||||||||||||||||
|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|

# **V vs I**

**OUT** **OUT**



0.00

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|-40o|Col13|C|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
||||||~~25~~<br>~~o~~|~~25~~<br>~~o~~|~~C~~|||o||||||||
|||||||||~~8~~|~~8~~|~~5~~<br>~~C~~|||~~V~~EN|~~=3.3V~~|~~=3.3V~~|||
|||||||||~~8~~|~~8~~|~~5~~<br>~~C~~||||||||
||||||||||||||~~R~~EX|~~=20~~|~~=20~~|||
|||||||||||||||||||
|||||||||||||||||||
|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT (V)|
|VO|VO|||||||RE|RE|||||||||
|VO|VO|UT=2V<br>|UT=2V<br>||||||RE|XT=8.2|XT=8.2|XT=8.2|XT=8.2|XT=8.2|XT=8.2|XT=8.2|XT=8.2|
|||~~R~~|~~R~~|EXT~~=6~~|EXT~~=6~~|~~.2~~|~~.2~~||||||REX|REX|T=10~~~~|T=10~~~~||
|||~~R~~|~~R~~|||||||||||||||
|||||||||||||||||||
|~~R~~EXT|~~R~~EXT|~~=30~~|~~=30~~|||||||||||||||
|||||||||||||||||||
|||||||||||REXT=|REXT=|60|~~R~~E|~~R~~E|XT~~= o~~|XT~~= o~~|~~en~~|
|||||||||||REXT=|REXT=|60|~~R~~E|~~R~~E||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||

0 1 2 3 4 5

V EN (V)
# **V vs I**

**EN** **OUT**



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



5 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


**Typical Electrical Characteristics BCR421U** (Cont.) (@T A = +25°C, unless otherwise specified.)



3.0m


2.5m


2.0m


1.5m


1.0m















0.015


0.010


0.005







500.0μ ~~µ~~


0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
|||||IOUT|=0A||||||||
|||||~~R~~<br>|~~=open~~<br>|~~=open~~<br>||85<br>o|85<br>o|C|||
|||||~~EXT~~|||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||25<br>oC||~~-~~|~~40~~<br>~~oC~~|~~40~~<br>~~oC~~||
||||||||||||||
||||||||||||||
||||||||||||||

0 1 2 3 4 5



0.000

|Col1|Col2|Col3|Col4|Col5|Col6|-40|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||-40|-40|-40|oC|oC|oC|
|||||||25|25|25||||
|||||||25|25|2|oC|oC|oC|
|||||||||||||
|||||||8|8|8|5<br>oC|||
|||||||8|8|8||||
||||||||||||2V|
|||||||||||VOUT=|2V|
|||||||||||REXT=|open|
|||||||||||||

0 1 2 3 4 5



V EN (V) V EN (V)


# **V vs I**

**EN** **EN**


# **V vs I**

**EN** **OUT**



0.06


0.05


0.04


0.03


0.02


0.01















0.20


0.15


0.10







0.05





0.00

|Col1|Col2|Col3|-40o|Col5|C|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||~~-40~~<br>o|~~-40~~<br>o|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||25<br>oC||||
|||||||o||||||
||||||~~85~~<br>|~~85~~<br>||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||||||||||~~V~~|~~=2V~~|~~=2V~~|
||||||||||OUT|||
||||||||||~~R~~EXT|~~= 20~~||
|||||||||||||

0 1 2 3 4 5



0.00

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||||~~-40~~<br>|~~oC~~||
||||||||||||
||||||~~25~~<br>~~oC~~||||||
||||||||||||
|||||||||o|o||
|||||||||o|o|o|
|||||||||~~5~~<br>~~C~~|~~5~~<br>~~C~~||
||||||||VOU|T=2V|T=2V||
||||||||REXT|=6.2|=6.2||
||||||||||||

0 1 2 3 4 5



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



V EN (V) V EN (V)
# **V vs I V vs I**

**EN** **OUT** **EN** **OUT**


6 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


**Typical Electrical Characteristics BCR420U** (Cont.) (@T A = +25°C, unless otherwise specified.)



0.20


0.16


0.12


0.08


0.04



0.20


0.15


0.10


0.05











0.00

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|V|EN|=2|4V|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||EX|T~~=~~|~~6.~~|~~~~||||RE|XT=|8.|2|||||||||||
|||||||||||||||RE|RE|XT=|10||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||~~~~||||
|||||||||||||||||E|XT|~~1~~|||||
|||||||||||||||||R|EXT|= 3|0||||
||||||||||||||~~R~~|||~~=~~|~~op~~|~~en~~|||||
|||||||||||||||~~EX~~|~~EX~~||||||||
||||||||||||||||||||||||

0 1 2 3 4 5 6 7 8 9 10 11 12

V OUT (V)
# **V vs I**

**OUT** **OUT**


0.18


0.16



0.00

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||VOUT|VOUT|= 5.4|V|||||||
||||||||||||VOUT|VOUT|||||||||
||||||||||||||||||||||
|V|V|V|||||||||||||||||||
|V|V|V|=1|.4V|||||||||||||||||
||||~~UT~~||||||||||||||||||
||||||||||||||||||||||
|~~V=~~|~~V=~~|~~V=~~|||||||||||||||||||
|~~V=~~|~~V=~~|~~V=~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|~~24V~~|
|EN|EN|EN|||||||||||||||||||
|EN|EN|EN|||||||||||||||||||

1 10 100

R **EXT** (  )
# R EXT (  )vs I OUT



0.06


0.05


0.04


0.03









0.14


0.12


0.10


0.08















0.06



0.02



V OUT (V) V OUT (V)
# **V vs I V vs I**

**OUT** **OUT** **OUT**







0.02


0.01


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|-4|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||-4|0<br>oC|0<br>oC|0<br>oC|0<br>oC|0<br>oC|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||~~25~~<br>|~~C~~||||o||||||
|||||||||~~5~~<br>~~C~~||~~V~~EN~~=~~|~~24V~~|||
|||||||||||||||
|||||||||||||||
|||||||||||~~R~~EXT|~~=20~~|||
|||||||||||||||
|||||||||||||||
|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>1<br>**VOUT vs IOUT**<br> VOUT  (V)|











0.15


0.10


0.05











0.00



0.00

|V|Col2|Col3|Col4|2V|Col6|Col7|Col8|R<br>E|Col10|Col11||Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|V|V|V|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|
|V|V|V|OUT=|OUT=|OUT=|OUT=|OUT=|OUT=|RE|XT=8|||||||
|~~R~~E|~~R~~E|~~R~~E||~~~~|RE|RE|XT=2|0|0|||||Rext=1|0||
|~~R~~E|~~R~~E|~~R~~E||~~~~|RE|RE|XT=2|0|0||||||||
|~~R~~E|~~R~~E|~~R~~E|T~~=30~~|~~~~|~~~~|~~~~|||||||||||
||||||||||||||||||
|||||||||||REX|T=60|||~~R~~EXT|~~=ope~~|~~n~~|
|||||||||||REX|T=60||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||

0 5 10 15 20 25 30

V EN (V)
# **V vs I**

**EN** **OUT**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||o|o|||||||
||||||||-|40<br>C|40<br>C|||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||25<br>~~o~~C||||||||||||
||||||||~~8~~|~~5~~<br>~~oC~~||||V=|24V|24V||
|||||||||||||~~EN~~||||
|||||||||||||||||
||||||||||||~~R~~E|XT~~=6.~~|~~2~~|||
|||||||||||||||||
|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|0<br>2<br>4<br>6<br>8<br>10<br>**VOUT vs IOUT**<br> VOUT  (V)|
|||||||||||||||||
||||||||-4|0<br>oC||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
||||~~o~~|~~o~~|~~o~~|~~o~~|~~o~~|~~o~~|~~o~~|~~o~~|~~o~~|||||
||||~~25~~<br>||8|8|oC|||||~~V~~EN|~~=24V~~|~~=24V~~|n<br>|
|||||||||||||REX|T=ope|T=ope|T=ope|
|||||||||||||||||
|||||||||||||||||
|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|~~2~~<br>~~4~~<br>~~6~~<br>~~8~~<br>~~10~~<br>~~1~~<br>|



V OUT (V)
# **V vs I**

**OUT** **OUT**


BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



7 of 13

**[www.diodes.com](http://www.diodes.com)**



January 2018
© Diodes Incorporated


**BCR420UFD / BCR421UFD**


**Typical Electrical Characteristics BCR420U** (Cont.) (@T A = +25°C, unless otherwise specified.)



3.0m


2.5m


2.0m


1.5m


1.0m











0.015


0.010


0.005











500.0 ~~µ~~ ~~μ~~


0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||
||||||||||REX<br>OUT|T=op<br>=0A|en||~~85~~<br>~~o~~|~~C~~|~~C~~||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
|||||||||||25<br>oC||~~-4~~|~~0~~<br>~~oC~~||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||

0 5 10 15 20 25 30 35 40



0.000

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|-40o|C|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||25<br>|oC|||
||||||||||||
||||||||8|5<br>oC|||
|||||||||VO||V|
|||||||||VO|UT=2|V|
|||||||||RE|XT=o|pen|
|||||||||RE|||

0 5 10 15 20 25 30



V EN (V) V EN (V)


# **V vs I**

**EN** **EN**


# **V vs I**

**EN** **OUT**



0.06


0.05


0.04


0.03


0.02


0.01



















0.20


0.15


0.10



0.05





0.00

|Col1|Col2|Col3|Col4|Col5|C|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||~~-40~~<br>o|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|~~C~~|
||||||||||||||
|||||8|5<br>oC||25<br>o|C|||||
||||||||||||||
||||||||||||||
|||||||||V|~~OUT~~=|2V|2V||
|||||||||~~R~~|EXT~~=2~~|~~0~~|||
||||||||||||||

0 5 10 15 20 25 30



0.00

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||~~-40~~<br>|~~oC~~|~~oC~~||
|||||||~~25~~<br>~~o~~|~~C~~|||||
||||||||~~85~~<br>~~o~~|~~C~~||||
|||||||||VOUT=2|V|||
||||||||R|EXT=6.|2|||
|||||||||||||

0 5 10 15 20 25 30



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



V EN (V) V EN (V)
# **V vs I V vs I**

**EN** **OUT** **EN** **OUT**


8 of 13

**[www.diodes.com](http://www.diodes.com)**


**Application Information**


Figure 1 Typical Application Circuit for

Linear Mode Current Sink LED Driver


Figure 2 Application Circuit for Increasing LED Current



**BCR420UFD / BCR421UFD**


The BCR420/1 are designed for driving low current LEDs with typical
LED currents of 10mA to 350mA. They provide a cost-effective way for
driving low current LEDs compared with more complex switching
regulator solutions. Furthermore, they reduce the PCB board area of the
solution as there is no need for external components like inductors,
capacitors and switching diodes.

Figure 1 shows a typical application circuit diagram for driving an LED
or string of LEDs. The device comes with an internal resistor (R INT ) of
typically 95Ω, which in the absence of an external resistor, sets an LED
current of 10mA (typical) from a V EN = 3.3V and V OUT = 1.4V for
BCR421; or V EN = 24V and V OUT = 1.4V for BCR420. LED current can
be increased to a desired value by choosing an appropriate external
resistor, R EXT.

The R EXT vs I OUT graphs should be used to select the appropriate
resistor. Choosing a low tolerance R EXT will improve the overall
accuracy of the current sense formed by the parallel connection of R INT
and R EXT.

Two or more BCR420/1s can be connected in parallel to construct
higher current LED strings as shown in Figure 2. Consideration of the
expected linear mode power dissipation must be factored into the
design, with respect to the BCR420/1’s thermal resistance. The
maximum voltage across the device can be calculated by taking the
maximum supply voltage and subtracting the voltage across the LED
string.

V OUT = V S – V LED

P D = (V OUT × I LED ) + (V EN × I EN )

As the output current of BCR420/1 increases, it is necessary to provide
appropriate thermal relief to the device. The power dissipation
supported by the device is dependent upon the PCB board material, the
copper area and the ambient temperature. The maximum dissipation
the device can handle is given by:

P D = ( T J(MAX) - T A ) / R θJA

Refer to the thermal characteristic graphs on Page 4 for selecting the
appropriate PCB copper area.



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



9 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


**Application Information** (Cont.)


PWM dimming can be achieved by driving the EN pin. Dimming is achieved by turning the LEDs ON and OFF for a portion of a single cycle. The
PWM signal can be provided by a micro-controller or analog circuitry; typical circuit is shown in Figure 3. Figure 4 is a typical response of LED
current vs. PWM duty cycle on the EN pin. PWM up to 25kHz with duty cycle of 0.5% (dimming range 200:1). This is above the audio band
minimizing audible power supply noise.


Figure 3 Application Circuits for LED Driver with PWM Dimming Functionality using BCR421U


Figure 4 Typical LED Current Response vs. PWM Duty Cycle for

25kHz PWM Frequency (Dimming Range 200:1)



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



10 of 13

**[www.diodes.com](http://www.diodes.com)**


**Application Information** (Cont.)


Figure 5 Application Circuit for LED Driver

with Reverse Polarity Protection


Figure 6 Application Circuit for LED Driver with

Assured Operation Regardless Of Polarity



**BCR420UFD / BCR421UFD**


To remove the potential of incorrect connection of the power supply
damaging the lamp’s LEDs, many systems use some form of
reverse polarity protection.

One solution for reverse input polarity protection is to simply use a
diode with a low V F in line with the driver/LED combination. The low
V F increases the available voltage to the LED stack and dissipates
less power. A circuit example is presented in Figure 5 which
protects the light engine although it will not function until the problem
is diagnosed and corrected. An SDM10U45LP (0.1A/45V) is shown,
providing exceptionally low V F for its package size of 1mm x 0.6mm.
Other reverse voltage ratings are available from Diodes
Incorporated’s website such as the SBR02U100LP (0.2A/100V) or
SBR0220LP (0.2A/20V).

While automotive applications commonly use this method for
reverse battery protection, an alternative approach shown in Figure
6, provides reverse polarity protection and corrects the reversed
polarity, allowing the light engine to function.

The BAS40BRW incorporates four low V F Schottky diodes in a
single package, reducing the power dissipated and maximizes the
voltage across the LED stack.

Figure 7 shows an example configuration for 350mA operation using
BCR421U. In such higher current configurations adequate enable
current is provided by increasing the enable voltage.


Figure 7 Example for 350mA Operation using BCR421U



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



11 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**

**Package Outline Dimensions**


[Please see http://www.diodes.com/package-outlines.html](http://www.diodes.com/package-outlines.html) for the latest version.



**U-DFN2020-6**


Seating Plane

|Col1|A1|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||A|A|A|A|A|A|
|A|||||||
|A|||||||
||||||||



L

|Col1|D|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||D2<br>D2/2|D2<br>D2/2|D2<br>D2/2|D2<br>D2/2|D2<br>D2/2|D2<br>D2/2|D2<br>D2/2|
|E<br>E2<br>E2/2||||||||
|E<br>E2<br>E2/2||||||||
|E<br>E2<br>E2/2||||||||
|E<br>E2<br>E2/2||||||||
||||e||b|b||



**Suggested Pad Layout**









Seating Plane








|U-DFN2020-6|Col2|Col3|Col4|
|---|---|---|---|
|**Dim**|**Min**|**Max**|**Typ**|
|**A **|0.57|0.63|0.60|
|**A1**|0|0.05|0.03|
|**A3**<br>|- <br>|- <br>|0.15<br>|
|**b **|0.20|0.30|0.25|
|**D **|1.95|2.075|2.00|
|**D2**<br>|1.45|1.65|1.55|
|**e **|-|-|0.65|
|**E **<br>|1.95<br>|2.075<br>|2.00<br>|
|**E2**<br>|0.76<br>|0.96<br>|0.86<br>|
|**L **<br>|0.30<br>|0.40<br>|0.35<br>|
|**All Dimensions in mm**|**All Dimensions in mm**|**All Dimensions in mm**|**All Dimensions in mm**|









L





[Please see http://www.diodes.com/package-outlines.html](http://www.diodes.com/package-outlines.html) for the latest version.


**U-DFN2020-6**


C



January 2018
© Diodes Incorporated


|Col1|X|Col3|
|---|---|---|
||||
||||
|Y|||


|Dimensions|Value<br>(in mm)|
|---|---|
|**C **<br>|0.65<br>|
|**G **|0.15|
|**X **|0.37|
|**X1**|1.67|
|**Y **|0.45|
|**Y1**|0.90|



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



12 of 13

**[www.diodes.com](http://www.diodes.com)**


**BCR420UFD / BCR421UFD**


**IMPORTANT NOTICE**

DIODES INCORPORATED MAKES NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARDS TO THIS DOCUMENT,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
(AND THEIR EQUIVALENTS UNDER THE LAWS OF ANY JURISDICTION).

Diodes Incorporated and its subsidiaries reserve the right to make modifications, enhancements, improvements, corrections or other changes
without further notice to this document and any product described herein. Diodes Incorporated does not assume any liability arising out of the
application or use of this document or any product described herein; neither does Diodes Incorporated convey any license under its patent or
trademark rights, nor the rights of others. Any Customer or user of this document or products described herein in such applications shall assume
all risks of such use and will agree to hold Diodes Incorporated and all the companies whose products are represented on Diodes Incorporated
website, harmless against all damages.

Diodes Incorporated does not warrant or accept any liability whatsoever in respect of any products purchased through unauthorized sales channel.
Should Customers purchase or use Diodes Incorporated products for any unintended or unauthorized application, Customers shall indemnify and
hold Diodes Incorporated and its representatives harmless against all claims, damages, expenses, and attorney fees arising out of, directly or
indirectly, any claim of personal injury or death associated with such unintended or unauthorized application.

Products described herein may be covered by one or more United States, international or foreign patents pending. Product names and markings
noted herein may also be covered by one or more United States, international or foreign trademarks.

This document is written in English but may be translated into multiple languages for reference. Only the English version of this document is the
final and determinative format released by Diodes Incorporated.


**LIFE SUPPORT**

Diodes Incorporated products are specifically not authorized for use as critical components in life support devices or systems without the express
written approval of the Chief Executive Officer of Diodes Incorporated. As used herein:

A.  Life support devices or systems are devices or systems which:

1. are intended to implant into the body, or


2. support or sustain life and whose failure to perform when properly used in accordance with instructions for use provided in the
labeling can be reasonably expected to result in significant injury to the user.

B.  A critical component is any component in a life support device or system whose failure to perform can be reasonably expected to cause the
failure of the life support device or to affect its safety or effectiveness.

Customers represent that they have all necessary expertise in the safety and regulatory ramifications of their life support devices or systems, and
acknowledge and agree that they are solely responsible for all legal, regulatory and safety-related requirements concerning their products and any
use of Diodes Incorporated products in such safety-critical, life support devices or systems, notwithstanding any devices- or systems-related
information or support that may be provided by Diodes Incorporated. Further, Customers must fully indemnify Diodes Incorporated and its
representatives against any damages arising out of the use of Diodes Incorporated products in such safety-critical, life support devices or systems.

Copyright © 2018, Diodes Incorporated

**[www.diodes.com](http://www.diodes.com)**



January 2018
© Diodes Incorporated



BCR420UFD / BCR421UFD

Document number: DS38588 Rev. 3 - 2



13 of 13

**[www.diodes.com](http://www.diodes.com)**


