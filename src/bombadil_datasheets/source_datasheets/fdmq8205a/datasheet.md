# GreenBridge� 2 Series of High-Efficiency Bridge Rectifiers FDMQ8205A

**General Description**
FDMQ8205A is GreenBridge 2 series of quad MOSFETs for a
bridge application so that the input will be insensitive to the polarity of
a power source coupled to the device. Many known bridge rectifier
circuits can be configured using typical diodes. The conventional
diode bridge has relatively high power loss that is undesirable in many
applications. Especially, Power over Ethernet (PoE) Power Device
(PD) application requires high−efficiency bridges because it should be
operated with the limited power delivered from Power Source
Equipment (PSE) which is classified by IEEE802.3at. FDMQ8205A
is configured with low r DS(on) dual P−ch MOSFETs and
N−ch MOSFETs so that it can reduce the power loss caused by the
voltage drop, compared to the conventional diode bridge.
FDMQ8205A enables the application to maximize the available
power and voltage and to eliminate the thermal design problems in
PoE PD applications.
FDMQ8205A GreenBridge 2 is compatible with IEEE802.3at PoE
standard by not compromising detection and classification
requirement as well as small backfeed voltage.


**Features**

- Low Power Loss GreenBridge Replaces Diode Bridge

- Self Driving Circuitry for MOSFETs

- Low r 100 V Rated MOSFETs
DS(on)

- Maximizing Available Power and Voltage

- Eliminating Thermal Design Problems

- IEEE802.3af/at and 3bt Compatible

 Meet Detection and Classification Requirement

 Work with 2 and 4−pair Architecture

 Small Backfeed Voltage

- Compact MLP 4.5x5 Package

- This is a Pb−Free Device


**Applications**

- Power over Ethernet (PoE) Power Device (PD)

- IP Phones

- Network Cameras

- Wireless Access Points

- Thin Clients

- Microcell

- Femtocell



**DATA SHEET**

