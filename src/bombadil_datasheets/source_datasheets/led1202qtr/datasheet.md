WLCSP20


QFN20 3x3




# **LED1202**

Datasheet

## 12-channel low quiescent current LED driver


**Features**


- Supply range from 2.6 V to 5 V

- 12 channels for single LED

- 20 mA current capability per channel

- 1% (typ.) current matching at 16 mA and 2% (typ.) at 2.5 mA

- 1.8 V compatible I²C control interface

- 8-bit analog dimming individual control

- 12-bit local PWM resolution

- 8 programmable patterns

- Programmable pattern sequence

- Synchronization for multi-device application

- Phase shifting between channels

- Open LED detection

- Overtemperature protection

- 8 configurable I²C slave addresses plus global address

- Fault flag pin


**Applications**


- RGB LED lighting, fade-in and fade-out breathing effect, indicator lights for:

– Wearable electronics

–
Battery powered devices

– Portable accessories


**Description**


[The LED1202 is a 12-channel low quiescent current LED driver; it guarantees 5 V](https://www.st.com/en/product/led1202)
output driving capability and each channel is able to provide up to 20 mA with a
headroom voltage of 350 mV (typ.) only. The output current can be adjusted
separately for each channel by 8-bit analog and 12-bit digital dimming control.


A slow turn-on and turn-off time improves the system low noise generation
performance; moreover, the phase shifting function helps to reduce the inrush
current. Eight patterns can be stored in the internal registers for automatic
sequencing without MCU intervention.


The pattern sequence can be also configured for duration time and number of
repetition. For multi-device applications, a common clock domain can be shared for
timing synchronization. The device includes thermal shutdown and open LED
detection.


The device I²C interface is based on fast mode specification and works up to 400
kHz. Eight I²C addresses are possible by using two configuration pins (A0/A1) only.
[The LED1202 is available in WLCSP20 package 1.71 x 2.16 x 0.5 mm with 0.4 mm](https://www.st.com/en/product/led1202)
pitch and in QFN20 3x3 package 3 x 3 x 0.6 mm with 0.5 mm pitch.





**DS12875** - **Rev 2** - **February 2019**
For further information contact your local STMicroelectronics sales office.



[www.st.com](http://www.st.com)


**LED1202**


**Introduction**


## **1 Introduction**

The LED1202 is a 12-channel LED driver with high current accuracy.


**1.1** **Block diagram**


**Figure 1. LED1202 simplified block diagram**
















|Col1|SCL|Col3|Col4|
|---|---|---|---|
||SDA<br>A0|||
||SDA<br>A0|||
||A1|||
||IRQn|IRQn|IRQn|





**DS12875** - **Rev 2** **page 2/54**


**LED1202**


**Pinout and pin description**

## **2 Pinout and pin description**


WLCSP20 and QFN20 3x3 package pinout and pin description.


**2.1** **WLCSP20 package – ball assignment**


**Figure 2. LED1202JR ball assignment (top and marking side view)**















**2.2** **QFN20 3x3 package – pin assignment**


**Figure 3. LED1202QTR pin assignment (top and marking side view)**

















**DS12875** - **Rev 2** **page 3/54**


**LED1202**


**Pin description**


**2.3** **Pin description**


**Table 1. Pin description**

|I/O balls/pins|Name|Description|
|---|---|---|
|D4 / 15|VIN|Power supply input|
|A3 / 08|GND|Power ground|
|E1 / 20|SCL|I²C clock signal|
|E2 / 19|SDA|I²C data signal|
|D1 / 01|IRQn|Interrupt output (open-drain) – active low|
|E3 / 17|A0|Address pin 0 / internal clock output|
|D2 / 18|A1|Address pin 1 / external clock input|
|E4 / 16|VLDO|LDO capacitor output|
|C1 / 02|CS0|Current sink 0 input|
|C2 / 03|CS1|Current sink 1 input|
|B1 / 04|CS2|Current sink 2 input|
|B2 / 05|CS3|Current sink 3 input|
|A1 / 06|CS4|Current sink 4 input|
|A2 / 07|CS5|Current sink 5 input|
|B3 / 09|CS6|Current sink 6 input|
|A4 / 10|CS7|Current sink 7 input|
|C3 / 11|CS8|Current sink 8 input|
|B4 / 12|CS9|Current sink 9 input|
|D3 / 13|CS10|Current sink 10 input|
|C4 / 14|CS11|Current sink 11 input|



**DS12875** - **Rev 2** **page 4/54**


**LED1202**


**Electrical characteristics**

## **3 Electrical characteristics**


**3.1** **Maximum ratings**


**Table 2. Absolute maximum ratings**

|Symbol|Parameter|Value|Unit|
|---|---|---|---|
|VIN|LED driver input voltage|-0.3 to 6|V|
|VSDA, VSCL, VIRQn|Digital domain voltages|-0.3 to 6|V|
|VCS0-CS11|LED outputs|-0.3 to 6|V|
|VLDO, VA0, VA1|Digital domain voltages|-0.3 to 6|V|
|ESD|Human body model (HBM) – JESD22-A114-B|±2000|V|



_Note:_ _Absolute maximum ratings are those values beyond which damage to the device may occur. Functional_
_operation under these conditions is not implied._


**3.2** **Thermal information**


**Table 3. Thermal data**

|Symbol|Parameter|Col3|Value|Unit|
|---|---|---|---|---|
|Ta|Operative free-air temperature range|Operative free-air temperature range|-40 to +85|°C|
|TJ|Operative junction temperature range|Operative junction temperature range|-40 to +125|°C|
|TSTG|Storage ambient temperature range|Storage ambient temperature range|-55 to +150|°C|
|θja|Thermal resistance junction-ambient(1)|WLCSP20 1.71x2.16 mm|89.5|°C/W|
|θja|Thermal resistance junction-ambient(1)|QFN20 3x3|65.3|°C/W|
|θjb|Thermal resistance junction-board(1)|WLCSP20 1.71x2.16 mm|53.0|°C/W|
|θjb|Thermal resistance junction-board(1)|QFN20 3x3|18.1|°C/W|
|θjc<br>|Thermal resistance junction-case(1)|WLCSP20 1.71x2.16 mm|13.8|°C/W|
|θjc<br>|Thermal resistance junction-case(1)|QFN20 3x3|19.4|°C/W|



_1._ _These parameters correspond to Standard JEDEC PCB (2S2P) as per JESD 51 specification._


**DS12875** - **Rev 2** **page 5/54**


**LED1202**


**LED1202 electrical characteristics**


**3.3** **LED1202 electrical characteristics**


**Table 4. LED1202 electrical characteristics V** **IN** **= 3.3 V, SDA, SCL and IRQn = 1.8 V, T** **a** **= 25 °C,**
**RC load = 50 Ω//10 pF, unless otherwise specified.**























|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|VIN|Operating input voltage||2.6||5|V|
|IQ|Quiescent current|EN=’0’||4|8|µA|
|IIN|Supply current|EN=’1’<br>ICS0-CS11 = 16 mA||0.8|2.0|mA|
|VIN_UVLO|Undervoltage lockout threshold|VUVLOR (VIN is rising)|||2.5|V|
|VIN_UVLO|Undervoltage lockout threshold|VUVLOF (VIN is falling)|2.1|||V|
|VLDO|LDO output voltage|Iout = 10 mA;<br>VIN = 2.6 V||1.8||V|
|ILDO_SH|LDO short-circuit current|Vout forced at 1.6 V|||200|mA|
|VCS_MIN|Minimal headroom voltage|ICS0-CS11 = 0.985 * ICSMAX||350||mV|
|VCS_MAX|Maximum output voltage|ICS0-CS11 = 0 mA|||5|V|
|ICS_SET|Analog dimming range(1)||1||20|mA|
|ΔICS0-CS11|Current matching between<br>channels(2)|ICS0-CS11 = 16.0 mA<br>@ VCS = 1 V||±1%|±3|%|
|ΔICS0-CS11|Current matching between<br>channels(2)|ICS0-CS11 = 2.5 mA<br>@ VCS = 1 V||±2%|±3|%|
|ΔICS|Absolute channel accuracy|ICS0-CS11 = 16.0 mA<br>@ VCS = 1 V|||±4|%|
|ΔICS|Absolute channel accuracy|ICS0-CS11 = 2.5 mA<br>@ VCS = 1 V|||±6|%|
|fPWM|Output digital dimming frequency|||220||Hz|
|DPWM|Output dimming duty-cycle range||0||100|%|
|DPWM_STEP|Output dimming duty-cycle step|||1/4095|||
|tPWM_ON-MIN|Minimum output pulse ON-time|||1||µs|
|tSHIFT|Phase shift time between channels|SHFT = ‘1’||1/12xfPWM||s|
|tINIT|Initialization time to start lighting|EN = ‘0’→ ‘1’<br>Pattern0 default condition||6||ms|
|TSHDN|Thermal shutdown|||150||°C|
|VOPEN_TH|Open LED detection threshold|ICS0-CS11 > 1 mA||100||mV|
|VIRQn|Output low level|ITEST = 1 mA|||0.4|V|
|IIRQn_LK|Input leakage current|VIRQn = 5 V|||1|µA|
|**I²C compatible interface**|**I²C compatible interface**|**I²C compatible interface**|**I²C compatible interface**|**I²C compatible interface**|**I²C compatible interface**|**I²C compatible interface**|
|VIH|High level input voltage||1.26|||V|
|VIL|Low level input voltage||||0.54|V|
|VOL|Low level output voltage|ITEST = 5 mA|||0.4|V|


**DS12875** - **Rev 2** **page 6/54**


**LED1202**


**LED1202 electrical characteristics**

|Symbol|Parameter|Test conditions|Min.|Typ.|Max.|Unit|
|---|---|---|---|---|---|---|
|CIO|IO pin capacitance||||10|pF|
|fSCL|SCL clock frequency||||400|kHz|
|tLOW|Minimum clock low period||1.3|||µs|
|tHIGH|Minimum clock high period||600|||ns|
|tF|SDA and SCL fall time||||300|ns|
|tR|SDA and SCL rise time||||300|ns|
|tHD:STA|Start condition hold time||600|||ns|
|tSU:STA|Start condition setup time||600|||ns|
|tSU:DAT|Data setup time||100|||ns|
|tHD:DAT|Data hold time||0|||µs|
|tSU:STO|Stop condition setup time||600|||ns|
|tBUF<br>|Minimum delay between operations||1.3|||µs|



_1._ _The correspondence between the programmed I_ _LED_ _and output current is not guaranteed for I_ _LED_ _< I_ _CS_SET_ _Min._


_2._ _ΔI_ _CS0-CS11_ _= ((I_ _CSx_ _– I_ _CSavg_ _) / ICSavg) * 100; I_ _CSavg_ _= (∑I_ _CSx_ _) / 12_


**DS12875** - **Rev 2** **page 7/54**


**LED1202**


**Headroom voltage**


**3.4** **Headroom voltage**


The minimum headroom voltage is not constant, it changes according to LED current value. The typical
characteristic at 25 °C ambient temperature is shown in the figure below.

In order to improve the accuracy and ground noise rejection at low current, the output stage implements two
different current sink branches, that is why the curve has a double slope.

The threshold to switch between the branches is the I LEDx (registers from address 09h to 14h) value of 48d
(3.76 mA).


**Figure 4. LED1202 headroom voltage vs. I** **LED**











**DS12875** - **Rev 2** **page 8/54**


**LED1202**


**Device description**

## **4 Device description**


The LED1202 implements 12 low-side current generators with independent dimming control. Internal volatile
memory allows the user to store up to 8 different patterns, each pattern is a particular output configuration in
terms of PWM duty-cycle (on 4096 steps). While analog dimming (on 256 steps) is per channel but common to all
patterns.


**4.1** **Device startup**


Once the supply voltage V IN is applied, the LED1202 executes some internal checks, afterwords it stops the
oscillator and puts the internal LDO in quiescent mode. To start the device, EN bit must be set inside the “Device
Enable” register at address 01h (see Section 7.2 Device enable register).

As soon as EN is set, the LED1202 loads the adjustment parameters from the internal non-volatile memory and
performs an auto-calibration procedure in order to increase the output current precision.

Such initialization lasts about 6.5 ms.


**4.2** **Device reset**


The LED1202 can be reset by software. The RST bit is inside the “Device Enable” register at address 01h (see
Section 7.2 Device enable register). When RST bit is set all the register values are restored to default value as
per a POR event. This bit is always read as zero since it is the POR value.


**4.3** **Device address selection**


The LED1202 allows up to eight different local I²C addresses to be selected ; furthermore, it has also a fixed
global address:

         - Global address – is factory pre-set and unchangeable for all devices (5Ch @ 7bit); it controls at the same
time all the devices sharing the same I²C bus (only write is possible)

         - Local address – it allows the user to control each single device according to the defined local address (read/
write operations are possible)


A read operation using a global address produces an ACK as reply to the valid address, but after that SDA line is
not driven generating a “false” FFh data reply, instead of any register content.

Internal register read is allowed using one of the 8 selectable local addresses only; local address can be defined
using only two pins (A0 and A1) connected, as per the following table:


**Table 5. LED1202 local address table**

|A1|A0|I²C slave address (7 bit)|
|---|---|---|
|GND|GND|58h|
|GND|VI2C|59h|
|VI2C|GND|5Ah|
|VI2C|VI2C|5Bh|
|GND|SDA|5Dh|
|GND|SCL|5Eh|
|VI2C|SDA|5Fh|
|VI2C|SCL|60h|



Local address is acquired and latched inside the device at first acknowledge. After that, any modification of A0
and/or A1 connection has not effect on the device I²C local address.


**DS12875** - **Rev 2** **page 9/54**


**LED1202**


**LED channel selection**


**4.4** **LED channel selection**


The enabling or disabling of channels is performed on “Channel Enable” registers at addresses 02h and 03h.
There are 8 + 4 enable bits available, one for each corresponding channel. "Channel Enable" registers are
detailed on Section 7.3 Channel enable registers. EN bit on “Device Enable” register at address 01h is the global
enable of the device that has higher priority than single channel enable bits (see Section 7.2 Device enable
register).


**4.5** **Output dimming modes**


There are two main methods for dimming LED light: changing the output DC current value (analog dimming) or
modifying the output current duty-cycle (digital dimming). The two methods are not mutually exclusive and can be
used at the same time to generate a specific channel by channel 20 bit depth dimming.


**4.5.1** **LED controlled by “CSx LED Current” registers (analog dimming)**


The output DC current value can be adjusted by “CSx LED Current” registers (see Section 7.8 LED current
registers). In this case, the LED brightness change is achieved by setting the output current in the range from 1
mA to 20 mA. “CSx LED Current” registers are between address 09h to 14h. Note that after POR, all output PWM
values are set by default on “Pattern0CSx PWM” registers: PWML = 55 h, PWMH = 05 h; limiting the maximum
brightness reachable acting on analog dimming alone.


**Figure 5. Analog dimming**


**4.5.2** **LED controlled by “PatternyCSx PWM” registers (digital dimming)**


The LED brightness can be adjusted by varying the output duty-cycle. The duty-cycle is programmed by
“PatternyCSx PWM” registers (see Section 7.11 Pattern PWM configuration registers). Note that “CSx LED
Current” registers (see Section 7.8 LED current registers) are set by default to 27h, limiting the output current DC
value to about 3.06 mA. To avoid any brightness artefacts, when SHFT=1 and/or EN=1, the update of
“PatternyCSx PWM” registers should be synchronized with SOF (start of frame) interrupt (refer to
Section 4.10.4 Start of frame interrupt for more details).


**Figure 6. Digital dimming**


**DS12875** - **Rev 2** **page 10/54**


**LED1202**


**Phase-shift**


**4.5.2.1** _**Global digital dimming configuration**_


Setting GCTRL bit in “Configuration” register at address 04h (see Section 7.4 Configuration register), the PWM
value set for the channel CS0 (PatternyCS0) is applied to all channels (same digital dimming level). This is valid
for any pattern selected by PATSEL[2:0] in “Configuration” register (refer to Section 4.7 Pattern selection and
configuration for more details).

During the execution of a pattern sequence (refer to Section 4.8 Pattern sequence configuration for more details)
the PatternyCS0 setting of the running pattern is applied to all channels (CS0-CS11).


**4.5.3** **LED controlled by “CSx LED Current” and “PatternyCSx PWM” registers**


The full control of LED brightness can be achieved by setting both the output current level (“CSx LED Current”
registers, see Section 7.8 LED current registers) and output current duty-cycle using “PatternyCSx PWM”
registers (see Section 7.11 Pattern PWM configuration registers).


**Figure 7. Analog+digital dimming**


**4.6** **Phase-shift**


Phase-shift feature delays channel power-on to minimize peak load current. This delay reduces voltage ripple on
the LED power supply rail and allows the smallest filtering capacitor to be used. This feature is controlled by
SHFT bit in “Configuration” register (see Section 7.4 Configuration register). The shift time (t SHIFT ) is the delay
between two contiguous channels and it is defined as follows:


tsℎift = 1/ 12 × fPWM = 1/ 12 × 220 ≈380 µs


To have the phase-shift properly executed, without LED blink artefacts, SHFT=1 has to be set before enabling the
device with EN=1.

When SHFT is set, to avoid any brightness artefact, PWM value change (from CS11 to CS0) must be
synchronized with SOF (start of frame) interrupt (refer to Section 4.10.4 Start of frame interrupt for more details).

While pattern change can be made at any time since the new selected pattern is automatically synchronized by
the LED1202 at the beginning of the new frame.


**DS12875** - **Rev 2** **page 11/54**


**LED1202**


**Pattern selection and configuration**



**Figure 8. Phase-shift feature scheme**





**4.7** **Pattern selection and configuration**


Active pattern can be selected in “Configuration” register at 04h (see Section 7.4 Configuration register) by
PATSEL[2:0] bits, choosing among 8 different patterns. A pattern is composed of the PWM value for each output
stored into “PatternyCSx PWM” registers. Analog dimming ILEDx (registers from 09h to 14h) is per channel and it
is common to all patterns.


**4.8** **Pattern sequence configuration**


The pattern sequence can be enabled in “Configuration” register at 04h (see Section 7.4 Configuration register)
by using PATS bit and setting PATSR bit starts in the same register. PATS bit can be set at any time, even when
EN=0, but after setting all outputs go OFF waiting for the sequence start. It is not possible to set PATSR bit when
EN=0, in this case it is cleared.

Since PATS and PATSR bits are in the same register they can be set at the same time, there is no point in setting
PATS earlier than PATSR. While setting PATSR earlier than PATS is not possible, in this case PATSR is cleared.

PATSR bit is set by user to start the pattern sequence, afterward it indicates (when it is read by user) that pattern
sequence is being run whether set or not if cleared.

The duration of each single pattern of the sequence can be configured from about 22.2 ms to 5660 ms, by step of
22.2 ms, in “Pattern y Duration” registers (see Section 7.10 Pattern duration registers) at address 16h to 1Dh.

22.2 ms step is generated using the internal oscillator as time base and, in case of application with multiple
devices, all the devices should be synchronized (refer to Section 4.9.1 Common clock domain configuration for
more details) to have a single master oscillator.

The pattern sequence can be repeated for a programmable number of times (from 1 to 254) or in infinite loop, it
depends on the value written in “Pattern Sequence Repetition” register at 15h (see Section 7.9 Pattern sequence
repetition register). Note: the value 00h is not allowed for such registers.

The pattern sequence runs always from pattern 0 to pattern 7, independently of PATSEL[2:0] value. It is possible
to skip a pattern writing 00h into “Pattern y Duration” register, so the sequence moves to the next one; in case all
patterns are set to skip, the device clears PATSR immediately.

When the pattern sequence runs, the displayed pattern can be checked by reading PATSEL bits (used as status
bits when PATSR=1). PATSEL bits can be written during the pattern sequence execution, but the new selected


**DS12875** - **Rev 2** **page 12/54**


**LED1202**


**Device synchronization**


pattern becomes active at the end of the pattern sequence (PATSR=0) only and visible only when the sequence is
disabled by PATS=0.

After setting EN=1, the device performs some auto adjustments, if the user sets PATSR during this time the
pattern sequence starts at the end of such auto adjustments only. As a consequence, if read by user, PATSR is
zero up to the end of auto adjustment since the sequence has not started yet and so it is not ongoing.

If “Pattern y Duration” and/or “Pattern Sequence Repetition” are modified during the pattern sequence execution,
new values are updated only when the sequence has been completed or stopped, in case of infinite loop.

At the end of the pattern sequence, the device can be forced in disable by setting AUTODIS bit in “Configuration”
register at 04h (see Section 7.4 Configuration register); in this manner, the internal oscillator is switched off.

Setting GCTRL bit in “Configuration” register forces the value “PatternyCS0 PWM” to all outputs, this feature can
be used, for example, in backlight applications where normally all LEDs use the same dimming.


**4.9** **Device synchronization**


When in one application there is more than one device, the way to activate all the devices at the same time is to
set the EN bit in “Device Enable” register through the global address. In this manner all LEDs are lighted up and
they are driven by those devices sharing the same I²C bus as they are controlled by a single device.

Global address is also important to launch the execution of complex pattern sequences which imply a lot of LEDs
driven by more than one device.


**4.9.1** **Common clock domain configuration**


The LED1202 generates internally the reference clock for all timings, from PWM period to pattern sequence
duration time. The internal clock is stable and precise, but it cannot be absolutely the same for all production
population. So, in those applications with multiple devices running a patter sequence managed by more than one
device, a device has to be selected as master and its clock has to be used as reference for all devices. This
ensures, even in case of long duration time or infinite looping, a synchronicity of patterns managed by different
devices.

I²C local address is set with A0 and A1 pins; the LED1202 latches the configured address after the first
acknowledge of an appropriate I²C frame. After that, any level change on A0 and A1 has no effect on the device
I²C local address, so pins can be used for different purposes.

Specifically to output internal clock (A0) and to input external clock (A1).

In a configuration with multiple devices and common clock domain there is a master device sharing its generated
clock internally with all the other slave devices. The LED1202 supports clock distribution either in daisy chain or
star configuration. In daisy chain configuration each device receives the clock from the previous one (master
excluded) and provides it to the next, in star configuration master distributes the clock to all slaves in parallel.

Clock output can be enabled on pin A0 setting bit CLK_O_En, while clock input is enabled on pin A1 by bit
CLK_I_En, both bits are in “clock configuration” register at address E0h (see Section 7.12 Clock configuration
register).


**4.10** **Alarms and IRQ generation**


Four device detections, fault or condition, can generate an interrupt on IRQn pin if it is not masked:

         - Open LED

         - Overtemperature

         - Pattern end

         - Start of frame


**DS12875** - **Rev 2** **page 13/54**


**LED1202**


**Alarms and IRQ generation**


**4.10.1** **Open LED interrupt**


When any used channel (CS0-CS11) goes to open condition, the respective CSx bit in “Open LED” status
registers at 07h and 08h is set. If LED connection is restored the respective bit is not reset since it is latched and
auto-cleared only by a read-back operation. The OPEN bit in “Fault and Status Interrupt” register (see
Section 7.6 Fault and status interrupt register) is set as cumulative result of active channels open detection, it
generates an interrupt on IRQn pin if OPEN_M bit in “Fault and Status Mask” register (see Section 7.5 Fault and
status mask register) is 0 (OPEN flag mask not set). IRQn pin is reset after reading “Fault and Status Interrupt”
register, while the CSx bit is cleared after “Open LED” status register read-back.

Open channel detection has a current threshold and deglitch, it works properly only if I LED value is higher than 1
mA and PWM ON time is longer than about 14 µs.


**4.10.2** **Overtemperature protection (OVTP) interrupt**


An internal temperature sensor monitors continuously the IC junction temperature. If the junction temperature
exceeds 150 °C (typ.) the device stops operating shutting down all the outputs, however the I²C interface stays
active. The OVTP bit in “Fault and Status Interrupt” register (see Section 7.6 Fault and status interrupt register) is
set.

Even if the temperature decreases, the respective fault bit is latched, this bit is auto-cleared by a read operation.
The OVTP bit, when asserted, generates an interrupt on IRQn pin if not masked by OVTP_M bit “Fault and Status
Mask” register (see Section 7.5 Fault and status mask register). Overtemperature detection has a deglitch of
about 18 µs.


**4.10.3** **Pattern end interrupt**


The PAT bit on “Fault and Status Interrupt” register at address 06h (see Section 7.6 Fault and status interrupt
register) is set when the pattern sequence is completed. This PAT bit generates an interrupt on IRQn pin if PAT_M
bit of “Fault and Status Mask” register (see Section 7.5 Fault and status mask register) is not set. Interrupt is
automatically cleared after “Fault and Status Interrupt” register read-back.

At the end of the pattern sequence, the bit PATSR is automatically cleared while bit PATS remains set and as a
consequence all outputs remain OFF. If PAT bit is not masked, at the end of the sequence, the IRQn pin is driven
and can be used as MCU interrupt. In this manner, the end of the sequence is quickly recognized making possible
an immediate PATS bit clearing to display the pattern defined by PATSEL[2:0] instead of leaving all channels OFF.


**4.10.4** **Start of frame interrupt**


SOF bit (Start of frame) in “Fault and Status Interrupt” register (see Section 7.6 Fault and status interrupt register)
can be used o generate an interrupt on IRQn pin in order to change CSx PWM setting of running pattern without
creating any brightness artefact. When not needed, SOF can be masked by SOF_M bit in in in “Fault and Status
Mask” register (see Section 7.5 Fault and status mask register).

When user wants to change CSx PWM settings of running pattern on fly and he wants that new CSx PWM
settings are taken all simultaneously, since I²C CSs pattern PWM settings writing is done sequentially, the steps
below need to be followed:

1. Unmask SOF bit;

2. Wait for the interrupt (generated at the beginning of the frame);

3. Update sequentially (using auto increment) CSx PWM settings of running pattern at 220 Hz. In this way all the
registers are updated within a PWM period and so at the beginning of next frame all CSx channels start
simultaneously with newer PWM settings;

4. Set again SOF_M mask bit, to avoid unnecessary interrupt.

Because SOF signal is synchronized with the start of CS0 frame, in case SHFT bit is set, user has to do the same
procedure described before, but, for point 3, he has to update all CSx PWM settings starting from CS11 PWM
settings down to CS0 PWM settings. This means that auto increment is not possible and the time available to
update each CSx PWM registers is 380 µs.

Since each CSx PWM value is on 2 registers, the I²C frame required for a single CSx PWM update lasts 36
clocks, meaning at least 360 µs with I²C in standard mode (refer to Section 5.2 I²C bus interface for more details)
and 90 µs in fast mode. In both cases a time shorter than t SHIFT allows the new CSx PWM value to be applied
exactly the frame afterward.


**DS12875** - **Rev 2** **page 14/54**


**LED1202**


**Alarms and IRQ generation**



**Figure 9. SOF position in case of SHFT=1**





**DS12875** - **Rev 2** **page 15/54**


**LED1202**


**Device interface**

## **5 Device interface**


This section describes the LED1202 device interfaces.


**5.1** **IRQn output pin**


The interrupt request (IRQ) pin is used to inform the system when an alarm event occurs. This IRQn pin is opendrain active low. “Fault and Status Interrupt” register (see Section 7.6 Fault and status interrupt register) filtered by
“Fault and Status Mask” register (see Section 7.5 Fault and status mask register) controls this pin. The IRQn pin
status is reset after “Fault and Status Interrupt” register read-back. When this pin is used to manage SOF (start of
frame) signal to synchronize PWM change, mainly when SHIFT is active, it had better temporary mask all the
other alarms in “Fault and Status Mask” register.


**5.2** **I²C bus interface**


The LED1202 is fully controlled, registers write and read, by I²C communication.

The I²C bus is a slave serial interface built with a data line (SDA) and a clock line (SCL):

         - SCL: input clock used to shift the data.

         - SDA: input/output bidirectional data transfer line.


The LED1202 device supports the following data transfer mode: standard mode (100 Kbit/s) and fast mode (400
Kbit/s) as defined in the I²C bus specifications.

I²C communication is composed of specific events on the bus:

         - Start condition - it is a falling edge of SDA while SCL is HIGH level

         - Slave addressing - it is the transmission (M→S) of the ID of the slave to be addressed (7-bit)

         - Communication direction - it is one bit immediately following the slave ID: 0 for data writing (M→S) or 1 for
data reading (S→M)

         - Register addressing - it is the transmission (M→S) of the register address of the slave to be accessed (8-bit)

         - Data bit - data are 8 bits per word driven either by MASTER or SLAVE depending on the communication
moment

         - Acknowledge - it is a LOW level on SDA line, driven by either SLAVE or MASTER depending on the
communication direction

         - Stop condition – it is a rising edge of SDA while SCL is HIGH level

         - Restart condition - it is a new start condition which happens before a stop condition: it normally implies a
change in the direction of the communication


**Figure 10. I²C timing reference**
















|Col1|Col2|Col3|
|---|---|---|
||||


|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|||||||
|P|P|P|S|S|S|


|Col1|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
|||||
|||||
|||||
|SR|SR|SR|SR|


|Col1|Col2|Col3|
|---|---|---|
||||
||||
||||
||||
||P|P|



**5.2.1** **The LED1202 addressing**


Since some applications could require more than a single LED1202 device, a method to differentiate each single
device has been put in place using pins A0 and A1; refer to Section 4.3 Device address selection for more details.


**DS12875** - **Rev 2** **page 16/54**


**LED1202**


**I²C bus interface**


**5.2.2** **Data validity**


As shown in the figure below, the data on the SDA line must be stable during the high period of the clock. The
HIGH and LOW state of the data line can only change when the clock signal on the SCL line is LOW.


**Figure 11. Data validity on the I²C Bus**


**5.2.3** **Start and stop conditions**


Both DATA and CLOCK lines remain HIGH when the bus is not busy. As shown in the figure below, a START
condition is a HIGH to LOW transition of the SDA line while SCL is HIGH. The STOP condition is a LOW to HIGH

transition of the SDA line while SCL is HIGH. A STOP condition must be sent to the end of each communication.
A START condition sent before a STOP condition is called RESTART and it is normally used to change the
communication direction, typically from write to read.


**Figure 12. Start and stop condition on the I²C Bus**


**5.2.4** **Byte format**


Every packet transferred on the SDA line must contain 8 bits, each byte is followed by an acknowledge bit. Each
clock pulse transfers a single bit of the packet, the data transfer is MSB first. The data on the SDA line must
remain stable during the HIGH period of the clock pulse. Any change in the SDA line at this time is considered as
a control signal (START or STOP condition).


**Figure 13. Bit transfer**

























**DS12875** - **Rev 2** **page 17/54**


**LED1202**


**I²C bus interface**


**5.2.5** **Acknowledge**


The master (MCU) puts a resistive HIGH level on the SDA line during the acknowledge clock pulse (see the figure
below). The peripheral (LED1202) has to pull down (LOW) the SDA line during the acknowledge clock pulse, so
that the SDA line is stable LOW during this clock pulse. The peripheral, which has been addressed, has to
generate an acknowledge pulse after the reception of each byte, otherwise the SDA line remains at the HIGH
level during the nin [th] clock pulse duration. In this case, the master transmitter can generate the STOP information
in order to abort the transfer. The LED1202 does not generate acknowledge if the V IN supply is below the
undervoltage lockout threshold.


**Figure 14. Acknowledge on the I²C bus**


**5.2.6** **Interface protocol**


The interface protocol is composed of (see figure below):

         - Start condition (START)

         - Device address (7 bit) + R/W bit (read = 1 / write = 0)

         - Register address byte

         - Sequence of N data packet (1 byte + acknowledge)

         - Stop condition (STOP)


The register address byte determines the first register in which the read or write operation takes place. When the
read or write operation is finished, the internal register address pointer is automatically incremented allowing
multiple register writing or reading.


**Figure 15. Interface protocol**


























|Col1|Device address + R/W bit|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Register address|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Data|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||7|6|5|4|3|2|1|0|0|7|6|5|4|3|2|1|0|0|7|6|5|4|3|2|1|0|0|0|
|S<br>T<br>A<br>R<br>T|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|L<br>S<br>B|R<br>W|A<br>C<br>K|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|L<br>S<br>B|A<br>C<br>K|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|M<br>S<br>B|L<br>S<br>B|A<br>C<br>K|S<br>T<br>O<br>P|



**5.2.7** **Writing to a single register**


Writing to a single register starts with a START condition followed by the 7-bit device address of the LED1202, the
8 [th] bit of the byte is the R/W bit, which is 0 for writing operations.

Then the master waits for the LED1202 acknowledge. Then the 8-bit address of register is sent to the LED1202, it
is also followed by an acknowledge pulse. The last transmitted byte is the data to be written into the register, the
LED1202 generates the acknowledge pulse at the end of packet. The master then generates a STOP condition
and the communication is over. See figure below.


**DS12875** - **Rev 2** **page 18/54**


**LED1202**


**I²C bus interface**



**Figure 16. Writing to a single register**



































**5.2.8** **Writing to multiple registers with incremental addressing**


It would not be easy to send several times the device address and the address of the register when writing to
multiple sequential registers. The LED1202 supports writing to multiple registers with incremental addressing.
When data is written to register, the internal address register pointer is automatically incremented, so the next
data can be sent without repeating the device address and new register address. See figure below.


**Figure 17. Writing to multiple registers**

































































**5.2.9** **Reading from a single register**

The reading operation starts with a START condition followed by the 7-bit device address of the LED1202, the 8 [th]

bit of the byte is the R/W bit, which has to be set to 0 as writing operations. The LED1202 confirms the receiving
of the address + R/W bit by an acknowledge pulse. The address of the register, which should be read, is sent
afterward and confirmed again by an acknowledge pulse of the LED1202. Then the master generates a
RESTART condition and sends the 7-bit device address followed by the R/W bit, which now is set to 1 for reading
operations. The LED1202 confirms the receiving of the address + R/W bit by an acknowledge pulse and starts to
send the data to the master, one data per clock pulse always generated by master. No acknowledge pulse from
the master is required after receiving the data. Then the master generates a STOP condition to terminate the
communication. See figure below:


**DS12875** - **Rev 2** **page 19/54**


**LED1202**


**I²C bus interface**



**Figure 18. Reading from a single register**









































**5.2.10** **Reading from multiple registers with incremental addressing**


Reading from multiple registers starts in the same way like reading from a single register. As soon as the first
register is read, the internal register address pointer is automatically incremented. If the master generates an
acknowledge pulse after receiving the data from the first register, then reading of the next register can start
immediately without sending again the device address and the new register address. The last acknowledge pulse
before the STOP condition is not required. See figure below.


**Figure 19. Reading from multiple registers**











































































**DS12875** - **Rev 2** **page 20/54**


**LED1202**


**Application hints**


## **6 Application hints**

The following section presents some application hints. Both the schematic and minimum components to properly
run the application are shown.



**6.1** **Schematic diagram**


The figure below shows the LED1202 typical application.

VLED value depends on the V F of used LED. In case of Red LED with a V F max. of 1.8 V we can choose a VLED
of 2.3 V in order to guarantee enough headroom to current generator at 20 mA. While white LED with V F max. of
3.5 V is used, we have to use 4 V as VLED.

There is always the possibility to connect VLED to V IN in order to use a single power supply, in this case, the
optimization of power dissipation is not easy and a ballast resistor in series to each LED could be necessary.

I²C pins can support buses from 1V8 to 5 V, so the advice is to connect the pull-up resistors to the VI2C used by
MCU in order to have a perfect matching. The value of pull-up resistors could be adapted for different VI2C to
match V IH and V IL level and respect I²C specifications.



**Figure 20. LED driver schematic diagram**








































|1K N2 1 2 3|1K|20 19 18 17 16 1K 1µF|
|---|---|---|
|~~3~~<br>||20|
|~~4~~<br>|~~4~~<br>|~~4~~<br>|



**DS12875** - **Rev 2** **page 21/54**


**LED1202**


**Cascading multiple devices**


**6.1.1** **Component list**


The following table provides the list of the minimum components required to run the application.


**Table 6. Typical component list**

|Component name|Value|Unit|Comments|
|---|---|---|---|
|C1|1|μF|Input capacitor, rated voltage 6.3 V|
|C2|1|μF|LDO output capacitor, rated voltage 6.3 V|
|C3|2.2|μF|VLED filter capacitor, rated voltage 6.3 V|
|R1-R2-R3|1|KΩ|I²C bus and IRQn pull-up resistors (for VI2C = 1.8 V)|
|D0-D11|LED||Load LEDs|
|U1|LED1202||12 channels LED driver|



**6.2** **Cascading multiple devices**


It is possible to connect multiple LED1202 devices in a cascade or matrix. Each device in the cascade needs to
have a separately controlled local register area for full independent functionality. It is possible to define up to eight
different I²C addresses with only two pins. The whole interface (SDA, SCL, IRQn) is connected in parallel.


**Figure 21. Multiple device connection concept**
















|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||19<br>18<br>|18<br>|
|SCL||||20|20|
|SCL||||||
|IRQn||||||
|IRQn||||||
|IRQn||||19|19|
|IRQn||||20|20|
|IRQn||||||


























|Col1|Col2|Col3|R11|
|---|---|---|---|
|||G11|R10|
|B11<br>~~9~~|B11<br>~~9~~|||
|~~7~~<br>~~8~~<br>|~~7~~<br>~~8~~<br>|~~7~~<br>~~8~~<br>|~~7~~<br>~~8~~<br>|
|~~7~~|~~7~~|~~7~~|~~7~~|
|~~6~~||G10|R9|
|~~6~~||||
|~~6~~||G9|R8<br>|
|~~6~~||||
|~~6~~||G8||
|~~6~~|||R7|
|~~6~~||||
|~~6~~||G7|R6|
|B7<br><br>~~9~~|B7<br><br>~~9~~|||
|~~7~~<br>~~8~~|~~7~~<br>~~8~~|~~7~~<br>~~8~~|~~7~~<br>~~8~~|
|~~7~~|~~7~~|~~7~~|~~7~~|
|~~6~~||G6|R5|
|~~6~~||||
|~~6~~||G5|R4|
|~~6~~||||
|~~6~~||G4|R3|
|~~6~~||||
|~~6~~||G3|R2|
|B3<br><br>~~9~~|B3<br><br>~~9~~|||
|~~7~~<br>~~8~~|~~7~~<br>~~8~~|~~7~~<br>~~8~~|~~7~~<br>~~8~~|
|~~7~~|~~7~~|~~7~~|~~7~~|
|~~6~~||G2|R1|
|~~6~~||||
|~~6~~||G1|G1|



**DS12875** - **Rev 2** **page 22/54**


**LED1202**


**Cascading multiple devices**


If the application allows the same configuration and patterns to be used, and does not need any register read, the
number of devices is no longer limited by different I²C address (it depends only on I²C bus capability) because by
using the global address all devices can be set in the same way with a unique writing I²C command.

If an application with multiple devices has to run a synchronous pattern sequence, a common clock domain
configuration is needed. Figure 21. Multiple device connection concept shows a conceptual connection of a case
with three devices (for an RGB application) using a common clock domain in star configuration.

A0 (clock out) of the LED1202-Red (that is the master of the clock domain) is connected with all the A1 (clock in)
of slaves; the resistor R (for example 1.2 kΩ) to ground is needed to define the I²C address of the devices.

“Clock Configuration” register at address E0h has to be set to 02h for master (CLK_O_En = 1) and to 01h for all
the slaves (CLK_I_En = 1). It is important to apply the above-mentioned setting before enabling the devices (EN =
1), this is to be sure that each device latches its own I²C address before that clock runs on A0 and A1 pins.
Moreover, by using the global address to set EN = 1, all the devices start synchronized immediately using the
common clock domain.


**Figure 22. Command sequence example for star common clock domain configuration**









In case of common clock domain configured in daisy chain, master has to be set like before (CLK_O_En=1 and
CLK_I_En=0), while the slaves need to accept clock but also to cascade it. So they have to be configured with
CLK_O_En=1 and CLK_I_En=1 (value 03h in register E0h); except the last device in the chain that has not to
output the clock, so it must be set as CLK_O_En=0 and CLK_I_En=1.

We have to note that in daisy chain configuration each connection A0-A1 has to be independent, so it is
necessary to have a dedicated pull-up or pull-down resistor per link.


**DS12875** - **Rev 2** **page 23/54**


**LED1202**


**Cascading multiple devices**


**Figure 23. Concept of daisy chain common clock domain configuration**
















|Col1|Col2|Col3|Col4|Col5|Col6|18 17 16|
|---|---|---|---|---|---|---|
|||||||18|
|||||||19|
|SCL||||||20|
|SCL|||||||
|IRQn|||||||
|IRQn|||||||
|IRQn||||||18|
|IRQn|||||19|19|
|IRQn|||||20|20|
|IRQn|||||||
|IRQn|||||||
|IRQn||||||18|
|IRQn||||||19|
|IRQn||||||20|
|IRQn|||||||
|IRQn|||VI2C|VI2C|VI2C|VI2C|
|IRQn|||VI2C|VI2C|VI2C|18|
|IRQn||20<br>19|19|19|19|19|



If pins A0 and A1 of two different devices, connected by a clock link, cannot have the same defined level to set
the appropriate I [2] C address, the use of a simple resistor is no longer possible. In this case, it is possible to use
GPIOs from an MCU (see Figure 23. Concept of daisy chain common clock domain configuration) to define
dynamically the appropriate level, high or low, to set the I [2] C address of each device. After the 1 [st] communication,
MCU GPIOs must be put in Hi-Z to allow the clock transfer. Please, refer to Figure 24. Command sequence
example for daisy chain common clock domain configuration as the right implementation of this concept.


**DS12875** - **Rev 2** **page 24/54**


**LED1202**


**Cascading multiple devices**


**Figure 24. Command sequence example for daisy chain common clock domain configuration**









It is a good rule to configure clock configuration register starting from the slaves and ending with master, in any
case this must be done with all the devices disabled (EN=0).


**DS12875** - **Rev 2** **page 25/54**


**LED1202**


**Register description**

## **7 Register description**


The LED1202 can be monitored and controlled using the I²C communication interface.


Two different slave address types are available:

         - Global address 5Ch (7-bit)

         - Local address 58h to 5Bh and 5D to 60h (7-bit)


Global slave address is always available and fixed independently of A0 and A1 connection, it is used to control all
the devices on the same I²C bus with a single writing. Local address, defined by A0 and A1 connection, allows
each device to be controlled individually. Reading is possible using local address only.


The following table shows the registers map.


**Table 7. Register map**

|Add|Name|POR<br>value|B[7]|B[6]|B[5]|B[4]|B[3]|B[2]|B[1]|B[0]|
|---|---|---|---|---|---|---|---|---|---|---|
|**00h**|**Device ID**|**12h**|PROD_ID|PROD_ID|PROD_ID|PROD_ID|REV_ID|REV_ID|REV_ID|REV_ID|
|**01h**|**Device Enable**|**00h**|RST|||||||EN|
|**02h**|**Channel Enable Low**|**FFh**|CS7|CS6|CS5|CS4|CS3|CS2|CS1|CS0|
|**03h**|**Channel Enable High**|**0Fh**|||||CS11|CS10|CS9|CS8|
|**04h**|**Configuration**|**00h**|PATS|PATSR|AUTODIS|GCTRL|SHFT|PATSEL|PATSEL|PATSEL|
|**05h**|**Fault and Status Mask**|**0Bh**|||||SOF_M|PAT_M|OPEN_M|OVTP_M|
|**06h**|**Fault and Status Interrupt**|**00h**|||||SOF|PAT|OPEN|OVTP|
|**07h**|**Open LED Low**|**00h**|O_CS7|O_CS6|O_CS5|O_CS4|O_CS3|O_CS2|O_CS1|O_CS0|
|**08h**|**Open LED High**|**00h**|||||O_CS11|O_CS10|O_CS9|O_CS8|
|**09h**|**CS0 LED Current**|**27h**|ILED0|ILED0|ILED0|ILED0|ILED0|ILED0|ILED0|ILED0|
|**0Ah**|**CS1 LED Current**|**27h**|ILED1|ILED1|ILED1|ILED1|ILED1|ILED1|ILED1|ILED1|
|**0Bh**|**CS2 LED Current**|**27h**|ILED2|ILED2|ILED2|ILED2|ILED2|ILED2|ILED2|ILED2|
|**0Ch**|**CS3 LED Current**|**27h**|ILED3|ILED3|ILED3|ILED3|ILED3|ILED3|ILED3|ILED3|
|**0Dh**|**CS4 LED Current**|**27h**|ILED4|ILED4|ILED4|ILED4|ILED4|ILED4|ILED4|ILED4|
|**0Eh**|**CS5 LED Current**|**27h**|ILED5|ILED5|ILED5|ILED5|ILED5|ILED5|ILED5|ILED5|
|**0Fh**|**CS6 LED Current**|**27h**|ILED6|ILED6|ILED6|ILED6|ILED6|ILED6|ILED6|ILED6|
|**10h**|**CS7 LED Current**|**27h**|ILED7|ILED7|ILED7|ILED7|ILED7|ILED7|ILED7|ILED7|
|**11h**|**CS8 LED Current**|**27h**|ILED8|ILED8|ILED8|ILED8|ILED8|ILED8|ILED8|ILED8|
|**12h**|**CS9 LED Current**|**27h**|ILED9|ILED9|ILED9|ILED9|ILED9|ILED9|ILED9|ILED9|
|**13h**|**CS10 LED Current**|**27h**|ILED10|ILED10|ILED10|ILED10|ILED10|ILED10|ILED10|ILED10|
|**14h**|**CS11 LED Current**|**27h**|ILED11|ILED11|ILED11|ILED11|ILED11|ILED11|ILED11|ILED11|
|**15h**|**Pattern Sequence Repetition**|**01h**|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|
|**16h**|**Pattern 0 Duration**|**1Fh**|PAT0_DUR|PAT0_DUR|PAT0_DUR|PAT0_DUR|PAT0_DUR|PAT0_DUR|PAT0_DUR|PAT0_DUR|
|**17h**|**Pattern 1 Duration**|**1Fh**|PAT1_DUR|PAT1_DUR|PAT1_DUR|PAT1_DUR|PAT1_DUR|PAT1_DUR|PAT1_DUR|PAT1_DUR|
|**18h**|**Pattern 2 Duration**|**1Fh**|PAT2_DUR|PAT2_DUR|PAT2_DUR|PAT2_DUR|PAT2_DUR|PAT2_DUR|PAT2_DUR|PAT2_DUR|
|**19h**|**Pattern 3 Duration**|**1Fh**|PAT3_DUR|PAT3_DUR|PAT3_DUR|PAT3_DUR|PAT3_DUR|PAT3_DUR|PAT3_DUR|PAT3_DUR|
|**1Ah**|**Pattern 4 Duration**|**1Fh**|PAT4_DUR|PAT4_DUR|PAT4_DUR|PAT4_DUR|PAT4_DUR|PAT4_DUR|PAT4_DUR|PAT4_DUR|



**DS12875** - **Rev 2** **page 26/54**


**LED1202**


**Register description**

|Add|Name|POR<br>value|B[7]|B[6]|B[5]|B[4]|B[3]|B[2]|B[1]|B[0]|
|---|---|---|---|---|---|---|---|---|---|---|
|**1Bh**|**Pattern 5 Duration**|**1Fh**|PAT5_DUR|PAT5_DUR|PAT5_DUR|PAT5_DUR|PAT5_DUR|PAT5_DUR|PAT5_DUR|PAT5_DUR|
|**1Ch**|**Pattern 6 Duration**|**1Fh**|PAT6_DUR|PAT6_DUR|PAT6_DUR|PAT6_DUR|PAT6_DUR|PAT6_DUR|PAT6_DUR|PAT6_DUR|
|**1Dh**|**Pattern 7 Duration**|**1Fh**|PAT7_DUR|PAT7_DUR|PAT7_DUR|PAT7_DUR|PAT7_DUR|PAT7_DUR|PAT7_DUR|PAT7_DUR|
|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|**Address offset 1Eh**|
|**00h**|**Pattern0CS0 PWM Low**|**55h**|PWM0_0_L|PWM0_0_L|PWM0_0_L|PWM0_0_L|PWM0_0_L|PWM0_0_L|PWM0_0_L|PWM0_0_L|
|**01h**|**Pattern0CS0 PWM High**|**05h**|||||PWM0_0_H|PWM0_0_H|PWM0_0_H|PWM0_0_H|
|**02h**|**Pattern0CS1 PWM Low**|**55h**|PWM1_0_L|PWM1_0_L|PWM1_0_L|PWM1_0_L|PWM1_0_L|PWM1_0_L|PWM1_0_L|PWM1_0_L|
|**03h**|**Pattern0CS1 PWM High**|**05h**|||||PWM1_0_H|PWM1_0_H|PWM1_0_H|PWM1_0_H|
|**04h**|**Pattern0CS2 PWM Low**|**55h**|PWM2_0_L|PWM2_0_L|PWM2_0_L|PWM2_0_L|PWM2_0_L|PWM2_0_L|PWM2_0_L|PWM2_0_L|
|**05h**|**Pattern0CS2 PWM High**|**05h**|||||PWM2_0_H|PWM2_0_H|PWM2_0_H|PWM2_0_H|
|**06h**|**Pattern0CS3 PWM Low**|**55h**|PWM3_0_L|PWM3_0_L|PWM3_0_L|PWM3_0_L|PWM3_0_L|PWM3_0_L|PWM3_0_L|PWM3_0_L|
|**07h**|**Pattern0CS3 PWM High**|**05h**|||||PWM3_0_H|PWM3_0_H|PWM3_0_H|PWM3_0_H|
|**08h**|**Pattern0CS4 PWM Low**|**55h**|PWM4_0_L|PWM4_0_L|PWM4_0_L|PWM4_0_L|PWM4_0_L|PWM4_0_L|PWM4_0_L|PWM4_0_L|
|**09h**|**Pattern0CS4 PWM High**|**05h**|||||PWM4_0_H|PWM4_0_H|PWM4_0_H|PWM4_0_H|
|**0Ah**|**Pattern0CS5 PWM Low**|**55h**|PWM5_0_L|PWM5_0_L|PWM5_0_L|PWM5_0_L|PWM5_0_L|PWM5_0_L|PWM5_0_L|PWM5_0_L|
|**0Bh**|**Pattern0CS5 PWM High**|**05h**|||||PWM5_0_H|PWM5_0_H|PWM5_0_H|PWM5_0_H|
|**0Ch**|**Pattern0CS6 PWM Low**|**55h**|PWM6_0_L|PWM6_0_L|PWM6_0_L|PWM6_0_L|PWM6_0_L|PWM6_0_L|PWM6_0_L|PWM6_0_L|
|**0Dh**|**Pattern0CS6 PWM High**|**05h**|||||PWM6_0_H|PWM6_0_H|PWM6_0_H|PWM6_0_H|
|**0Eh**|**Pattern0CS7 PWM Low**|**55h**|PWM7_0_L|PWM7_0_L|PWM7_0_L|PWM7_0_L|PWM7_0_L|PWM7_0_L|PWM7_0_L|PWM7_0_L|
|**0Fh**|**Pattern0CS7 PWM High**|**05h**|||||PWM7_0_H|PWM7_0_H|PWM7_0_H|PWM7_0_H|
|**10h**|**Pattern0CS8 PWM Low**|**55h**|PWM8_0_L|PWM8_0_L|PWM8_0_L|PWM8_0_L|PWM8_0_L|PWM8_0_L|PWM8_0_L|PWM8_0_L|
|**11h**|**Pattern0CS8 PWM High**|**05h**|||||PWM8_0_H|PWM8_0_H|PWM8_0_H|PWM8_0_H|
|**12h**|**Pattern0CS9 PWM Low**|**55h**|PWM9_0_L|PWM9_0_L|PWM9_0_L|PWM9_0_L|PWM9_0_L|PWM9_0_L|PWM9_0_L|PWM9_0_L|
|**13h**|**Pattern0CS9 PWM High**|**05h**|||||PWM9_0_H|PWM9_0_H|PWM9_0_H|PWM9_0_H|
|**14h**|**Pattern0CS10 PWM Low**|**55h**|PWM10_0_L|PWM10_0_L|PWM10_0_L|PWM10_0_L|PWM10_0_L|PWM10_0_L|PWM10_0_L|PWM10_0_L|
|**15h**|**Pattern0CS10 PWM High**|**05h**|||||PWM10_0_H|PWM10_0_H|PWM10_0_H|PWM10_0_H|
|**16h**|**Pattern0CS11 PWM Low**|**55h**|PWM11_0_L|PWM11_0_L|PWM11_0_L|PWM11_0_L|PWM11_0_L|PWM11_0_L|PWM11_0_L|PWM11_0_L|
|**17h**|**Pattern0CS11 PWM High**|**05h**|||||PWM11_0_H|PWM11_0_H|PWM11_0_H|PWM11_0_H|
|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|**Address offset 36h**|
|**00h**|**Pattern1CS0 PWM Low**|**FFh**|PWM0_1_L|PWM0_1_L|PWM0_1_L|PWM0_1_L|PWM0_1_L|PWM0_1_L|PWM0_1_L|PWM0_1_L|
|**01h**|**Pattern1CS0 PWM High**|**0Fh**|||||PWM0_1_H|PWM0_1_H|PWM0_1_H|PWM0_1_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern1CS11 PWM Low**|**FFh**|PWM11_1_L|PWM11_1_L|PWM11_1_L|PWM11_1_L|PWM11_1_L|PWM11_1_L|PWM11_1_L|PWM11_1_L|
|**17h**|**Pattern1CS11 PWM High**|**0Fh**|||||PWM11_1_H|PWM11_1_H|PWM11_1_H|PWM11_1_H|
|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|**Address offset 4Eh**|
|**00h**|**Pattern2CS0 PWM Low**|**FFh**|PWM0_2_L|PWM0_2_L|PWM0_2_L|PWM0_2_L|PWM0_2_L|PWM0_2_L|PWM0_2_L|PWM0_2_L|
|**01h**|**Pattern2CS0 PWM High**|**0Fh**|||||PWM0_2_H|PWM0_2_H|PWM0_2_H|PWM0_2_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern2CS11 PWM Low**|**FFh**|PWM11_2_L|PWM11_2_L|PWM11_2_L|PWM11_2_L|PWM11_2_L|PWM11_2_L|PWM11_2_L|PWM11_2_L|
|**17h**|**Pattern2CS11 PWM High**|**0Fh**|||||PWM11_2_H|PWM11_2_H|PWM11_2_H|PWM11_2_H|



**DS12875** - **Rev 2** **page 27/54**


**LED1202**


**Register description**

|Add|Name|POR<br>value|B[7]|B[6]|B[5]|B[4]|B[3]|B[2]|B[1]|B[0]|
|---|---|---|---|---|---|---|---|---|---|---|
|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|**Address offset 66h**|
|**00h**|**Pattern3CS0 PWM Low**|**FFh**|PWM0_3_L|PWM0_3_L|PWM0_3_L|PWM0_3_L|PWM0_3_L|PWM0_3_L|PWM0_3_L|PWM0_3_L|
|**01h**|**Pattern3CS0 PWM High**|**0Fh**|||||PWM0_3_H|PWM0_3_H|PWM0_3_H|PWM0_3_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern3CS11 PWM Low**|**FFh**|PWM11_3_L|PWM11_3_L|PWM11_3_L|PWM11_3_L|PWM11_3_L|PWM11_3_L|PWM11_3_L|PWM11_3_L|
|**17h**|**Pattern3CS11 PWM High**|**0Fh**|||||PWM11_3_H|PWM11_3_H|PWM11_3_H|PWM11_3_H|
|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|**Address offset 7Eh**|
|**00h**|**Pattern4CS0 PWM Low**|**FFh**|PWM0_4_L|PWM0_4_L|PWM0_4_L|PWM0_4_L|PWM0_4_L|PWM0_4_L|PWM0_4_L|PWM0_4_L|
|**01h**|**Pattern4CS0 PWM High**|**0Fh**|||||PWM0_4_H|PWM0_4_H|PWM0_4_H|PWM0_4_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern4CS11 PWM Low**|**FFh**|PWM11_4_L|PWM11_4_L|PWM11_4_L|PWM11_4_L|PWM11_4_L|PWM11_4_L|PWM11_4_L|PWM11_4_L|
|**17h**|**Pattern4CS11 PWM High**|**0Fh**|||||PWM11_4_H|PWM11_4_H|PWM11_4_H|PWM11_4_H|
|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|**Address offset 96h**|
|**00h**|**Pattern5CS0 PWM Low**|**FFh**|PWM0_5_L|PWM0_5_L|PWM0_5_L|PWM0_5_L|PWM0_5_L|PWM0_5_L|PWM0_5_L|PWM0_5_L|
|**01h**|**Pattern5CS0 PWM High**|**0Fh**|||||PWM0_5_H|PWM0_5_H|PWM0_5_H|PWM0_5_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern5CS11 PWM Low**|**FFh**|PWM11_5_L|PWM11_5_L|PWM11_5_L|PWM11_5_L|PWM11_5_L|PWM11_5_L|PWM11_5_L|PWM11_5_L|
|**17h**|**Pattern5CS11 PWM High**|**0Fh**|||||PWM11_5_H|PWM11_5_H|PWM11_5_H|PWM11_5_H|
|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|**Address offset AEh**|
|**00h**|**Pattern6CS0 PWM Low**|**FFh**|PWM0_6_L|PWM0_6_L|PWM0_6_L|PWM0_6_L|PWM0_6_L|PWM0_6_L|PWM0_6_L|PWM0_6_L|
|**01h**|**Pattern6CS0 PWM High**|**0Fh**|||||PWM0_6_H|PWM0_6_H|PWM0_6_H|PWM0_6_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern6CS11 PWM Low**|**FFh**|PWM11_6_L|PWM11_6_L|PWM11_6_L|PWM11_6_L|PWM11_6_L|PWM11_6_L|PWM11_6_L|PWM11_6_L|
|**17h**|**Pattern6CS11 PWM High**|**0Fh**|||||PWM11_6_H|PWM11_6_H|PWM11_6_H|PWM11_6_H|
|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|**Address offset C6h**|
|**00h**|**Pattern7CS0 PWM Low**|**FFh**|PWM0_7_L|PWM0_7_L|PWM0_7_L|PWM0_7_L|PWM0_7_L|PWM0_7_L|PWM0_7_L|PWM0_7_L|
|**01h**|**Pattern7CS0 PWM High**|**0Fh**|||||PWM0_7_H|PWM0_7_H|PWM0_7_H|PWM0_7_H|
|**…**|**…**|**…**|…|…|…|…|…|…|…|…|
|**16h**|**Pattern7CS11 PWM Low**|**FFh**|PWM11_7_L|PWM11_7_L|PWM11_7_L|PWM11_7_L|PWM11_7_L|PWM11_7_L|PWM11_7_L|PWM11_7_L|
|**17h**|**Pattern7CS11 PWM High**|**0Fh**|||||PWM11_7_H|PWM11_7_H|PWM11_7_H|PWM11_7_H|
|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|**Address offset 00h**|
|**E0h**|**Clock Configuration**|**00h**|||||||CLK_O_En|CLK_I_En|



**DS12875** - **Rev 2** **page 28/54**


**LED1202**


**Device ID register**


**7.1** **Device ID register**


**Table 8. Device ID register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 00h|PROD_ID|PROD_ID|PROD_ID|PROD_ID|REV_ID|REV_ID|REV_ID|REV_ID|
|POR = 12h|0|0|0|1|0|0|1|0|
|Comments|R|R|R|R|R|R|R|R|



**REV_ID:** Silicon release identification

         - 02h: cut 1.1


**PROD_ID:** Product identification

         - 01h: LED1202


**DS12875** - **Rev 2** **page 29/54**


**LED1202**


**Device enable register**


**7.2** **Device enable register**


**Table 9. Device enable register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 01h|RST|-|-|-|-|-|-|EN|
|POR = 00h|0|0|0|0|0|0|0|0|
|Comments|R/W|R|R|R|R|R|R|R/W|



**EN:** Enable device

         - 0: device is disabled (default)

         - 1: device is enabled


**RST:** Reset device

         - 0: device is not reset (default)

         - 1: device is reset to default values


**DS12875** - **Rev 2** **page 30/54**


**LED1202**


**Channel enable registers**


**7.3** **Channel enable registers**


**Table 10. Channel enable low register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 02h|EN_CS7|EN_CS6|EN_CS5|EN_CS4|EN_CS3|EN_CS2|EN_CS1|EN_CS0|
|POR = FFh|1|1|1|1|1|1|1|1|
|Comments|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



**Table 11. Channel enable high register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 03h|-|-|-|-|EN_CS11|EN_CS10|EN_CS9|EN_CS8|
|POR = 0Fh|0|0|0|0|1|1|1|1|
|Comments|R|R|R|R|R/W|R/W|R/W|R/W|



**EN_CS0:** LED channel 0 enable

         - 0: channel is disabled

         - 1: channel is enabled (default)


**EN_CS11:** LED channel 11 enable

         - 0: channel is disabled

         - 1: channel is enabled (default)


**DS12875** - **Rev 2** **page 31/54**


**LED1202**


**Configuration register**


**7.4** **Configuration register**


**Table 12. Configuration register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 04h|PATS|PATSR|AUTODIS|GCTRL|SHFT|PATSEL|PATSEL|PATSEL|
|POR = 00h|0|0|0|0|0|0|0|0|
|Comments|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



**PATSEL:** Pattern selection

         - 000: pattern 0 is selected (default)

         - 001: pattern 1 is selected

         -          - ··

         - 111: pattern 7 is selected


**SHFT:** Phase-shift feature

         - 0: feature is disabled (default)

         - 1: feature is enabled


**AUTODIS:** Auto disable device at the end of patterns sequence

         -          - 0: Auto disable off

         -          - 1: Auto disable on


_Note:_ _If AUTODIS=1, after the pattern repetition it is necessary to re-enable the device (by writing EN=1 in the enable_
_register 01h). This setting guarantees the running of internal system clock mandatory to read the status_
_registers._


**GCTRL:** Group control

         - 0: feature is disabled (default)

         - 1: feature is enabled, PatternyCS0 PWM Low/High (y selected by PATSEL[2:0]) is used for all channels (can
be used for backlight where each LED uses the same dimming)


**PATSR:** Pattern sequence runs (self-clear when sequence is finished)

         - 0: pattern sequence is finished (default)

         - 1: pattern sequence is run


**PATS:** Pattern sequence feature enable

         - 0: pattern sequence feature is disabled (default)

         - 1: pattern sequence feature is enabled; all outputs OFF when sequence does not run


**DS12875** - **Rev 2** **page 32/54**


**LED1202**


**Fault and status mask register**


**7.5** **Fault and status mask register**


**Table 13. Fault and status mask register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 05h|-|-|-|-|SOF_M|PAT_M|OPEN_M|OVTP_M|
|POR = 0Bh|0|0|0|0|1|0|1|1|
|Comments|R|R|R|R|R/W|R/W|R/W|R/W|



**OVTP_M:** Chip overtemperature protection interrupt mask bit

         - 0: interrupt not masked

         - 1: interrupt masked


**OPEN_M:** Open LED detection on CS0-CS11 interrupt mask bit

         - 0: interrupt not masked

         - 1: interrupt masked


**PAT_M:** Pattern sequence finished interrupt mask bit

         - 0: interrupt not masked

         - 1: interrupt masked


**SOF_M:** Start of PWM frame interrupt mask bit

         - 0: interrupt not masked

         - 1: interrupt masked


**DS12875** - **Rev 2** **page 33/54**


**LED1202**


**Fault and status interrupt register**


**7.6** **Fault and status interrupt register**


**Table 14. Fault and status interrupt register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 06h|-|-|-|-|SOF|PAT|OPEN|OVTP|
|POR = 00h|0|0|0|0|0|0|0|0|
|Comments|R|R|R|R|R|R|R|R|



**OVTP:** Chip overtemperature protection reached

0: OVTP not occurred

1: OVTP occurred

**OPEN:** Open LED detection on CS0-CS11

0: Open led on CSx not occurred

1: Open led on CSx occurred

**PAT:** Pattern sequence finished

0: Pattern sequence not finished

1: Pattern sequence finished

**SOF:** Start of PWM frame interrupt flag

0: PWM frame not started

1: PWM frame started


**DS12875** - **Rev 2** **page 34/54**


**LED1202**


**Open LED registers**


**7.7** **Open LED registers**


**Table 15. Open LED low register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 07h|O_CS7|O_CS6|O_CS5|O_CS4|O_CS3|O_CS2|O_CS1|O_CS0|
|POR = 00h|0|0|0|0|0|0|0|0|
|Comments|R|R|R|R|R|R|R|R|



**Table 16. Open LED high register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 08h|-|-|-|-|O_CS11|O_CS10|O_CS9|O_CS8|
|POR = 00h|0|0|0|0|0|0|0|0|
|Comments|R|R|R|R|R|R|R|R|



If respective bit is set:

**CS0:** channel 0 is open

          - ··

**CS11:** channel 11 is open


**DS12875** - **Rev 2** **page 35/54**


**LED1202**


**LED current registers**


**7.8** **LED current registers**


**Table 17. CSx LED current register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = ADD(1)|ILEDx|ILEDx|ILEDx|ILEDx|ILEDx|ILEDx|ILEDx|ILEDx|
|POR = 27h|0|0|1|0|0|1|1|1|
|Comments<br>|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



_1._ _ADD = 09h + xh, where x is the channel number in hexadecimal (x = 00h .. 0Bh)_


**ILEDx:** Channel x LED current selection

I CS_SET = ILEDx_value/255 * 20 mA


         - LSB: 20 mA / 255 (step size)

         - Range: 1 mA to 20 mA (3.06 mA as default)


_Note:_ _Registers value from 00h to 0Dh are functional, but the ILED provided is not guaranteed to be monotonic and_
_accurate. 00h does not switch OFF the channel; it provides a minimal uncontrolled current because of some_
_internal offsets._


**DS12875** - **Rev 2** **page 36/54**


**LED1202**


**Pattern sequence repetition register**


**7.9** **Pattern sequence repetition register**


**Table 18. Pattern sequence repetition number register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = 15h|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|PAT_REP|
|POR = 01h|0|0|0|0|0|0|0|1|
|Comments|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



**PAT_REP:** Pattern sequence repetition number selection

         - LSB: 1 time

         - Range: 1 time to 254 times (not allowed to write PAT_REP=00h)

         - Infinite loop: PAT_REP = FFh


**DS12875** - **Rev 2** **page 37/54**


**LED1202**


**Pattern duration registers**


**7.10** **Pattern duration registers**


**Table 19. Pattern y duration time register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = ADD(1)|PATy_DUR|PATy_DUR|PATy_DUR|PATy_DUR|PATy_DUR|PATy_DUR|PATy_DUR|PATy_DUR|
|POR = 1Fh|0|0|0|1|1|1|1|1|
|Comments<br>|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



_1._ _ADD = 16h + yh, where y is the pattern number in hexadecimal (y = 00h .. 07h)_


**PATy_DUR:** Pattern y duration time selection

         - LSB: 22.2 ms

         - Range: 22.2 ms to 5660 ms (690 ms as default)

         - Pattern skip: PATy_DUR = 00h


**DS12875** - **Rev 2** **page 38/54**


**LED1202**


**Pattern PWM configuration registers**


**7.11** **Pattern PWM configuration registers**


**Table 20. Pattern0CSx PWM low register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = ADDL(1)|PWMx_0_L|PWMx_0_L|PWMx_0_L|PWMx_0_L|PWMx_0_L|PWMx_0_L|PWMx_0_L|PWMx_0_L|
|POR = 55h|0|1|0|1|0|1|0|1|
|Comments<br>|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



_1._ _ADDL = 1Eh + 2*(xh), where x is the channel number in hexadecimal (x = 00h .. 0Bh)_


**Table 21. Pattern0CSx PWM high register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = ADDH(1)|-|-|-|-|PWMx_0_H|PWMx_0_H|PWMx_0_H|PWMx_0_H|
|POR = 05h|0|0|0|0|0|1|0|1|
|Comments<br>|R|R|R|R|R/W|R/W|R/W|R/W|



_1._ _ADDH = 1Eh + 01h + 2(xh), where x is the channel number in hexadecimal (x = 00h .. 0Bh)_


**PWMx_0_L:** represents low 8 bits of PWM duty cycle value

**PWMx_0_H:** represents high 4 bits of PWM duty cycle value

         - LSB: 1/4095 (step size)

         - Offset: 0


**(555h as default; channel ON with PWM at 33%)**


**Table 22. PatternyCSx PWM low register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = ADDL|PWMx_y_L|PWMx_y_L|PWMx_y_L|PWMx_y_L|PWMx_y_L|PWMx_y_L|PWMx_y_L|PWMx_y_L|
|POR = FFh(1)|1|1|1|1|1|1|1|1|
|Comments<br>|R/W|R/W|R/W|R/W|R/W|R/W|R/W|R/W|



_1._ _ADDL = 1Eh + 2*(xh) + 18h*(yh), where x is the channel number in hexadecimal (x = 00h .. 0Bh) and y is the pattern_
_number in hexadecimal (y = 01h .. 07h)_


**Table 23. PatternyCSx PWM high register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = ADDH(1)|-|-|-|-|PWMx_y_H|PWMx_y_H|PWMx_y_H|PWMx_y_H|
|POR = 0Fh|0|0|0|0|1|1|1|1|
|Comments<br>|R|R|R|R|R/W|R/W|R/W|R/W|



_1._ _ADDH = 1Eh + 01h + 2(xh) +18h*(yh), where x is the channel number in hexadecimal (x = 00h .. 0Bh) and y is the pattern_
_number in hexadecimal (y = 01h .. 07h)_


**PWMx_y_L:** represents low 8 bits of PWM duty cycle value

**PWMx_y_H:** represents high 4 bits of PWM duty cycle value

         - LSB: 1/4095 (step size)

         - Offset: 0


**(FFFh as default; channel ON with PWM at 100% = fully ON)**


**DS12875** - **Rev 2** **page 39/54**


**LED1202**


**Pattern PWM configuration registers**


**Table 24. PatternyCSx PWM low/high registers**
















|CSx|Patterny<br>low/high register ADDRs (hex)<br>Default value (hex)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|**CS0**|1E/1F<br>555|36/37<br>FFF|4E/4F<br>FFF|66/67<br>FFF|7E/7F<br>FFF|96/97<br>FFF|AE/AF<br>FFF|C6/C7<br>FFF|
|**CS1**|20/21<br>555|38/39<br>FFF|50/51<br>FFF|68/69<br>FFF|80/81<br>FFF|98/99<br>FFF|B0/B1<br>FFF|C8/C9<br>FFF|
|**CS2**|22/23<br>555|3A/3B<br>FFF|52/53<br>FFF|6A/6B<br>FFF|82/83<br>FFF|9A/9B<br>FFF|B2/B3<br>FFF|CA/CB<br>FFF|
|**CS3**|24/25<br>555|3C/3D<br>FFF|54/55<br>FFF|6C/6D<br>FFF|84/85<br>FFF|9C/9D<br>FFF|B4/B5<br>FFF|CC/CD<br>FFF|
|**CS4**|26/27<br>555|3E/3F<br>FFF|56/57<br>FFF|6E/6F<br>FFF|86/87<br>FFF|9E/9F<br>FFF|B6/B7<br>FFF|CE/CF<br>FFF|
|**CS5**|28/29<br>555|40/41<br>FFF|58/59<br>FFF|70/71<br>FFF|88/89<br>FFF|A0/A1<br>FFF|B8/B9<br>FFF|D0/D1<br>FFF|
|**CS6**|2A/2B<br>555|42/43<br>FFF|5A/5B<br>FFF|72/73<br>FFF|8A/8B<br>FFF|A2/A3<br>FFF|BA/BB<br>FFF|D2/D3<br>FFF|
|**CS7**|2C/2D<br>555|44/45<br>FFF|5C/5D<br>FFF|74/75<br>FFF|8C/8D<br>FFF|A4/A5<br>FFF|BC/BD<br>FFF|D4/D5<br>FFF|
|**CS8**|2E/2F<br>555|46/47<br>FFF|5E/5F<br>FFF|76/77<br>FFF|8E/8F<br>FFF|A6/A7<br>FFF|BE/BF<br>FFF|D6/D7<br>FFF|
|**CS9**|30/31<br>555|48/49<br>FFF|60/61<br>FFF|78/79<br>FFF|90/91<br>FFF|A8/A9<br>FFF|C0/C1<br>FFF|D8/D9<br>FFF|
|**CS10**|32/33<br>555|4A/4B<br>FFF|62/63<br>FFF|7A/7B<br>FFF|92/93<br>FFF|AA/AB<br>FFF|C2/C3<br>FFF|DA/DB<br>FFF|
|**CS11**|34/35<br>555|4C/4D<br>FFF|64/65<br>FFF|7C/7D<br>FFF|94/95<br>FFF|AC/AD<br>FFF|C4/C5<br>FFF|DC/DD<br>FFF|



**DS12875** - **Rev 2** **page 40/54**


**LED1202**


**Clock configuration register**


**7.12** **Clock configuration register**


**Table 25. Clock Configuration register format**

|Col1|Bit 7|Bit 6|Bit5|Bit4|Bit 3|Bit 2|Bit1|Bit 0|
|---|---|---|---|---|---|---|---|---|
|Add = E0h|-|-|-|-|-|-|CLK_O_En|CLK_I_En|
|POR = 00h|0|0|0|0|0|0|0|0|
|Comments|R|R|R|R|R|R|R/W|R/W|



**CLK_O_En:** Enable internal clock output to A0

0: Disable

1: Enable

**CLK_I_En:** Enable external clock input to A1

0: Disable

1: Enable


_Note:_ _After first ACK, device latches the I²C address freeing A0 and A1 for different use_


**DS12875** - **Rev 2** **page 41/54**


**LED1202**


**Package information**

## **8 Package information**


[In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK](https://www.st.com/ecopack) [®]

packages, depending on their level of environmental compliance. ECOPACK [®] specifications, grade definitions
[and product status are available at: www.st.com. ECOPACK](http://www.st.com) [®] is an ST trademark.


**DS12875** - **Rev 2** **page 42/54**


**LED1202**


**WLCSP20 (1.71 x 2.16 x 0.5 mm) package information**


**8.1** **WLCSP20 (1.71 x 2.16 x 0.5 mm) package information**


The LED1202JR is in Wafer Level Chip Scale Package (WLCSP).


**Figure 25. WLCSP20 (1.71 x 2.16 x 0.5 mm) package outline**


**Table 26. WLCSP20 (1.71 x 2.16 x 0.5 mm) package mechanical data**

|Dim.|mm|Col3|Col4|
|---|---|---|---|
|**Dim.**|**Min.**|**Typ.**|**Max.**|
|A|0.537|0.595|0.653|
|A1|0.165||0.225|
|A2|0.022|0.025|0.028|
|A3|0.285|0.300|0.315|
|E|1.689|1.709|1.729|
|D|2.144|2.164|2,184|
|SE|0.2 BSC|0.2 BSC|0.2 BSC|
|E1|1.2 BSC|1.2 BSC|1.2 BSC|
|D1|1.6 BSC|1.6 BSC|1.6 BSC|
|e||0.4||
|b|0.21|0.24|0.27|



**DS12875** - **Rev 2** **page 43/54**


**LED1202**


**WLCSP20 (1.71 x 2.16 x 0.5 mm) package information**


**Figure 26. WLCSP20 (1.71 x 2.16 x 0.5 mm) recommended footprint**


**DS12875** - **Rev 2** **page 44/54**


**LED1202**


**QFN20 3x3 package information**


**8.2** **QFN20 3x3 package information**


The LED1202QTR is in Quad Flat No-lead (QFN) package.


**Figure 27. QFN20 3x3 (3 x 3 x 0.6 mm 20 L with 0.5 mm pitch) package outline**


**DS12875** - **Rev 2** **page 45/54**


**LED1202**


**QFN20 3x3 package information**


**Table 27. QFN20 3x3 (3 x 3 x 0.6 mm 20 L with 0.5 mm pitch) package mechanical data**

|Dim.|mm|Col3|Col4|
|---|---|---|---|
|**Dim.**|**Min.**|**Typ.**|**Max.**|
|A|0.50|0.55|0.60|
|A1|0.00|0.02|0.05|
|A3||0.153 Ref.||
|b|0.18|0.25|0.30|
|D|3.00 BSC|3.00 BSC|3.00 BSC|
|E|3.00 BSC|3.00 BSC|3.00 BSC|
|e|0.50 BSC|0.50 BSC|0.50 BSC|
|L1|0.45|0.55|0.65|
|L2|0.30|0.40|0.50|
|L3|0.85|0.95|1.05|
|L4|0.25|0.35|0.45|
|k||0.25 Ref.||
|N|20|20|20|



**Figure 28. QFN20 3x3 (3 x 3 x 0.6 mm 20 L with 0.5 mm pitch) recommended footprint**


**DS12875** - **Rev 2** **page 46/54**


**LED1202**


**Ordering information**

## **9 Ordering information**


**Table 28. Ordering information**

|Order code|Package|Packing|
|---|---|---|
|LED1202QTR|QFN20 3x3|Tape and reel|
|LED1202JR|WLCSP20|WLCSP20|



**DS12875** - **Rev 2** **page 47/54**


**LED1202**


**Revision history**


**Table 29. Document revision history**

|Date|Revision|Changes|
|---|---|---|
|31-Jan-2019|1|First release.|
|14-Feb-2019|2|Updated package figure on the cover page.|



**DS12875** - **Rev 2** **page 48/54**


**LED1202**


**Contents**

## **Contents**


**1** **Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2**


**1.1** Block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2


**2** **Pinout and pin description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3**


**2.1** WLCSP20 package - ball assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


**2.2** QFN20 3x3 package - pin assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


**2.3** Pin description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


**3** **Electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5**


**3.1** Maximum ratings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


**3.2** Thermal information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


**3.3** LED1202 electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6


**3.4** Headroom voltage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8


**4** **Device description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9**


**4.1** Device startup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**4.2** Device reset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**4.3** Device address selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**4.4** LED channel selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


**4.5** Output dimming modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .10


**4.5.1** LED controlled by “CSx LED Current” registers (analog dimming) . . . . . . . . . . . . . . . . . . 10


**4.5.2** LED controlled by “PatternyCSx PWM” registers (digital dimming) . . . . . . . . . . . . . . . . . . 10


**4.5.3** LED controlled by “CSx LED Current” and “PatternyCSx PWM” registers. . . . . . . . . . . . . 11


**4.6** Phase-shift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11


**4.7** Pattern selection and configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .12


**4.8** Pattern sequence configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .12


**4.9** Device synchronization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13


**4.9.1** Common clock domain configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13


**4.10** Alarms and IRQ generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .13


**4.10.1** Open LED interrupt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**4.10.2** Overtemperature protection (OVTP) interrupt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**4.10.3** Pattern end interrupt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**DS12875** - **Rev 2** **page 49/54**


**LED1202**


**Contents**


**4.10.4** Start of frame interrupt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


**5** **Device interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16**


**5.1** IRQn output pin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16


**5.2** I²C bus interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16


**5.2.1** The LED1202 addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


**5.2.2** Data validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16


**5.2.3** Start and stop conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17


**5.2.4** Byte format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17


**5.2.5** Acknowledge. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17


**5.2.6** Interface protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


**5.2.7** Writing to a single register. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


**5.2.8** Writing to multiple registers with incremental addressing . . . . . . . . . . . . . . . . . . . . . . . . . 19


**5.2.9** Reading from a single register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


**5.2.10** Reading from multiple registers with incremental addressing . . . . . . . . . . . . . . . . . . . . . . 20


**6** **Application hints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21**


**6.1** Schematic diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21


**6.1.1** Component list . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


**6.2** Cascading multiple devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .22


**7** **Register description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26**


**7.1** Device ID register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29


**7.2** Device enable register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .30


**7.3** Channel enable registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .31


**7.4** Configuration register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32


**7.5** Fault and status mask register. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .33


**7.6** Fault and status interrupt register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34


**7.7** Open LED registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .35


**7.8** LED current registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .36


**7.9** Pattern sequence repetition register. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .37


**7.10** Pattern duration registers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .38


**7.11** Pattern PWM configuration registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .39


**7.12** Clock configuration register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .41


**DS12875** - **Rev 2** **page 50/54**


**LED1202**


**Contents**


**8** **Package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .42**


**8.1** WLCSP20 (1.71 x 2.16 x 0.5 mm) 20 package information. . . . . . . . . . . . . . . . . . . . . . . . . . . 43


**8.2** VFQFPN (3 x 3 x 0.6 mm 20 L) package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


**9** **Ordering information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .47**


**Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .48**


**DS12875** - **Rev 2** **page 51/54**


**LED1202**


**List of tables**

## **List of tables**


**Table 1.** Pin description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
**Table 2.** Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

**Table 3.** Thermal data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

**Table 4.** LED1202 electrical characteristics V IN = 3.3 V, SDA, SCL and IRQn = 1.8 V, T a = 25 °C, RC load = 50 Ω//10 pF,
unless otherwise specified. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

**Table 5.** LED1202 local address table. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

**Table 6.** Typical component list . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
**Table 7.** Register map. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
**Table 8.** Device ID register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
**Table 9.** Device enable register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
**Table 10.** Channel enable low register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
**Table 11.** Channel enable high register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
**Table 12.** Configuration register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
**Table 13.** Fault and status mask register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
**Table 14.** Fault and status interrupt register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
**Table 15.** Open LED low register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
**Table 16.** Open LED high register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
**Table 17.** CSx LED current register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
**Table 18.** Pattern sequence repetition number register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
**Table 19.** Pattern y duration time register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
**Table 20.** Pattern0CSx PWM low register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
**Table 21.** Pattern0CSx PWM high register format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
**Table 22.** PatternyCSx PWM low register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
**Table 23.** PatternyCSx PWM high register format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
**Table 24.** PatternyCSx PWM low/high registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
**Table 25.** Clock Configuration register format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
**Table 26.** WLCSP20 (1.71 x 2.16 x 0.5 mm) package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
**Table 27.** QFN20 3x3 (3 x 3 x 0.6 mm 20 L with 0.5 mm pitch) package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . 46
**Table 28.** Ordering information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
**Table 29.** Document revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48


**DS12875** - **Rev 2** **page 52/54**


**LED1202**


**List of figures**

## **List of figures**


**Figure 1.** LED1202 simplified block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
**Figure 2.** LED1202JR ball assignment (top and marking side view) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
**Figure 3.** LED1202QTR pin assignment (top and marking side view). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
**Figure 4.** LED1202 headroom voltage vs. I LED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

**Figure 5.** Analog dimming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
**Figure 6.** Digital dimming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
**Figure 7.** Analog+digital dimming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
**Figure 8.** Phase-shift feature scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
**Figure 9.** SOF position in case of SHFT=1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
**Figure 10.** I²C timing reference. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
**Figure 11.** Data validity on the I²C Bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
**Figure 12.** Start and stop condition on the I²C Bus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
**Figure 13.** Bit transfer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
**Figure 14.** Acknowledge on the I²C bus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
**Figure 15.** Interface protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
**Figure 16.** Writing to a single register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
**Figure 17.** Writing to multiple registers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
**Figure 18.** Reading from a single register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
**Figure 19.** Reading from multiple registers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
**Figure 20.** LED driver schematic diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
**Figure 21.** Multiple device connection concept . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
**Figure 22.** Command sequence example for star common clock domain configuration . . . . . . . . . . . . . . . . . . . . . . . . . 23
**Figure 23.** Concept of daisy chain common clock domain configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
**Figure 24.** Command sequence example for daisy chain common clock domain configuration . . . . . . . . . . . . . . . . . . . . 25
**Figure 25.** WLCSP20 (1.71 x 2.16 x 0.5 mm) package outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
**Figure 26.** WLCSP20 (1.71 x 2.16 x 0.5 mm) recommended footprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
**Figure 27.** QFN20 3x3 (3 x 3 x 0.6 mm 20 L with 0.5 mm pitch) package outline. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
**Figure 28.** QFN20 3x3 (3 x 3 x 0.6 mm 20 L with 0.5 mm pitch) recommended footprint . . . . . . . . . . . . . . . . . . . . . . . . 46


**DS12875** - **Rev 2** **page 53/54**


**LED1202**


**IMPORTANT NOTICE – PLEASE READ CAREFULLY**


STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST
products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST
products are sold pursuant to ST’s terms and conditions of sale in place at the time of order acknowledgement.


Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of
Purchasers’ products.


No license, express or implied, to any intellectual property right is granted by ST herein.


Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.


ST and the ST logo are trademarks of ST. All other product or service names are the property of their respective owners.


Information in this document supersedes and replaces information previously supplied in any prior versions of this document.


© 2019 STMicroelectronics – All rights reserved


**DS12875** - **Rev 2** **page 54/54**


