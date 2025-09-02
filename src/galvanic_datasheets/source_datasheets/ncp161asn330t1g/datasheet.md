# LDO Regulator for RF and Analog Circuits - Ultra-Low Noise and High PSRR

## 450 mA

# NCP161

The NCP161 is a linear regulator capable of supplying 450 mA
output current. Designed to meet the requirements of RF and analog
circuits, the NCP161 device provides low noise, high PSRR, low
quiescent current, and very good load/line transients. The device is
designed to work with a 1 �F input and a 1 �F output ceramic capacitor.
It is available in two thickness ultra−small 0.35P, 0.64 mm x 0.64 mm
Chip Scale Package (CSP) and XDFN4 0.65P, 1 mm x 1 mm.


**Features**

- Operating Input Voltage Range: 1.9 V to 5.5 V

- Available in Fixed Voltage Option: 1.8 V to 5.14 V

- ±2% Accuracy Over Load/Temperature

- Ultra Low Quiescent Current Typ. 18 �A

- Standby Current: Typ. 0.1 �A

- Very Low Dropout: 150 mV at 450 mA

- Ultra High PSRR: Typ. 98 dB at 20 mA, f = 1 kHz

- Ultra Low Noise: 10 �V RMS

- Stable with a 1 �F Small Case Size Ceramic Capacitors

- Available in −WLCSP4 0.64 mm x 0.64 mm x 0.4 mm

−WLCSP4 0.64 mm x 0.64 mm x 0.33 mm

−XDFN4 1 mm x 1 mm x 0.4 mm

−SOT23−5 2.9 mm x 2.8 mm x 1.2 mm

- These Devices are Pb−Free and are RoHS Compliant


**Typical Applications**

- Battery−powered Equipment

- Wireless LAN Devices

- Smartphones, Tablets

- Cameras, DVRs, STB and Camcorders



**WLCSP4**

**CASE 567JZ**


1


**XDFN4**

**CASE 711AJ**



**DATA SHEET**

