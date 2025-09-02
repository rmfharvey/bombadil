## LTC7871 Six-Phase, Synchronous Bidirectional Buck or Boost Controller

### **FEATURES DESCRIPTION**



n **Unique Architecture Allows Dynamic Regulation of**

**Input Voltage, Output Voltage or Current**

n **Operates with External Gate Drivers and MOSFETs**

n **V** **HIGH** **Voltages Up to 100V; V** **LOW** **Voltages Up to 60V**

n **Synchronous Rectification: Up to 98% Efficiency**

n **ADI-Proprietary Advanced Current Mode Control**

n **±1% Voltage Regulation Accuracy Overtemperature**

n **Accurate, Programmable Inductor Current**

**Monitoring and Bidirectional Regulation**

n **SPI Compliant Serial Interface**

n **Operation Status and Fault Report**

n **Programmable V** **HIGH** **, V** **LOW** **Margining**

n Phase-Lockable Frequency: 60kHz to 750kHz

n Optional Spread Spectrum Modulation

n Multiphase/Multi-ICs Operation Up to 24 Phases

n Selectable CCM/DCM/Burst Mode Operation

n Thermally Enhanced 64-Lead LQFP Package

n AEC-Q100 Qualification in Progress

### **APPLICATIONS**


n Automotive 48V/12V Dual Battery Systems

n Backup Power Systems

### **TYPICAL APPLICATION**



The LTC [®] 7871 is a high performance bidirectional buck or
boost switching regulator controller that operates in either
buck or boost mode on demand. It regulates in buck mode
from V HIGH -to-V LOW and boost mode from V LOW -to-V HIGH
depending on a control signal, making it ideal for 48V/12V
automotive dual battery systems. An accurate current pro­
gramming loop regulates the maximum current that can
be delivered in either direction. The LTC7871 allows both
batteries to supply energy to the load simultaneously by
driving energy from either battery to the other.


Its proprietary constant frequency current mode archi­
tecture enhances the signal-to-noise ratio enabling low
noise operation and provides excellent current match­
ing between phases. Additional features include an SPIcompliant serial interface, discontinuous or continuous
mode of operation, OV/UV monitors, independent loop
compensation for buck and boost operation, accurate
inductor current monitoring and overcurrent protection.


The LTC7871 is available in a 64 pin 10mm × 10mm
LWE package.


All registered trademarks and trademarks are the property of their respective owners.



**High Voltage Bidirectional Controller with Programming and Monitoring Functions** **Boost-to-Buck Transition**



V HIGH
30V TO
70V



2.2µF
×12



3.01M









VFB LOW
OV LOW

























BUCK
5V/DIV

V LOW
2V/DIV


I L
5A/DIV


V HIGH
2V/DIV


V SW
100V/DIV





V LOW
12V/180A























50µs/DIV



7871 TA01b


Rev. B
# 1




|45.3k<br>100pF 4.7µF 51k<br>0.1µF 4.7µF 37.4k|Col2|Col3|Col4|
|---|---|---|---|
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k||||







PINS NOT USED
IN THIS CIRCUIT:
CLKOUT
DRVSET
MODE
ILIM

RUN
FAULT
PGOOD








|Col1|Col2|
|---|---|
||DRIVER|
|LTC7060|LTC7060|





|×12 + 33µF ×12 2.2Ω 499k 12.7k 210k 10k 3.01M 48.7k|OVLOW EXTVCC OVHIGH UVHIGH VFBHIGH VHIGH|1mΩ 6.8µH VHIGH|Col4|Col5|
|---|---|---|---|---|
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>0.33µF<br>1nF<br>499Ω<br>51k<br>37.4k<br>0.1µF<br>47pF<br>499Ω<br>12.7k<br>10k<br><br>BOOST<br>BUCK<br>SPI<br>INTERFACE<br>1µF<br>DO REQUIRES PULL-UP|PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br><br>ITHLOW<br>IMON<br>SS<br>SETCUR<br>DRVCC<br>V5<br>PWMEN<br>FREQ<br>SGND<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>LTC7871<br>~~I~~THHIGH<br>~~B~~UCK<br>~~S~~CLK<br>~~S~~DI<br>~~S~~DO<br>~~C~~SB|DRIVER<br>0.1µF<br>1.69k<br><br>16.9k<br>0.1µF<br>1.5k<br><br>DRIVER<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>6.8µH<br>VHIGH<br>(PHASE 2 TO PHASE 5)<br>LTC7060<br>LTC7060|DRIVER<br>0.1µF<br>1.69k<br><br>16.9k<br>0.1µF<br>1.5k<br><br>DRIVER<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>6.8µH<br>VHIGH<br>(PHASE 2 TO PHASE 5)<br>LTC7060<br>LTC7060|DRIVER<br>0.1µF<br>1.69k<br><br>16.9k<br>0.1µF<br>1.5k<br><br>DRIVER<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>6.8µH<br>VHIGH<br>(PHASE 2 TO PHASE 5)<br>LTC7060<br>LTC7060|
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>0.33µF<br>1nF<br>499Ω<br>51k<br>37.4k<br>0.1µF<br>47pF<br>499Ω<br>12.7k<br>10k<br><br>BOOST<br>BUCK<br>SPI<br>INTERFACE<br>1µF<br>DO REQUIRES PULL-UP|PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br><br>ITHLOW<br>IMON<br>SS<br>SETCUR<br>DRVCC<br>V5<br>PWMEN<br>FREQ<br>SGND<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>LTC7871<br>~~I~~THHIGH<br>~~B~~UCK<br>~~S~~CLK<br>~~S~~DI<br>~~S~~DO<br>~~C~~SB|DRIVER<br>0.1µF<br>1.69k<br><br>16.9k<br>0.1µF<br>1.5k<br><br>DRIVER<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>6.8µH<br>VHIGH<br>(PHASE 2 TO PHASE 5)<br>LTC7060<br>LTC7060|0.1µF<br>9k<br>k<br>1.|0.1µF<br>5k|
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>0.33µF<br>1nF<br>499Ω<br>51k<br>37.4k<br>0.1µF<br>47pF<br>499Ω<br>12.7k<br>10k<br><br>BOOST<br>BUCK<br>SPI<br>INTERFACE<br>1µF<br>DO REQUIRES PULL-UP|PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br><br>ITHLOW<br>IMON<br>SS<br>SETCUR<br>DRVCC<br>V5<br>PWMEN<br>FREQ<br>SGND<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>LTC7871<br>~~I~~THHIGH<br>~~B~~UCK<br>~~S~~CLK<br>~~S~~DI<br>~~S~~DO<br>~~C~~SB|DRIVER<br>0.1µF<br>1.69k<br><br>16.9k<br>0.1µF<br>1.5k<br><br>DRIVER<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>6.8µH<br>VHIGH<br>(PHASE 2 TO PHASE 5)<br>LTC7060<br>LTC7060|0.1µF<br>9k<br>k<br>1.||
|100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>0.33µF<br>1nF<br>499Ω<br>51k<br>37.4k<br>0.1µF<br>47pF<br>499Ω<br>12.7k<br>10k<br><br>BOOST<br>BUCK<br>SPI<br>INTERFACE<br>1µF<br>DO REQUIRES PULL-UP|PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br><br>ITHLOW<br>IMON<br>SS<br>SETCUR<br>DRVCC<br>V5<br>PWMEN<br>FREQ<br>SGND<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>LTC7871<br>~~I~~THHIGH<br>~~B~~UCK<br>~~S~~CLK<br>~~S~~DI<br>~~S~~DO<br>~~C~~SB||||


