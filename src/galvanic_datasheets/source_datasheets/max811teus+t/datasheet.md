_Click_ _**[here](https://www.maximintegrated.com/en/storefront/storefront.html)**_ _for production status of specific part numbers._

# **MAX811/MAX812 4-Pin μP Voltage Monitors** **with Manual Reset Input**



**General Description**
The MAX811/MAX812 are low-power microprocessor
(μP) supervisory circuits used to monitor power supplies
in μP and digital systems. They provide excellent circuit
reliability and low cost by eliminating external compo­
nents and adjustments when used with 5Vpowered or
3V-powered circuits. The MAX811/MAX812 also provide
a debounced manual reset input.


These devices perform a single function: They assert a
reset signal whenever the V CC supply voltage falls below
a preset threshold, keeping it asserted for at least 140ms
after V CC has risen above the reset threshold. The only
difference between the two devices is that the MAX811

has an active-low RESET output (which is guaranteed
to be in the correct state for V CC down to 1V), while the
MAX812 has an active-high RESET output. The reset
comparator is designed to ignore fast transients on V CC .
Reset thresholds are available for operation with a variety
of supply voltages.


Low supply current makes the MAX811/MAX812 ideal for
use in portable equipment. The devices come in a 4-pin
SOT143 package.

**Applications**


- Computers


- Controllers


- Intelligent Instruments


- Critical μP and μC Power Monitoring


- Portable/Battery-Powered Equipment



**Benefits and Features**

- Integrated Voltage Monitor Increases System
Robustness with Added Manual Reset

  - Precision Monitoring of 3V, 3.3V, and 5V

Power-Supply Voltages

  - 140ms Min Power-On-Reset Pulse Width

     - RESET Output (MAX811), RESET Output

(MAX812)

  - Guaranteed Over Temperature

  - Guaranteed RESET Valid to V CC = 1V (MAX811)

  - Power-Supply Transient Immunity


- Saves Board Space

  - No External Components

  - 4-Pin SOT143 Package


- Low Power Consumption Simplifies Power-Supply
Requirements

  - 6μA Supply Current


**Ordering Information**


**PART*** **TEMP RANGE** **PIN-PACKAGE**


MAX811_EUS-T -40°C to +85°C 4 SOT143


MAX812_EUS-T -40°C to +85°C 4 SOT143


_*This part offers a choice of five different reset threshold voltages._
_Select the letter corresponding to the desired nominal reset_
_threshold voltage, and insert it into the blank to complete the_
_part number._
_Devices are available in both leaded and lead(Pb)-free packaging._
_Specify lead-free by replacing “-T” with “+T” when ordering._


|RESET THRESHOLD|Col2|
|---|---|
|**SUFFIX**|**VOLTAGE (V)**|
|L|4.63|
|M|4.38|
|T|3.08|
|S|2.93|
|R|2.63|



**Typical Operating Circuit** **Pin Configuration**







































_19-0411; Rev 6; 5/18_


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input

**Absolute Maximum Ratings**


**.**


**.** **.**

**.**

**.**



Terminal Voltage (with respect to GND) **.**

V CC **.** ....................................................................-0.3V to 6.0V **.**
All Other Inputs **.** .................................... -0.3V to (V CC + 0.3V)
Input Current, V CC, MR **.** .....................................................20mA
Output Current, RESET or RESET .....................................20mA
Continuous Power Dissipation (T A = +70°C)

SOT143 (derate 4mW/°C above +70°C)......................320mW



Operating Temperature Range **.** .......................... -40°C to +85°C

**.** Junction Temperature **.** .....................................................+150°C
**.** Storage Temperature Range............................. -65°C to +160°C
**.** Lead Temperature (soldering, 10sec)..............................+300°C



**.**


**.** **.**

**.**

**.**


_Stresses beyond those listed under “Absolute Maximum Ratings” may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these_
_or any other conditions beyond those indicated in the operational sections of the specifications is not implied. Exposure to absolute maximum rating conditions for extended periods may affect_
_device reliability._


**Electrical Characteristics**


(V CC = 5V for L/M versions, V CC = 3.3V for T/S versions, V CC = 3V for R version, T A = -40°C to +85°C, unless otherwise noted.
Typical values are at T A = +25°C.) (Note 1)



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**



**.**


**.** **.**

**.**

**.**


|PARAMETER|SYMBOL|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
|Operating Voltage Range|VCC|TA = 0°C to +70°C|TA = 0°C to +70°C|1.0<br>5.5|V|
|Operating Voltage Range|VCC|TA = -40°C to +85°C|TA = -40°C to +85°C|1.2|1.2|
|Supply Current|ICC|MAX81_L/M, VCC= 5.5V, IOUT= 0|MAX81_L/M, VCC= 5.5V, IOUT= 0|6<br>15|µA|
|Supply Current|ICC|MAX81_R/S/T, VCC= 3.6V, IOUT= 0|MAX81_R/S/T, VCC= 3.6V, IOUT= 0|2.7<br>10|2.7<br>10|
|Reset Threshold|VTH|MAX81_L|TA = +25°C|4.54<br>4.63<br>4.72|V|
|Reset Threshold|VTH|MAX81_L|TA = -40°C to +85°C|4.50<br>4.75|4.50<br>4.75|
|Reset Threshold|VTH|MAX81_M|TA = +25°C|4.30<br>4.38<br>4.46|4.30<br>4.38<br>4.46|
|Reset Threshold|VTH|MAX81_M|TA = -40°C to +85°C|4.25<br>4.50|4.25<br>4.50|
|Reset Threshold|VTH|MAX81_T|TA = +25°C|3.03<br>3.08<br>3.14|3.03<br>3.08<br>3.14|
|Reset Threshold|VTH|MAX81_T|TA = -40°C to +85°C|3.00<br>3.15|3.00<br>3.15|
|Reset Threshold|VTH|MAX81_S|TA = +25°C|2.88<br>2.93<br>2.98|2.88<br>2.93<br>2.98|
|Reset Threshold|VTH|MAX81_S|TA = -40°C to +85°C|2.85<br>3.00|2.85<br>3.00|
|Reset Threshold|VTH|MAX81_R|TA = +25°C|2.58<br>2.63<br>2.68|2.58<br>2.63<br>2.68|
|Reset Threshold|VTH|MAX81_R|TA = -40°C to +85°C|2.55<br>2.70|2.55<br>2.70|
|Reset Threshold Tempco||||30|ppm/°C|
|VCCto Reset Delay (Note 2)||VOD= 125mV, MAX81_L/M|VOD= 125mV, MAX81_L/M|40|µs|
|VCCto Reset Delay (Note 2)||VOD= 125mV, MAX81_R/S/T<br>|VOD= 125mV, MAX81_R/S/T<br>|20|20|
|Reset Active Timeout Period|~~t~~RP<br>|~~V~~CC~~= V~~TH(MAX)|~~V~~CC~~= V~~TH(MAX)|140<br>560|ms|
|MR Minimum Pulse Width|~~t~~MR|||10|µs|
|MR Glitch Immunity (Note 3)||||100|ns|
|MR to Reset Propagation<br>Delay (Note 2)|tMD<br>|||0.5|µs|
|MR Input Threshold|~~V~~IH<br>|VCC> VTH(MAX), MAX81_L/M|VCC> VTH(MAX), MAX81_L/M|2.3|V|
|MR Input Threshold|~~V~~IL<br>|~~V~~IL<br>|~~V~~IL<br>|0.8|0.8|
|MR Input Threshold|~~V~~IH<br>|VCC> VTH(MAX), MAX81_R/S/T|VCC> VTH(MAX), MAX81_R/S/T|0.7 x VCC|0.7 x VCC|
|MR Input Threshold|~~V~~IL|~~V~~IL|~~V~~IL|0.25 x VCC|0.25 x VCC|
|MR Pull-Up Resistance||||10<br>20<br>30|kΩ|
|RESET Output Voltage<br>(MAX812)|~~V~~OH|ISOURCE= 150µA, 1.8V < VCC< VTH(MIN)|ISOURCE= 150µA, 1.8V < VCC< VTH(MIN)|0.8 x VCC|V|
|RESET Output Voltage<br>(MAX812)|VOL|MAX812R/S/T only, ISINK= 1.2mA,<br>VCC= VTH(MAX)|MAX812R/S/T only, ISINK= 1.2mA,<br>VCC= VTH(MAX)|0.3|0.3|
|RESET Output Voltage<br>(MAX812)|VOL|MAX812L/M only, ISINK= 3.2mA,<br>VCC= VTH(MAX)|MAX812L/M only, ISINK= 3.2mA,<br>VCC= VTH(MAX)|0.4|0.4|



**.**


**.** **.**

**.**

**.**


www.maximintegrated.com Maxim Integrated │ 2


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input

**Electrical Characteristics (continued)**


(V CC = 5V for L/M versions, V CC = 3.3V for T/S versions, V CC = 3V for R version, T A = -40°C to +85°C, unless otherwise noted.
Typical values are at T A = +25°C.) (Note 1)


















|PARAMETER|SYMBOL|CONDITIONS|MIN TYP MAX|UNITS|
|---|---|---|---|---|
|RESET Output Voltage<br>(MAX811)|VOL|MAX811R/S/T only, ISINK = 1.2mA,<br>VCC = VTH(MIN)|0.3|V|
|RESET Output Voltage<br>(MAX811)|VOL|MAX811L/M only, ISINK = 3.2mA,<br>VCC = VTH(MIN)|0.4|0.4|
|RESET Output Voltage<br>(MAX811)|VOL|ISINK = 50µA, VCC > 1.0V|0.3|0.3|
|RESET Output Voltage<br>(MAX811)|VOH|MAX811R/S/T only, ISOURCE = 500µA,<br>VCC > VTH(MAX)|0.8 x VCC|0.8 x VCC|
|RESET Output Voltage<br>(MAX811)|VOH|MAX811L/M only, ISOURCE = 800µA,<br>VCC > VTH(MAX)|VCC - 1.5|VCC - 1.5|



**Note 1:** Production testing done at T A = +25°C, over temperature limits guaranteed by design using six sigma design limits.
**Note 2:** RESET output for MAX811, RESET output for MAX812.
**Note 3:** “Glitches” of 100ns or less typically will not generate a reset pulse.


www.maximintegrated.com Maxim Integrated │ 3


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input

**Typical Operating Characteristics**

(T A = +25°C, unless otherwise noted.)



**SUPPLY CURRENT vs. TEMPERATURE**
**(MAX81_L/M)**

8



3.0


2.5


2.0


1.5


1.0


0.5



**SUPPLY CURRENT vs. TEMPERATURE**
**(MAX81_R/S/T)**



6


4


2





0

|VCC|Col2|= 3.6V|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|VCC|VCC|= 3.6V|= 3.6V|= 3.6V|= 3.6V|= 3.6V|
|||V~~CC~~ =|V~~CC~~ =|3.3V|||
|||V~~CC~~ =|V~~CC~~ =|3.3V|3.3V|3.3V|
||||||||
||||||||
||||||||
||||||~~V~~CC~~= 1~~||
||||||||

-40 -15 10 35 60 85


|Col1|Col2|Col3|Col4|Col5|V|
|---|---|---|---|---|---|
|||||~~VCC = 5.5~~|~~V~~|
|||||||
|||V~~CC~~|V~~CC~~|= 3V||
|||V~~CC~~|V~~CC~~|= 3V|= 3V|
|||||||
|||VCC= 1V|VCC= 1V|VCC= 1V|VCC= 1V|
|||||||



-15 10 35 60



10



35



TEMPERATURE (°C)


**POWER-DOWN RESET DELAY vs. TEMPERATURE**
**(MAX81_R/S/T)**



0


-40 -15 10 35 60 85


TEMPERATURE (°C)


**POWER-DOWN RESET DELAY vs. TEMPERATURE**
**(MAX81_L/M)**

200



100


80


60


40


20


0





|Col1|V|Col3|Col4|Col5|Col6|VOD = VTH|- VCC|
|---|---|---|---|---|---|---|---|
||V|V||||||
||V|V|OD = 20mV|OD = 20mV|OD = 20mV|OD = 20mV|OD = 20mV|
|||||||||
|||||||||
||||~~VOD =~~<br>VO|~~VOD =~~|~~VOD =~~|~~25mV~~||
||||~~VOD =~~<br>VO|~~VOD =~~|VO|D = 200m|D = 200m|


-40 -15 10 35 60 85


TEMPERATURE (°C)


**RESET THRESHOLD DEVIATION**

**vs. TEMPERATURE**


-40 -15 10 35 60 85


TEMPERATURE (°C)


|Col1|Col2|Col3|0mV|Col5|VOD = V|TH - VCC|
|---|---|---|---|---|---|---|
||||0mV|0mV|||
||VOD = 2|VOD = 2|mV|mV|mV|mV|
||||||||
||||||||
||V|V|||V||
||V|V|OD = 125m|OD = 125m|V|V|
||V|V|||||
||||V|V||mV|
||||V|V|OD = 200|V|
||||V|V|||



-40 -15 10 35 60 85


TEMPERATURE (°C)


**POWER-UP RESET TIMEOUT**

**vs. TEMPERATURE**

230


220


210



200


190



|Col1|Col2|MAX81_|Col4|R/S/T|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||~~MAX81~~|~~MAX81~~|~~L/M~~||


-40 -15 10 35 60 85


TEMPERATURE (°C)



150


100


50


0


1.0005


1.0000


0.9995


0.9990


0.9985


0.9980



www.maximintegrated.com Maxim Integrated │ 4


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input








|Pin Description|Col2|Col3|Col4|
|---|---|---|---|
|**PIN**|**PIN**|**NAME**|**FUNCTION**|
|**MAX811**|**MAX812**|**MAX812**|**MAX812**|
|1|1|GND|Ground|
|2|—|RESET|Active-Low Reset Output.RESET remains low while VCC is below the reset threshold or while<br>MR is held low.RESET remains low for the Reset Active Timeout Period (tRP) after the reset<br>conditions are terminated.|
|—|2|RESET|Active-High Reset Output. RESET remains high while VCC is below the reset threshold or while<br>MR is held low. RESET remains high for Reset Active Timeout Period (tRP) after the reset<br>conditions are terminated.|
|3|3|MR|Manual Reset Input. A logic low onMR asserts reset. Reset remains asserted as long asMR <br>is low and for 180ms afterMR returns high. This active-low input has an internal 20kΩ pull-up<br>resistor. It can be driven from a TTL or CMOS-logic line, or shorted to ground with a switch.<br>Leave open if unused.|
|4|4|VCC|+5V, +3.3V, or +3V Supply Voltage|



**Detailed Description**


**Reset Output**

A microprocessor’s (μP’s) reset input starts the μP in a
known state. These μP supervisory circuits assert reset
to prevent code execution errors during power-up, powerdown, or brownout conditions.


RESET is guaranteed to be a logic low for V CC - 1V.
Once V CC exceeds the reset threshold, an internal timer
keeps RESET low for the reset timeout period; after this
interval, RESET goes high.


If a brownout condition occurs (V CC dips below the reset
threshold), RESET goes low. Any time V CC goes below
the reset threshold, the internal timer resets to zero, and
RESET goes low. The internal timer starts after V CC
returns above the reset threshold, and RESET remains
low for the reset timeout period.

The manual reset input ( MR ) can also initiate a reset. See
the _Manual Reset Input_ section.


The MAX812 has an active-high RESET output that is the
inverse of the MAX811’s RESET output.



**Manual Reset Input**

Many μP-based products require manual reset capabil­
ity, allowing the operator, a test technician, or external
logic circuitry to initiate a reset. A logic low on MR asserts
reset. Reset remains asserted while MR is low, and for
the Reset Active Timeout Period (t RP ) after MR returns
high. This input has an internal 20kΩ pull-up resistor, so
it can be left open if it is not used. MR can be driven with
TTL or CMOS-logic levels, or with open-drain/collector
outputs. Connect a normally open momentary switch from
MR to GND to create a manual-reset function; external
debounce circuitry is not required. If MR is driven from
long cables or if the device is used in a noisy environment,
connecting a 0.1μF capacitor from MR to ground provides
additional noise immunity.


**Reset Threshold Accuracy**
The MAX811/MAX812 are ideal for systems using a 5V
±5% or 3V ±5% power supply with ICs specified for 5V
±10% or 3V ±10%, respectively. They are designed to
meet worst-case specifications over temperature. The
reset is guaranteed to assert after the power supply
falls out of regulation, but before power drops below the
minimum specified operating voltage range for the system
ICs. The thresholds are pre-trimmed and exhibit tight dis­
tribution, reducing the range over which an undesirable
reset may occur.



www.maximintegrated.com Maxim Integrated │ 5


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input

8


7



6


5


4


3


2


1









0

|TA|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TA|TA|= +|2|°C|°C|°C|°C|°C|°C|°C|°C|°C|°C|°C|
|TA|TA||||||||||||||
||||||||||||||||
|MA|MA||||M||||||||||
|MA|M|X8|1|_L/|_L/|_L/|_L/|_L/|_L/|_L/|_L/|_L/|_L/|_L/|
||||||||||||||||
||||||||||||||||
|||M|X|81|_R/S/T|_R/S/T|_R/S/T|_R/S/T|_R/S/T|_R/S/T|_R/S/T|_R/S/T|_R/S/T|_R/S/T|
||||||||||||||||
||||||||||||||||
||||||||||||||||



1 10 100 1000



RESET COMPARATOR OVERDRIVE, V TH         - V CC (mV)


_Figure 1. Maximum Transient Duration without Causing a Reset_
_Pulse vs. Comparator Overdrive_


**Applications Information**


**Negative-Going V** **CC** **Transients**

In addition to issuing a reset to the μP during power-up,
power-down, and brownout conditions, the MAX811/
MAX812 are relatively immune to short duration negativegoing V CC transients (glitches).


Figure 1 shows typical transient durations vs. reset com­
parator overdrive, for which the MAX811/MAX812 do
not generate a reset pulse. This graph was generated
using a negative-going pulse applied to V CC, starting
above the actual reset threshold and ending below it by
the magnitude indicated (reset comparator overdrive).
The graph indicates the typical maximum pulse width a
negative-going V CC transient may have without causing
a reset pulse to be issued. As the magnitude of the tran­
sient increases (goes farther below the reset threshold),
the maximum allowable pulse width decreases. Typically,
a V CC transient that goes 125mV below the reset thresh­
old and lasts 40μs or less (MAX81_L/M) or 20μs or less
(MAX81_T/S/R) will not cause a reset pulse to be issued.
A 0.1μF capacitor mounted as close as possible to V CC
provides additional transient immunity.



_Figure 2._ _RESET_ _Valid to VCC = Ground Circuit_


**Ensuring a Valid** **RESET** **Output**
**Down to V** **CC** **= 0V**
When V CC falls below 1V, the MAX811 RESET output
no longer sinks current—it becomes an open circuit.
Therefore, high-impedance CMOS-logic inputs connected
to the RESET output can drift to undetermined voltages.
This presents no problem in most applications, since most
μP and other circuitry is inoperative with V CC below 1V.
However, in applications where the RESET output must
be valid down to 0V, adding a pulldown resistor to the
RESET pin will cause any stray leakage currents to flow
to ground, holding RESET low (Figure 2). R1’s value is
not critical; 100kΩ is large enough not to load RESET and
small enough to pull RESET to ground.


A 100kΩ pull-up resistor to V CC is also recommended
for the MAX812 if RESET is required to remain valid for
V CC < 1V.



www.maximintegrated.com Maxim Integrated │ 6


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input



**Interfacing to μPs with**
**Bidirectional Reset Pins**

μPs with bidirectional reset pins (such as the Motorola
68HC11 series) can contend with the MAX811/MAX812
reset outputs. If, for example, the MAX811 RESET output
is asserted high and the μP wants to pull it low, indeter­
minate logic levels may result. To correct such cases,
connect a 4.7kΩ resistor between the MAX811 RESET (or
MAX812 RESET) output and the μP reset I/O (Figure 3).
Buffer the reset output to other system components.


**Chip Information**

TRANSISTOR COUNT: 341



_Figure 3. Interfacing to μPs with Bidirectional Reset I/O_











www.maximintegrated.com Maxim Integrated │ 7


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input

**Package Information**
For the latest package outline information and land patterns (footprints), go to **[www.maximintegrated.com/packages](http://www.maximintegrated.com/packages)** . Note that a “+”,
“#”, or “-” in the package code indicates RoHS status only. Package drawings may show a different suffix character, but the drawing
pertains to the package regardless of RoHS status.

|PACKAGE TYPE|PACKAGE CODE|OUTLINE NO.|LAND PATTERN NO.|
|---|---|---|---|
|4 SOT143|U4+1|**21-0052**|**90-0183**|



www.maximintegrated.com Maxim Integrated │ 8


# MAX811/MAX812 4-Pin μP Voltage Monitors with Manual Reset Input

**Revision History**







|REVISION<br>NUMBER|REVISION<br>DATE|DESCRIPTION|PAGES<br>CHANGED|
|---|---|---|---|
|5|6/15|Updated_Benefts and Features_ and_Package Information_ sections|1, 8|
|6|5/18|Updated_Absolute Maximum Ratings_|2|


For pricing, delivery, and ordering information, please visit Maxim Integrated’s online storefront at https://www.maximintegrated.com/en/storefront/storefront.html.


_Maxim Integrated cannot assume responsibility for use of any circuitry other than circuitry entirely embodied in a Maxim Integrated product. No circuit patent licenses_
_are implied. Maxim Integrated reserves the right to change the circuitry and specifications without notice at any time. The parametric values (min and max limits)_
_shown in the Electrical Characteristics table are guaranteed. Other parametric values quoted in this data sheet are provided for guidance._


Maxim Integrated and the Maxim Integrated logo are trademarks of Maxim Integrated Products, Inc. © 2018 Maxim Integrated Products, Inc. │ 9