**[www.onsemi.com](http://www.onsemi.com/)**


**WDFN12 5x4.5, 0.8P**
**CASE 511CS**


**MARKING DIAGRAM**


$Y&Z&2&K
FDMQ

8205A


FDMQ8205A = Specific Device Code
$Y = **onsemi** Logo
&Z = Assembly Plant Code
&2 = 2−Digit Data Code
&K = 2−Digits Lot Run Traceability Code


**ORDERING INFORMATION**


See detailed ordering and shipping information on page 9 of
this data sheet.



 Semiconductor Components Industries, LLC, 2016 **1** Publication Order Number:
**September, 2024 − Rev. 3** **FDMQ8205A/D**


**FDMQ8205A**


**TYPICAL APPLICATION**

















VOUT+


VOUT−

































**Figure 1. Typical Application of Power Device for 2−Pair Architecture of IEEE802.3af/at Power over Ethernet**
**Standard**


RJ45















VOUT+


VOUT−











































**Figure 2. Typical Application of Power Device for IEEE802.3bt Power over Ethernet Standard**


**TYPICAL BOM OF GATE DRIVING CIRCUITS**

|Reference|Description|Part Name|
|---|---|---|
|T1, T2, T3, T4|NPN & PNP Transistors|BC846BPDW1T1|
|D1, D2|Dual Common Anode Zeners|MMBZ27VALT1G|
|R1, R2|162 k Resistor|RC0603FR−07162KL|



**[www.onsemi.com](http://www.onsemi.com/)**


**2**


**FDMQ8205A**


**BLOCK DIAGRAM**






|OUTP|Col2|OUTP|
|---|---|---|
||||
















|G3|Col2|
|---|---|
|||
|G4||


|Col1|G2|
|---|---|
|||
||G1|








|OUTN|Col2|INPUT2|Col4|INPUT1|Col6|OUTN|
|---|---|---|---|---|---|---|
||||||||



**Figure 3. Block Diagram**


**[www.onsemi.com](http://www.onsemi.com/)**


**3**


**FDMQ8205A**


**PIN CONFIGURATION**



G4


OUTN


OUTN


G3


OUTP


OUTP











G1


OUTN


OUTN


G2


OUTP


OUTP









MLP 4.5x5


**Figure 4. Pin Assignment (Bottom View)**


**PIN DESCRIPTION**

|Pin No.|Name|Description|
|---|---|---|
|1|G1|Gate of Q1 N−ch MOSFET|
|4|G2|Gate of Q2 P−ch MOSFET|
|9|G3|Gate of Q3 P−ch MOSFET|
|12|G4|Gate of Q4 N−ch MOSFET|
|13, 14|INPUT1|Input1 of GreenBridge|
|15, 16|INPUT2|Input2 of GreenBridge|
|2, 3, 11, 10|OUTN|Negative Output of GreenBridge|
|5, 6, 7, 8|OUTP|Positive Output of GreenBridge|



1. Show the feature that provides orientation or pin 1 location.


**[www.onsemi.com](http://www.onsemi.com/)**


**4**


**FDMQ8205A**



**ABSOLUTE MAXIMUM RATINGS**













|Col1|Col2|Min|Max|Unit|
|---|---|---|---|---|
|INPUT1, INPUT2 to OUTN|INPUT1, INPUT2 to OUTN|−|100|V|
|OUTP to INPUT1, INPUT2|OUTP to INPUT1, INPUT2|−|100|V|
|INPUT1 to INPUT2|INPUT1 to INPUT2|−|100|V|
|INPUT2 to INPUT1|INPUT2 to INPUT1|−|100|V|
|OUTP to OUTN|OUTP to OUTN|−|100|V|
|G1, G2, G3, G4 to OUTN|G1, G2, G3, G4 to OUTN|−|70|V|
|OUTP to G1, G2, G3, G4|OUTP to G1, G2, G3, G4|−|70|V|
|VG_TRANSIENT|Transient Gate Voltage, Pulse Width < 200s,<br>Duty Cycle < 0.003%|−|100|V|
|Continuous IINPUT(GreenBridge Current,<br>Q1 + Q3 or Q2 + Q4)|TA= 25C (Note 2a)|−|3.0|A|
|Continuous IINPUT(GreenBridge Current,<br>Q1 + Q3 or Q2 + Q4)|TA= 25C (Note 2b)|−|1.7|A|
|Pulsed IINPUT(Q1 + Q3 or Q2 + Q4)|Pulse Width < 300s, Duty Cycle < 2% (Note 3)|−|58|A|
|PD (Power Dissipation, Q1 + Q3 or Q2 + Q4)|TA= 25C (Note 2a)|−|2.5|W|
|PD (Power Dissipation, Q1 + Q3 or Q2 + Q4)|TA= 25C (Note 2b)|−|0.78|W|
|Max Junction Temperature|Max Junction Temperature|−|150|C|


Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality
should not be assumed, damage may occur and reliability may be affected.
2. R � JA is determined with the device mounted on a 1 in [2] pad 2 oz copper pad on a 1.5 x 1.5 in. board of FR−4 material. R � JC is guaranteed
by design while R � CA is determined by the user’s board design.



a. 50C/W when mounted on a 1 in [2] pad of
2 oz copper, the board designed Q1 + Q3
or Q2 + Q4.


3. Pulse Id measured at td  300 � s, refer to SOA graph for more details.


**THERMAL CHARACTERISTICS**



b. 160C/W when mounted on a minimum

pad of 2 oz copper, the board designed
Q1 + Q3 or Q2 + Q4.



|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|RJC|Thermal Resistance, Junction to Case|−|5.1|−|C/W|
|RJA|Thermal Resistance, Junction to Ambient (Note 2a)|−|50|−|−|
|RJA|Thermal Resistance, Junction to Ambient (Note 2b)|−|160|−|−|


**[www.onsemi.com](http://www.onsemi.com/)**


**5**


**FDMQ8205A**


**RECOMMENDED OPERATING CONDITIONS**

|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|VINPUT|Input Voltage of Bridge|INPUT1 to INPUT2 or INPUT2 to INPUT1|−|57|V|
|VG|Gate Voltage of MOSFETs|G1, G4 to OUTN G2, G3 to OUTP|−|57|V|
|IINPUT|Input Current of Bridge|Bridge Current through Q2 and Q4 or (Q3 and Q1)|−|1.7|A|
|Ambient Operation Temperature (TA)|Ambient Operation Temperature (TA)|Ambient Operation Temperature (TA)|−40|85|C|
|Junction Operating Temperature (TJ) (Note 4)|Junction Operating Temperature (TJ) (Note 4)|Junction Operating Temperature (TJ) (Note 4)|−40|125|C|



Functional operation above the stresses listed in the Recommended Operating Ranges is not implied. Extended exposure to stresses beyond
the Recommended Operating Ranges limits may affect device reliability.
4. Backfeed Voltage can not be guaranteed for junction temperature in excess of 85C. See V BF in Electrical Characteristics Table.


**ELECTRICAL CHARACTERISTICS** (T J = 25C unless otherwise noted)













|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|VINPUT|Input Voltage of Bridge|At INPUT1 to INPUT2 or INPUT2 to INPUT1|−|−|57|V|
|VG|Gate Voltage of MOSFETs|At G1, G4 to OUTN and G2, G3 to OUTP|−|−|57|V|
|IQ|Quiescent Current|Detection Mode<br>1.5 V < VINPUT= VG < 10.1 V (Note 5)|−|−|5|A|
|IQ|Quiescent Current|Classification Mode<br>10.2 V < VINPUT= VG < 23.9 V (Note 5)|−|−|400|A|
|IQ|Quiescent Current|Power On Mode<br>Maximum VINPUT= VG = 57 V (Note 5)|−|−|3.2|mA|
|VTURN_ON|Turn−On Voltage of MOS-<br>FETs|Turn−On of MOSFETs while VG Increases<br>(Note 4)|32|−|36|V|
|ILEAKAGE|Turn−Off Leakage Current|VOUTP= 57 V, VOUTN= 0 V TJ = −40C to 85C<br>(Note 5)|−|−|700|A|
|VBF|Backfeed Voltage|VOUTP= 57 V, VOUTN= 0 V, 100 k between<br>INPUT1 and INPUT2<br>TJ = −40C to 85C (Note 5)|−|−|2.7|V|
|rDS(on)|N−ch MOSFET|VG = 42 V, IINPUT= 1.5 A, TA = 25C|−|35|51|m|
|rDS(on)|N−ch MOSFET|VG = 48 V, IINPUT= 1.5 A, TA = 25C|−|29|44|m|
|rDS(on)|N−ch MOSFET|VG = 57 V, IINPUT= 1.5 A, TA = 25C|−|26|37|m|
|rDS(on)|P−ch MOSFET|VG = −42 V, IINPUT= −1.5 A, TA = 25C|−|95|147|m|
|rDS(on)|P−ch MOSFET|VG = −48 V, IINPUT= −1.5 A, TA = 25C|−|83|125|m|
|rDS(on)|P−ch MOSFET|VG = −57 V, IINPUT = −1.5 A, TA = 25C|−|76|107|m|


Product parametric performance is indicated in the Electrical Characteristics for the listed test conditions, unless otherwise noted. Product
performance may not be indicated by the Electrical Characteristics if operated under different conditions.
5. INPUT1 is connected to G3 and G4 and also INPUT2 is connected to G1 and G2 like below.


**[www.onsemi.com](http://www.onsemi.com/)**


**6**


2.0


1.8


1.6


1.4


1.2


1.0


0.8



1


10 [−1]


10 [−2]


10 [−3]


10 [−4]





**FDMQ8205A**


**TYPICAL CHARACTERISTICS (Q1 OR Q4 N−CHANNEL)**

(T J = 25C unless otherwise noted.)


10 [2]


10







0.6

|I<br>D<br>V<br>G|= 1.7<br>= 5<br>S|A<br>7 V|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

−75 −50 −25 0 25 50 75 100 125 150


T J, JUNCTION TEMPERATURE (C)



10 [−5]

|V =<br>GS|0 V|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
|~~TJ =~~|~~150C~~||||
||||~~TJ~~|~~ 25C~~|
||||||
||||||
||||||
||||||
||||||
||||~~J = −55~~||
||||||
||||||
||||||

0.2 0.4 0.6 0.8 1.0 1.2


V SD, BODY DIODE FORWARD VOLTAGE (V)



**Figure 5. Normalized On Resistance vs.** **Figure 6. Source to Drain Diode Forward Voltage**
**Junction Temperature** **vs. Source Current**



10 [−1]

10 [−2]

10 [−3]

10 [−5]

10 [−6]

10 [−8]

10 [−9]

|V<br>DS|= 0 V|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|~~TJ =~~|~~125C~~||||||
||||||||
||||||||
||~~TJ =~~|~~25C~~|||||
||||||||
||||||||

0 10 20 30 40 50 60









V GS, GATE TO SOURCE VOLTAGE (V)


**Figure 7. Gate Leakage Current vs.**
**Gate to Source Voltage**



70


**[www.onsemi.com](http://www.onsemi.com/)**


**7**


1.8


1.6


1.4


1.2


1.0


0.8



1


10 [−1]


10 [−2]


10 [−3]


10 [−4]





**FDMQ8205A**


**TYPICAL CHARACTERISTICS (Q2 OR Q3 P−CHANNEL)**

(T J = 25C unless otherwise noted.)


10 [2]


10







0.6

|I =<br>D<br>V<br>GS|−1.7<br>= −5|A<br>7 V|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

−75 −50 −25 0 25 50 75 100 125 150


T J, JUNCTION TEMPERATURE (C)



10 [−5]

|V =<br>GS|0 V|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
|~~TJ =~~|~~150C~~||||
||||~~TJ~~|~~ 25C~~|
||||||
||||||
||||||
||||||
||||~~J = −55~~||
||||||
||||||
||||||

0.2 0.4 0.6 0.8 1.0 1.2


−V SD, BODY DIODE FORWARD VOLTAGE (V)



**Figure 8. Normalized On Resistance vs.** **Figure 9. Source to Drain Diode Forward Voltage**
**Junction Temperature** **vs. Source Current**



10 [−1]

10 [−2]

10 [−3]

10 [−5]

10 [−6]

10 [−8]

10 [−9]

|V<br>DS|= 0 V|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|~~TJ =~~|~~125C~~||||||
||||||||
||||||||
||~~TJ =~~|~~25C~~|||||
||||||||
||||||||

0 10 20 30 40 50 60









−V GS, GATE TO SOURCE VOLTAGE (V)


**Figure 10. Gate Leakage Current vs.**
**Gate to Source Voltage**



70


**[www.onsemi.com](http://www.onsemi.com/)**


**8**


**FDMQ8205A**


**TYPICAL CHARACTERISTICS (Q1 + Q3 OR Q2 + Q4 IN SERIAL)**

(T J = 25C unless otherwise noted.)





100


10


1


0.1


0.01







2000

1000


100


10


1



0.001

|Col1|Col2|Col3|Col4|Col5|Col6|1 ms|
|---|---|---|---|---|---|---|
||~~S~~<br>~~T~~<br>~~R~~|~~ING~~<br>~~J =~~<br>|~~LE P~~<br>~~MAX~~<br>~~ = 16~~|~~U~~<br>~~R~~<br>~~~~|~~LSE~~<br>~~ATED~~<br>~~C/W~~|~~DC~~<br>~~10 s~~<br>~~10 m~~<br>~~1 s~~<br>~~100~~<br>|
||~~T~~|~~JA~~<br>~~A =~~|~~ 25C~~||||

0.01 0.1 1 10 100 400


V DS, DRAIN TO SOURCE VOLTAGE (V)



0.1

|0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||~~SI~~<br>~~R~~|~~NG~~<br>|~~LE~~<br>~~= 1~~|~~PUL~~<br>~~0C~~|~~SE~~<br>~~/~~||||||
|||~~TA~~|~~JA~~<br>~~ =~~|~~25~~|~~C~~|||||||

10 [−4] 10 [−3] 10 [−2] 10 [−1] 1 10 10 [2] 10 3


t, PULSE WIDTH (sec)



**Figure 11. Forward Bias Safe Operating Area** **Figure 12. Single Pulse Maximum Power**
**Dissipation**



2


1


10 [−1]


10 [−2]


10 [−3]







10 [−4]

|D|U|TY CYCLE−DE|SCENDING OR|DE|R|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|~~D~~|~~ =~~|~~ 0.5~~|||||||||||||||||||||
||||||||||||||||||||||||
||<br> <br>|~~0.2~~<br>~~ 0.1~~<br>|||||||||||||||||~~PDM~~||||
||<br>|~~ 0.05~~<br>|||||||||||||||||||||
||<br>|~~0.02~~<br>~~ 0.01~~||||||||||||||||||~~t ~~1<br>~~t~~|||
||<br>|~~0.02~~<br>~~ 0.01~~||||||||||||||||||~~t ~~1<br>~~t~~|||
|||||||||||||||||||||~~ 2~~|||
||||||||||||||||||||||||
||||||||||||||||||||||||
|||~~SINGLE~~|~~ULSE~~||||||||||||||~~ZJ~~<br>~~RJ~~|~~ (t)~~<br>~~ =~~|~~= r(t)~~<br>~~160C~~|~~ RJA~~<br>~~/W~~|||
||||||||||||||||||~~DU~~|~~Y~~|~~ACT~~|~~R: D =~~|~~t /~~|~~t~~|
||||||||||||||||||||||||
||||||||||||||||||~~T~~|~~ T~~|~~= P~~|~~ x Z~~|~~(t)~~||
||||||||||||||||||~~J~~|~~A~~|~~D~~|~~JA~~|||

10 [−4] 10 [−3] 10 [−2] 10 [−1] 1 10 100 1000


t, RECTANGULAR PULSE DURATION (sec)


**Figure 13. Junction−to−Ambient Transient Thermal Response Curve**


**PACKEGE MARKING AND ORDERING INFORMATION**






|Device Marking|Device|Package|Reel Size|Tape Width|Shipping†|
|---|---|---|---|---|---|
|FDMQ8205A|FDMQ8205A|WDFN12 5x4.5, 0.8P<br>MLP4.5x5<br>(Pb−Free)|13”|12 mm|3000 / Tape & Reel|




- For information on tape and reel specifications, including part orientation and tape sizes, please refer to our Tape and Reel Packaging
Specifications Brochure, BRD8011/D.


GreenBridge is trademarks of Semiconductor Components Industries, LLC dba “ **onsemi** ” or its affiliates and/or subsidiaries in the United States and/or other
countries.


**[www.onsemi.com](http://www.onsemi.com/)**


**9**


MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**


**WDFN12 5x4.5, 0.8P**
CASE 511CS

ISSUE O

DATE 31 AUG 2016



|5.00 A<br>0.10 C<br>2X B<br>4.50<br>PIN#1<br>AREA<br>0.10 C|Col2|Col3|Col4|
|---|---|---|---|
|A<br>B<br>0.10 C<br>0.10 C<br>2X<br>PIN#1<br> AREA<br>4.50<br>5.00||0.10|C|


2X





IDENT AREA

|0.10 C|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|0.10 C||0.10|0.10|C|C|C|C|C|
|0.10 C||0.10|0.10|C|||||
|0.10 C||0.10|0.10|C|||||
||0.08|0.08|C|C|C|C|C|C|



0.05



|Col1|Col2|
|---|---|
|||



6





3.50


|Col1|4|
|---|---|
||12<br>(0.40)<br><br>(0.25)|
|(4X)||





1.00(4X)


(0.50)2X


(0.65)





4.45


(0.40) 2.10(4X)


(12x)





TOP VIEW



(0.20)







RECOMMENDED LAND PATTERN


NOTES:

A. PACKAGE DOES NOT FULLY CONFORM TO

JEDEC MO−229 REGISTRATION

B. DIMENSIONS ARE IN MILLIMETERS.

C. DIMENSIONS AND TOLERANCES PER

ASME Y14.5M, 1994.




|Col1|0.10|C|A|B|
|---|---|---|---|---|
||0.05|C|||





(0.50)2X


(0.50)2X


0.55
0.45


0.35
0.25 [(12X)]

|SEATING PLANE 0.05 0.00|SIDE VIEW 5.00±0.05|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|6<br>1<br>1.95<br>1.85(4X)<br>5.00±0.05|
|PIN#1<br>IDENT<br>1.05<br>0.95(4X)<br><br>±0.05||||||||||
|PIN#1<br>IDENT<br>1.05<br>0.95(4X)<br><br>±0.05||||||||||
|PIN#1<br>IDENT<br>1.05<br>0.95(4X)<br><br>±0.05||||||||||
|PIN#1<br>IDENT<br>1.05<br>0.95(4X)<br><br>±0.05||||||||||
|PIN#1<br>IDENT<br>1.05<br>0.95(4X)<br><br>±0.05||||||||||
|12|12|12|12|0.80<br>2.40|0.80<br>2.40|0.80<br>2.40|0.80<br>2.40|0.80<br>2.40|0.80<br>2.40|



BOTTOM VIEW










|DOCUMENT NUMBER:|98AON13607G|Electronic versions are uncontrolled except when accessed directly from the Document Repository.<br>Printed versions are uncontrolled except when stamped “CONTROLLED COPY” in red.|Col4|
|---|---|---|---|
|**DESCRIPTION:**|**WDFN12 5X4.5, 0.8P**|**WDFN12 5X4.5, 0.8P**|**PAGE 1 OF 1**|





© Semiconductor Components Industries, LLC, 2016 www.onsemi.com


**ADDITIONAL INFORMATION**


**TECHNICAL PUBLICATIONS** :
**Technical Library:** [www.onsemi.com/design/resources/technical−documentation](https://www.onsemi.com/design/resources/technical-documentation)
**onsemi Website:** [www.onsemi.com](https://www.onsemi.com/)






**ONLINE SUPPORT** : [www.onsemi.com/support](https://www.onsemi.com/support?utm_source=techdocs&utm_medium=pdf)
**For additional information, please contact your local Sales Representative at**
[www.onsemi.com/support/sales](https://www.onsemi.com/support/sales)