**[www.onsemi.com](http://www.onsemi.com/)**


**WLCSP4**

**CASE 567KA**


1


**SOT23−5**

**CASE 527AH**



**MARKING DIAGRAMS**



A1



A1



XX M


1

|Col1|XXX M|Col3|
|---|---|---|
||XXX M||



X, XX, XXX = Specific Device Code
M = Date Code


**PIN CONNECTIONS** (Top Views)



OUT


NC



IN


GND


EN

|Col1|Col2|5<br>1<br>2<br>3 4|
|---|---|---|
||||
||||
||||
||||
||||
||||



IN OUT



IN







EN









GND



EN GND



OUT



**ORDERING INFORMATION**


See detailed ordering and shipping information on page 17 of
this data sheet.


© Semiconductor Components Industries, LLC, 2017 **1** Publication Order Number:
**May, 2024 − Rev. 20** **NCP161/D**


**NCP161**



V IN



V OUT



















**Figure 1. Typical Application Schematics**



**IN**















**OUT**





**GND**


**PIN FUNCTION DESCRIPTION**



**Figure 2. Simplified Schematic Block Diagram**











|Pin No.<br>CSP4|Pin No.<br>SOT23−5|Pin No.<br>XDFN4|Pin<br>Name|Description|
|---|---|---|---|---|
|A1|1|4|IN|Input voltage supply pin|
|A2|5|1|OUT|Regulated output voltage. The output should be bypassed with small 1F ceramic capacitor.|
|B1|3|3|EN|Chip enable: Applying VEN < 0.4 V disables the regulator, Pulling VEN > 1.2 V enables the LDO.|
|B2|2|2|GND|Common ground connection|
|−|−|EPAD|EPAD|Expose pad should be tied to ground plane for better power dissipation|


**[www.onsemi.com](http://www.onsemi.com/)**


**2**


**NCP161**


**ABSOLUTE MAXIMUM RATINGS**

|Rating|Symbol|Value|Unit|
|---|---|---|---|
|Input Voltage (Note 1)|VIN|−0.3 V to 6|V|
|Output Voltage|VOUT|−0.3 to VIN + 0.3, max. 6|V|
|Chip Enable Input|VCE|−0.3 to 6|V|
|Output Short Circuit Duration|tSC|unlimited|s|
|Maximum Junction Temperature|TJ|150|°C|
|Storage Temperature|TSTG|−55 to 150|°C|
|ESD Capability, Human Body Model (Note 2)|ESDHBM|2000|V|
|ESD Capability, Machine Model (Note 2)|ESDMM|200|V|



Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality
should not be assumed, damage may occur and reliability may be affected.
1. Refer to ELECTRICAL CHARACTERISTIS and APPLICATION INFORMATION for Safe Operating Area.
2. This device series incorporates ESD protection and is tested by the following methods:
ESD Human Body Model tested per EIA/JESD22−A114
ESD Machine Model tested per EIA/JESD22−A115
Latchup Current Maximum Rating tested per JEDEC standard: JESD78.


**THERMAL CHARACTERISTICS**







|Rating|Symbol|Value|Unit|
|---|---|---|---|
|Thermal Characteristics, CSP4 (Note 3)<br>Thermal Resistance, Junction−to−Air|RJA|108|°C/W|
|Thermal Characteristics, XDFN4 (Note 3)<br>Thermal Resistance, Junction−to−Air|Thermal Characteristics, XDFN4 (Note 3)<br>Thermal Resistance, Junction−to−Air|198.1|198.1|
|Thermal Characteristics, SOT23−5 (Note 3)<br>Thermal Resistance, Junction−to−Air|Thermal Characteristics, SOT23−5 (Note 3)<br>Thermal Resistance, Junction−to−Air|218|218|


3. Measured according to JEDEC board specification. Detailed description of the board can be found in JESD51−7


**[www.onsemi.com](http://www.onsemi.com/)**


**3**


**NCP161**


**ELECTRICAL CHARACTERISTICS** noted. V EN = 1.2 V. Typical values are at T −40 J = +25 ° C ≤° TC (Note 4). J ≤ 125 ° C; V IN = V OUT(NOM) + 1 V; I OUT = 1 mA, C IN = C OUT = 1 � F, unless otherwise










































































|Parameter|Test Conditions|Col3|Symbol|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|Operating Input Voltage|||VIN|1.9||5.5|V|
|Output Voltage Accuracy|VIN = VOUT(NOM)+ 1 V<br>0 mA≤ IOUT ≤ 450 mA|WLCSP4, XDFN4|VOUT|−2||+2|%|
|Output Voltage Accuracy|VIN = VOUT(NOM) + 1 V|SOT23−5|SOT23−5|−2||+2|+2|
|Line Regulation|VOUT(NOM) + 1 V≤ VIN ≤ 5.5 V|VOUT(NOM) + 1 V≤ VIN ≤ 5.5 V|LineReg||0.02||%/V|
|Load Regulation|IOUT = 1 mA to 450 mA<br>WLCSP4, XDFN4|WLCSP4, XDFN4|LoadReg||0.001||%/mA|
|Load Regulation|IOUT = 1 mA to 450 mA<br>WLCSP4, XDFN4|SOT23−5|SOT23−5||0.005|0.008|0.008|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 1.8 V|VDO||300|450|mV|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 1.85 V|VOUT(NOM) = 1.85 V||290|393|393|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 2.5 V|VOUT(NOM) = 2.5 V||190|315|315|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 2.8 V|VOUT(NOM) = 2.8 V||175|290|290|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 2.85 V|VOUT(NOM) = 2.85 V||170|290|290|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 3.0 V|VOUT(NOM) = 3.0 V||165|275|275|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 3.3 V|VOUT(NOM) = 3.3 V||160|260|260|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 3.5 V|VOUT(NOM) = 3.5 V||150|255|255|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 4.5 V|VOUT(NOM) = 4.5 V||120|210|210|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 5.0 V|VOUT(NOM) = 5.0 V||105|190|190|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>WLCSP4, XDFN4|VOUT(NOM) = 5.14 V|VOUT(NOM) = 5.14 V||105|185|185|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>SOT23−5|VOUT(NOM) = 1.8 V|VDO||365|480|mV|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>SOT23−5|VOUT(NOM) = 2.8 V|VOUT(NOM) = 2.8 V||260|345|345|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>SOT23−5|VOUT(NOM) = 3.0 V|VOUT(NOM) = 3.0 V||240|330|330|
|Dropout Voltage (Note 5)|IOUT = 450 mA<br>SOT23−5|VOUT(NOM) = 3.3 V|VOUT(NOM) = 3.3 V||225|305|305|
|Output Current Limit|VOUT = 90% VOUT(NOM)|VOUT = 90% VOUT(NOM)|ICL|450|700||mA|
|Short Circuit Current|VOUT = 0 V|VOUT = 0 V|ISC||690|||
|Quiescent Current|IOUT = 0 mA|IOUT = 0 mA|IQ||18|23|A|
|Shutdown Current|VEN ≤ 0.4 V, VIN = 4.8 V|VEN ≤ 0.4 V, VIN = 4.8 V|IDIS||0.01|1|A|
|EN Pin Threshold Voltage|EN Input Voltage “H”|EN Input Voltage “H”|VENH|1.2|||V|
|EN Pin Threshold Voltage|EN Input Voltage “L”|EN Input Voltage “L”|VENL|||0.4|0.4|
|EN Pull Down Current|VEN = 4.8 V|VEN = 4.8 V|IEN||0.2|0.5|A|
|Turn−On Time|COUT = 1F, From assertion of VENto<br>VOUT= 95% VOUT(NOM)|COUT = 1F, From assertion of VENto<br>VOUT= 95% VOUT(NOM)|||120||s|
|Power Supply Rejection Ratio|IOUT = 20 mA|f = 100 Hz<br>f = 1 kHz<br>f = 10 kHz<br>f = 100 kHz|PSRR||91<br>98<br>82<br>48||dB|
|Output Voltage Noise|f = 10 Hz to 100 kHz|IOUT= 1 mA<br>IOUT= 250 mA|VN||14<br>10||VRMS|
|Thermal Shutdown Threshold|Temperature rising|Temperature rising|TSDH||160||°C|
|Thermal Shutdown Threshold|Temperature falling|Temperature falling|TSDL||140||°C|
|Active output discharge resistance|VEN < 0.4 V, Version A only|VEN < 0.4 V, Version A only|RDIS||280|||
|Line transient (Note 6)|VIN = (VOUT(NOM) + 1 V) to (VOUT(NOM) + 1.6 V)<br>in 30s, IOUT = 1 mA|VIN = (VOUT(NOM) + 1 V) to (VOUT(NOM) + 1.6 V)<br>in 30s, IOUT = 1 mA|TranLINE|−1|||mV|
|Line transient (Note 6)|VIN= (VOUT(NOM) + 1.6 V) to (VOUT(NOM) + 1 V)<br>in 30s, IOUT = 1 mA|VIN= (VOUT(NOM) + 1.6 V) to (VOUT(NOM) + 1 V)<br>in 30s, IOUT = 1 mA|VIN= (VOUT(NOM) + 1.6 V) to (VOUT(NOM) + 1 V)<br>in 30s, IOUT = 1 mA|||+1|+1|
|Load transient (Note 6)|IOUT = 1 mA to 450 mA in 10s|IOUT = 1 mA to 450 mA in 10s|TranLOAD|−40|||mV|
|Load transient (Note 6)|IOUT = 450 mA to 1mA in 10s|IOUT = 450 mA to 1mA in 10s|IOUT = 450 mA to 1mA in 10s|||+40|+40|



Product parametric performance is indicated in the Electrical Characteristics for the listed test conditions, unless otherwise noted. Product
performance may not be indicated by the Electrical Characteristics if operated under different conditions.
4. Performance guaranteed over the indicated operating temperature range by design and/or characterization. Production tested at T A = 25 ° C.
Low duty cycle pulse techniques are used during the testing to maintain the junction temperature as close to ambient as possible.
5. Dropout voltage is characterized when V OUT falls 100 mV below V OUT(NOM) .
6. Guaranteed by design.


**[www.onsemi.com](http://www.onsemi.com/)**


**4**


1.820


1.815


1.810


1.805


1.800


1.795


1.790


1.785





**NCP161**


**TYPICAL CHARACTERISTICS**


2.520





2.515


2.510


2.505


2.500


2.495


2.490


2.485





1.780

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||||~~IOU~~|~~T = 10~~|~~mA~~|||
||||||||||
|||||IOU|T = 45|0 mA|||
||||||||||
|||||||VIN<br>|= 2.8<br>|V<br>|
|||||||~~V~~O<br>CI<br>|UT~~ = 1~~<br> = 1<br>|~~.8 V~~<br>F<br>|
|||||||~~C~~O|UT~~ = 1~~|~~F~~|

−40 −20 0 20 40 60 80 100 120 140



2.480

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||IOU|T = 10|mA||||
||||||||||
||||IOU|T = 45|0 mA||||
||||||||||
|||||||VIN<br>|= 3.5<br>|V<br>|
|||||||~~V~~O<br>CI|UT~~ = 2~~<br> = 1|~~.5 V~~<br>F|
|||||||CO|UT = 1|F|

−40 −20 0 20 40 60 80 100 120 140



3.33


3.32


3.31


3.30


3.29


3.28


3.27


3.26



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 3. Output Voltage vs. Temperature −** **Figure 4. Output Voltage vs. Temperature −**
**V** **OUT** **= 1.8 V − XDFN Package** **V** **OUT** **= 2.5 V − XDFN Package**


3.35


3.34


3.33









3.31


3.30


3.29


3.28



3.25

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|||I~~OU~~|= 10|mA|||||
||||||||||
|||I~~OUT~~|= 450|mA|||||
|||||||VIN<br>|= 4.3<br>|V<br>|
|||||||~~V~~OU<br>C~~IN~~|T~~ = 3.~~<br> = 1F|~~3 V~~<br>|
|||||||CO|UT = 1|F|



−40 −20 0 20 40 60 80 100 120



3.27

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||I~~OU~~|~~T~~ = 10|mA an|d 450|mA||||
||||||||||
||||||||||
|||||||VIN<br>|= 4.3<br>|V<br>|
|||||||~~V~~O<br>CIN|UT~~ = 3.~~<br> = 1|~~3 V~~<br>F|
|||||||CO|UT = 1|F|



−40 −20 0 20 40 60 80 100 120



60 80 100 120 140 −40 −20 0 20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 5. Output Voltage vs. Temperature −** **Figure 6. Output Voltage vs. Temperature −**
**V** **OUT** **= 3.3 V − XDFN Package** **V** **OUT** **= 3.3 V − CSP Package**



5.19


5.18


5.17


5.16


5.15


5.14


5.13


5.12









0.010


0.009


0.008


0.007


0.006


0.005


0.004


0.003


0.002



5.11

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|||IOU|T = 10|mA|||||
||||||||||
|||IOUT|= 450|mA|||||
|||||||VIN <br>|= 5.5<br>|V<br>|
|||||||~~V~~OU<br>C~~IN~~|T~~ = 5.~~<br>= 1F|~~4 V~~<br>|
|||||||COU|T = 1|F|

−40 −20 0 20 40 60 80 100 120 140



0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||||~~V~~|~~ = 2.8~~|~~V~~|
|||||||~~IN~~<br>VO<br>|UT = 1<br>|.8 V<br>|
|||||||~~C~~IN<br>|~~ = 1~~<br>|~~F~~<br>|
|||||||~~CO~~|~~UT = 1~~|~~F~~|

−40 −20 0 20 40 60 80 100 120



40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 7. Output Voltage vs. Temperature −** **Figure 8. Line Regulation vs. Temperature −**
**V** **OUT** **= 5.14 V − XDFN Package** **V** **OUT** **= 1.8 V**


**[www.onsemi.com](http://www.onsemi.com/)**


**5**


0.010


0.009


0.008


0.007


0.006


0.005


0.004


0.003


0.002



**NCP161**


**TYPICAL CHARACTERISTICS**


0.020





0.012


0.010


0.008


0.006


0.004



0.001

0

|Col1|Col2|Col3|Col4|Col5|Col6|V|= 4.3|V|
|---|---|---|---|---|---|---|---|---|
|||||||~~IN~~<br>VO|UT = 3.|3 V|
|||||||CIN<br>|= 1<br>|F<br>|
|||||||~~CO~~|~~UT = 1~~|~~F~~|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

−40 −20 0 20 40 60 80 100 120 140



0.002

0

|Col1|Col2|Col3|Col4|Col5|Col6|V|= 5.5|V|
|---|---|---|---|---|---|---|---|---|
|||||||~~IN~~<br>VO|T = 5.|14 V|
|||||||CIN<br>|= 1F<br>||
|||||||~~CO~~|~~UT = 1~~|~~F~~|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

−40 −20 0 20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 9. Line Regulation vs. Temperature −** **Figure 10. Line Regulation vs. Temperature −**
**V** **OUT** **= 3.3 V** **V** **OUT** **= 5.14 V**



0.0020


0.0018


0.0016


0.0014


0.0012


0.0010


0.0008


0.0006


0.0004


0.0002







0.0020


0.0018


0.0016


0.0014


0.0012


0.0010


0.0008


0.0006


0.0004



0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||~~VI~~|~~ = 2.8~~|~~ V, VO~~|~~T = 1~~|~~8 V~~|
|||||CI<br>|N = 1<br>|F, COU<br>|T = 1<br>|F<br>|
|||||~~I~~O|UT~~ = 1~~|~~mA to~~|~~450 m~~|~~A~~|



−40 −20 0 20 40 60 80 100 120 140



0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||V|~~IN~~ = 4|3 V, V|~~OUT~~ =|3.3 V|
|||||C<br>|IN = 1<br>|F, CO<br>|UT = 1<br>|F<br>|
|||||~~I~~|OUT~~ =~~|~~1 mA t~~|~~o 450~~|~~mA~~|



−40 −20 0 20 40 60 80 100 120



40 60 80 100 120 140



0.0020


0.0018


0.0016


0.0014


0.0012


0.0010


0.0008


0.0006


0.0004



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 11. Load Regulation vs. Temperature −** **Figure 12. Load Regulation vs. Temperature −**
**V** **OUT** **= 1.8 V (WLCSP4)** **V** **OUT** **= 3.3 V (WLCSP4)**


70





60


50


40


30


20


10





0.0002

0

|V<br>IN|= 5.5|V, C<br>OU|= 1<br>T|F|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|VO<br>|UT = 5.<br>|14 V,<br>|CIN = 1<br>|F<br>|||||
|~~I~~OU|T~~ = 1~~|~~mA to~~|~~50 m~~||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

−40 −20 0 20 40 60 80 100 120 140



0

|I<br>OUT<br>C =|= 1 m<br>1 F|A to 45|0 mA|Col5|SOT|23−5 P|ackag|e|
|---|---|---|---|---|---|---|---|---|
|~~IN~~|||||||||
||||||||||
||||||||||
||||||XDF|N4 Pa|ckage||
||||||||||
||||||~~WLC~~|~~SP4 P~~|~~ackag~~|~~e~~|

−40 −20 0 20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 13. Load Regulation vs. Temperature −** **Figure 14. Load Regulation vs. Temperature**
**V** **OUT** **= 5.14 V (WLCSP4)**


**[www.onsemi.com](http://www.onsemi.com/)**


**6**


2.0


1.8


1.6


1.4


1.2


1.0


0.8


0.6


0.4



**NCP161**


**TYPICAL CHARACTERISTICS**





0.2

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||~~T~~|~~ = 12~~|~~°C~~||
|||||||~~J~~<br>||||
|||||~~TJ~~|~~ 25°~~|||||
|||||||||||
||||||||~~T~~|~~ = −4~~|~~0°C~~|
|||||||||||
||||||||~~V~~IN<br>~~V~~|~~ = 2.8~~<br>~~ = 1~~|~~ V~~<br>~~.8 V~~|
||||||||~~O~~<br>CIN<br>|~~T~~<br> = 1<br>|F<br>|
||||||||~~C~~O|UT~~ = 1~~|~~F~~|

0 50 100 150 200 250 300 350 400 450



100 150 200 250 300 350 400 450 500



I OUT, OUTPUT CURRENT (mA)


**Figure 15. Ground Current vs. Load Current −**
**V** **OUT** **= 1.8 V**



2.0


1.8


1.6


1.4


1.2


1.0


0.8


0.6


0.4













2.50


2.25


2.00


1.75


1.50


1.25


1.00


0.75


0.50



0.2

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||~~T~~|~~ = 12~~|~~C~~||
|||||||~~J~~||~~°~~||
|||||TJ = 2|5°C|||||
|||||||||||
|||||||||||
|||||||~~T~~|J~~ = −4~~|~~0°C~~||
||||||||~~V~~IN<br>~~V~~|~~ = 4.3~~<br>~~ = 3~~|~~ V~~<br>~~.3 V~~|
||||||||~~O~~<br>CIN|~~UT~~<br> = 1|F|
||||||||CO|UT = 1|F|

0 50 100 150 200 250 300 350 400 450


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||TJ|= 125|°C||
|||||||||||
||||||||T|J = 2|5°C|
|||||||||||
|||||||||||
||||||||~~T~~|J~~ = −~~|~~0~~°~~C~~|
||||||||~~V~~IN <br>~~V~~|~~= 5.5~~<br>~~ = 5.~~|~~V~~<br>~~14 V~~|
||||||||~~OU~~<br>CIN <br>|~~T~~<br>= 1F<br>||
||||||||~~C~~OU|T~~ = 1~~|~~F~~|



200 250 300 350 400 450 500



0.25

0
0 50 100 150 200 250 300 350 400 450



150 200 250 300 350 400 450 500



400


360


320


280


240


200


160


120


80



I OUT, OUTPUT CURRENT (mA) I OUT, OUTPUT CURRENT (mA)


**Figure 16. Ground Current vs. Load Current −** **Figure 17. Ground Current vs. Load Current −**
**V** **OUT** **= 3.3 V** **V** **OUT** **= 5.14 V**


225











200


175


150


125


100


75


50


25



40

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||TJ|= 125|°C||
|||||||||||
|||||~~J = 2~~|~~°C~~|||||
|||||||||||
||||||||~~T~~|J~~ = −4~~|~~0~~°~~C~~|
|||||||||||
||||||||~~V~~|~~ = 1~~|~~8 V~~|
||||||||~~O~~<br>CIN|~~T~~<br> = 1|F|
||||||||~~C~~O|UT~~ = 1~~|~~F~~|



0 50 100 150 200 250 300 350 400 450


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||~~T~~|~~J = 12~~|~~5°C~~||
|||||||||TJ =|25°C|
|||||||||||
|||||||||||
||||||||~~T~~|J~~ = −4~~|~~0°C~~|
|||||||||||
||||||||~~VO~~<br>CIN<br>|~~T = 3~~<br> = 1<br>|~~3 V~~<br>F<br>|
||||||||CO|UT = 1|F|



250 300 350 400 450 500



0

0 50 100 150 200 250 300 350 400 450 500



I OUT, OUTPUT CURRENT (mA) I OUT, OUTPUT CURRENT (mA)


**Figure 18. Dropout Voltage vs. Load Current −** **Figure 19. Dropout Voltage vs. Load Current −**
**V** **OUT** **= 1.8 V** **V** **OUT** **= 3.3 V**


**[www.onsemi.com](http://www.onsemi.com/)**


**7**


**NCP161**


**TYPICAL CHARACTERISTICS**



150


135


120


105


90


75


60


45


30











400


360


320


280


240


200


160


120


80



0

|Col1|Col2|Col3|Col4|Col5|Col6|T<br>J|= 12|5°C|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||TJ =|25°C|
|||||||||||
|||||||||||
||||||||~~T~~|J~~ = −~~|~~40~~°~~C~~|
|||||||||||
||||||||V~~OU~~|~~T~~ = 5|.14 V|
||||||||CIN <br>|= 1<br>|F<br>|
||||||||~~C~~OU|T~~ = 1~~|~~F~~|

0 50 100 150 200 250 300 350 400 450


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||~~I~~OU|T~~ = 45~~|~~ mA~~||||||
||||||||||
|||||||V~~O~~|~~UT~~ = 1.|8 V|
|||||||CIN<br>|= 1<br>|F<br>|
|||||||~~C~~O|UT~~ = 1~~|~~F~~|
||||||||||
||IO|UT = 0|mA||||||
||||||||||



150 200 250 300 350 400 450 500



40

0
−40 −20 0 20 40 60 80 100 120 140



I OUT, OUTPUT CURRENT (mA) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 20. Dropout Voltage vs. Load Current −** **Figure 21. Dropout Voltage vs. Temperature−**
**V** **OUT** **= 5.14 V** **V** **OUT** **= 1.8 V**





250


225


200


175


150


125


100


75


50









150


135


120


105


90


75


60


45


30



25

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||||||I~~OUT~~|= 450|mA|
||||||||||
||||||||||
||||||||||
||||||||||
|||||||I~~OU~~|~~T~~ = 0 m|A|
||||||||||
|||||||~~VO~~<br>C~~I~~|~~UT = 3~~<br> = 1|~~3 V~~<br>F|
|||||||CO|UT = 1|F|

−40 −20 0 20 40 60 80 100 120


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
|||||||~~IOUT~~|~~= 450~~|~~mA~~|
||||||||||
|||||||~~IOU~~|~~T = 0~~|~~A~~|
||||||||||
||||||||||
|||||||V~~O~~|~~T~~ = 5.|14 V|
|||||||CIN <br>|= 1F<br>||
|||||||~~C~~OU|T~~ = 1~~|~~F~~|



40 60 80 100 120 140



0
−40 −20 0 20 40 60 80 100 120



20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 22. Dropout Voltage vs. Temperature−** **Figure 23. Dropout Voltage vs. Temperature−**
**V** **OUT** **= 3.3 V** **V** **OUT** **= 5.14 V**



500


450


400


350


300


250


200


150


100







0

|Col1|Col2|Col3|Col4|S|OT23−5|Pack|age|Col9|
|---|---|---|---|---|---|---|---|---|
|~~XD~~|~~FN4 P~~|~~ackag~~|~~e~~||||||
||||||||||
||||||||||
||||||~~WLC~~|~~P4 P~~|~~ckage~~||
||||||||||
||||||||||
|||||||I~~OUT~~|= 450|mA|
|||||||CIN =<br>|1F<br>||
|||||||~~COU~~|~~T = 1~~|~~F~~|

−40 −20 0 20 40 60 80 100 120



40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C)


**Figure 24. Dropout Voltage vs. Temperature**
**V** **OUT** **= 1.8 V**


**[www.onsemi.com](http://www.onsemi.com/)**


**8**


**NCP161**


**TYPICAL CHARACTERISTICS**



750


740


730


720


710


700


690


680


670


660







700


690


680


670


660


650


640


630


620



650

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||~~V~~IN~~ =~~<br>~~V~~|~~ 4.3 V~~<br>~~ = 90~~|~~ V~~||
||||||~~OU~~<br>CIN =|1F|~~OU~~|~~(nom)~~|
||||||COU|T = 1|F||



−40 −20 0 20 40 60 80 100 120


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||~~V~~|~~ = 4.3~~|~~V~~||
||||||~~I~~<br>VO|UT = 0|V (Sh|ort)|
||||||CIN<br>|= 1<br>|F<br>||
||||||~~CO~~|~~UT = 1~~|~~F~~||



20 40 60 80 100 120 140



600

−40 −20 0 20 40 60 80 100 120



20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 25. Current Limit vs. Temperature** **Figure 26. Short Circuit Current vs.**
**Temperature**



1.0


0.9


0.8


0.7


0.6


0.5


0.4


0.3


0.2









0.50


0.45


0.40


0.35


0.30


0.25


0.20


0.15


0.10



0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||~~O~~|~~F −>~~|~~N~~||
||||||||||
||||||O|N −> O|FF||
||||||||||
|||||||~~V~~|~~ = 4.3~~||
|||||||~~IN~~<br>VO|UT = 3.|3 V|
|||||||CIN<br>|= 1<br>|F<br>|
|||||||~~CO~~|~~UT = 1~~|~~F~~|

−40 −20 0 20 40 60 80 100 120


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||||~~V~~|~~ = 4.3~~|~~V~~|
|||||||~~IN~~<br>VO<br>|UT = 3.<br>|3 V<br>|
|||||||~~C~~IN<br>|~~ = 1~~<br>|~~F~~<br>|
|||||||~~CO~~|~~UT = 1~~|~~F~~|



40 60 80 100 120 140



0
−40 −20 0 20 40 60 80 100 120



20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 27. Enable Threshold Voltage vs.** **Figure 28. Enable Current Temperature**
**Temperature**



100


90


80


70


60


50


40


30


20







10

0

|V|= 4.3|V|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|~~IN~~<br>VO<br>|UT = 3.<br>|3 V<br>|||||||
|~~C~~IN<br>|~~ = 1~~<br>|~~F~~<br>|||||||
|~~CO~~|~~UT = 1~~|~~F~~|||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

−40 −20 0 20 40 60 80 100 120 140



300


290


280


270


260


250


240


230


220


210



200

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||||~~VIN~~<br>V~~O~~|~~= 4.3~~<br>~~T~~ = 3.|3 V|
|||||||CIN<br>|= 1F<br>||
|||||||~~C~~O|UT~~ = 1~~|~~F~~|

−40 −20 0 20 40 60 80 100 120 140



T J, JUNCTION TEMPERATURE ( ° C) T J, JUNCTION TEMPERATURE ( ° C)


**Figure 29. Disable Current vs. Temperature** **Figure 30. Discharge Resistivity vs.**
**Temperature**


**[www.onsemi.com](http://www.onsemi.com/)**


**9**


**NCP161**


**TYPICAL CHARACTERISTICS**



10,000


1000


100


10












|I<br>OUT|RMS Output Noise (V)|Col3|
|---|---|---|
|**IOUT**|10 Hz − 100 kHz|100 Hz − 100 kHz|
|1 mA|14.62|14.10|
|10 mA|11.12|10.48|
|250 mA|10.37|9.82|
|450 mA|10.22|9.62|



1


**Figure 31. Output Voltage Noise Spectral Density − V** **OUT** **= 1.8 V**



10,000


1000


100


10












|I<br>OUT|RMS Output Noise (V)|Col3|
|---|---|---|
|**IOUT**|10 Hz − 100 kHz|100 Hz − 100 kHz|
|1 mA|16.9|15.79|
|10 mA|12.64|11.13|
|250 mA|11.96|10.64|
|450 mA|11.50|10.40|



1

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|I|OUT|= 2|I<br>O<br>5|UT<br>0 m|= 4<br>A|50|mA|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||IO|UT<br>|<br>IO|=<br>|1<br>UT|mA<br>= 10|m|A|||||
||V<br>V|IN<br>~~O~~|<br>~~U~~|=<br>~~T~~|2.8 V<br>= 1.8|V||||||||||||||||
||C<br>C|IN<br>O|<br>U|=<br>T|1F<br>= 1|F||||||||||||||||
|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|**Figure 31. Output Voltage N**<br>FREQUENCY (kHz)<br><br>100<br>10<br>1<br>0.1<br>0.01|
|||||||||||||||I|OUT =|4|50<br>I|m<br>OU|A<br>T = 2|50|mA|
|||||||||||IOU<br>I|T <br>OU|=<br>T|1<br>|m<br>=|A<br>10 m|A||||||
|V<br>|IN<br>|<br>|=<br>|4.<br>|3 V<br>|||||||||||||||||
|~~V~~<br>C<br>C|O<br>IN<br>O|U<br> <br>U|T<br>=<br>T|~~=~~<br> 1<br> =|~~3.3 V~~<br>F<br>1F|||||||||||||||||



0.01 0.1 1 10 100 1000


FREQUENCY (kHz)


**Figure 32. Output Voltage Noise Spectral Density − V** **OUT** **= 3.3 V**


**[www.onsemi.com](http://www.onsemi.com/)**


**10**


120


100


80


60


40


20



**NCP161**


**TYPICAL CHARACTERISTICS**


120







100


80


60


40


20









0

|I<br>O|=<br>UT|10 m|A|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|V<br>I<br>V|N|=|2.5<br>= 1.|V<br>8|V|Col22|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||C|~~O~~<br>O|~~UT~~<br>UT|= 1||F||
|||||||||||||||||||||||
||~~I~~|~~I~~<br>~~ =~~|OU<br>|T<br>|~~ =~~<br>~~0~~|~~ 20~~<br>~~mA~~|~~m~~|~~A~~||||||||||||||
||IOU<br>|T = 2<br>~~UT~~|5<br>|0<br>|m<br>|A<br>||||||||||||||||
|IO|UT =|450|m||A|||||||||||||||||

0.01 0.1 1 10 100 1k 10k



0

|I<br>O|UT|=|10|mA|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|V<br>V|IN|= 3.6<br>= 3|.|V<br>3|V|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||C|~~OU~~<br>OU|~~T~~<br>T =|1||F|
||||||||||||||||||||||
||||IO|U|T|=|20 m||A||||||||||||
||I|~~OU~~<br>|= 2<br>OUT|5<br>~~ =~~|0<br>|m<br>~~10~~|A<br>~~0 m~~||||||||||||||
|I|OU|T =|450||m|A|||||||||||||||

0.01 0.1 1 10 100 1k 10k



90


80


70


60


50


40


30


20


10





FREQUENCY (kHz) FREQUENCY (kHz)


**Figure 33. Power Supply Rejection Ratio,** **Figure 34. Power Supply Rejection Ratio,**
**V** **OUT** **= 1.8 V** **V** **OUT** **= 3.3 V**


100







0

|Col1|I<br>OU|= 2<br>T|0|m|A|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|V<br>I|N|=|5.5|V|Col21|Col22|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||VO<br>||UT <br>|= 5.<br>~~= 1~~|14<br>|<br>|V|
||||||||||||||||||~~T~~|||||
|||||||||||||||||||||||
|||~~I~~|O|U|T~~ =~~|~~ 10~~|~~m~~|~~A~~||||||||||||||
|||IOU|T|=|10|0 m|A|||||||||||||||
||~~I~~|~~ =~~|~~2~~|~~5~~|~~0~~|~~A~~||||||||||||||||
|||~~UT~~<br>||||||||||||||||||||
|~~I~~|OUT|~~= 45~~|||~~A~~|||||||||||||||||

0.01 0.1 1 10 100 1k 10k



10


1


0.1

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||~~ns~~|~~abl~~|~~ Op~~|~~erati~~|~~n~~||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||~~St~~|~~ble~~|~~Ope~~|~~ratio~~|||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||
||||||||||||||||||



0 50 100 150 200 250 300



350 400 450 500



FREQUENCY (kHz) I OUT, OUTPUT CURRENT (mA)


**Figure 35. Power Supply Rejection Ratio,** **Figure 36. Stability vs. ESR**
**V** **OUT** **= 5.14 V**











100 � s/div 100 � s/div


**Figure 37. Enable Turn−on Response −** **Figure 38. Enable Turn−on Response −**
**C** **OUT** **= 1** **�** **F, I** **OUT** **= 10 mA** **C** **OUT** **= 1** **�** **F, I** **OUT** **= 250 mA**


**[www.onsemi.com](http://www.onsemi.com/)**


**11**


**NCP161**


**TYPICAL CHARACTERISTICS**











20 � s/div 20 � s/div


**Figure 39. Line Transient Response −** **Figure 40. Line Transient Response −**
**V** **OUT** **= 1.8 V** **V** **OUT** **= 3.3 V**









20 � s/div 4 ms/div


**Figure 41. Line Transient Response −** **Figure 42. Turn−on/off − Slow Rising V** **IN**
**V** **OUT** **= 5.14 V**













4 � s/div 20 � s/div


**Figure 43. Load Transient Response −** **Figure 44. Load Transient Response −**
**1 mA to 450 mA − V** **OUT** **= 1.8 V** **450 mA to 1 mA − V** **OUT** **= 1.8 V**


**[www.onsemi.com](http://www.onsemi.com/)**


**12**


**NCP161**


**TYPICAL CHARACTERISTICS**







4 � s/div 20 � s/div


**Figure 45. Load Transient Response −** **Figure 46. Load Transient Response −**
**1 mA to 450 mA − V** **OUT** **= 3.3 V** **450 mA to 1 mA − V** **OUT** **= 3.3 V**













4 � s/div 20 � s/div


**Figure 47. Load Transient Response −** **Figure 48. Load Transient Response −**
**1 mA to 450 mA − V** **OUT** **= 5.14 V** **450 mA to 1 mA − V** **OUT** **= 5.14 V**

















10 ms/div 400 � s/div


**Figure 49. Short Circuit and Thermal** **Figure 50. Enable Turn−off**
**Shutdown**


**[www.onsemi.com](http://www.onsemi.com/)**


**13**


**NCP161**


**APPLICATIONS INFORMATION**



**General**

The NCP161 is an ultra−low noise 450 mA low dropout
regulator designed to meet the requirements of RF
applications and high performance analog circuits. The
NCP161 device provides very high PSRR and excellent
dynamic response. In connection with low quiescent current
this device is well suitable for battery powered application
such as cell phones, tablets and other. The NCP161 is fully
protected in case of current overload, output short circuit and
overheating.


**Input Capacitor Selection (C** **IN** **)**
Input capacitor connected as close as possible is necessary
for ensure device stability. The X7R or X5R capacitor
should be used for reliable performance over temperature
range. The value of the input capacitor should be 1 �F or
greater to ensure the best dynamic performance. This
capacitor will provide a low impedance path for unwanted
AC signals or noise modulated onto constant input voltage.
There is no requirement for the ESR of the input capacitor
but it is recommended to use ceramic capacitors for their low
ESR and ESL. A good input capacitor will limit the
influence of input trace inductance and source resistance
during sudden load current changes.


**Output Decoupling (C** **OUT** **)**
The NCP161 requires an output capacitor connected as
close as possible to the output pin of the regulator. The
recommended capacitor value is 1 �F and X7R or X5R
dielectric due to its low capacitance variations over the
specified temperature range. The NCP161 is designed to
remain stable with minimum effective capacitance of 0.7 �F
to account for changes with temperature, DC bias and
package size. Especially for small package size capacitors
such as 0201 the effective capacitance drops rapidly with the
applied DC bias. Please refer Figure 51.


**Figure 51. Capacity vs DC Bias Voltage**


There is no requirement for the minimum value of
Equivalent Series Resistance (ESR) for the C OUT but the
maximum value of ESR should be less than 2 Ω. Larger
output capacitors and lower ESR could improve the load



transient response or high frequency PSRR. It is not
recommended to use tantalum capacitors on the output due
to their large ESR. The equivalent series resistance of
tantalum capacitors is also strongly dependent on the
temperature, increasing at low temperature.


**Enable Operation**
The NCP161 uses the EN pin to enable/disable its device
and to deactivate/activate the active discharge function.
If the EN pin voltage is <0.4 V the device is guaranteed to
be disabled. The pass transistor is turned−off so that there is
virtually no current flow between the IN and OUT. The
active discharge transistor is active so that the output voltage
V OUT is pulled to GND through a 280 Ω resistor. In the
disable state the device consumes as low as typ. 10 nA from
the V IN .
If the EN pin voltage >1.2 V the device is guaranteed to
be enabled. The NCP161 regulates the output voltage and
the active discharge transistor is turned−off.
The EN pin has internal pull−down current source with
typ. value of 200 nA which assures that the device is
turned−off when the EN pin is not connected. In the case
where the EN function isn’t required the EN should be tied
directly to IN.


**Output Current Limit**
Output Current is internally limited within the IC to a
typical 700 mA. The NCP161 will source this amount of
current measured with a voltage drops on the 90% of the
nominal V OUT . If the Output Voltage is directly shorted to
ground (V OUT = 0 V), the short circuit protection will limit
the output current to 690 mA (typ). The current limit and
short circuit protection will work properly over whole
temperature range and also input voltage range. There is no
limitation for the short circuit duration.


**Thermal Shutdown**

When the die temperature exceeds the Thermal Shutdown
threshold (T SD � 160°C typical), Thermal Shutdown event
is detected and the device is disabled. The IC will remain in

this state until the die temperature decreases below the
Thermal Shutdown Reset threshold (T SDU − 140°C typical).
Once the IC temperature falls below the 140°C the LDO is
enabled again. The thermal shutdown feature provides the
protection from a catastrophic device failure due to
accidental overheating. This protection is not intended to be
used as a substitute for proper heat sinking.


**Power Dissipation**
As power dissipated in the NCP161 increases, it might
become necessary to provide some thermal relief. The
maximum power dissipation supported by the device is
dependent upon board design and layout. Mounting pad
configuration on the PCB, the board material, and the



**[www.onsemi.com](http://www.onsemi.com/)**


**14**


**NCP161**



ambient temperature affect the rate of junction temperature
rise for the part.
The maximum power dissipation the NCP161 can handle
is given by:



The power dissipated by the NCP161 for given
application conditions can be calculated from the following
equations:

P D � V IN � I GND � I OUT [�] V IN � V OUT [�] (eq. 2)


1.6



� 125 [o] C � T A �
P D(MAX) � �

JA


160


150


140


130


120


110


100


90


80



(eq. 1)





1.4


1.2


1.0


0.8


0.6


0.4


0.2


0


|Col1|Col2|Col3|P|, T =<br>D(MAX) A|25°C, 2 oz C|u|
|---|---|---|---|---|---|---|
||||~~P~~|~~, T =~~|~~25°C, 1 oz C~~|~~u~~|
|||||~~D(MAX)A~~|||
||||||||
|||||JA, 1|oz Cu||
||||||||
|||||JA, 2|oz Cu||
||||||||



0 100 200 300 400 500 600 700


PCB COPPER AREA (mm [2] )


**Figure 52.** **�** **JA** **and P** **D (MAX)** **vs. Copper Area (CSP4)**



220


210


200


190


180


170


160


150





1.0


0.9


0.8


0.7


0.6


0.5


0.4


0.3


|Col1|Col2|Col3|Col4|JA, 1|oz Cu|Col7|
|---|---|---|---|---|---|---|
||||||||
|||||JA, 2|oz Cu||
||||P<br>P|D(MAX), TA =<br>D(MAX), TA =|25°C, 1 oz C<br> 25°C, 2 oz C|u<br>u|
||||||||
||||||||
||||||||



0 100 200 300 400 500 600 700

PCB COPPER AREA (mm [2] )

**Figure 53.** **�** **JA** **and P** **D (MAX)** **vs. Copper Area (XDFN4)**


**[www.onsemi.com](http://www.onsemi.com/)**


**15**


0.7


0.6


0.5


0.4


0.3



325


300


275


250


225


200


175


150



0.2


0.1


0

|Col1|Col2|Col3|P|, T =<br>D(MAX) A|25°C, 2 oz C|u|
|---|---|---|---|---|---|---|
||||P<br>|D(MAX), TA =<br>|25°C, 1 oz C<br>|u<br>|
||||||||
|||||~~JA~~, 1|oz Cu||
|||||JA, 2<br>|oz Cu<br>||
||||||||
||||||||



0 100 200 300 400 500 600 700

PCB COPPER AREA (mm [2] )

**Figure 54.** **�** **JA** **and P** **D (MAX)** **vs. Copper Area (SOT23−5)**



**NCP161**



**Reverse Current**

The PMOS pass transistor has an inherent body diode
which will be forward biased in the case that V OUT - V IN .
Due to this fact in cases, where the extended reverse current
condition can be anticipated the device may require
additional external protection.


**Power Supply Rejection Ratio**
The NCP161 features very high Power Supply Rejection
ratio. If desired the PSRR at higher frequencies in the range
100 kHz – 10 MHz can be tuned by the selection of C OUT
capacitor and proper PCB layout.



**Turn−On Time**

The turn−on time is defined as the time period from EN
assertion to the point in which V OUT will reach 98% of its
nominal value. This time is dependent on various
application conditions such as V OUT(NOM), C OUT, T A .


**PCB Layout Recommendations**
To obtain good transient performance and good regulation
characteristics place C IN and C OUT capacitors close to the
device pins and make the PCB traces wide. In order to
minimize the solution size, use 0402 or 0201 capacitors with
appropriate capacity. Larger copper area connected to the
pins will also improve the device thermal resistance. The
actual power dissipation can be calculated from the equation
above (Equation 2). Expose pad can be tied to the GND pin
for improvement power dissipation and lower device
temperature.



**[www.onsemi.com](http://www.onsemi.com/)**


**16**


**NCP161**



**ORDERING INFORMATION**


































|Device|Nominal<br>Output<br>Voltage|Description|Marking|Rotation|Package|Shipping†|
|---|---|---|---|---|---|---|
|NCP161AFCS180T2G|1.8 V|450 mA, Active Discharge|A|180°|WLCSP4<br>CASE 567KA*<br>(Pb-Free)|5000 / Tape<br>& Reel|
|NCP161AFCS250T2G|2.5 V|2.5 V|D|180°|180°|180°|
|NCP161AFCS270T2G<br>(Consult**onsemi** Sales)|2.7 V|2.7 V|V|180°|180°|180°|
|NCP161AFCS280T2G|2.8 V|2.8 V|E|180°|180°|180°|
|NCP161AFCS285T2G|2.85 V|2.85 V|F|180°|180°|180°|
|NCP161AFCS300T2G|3.0 V|3.0 V|J|180°|180°|180°|
|NCP161AFCS320T2G|3.2 V|3.2 V|T|180°|180°|180°|
|NCP161AFCS330T2G|3.3 V|3.3 V|K|180°|180°|180°|
|NCP161AFCS350T2G|3.5 V|3.5 V|L|180°|180°|180°|
|NCP161AFCS450T2G|4.5 V|4.5 V|P|180°|180°|180°|
|NCP161AFCS500T2G|5.0 V|5.0 V|R|180°|180°|180°|
|NCP161AFCS514T2G|5.14 V|5.14 V|Q|180°|180°|180°|
|NCP161BFCS180T2G<br>(Consult**onsemi** Sales)|1.8 V|450 mA, Non-Active<br>Discharge|A|270°|WLCSP4<br>CASE 567KA*<br>(Pb-Free)|5000 / Tape<br>& Reel|
|NCP161BFCS250T2G|2.5 V|2.5 V|D|270°|270°|270°|
|NCP161BFCS280T2G<br>(Consult**onsemi** Sales)|2.8 V|2.8 V|E|270°|270°|270°|
|NCP161BFCS285T2G<br>(Consult**onsemi** Sales)|2.85 V|2.85 V|F|270°|270°|270°|
|NCP161BFCS300T2G<br>(Consult**onsemi** Sales)|3.0 V|3.0 V|J|270°|270°|270°|
|NCP161BFCS330T2G|3.3 V|3.3 V|K|270°|270°|270°|
|NCP161BFCS350T2G|3.5 V|3.5 V|L|270°|270°|270°|
|NCP161BFCS450T2G|4.5 V|4.5 V|P|270°|270°|270°|
|NCP161BFCS500T2G<br>(Consult**onsemi** Sales)|5.0 V|5.0 V|R|270°|270°|270°|
|NCP161BFCS514T2G<br>(Consult**onsemi** Sales)|5.14 V|5.14 V|Q|270°|270°|270°|



*UBM = 180 � m ( ± 5 � m)
7. Product processed after April 1, 2023 are shipped with quantity 10000 units / tape & reel.


**[www.onsemi.com](http://www.onsemi.com/)**


**17**


**NCP161**


**ORDERING INFORMATION**


































































|Device|Nominal<br>Output<br>Voltage|Description|Marking|Rotation|Package|Shipping†|
|---|---|---|---|---|---|---|
|NCP161AFCT180T2G|1.8 V|450 mA, Active Discharge|A|180°|WLCSP4<br>CASE 567JZ<br>(Pb-Free)|5000 or<br>10000 / Tape<br>& Reel<br>(Note 7)|
|NCP161AFCT185T2G<br>(Consult**onsemi** Sales)|1.85 V|1.85 V|V|180°|180°|180°|
|NCP161AFCT250T2G<br>(Consult**onsemi** Sales)|2.5 V|2.5 V|D|180°|180°|180°|
|NCP161AFCT280T2G|2.8 V|2.8 V|E|180°|180°|180°|
|NCP161AFCT285T2G<br>(Consult**onsemi** Sales)|2.85 V|2.85 V|F|180°|180°|180°|
|NCP161AFCT290T2G<br>(Consult**onsemi** Sales)|2.9 V|2.9 V|T|180°|180°|180°|
|NCP161AFCT300T2G|3.0 V|3.0 V|J|180°|180°|180°|
|NCP161AFCT310T2G<br>(Consult**onsemi** Sales)|3.1 V|3.1 V|6|180°|180°|180°|
|NCP161AFCT330T2G|3.3 V|3.3 V|K|180°|180°|180°|
|NCP161AFCT350T2G<br>(Consult**onsemi** Sales)|3.5 V|3.5 V|L|180°|180°|180°|
|NCP161AFCT450T2G|4.5 V|4.5 V|P|180°|180°|180°|
|NCP161AFCT500T2G<br>(Consult**onsemi** Sales)|5.0 V|5.0 V|R|180°|180°|180°|
|NCP161AFCT514T2G|5.14 V|5.14 V|Q|180°|180°|180°|
|NCP161AFCTC280T2G|2.8 V|450 mA, Active<br>Discharge, Backside<br>Coating|E|180°|180°|180°|
|NCP161AFCTC350T2G<br>(Consult**onsemi** Sales)|3.5 V|3.5 V|L|180°|180°|180°|
|NCP161BFCT180T2G|1.8 V|450 mA, Non-Active<br>Discharge|A|270°|270°|270°|
|NCP161BFCT185T2G<br>(Consult**onsemi** Sales)|1.85 V|1.85 V|V|270°|270°|270°|
|NCP161BFCT250T2G|2.5 V|2.5 V|D|270°|270°|270°|
|NCP161BFCT280T2G|2.8 V|2.8 V|E|270°|270°|270°|
|NCP161BFCT285T2G<br>(Consult**onsemi** Sales)|2.85 V|2.85 V|F|270°|270°|270°|
|NCP161BFCT300T2G<br>(Consult**onsemi** Sales)|3.0 V|3.0 V|J|270°|270°|270°|
|NCP161BFCT330T2G<br>(Consult**onsemi** Sales)|3.3 V|3.3 V|K|270°|270°|270°|
|NCP161BFCT350T2G<br>(Consult**onsemi** Sales)|3.5 V|3.5 V|L|270°|270°|270°|
|NCP161BFCT450T2G<br>(Consult**onsemi** Sales)|4.5 V|4.5 V|P|270°|270°|270°|
|NCP161BFCT500T2G|5.0 V|5.0 V|R|270°|270°|270°|
|NCP161BFCT514T2G<br>(Consult**onsemi** Sales)|5.14 V|5.14 V|Q|270°|270°|270°|



*UBM = 180 � m ( ± 5 � m)
7. Product processed after April 1, 2023 are shipped with quantity 10000 units / tape & reel.


**[www.onsemi.com](http://www.onsemi.com/)**


**18**


**NCP161**



**ORDERING INFORMATION** (continued)































|Device|Nominal Output<br>Voltage|Description|Marking|Package|Shipping†|
|---|---|---|---|---|---|
|NCP161AMX180TBG (Note 8)|1.8 V|450 mA,<br>Active<br>Discharge|DN|XDFN4<br>(Pb-Free)|3000 or 5000 /<br>Tape & Reel<br>(Note 8)|
|NCP161AMX185TBG (Note 8)|1.85 V|1.85 V|EY|EY|EY|
|NCP161AMX250TBG|2.5 V|2.5 V|DP|DP|DP|
|NCP161AMX280TBG (Note 8)|2.8 V|2.8 V|DQ|DQ|DQ|
|NCP161AMX285TBG|2.85 V|2.85 V|DR|DR|DR|
|NCP161AMX300TBG (Note 8)|3.0 V|3.0 V|DT|DT|DT|
|NCP161AMX320TBG (Note 8)|3.2 V|3.2 V|DZ|DZ|DZ|
|NCP161AMX330TBG (Note 8)|3.3 V|3.3 V|DD|DD|DD|
|NCP161AMX350TBG|3.5 V|3.5 V|DU|DU|DU|
|NCP161AMX450TBG|4.5 V|4.5 V|DV|DV|DV|
|NCP161AMX500TBG|5.0 V|5.0 V|DX|DX|DX|
|NCP161AMX514TBG (Note 8)|5.14 V|5.14 V|DE|DE|DE|
|NCP161BMX180TBG (Note 8)|1.8 V|450 mA,<br>Non-Active<br>Discharge|EN|XDFN4<br>(Pb-Free)|3000 or 5000 /<br>Tape & Reel<br>(Note 8)|
|NCP161BMX250TBG (Note 8)|2.5 V|2.5 V|EP|EP|EP|
|NCP161BMX280TBG (Note 8)|2.8 V|2.8 V|EQ|EQ|EQ|
|NCP161BMX285TBG|2.85 V|2.85 V|ER|ER|ER|
|NCP161BMX300TBG|3.0 V|3.0 V|ET|ET|ET|
|NCP161BMX330TBG (Note 8)|3.3 V|3.3 V|ED|ED|ED|
|NCP161BMX350TBG (Note 8)|3.5 V|3.5 V|EU|EU|EU|
|NCP161BMX450TBG|4.5 V|4.5 V|EV|EV|EV|
|NCP161BMX500TBG|5.0 V|5.0 V|EX|EX|EX|
|NCP161BMX514TBG (Note 8)|5.14 V|5.14 V|EE|EE|EE|
|NCP161ASN180T1G|1.8 V|450 mA,<br>Active<br>Discharge|JAF|SOT23−5L<br>(Pb-Free)|3000 / Tape & Reel|
|NCP161ASN250T1G|2.5 V|2.5 V|JAA|JAA|JAA|
|NCP161ASN280T1G|2.8 V|2.8 V|JAC|JAC|JAC|
|NCP161ASN300T1G|3.0 V|3.0 V|JAD|JAD|JAD|
|NCP161ASN330T1G|3.3 V|3.3 V|JAG|JAG|JAG|
|NCP161ASN350T1G|3.5 V|3.5 V|JAH|JAH|JAH|
|NCP161ASN500T1G|5.0 V|5.0 V|JAE|JAE|JAE|



- For information on tape and reel specifications, including part orientation and tape sizes, please refer to our Tape and Reel Packaging
[Specifications Brochure, BRD8011/D.](https://www.onsemi.com/pub/collateral/brd8011-d.pdf)
8. Product processed after October 1, 2022 are shipped with quantity 5000 units / tape & reel.


**[www.onsemi.com](http://www.onsemi.com/)**


**19**


MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**


**SOT−23, 5 Lead**
CASE 527AH

ISSUE A

DATE 09 JUN 2021











**GENERIC**

**MARKING DIAGRAM***


XXX = Specific Device Code
M = Date Code


*This information is generic. Please refer to
device data sheet for actual part marking.
Pb−Free indicator, “G” or microdot “ � ”, may
or may not be present. Some products may
not follow the Generic Marking.








|CUMENT NUMBER: 98A|Electronic versions are uncontrolled ex<br>ON34320E<br>Printed versions are uncontrolled exce|cept when accessed directly from the Document Repository.<br>pt when stamped “CONTROLLED COPY” in red.|
|---|---|---|
|**DESCRIPTION:**<br>**SO**|**T−23, 5 LEAD**|**PAGE 1 OF 1**|





© Semiconductor Components Industries, LLC, 2008 www.onsemi.com


MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**


**WLCSP4, 0.64x0.64x0.33**
CASE 567JZ

ISSUE B

DATE 16 MAY 2022



**GENERIC**

**MARKING DIAGRAM***


XM


X = Specific Device Code
M = Date Code


*This information is generic. Please refer to
device data sheet for actual part marking.
Pb−Free indicator, “G” or microdot “ � ”, may
or may not be present. Some products may
not follow the Generic Marking.








|DOCUMENT NUMBER:|98AON85781F|Electronic versions are uncontrolled except when accessed directly from the Document Repository.<br>Printed versions are uncontrolled except when stamped “CONTROLLED COPY” in red.|Col4|
|---|---|---|---|
|**DESCRIPTION:**<br>|**WLCSP4, 0.64X0.64x0.33**|**WLCSP4, 0.64X0.64x0.33**|**PAGE 1 OF 1**|





© Semiconductor Components Industries, LLC, 2014 www.onsemi.com


MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**


**WLCSP4, 0.64x0.64**
CASE 567KA
**SCALE 4:1** ISSUE B
DATE 24 MAR 2020


**GENERIC**

**MARKING DIAGRAM***


XM


X = Specific Device Code
M = Date Code


*This information is generic. Please refer to
device data sheet for actual part marking.
Pb−Free indicator, “G” or microdot “ � ”, may
or may not be present. Some products may
not follow the Generic Marking.










|DOCUMENT NUMB|ER: 98AON85783F|Electronic versions are uncontrolled except when accessed directly from the Document Repository.<br>Printed versions are uncontrolled except when stamped “CONTROLLED COPY” in red.|Col4|
|---|---|---|---|
|**DESCRIPTI**|**ON:**<br>**WLCSP4, 0.64X0.64**|**ON:**<br>**WLCSP4, 0.64X0.64**|**PAGE 1 OF 1**|





© Semiconductor Components Industries, LLC, 2014 www.onsemi.com


MECHANICAL CASE OUTLINE

**PACKAGE DIMENSIONS**


**XDFN4 1.0x1.0, 0.65P**
CASE 711AJ

ISSUE C

DATE 08 MAR 2022



**GENERIC**

**MARKING DIAGRAM***



*This information is generic. Please refer to
device data sheet for actual part marking.
Pb−Free indicator, “G” or microdot “ � ”, may
or may not be present. Some products may
not follow the Generic Marking.



1



XX M XX = Specific Device Code
M = Date Code










|DOCUMENT N|UMBER: 98AON67179E|Electronic versions are uncontrolled except when accessed directly from the Document Repository.<br>Printed versions are uncontrolled except when stamped “CONTROLLED COPY” in red.|Col4|
|---|---|---|---|
|**DESCR**|**IPTION:**<br>**XDFN4, 1.0X1.0, 0.65P**|**IPTION:**<br>**XDFN4, 1.0X1.0, 0.65P**|**PAGE 1 OF 1**|





© Semiconductor Components Industries, LLC, 2012 www.onsemi.com


**ADDITIONAL INFORMATION**


**TECHNICAL PUBLICATIONS** :
**Technical Library:** [www.onsemi.com/design/resources/technical−documentation](https://www.onsemi.com/design/resources/technical-documentation)
**onsemi Website:** [www.onsemi.com](https://www.onsemi.com/)






**ONLINE SUPPORT** : [www.onsemi.com/support](https://www.onsemi.com/support?utm_source=techdocs&utm_medium=pdf)
**For additional information, please contact your local Sales Representative at**
[www.onsemi.com/support/sales](https://www.onsemi.com/support/sales)