[Document Feedback](https://form.analog.com/Form_Pages/feedback/documentfeedback.aspx?doc=LTC7871.pdf&product=LTC7871&Rev=A) [For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

### **TABLE OF CONTENTS**

**Features............................................................................................................................. 1**
**Applications........................................................................................................................ 1**
**Typical Application ............................................................................................................... 1**
**Description......................................................................................................................... 1**
**Absolute Maximum Ratings..................................................................................................... 3**
**Order Information................................................................................................................. 3**
**Pin Configuration.................................................................................................................. 3**
**Electrical Characteristics......................................................................................................... 4**
**Typical Performance Characteristics........................................................................................... 8**
**Pin Functions......................................................................................................................10**
**Block Diagram....................................................................................................................12**
**Operation..........................................................................................................................13**
**Applications Information........................................................................................................20**

Serial Port **.** ............................................................................................................................................................ 31
Serial Port Register Details.................................................................................................................................... 35
**Typical Applications..............................................................................................................47**
**Package Description.............................................................................................................48**
**Revision History..................................................................................................................49**
**Typical Application...............................................................................................................50**
**Related Parts......................................................................................................................50**


Rev. B



**.**

# 2



**.**


[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

**.**

**.**

**.**

**.**

**.**

**.**


**.**


### **ABSOLUTE MAXIMUM RATINGS PIN CONFIGURATION**

**(Note 1)**


**.**

**.**

**.**

**.**

**.**

**.**


**.**



V HIGH ...................................................... –0.3V to 100V
Current Sense Voltages
(SNSD [+], SNSA [+], SNS [–] Phase 1 to 6) .... –0.3V to 60V
(SNSA [+] – SNS [–] ) .................................. –0.3V to 0.3V
(SNSD [+] – SNS [–] ) .................................. –0.3V to 0.3V
EXTV CC ..................................................... –0.3V to 60V
DRV CC **.** ...................................................... –0.3V to 11V
RUN, OV HIGH, UV HIGH, OV LOW **.** ................... –0.3V to 6V
V5 ............................................................... –0.3V to 6V
SCLK, SDI, SDO, CSB **.** ................................. –0.3V to 6V
PWM1, PWM2, PWM3
PWM4, PWM5, PWM6, PWMEN.............. –0.3V to V5
ITH HIGH, ITH LOW, VFB HIGH, VFB LOW **.** ........... –0.3V to V5
FAULT, SETCUR, DRVSET, PGOOD **.** ............. –0.3V to V5
IMON, ILIM, SS, BUCK, MODE **.** ................... –0.3V to V5
FREQ, SYNC, CLKOUT................................. –0.3V to V5
Operating Junction Temperature Range

(Notes 2, 3) **.** ...................................... –40°C to 150°C
Storage Temperature Range.................. –65°C to 150°C
DRV CC /EXTV CC Peak Current

(Guarantee by Design)......................................150mA

### **ORDER INFORMATION**



**.**


**.**



**.**

**.**

**.**

**.**

**.**

**.**


**.**



**.**


**.**



**.**


**.**



**.**


**.**



**.**

**.**

**.**

**.**

**.**


**.**



**.**


**.**



**.**

**.**

**.**

**.**

**.**

**.**


**.**



**.**

**.**

**.**

**.**

**.**

**.**


**.**

|LEAD FREE FINISH|PART MARKING*|PACKAGE DESCRIPTION*|TEMPERATURE RANGE|
|---|---|---|---|
|LTC7871ELWE#PBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 125°C|
|LTC7871ILWE#PBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 125°C|
|LTC7871JLWE#PBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 150°C|
|LTC7871HLWE#PBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 150°C|


|AUTOMOTIVE PRODUCTS**|Col2|Col3|Col4|
|---|---|---|---|
|LTC7871ELWE#WPBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 125°C|
|LTC7871ILWE#WPBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 125°C|
|LTC7871JLWE#WPBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 150°C|
|LTC7871HLWE#WPBF|LTC7871|64-Lead (10mm × 10mm) Plastic LQFP|–40°C to 150°C|



Contact the factory for parts specified with wider operating temperature ranges. *The temperature grade is identified by a label on the shipping container.


This product is available in 160-piece trays.


****** Versions of this part are available with controlled manufacturing to support the quality and reliability requirements of automotive applications. These

models are designated with a #W suffix. Only the automotive grade products shown are available for use in automotive applications. Contact your
local Analog Devices account representative for specific product ordering information and to obtain the specific Automotive Reliability reports for
these models.


[or more information on lead free part marking, go to: http://www.adi.com/leadfree/](https://www.analog.com/en/about-adi/quality-reliability/material-declarations.html)
[For more information on tape and reel specifications, go to: http://www.adi.com/tapeandreel/](https://www.analog.com/media/en/package-pcb-resources/package/tape-reel-rev-n.pdf)


Rev. B



**.**

**.**

**.**

**.**

**.**

**.**


**.**


[For more information LTC7871](http://www.linear.com/LTC7871)



**.**

**.**

**.**

**.**

**.**

**.**


**.**

# 3


## LTC7871

### ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the full operating

**temperature range, otherwise specifications are at T** **A** **= 25°C, V** **HIGH** **= 48V, V** **RUN** **= 5V unless otherwise noted. (Note 2)**


**SYMBOL** **PARAMETER** **CONDITIONS** **MIN** **TYP** **MAX** **UNITS**


**Main Control Loops**







































|V<br>HIGH|V Supply Voltage Range<br>HIGH|Col3|Col4|6 100|V|
|---|---|---|---|---|---|
|VLOW|VLOW Supply Voltage Range|VHIGH > 6V||1.2<br>60|V|
||VLOW Regulated Feedback Voltage|(Note 4); ITHLOW Voltage = 1.5V|l|1.188<br>1.200<br>1.212|V|
||VHIGH Regulated Feedback Voltage|(Note 4); ITHHIGH Voltage = 0.5V|l|1.188<br>1.200<br>1.212|V|
||VLOW EA Feedback Current|(Note 4)||–10<br>–40|nA|
||VHIGH EA Feedback Current|(Note 4)||–10<br>–40|nA|
||Reference Voltage Line Regulation|(Note 4); VHIGH = 7V to 80V||0.02<br>0.2|%|
||VHIGH/VLOW Voltage Load Regulation|Measured in Servo Loop, ∆ITH Voltage = 1.0V to 1.5V<br>Measured in Servo Loop, ∆ITH Voltage = 1.0V to 0.5V||0.01<br>–0.01<br>0.2<br>–0.2|%<br>%|
|gm–buck|Buck Mode Transconductance<br>Amplifier gm–buck|(Note 4) ITHLOW = 1.5V, Sink/Source 5µA||2|mmho|
|gm–boost|Boost Mode Transconductance<br>Amplifier gm–boost|(Note 4) ITHHIGH = 0.5V, Sink/Source 5µA||1|mmho|
|IQ|VHIGH DC Supply Current<br>Shutdown Mode, VHIGH Supply Current<br>Shutdown Mode, VLOW Supply Current|(Note 5)<br>VRUN = 0V; VHIGH = 48V<br>VRUN = 0V; VLOW = 12V||10<br>30<br>20<br>16|mA<br>µA<br>µA|
|UVLO|DRVCC Undervoltage Lockout<br>Threshold|DRVCC Ramping Down, VDRVSET = VV5<br>DRVCC Ramping Down, VDRVSET = Float <br>DRVCC Ramping Down, VDRVSET = 0V||6.9<br>4.8<br>3.9<br>7.2<br>5.0<br>4.1<br>7.5<br>5.2<br>4.3|V<br>V<br>V|
|UVLO|DRVCC Undervoltage Hysteresis|VDRVSET = Float, VV5<br>VDRVSET = 0V||0.8<br>0.5|V<br>V|
|UVLO|V5 Undervoltage Lockout Threshold|V5 Ramping Down, VDRVSET = Float, VV5<br>V5 Ramping Down, VDRVSET = 0V||4.2<br>3.9<br>4.4<br>4.1<br>4.6<br>4.3|V<br>V|
|UVLO|V5 Undervoltage Hysteresis|VDRVSET = Float, VV5<br>VDRVSET = 0V||0.2<br>0.5|V<br>V|
||RUN Pin On Threshold|VRUN Rising||1.1<br>1.22<br>1.35|V|
||RUN Pin On Hysteresis|||80|mV|
||RUN Pin Source Current|VRUN < 1.1V|l|0.6<br>2|µA|
||RUN Pin Hysteresis Current|VRUN > 1.3V|l|2<br>6|µA|
|ISS|Soft-Start Charging Current|VSS = 1.2V||0.8<br>1.0<br>1.2|µA|
||BUCK Pin Input Threshold|VBUCK Rising<br>VBUCK Falling||2.2<br>1.7|V<br>V|
||BUCK Pin Pull-Up Resistance|BUCK Pin to V5||200|kΩ|
||Maximum Duty Cycle|Buck Mode<br>Boost Mode||96<br>98<br>92|%<br>%|


**Current Monitoring and Regulation Functions**












|I +<br>SNSA|SNSA+ Pins Input Current|Col3|Col4|±0.05 ±1|µA|
|---|---|---|---|---|---|
|ISNSD+|SNSD+ Pins Input Current|||±0.05<br>±1|µA|
|ISNS–|SNS– Pins Input Current|||1|mA|
||ILIM Pin Input Resistance|||100|kΩ|
|ISETCUR|SETCUR Pin Sourcing Current|MFR_IDAC_SETCUR = 0x00|l|15.0<br>16.0<br>17.0|µA|
||IMON Current Proportional to VLOW at<br>Max Current|VILIM = Float, RSENSE = 3mΩ||±10|%|
||IMON Zero Current Voltage|||1.240<br>1.250<br>1.260|V|


# 4



Rev. B


[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

### ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the full operating

**temperature range, otherwise specifications are at T** **A** **= 25°C, V** **HIGH** **= 48V, V** **RUN** **= 5V unless otherwise noted. (Note 2)**


































|SYMBOL|PARAMETER|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
||Current Sense Pin Voltage<br>(VSNSD+ – VSNS–) to IMON Gain|VILIM = 0V, 1/4 VV5<br>VILIM = Float, 3/4 VV5, VV5||40<br>20|V/V<br>V/V|
||Total DC Sense Signal Gain|DCR Configuration||5|V/V|
||Total DC Sense Signal Gain|RSENSE Configuration||4|V/V|
|VSENSE(MAX)<br>(DCR<br>Configuration)|Maximum Current Sense Threshold<br>(Buck and Boost Mode)|VILIM = 0V<br>VILIM = 1/4 VV5<br>VILIM = Float<br>VILIM = 3/4 VV5<br>VILIM = VV5|l
<br>l
<br>l
<br>l
<br>l|6.5<br>17.0<br>27.0<br>36.0<br>44.0<br>10.0<br>20.0<br>30.0<br>40.0<br>50.0<br>13.5<br>23.0<br>33.0<br>44.0<br>56.0|mV<br>mV<br>mV<br>mV<br>mV|
|VSENSE(MAX)<br>(RSENSE <br>Configuration)|Maximum Current Sense Threshold<br>(Buck and Boost Mode)|VILIM = 0V<br>VILIM = 1/4 VV5<br>VILIM = Float<br>VILIM = 3/4 VV5<br>VILIM = VV5|l
<br>l
<br>l
<br>l
<br>l|8.1<br>21.2<br>33.7<br>45.0<br>55.0<br>12.5<br>25.0<br>37.5<br>50.0<br>62.5<br>16.9<br>28.8<br>41.3<br>55.0<br>70.0|mV<br>mV<br>mV<br>mV<br>mV|
|VOCFT|Overcurrent Fault Threshold,<br>VSNSD+ – VSNS–|VILIM = 0V<br>VILIM = 1/4 VV5<br>VILIM = Float<br>VILIM = 3/4 VV5<br>VILIM = VV5|l
<br>l
<br>l
<br>l
<br>l|31.0<br>43.0<br>54.0<br>65.0<br>76.0<br>37.5<br>50.0<br>62.5<br>75.0<br>87.5<br>44.0<br>57.0<br>71.0<br>85.0<br>99.0|mV<br>mV<br>mV<br>mV<br>mV|
|VNOCFT|Negative Overcurrent Fault Threshold,<br>VSNSD+ – VSNS–|VILIM = 0V<br>VILIM = 1/4 VV5<br>VILIM = Float<br>VILIM = 3/4 VV5<br>VILIM = VV5|l
<br>l
<br>l
<br>l
<br>l|–45.0<br>–58.0<br>–72.0<br>–86.0<br>–100.0<br>–37.5<br>–50.0<br>–62.5<br>–75.0<br>–87.5<br>–30.0<br>–42.0<br>–53.0<br>–64.0<br>–75.0|mV<br>mV<br>mV<br>mV<br>mV|
||Overcurrent Fault Threshold<br>Hysteresis, |VSNSD+ – VSNS–||VILIM = 0V<br>VILIM = 1/4 VV5, Float, 3/4 VV5, VV5||25<br>31|mV<br>mV|













|DRVCC and V5|Linear Regulators|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|VDRVCC|DRVCC Regulation Voltage|12V < VEXTVCC < 60V, VDRVSET = VV5 <br>12V < VEXTVCC < 60V, VDRVSET = Float<br>12V < VEXTVCC < 60V, VDRVSET = 0V||9.5<br>7.6<br>4.8<br>10<br>8
<br>5<br>10.5<br>8.4<br>5.2|V<br>V<br>V|
||DRVCC Load Regulation|IDRVCC = 0mA to 100mA, VEXTVCC = 14V||1.6<br>3.0|%|
||EXTVCC Switchover Voltage|EXTVCC Ramping Positive, VDRVSET = VV5<br>EXTVCC Ramping Positive, VDRVSET = Float<br>EXTVCC Ramping Positive, VDRVSET = 0V||10.7<br>8.5<br>6.9|V<br>V<br>V|
||EXTVCC Hysteresis|||12|%|
|V5|V5 Regulation Voltage|6V < VDRVCC < 10V||4.8<br>5.0<br>5.2|V|
||V5 Load Regulation|IV5 = 0mA to 20mA||0.5<br>1|%|


**Current DACs (IDAC)**



|Col1|V /V IDAC Accuracy<br>HIGH LOW|MFR_IDAC_V = 0x40 or 0x7F<br>LOW/HIGH|Col4|–1 1|%|
|---|---|---|---|---|---|
||VHIGH/VLOW IDAC Program Range|||–64<br>63|µA|
||SETCUR IDAC Program Range|||0<br>31|µA|
|LSB|VHIGH/VLOW IDAC LSB<br>SETCUR IDAC LSB|||1
<br>1|µA<br>µA|


**Oscillator and Phase-Locked Loop**







|I<br>FREQ|FREQ Pin Output Current|Col3|l|19 20 21|µA|
|---|---|---|---|---|---|
||Nominal Frequency|VSYNC = 0V, RFREQ = 51.1k||230<br>250<br>270|kHz|
|fLOW|Low Fixed Frequency|VSYNC = 0V, RFREQ = 27.4k||55<br>70<br>85|kHz|
|fHIGH|High Fixed Frequency|VSYNC = 0V, RFREQ = 105k||640<br>710<br>780|kHz|


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 5


## LTC7871

### ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the full operating

**temperature range, otherwise specifications are at T** **A** **= 25°C, V** **HIGH** **= 48V, V** **RUN** **= 5V unless otherwise noted. (Note 2)**















|SYMBOL|PARAMETER|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
||Synchronizable Frequency|SYNC = External Clock|l|60<br>750|kHz|
||Spread Spectrum Frequency<br>Modulation Range|VSYNC = 5V, RFREQ = 51.1k, MFR_SSFM = 0x00||–12<br>12|%|
|θ2 –θ1|Phase 2 Relative to Phase 1|||180|Deg|
|θ3 –θ1|Phase 3 Relative to Phase 1|||60|Deg|
|θ4 –θ1|Phase 4 Relative to Phase 1|||240|Deg|
|θ5 –θ1|Phase 5 Relative to Phase 1|||120|Deg|
|θ6 –θ1|Phase 6 Relative to Phase 1|||300|Deg|
|θCLKOUT –θ1|CLKOUT Phase to Phase 1|||30|Deg|
||Clock Output High Voltage|ILOAD = 0.5mA||V5 – 0.2<br>V5|V|
||Clock Output Low Voltage|ILOAD = –0.5mA||0.2|V|
||SYNC Pin Input Threshold|SYNC Pin Rising<br>SYNC Pin Falling||2<br> <br>0.8|V<br>V|
||SYNC Pin Input Resistance|||100|kΩ|


**Power Good and FAULT**










|Col1|PGOOD Voltage Low|I = 2mA<br>PGOOD|Col4|0.1 0.3|V|
|---|---|---|---|---|---|
||PGOOD Leakage Current|VPGOOD = 5V||±1|µA|
||PGOOD Trip Level, VFBHIGH/VFBLOW <br>With Respect to the Regulated Voltage|VFBHIGH/VFBLOW Ramping Negative<br>VFBHIGH/VFBLOW Ramping Positive||–10<br>10|%<br>%|
||PGOOD Delay|PGOOD Pin High to Low||40|µs|
||FAULT Voltage Low|IFAULT = 2mA||0.1<br>0.3|V|
||FAULTVoltage Leakage Current|VFAULT = 5V||±1|µA|
||FAULTDelay|FAULTPin High to Low||120|µs|
||VLOW OV Comparator Threshold|||1.15<br>1.2<br>1.25|V|
||VLOW OV Comparator Hysteresis|VOVLOW > 1.2V||5|µA|
||VHIGH OV Comparator Threshold|||1.15<br>1.2<br>1.25|V|
||VHIGH OV Comparator Hysteresis|VOVHIGH > 1.2V||5|µA|
||VHIGH UV Comparator Threshold|||1.15<br>1.2<br>1.25|V|
||VHIGH UV Comparator Hysteresis|VUVHIGH < 1.2V||5|µA|






|PWM Outputs|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||PWM Output High Voltage|ILOAD = 0.5mA|l|V5 – 0.5|V|
||PWM Output Low Voltage|ILOAD = –0.5mA|l|0.5|V|
||PWM Output Current in Hi-Z State|||±5|µA|



**DIGITAL I/O: CSB, SCLK, SDI, SDO**

|V<br>IL|Digital Input Low Voltage|Pins CSB, SCLK, SDI|Col4|0.5|V|
|---|---|---|---|---|---|
|VIH|Digital Input High Voltage|Pins CSB, SCLK, SDI||1.8|V|
|VOL|Digital Output Voltage Low|Pin SDO, Sinking 1mA||0.3|V|
|RCSB|CSB Pin Pull-Up Resistor|||300|kΩ|
|RSCLK|SCLK Pin Pull-Down Resistor|||300|kΩ|
|RSDI|SDI Pin Pull-Down Resistor|||300|kΩ|



Rev. B


# 6



[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

### ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the full operating

**temperature range, otherwise specifications are at T** **A** **= 25°C, V** **HIGH** **= 48V, V** **RUN** **= 5V unless otherwise noted. (Note 2)**


**SYMBOL** **PARAMETER** **CONDITIONS** **MIN** **TYP** **MAX** **UNITS**


**SPI Interface Timing Characteristics (Refer to Timing Diagram in Figure 9 and 10)**


|t<br>CKH|SCLK High Time|Col3|Col4|45|ns|
|---|---|---|---|---|---|
|tCSS|CSB Setup Time|||40|ns|
|tCSH|CSB High Time|||60|ns|
|tCS|SDI to SCLK Setup Time|||40|ns|
|tCH|SDI to SCLK Hold Time|||20|ns|
|tDO|SCLK to SDO Time|||90|ns|
|tC%|SCLK Duty Cycle|||45<br>50<br>55|%|
|fSCLK(MAX)|Maximum SCLK Frequency|||5|MHz|



**Note 1:** Stresses beyond those listed under Absolute Maximum Ratings
may cause permanent damage to the device. Exposure to any Absolute
Maximum Rating condition for extended periods may affect device
reliability and lifetime.

**Note 2:** The LTC7871 is tested under pulsed load conditions such that
T J ≈ T A . The LTC7871E is guaranteed to meet performance specifications
from 0°C to 85°C junction temperature. Specifications over the –40°C
to 125°C operating junction temperature range are assured by design,
characterization and correlation with statistical process controls. The
LTC7871I is guaranteed over the –40°C to 125°C operating junction
temperature range. The LTC7871J is guaranteed over the –40°C to 150°C
operating junction temperature range. The LTC7871H is guaranteed
over the full –40°C to 150°C operating junction temperature range. High



junction temperature degrades operating lifetimes; operating lifetime
is derated for junction temperatures greater than 125°C. Note that the
maximum ambient temperature consistent with these specifications is
determined by specific operating conditions in conjunction with board
layout, the rated package thermal impedance and other environmental
factors.

**Note 3:** T J is calculated from the ambient temperature T A and power
dissipation P D according to the following formula:
T J = T A + (P D     - 17°C/W)
**Note 4:** The LTC7871 is tested in a feedback loop that servos V ITHHIGH
and V ITHLOW to a specified voltage and measures the resultant VFB HIGH,
VFB LOW, respectively.

**Note 5:** Dynamic supply current may be higher due to the loading current
at DRV CC linear regulator.


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 7


## LTC7871

### **TYPICAL PERFORMANCE CHARACTERISTICS**



**T** **A** **= 25°C, unless otherwise noted.**



**Efficiency Buck Mode** **Power Loss Buck Mode** **Efficiency Boost Mode**



100


95


90


85


80


75


70


65









100


95


90


85


80


75


70


65



70


60


50


40


30


20


10



60

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
||||||VHIGH = 48<br>|V<br>|
||||||~~V~~LOW~~ = 12~~<br>FIGURE 18|~~V~~<br> CIRCUIT|

1 10 100 200

LOAD CURRENT (A)

7871 G01


**Power Loss Boost Mode**


60


|VHIG<br>VLOW|H =<br>= 1|48<br>2|V<br>V|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|~~FIGU~~|~~RE~~|~~18~~|~~CI~~|~~RC~~|~~UIT~~||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||V<br>|HI<br>|G<br>|H =<br>|48V<br>||||
|||||||||~~V~~<br>FI|LO<br>G|U|W~~ =~~<br>RE|~~12V~~<br> 18 CIR|C|UI|T|



1.5


1.4


1.3


1.2


1.1


1.0



60
0.1 1 10 50

LOAD CURRENT (A)

7871 G03


**RUN Pin Threshold**
**vs Temperature**



50


40


30


20


10







0

|VHIG<br>VLOW<br>FIGU|H =<br>=<br>RE|4<br>1<br>1|8<br>2<br>8|V<br>V<br>CIRC|UIT|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||

0.1 1 10 50

LOAD CURRENT (A)

7871 G04


**Regulated Feedback Voltage**
**vs Temperature**



0
1 10 100 200

LOAD CURRENT (A)

7871 G02


**SS Pin Pull-Up Current**
**vs Temperature**


2.0


1.6


1.2


0.8


0.4


0
–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G05


**Oscillator Frequency**
**vs Temperature**


300


280


260


240


220


200
–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G08


[For more information LTC7871](http://www.linear.com/LTC7871)



0.9

|Col1|ON<br>OFF|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G06


**Undervoltage Lockout**
**Threshold (V5) vs Temperature**


5.0


4.8


4.6


4.4


4.2


4.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||||RIS|ING||||
|||||||||
|||||||||
|||||||||
|||||||||

–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G09


Rev. B



1.206


1.204


1.202


1.200


1.198


1.196





1.194

|Col1|VFB<br>VFB|LOW<br>HIGH|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||

–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G07


# 8


### **TYPICAL PERFORMANCE CHARACTERISTICS**


## LTC7871

**T** **A** **= 25°C, unless otherwise noted.**



13.0


12.0


11.0


10.0


9.0


8.0



**Quiescent Current vs Temperature** **Shutdown Current vs Temperature**


60.0





**FREQ Pin Source Current**
**vs Temperature**


21.5


21.0


20.5


20.0


19.5


19.0


18.5
–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G12


**Maximum Current Sense**
**Threshold vs Feedback Voltage—**


70



7.0

|VHIGH|= 48|V|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G10


**SETCUR Pin Source Current**
**vs Temperature**


17.0


16.8


16.6


16.4


16.2


16.0


15.8


15.6


15.4


15.2


15.0
–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G13


**Current Sense Threshold**
**vs ITH Voltage—(R** **SENSE** **)**


70



50.0


40.0


30.0


20.0

|VHIG|H = 48|V|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||

–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)

7871 G11


**Current Sense Threshold**
**vs ITH Voltage (DCR)**



50


40


30


20


10


0


–10


–20


–30


–40





60


50


40


30


20


10





–50

|GN|D|Col3|Col4|
|---|---|---|---|
|~~1/4~~<br>FLO<br>|~~V5~~<br>AT<br>|||
|~~3/4~~<br>~~V5~~|~~V5~~|||
|||||
|||||
|||||
|||||
|||||
|||||
|||||

0 0.5 1 1.5 2

ITH VOLTAGE (V)

7871 G14


**Maximum Current Sense**
**Threshold vs Feedback Voltage—**
**BUCK (R** **SENSE** **)**


80


|Thresh BUCK BUCK|hold vs (DCR) (DCR)|s Fee|edback|k Volta|age—|
|---|---|---|---|---|---|
||GND<br>1/4 V5<br>|||||
||FLOAT<br>3/4 V5<br>|||||
||~~V5~~|||||
|||||||
|||||||
|||||||
|||||||



100


80


60


40


20



0
0 0.2 0.4 0.6 0.8 1.0 1.2

FEEDBACK VOLTAGE (V)

7871 G15


**Overcurrent Fault Threshold**
**vs Temperature**





70


60


50


40


30


20


10





50


30


10


–10


–30


–50





–70

|GN<br>1/4|D<br>V5|Col3|Col4|
|---|---|---|---|
|~~FLO~~<br>3/4<br>|~~AT~~<br> V5|||
|~~V5~~||||
|||||
|||||
|||||
|||||

0 0.5 1 1.5 2

ITH VOLTAGE (V)

7871 G16



0

|Col1|GND<br>1/4 V5|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||FLOAT<br>3/4 V5|||||
||FLOAT<br>3/4 V5|||||
||V5|||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

0 0.2 0.4 0.6 0.8 1.0 1.2

FEEDBACK VOLTAGE (V)

7871 G17


[For more information LTC7871](http://www.linear.com/LTC7871)


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||G<br>1/|ND<br>4 V5|
|||||||FL<br>3/<br>V|OAT<br>4 V5<br>5|



7871 G18


Rev. B
# 9



0
–45 –20 5 30 55 80 105 130 155

TEMPERATURE (°C)


## LTC7871

### **PIN FUNCTIONS**

**RUN (Pin 27):** Enable Control Input. A voltage above
1.22V turns on the IC. There is a 2µA pull-up current on
this pin. Once the RUN pin rises above the 1.22V thresh­
old, the pull-up current increases to 6µA.


**VFB** **HIGH** **(Pin 7):** V HIGH Voltage Sensing Error Amplifier
Noninverting Input.


**VFB** **LOW** **(Pin 3):** V LOW Voltage Sensing Error Amplifier
Inverting Input.


**ITH** **HIGH** **/ITH** **LOW** **(Pins 6 and 4):** Current Control Threshold
and Error Amplifier Compensation Point. The current com­
parator’s threshold varies with the ITH control voltage.


**SS (Pin 1):** Soft-Start Input. The voltage ramp rate at this
pin sets the voltage ramp rate of the regulated voltage. A
capacitor to ground accomplishes soft-start. This pin has
a 1µA pull-up current.


**MODE (Pin 51):** Mode Set Pin. Tying this pin to SGND
enables forced continuous mode in buck or boost modes.
Floating this pin results in burst mode in buck mode and
discontinuous mode in boost mode. Tying this pin to V5
enables discontinuous mode in buck or boost modes. The
input impedance of this pin is 90kΩ.


**SYNC (Pin 52):** Switching Frequency Synchronization
or Spread Spectrum Set Pin. Applying an external clock
between 60kHz to 750kHz to this pin causes the switch­
ing frequency to synchronize to the clock signal. If SYNC
is low, a resistor from the FREQ pin to SGND sets the
switching frequency. Tying this pin to V5 allows switching
frequency spread spectrum. This pin has a 100kΩ internal
resistor to ground.


**FREQ (Pin 53):** Frequency Set Pin. A resistor between
this pin and SGND sets the switching frequency. This pin
sources 20µA current.


**DRVSET (Pin 44):** The voltage setting on this pin pro­
grams the DRV CC output voltage. There are two internal
resistors, 200kΩ and 160kΩ, connecting this pin to the
V5 and SGND, respectively.


**CLKOUT (Pin 50):** Clock Output Pin. Use this pin to syn­
chronize multiple LTC7871 ICs. Signal swing is from V5
to ground.



**V5 (Pin 9):** Internal 5V Regulator Output. The control
circuits are powered from this voltage. Bypass this pin
to SGND with a minimum of 4.7µF low ESR tantalum or
ceramic capacitor.


**DRV** **CC** **(Pin 46):** Gate Driver Current Supply LDO Output.
The voltage on this pin can be set to 5V, 8V, or 10V by
the DRVSET pin. Bypass this pin to ground plane with a
minimum of 4.7μF low ESR tantalum or ceramic capacitor.


**EXTV** **CC** **(Pin 42):** External Power Input to an Internal LDO
Connected to DRV CC . This LDO supplies DRV CC power,
bypassing the internal LDO powered from V HIGH, when­
ever EXTV CC is higher than its switchover threshold. Do
not exceed 60V on this pin.


**ILIM (Pin 49):** Current Comparator Sense Voltage Limit
Selection Pin. The input impedance of this pin is 100kΩ.


**SNSD1** **[+]** **/SNSD2** **[+]** **/SNSD3** **[+]** **/SNSD4** **[+]** **/SNSD5** **[+]** **/SNSD6** **[+]**
**(Pins 19, 20, 25, 56, 61, and 62):** DC Positive Current
Sense Comparator Inputs. These inputs amplify the DC
portion of the current signal to the IC’s current compara­
tors and current sense amplifiers.


**SNS1** **[–]** **/SNS2** **[–]** **/SNS3** **[–]** **/SNS4** **[–]** **/SNS5** **[–]** **/SNS6** **[–]** **(Pins 18, 21,**
**24, 57, 60, and 63):** Negative Current Sense Comparator
Inputs. The negative input of the current comparator is
normally connected to the V LOW .


**SNSA1** **[+]** **/SNSA2** **[+]** **/SNSA3** **[+]** **/SNSA4** **[+]** **/SNSA5** **[+]** **/SNSA6** **[+]**
**(Pins 17, 22, 23, 58, 59, and 64):** AC Positive Current
Sense Comparator Inputs. These inputs amplify the AC
portion of the current signal to the IC’s current comparator.


**V** **HIGH** **(Pin 48):** Main V HIGH Supply. Bypass this pin to
ground with a capacitor (0.1μF to 1μF).


**FAULT (Pin 35):** Fault Indicator Output. Open-drain output
that pulls to ground during a fault condition.


**PGOOD (Pin 30):** Power Good Indictor Output for the
Regulated V HIGH /V LOW . Open drain logic out that is pulled
to ground when the regulated V HIGH /V LOW exceeds ±10%
regulation window, after the internal 40µS power bad
mask timer expires.


Rev. B


# 10



[For more information LTC7871](http://www.linear.com/LTC7871)


### **PIN FUNCTIONS**

**UV** **HIGH** **(Pin 14):** V HIGH Undervoltage Threshold Set Pin.
A resistor divider from V HIGH is needed to set this thresh­
old. When the voltage on this pin falls below the 1.2V
trip point, a 5μA current is sunk in to the pin to provide
externally adjustable hysteresis.


**OV** **HIGH** **(Pin 13):** V HIGH Overvoltage Threshold Set Pin. A
resistor divider from V HIGH is needed to set this thresh­
old. When the voltage on this pin rises past the 1.2V trip
point, a 5μA current is sourced out of the pin to provide
externally adjustable hysteresis.


**OV** **LOW** **(Pin 15):** V LOW Overvoltage Threshold Set Pin. A
resistor divider from V LOW is needed to set this thresh­
old. When the voltage on this pin rises past the 1.2V trip
point, a 5μA current is sourced out of the pin to provide
externally adjustable hysteresis.


**BUCK (Pin 54):** The voltage on this pin determines if the
IC is regulating the V LOW or V HIGH voltage/current. Float
or tie this pin to V5 for buck mode operation. Ground this
pin for boost mode operation.


**IMON (Pin 10):** Current Monitor Pin. The voltage on this
pin is directly proportional to the average inductor cur­
rents of all 6 channels. 1.25V on this pin indicates zero
average inductor current per phase.


## LTC7871

**SETCUR (Pin 11):** This pin sets the maximum average
inductor current in buck or boost mode. This pin sources
16μA current and it is programmable by the SPI interface.


**PWM1, PWM2, PWM3, PWM4, PWM5, PWM6 (Pins 29,**
**31, 32, 33, 34, and 36):** (Top) Gate Signal Output. This
signal goes to the PWM or top gate input of the external
gate driver or integrated driver MOSFET. This is a threestate compatible output.


**PWMEN (Pin 28):** Enable Pin for External Gate Drivers.
Open drain logic that is pulled to ground when the
LTC7871 shut downs the external gate drivers. When this
pin is low, all the PWM pin outputs are high impedance.


**CSB, SDO, SDI, SCLK (Pins 37, 38, 39 and 40):** 4-Wire
Serial Peripheral Interface (SPI). Active low chip select
(CSB), serial clock (SCLK) and serial data in (SDI) are
digital Inputs. Serial data out (SDO) is an open-drain
NMOS output pin. SDO requires an external pull-up resis­
tor. Refer to the Serial Port section for more details.


**NC (Pins 2, 8, 12, 26, 41, 43, 47, and 55):** No Connect Pins.


**SGND (Pins 5, 16, 45 and Exposed Pad):** Ground. Must
be soldered to PCB ground for rated thermal performance.
Connect this pin closely to negative terminal of V HIGH,
DRV CC, V5 bypass capacitors. All small signal components
and compensation components should connect here.


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 11


## LTC7871

### **BLOCK DIAGRAM Functional Diagram Shows Two Channels Only.**












|I|Col2|
|---|---|
|||


|Col1|Col2|
|---|---|
||HIGH<br>|




|CSB<br>2.4V|Col2|
|---|---|
|SPI INTERFACE|SPI INTERFACE|































V LOW

|VHIGH|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|||||
|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|||||
|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1||||||
|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|||SNSA1+<br>SNS1–<br>SNSD1+|SNSA1+<br>SNS1–<br>SNSD1+|SNSA1+<br>SNS1–<br>SNSD1+|
|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|||SNSA1+<br>SNS1–<br>SNSD1+|SNSD2+||
|+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>+<br>–<br>1.32V<br>1.08V<br>BUCK_EN<br>7871 BD<br>DRIVER<br>PWM1<br>VHIGH<br>PWMEN<br>DRIVER<br>–<br>+<br>~~–~~<br>~~+~~<br>CLK<br>SNSA1+<br>SNSD1+<br>SNS1–<br>+<br>–<br>~~+–~~<br>SNSA2+<br>SNSD2+<br>SNS2–<br>+<br>–<br>+–<br>ICMP1<br>ICMP2<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>VFBLOW<br>VFBHIGH<br>CONTROL<br>LOGIC<br>IDAC<br>SPI INTERFACE<br>IDAC<br>SETCUR<br>VHIGH_UV<br>VHIGH_OV<br>OVHIGH<br>UVHIGH<br>VREF<br>EXTVCC<br>VHIGH<br>VHIGH<br>PWM2<br>LOGIC 2<br>PGOOD<br>CSB<br>BUCK<br>2.4V<br>BUCK_EN<br>SCLK SDI<br>SDO<br>V5<br>IREV1,2<br>ICMP1,2<br>VFLD<br>**BUCK_EN**<br>VREF<br>OVLOW<br>MODE<br>VREF<br>VLOW_OV<br>VHIGH<br>**VFBLOW**<br>ITHLOW<br>SETCUR<br>IMON<br>VLOW<br>VLOW<br>SNSA1+<br>SNS1–<br>SNSD1+<br>SNSA2+<br>SNS2–<br>SNSD2+<br>**SS**<br>**1.2V**<br>ITHHIGH<br>SYNC<br>BOOST_EN<br>VFBHIGH<br>FREQ<br>CLKOUT<br>SS<br>1.2V<br>~~–~~<br>+<br>~~+~~<br>–<br>~~–~~<br>+<br>~~E~~A_VHIGH<br>~~**E**~~**A_VLOW**<br>INTERNAL<br>LDO REG<br>EXTVCC<br>~~LDO REG~~<br>5V LDO<br>PLL/OSC<br>PHASE<br>DETECTOR<br>VFBLOW<br>VFBHIGH<br>FAULT<br>VLOW_OV<br>VHIGH_OV<br>VHIGH_UV<br>+<br>–<br>+<br>–<br>SS<br>SGND<br>V5<br>DRVCC<br>EXTVCC<br>DRVSET<br>1µA<br>VHIGH<br>20µA<br>100k<br>CLK<br>V5<br>~~L~~OGIC 1|||SNSA1+<br>SNS1–<br>SNSD1+|||



Rev. B


|SNSD1+|Col2|
|---|---|
|||






|Col1|Col2|V|
|---|---|---|
||||
|WMEN||DRIVER|
|PWM2|PWM2|PWM2|


|Col1|V5|
|---|---|
|||
||DRIVER|
|||


|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||**BUCK_EN**<br>**VFBLOW**<br>ITHLOW<br>**SS**<br>**1.2V**<br>~~–~~<br>+<br>~~+~~<br>–<br>~~**E**~~**A_VLOW**|**BUCK_EN**<br>**VFBLOW**<br>ITHLOW<br>**SS**<br>**1.2V**<br>~~–~~<br>+<br>~~+~~<br>–<br>~~**E**~~**A_VLOW**|||
||**BUCK_EN**<br>**VFBLOW**<br>ITHLOW<br>**SS**<br>**1.2V**<br>~~–~~<br>+<br>~~+~~<br>–<br>~~**E**~~**A_VLOW**|**BUCK_EN**<br>**VFBLOW**<br>ITHLOW<br>**SS**<br>**1.2V**<br>~~–~~<br>+<br>~~+~~<br>–<br>~~**E**~~**A_VLOW**||VFLD|
||SETCUR||||
||IMON|IMON|IMON|IMON|


|SNSA1+ +– ICMP1|Col2|Col3|Col4|
|---|---|---|---|
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|||
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|NSD2+|||
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|NSD2+|||
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNS2–|||
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNS2–|||
|SNSD1+<br>SNS1–<br>+<br>–<br>~~–~~<br>SNSA2+<br>+<br><br>ICMP2|SNS2–|||









|Col1|BUCK CSB SCLK SDI SDO VHIGH OVHIGH UVHIGH<br>BUCK_EN<br>2.4V<br>VREF<br>EXTVCC<br>V5 SPI INTERFACE<br>+ – – +<br>VFB<br>IDAC LOW<br>IDAC<br>SETCUR<br>VFB VHIGH_OV<br>HIGH CONTROL VHIGH_UV<br>LOGIC<br>VREF – VLOW_OV<br>OVLOW<br>+<br>MODE<br>+<br>PWM1<br>BUCK_EN VREF – LOGIC 1<br>VFBLOW –+ PWMEN<br>–<br>SS EA_VLOW<br>1.2V +– IREV1,2<br>+<br>ITHLOW VFLD<br>CLK<br>PWM2<br>+ LOGIC 2<br>ICMP1,2<br>SETCUR –<br>1.25V + SETCUR<br>|1.25V – SETCUR|<br>ICMP1 + SNSA1+<br>IMON –<br>SNSD1+<br>+<br>SNS1– + – – +<br>–<br>ICMP2 + SNSA2+<br>–<br>SNSD2+<br>+<br>SNS2–<br>–<br>VFBHIGH<br>+<br>1.S 2S –EA_VHIGH BUCK_EN 1.32V +<br>V PGOOD<br>–<br>VFB<br>BOOST_EN LOW<br>ITHHIGH<br>VFB +<br>HIGH<br>1.08V –<br>SYNC PHASE FAULT<br>DETECTOR VHIGH VLOW_OV<br>100k VHIGH_OV<br>20µA INTERNAL VHIGH_UV<br>CLK LDO REG 1µA<br>FREQ EXTVCC<br>PLL/OSC 5V LDO<br>LDO REG<br>CLKOUT<br>DRVSET EXTVCC DRVCC V5 SGND SS|
|---|---|
|||


|Col1|Col2|
|---|---|
||FREQ<br>DETE<br>100k|
|||

# 12











|INTERNAL LDO REG|Col2|Col3|Col4|
|---|---|---|---|
|LDO REG<br>EXTVCC<br>|LDO REG<br>EXTVCC<br>|LDO REG<br>EXTVCC<br>|LDO REG<br>EXTVCC<br>|
|~~LDO REG~~<br>EXTVCC<br>DRVSET|~~LDO REG~~<br>EXTVCC<br>DRVSET|~~LDO REG~~<br>EXTVCC<br>DRVSET|~~LDO REG~~<br>EXTVCC<br>DRVSET|
|~~LDO REG~~<br>EXTVCC<br>DRVSET||||


[For more information LTC7871](http://www.linear.com/LTC7871)






### **OPERATION**

**Main Control Loop**


The LTC7871 is a bidirectional, constant-frequency, cur­
rent mode buck or boost switching regulator controller
with six channels operating equally out of phase. The
LTC7871 is capable of delivering power from V HIGH to
V LOW as well as from V LOW back to V HIGH . When power
is delivered from V HIGH to V LOW, the LTC7871 operates
as a peak-current mode constant-frequency buck regula­
tor; and when power delivery is reversed, it operates as a
valley current mode constant-frequency boost regulator.
Four control loops, two for current and two for voltage,
allow control of voltage or bidirectional current on either
V HIGH or V LOW . The LTC7871 uses an ADI proprietary cur­
rent sensing, current mode architecture. During normal
buck mode operation, the top MOSFET is turned on every
cycle when the oscillator sets the RS latch, and turned off
when the main current comparator, I CMP, resets the RS
latch. The peak inductor current at which I CMP resets the
RS latch is controlled by the voltage on the ITH pin, which
is the output of the error amplifier, EA. The error amplifier
receives the feedback signal and compares it to the inter­
nal 1.2V reference. When the load current increases, it
causes a slight change in the feedback pin voltage relative
to the 1.2V reference, which in turn causes the ITH voltage
to change until the inductor’s average current equals the
new load current. After the top MOSFET has turned off,
the bottom synchronous MOSFET is turned on until the
beginning of the next cycle.


In either buck or boost mode, the two current control
loops always monitor the maximum average inductor cur­
rent. When it increases above the thresholds, the current
loops will take over the ITH pin control from the voltage
loop. As a result, the maximum average inductor current
is limited.


The main control loop is shut down by pulling the RUN pin
low. Releasing the RUN pin allows an internal 2μA current
source to pull it up. When the RUN pin reaches 1.22V,
the IC is powered up and the pull-up current increases to
6μA. When the RUN pin is low, all functions are kept in a
controlled shutdown state.


## LTC7871

**Current Sensing with Low DCR or R** **SENSE**


The LTC7871 employs a unique architecture to enhance
the signal-to-noise ratio with low current sense offsets.
This enables it to operate with a small current sense signal
from a very low value inductor DCR to improve power
efficiency, and reduce jitter due to switching noise which
could corrupt the signal. Each channel has two positive
current sense pins, SNSD [+] and SNSA [+], which share
the negative current sense pin SNS [–] . These sense pins
acquire signals and process them internally to provide
the response equivalent to a DCR sense signal that has
a 14dB (5 times) signal-to-noise ratio. Accordingly, the
current limit threshold is still a function of the inductor
peak-current and its DCR value and can be accurately set
from 10mV to 50mV in 10mV steps with the ILIM pin.


**DRV** **CC** **/EXTV** **CC** **/V5 Power**


Power for the external top and bottom MOSFET drivers
is derived from the DRV CC pin. The DRV CC voltage can
be set to 5V, 8V, or 10V using the DRVSET pin. When
the EXTV CC pin is left open or tied to a voltage less than
the switchover voltage programmed by the DRVSET pin,
an internal linear regulator supplies DRV CC power from
V HIGH . When EXTV CC is taken above the switchover volt­
age, the internal regulator between V HIGH and DRV CC is
turned off, and a second internal regulator is turned on
between EXTV CC and DRV CC . Each top MOSFET driver is
biased from a floating bootstrap capacitor, which nor­
mally recharges during each off cycle through an external
diode when the top MOSFET turns off. If the input volt­
age, V HIGH, decreases to a voltage close to V LOW, the
loop may enter dropout and attempt to turn on the top
MOSFET continuously. The dropout detector detects this
and forces the top MOSFET off for about one-twelfth of
the clock period plus 160ns every fifth cycle to allow the
bootstrap capacitor to recharge.


Most of the internal circuitry is powered from the V5
rail that is generated by an internal linear regulator from
DRV CC . The V5 pin needs to be bypassed with a minimum
4.7μF external capacitor to SGND. This pin provides a 5V
output that can supply up to 20mA of current. See the
Applications Information section for more details.


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 13


## LTC7871

### **OPERATION**

**Soft-Start (Buck Mode)**


By default, the start-up of the V LOW voltage is normally
controlled by an internal soft-start ramp. The internal softstart ramp represents a noninverting input to the error
amplifier. The VFB LOW pin is regulated to the lowest of the
error amplifier’s three noninverting inputs (the internal
soft-start ramp, the SS pin or the internal 1.2V reference).
As the ramp voltage rises from 0V to 1.2V over approxi­
mately 1ms, the V LOW voltage rises smoothly from its
prebiased value to its final set value. Certain applications
can require the start-up of the converter into a non-zero
load voltage, where residual charge is stored on the V LOW
capacitor at the onset of converter switching. In order to
prevent the V LOW from discharging under these condi­
tions, the top and bottom MOSFETs are disabled until
soft-start is greater than VFB LOW .


**Soft-Start (Boost Mode)**


The same internal soft-start capacitor and external softstart capacitor are also active if the controller starts with
boost mode of operation. The error amplifier for boost
mode also tries to regulate to the lowest reference during
start-up. However, the topology of the boost converter
limits the effectiveness of this soft-start mechanism until
the boost output voltage reaches its input voltage level.
Therefore, it is recommended that the controller starts in
buck mode of operation.


**Shutdown and Start-Up (RUN and SS Pins)**


The LTC7871 can be shut down using the RUN pin.
Pulling the RUN pin below 1.22V shuts down the main
control loop for the controller and most internal circuits,
including the DRV CC and V5 regulators. Releasing the
RUN pin allows an internal 2μA current to pull up the
pin and enable the controller. Alternatively, the RUN pin
may be externally pulled up or driven directly by logic. Be
careful not to exceed the absolute maximum rating of 6V
on this pin. The start-up of the controller’s V LOW voltage
is controlled by the voltage on the SS pin. When the volt­
age on the SS pin is less than the 1.2V internal reference,
the LTC7871 regulates the VFB LOW voltage to the SS pin
voltage instead of the 1.2V reference. This allows the SS



pin to be used to program a soft-start by connecting an
external capacitor from the SS pin to SGND. An internal
1μA pull-up current charges this capacitor, creating a volt­
age ramp on the SS pin. As the SS voltage rises linearly
from 0V to 1.2V (and beyond), the V LOW voltage rises
smoothly from zero to its final value. When the RUN pin
is pulled low to disable the controller, or when V5 drops
below its undervoltage lockout threshold, the SS pin is
pulled low by an internal MOSFET. When in undervolt­
age lockout, the controller is disabled and the external
MOSFETs are held off. External circuitry can be added to
discharge the soft-start capacitor during fault conditions
to ensure a soft-start when the faults are cleared.


**Frequency Selection, Spread Spectrum, and Phase-**
**Locked Loop (FREQ and SYNC Pins)**


The selection of switching frequency is a trade-off between
efficiency and component size. Low frequency opera­
tion increases efficiency by reducing MOSFET switching
losses, but requires larger inductance and/or capacitance
to maintain low output ripple voltage.


If the SYNC pin is tied to SGND, the FREQ pin can be
used to program the controller’s operating frequency
from 67kHz to 725kHz. There is a precision 20μA current
flowing out of the FREQ pin so that the user can program
the controller’s switching frequency with a single resis­
tor to SGND. A curve is provided later in the Applications
Information section showing the relationship between
the voltage on the FREQ pin and switching frequency
(Figure 7).


Switching regulators can be particularly troublesome for
applications when electromagnetic interface (EMI) is a
concern. To improve EMI, the LTC7871 can operate in
spread spectrum mode, which is enabled by tying the
SYNC pin to V5. This feature varies the switching fre­
quency at low frequency rate (switching frequency/512,
by default) with a triangular frequency modulation of
±12%. For example, if the LTC7871’s frequency is pro­
grammed to switch at 200kHz, enabling spread spectrum
will modulate the frequency between 176kHz and 224kHz
at a 0.4kHz rate. These spread spectrum parameters are
programmed by the MFR_SSFM register.


Rev. B


# 14



[For more information LTC7871](http://www.linear.com/LTC7871)


### **OPERATION**

A phase-locked loop (PLL) is available on the LTC7871
to synchronize the internal oscillator to an external clock
source that is connected to the SYNC pin. The PLL loop
filter network is integrated inside the LTC7871. The phase
locked loop is capable of locking to any frequency within
the range of 60kHz to 750kHz. The frequency setting
resistor should always be present to set the controller’s
initial switching frequency before locking to the external
clock. The controller operates in the user selected mode
when it is synchronized.


**Undervoltage Lockout**


The LTC7871 has two functions that help protect the con­
troller in case of undervoltage conditions. Two precision
UVLO comparators constantly monitor the V5 and DRV CC
voltages to ensure that adequate voltages are present. The
switching action is stopped when V5 or DRV CC is below
the undervoltage lockout threshold. To prevent oscillation
when there is a disturbance on the V5 or DRV CC, the UVLO
comparators have precision hysteresis.


Another way to detect an undervoltage condition is to
monitor the V HIGH supply. Because the RUN pin has a
precision turn-on reference of 1.22V, one can use a resis­
tor divider to V HIGH to turn on the IC when V HIGH is high
enough. An extra 4μA of current flows out of the RUN pin
once the RUN pin voltage passes 1.22V. The RUN com­
parator itself has about 80mV of hysteresis. Additional
hysteresis for the RUN comparator can be programmed
by adjusting the values of the resistive divider. For accu­
rate V HIGH undervoltage detection, V HIGH needs to be
higher than 5V.


**Fault Flag (FAULT, OV** **HIGH** **, OV** **LOW** **and UV** **HIGH** **Pins)**


The FAULT pin is connected to the open-drain of an inter­
nal N-channel MOSFET. It can be pulled high with an exter­
nal resistor connected to a voltage up to 6V, such as V5
or an external bias voltage. The FAULT pin is pulled low
when at least one of the following conditions is met:


a. The RUN pin is below its turn on threshold.


b. When V5 or DRV CC is below its UVLO threshold.


c. Any of the three OV/UV comparators has been tripped.


## LTC7871

d. During a startup sequence until the SS pin charges up

past 1.2V.


e. When any channel is in overcurrent fault status.


f. When the IC is over temperature.


The OV LOW and OV HIGH thresholds are set using an exter­
nal resistor divider off V LOW and V HIGH, respectively.
When the voltage at the pin exceeds the comparator
threshold of 1.2V, a 5μA hysteresis current is sourced
out of the respective pin and the FAULT signal goes low
after a 120μs delay. The UV HIGH threshold is also set using
an external resistor divider off V HIGH . When the voltage
at the pin falls below the comparator threshold of 1.2V, a
5μA hysteresis current is sunk into the UV HIGH pin and the
FAULT signal goes low after a 120μs delay. The amount of
hysteresis can be adjusted by changing the total imped­
ance of the resistor divider, while the resistor ratio sets
the UV/OV trip point.


Besides flagging the FAULT pin, the UV/OV compara­
tors also affect the operation of the controller, as shown
in Table 1. When the OV LOW comparator crosses its
1.2V threshold:


a. In buck mode, the controller stops switching.


b. In boost mode, the controller continues to switch.


c. ITH and SS are unaffected in both buck and boost

modes. Whenever a fault is detected, discharge the
SS pin as needed externally.


When the OV HIGH comparator crosses its 1st threshold
of 1.2V:


a. The controller stops switching in both buck and

boost modes.


b. ITH and SS are unaffected in both buck and boost

modes. Whenever a fault is detected, discharge the
SS pin as needed externally.


When the OV HIGH comparator crosses its 2nd threshold
of 2.4V:


a. The controller stops switching in both buck and

boost modes.


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 15


## LTC7871

### **OPERATION**

b. Both ITH and IMON pins are driven into high imped­

ance. This feature allows the users to isolate one
LTC7871 from a multiphase system in case a fault is
detected on one particular IC.


c. The SS pin is unaffected.


When the UV HIGH comparator crosses its 1.2V threshold:


a. In buck mode, the controller stops switching after a

120μs delay, and the SS pin pulls to SGND.


b. In boost mode, the controller continues to switch. The

SS pin is unaffected.


c. ITH is unaffected in both buck and boost modes.


**Table 1. OV/UV Faults**



V
SETCUR =


where:



where:


V ZERO is the IMON voltage when average output current

is zero; V ZERO = 1.25V typically


K = 40 if the ILIM voltage is 0V or 1/4 V V5


K = 20 if the ILIM voltage is float, 3/4 V V5 or V V5


I L(ALL) is the total average inductor current including

all six channels


R SENSE is the current sensing resistor value.


An external voltage can be applied to the SETCUR pin
to regulate the maximum average inductor current. The
SETCUR pin voltage should be set as:



K •I L MAX ( ) [•R] SENSE

6






|FAULT|MODE|SWITCHING|ITH PINS|IMON|SS|
|---|---|---|---|---|---|
|OVLOW 1.2V<br>Threshold|Buck|Stops|No Effect|No Effect|No Effect|
|OVLOW 1.2V<br>Threshold|Boost|Continues|No Effect|No Effect|No Effect|
|OVHIGH 1.2V<br>Threshold|Buck|Stops|No Effect|No Effect|No Effect|
|OVHIGH 1.2V<br>Threshold|Boost|Stops|No Effect|No Effect|No Effect|
|OVHIGH 2.4V<br>Threshold|Buck|Stops|Hi-Z|Hi-Z|No Effect|
|OVHIGH 2.4V<br>Threshold|Boost|Stops|Hi-Z|Hi-Z|No Effect|
|UVHIGH 1.2V<br>Threshold|Buck|Stops|No Effect|No Effect|Pulls to SGND|
|UVHIGH 1.2V<br>Threshold|Boost|Continues|No Effect|No Effect|No Effect|



**Current Monitoring and Regulation**
**(IMON, SETCUR Pins)**


The inductor current can be sensed using either its DCR or
a R SENSE resistor. The current monitoring pin, IMON, out­
puts a voltage that is proportional to the average inductor
current of the six channels sensed by the LTC7871. The
operational range of IMON is 0.4V to 2.5V. When the aver­
age inductor current is zero, the IMON pin voltage rests
at 1.25V. As the inductor current increases in buck mode,
the IMON voltage proportionally increases; As the induc­
tor current increases in boost mode, the IMON voltage
proportionally decreases. Use the following equation to
calculate the voltages on IMON:



I L(MAX) is the maximum total average inductor current

including all six channels


The SETCURP and SETCURN are internally generated
voltages based on the SETCUR pin:


SETCURP = 1.25V + V SETCUR


SETCURN = |1.25V – V SETCUR |


SETCURP, SETCURN, and IMON are the three inputs to
the current regulation loop error amplifier with SETCURP
and SETCURN acting as the reference. When the IMON pin
voltage approaches SETCURP or SETCURN, the ITH pin
control is taken over by the current loop error amplifier
from the voltage loop error amplifier.


In either buck or boost mode, both the maximum positive
average current and the maximum negative average cur­
rent are regulated. There is a 16µA current flowing out of
the SETCUR pin so that a single resistor to SGND can set
both the positive average current loop and negative aver­
age current loop. The sourcing current from the SETCUR
pin is programmable through the SPI interface. For bat­
tery charging applications, SETCUR can be programmed
dynamically on-the-fly to set the charging currents to the
batteries in either buck or boost mode. SETCUR can be
used at start-up to limit the in-rush current in both buck
mode and boost mode.


Rev. B



V V
IMON = ZERO +



K •I L ALL ( ) [•R] SENSE
; Buck Mode
6



K •I L ALL ( ) [•R] SENSE
V IMON = V ZERO – ; Boost Mode
6


# 16



[For more information LTC7871](http://www.linear.com/LTC7871)


### **OPERATION**

To defeat the average current programming operation,
tie the SETCUR pin to V5 or voltage higher than 1.25V.


**Buck and Boost Modes (BUCK Pin)**


The LTC7871 can be dynamically and seamlessly switched
from buck mode to boost mode and vice versa via the
BUCK pin. Tie this pin to V5 to select buck mode and
to ground to select boost mode operation. This pin has
an internal pull up resistor that defaults to buck mode if
left floating. There are two separate error amplifiers for
V HIGH or V LOW regulation. Having two error amplifiers
allows fine tuning of the loop compensation for the buck
and boost modes independently to optimize transient
response. When buck mode is selected, the correspond­
ing error amplifier is enabled, and ITH LOW voltage con­
trols the peak inductor current. The other error amplifier
is disabled and ITH HIGH is parked at its zero current level.
In boost mode, ITH HIGH is enabled while ITH LOW is parked
at its zero current level. During a buck to boost or a boost
to buck transition, the internal soft-start is reset. Resetting
soft-start and parking the ITH pin at the zero current level
ensures a smooth transition to the newly selected mode.
Refer to Table 2 for a summary.


To further minimize any transients, SETCUR can be pro­
grammed to zero current level before switching between
boost and buck modes.


**Table 2. ITH PIN Parking Conditions**


## LTC7871

immediately when the regulated VFB LOW /VFB HIGH volt­
age is within ±10% of the reference window. However,
there is an internal 40µs power bad mask when regulated
VFB LOW /VFB HIGH voltage goes out of the ±10% window.
The PGOOD pin is allowed to be pulled up by an external
resistor to sources of up to 6V.


**Programmable V** **HIGH** **, V** **LOW** **Margining**


As shown in the Figure 1, the LTC7871 has a SPI con­
trolled 7-bit D/A converter current source. Through the
SPI interface, the LTC7871 receives a 7-bit DAC code and
converts this value to a bidirectional analog output cur­
rent. The current is connected to the VFB LOW pin in buck
mode or the VFB HIGH pin in boost mode. By connecting
the DAC current to the feedback node of a voltage regula­
tor, in buck mode, V LOW voltage is programmed with the
equation:


V LOW = 1.2V • (1 + R B /R A ) – I DAC - R B

In boost mode, V HIGH voltage is programmed with
the equation:


V HIGH = 1.2V • (1 + R D /R C ) – I DAC - R D


There are two different registers for V LOW and V HIGH pro­
gramming, MFR_IDAC_VLOW and MFR_IDAC_VHIGH.
The current DAC selects the register value based on the
buck or boost mode. The current DAC’s LSB is 1µA. The
MSB determines the current direction. When MSB is 0,
IDAC is sourcing current (reducing V LOW or V HIGH ), which
is positive current flowing out of the feedback pin. When
MSB is 1, IDAC is sinking current (increasing V LOW or
V HIGH ), which is negative current flowing into the feed­
back pin.












|Pin|Mode|When Parked|Comments|
|---|---|---|---|
|ITHHIGH|Buck|Normal<br>Operation|OVHIGH 2.4V Threshold Overrides Park|
|ITHHIGH|Boost|Prebiased<br>Turn-on|OVHIGH 2.4V Threshold Overrides Park|
|ITHLOW|Buck|Prebiased<br>Turn-on|OVHIGH 2.4V Threshold and OVLOW <br>Override Park|
|ITHLOW|Boost|Normal<br>Operation|OVHIGH 2.4V Threshold Overrides Park|







V LOW


R B


VFB LOW





**Power Good (PGOOD Pin)**
When the regulated VFB LOW /VFB HIGH voltage is not within
±10% of the 1.2V reference voltage, the PGOOD pin is
pulled low. The PGOOD pin is also pulled low when the
RUN pin is below 1.2V or when the LTC7871 is in the
soft-start or UVLO. The PGOOD pin will flag power good



V HIGH


VFB HIGH





**Figure 1. Current DAC for V** **LOW** **/V** **HIGH** **Programming**



[For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B
# 17


## LTC7871

### **OPERATION**

**Buck Mode Light Load Current Operation (DCM/CCM/**
**Burst Mode Operation)**


In buck mode, the LTC7871 can be enabled to enter dis­
continuous conduction mode (DCM), forced continuous
conduction mode (CCM), or Burst Mode operation. To
select forced continuous operation, tie the MODE pin
to SGND. To select discontinuous conduction mode of
operation, tie the MODE pin to V5. To select Burst Mode
operation, float the MODE pin.


In forced continuous operation, the inductor current is
allowed to reverse at light loads or under large transient
conditions. The peak inductor current is determined by
the voltage on the ITH LOW pin, just as in normal operation.
In this mode, the efficiency at light loads is lower than
in DCM operation. However, continuous mode has the
advantages of lower output ripple and less interference
with audio circuitry.


When the LTC7871 is enabled for Burst Mode operation,
the peak current in the inductor is set to approximately
one-third of the maximum sense voltage even though the
voltage on the ITH LOW pin indicates a lower value. If the
average inductor current is higher than the load current,
the error amplifier, EA, will decrease the voltage on the
ITH LOW pin. When the ITH LOW voltage drops below 1.1V,
the internal sleep signal goes high (enabling sleep mode)
and both external MOSFETs are turned off.


In sleep mode, the load current is supplied by the output
capacitor. As the output voltage decreases, the EA’s out­
put begins to rise. When the output voltage drops enough,

­
the sleep signal goes low, and the controller resumes nor
mal operation by turning on the top external MOSFET on
the next cycle of the internal oscillator. When a controller
is enabled for Burst Mode operation, the inductor cur­
rent is not allowed to reverse. The reverse current com­
parator (I REV ) turns off the bottom external MOSFET just
before the inductor current reaches zero, preventing it
from reversing and going negative. Thus, the controller
operates in discontinuous conduction mode.


When the MODE pin is connected to V5, the LTC7871
operates in discontinuous conduction mode at light loads.



At very light loads, the current comparator, I CMP, may
remain tripped for several cycles and force the external top
MOSFET to stay off for the same number of cycles (i.e.,
skipping-pulses). The inductor current is not allowed to
reverse (discontinuous operation). This mode, like forced
continuous operation, exhibits low output ripple as well
as low audio noise and reduced RF interference. It pro­
vides higher low current efficiency than forced continuous
mode, but not nearly as high as Burst Mode operation.


**Boost Mode Light Load Current Operation (DCM/CCM)**


In boost mode, the LTC7871 can be enabled to enter
constant-frequency discontinuous conduction mode or
forced continuous conduction mode. To select forced con­
tinuous operation, tie the MODE pin to SGND. To select
discontinuous conduction mode of operation, tie the
MODE pin to V5 or float it. In forced continuous operation,
the inductor current is allowed to reverse at light loads
or under large transient conditions. The inductor current
valley is determined by the voltage on the ITH HIGH pin,
just as in normal operation. In this mode, the efficiency
at light loads is lower. However, continuous mode has the
advantage of lower output ripple.


When the MODE pin is connected to V5 or floated, the
LTC7871 operates in discontinuous conduction mode at
light loads. At very light loads, the current comparator,
I CMP, may remain tripped for several cycles and force
the external top MOSFET to stay off for the same number
of cycles (i.e., skipping-pulses). The inductor current is
not allowed to reverse (discontinuous operation). This
mode, like forced continuous operation, exhibits low
output ripple as well as low audio noise and reduced RF
interference. It provides higher low current efficiency than
forced continuous mode.


The LTC7871 operation mode is summarized in Table 3.


**Table 3. Operation Mode**

|MODE Pin|Buck Operation Mode|Boost Operation Mode|
|---|---|---|
|0V|CCM|CCM|
|Float|Burst Mode Operation|DCM|
|VV5|DCM|DCM|



Rev. B


# 18



[For more information LTC7871](http://www.linear.com/LTC7871)


### **OPERATION**

**Overcurrent Fault Monitor (OCFT and NOCFT)**


Besides the peak/valley current comparator and the maxi­
mum average current regulation loops, the LTC7871 has
an additional overcurrent fault comparator to monitor the
voltage difference between the SNSD [+] and SNS [–] pins.
If one channel’s (V SNSD [+] – V SNS [–] ) is larger than over­
current fault threshold (OCFT) or less than the nega­
tive overcurrent threshold (NOCFT) as shown in the
Table 4, all six channels stop switching and all PWM pins
are Hi-Z. The OCFT and NOCFT status can be obtained
through the SPI interface by the MFR_OC_FAULT and
MFR_NOC_FAULT registers.


**Table 4. OCFT and NOCFT Threshold** **(V** **SNSD** **[+]** **– V** **SNS** **[–]** **)**









|ILIM Pin<br>Voltage|OCFT<br>Threshold|NOCFT<br>Threshold|Hysteresis|
|---|---|---|---|
|0V|37.5mV|–37.5mV|25mV|
|1/4 VV5|50mV|–50mV|31mV|
|Float|62.5mV|–62.5mV|31mV|
|3/4 VV5|75mV|–75mV|31mV|
|VV5|87.5mV|–87.5mV|31mV|


**PWM and PWMEN Pins**

The PWM pins are three-state compatible outputs,
designed to drive power stages such as power blocks,
DrMOS, and drivers with MOSFETs, none of which repre­
sents a heavy capacitive load. An external resistor divider
may be used to set the PWM voltage to mid-rail while the
PWM is in the high impedance state.


The PWMEN pin is an open-drain output pin. It should
be pulled up by an external resistor to V5 when the
controller starts switching. During any fault status, the
LTC7871 pulls down the PWMEN pin to disable the exter­
nal MOSFET driver.


## LTC7871

The LTC7871’s PWMEN pin is used to communicate the
controller’s status with the external MOSFET drivers or
other LTC7871s. When the LTC7871 releases the PWMEN
pin but finds it is still pulled down externally, the LTC7871
will keep all the PWM pins in Hi-Z status.


**Multiphase Operation**


For output loads that demand high current, multiple
LTC7871s can be daisy chained to run out of phase to
provide more output current without increasing input and
output voltage ripple. The SYNC pin allows the LTC7871
to synchronize to the CLKOUT signal of another LTC7871.
The CLKOUT signal can be connected to the SYNC pin of
the following LTC7871 stage to line up both the frequency
and the phase of the entire system. When paralleling mul­
tiple ICs, please be aware of the input impedance of pins
connected to the same node.


**Thermal Shutdown**


The LTC7871 has a temperature sensor integrated on
the IC, to sense the die temperature. When the die tem­
perature exceeds 180°C, all switching actions stop, and
all PWM pins become Hi-Z, thus turning off all external
MOSFETs. At the same time, all the channels are discon­
nected from the IMON pins, and the SS and ITH HIGH /
ITH LOW pins continue to function normally, so as not to
interfere with other LTC7871 chips that may reference the
common pins. When the temperature drops 15°C below
the trip threshold, normal operation resumes.


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 19


## LTC7871

### **APPLICATIONS INFORMATION**

The Typical Application on the first page of this data sheet
is a basic LTC7871 application circuit. In general, external
component selection is driven by the load requirements,
and begins with the DCR or R SENSE and inductor value.
Next, power MOSFETs are selected. Finally, V HIGH and
V LOW capacitors are selected.


**Slope Compensation and Inductor Peak Current**


Slope compensation provides stability in constant fre­
quency architectures by preventing subharmonic oscilla­
tions at high duty cycles. It is accomplished internally by
adding a compensating ramp to the inductor current sig­
nal at duty cycles in excess of 40%. Normally, this results
in a reduction of maximum inductor peak current for duty
cycles > 40%. However, the LTC7871 uses a scheme that
counteracts this compensating ramp, which allows the
maximum inductor peak current to remain unaffected
throughout all duty cycles.


**Current Limit Programming**


The ILIM pin is a 5-level logic input which sets the maxi­
mum current limit of the controller. Table 5 shows the five
ILIM settings. Please note that these settings represent
the peak inductor current setting. Because of the inductor
ripple current, the average output current is lower than
the peak current. Setting ILIM using a resistor divider
from V5 to SGND will allow the maximum current sense
threshold setting to not change when the 5V LDO is in
dropout at start-up. Please note that the ILIM pin has an
internal 200k pull down resistor to SGND and a 200k pull
up resistor to V5.


**Table 5. ILIM Settings**



**SNSD** **[+]** **, SNSA** **[+]** **and SNS** **[–]** **Pins**


The SNSA [+] and SNS [–] pins are the inputs to the current
comparators, while the SNSD [+] and SNS [–] pins are the input
of an internal DC amplifier. The operating input voltage
range is 0V to 60V for all three sense pins. All the positive
sense pins that are connected to the current comparator
or the amplifier are high impedance with input bias cur­
rents of less than 1μA. The SNS [–] pin is not a high imped­
ance pin. For V LOW voltages greater than V5, the current
comparators derive their bias currents directly from the
SNS [– ] pins. The SNS [–] pins should be connected directly
to V LOW . Care must be taken not to float these pins during
normal operation. Filter components, especially capaci­
tors, must be placed close to the LTC7871, and the sense
lines should run close together to a Kelvin connection
underneath the current sense element (Figure 2). Because
the LTC7871 is designed to be used with a very low value
sensing element to sense inductor current, without proper
care, the parasitic resistance, capacitance and inductance
will degrade the current sense signal integrity, making
the programmed current limit unpredictable. As shown in
Figure 3, resistor R1 is placed close to the output induc­
tor and capacitors C1 and C2 are close to the IC pins to
prevent noise coupling to the sense signal.


TO SENSE FILTER LOCATED
NEXT TO THE CONTROLLER


C OUT


7871 F02


**Figure 2. Sense Lines Placement with Sense Resistor**


**Inductor DCR Sensing**


The LTC7871 is specifically designed for high load current
applications requiring the highest possible efficiency; it is
capable of sensing the signal of an inductor DCR in the
milliohm range (Figure 3). The DCR is the DC winding
resistance of the inductor’s copper, which is often several
mΩ for high current inductors. In high current applica­

­
tions, the conduction loss of a high DCR or a sense resis
tor will cause a significant reduction in power efficiency.
The SNSA [+] pin connects to the filter that has a R1 • C1
time constant one-fifth of the L/DCR of the inductor. The
SNSD [+] pin is connected to the second filter with the time


Rev. B


|ILIM Pin Voltage|Maximum Current Sense Threshold|Col3|
|---|---|---|
|**ILIM Pin Voltage**|**DCR Sensing**|**RSENSE**|
|0V|10mV|12.5mV|
|1/4 VV5|20mV|25mV|
|Float|30mV|37.5mV|
|3/4 VV5|40mV|50mV|
|VV5|50mV|62.5mV|


# 20



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

constant matched to L/DCR of the inductor. For a specific
output requirement, choose the inductor with the DCR
that satisfies the maximum desired sense voltage, and
uses the relationship of the sense pin filters to output
inductor characteristics as depicted below.


## LTC7871

provides better efficiency at heavy loads. To maintain a
good signal-to-noise ratio for the current sense signal,
use a minimum of 10mV between SNSA [+] and SNS [–] pins
or the equivalent of 2mV ripple on the current sense signal
for duty cycles less than 40%. The actual ripple voltage
across SNSA [+] and SNS [–] pins will be determined by the
following equation:



DCR = [V] [SENSE][(][MAX][)]



I MAX + [∆I] [L]




- [V] [HIGH] [– V] [LOW]
R1•C1•f
OSC



2



L
DCR [=] [ 5 •R1•C1] [=] [ R2 •C2]


where:


V SENSE(MAX) is the maximum sense voltage for a given

ILIM threshold


∆I L is the Inductor ripple current


L and DCR are the output inductor characteristics


R1 • C1 is the filter time constant of the SNSA [+] pin


R2 • C2 is the filter time constant of the SNSD [+] pin


To ensure that the load current will be delivered over the
full operating temperature range, the temperature coef­
ficient of DCR resistance, approximately 0.4%/°C, should
be taken into account.


Typically, C1 and C2 are selected in the range of 0.047μF
to 0.47μF. If C1 and C2 are chosen to be 0.1μF, and an
inductor of 10μH with 2mΩ DCR is selected, R1 and R2
will be 10k and 49.9k, respectively. The bias current at
SNSD [+] and SNSA [+] is less than 1μA, and it introduces a
small error to the sense signal.


There will be some power loss in R1 that relates to the
duty cycle, and will be the most in continuous mode at
the maximum V HIGH voltage:
#### ( V HIGH(MAX) – V LOW ) [• V] LOW
###### P LOSS R ( ) =

R


Ensure that R1 has a power rating higher than this value.
Care has to be taken for voltage coefficients of these resis­
tors at high V HIGH voltages. Multiple resistors can be used
in series to minimize this effect. However, DCR sensing
eliminates the conduction loss of a sense resistor; it also



∆V [V] [LOW]
SENSE =
V
HIGH

|SNS–<br>LTC7871<br>SNSD+<br>SNSA+|Col2|Col3|
|---|---|---|
|LTC7871<br>SNS–<br>SNSD+<br>SNSA+||C2<br>R2|
|LTC7871<br>SNS–<br>SNSD+<br>SNSA+|||



7871 F03





SW



V LOW



+



**Figure 3. Inductor DCR Sensing**



**Sensing Using an R** **SENSE** **Resistor**


The LTC7871 can be used with an external R SENSE resis­
tor to sense current accurately. The external components
required to accomplish this are shown in Figure 4. The
SNSD [+] pin senses directly across the R S resistor through
R3 and C3 network. The R1, R2, and C1 network provide
the current signal path to the SNSA [+] pin. Internally the
signals from the AC and DC paths are combined for accu­
rate current sensing and low jitter performance. Resistor
R2 is used to divide down the DC component of the signal
seen by SNSA [+] due to the DCR of the inductor. As a rule
of thumb, R2 needs to be 10 times smaller than R1 so
the DCR value can be safely ignored.


SNSD [+]



LTC7871


SNS [–]


SNSA [+]


7871 F04






|Col1|R3|Col3|
|---|---|---|
||C2|C2|
||C1|RS|



+



V LOW


Rev. B
# 21



**Figure 4. R** **SENSE** **Resistor Sensing**



[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

### **APPLICATIONS INFORMATION**

The R1 • C1 time constant should be selected such that:



L

R
S



= 4•R1•C1 for R1 = 10•R2



The R3 • C2 time constant should be selected such that:


R3•C2 = [R1•R2]
R1 + R2 [•C1]


If a 6.8μH inductor and a 1mΩ sense resistor are selected
and C1 and C2 are chosen to be 0.1µF, then the values for
R1, R2 and R3 will be 16.9k, 1.69k and 1.5k, respectively
when the nearest standard value is chosen.


**Pre-Biased Output Start-Up**


There may be situations that require the power supply to
start up with a prebias on the V LOW output capacitors. In
this case, it is desirable to start up without discharging
that output prebias. The LTC7871 can safely power up
into a prebiased output without discharging it.


The LTC7871 accomplishes this by disabling both the
top and bottom MOSFETs until the SS pin voltage and the
internal soft-start voltage are above the VFB LOW pin volt­
age. When VFB LOW is higher than SS or the internal softstart voltage, the error amp output is parked at its zero
current level. Disabling both top and bottom MOSFETs
prevents the prebiased output voltage from being dis­
charged. When SS and the internal soft-start both cross
1.32V or VFB LOW, whichever is lower, both top and bottom
MOSFETs are enabled.


**Overcurrent Fault Protection**


In the buck mode, when the output of the power supply
is loaded beyond its preset current limit, the regulated
output voltage will collapse depending on the load. The
V LOW rail may be shorted to ground through a very low
impedance path or it may be a resistive short, in which
case the output will collapse partially, until the load cur­
rent equals the preset current limit. The controller will
continue to source current into the short. The amount of
current sourced depends on the ILIM pin setting and the
VFB LOW voltage as shown in the Current Foldback graph
in the Typical Performance Characteristics section.



Upon removal of the short, V LOW soft starts using the
internal soft-start, thus reducing output overshoot. In
the absence of this feature, the output capacitors would
have been charged at current limit, and in applications
with minimal output capacitance this may have resulted
in output overshoot. Current limit foldback is not disabled
during an overcurrent recovery. The load must drop below
the folded back current limit threshold in order to restart

from a hard short.


In both buck and boost modes of operation, forcing a
voltage on the SETCUR pin regulates the average current.
Zero average inductor current can be obtained by forcing
0V on SETCUR.


The LTC7871 has additional overcurrent fault compara­
tors to monitor the current of each channel. If there is
any catastrophic failure in the system which causes one
or more channel’s inductor current to be higher than the
overcurrent fault threshold, all the channels will be shut
down and both the PWMEN and the FAULT pins will be
pulled down to SGND.


Another way to protect against overcurrent is to moni­
tor the IMON pin voltage. If the IMON voltage indicates
excessive current, an external circuit can be used to shut
down the system.


**Inductor Value Calculation**


Given the desired input and output voltages, the inductor
value and operating frequency, f OSC, directly determine
the inductor’s peak-to-peak ripple current:



Lower ripple current reduces core losses in the inductor,
ESR losses in the output capacitors, and output voltage
ripple. Thus, highest efficiency operation is obtained at
low frequency with a small ripple current. Achieving this,
however, requires a large inductor.


A reasonable starting point is to choose a ripple current
that is about 40% of the maximum inductor current. Note
that the largest ripple current occurs at the highest V HIGH
voltage. To guarantee that ripple current does not exceed


Rev. B



⎠ [⎟]



I RIPPLE = [V] [LOW]
V
HIGH



⎛ V HIGH – V LOW

⎝ [⎜] f OSC - L



⎛ V HIGH – V LOW ⎞

⎝ [⎜] f OSC - L ⎠ [⎟]


# 22



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

a specified maximum, the inductor should be chosen
according to:



L ≥ [V] [HIGH] [– V] [LOW]
f OSC    - I RIPPLE




- [V] [LOW]
V
HIGH



**Inductor Core Selection**


Once the inductance value is determined, the type of
inductor must be selected. Core loss is independent of
core size for a fixed inductor value, but it is very depen­
dent on inductance selected. As inductance increases,
core losses go down. Unfortunately, increased inductance
requires more turns of wire and therefore copper losses
will increase.


Ferrite designs have very low core loss and are preferred
at high switching frequencies, so design goals can con­
centrate on copper loss and preventing saturation. Ferrite
core material saturates “hard,” which means that induc­
tance collapses abruptly when the peak design current is
exceeded. This results in an abrupt increase in inductor
ripple current and consequent output voltage ripple. Do
not allow the core to saturate!


**Power MOSFET and Schottky Diode (Optional)**
**Selection**


At least two external power MOSFETs need to be selected:
One N-channel MOSFET for the top switch and one or
more N-channel MOSFET(s) for the bottom switch. The
number, type and on-resistance of all MOSFETs selected
take into account the voltage step-down ratio as well
as the actual position (top or bottom) in which the
MOSFET will be used. A much smaller and much lower
input capacitance MOSFET should be used for the top
MOSFET in applications that have an V LOW that is less
than one-third of V HIGH . In applications where V HIGH >>
V LOW, the top MOSFETs’ on-resistance is normally less
important for overall efficiency than its input capacitance
at operating frequencies above 300kHz. MOSFET man­
ufacturers have designed special purpose devices that
provide reasonably low on-resistance with significantly
reduced input capacitance for the top switch application
in switching regulators.


## LTC7871

The peak-to-peak MOSFET gate drive levels are set by
the internal DRV CC regulator voltage. Pay close atten­
tion to the BV DSS specification for the MOSFETs as well.
Selection criteria for the power MOSFETs include the onresistance R DS(ON), input capacitance, input voltage and
maximum output current. MOSFET input capacitance is
a combination of several components but can be taken
from the typical gate charge curve included on most data
sheets (Figure 5). The curve is generated by forcing a
constant input current into the gate of a common source,
current source loaded stage and then plotting the gate
voltage versus time.


V IN


|V<br>+<br>GS<br>–|Col2|+<br>V<br>–|
|---|---|---|
|GS<br>V<br>+<br>–|||



The initial slope is the effect of the gate-to-source and the
gate-to-drain capacitance. The flat portion of the curve is
the result of the Miller multiplication effect of the drainto-gate capacitance as the drain drops the voltage across
the current source load. The upper sloping line is due to
the drain-to-gate accumulation capacitance and the gateto-source capacitance. The Miller charge (the increase
in coulombs on the horizontal axis from a to b while the
curve is flat) is specified for a given V DS drain voltage,
but can be adjusted for different V DS voltages by multi­
plying the ratio of the application V DS to the curve speci­
fied V DS values. A way to estimate the C MILLER term is to
take the change in gate charge from points a and b on a
manufacturer’s data sheet and divide by the stated V DS
voltage specified. C MILLER is the most important selec­
tion criteria for determining the transition loss term in
the top MOSFET but is not directly specified on MOSFET
data sheets. C RSS and C OS are specified sometimes but
definitions of these parameters are not included. When


Rev. B













Q IN


C MILLER = (Q B – Q A )/V DS





7871 F05



**Figure 5. Gate Charge Characteristic**



[For more information LTC7871](http://www.linear.com/LTC7871)


# 23


## LTC7871

### **APPLICATIONS INFORMATION**

the controller is operating in continuous mode the duty
cycles for the top and bottom MOSFETs are given by:

TopSwitchDuty Cycle = [V] [LOW]
V
HIGH



⎛



⎛ [– V] [LOW] ⎞

[V] [HIGH]

⎜ ⎟

V

⎝ HIGH ⎠




[– V] [LOW]
BottomSwitchDuty Cycle = ⎜ [V] [HIGH]
V

⎝ HIGH



⎟
⎠



The power dissipation for the top and bottom MOSFETs
at maximum output current are given by:



An optional Schottky diode across the bottom MOSFET
conducts during the dead time between the conduction
of the two large power MOSFETs in buck mode. This pre­
vents the body diode of the bottom MOSFET from turning
on, storing charge during the dead time and requiring
a reverse-recovery period which could cost as much as
several percent in efficiency. A 2A to 8A Schottky is gen­
erally a good compromise for both regions of operation
due to the relatively small average current. Larger diodes
result in additional transition loss due to their larger
junction capacitance.


**C** **HIGH** **and MOSFETs Selection (on V** **HIGH** **and V** **LOW** **)**


In continuous mode, the source current of the top
MOSFET is a square wave of duty cycle (V LOW )/(V HIGH ).
To prevent large voltage transients, a low ESR capaci­
tor sized for the maximum RMS current of one channel
must be used. In the following discussion, it is assumed
that C IN is C HIGH, C OUT is C LOW, V IN is V HIGH, and V OUT is
V LOW . The maximum RMS capacitor current is given by:



P TOP = [V] [LOW]
V
HIGH



2
###### ( I MAX ) 1 ( +δ ) [R] DS(ON) [+]



⎛



⎛ [I] MAX ⎞

⎜ ⎟
⎝ 2 ⎠



2 ⎛ [I] MAX
V
( HIGH ) ⎜
2



⎟ ( R DR ) ( [C] MILLER ) [•]
⎠



⎡

⎢
⎢⎣



1

DRV CC – V TH(MIN)



1
+
V
TH(MIN)



⎤

⎥•f
⎥⎦



P BOT = [V] [HIGH] [– V] [LOW]

V
HIGH



2
###### ( I MAX ) 1 ( +δ ) [R] DS(ON)



I MAX = Maximum Inductor Current.


where δ is the temperature dependency of R DS(ON), R DR
is the effective top driver resistance; V HIGH is the drain
potential and the change in drain potential in the particular
application. V TH(MIN) is the data sheet specified typical
gate threshold voltage specified in the power MOSFET
data sheet at the specified drain current. C MILLER is the
calculated capacitance using the gate charge curve from
the MOSFET data sheet and the technique described
above.


Both MOSFETs have I [2] R losses while the topside
N-channel equation includes an additional term for tran­
sition losses, which peak at the highest input voltage.
The bottom MOSFET losses are greatest at high V HIGH
voltage when the top switch duty factor is low or during
a V LOW short-circuit when the bottom switch is on close
to 100% of the period.


The term (1 + δ ) is generally given for a MOSFET in the
form of a normalized R DS(ON) vs temperature curve, but
δ = 0.005/°C can be used as an approximation for low
voltage MOSFETs.



This formula has a maximum at V IN = 2V OUT, where
I RMS = I OUT /2. This simple worst-case condition is com­
monly used for design because even significant deviations
do not offer much relief. Note that capacitor manufacturers’
ripple current ratings are often based on only 2000 hours
of use.


This makes it advisable to further derate the capacitor, or
to choose a capacitor rated at a higher temperature than
required. Several capacitors may be paralleled to meet size
or height requirements in the design. Ceramic capacitors
can also be used for C IN . Always consult the manufacturer
if there is any question.


Ceramic capacitors are becoming very popular for small
designs but several cautions should be observed. X7R, X5R
and Y5V are examples of a few of the ceramic materials
used as the dielectric layer, and these different dielectrics
have very different effect on the capacitance value due to
the voltage and temperature conditions applied. Physically,
if the capacitance value changes due to applied voltage
change, there is a concomitant piezo effect which results


Rev. B



C IN Required I RMS ≈ [I] [MAX]
V IN



1/2
##### ⎡⎣ ( V OUT ) V ( IN – V OUT ) ⎤⎦


# 24



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

in radiating sound! A load that draws varying current at an
audible rate may cause an attendant varying input voltage
on a ceramic capacitor, resulting in an audible signal. A
secondary issue relates to the energy flowing back into
a ceramic capacitor whose capacitance value is being
reduced by the increasing charge. The voltage can increase
at a considerably higher rate than the constant current
being supplied because the capacitance value is decreasing
as the voltage is increasing! Nevertheless, ceramic capaci­
tors, when properly selected and used, can provide the
lowest overall loss due to their extremely low ESR.


A small (0.1μF to 1μF) capacitor, C IN, placed close to
the LTC7871 between the V IN pin and ground, bypasses
switching noise to ground. A 2.2Ω to 10Ω resistor, placed
between C IN and V HIGH pins decouples the V HIGH pin from
switching noise.


The selection of C OUT at V OUT is driven by the required
effective series resistance (ESR). Typically once the ESR
requirement is satisfied the capacitance is adequate for
filtering. The steady-state output ripple (∆V OUT ) is deter­
mined by:



⎛



⎛ 1 ⎞

ESR +
8fC

⎝ [⎜] OUT ⎠ [⎟]



1
ΔV OUT ≈ΔI RIPPLE ESR +
8fC

⎝ [⎜] OUT



⎠ [⎟]



where f = operating frequency, C OUT = output capacitance
and ∆I RIPPLE = ripple current in the inductor. The output
ripple is highest at maximum input voltage since ∆I RIPPLE
increases with input voltage (V HIGH ). The output ripple will
be less than 50mV at maximum V IN with ∆I RIPPLE = 0.4

IOUT(MAX) [ assuming:]


C OUT required ESR < N • R SENSE


and


1
C OUT  ###### ( ) 8f R ( SENSE )


The emergence of very low ESR capacitors in small,
surface mount packages makes very small physical
implementations possible. The ability to externally com­
pensate the switching regulator loop using the ITH pin
allows a much wider selection of output capacitor types.
The impedance characteristic of each capacitor type is


## LTC7871

significantly different from that of an ideal capacitor and
therefore requires accurate modeling or bench evalua­
tion during design. Manufacturers such as Nichicon,
Nippon Chemi-Con and Sanyo should be considered for
high performance through-hole capacitors. The OS-CON
semiconductor dielectric capacitors available from Sanyo
and the Panasonic SP surface mount types have a good
(ESR)(size) product.


Once the ESR requirement for C OUT has been met, the
RMS current rating generally far exceeds the I RIPPLE(P–P)
requirement. Ceramic capacitors from AVX, Taiyo
Yuden, Murata and TDK offer high capacitance value
and very low ESR, especially applicable for low output
voltage applications.


In surface mount applications, multiple capacitors may
have to be paralleled to meet the ESR or RMS current
handling requirements of the application. Aluminum elec­
trolytic and dry tantalum capacitors are both available in
surface mount configurations. New special polymer sur­
face mount capacitors offer very low ESR also but have
much lower capacitive density per unit volume. In the
case of tantalum, it is critical that the capacitors are surge
tested for use in switching power supplies. Several excel­
lent choices are the AVX TPS, AVX TPSV, the KEMET T510
series of surface mount tantalums or the Panasonic SP
series of surface mount special polymer capacitors avail­
able in case heights ranging from 2mm to 4mm. Other
capacitor types include Sanyo POSCAP, Sanyo OS-CON,
Nichicon PL series and Sprague 595D series. Consult the
manufacturers for other specific recommendations.


**C** **HIGH** **Capacitor Selection for Boost Operation**


Contributions of ESR (equivalent series resistance), ESL
(equivalent series inductance) and the bulk capacitance
must be considered when choosing the correct combina­
tion of output capacitors for a boost converter application.


The choice of component(s) begins with the maximum
acceptable ripple voltage (expressed as a percentage of
the output voltage), and how this ripple should be divided
between the ESR step and the charging/discharging ∆ V.
For the purpose of simplicity we will choose 2% for the
maximum output ripple, to be divided equally between the
ESR step and the charging/discharging ΔV. This percentage


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 25


## LTC7871

### **APPLICATIONS INFORMATION**

ripple will change, depending on the requirements of the
application, and the equations provided below can easily
be modified.


One of the key benefits of multiphase operation is a reduc­
tion in the peak current supplied to the output capacitor
by the boost diodes. As a result, the ESR requirement
of the capacitor is relaxed. For a 1% contribution to the
total ripple voltage, the ESR of the output capacitor can
be determined using the following equation:

ESR COUT  - [0.01• V] [OUT]
I
D PEAK ( )


where:

I D PEAK ( ) [=] [1] ⎛ [χ] ⎞ [I] [O MAX] ( )
n [• 1] ⎝ [+] 2 ⎠ [•] 1–D MAX


The factor n represents the number of phases and the
factor [χ] represents the percentage inductor ripple current.


For the bulk capacitance, which we assume contributes
1% to the total output ripple, the minimum required
capacitance is approximately:


I
O MAX ( )
C OUT ≥
0.01•n•V OUT     - f


For many designs it will be necessary to use one type of
capacitor to obtain the required ESR, and another type to
satisfy the bulk capacitance. For example, using a low ESR
ceramic capacitor can minimize the ESR step, while an
electrolytic capacitor can be used to supply the required
bulk C.


The voltage rating of the output capacitor must be greater
than the maximum output voltage, with sufficient derating
to account for the maximum capacitor temperature.


Because the ripple current in the output capacitor is a
square wave, the ripple current requirements for this
capacitor depend on the duty cycle, the number of phases
and the maximum output current. In order to choose a
ripple current rating for the output capacitor, first establish
the duty cycle range, based on the output voltage and
range of input voltage.



The output ripple current is divided between the various
capacitors connected in parallel at the output voltage.
Although ceramic capacitors are generally known for low
ESR (especially X5R and X7R), these capacitors suffer
from a relatively high voltage coefficient. Therefore, it is
not safe to assume that the entire ripple current flows in
the ceramic capacitor. Aluminum electrolytic capacitors
are generally chosen because of their high bulk capaci­
tance, but they have a relatively high ESR. As a result,
some amount of ripple current will flow in this capacitor.
If the ripple current flowing into a capacitor exceeds its
RMS rating, the capacitor will heat up, reducing its effec­
tive capacitance and adversely affecting its reliability. After
the output capacitor configuration has been determined
using the equations provided, measure the individual
capacitor case temperatures in order to verify good ther­
mal performance.


**Setting Output Voltage**


The LTC7871 output voltage is set by two external feed­
back resistive dividers carefully placed across V HIGH to
ground and V LOW to ground, as shown in Figure 6. The
regulated output voltage is determined by:



⎛ ⎞ ⎛

+ [R] [B]

⎝ [⎜] R A ⎠ [⎟] [ and V] [HIGH] [ =][ 1.2V • 1] ⎝ [⎜] [+][ R] R [D] C



⎠ [⎟]



⎛

V 1.2V • 1+ [R] [B]
LOW =

⎝ [⎜] R A



⎛



⎛ ⎞

[+][ R] [D]
R

⎝ [⎜] C ⎠ [⎟]



To improve the frequency response, a feed forward capac­
itor, C FF1 /C FF2, may be used. Great care should be taken
to route the feedback line away from noise sources, such
as the inductor or the SW line.



V HIGH





V LOW







**Figure 6. Setting Output Voltage**



Rev. B


# 26



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

**External Soft-Start**


The LTC7871 has the ability to soft-start by itself using
the internal soft-start or at a slower rate with an external
capacitor on the SS pin. The controller is in the shutdown
state if its RUN pin voltage is below 1.14V and its SS pin
is actively pulled to ground in this shutdown state. If the
RUN pin voltage is above 1.22V, the controller powers
up. Once V5 and DRV CC pass the UVLO thresholds and
power on reset delay expires, a soft-start current of 1μA
then starts to charge the SS soft-start capacitor. Note that
soft-start is achieved not by limiting the maximum V LOW
output current of the controller but by controlling the out­
put ramp voltage according to the ramp rate on the SS
pin. Current foldback is disabled during this phase. The
soft-start range is defined to be the voltage range from
0V to 1.2V on the SS pin. The total soft-start time can be
calculated as:


t 1.2 • [C] [SS]
SOFTSTART =
1µA


**The Internal LDOs**


The LTC7871 features three internal PMOS LDOs. Two
provide power to DRV CC from either the V HIGH or V LOW
supply, and the third provides the V5 rail from DRV CC .
DRV CC powers the external top and bottom gate drive
circuits, and V5 powers the LTC7871’s internal circuitry.


There are two DRV CC LDOs—one that converts DRV CC
from V HIGH (LDO1) and another that converts DRV CC from
V LOW (LDO2), thus allowing the part to start up with just
one of the two rails present! Only one of those LDOs is
active at any given time. If V LOW is higher than the EXTV CC
switchover threshold, LDO2 is active; if it is below the swi­
tchover threshold, LDO1 is active. The DRV CC pin regula­
tion voltage is determined by the state of the DRVSET pin.
The DRVSET pin uses a 3-level logic. When DRVSET is
either grounded, floated or tied to V5, the typical value for
the DRV CC voltage will be 5V, 8V and 10V, respectively.
Please note that the DRVSET pin has an internal 160kΩ pull
down resistor to SGND and a 200kΩ pull up resistor to V5.


The V5 LDO regulates the voltage at the V5 pin to 5V when
DRV CC is at least 6V. The LDO can supply a peak current of
20mA and must be bypassed to ground with a minimum


## LTC7871

of 4.7μF ceramic capacitor or low ESR electrolytic capaci­
tor. No matter what type of bulk capacitor is used, an addi­
tional 0.1μF ceramic capacitor placed directly adjacent to
the V5 and SGND pins is highly recommended.


**Fault Conditions: Current Limit and Current Foldback**


In buck mode, the LTC7871 includes current foldback to
help limit power dissipation when the V LOW is shorted to
ground. If the V LOW falls below 33% of its nominal output
level, then the maximum sense voltage is progressively
lowered from its maximum programmed value to one-third
of the maximum value. Foldback current limiting is disabled
during soft-start. Under short-circuit conditions with very
low duty cycles, the LTC7871 will begin cycle skipping in
order to limit the short-circuit current. In this situation the
bottom MOSFET will be dissipating most of the power but
less than in normal operation. The short circuit ripple cur­
rent is determined by the minimum on-time t ON(MIN) of the
LTC7871, the V HIGH voltage and inductor value:

∆I L SC ( ) [=] [ t] ON MIN ( ) [•] [V] [HIGH]

L


The resulting short circuit current is:



After a short, make sure that the load current takes the
folded back current limit into account.


**Phase-Locked Loop and Frequency Synchronization**


The LTC7871 has a phase-locked loop (PLL) comprised
of an internal voltage-controlled oscillator (VCO) and a
phase detector. This allows the turn-on of the top MOSFET
to be locked to the rising edge of an external clock signal
applied to the SYNC pin. The phase detector is an edge
sensitive digital type that provides zero degrees phase
shift between the external and internal oscillators. This
type of phase detector does not exhibit false lock to har­
monics of the external clock.


The output of the phase detector is a pair of comple­
mentary current sources that charge or discharge the
internal filter network. There is a precision 20μA current


Rev. B




[1]
( )

R 2 [∆I] [L SC]

[⎜]



⎛ 13 V SENSE MAX ( ) – ⎞

[1]
( )

R 2 [∆I] [L SC]

⎝ [⎜] SENSE ⎠ [⎟]



⎠ [⎟]



I
SC =
R

⎝ [⎜] SENSE



[For more information LTC7871](http://www.linear.com/LTC7871)


# 27


## LTC7871

### **APPLICATIONS INFORMATION**

flowing out of the FREQ pin. This allows the user to use
a single resistor to SGND to set the switching frequency
when no external clock is applied to the SYNC pin. The
internal switch between the FREQ pin and the integrated
PLL filter network is on, allowing the filter network to be
pre-charged at the same voltage as of the FREQ pin. The
relationship between the voltage on the FREQ pin and
operating frequency is shown in Figure 7 and specified in
the Electrical Characteristics table. If an external clock is
detected on the SYNC pin, the internal switch mentioned
above turns off and isolates the influence of the FREQ
pin. Note that the LTC7871 can only be synchronized to
an external clock whose frequency is within range of the
LTC7871’s internal VCO. A simplified block diagram is
shown in Figure 8.


1000


800


600


400


200


0
0 0.5 1 1.5 2 2.5 3


V FREQ (V)

7871 F07



If the external clock frequency is greater than the inter­
nal oscillator’s frequency, f OSC, then current is sourced
continuously from the phase detector output, pulling up
the filter network. When the external clock frequency is
less than f OSC, current is sunk continuously, pulling down
the filter network. If the external and internal frequencies
are the same but exhibit a phase difference, the current
sources turn on for an amount of time corresponding to
the phase difference. The voltage on the filter network is
adjusted until the phase and frequency of the internal and
external oscillators are identical. At the stable operating
point, the phase detector output is high impedance and
the filter capacitor holds the voltage.


Typically, the external clock (on the SYNC pin) input high
threshold is 2V, while the input low threshold is 1.1V. The
LTC7871 switching frequency is determined by:


Frequency = V FREQ - 414kHz/V – 163.5kHz


where, V FREQ = I FREQ (from spec table) • R FREQ


Or,


Frequency = R FREQ - 8.28kHz/kΩ– 163.5kHz


This assumes a perfect 20μA I FREQ .


**Shared Pin Connections in Multichip Applications**


When multiple LTC7871 ICs are used together in high cur­
rent applications, the customer may or may not connect
certain pins together, balancing better communication
between the ICs versus avoiding a single point failure.


The CLKOUT pin allows multiple LTC7871s to be daisy
chained together. The clock output signal on the CLKOUT
pin can be used to synchronize additional ICs in a multi­
phase power supply solution feeding a single high current
output, or even several outputs from the same input supply.


The SS and PWMEN pins should be tied together to enable
every LTC7871 IC to start up together. Not connecting
them together may result in some phases sourcing a lot
of current and others sinking current.


The IMON pins may or may not be tied together, depend­
ing on whether the customer wants to monitor the
average current per IC or the total average current in
the application.


Rev. B



**Figure 7. Relationship Between Oscillator Frequency**

**and Voltage at the FREQ Pin**


**2.4V** **5V**













**Figure 8.**



**Phase-Locked Loop Block Diagram**


# 28



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

The ILIM, SETCUR, FREQ, MODE, BUCK, and DRVSET
pins may or may not be tied together based on conve­
nience. When tying these pins together, please be aware
of the pull-up/down currents/resistors on these pins! Any
external resistor or resistor divider network must take
those into account. For example, each FREQ pin sources
20μA. When two LTC7871 ICs have their FREQ pins tied
together, that is 40μA.


The OV LOW, OV HIGH and UV HIGH pins of multiple LTC7871s
must be tied together. This enables the entire system to
react to an OV/UV condition appropriately. The resistor
divider used on these pins must be scaled based on the
number of LTC7871s paralleled, as these pins have 5μA
hysteresis currents that turn on and off.


The ITH LOW and ITH HIGH pins of multiple LTC7871s
should be tied together. Tying the ITH LOW pins together
and the ITH HIGH pins together gives the best current shar­
ing between phases. Each error amplifier’s compensation
network must be placed local to the specific IC to mini­
mize jitter and stability issues.


The RUN pins must be tied together – this is very critical
for boost mode operation. In boost mode, when multiple
LTC7871 have their RUN pins connected together, care
must be taken to ensure that the logic signal on the RUN
pin is a clean fast rising/falling signal so all ICs are enabled
at the same instant. If a resistor divider is used on the
RUN pin, then the part must be started up in buck mode.
Using a resistor divider on the RUN pin off V HIGH, set for
a start-up voltage higher than the UV HIGH set point, allows
the part to soft start cleanly after a UV HIGH fault is cleared.


**Minimum On-Time Considerations**


Minimum on-time, t ON(MIN), is the smallest time duration
that the LTC7871 is capable of turning on the top MOSFET.
It is determined by internal timing delays, power stage
timing delays and the gate charge required to turn on the
top MOSFET. Low duty cycle applications may approach
this minimum on-time limit and care should be taken to

ensure that:


V
LOW
t ON(MIN) <
###### V HIGH f ( )


## LTC7871

If the duty cycle falls below what can be accommodated by
the minimum on-time, the controller will begin to skip cycles.
The output voltage and current will continue to be regulated,
but the voltage ripple and current ripple will increase. The
minimum on-time for the LTC7871 is approximately 150ns,
with good PCB layout, minimum 30% inductor current rip­
ple and at least 2mV ripple on the current sense signal or
equivalent 10mV between SNSA [+] and SNS [–] pins.


The minimum on-time can be affected by PCB switch­
ing noise in the voltage and current loop. As the peak
sense voltage decreases, the minimum on-time gradu­
ally increases. This is of particular concern in forced
continuous applications with low ripple current at light
loads. If the duty cycle drops below the minimum ontime limit in this situation, a significant amount of cycle
skipping can occur with correspondingly larger current
and voltage ripple.


**Efficiency Considerations**


The percent efficiency of a switching regulator is equal to
the output power divided by the input power times 100%.
It is often useful to analyze individual losses to determine
what is limiting the efficiency and which change would
produce the most improvement. Percent efficiency can
be expressed as:


%Efficiency = 100% – (L1 + L2 + L3 + ...)


where L1, L2, etc. are the individual losses as a percent­
age of input power.


Although all dissipative elements in the circuit produce
losses, four main sources usually account for most of
the losses in LTC7871 circuits: 1) IC V HIGH current, 2)
MOSFET driver current, 3) I [2] R losses, 4) top MOSFET
transition losses.


1. The V HIGH current is the DC supply current given in the

Electrical Characteristics table. V HIGH current typically
results in a small (<0.1%) loss.


2. The MOSFET driver current results from switching the

gate capacitance of the power MOSFETs. Each time
a MOSFET gate is switched from low to high to low
again, a packet of charge d Q moves from the driver
supply to ground. The resulting d Q /d t is a current


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 29


## LTC7871

### **APPLICATIONS INFORMATION**

out of the driver supply that is typically much larger
than the control circuit current. In continuous mode,
I GATECHG = f(Q T + Q B ), where Q T and Q B are the gate
charges of the top and bottom MOSFETs.

3. I [2] R losses are predicted from the DC resistances of

the fuse (if used), MOSFETs, inductor and current
sense resistor. In continuous mode, the average output
current flows through L and R SENSE, but is chopped
between the top MOSFET and the bottom MOSFET.
If the two MOSFETs have approximately the same
R DS(ON), then the resistance of one MOSFET can sim­
ply be summed with the resistances of L and R SENSE to
obtain I [2] R losses. For example, if each R DS(ON) = 10mΩ,
R L = 10mΩ, R SENSE = 5mΩ, then the total resistance
is 25mΩ. This results in losses ranging from 0.6% to
3% as the output current increases from 3A to 15A for
a 12V output in buck mode.


Efficiency varies as the inverse square of V LOW for the

same external components and output power level. The
combined effects of increasingly lower output voltages
and higher currents required by high performance digi­
tal systems is not doubling but quadrupling the impor­
tance of loss terms in the switching regulator system!


4. Transition losses apply only to the top MOSFET(s), and

become significant only when operating at high V HIGH
voltages (typically 15V or greater). Transition losses
can be estimated from:


Transition Loss = (1.7) V HIGH [2] - I O(MAX) - C RSS - f

I O(MAX) = Maximum Load on V LOW


Other hidden losses such as copper trace and internal
battery resistances can account for an additional 5% to
10% efficiency degradation in portable systems. It is very
important to include these system level losses during the
design phase. The internal battery and fuse resistance
losses can be minimized by making sure that C HIGH has
adequate charge storage and very low ESR at the switch­
ing frequency. Other losses including Schottky conduc­
tion losses during dead time and inductor core losses
generally account for less than 2% total additional loss.



**Checking Transient Response**


The regulator loop response can be checked by looking at
the load current transient response. Switching regulators
take several cycles to respond to a step in DC (resistive)
load current. When a load step occurs, V LOW shifts by an
amount equal to ∆I LOAD - ESR, where ESR is the effective
series resistance of C OUT at V LOW . ∆I LOAD also begins to
charge or discharge C OUT generating the feedback error sig­
nal that forces the regulator to adapt to the current change
and return V LOW to its steady-state value. During this recov­
ery time V LOW can be monitored for excessive overshoot
or ringing, which would indicate a stability problem. The
availability of the ITH pin not only allows optimization of
control loop behavior but also provides a DC-coupled and
AC-filtered closed-loop response test point. The DC step,
rise time and settling at this test point truly reflects the
closed-loop response. Assuming a predominantly second
order system, phase margin and/or damping factor can be
estimated using the percentage of overshoot seen at this
pin. The bandwidth can also be estimated by examining the
rise time at the pin. The ITH external components shown in
the Typical Application circuit will provide an adequate start­
ing point for most applications. The ITH series RC‑CC filter
sets the dominant pole-zero loop compensation. The values
can be modified slightly (from 0.5 to 2 times their suggested
values) to optimize transient response once the final PC
layout is done and the particular output capacitor type and
value have been determined. The output capacitors need to
be selected because the various types and values determine
the loop gain and phase. An output current pulse of 20% to
80% of full-load current having a rise time of 1μs to 10μs
will produce output voltage and ITH pin waveforms that will
give a sense of the overall loop stability without breaking
the feedback loop. Placing a power MOSFET directly across
the output capacitor and driving the gate with an appropri­
ate signal generator is a practical way to produce a realistic
load step condition. The initial output voltage step resulting
from the step change in output current may not be within
the bandwidth of the feedback loop, so this signal cannot be
used to determine phase margin. This is why it is better to
look at the ITH pin signal which is in the feedback loop and
is the filtered and compensated control loop response. The
gain of the loop will be increased by increasing RC and the


Rev. B


# 30



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

bandwidth of the loop will be increased by decreasing CC.
If RC is increased by the same factor that CC is decreased,
the zero frequency will be kept the same, thereby keeping
the phase shift the same in the most critical frequency range
of the feedback loop. The output voltage settling behavior
is related to the stability of the closed-loop system and will
demonstrate the actual overall supply performance. A sec­
ond, more severe transient is caused by switching in loads
with large (>1μF) supply bypass capacitors. The discharged
bypass capacitors are effectively put in parallel with C LOW,
causing a rapid drop in V LOW . No regulator can alter its
delivery of current quickly enough to prevent this sudden
step change in output voltage if the load switch resistance
is low and it is driven quickly. If the ratio of C LOAD to C OUT is
greater than 1:50, the switch rise time should be controlled
so that the load rise time is limited to approximately 25 •
C LOAD . Thus a 10μF capacitor would require a 250μs rise
time, limiting the charging current to about 200mA.


**SERIAL PORT**


­
The SPI-compatible serial port provides control and moni
toring functionality.


MASTER–CSB


MASTER–SCLK


## LTC7871

**Communication Sequence**


The serial bus is comprised of CSB, SCLK, SDI and SDO.
Data transfers to the part are accomplished by the serial
bus master device first taking CSB low to enable the
LTC7871’s port. Input data applied on SDI is clocked on
the rising edge of SCLK, with all transfers MSB first. The
communication burst is terminated by the serial bus mas­
ter returning CSB high. See Figure 9 for details.


Data is read from the part during a communication burst
using SDO. Readback may be multidrop (more than one
LTC7871 connected in parallel on the serial bus), as SDO
is high impedance (Hi-Z) when CSB = 1, or when data is
not being read from the part. If the LTC7871 is not used
in a multidrop configuration, or if the serial port mas­
ter is not capable of setting the SDO line level between
read sequences, it is recommended to attach a resistor
between SDO and V5 to ensure the line returns to V5 dur­
ing Hi-Z states. The resistor value should be large enough
to ensure that the SDO output current does not exceed
10mA. See Figure 10 for details.



MASTER–SDI



|tCSS tCSS<br>tCKL tCKH tCSH<br>tCS tCH<br>DATA DATA|Col2|Col3|
|---|---|---|
||||


7871 F09


**Figure 9. Serial Port Write Timing Diagram**



MASTER–CSB


MASTER–SCLK







**Figure 10. Serial Port Read Timing Diagram**


[For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B
# 31


## LTC7871

### **APPLICATIONS INFORMATION**

**Single Byte Transfers**


The serial port is arranged as a simple memory map, with
status and control available in 5 read/write and 6 read only
byte-wide registers. All data bursts are comprised of at
least three bytes. The 7 most significant bits (MSB) of the
first byte are the register address, with an LSB of 1 indi­
cating a read from the part, and LSB of 0 indicating a write


MASTER-CSB


MASTER-SCLK



to the part. The second byte, is data from/to the specified
register address. The third byte, is the PEC (packet error
code) byte. See Figure 11 for an example of a detailed
write sequence, and Figure 12 for a read sequence. All
bytes shift with MSB first.


Figure 13 shows an example of two write communica­
tion bursts. The first byte of the first burst sent from the


24 CLOCKS



7-BIT REGISTER ADDRESS


MASTER-SDI A6 A5 A4 A3 A2 A1 A0 0


LTC7871-SDO



8 BITS OF DATA


D7 D6 D5 D4 D3 D2 D1 D0


0 = WRITE



8 BITS OF PEC PARALLEL LOAD


P7 P6 P5 P4 P3 P2 P1 P0


7871 F11



**Figure 11. Serial Port Write Sequence**



MASTER-CSB


MASTER-SCLK


MASTER-SDI


LTC7871-SDO


MASTER–CSB


MASTER–SDI



24 CLOCKS







|Col1|Col2|8 BITS OF DATA 8 BITS OF PEC|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||X|D7|D6|D5|D4 D|3 D2|D1|D0|P7|P6|P5|P4|P3|P2|P1|P0||


7871 F12


**Figure 12. Serial Port Read Sequence**



Rev. B


# 32



LTC7871–SDO 7871 F13


**Figure 13. Two Write Communication Bursts**


[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

serial bus master on SDI contains the destination register
address (ADDR0) and a following 0 indicating a write.
The next byte is the DATA0 intended for the register at
address ADDR0. The third byte is the PEC0. CSB is then
taken high to terminate the transfer. The first byte of the
second burst contains the destination register address
(ADDR1) and a following 0 indicating a write. The next
byte on SDI is the DATA1 intended for the register at
address ADDR1. The third byte is the PEC1. CSB is then
taken high to terminate the transfer. Note that the written
data is transferred to the internal register at the falling
edge of the 24th clock cycle (parallel load) in each burst
after the PEC is checked as valid.


**PEC Byte**


The PEC byte a cyclic redundancy check (CRC) value cal­
culated for all the bits in a register group in the order they
are passed, using the initial PEC value of 01000001 (0x41)
and the following characteristic polynomial:


x [8] + x [2] + x + 1


To calculate the 8-bit PEC value, a simple procedure can
be established:


1. Initialize the PEC to 0100 0001.


2. For each bit DIN coming into the register group, set

IN0 = DIN XOR PEC[7], then IN1=PEC[0] XOR IN0,
IN2 = PEC[1] XOR IN0.


**Table 6. Procedure to Calculate PEC Byte**


## LTC7871

3. Update the 8-bit PEC as PEC[7] = PEC[6],

PEC[6] = PEC[5],……PEC[3] = PEC[2], PEC[2] = IN2,
PEC[1] = IN1, PEC[0] = IN0.


4. Go back to step 2 until all data are shifted. The 8-bit

result is the final PEC byte.


An example to calculate the PEC is listed in Table 6 and
Figure 14. The PEC of the 1 byte data 0x01 is computed
as 0xC7 after the last bit of the byte clocked in.


For the serial port write sequence, the master calculates
the PEC byte for the address byte and data byte it sends
out. The master latches the PEC byte it calculates at the
15th clock falling edge and attaches the calculated PEC
byte following the data byte it shifts out. The LTC7871
also calculates PEC byte for the address byte and data
byte it receives. The LTC7871 latches the PEC byte it cal­
culates at the 16th clock rising edge and compares it with
the PEC byte following the data byte. The data is regarded
as valid only if the PEC bytes match.


For the serial port read sequence, the LTC7871 calculates
PEC byte for the received address byte and data byte it
sends out. The LTC7871 latches the PEC byte at the 15th
clock falling edge and attaches the calculated PEC byte
following the data byte it shifts out. The master calculates
PEC byte for the address byte it sends and data byte it
receives. The master latches the PEC byte at the 16th
clock rising edge and compares it with the PEC byte fol­
lowing the data byte it receivers. The data is regarded as
valid only if the PEC bytes match.



|CLOCK<br>CYCLE|DIN|IN0|IN1|IN2|PEC[7]|PEC[6]|PEC[5]|PEC[4]|PEC[3]|PEC[2]|PEC[1]|PEC[0]|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|1|0|0|1|0|0|0|0|0|1|
|1|0|1|1|0|1|0|0|0|0|0|1|0|
|2|0|0|1|1|0|0|0|0|0|0|1|1|
|3|0|0|0|1|0|0|0|0|0|1|1|0|
|4|0|0|0|0|0|0|0|0|1|1|0|0|
|5|0|0|0|0|0|0|0|1|1|0|0|0|
|6|0|0|0|0|0|0|1|1|0|0|0|0|
|7|1|1|1|1|0|1|1|0|0|0|0|0|
|8|||||1|1|0|0|0|1|1|1|


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 33


## LTC7871

### **APPLICATIONS INFORMATION**



Rev. B


# 34



[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

### **APPLICATIONS INFORMATION**

**Multidrop Configuration**


Several LTC7871s may share the serial bus. In this multidrop configuration, SCLK, SDI, and SDO are common between
all parts. The serial bus master must use a separate CSB for each LTC7871 and ensure that only one device has CSB
asserted at any time during the serial port read sequence. It is recommended to attach a high value resistor to SDO to
ensure the line returns to a known level during Hi-Z states.


**Serial Port Register Definition**


**Table 7. Register Summary**









|Register NAME|Register<br>Address<br>(7 bits)|Description|TYPE|DEFAULT<br>VALUE|
|---|---|---|---|---|
|MFR_FAULT|0x01|One byte summary of the unit’s fault condition.|R||
|MFR_OC_FAULT|0x02|One byte summary of the unit’s overcurrent fault condition.|R||
|MFR_NOC_FAULT|0x03|One byte summary of the unit’s negative overcurrent fault condition.|R||
|MFR_STATUS|0x04|One byte summary of the unit’s operation status.|R||
|MFR_CONFIG1|0x05|One byte summary of the unit’s configuration|R||
|MFR_CONFIG2|0x06|One byte summary of the unit’s configuration|R||
|MFR_CHIP_CTRL|0x07|[3] = Communication Fault, [1] = Sticky Bit, [0] = Write Protection|R/W|0x00|
|MFR_IDAC_VLOW|0x08|Adjust the IDAC_VLOW to program VLOW voltage.|R/W|0x00|
|MFR_IDAC_VHIGH|0x09|Adjust the IDAC_VHIGH to program VHIGH voltage.|R/W|0x00|
|MFR_IDAC_SETCUR|0x0A|Adjust the IDAC_SETCUR to program SETCUR pin’s sourcing current.|R/W|0x00|
|MFR_SSFM|0x0B|Adjust the spread spectrum frequency modulation parameters.|R/W|0x00|
|RESERVED|0x0C<br>0x0D<br>0x0E<br>0x0F||||


**SERIAL PORT REGISTER DETAILS**


_**MFR_FAULT**_


The MFR_FAULT returns a one-byte summary of the most critical faults.


**MFR_FAULT Register Contents:**

|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7|||Reserved|
|6|VLOW_OV|1|The OVLOW pin is higher than 1.2V threshold.|
|5|VHIGH_OV|1|The OVHIGH pin is higher than 1.2V threshold.|
|4|VHIGH_UV|1|The UVHIGH pin is less than 1.2V threshold.|
|3|DRVCC_UV|1|The DRVCC pin is undervoltage.|
|2|V5_UV|1|The V5 pin is undervoltage.|
|1|VREF_BAD|1|The internal reference self-check fails.|
|0|OVER_TEMP|1|An over temperature fault has occurred.|



Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 35


## LTC7871

### **APPLICATIONS INFORMATION**

_**MFR_OC_FAULT**_


The MFR_OC_FAULT returns a one-byte summary of overcurrent fault condition. When the voltage difference between
SNSD [+] and SNS [–] pins is larger than the overcurrent fault threshold programmed by the ILIM pin, the corresponding
register bit will become 1.


**MFR_OC_FAULT Register Contents:**

|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:6|||Reserved|
|5|OC_FAULT_6|1|Channel 6 overcurrent fault has occurred.|
|4|OC_FAULT_5|1|Channel 5 overcurrent fault has occurred.|
|3|OC_FAULT_4|1|Channel 4 overcurrent fault has occurred.|
|2|OC_FAULT_3|1|Channel 3 overcurrent fault has occurred.|
|1|OC_FAULT_2|1|Channel 2 overcurrent fault has occurred.|
|0|OC_FAULT_1|1|Channel 1 overcurrent fault has occurred.|



_**MFR_NOC_FAULT**_


The MFR_NOC_FAULT returns a one-byte summary of negative overcurrent fault condition. When the voltage difference
between SNSD [+] and SNS [–] pins is less than the negative overcurrent fault threshold programmed by the ILIM pin, the
corresponding register bit will become 1.


**MFR_NOC_FAULT Register Contents:**

|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:6|||Reserved|
|5|NOC_FAULT_6|1|Channel 6 negative overcurrent fault has occurred.|
|4|NOC_FAULT_5|1|Channel 5 negative overcurrent fault has occurred.|
|3|NOC_FAULT_4|1|Channel 4 negative overcurrent fault has occurred.|
|2|NOC_FAULT_3|1|Channel 3 negative overcurrent fault has occurred.|
|1|NOC_FAULT_2|1|Channel 2 negative overcurrent fault has occurred.|
|0|NOC_FAULT_1|1|Channel 1 negative overcurrent fault has occurred.|



Rev. B


# 36



[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

### **APPLICATIONS INFORMATION**

_**MFR_STATUS**_


The MFR_STATUS returns a one-byte summary of the operation status. The content of the MFR_STATUS register is
read only.


**MFR_STATUS Register Contents:**

|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:3|||Reserved|
|2|SS_DONE|1|The soft-start is finished.|
|1|MAX_CURRENT|1|The maximum current programmed by the ILIM pin is reached.|
|0|PGOOD|1|The regulated VLOW/VHIGH is within ±10% regulation windows.|



_**MFR_CONFIG1**_


The MFR_CONFIG1 returns a one-byte summary of the configuration of the controller programmed by the pins. The
content of the MFR_CONFIG1 register is read only.


**MFR_CONFIG1 Register Contents:**





|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:6|||Reserved|
|5|SERCUR_WARNING|1|The SETCUR pin is programmed to be above 1.25V.|
|4:3|DRVCC_SET[1:0]|00<br>01<br>10|The DRVCC is programmed to 5V.<br>The DRVCC is programmed to 8V.<br>The DRVCC is programmed to 10V.|
|2:0|ILIM_SET[2:0]|000<br>001<br>010<br>011<br>100|The maximum current sense threshold is programmed to 10mV.<br>The maximum current sense threshold is programmed to 20mV.<br>The maximum current sense threshold is programmed to 30mV.<br>The maximum current sense threshold is programmed to 40mV.<br>The maximum current sense threshold is programmed to 50mV.|


[For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B
# 37


## LTC7871

### **APPLICATIONS INFORMATION**

_**MFR_CONFIG2**_


The MFR_CONFIG2 returns a one-byte summary of the
configuration of the controller programmed by the pins.
The content of the MFR_CONFIG2 register is read only.


**MFR_CONFIG2 Register Contents:**



|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:5|||Reserved|
|4|BURST|1|The controller is in burst mode operation.|
|3|DCM|1|The controller is in DCM.|
|2|HIZ|1|The controller is in Hi-Z mode.|
|1|SPRD|1|The controller is in spread spectrum mode.|
|0|BUCK_BOOST|0
<br>1|The controller is in boost mode.<br>The controller is in buck mode.|


_**MFR_CHIP_CTRL**_





The MFR_CHIP_CTRL is for general chip control.


**MFR_CHIP_CTRL Message Contents:**



|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:3|||Reserved|
|2|CML|1|A communication fault related to PEC during writing registers has occurred. Write 1 to this bit will clear the CML.|
|1|RESET|1|Sticky bit, reset all R/W registers.|
|0|WP|0
<br>1|Write allowed for all three IDAC registers, and MFR_SSFM register.<br>Write inhibited for all three IDAC registers, and MFR_SSFM register.|

# 38



[For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B


## LTC7871

### **APPLICATIONS INFORMATION**

_**MFR_IDAC_VLOW**_


The MFR_IDAC_VLOW stores the current DAC value to program the V LOW voltage by injecting the current DAC output
to the VFB LOW pin. It is formatted as a 7-bit two’s complement value. Setting BIT[6] = 0 means sourcing current from
the VFB LOW pin; and BIT[6] = 1 means sinking current. The detail is listed in Table 8. The DAC current is only injected
to the VFB LOW pin in buck mode. Sinking current will cause V LOW to rise. The default value for this register is 0x00.
Writes to this register are inhibited when the WP, BIT[0] in MFR_CHIP_CTRL, is set high.


**MFR_IDAC_VLOW Message Contents:**



|BIT|VALUE|MEANING|
|---|---|---|
|7||Reserved|
|6|0
<br>1|0µA<br>–64µA|
|5|0
<br>1|0µA<br>32µA|
|4|0
<br>1|0µA<br>16µA|
|3|0
<br>1|0µA<br>8µA|
|2|0
<br>1|0µA<br>4µA|
|1|0
<br>1|0µA<br>2µA|
|0|0
<br>1|0µA<br>1µA|


_**MFR_IDAC_VHIGH**_





The MFR_IDAC_VHIGH stores the current DAC value to program the V HIGH voltage by injecting the current DAC output
to the VFB HIGH pin. It is formatted as a 7-bit two’s complement value. Setting BIT[6] = 0 means sourcing current from
the VFB HIGH pin; and BIT[6] = 1 means sinking current. The detail is listed in Table 8. The DAC current is only injected
to the VFB HIGH pin in boost mode. Sinking current will cause V HIGH to rise in boost mode. The default value for this
register is 0x00. Writes to this register are inhibited when the WP, BIT[0] in MFR_CHIP_CTRL, is set high.


**MFR_IDAC_VHIGH Message Contents:**






|BIT|VALUE|MEANING|
|---|---|---|
|7||Reserved|
|6|0
<br>1|0µA<br>–64µA|
|5|0
<br>1|0µA<br>32µA|
|4|0
<br>1|0µA<br>16µA|
|3|0
<br>1|0µA<br>8µA|
|2|0
<br>1|0µA<br>4µA|
|1|0
<br>1|0µA<br>2µA|
|0|0
<br>1|0µA<br>1µA|



[For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B
# 39


## LTC7871

### **APPLICATIONS INFORMATION**

_**MFR_IDAC_SETCUR**_


The MFR_IDAC_SETCUR stores the current DAC value to program the sourcing current of the SETCUR pin. It is for­
matted as a 5-bit two’s complement value. The default value for this register is 0x00 and the SETCUR pin originally
sources 16µA. This register can program the SETCUR pin sourcing current from 0 to 31µA as shown in the Table 9.
Writes to this register are inhibited when the WP, BIT[0] in MFR_CHIP_CTRL, is set high.


**MFR_IDAC_SETCUR Message Contents:**



|BIT|VALUE|MEANING|
|---|---|---|
|7:5||RESERVED|
|4|0
<br>1|16µA<br>0µA|
|3|0
<br>1|0µA<br>8µA|
|2|0
<br>1|0µA<br>4µA|
|1|0
<br>1|0µA<br>2µA|
|0|0
<br>1|0µA<br>1µA|


_**MFR_SSFM**_





The MFR_SSFM is for spread spectrum frequency modulation control. The default value for this register is 0x00. Writes
to this register are inhibited when the WP, BIT[0] in MFR_CHIP_CTRL, is set high.


**MFR_SSFM Message Contents:**



|BIT|NAME|VALUE|MEANING|
|---|---|---|---|
|7:5|||Reserved|
|4:3|Frequency Spread<br>Range|00|±12%|
|4:3|Frequency Spread<br>Range|01|±15%|
|4:3|Frequency Spread<br>Range|10|±10%|
|4:3|Frequency Spread<br>Range|11|±8%|
|2:0|Modulation Signal<br>Frequency|000|Controller Switching Frequency/512|
|2:0|Modulation Signal<br>Frequency|001|Controller Switching Frequency/1024|
|2:0|Modulation Signal<br>Frequency|010|Controller Switching Frequency/2048|
|2:0|Modulation Signal<br>Frequency|011|Controller Switching Frequency/4096|
|2:0|Modulation Signal<br>Frequency|100|Controller Switching Frequency/256|
|2:0|Modulation Signal<br>Frequency|101|Controller Switching Frequency/128|
|2:0|Modulation Signal<br>Frequency|110|Controller Switching Frequency/64|
|2:0|Modulation Signal<br>Frequency|111|Controller Switching Frequency/512|

# 40



[For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B


### **APPLICATIONS INFORMATION**

**Table 8. VFB** **LOW** **/VFB** **HIGH** **PIN Current and Corresponding DAC Codes**


## LTC7871

**Table 8. VFB** **LOW** **/VFB** **HIGH** **PIN Current and Corresponding DAC Codes**

|MFR_IDAC_V /MFR_IDAC_V<br>LOW HIGH|Col2|Col3|Col4|Col5|Col6|Col7|I (µA)<br>VFBLOW/VFBHIGH|
|---|---|---|---|---|---|---|---|
|**[6]**|**[5]**|**[4]**|**[3]**|**[2]**|**[1]**|**[0]**|**[0]**|
|1|1|0|0|0|0|0|–32|
|1|1|0|0|0|0|1|–31|
|1|1|0|0|0|1|0|–30|
|1|1|0|0|0|1|1|–29|
|1|1|0|0|1|0|0|–28|
|1|1|0|0|1|0|1|–27|
|1|1|0|0|1|1|0|–26|
|1|1|0|0|1|1|1|–25|
|1|1|0|1|0|0|0|–24|
|1|1|0|1|0|0|1|–23|
|1|1|0|1|0|1|0|–22|
|1|1|0|1|0|1|1|–21|
|1|1|0|1|1|0|0|–20|
|1|1|0|1|1|0|1|–19|
|1|1|0|1|1|1|0|–18|
|1|1|0|1|1|1|1|–17|
|1|1|1|0|0|0|0|–16|
|1|1|1|0|0|0|1|–15|
|1|1|1|0|0|1|0|–14|
|1|1|1|0|0|1|1|–13|
|1|1|1|0|1|0|0|–12|
|1|1|1|0|1|0|1|–11|
|1|1|1|0|1|1|0|–10|
|1|1|1|0|1|1|1|–9|
|1|1|1|1|0|0|0|–8|
|1|1|1|1|0|0|1|–7|
|1|1|1|1|0|1|0|–6|
|1|1|1|1|0|1|1|–5|
|1|1|1|1|1|0|0|–4|
|1|1|1|1|1|0|1|–3|
|1|1|1|1|1|1|0|–2|
|1|1|1|1|1|1|1|–1|



Rev. B


|MFR_IDAC_V /MFR_IDAC_V<br>LOW HIGH|Col2|Col3|Col4|Col5|Col6|Col7|I (µA)<br>VFBLOW/VFBHIGH|
|---|---|---|---|---|---|---|---|
|**[6]**|**[5]**|**[4]**|**[3]**|**[2]**|**[1]**|**[0]**|**[0]**|
|1|0|0|0|0|0|0|–64|
|1|0|0|0|0|0|1|–63|
|1|0|0|0|0|1|0|–62|
|1|0|0|0|0|1|1|–61|
|1|0|0|0|1|0|0|–60|
|1|0|0|0|1|0|1|–59|
|1|0|0|0|1|1|0|–58|
|1|0|0|0|1|1|1|–57|
|1|0|0|1|0|0|0|–56|
|1|0|0|1|0|0|1|–55|
|1|0|0|1|0|1|0|–54|
|1|0|0|1|0|1|1|–53|
|1|0|0|1|1|0|0|–52|
|1|0|0|1|1|0|1|–51|
|1|0|0|1|1|1|0|–50|
|1|0|0|1|1|1|1|–49|
|1|0|1|0|0|0|0|–48|
|1|0|1|0|0|0|1|–47|
|1|0|1|0|0|1|0|–46|
|1|0|1|0|0|1|1|–45|
|1|0|1|0|1|0|0|–44|
|1|0|1|0|1|0|1|–43|
|1|0|1|0|1|1|0|–42|
|1|0|1|0|1|1|1|–41|
|1|0|1|1|0|0|0|–40|
|1|0|1|1|0|0|1|–39|
|1|0|1|1|0|1|0|–38|
|1|0|1|1|0|1|1|–37|
|1|0|1|1|1|0|0|–36|
|1|0|1|1|1|0|1|–35|
|1|0|1|1|1|1|0|–34|
|1|0|1|1|1|1|1|–33|



[For more information LTC7871](http://www.linear.com/LTC7871)


# 41


## LTC7871

### **APPLICATIONS INFORMATION**

**Table 8. VFB** **LOW** **/VFB** **HIGH** **PIN Current and Corresponding DAC Codes**



**Table 8. VFB** **LOW** **/VFB** **HIGH** **PIN Current and Corresponding DAC Codes**

|MFR_IDAC_V /MFR_IDAC_V<br>LOW HIGH|Col2|Col3|Col4|Col5|Col6|Col7|I (µA)<br>VFBLOW/VFBHIGH|
|---|---|---|---|---|---|---|---|
|**[6]**|**[5]**|**[4]**|**[3]**|**[2]**|**[1]**|**[0]**|**[0]**|
|0|1|0|0|0|0|0|32|
|0|1|0|0|0|0|1|33|
|0|1|0|0|0|1|0|34|
|0|1|0|0|0|1|1|35|
|0|1|0|0|1|0|0|36|
|0|1|0|0|1|0|1|37|
|0|1|0|0|1|1|0|38|
|0|1|0|0|1|1|1|39|
|0|1|0|1|0|0|0|40|
|0|1|0|1|0|0|1|41|
|0|1|0|1|0|1|0|42|
|0|1|0|1|0|1|1|43|
|0|1|0|1|1|0|0|44|
|0|1|0|1|1|0|1|45|
|0|1|0|1|1|1|0|46|
|0|1|0|1|1|1|1|47|
|0|1|1|0|0|0|0|48|
|0|1|1|0|0|0|1|49|
|0|1|1|0|0|1|0|50|
|0|1|1|0|0|1|1|51|
|0|1|1|0|1|0|0|52|
|0|1|1|0|1|0|1|53|
|0|1|1|0|1|1|0|54|
|0|1|1|0|1|1|1|55|
|0|1|1|1|0|0|0|56|
|0|1|1|1|0|0|1|57|
|0|1|1|1|0|1|0|58|
|0|1|1|1|0|1|1|59|
|0|1|1|1|1|0|0|60|
|0|1|1|1|1|0|1|61|
|0|1|1|1|1|1|0|62|
|0|1|1|1|1|1|1|63|



Rev. B


|MFR_IDAC_V /MFR_IDAC_V<br>LOW HIGH|Col2|Col3|Col4|Col5|Col6|Col7|I (µA)<br>VFBLOW/VFBHIGH|
|---|---|---|---|---|---|---|---|
|**[6]**|**[5]**|**[4]**|**[3]**|**[2]**|**[1]**|**[0]**|**[0]**|
|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|1|1|
|0|0|0|0|0|1|0|2|
|0|0|0|0|0|1|1|3|
|0|0|0|0|1|0|0|4|
|0|0|0|0|1|0|1|5|
|0|0|0|0|1|1|0|6|
|0|0|0|0|1|1|1|7|
|0|0|0|1|0|0|0|8|
|0|0|0|1|0|0|1|9|
|0|0|0|1|0|1|0|10|
|0|0|0|1|0|1|1|11|
|0|0|0|1|1|0|0|12|
|0|0|0|1|1|0|1|13|
|0|0|0|1|1|1|0|14|
|0|0|0|1|1|1|1|15|
|0|0|1|0|0|0|0|16|
|0|0|1|0|0|0|1|17|
|0|0|1|0|0|1|0|18|
|0|0|1|0|0|1|1|19|
|0|0|1|0|1|0|0|20|
|0|0|1|0|1|0|1|21|
|0|0|1|0|1|1|0|22|
|0|0|1|0|1|1|1|23|
|0|0|1|1|0|0|0|24|
|0|0|1|1|0|0|1|25|
|0|0|1|1|0|1|0|26|
|0|0|1|1|0|1|1|27|
|0|0|1|1|1|0|0|28|
|0|0|1|1|1|0|1|29|
|0|0|1|1|1|1|0|30|
|0|0|1|1|1|1|1|31|


# 42



[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

**Table 9. SETCUR Pin Current and Corresponding DAC Codes**


## LTC7871

**Table 9. SETCUR Pin Current and Corresponding DAC Codes**

|MFR_IDAC_SETCUR[4:0]|Col2|Col3|Col4|Col5|I (µA)<br>SETCUR|
|---|---|---|---|---|---|
|**[4]**|**[3]**|**[2]**|**[1]**|**[0]**|**[0]**|
|0|0|0|0|0|16|
|0|0|0|0|1|17|
|0|0|0|1|0|18|
|0|0|0|1|1|19|
|0|0|1|0|0|20|
|0|0|1|0|1|21|
|0|0|1|1|0|22|
|0|0|1|1|1|23|
|0|1|0|0|0|24|
|0|1|0|0|1|25|
|0|1|0|1|0|26|
|0|1|0|1|1|27|
|0|1|1|0|0|28|
|0|1|1|0|1|29|
|0|1|1|1|0|30|
|0|1|1|1|1|31|



Rev. B


|MFR_IDAC_SETCUR[4:0]|Col2|Col3|Col4|Col5|I (µA)<br>SETCUR|
|---|---|---|---|---|---|
|**[4]**|**[3]**|**[2]**|**[1]**|**[0]**|**[0]**|
|1|0|0|0|0|0|
|1|0|0|0|1|1|
|1|0|0|1|0|2|
|1|0|0|1|1|3|
|1|0|1|0|0|4|
|1|0|1|0|1|5|
|1|0|1|1|0|6|
|1|0|1|1|1|7|
|1|1|0|0|0|8|
|1|1|0|0|1|9|
|1|1|0|1|0|10|
|1|1|0|1|1|11|
|1|1|1|0|0|12|
|1|1|1|0|1|13|
|1|1|1|1|0|14|
|1|1|1|1|1|15|



[For more information LTC7871](http://www.linear.com/LTC7871)


# 43


## LTC7871

### **APPLICATIONS INFORMATION**

**PC Board Layout Checklist**


When laying out the printed circuit board, the following
checklist should be used to ensure proper operation of
the IC. These items are also illustrated graphically in the
layout diagram of Figure 15. Check the following in the
PC layout:


1. The DRV CC bypass capacitor should be placed imme­

diately adjacent to the IC between the DRV CC pin and
the GND plane. A 1μF ceramic capacitor of the X7R or
X5R type is small enough to fit very close to the IC. An
additional 4.7μF to 10μF of ceramic, tantalum or other
very low ESR capacitance is recommended in order to
keep the internal IC supply quiet.


2. The V5 bypass capacitor should be placed immediately

adjacent to the IC between the V5 and the SGND pins.
A 4.7μF to 10μF capacitor of ceramic, tantalum or other
very low ESR capacitance is recommended.


3. Place the feedback divider between the + and – terminals

of C LOW /C HIGH . Route VFB LOW /VFB HIGH with minimum
PC trace spacing from the IC to the feedback dividers.


4. Are the SNSA [+], SNSD [+] and SNS [–] printed circuit traces

routed together with minimum PC trace spacing? The
filter capacitors between SNSA [+,] SNSD [+] and SNS [–]
should be as close as possible to the pins of the IC.


5. Do the (+) plates of C HIGH decoupling cap connect to

the drain of the topside MOSFET as closely as pos­
sible? This capacitor provides the pulsed current to
the MOSFET.



6. Keep the switching nodes away from sensitive small
signal nodes (SNSD [+], SNSA [+], SNS [–], V FB ). Ideally the
switch nodes printed circuit traces should be routed
away and separated from the IC and especially the
quiet side of the IC. Separate the high dV/dt traces
from sensitive small-signal nodes with ground traces
or ground planes.


7. Use a low impedance source such as a logic gate to

drive the SYNC pin and keep the PCB trace as short
as possible.


8. The ceramic capacitors between each ITH pin and sig­

nal ground should be placed as close as possible to
the IC. Figure 15 illustrates all branch currents in a
switching regulator. It becomes very clear after study­
ing the current waveforms why it is critical to keep
the high switching current paths to a small physical
size. High electric and magnetic fields will radiate from
these loops just as radio stations transmit signals. The
C LOW ground should return to the negative terminal of
C HIGH and not share a common ground path with any
switched current paths. The left half of the circuit gives
rise to the noise generated by a switching regulator.
The ground terminations of the bottom MOSFET and
Schottky diode should return to the bottom plate(s) of
the V HIGH capacitor(s) with a short isolated PC trace
since very high switched currents are present. External
OPTI-LOOP [®] compensation allows overcompensation
for PC layouts which are not optimized, but this is not
the recommended design procedure.

















R LOW



Rev. B


# 44



7871 F15

BOLD LINES INDICATE HIGH, SWITCHING CURRENTS. KEEP LINES TO A MINIMUM LENGTH


**Figure 15. Branch Current Waveforms (Buck Mode Shown)**


[For more information LTC7871](http://www.linear.com/LTC7871)


### **APPLICATIONS INFORMATION**

**Special Layout Consideration**


Exceeding Absolute Max ratings on the EXTV CC pin can
result in damage to the controller. As the EXTV CC pin is
normally connected to V LOW, it is recommended to put
a Schottky diode with an appropriately high voltage rat­
ing between the V LOW and the EXTV CC pins as shown in
Figure 16(a). Choose the right Schottky diode with the
forward voltage less than 0.5V at the maximum EXTV CC
pin current.


Another method to protect on the EXTV CC pin is to use a
Schottky diode to clamp the EXTV CC pin to reduce volt­
age spiking below ground. The Schottky diode should be
placed close to the controller IC, with the cathode con­
nected to the EXTV CC pin and the anode connected to
ground as shown in the Figure 16(b). Choose a minimum
1Ω R FLTR and keep the maximum voltage drop across the
R FLTR less than 0.5V.


## LTC7871

(30A/phase), and f = 150kHz. The regulated output voltage
is determined by:


V LOW = 1.2V • (1 + R B /R A ).


Using a 10k 1% resistor from the VFB LOW node to ground,
the top feedback resistor is (to the nearest 1% standard
value) 90.9k. The frequency is set by selecting the R FREQ
to be 37.4kΩ. The inductance values are based on a 35%
maximum ripple current assumption (10.5A for each
phase). The highest value of ripple current occurs at the
maximum V HIGH voltage:



V
L = LOW
f•∆I
L MAX ( )



V

⎛ LOW ⎞

- 1–
V

⎝ [⎜] HIGH MAX ( ) ⎠ [⎟]



Each phase will require 6.1μH. The Sagami CVE2622C6R8M, 6.8μH, 1.8mΩ DCR inductor is chosen. At the
nominal V HIGH voltage (48V), the ripple current will be:



⎛



⎠ [⎟]





V

⎛ LOW

∆I L NOM ( ) [=] [V] [LOW]
f•L [• 1–] V

⎝ [⎜] HIGH NOM ( )



V

⎛ LOW ⎞

V

⎝ [⎜] HIGH NOM ( ) ⎠ [⎟]



**(a)**


**(b)**


**Figure 16. Methods to Protect the EXTV** **CC** **Pin**


**Design Example**


As a design example for a six-phase single output
high current regulator, assume V HIGH = 48V (nominal),
V HIGH = 60V (maximum), V LOW = 12V, I VLOW(MAX) = 180A



Each phase will have 8.8A (29.3%) ripple. The peak induc­
tor current will be the maximum DC value plus one-half the
ripple current, or 34.4A. The minimum on-time occurs at
the maximum V HIGH, and should not be less than 150ns:


V 12V
T ON MIN ( ) [=] LOW
V HIGH MAX ( ) [•f] [=] 60V •150kHz [=] [1.33µs]


With V ILIM = 3/4 V V5, the equivalent R SENSE resistor value
can be calculated by using the minimum value for the
maximum current sense threshold (45mV):


V
SENSE MIN( )
R SENSE EQUIV ( ) [=] I ∆I
LOAD MAX( ) L NOM ( )
#OF PHASES [+] 2


The equivalent required R SENSE value is 1.31mΩ. Choose
R S = 1mΩ to allow some design margin. As shown in
Figure 17, set R2 to be below 1/10th of the R1. Therefore,
the DC component of the SNSA [+] filter is small enough to
be omitted. R1 • C1 should have a bandwidth that is four
times as high as the L/R S .


Rev. B



[For more information LTC7871](http://www.linear.com/LTC7871)


# 45


## LTC7871

### **APPLICATIONS INFORMATION**

Typically, C1 is selected in the range of 0.047μF to 0.47μF.
If C1 is chosen to be 0.1μF, R1 and R2 will be 16.9kΩ
and 1.69kΩ respectively. The bias current at SNSD [+] and
SNSA [+] is about 50nA, and it causes some small error to
the current sense signal. If C2 is also chosen to be 0.1μF,
R3 will be 1.5kΩ.


SNSD [+]



⎫

⎪
⎬ - 2

⎪
⎭



P
SYNC =



⎧ 48V –12V

     - 15A [2]

⎪

48V

⎨
###### ⎪⎩• (1 [ + 0.005• 75 ( °C–25°C ) )•5.2mΩ ]



LTC7871


SNS [–]


SNSA [+]


7871 F17













V LOW


|Col1|R3 1.5k|Col3|
|---|---|---|
||C2<br>0.1µF|C2<br>0.1µF|
||C1<br>0.1µF|RS<br>1mΩ|



+


**Figure 17. R** **SENSE** **Resistor Sensing in Design Example**


The power dissipation on the top MOSFET can be eas­
ily estimated. Set the gate drive voltage (DRV CC ) to be
10V. Choosing two Infineon BSC117N08NS5 MOSFETs
results in:


R DS(ON) = 11.7mΩ (max),

V MILLER = 5V, C MILLER ≅ 19pF.


At typical V HIGH voltage with T J (estimated) = 75°C:



= 1.1W { }    - 2


= 2.2W


C HIGH is chosen for an equivalent RMS current rating of
at least 20A. C LOW is chosen with an equivalent ESR of
10mΩ for low output ripple. The V LOW output ripple in
continuous mode will be highest at the maximum V HIGH
voltage. The V LOW output voltage ripple due to ESR
is approximately:


V LOWRIPPLE = R ESR - ΔI L = 0.01Ω • 8.8A = 88mV


Further reductions in V LOW output voltage ripple can be
made by placing ceramic capacitors across C LOW .


If the output load is a battery, the voltage loop is first set
for the desired output voltage and then the charge current
can be regulated using the current regulation loop—via
the SETCUR and IMON pins. Selecting a maximum charge
current of 120A, the desired SETCUR pin voltage is cal­
culated using:



12V ⎫
48V [•15A] [2] ⎪

⎪

° ° ⎪
###### • (1 [ + 0.005• 75 ( C–25 C ) )•11.7mΩ ]

⎪⎪

⎬

+48V [2] - [15A] ⎪
2 [•4][Ω] [•19pF]

⎪
⎪

- ⎛ 1 [1] ⎞ ⎪
⎝ [⎜] 10 − 5 [+] 5⎠ [⎟] [•150k] ⎪⎭



V
SETCUR =



K •I L MAX ( ) [•R] SENSE

6



P MAIN =



⎧

⎪
⎪
⎪
⎪⎪

⎨

⎪
⎪
⎪
⎪
⎪⎩




- 2



= 823mW { + 79mW }    - 2


= 1804mW


Two Infineon BSC052N08NS5 MOSFETs, R DS(ON) =
5.2mΩ, C OSS = 370pF are chosen for the bottom MOSFET.
The resulting power loss is:



= [20•120A •1m][Ω]
6

= 400mV


The SETCUR pin can be driven by an ADC’s output to
400mV for the best accuracy. If one is not available, the
16μA current sourced out of the SETCUR pin can be used
to set the voltage with a resistor from SETCUR to ground,
calculated using:


R [400mV]
SETCUR = 16µA [=][ 25k]


A 1% or more accurate 30.1k resistor can be chosen to
allow some design margin. The 16μA current out of the
SETCUR pin can be programmed by the SPI interface so
the maximum charge current can be changed on-the-fly.


Rev. B


# 46



[For more information LTC7871](http://www.linear.com/LTC7871)


### **TYPICAL APPLICATIONS**


|TG VCC EN SW FLT BG PWM|BGRTN 1µF DT SGND|
|---|---|
|PWMEN<br>0.22µF<br>0Ω<br>|PWMEN<br>0.22µF<br>0Ω<br>|


|BGV V|VCC EN FLT PW|
|---|---|
|10Ω|PWMEN<br>0.22µF<br>|
|10Ω||


|BGV V|VCC EN FLT PW|
|---|---|
|10Ω|PWMEN<br>0.22µF<br>|
|10Ω||


|0.1µF 1.69k|Col2|
|---|---|
|0.1µF<br>1.69k<br><br>||


|10Ω|0.22µF|
|---|---|
|10Ω|PWMEN<br>|


|10Ω|0.22µF|
|---|---|
|10Ω|PWMEN<br>|


|Col1|PWMEN 0.22 0Ω 10Ω|
|---|---|
||BST<br>TG<br>SW<br>BG<br>BGRTN<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>DT<br>SGND<br>LTC7060|
|||
|||


|Col1|PWMEN 0Ω|
|---|---|
||BST<br>TG<br>SW<br>BG<br>BGRTN<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>DT<br>SGND<br>LTC7060|
|||
|||


|1µF 210k 499k 48.7k 10k 12.7k 37.4k|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|1µF<br>499k<br>12.7k<br>210k<br>10k<br>48.7k<br>37.4k|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|
|1µF<br>499k<br>12.7k<br>210k<br>10k<br>48.7k<br>37.4k|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|M9<br>×2<br>M10<br>×2<br>M7<br>×2<br>M8<br>×2<br>BGRTN<br>DT<br>SGND<br>0.1µF<br>1.69k<br>1µF<br>0.22µF<br>D5<br>0.22µF<br>D4<br><br>BST<br>TG<br>SW<br>BG<br>BGRTN<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>DT<br>SGND<br>PWMEN<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>L5<br>6.8µH<br>VHIGH<br>LTC7060<br>0.22µF<br>1µF<br>0Ω<br>10Ω<br>DRVCC<br>BST<br>TG<br>SW<br>BG<br>BGRTN<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>DT<br>SGND<br>PWMEN<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>L4<br>6.8µH<br>VHIGH<br>LTC7060<br>0.22µF<br>1µF<br>0Ω<br>10Ω<br>DRVCC<br>PWMEN<br>10k<br>V5<br>V5|M9<br>×2<br>M10<br>×2<br>M7<br>×2<br>M8<br>×2<br>BGRTN<br>DT<br>SGND<br>0.1µF<br>1.69k<br>1µF<br>0.22µF<br>D5<br>0.22µF<br>D4<br><br>BST<br>TG<br>SW<br>BG<br>BGRTN<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>DT<br>SGND<br>PWMEN<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>L5<br>6.8µH<br>VHIGH<br>LTC7060<br>0.22µF<br>1µF<br>0Ω<br>10Ω<br>DRVCC<br>BST<br>TG<br>SW<br>BG<br>BGRTN<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>DT<br>SGND<br>PWMEN<br>0.1µF<br>1.69k<br>1mΩ<br>16.9k<br>0.1µF<br>1.5k<br>L4<br>6.8µH<br>VHIGH<br>LTC7060<br>0.22µF<br>1µF<br>0Ω<br>10Ω<br>DRVCC<br>PWMEN<br>10k<br>V5<br>V5|0.1µF<br>1.69k<br><br>||||
|1µF<br>499k<br>12.7k<br>210k<br>10k<br>48.7k<br>37.4k|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|||||||
|1µF<br>499k<br>12.7k<br>210k<br>10k<br>48.7k<br>37.4k|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|||||||
|1µF<br>499k<br>12.7k<br>210k<br>10k<br>48.7k<br>37.4k|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|0.1µF<br>1.69k||||||
|1µF<br>499k<br>12.7k<br>210k<br>10k<br>48.7k<br>37.4k|M11<br>×2<br>M12<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>PWMEN<br>1mΩ<br>16.9k<br>1.5k<br>L6<br>6.8µH<br>VHIGH<br>22µF<br>×6<br>110k<br>10k<br>1µF<br>LTC7060<br>0.22µF<br>0.22µF<br>D6<br>0Ω<br>10Ω<br>DRVCC<br>0.1µF<br>D7|BGRTN<br>DT<br>SGND<br>1µF<br>|BGRTN<br>DT<br>SGND<br>1µF<br>|BGRTN<br>DT<br>SGND<br>1µF<br>|BGRTN<br>DT<br>SGND<br>1µF<br>|BGRTN<br>DT<br>SGND<br>1µF<br>|BGRTN<br>DT<br>SGND<br>1µF<br>|
|210k|210k|210k|210k|210k|210k|210k|210k|
|||||||||
|1µF|1µF|1µF|1µF|1µF|1µF|1µF|1µF|
|1µF|1µF|1µF|1µF|1µF|1µF|1µF|100pF|
|1µF|1µF|1µF|1µF|1µF|1µF|1µF|7871 TA02<br>PGOOD SGND<br><br><br>4.7µF|
|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|VFBLOW<br>OVLOW<br>EXTVCC<br>FREQ<br>CLKOUT<br>OVHIGH<br>UVHIGH<br>VFBHIGH<br>FAULT<br>ITHLOW<br>ILIM<br>V5<br>PWM6<br>SNSA6+<br>SNSD6+<br>SNS6–<br>ITHHIGH<br>BUCK<br>LTC7871<br>PWM5<br>SNSA5+<br>SNSD5+<br>SNS5–<br>PWM4<br>SNSA4+<br>SNSD4+<br>SNS4–<br>SDI<br>SDO<br>CSB<br>PWMEN<br>DRVSET<br>PWM1<br>SNSA1+<br>SNSD1+<br>SNS1–<br>PWM2<br>SNSA2+<br>SNSD2+<br>SNS2–<br>PWM3<br>SNSA3+<br>SNSD3+<br>SNS3–<br>SETCUR<br>SYNC<br>MODE<br>RUN<br>DRVCC<br>SS<br>IMON|
|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|BGRTN<br>DT<br>SGND<br>1µF<br>16.9k<br>||||51k<br>10k<br>V5|51k<br>10k<br>V5|
|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|BGRTN<br>DT<br>SGND<br>1µF<br>16.9k<br>||||51k<br>10k<br>V5|30.1k|
|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|0.1µF<br>1.69k|0.1µF<br>1.69k|0.1µF<br>1.69k|0.1µF<br>1.69k|0.1µF<br>1.69k|0.1µF<br>1.69k|
|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|**BOOST**<br>**BUCK**<br>M1<br>×2<br>M2<br>×2<br>BST<br>TG<br>SW<br>BG<br>BGVCC<br>VCC<br>EN<br>FLT<br>PWM<br>0.1µF<br>VHIGH<br>0.33µF<br>1nF<br>499Ω<br>0.1µF<br>47pF<br>499Ω<br>SPI<br>INTERFACE<br>LTC7060<br>PWMEN<br>0.22µF<br>0.22µF<br>DRVCC<br>1mΩ<br><br>1.5k<br>L1<br>6.8µH<br>0Ω<br>10Ω<br>D1<br>|||||||



[For more information LTC7871](http://www.linear.com/LTC7871)


## LTC7871

Rev. B
# 47


## LTC7871

### **PACKAGE DESCRIPTION**

**[Please refer to http://www.adi.com/designtools/packaging/ for the most recent package drawings.](https://www.analog.com/en/design-center/packaging-quality-symbols-footprints.html)**


**LWE Package**
**64-Lead Plastic Exposed Pad LQFP (10mm** × **10mm)**
(Reference LTC DWG #05-08-1982 Rev A)


0.50 BSC


0.20 – 0.30


10.15 – 10.25


|Col1|Col2|10.15 – 10.25<br>7.50 REF<br>64 4<br>1<br>5.74 ±0.05|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||7.50 REF<br>10.15– 10.25 <br>5.74 ±0.05<br>1<br>4<br>64|7.50 REF<br>10.15– 10.25 <br>5.74 ±0.05<br>1<br>4<br>64|7.50 REF<br>10.15– 10.25 <br>5.74 ±0.05<br>1<br>4<br>64||||
|||7.50 REF<br>10.15– 10.25 <br>5.74 ±0.05<br>1<br>4<br>64|7.50 REF<br>10.15– 10.25 <br>5.74 ±0.05<br>1<br>4<br>64|7.50 REF<br>10.15– 10.25 <br>5.74 ±0.05<br>1<br>4<br>64||4|4|
||||5.74 ±0.05|5.74 ±0.05|5.74 ±0.05|5.74 ±0.05|5.74 ±0.05|
|||||||||
|||||||||
|||||||||
|||||||||





1.30 MIN


1


16


C0.30 – 0.50

# 48



16 PACKAGE OUTLINE 33

17 32


RECOMMENDED SOLDER PAD LAYOUT
APPLY SOLDER MASK TO AREAS THAT ARE NOT SOLDERED


|12.00 BSC|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC||
|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|||||||||||||||||||||||
|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|||||||||||||||||||||||
|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC|49<br>64<br>SEE NOTE: 3<br>10.00 BSC<br>12.00 BSC||||||E|E|O||:|3||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
|||||||||||||||||||||||||A|||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
|50|50|50|||||||||||||||||||||||||
|50|50|50|||||||||||||||||||||||||
|50|50|50|||||||||||||||||||||||||


|49|Col2|Col3|Col4|Col5|Col6|Col7|5.74 ±0.10|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|64<br>1|Col27|Col28|Col29|Col30|Col31|Col32|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|49|49|49||||||||||||||||||||||||||||||
|49|49|49||||||||||||||||||||||||||||||
|49|49|49||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||
||||||||||0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27|0.17 – 0.27||LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|LWE64 LQFP 0416 REV A<br>0.05 – 0.15|



NOTE:
1. DIMENSIONS ARE IN MILLIMETERS 3. PIN-1 INDENTIFIER IS A MOLDED INDENTATION, 0.50mm DIAMETER
2. DIMENSIONS OF PACKAGE DO NOT INCLUDE MOLD FLASH. MOLD FLASH 4. DRAWING IS NOT TO SCALE
SHALL NOT EXCEED 0.25mm (10 MILS) BETWEEN THE LEADS AND
MAX 0.50mm (20 MILS) ON ANY SIDE OF THE EXPOSED PAD, MAX 0.77mm
(30 MILS) AT CORNER OF EXPOSED PAD, IF PRESENT


[For more information LTC7871](http://www.linear.com/LTC7871)









48





5.74 ±0.10


1.60
1.35 – 1.45 MAX



17 32


11° – 13°





32 17

BOTTOM OF PACKAGE—EXPOSED PAD (SHADED AREA)



11° – 13°


1.00 REF


0.45 – 0.75



SECTION A – A



BSC


SIDE VIEW



Rev. B


## LTC7871

### **REVISION HISTORY**



|REV|DATE|DESCRIPTION|PAGE NUMBER|
|---|---|---|---|
|A|07/21|Add Guarantee by Design to DRVCC/EXTVCC Peak Current in ABS MAX Rating section.<br>Add UNITS for V5 UVLO and EXTVCC Switchover Voltage parameters.<br>SYNC (Pin 52): Update internal resistor value.<br>Update EA_VLOW.<br>Update PTOP equation.<br>Update the external clock (on the SYNC pin) input low threshold voltage.<br>Update MFR_IDAC_VLOW and MFR_IDAC_VHIGH tables.<br>Update inductor’s name.|3<br>4, 5<br>10<br>12<br>24<br>28<br>38<br>44, 46|
|B|10/22|Updated Sync Pin Input Falling Threshold in Electrical Specifications.<br>Updated Block Diagram.|6<br>12|


Information furnished by Analog Devices is believed to be accurate and reliable. However, no responsibility is assumed by Analog
Devices for its use, nor for any infringements of patents or other rights of third parties that may result from its use. Specifications
[subject to change without notice. No license is granted by implication or otherwise under any patent or patent rights of Analog Devices.](http://www.linear.com/LTC7871) [For more information LTC7871](http://www.linear.com/LTC7871)



Rev. B
# 49


## LTC7871

### **TYPICAL APPLICATION**

**High Efficiency 6-Phase 24V/90A Bidirectional Supply**



V HIGH











































V LOW
24V/90A




|V5|Col2|Col3|Col4|
|---|---|---|---|
|1<br>V5|1<br>V5|1<br>V5|1<br>V5|
|+||499k|267k<br>3.01M|
|+||12.7k|10k<br>48.7k|


















|Col1|15µH|2m|
|---|---|---|
||0.1µF<br>1.87k<br>18.7k|1.69k|
||1.87k||
||||


|45.3k V5<br>51k<br>100pF 4.7µF<br>0.1µF 4.7µF 37.4k|Col2|Col3|Col4|
|---|---|---|---|
|V5<br>100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|
|V5<br>100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|
|V5<br>100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|V5<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k|51k<br>37.4k|
|V5<br>100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k||||
|V5<br>100pF<br>0.1µF<br>4.7µF<br>4.7µF<br>45.3k<br>51k<br>37.4k||||

















33µF
















|Col1|15µH|2mΩ|
|---|---|---|
||0.1µF<br>1.87k<br>18.7k<br>1.|0.1µF<br>69k|
||1.87k||
||||


### **RELATED PARTS**











|PART NUMBER|DESCRIPTION|COMMENTS|
|---|---|---|
|LTC7060|100V Half Bridge Gate Driver with Floating Grounds<br>and Programmable Dead-Time|Up to 100V Supply Voltage, 6V ≤ VCC ≤ 14V, Adaptive Shoot-Through<br>Protection, 2mm × 3mm LFCSP and 12-LEAD MSOP|
|LT8228|Bidirectional Buck or Boost Controller with Fault<br>Protection|Up to 100V for VHIGH, and VLOW, Ideal for 48V/12V Automotive Battery<br>Applications|
|LT8708/LT8708-1|80V Synchronous 4-Switch Buck-Boost DC/DC<br>Controller with Flexible Bidirectional Capability|2.8V ≤ VIN ≤ 80V, 1.3V ≤ VOUT ≤ 80V, PLL Fixed Frequency 100kHz to 400kHz,<br>5mm × 8mm QFN-40|
|LTC3871|Bidirectional PolyPhase Synchronous Buck or<br>Boost Controller|Up to 100V VHIGH, Up to 30V VLOW, PLL Fixed Frequency 60kHz to 460kHz,<br>48-Lead LQFP|
|LTC4449|High Speed Synchronous N-Channel MOSFET Driver|Up to 38V Supply Voltage, 4V ≤ VCC ≤ 6.5V, Adaptive Shoot-Through<br>Protection, 2mm × 3mm DFN-8|
|LTC3779|150V VIN and VOUT Synchronous 4-Switch<br>Buck-Boost Controller|4.5V ≤ VIN ≤ 150V, 1.2V ≤ VOUT ≤ 150V, PLL Fixed Frequency 50kHz to<br>600kHz, FE38 TSSOP|
|LTC7813|60V Low IQ Synchronous Boost+Buck Controller,<br>Low EMI and Low Input/Output Ripple|4.5V (Down to 2.2V After Start-Up) ≤ VIN ≤ 60V, Boost VOUT Up to 60V, 0.8V ≤<br>Buck VOUT ≤ 60V, IQ = 29µA, 5mm × 5mm QFN-32 Package|
|LTC3899|60V, Triple Output, Buck/Buck/Boost Synchronous<br>Controller with 29µA Burst Mode IQ|4.5V (Down to 2.2V after Start-Up) ≤ VIN ≤ 60V, VOUT Up to 60V, Buck VOUT <br>Range: 0.8V to 60V, Boost VOUT Up to 60V|
|LTM<br>® 8056|58VIN, Buck-Boost µModule Regulator, Adjustable<br>Input and Output Current Limiting|5V ≤ VIN ≤ 58V, 1.2V ≤ VOUT ≤ 48V, 15mm × 15mm × 4.92mm BGA Package|
|LTC7103|105V, 2.3A, Low EMI Synchronous<br>Step-Down Regulator|4.4V ≤ VIN ≤ 105V, 1V ≤ VOUT ≤ VIN, IQ = 2µA, Fixed Frequency 200kHz,<br>5mm × 6mm QFN Package|


Rev. B


10/22
[www.analog.com](https://www.analog.com)


# 50



[For more information LTC7871](http://www.linear.com/LTC7871)  ANALOG DEVICES, INC. 2021 –2022


