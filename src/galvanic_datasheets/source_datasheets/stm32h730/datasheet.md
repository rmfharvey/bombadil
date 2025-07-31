## **STM32H730AB STM32H730IB ** **STM32H730VB STM32H730ZB**
##### Arm [®] Cortex [®] -M7 32b 550 MHz MCU, 128 KB flash, 564 KB RAM, Ethernet, USB, 3xFDCAN, Graphics, 2x 16-bit ADCs, crypto/hash

**Datasheet**                                      - **production data**
###### **Features**


**Includes ST state-of-the-art patented**
**technology**

**Core**

- 32-bit Arm [®] Cortex [®] -M7 CPU with DP-FPU, L1
cache: 32-Kbyte data cache and 32-Kbyte
instruction cache allowing 0-wait state
execution from embedded flash memory and
external memories, frequency up to 550 MHz,
MPU, 2778 CoreMark, and DSP instructions

**Memories**

- 128 Kbytes of embedded flash memory with
ECC

- SRAM: total 564 Kbytes all with ECC, including
128 Kbytes of data TCM RAM for critical realtime data + 432 Kbytes of system RAM (up to
256 Kbytes can remap on instruction TCM
RAM for critical real-time instructions) +
4 Kbytes of backup SRAM (available in the
lowest-power modes)

- Flexible external memory controller with up to
24-bit data bus: SRAM, PSRAM,
SDRAM/LPSDR SDRAM, NOR/NAND
memories

- 2 x Octo-SPI interface with XiP and on-the-fly
decryption support

- 2 x SD/SDIO/MMC interface

- Bootloader with security services support (SFI
and SB-SFU)

**Graphics**

- Chrom-ART Accelerator graphical hardware
accelerator enabling enhanced graphical user
interface to reduce CPU load

- LCD-TFT controller supporting up to XGA
resolution

|Col1|FBGA|
|---|---|
|||

|Col1|FBGA|
|---|---|
|||


**Clock, reset, and supply management**

- 1.62 V to 3.6 V application supply and I/O

- POR, PDR, PVD, and BOR

- Dedicated USB power

- Embedded DC-DC and LDO regulator

- Internal oscillators: 64 MHz HSI, 48 MHz
HSI48, 4 MHz CSI, 32 kHz LSI

- External oscillators: 4-50 MHz HSE,
32.768 kHz LSE

**Low power**

- Sleep, Stop, and Standby modes

- V BAT supply for RTC, 32×32-bit backup
registers

**Analog**

- 2×16-bit ADC, up to 3.6 MSPS in 16-bit: up to
22 channels and 7.2 MSPS in double
interleaved mode

- 1 x 12-bit ADC, up to 5 MSPS in 12-bit, up to 12
channels

- 2 x comparators

- 2 x operational amplifier GBW = 8 MHz




Ma y 2025 DS13315 Rev 5 1/270

*[www.st.com](http://www.st.com)*

- 2× 12-bit D/A converters

**Digital filters for sigma delta modulator**
**(DFSDM)**

- 8 channels/4 filters

**4 DMA controllers to offload the CPU**

- 1 × MDMA with linked list support

- 2 × dual-port DMAs with FIFO

- 1 × basic DMA with request router capabilities

**24 timers**

- Seventeen 16-bit (including 5 x low power
16-bit timer available in stop mode) and four
32-bit timers, each with up to 4 IC/OC/PWM or
pulse counter and quadrature (incremental)
encoder input

- 2x watchdogs, 1x SysTick timer

**Debug mode**

- SWD and JTAG interfaces

- 2-Kbyte embedded trace buffer

**Up to 128 I/O ports with interrupt**
**capability**

**Up to 35 communication interfaces**

- Up to 5 × I2C Fm+ interfaces
(SMBus/PMBus™)

- Up to 6 USART/UART/LPUART (SPI, ISO7816
interface, LIN, IrDA, modem)

- Up to 6 SPIs (+ up to 5 with USART + 2 with
OCTOSPI), 4 with muxed duplex I2S for audio
class accuracy via internal audio PLL or
external clock and up to 5 x SPI (from 5 x
USART when configured in synchronous
mode)

- 2x SAI (serial audio interface)

- 1× FD/TTCAN and 2x FDCANs

- 8- to 14-bit camera interface

- 16-bit parallel slave synchronous interface

- SPDIF-IN interface

- HDMI-CEC

- Ethernet MAC interface with DMA controller


**STM32H730xB**

- USB 2.0 high-speed/full-speed
device/host/OTG controller with dedicated

DMA, on-chip FS PHY and ULPI for external
HS PHY

- SWPMI single-wire protocol master I/F

- MDIO slave interface

**Mathematical acceleration**

- CORDIC for trigonometric functions
acceleration

- FMAC: Filter mathematical accelerator

**Digital temperature sensor**

**Cryptographic/HASH acceleration**

- AES 128, 192, 256, TDES, HASH (MD5, SHA1, SHA-2), HMAC

- 2x OTFDEC AES-128 in CTR mode for OctoSPI memory encryption/decryption

**True random number generator**

**CRC calculation unit**

**RTC with subsecond accuracy and**
**hardware calendar**

**ROP, PC-ROP, tamper detection, secure**
**firmware upgrade support**

**96-bit unique ID**

**All packages are ECOPACK2 compliant**


2/270 DS13315 Rev 5

**STM32H730xB** **Contents**
### **Contents**

**1** **Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14**

**2** **Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15**

**3** **Functional overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22**

3.1 Arm [®] Cortex [®] -M7 with FPU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

3.2 Memory protection unit (MPU) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

3.3 Memories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

3.3.1 Embedded flash memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

3.3.2 Embedded SRAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

Error code correction (ECC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .24

3.4 Secure access mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

3.5 Boot modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

3.6 CORDIC coprocessor (CORDIC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

CORDIC features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .25

3.7 Filter mathematical accelerator (FMAC) . . . . . . . . . . . . . . . . . . . . . . . . . . 25

FMAC features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26

3.8 Power supply management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

3.8.1 Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

3.8.2 Power supply supervisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

3.8.3 Voltage regulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

3.9 Low-power strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

3.10 Reset and clock controller (RCC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

3.10.1 Clock management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

3.10.2 System reset sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

3.11 General-purpose input/outputs (GPIOs) . . . . . . . . . . . . . . . . . . . . . . . . . . 30

3.12 Bus-interconnect matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

3.13 DMA controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3.14 Chrom-ART Accelerator (DMA2D) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3.15 Nested vectored interrupt controller (NVIC) . . . . . . . . . . . . . . . . . . . . . . . 33

3.16 Extended interrupt and event controller (EXTI) . . . . . . . . . . . . . . . . . . . . 33

3.17 Cyclic redundancy check calculation unit (CRC) . . . . . . . . . . . . . . . . . . . 33

3.18 Flexible memory controller (FMC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

DS13315 Rev 5 3/270


8

**Contents** **STM32H730xB**

3.19 Octo-SPI memory interface (OCTOSPI) . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.20 Analog-to-digital converters (ADCs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

3.21 Temperature sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

3.22 Digital temperature sensor (DTS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

3.23 V BAT operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

3.24 Digital-to-analog converters (DAC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

3.25 Ultra-low-power comparators (COMP) . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

3.26 Operational amplifiers (OPAMP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

3.27 Digital filter for sigma-delta modulators (DFSDM) . . . . . . . . . . . . . . . . . . 38

3.28 Digital camera interface (DCMI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3.29 PSSI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3.30 LCD-TFT controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3.31 True random number generator (RNG) . . . . . . . . . . . . . . . . . . . . . . . . . . 41

3.32 Cryptographic acceleration (CRYP and HASH) . . . . . . . . . . . . . . . . . . . . 41

3.33 On-the-fly decryption engine (OTFDEC) . . . . . . . . . . . . . . . . . . . . . . . . . 41

3.34 Timers and watchdogs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

3.34.1 Advanced-control timers (TIM1, TIM8) . . . . . . . . . . . . . . . . . . . . . . . . . 45

3.34.2 General-purpose timers (TIMx) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3.34.3 Basic timers TIM6 and TIM7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.34.4 Low-power timers (LPTIM1, LPTIM2, LPTIM3, LPTIM4, LPTIM5) . . . . 46

3.34.5 Independent watchdog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.34.6 Window watchdog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.34.7 SysTick timer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3.35 Real-time clock (RTC), backup SRAM and backup registers . . . . . . . . . . 47

3.36 Inter-integrated circuit interface (I [2] C) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

3.37 Universal synchronous/asynchronous receiver transmitter (USART) . . . 48

3.38 Low-power universal asynchronous receiver transmitter (LPUART) . . . . 49

3.39 Serial peripheral interface (SPI)/inter- integrated sound interfaces (I2S) . 50

3.40 Serial audio interfaces (SAI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

3.41 SPDIFRX Receiver Interface (SPDIFRX) . . . . . . . . . . . . . . . . . . . . . . . . . 51

3.42 Single wire protocol master interface (SWPMI) . . . . . . . . . . . . . . . . . . . . 51

3.43 Management data input/output (MDIO) slaves . . . . . . . . . . . . . . . . . . . . . 52

3.44 SD/SDIO/MMC card host interfaces (SDMMC) . . . . . . . . . . . . . . . . . . . . 52

3.45 Controller area network (FDCAN1, FDCAN2, FDCAN3) . . . . . . . . . . . . . 52

4/270 DS13315 Rev 5

**STM32H730xB** **Contents**

3.46 Universal serial bus on-the-go high-speed (OTG_HS) . . . . . . . . . . . . . . . 53

3.47 Ethernet MAC interface with dedicated DMA controller (ETH) . . . . . . . . . 53

3.48 High-definition multimedia interface (HDMI)

            - consumer electronics control (CEC) . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

3.49 Debug infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

**4** **Memory mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55**

**5** **Pinouts, pin descriptions and alternate functions . . . . . . . . . . . . . . . . 56**

**6** **Electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102**

6.1 Parameter conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.1.1 Minimum and maximum values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.1.2 Typical values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.1.3 Typical curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.1.4 Loading capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.1.5 Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.1.6 Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

6.1.7 Current consumption measurement . . . . . . . . . . . . . . . . . . . . . . . . . . 104

6.2 Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

6.3 Operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

6.3.1 General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

6.3.2 VCAP external capacitor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

6.3.3 SMPS step-down converter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

6.3.4 Operating conditions at power-up / power-down . . . . . . . . . . . . . . . . . 113

6.3.5 Embedded reset and power control block characteristics . . . . . . . . . . 114

6.3.6 Embedded reference voltage characteristics . . . . . . . . . . . . . . . . . . . . 115

6.3.7 Embedded USB regulator characteristics . . . . . . . . . . . . . . . . . . . . . . 116

6.3.8 Supply current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116

Typical and maximum current consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . .117

Typical SMPS efficiency versus load current and temperature . . . . . . . . . . . . .124

I/O system current consumption. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .126

On-chip peripheral current consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .127

6.3.9 Wake-up time from low-power modes . . . . . . . . . . . . . . . . . . . . . . . . . 134

6.3.10 External clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 135

High-speed external user clock generated from an external source . . . . . . . . .135

Low-speed external user clock generated from an external source . . . . . . . . . .136

High-speed external clock generated from a crystal/ceramic resonator. . . . . . .137

DS13315 Rev 5 5/270


8

**Contents** **STM32H730xB**

Low-speed external clock generated from a crystal/ceramic resonator . . . . . . .138

6.3.11 Internal clock source characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 139

48 MHz high-speed internal RC oscillator (HSI48). . . . . . . . . . . . . . . . . . . . . . .139

64 MHz high-speed internal RC oscillator (HSI). . . . . . . . . . . . . . . . . . . . . . . . .140

4 MHz low-power internal RC oscillator (CSI) . . . . . . . . . . . . . . . . . . . . . . . . . .141

Low-speed internal (LSI) RC oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .141

6.3.12 PLL characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142

6.3.13 Memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

Flash memory. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .146

6.3.14 EMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

Functional EMS (electromagnetic susceptibility) . . . . . . . . . . . . . . . . . . . . . . . .147

Designing hardened software to avoid noise problems . . . . . . . . . . . . . . . . . . .147

Electromagnetic Interference (EMI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .148

6.3.15 Absolute maximum ratings (electrical sensitivity) . . . . . . . . . . . . . . . . 149

Electrostatic discharge (ESD). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .149

Static latchup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .149

6.3.16 I/O current injection characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

Functional susceptibility to I/O current injection . . . . . . . . . . . . . . . . . . . . . . . . .150

6.3.17 I/O port characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

General input/output characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .150

Output driving current . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .152

Output voltage levels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .153

Output buffer timing characteristics (HSLV option disabled) . . . . . . . . . . . . . . .155

Output buffer timing characteristics (HSLV option enabled). . . . . . . . . . . . . . . .157

Analog switch between ports Pxy_C and Pxy . . . . . . . . . . . . . . . . . . . . . . . . . .158

6.3.18 NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

6.3.19 FMC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

Asynchronous waveforms and timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .159

Synchronous waveforms and timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .167

NAND controller waveforms and timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .176

SDRAM waveforms and timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .178

6.3.20 Octo-SPI interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181

6.3.21 Delay block (DLYB) characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . 186

6.3.22 16-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186

General PCB design guidelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .194

6.3.23 12-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195

6.3.24 DAC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201

6.3.25 Voltage reference buffer characteristics . . . . . . . . . . . . . . . . . . . . . . . 205

6.3.26 Analog temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . 206

6.3.27 Digital temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . 207

6/270 DS13315 Rev 5

**STM32H730xB** **Contents**

6.3.28 Temperature and V BAT monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207

6.3.29 Voltage booster for analog switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208

6.3.30 Comparator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208

6.3.31 Operational amplifier characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . 209

6.3.32 Digital filter for Sigma-Delta Modulators (DFSDM) characteristics . . . 212

6.3.33 Camera interface (DCMI) timing specifications . . . . . . . . . . . . . . . . . . 214

6.3.34 Parallel synchronous slave interface (PSSI) characteristics . . . . . . . . 215

6.3.35 LCD-TFT controller (LTDC) characteristics . . . . . . . . . . . . . . . . . . . . . 216

6.3.36 Timer characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

6.3.37 Low-power timer characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

6.3.38 Communication interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219

I2C interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .219

USART interface characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .220

SPI interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .222

I2S Interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .225

SAI characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .227

MDIO characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .229

SD/SDIO MMC card host interface (SDMMC) characteristics . . . . . . . . . . . . . .230

USB OTG_FS characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .232

USB OTG_HS characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .233

Ethernet interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .234

JTAG/SWD interface characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .236

**7** **Package information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239**

7.1 Device marking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239

7.2 LQFP100 package information (1L) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240

Notes: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .242

7.3 TFBGA100 package information (A08Q) . . . . . . . . . . . . . . . . . . . . . . . . 243

Notes: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .244

7.4 LQFP144 package information (1A) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246

Notes: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .248

7.5 UFBGA144 package information (A0AS) . . . . . . . . . . . . . . . . . . . . . . . . 250

7.6 UFBGA169 package information (A0YV) . . . . . . . . . . . . . . . . . . . . . . . . 252

7.7 LQFP176 package information (1T) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255

Notes: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .257

7.8 UFBGA(176+25) package information (A0E7) . . . . . . . . . . . . . . . . . . . . 259

7.9 Thermal characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

7.9.1 Reference documents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262

DS13315 Rev 5 7/270


8

**Contents** **STM32H730xB**

**8** **Ordering information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263**

**9** **Important security notice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264**

**10** **Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265**

8/270 DS13315 Rev 5

**STM32H730xB** **List of tables**
### **List of tables**

Table 1. STM32H730xB features and peripheral counts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Table 2. System versus domain low-power mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
Table 3. DFSDM implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Table 4. Timer feature comparison. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
Table 5. USART features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
Table 6. Legend/abbreviations used in the pinout table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
Table 7. STM32H730xB pin and ball descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Table 8. STM32H730xB pin alternate functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
Table 9. Voltage characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Table 10. Current characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105

Table 11. Thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
Table 12. General operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Table 13. Supply voltage and maximum temperature configuration. . . . . . . . . . . . . . . . . . . . . . . . . 108
Table 14. VCAP operating conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Table 15. Characteristics of SMPS step-down converter external components. . . . . . . . . . . . . . . . 110
Table 16. SMPS step-down converter characteristics for external usage . . . . . . . . . . . . . . . . . . . . 110
Table 17. Inrush current and inrush electric charge characteristics for LDO and SMPS . . . . . . . . . 111
Table 18. Operating conditions at power-up/power-down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Table 19. Reset and power control block characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
Table 20. Embedded reference voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
Table 21. Internal reference voltage calibration values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
Table 22. USB regulator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
Table 23. Typical and maximum current consumption in Run mode,
code with data processing running from ITCM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
Table 24. Typical and maximum current consumption in Run mode, code with data processing
running from flash memory, cache ON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
Table 25. Typical and maximum current consumption in Run mode,
code with data processing running from flash memory, cache OFF . . . . . . . . . . . . . . . . 120
Table 26. Typical consumption in Run mode and corresponding performance
versus code position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Table 27. Typical current consumption in Autonomous mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Table 28. Typical and maximum current consumption in Sleep mode . . . . . . . . . . . . . . . . . . . . . . . 121
Table 29. Typical and maximum current consumption in System Stop mode . . . . . . . . . . . . . . . . . 122
Table 30. Typical and maximum current consumption in Standby mode . . . . . . . . . . . . . . . . . . . . . 123
Table 31. Typical and maximum current consumption in VBAT mode . . . . . . . . . . . . . . . . . . . . . . . 123
Table 32. Peripheral current consumption in Run mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Table 33. Low-power mode wakeup timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
Table 34. High-speed external user clock characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
Table 35. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
Table 36. 4-50 MHz HSE oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137

Table 37. Low-speed external user clock characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
Table 38. HSI48 oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

Table 39. HSI oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

Table 40. CSI oscillator characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141

Table 41. LSI oscillator characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
Table 42. PLL1 characteristics (wide VCO frequency range). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
Table 43. PLL1 characteristics (medium VCO frequency range) . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
Table 44. PLL2 and PLL3 characteristics (wide VCO frequency range) . . . . . . . . . . . . . . . . . . . . . 144

DS13315 Rev 5 9/270


11

**List of tables** **STM32H730xB**

Table 45. PLL2 and PLL3 characteristics (medium VCO frequency range) . . . . . . . . . . . . . . . . . . . 145
Table 46. Flash memory characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
Table 47. Flash memory programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
Table 48. Flash memory endurance and data retention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
Table 49. EMS characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

Table 50. EMI characteristics for fHSE = 8 MHz and fCPU = 550 MHz . . . . . . . . . . . . . . . . . . . . . 148
Table 51. ESD absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Table 52. Electrical sensitivities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Table 53. I/O current injection susceptibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
Table 54. I/O static characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
Table 55. Output voltage characteristics for all I/Os except PC13, PC14 and PC15 . . . . . . . . . . . . 153
Table 56. Output voltage characteristics for PC13, PC14 and PC15 . . . . . . . . . . . . . . . . . . . . . . . . 154
Table 57. Output timing characteristics (HSLV OFF) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
Table 58. Output timing characteristics (HSLV ON) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
Table 59. Pxy_C and Pxy analog switch characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
Table 60. NRST pin characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
Table 61. Asynchronous non-multiplexed SRAM/PSRAM/NOR read timings . . . . . . . . . . . . . . . . . 160
Table 62. Asynchronous non-multiplexed SRAM/PSRAM/NOR read-NWAIT timings . . . . . . . . . . . 160
Table 63. Asynchronous non-multiplexed SRAM/PSRAM/NOR write timings . . . . . . . . . . . . . . . . . 162
Table 64. Asynchronous non-multiplexed SRAM/PSRAM/NOR write-NWAIT timings. . . . . . . . . . . 162
Table 65. Asynchronous multiplexed PSRAM/NOR read timings. . . . . . . . . . . . . . . . . . . . . . . . . . . 164
Table 66. Asynchronous multiplexed PSRAM/NOR read-NWAIT timings . . . . . . . . . . . . . . . . . . . . 164
Table 67. Asynchronous multiplexed PSRAM/NOR write timings . . . . . . . . . . . . . . . . . . . . . . . . . . 166
Table 68. Asynchronous multiplexed PSRAM/NOR write-NWAIT timings . . . . . . . . . . . . . . . . . . . . 166
Table 69. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 168
Table 70. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
Table 71. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
Table 72. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
Table 73. Switching characteristics for NAND flash read cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
Table 74. Switching characteristics for NAND flash write cycles . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
Table 75. SDRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Table 76. LPSDR SDRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Table 77. SDRAM Write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
Table 78. LPSDR SDRAM Write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
Table 79. OCTOSPI characteristics in SDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
Table 80. OCTOSPI characteristics in DTR mode (no DQS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
Table 81. OCTOSPI characteristics in DTR mode (with DQS)/Octal and Hyperbus . . . . . . . . . . . . 184
Table 82. Delay Block characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
Table 83. 16-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
Table 84. Minimum sampling time vs RAIN (16-bit ADC). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Table 85. 16-bit ADC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
Table 86. 12-bit ADC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
Table 87. Minimum sampling time vs RAIN (12-bit ADC). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
Table 88. 12-bit ADC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200
Table 89. DAC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Table 90. DAC accuracy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203
Table 91. VREFBUF characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205

Table 92. Temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
Table 93. Temperature sensor calibration values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
Table 94. Digital temperature sensor characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Table 95. V BAT monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Table 96. V BAT charging characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207

10/270 DS13315 Rev 5

**STM32H730xB** **List of tables**

Table 97. Temperature monitoring characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
Table 98. Voltage booster for analog switch characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
Table 99. COMP characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208

Table 100. Operational amplifier characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
Table 101. DFSDM measured timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
Table 102. DCMI characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214

Table 103. PSSI transmit characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215

Table 104. PSSI receive characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215

Table 105. LTDC characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

Table 106. TIMx characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

Table 107. LPTIMx characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
Table 108. Minimum i2c_ker_ck frequency in all I2C modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
Table 109. I2C analog filter characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
Table 110. USART (SPI mode) characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
Table 111. SPI characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
Table 112. I [2] S dynamic characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
Table 113. SAI characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
Table 114. MDIO slave timing parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
Table 115. Dynamics characteristics: SD / MMC characteristics, VDD = 2.7 to 3.6 V . . . . . . . . . . . . 230
Table 116. Dynamics characteristics: eMMC characteristics VDD = 1.71V to 1.9V. . . . . . . . . . . . . . 231
Table 117. USB OTG_FS electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
Table 118. Dynamics characteristics: USB ULPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
Table 119. Dynamics characteristics: Ethernet MAC signals for SMI . . . . . . . . . . . . . . . . . . . . . . . . 234
Table 120. Dynamics characteristics: Ethernet MAC signals for RMII . . . . . . . . . . . . . . . . . . . . . . . . 235
Table 121. Dynamics characteristics: Ethernet MAC signals for MII . . . . . . . . . . . . . . . . . . . . . . . . . 236
Table 122. Dynamics JTAG characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
Table 123. Dynamics SWD characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
Table 124. LQFP100 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241

Table 125. TFBGA100 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
Table 126. TFBGA100 - Example of PCB design rules (0.8 mm pitch BGA) . . . . . . . . . . . . . . . . . . . 245
Table 127. LQFP144 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
Table 128. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array
package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
Table 129. UFBGA144 recommended PCB design rules (0.50 mm pitch BGA) . . . . . . . . . . . . . . . . 251
Table 130. UFBGA169 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
Table 131. UFBGA169 - Example of PCB design rules (0.5 mm pitch BGA). . . . . . . . . . . . . . . . . . . 254
Table 132. LQFP176 - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
Table 133. UFBGA(176+25) - Mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
Table 134. UFBGA(176+25) - Example of PCB design rules (0.65 mm pitch BGA) . . . . . . . . . . . . . 260
Table 135. Thermal characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

Table 136. Document revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265

DS13315 Rev 5 11/270


11

**List of figures** **STM32H730xB**
### **List of figures**

Figure 1. STM32H730xB block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Figure 2. Power-up/power-down sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
Figure 3. STM32H730xB bus matrix  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
Figure 4. TFBGA100 ballout (without SMPS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
Figure 5. LQFP100 pinout (without SMPS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
Figure 6. UFBGA144 ballout (without SMPS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
Figure 7. LQFP144 pinout (without SMPS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
Figure 8. LQFP176 pinout (with SMPS). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
Figure 9. UFBGA169 ballout (with SMPS). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Figure 10. UFBGA176+25 ballout (with SMPS). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Figure 11. Pin loading conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Figure 12. Pin input voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Figure 13. Power supply scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
Figure 14. Current consumption measurement scheme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Figure 15. External capacitor C EXT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Figure 16. External components for SMPS step-down converter . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Figure 17. Typical SMPS efficiency (%) vs load current (A) in Run mode at TJ = 30 °C. . . . . . . . . . 124
Figure 18. Typical SMPS efficiency (%) vs load current (A) in Run mode at TJ = TJmax . . . . . . . . . 124
Figure 19. Typical SMPS efficiency (%) vs load current (A) in Stop and
DStop modes at TJ = 30 °C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Figure 20. Typical SMPS efficiency (%) vs load current (A) in low-power mode at TJ = TJmax . . . 125
Figure 21. High-speed external clock source AC timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
Figure 22. Low-speed external clock source AC timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
Figure 23. Typical application with an 8 MHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
Figure 24. Typical application with a 32.768 kHz crystal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
Figure 25. VIL/VIH for all I/Os except BOOT0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
Figure 26. Recommended NRST pin protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
Figure 27. Asynchronous non-multiplexed SRAM/PSRAM/NOR read waveforms . . . . . . . . . . . . . . 161
Figure 28. Asynchronous non-multiplexed SRAM/PSRAM/NOR write waveforms . . . . . . . . . . . . . . 163
Figure 29. Asynchronous multiplexed PSRAM/NOR read waveforms. . . . . . . . . . . . . . . . . . . . . . . . 165
Figure 30. Asynchronous multiplexed PSRAM/NOR write waveforms . . . . . . . . . . . . . . . . . . . . . . . 167
Figure 31. Synchronous non-multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . 169
Figure 32. Synchronous non-multiplexed PSRAM write timings . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
Figure 33. Synchronous multiplexed NOR/PSRAM read timings . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
Figure 34. Synchronous multiplexed PSRAM write timings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
Figure 35. NAND controller waveforms for read access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
Figure 36. NAND controller waveforms for write access . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
Figure 37. SDRAM read access waveforms (CL = 1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Figure 38. SDRAM write access waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
Figure 39. OCTOSPI SDR read/write timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
Figure 40. OCTOSPI DTR mode timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
Figure 41. OCTOSPI Hyperbus clock timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
Figure 42. OCTOSPI Hyperbus read timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
Figure 43. OCTOSPI Hyperbus write timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
Figure 44. ADC accuracy characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193
Figure 45. Typical connection diagram when using the ADC with FT/TT pins
featuring analog switch function193
Figure 46. Power supply and reference decoupling (V REF+ not connected to V DDA ). . . . . . . . . . . . . 194

12/270 DS13315 Rev 5

**STM32H730xB** **List of figures**

Figure 47. Power supply and reference decoupling (V REF+ connected to V DDA ). . . . . . . . . . . . . . . . 194
Figure 48. 12-bit buffered /non-buffered DAC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
Figure 49. Channel transceiver timing diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Figure 50. DCMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
Figure 51. LCD-TFT horizontal timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
Figure 52. LCD-TFT vertical timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
Figure 53. USART timing diagram in SPI master mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
Figure 54. USART timing diagram in SPI slave mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
Figure 55. SPI timing diagram - slave mode and CPHA = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
Figure 56. SPI timing diagram - slave mode and CPHA = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
Figure 57. SPI timing diagram - master mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
Figure 58. I [2] S slave timing diagram (Philips protocol) [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
Figure 59. I [2] S master timing diagram (Philips protocol) [(1)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
Figure 60. SAI master timing waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
Figure 61. SAI slave timing waveforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
Figure 62. MDIO slave timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
Figure 63. SD high-speed mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
Figure 64. SD default mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
Figure 65. SDMMC DDR mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
Figure 66. ULPI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
Figure 67. Ethernet SMI timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
Figure 68. Ethernet RMII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
Figure 69. Ethernet MII timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
Figure 70. JTAG timing diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
Figure 71. SWD timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
Figure 72. LQFP100 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
Figure 73. LQFP100 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
Figure 74. TFBGA100 - Outline [(13)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
Figure 75. TFBGA100 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
Figure 76. LQFP144 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
Figure 77. LQFP144 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
Figure 78. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array
package outline. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
Figure 79. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array
package recommended footprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
Figure 80. UFBGA169 - Outline. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
Figure 81. UFBGA169 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
Figure 82. LQFP176 - Outline [(15)] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
Figure 83. LQFP176 - Footprint example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
Figure 84. UFBGA(176+25) - Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
Figure 85. UFBGA(176+25) - Footprint example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

DS13315 Rev 5 13/270


13

**Introduction** **STM32H730xB**
#### **1 Introduction **

This document provides information on STM32H730xB microcontrollers, such as
description, functional overview, pin assignment and definition, packaging, and ordering
information.

This document should be read in conjunction with the STM32H730xB reference manual
(RM0468), available from the STMicroelectronics website *www.st.com* .

For information on the device errata with respect to the datasheet and reference manual,
refer to the STM32H730 errata sheet (ES0491) available on the STMicroelectronics website
*www.st.com* .

For information on the Arm [®(a)] Cortex [®] -M7 core, refer to the Cortex [®] -M7 Technical
Reference Manual, available from the http://www.arm.com website.

a. Arm is a registered trademark of Arm Limited (or its subsidiaries) in the US and/or elsewhere.

14/270 DS13315 Rev 5

**STM32H730xB** **Description**
#### **2 Description**

STM32H730xB devices are based on the high-performance Arm [®] Cortex [®] -M7 32-bit RISC
core operating at up to 550 MHz. The Cortex® -M7 core features a floating-point unit (FPU)
which supports Arm [®] double-precision (IEEE 754 compliant) and single-precision dataprocessing instructions and data types. The Cortex -M7 core includes 32 Kbytes of
instruction cache and 32 Kbytes of data cache. STM32H730xB devices support a full set of
DSP instructions and a memory protection unit (MPU) to enhance application security.

STM32H730xB devices incorporate high-speed embedded memories with 128 Kbytes of
flash memory, up to 564 Kbytes of RAM (including 192 Kbytes that can be shared between
ITCM and AXI, plus 64 Kbytes exclusively ITCM, plus 128 Kbytes exclusively AXI,
128 Kbyte DTCM, 48 Kbytes AHB and 4 Kbytes of backup RAM), as well as an extensive
range of enhanced I/Os and peripherals connected to APB buses, AHB buses, 2x32-bit
multi-AHB bus matrix and a multilayer AXI interconnect supporting internal and external
memory access. To improve application robustness, all memories feature error code
correction (one error correction, two error detections).

The devices embed peripherals allowing mathematical/arithmetic function acceleration
(CORDIC coprocessor for trigonometric functions and FMAC unit for filter functions). All the
devices offer three ADCs, two DACs, two operational amplifiers, two ultra-low-power
comparators, a low-power RTC, four general-purpose 32-bit timers, 12 general-purpose 16bit timers including two PWM timers for motor control, five low-power timers, a true random
number generator (RNG), and a cryptographic acceleration cell, and a HASH processor.
The devices support four digital filters for external sigma-delta modulators (DFSDM). They
also feature standard and advanced communication interfaces.

      - Standard peripherals

– Five I [2] Cs

–
Five USARTs, five UARTs, and one LPUART

–
Six SPIs, four I [2] Ss. To achieve audio class accuracy, the I [2] S peripherals can be
clocked by a dedicated internal audio PLL or by an external clock to allow
synchronization (note that the five USARTs also provide SPI slave capability).

– Two SAI serial audio interfaces

–
One SPDIFRX interface with four inputs

–
One SWPMI (Single Wire Protocol Master Interface)

–
Management Data Input/Output (MDIO) slaves

– Two SDMMC interfaces

–
A USB OTG high-speed interface with full-speed capability (with the ULPI)

–
Two FDCANs plus one TT-FDCAN interface

– An Ethernet interface

– Chrom-ART Accelerator

– HDMI-CEC

DS13315 Rev 5 15/270


55

**Description** **STM32H730xB**

      - Advanced peripherals including

–
A flexible memory control (FMC) interface

–
Two Octo-SPI memory interfaces with on-the-fly decryption (OTFDEC)

– A camera interface for CMOS sensors

–
An LCD-TFT display controller

Refer to *Table 1: STM32H730xB features and peripheral counts* for the list of peripherals
available on each part number.

To reduce the power consumption some STM32H730xB devices include an optional stepdown converter that can be used either for internal or external supply, or both.

STM32H730xB devices operate in the –40 to +85 °C ambient temperature range from a
1.62 to 3.6 V power supply. The supply voltage can drop down to 1.62 V by using an
external power supervisor (see *Section 3.8.2: Power supply supervisor)* and connecting the
PDR_ON pin to V SS . Otherwise, the supply voltage must stay above 1.71 V with the
embedded power voltage detector enabled.

Dedicated supply inputs for USB are available to allow a greater power supply choice.

A comprehensive set of power-saving modes allows the design of low-power applications.

STM32H730xB devices are offered in several packages ranging from 100 to 176 pins/balls.
The set of included peripherals changes with the device chosen.

These features make STM32H730xB microcontrollers suitable for a wide range of
applications:

      - Motor drive and application control

      - Medical equipment

      - Industrial applications: PLC, inverters, circuit breakers

      - Printers, and scanners

      - Alarm systems, video intercom, and HVAC

      - Home audio appliances

      - Mobile applications, Internet of Things

      - Wearable devices: smart watches.

*Figure 1* shows the device block diagram.

16/270 DS13315 Rev 5

**STM32H730xB** **Description**

**Fi** **g** **ure 1. STM32H730xB block dia** **g** **ram**








































































DS13315 Rev 5 17/270


55

**Description** **STM32H730xB**

**Table 1. STM32H730xB features and** **p** **eri** **p** **heral counts**










|Peripherals|Col2|no SMPS|Col4|Col5|Col6|SMPS|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||STM32H730VBT6|STM32H730VBH6|STM32H730ZBT6|STM32H730ZBI6|STM32H730ABI6Q|STM32H730IBK6Q|STM32H730IBT6Q|
|Flash memory (Kbytes)||128|||||||
|SRAM (Kbytes)|SRAM mapped onto AXI bus|128|||||||
||SRAM1 (D2 domain)|16|||||||
||SRAM2 (D2 domain)|16|||||||
||SRAM4 (D3 domain)|16|||||||
|RAM shared between ITCM and AXI (Kbytes)||192|||||||
|TCM RAM in Kbytes|ITCM RAM (instruction)|64|||||||
||DTCM RAM (data)|128|||||||
|Backup SRAM (Kbytes)||4|||||||
|FMC|Interface|1|||||||
||NOR flash memory/RAM controller|-|-|yes|yes|yes|yes|yes|
||Multiplexed I/O NOR flash memory|yes|yes|yes|yes|yes|yes|yes|
||16-bit NAND flash memory|yes|yes|yes|yes|yes|yes|yes|
||16-bit SDRAM controller|-|-|yes|yes|yes|yes|yes|
||24-bit SDRAM controller(1)|-|-|-|-|-|yes|-|
|GPIO||80||112|114|121|128|119|
|Octo-SPI interface||1|1|2|2|2|2|2|


18/270 DS13315 Rev 5

**STM32H730xB** **Description**

**Table 1. STM32H730xB features and** **p** **eri** **p** **heral counts** **(** **continued** **)**






|Peripherals|Col2|no SMPS|Col4|Col5|Col6|SMPS|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||STM32H730VBT6|STM32H730VBH6|STM32H730ZBT6|STM32H730ZBI6|STM32H730ABI6Q|STM32H730IBK6Q|STM32H730IBT6Q|
|OTFDEC||yes|||||||
|Cordic||yes|||||||
|FMAC||yes|||||||
|Timers|General purpose 32 bits|4|4|4|4|4|4|4|
||General purpose 16 bits|10|10|10|10|10|10|10|
||Advanced control (PWM)|2|2|2|2|2|2|2|
||Basic|2|2|2|2|2|2|2|
||Low-power|5|5|5|5|5|5|5|
||RTC|1|1|1|1|1|1|1|
||Window watchdog / independent watchdog|2|2|2|2|2|2|2|
|Wakeup pins||4|4|4|4|4|4|4|
|Tamper pins||2|2|2|2|2|2|2|
|Random number generator||yes|||||||
|Cryptographic accelerator||yes|||||||


DS13315 Rev 5 19/270


55

**Description** **STM32H730xB**

**Table 1. STM32H730xB features and** **p** **eri** **p** **heral counts** **(** **continued** **)**








|Peripherals|Col2|no SMPS|Col4|Col5|Col6|SMPS|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||STM32H730VBT6|STM32H730VBH6|STM32H730ZBT6|STM32H730ZBI6|STM32H730ABI6Q|STM32H730IBK6Q|STM32H730IBT6Q|
|Communic ation interfaces|SPI / I2S|5/4|5/4|6/4|6/4|6/4|6/4|6/4|
||I2C|5|5|5|5|5|5|5|
||USART/UART/ LPUART|5/5/1|5/5/1|5/5/1|5/5/1|5/5/1|5/5/1|5/5/1|
||SAI/PDM|2/2(2)|2/2(2)|2/2|2/2|2/2|2/2|2/2|
||SPDIFRX|1|||||||
||HDMI-CEC|1|||||||
||SWPMI|1|||||||
||MDIO|1|||||||
||SDMMC|2|||||||
||FDCAN/TT- FDCAN|2/1|2/1|2/1|2/1|2/1|2/1|2/1|
||USB [OTG_HS(ULPI)/ FS(PHY)]|1 [1/1]|1 [1/1]|1 [1/1]|1 [1/1]|1 [1/1]|1 [1/1]|1 [1/1]|
||Ethernet [MII/RMII]|1 [0/1]|1 [0/1]|1 [0/1]|1 [1/1]|1 [1/1]|1 [0/1]|1 [1/1]|
|Camera interface/PSSI||yes|||||||
|LCD-TFT||yes|||||||
|Chrom-ART Accelerator (DMA2D)||yes|||||||
|16-bit ADCs|Number of ADCs|2|||||||
||Number of Direct channels ADC1/ADC2|0|2/2|0|2/2|2/2|2/2|0|
||Number of Fast channels ADC1/ADC2|3/2|3/2|4/3|4/3|6/5|6/5|4/3|
||Number of Slow channels ADC1/ADC2|11/10|9/8|12/11|12/11|12/11|12/11|12/11|


20/270 DS13315 Rev 5

**STM32H730xB** **Description**

**Table 1. STM32H730xB features and** **p** **eri** **p** **heral counts** **(** **continued** **)**




|Peripherals|Col2|no SMPS|Col4|Col5|Col6|SMPS|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||STM32H730VBT6|STM32H730VBH6|STM32H730ZBT6|STM32H730ZBI6|STM32H730ABI6Q|STM32H730IBK6Q|STM32H730IBT6Q|
|12-bit ADCs|Number of ADCs|1|||||||
||Number of Direct channels|2|2|2|2|2|2|2|
||Number of Fast channels|2|6|6|6|6|6|6|
||Number of Slow channels|0|9|4|9|9|9|4|
|12-bit DAC|Present in IC|yes|||||||
||Number of channels|2|||||||
|Comparators||2|||||||
|Operational amplifiers||2|||||||
|DFSDM||yes|||||||
|Maximum CPU frequency||550 MHz|||||||
|USB separate supply pad||-|yes|yes|yes|yes|yes|yes|
|USB internal regulator||-|-|-|-|yes|yes|yes|
|LDO||yes|||||||
|SMPS step-down converter||no||||yes|||
|Operating voltage||1.71 to 3.6 V|1.62 to 3.6 V||||||
|Operating temperature||-40°C to +85°C|||||||
|Package||LQFP 100|TFBGA 100|LQFP 144|UFBGA 144|UFBGA 169|UFBGA 176+25|LQFP176|


1. The 24-bit SDRAM controller is a 32-bit controller with only a 24-bit data bus and without NBL2-3. It can be used for
graphical purposes to access aligned 32-bit words ignoring upper 8 bits.

2. For limitations on peripheral features depending on packages, check the available pins/balls in *Table 7: STM32H730xB pin*
*and ball descriptions* .

DS13315 Rev 5 21/270


55

**Functional overview** **STM32H730xB**
#### **3 Functional overview**
###### **3.1 Arm [®] Cortex [®] -M7 with FPU**

The Arm [®] Cortex [®] -M7 with double-precision FPU processor is the latest generation of Arm
processors for embedded systems. It was developed to provide a low-cost platform that
meets the needs of MCU implementation, with a reduced pin count and optimized power
consumption, while delivering outstanding computational performance and low interrupt
latency.

The Cortex [®] -M7 processor is a highly efficient high-performance featuring:

      - Six-stage dual-issue pipeline

      - Dynamic branch prediction

      - Harvard architecture with L1 caches (32 Kbytes of I-cache and 32 Kbytes of D-cache)

      - 64-bit AXI interface

      - 64-bit ITCM interface

      - 2x32-bit DTCM interfaces

The following memory interfaces are supported:

      - Separate Instruction and Data buses (Harvard Architecture) to optimize CPU latency

      - Tightly Coupled Memory (TCM) interface designed for fast and deterministic SRAM

accesses

      - AXI Bus interface to optimize Burst transfers

      - Dedicated low-latency AHB-Lite peripheral bus (AHBP) to connect to peripherals.

The processor supports a set of DSP instructions, which allow efficient signal processing
and complex algorithm execution.

It also supports single and double precision FPU (floating-point unit) speeds up software
development by using metalanguage development tools, while avoiding saturation.

*Figure 1* shows the general block diagram of the STM32H730xB family.
###### **3.2 Memory protection unit (MPU)**

The memory protection unit (MPU) manages the CPU access rights and the attributes of the
system resources. It has to be programmed and enabled before use. Its main purposes are
to prevent an untrusted user program to accidentally corrupt data used by the OS and/or by
a privileged task, but also to protect data processes or read-protect memory regions.

The MPU defines access rules for privileged accesses and user program accesses. It
allows defining up to 16 protected regions that can in turn be divided into up to eight
independent subregions, where region address, size, and attributes can be configured. The
protection area ranges from 32 bytes to 4 Gbytes of addressable memory.
When an unauthorized access is performed, a memory management exception is
generated.

22/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.3 Memories**

**3.3.1** **Embedded flash memory**

The STM32H730xB devices embed 128 Kbytes of flash memory that can be used for
storing programs and data.

The flash memory is organized as 266-bit flash words memory that can be used for storing
both code and data constants. Each word consists of:

      - one flash word (eight words, 32 bytes, or 256 bits)

      - 10 ECC bits (single-error correction and double-error detection).

The flash memory is organized as follows:

**•** One sector of 128 Kbytes of user flash memory (4 K flash memory words)

**•** 128 Kbytes of system flash memory from which the device can boot

      - 2 Kbytes (64 flash words) of user option bytes for user configuration

**3.3.2** **Embedded SRAM**

All devices feature:

      - from 128 to 320 Kbytes of AXI-SRAM mapped onto the AXI bus on D1 domain

      - SRAM1 mapped on D2 domain: 16 Kbytes

      - SRAM2 mapped on D2 domain: 16 Kbytes

      - SRAM4 mapped on D3 domain: 16 Kbytes

      - 4 Kbytes of backup SRAM

The content of this area is protected against possible unwanted write accesses, and
can be retained in Standby or V BAT mode.

      - RAM mapped to TCM interface (ITCM and DTCM):

Both ITCM and DTCM RAMs are zero wait state memories. They can be accessed
either from the CPU or the MDMA (even in Sleep mode) through a specific AHB slave
of the Cortex®-M7CPU(AHBSAHBP):

–
64 to 256 Kbytes of ITCM-RAM (instruction RAM)

This RAM is connected to an ITCM 64-bit interface designed for execution of
critical real-time routines by the CPU.

–
128 Kbytes of DTCM-RAM (2x 64-Kbyte DTCM-RAMs on 2x32-bit DTCM ports)

The DTCM-RAM could be used for critical real-time data, such as interrupt service
routines or stack/heap memory. Both DTCM-RAMs can be used in parallel (for
load/store operations) thanks to the Cortex®-M7 dual issue capability.

The MDMA can be used to load code or data in ITCM or DTCM RAMs. As reflected
above, 192 Kbyte of RAM can be used either for AXI SRAM or ITCM, with a 64Kbyte
granularity.

DS13315 Rev 5 23/270


55

**Functional overview** **STM32H730xB**

**Error code correction (ECC)**

Over the product lifetime, and/or due to external events such as radiations, invalid bits in
memories may occur. They can be detected and corrected by ECC. This is an expected
behavior that has to be managed at final-application software level in order to ensure data
integrity through ECC algorithms implementation.

SRAM data are protected by ECC:

      - 7 ECC bits are added per 32-bit word.

      - 8 ECC bits are added per 64-bit word for AXI-SRAM and ITCM-RAM.

The ECC mechanism is based on the SECDED algorithm. It supports single-error correction
and double-error detection.
###### **3.4 Secure access mode**

In addition to other typical memory protection mechanism (RDP, PCROP), STM32H730xB
devices introduce the Secure access mode, a new enhanced security feature. This mode
allows developing user-defined secure services by ensuring, on the one hand code and
data protection and on the other hand code safe execution.

Two types of secure services are available:

      - STMicroelectronics Root Secure Services:

These services are embedded in System memory. They provide a secure solution for
firmware and third-party modules installation. These services rely on cryptographic
algorithms based on a device unique private key.

      - User-defined secure services:

These services are embedded in user flash memory. Examples of user secure services
are proprietary user firmware update solution, secure flash integrity check or any other
sensitive applications that require a high level of protection.

The secure firmware is embedded in specific user flash memory areas configured
through option bytes.

Secure services are executed just after a reset and preempt all other applications to
guarantee protected and safe execution. Once executed, the corresponding code and data
are no more accessible.

The above secure services is activated for the next reset exits through an option bit.
###### **3.5 Boot modes**

At startup, the boot memory space is selected by the BOOT pin and BOOT_ADDx option
bytes, allowing to program any boot memory address from 0x0000 0000 to 0x3FFF FFFF,
which includes:

      - All flash address space

      - All RAM address space: ITCM, DTCM RAMs and SRAMs

      - The system memory bootloader

The bootloader is located in nonuser system memory. It is used to reprogram the flash
memory through a serial interface (USART, I2C, SPI, FDCAN, USB-DFU). Refer to
application note AN2606 “ *STM32 microcontroller system memory Boot mode”* for details.

24/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.6 CORDIC coprocessor (CORDIC) **

The CORDIC coprocessor provides hardware acceleration of certain mathematical
functions, notably trigonometric, commonly used in motor control, metering, signal
processing and many other applications.

It speeds up the calculation of these functions compared to a software implementation,
allowing a lower operating frequency, or freeing up processor cycles in order to perform
other tasks.

The filter mathematical accelerator unit performs arithmetic operations on vectors. It
comprises a multiplier/accumulator (MAC) unit, together with address generation logic,
which allows it to index vector elements held in local memory.

The unit includes support for circular buffers on input and output, which allows digital filters
to be implemented. Both finite and infinite impulse response filters can be realized.

The unit allows frequent or lengthy filtering operations to be offloaded from the CPU, freeing
up the processor for other tasks. In many cases it can accelerate such calculations
compared to a software implementation, resulting in a speed-up of time critical tasks.

**CORDIC features**

      - 24-bit CORDIC rotation engine

      - Circular and Hyperbolic modes

      - Rotation and Vectoring modes

      - Functions: Sine, Cosine, Sinh, Cosh, Atan, Atan2, Atanh, Modulus, Square root,
Natural logarithm

      - Programmable precision up to 20-bit

      - Fast convergence: 4 bits per clock cycle

      - Supports 16-bit and 32-bit fixed point input and output formats

      - Low latency AHB slave interface

      - Results can be read as soon as ready without polling or interrupt

      - DMA read and write channels
###### **3.7 Filter mathematical accelerator (FMAC)**

The filter mathematical accelerator unit performs arithmetic operations on vectors. It
comprises a multiplier/accumulator (MAC) unit, together with address generation logic,
which allows it to index vector elements held in local memory.

The unit includes support for circular buffers on input and output, which allows digital filters
to be implemented. Both finite and infinite impulse response filters can be realized.

The unit allows frequent or lengthy filtering operations to be offloaded from the CPU, freeing
up the processor for other tasks. In many cases it can accelerate such calculations
compared to a software implementation, resulting in a speed-up of time critical tasks.

DS13315 Rev 5 25/270


55

**Functional overview** **STM32H730xB**

**FMAC features**

      - 16 x 16-bit multiplier

      - 24+2-bit accumulator with addition and subtraction

      - 16-bit input and output data

      - 256 x 16-bit local memory

      - Up to three areas can be defined in memory for data buffers (two inputs, one output),
defined by programmable base address pointers and associated size registers

      - Input and output sample buffers can be circular

      - Buffer “watermark” feature reduces overhead in interrupt mode

      - Filter functions: FIR, IIR (direct form 1)

      - AHB slave interface

      - DMA read and write data channels
###### **3.8 Power supply management**

**3.8.1** **Power supply scheme**

STM32H730xB power supply voltages are the following:

      - V DD = 1.62 to 3.6 V: external power supply for I/Os, provided externally through V DD
pins.

      - V DDLDO = 1.62 to 3.6 V: supply voltage for the internal regulator supplying V CORE

      - V DDA = 1.62 to 3.6 V: external analog power supplies for ADC, DAC, COMP and
OPAMP.

      - V DD33USB : allows the support of a VDD supply different from 3.3 V while powering the
USB transceiver with 3.3V on V DD33USB .

      - V DD50USB can be supplied through the USB cable to generate the V DD33USB via the
USB internal regulator. This allows support of a V DD supply different to 3.3 V.

The USB regulator can be bypassed to supply directly V DD33USB with
V DD33USB ≈ 3.3 V (see *Section 6: Electrical characteristics* ).

      - V BAT = 1.2 to 3.6 V: power supply for the V SW domain when V DD is not present.

      - V CAP : V CORE supply voltage, which values depend on voltage scaling (1.0 V, 1.1 V,
1.2 V or 1.35 V). They are configured through VOS bits in PWR_D3CR register. The
V CORE domain is split into the following power domains that can be independently
switch off.

– D1 domain containing some peripherals and the Cortex [®] -M7 core

–
D2 domain containing a large part of the peripherals

–
D3 domain containing some peripherals and the system control

      - VDDSMPS= 1.62 V to 3.6 V: SMPS step-down converter power supply VDDSMPS
must be kept at the same voltage level as VDD

      - VLXSMPS = SMPS step-down converter output coupled to an inductor

      - VFBSMPS = VCORE or 1.8 V or 2.5 V external SMPS step-down converter feedback
voltage sense input.

26/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**

During power-up and power-down phases, the following power sequence requirements
must be respected (see *Figure 2* ):

      - When V DD is below V DDmin, other power supplies (V DDA, V DD33USB, V DD50USB ) must
remain below V DD + 300 mV.

      - When V DD is above V DDmin, all power supplies are independent.

During the power-down phase, V DD can temporarily become lower than other supplies only
if the energy provided to the microcontroller remains below 1 mJ. This allows external
decoupling capacitors to be discharged with different time constants during the power-down
transient phase.

**3.8.2** **Power supply supervisor**

The devices have an integrated power-on reset (POR)/ power-down reset (PDR) circuitry
coupled with a brownout reset (BOR) circuitry:

      - Power-on reset (POR)

The POR supervisor monitors V DD power supply and compares it to a fixed threshold.
The devices remain in reset mode when V DD is below this threshold,

      - Power-down reset (PDR)

The PDR supervisor monitors V DD power supply. A reset is generated when V DD drops
below a fixed threshold.

The PDR supervisor can be enabled/disabled through PDR_ON pin.

      - Brownout reset (BOR)

The BOR supervisor monitors V DD power supply. Three BOR thresholds (from 2.1 to
2.7 V) can be configured through option bytes. A reset is generated when V DD drops
below this threshold.

**Fi** **g** **ure 2. Power-u** **p** **/** **p** **ower-down se** **q** **uence**



1. V DDx refers to any power supply among V DDA, V DD33USB, V DD50USB .

DS13315 Rev 5 27/270


55

**Functional overview** **STM32H730xB**

**3.8.3** **Voltage regulator**

The same voltage regulator supplies the three power domains (D1, D2, and D3). D1 and D2
can be independently switched off.

Voltage regulator output can be adjusted according to application needs through six power
supply levels:

      - Run mode (VOS0 to VOS3)

–
Scale 0: boosted performance

–
Scale 1: high performance

–
Scale 2: medium performance and consumption

–
Scale 3: optimized performance and low-power consumption

      - Stop mode (SVOS3 to SVOS5)

–
Scale 3: peripheral with wake-up from Stop mode capabilities (UART, SPI, I2C,
LPTIM) are operational

–
Scale 4 and 5 where the peripheral with wake-up from Stop mode is disabled. The
peripheral functionality is disabled but wake-up from Stop mode is possible
through GPIO or asynchronous interrupt.
###### **3.9 Low-power strategy**

There are several ways to reduce power consumption on STM32H730xB:

      - Decrease the dynamic power consumption by slowing down the system clocks even in
Run mode and by individually clock gating the peripherals that are not used.

      - Save power when the CPU is idle, by selecting among the available low-power modes
according to the user application needs. This allows the best compromise between
short startup time and low power consumption to be achieved, according to the
available wake-up sources.

The devices feature several low-power modes:

      - CSleep (CPU clock stopped)

      - CStop (CPU subsystem clock stopped)

      - DStop (Domain bus matrix clock stopped)

      - Stop (system clock stopped)

      - DStandby (Domain powered down)

      - Standby (system powered down)

CSleep and CStop low-power modes are entered by the MCU when executing the WFI
(Wait for Interrupt) or WFE (Wait for Event) instructions, or when the SLEEPONEXIT bit of
the Cortex [®] -Mx core is set after returning from an interrupt service routine.

A domain can enter low-power mode (DStop or DStandby) when the processor, its
subsystem, and the peripherals allocated in the domain enter low-power mode.

If part of the domain is not in low-power mode, the domain remains in the current mode.

Finally, the system can enter Stop or Standby when all EXTI wake-up sources are cleared
and the power domains are in DStop or DStandby mode.

28/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**

**Table 2. System versus domain low-** **p** **ower mode**

|System power mode|D1 domain power mode|D2 domain power mode|D3 domain power mode|
|---|---|---|---|
|Run|DRun/DStop/DStandby|DRun/DStop/DStandby|DRun|
|Stop|DStop/DStandby|DStop/DStandby|DStop|
|Standby|DStandby|DStandby|DStandby|

###### **3.10 Reset and clock controller (RCC)**

The clock and reset controller is located in D3 domain. The RCC manages the generation of
all the clocks, as well as the clock gating and the control of the system and peripheral
resets. It provides a high flexibility in the choice of clock sources and allows clock ratios to
be applied to improve the power consumption. In addition, on some communication
peripherals that are capable to work with two different clock domains (either a bus interface
clock or a kernel peripheral clock), thus the system frequency can be changed without
modifying the baud rate.

**3.10.1** **Clock management**

The devices embed four internal oscillators, two oscillators with external crystal or
resonator, two internal oscillators with fast startup time and three PLLs.

The RCC receives the following clock source inputs:

      - Internal oscillators:

– 64 MHz HSI clock

– 48 MHz RC oscillator

– 4 MHz CSI clock

– 32 kHz LSI clock

      - External oscillators:

–
HSE clock: 4-50 MHz (generated from an external source) or 4-48 MHz(generated
from a crystal/ceramic resonator)

– LSE clock: 32.768 kHz

The RCC provides three PLLs: one for system clock, two for kernel clocks.

The system starts on the HSI clock. The user application can then select the clock
configuration.

DS13315 Rev 5 29/270


55

**Functional overview** **STM32H730xB**

**3.10.2** **System reset sources**

Power-on reset initializes all registers while system reset reinitializes the system except for
the debug, part of the RCC and power controller status registers, as well as the backup
power domain.

A system reset is generated in the following cases:

      - Power-on reset (pwr_por_rst)

      - Brownout reset

      - Low level on NRST pin (external reset)

      - Window watchdog

      - Independent watchdog

      - Software reset

      - Low-power mode security reset

      - Exit from Standby
###### **3.11 General-purpose input/outputs (GPIOs)**

Each of the GPIO pins can be configured by software as output (push-pull or open-drain,
with or without pull-up or pull-down), as input (floating, with or without pull-up or pull-down)
or as peripheral alternate function. Most of the GPIO pins are shared with digital or analog
alternate functions. All GPIOs are high-current-capable and have speed selection to better
manage internal noise, power consumption and electromagnetic emission.

After reset, all GPIOs (except debug pins) are in Analog mode to reduce power
consumption (refer to GPIOs register reset values in the device reference manual).

The I/O configuration can be locked if needed by following a specific sequence in order to
avoid spurious writing to the I/Os registers.
###### **3.12 Bus-interconnect matrix**

The devices feature an AXI bus matrix, two AHB bus matrices and bus bridges that allow
the interconnection of bus masters with bus slaves (see *Figure 3* ).

30/270 DS13315 Rev 5

**Figure 3. STM32H730xB bus matrix**






|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|CPU Cortex-M7 I$ D$ 32KB 32KB||||ITCM 64 Kbyte|
|||||ITCM 192 Kbyt DTCM|
||||||
|||128 Kbyt|||





|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||
|||||||||OTFDEC2|
||||||||||
||||||||||

|Col1|Col2|Col3|DMA1_PERIPH|Col5|DMA2_PERIPH|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
||||||||||||AHB2 APB1|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||








|Col1|AHB4|
|---|---|
|||
|||





**Functional overview** **STM32H730xB**
###### **3.13 DMA controllers**

The devices feature four DMA instances and a DMA request router to unload CPU activity:

      - A master direct memory access (MDMA)

The MDMA is a high-speed DMA controller, which is in charge of all types of memory
transfers (peripheral to memory, memory to memory, memory to peripheral), without
any CPU action. It features a master AXI interface and a dedicated AHB interface to
access Cortex [®] -M7 TCM memories.

The MDMA is located in D1 domain. It is able to interface with the other DMA

controllers located in D2 domain to extend the standard DMA capabilities, or can
manage peripheral DMA requests directly.

Each of the 16 channels can perform single block transfers, repeated block transfers
and linked list transfers.

      - Two dual-port DMAs (DMA1, DMA2) located in D2 domain, with FIFO and request
router capabilities.

      - One basic DMA (BDMA) located in D3 domain, with request router capabilities.

      - A DMA request multiplexer (DMAMUX)

The DMA request router could be considered as an extension of the DMA controller. It
routes the DMA peripheral requests to the DMA controller itself. This allowing
managing the DMA requests with a high flexibility, maximizing the number of DMA
requests that run concurrently, as well as generating DMA requests from peripheral
output trigger or DMA event.
###### **3.14 Chrom-ART Accelerator (DMA2D)**

The Chrom-ART Accelerator (DMA2D) is a specialized DMA dedicated to image
manipulation. It can perform the following operations:

      - Filling a part or the whole of a destination image with a specific color

      - Copying a part or the whole of a source image into a part or the whole of a destination
image

      - Copying a part or the whole of a source image into a part or the whole of a destination
image with a pixel format conversion

      - Blending a part and/or two complete source images with different pixel format and copy
the result into a part or the whole of a destination image with a different color format.

      - All the classical color coding schemes are supported from 4-bit up to 32-bit per pixel
with indexed or direct color mode, including block based YCbCr to handle JPEG
decoder output.

      - The DMA2D has its own dedicated memories for CLUTs (color look-up tables).

An interrupt can be generated when an operation is complete or at a programmed
watermark.

All the operations are fully automated and are running independently from the CPU or the
DMAs.

32/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.15 Nested vectored interrupt controller (NVIC)**

The devices embed a nested vectored interrupt controller, which is able to manage 16
priority levels, and handle up to 140 maskable interrupt channels plus the 16 interrupt lines
of the Cortex [®] -M7 with FPU core.

      - Closely coupled NVIC gives low-latency interrupt processing

      - Interrupt entry vector table address passed directly to the core

      - Allows early processing of interrupts

      - Processing of late arriving, higher-priority interrupts

      - Support tail chaining

      - Processor context automatically saved on interrupt entry, and restored on interrupt exit
with no instruction overhead

This hardware block provides flexible interrupt management features with minimum interrupt
latency.
###### **3.16 Extended interrupt and event controller (EXTI)**

The EXTI controller performs interrupt and event management. In addition, it can wake up
the processor, power domains and/or D3 domain from Stop mode.

The EXTI handles up to 80 independent event/interrupt lines split as 26 configurable events
and 54 direct events.

Configurable events have dedicated pending flags, active edge selection, and software
trigger capable.

Direct events provide interrupts or events from peripherals having a status flag.
###### **3.17 Cyclic redundancy check calculation unit (CRC) **

The CRC (cyclic redundancy check) calculation unit is used to get a CRC code using a
programmable polynomial.

Among other applications, CRC-based techniques are used to verify data transmission or
storage integrity. In the scope of the EN/IEC 60335-1 standard, they offer a means of
verifying the flash memory integrity. The CRC calculation unit helps compute a signature of
the software during runtime, to be compared with a reference signature generated at linktime and stored at a given memory location.

DS13315 Rev 5 33/270


55

**Functional overview** **STM32H730xB**
###### **3.18 Flexible memory controller (FMC)**

The FMC controller main features are the following:

      - Interface with static-memory mapped devices including:

–
Static random access memory (SRAM)

–
NOR flash memory/OneNAND flash memory

–
PSRAM (four memory banks)

–
NAND flash memory with ECC hardware to check up to 8 Kbytes of data

      - Interface with synchronous DRAM (SDRAM/Mobile LPSDR SDRAM) memories

      - 8-,16-, 24-bit data bus width

      - Independent Chip Select control for each memory bank

      - Independent configuration for each memory bank

      - Write FIFO

      - Read FIFO for SDRAM controller

      - The maximum FMC_CLK/FMC_SDCLK frequency for synchronous accesses is the
FMC kernel clock divided by 2.
###### **3.19 Octo-SPI memory interface (OCTOSPI) **

The OCTOSPI is a specialized communication interface targeting single, dual, quad, or octal
SPI memories. The STM32H730xB embeds two separate Octo-SPI interfaces.

Each OCTOSPI instance supports single/dual/quad/octal SPI formats. multiplexing of
single/dual/quad/octal SPI over the same bus can be achieved using the integrated OctoSPI I/O manager (OCTOSPIM).

The OCTOSPI can operate in any of the three following modes:

      - Indirect mode: all the operations are performed using the OCTOSPI registers

      - Status-polling mode: the external memory status register is periodically read and an
interrupt can be generated in case of flag setting

      - Memory-mapped mode: the external memory is memory mapped and it is seen by the
system as if it was an internal memory supporting both read and write operations.

The OCTOSPI supports two frame formats supported by most external serial memories
such as serial PSRAMs, serial NAND and serial NOR flash memories, Hyper RAMs and
Hyper flash memories.

Multichip package (MCP) combining any of the above mentioned memory types can also be
supported.

      - The classical frame format with the command, address, alternate byte, dummy cycles,
and data phase

      - The HyperBus™ frame format.

34/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.20 Analog-to-digital converters (ADCs)**

STM32H730xB devices embed three analog-to-digital converters, two of 16-bit resolution,
and the third of 12-bit resolution. The 16-bit resolution ADCs can be configured as 16, 14,
12, 10 or 8 bits. The 12-bit resolution ADC can be configured to 12, 10 or 8 bits.

Each ADC shares up to 20 external channels, performing conversions in Single-shot or
Scan mode. In Scan mode, automatic conversion is performed on a selected group of
analog inputs.

Additional logic functions embedded in the ADC interface allow:

      - simultaneous sample and hold

      - Interleaved sample and hold

The ADC can be served by the DMA controller, thus allowing automatic transfer of ADC
converted values to a destination location without any software action.

In addition, an analog watchdog feature can accurately monitor the converted voltage of
one, some, or all selected channels. An interrupt is generated when the converted voltage is
outside the programmed thresholds.

To synchronize A/D conversion and timers, the ADCs can be triggered by any of the TIM1,
TIM2, TIM3, TIM4, TIM6, TIM8, TIM15, TIM23, TIM24, and LPTIM1 timers.
###### **3.21 Temperature sensor**

STM32H730xB devices embed a temperature sensor that generates a voltage (V TS ) that
varies linearly with the temperature. This temperature sensor is internally connected to
ADC3_IN17. The conversion range is between 1.7 V and 3.6 V. It can measure the device

−
junction temperature ranging from 40 to +125°C.

The temperature sensor have a good linearity, but it has to be calibrated to obtain a good
overall accuracy of the temperature measurement. As the temperature sensor offset varies
from chip to chip due to process variation, the uncalibrated internal temperature sensor is
suitable for applications that detect temperature changes only. To improve the accuracy of
the temperature sensor measurement, each device is individually factory-calibrated by ST.
The temperature sensor factory calibration data are stored by ST in the system memory
area, which is accessible in read-only mode.
###### **3.22 Digital temperature sensor (DTS)**

STM32H730xB devices embed a sensor that converts the temperature into a square wave
the frequency of which is proportional to the temperature. The PCLK or the LSE clock can
be used as the reference clock for the measurements. A formula given in the product
reference manual allows calculation of the temperature according to the measured
frequency stored in the DTS_DR register.

DS13315 Rev 5 35/270


55

**Functional overview** **STM32H730xB**
###### **3.23 V BAT operation**

The V BAT power domain contains the RTC, the backup registers, and the backup SRAM.

To optimize battery duration, this power domain is supplied by V DD when available or by the
voltage applied on VBAT pin (when V DD supply is not present). V BAT power is switched
when the PDR detects that V DD dropped below the PDR level.

The voltage on the VBAT pin could be provided by an external battery, a supercapacitor or
directly by V DD, in which case, the V BAT mode is not functional.

V BAT operation is activated when V DD is not present.

The V BAT pin supplies the RTC, the backup registers, and the backup SRAM.

*Note:* *When the microcontroller is supplied from V* *BAT* *, external interrupts and RTC alarm/events*
*do not exit it from V* *BAT* *operation.*

*When PDR_ON pin is connected to V* *SS* *(Internal Reset OFF), the V* *BAT* *functionality is no*
*more available and V* *BAT* *pin should be connected to V* *DD* *.*
###### **3.24 Digital-to-analog converters (DAC)**

The two 12-bit buffered DAC channels can be used to convert two digital signals into two
analog voltage signal outputs.

This dual digital interface supports the following features:

      - two DAC converters: one for each output channel

      - 8-bit or 12-bit monotonic output

      - left or right data alignment in 12-bit mode

      - synchronized update capability

      - noise-wave generation

      - triangular-wave generation

      - dual DAC channel independent or simultaneous conversions

      - DMA capability for each channel including DMA underrun error detection

      - external triggers for conversion

      - input voltage reference V REF+ or internal VREFBUF reference.

The DAC channels are triggered through the timer update outputs that are also connected
to different DMA streams.

36/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.25 Ultra-low-power comparators (COMP)**

STM32H730xB devices embed two rail-to-rail comparators (COMP1 and COMP2). They
feature programmable reference voltage (internal or external), hysteresis, and speed (low
speed for low-power) as well as selectable output polarity.

The reference voltage can be one of the following:

      - An external I/O

      - A DAC output channel

      - An internal reference voltage or submultiple (1/4, 1/2, 3/4).

All comparators can wake up from Stop mode, generate interrupts and breaks for the timers,
and be combined into a window comparator.
###### **3.26 Operational amplifiers (OPAMP) **

STM32H730xB devices embed two rail-to-rail operational amplifiers (OPAMP1 and
OPAMP2) with external or internal follower routing and PGA capability.

The operational amplifier main features are:

      - PGA with a noninverting gain ranging of 2, 4, 8 or 16 or inverting gain ranging of -1, -3,
-7 or -15

      - One positive input connected to DAC

      - Output connected to internal ADC

      - Low input bias current down to 1 nA

      - Low input offset voltage down to 1.5 mV

      - Gain bandwidth up to 7.3 MHz

The devices embed two operational amplifiers (OPAMP1 and OPAMP2) with two inputs and
one output each. These three I/Os can be connected to the external pins, thus enabling any
type of external interconnections. The operational amplifiers can be configured internally as
a follower, as an amplifier with a noninverting gain ranging from 2 to 16 or with inverting gain
ranging from -1 to -15.

DS13315 Rev 5 37/270


55

**Functional overview** **STM32H730xB**
###### **3.27 Digital filter for sigma-delta modulators (DFSDM)**

The devices embed one DFSDM with four digital filters modules and eight external input
serial channels (transceivers) or alternately eight internal parallel inputs support.

The DFSDM peripheral is dedicated to interface the external Σ∆ modulators to
microcontroller and then to perform digital filtering of the received data streams (which
represent analog value on Σ∆ modulators inputs). DFSDM can also interface PDM (Pulse
Density Modulation) microphones and perform PDM to PCM conversion and filtering in
hardware. DFSDM features optional parallel data stream inputs from internal ADC
peripherals or microcontroller memory (through DMA/CPU transfers into DFSDM).

DFSDM transceivers support several serial interface formats (to support various Σ∆
modulators). DFSDM digital filter modules perform digital processing according to userselected filter parameters with up to 24-bit final ADC resolution.

The DFSDM peripheral supports:

      - 8 multiplexed input digital serial channels:

–
configurable SPI interface to connect various SD modulators

–
configurable Manchester coded 1 wire interface support

–
PDM (Pulse Density Modulation) microphone input support

–
maximum input clock frequency up to 20 MHz (10 MHz for Manchester coding)

–
clock output for SD modulators: 0..20 MHz

      - alternative inputs from eight internal digital parallel channels (up to 16-bit input
resolution):

–
internal sources: ADC data or memory data streams (DMA)

      - 4 digital filter modules with adjustable digital signal processing:

– Sinc [x] filter: filter order/type (1..5), oversampling ratio (up to 1..1024)

–
integrator: oversampling ratio (1..256)

      - up to 24-bit output data resolution, signed output data format

      - automatic data offset correction (offset stored in register by user)

      - continuous or single conversion

      - start-of-conversion triggered by:

–
software trigger

– internal timers

– external events

–
start-of-conversion synchronously with first digital filter module (DFSDM0)

      - analog watchdog feature:

–
low value and high value data threshold registers

–
dedicated configurable Sincx digital filter (order = 1..3, oversampling ratio = 1..32)

–
input from final output data or from selected input digital serial channels

–
continuous monitoring independently from standard conversion

      - short circuit detector to detect saturated analog input values (bottom and top range):

–
up to 8-bit counter to detect 1..256 consecutive 0’s or 1’s on serial data stream

–
monitoring continuously each input serial channel

      - break signal generation on analog watchdog event or on short circuit detector event

38/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**

      - extremes detector:

–
storage of minimum and maximum values of final conversion data

–
refreshed by software

      - DMA capability to read the final conversion data

      - interrupts: end of conversion, overrun, analog watchdog, short circuit, input serial
channel clock absence

      - “regular” or “injected” conversions:

–
“regular” conversions can be requested at any time or even in Continuous mode
without having any impact on the timing of “injected” conversions

–
“injected” conversions for precise timing and with high conversion priority

      - Pulse skipper feature to support beamforming applications (delay-line like behavior).

**Table 3. DFSDM im** **p** **lementation**

|DFSDM features|DFSDM1|
|---|---|
|Number of filters|4|
|Number of input transceivers/channels|8|
|Internal ADC parallel input|X|
|Number of external triggers|16|
|Regular channel information in identification register|X|



DS13315 Rev 5 39/270


55

**Functional overview** **STM32H730xB**
###### **3.28 Digital camera interface (DCMI)**

The devices embed a camera interface that can connect with camera modules and CMOS
sensors through an 8-bit to 14-bit parallel interface, to receive video data. The camera
interface can achieve a data transfer rate up to 140 Mbyte/s using an 80 MHz pixel clock. It
features:

      - Programmable polarity for the input pixel clock and synchronization signals

      - Parallel data communication can be 8-, 10-, 12-, or 14-bit

      - Supports 8-bit progressive video monochrome or raw bayer format, YCbCr 4:2:2
progressive video, RGB 565 progressive video or compressed data (like JPEG)

      - Supports Continuous mode or Snapshot (a single frame) mode

      - Capability to automatically crop the image
###### **3.29 PSSI**

The PSSI is a generic synchronous 8-/16-bit parallel data input/output slave interface. It
allows the transmitter to send a data valid signal to indicate when the data is valid, and the
receiver to output a flow control signal to indicate when it is ready to sample the data.

The main PSSI features are:

      - Slave mode operation

      - 8- or 16-bit parallel data input or output

      - 8-word (32-byte) FIFO

      - Data enable (DE) alternate function input and Ready (RDY) alternate function output.

When enabled, these signals can either allow the transmitter to indicate when the data is
valid or the receiver to indicate when it is ready to sample the data, or both.

The PSSI shares most of its circuitry with the digital camera interface (DCMI). It therefore
cannot be used simultaneously with the DCMI.
###### **3.30 LCD-TFT controller**

The LCD-TFT display controller provides a 24-bit parallel digital RGB (Red, Green, Blue)
and delivers all signals to interface directly to a broad range of LCD and TFT panels up to
XGA (1024 x 768) resolution with the following features:

      - 2 display layers with dedicated FIFO (64x64-bit)

      - Color look-up table (CLUT) up to 256 colors (256x24-bit) per layer

      - Up to eight input color formats selectable per layer

      - Flexible blending between two layers using alpha value (per pixel or constant)

      - Flexible programmable parameters for each layer

      - Color keying (transparency color)

      - Up to four programmable interrupt events

      - AXI master interface with burst of 16 words

40/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.31 True random number generator (RNG)**

The RNG is a true random number generator that provides full entropy outputs to the
application as 32-bit samples. It is composed of a live entropy source (analog) and an
internal conditioning component.

The RNG can be used to construct a nondeterministic random bit generator (NDRBG), as a
NIST SP 800-90B compliant entropy source.

The RNG true random number generator has been tested using German BSI statistical tests
of AIS-31 (T0 to T8), and NIST SP800-90B statistical test suite.
###### **3.32 Cryptographic acceleration (CRYP and HASH)**

The devices embed a cryptographic processor that supports the advanced cryptographic
algorithms usually required to ensure confidentiality, authentication, data integrity and nonrepudiation when exchanging messages

with a peer:

      - Encryption/Decryption

–
DES/TDES (data encryption standard/triple data encryption standard): ECB
(electronic codebook) and CBC (cipher block chaining) chaining algorithms, 64-,
128- or 192-bit key

–
AES (advanced encryption standard): ECB, CBC, GCM, CCM, and CTR (counter
mode) chaining algorithms, 128, 192 or 256-bit key

      - Universal HASH

–
– SHA-1 and SHA-2 (secure HASH algorithms)

– – MD5

– – HMAC

The cryptographic accelerator supports DMA request generation.
###### **3.33 On-the-fly decryption engine (OTFDEC)**

The embedded OTFDEC decrypts in real-time the encrypted content stored in the external
Octo-SPI memories used in Memory-mapped mode.

The OTFDEC uses the AES-128 algorithm in counter mode (CTR).

Code execution on external Octo-SPI memories can be protected against fault injection
thanks to

STMicroelectronics enhanced encryption mode (refer to RM0468 for details).

DS13315 Rev 5 41/270


55

**Functional overview** **STM32H730xB**

The OTFDEC main features are as follow:

      - On-the-fly 128-bit decryption during STM32 Octo-SPI read operations (single or
multiple).

–
AES-CTR algorithm with keystream FIFO (depth= 4)

–
Support for any read size

      - Up to four independent encrypted regions

–
Region definition granularity: 4096 bytes

–
Region configuration write locking mechanism

–
Two optional decryption modes: execute-only and execute-never

      - 128-bit key for each region, two-byte firmware version, and eight-byte applicationdefined nonce

      - Encryption keys confidentiality and integrity protection

–
Write only registers with software locking mechanism

–
Availability of 8-bit CRC as public key information

      - Support for STM32 Octo-SPI prefetching mechanism.

42/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.34 Timers and watchdogs**

The devices include two advanced-control timers, twelve general-purpose timers, two basic
timers, five low-power timers, two watchdogs and a SysTick timer.

All timer counters can be frozen in Debug mode.

*Table 4* compares the features of the advanced-control, general-purpose and basic timers.

**Table 4. Timer feature com** **p** **arison**














|Timer type|Timer|Counter resolution|Counter type|Prescaler factor|DMA request generation|Capture/ compare channels|Comple- mentary output|Max interface clock (MHz)|Max timer clock (MHz) (1)|
|---|---|---|---|---|---|---|---|---|---|
|Advanced -control|TIM1, TIM8|16-bit|Up, Down, Up/down|Any integer between 1 and 65536|Yes|4|Yes|137.5|275|
|General purpose|TIM2, TIM5, TIM23, TIM24|32-bit|Up, Down, Up/down|Any integer between 1 and 65536|Yes|4|No|137.5|275|
||TIM3, TIM4|16-bit|Up, Down, Up/down|Any integer between 1 and 65536|Yes|4|No|137.5|275|
||TIM12|16-bit|Up|Any integer between 1 and 65536|No|2|No|137.5|275|
||TIM13, TIM14|16-bit|Up|Any integer between 1 and 65536|No|1|No|137.5|275|
||TIM15|16-bit|Up|Any integer between 1 and 65536|Yes|2|1|137.5|275|
||TIM16, TIM17|16-bit|Up|Any integer between 1 and 65536|Yes|1|1|137.5|275|


DS13315 Rev 5 43/270


55

**Functional overview** **STM32H730xB**

**Table 4. Timer feature com** **p** **arison** **(** **continued** **)**













|Timer type|Timer|Counter resolution|Counter type|Prescaler factor|DMA request generation|Capture/ compare channels|Comple- mentary output|Max interface clock (MHz)|Max timer clock (MHz) (1)|
|---|---|---|---|---|---|---|---|---|---|
|Basic|TIM6, TIM7|16-bit|Up|Any integer between 1 and 65536|Yes|0|No|137.5|275|
|Low- power timer|LPTIM1, LPTIM2, LPTIM3, LPTIM4, LPTIM5|16-bit|Up|1, 2, 4, 8, 16, 32, 64, 128|No|0|No|137.5|275|


1. The maximum timer clock is up to 275 MHz depending on the TIMPRE bit in the RCC_CFGR register and D2PRE1/2 bits in
RCC_D2CFGR register.

44/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**

**3.34.1** **Advanced-control timers (TIM1, TIM8)**

The advanced-control timers (TIM1, TIM8) can be seen as three-phase PWM generators
multiplexed on six channels. They have complementary PWM outputs with programmable
inserted dead times. They can also be considered as complete general-purpose timers.
Their four independent channels can be used for:

      - Input capture

      - Output compare

      - PWM generation (Edge- or center-aligned modes)

      - One-pulse mode output

If configured as standard 16-bit timers, they have the same features as the general-purpose
TIMx timers. If configured as 16-bit PWM generators, they have full modulation capability (0100%).

The advanced-control timer can work together with the TIMx timers via the Timer Link
feature for synchronization or event chaining.

TIM1 and TIM8 support independent DMA request generation.

**3.34.2** **General-purpose timers (TIMx)**

There are 10 synchronizable general-purpose timers embedded in the STM32H730xB
devices (see *Table 4: Timer feature comparison* for differences).

      - **TIM2, TIM3, TIM4, TIM5, TIM23, TIM24**

The devices include four full-featured general-purpose timers: TIM2, TIM3, TIM4,
TIM5, TIM23 and TIM24. TIM2, TIM5, TIM23 and TIM24 are based on a 32-bit
autoreload up/downcounter and a 16-bit prescaler while TIM3 and TIM4 are based on a
16-bit autoreload up/downcounter and a 16-bit prescaler. All timers feature 4
independent channels for input capture/output compare, PWM or One-pulse mode
output. This gives up to 24 input capture/output compare/PWMs on the largest
packages.

TIM2, TIM3, TIM4, TIM5, TIM23 and TIM24 general-purpose timers can work together,
or with the other general-purpose timers and the advanced-control timers TIM1 and
TIM8 via the Timer Link feature for synchronization or event chaining.

Any of these general-purpose timers can be used to generate PWM outputs.

TIM2, TIM3, TIM4, TIM5, TIM23, and TIM24 all have independent DMA request
generation. They are capable of handling quadrature (incremental) encoder signals
and the digital outputs from one to four hall-effect sensors.

      - **TIM12, TIM13, TIM14, TIM15, TIM16, TIM17**

These timers are based on a 16-bit autoreload upcounter and a 16-bit prescaler.
TIM13, TIM14, TIM16 and TIM17 feature one independent channel, whereas TIM12
and TIM15 have two independent channels for input capture/output compare, PWM or
One-pulse mode output. They can be synchronized with the TIM2, TIM3, TIM4, TIM5,
TIM23, and TIM24 full-featured general-purpose timers or used as simple time bases.

DS13315 Rev 5 45/270


55

**Functional overview** **STM32H730xB**

**3.34.3** **Basic timers TIM6 and TIM7**

These timers are mainly used for DAC trigger and waveform generation. They can also be
used as a generic 16-bit time base.

TIM6 and TIM7 support independent DMA request generation.

**3.34.4** **Low-power timers (LPTIM1, LPTIM2, LPTIM3, LPTIM4, LPTIM5)**

The low-power timers have an independent clock and is running also in Stop mode if it is
clocked by LSE, LSI or an external clock. It is able to wake up the devices from Stop mode.

This low-power timer supports the following features:

      - 16-bit up counter with 16-bit autoreload register

      - 16-bit compare register

      - Configurable output: pulse, PWM

      - Continuous / One-shot mode

      - Selectable software / hardware input trigger

      - Selectable clock source:

      - Internal clock source: LSE, LSI, HSI or APB clock

      - External clock source over LPTIM input (working even with no internal clock source
running, used by the Pulse Counter Application)

      - Programmable digital glitch filter

      - Encoder mode

**3.34.5** **Independent watchdog**

The independent watchdog is based on a 12-bit downcounter and 8-bit prescaler. It is
clocked from an independent 32 kHz internal RC and as it operates independently from the
main clock, it can operate in Stop and Standby modes. It can be used either as a watchdog
to reset the device when a problem occurs, or as a free-running timer for application timeout
management. It is hardware- or software-configurable through the option bytes.

A window option allows the device to be reset when a reload operation is made too early
after the previous reload.

**3.34.6** **Window watchdog**

The window watchdog is based on a 7-bit downcounter that can be set as free-running. It
can be used as a watchdog to reset the device when a problem occurs. It is clocked from
the main clock. It has an early warning interrupt capability and the counter can be frozen in
Debug mode.

**3.34.7** **SysTick timer**

This timer is dedicated to real-time operating systems, but could also be used as a standard
down counter. It features:

      - A 24-bit down counter

      - Autoreload capability

      - Maskable system interrupt generation when the counter reaches 0

      - Programmable clock source.

46/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.35 Real-time clock (RTC), backup SRAM and backup registers**

The RTC is an independent BCD timer/counter. It supports the following features:

      - Calendar with subsecond, seconds, minutes, hours (12 or 24 format), week day, date,
month, year, in BCD (binary-coded decimal) format.

      - Automatic correction for 28, 29 (leap year), 30, and 31 days of the month.

      - Two programmable alarms.

      - On-the-fly correction from 1 to 32767 RTC clock pulses. This can be used to
synchronize it with a master clock.

      - Reference clock detection: a more precise second source clock (50 or 60 Hz) can be
used to enhance the calendar precision.

      - Digital calibration circuit with 0.95 ppm resolution, to compensate for quartz crystal
inaccuracy.

      - Three anti-tamper detection pins with programmable filter.

      - Timestamp feature which can be used to save the calendar content. This function can
be triggered by an event on the timestamp pin, or by a tamper event, or by a switch to
V BAT mode.

      - 17-bit autoreload wake-up timer (WUT) for periodic events with programmable
resolution and period.

The RTC and the 32 backup registers are supplied through a switch that takes power either
from the V DD supply when present or from the V BAT pin.

The backup registers are 32-bit registers used to store 128 bytes of user application data
when V DD power is not present. They are not reset by a system or power reset, or when the
device wakes up from Standby mode.

The RTC clock sources can be:

      - A 32.768 kHz external crystal (LSE)

      - An external resonator or oscillator (LSE)

      - The internal low-power RC oscillator (LSI, with typical frequency of 32 kHz)

      - The high-speed external clock (HSE) divided by 32.

The RTC is functional in V BAT mode and in all low-power modes when it is clocked by the
LSE. When clocked by the LSI, the RTC is not functional in V BAT mode, but is functional in
all low-power modes.

All RTC events (Alarm, wake-up timer, timestamp or tamper) can generate an interrupt and
wake up the device from the low-power modes.

DS13315 Rev 5 47/270


55

**Functional overview** **STM32H730xB**
###### **3.36 Inter-integrated circuit interface (I2C)**

STM32H730xB devices embed five I [2] C interfaces.

The I [2] C bus interface handles communications between the microcontroller and the serial
I [2] C bus. It controls all I [2] C bus-specific sequencing, protocol, arbitration and timing.

The I2C peripheral supports:

      - I [2] C-bus specification and user manual rev. 5 compatibility:

–
Target and controller modes, multicontroller capability

–
Standard-mode (Sm), with a bitrate up to 100 kbit/s

–
Fast-mode (Fm), with a bitrate up to 400 kbit/s

–
Fast-mode Plus (Fm+), with a bitrate up to 1 Mbit/s and 20 mA output drive I/Os

–
7-bit and 10-bit addressing mode, multiple 7-bit target addresses

–
Programmable setup and hold times

–
Optional clock stretching

      - System Management Bus (SMBus) specification rev 2.0 compatibility:

–
Hardware PEC (Packet Error Checking) generation and verification with ACK
control

–
Address resolution protocol (ARP) support

– SMBus alert

      - Power system management protocol (PMBus [TM] ) specification rev 1.1 compatibility

      - Independent clock: a choice of independent clock sources allowing the I2C
communication speed to be independent from the PCLK reprogramming.

      - Wake up from Stop mode on address match

      - Programmable analog and digital noise filters

      - 1-byte buffer with DMA capability
###### **3.37 Universal synchronous/asynchronous receiver transmitter ** **(USART)**

STM32H730xB devices have five embedded universal synchronous receiver transmitters
(USART1, USART2, USART3, USART6, and USART10) and five universal asynchronous
receiver transmitters (UART4, UART5, UART7, UART8, and UART9). Refer to *Table 5:*
*USART features* for a summary of USARTx and UARTx features.

These interfaces provide asynchronous communication, IrDA SIR ENDEC support,
multiprocessor communication mode, single-wire half-duplex communication mode and
have LIN master/slave capability. They provide hardware management of the CTS and RTS
signals, and RS485 Driver Enable. They are able to communicate at speeds of up to
17 Mbit/s.

USART1, USART2, USART3, USART6, and USART10 also provide Smartcard mode (ISO
7816 compliant) and SPI-like communication capability.

The USARTs embed a Transmit FIFO (TXFIFO) and a Receive FIFO (RXFIFO). FIFO mode
is enabled by software and is disabled by default.

48/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**

All USART have a clock domain independent from the CPU clock, allowing the USARTx to
wake up the MCU from Stop mode. The wake-up from Stop mode is programmable and can
be done on:

      - Start bit detection

      - Any received data frame

      - A specific programmed data frame

      - Specific TXFIFO/RXFIFO status when FIFO mode is enabled.

All USART interfaces can be served by the DMA controller.

**Table 5. USART features**




|USART modes/features(1)|USART1/2/3/6/10|UART4/5/7/8/9|
|---|---|---|
|Hardware flow control for modem|X|X|
|Continuous communication using DMA|X|X|
|Multiprocessor communication|X|X|
|Synchronous SPI mode (master/slave)|X|-|
|Smartcard mode|X|-|
|Single-wire half-duplex communication|X|X|
|IrDA SIR ENDEC block|X|X|
|LIN mode|X|X|
|Dual clock domain and wake-up from low power mode|X|X|
|Receiver timeout interrupt|X|X|
|Modbus communication|X|X|
|Auto baud rate detection|X|X|
|Driver Enable|X|X|
|USART data length|7, 8 and 9 bits||
|Tx/Rx FIFO|X|X|
|Tx/Rx FIFO size|16||


1. X = supported.
###### **3.38 Low-power universal asynchronous receiver transmitter ** **(LPUART)**

The device embeds one Low-Power UART (LPUART1). The LPUART supports
asynchronous serial communication with minimum power consumption. It supports half
duplex single wire communication and modem operations (CTS/RTS). It allows
multiprocessor communication.

The LPUARTs embed a Transmit FIFO (TXFIFO) and a Receive FIFO (RXFIFO). FIFO
mode is enabled by software and is disabled by default.

DS13315 Rev 5 49/270


55

**Functional overview** **STM32H730xB**

The LPUART has a clock domain independent from the CPU clock, and can wake up the
system from Stop mode. The wake-up from Stop mode are programmable and can be done

on:

      - Start bit detection

      - Any received data frame

      - A specific programmed data frame

      - Specific TXFIFO/RXFIFO status when FIFO mode is enabled.

Only a 32.768 kHz clock (LSE) is needed to allow LPUART communication up to
9600 baud. Therefore, even in Stop mode, the LPUART can wait for an incoming frame
while having an extremely low energy consumption. Higher speed clock can be used to
reach higher baud rates.

LPUART interface can be served by the DMA controller.
###### **3.39 Serial peripheral interface (SPI)/inter- integrated sound ** **interfaces (I2S) **

The devices feature up to six SPIs (SPI2S1, SPI2S2, SPI2S3, SPI4, SPI5 and SPI2S6) that
allow communicating up to 150 Mbits/s in master and slave modes, in half-duplex, fullduplex and simplex modes. The 3-bit prescaler gives eight master mode frequencies and
the frame is configurable from 4 to 32 bits for SPI1/I2S1, SPI2/I2S2, SPI3/I2S3, and from 4
to 16 bits for the other peripherals.

All SPI interfaces support NSS pulse mode, TI mode, Hardware CRC calculation, and 16x
8-bit embedded Rx and Tx FIFOs (SPI1/I2S1, SPI2/I2S2, SPI3/I2S3), and 8x 8-bit
embedded Rx and Tx FIFOs (SPI4, SPI5, SPI6/I2S6), all with DMA capability.

Four standard I [2] S interfaces (multiplexed with SPI1, SPI2, SPI3 and SPI6) are available.
They can be operated in master or slave mode, in half-, full-duplex or simplex
communication mode, and can be configured to operate as a 16-/32-bit resolution input or
output channel (except SPI2S6 which is limited to 16 bits). Audio sampling frequencies from
8 kHz up to 192 kHz are supported. When either or both of the I [2] S interfaces is/are
configured in master mode, the master clock can be output to the external DAC/CODEC at
256 times the sampling frequency. All I [2] S interfaces support 16x 8-bit embedded Rx and Tx
FIFOs with DMA capability.
###### **3.40 Serial audio interfaces (SAI)**

The devices embed two SAIs (SAI1, and SAI4) that allow designing many stereo or mono
audio protocols such as I2S, LSB or MSB-justified, PCM/DSP, TDM or AC’97. An SPDIF
output is available when the audio block is configured as a transmitter. To bring this level of
flexibility and reconfigurability, the SAI contains two independent audio subblocks. Each
block has it own clock generator and I/O line controller.
Audio sampling frequencies up to 192 kHz are supported.
In addition, up to six microphones per SAI instance can be supported thanks to an
embedded PDM interface, with a maximum of 10 microphones due to pinout constraints.
The SAI can work in master or slave configuration. The audio subblocks can be either
receiver or transmitter and can work synchronously or asynchronously (with respect to the
other one). The SAI can be connected with other SAIs to work synchronously.

50/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.41 SPDIFRX Receiver Interface (SPDIFRX)**

The SPDIFRX peripheral is designed to receive an S/PDIF flow compliant with IEC-60958
and IEC-61937. These standards support simple stereo streams up to high sample rate,
and compressed multichannel surround sound, such as those defined by Dolby or DTS (up
to 5.1).

The main SPDIFRX features are the following:

      - Up to four inputs available

      - Automatic symbol rate detection

      - Maximum symbol rate: 12.288 MHz

      - Stereo stream from 32 to 192 kHz supported

      - Supports Audio IEC-60958 and IEC-61937, consumer applications

      - Parity bit management

      - Communication using DMA for audio samples

      - Communication using DMA for control and user channel information

      - Interrupt capabilities

The SPDIFRX receiver provides all the necessary features to detect the symbol rate, and
decode the incoming data stream. The user can select the wanted SPDIF input, and when a
valid signal is available, the SPDIFRX resamples the incoming signal, decode the
Manchester stream, recognize frames, subframes and blocks elements. It delivers to the
CPU decoded data, and associated status flags.

The SPDIFRX also offers a signal named spdif_frame_sync, which toggles at the S/PDIF
subframe rate that is used to compute the exact sample rate for clock drift algorithms.
###### **3.42 Single wire protocol master interface (SWPMI)**

The Single wire protocol master interface (SWPMI) is the master interface corresponding to
the Contactless Frontend (CLF) defined in the ETSI TS 102 613 technical specification. The
main features are:

      - full-duplex communication mode

      - automatic SWP bus state management (active, suspend, resume)

      - configurable bitrate up to 2 Mbit/s

      - automatic SOF, EOF and CRC handling

SWPMI can be served by the DMA controller.

DS13315 Rev 5 51/270


55

**Functional overview** **STM32H730xB**
###### **3.43 Management data input/output (MDIO) slaves**

The devices embed an MDIO slave interface it includes the following features:

      - 32 MDIO Registers addresses, each of which is managed using separate input and
output data registers:

–
32 x 16-bit firmware read/write, MDIO read-only output data registers

–
32 x 16-bit firmware read-only, MDIO write-only input data registers

      - Configurable slave (port) address

      - Independently maskable interrupts/events:

–
MDIO Register write

–
MDIO Register read

–
MDIO protocol error

      - Able to operate in and wake up from Stop mode
###### **3.44 SD/SDIO/MMC card host interfaces (SDMMC)**

Two SDMMC host interfaces are available. They support *MultiMediaCard System*
*Specification Version 4.51* in three different databus modes: 1 bit (default), 4 bits and 8 bits.

Both interfaces support the *SD memory card specifications version 4.1.* and the *SDIO card*
*specification version 4.0.* in two different databus modes: 1 bit (default) and 4 bits.

Each SDMMC host interface supports only one SD/SDIO/MMC card at any one time and a
stack of MMC Version 4.51 or previous.

The SDMMC host interface embeds a dedicated DMA controller allowing high-speed
transfers between the interface and the SRAM.
###### **3.45 Controller area network (FDCAN1, FDCAN2, FDCAN3)**

The controller area network (CAN) subsystem consists of two CAN modules, a shared
message RAM memory and a clock calibration unit.

All CAN modules (FDCAN1, FDCAN2, and FDCAN3) are compliant with ISO 11898-1 (CAN
protocol specification version 2.0 part A, B) and CAN FD protocol specification version 1.0.

FDCAN1 supports time triggered CAN (TT-FDCAN) specified in ISO 11898-4, including
event synchronized time-triggered communication, global system time, and clock drift
compensation. The FDCAN1 contains additional registers, specific to the time triggered
feature. The CAN FD option can be used together with event-triggered and time-triggered
CAN communication.

A 10-Kbyte message RAM memory implements filters, receive FIFOs, receive buffers,
transmit event FIFOs, transmit buffers (and triggers for TT-FDCAN). This message RAM is
shared between the three modules - FDCAN1 FDCAN2 and FDCAN3.

The common clock calibration unit is optional. It can be used to generate a calibrated clock
for FDCAN1, FDCAN2 and FDCAN3 from the HSI internal RC oscillator and the PLL, by
evaluating CAN messages received by the FDCAN1.

52/270 DS13315 Rev 5

**STM32H730xB** **Functional overview**
###### **3.46 Universal serial bus on-the-go high-speed (OTG_HS)**

The devices embed a USB OTG high-speed (up to 480 Mbit/s) device/host/OTG peripheral
that supports both full-speed and high-speed operations. It integrates the transceivers for
full-speed operation (12 Mbit/s) and a UTMI low-pin interface (ULPI) for high-speed
operation (480 Mbit/s). When using the USB OTG_HS interface in HS mode, an external
PHY device connected to the ULPI is required.

The USB OTG_HS peripheral is compliant with the USB 2.0 specification and with the OTG
2.0 specification. It features software-configurable endpoint setting and supports
suspend/resume. The USB OTG_HS controller requires a dedicated 48 MHz clock that is
generated by a PLL connected to the HSE oscillator.

The main features are:

      - Combined Rx and Tx FIFO size of 4 Kbytes with dynamic FIFO sizing

      - Supports the session request protocol (SRP) and host negotiation protocol (HNP)

      - 8 bidirectional endpoints

      - 16 host channels with periodic OUT support

      - Software configurable to OTG1.3 and OTG2.0 modes of operation

      - USB 2.0 LPM (Link Power Management) support

      - Battery Charging Specification Revision 1.2 support

      - Internal FS OTG PHY support

      - External HS or HS OTG operation supporting ULPI in SDR mode The OTG PHY is
connected to the microcontroller ULPI port through 12 signals. It can be clocked using
the 60 MHz output.

      - Internal USB DMA

      - HNP/SNP/IP inside (no need for any external resistor)

      - For OTG/Host modes, a power switch is needed in case bus-powered devices are
connected
###### **3.47 Ethernet MAC interface with dedicated DMA controller (ETH) **

The devices provide an IEEE-802.3-2002-compliant media access controller (MAC) for
ethernet LAN communications through an industry-standard medium-independent interface
(MII) or a reduced medium-independent interface (RMII). The microcontroller requires an
external physical interface device (PHY) to connect to the physical LAN bus (twisted-pair,
fiber, etc.). The PHY is connected to the device MII port using 17 signals for MII or 9 signals
for RMII, and can be clocked using the 25 MHz (MII) from the microcontroller.

DS13315 Rev 5 53/270


55

**Functional overview** **STM32H730xB**

The devices include the following features:

      - Supports 10 and 100 Mbit/s rates

      - Dedicated DMA controller allowing high-speed transfers between the dedicated SRAM
and the descriptors

      - Tagged MAC frame support (VLAN support)

      - Half-duplex (CSMA/CD) and full-duplex operation

      - MAC control sublayer (control frames) support

      - 32-bit CRC generation and removal

      - Several address filtering modes for physical and multicast address (multicast and
group addresses)

      - 32-bit status code for each transmitted or received frame

      - Internal FIFOs to buffer transmit and receive frames. The transmit FIFO and the
receive FIFO are both 2 Kbytes.

      - Supports hardware PTP (precision time protocol) in accordance with IEEE 1588 2008
(PTP V2) with the time stamp comparator connected to the TIM2 input

      - Triggers interrupt when system time becomes greater than target time
###### **3.48 High-definition multimedia interface (HDMI) ** **- consumer electronics control (CEC)**

The devices embed a HDMI-CEC controller that provides hardware support for the
Consumer Electronics Control (CEC) protocol (Supplement 1 to the HDMI standard).

This protocol provides high-level control functions between all audiovisual products in an
environment. It is specified to operate at low speeds with minimum processing and memory
overhead. It has a clock domain independent from the CPU clock, allowing the HDMI-CEC
controller to wake up the MCU from Stop mode on data reception.
###### **3.49 Debug infrastructure**

The devices offer a comprehensive set of debug and trace features to support software
development and system integration.

      - Breakpoint debugging

      - Code execution tracing

      - Software instrumentation

      - JTAG debug port

      - Serial-wire debug port

      - Trigger input and output

      - Serial-wire trace port

      - Trace port

      - Arm [®] CoreSight™ debug and trace components

The debug can be controlled via a JTAG/Serial-wire debug access port, using industrystandard debugging tools. The trace port performs data capture for logging and analysis.

54/270 DS13315 Rev 5

**STM32H730xB** **Memory mapping**
#### **4 Memory mapping**

Refer to the product line reference manual for details on the memory mapping as well as the
boundary addresses for all peripherals.

DS13315 Rev 5 55/270


55

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**
#### **5 Pinouts, pin descriptions and alternate functions**

**Fi** **g** **ure 4. TFBGA100 ballout** **(** **without SMPS** **)**

**1** **2** **3** **4** **5** **6** **7** **8** **9** **10**


**A**

**B**

**C**

**D**

**E**

**F**

**G**

**H**

**J**

**K**










|PC14- OSC32_IN|PC13|PE2|PB9|PB7|PB4|PB3|PA15|PA14|PA13|
|---|---|---|---|---|---|---|---|---|---|
|PC15- OSC32_OUT|VBAT|PE3|PB8|PB6|PD5|PD2|PC11|PC10|PA12|
|PH0-OSC_IN|VSS|PE4|PE1|PB5|PD6|PD3|PC12|PA9|PA11|
|PH1- OSC_OUT|VDD|PE5|PE0|BOOT0|PD7|PD4|PD0|PA8|PA10|
|NRST|PC2_C|PE6|VSS|VSS|VSS|VCAP|PD1|PC9|PC7|
|PC0|PC1|PC3_C|VDD|VDD|VDD33USB|PDR_ON|VCAP|PC8|PC6|
|VSSA|PA0|PA4|PC4|PB2|PE10|PE14|PD15|PD11|PB15|
|VDDA|PA1|PA5|PC5|PE7|PE11|PE15|PD14|PD10|PB14|
|VSS|PA2|PA6|PB0|PE8|PE12|PB10|PB13|PD9|PD13|
|VDD|PA3|PA7|PB1|PE9|PE13|PB11|PB12|PD8|PD12|


MSv52520V1.


1. The above figure shows the package top view.

56/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Fi** **g** **ure 5. LQFP100** **p** **inout** **(** **without SMPS** **)**








1. The above figure shows the package top view.

DS13315 Rev 5 57/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Fi** **g** **ure 6. UFBGA144 ballout** **(** **without SMPS** **)**

**1** **2** **3** **4** **5** **6** **7** **8** **9** **10** **11** **12**


**A**

**B**

**C**

**D**

**E**

**F**

**G**

**H**

**J**

**K**

**L**

**M**



|PC13|PE3|PE2|PE1|PE0|PB4|PB3|PD6|PD7|PA15|PA14|PA13|
|---|---|---|---|---|---|---|---|---|---|---|---|
|PC14- OSC32_IN|PE4|PE5|PE6|PB9|PB5|PG15|PG12|PD5|PC11|PC10|PA12|
|PC15- OSC32_OUT|VBAT|PF0|PF1|PB8|PB6|PG14|PG11|PD4|PC12|VDD33USB|PA11|
|PH0-OSC_IN|VSS|VDD|PF2|BOOT0|PB7|PG13|PG10|PD3|PD1|PA10|PA9|
|PH1- OSC_OUT|PF3|PF4|PF5|PDR_ON|VSS|VSS|PG9|PD2|PD0|PC9|PA8|
|NRST|PF7|PF6|VDD|VDD|VDD|VDD|VDD|VDD|VDD|PC8|PC7|
|PF10|PF9|PF8|VSS|VDD|VDD|VDD|VSS|VCAP|VSS|PG8|PC6|
|PC0|PC1|PC2|PC3|VSS|VSS|VCAP|PE11|PD11|PG7|PG6|PG5|
|VSSA|PA0|PA4|PC4|PB2|PG1|PE10|PE12|PD10|PG4|PG3|PG2|
|VREF-|PA1|PA5|PC5|PF13|PG0|PE9|PE13|PD9|PD13|PD14|PD15|
|VREF+|PA2|PA6|PB0|PF12|PF15|PE8|PE14|PD8|PD12|PB14|PB15|
|VDDA|PA3|PA7|PB1|PF11|PF14|PE7|PE15|PB10|PB11|PB12|PB13|


MSv65136V2













1. The above figure shows the package top view.

58/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**









|Figure 7. LQFP144 pinout (without SMPS) PDR_ON BOOT0 VDD PE1 PE0 PB9 PB8 PB7 PB6 PB5 PB4 PB3 PG15 VDD VSS PG14 PG13 PG12 PG11 PG10 PG9 PD7 PD6 VDD VSS PD5 PD4 PD3 PD2 PD1 PD0 PC12 PC11 PC10 PA15 PA14 144 143 142 141 140 139 138 137 136 135 134 133 132 131 130 129 128 127 126 125 124 123 122 121 120 119 118 117 116 115 114 113 112 111 110 109 PE2 1 108 VDD PE3 2 107 VSS PE4 3 106 VCAP PE5 4 105 PA13 PE6 5 104 PA12 VBAT 6 103 PA11 PC13 7 102 PA10 PC14-OSC32_IN 8 101 PA9 PC15-OSC32_OUT 9 100 PA8 PF0 10 99 PC9 PF1 11 98 PC8 PF2 12 97 PC7 PF3 13 96 PC6 PF4 14 95 VDD33USB PF5 15 94 VSS VSS 16 93 PG8 VDD 17 92 PG7 PF6 18 LQFP144 91 PG6 PF7 19 90 PG5 PF8 20 89 PG4 PF9 21 88 PG3 PF10 22 87 PG2 PH0-OSC_IN 23 86 PD15 PH1-OSC_OUT 24 85 PD14 NRST 25 84 VDD PC0 26 83 VSS PC1 27 82 PD13 PC2_C 28 81 PD12 PC3_C 29 80 PD11 VDD 30 79 PD10 VSSA 31 78 PD9 VREF+ 32 77 PD8 VDDA 33 76 PB15 PA0 34 75 PB14 PA1 35 74 PB13 PA2 36 73 PB12 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 PA3 VSS VDD PA4 PA5 PA6 PA7 PC4 PC5 PB0 PB1 PB2 PF11 PF12 VSS VDD PF13 PF14 PF15 PG0 PG1 PE7 PE8 PE9 VSS VDD PE10 PE11 PE12 PE13 PE14 PE15 PB10 PB11 VCAP VDD MSv52522V1.|Col2|Col3|
|---|---|---|
||PDR_ON BOOT0 VDD PE1 PE0 PB9 PB8 PB7 PB6 PB5 PB4 PB3 PG15 VDD VSS PG14 PG13 PG12 PG11 PG10 PG9 PD7 PD6 VDD VSS PD5 PD4 PD3 PD2 PD1 PD0 PC12 PC11 PC10 PA15 PA14 144 143 142 141 140 139 138 137 136 135 134 133 132 131 130 129 128 127 126 125 124 123 122 121 120 119 118 117 116 115 114 113 112 111 110 109 PE2 1 108 VDD PE3 2 107 VSS PE4 3 106 VCAP PE5 4 105 PA13 PE6 5 104 PA12 VBAT 6 103 PA11 PC13 7 102 PA10 PC14-OSC32_IN 8 101 PA9 PC15-OSC32_OUT 9 100 PA8 PF0 10 99 PC9 PF1 11 98 PC8 PF2 12 97 PC7 PF3 13 96 PC6 PF4 14 95 VDD33USB PF5 15 94 VSS VSS 16 93 PG8 VDD 17 92 PG7 PF6 18 LQFP144 91 PG6 PF7 19 90 PG5 PF8 20 89 PG4 PF9 21 88 PG3 PF10 22 87 PG2 PH0-OSC_IN 23 86 PD15 PH1-OSC_OUT 24 85 PD14 NRST 25 84 VDD PC0 26 83 VSS PC1 27 82 PD13 PC2_C 28 81 PD12 PC3_C 29 80 PD11 VDD 30 79 PD10 VSSA 31 78 PD9 VREF+ 32 77 PD8 VDDA 33 76 PB15 PA0 34 75 PB14 PA1 35 74 PB13 PA2 36 73 PB12 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 PA3 VSS VDD PA4 PA5 PA6 PA7 PC4 PC5 PB0 PB1 PB2 PF11 PF12 VSS VDD PF13 PF14 PF15 PG0 PG1 PE7 PE8 PE9 VSS VDD PE10 PE11 PE12 PE13 PE14 PE15 PB10 PB11 VCAP VDD MSv52522V1.||
||||


1. The above figure shows the package top view.


DS13315 Rev 5 59/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**













|Figure 8. LQFP176 pinout (with SMPS) VDDLDO PDR_ON VDDLDO BOOT0 VDD VSS VCAP PE1 PE0 PB9 PB8 PB7 PB6 PB5 PB4 PB3 PG15 VDD VSS PG14 PG13 PG12 PG11 PG10 PG9 VDD VSS PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0 PC12 PC11 PC10 PA15 PA14 VSS VDD VSS VCAP 176 175 174 173 172 171 170 169 168 167 166 165 164 163 162 161 160 159 158 157 156 155 154 153 152 151 150 149 148 147 146 145 144 143 142 141 140 139 138 137 136 135 134 133 PE2 1 132 PA13 PE3 2 131 PA12 PE4 3 130 PA11 PE5 4 129 PA10 PE6 5 128 PA9 VSS 6 127 PA8 VDD 7 126 VDD VBAT 8 125 PC9 PC13 9 124 PC8 PC14-OSC32_IN 10 123 PC7 PC15-OSC32_OUT 11 122 PC6 VSS 12 121 VDD33USB VDD 13 120 VDD50USB VSSSMPS 14 119 VSS VLXSMPS 15 118 PG8 VDDSMPS 16 117 PG7 VFBSMPS 17 116 PG6 PF0 18 115 PG5 PF1 19 114 PG4 PF2 20 113 VDD PF3 21 112 VSS PF4 22 LQFP176 111 PG3 PF5 23 110 PG2 VSS 24 109 PK2 VDD 25 108 PK1 PF6 26 107 PK0 PF7 27 106 VSS PF8 28 105 VDD PF9 29 104 PJ11 PF10 30 103 PJ10 PH0-OSC_IN 31 102 PJ9 PH1-OSC_OUT 32 101 PJ8 NRST 33 100 VSS PC0 34 99 VDD PC1 35 98 PD15 PC2_C 36 97 PD14 PC3_C 37 96 PD13 VSSA 38 95 PD12 VREF+ 39 94 PD11 VDDA 40 93 VSS PA0 41 92 VDD PA1 42 91 PD10 PA2 43 90 PD9 VDD 44 89 PD8 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 VSS PA3 VSS VDD PA4 PA5 PA6 PA7 PC4 PC5 PB0 PB1 PB2 PF11 PF12 PF13 PF14 PF15 PG0 VSS VDD PG1 PE7 PE8 PE9 VSS VDD PE10 PE11 PE12 PE13 PE14 PE15 PB10 PB11 VCAP VSS VDDLDO VSS VDD PB12 PB13 PB14 PB15 MSv52553V1.|Col2|Col3|
|---|---|---|
||VDDLDO PDR_ON VDDLDO BOOT0 VDD VSS VCAP PE1 PE0 PB9 PB8 PB7 PB6 PB5 PB4 PB3 PG15 VDD VSS PG14 PG13 PG12 PG11 PG10 PG9 VDD VSS PD7 PD6 PD5 PD4 PD3 PD2 PD1 PD0 PC12 PC11 PC10 PA15 PA14 VSS VDD VSS VCAP 176 175 174 173 172 171 170 169 168 167 166 165 164 163 162 161 160 159 158 157 156 155 154 153 152 151 150 149 148 147 146 145 144 143 142 141 140 139 138 137 136 135 134 133 PE2 1 132 PA13 PE3 2 131 PA12 PE4 3 130 PA11 PE5 4 129 PA10 PE6 5 128 PA9 VSS 6 127 PA8 VDD 7 126 VDD VBAT 8 125 PC9 PC13 9 124 PC8 PC14-OSC32_IN 10 123 PC7 PC15-OSC32_OUT 11 122 PC6 VSS 12 121 VDD33USB VDD 13 120 VDD50USB VSSSMPS 14 119 VSS VLXSMPS 15 118 PG8 VDDSMPS 16 117 PG7 VFBSMPS 17 116 PG6 PF0 18 115 PG5 PF1 19 114 PG4 PF2 20 113 VDD PF3 21 112 VSS PF4 22 LQFP176 111 PG3 PF5 23 110 PG2 VSS 24 109 PK2 VDD 25 108 PK1 PF6 26 107 PK0 PF7 27 106 VSS PF8 28 105 VDD PF9 29 104 PJ11 PF10 30 103 PJ10 PH0-OSC_IN 31 102 PJ9 PH1-OSC_OUT 32 101 PJ8 NRST 33 100 VSS PC0 34 99 VDD PC1 35 98 PD15 PC2_C 36 97 PD14 PC3_C 37 96 PD13 VSSA 38 95 PD12 VREF+ 39 94 PD11 VDDA 40 93 VSS PA0 41 92 VDD PA1 42 91 PD10 PA2 43 90 PD9 VDD 44 89 PD8 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 VSS PA3 VSS VDD PA4 PA5 PA6 PA7 PC4 PC5 PB0 PB1 PB2 PF11 PF12 PF13 PF14 PF15 PG0 VSS VDD PG1 PE7 PE8 PE9 VSS VDD PE10 PE11 PE12 PE13 PE14 PE15 PB10 PB11 VCAP VSS VDDLDO VSS VDD PB12 PB13 PB14 PB15 MSv52553V1.||


1. The above figure shows the package top view.

60/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Fi** **g** **ure 9. UFBGA169 ballout** **(** **with SMPS** **)**


**A**

**B**

**C**

**D**

**E**

**F**

**G**

**H**

**J**

**K**

**L**

**M**


**1** **2** **3** **4** **5** **6** **7** **8** **9** **10** **11** **12**






**13**










|PE4|PE2|VDD|VCAP|PB6|VDD|VDD|PG10|PD5|VDD|PC12|PC10|PH14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PC15- OSC32_OUT|PE3|VSS|VDDLDO|PB8|PB4|VSS|PG11|PD6|VSS|PC11|PA14|PH13|
|PC14- OSC32_IN|PE6|PE5|PDR_ON|PB9|PB5|PG14|PG9|PD4|PD1|PA15|VSS|VDD|
|VDD|VSS|PC13|PE1|PE0|PB7|PG13|PD7|PD3|PD0|PA13|VDDLDO|VCAP|
|VLXSMPS|VSSSMPS|VBAT|PF1|PF3|BOOT0|PG15|PG12|PD2|PA10|PA9|PA8|PA12|
|VDDSMPS|VFBSMPS|PF0|PF2|PF5|PF7|PB3|PG4|PC6|PC7|PC9|PC8|PA11|
|VDD|VSS|PF4|PF6|PF9|NRST|PF13|PE7|PG6|PG7|PG8|VDD50USB|VDD33USB|
|PH0-OSC_IN|PH1- OSC_OUT|PF10|PF8|PC2|PA4|PF14|PE8|PG2|PG3|PG5|VSS|VDD|
|PC0|PC1|VSSA|PC3|PA0|PA7|PF15|PE9|PE14|PD11|PD13|PD15|PD14|
|PC3_C|PC2_C|PA0_C|PA1|PA6|PC4|PG0|PE13|PH10|PH12|PD9|PD10|PD12|
|VDDA|VREF+|PA1_C|PA5|PB1|PB2|PG1|PE12|PB10|PH11|PB13|VSS|VDD|
|VDD|VSS|PH3|VSS|PB0|PF11|VSS|PE10|PB11|VDDLDO|VSS|PD8|PB15|
|PA2|PH2|PA3|VDD|PC5|PF12|VDD|PE11|PE15|VCAP|VDD|PB12|PB14|


MSv52551V1.

1. The above figure shows the package top view.





|VSS|VSS|VSS|VSS|VSS|
|---|---|---|---|---|
|VSS|VSS|VSS|VSS|VSS|
|VSS|VSS|VSS|VSS|VSS|
|VSS|VSS|VSS|VSS|VSS|
|VSS|VSS|VSS|VSS|VSS|













|Col1|Figure 10. UFBGA176+25 ballout (with SMPS)|Col3|
|---|---|---|
||||
||1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 A VSS PB8 VDDLDO VCAP PB6 PB3 PG11 PG9 PD3 PD1 PA15 PA14 VDDLDO VCAP VSS B PE4 PE3 PB9 PE0 PB7 PB4 PG13 PD7 PD5 PD2 PC12 PH14 PA13 PA8 PA12 C PC13 VSS PE2 PE1 BOOT0 PB5 PG14 PG10 PD4 PD0 PC11 PC10 PH13 PA10 PA11 D OSCP 3C 21 _5 O- UT OSP CC 31 24 _- IN PE5 PDR_ON VDD VSS PG15 PG12 PD6 VSS VDD PH15 PA9 PC8 PC7 E VSS VBAT PE6 VDD VDD PC9 PC6 VDD50USB F VLXSMPS VSSSMPS PF1 PF0 VSS VSS VSS VSS VSS VSS VDD33USB PG6 PG5 G VDDSMPS VFBSMPS PF2 VDD VSS VSS VSS VSS VSS PG8 PG7 PG4 PG2 H PF6 PF4 PF5 PF3 VSS VSS VSS VSS VSS VDD PG3 PD14 PD13 J PH0-OSC_IN PF8 PF7 PF9 VSS VSS VSS VSS VSS PD15 PD11 VSS PD12 K OSP CH _1 O- UT VSS PF10 VDD VSS VSS VSS VSS VSS VSS PD9 PB15 PB14 L NRST PC0 PC1 VREF- VDD PD10 PD8 PB13 M PC2 PC3 VREF+ VDDA VDD VSS PC5 PB1 VDD VSS PH7 PE14 PH11 PH9 PB12 N PC2_C PC3_C VSSA PH2 PA3 PA7 PF11 PE8 PG1 PF15 PF13 PB10 PH8 PH10 PH12 P PA0 PA1 PA1_C PH4 PA4 PA5 PB2 PG0 PE7 PB11 PF12 PE12 PE13 PE15 PH6 R VSS PA2 PA0_C PH3 PH5 PC4 PA6 PB0 PE10 PF14 PE9 PE11 VCAP VDDLDO VSS MSv52552V1.||


|VSS|PB8|VDDLDO|VCAP|PB6|PB3|PG11|PG9|PD3|PD1|PA15|PA14|VDDLDO|VCAP|VSS|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|PE4|PE3|PB9|PE0|PB7|PB4|PG13|PD7|PD5|PD2|PC12|PH14|PA13|PA8|PA12|
|PC13|VSS|PE2|PE1|BOOT0|PB5|PG14|PG10|PD4|PD0|PC11|PC10|PH13|PA10|PA11|
|PC15- OSC32_OUT|PC14- OSC32_IN|PE5|PDR_ON|VDD|VSS|PG15|PG12|PD6|VSS|VDD|PH15|PA9|PC8|PC7|
|VSS|VBAT|PE6|VDD|VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS|||||||VDD|PC9|PC6|VDD50USB|
|VLXSMPS|VSSSMPS|PF1|PF0||||||||VSS|VDD33USB|PG6|PG5|
|VDDSMPS|VFBSMPS|PF2|VDD||||||||PG8|PG7|PG4|PG2|
|PF6|PF4|PF5|PF3||||||||VDD|PG3|PD14|PD13|
|PH0-OSC_IN|PF8|PF7|PF9||||||||PD15|PD11|VSS|PD12|
|PH1- OSC_OUT|VSS|PF10|VDD||||||||VSS|PD9|PB15|PB14|
|NRST|PC0|PC1|VREF-||||||||VDD|PD10|PD8|PB13|
|PC2|PC3|VREF+|VDDA|VDD|VSS|PC5|PB1|VDD|VSS|PH7|PE14|PH11|PH9|PB12|
|PC2_C|PC3_C|VSSA|PH2|PA3|PA7|PF11|PE8|PG1|PF15|PF13|PB10|PH8|PH10|PH12|
||||||||||||||||
|PA0|PA1|PA1_C|PH4|PA4|PA5|PB2|PG0|PE7|PB11|PF12|PE12|PE13|PE15|PH6|
|VSS|PA2|PA0_C|PH3|PH5|PC4|PA6|PB0|PE10|PF14|PE9|PE11|VCAP|VDDLDO|VSS|


1. The above figure shows the package top view.

DS13315 Rev 5 61/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 6. Le** **g** **end/abbreviations used in the** **p** **inout table**




|Name|Col2|Abbreviation|Definition|
|---|---|---|---|
|Pin name||Unless otherwise specified in brackets below the pin name, the pin function during and after reset is the same as the actual pin name||
|Pin type||S|Supply pin|
|||I|Input only pin|
|||I/O|Input / output pin|
|||ANA|Analog-only Input|
|I/O structure||FT|5 V tolerant I/O|
|||TT|3.3 V tolerant I/O|
|||B|Dedicated BOOT0 pin|
|||RST|Bidirectional reset pin with embedded weak pull-up resistor|
|||Option for TT and FT I/Os||
|||_f|I2C FM+ option|
|||_a|analog option (supplied by V ) DDA|
|||_u|USB option (supplied by V ) DD33USB|
|||_h|High-speed low-voltage I/O|
|Notes||Unless otherwise specified by a note, all I/Os are set as floating inputs during and after reset.||
|Pin functions|Alternate functions|Functions selected through GPIOx_AFR registers||
||Additional functions|Functions directly selected/enabled through peripheral registers||


62/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions**






|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|A3|1|1|A3|A2|C3|1|PE2|I/O|FT _h|-|TRACECLK, SAI1_CK1, USART10_RX, SPI4_SCK, SAI1_MCLK_A, SAI4_MCLK_A, OCTOSPIM_P1_IO2, SAI4_CK1, ETH_MII_TXD3, FMC_A23, EVENTOUT|-|
|B3|2|2|A2|B2|B2|2|PE3|I/O|FT _h|-|TRACED0, TIM15_BKIN, SAI1_SD_B, SAI4_SD_B, USART10_TX, FMC_A19, EVENTOUT|-|
|C3|3|3|B2|A1|B1|3|PE4|I/O|FT _h|-|TRACED1, SAI1_D2, DFSDM1_DATIN3, TIM15_CH1N, SPI4_NSS, SAI1_FS_A, SAI4_FS_A, SAI4_D2, FMC_A20, DCMI_D4/PSSI_D4, LCD_B0, EVENTOUT|-|
|D3|4|4|B3|C3|D3|4|PE5|I/O|FT _h|-|TRACED2, SAI1_CK2, DFSDM1_CKIN3, TIM15_CH1, SPI4_MISO, SAI1_SCK_A, SAI4_SCK_A, SAI4_CK2, FMC_A21, DCMI_D6/PSSI_D6, LCD_G0, EVENTOUT|-|
|E3|5|5|B4|C2|E3|5|PE6|I/O|FT _h|-|TRACED3, TIM1_BKIN2, SAI1_D1, TIM15_CH2, SPI4_MOSI, SAI1_SD_A, SAI4_SD_A, SAI4_D1, SAI4_MCLK_B, TIM1_BKIN2_COMP12, FMC_A22, DCMI_D7/PSSI_D7, LCD_G1, EVENTOUT|-|
|-|-|-|-|-|-|6|VSS|S|-|-|-|-|
|-|-|-|-|-|-|7|VDD|S|-|-|-|-|
|B2|6|6|C2|E3|E2|8|VBAT|S|-|-|-|-|
|A2|7|7|A1|D3|C1|9|PC13|I/O|FT|-|EVENTOUT|RTC_TAMP1/ RTC_TS, WKUP4|
|A1|8|8|B1|C1|D2|10|PC14-OSC32_IN|I/O|FT|-|EVENTOUT|OSC32_IN|


DS13315 Rev 5 63/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**









|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|B1|9|9|C1|B1|D1|11|PC15- OSC32_OUT|I/O|FT|-|EVENTOUT|OSC32_OUT|
|-|-|-|-|-|-|12|VSS|S|-|-|-|-|
|-|-|-|-|-|-|13|VDD|S|-|-|-|-|
|-|-|-|-|E2|F2|14|VSSSMPS|S|-|-|-|-|
|-|-|-|-|E1|F1|15|VLXSMPS|S|-|-|-|-|
|-|-|-|-|F1|G1|16|VDDSMPS|S|-|-|-|-|
|-|-|-|-|F2|G2|17|VFBSMPS|S|-|-|-|-|
|-|-|10|C3|F3|F4|18|PF0|I/O|FT _fh|-|I2C2_SDA(boot), I2C5_SDA, OCTOSPIM_P2_IO0, FMC_A0, TIM23_CH1, EVENTOUT|-|
|-|-|11|C4|E4|F3|19|PF1|I/O|FT _fh|-|I2C2_SCL(boot), I2C5_SCL, OCTOSPIM_P2_IO1, FMC_A1, TIM23_CH2, EVENTOUT|-|
|-|-|12|D4|F4|G3|20|PF2|I/O|FT _h|-|I2C2_SMBA, I2C5_SMBA, OCTOSPIM_P2_IO2, FMC_A2, TIM23_CH3, EVENTOUT|-|
|-|-|13|E2|E5|H4|21|PF3|I/O|FT _ha|-|OCTOSPIM_P2_IO3, FMC_A3, TIM23_CH4, EVENTOUT|ADC3_INP5|
|-|-|14|E3|G3|H2|22|PF4|I/O|FT _ha|-|OCTOSPIM_P2_CLK, FMC_A4, EVENTOUT|ADC3_INN5, ADC3_INP9|
|-|-|15|E4|F5|H3|23|PF5|I/O|FT _ha|-|OCTOSPIM_P2_NCLK, FMC_A5, EVENTOUT|ADC3_INP4|
|-|10|16|-|-|-|24|VSS|S|-|-|-|-|
|-|11|17|-|-|-|25|VDD|S|-|-|-|-|
|-|-|18|F3|G4|H1|26|PF6|I/O|FT _ha|-|TIM16_CH1, FDCAN3_RX, SPI5_NSS, SAI1_SD_B, UART7_RX, SAI4_SD_B, OCTOSPIM_P1_IO3, TIM23_CH1, EVENTOUT|ADC3_INN4, ADC3_INP8|


64/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**









|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|19|F2|F6|J3|27|PF7|I/O|FT _ha|-|TIM17_CH1, FDCAN3_TX, SPI5_SCK, SAI1_MCLK_B, UART7_TX, SAI4_MCLK_B, OCTOSPIM_P1_IO2, TIM23_CH2, EVENTOUT|ADC3_INP3|
|-|-|20|G3|H4|J2|28|PF8|I/O|FT _ha|-|TIM16_CH1N, SPI5_MISO, SAI1_SCK_B, UART7_RTS/UART7_DE, SAI4_SCK_B, TIM13_CH1, OCTOSPIM_P1_IO0, TIM23_CH3, EVENTOUT|ADC3_INN3, ADC3_INP7|
|-|-|21|G2|G5|J4|29|PF9|I/O|FT _ha|-|TIM17_CH1N, SPI5_MOSI, SAI1_FS_B, UART7_CTS, SAI4_FS_B, TIM14_CH1, OCTOSPIM_P1_IO1, TIM23_CH4, EVENTOUT|ADC3_INP2|
|-|-|22|G1|H3|K3|30|PF10|I/O|FT _ha|-|TIM16_BKIN, SAI1_D3, PSSI_D15, OCTOSPIM_P1_CLK, SAI4_D3, DCMI_D11/PSSI_D11, LCD_DE, EVENTOUT|ADC3_INN2, ADC3_INP6|
|C1|12|23|D1|H1|J1|31|PH0-OSC_IN|I/O|FT|-|EVENTOUT|OSC_IN|
|D1|13|24|E1|H2|K1|32|PH1-OSC_OUT|I/O|FT|-|EVENTOUT|OSC_OUT|
|E1|14|25|F1|G6|L1|33|NRST|I/O|RS T|-|-|-|
|F1|15|26|H1|J1|L2|34|PC0|I/O|FT _ha|-|FMC_D12/FMC_AD12, DFSDM1_CKIN0, DFSDM1_DATIN4, SAI4_FS_B, FMC_A25, OTG_HS_ULPI_STP, LCD_G2, FMC_SDNWE, LCD_R5, EVENTOUT|ADC123_INP10|
|F2|16|27|H2|J2|L3|35|PC1|I/O|FT _ha|-|TRACED0, SAI4_D1, SAI1_D1, DFSDM1_DATIN0, DFSDM1_CKIN4, SPI2_MOSI/I2S2_SDO, SAI1_SD_A, SAI4_SD_A, SDMMC2_CK, OCTOSPIM_P1_IO4, ETH_MDC, MDIOS_MDC, LCD_G5, EVENTOUT|ADC123_INN10, ADC123_INP11, RTC_TAMP3, WKUP6|


DS13315 Rev 5 65/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**














|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|-|H3|H5 (1)|M1 (1)|-|PC2|I/O|FT _a|-|PWR_DEEPSLEEP, DFSDM1_CKIN1, OCTOSPIM_P1_IO5, SPI2_MISO/I2S2_SDI, DFSDM1_CKOUT, OCTOSPIM_P1_IO2, OTG_HS_ULPI_DIR, ETH_MII_TXD2, FMC_SDNE0, EVENTOUT|ADC123_INN11, ADC123_INP12|
|E2 (2)|17 (2)|28 (2)|-|K2 (1)|N1 (1)|36 (2)|PC2_C(3)|AN A|TT _a|-|-|ADC3_INN1, ADC3_INP0|
|-|-|-|H4|J4 (1)|M2 (1)|-|PC3|I/O|FT _a|-|PWR_SLEEP, DFSDM1_DATIN1, OCTOSPIM_P1_IO6, SPI2_MOSI/I2S2_SDO, OCTOSPIM_P1_IO0, OTG_HS_ULPI_NXT, ETH_MII_TX_CLK, FMC_SDCKE0, EVENTOUT|ADC12_INN12, ADC12_INP13|
|F3 (2)|18 (2)|29 (2)|-|K1 (1)|N2 (1)|37 (2)|PC3_C(3)|AN A|TT _a|-|-|ADC3_INP1|
|-|-|30|-|-|-|-|VDD|S|-|-|-|-|
|G1|19|31|J1|J3|N3|38|VSSA|S|-|-|-|-|
|-|-|-|K1|-|L4|-|VREF-|S|-|-|-|-|
|-|20|32|L1|L2|M3|39|VREF+|S|-|-|-|-|
|H1|21|33|M1|L1|M4|40|VDDA|S|-|-|-|-|
|G2|22|34|J2|J5 (1)|P1 (1)|41|PA0|I/O|FT _ha|-|TIM2_CH1/TIM2_ETR, TIM5_CH1, TIM8_ETR, TIM15_BKIN, SPI6_NSS/I2S6_WS, USART2_CTS/USART2_NSS, UART4_TX, SDMMC2_CMD, SAI4_SD_B, ETH_MII_CRS, FMC_A19, EVENTOUT|ADC1_INP16, WKUP1|
|-|-|-|-|K3 (1)|R3 (1)|-|PA0_C(3)|AN A|TT _a|-|-|ADC12_INN1, ADC12_INP0|


66/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**














|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|H2|23|35|K2|K4 (1)|P2 (1)|42|PA1|I/O|FT _ha|-|TIM2_CH2, TIM5_CH2, LPTIM3_OUT, TIM15_CH1N, USART2_RTS/USART2_DE, UART4_RX, OCTOSPIM_P1_IO3, SAI4_MCLK_B, ETH_MII_RX_CLK/ETH_RMII _REF_CLK, OCTOSPIM_P1_DQS, LCD_R2, EVENTOUT|ADC1_INN16, ADC1_INP17|
|-|-|-|-|L3 (1)|P3 (1)|-|PA1_C(3)|AN A|TT _a|-|-|ADC12_INP1|
|J2|24|36|L2|N1|R2|43|PA2|I/O|FT _ha|-|TIM2_CH3, TIM5_CH3, LPTIM4_OUT, TIM15_CH1, OCTOSPIM_P1_IO0, USART2_TX(boot), SAI4_SCK_B, ETH_MDIO, MDIOS_MDIO, LCD_R1, EVENTOUT|ADC12_INP14, WKUP2|
|-|-|-|-|N2|N4|-|PH2|I/O|FT _ha|-|LPTIM1_IN2, OCTOSPIM_P1_IO4, SAI4_SCK_B, ETH_MII_CRS, FMC_SDCKE0, LCD_R0, EVENTOUT|ADC3_INP13|
|-|-|-|-|-|-|44|VDD|S|-|-|-|-|
|-|-|-|-|-|-|45|VSS|S|-|-|-|-|
|-|-|-|-|M3|R4|-|PH3|I/O|FT _ha|-|OCTOSPIM_P1_IO5, SAI4_MCLK_B, ETH_MII_COL, FMC_SDNE0, LCD_R1, EVENTOUT|ADC3_INN13, ADC3_INP14|
|-|-|-|-|-|P4|-|PH4|I/O|FT _fa|-|I2C2_SCL, LCD_G5, OTG_HS_ULPI_NXT, PSSI_D14, LCD_G4, EVENTOUT|ADC3_INN14, ADC3_INP15|
|-|-|-|-|-|R5|-|PH5|I/O|FT _fh a|-|I2C2_SDA, SPI5_NSS, FMC_SDNWE, EVENTOUT|ADC3_INN15|


DS13315 Rev 5 67/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**







|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|K2|25|37|M2|N3|N5|46|PA3|I/O|FT _ha|-|TIM2_CH4, TIM5_CH4, LPTIM5_OUT, TIM15_CH2, I2S6_MCK, OCTOSPIM_P1_IO2, USART2_RX(boot), LCD_B2, OTG_HS_ULPI_D0, ETH_MII_COL, OCTOSPIM_P1_CLK, LCD_B5, EVENTOUT|ADC12_INP15|
|-|26|38|-|-|-|47|VSS|S|-|-|-|-|
|-|27|39|-|-|-|48|VDD|S|-|-|-|-|
|G3|28|40|J3|H6|P5|49|PA4|I/O|TT _ha|-|D1PWREN, TIM5_ETR, SPI1_NSS(boot)/I2S1_WS, SPI3_NSS/I2S3_WS, USART2_CK, SPI6_NSS/I2S6_WS, FMC_D8/FMC_AD8, DCMI_HSYNC/PSSI_DE, LCD_VSYNC, EVENTOUT|ADC12_INP18, DAC1_OUT1|
|H3|29|41|K3|L4|P6|50|PA5|I/O|TT _ha|-|D2PWREN, TIM2_CH1/TIM2_ETR, TIM8_CH1N, SPI1_SCK(boot)/I2S1_CK, SPI6_SCK/I2S6_CK, OTG_HS_ULPI_CK, FMC_D9/FMC_AD9, PSSI_D14, LCD_R4, EVENTOUT|ADC12_INN18, ADC12_INP19, DAC1_OUT2|
|J3|30|42|L3|K5|R7|51|PA6|I/O|FT _ha|-|TIM1_BKIN, TIM3_CH1, TIM8_BKIN, SPI1_MISO(boot)/I2S1_SDI, OCTOSPIM_P1_IO3, SPI6_MISO/I2S6_SDI, TIM13_CH1, TIM8_BKIN_COMP12, MDIOS_MDC, TIM1_BKIN_COMP12, DCMI_PIXCLK/PSSI_PDCK, LCD_G2, EVENTOUT|ADC12_INP3|


68/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**





|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|K3|31|43|M3|J6|N6|52|PA7|I/O|TT _ha|-|TIM1_CH1N, TIM3_CH2, TIM8_CH1N, SPI1_MOSI(boot)/I2S1_SDO, SPI6_MOSI/I2S6_SDO, TIM14_CH1, OCTOSPIM_P1_IO2, ETH_MII_RX_DV/ETH_RMII_ CRS_DV, FMC_SDNWE, LCD_VSYNC, EVENTOUT|ADC12_INN3, ADC12_INP7, OPAMP1_VINM|
|G4|32|44|J4|K6|R6|53|PC4|I/O|TT _ha|-|PWR_DEEPSLEEP, FMC_A22, DFSDM1_CKIN2, I2S1_MCK, SPDIFRX1_IN3, SDMMC2_CKIN, ETH_MII_RXD0/ETH_RMII_R XD0, FMC_SDNE0, LCD_R7, EVENTOUT|ADC12_INP4, OPAMP1_VOUT, COMP1_INM|
|H4|33|45|K4|N5|M7|54|PC5|I/O|TT _ha|-|PWR_SLEEP, SAI4_D3, SAI1_D3, DFSDM1_DATIN2, PSSI_D15, SPDIFRX1_IN4, OCTOSPIM_P1_DQS, ETH_MII_RXD1/ETH_RMII_R XD1, FMC_SDCKE0, COMP1_OUT, LCD_DE, EVENTOUT|ADC12_INN4, ADC12_INP8, OPAMP1_VINM|
|J4|34|46|L4|M5|R8|55|PB0|I/O|TT _ha|-|TIM1_CH2N, TIM3_CH3, TIM8_CH2N, OCTOSPIM_P1_IO1, DFSDM1_CKOUT, UART4_CTS, LCD_R3, OTG_HS_ULPI_D1, ETH_MII_RXD2, LCD_G1, EVENTOUT|ADC12_INN5, ADC12_INP9, OPAMP1_VINP, COMP1_INP|
|K4|35|47|M4|L5|M8|56|PB1|I/O|FT _ha|-|TIM1_CH3N, TIM3_CH4, TIM8_CH3N, OCTOSPIM_P1_IO0, DFSDM1_DATIN1, LCD_R6, OTG_HS_ULPI_D2, ETH_MII_RXD3, LCD_G0, EVENTOUT|ADC12_INP5, COMP1_INM|


DS13315 Rev 5 69/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**











|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|G5|36|48|J5|L6|P7|57|PB2|I/O|FT _ha|-|RTC_OUT, SAI4_D1, SAI1_D1, DFSDM1_CKIN1, SAI1_SD_A, SPI3_MOSI/I2S3_SDO, SAI4_SD_A, OCTOSPIM_P1_CLK, OCTOSPIM_P1_DQS, ETH_TX_ER, TIM23_ETR, EVENTOUT|COMP1_INP|
|-|-|49|M5|M6|N7|58|PF11|I/O|FT _ha|-|SPI5_MOSI, OCTOSPIM_P1_NCLK, SAI4_SD_B, FMC_NRAS, DCMI_D12/PSSI_D12, TIM24_CH1, EVENTOUT|ADC1_INP2|
|-|-|50|L5|N6|P11|59|PF12|I/O|FT _ha|-|OCTOSPIM_P2_DQS, FMC_A6, TIM24_CH2, EVENTOUT|ADC1_INN2, ADC1_INP6|
|-|-|51|-|-|-|-|VSS|S|-|-|-|-|
|-|-|52|-|-|-|-|VDD|S|-|-|-|-|
|-|-|53|K5|G7|N11|60|PF13|I/O|FT _ha|-|DFSDM1_DATIN6, I2C4_SMBA, FMC_A7, TIM24_CH3, EVENTOUT|ADC2_INP2|
|-|-|54|M6|H7|R10|61|PF14|I/O|FT _fh a|-|DFSDM1_CKIN6, I2C4_SCL, FMC_A8, TIM24_CH4, EVENTOUT|ADC2_INN2, ADC2_INP6|
|-|-|55|L6|J7|N10|62|PF15|I/O|FT _fh|-|I2C4_SDA, FMC_A9, EVENTOUT|-|
|-|-|56|K6|K7|P8|63|PG0|I/O|FT _h|-|OCTOSPIM_P2_IO4, UART9_RX, FMC_A10, EVENTOUT|-|
|-|-|-|-|-|-|64|VSS|S|-|-|-|-|
|-|-|-|-|-|-|65|VDD|S|-|-|-|-|
|-|-|57|J6|L7|N9|66|PG1|I/O|TT _h|-|OCTOSPIM_P2_IO5, UART9_TX, FMC_A11, EVENTOUT|OPAMP2_VINM|
|H5|37|58|M7|G8|P9|67|PE7|I/O|TT _ha|-|TIM1_ETR, DFSDM1_DATIN2, UART7_RX, OCTOSPIM_P1_IO4, FMC_D4/FMC_AD4, EVENTOUT|OPAMP2_VOUT, COMP2_INM|


70/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**









|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|J5|38|59|L7|H8|N8|68|PE8|I/O|TT _ha|-|TIM1_CH1N, DFSDM1_CKIN2, UART7_TX, OCTOSPIM_P1_IO5, FMC_D5/FMC_AD5, COMP2_OUT, EVENTOUT|OPAMP2_VINM|
|K5|39|60|K7|J8|R11|69|PE9|I/O|TT _ha|-|TIM1_CH1, DFSDM1_CKOUT, UART7_RTS/UART7_DE, OCTOSPIM_P1_IO6, FMC_D6/FMC_AD6, EVENTOUT|OPAMP2_VINP, COMP2_INP|
|-|-|61|-|-|-|70|VSS|S|-|-|-|-|
|-|-|62|-|-|-|71|VDD|S|-|-|-|-|
|G6|40|63|J7|M8|R9|72|PE10|I/O|FT _ha|-|TIM1_CH2N, DFSDM1_DATIN4, UART7_CTS, OCTOSPIM_P1_IO7, FMC_D7/FMC_AD7, EVENTOUT|COMP2_INM|
|H6|41|64|H8|N8|R12|73|PE11|I/O|FT _ha|-|TIM1_CH2, DFSDM1_CKIN4, SPI4_NSS(boot), SAI4_SD_B, OCTOSPIM_P1_NCS, FMC_D8/FMC_AD8, LCD_G3, EVENTOUT|COMP2_INP|
|J6|42|65|J8|L8|P12|74|PE12|I/O|FT _h|-|TIM1_CH3N, DFSDM1_DATIN5, SPI4_SCK(boot), SAI4_SCK_B, FMC_D9/FMC_AD9, COMP1_OUT, LCD_B4, EVENTOUT|-|
|K6|43|66|K8|K8|P13|75|PE13|I/O|FT _h|-|TIM1_CH3, DFSDM1_CKIN5, SPI4_MISO(boot), SAI4_FS_B, FMC_D10/FMC_AD10, COMP2_OUT, LCD_DE, EVENTOUT|-|
|G7|44|67|L8|J9|M12|76|PE14|I/O|FT _h|-|TIM1_CH4, SPI4_MOSI(boot), SAI4_MCLK_B, FMC_D11/FMC_AD11, LCD_CLK, EVENTOUT|-|


DS13315 Rev 5 71/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**







|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|H7|45|68|M8|N9|P14|77|PE15|I/O|FT _h|-|TIM1_BKIN, USART10_CK, FMC_D12/FMC_AD12, TIM1_BKIN_COMP12, LCD_R7, EVENTOUT|-|
|J7|46|69|M9|L9|N12|78|PB10|I/O|FT _fh|-|TIM2_CH3, LPTIM2_IN1, I2C2_SCL, SPI2_SCK/I2S2_CK, DFSDM1_DATIN7, USART3_TX(boot), OCTOSPIM_P1_NCS, OTG_HS_ULPI_D3, ETH_MII_RX_ER, LCD_G4, EVENTOUT|-|
|K7|47|70|M10|M9|P10|79|PB11|I/O|FT _f|-|TIM2_CH4, LPTIM2_ETR, I2C2_SDA, DFSDM1_CKIN7, USART3_RX(boot), OTG_HS_ULPI_D4, ETH_MII_TX_EN/ETH_RMII_T X_EN, LCD_G5, EVENTOUT|-|
|F8|48|71|H7|N10|R13|80|VCAP|S|-|-|-|-|
|-|49|-|-|-|-|81|VSS|S|-|-|-|-|
|-|-|-|-|M10|R14|82|VDDLDO|S|-|-|-|-|
|-|50|72|-|-|-|-|VDD|S|-|-|-|-|
|-|-|-|-|-|P15|-|PH6|I/O|FT _h|-|TIM12_CH1, I2C2_SMBA, SPI5_SCK, ETH_MII_RXD2, FMC_SDNE1, DCMI_D8/PSSI_D8, EVENTOUT|-|
|-|-|-|-|-|M11|-|PH7|I/O|FT _fh|-|I2C3_SCL, SPI5_MISO, ETH_MII_RXD3, FMC_SDCKE1, DCMI_D9/PSSI_D9, EVENTOUT|-|
|-|-|-|-|-|N13|-|PH8|I/O|FT _fh|-|TIM5_ETR, I2C3_SDA, FMC_D16, DCMI_HSYNC/PSSI_DE, LCD_R2, EVENTOUT|-|
|-|-|-|-|-|M14|-|PH9|I/O|FT _h|-|TIM12_CH2, I2C3_SMBA, FMC_D17, DCMI_D0/PSSI_D0, LCD_R3, EVENTOUT|-|


72/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**









|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|-|-|K9|N14|-|PH10|I/O|FT _h|-|TIM5_CH1, I2C4_SMBA, FMC_D18, DCMI_D1/PSSI_D1, LCD_R4, EVENTOUT|-|
|-|-|-|-|L10|M13|-|PH11|I/O|FT _fh|-|TIM5_CH2, I2C4_SCL, FMC_D19, DCMI_D2/PSSI_D2, LCD_R5, EVENTOUT|-|
|-|-|-|-|-|-|83|VSS|S|-|-|-|-|
|-|-|-|-|-|-|84|VDD|S|-|-|-|-|
|-|-|-|-|K10|N15|-|PH12|I/O|FT _fh|-|TIM5_CH3, I2C4_SDA, FMC_D20, DCMI_D3/PSSI_D3, LCD_R6, EVENTOUT|-|
|K8|51|73|M11|N12|M15|85|PB12|I/O|FT _h|-|TIM1_BKIN, OCTOSPIM_P1_NCLK, I2C2_SMBA, SPI2_NSS/I2S2_WS, DFSDM1_DATIN1, USART3_CK, FDCAN2_RX, OTG_HS_ULPI_D5, ETH_MII_TXD0/ETH_RMII_TX D0, OCTOSPIM_P1_IO0, TIM1_BKIN_COMP12, UART5_RX, EVENTOUT|-|
|J8|52|74|M12|L11|L15|86|PB13|I/O|FT _h|-|TIM1_CH1N, LPTIM2_OUT, OCTOSPIM_P1_IO2, SPI2_SCK/I2S2_CK, DFSDM1_CKIN1, USART3_CTS/USART3_NSS, FDCAN2_TX, OTG_HS_ULPI_D6, ETH_MII_TXD1/ETH_RMII_TX D1, SDMMC1_D0, DCMI_D2/PSSI_D2, UART5_TX, EVENTOUT|-|


DS13315 Rev 5 73/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**







|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|H10|53|75|L11|N13|K15|87|PB14|I/O|FT _h|-|TIM1_CH2N, TIM12_CH1, TIM8_CH2N, USART1_TX, SPI2_MISO/I2S2_SDI, DFSDM1_DATIN2, USART3_RTS/USART3_DE, UART4_RTS/UART4_DE, SDMMC2_D0, FMC_D10/FMC_AD10, LCD_CLK, EVENTOUT|-|
|G10|54|76|L12|M13|K14|88|PB15|I/O|FT _h|-|RTC_REFIN, TIM1_CH3N, TIM12_CH2, TIM8_CH3N, USART1_RX, SPI2_MOSI/I2S2_SDO, DFSDM1_CKIN2, UART4_CTS, SDMMC2_D1, FMC_D11/FMC_AD11, LCD_G7, EVENTOUT|-|
|K9|55|77|L9|M12|L14|89|PD8|I/O|FT _h|-|DFSDM1_CKIN3, USART3_TX(boot), SPDIFRX1_IN2, FMC_D13/FMC_AD13, EVENTOUT|-|
|J9|56|78|K9|K11|K13|90|PD9|I/O|FT _h|-|DFSDM1_DATIN3, USART3_RX(boot), FMC_D14/FMC_AD14, EVENTOUT|-|
|H9|57|79|J9|K12|L13|91|PD10|I/O|FT _h|-|DFSDM1_CKOUT, USART3_CK, FMC_D15/FMC_AD15, LCD_B3, EVENTOUT|-|
|-|-|-|-|-|-|92|VDD|S|-|-|-|-|
|-|-|-|-|-|-|93|VSS|S|-|-|-|-|
|G9|58|80|H9|J10|J13|94|PD11|I/O|FT _h|-|LPTIM2_IN2, I2C4_SMBA, USART3_CTS/USART3_NSS, OCTOSPIM_P1_IO0, SAI4_SD_A, FMC_A16/FMC_CLE, EVENTOUT|-|


74/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**










|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|K10|59|81|L10|K13|J15|95|PD12|I/O|FT _fh|-|LPTIM1_IN1, TIM4_CH1, LPTIM2_IN1, I2C4_SCL, FDCAN3_RX, USART3_RTS/USART3_DE, OCTOSPIM_P1_IO1, SAI4_FS_A, FMC_A17/FMC_ALE, DCMI_D12/PSSI_D12, EVENTOUT|-|
|J10|60|82|K10|J11|H15|96|PD13|I/O|FT _fh|-|LPTIM1_OUT, TIM4_CH2, I2C4_SDA, FDCAN3_TX, OCTOSPIM_P1_IO3, SAI4_SCK_A, UART9_RTS/UART9_DE, FMC_A18, DCMI_D13/PSSI_D13, EVENTOUT|-|
|-|-|83|-|-|-|-|VSS|S|-|-|-|-|
|-|-|84|-|-|-|-|VDD|S|-|-|-|-|
|H8|61|85|K11|J13|H14|97|PD14|I/O|FT _h|-|TIM4_CH3, UART8_CTS, UART9_RX, FMC_D0/FMC_AD0, EVENTOUT|-|
|G8|62|86|K12|J12|J12|98|PD15|I/O|FT _h|-|TIM4_CH4, UART8_RTS/UART8_DE, UART9_TX, FMC_D1/FMC_AD1, EVENTOUT|-|
|-|-|-|-|-|-|99|VDD|S|-|-|-|-|
|-|-|-|-|-|-|100|VSS|S|-|-|-|-|
|-|-|-|-|-|-|101|PJ8|I/O|FT|-|TIM1_CH3N, TIM8_CH1, UART8_TX, LCD_G1, EVENTOUT|-|
|-|-|-|-|-|-|102|PJ9|I/O|FT|-|TIM1_CH3, TIM8_CH1N, UART8_RX, LCD_G2, EVENTOUT|-|
|-|-|-|-|-|-|103|PJ10|I/O|FT|-|TIM1_CH2N, TIM8_CH2, SPI5_MOSI, LCD_G3, EVENTOUT|-|


DS13315 Rev 5 75/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**













|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|-|-|-|-|104|PJ11|I/O|FT|-|TIM1_CH2, TIM8_CH2N, SPI5_MISO, LCD_G4, EVENTOUT|-|
|-|-|-|-|-|-|105|VDD|S|-|-|-|-|
|-|-|-|-|-|-|106|VSS|S|-|-|-|-|
|-|-|-|-|-|-|107|PK0|I/O|FT|-|TIM1_CH1N, TIM8_CH3, SPI5_SCK, LCD_G5, EVENTOUT|-|
|-|-|-|-|-|-|108|PK1|I/O|FT|-|TIM1_CH1, TIM8_CH3N, SPI5_NSS, LCD_G6, EVENTOUT|-|
|-|-|-|-|-|-|109|PK2|I/O|FT|-|TIM1_BKIN, TIM8_BKIN, TIM8_BKIN_COMP12, TIM1_BKIN_COMP12, LCD_G7, EVENTOUT|-|
|-|-|87|J12|H9|G15|110|PG2|I/O|FT _h|-|TIM8_BKIN, TIM8_BKIN_COMP12, FMC_A12, TIM24_ETR, EVENTOUT|-|
|-|-|88|J11|H10|H13|111|PG3|I/O|FT _h|-|TIM8_BKIN2, TIM8_BKIN2_COMP12, FMC_A13, TIM23_ETR, EVENTOUT|-|
|-|-|-|-|-|-|112|VSS|S|-|-|-|-|
|-|-|-|-|-|-|113|VDD|S|-|-|-|-|
|-|-|89|J10|F8|G14|114|PG4|I/O|FT _h|-|TIM1_BKIN2, TIM1_BKIN2_COMP12, FMC_A14/FMC_BA0, EVENTOUT|-|
|-|-|90|H12|H11|F15|115|PG5|I/O|FT _h|-|TIM1_ETR, FMC_A15/FMC_BA1, EVENTOUT|-|
|-|-|91|H11|G9|F14|116|PG6|I/O|FT _h|-|TIM17_BKIN, OCTOSPIM_P1_NCS, FMC_NE3, DCMI_D12/PSSI_D12, LCD_R7, EVENTOUT|-|


76/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**









|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|92|H10|G10|G13|117|PG7|I/O|FT _h|-|SAI1_MCLK_A, USART6_CK, OCTOSPIM_P2_DQS, FMC_INT, DCMI_D13/PSSI_D13, LCD_CLK, EVENTOUT|-|
|-|-|93|G11|G11|G12|118|PG8|I/O|FT _h|-|TIM8_ETR, SPI6_NSS/I2S6_WS, USART6_RTS/USART6_DE, SPDIFRX1_IN3, ETH_PPS_OUT, FMC_SDCLK, LCD_G7, EVENTOUT|-|
|-|-|94|-|-|-|119|VSS|S|-|-|-|-|
|-|-|-|-|G12|E15|120|VDD50USB|S|-|-|-|-|
|F6|-|95|C11|G13|F13|121|VDD33USB|S|-|-|-|-|
|F10|63|96|G12|F9|E14|122|PC6|I/O|FT _h|-|TIM3_CH1, TIM8_CH1, DFSDM1_CKIN3, I2S2_MCK, USART6_TX, SDMMC1_D0DIR, FMC_NWAIT, SDMMC2_D6, SDMMC1_D6, DCMI_D0/PSSI_D0, LCD_HSYNC, EVENTOUT|SWPMI_IO|
|E10|64|97|F12|F10|D15|123|PC7|I/O|FT _h|-|DBTRGIO, TIM3_CH2, TIM8_CH2, DFSDM1_DATIN3, I2S3_MCK, USART6_RX, SDMMC1_D123DIR, FMC_NE1, SDMMC2_D7, SWPMI_TX, SDMMC1_D7, DCMI_D1/PSSI_D1, LCD_G6, EVENTOUT|-|
|F9|65|98|F11|F12|D14|124|PC8|I/O|FT _h|-|TRACED1, TIM3_CH3, TIM8_CH3, USART6_CK, UART5_RTS/UART5_DE, FMC_NE2/FMC_NCE, FMC_INT, SWPMI_RX, SDMMC1_D0, DCMI_D2/PSSI_D2, EVENTOUT|-|


DS13315 Rev 5 77/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**







|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|E9|66|99|E11|F11|E13|125|PC9|I/O|FT _fh|-|MCO2, TIM3_CH4, TIM8_CH4, I2C3_SDA(boot), I2S_CKIN, I2C5_SDA, UART5_CTS, OCTOSPIM_P1_IO0, LCD_G3, SWPMI_SUSPEND, SDMMC1_D1, DCMI_D3/PSSI_D3, LCD_B2, EVENTOUT|-|
|-|-|-|-|-|-|126|VDD|S|-|-|-|-|
|D9|67|100|E12|E12|B14|127|PA8|I/O|FT _fh|-|MCO1, TIM1_CH1, TIM8_BKIN2, I2C3_SCL(boot), I2C5_SCL, USART1_CK, OTG_HS_SOF, UART7_RX, TIM8_BKIN2_COMP12, LCD_B3, LCD_R6, EVENTOUT|-|
|C9|68|101|D12|E11|D13|128|PA9|I/O|FT _u|-|TIM1_CH2, LPUART1_TX, I2C3_SMBA, SPI2_SCK/I2S2_CK, I2C5_SMBA, USART1_TX(boot), ETH_TX_ER, DCMI_D0/PSSI_D0, LCD_R5, EVENTOUT|OTG_HS_VBUS|
|D10|69|102|D11|E10|C14|129|PA10|I/O|FT _u|-|TIM1_CH3, LPUART1_RX, USART1_RX(boot), OTG_HS_ID, MDIOS_MDIO, LCD_B4, DCMI_D1/PSSI_D1, LCD_B1, EVENTOUT|-|
|C10|70|103|C12|F13|C15|130|PA11|I/O|FT _u|-|TIM1_CH4, LPUART1_CTS, SPI2_NSS/I2S2_WS, UART4_RX, USART1_CTS/USART1_NSS, FDCAN1_RX, LCD_R4, EVENTOUT|OTG_HS_DM (boot)|


78/270 DS13315 Rev 5



**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**













|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|B10|71|104|B12|E13|B15|131|PA12|I/O|FT _u|-|TIM1_ETR, LPUART1_RTS/LPUART1_DE, SPI2_SCK/I2S2_CK, UART4_TX, USART1_RTS/USART1_DE, SAI4_FS_B, FDCAN1_TX, TIM1_BKIN2, LCD_R5, EVENTOUT|OTG_HS_DP (boot)|
|A10|72|105|A12|D11|B13|132|PA13(JTMS/ SWDIO)|I/O|FT|-|JTMS/SWDIO, EVENTOUT|-|
|E7|73|106|G9|D13|A14|133|VCAP|S|-|-|-|-|
|-|74|107|-|-|-|134|VSS|S|-|-|-|-|
|-|-|-|-|D12|A13|135|VDDLDO|S|-|-|-|-|
|-|75|108|-|-|-|136|VDD|S|-|-|-|-|
|-|-|-|-|B13|C13|-|PH13|I/O|FT _h|-|TIM8_CH1N, UART4_TX, FDCAN1_TX(boot), FMC_D21, LCD_G2, EVENTOUT|-|
|-|-|-|-|A13|B12|-|PH14|I/O|FT _h|-|TIM8_CH2N, UART4_RX, FDCAN1_RX(boot), FMC_D22, DCMI_D4/PSSI_D4, LCD_G3, EVENTOUT|-|
|-|-|-|-|-|D12|-|PH15|I/O|FT _h|-|TIM8_CH3N, FMC_D23, DCMI_D11/PSSI_D11, LCD_G4, EVENTOUT|-|
|-|-|-|-|-|-|137|VSS|S|-|-|-|-|
|A9|76|109|A11|B12|A12|138|PA14(JTCK/ SWCLK)|I/O|FT|-|JTCK/SWCLK, EVENTOUT|-|
|A8|77|110|A10|C11|A11|139|PA15(JTDI)|I/O|FT|-|JTDI, TIM2_CH1/TIM2_ETR, CEC, SPI1_NSS/I2S1_WS, SPI3_NSS(boot)/I2S3_WS, SPI6_NSS/I2S6_WS, UART4_RTS/UART4_DE, LCD_R3, UART7_TX, LCD_B6, EVENTOUT|-|


DS13315 Rev 5 79/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**






|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|B9|78|111|B11|A12|C12|140|PC10|I/O|FT _fh|-|DFSDM1_CKIN5, I2C5_SDA, SPI3_SCK(boot)/I2S3_CK, USART3_TX, UART4_TX, OCTOSPIM_P1_IO1, LCD_B1, SWPMI_RX, SDMMC1_D2, DCMI_D8/PSSI_D8, LCD_R2, EVENTOUT|-|
|B8|79|112|B10|B11|C11|141|PC11|I/O|FT _fh|-|DFSDM1_DATIN5, I2C5_SCL, SPI3_MISO(boot)/I2S3_SDI, USART3_RX, UART4_RX, OCTOSPIM_P1_NCS, SDMMC1_D3, DCMI_D4/PSSI_D4, LCD_B4, EVENTOUT|-|
|C8|80|113|C10|A11|B11|142|PC12|I/O|FT _h|-|TRACED3, FMC_D6/FMC_AD6, TIM15_CH1, I2C5_SMBA, SPI6_SCK/I2S6_CK, SPI3_MOSI(boot)/I2S3_SDO, USART3_CK, UART5_TX, SDMMC1_CK, DCMI_D9/PSSI_D9, LCD_R6, EVENTOUT|-|
|D8|81|114|E10|D10|C10|143|PD0|I/O|FT _h|-|DFSDM1_CKIN6, UART4_RX, FDCAN1_RX(boot), UART9_CTS, FMC_D2/FMC_AD2, LCD_B1, EVENTOUT|-|
|E8|82|115|D10|C10|A10|144|PD1|I/O|FT _h|-|DFSDM1_DATIN6, UART4_TX, FDCAN1_TX(boot), FMC_D3/FMC_AD3, EVENTOUT|-|
|B7|83|116|E9|E9|B10|145|PD2|I/O|FT _h|-|TRACED2, FMC_D7/FMC_AD7, TIM3_ETR, TIM15_BKIN, UART5_RX, LCD_B7, SDMMC1_CMD, DCMI_D11/PSSI_D11, LCD_B2, EVENTOUT|-|


80/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**













|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|C7|84|117|D9|D9|A9|146|PD3|I/O|FT _h|-|DFSDM1_CKOUT, SPI2_SCK/I2S2_CK, USART2_CTS/USART2_NSS, FMC_CLK, DCMI_D5/PSSI_D5, LCD_G7, EVENTOUT|-|
|D7|85|118|C9|C9|C9|147|PD4|I/O|FT _h|-|USART2_RTS/USART2_DE, OCTOSPIM_P1_IO4, FMC_NOE, EVENTOUT|-|
|B6|86|119|B9|A9|B9|148|PD5|I/O|FT _h|-|USART2_TX, OCTOSPIM_P1_IO5, FMC_NWE, EVENTOUT|-|
|-|-|120|-|-|-|-|VSS|S|-|-|-|-|
|-|-|121|-|-|-|-|VDD|S|-|-|-|-|
|C6|87|122|A8|B9|D9|149|PD6|I/O|FT _h|-|SAI4_D1, SAI1_D1, DFSDM1_CKIN4, DFSDM1_DATIN1, SPI3_MOSI/I2S3_SDO, SAI1_SD_A, USART2_RX, SAI4_SD_A, OCTOSPIM_P1_IO6, SDMMC2_CK, FMC_NWAIT, DCMI_D10/PSSI_D10, LCD_B2, EVENTOUT|-|
|D6|88|123|A9|D8|B8|150|PD7|I/O|FT _h|-|DFSDM1_DATIN4, SPI1_MOSI/I2S1_SDO, DFSDM1_CKIN1, USART2_CK, SPDIFRX1_IN1, OCTOSPIM_P1_IO7, SDMMC2_CMD, FMC_NE1, EVENTOUT|-|
|-|-|-|-|-|-|151|VSS|S|-|-|-|-|
|-|-|-|-|-|-|152|VDD|S|-|-|-|-|
|-|-|124|E8|C8|A8|153|PG9|I/O|FT _h|-|FDCAN3_TX, SPI1_MISO/I2S1_SDI, USART6_RX, SPDIFRX1_IN4, OCTOSPIM_P1_IO6, SAI4_FS_B, SDMMC2_D0, FMC_NE2/FMC_NCE, DCMI_VSYNC/PSSI_RDY, EVENTOUT|-|


DS13315 Rev 5 81/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**






|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|125|D8|A8|C8|154|PG10|I/O|FT _h|-|FDCAN3_RX, OCTOSPIM_P2_IO6, SPI1_NSS/I2S1_WS, LCD_G3, SAI4_SD_B, SDMMC2_D1, FMC_NE3, DCMI_D2/PSSI_D2, LCD_B2, EVENTOUT|-|
|-|-|126|C8|B8|A7|155|PG11|I/O|FT _h|-|LPTIM1_IN2, USART10_RX, SPI1_SCK/I2S1_CK, SPDIFRX1_IN1, OCTOSPIM_P2_IO7, SDMMC2_D2, ETH_MII_TX_EN/ETH_RMII_T X_EN, DCMI_D3/PSSI_D3, LCD_B3, EVENTOUT|-|
|-|-|127|B8|E8|D8|156|PG12|I/O|FT _h|-|LPTIM1_IN1, OCTOSPIM_P2_NCS, USART10_TX, SPI6_MISO/I2S6_SDI, USART6_RTS/USART6_DE, SPDIFRX1_IN2, LCD_B4, SDMMC2_D3, ETH_MII_TXD1/ETH_RMII_TX D1, FMC_NE4, TIM23_CH1, LCD_B1, EVENTOUT|-|
|-|-|128|D7|D7|B7|157|PG13|I/O|FT _h|-|TRACED0, LPTIM1_OUT, USART10_CTS/USART10_NS S, SPI6_SCK/I2S6_CK, USART6_CTS/USART6_NSS, SDMMC2_D6, ETH_MII_TXD0/ETH_RMII_TX D0, FMC_A24, TIM23_CH2, LCD_R0, EVENTOUT|-|
|-|-|129|C7|C7|C7|158|PG14|I/O|FT _h|-|TRACED1, LPTIM1_ETR, USART10_RTS/USART10_DE, SPI6_MOSI/I2S6_SDO, USART6_TX, OCTOSPIM_P1_IO7, SDMMC2_D7, ETH_MII_TXD1/ETH_RMII_TX D1, FMC_A25, TIM23_CH3, LCD_B0, EVENTOUT|-|
|-|-|130|-|-|-|159|VSS|S|-|-|-|-|


82/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**







|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|131|-|-|-|160|VDD|S|-|-|-|-|
|-|-|132|B7|E7|D7|161|PG15|I/O|FT _h|-|USART6_CTS/USART6_NSS, OCTOSPIM_P2_DQS, USART10_CK, FMC_NCAS, DCMI_D13/PSSI_D13, EVENTOUT|-|
|A7|89|133|A7|F7|A6|162|PB3(JTDO/TRAC ESWO)|I/O|FT _h|-|JTDO/TRACESWO, TIM2_CH2, SPI1_SCK/I2S1_CK, SPI3_SCK/I2S3_CK, SPI6_SCK/I2S6_CK, SDMMC2_D2, CRS_SYNC, UART7_RX, TIM24_ETR, EVENTOUT|-|
|A6|90|134|A6|B6|B6|163|PB4(NJTRST)|I/O|FT _h|-|NJTRST, TIM16_BKIN, TIM3_CH1, SPI1_MISO/I2S1_SDI, SPI3_MISO/I2S3_SDI, SPI2_NSS/I2S2_WS, SPI6_MISO/I2S6_SDI, SDMMC2_D3, UART7_TX, EVENTOUT|-|
|C5|91|135|B6|C6|C6|164|PB5|I/O|FT _h|-|TIM17_BKIN, TIM3_CH2, LCD_B5, I2C1_SMBA, SPI1_MOSI/I2S1_SDO, I2C4_SMBA, SPI3_MOSI/I2S3_SDO, SPI6_MOSI/I2S6_SDO, FDCAN2_RX, OTG_HS_ULPI_D7, ETH_PPS_OUT, FMC_SDCKE1, DCMI_D10/PSSI_D10, UART5_RX, EVENTOUT|-|
|B5|92|136|C6|A5|A5|165|PB6|I/O|FT _fh|-|TIM16_CH1N, TIM4_CH1, I2C1_SCL(boot), CEC, I2C4_SCL, USART1_TX, LPUART1_TX, FDCAN2_TX, OCTOSPIM_P1_NCS, DFSDM1_DATIN5, FMC_SDNE1, DCMI_D5/PSSI_D5, UART5_TX, EVENTOUT|-|


DS13315 Rev 5 83/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**










|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|A5|93|137|D6|D6|B5|166|PB7|I/O|FT _fa|-|TIM17_CH1N, TIM4_CH2, I2C1_SDA, I2C4_SDA, USART1_RX, LPUART1_RX, DFSDM1_CKIN5, FMC_NL, DCMI_VSYNC/PSSI_RDY, EVENTOUT|PVD_IN|
|D5|94|138|D5|E6|C5|167|BOOT0|I|B|-|-|VPP|
|B4|95|139|C5|B5|A2|168|PB8|I/O|FT _fh|-|TIM16_CH1, TIM4_CH3, DFSDM1_CKIN7, I2C1_SCL, I2C4_SCL, SDMMC1_CKIN, UART4_RX, FDCAN1_RX, SDMMC2_D4, ETH_MII_TXD3, SDMMC1_D4, DCMI_D6/PSSI_D6, LCD_B6, EVENTOUT|-|
|A4|96|140|B5|C5|B3|169|PB9|I/O|FT _fh|-|TIM17_CH1, TIM4_CH4, DFSDM1_DATIN7, I2C1_SDA(boot), SPI2_NSS/I2S2_WS, I2C4_SDA, SDMMC1_CDIR, UART4_TX, FDCAN1_TX, SDMMC2_D5, I2C4_SMBA, SDMMC1_D5, DCMI_D7/PSSI_D7, LCD_B7, EVENTOUT|-|
|D4|97|141|A5|D5|B4|170|PE0|I/O|FT _h|-|LPTIM1_ETR, TIM4_ETR, LPTIM2_ETR, UART8_RX, SAI4_MCLK_A, FMC_NBL0, DCMI_D2/PSSI_D2, LCD_R0, EVENTOUT|-|
|C4|98|142|A4|D4|C4|171|PE1|I/O|FT _h|-|LPTIM1_IN2, UART8_TX, FMC_NBL1, DCMI_D3/PSSI_D3, LCD_R6, EVENTOUT|-|
|-|-|-|-|A4|A4|172|VCAP|S|-|-|-|-|
|-|99|-|-|-|-|173|VSS|S|-|-|-|-|
|F7|-|143|E5|C4|D4|174|PDR_ON|S|-|-|-|-|
|-|-|-|-|B4|A3|175|VDDLDO|S|-|-|-|-|
|-|100|144|-|-|-|-|VDD|S|-|-|-|-|


84/270 DS13315 Rev 5

**STM32H730xB** **Pinouts, pin descriptions and alternate functions**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**




|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|-|-|-|-|176|VDD|S|-|-|-|-|
|C2|-|-|D2|B3|A1|-|VSS|S|-|-|-|-|
|E6|-|-|E6|B7|A15|-|VSS|S|-|-|-|-|
|J1|-|-|E7|B10|C2|-|VSS|S|-|-|-|-|
|E4|-|-|G4|C12|D10|-|VSS|S|-|-|-|-|
|E5|-|-|G8|D2|D6|-|VSS|S|-|-|-|-|
|-|-|-|G10|G2|E1|-|VSS|S|-|-|-|-|
|-|-|-|H5|H12|F10|-|VSS|S|-|-|-|-|
|-|-|-|H6|L12|F12|-|VSS|S|-|-|-|-|
|-|-|-|-|M2|F6|-|VSS|S|-|-|-|-|
|-|-|-|-|M4|F7|-|VSS|S|-|-|-|-|
|-|-|-|-|M7|F8|-|VSS|S|-|-|-|-|
|-|-|-|-|M11|F9|-|VSS|S|-|-|-|-|
|-|-|-|-|-|G10|-|VSS|S|-|-|-|-|
|-|-|-|-|-|G6|-|VSS|S|-|-|-|-|
|-|-|-|-|-|G7|-|VSS|S|-|-|-|-|
|-|-|-|-|-|G8|-|VSS|S|-|-|-|-|
|-|-|-|-|-|G9|-|VSS|S|-|-|-|-|
|-|-|-|-|-|H10|-|VSS|S|-|-|-|-|
|-|-|-|-|-|H6|-|VSS|S|-|-|-|-|
|-|-|-|-|-|H7|-|VSS|S|-|-|-|-|
|-|-|-|-|-|H8|-|VSS|S|-|-|-|-|
|-|-|-|-|-|H9|-|VSS|S|-|-|-|-|
|-|-|-|-|-|J10|-|VSS|S|-|-|-|-|
|-|-|-|-|-|J14|-|VSS|S|-|-|-|-|
|-|-|-|-|-|J6|-|VSS|S|-|-|-|-|
|-|-|-|-|-|J7|-|VSS|S|-|-|-|-|
|-|-|-|-|-|J8|-|VSS|S|-|-|-|-|
|-|-|-|-|-|J9|-|VSS|S|-|-|-|-|
|-|-|-|-|-|K10|-|VSS|S|-|-|-|-|


DS13315 Rev 5 85/270


101

**Pinouts, pin descriptions and alternate functions** **STM32H730xB**

**Table 7. STM32H730xB** **p** **in and ball descri** **p** **tions** **(** **continued** **)**




|Pin Number|Col2|Col3|Col4|Col5|Col6|Col7|Pin name (function after reset)|Pin type|I/O structure|Notes|Alternate functions|Additional functions|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TFBGA100|LQFP100|LQFP144|UFBGA144|UFBGA169|UFBGA176+25|LQFP176|||||||
|-|-|-|-|-|K12|-|VSS|S|-|-|-|-|
|-|-|-|-|-|K2|-|VSS|S|-|-|-|-|
|-|-|-|-|-|K6|-|VSS|S|-|-|-|-|
|-|-|-|-|-|K7|-|VSS|S|-|-|-|-|
|-|-|-|-|-|K8|-|VSS|S|-|-|-|-|
|-|-|-|-|-|K9|-|VSS|S|-|-|-|-|
|-|-|-|-|-|M10|-|VSS|S|-|-|-|-|
|-|-|-|-|-|M6|-|VSS|S|-|-|-|-|
|-|-|-|-|-|R1|-|VSS|S|-|-|-|-|
|-|-|-|-|-|R15|-|VSS|S|-|-|-|-|
|D2|-|-|D3|A3|D5|-|VDD|S|-|-|-|-|
|F5|-|-|F4|A6|D11|-|VDD|S|-|-|-|-|
|K1|-|-|F5|A7|E4|-|VDD|S|-|-|-|-|
|F4|-|-|F6|A10|E12|-|VDD|S|-|-|-|-|
|-|-|-|F7|C13|G4|-|VDD|S|-|-|-|-|
|-|-|-|F8|D1|H12|-|VDD|S|-|-|-|-|
|-|-|-|F9|G1|K4|-|VDD|S|-|-|-|-|
|-|-|-|F10|H13|L12|-|VDD|S|-|-|-|-|
|-|-|-|G5|L13|M5|-|VDD|S|-|-|-|-|
|-|-|-|G6|M1|M9|-|VDD|S|-|-|-|-|
|-|-|-|G7|N4|-|-|VDD|S|-|-|-|-|
|-|-|-|-|N7|-|-|VDD|S|-|-|-|-|
|-|-|-|-|N11|-|-|VDD|S|-|-|-|-|


1. Pxy_C and Pxy pins/balls are two separate pads (analog switch open). The analog switch is configured through a SYSCFG
register. Refer to the product reference manual for a detailed description of the switch configuration bits.

2. There is a direct path between Pxy_C and Pxy pins/balls, through an analog switch. Pxy alternate functions are available
on Pxy_C when the analog switch is closed. The analog switch is configured through a SYSCFG register. Refer to the
product reference manual for a detailed description of the switch configuration bits.

3. Pxy_C pins have specific electrical limitations described in *Section 6: Electrical characteristics* .

86/270 DS13315 Rev 5

**Table 8. STM32H730xB** **p** **in alternate functions**














































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Port A|PA0|-|TIM2_ CH1/TIM 2_ETR|TIM5_ CH1|TIM8_ ETR|TIM15_ BKIN|SPI6_NSS /I2S6_WS|-|USART2_ CTS/ USART2_ NSS|UART4_ TX|SDMMC2_ CMD|SAI4_SD_ B|ETH_MII_ CRS|FMC_A19|-|-|EVENT OUT|
||PA1|-|TIM2_CH 2|TIM5_ CH2|LPTIM3_ OUT|TIM15_CH1 N|-|-|USART2_ RTS/ USART2_ DE|UART4_ RX|OCTOSPIM _P1_IO3|SAI4_ MCLK_B|ETH_MII_ RX_CLK/ ETH_RMII_ REF_CLK|OCTOSPI M_P1_ DQS|-|LCD_R 2|EVENT OUT|
||PA2|-|TIM2_CH 3|TIM5_ CH3|LPTIM4_ OUT|TIM15_CH1|-|OCTOSPI M_P1_IO0|USART2_ TX|SAI4_ SCK_B|-|-|ETH_MDIO|MDIOS_ MDIO|-|LCD_R 1|EVENT OUT|
||PA3|-|TIM2_CH 4|TIM5_ CH4|LPTIM5_ OUT|TIM15_CH2|I2S6_MCK|OCTOSPI M_P1_IO2|USART2_ RX|-|LCD_B2|OTG_HS_ ULPI_D0|ETH_MII_ COL|OCTOSPI M_P1_ CLK|-|LCD_B 5|EVENT OUT|
||PA4|D1PW REN|-|TIM5_ ETR|-|-|SPI1_NSS /I2S1_WS|SPI3_NSS/ I2S3_WS|USART2_ CK|SPI6_NS S/I2S6_ WS|-|-|-|FMC_D8/ FMC_AD 8|DCMI_ HSYNC /PSSI_ DE|LCD_V SYNC|EVENT OUT|
||PA5|D2PW REN|TIM2_CH 1/TIM2_ ETR|-|TIM8_ CH1N|-|SPI1_SCK /I2S1_CK|-|-|SPI6_SC K/I2S6_ CK|-|OTG_HS_ ULPI_CK|-|FMC_D9/ FMC_AD 9|PSSI_ D14|LCD_R 4|EVENT OUT|
||PA6|-|TIM1_ BKIN|TIM3_C H1|TIM8_ BKIN|-|SPI1_ MISO/I2S 1_SDI|OCTOSPI M_P1_IO3|-|SPI6_MIS O/I2S6_S DI|TIM13_CH 1|TIM8_BKIN _COMP12|MDIOS_ MDC|TIM1_ BKIN_ COMP12|DCMI_ PIXCL K/PSSI _PDCK|LCD_G 2|EVENT OUT|
||PA7|-|TIM1_CH 1N|TIM3_ CH2|TIM8_CH 1N|-|SPI1_ MOSI/I2S 1_SDO|-|-|SPI6_ MOSI/I2S 6_SDO|TIM14_CH 1|OCTOSPI M_P1_IO2|ETH_MII_ RX_DV/ETH _RMII_CRS _DV|FMC_SD NWE|-|LCD_V SYNC|EVENT OUT|
||PA8|MCO1|TIM1_CH 1|-|TIM8_ BKIN2|I2C3_SCL|-|I2C5_SCL|USART1_ CK|-|-|OTG_HS_ SOF|UART7_RX|TIM8_ BKIN2_ COMP12|LCD_B 3|LCD_R 6|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**




























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Port A|PA9|-|TIM1_CH 2|-|LPUART1 _TX|I2C3_ SMBA|SPI2_SCK /I2S2_CK|I2C5_ SMBA|USART1_ TX|-|-|-|ETH_TX_ER|-|DCMI_ D0/ PSSI_ D0|LCD_R 5|EVENT OUT|
||PA10|-|TIM1_CH 3|-|LPUART1 _RX|-|-|-|USART1_ RX|-|-|OTG_HS_ ID|MDIOS_ MDIO|LCD_B4|DCMI_ D1/ PSSI_ D1|LCD_B 1|EVENT OUT|
||PA11|-|TIM1_CH 4|-|LPUART1 _CTS|-|SPI2_NSS /I2S2_WS|UART4_RX|USART1_ CTS/ USART1_ NSS|-|FDCAN1_ RX|-|-|-|-|LCD_R 4|EVENT OUT|
||PA12|-|TIM1_ ETR|-|LPUART1 _RTS/ LPUART1 _DE|-|SPI2_SCK /I2S2_CK|UART4_TX|USART1_ RTS/ USART1_ DE|SAI4_FS_ B|FDCAN1_ TX|-|-|TIM1_ BKIN2|-|LCD_R 5|EVENT OUT|
||PA13|JTMS/ SWDI O|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|
||PA14|JTCK/ SWCL K|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|
||PA15|JTDI|TIM2_CH 1/TIM2_ ETR|-|-|CEC|SPI1_NSS /I2S1_WS|SPI3_NSS/ I2S3_WS|SPI6_NS S/I2S6_W S|UART4_R TS/UART 4_DE|LCD_R3|-|UART7_TX|-|-|LCD_B 6|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**






































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Port B|PB0|-|TIM1_ CH2N|TIM3_ CH3|TIM8_ CH2N|OCTOSPIM _P1_IO1|-|DFSDM1_ CKOUT|-|UART4_ CTS|LCD_R3|OTG_HS_ ULPI_D1|ETH_MII_ RXD2|-|-|LCD_G 1|EVENT OUT|
||PB1|-|TIM1_ CH3N|TIM3_ CH4|TIM8_CH 3N|OCTOSPIM _P1_IO0|-|DFSDM1_ DATIN1|-|-|LCD_R6|OTG_HS_ ULPI_D2|ETH_MII_ RXD3|-|-|LCD_G 0|EVENT OUT|
||PB2|RTC_ OUT|SAI4_D1|SAI1_D1|-|DFSDM1_ CKIN1|-|SAI1_SD_ A|SPI3_ MOSI/I2S 3_SDO|SAI4_SD_ A|OCTOSPIM _P1_CLK|OCTOSPI M_P1_ DQS|ETH_TX_ER|-|TIM23_ ETR|-|EVENT OUT|
||PB3|JTDO/ TRAC ESWO|TIM2_CH 2|-|-|-|SPI1_SCK /I2S1_CK|SPI3_SCK/ I2S3_CK|-|SPI6_ SCK/I2S6 _CK|SDMMC2_ D2|CRS_ SYNC|UART7_RX|-|-|TIM24_ ETR|EVENT OUT|
||PB4|NJT RST|TIM16_ BKIN|TIM3_ CH1|-|-|SPI1_ MISO/I2S 1_SDI|SPI3_ MISO/I2S3 _SDI|SPI2_ NSS/I2S2 _WS|SPI6_ MISO/I2S 6_SDI|SDMMC2_ D3|-|UART7_TX|-|-|-|EVENT OUT|
||PB5|-|TIM17_ BKIN|TIM3_ CH2|LCD_B5|I2C1_ SMBA|SPI1_ MOSI/I2S 1_SDO|I2C4_SMB A|SPI3_ MOSI/I2S 3_SDO|SPI6_ MOSI/I2S 6_SDO|FDCAN2_ RX|OTG_HS_ ULPI_D7|ETH_PPS_ OUT|FMC_SD CKE1|DCMI_ D10/ PSSI_ D10|UART5 _RX|EVENT OUT|
||PB6|-|TIM16_ CH1N|TIM4_ CH1|-|I2C1_SCL|CEC|I2C4_SCL|USART1_ TX|LPUART1 _TX|FDCAN2_ TX|OCTOSPI M_P1_ NCS|DFSDM1_ DATIN5|FMC_SD NE1|DCMI_ D5/ PSSI_ D5|UART5 _TX|EVENT OUT|
||PB7|-|TIM17_ CH1N|TIM4_ CH2|-|I2C1_SDA|-|I2C4_SDA|USART1_ RX|LPUART1 _RX|-|-|DFSDM1_ CKIN5|FMC_NL|DCMI_ VSYNC /PSSI_ RDY|-|EVENT OUT|
||PB8|-|TIM16_ CH1|TIM4_ CH3|DFSDM1_ CKIN7|I2C1_SCL|-|I2C4_SCL|SDMMC1 _CKIN|UART4_ RX|FDCAN1_ RX|SDMMC2_ D4|ETH_MII_ TXD3|SDMMC1 _D4|DCMI_ D6/ PSSI_ D6|LCD_B 6|EVENT OUT|
||PB9|-|TIM17_ CH1|TIM4_ CH4|DFSDM1_ DATIN7|I2C1_SDA|SPI2_NSS /I2S2_WS|I2C4_SDA|SDMMC1 _CDIR|UART4_ TX|FDCAN1_ TX|SDMMC2_ D5|I2C4_SMBA|SDMMC1 _D5|DCMI_ D7/ PSSI_ D7|LCD_B 7|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**




































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|P r o t B|PB10|-|TIM2_ CH3|-|LPTIM2_ IN1|I2C2_SCL|SPI2_SCK /I2S2_CK|DFSDM1_ DATIN7|USART3_ TX|-|OCTOSPIM _P1_NCS|OTG_HS_ ULPI_D3|ETH_MII_ RX_ER|-|-|LCD_G 4|EVENT OUT|
||PB11|-|TIM2_ CH4|-|LPTIM2_ ETR|I2C2_SDA|-|DFSDM1_ CKIN7|USART3_ RX|-|-|OTG_HS_ ULPI_D4|ETH_MII_TX _EN/ETH_ RMII_TX_ EN|-|-|LCD_G 5|EVENT OUT|
||PB12|-|TIM1_ BKIN|-|OCTOSPI M_P1_ NCLK|I2C2_ SMBA|SPI2_NSS /I2S2_WS|DFSDM1_ DATIN1|USART3_ CK|-|FDCAN2_ RX|OTG_HS_ ULPI_D5|ETH_MII_TX D0/ETH_ RMII_TXD0|OCTOSPI M_P1_IO 0|TIM1_ BKIN_ COMP 12|UART5 _RX|EVENT OUT|
||PB13|-|TIM1_ CH1N|-|LPTIM2_ OUT|OCTOSPIM _P1_IO2|SPI2_SCK /I2S2_CK|DFSDM1_ CKIN1|USART3_ CTS/ USART3_ NSS|-|FDCAN2_ TX|OTG_HS_ ULPI_D6|ETH_MII_TX D1/ETH_ RMII_TXD1|SDMMC1 _D0|DCMI_ D2/P SSI_D2|UART5 _TX|EVENT OUT|
||PB14|-|TIM1_ CH2N|TIM12_ CH1|TIM8_ CH2N|USART1_ TX|SPI2_ MISO/ I2S2_SDI|DFSDM1_ DATIN2|USART3_ RTS/ USART3_ DE|UART4_ RTS /UART4_ DE|SDMMC2_ D0|-|-|FMC_D1 0/FMC_ AD10|-|LCD_ CLK|EVENT OUT|
||PB15|RTC_ REFIN|TIM1_ CH3N|TIM12_ CH2|TIM8_ CH3N|USART1_ RX|SPI2_MO SI/I2S2_ SDO|DFSDM1_ CKIN2|-|UART4_ CTS|SDMMC2_ D1|-|-|FMC_D11 /FMC_AD 11|-|LCD_G 7|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**






































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot C|PC0|-|FMC_D1 2/FMC_ AD12|-|DFSDM1_ CKIN0|-|-|DFSDM1_ DATIN4|-|SAI4_FS_ B|FMC_A25|OTG_HS_ ULPI_STP|LCD_G2|FMC_ SDNWE|-|LCD_R 5|EVENT OUT|
||PC1|TRA CED0|SAI4_D1|-|DFSDM1_ DATIN0|DFSDM1_C KIN4|SPI2_MO SI/I2S2_S DO|SAI1_SD_ A|-|SAI4_SD_ A|SDMMC2_ CK|OCTOSPI M_P1_IO4|ETH_MDC|MDIOS_ MDC|-|LCD_G 5|EVENT OUT|
||PC2|PWR_ DEEP SLEEP|-|-|DFSDM1_ CKIN1|OCTOSPIM _P1_IO5|SPI2_MIS O/I2S2_S DI|DFSDM1_ CKOUT|-|-|OCTOSPIM _P1_IO2|OTG_HS_ ULPI_DIR|ETH_MII_ TXD2|FMC_SD NE0|-|-|EVENT OUT|
||PC3|PWR_ SLEEP|-|-|DFSDM1_ DATIN1|OCTOSPIM _P1_IO6|SPI2_MO SI/I2S2_S DO|-|-|-|OCTOSPIM _P1_IO0|OTG_HS_ ULPI_NXT|ETH_MII_ TX_CLK|FMC_SD CKE0|-|-|EVENT OUT|
||PC4|PWR_ DEEP SLEEP|FMC_A2 2|-|DFSDM1_ CKIN2|-|I2S1_MCK|-|-|-|SPDIFRX1 _IN3|SDMMC2_ CKIN|ETH_MII_ RXD0/ETH_ RMII_RXD0|FMC_SD NE0|-|LCD_R 7|EVENT OUT|
||PC5|PWR_ SLEEP|SAI4_D3|SAI1_D3|DFSDM1_ DATIN2|PSSI_D15|-|-|-|-|SPDIFRX1 _IN4|OCTOSPI M_P1_ DQS|ETH_MII_ RXD1/ETH_ RMII_RXD1|FMC_SD CKE0|COMP 1_OUT|LCD_ DE|EVENT OUT|
||PC6|-|-|TIM3_ CH1|TIM8_CH 1|DFSDM1_ CKIN3|I2S2_MCK|-|USART6_ TX|SDMMC1 _D0DIR|FMC_ NWAIT|SDMMC2_ D6|-|SDMMC1 _D6|DCMI_ D0/ PSSI_ D0|LCD_ HSYNC|EVENT OUT|
||PC7|DBTR GIO|-|TIM3_ CH2|TIM8_CH 2|DFSDM1_ DATIN3|-|I2S3_MCK|USART6_ RX|SDMMC1 _D123DIR|FMC_NE1|SDMMC2_ D7|SWPMI_TX|SDMMC1 _D7|DCMI_ D1/PS SI_D1|LCD_G 6|EVENT OUT|
||PC8|TRA CED1|-|TIM3_ CH3|TIM8_CH 3|-|-|-|USART6_ CK|UART5_ RTS/ UART5_ DE|FMC_NE2/ FMC_NCE|FMC_INT|SWPMI_RX|SDMMC1 _D0|DCMI_ D2/PS SI_D2|-|EVENT OUT|
||PC9|MCO2|-|TIM3_C H4|TIM8_CH 4|I2C3_SDA|I2S_CKIN|I2C5_SDA|-|UART5_ CTS|OCTOSPIM _P1_IO0|LCD_G3|SWPMI_SU SPEND|SDMMC1 _D1|DCMI_ D3/PS SI_D3|LCD_B 2|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**

























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot C|PC10|-|-|-|DFSDM1_ CKIN5|I2C5_SDA|-|SPI3_SCK/ I2S3_CK|USART3_ TX|UART4_ TX|OCTOSPIM _P1_IO1|LCD_B1|SWPMI_RX|SDMMC1 _D2|DCMI_ D8/ PSSI_ D8|LCD_R 2|EVENT OUT|
||PC11|-|-|-|DFSDM1_ DATIN5|I2C5_SCL|-|SPI3_ MISO/I2S3 _SDI|USART3_ RX|UART4_ RX|OCTOSPIM _P1_NCS|-|-|SDMMC1 _D3|DCMI_ D4/ PSSI_ D4|LCD_B 4|EVENT OUT|
||PC12|TRAC ED3|FMC_D6/ FMC_AD 6|TIM15_ CH1|-|I2C5_SMB A|SPI6_SCK /I2S6_CK|SPI3_ MOSI/I2S3 _SDO|USART3_ CK|UART5_ TX|-|-|-|SDMMC1 _CK|DCMI_ D9/ PSSI_ D9|LCD_R 6|EVENT OUT|
||PC13|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|
||PC14|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|
||PC15|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**




































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Port D|PD0|-|-|-|DFSDM1_ CKIN6|-|-|-|-|UART4_ RX|FDCAN1_ RX|-|UART9_CTS|FMC_D2/ FMC_AD 2|-|LCD_B 1|EVENT OUT|
||PD1|-|-|-|DFSDM1_ DATIN6|-|-|-|-|UART4_ TX|FDCAN1_ TX|-|-|FMC_D3/ FMC_AD 3|-|-|EVENT OUT|
||PD2|TRAC ED2|FMC_D7/ FMC_AD 7|TIM3_ ETR|-|TIM15_ BKIN|-|-|-|UART5_ RX|LCD_B7|-|-|SDMMC1 _CMD|DCMI_ D11/ PSSI_ D11|LCD_B 2|EVENT OUT|
||PD3|-|-|-|DFSDM1_ CKOUT|-|SPI2_SCK /I2S2_CK|-|USART2_ CTS/ USART2_ NSS|-|-|-|-|FMC_ CLK|DCMI_ D5/ PSSI_ D5|LCD_G 7|EVENT OUT|
||PD4|-|-|-|-|-|-|-|USART2_ RTS/ USART2_ DE|-|-|OCTOSPI M_P1_IO4|-|FMC_ NOE|-|-|EVENT OUT|
||PD5|-|-|-|-|-|-|-|USART2_ TX|-|-|OCTOSPI M_P1_IO5|-|FMC_NW E|-|-|EVENT OUT|
||PD6|-|SAI4_D1|SAI1_D1|DFSDM1_ CKIN4|DFSDM1_ DATIN1|SPI3_ MOSI/I2S 3_SDO|SAI1_SD_ A|USART2_ RX|SAI4_SD_ A|-|OCTOSPI M_P1_IO6|SDMMC2_ CK|FMC_ NWAIT|DCMI_ D10/ PSSI_ D10|LCD_B 2|EVENT OUT|
||PD7|-|-|-|DFSDM1_ DATIN4|-|SPI1_ MOSI/I2S 1_SDO|DFSDM1_ CKIN1|USART2_ CK|-|SPDIFRX1 _IN1|OCTOSPI M_P1_IO7|SDMMC2_ CMD|FMC_NE 1|-|-|EVENT OUT|
||PD8|-|-|-|DFSDM1_ CKIN3|-|-|-|USART3_ TX|-|SPDIFRX1 _IN2|-|-|FMC_D1 3/FMC_A D13|-|-|EVENT OUT|
||PD9|-|-|-|DFSDM1_ DATIN3|-|-|-|USART3_ RX|-|-|-|-|FMC_D1 4/FMC_ AD14|-|-|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**





















|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot D|PD10|-|-|-|DFSDM1_ CKOUT|-|-|-|USART3_ CK|-|-|-|-|FMC_D1 5/FMC_A D15|-|LCD_B 3|EVENT OUT|
||PD11|-|-|-|LPTIM2_I N2|I2C4_SMB A|-|-|USART3_ CTS/USA RT3_NSS|-|OCTOSPIM _P1_IO0|SAI4_SD_ A|-|FMC_A16 /FMC_CL E|-|-|EVENT OUT|
||PD12|-|LPTIM1_ IN1|TIM4_C H1|LPTIM2_I N1|I2C4_SCL|FDCAN3_ RX|-|USART3_ RTS/USA RT3_DE|-|OCTOSPIM _P1_IO1|SAI4_FS_ A|-|FMC_A17 /FMC_AL E|DCMI_ D12/PS SI_D12|-|EVENT OUT|
||PD13|-|LPTIM1_ OUT|TIM4_C H2|-|I2C4_SDA|FDCAN3_ TX|-|-|-|OCTOSPIM _P1_IO3|SAI4_SCK _A|UART9_RTS /UART9_DE|FMC_A18|DCMI_ D13/PS SI_D13|-|EVENT OUT|
||PD14|-|-|TIM4_C H3|-|-|-|-|-|UART8_C TS|-|-|UART9_RX|FMC_D0/ FMC_AD 0|-|-|EVENT OUT|
||PD15|-|-|TIM4_C H4|-|-|-|-|-|UART8_R TS/UART 8_DE|-|-|UART9_TX|FMC_D1/ FMC_AD 1|-|-|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**

























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Port E|PE0|-|LPTIM1_ ETR|TIM4_E TR|-|LPTIM2_ET R|-|-|-|UART8_R X|-|SAI4_MCL K_A|-|FMC_NB L0|DCMI_ D2/PS SI_D2|LCD_R 0|EVENT OUT|
||PE1|-|LPTIM1_I N2|-|-|-|-|-|-|UART8_T X|-|-|-|FMC_NB L1|DCMI_ D3/PS SI_D3|LCD_R 6|EVENT OUT|
||PE2|TRAC ECLK|-|SAI1_C K1|-|USART10_ RX|SPI4_SCK|SAI1_MCL K_A|-|SAI4_MC LK_A|OCTOSPIM _P1_IO2|SAI4_CK1|ETH_MII_TX D3|FMC_A23|-|-|EVENT OUT|
||PE3|TRAC ED0|-|-|-|TIM15_BKI N|-|SAI1_SD_ B|-|SAI4_SD_ B|-|-|USART10_T X|FMC_A19|-|-|EVENT OUT|
||PE4|TRAC ED1|-|SAI1_D2|DFSDM1_ DATIN3|TIM15_CH1 N|SPI4_NSS|SAI1_FS_A|-|SAI4_FS_ A|-|SAI4_D2|-|FMC_A20|DCMI_ D4/PS SI_D4|LCD_B 0|EVENT OUT|
||PE5|TRAC ED2|-|SAI1_C K2|DFSDM1_ CKIN3|TIM15_CH1|SPI4_MIS O|SAI1_SCK _A|-|SAI4_SC K_A|-|SAI4_CK2|-|FMC_A21|DCMI_ D6/PS SI_D6|LCD_G 0|EVENT OUT|
||PE6|TRAC ED3|TIM1_BKI N2|SAI1_D1|-|TIM15_CH2|SPI4_MO SI|SAI1_SD_ A|-|SAI4_SD_ A|SAI4_D1|SAI4_MCL K_B|TIM1_BKIN2 _COMP12|FMC_A22|DCMI_ D7/PS SI_D7|LCD_G 1|EVENT OUT|
||PE7|-|TIM1_ET R|-|DFSDM1_ DATIN2|-|-|-|UART7_R X|-|-|OCTOSPI M_P1_IO4|-|FMC_D4/ FMC_AD 4|-|-|EVENT OUT|
||PE8|-|TIM1_CH 1N|-|DFSDM1_ CKIN2|-|-|-|UART7_T X|-|-|OCTOSPI M_P1_IO5|-|FMC_D5/ FMC_AD 5|COMP 2_OUT|-|EVENT OUT|
||PE9|-|TIM1_CH 1|-|DFSDM1_ CKOUT|-|-|-|UART7_R TS/UART 7_DE|-|-|OCTOSPI M_P1_IO6|-|FMC_D6/ FMC_AD 6|-|-|EVENT OUT|
||PE10|-|TIM1_CH 2N|-|DFSDM1_ DATIN4|-|-|-|UART7_C TS|-|-|OCTOSPI M_P1_IO7|-|FMC_D7/ FMC_AD 7|-|-|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**


























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot E|PE11|-|TIM1_CH 2|-|DFSDM1_ CKIN4|-|SPI4_NSS|-|-|-|-|SAI4_SD_ B|OCTOSPIM _P1_NCS|FMC_D8/ FMC_AD 8|-|LCD_G 3|EVENT OUT|
||PE12|-|TIM1_CH 3N|-|DFSDM1_ DATIN5|-|SPI4_SCK|-|-|-|-|SAI4_SCK _B|-|FMC_D9/ FMC_AD 9|COMP 1_OUT|LCD_B 4|EVENT OUT|
||PE13|-|TIM1_CH 3|-|DFSDM1_ CKIN5|-|SPI4_MIS O|-|-|-|-|SAI4_FS_ B|-|FMC_D1 0/FMC_A D10|COMP 2_OUT|LCD_D E|EVENT OUT|
||PE14|-|TIM1_CH 4|-|-|-|SPI4_MO SI|-|-|-|-|SAI4_MCL K_B|-|FMC_D11 /FMC_AD 11|-|LCD_C LK|EVENT OUT|
||PE15|-|TIM1_BKI N|-|-|-|-|-|-|-|-|-|USART10_C K|FMC_D1 2/FMC_A D12|TIM1_B KIN_C OMP12|LCD_R 7|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**





















|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Port F|PF0|-|-|-|-|I2C2_SDA|-|I2C5_SDA|-|-|OCTOSPIM _P2_IO0|-|-|FMC_A0|TIM23_ CH1|-|EVENT OUT|
||PF1|-|-|-|-|I2C2_SCL|-|I2C5_SCL|-|-|OCTOSPIM _P2_IO1|-|-|FMC_A1|TIM23_ CH2|-|EVENT OUT|
||PF2|-|-|-|-|I2C2_SMB A|-|I2C5_SMB A|-|-|OCTOSPIM _P2_IO2|-|-|FMC_A2|TIM23_ CH3|-|EVENT OUT|
||PF3|-|-|-|-|-|-|-|-|-|OCTOSPIM _P2_IO3|-|-|FMC_A3|TIM23_ CH4|-|EVENT OUT|
||PF4|-|-|-|-|-|-|-|-|-|OCTOSPIM _P2_CLK|-|-|FMC_A4|-|-|EVENT OUT|
||PF5|-|-|-|-|-|-|-|-|-|OCTOSPIM _P2_NCLK|-|-|FMC_A5|-|-|EVENT OUT|
||PF6|-|TIM16_C H1|FDCAN3 _RX|-|-|SPI5_NSS|SAI1_SD_ B|UART7_R X|SAI4_SD_ B|-|OCTOSPI M_P1_IO3|-|-|TIM23_ CH1|-|EVENT OUT|
||PF7|-|TIM17_C H1|FDCAN3 _TX|-|-|SPI5_SCK|SAI1_MCL K_B|UART7_T X|SAI4_MC LK_B|-|OCTOSPI M_P1_IO2|-|-|TIM23_ CH2|-|EVENT OUT|
||PF8|-|TIM16_C H1N|-|-|-|SPI5_MIS O|SAI1_SCK _B|UART7_R TS/UART 7_DE|SAI4_SC K_B|TIM13_CH 1|OCTOSPI M_P1_IO0|-|-|TIM23_ CH3|-|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot F|PF9|-|TIM17_C H1N|-|-|-|SPI5_MO SI|SAI1_FS_B|UART7_C TS|SAI4_FS_ B|TIM14_CH 1|OCTOSPI M_P1_IO1|-|-|TIM23_ CH4|-|EVENT OUT|
||PF10|-|TIM16_B KIN|SAI1_D3|-|PSSI_D15|-|-|-|-|OCTOSPIM _P1_CLK|SAI4_D3|-|-|DCMI_ D11/PS SI_D11|LCD_D E|EVENT OUT|
||PF11|-|-|-|-|-|SPI5_MO SI|-|-|-|OCTOSPIM _P1_NCLK|SAI4_SD_ B|-|FMC_NR AS|DCMI_ D12/PS SI_D12|TIM24_ CH1|EVENT OUT|
||PF12|-|-|-|-|-|-|-|-|-|OCTOSPIM _P2_DQS|-|-|FMC_A6|-|TIM24_ CH2|EVENT OUT|
||PF13|-|-|-|DFSDM1_ DATIN6|I2C4_SMB A|-|-|-|-|-|-|-|FMC_A7|-|TIM24_ CH3|EVENT OUT|
||PF14|-|-|-|DFSDM1_ CKIN6|I2C4_SCL|-|-|-|-|-|-|-|FMC_A8|-|TIM24_ CH4|EVENT OUT|
||PF15|-|-|-||I2C4_SDA|-|-|-|-|-|-|-|FMC_A9|-|-|EVENT OUT|
|Port G-|PG0|-|-|-|-|-|-|-|-|-|OCTOSPIM _P2_IO4|-|UART9_RX|FMC_A10|-|-|EVENT OUT|
||PG1|-|-|-|-|-|-|-|-|-|OCTOSPIM _P2_IO5|-|UART9_TX|FMC_A11|-|-|EVENT OUT|
||PG2|-|-|-|TIM8_BKI N|-|-|-|-|-|-|-|TIM8_BKIN_ COMP12|FMC_A12|-|TIM24_ ETR|EVENT OUT|
||PG3|-|-|-|TIM8_BKI N2|-|-|-|-|-|-|-|TIM8_BKIN2 _COMP12|FMC_A13|TIM23_ ETR|-|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**











































|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot G|PG4|-|TIM1_BKI N2|-|-|-|-|-|-|-|-|-|TIM1_BKIN2 _COMP12|FMC_A14 /FMC_BA 0|-|-|EVENT OUT|
||PG5|-|TIM1_ET R|-|-|-|-|-|-|-|-|-|-|FMC_A15 /FMC_BA 1|-|-|EVENT OUT|
||PG6|-|TIM17_B KIN|-|-|-|-|-|-|-|-|OCTOSPI M_P1_NC S|-|FMC_NE 3|DCMI_ D12/PS SI_D12|LCD_R 7|EVENT OUT|
||PG7|-|-|-|-|-|-|SAI1_MCL K_A|USART6_ CK|-|OCTOSPIM _P2_DQS|-|-|FMC_INT|DCMI_ D13/PS SI_D13|LCD_C LK|EVENT OUT|
||PG8|-|-|-|TIM8_ET R|-|SPI6_NSS /I2S6_WS|-|USART6_ RTS/USA RT6_DE|SPDIFRX 1_IN3|-|-|ETH_PPS_ OUT|FMC_SD CLK|-|LCD_G 7|EVENT OUT|
||PG9|-|-|FDCAN3 _TX|-|-|SPI1_MIS O/I2S1_S DI|-|USART6_ RX|SPDIFRX 1_IN4|OCTOSPIM _P1_IO6|SAI4_FS_ B|SDMMC2_D 0|FMC_NE 2/FMC_N CE|DCMI_ VSYNC /PSSI_ RDY|-|EVENT OUT|
||PG10|-|-|FDCAN3 _RX|OCTOSPI M_P2_IO 6|-|SPI1_NSS /I2S1_WS|-|-|-|LCD_G3|SAI4_SD_ B|SDMMC2_D 1|FMC_NE 3|DCMI_ D2/PS SI_D2|LCD_B 2|EVENT OUT|
||PG11|-|LPTIM1_I N2|-|-|USART10_ RX|SPI1_SCK /I2S1_CK|-|-|SPDIFRX 1_IN1|OCTOSPIM _P2_IO7|SDMMC2_ D2|ETH_MII_TX _EN/ETH_R MII_TX_EN|-|DCMI_ D3/PS SI_D3|LCD_B 3|EVENT OUT|
||PG12|-|LPTIM1_I N1|-|OCTOSPI M_P2_NC S|USART10_ TX|SPI6_MIS O/I2S6_S DI|-|USART6_ RTS/USA RT6_DE|SPDIFRX 1_IN2|LCD_B4|SDMMC2_ D3|ETH_MII_TX D1/ETH_RM II_TXD1|FMC_NE 4|TIM23_ CH1|LCD_B 1|EVENT OUT|
||PG13|TRAC ED0|LPTIM1_ OUT|-|-|USART10_ CTS/USAR T10_NSS|SPI6_SCK /I2S6_CK|-|USART6_ CTS/USA RT6_NSS|-|-|SDMMC2_ D6|ETH_MII_TX D0/ETH_RM II_TXD0|FMC_A24|TIM23_ CH2|LCD_R 0|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**



























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot G|PG14|TRAC ED1|LPTIM1_ ETR|-|-|USART10_ RTS/USAR T10_DE|SPI6_MO SI/I2S6_S DO|-|USART6_ TX|-|OCTOSPIM _P1_IO7|SDMMC2_ D7|ETH_MII_TX D1/ETH_RM II_TXD1|FMC_A25|TIM23_ CH3|LCD_B 0|EVENT OUT|
||PG15|-|-|-|-|-|-|-|USART6_ CTS/USA RT6_NSS|-|OCTOSPIM _P2_DQS|-|USART10_C K|FMC_NC AS|DCMI_ D13/PS SI_D13|-|EVENT OUT|
|Port H|PH0|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|
||PH1|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|EVENT OUT|
||PH2|-|LPTIM1_I N2|-|-|-|-|-|-|-|OCTOSPIM _P1_IO4|SAI4_SCK _B|ETH_MII_C RS|FMC_SD CKE0|-|LCD_R 0|EVENT OUT|
||PH3|-|-|-|-|-|-|-|-|-|OCTOSPIM _P1_IO5|SAI4_MCL K_B|ETH_MII_C OL|FMC_SD NE0|-|LCD_R 1|EVENT OUT|
||PH4|-|-|-|-|I2C2_SCL|-|-|-|-|LCD_G5|OTG_HS_ ULPI_NXT|-|-|PSSI_ D14|LCD_G 4|EVENT OUT|
||PH5|-|-|-|-|I2C2_SDA|SPI5_NSS|-|-|-|-|-|-|FMC_SD NWE|-|-|EVENT OUT|
||PH6|-|-|TIM12_ CH1|-|I2C2_SMB A|SPI5_SCK|-|-|-|-|-|ETH_MII_R XD2|FMC_SD NE1|DCMI_ D8/PS SI_D8|-|EVENT OUT|
||PH7|-|-|-|-|I2C3_SCL|SPI5_MIS O|-|-|-|-|-|ETH_MII_R XD3|FMC_SD CKE1|DCMI_ D9/PS SI_D9|-|EVENT OUT|
||PH8|-|-|TIM5_E TR|-|I2C3_SDA|-|-|-|-|-|-|-|FMC_D1 6|DCMI_ HSYNC /PSSI_ DE|LCD_R 2|EVENT OUT|
||PH9|-|-|TIM12_ CH2|-|I2C3_SMB A|-|-|-|-|-|-|-|FMC_D1 7|DCMI_ D0/PS SI_D0|LCD_R 3|EVENT OUT|

**Table 8. STM32H730xB** **p** **in alternate functions** **(** **continued** **)**























|Port|Col2|AF0|AF1|AF2|AF3|AF4|AF5|AF6|AF7|AF8|AF9|AF10|AF11|AF12|AF13|AF14|AF15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||SYS|FMC/ LPTIM1/ SAI4/ TIM16/17 /TIM1x/ TIM2x|FDCAN3 /PDM_ SAI1/ TIM3/4/5 /12/15|DFSDM1/ LCD/ LPTIM2/3/ 4/5/ LPUART1 /OCTO SPIM_P1/ 2/TIM8|CEC/DCMI/ PSSI/ DFSDM1/ I2C1/2/3/4/5 /LPTIM2/ OCTOSPIM _P1/TIM15/ USART1/10|CEC/ FDCAN3/ SPI1/I2S1/ SPI2/I2S2/ SPI3/I2S3/ SPI4/5/6|DFSDM1/ I2C4/5/ OCTO SPIM_P1/ SAI1/SPI3/ I2S3/ UART4|SDMMC1/ SPI2/I2S2 /SPI3/I2S 3/SPI6/ UART7 /USART1/ 2/3/6|LPUART1 /SAI4/ SDMMC1/ SPDIFRX 1/SPI6/ UART4/5/ 8|FDCAN1/2/ FMC/LCD/ OCTOSPIM _P1/2/SAI4 /SDMMC2/ SPDIFRX1/ TIM13/14|CRS/FMC/ LCD/OCT OSPIM_P1 /OTG1_FS/ OTG1_HS/ SAI4/ SDMMC2/ TIM8|DFSDM1/ ETH/I2C4/ LCD/MDIOS /OCTOSPIM _P1/SDMMC 2/SWPMI1/ TIM1x/TIM8/ UART7/9/ USART10|FMC/LCD /MDIOS/ OCTOSPI M_P1/ SDMMC1 /TIM1x/ TIM8|COMP/ DCMI/ PSSI/ LCD/ TIM1x/ TIM23|LCD/ TIM24/ UART5|SYS|
|Prot H|PH10|-|-|TIM5_C H1|-|I2C4_SMB A|-|-|-|-|-|-|-|FMC_D1 8|DCMI_ D1/PS SI_D1|LCD_R 4|EVENT OUT|
||PH11|-|-|TIM5_C H2|-|I2C4_SCL|-|-|-|-|-|-|-|FMC_D1 9|DCMI_ D2/PS SI_D2|LCD_R 5|EVENT OUT|
||PH12|-|-|TIM5_C H3|-|I2C4_SDA|-|-|-|-|-|-|-|FMC_D2 0|DCMI_ D3/PS SI_D3|LCD_R 6|EVENT OUT|
||PH13|-|-|-|TIM8_CH 1N|-|-|-|-|UART4_T X|FDCAN1_T X|-|-|FMC_D2 1|-|LCD_G 2|EVENT OUT|
||PH14|-|-|-|TIM8_CH 2N|-|-|-|-|UART4_R X|FDCAN1_R X|-|-|FMC_D2 2|DCMI_ D4/PS SI_D4|LCD_G 3|EVENT OUT|
||PH15|-|-|-|TIM8_CH 3N|-|-|-|-|-|-|-|-|FMC_D2 3|DCMI_ D11/PS SI_D11|LCD_G 4|EVENT OUT|
|Port J|PJ8|-|TIM1_CH 3N|-|TIM8_CH 1|-|-|-|-|UART8_T X|-|-|-|-|-|LCD_G 1|EVENT OUT|
||PJ9|-|TIM1_CH 3|-|TIM8_CH 1N|-|-|-|-|UART8_R X|-|-|-|-|-|LCD_G 2|EVENT OUT|
||PJ10|-|TIM1_CH 2N|-|TIM8_CH 2|-|SPI5_MO SI|-|-|-|-|-|-|-|-|LCD_G 3|EVENT OUT|
||PJ11|-|TIM1_CH 2|-|TIM8_CH 2N|-|SPI5_MIS O|-|-|-|-|-|-|-|-|LCD_G 4|EVENT OUT|

**Electrical characteristics** **STM32H730xB**
#### **6 Electrical characteristics**
###### **6.1 Parameter conditions**

Unless otherwise specified, all voltages are referenced to V SS .

**6.1.1** **Minimum and maximum values**

Unless otherwise specified the minimum and maximum values are guaranteed in the worst
conditions of junction temperature, supply voltage and frequencies by tests in production on
100% of the devices with a junction temperature at T J = 25 °C and T J = T Jmax (given by the
selected temperature range).

Data based on characterization results, design simulation and/or technology characteristics
are indicated in the table footnotes. Based on characterization, the minimum and maximum
values refer to sample tests and represent the mean value plus or minus three times the
standard deviation (mean±3σ).

**6.1.2** **Typical values**

Unless otherwise specified, typical data are based on T J = 25 °C, V DD = 3.3 V (for the
1.7 V ≤ V DD ≤ 3.6 V voltage range). They are given only as design guidelines and are not
tested.

Typical ADC accuracy values are determined by characterization of a batch of samples from
a standard diffusion lot over the full temperature range, where 95% of the devices have an
error less than or equal to the value indicated (mean±2σ) .

**6.1.3** **Typical curves**

Unless otherwise specified, all typical curves are given only as design guidelines and are
not tested.

**6.1.4** **Loading capacitor**

The loading conditions used for pin parameter measurement are shown in *Figure 11* .

**6.1.5** **Pin input voltage**

The input voltage measurement on a pin of the device is described in *Figure 12* .

**Figure 11. Pin loading conditions** **Figure 12. Pin input voltage**


MCU pin

C = 50 pF

MS19011V2

102/270 DS13315 Rev 5


MCU pin


VIN


MS19010V2

**STM32H730xB** **Electrical characteristics**

**6.1.6** **Power supply scheme**

**Fi** **g** **ure 13. Power su** **pp** **l** **y** **scheme**









|Col1|Core domain (V ) CORE|Col3|
|---|---|---|
||Power switch Power switch D3 domain (System logic, D1 domain shifter IO EXTI, D2 domain (CPU, peripherals, logic Peripherals, (peripherals, RAM) Level RAM) RAM) Flash||
|||D3 domain (System logic, IO EXTI, logic Peripherals, RAM)|
||Level shifter|IO logic|
||||





|Col1|Col2|USB FS IOs|
|---|---|---|
||||









1. Refer to application note AN5419 “ *Getting started with STM32H723/733, STM32H725/735 and*
*STM32H730 Value Line hardware development* “ for the possible power scheme and connected capacitors.

DS13315 Rev 5 103/270


239

**Electrical characteristics** **STM32H730xB**

**6.1.7** **Current consumption measurement**

**Fi** **g** **ure 14. Current consum** **p** **tion measurement scheme**





###### **6.2 Absolute maximum ratings**

Stresses above the absolute maximum ratings listed in *Table 9: Voltage characteristics*,
*Table 10: Current characteristics*, and *Table 11: Thermal characteristics* may cause
permanent damage to the device. These are stress ratings only and the functional operation
of the device at these conditions is not implied. Exposure to maximum rating conditions for
extended periods may affect device reliability. Device mission profile (application conditions)
is compliant with JEDEC JESD47 Qualification Standard, extended mission profiles are
available on demand.

*Note:* *For information on product lifetime estimation, refer to application note AN5337: Guidelines*
*for estimating STM32H7 MCUs lifetime, available from the STMicroelectronics website*
*www.st.com.*

**Table 9. Volta** **g** **e characteristics**






|Symbols|Ratings|Min|Max|Unit|
|---|---|---|---|---|
|V - V (1) DDX SS|External main supply voltage (including V, DD V, V, V, V, V ) DDLDO DDSMPS DDA DD33USB BAT|−0.3|4.0|V|
|V (2) IN|Input voltage on FT_xxx pins|V −0.3 SS|Min(Min(V, DD V, V, DDA DD33USB V ) + 4.0, 6 V) BAT (3)(4)(5)|V|
||Input voltage on TT_xx pins|V −0.3 SS|4.0|V|
||Input voltage on BOOT0 pin|V SS|9.0|V|
||Input voltage on any other pins|V -0.3 SS|4.0|V|
||∆V | DDX|Variations between different V power DDX pins of the same domain|-|50|mV|
||V -V | SSx SS|Variations between all the different ground pins|-|50|mV|


104/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

1. All main power (V DD, V DDA, V DD33USB, V DDSMPS, V BAT ) and ground (V SS, V SSA ) pins must always be
connected to the external power supply, in the permitted range.

2. V IN maximum must always be respected. Refer to *Table 53: I/O current injection susceptibility* for the
maximum allowed injected current values.

3. This formula has to be applied on power supplies related to the IO structure described by the pin definition
table.

4. To sustain a voltage higher than 4 V the internal pull-up/pull-down resistors must be disabled.

5. When an FT_a pin is used by an analog peripheral such as ADC, the maximum V IN is 4 V.














|Col1|Table 10. Current characteristics|Col3|Col4|
|---|---|---|---|
|Symbols|Ratings|Max|Unit|
|ΣIV DD|Total current into sum of all V power lines (source)(1) DD|620|mA|
|ΣIV SS|Total current out of sum of all V ground lines (sink)(1) SS|620||
|IV DD|Maximum current into each V power pin (source)(1) DD|100||
|IV SS|Maximum current out of each V ground pin (sink)(1) SS|100||
|I IO|Output current sunk or sourced by any I/O and control pin, except Pxy_C|20||
||Output current sunk or sourced by Pxy_C pins|1||
|ΣI (PIN)|Total output current sunk by sum of all I/Os and control pins(2)|140||
||Total output current sourced by sum of all I/Os and control pins(2)|140||
|I (3)(4) INJ(PIN)|Injected current on FT_xxx, TT_xx, RST and B pins except PA4, PA5|−5/+0||
||Injected current on PA4, PA5|−0/0||
|ΣI INJ(PIN)|Total injected current (sum of all I/Os and control pins)(5)|±25||


1. All main power (V DD, V DDA, V DD33USB ) and ground (V SS, V SSA ) pins must always be connected to the
external power supplies, in the permitted range.

2. This current consumption must be correctly distributed over all I/Os and control pins. The total output
current must not be sunk/sourced between two consecutive power supply pins referring to high pin count
QFP packages.

3. Positive injection is not possible on these I/Os and does not occur for input voltages lower than the
specified maximum value.

4. A positive injection is induced by V IN >V DD while a negative injection is induced by V IN <V SS . I INJ(PIN) must
never be exceeded. Refer also to *Table 9: Voltage characteristics* for the maximum allowed input voltage
values.

5. When several inputs are submitted to a current injection, the maximum ∑I INJ(PIN) is the absolute sum of the
positive and negative injected currents (instantaneous values).

|Col1|Table 11. Thermal characteristics|Col3|Col4|Col5|
|---|---|---|---|---|
|Symbol|Ratings||Value|Unit|
|T STG|Storage temperature range||−65 to +150|°C|
|T J|Maximum junction temperature|Industrial temperature range 6|125||



DS13315 Rev 5 105/270


239

**Electrical characteristics** **STM32H730xB**
###### **6.3 Operating conditions**

**6.3.1** **General operating conditions**

**Table 12. General o** **p** **eratin** **g** **conditions**









|Symbol|Parameter|Operating conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V DD|Standard operating voltage|-|1.62(1)|-|3.6|V|
|V DDLDO|Supply voltage for the internal regulator|V ≤ V DDLDO DD|1.62(1)|-|3.6||
|V DDSMPS|Supply voltage for the internal SMPS Step-down converter|V = V DDSMPS DD|1.62(1)|-|3.6||
|V DD50USB|-|USB regulator ON|4|5|5.5||
|||USB regulator OFF|-|V DD33US B|-||
|V DD33USB|Standard operating voltage, USB domain|USB used|3.0|-|3.6||
|||USB not used|0|-|3.6||
|V DDA|Analog operating voltage|ADC or COMP used|1.62|-|3.6||
|||DAC used|1.8|-|||
|||OPAMP used|2.0|-|||
|||VREFBUF used|1.8|-|||
|||ADC, DAC, OPAMP, COMP, VREFBUF not used|0|-|||
|V BAT|Supply voltage for Backup domain|-|1.2(2)|-|3.6||
|V IN|I/O Input voltage|TT_xx I/O except Pxy_C|−0.3|-|V +0.3 DD||
|||Pxy_C I/O|−0.3|-|Min(V, DDA V ) + 0.3 DD||
|||BOOT0|0|-|9||
|||All I/Os except BOOT0, TT_xx and Pxy_C|−0.3|-|Min(V, V, DD DDA V ) + 3. DD33USB 6 < 5.5(3)||


106/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 12. General o** **p** **eratin** **g** **conditions** **(** **continued** **)**









|Symbol|Parameter|Operating conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V CORE|Internal regulator ON (LDO or SMPS)(4)|VOS3|0.95|1.0|1.05|V|
|||VOS2|1.05|1.10|1.15||
|||VOS1|1.15|1.21|1.26||
|||VOS0|1.30|1.36|1.40||
||Regulator OFF: external V CORE voltage must be supplied from external regulator on VCAP pins|VOS3|0.98|1.03|1.08||
|||VOS2|1.08|1.13|1.18||
|||VOS1|1.18|1.23|1.28||
|||VOS0|1.33|1.38|1.40||
|f CPU|Arm® Cortex®-M7 clock frequency|VOS3|-|-|170|MHz|
|||VOS2|-|-|300||
|||VOS1|-|-|400||
|||VOS0|-|-|520||
|||VOS0 and CPU_FREQ_BOOST|-|-|550||
|f ACLK|AXI clock frequency|VOS3|-|-|85||
|||VOS2|-|-|150||
|||VOS1|-|-|200||
|||VOS0|-|-|275||
|f HCLK|AHB clock frequency|VOS3|-|-|85||
|||VOS2|-|-|150||
|||VOS1|-|-|200||
|||VOS0|-|-|275||
|f PCLK|APB clock frequency|VOS3|-|-|42.5(5)||
|||VOS2|-|-|75||
|||VOS1|-|-|100||
|||VOS0|-|-|137.5||
|T (6) A|Ambient temperature for temperature range 3|Maximum power dissipation|−40||125|°C|
||Ambient temperature for temperature range 6|Maximum power dissipation|−40||85||
|||Low-power dissipation(7)|−40||105||


1. When RESET is released, the functionality is guaranteed down to V PDRmax or down to the specified V DDmin when the PDR is
OFF. The PDR can only be switched OFF though the PDR_ON pin that not available in all packages.

2. V BAT minimum value can be reduced to 0 V if V DD is present.

3. This formula has to be applied on power supplies related to the I/O structure described by the pin definition table.

4. At startup, the external V CORE voltage must remain higher or equal to 1.10 V before disabling the internal regulator (LDO).

DS13315 Rev 5 107/270


239

**Electrical characteristics** **STM32H730xB**

5. This value corresponds to the maximum APB clock frequency when at least one peripheral is enabled.

6. The device junction temperature must be kept below maximum T J indicated in *Table 13: Supply voltage and maximum*
*temperature configuration* and the maximum temperature.

7. In low-power dissipation state, T A can be extended to this range as long as T J does not exceed T Jmax (see *Section 7.9:*
*Thermal characteristics* ).

**Table 13. Su** **pp** **l** **y** **volta** **g** **e and maximum tem** **p** **erature confi** **g** **uration**














|Power scale|V source CORE|Max. T (°C)(1) J|Min. V (V) DD|Min. V (V) DDLDO|
|---|---|---|---|---|
|VOS0|SMPS|105|2.2|-|
||LDO||1.7|1.7|
||SMPS supplies LDO||3(2)|1.7|
||External (Bypass)||1.62|-|
|VOS1|SMPS|140|2.2|-|
|||125|1.62|-|
||LDO||1.62|1.62|
||SMPS supplies LDO||2.3|-|
||External (Bypass)||1.62|-|
|VOS2|SMPS|140|1.62|-|
||LDO|125|1.62|1.62|
||SMPS supplies LDO||2.3|-|
||External (Bypass)||1.62|-|
|VOS3|SMPS|140|1.62|-|
||LDO|125|1.62|1.62|
||SMPS supplies LDO||2.3|-|
||External (Bypass)||1.62|-|
|SVOS4/SVOS5|SMPS|140|1.62|-|
||LDO|125|2|2|
|||105|1.62|1.62|
||SMPS supplies LDO|125|3(2)|2|
|||105|2.3|-|
||External (Bypass)|125|1.62|-|


1. 140 °C can be reached only for part numbers in temperature range 3. For part numbers in temperature
range 6, this value must be decreased to 125 °C.

2. The SMPS must be configured to output 2,5 V.

108/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.2** **VCAP external capacitor**

Stabilization for the main regulator is achieved by connecting an external capacitor C EXT to
the VCAP pin. C EXT is specified in *Table 14* . Two external capacitors can be connected to
VCAP pins.

**Fi** **g** **ure 15. External ca** **p** **acitor C** **EXT**

1. Legend: ESR is the equivalent series resistance.

**Table 14. VCAP o** **p** **eratin** **g** **conditions** **[(1)]**

|Symbol|Parameter|Conditions|
|---|---|---|
|CEXT|Capacitance of external capacitor|2.2 µF(2)(3)|
|ESR|ESR of external capacitor|< 100 m|



1. When bypassing the voltage regulator, the two 2.2 µF V CAP capacitors are not required and should be
replaced by two 100 nF decoupling capacitors.

2. This value corresponds to CEXT typical value. A variation of +/-20% is tolerated.

3. I f a third VCAP pin is available on the package, it must be connected to the other VCAP pins but no
additional capacitor is required.

**6.3.3** **SMPS step-down converter**

The devices embed a high power efficiency SMPS step-down converter. SMPS
characteristics for external usage are given in *Table 16* . The SMPS step-down converter
requires external components that are fully described in AN5419 *“Getting started with*
*STM32H723/733, STM32H725/735 and STM32H730 Value Line hardware development”.*
The components used for datasheet characterization are specified in *Figure 16* and
*Table 15* .

DS13315 Rev 5 109/270


239

|Col1|SMPS (ON)|
|---|---|
|||











|Voltage|Col2|
|---|---|
||regulator (OFF)|

|Col1|SMPS (ON)|Col3|
|---|---|---|
||||
||||
|Voltage|||
||regulator (ON)||


|E|lectrical characteristics ST|M32H730xB|
|---|---|---|
||Figure 16. External components for SMPS step-down converter||
|VDD VDDSMPS VDD VDDSMPS Cin L VLXSMPS Cin L VLXSMPS VFBSMPS Cfilt S (M ONPS VFBSMPS Cfilt S (M ONPS ) VVDDDD__ ) EExxteternrnaall Cout1 VSSSMPS 2xCou1 VSSSMPS VCAP VCAP VDDLDO VVCCOORREE VDDLDO VVCCOORREE Voltage Voltage Cout2 re (g Ou Fla Ft )or Cout2 reg (Ou Nla )tor VSS VSS External SMPS supply, LDO supplied Direct SMPS supply by SMPS MSv61398V4|VDD VDDSMPS VDD VDDSMPS Cin L VLXSMPS Cin L VLXSMPS VFBSMPS Cfilt S (M ONPS VFBSMPS Cfilt S (M ONPS ) VVDDDD__ ) EExxteternrnaall Cout1 VSSSMPS 2xCou1 VSSSMPS VCAP VCAP VDDLDO VVCCOORREE VDDLDO Voltage Voltage Cout2 re (g Ou Fla Ft )or Cout2 reg (Ou Nla )tor VSS VSS External SMPS supply, LDO sup Direct SMPS supply by SMPS||


**Table 15. Characteristics of SMPS ste** **p** **-down converter external com** **p** **onents**

|Symbol|Parameter|Conditions|
|---|---|---|
|C in|Capacitance of external capacitor on V DDSMPS|4.7 µF|
||ESR of external capacitor|100 mΩ|
|C filt|Capacitance of external capacitor on V pin LXSMPS|220 pF|
|C OUT|Capacitance of external capacitor on V pin FBSMPS|10 µF|
||ESR of external capacitor|20 mΩ|
|L|Inductance of external Inductor on V pin LXSMPS|2.2 µH|
|-|Serial DC resistor|150 mΩ|
|I SAT|DC current at which the inductance drops 30% from its value without current.|1.7 A|
|I RMS|Average current for a 40 °C rise: rated current for which the temperature of the inductor is raised 40°C by DC current|1.4 A|



**Table 16. SMPS ste** **p** **-down converter characteristics for external usa** **g** **e**

|Parameters|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|V (1) DDSMPS|V = 1.8 V OUT|2.3|-|3.6|V|
||V = 2.5 V OUT|3|-|3.6||
|V (2) OUT|Iout=600 mA|2.25|2.5|2.75|V|
|||1.62|1.8|1.98||
|I OUT|internal and external usage|-|-|600|mA|
||External usage only(3)|-|-|600||
|RDS ON|-|-|100|120|mΩ|
|I DDSMPS_Q|Quiescent current|-|220|-|µA|



110/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 16. SMPS ste** **p** **-down converter characteristics for external usa** **g** **e** **(** **continued** **)**

|Parameters|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|T SMPS_START|V = 1.8 V OUT|-|270|405|µs|
||V = 2.5 V OUT|-|360|540||



1. The switching frequency is 2.4 MHz±10%

2. Including line transient and load transient.

3. These characteristics are given for SDEXTHP bit is set in the PWR_CR3 register.

**Table 17. Inrush current and inrush electric charge characteristics for LDO and**
**SMPS** **[(1)(2)]**







|Symbol|Parameter|Conditions|-|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|I RUSH|Inrush current on voltage regulator power-on (POR or wakeup from Standby)|on V (3) DDLDO|-|-|55|96(4)|mA|
|||on V (5) DDSMPS|SMPS supplies the V DDCORE|-|100|420(6)||
||Inrush current on voltage regulator power-on (POR)|on V (5) DDSMPS|SMPS supplies internal LDO, V = 1. 8 V(7) OUT|-|130|400(6)||
||||SMPS supplies internal LDO, V = 2.5 V(7) OUT|-|-|300(6)||
||||SMPS supplies external circuit, V = 1.8 V(7) OUT|-|100|320(6)||
||||SMPS supplies external circuit, V = 2.5 V(7) OUT|-|-|240(6)||
||Inrush current on voltage regulator power-on (wakeup from Standby)|on V (5) DDSMPS|SMPS supplies internal LDO, V = 1.8 V OUT|-|170|530(6)||
||||SMPS supplies internal LDO, V = 2.5 V OUT|-|240|550(6)||


DS13315 Rev 5 111/270


239

**Electrical characteristics** **STM32H730xB**

**Table 17. Inrush current and inrush electric charge characteristics for LDO and**
**SMPS** **[(1)(2)]** **(** **continued** **)**














|Symbol|Parameter|Conditions|-|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|Q RUSH|Inrush current on voltage regulator power-on (POR or wakeup from Standby)|on V (3) DDLDO|-|-|4.4|5.3(4)|μC|
|||on V (5) DDSMPS|SMPS supplies the V DDCORE|-|7.3|18(6)||
||Inrush current on voltage regulator power-on (POR)|on V (5) DDSMPS|SMPS supplies internal LDO, V = 1. 8 V(7) OUT|-|8.8|17(6)||
||||SMPS supplies internal LDO, V = 2.5 V(7) OUT|-||13(6)||
||||SMPS supplies external circuit, V = 1.8 V(7) OUT|-|7.3|13.7(6)||
||||SMPS supplies external circuit, V = 2.5 V(7) OUT|-||10.5(6)||
||Inrush current on voltage regulator power-on (wakeup from Standby)|on V (5) DDSMPS|SMPS supplies internal LDO, V = 1.8 V OUT|-|15.0|28(6)||
||||SMPS supplies internal LDO, V = 2.5 V OUT|-|28.0|39(6)||


1. The typical values are given for V DDLDO = V DDSMPS = 3.3 V and for typical decoupling capacitor values of
C EXT and C OUT .

2. The product consumption (on VDDCORE) is not taken into account in the inrush current and inrush electric
charges.

3. The inrush current and inrush electric charge on VDDLDO are not present in Bypass mode or when the
SMPS supplies the VDDCORE.

4. The maximum value is given for the maximum decoupling capacitor C EXT .

5. The inrush current and inrush electric charges on VDDSMPS are not present if the external component (L
or C OUT ) is not present that is if the SMPS is not used.

6. The maximum value is given for the maximum decoupling capacitor C OUT and the minimum V DDSMPS
voltage.

7. The inrush current due to transition from 1.2 V to the final V OUT Value (1.8 V or 2.5 V) is not taken into
account.

112/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.4** **Operating conditions at power-up / power-down**

Subject to general operating conditions for T A .

**Table 18. O** **p** **eratin** **g** **conditions at** **p** **ower-u** **p** **/** **p** **ower-down**







|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t VDD|V rise time rate DD|0|∞|µs/V|
||V fall time rate DD|10|∞||
|t VDDA|V rise time rate DDA|0|∞||
||V fall time rate DDA|10|∞||
|t VDDUSB|V rise time rate DDUSB|0|∞||
||V fall time rate DDUSB|10|∞||
|t (1) VCORE|V rise time rate(2) CORE|0|285||
||V fall time rate CORE|10|∞||


1. t VCORE should be achieved when V CORE is provided by an external supply voltage (bypass with
VDDLDO = V CORE ).

2. V CORE rising slope must respect the above constraints. There are no constraints on the delay between V DD
rising and V CORE rising.

DS13315 Rev 5 113/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.5** **Embedded reset and power control block characteristics**

The parameters given in *Table 19* are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in *Table 12: General operating*
*conditions* .

**Table 19. Reset and** **p** **ower control block characteristics**










|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|t (1) RSTTEMPO|Reset temporization after BOR0 released|-|-|377|550|µs|
|V BOR0/POR/PDR|Power-on/power-down reset threshold|Rising edge(1)|1.62|1.67|1.71|V|
|||Falling edge|1.58|1.62|1.68||
|V BOR1|Brown-out reset threshold 1|Rising edge|2.04|2.10|2.15||
|||Falling edge|1.95|2.00|2.06||
|V BOR2|Brown-out reset threshold 2|Rising edge|2.34|2.41|2.47||
|||Falling edge|2.25|2.31|2.37||
|V BOR3|Brown-out reset threshold 3|Rising edge|2.63|2.70|2.78||
|||Falling edge|2.54|2.61|2.68||
|V PVD0|Programmable Voltage Detector threshold 0|Rising edge|1.90|1.96|2.01||
|||Falling edge|1.81|1.86|1.91||
|V PVD1|Programmable Voltage Detector threshold 1|Rising edge|2.05|2.10|2.16||
|||Falling edge|1.96|2.01|2.06||
|V PVD2|Programmable Voltage Detector threshold 2|Rising edge|2.19|2.26|2.32||
|||Falling edge|2.10|2.15|2.21||
|V PVD3|Programmable Voltage Detector threshold 3|Rising edge|2.35|2.41|2.47||
|||Falling edge|2.25|2.31|2.37||
|V PVD4|Programmable Voltage Detector threshold 4|Rising edge|2.49|2.56|2.62||
|||Falling edge|2.39|2.45|2.51||
|V PVD5|Programmable Voltage Detector threshold 5|Rising edge|2.64|2.71|2.78||
|||Falling edge|2.55|2.61|2.68||
|V PVD6|Programmable Voltage Detector threshold 6|Rising edge|2.78|2.86|2.94||
|||Falling edge in Run mode|2.69|2.76|2.83||
|V hyst_POR_PDR|Hysteresis voltage for Power-on/power-down reset (including BOR0)|Hysteresis in Run mode|-|43.00|-|mV|
|V hyst_BOR_PVD|Hysteresis voltage for BOR (except BOR0)|Hysteresis in Run mode|-|100|-||
|I (1) DD_BOR_PVD|BOR and PVD consumption from V DD|-|-|-|0.630|µA|
|I DD_POR_PVD|POR and PVD consumption from V DD|-|0.8|-|1.200||


114/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 19. Reset and** **p** **ower control block characteristics** **(** **continued** **)**





|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V AVM_0|Analog voltage detector for V threshold 0 DDA|Rising edge|1.66|1.71|1.76|V|
|||Falling edge|1.56|1.61|1.66||
|V AVM_1|Analog voltage detector for V threshold 1 DDA|Rising edge|2.06|2.12|2.19||
|||Falling edge|1.96|2.02|2.08||
|V AVM_2|Analog voltage detector for V threshold 2 DDA|Rising edge|2.42|2.50|2.58||
|||Falling edge|2.35|2.42|2.49||
|V AVM_3|Analog voltage detector for V threshold 3 DDA|Rising edge|2.74|2.83|2.91||
|||Falling edge|2.64|2.72|2.80||
|V hyst_VDDA|Hysteresis of V voltage DDA detector|-|-|100|-|mV|
|I DD_PVM|PVM consumption from V DD(1)|-|-|-|0.25|µA|
|I DD_VDDA|Voltage detector consumption on V (1) DDA|Resistor bridge|-|-|2.5|µA|


1. Guaranteed by design.

**6.3.6** **Embedded reference voltage characteristics**

The parameters given in *Table 20* are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in *Table 12: General operating*
*conditions* .

**Table 20. Embedded reference volta** **g** **e**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V REFINT|Internal reference voltages|-40°C < T < T J Jmax|1.180|1.216|1.255|V|
|t (1)(2) S_vrefint (3)|ADC sampling time when reading the internal reference voltage|-|4.3|-|-|µs|
|t (2) S_vbat|VBAT sampling time when reading the internal VBAT reference voltage|-|9|-|-||
|t (2) start_vrefint|Start time of reference voltage buffer when ADC is enable|-|-|-|4.4||
|I (2) refbuf|Reference Buffer consumption for ADC|V = 3.3 V DD|9|13.5|23|µA|
|ΔV (2) REFINT|Internal reference voltage spread over the temperature range|-40°C < T < T J Jmax|-|5|15|mV|
|T (2) coeff|Average temperature coefficient|Average temperature coefficient|-|20|70|ppm/°C|
|V (2) DDcoeff|Average Voltage coefficient|3.0 V < V < 3.6 V DD|-|10|1370|ppm/V|



DS13315 Rev 5 115/270


239

**Electrical characteristics** **STM32H730xB**

**Table 20. Embedded reference volta** **g** **e** **(** **continued** **)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V REFINT_DIV1|1/4 reference voltage|-|-|25|-|% V REFINT|
|V REFINT_DIV2|1/2 reference voltage|-|-|50|-||
|V REFINT_DIV3|3/4 reference voltage|-|-|75|-||



1. The shortest sampling time for the application can be determined by multiple iterations.

2. Guaranteed by design.

3. Guaranteed by design. and tested in production at 3.3 V.

**Table 21. Internal reference volta** **g** **e calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|V REFIN_CAL|Raw data acquired at temperature of 30 °C, V = 3.3 V DDA|1FF1 E860 - 1FF1 E861|



**6.3.7** **Embedded USB regulator characteristics**

The parameters given in *Table 22* are derived from tests performed under ambient
temperature and V DD supply voltage conditions summarized in *Table 12: General operating*
*conditions* .

**Table 22. USB re** **g** **ulator characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V DD50USB|Supply voltage|-|4|5|5.5|V|
|I DD50USB|Current consumption|-|-|14|-|µA|
|V REGOUTV33V|Regulated output voltage|-|3|-|3.6|V|
|I OUT|Output current load sinked by USB block|-|-|-|20|mA|
|T WKUP|Wakeup time|-|-|120|170|us|



**6.3.8** **Supply current characteristics**

The current consumption is a function of several parameters and factors such as the
operating voltage, ambient temperature, I/O pin loading, device software configuration,
operating frequencies, I/O pin switching rate, program location in memory and executed
binary code.

The current consumption is measured as described in *Figure 14: Current consumption*
*measurement scheme* .

All the Run-mode current consumption measurements given in this section are performed
with a CoreMark code.

116/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Typical and maximum current consumption**

The MCU is placed under the following conditions:

      - All I/O pins are in analog input mode.

      - All peripherals are disabled except when explicitly mentioned.

      - The flash memory access time is adjusted with the minimum wait states number,
depending on the f ACLK frequency (refer to the table “Number of wait states according to
CPU clock (f rcc_c_ck ) frequency and V CORE range” available in the reference manual).

      - When the peripherals are enabled, the AHB clock frequency is the CPU frequency
divided by 2 and the APB clock frequency is AHB clock frequency divided by 2.

      - For typical values, the power supply is 3 V unless otherwise specified.

The parameters given in the below tables are derived from tests performed at supply
voltage conditions summarized in *Table 12: General operating conditions*, and at ambient
temperature unless otherwise specified.

DS13315 Rev 5 117/270


239

**Electrical characteristics** **STM32H730xB**

**Table 23. Typical and maximum current consumption in Run mode,**
**code with data** **p** **rocessin** **g** **runnin** **g** **from ITCM** **[(1)]**
















|Symbol|Parameter|Conditions|Col4|f rcc_c_ck (MHz)|Typ LDO regulator ON|Typ SMPS ON|Max LDO regulator ON(2)|Col9|Col10|Col11|Max SMPS ON(3)|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||T = J 25 °C|T = J 85 °C|T = J 105 °C|T = J 125 °C|T = J 140 °C||
|I DD|Supply current in Run mode|All peripherals disabled|VOS0 (4)|550|145|81|170|260|330|-|-|mA|
|||||520|135|76|160|260|320|-|-||
||||VOS0|520|135|76|160|260|320|-|-||
|||||480|125|72.5|150|250|310|-|-||
|||||450|115|67.5|150|240|300|-|-||
|||||400|105|60|130|230|290|-|-||
||||VOS1|400|90.5|47|110|170|220|280|160||
|||||300|69.5|36.5|84|150|200|260|150||
||||VOS2|300|63|31.5|74|130|170|220|110||
|||||280|58|29|69|120|160|210|110||
|||||216|45.5|22.5|56|110|150|200|110||
|||||200|42|21|53|110|140|200|110||
||||VOS3|170|32.5|15|40|80|110|160|74||
|||||168|32|15|40|79|110|160|74||
|||||144|28|13.5|36|75|110|150|74||
|||||60|13.5|6.7|21|61|90|140|67||
|||||25|6.9|3.6|14|54|83|130|67||
|||All peripherals enabled|VOS0 (4)|550|215|125|250|360|430|-|-||
|||||520|205|120|240|350|420|-|-||
||||VOS0|520|205|120|240|350|420|-|-||
|||||400|160|92.5|190|300|370|-|-||
||||VOS1|400|135|72|160|230|290|360|200||
|||||300|105|54.5|130|200|250|330|180||
||||VOS2|300|95|46.5|110|170|210|280|140||
|||||280|88|43|100|160|210|270|140||
||||VOS3|170|49|22.5|58|110|140|190|93||


1. Data are in DTCM for best computation performance, the cache has no influence on consumption in this case.

2. Guaranteed by characterization results, unless otherwise specified. Refer to *Section 6.3.3: SMPS step-down converter* for the SMPS
maximum consumption.

3. The parameter values given in the above table for the SMPS regulator are extrapolated from the LDO consumption and typical SMPS
efficiency factors.

4. CPU_FREQ_BOOST is enabled.

118/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 24. Typical and maximum current consumption in Run mode, code with data processing**
**runnin** **g** **from flash memory, cache ON** **[(1)]**













|Symbol|Parameter|Conditions|Col4|f rcc_c_ck (MHz)|Typ LDO regulator ON|Typ SMPS ON|Max LDO regulator ON(2)|Col9|Col10|Col11|Max SMPS ON(3)|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||T = J 25 °C|T = J 85 °C|T = J 105 °C|T = J 125 °C|T = J 140 °C||
|I DD|Supply current in Run mode|All peripherals disabled|VOS0 (4)|550|145|83.5|170|270|330|-|-|mA|
|||||520|140|78.5|170|260|320|-|-||
||||VOS0|520|140|78.5|170|260|320|-|-||
|||||400|110|62|140|230|290|-|-||
||||VOS1|400|92|48.5|110|180|220|290|160||
|||||300|71|37.5|86|150|200|260|150||
||||VOS2|300|64|32|75|130|170|220|110||
|||||280|59|29.5|70|120|160|210|110||
|||||216|46.5|23|-|-|-|-|-||
|||||200|42.5|21.5|53|110|140|200|110||
|||||180|36|17|43|83|120|160|85||
||||VOS3|170|33.5|15.5|41|81|110|160|74||
|||||168|33|15.5|-|-|-|-|-||
|||||144|29|13.5|-|-|-|-|-||
|||||60|14|6.85|-|-|-|-|-||
|||||25|6.85|3.7|-|-|-|-|-||
|||All peripherals enabled|VOS0 (4)|550|220|130|250|360|430|-|-||
|||||520|210|120|240|350|420|-|-||
||||VOS0|520|210|120|240|350|420|-|-||
|||||400|160|94.5|190|300|370|-|-||
||||VOS1|400|140|73|160|240|290|360|200||
|||||300|105|55.5|130|200|250|330|180||
||||VOS2|300|96|47|110|170|210|280|140||
|||||280|89|43.5|110|160|210|270|140||
||||VOS3|170|50|23|59|110|140|190|93||


1. Data are in DTCM for best computation performance, the cache has no influence on consumption in this case.

2. Guaranteed by characterization results, unless otherwise specified. Refer to *Section 6.3.3: SMPS step-down converter* for
the SMPS maximum consumption.

3. The parameter values given in the above table for the SMPS regulator are extrapolated from the LDO consumption and
typical SMPS efficiency factors.

4. CPU_FREQ_BOOST is enabled.

DS13315 Rev 5 119/270


239

**Electrical characteristics** **STM32H730xB**

**Table 25. Typical and maximum current consumption in Run mode,**
**code with data** **p** **rocessin** **g** **runnin** **g** **from flash memor** **y** **, cache OFF** **[(1)]**










|Symbol|Parameter|Conditions|Col4|f rcc_c_ck (MHz)|Typ LDO regulator ON|Typ SMPS ON|Unit|
|---|---|---|---|---|---|---|---|
|I DD|Supply current in Run mode|All peripherals disabled|VOS0(2)|550|99|59.5|mA|
|||||520|95|56||
||||VOS0|520|95|56||
|||||400|76.5|47||
||||VOS1|400|66.5|38||
|||||300|51.5|30||
||||VOS2|300|47.5|26||
|||||280|43.5|24||
||||VOS3|170|24.5|13||
|||All peripherals enabled|VOS0(2)|550|170|100||
|||||520|165|95.5||
||||VOS0|520|165|95.5||
|||||400|130|77.5||
||||VOS1|400|115|62||
|||||300|87|47.5||
||||VOS2|300|79|41.5||
|||||280|73.5|38||
||||VOS3|170|41|20.5||


1. Data are in DTCM for best computation performance, the cache has no influence on consumption in this

case.

2. CPU_FREQ_BOOST is enabled.

120/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 26. Typical consumption in Run mode and corresponding performance**
**versus code** **p** **osition**













|Symbol|Parameter|Conditions|Col4|f rcc_c_c k (MHz)|Coremark|Typ LDO regulator ON|Typ SMPS ON|Unit|LDO I / DD Coremark|SMPS I / DD Coremark|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||Peripheral|Code|||||||||
|I DD|Supply current in Run mode|All peripherals disabled, cache ON|ITCM|550|2778|145|81|mA|52.2|29.2|µA/ Core- mark|
||||FLASH|550|2778|145|83.5||52.2|30.1||
||||AXI SRAM|550|2778|145|83.5||52.2|30.1||
||||SRAM 1|550|2778|150|86||54.0|31.0||
||||SRAM 4|550|2778|145|83.5||52.2|30.1||
|||All peripherals disabled cache OFF|FLASH|550|923|99|59.5||107.3|64.5||
||||AXI SRAM|550|1271|105|60.5||82.6|47.6||
||||SRAM 1|550|790|96.5|54.5||122.2|69.0||
||||SRAM 4|550|723|89.5|50.5||123.8|69.8||


**Table 27. T** **y** **pical current consum** **p** **tion in Autonomous mode**






|Symbol|Parameter|Conditions|Col4|f rcc_c_c k (MHz)|Typ LDO regulator ON|Typ SMPS ON|Unit|
|---|---|---|---|---|---|---|---|
|I DD|Supply current in Autonous mode|Run, D1Stop, D2Stop|VOS3|64|3.6|2.2|mA|
|||Run, D1Standby, D2Standby|VOS3|64|2.6|1.6||


**Table 28. T** **yp** **ical and maximum current consum** **p** **tion in Slee** **p** **mode**










|Symbol|Parameter|Conditions|Col4|f rcc_c_ck (MHz)|Typ LDO regulator ON|Typ SMPS ON|Max LDO regulator ON(1)(2)|Col9|Col10|Col11|Max SMPS ON(3)|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||T = J 25 °C|T = J 85 °C|T = J 105 °C|T = J 125 °C|T = J 140 °C||
|I DD(Sleep)|Supply current in Sleep mode|All peripherals disabled|VOS0 (4)|550|36|20.5|-|-|-|-|-|mA|
|||||520|33.5|19.5|60|170|240|-|-||
||||VOS0|520|33.5|19.5|60|170|240|-|-||
|||||400|27|16|52|160|230|-|-||
||||VOS1|400|22.5|12.5|39|110|170|240|140||
|||||300|18.5|10.5|34|110|160|240|140||
||||VOS2|300|16.5|8.75|28|85|130|190|110||
|||||170|9.7|5.2|21|78|120|190|110||
||||VOS3|170|8.5|4.35|17|61|96|150|74||


DS13315 Rev 5 121/270


239

**Electrical characteristics** **STM32H730xB**

1. Guaranteed by characterization results.

2. Refer to *Section 6.3.3: SMPS step-down converter* for the SMPS maximum consumption.

3. The parameter values given in the above table for the SMPS regulator are extrapolated from the LDO consumption and
typical SMPS efficiency factors.

4. CPU_FREQ_BOOST is enabled.

**Table 29. T** **yp** **ical and maximum current consum** **p** **tion in S** **y** **stem Sto** **p** **mode**











|Symbol|Parameter|Conditions|Col4|Typ LDO regulator ON|Typ SMPS ON(3)|Max LDO regulator ON(1)(2)|Col8|Col9|Col10|Max SMPS ON(3)|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||T = J 25 °C|T = J 85 °C|T = J 105 °C|T = J 125 °C|T = J 140 °C||
|I DD(Stop)|D1, D2 and D3 domains in DStop mode|Flash memory in low-power mode|SVOS5|0.52|0.2|3.7|26.0|44.0|72.0|50.0|mA|
||||SVOS4|0.81|0.34|6.1|39.0|64.0|110.0|70.0||
||||SVOS3|1.15|0.51|8.6|51.0|83.0|130.0|100.0||
|||Flash memory in normal mode, IWDG OFF|SVOS5|0.535|0.2|3.7|26.0|44.0|72.0|50.0||
||||SVOS4|0.96|0.4|6.2|39.0|64.0|110.0|75.0||
||||SVOS3|1.45|0.65|8.8|51.0|83.0|130.0|100.0||
||D1 and D3 domains in DStop mode, D2 domain in DStandby mode|Flash memory in low-power mode, IWDG OFF|SVOS5|0.48|0.19|3.3|23.0|39.0|63.0|43.0||
||||SVOS4|0.73|0.31|5.4|34.0|56.0|88.0|58.0||
||||SVOS3|1|0.46|7.7|45.0|72.0|120.0|71.0||
|||Flash memory in normal mode, IWDG OFF|SVOS5|0.46|0.18|3.3|23.0|39.0|63.0|43.0||
||||SVOS4|0.9|0.38|5.6|34.0|56.0|89.0|58.0||
||||SVOS3|1.17|0.52|7.8|45.0|72.0|120.0|71.0||
||D1 domain in DStandby mode, D2 and D3 domains in DStop mode|Flash memory in low-power mode, IWDG OFF|SVOS5|0.15|0.069|0.8|5.4|9.2|16.0|9.8||
||||SVOS4|0.21|0.098|1.3|7.9|14.0|22.0|14.0||
||||SVOS3|0.275|0.15|1.8|11.0|18.0|28.0|17.0||
||D1 and D2 domains in DStandby mode, D3 domain in DStop mode||SVOS5|0.095|0.055|0.3|2.1|3.6|5.9|3.8||
||||SVOS4|0.12|0.064|0.5|3.2|5.2|8.3|5.1||
||||SVOS3|0.15|0.084|0.8|4.2|6.8|11.0|6.3||


1. Guaranteed by characterization results.

2. Refer to *Section 6.3.3: SMPS step-down converter* for the SMPS maximum consumption.

3. The parameter values given in the above table for the SMPS regulator are extrapolated from the LDO consumption and
typical SMPS efficiency factors.

122/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 30. T** **yp** **ical and maximum current consum** **p** **tion in Standb** **y** **mode**












|Symbol|Parameter|Conditions|Col4|Typ(1)|Col6|Col7|Col8|Max at 3.6 V with LDO regulator ON(2)|Col10|Col11|Col12|Max at 3.6 V with SMPS ON(3)|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Backup SRAM|RTC and LSE(4)|1.65 V|2.4 V|3 V|3.3 V|T = J 25 ° C|T = J 85 ° C|T = J 105 ° C|T = J 125 ° C|T = 140 °C J||
|I DD (Standby)|Supply current in Standby mode, IWDG OFF|OFF|OFF|2.2|2.35|2.5|2.8|-|-|-|-|-|µA|
|||ON|OFF|3.5|3.7|4|4.3|-|-|-|-|-||
|||OFF|ON|2.2|2.4|2.85|3.25|4.5|15|30|64|96||
|||ON|ON|3.5|3.8|4.35|4.75|8.3|39|75|140|180||


1. These values are given for PDR OFF. When the PDR is ON, the typical current consumption is increased (refer to *Table 19:*
*Reset and power control block characteristics* .

2. Guaranteed by characterization results.

3. The parameter values given in the above table for the SMPS regulator are extrapolated from the LDO consumption and
typical SMPS efficiency factors.

4. The LSE is in Low-drive mode.

**Table 31. T** **yp** **ical and maximum current consum** **p** **tion in V** **BAT** **mode**












|Sym- bol|Para- meter|Conditions|Col4|Typ|Col6|Col7|Col8|Max at 3.6 V with LDO regulator ON(1)(2)|Col10|Col11|Col12|Max at 3.6 V with SMPS ON(1)(2)|Unit|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Back- up SRAM|RTC and LSE(3)|1.2 V|2 V|3 V|3.3 V|T = J 25 °C|T = J 85 ° C|T = J 105 °C|T = J 125 °C|T = J 140 °C||
|I DD (VBAT)|Supply current in VBAT mode|OFF|OFF|0.008|0.01|0.025|0.05|0.3|3.1|7.4|18|34|µA|
|||ON|OFF|1.5|1.7|1.9|1.9|4|28|53|91|110||
|||OFF|ON|0.4|0.5|0.75|0.8|-|-|-|-|-||
|||ON|ON|1.8|2.1|2.8|3.2|-|-|-|-|-||


1. Guaranteed by characterization results.

2. The LDO regulator is used before switching to V BAT mode.

3. The LSE is in Low-drive mode.

DS13315 Rev 5 123/270


239

**Electrical characteristics** **STM32H730xB**

**Typical SMPS efficiency versus load current and temperature**

**Fi** **g** **ure 17. T** **yp** **ical SMPS efficienc** **y** **(** **%** **)** **vs load current** **(** **A** **)** **in Run mode at T** **J** **= 30 °C**






**Fi** **g** **ure 18. T** **yp** **ical SMPS efficienc** **y** **(** **%** **)** **vs load current** **(** **A** **)** **in Run mode at T** **J** **= T** **Jmax**





124/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Figure 19. Typical SMPS efficiency (%) vs load current (A) in Stop and**
**DSto** **p** **modes at T** **J** **= 30 °C**




**Figure 20. Typical SMPS efficiency (%) vs load current (A) in low-power mode at**
**T** **J** **= T** **Jmax**





DS13315 Rev 5 125/270


239

**Electrical characteristics** **STM32H730xB**

**I/O system current consumption**

The current consumption of the I/O system has two components: static and dynamic.

**I/O static current consumption**

All the I/Os used as input with pull-up or pull-down generate a current consumption when
the pin is externally held to the opposite level.

The value of this current consumption can be simply computed by using the pull-up/pulldown resistors values given in *Table 54: I/O static characteristics* .

For the output pins, any internal or external pull-up or pull-down and external load must also
be considered to estimate the current consumption.

An additional I/O current consumption is due to I/Os configured as inputs if an intermediate
voltage level is externally applied. This current consumption is caused by the input Schmitt
trigger circuits used to discriminate the input value. Unless this specific configuration is
required by the application, this supply current consumption can be avoided by configuring
these I/Os in analog mode. This is notably the case of ADC input pins which should be
configured as analog inputs.

**Caution:** Any floating input pin can also settle to an intermediate voltage level or switch inadvertently,
as a result of external electromagnetic noise. To avoid a current consumption related to
floating pins, they must either be configured in analog mode, or forced internally to a definite
digital value. This can be done either by using pull-up/down resistors or by configuring the
pins in output mode.

**I/O dynamic current consumption**

In addition to the internal peripheral current consumption (see *Table 32: Peripheral current*
*consumption in Run mode* ), the I/Os used by an application also contribute to the current
consumption. When an I/O pin switches, it uses the current from the MCU supply voltage to
supply the I/O pin circuitry and to charge/discharge the capacitive load (internal and
external) connected to the pin:

I = V × f × C
SW DDx SW L

where

I SW is the current sunk by a switching I/O to charge/discharge the capacitive load

V DDx is the MCU supply voltage

f SW is the I/O switching frequency

C L is the total capacitance seen by the I/O pin: C = C INT + C EXT

The test pin is configured in push-pull output mode and is toggled by software at a fixed
frequency.

126/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**On-chip peripheral current consumption**

The MCU is placed under the following conditions:

      - At startup, all I/O pins are in analog input configuration.

      - All peripherals are disabled unless otherwise mentioned.

      - The I/O compensation cell is enabled.

      - f rcc_c_ck is the CPU clock. f PCLK = f rcc_c_ck /4, and f HCLK = f rcc_c_ck /2.

The given value is calculated by measuring the difference of current consumption

–
with all peripherals clocked off

–
with only one peripheral clocked on

– f rcc_c_ck = 550 MHz (Scale 0), f rcc_c_ck = 400 MHz (Scale 1), f rcc_c_ck = 300 MHz
(Scale 2), f rcc_c_ck = 170 MHz (Scale 3)

      - The ambient operating temperature is 25 °C and V DD =3.3 V

      - The LDO regulator supplies V CORE .

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode**



|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|AHB3|MDMA|3.70|3.10|2.90|2.60|µA/MHz|
||DMA2D|2.70|2.30|2.10|1.90||
||Flash memory|15.20|14.00|12.00|10.90||
||FMC registers|0.90|0.90|0.80|0.70||
||FMC kernel|7.00|6.10|5.60|5.40||
||OCTOSPI1 registers|1.40|1.30|0.50|0.40||
||OCTOSPI1 kernel|3.10|1.20|0.50|0.20||
||SDMMC1 registers|8.70|7.60|6.90|6.10||
||SDMMC1 kernel|2.10|1.80|1.40|1.20||
||OCTOSPI2 registers|1.40|1.30|0.90|0.60||
||OCTOSPI2 kernel|2.50|1.50|1.40|0.50||
||OTFDEC1|0.80|0.70|0.10|0.10||
||OTFDEC2|0.80|0.70|0.10|0.10||
||AXI SRAM|8.50|7.50|6.90|6.00||


DS13315 Rev 5 127/270


239

**Electrical characteristics** **STM32H730xB**

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode** **(** **continued** **)**




|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|AHB1|DMA1|0.70|0.60|0.50|0.40|µA/MHz|
||DMA2|1.00|0.80|0.70|0.70||
||DMAMUX1|0.10|0.10|0.10|0.10||
||ADC1/2 registers|4.50|4.00|3.60|2.30||
||ADC1/2 kernel|0.90|0.80|0.60|0.40||
||USB1 registers|20.80|17.50|16.50|14.80||
||USB1 kernel|1.20|0.90|0.90|0.90||
||USB1 ULPI kernel|31.00|30.00|29.50|27.00||
||Ethernet|17.30|14.40|13.70|12.30||
|AHB2|DCMI|4.80|4.00|3.80|3.40|µA/MHz|
||CRYP|1.40|1.20|1.10|0.80||
||HASH1|1.70|1.40|1.30|1.00||
||HSEM|0.60|0.60|0.10|0.10||
||RNG1 registers|1.20|1.00|0.90|0.70||
||RNG1 kernel|15.00|13.60|10.00|9.00||
||SDMMC2 registers|15.00|12.20|11.70|10.40||
||SDMMC2 kernel|2.10|1.80|1.40|1.20||
||BDMA|6.50|5.90|4.80|4.30||
||SRAM1|2.40|2.00|1.80|1.60||
||SRAM2|2.70|2.30|2.00|1.80||
||CORDIC|0.80|0.60|0.50|0.50||
||FMAC|2.40|2.10|1.90|1.60||


128/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode** **(** **continued** **)**

|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|AHB4|GPIOA|0.10|0.10|0.10|0.10|µA/MHz|
||GPIOB|0.90|0.80|0.10|0.10||
||GPIOC|0.50|0.10|0.10|0.10||
||GPIOD|0.90|0.80|0.10|0.10||
||GPIOE|0.90|0.80|0.10|0.10||
||GPIOF|0.30|0.10|0.10|0.10||
||GPIOG|0.90|0.80|0.30|0.20||
||GPIOH|0.10|0.10|0.10|0.10||
||GPIOJ|0.90|0.80|0.30|0.20||
||GPIOK|0.80|0.80|0.10|0.10||
||HSEM|0.60|0.60|0.10|0.10||
||BDMA|6.50|5.90|4.80|4.30||
||CRC|0.90|0.30|0.30|0.30||
||ADC3 registers|2.10|1.40|1.30|1.20||
||ADC3 kernel|0.40|0.30|0.30|0.20||
||Backup SRAM|1.80|1.00|1.00|0.80||
|APB3|LTDC|9.00|7.90|7.70|6.40||
||WWDG1|0.60|0.50|0.50|0.50||



DS13315 Rev 5 129/270


239

**Electrical characteristics** **STM32H730xB**

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode** **(** **continued** **)**




|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|APB1|TIM2|4.50|4.40|3.30|3.00|µA/MHz|
||TIM3|3.80|3.20|2.90|2.70||
||TIM4|3.60|3.10|2.60|2.50||
||TIM5|4.10|3.40|3.10|2.90||
||TIM6|1.50|1.10|1.00|1.00||
||TIM7|1.40|1.10|0.90|0.90||
||TIM12|2.30|1.80|1.60|1.60||
||TIM13|1.90|1.40|1.30|1.20||
||TIM14|1.60|1.20|1.10|1.10||
||TIM23|4.60|3.90|3.60|3.40||
||TIM24|4.40|3.80|3.50|3.30||
||LPTIM1 registers|3.50|2.90|2.70|2.60||
||LPTIM1 kernel|2.60|2.30|2.00|1.80||
||SPI2 registers|2.10|1.60|0.90|0.80||
||SPI2 kernel|1.50|1.20|1.10|1.00||
||SPI3 registers|2.40|2.00|1.90|1.80||
||SPDIFRX registers|0.60|0.50|0.50|0.50||
||SPDIFRX kernel|3.50|2.80|2.40|2.20||
||USART2 registers|6.60|5.70|5.20|4.90||
||USART2 kernel|4.80|4.80|4.60|3.80||
||USART3 registers|5.90|5.40|4.60|4.30||
||USART3 kernel|4.00|3.40|3.00|2.90||
||UART4 registers|5.60|4.80|3.50|3.10||
||UART4 kernel|3.80|3.20|3.00|2.40||
||UART5 registers|5.60|4.60|4.40|4.00||
||UART5 kernel|3.90|3.40|3.30|3.20||
||UART7 registers|5.40|4.60|4.20|3.90||
||UART7 kernel|3.80|3.30|3.00|3.00||
||UART8 registers|5.60|4.10|3.50|3.40||
||UART8 kernel|3.60|3.20|3.20|3.10||
||I2C1 registers|0.90|0.60|0.60|0.50||
||I2C1 kernel|2.30|2.00|1.80|1.60||
||I2C2 registers|1.00|0.70|0.60|0.60||


130/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode** **(** **continued** **)**



|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|APB1|I2C2 kernel|2.30|1.90|1.70|1.20|µA/MHz|
||I2C3 registers|0.90|0.60|0.50|0.50||
||I2C3 kernel|2.30|2.00|1.00|1.00||
||I2C5 registers|0.90|0.60|0.50|0.50||
||I2C5 kernel|2.20|2.10|1.90|1.80||
||CEC registers|0.60|0.30|0.20|0.20||
||CEC kernel|0.10|0.10|0.10|0.10||
||DAC1|1.60|1.30|1.10|1.10||
||FDCAN1/2/3 registers|24.10|20.90|18.20|17.40||
||FDCAN1/2/3 kernel|9.90|9.90|9.00|8.00||
||CRS|4.90|3.90|3.50|3.20||
||SWPMI registers|1.10|0.80|0.80|0.80||
||SWPMI kernel|1.50|1.10|1.00|1.00||
||OPAMP|0.50|0.40|0.30|0.20||


DS13315 Rev 5 131/270


239

**Electrical characteristics** **STM32H730xB**

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode** **(** **continued** **)**


|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|APB2|TIM1|5.30|4.40|4.20|3.80|µA/MHz|
||TIM8|5.60|5.40|5.20|3.90||
||USART1 registers|1.80|1.60|1.40|1.10||
||USART1 kernel|3.00|2.90|2.80|2.70||
||USART6 registers|1.90|1.70|1.50|1.20||
||USART6 kernel|4.50|4.00|3.60|3.10||
||UART9 registers|1.70|1.70|1.60|1.10||
||UART9 kernel|3.80|3.30|2.90|2.90||
||USART10 registers|1.80|1.70|1.40|1.10||
||USART10 kernel|3.80|3.30|2.90|2.90||
||SPI1 registers|1.90|1.80|1.40|1.20||
||SPI1 kernel|1.50|1.20|1.10|1.00||
||SPI4 registers|1.80|1.60|1.40|1.10||
||SPI4 kernel|1.50|1.20|1.10|1.00||
||SPI5 registers|1.60|1.60|1.40|1.10||
||SPI5 kernel|1.50|1.20|1.10|1.00||
||TIM15|2.80|2.50|2.30|1.90||
||TIM16|2.00|1.90|1.60|1.30||
||TIM17|2.10|2.00|1.70|1.40||
||SAI1 registers|1.40|1.40|1.20|0.90||
||SAI1 kernel|0.80|0.70|0.70|0.70||
||DFSDM1 registers|5.60|5.40|5.30|4.00||
||DFSDM1 kernel|0.30|0.20|0.20|0.10||
||SYSCFG|1.20|1.10|1.10|1.10||


132/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Table 32. Peri** **p** **heral current consum** **p** **tion in Run mode** **(** **continued** **)**




|Peripheral|Col2|I DD(Typ)|Col4|Col5|Col6|Unit|
|---|---|---|---|---|---|---|
|||VOS0|VOS1|VOS2|VOS3||
|APB4|LPUART1 registers|1.80|0.90|0.80|0.60|µA/MHz|
||LPUART1 kernel|2.40|2.30|2.00|1.90||
||SPI6 registers|2.60|2.30|2.10|1.80||
||SPI6 kernel|1.20|1.10|1.00|0.90||
||I2C4 registers|0.70|0.70|0.60|0.40||
||I2C4 kernel|2.00|1.70|1.70|1.40||
||LPTIM2 registers|1.50|0.70|0.50|0.30||
||LPTIM2 kernel|2.50|2.10|2.00|1.90||
||LPTIM3 registers|2.90|2.60|2.30|1.90||
||LPTIM3 kernel|2.40|2.00|1.90|1.70||
||LPTIM4 registers|2.60|2.30|2.10|1.80||
||LPTIM4 kernel|2.10|1.80|1.70|1.60||
||LPTIM5 registers|2.60|2.30|2.00|1.70||
||LPTIM5 kernel|2.10|1.80|1.60|1.50||
||COMP1/2|0.70|0.30|0.20|0.10||
||VREF|0.10|0.10|0.10|0.10||
||RTC|0.10|0.10|0.10|0.10||
||WWDG1|0.60|0.50|0.50|0.50||
||SAI4 registers|2.40|2.20|2.10|1.70||
||SAI4 kernel|0.90|0.90|0.90|0.70||
||DTS|2.90|2.60|2.30|2.00||


DS13315 Rev 5 133/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.9** **Wake-up time from low-power modes**

The wake-up times given in *Table 33* are measured starting from the wake-up event trigger
up to the first instruction executed by the CPU:

      - For Stop or Sleep modes: the wake-up event is WFE.

      - WKUP (PC1) pin is used to wake-up from Standby, Stop and Sleep modes.

All timings are derived from tests performed under ambient temperature and V DD =3.3 V.

**Table 33. Low-** **p** **ower mode wakeu** **p** **timin** **g** **s**





|Symbol|Parameter|Conditions|Typ(1)|Max(1) (2)|Unit|
|---|---|---|---|---|---|
|t (3) WUSLEEP|Wakeup from Sleep|-|14.00|15.00|CPU clock cycles|
|t (3) WUSTOP|Wakeup from Stop mode|SVOS3, HSI, flash memory in Normal mode|4.6|6.2|µs|
|||SVOS3, HSI, flash memory in low-power mode|12.4|17.4||
|||SVOS4, HSI, flash memory in Normal mode|15.5|21.1||
|||SVOS4, HSI, flash memory in low-power mode|23.3|31.8||
|||SVOS5, HSI, flash memory in Normal mode|39.1|52.6||
|||SVOS5, HSI, flash memory in low-power mode|39.1|52.7||
|||SVOS3, CSI, flash memory in Normal mode|30.0|41.6||
|||SVOS3, CSI, flash memory in low-power mode|40.6|55.0||
|||SVOS4, CSI, flash memory in Normal mode|41.0|55.4||
|||SVOS4, CSI, flash memory in low-power mode|51.5|68.8||
|||SVOS5, CSI, flash memory in Normal mode|67.3|89.5||
|||SVOS5, CSI, flash memory in low-power mode|67.2|89.5||
|t (3) WUSTDBY|Wakeup from Standby mode|-|400.0|504.3||


1. Guaranteed by characterization results.

2. The maximum values have been measured at -40 °C, in worst conditions.

3. The wake-up times are measured from the wake-up event to the point in which the application code reads the first

134/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.10** **External clock source characteristics**

**High-speed external user clock generated from an external source**

In bypass mode the HSE oscillator is switched off and the input pin is a standard I/O.

The external clock signal has to respect the *Table 54: I/O static characteristics* . However,
the recommended clock input waveform is shown in *Figure 21* .

**Table 34. Hi** **g** **h-s** **p** **eed external user clock characteristics** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|f HSE_ext|User external clock source frequency|4|25|50|MHz|
|V HSEH|Digital OSC_IN input high-level voltage|0.7 V DD|-|V DD|V|
|V HSEL|Digital OSC_IN input low-level voltage|V SS|-|0.3 V DD||
|t W(HSE)|OSC_IN high or low time|7|-|-|ns|



1. Guaranteed by design.

**Fi** **g** **ure 21. Hi** **g** **h-s** **p** **eed external clock source AC timin** **g** **dia** **g** **ram**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||






DS13315 Rev 5 135/270


239

**Electrical characteristics** **STM32H730xB**

**Low-speed external user clock generated from an external source**

In bypass mode the LSE oscillator is switched off and the input pin is a standard I/O. The
external clock signal has to respect the *Table 54: I/O static characteristics* . However, the
recommended clock input waveform is shown in *Figure 22* .

**Table 35. Low-s** **p** **eed external user clock characteristics** **[(1)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f LSE_ext|User external clock source frequency|-|-|32.768|1000|kHz|
|V LSEH|OSC32_IN input pin high-level voltage|-|0.7 V DD|-|V DD|V|
|V LSEL|OSC32_IN input pin low-level voltage|-|V SS|-|0.3 V DD||
|t w(LSEH) t w(LSEL)|OSC32_IN high or low time|-|250|-|-|ns|



1. Guaranteed by design.

**Fi** **g** **ure 22. Low-s** **p** **eed external clock source AC timin** **g** **dia** **g** **ram**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||








136/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**High-speed external clock generated from a crystal/ceramic resonator**

The high-speed external (HSE) clock can be supplied with a 4 to 50 MHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
characterization results obtained with typical external components specified in *Table 36* . In
the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).

**Table 36. 4-50 MHz HSE oscillator characteristics** **[(1)]**












|Symbol|Parameter|Operating conditions(2)|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F|Oscillator frequency|-|4|-|50|MHz|
|R F|Feedback resistor|-|-|200|-|kΩ|
|I DD(HSE)|HSE current consumption|During startup(3)|-|-|4|mA|
|||V =3 V, Rm=30 Ω DD C =10 pF at 4 MHz L|-|0.35|-||
|||V =3 V, Rm=30 Ω DD C =10 pF at 8 MHz L|-|0.40|-||
|||V =3 V, Rm=30 Ω DD C =10 pF at 16 MHz L|-|0.45|-||
|||V =3 V, Rm=30 Ω DD C =10 pF at 32 MHz L|-|0.65|-||
|||V =3 V, Rm=30 Ω DD C =10 pF at 48 MHz L|-|0.95|-||
|Gm critmax|Maximum critical crystal gm|Startup|-|-|1.5|mA/V|
|t (4) SU|Start-up time|V is stabilized DD|-|2|-|ms|


1. Guaranteed by design.

2. Resonator characteristics given by the crystal/ceramic resonator manufacturer.

3. This consumption level occurs during the first 2/3 of the t SU(HSE) startup time.

4. t SU(HSE) is the startup time measured from the moment it is enabled (by software) to a stabilized 8 MHz
oscillation is reached. This value is measured for a standard crystal resonator and it can vary significantly
with the crystal manufacturer.

*Note:* *For information on selecting the crystal, refer to application note AN2867 “Oscillator design*
*guide for STM8AF/AL/S, STM32 MCUs and MPUs” available from the ST website*
*www.st.com.*

DS13315 Rev 5 137/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 23. T** **yp** **ical a** **pp** **lication with an 8 MHz cr** **y** **stal**





|8 MHz resonator|Col2|Col3|
|---|---|---|
||||

|Col1|Col2|Col3|
|---|---|---|
||RF|Bias controlled gain|
||||


1. R EXT value depends on the crystal characteristics.

**Low-speed external clock generated from a crystal/ceramic resonator**

The low-speed external (LSE) clock can be supplied with a 32.768 kHz crystal/ceramic
resonator oscillator. All the information given in this paragraph are based on
characterization results obtained with typical external components specified in *Table 37* . In
the application, the resonator and the load capacitors have to be placed as close as
possible to the oscillator pins in order to minimize output distortion and startup stabilization
time. Refer to the crystal resonator manufacturer for more details on the resonator
characteristics (frequency, package, accuracy).

**Table 37. Low-s** **p** **eed external user clock characteristics** **[(1)]**





|Symbol|Parameter|Operating conditions(2)|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F|Oscillator frequency|-|-|32.768|-|kHz|
|I DD|LSE current consumption|LSEDRV[1:0] = 00, Low drive capability|-|290|-|nA|
|||LSEDRV[1:0] = 01, Medium Low drive capability|-|390|-||
|||LSEDRV[1:0] = 10, Medium high drive capability|-|550|-||
|||LSEDRV[1:0] = 11, High drive capability|-|900|-||
|Gm critmax|Maximum critical crystal gm|LSEDRV[1:0] = 00, Low drive capability|-|-|0.5|µA/V|
|||LSEDRV[1:0] = 01, Medium Low drive capability|-|-|0.75||
|||LSEDRV[1:0] = 10, Medium high drive capability|-|-|1.7||
|||LSEDRV[1:0] = 11, High drive capability|-|-|2.7||
|t (3) SU|Startup time|VDD is stabilized|-|2|-|s|


1. Guaranteed by design.

2. Refer to the note and caution paragraphs below the table, and to the application note AN2867 *“Oscillator design guide for*
*STM8AF/AL/S, STM32 MCUs and MPUs”* .

3. t SU is the startup time measured from the moment it is enabled (by software) to a stabilized 32.768k Hz oscillation is
reached. This value is measured for a standard crystal resonator and it can vary significantly with the crystal manufacturer.

138/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

*Note:* *For information on selecting the crystal, refer to the application note AN2867 “Oscillator*
*design guide for STM8AF/AL/S, STM32 MCUs and MPUs” available from the ST website*
*www.st.com.*

**Fi** **g** **ure 24. T** **yp** **ical a** **pp** **lication with a 32.768 kHz cr** **y** **stal**





|Col1|Col2|Col3|
|---|---|---|
|32.768 kHz resonator|||
||||

|Col1|Col2|Col3|
|---|---|---|
||R F|Bias controlled gain|
||||




*1.* *An external resistor is not required between OSC32_IN and OSC32_OUT and it is forbidden to add one.*

**6.3.11** **Internal clock source characteristics**

The parameters given in *Table 38* to *Table 40* are derived from tests performed under
ambient temperature and V DD supply voltage conditions summarized in *Table 12: General*
*operating conditions* .

**48 MHz high-speed internal RC oscillator (HSI48)**

**Table 38. HSI48 oscillator characteristics**




|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f HSI48|HSI48 frequency|V =3.3 V, DD TJ=30 °C|47.5(1)|48|48.5(1)|MHz|
|TRIM(2)|USER trimming step|-|-|0.175|0.250|%|
|USER TRIM COVERAGE(3)|USER TRIMMING coverage|± 32 steps|±4.70|±5.6|-|%|
|DuCy(HSI48)(2)|Duty Cycle|-|45|-|55|%|
|ACCHSI48_REL(3)(4)|Accuracy of the HSI48 oscillator over temperature (factory calibrated)|T =-40 to 125 °C J|–4.5|-|3.5|%|
|∆ (HSI48)(2)(5) VDD|HSI48 oscillator frequency drift with V (6) (the reference is 3.3 V) DD|V =3 to 3.6 V DD|-|0.025|0.05|%|
|||V =1.62 V to 3.6 V DD|-|0.05|0.1||
|t (2) su(HSI48)|HSI48 oscillator start-up time|-|-|2.1|4.0|µs|
|I (2) DD(HSI48)|HSI48 oscillator power consumption|-|-|350|400|µA|
|N jitter(2) T|Next transition jitter Accumulated jitter on 28 cycles(7)|-|-|± 0.15|-|ns|
|P jitter(2) T|Paired transition jitter Accumulated jitter on 56 cycles(7)|-|-|± 0.25|-|ns|


1. Guaranteed by test in production.

2. Guaranteed by design.

3. Guaranteed by characterization results.

4. ∆f HSI = ACCHSI48_REL + ∆ VDD .

DS13315 Rev 5 139/270


239

**Electrical characteristics** **STM32H730xB**

5. ∆f HSI = ACCHSI48_REL + ∆ VDD .

6. These values are obtained by using the formula: (Freq(3.6 V) - Freq(3.0 V)) / Freq(3.0 V) or (Freq(3.6 V) - Freq(1.62 V)) /
Freq(1.62 V).

7. Jitter measurements are performed without clock source activated in parallel.

**64 MHz high-speed internal RC oscillator (HSI)**

**Table 39. HSI oscillator characteristics** **[(1)]**










|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f HSI|HSI frequency|V =3.3 V, T =30 °C DD J|63.7(2)|64|64.3(2)|MHz|
|TRIM|HSI user trimming step|Trimming is not a multiple of 32|-|0.24|0.32|%|
|||Trimming is 128, 256 and 384|−5.2|−1.8|-||
|||Trimming is 64, 192, 320 and 448|−1.4|−0.8|-||
|||Other trimming are a multiple of 32 (not including multiple of 64 and 128)|−0.6|−0.25|-||
|DuCy(HSI)|Duty cycle|-|45|-|55|%|
|Δ VDD (HSI)|HSI oscillator frequency drift over V (the reference is 3.3 V) DD|V =1.62 to 3.6 V DD|−0.12|-|0.03|%|
|Δ TEMP(HSI)|HSI oscillator frequency drift over temperature (the reference is 64 MHz)|T =-20 to 105 °C J|−1(3)|-|1(3)|%|
|||T =−40 to T max °C J J|−2(3)|-|1(3)||
|t (HSI) su|HSI oscillator start-up time|-|-|1.4|2|µs|
|t (HSI) stab|HSI oscillator stabilization time|at 1% of target frequency|-|4|8||
|||at 5% of target frequency|-|-|4||
|I (HSI) DD|HSI oscillator power consumption|-|-|300|400|µA|


1. Guaranteed by design unless otherwise specified.

2. Guaranteed by test in production.

3. Guaranteed by characterization results.

140/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**4 MHz low-power internal RC oscillator (CSI)**

**Table 40. CSI oscillator characteristics** **[(1)]**










|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f CSI|CSI frequency|V =3.3 V, T =30 °C DD J|3.96(2)|4|4.04(2)|MHz|
|TRIM|CSI trimming step|Trimming is not a multiple of 16|-|0.40|0.75|%|
|||Trimming is a multiple of 32|−4.75|−2.75|0.75||
|||Other trimming values not multiple of 16 (excluding multiple of 32)|−0.43|0.00|0.75||
|DuCy(CSI)|Duty cycle|-|45|-|55|%|
|∆ (CSI) TEMP|CSI oscillator frequency drift over temperature|T = 0 to 85 °C J|−3.7(3)|-|4.5(3)|%|
|||T = −40 to 125 °C J|−11(3)|-|7.5(3)||
|∆ (CSI) VDD|CSI oscillator frequency drift over V DD|V = 1.62 to 3.6 V DD|−0.06|-|0.06|%|
|t su(CSI)|CSI oscillator startup time|-|-|1|2|µs|
|t stab(CSI)|CSI oscillator stabilization time (to reach ± 3% of f ) CSI|-|-|-|4|cycle|
|I DD(CSI)|CSI oscillator power consumption|-|-|23|30|µA|


1. Guaranteed by design, unless otherwise specified.

2. Guaranteed by test in production.

3. Guaranteed by characterization results.

**Low-speed internal (LSI) RC oscillator**

**Table 41. LSI oscillator characteristics**




|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f LSI|LSI frequency|V = 3.3 V, T = 25 °C DD J|31.4(1)|32|32.6(1)|kHz|
|||T = –40 to 110 °C, J V = 1.62 to 3.6 V DD|29.76(2)|-|33.6(2)||
|||T = –40 to 125 °C, J V = 1.62 to 3.6 V DD|29.4(2)|-|33.6(2)||
|t (3) su(LSI)|LSI oscillator startup time|-|-|80|130|µs|
|t (3) stab(LSI)|LSI oscillator stabilization time (5% of final value)|-|-|120|170||
|I (3) DD(LSI)|LSI oscillator power consumption|-|-|130|280|nA|


1. Guaranteed by test in production.

2. Guaranteed by characterization results.

3. Guaranteed by design.

DS13315 Rev 5 141/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.12** **PLL characteristics**

The parameters given in *Table 42*, *Table 45* are derived from tests performed under
temperature and V DD supply voltage conditions summarized in *Table 12: General operating*
*conditions* .

**Table 42. PLL1 characteristics** **(** **wide VCO fre** **q** **uenc** **y** **ran** **g** **e** **)** **[(1)]**










|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|f PLL_IN|PLL input clock|-||2|-|16|MHz|
||PLL input clock duty cycle|-||10|-|90|%|
|f PLL_P_OUT|PLL multiplier output clock P|VOS0||1.5|-|550(2)|MHz|
|||VOS1||1.5|-|400(2)||
|||VOS2||1.5|-|300(2)||
|||VOS3||1.5|-|170(2)||
|f VCO_OUT|PLL VCO output|-||192|-|836(3)||
|t LOCK|PLL lock time|Normal mode||15|50|150(3)|µs|
|||Sigma-delta mode (CKIN ≥ 8 MHz)||25|65|170||
|Jitter|Cycle-to-cycle jitter(4)|f = PLL_OUT f /100 VCO_OUT|f VCO_OUT = 192 MHz|-|51|-|ps|
||||f VCO_OUT = 400 MHz|-|19|-||
||||f VCO_OUT = 560 MHz|-|10|-||
||||f VCO_OUT = 800 MHz|-|9|-||
||Period jitter||f VCO_OUT = 192 MHz|-|38|-||
||||f VCO_OUT = 560 MHz|-|8|-||
||||f VCO_OUT = 800 MHz|-|7|-||
||Long term jitter|Normal mode (CKIN = 2 MHz)|f VCO_OUT = 192 MHz|-|0.15|-|%|
||||f VCO_OUT = 400 MHz|-|0.14|-||
||||f VCO_OUT = 832 MHz|-|0.16|-||
|||Sigma-delta mode (CKIN = 16 MHz)|f VCO_OUT = 192 MHz|-|0.17|-||
||||f VCO_OUT = 500 MHz|-|0.08|-||
||||f VCO_OUT = 836 MHz|-|0.06|-||


142/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 42. PLL1 characteristics** **(** **wide VCO fre** **q** **uenc** **y** **ran** **g** **e** **)** **[(1)]** **(** **continued** **)**



|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|I DD(PLL)|PLL power consumption|f = VCO_OUT 560 MHz|V DDA|530|557|670|µA|
||||V CORE|1190|1285|6300||
|||f = VCO_OUT 192 MHz|V DDA|260|286|513||
||||V CORE|309|377|5700||


1. Guaranteed by design unless otherwise specified.



2. This value must be limited to the maximum frequency due to the product limitation.

3. Guaranteed by characterization results.

4. Integer mode only.

**Table 43. PLL1 characteristics** **(** **medium VCO fre** **q** **uenc** **y** **ran** **g** **e** **)** **[(1)]**














|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|f PLL_IN|PLL input clock|-||1|-|2|MHz|
||PLL input clock duty cycle|-||10|-|90|%|
|f PLL_OUT|PLL multiplier output clock P, Q, R|VOS0||1.17|-|210|MHz|
|||VOS1||1.17|-|210||
|||VOS2||1.17|-|210||
|||VOS3||1.17|-|200||
|f VCO_OUT|PLL VCO output|-||150|-|420||
|t LOCK|PLL lock time|Normal mode||-|60(2)|100(2)|µs|
|||Sigma-delta mode||forbidden||||
|Jitter|Cycle-to-cycle jitter(3)|-|f = VCO_OUT 150 MHz|-|145|-|±ps|
||||f = VCO_OUT 300 MHz|-|91|-||
||||f = VCO_OUT 400 MHz|-|64|-||
||||f = VCO_OUT 420 MHz|-|63|-||
||Period jitter|f = PLL_OUT 50 MHz|f = VCO_OUT 150 MHz|-|55|-|±-ps|
||||f = VCO_OUT 400 MHz|-|30|-||
||Long term jitter|Normal mode|f = VCO_OUT 400 MHz|-|±0.3|-|%|
|I(PLL)|PLL power consumption on V DD|f = VCO_OUT 420 MHz|VDD|-|440|1150|µA|
||||VCORE|-|530|-||
|||f = VCO_OUT 150 MHz|VDD|-|180|500||
||||VCORE|-|200|-||


DS13315 Rev 5 143/270


239

**Electrical characteristics** **STM32H730xB**

1. Guaranteed by design unless otherwise specified.

2. Guaranteed by characterization results.

3. Integer mode only.

**Table 44. PLL2 and PLL3 characteristics** **(** **wide VCO frequency range)** **[(1)]**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|f PLL_IN|PLL input clock|-||2|-|16|MHz|
||PLL input clock duty cycle|-||10|-|90|%|
|f PLL_OUT|PLL multiplier output clock P, Q, R|VOS0||1.5|-|550(2)|MHz|
|||VOS1||1.5|-|400(2)||
|||VOS2||1.5|-|300(2)||
|||VOS3||1.5|-|170(2)||
|f VCO_OUT|PLL VCO output|-||192|-|960(3)||
|t LOCK|PLL lock time|Normal mode||-|50|150(3)|µs|
|||Sigma-delta mode (f PLL_IN ≥ 8 MHz)||-|58|166(3)||
|Jitter|Cycle-to-cycle jitter(4)|f = 192 MHz VCO_OUT||-|134|-|±ps|
|||f = 200 MHz VCO_OUT||-|134|-||
|||f = 400 MHz VCO_OUT||-|76|-||
|||f = 800 MHz VCO_OUT||-|39|-||
||Long term jitter|Normal mode (f = PLL_IN 2 MHz)|f = VCO_OUT 560 MHz|-|±0.2|-|%|
|||Normal mode (f = PLL_IN 16 MHz)|f = VCO_OUT 560 MHz|-|±0.8|-||
|||Sigma-delta mode (f = PLL_IN 2 MHz)|f = VCO_OUT 560 MHz|-|±0.2|-||
|||Sigma-delta mode (f = PLL_IN 16 MHz)|f = VCO_OUT 560 MHz|-|±0.8|-||
|I (3) DD(PLL)|PLL power consumption|f = VCO_OUT 836 MHz|V DD|-|590|1500|µA|
||||V CORE|-|720|-||
|||f = VCO_OUT 192 MHz|V DD|-|180|600||
||||V CORE|-|280|-||


1. Guaranteed by design unless otherwise specified.

2. This value must be limited to the maximum frequency due to the product limitation.

144/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

3. Guaranteed by characterization results.

4. Integer mode only.

**Table 45. PLL2 and PLL3 characteristics** **(** **medium VCO fre** **q** **uenc** **y** **ran** **g** **e** **)** **[(1)]**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|f PLL_IN|PLL input clock|-||1|-|2|MHz|
||PLL input clock duty cycle|-||10|-|90|%|
|f PLL_OUT|PLL multiplier output clock P, Q, R|VOS0||1.17|-|210|MHz|
|||VOS1||1.17|-|210|-|
|||VOS2||1.17|-|210|-|
|||VOS3||1.17|-|200|-|
|f VCO_OUT|PLL VCO output|-||150|-|420|-|
|t LOCK|PLL lock time|Normal mode||-|60|100(2)|µs|
|||Sigma-delta mode||forbidden||||
|Jitter|Cycle-to-cycle jitter(3)|f = 150 MHz VCO_OUT||-|145|-|±ps|
|||f = 200 MHz VCO_OUT||-|91|-||
|||f = 400 MHz VCO_OUT||-|64|-||
|||f = 420 MHz VCO_OUT||-|63|-||
||Period jitter|f = PLL_OUT 50 MHz|f = VCO_OUT 150 MHz|-|55|-|±ps|
|||f = 400 MHz VCO_OUT||-|30|-||
||Long term jitter|Normal mode|f = VCO_OUT 400 MHz|-|±0.3|-|%|
|I DD(PLL)|PLL power consumption on V DD|f = VCO_OUT 420 MHz|V DD|-|440|1150|µA|
||||V CORE|-|530|-||
|||f = VCO_OUT 150 MHz|V DD|-|180|500||
||||V CORE|-|200|-||


1. Guaranteed by design unless otherwise specified.

2. Guaranteed by characterization results.

3. Integer mode only.


DS13315 Rev 5 145/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.13** **Memory characteristics**

**Flash memory**

The characteristics are given at T J = –40 to 125 °C unless otherwise specified.

The devices are shipped to customers with the flash memory erased.

**Table 46. Flash memor** **y** **characteristics**



|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|I DD|Supply current|Write / Erase 8-bit mode|-|6.5|-|mA|
|||Write / Erase 16-bit mode|-|11.5|-||
|||Write / Erase 32-bit mode|-|20|-||
|||Write / Erase 64-bit mode|-|35|-||


**Table 47. Flash memor** **y** **p** **ro** **g** **rammin** **g**



|Symbol|Parameter|Conditions|Min(1)|Typ|Max(1)|Unit|
|---|---|---|---|---|---|---|
|t prog|Word (266 bits) programming time|Program/erase parallelism x 8|-|290|580(2)|µs|
|||Program/erase parallelism x 16|-|180|360||
|||Program/erase parallelism x 32|-|130|260||
|||Program/erase parallelism x 64|-|100|200||
|t ERASE|Sector (128 Kbytes) erase time|Program/erase parallelism x 8|-|2|4|s|
|||Program/erase parallelism x 16|-|1.8|3.6||
|||Program/erase parallelism x 32|-|1.1|2.2||
|t ME|Mass erase time (1 Mbyte)|Program/erase parallelism x 8|-|13|26||
|||Program/erase parallelism x 16|-|8|16||
|||Program/erase parallelism x 32|-|6|12||
|||Program/erase parallelism x 64|-|5|10||
|V prog|Programming voltage|Program parallelism x 8|1.62|-|3.6|V|
|||Program parallelism x 16|||||
|||Program parallelism x 32|||||
|||Program parallelism x 64|1.8|-|3.6||


1. Guaranteed by characterization results.






2. The maximum programming time is measured after 10K erase operations.

**Table 48. Flash memor** **y** **endurance and data retention**

|Symbol|Parameter|Conditions|Min(1)|Unit|
|---|---|---|---|---|
|N END|Endurance|T = –40 to +125 °C J|10|kcycles|
|t RET|Data retention|1 kcycle at T = 85 °C A|30|Years|
|||10 kcycles at T = 55 °C A|20||



146/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

1. Guaranteed by characterization results.

**6.3.14** **EMC characteristics**

Susceptibility tests are performed on a sample basis during device characterization.

**Functional EMS (electromagnetic susceptibility)**

While a simple application is executed on the device (toggling 2 LEDs through I/O ports).
the device is stressed by two electromagnetic events until a failure occurs. The failure is
indicated by the LEDs:

      - **Electrostatic discharge (ESD)** (positive and negative) is applied to all device pins until
a functional disturbance occurs. This test is compliant with the IEC 61000-4-2 standard.

      - **FTB** : A burst of fast transient voltage (positive and negative) is applied to V DD and V SS
through a 100 pF capacitor, until a functional disturbance occurs. This test is compliant
with the IEC 61000-4-4 standard.

A device reset allows normal operations to be resumed.

The test results are given in *Table 49* . They are based on the EMS levels and classes
defined in application note AN1709 “ *EMC design guide for STM8, STM32 and Legacy*
*MCUs* ”.

**Table 49. EMS characteristics**



|Symbol|Parameter|Conditions|Level/ Class|
|---|---|---|---|
|V FESD|Voltage limits to be applied on any I/O pin to induce a functional disturbance|V = 3.3 V, T = 25 °C, DD A LQFP176, conforming to IEC 61000-4-2|3B|
|V FTB|Fast transient voltage burst limits to be applied through 100 pF on V and V pins to induce a DD SS functional disturbance|V = 3.3 V, T = 25 °C, DD A LQFP176, conforming to IEC 61000-4-4|5A|


As a consequence, it is recommended to add a serial resistor (1 kΏ) located as close as
possible to the MCU to the pins exposed to noise (connected to tracks longer than 50 mm
on PCB).

**Designing hardened software to avoid noise problems**

EMC characterization and optimization are performed at component level with a typical
application environment and simplified MCU software. It should be noted that good EMC
performance is highly dependent on the user application and the software in particular.

Therefore, it is recommended that the user applies EMC software optimization and
prequalification tests in relation with the EMC level requested for his application.

**Software recommendations**

The software flowchart must include the management of runaway conditions such as:

- Corrupted program counter

- Unexpected reset

- Critical Data corruption (control registers...)

DS13315 Rev 5 147/270


239

**Electrical characteristics** **STM32H730xB**

**Prequalification trials**

Most of the common failures (unexpected reset and program counter corruption) can be
reproduced by manually forcing a low state on the NRST pin or the Oscillator pins for 1
second.

To complete these trials, ESD stress can be applied directly on the device, over the range of
specification values. When unexpected behavior is detected, the software can be hardened
to prevent unrecoverable errors occurring (see application note AN1015 *“Software*
*techniques for improving microcontrollers EMC performance”).*

**Electromagnetic Interference (EMI)**

The electromagnetic field emitted by the device are monitored while a simple application,
executing EEMBC code, is running. This emission test is compliant with SAE IEC61967-2
standard, which specifies the test board and the pin loading.

**Table 50. EMI characteristics for f** **HSE** **= 8 MHz and f** **CPU** **= 550 MHz**





|Symbol|Parameter|Conditions|Monitored frequency band|Max|Unit|
|---|---|---|---|---|---|
|S EMI|Peak level(1)|V = 3.6 V, T = 25 °C, LQFP176 package, DD A compliant with IEC61967-2|0.1 to 30 MHz|14|dBµV|
||||30 to 130 MHz|20||
||||130 MHz to 1 GHz|27||
||||1 GHz to 2 GHz|17||
||Level(2)||0.1 MHz to 2 GHz|2.5|-|


1. Refer to AN1709 “EMI radiated test” chapter.

2. Refer to AN1709 “EMI level classification” chapter.

148/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.15** **Absolute maximum ratings (electrical sensitivity)**

Based on three different tests (ESD, LU) using specific measurement methods, the device is
stressed in order to determine its performance in terms of electrical sensitivity.

**Electrostatic discharge (ESD)**

Electrostatic discharges (a positive then a negative pulse) are applied to the pins of each
sample according to each pin combination. This test conforms to the ANSI/ESDA/JEDEC
JS-001 and ANSI/ESDA/JEDEC JS-002 standards.

**Table 51. ESD absolute maximum ratin** **g** **s**




|Symbol|Ratings|Conditions|Packages|Class|Maximum value(1)|Unit|
|---|---|---|---|---|---|---|
|V ESD(HBM)|Electrostatic discharge voltage (human body model)|T = 25 °C conforming to A ANSI/ESDA/JEDEC JS-001|Packages with SMPS|1C|1000(2)|V|
||||Packages without SMPS|2|2000||
|V ESD(CDM)|Electrostatic discharge voltage (charge device model)|T = +25 °C conforming to A ANS I/ESDA/JEDEC JS-002|All LQFP packages|C1|250||
||||All BGA and WLCSP packages|C2a|500||


1. Guaranteed by characterization results.




2. Excluding V FBSMPS,the maximum value is 2000 V.

**Static latchup**

Two complementary static tests are required on six parts to assess the latchup
performance:

       - A supply overvoltage is applied to each power supply pin

       - A current injection is applied to each input, output and configurable I/O pin

These tests are compliant with JESD78 IC latchup standard.

**Table 52. Electrical sensitivities**

|Symbol|Parameter|Conditions|Class|
|---|---|---|---|
|LU|Static latchup class|Conforming to JESD78, T =T J JMax|II level A|



DS13315 Rev 5 149/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.16** **I/O current injection characteristics**

As a general rule, a current injection to the I/O pins, due to external voltage below V SS or
above V DD (for standard, 3.3 V-capable I/O pins) should be avoided during the normal
product operation. However, in order to give an indication of the robustness of the
microcontroller in cases when an abnormal injection accidentally happens, susceptibility
tests are performed on a sample basis during the device characterization.

**Functional susceptibility to I/O current injection**

While a simple application is executed on the device, the device is stressed by injecting
current into the I/O pins programmed in floating input mode. While current is injected into
the I/O pin, one at a time, the device is checked for functional failures.

The failure is indicated by an out of range parameter: ADC error above a certain limit (higher
than 5 LSB TUE), out of conventional limits of induced leakage current on adjacent pins (out
of –5 µA/+0 µA range), or other functional failure (for example reset, oscillator frequency
deviation).

The following tables are the compilation of the SIC1/SIC2 and functional ESD results.

Negative induced A negative induced leakage current is caused by negative injection and
positive induced leakage current by positive injection.

**Table 53. I/O current in** **j** **ection susce** **p** **tibilit** **y** **[(1)]**






|Symbol|Description|Functional susceptibility|Col4|Unit|
|---|---|---|---|---|
|||Negative injection|Positive injection||
|I INJ|PA12, PE8|5|0|mA|
||PC4, PE12, PF15, PH0|0|NA||
||PA0, PA0_C, PA1, PA1_C, PC2, PC2_C, PC3, PC3_C, PA4, PA5, PE7, PG1, PH4, PH5, BOOT0|0|0||
||All other I/Os|5|NA||


1. Guaranteed by characterization results.

**6.3.17** **I/O port characteristics**

**General input/output characteristics**

Unless otherwise specified, the parameters given in *Table 54: I/O static characteristics* are
derived from tests performed under the conditions summarized in *Table 12: General*
*operating conditions* . All I/Os are CMOS and TTL compliant (except for BOOT0).

*Note:* *For information on GPIO configuration, refer to application note AN4899 “STM32 GPIO*
*configuration for hardware settings and low-power consumption”, available from the ST*
*website www.st.com.*

150/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 54. I/O static characteristics**



















|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V IL|I/O input low level voltage except BOOT0|1.62 V<V <3.6 V DD|-|-|0.3V (1) DD|V|
||I/O input low level voltage except BOOT0||-|-|0.4V −0.1 DD (2)||
||BOOT0 I/O input low level voltage||-|-|0.19V +0.1 DD (2)||
|V IH|I/O input high level voltage except BOOT0 and Pxy_C I/Os|1.62 V<V <3.6 V DD|0.7V (1) DD|-|-|V|
||Pxy_C pin input high level voltage||0.7V (3) DD||||
||I/O input high level voltage except BOOT0||0.47V + DD 0.25(2)|-|-||
||BOOT0 I/O input high level voltage||0.17V + DD 0.6(2)|-|-||
|V (2) HYS|TT_xx, FT_xxx and NRST I/O input hysteresis|1.62 V< V <3.6 V DD|-|250|-|mV|
||BOOT0 I/O input hysteresis||-|200|-||
|I (4) lkg|FT_xx Input leakage current(2)|0< V ≤ Max(V )(9) IN DDXXX|-|-|+/-250|nA|
|||Max(V ) < V ≤ 5.5 V DDXXX IN (5)(6)(9)|-|-|1500||
||FT_u IO|0< V ≤ Max(V )(9) IN DDXXX|-|-|+/- 350||
|||Max(V ) < V ≤ 5.5 V DDXXX IN (5)(6)(9)|-|-|5000(7)||
||TT_xx Input leakage current|0< V ≤ Max(V ) (9) IN DDXXX|-|-|+/-250||
||VPP (BOOT0 alternate function)|0< V ≤ V IN DD|-|-|15||
|||V < V ≤ 9 V DD IN|||35||
|R PU|Weak pull-up equivalent resistor(8)|V =V IN SS|30|40|50|kΩ|
|R PD|Weak pull-down equivalent resistor(8)|V =V (9) IN DD|30|40|50||
|C IO|I/O pin capacitance|-|-|5|-|pF|


1. Compliant with CMOS requirements.

2. Guaranteed by design.

3. To use these I/Os in digital input mode, V DD must respect the following condition: 0.7 V DD < V DDA + 0.3 V.

4. This parameter represents the pad leakage of the I/O itself. The total product pad leakage is provided by the following
formula: I Total_Ieak_max = 10 μA + [number of I/Os where V IN is applied on the pad] ₓ I lkg(Max) .

5. All FT_xx IO except FT_lu, FT_u and PC3.

6. V IN must be less than Max(VDDXXX) + 3.6 V.

7. To sustain a voltage higher than MIN(V DD, V DDA, V DD33USB ) +0.3 V, the internal pull-up and pull-down resistors must be
disabled.

8. The pull-up and pull-down resistors are designed with a true resistance in series with a switchable PMOS/NMOS. This
PMOS/NMOS contribution to the series resistance is minimal (~10% order).

DS13315 Rev 5 151/270


239

**Electrical characteristics** **STM32H730xB**

9. Max(VDDXXX) is the maximum value of all the I/O supplies.

All I/Os are CMOS and TTL compliant (no software configuration required). Their
characteristics cover more than the strict CMOS-technology or TTL parameters. The
coverage of these requirements for FT I/Os is shown in *Figure 25* .

**Fi** **g** **ure 25. V** **IL** **/V** **IH** **for all I/Os exce** **p** **t BOOT0**




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
||||||.7 V DD||TLL re|quirement:|VIHmin = 2 V|
||||C M O S re q|u ire o m n e n t: sim V u|la IHm tio in= n 0 V IHm in|= 0 .4 7 V DD+ 0|.2 5|||
||||B a|se d o|n sim u la tio n|V ILm ax= 0 .4 .3 V|V DD DD-0 .1|||
|||||B C a M se O d S|re q u ire m e n|t: V ILm ax= 0||||
||||||||TLL req|uirement: VI|Lmin = 0.8 V|
|||||||||||


**Output driving current**

The GPIOs (general purpose input/outputs) can sink or source up to ± 8 mA, and sink or
source up to ± 20 mA (with a relaxed V OL /V OH ).

In the user application, the number of I/O pins which can drive current must be limited to
respect the absolute maximum rating specified in *Section 6.2* . In particular:

       - The sum of the currents sourced by all the I/Os on V DD, plus the maximum Run
consumption of the MCU sourced on V DD, cannot exceed the absolute maximum rating
ΣI VDD (see *Table 10* ).

       - The sum of the currents sunk by all the I/Os on V SS plus the maximum Run
consumption of the MCU sunk on V SS cannot exceed the absolute maximum rating
ΣI VSS (see *Table 10* ).

152/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Output voltage levels**

Unless otherwise specified, the parameters given in *Table 55: Output voltage characteristics*
*for all I/Os except PC13, PC14 and PC15* and *Table 56: Output voltage characteristics for*
*PC13, PC14 and PC15* are derived from tests performed under ambient temperature and
V DD supply voltage conditions summarized in *Table 12: General operating conditions* . All
I/Os are CMOS and TTL compliant.

**Table 55. Out** **p** **ut volta** **g** **e characteristics for all I/Os except PC13, PC14 and PC15** **[(1)]**





|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|V OL|Output low level voltage|CMOS port(2) I = 8 mA IO 2.7 V ≤ V ≤ 3.6 V DD|-|0.4|V|
|V OH|Output high level voltage|CMOS port(2) I = −8 mA IO 2.7 V ≤ V ≤ 3.6 V DD|V − 0.4 DD|-||
|V (3) OL|Output low level voltage|TTL port(2) I = 8 mA IO 2.7 V ≤ V ≤ 3.6 V DD|-|0.4||
|V (3) OH|Output high level voltage|TTL port(2) I = −8 mA IO 2.7 V ≤ V ≤ 3.6 V DD|2.4|-||
|V (3) OL|Output low level voltage|I = 20 mA IO 2.7 V ≤ V ≤ 3.6 V DD|-|1.3||
|V (3) OH|Output high level voltage|I = −20 mA IO 2.7 V ≤ V ≤ 3.6 V DD|V − 1.3 DD|-||
|V (3) OL|Output low level voltage|I = 4 mA IO 1.62 V ≤ V ≤ 3.6 V DD|-|0.4||
|V (3) OH|Output high level voltage|I = −4 mA IO 1.62 V ≤V < 3.6 V DD|V − 0.4 DD|-||
|V (3) OL|Output low level voltage for Pxy_C pins|I = 1 mA IO 1.62 V ≤ V < 3.6 V DD|-|0.4||
|V (3) OH|Output high level voltage for Pxy_C pins(4)|I = 1 mA IO 1.62 V ≤ V < 3.6 V DD|Min(V − 0.4, DD V + 0.3) DDA|-||
|V (3) OLFM+|Output low level voltage for an FTf I/O pin in FM+ mode|I = 20 mA IO 2.3 V ≤ V ≤ 3.6 V DD|-|0.4||
|||I = 10 mA IO 1.62 V ≤ V ≤ 3.6 V DD|-|0.4||


1. The IIO current sourced or sunk by the device must always respect the absolute maximum rating specified in *Table 9:*
*Voltage characteristics*, and the sum of the currents sourced or sunk by all the I/Os (I/O ports and control pins) must always
respect the absolute maximum ratings ΣIIO.

2. TTL and CMOS outputs are compatible with JEDEC standards JESD36 and JESD52.

3. Guaranteed by design.

4. If V DDA + 0.3V < V DD - 0.4 V, an injection current from V DD to V DDA can be observed that can perturb the analog
peripherals.

DS13315 Rev 5 153/270


239

**Electrical characteristics** **STM32H730xB**

**Table 56. Out** **p** **ut volta** **g** **e characteristics for PC13, PC14 and PC15** **(1)**




|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|V OL|Output low level voltage|CMOS port(2) I = 3 mA IO 2.7 V≤ V ≤3.6 V DD|-|0.4|V|
|V OH|Output high level voltage|CMOS port(2) I = −3 mA IO 2.7 V≤ V ≤3.6 V DD|V −0.4 DD|-||
|V (3) OL|Output low level voltage|TTL port(2) I = 3 mA IO 2.7 V≤ V ≤3.6 V DD|-|0.4||
|V (2) OH|Output high level voltage|TTL port(2) I = −3 mA IO 2.7 V≤ V ≤3.6 V DD|2.4|-||
|V (2) OL|Output low level voltage|I = 1.5 mA IO 1.62 V≤ V ≤3.6 V DD|-|0.4||
|V (2) OH|Output high level voltage|I = −1.5 mA IO 1.62 V≤ V ≤3.6 V DD|V −0.4 DD|-||


1. The IIO current sourced or sunk by the device must always respect the absolute maximum rating specified in *Table 9:*
*Voltage characteristics*, and the sum of the currents sourced or sunk by all the I/Os (I/O ports and control pins) must always
respect the absolute maximum ratings ΣIIO.

2. TTL and CMOS outputs are compatible with JEDEC standards JESD36 and JESD52.

3. Guaranteed by design.

154/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Output buffer timing characteristics (HSLV option disabled)**

The HSLV bit of SYSCFG_CCCSR register can be used to optimize the I/O speed when the
product voltage is below 2.7 V.

**Table 57. Out** **p** **ut timin** **g** **characteristics** **(** **HSLV OFF** **)** **[(1)]**





|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|00|F (2) max|Maximum frequency|C=50 pF, 2.7 V≤ V ≤3.6 V DD|-|12|MHz|
||||C=50 pF, 1.62 V≤V ≤2.7 V DD|-|3||
||||C=30 pF, 2.7 V≤V ≤3.6 V DD|-|12||
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|3||
||||C=10 pF, 2.7 V≤V ≤3.6 V DD|-|16||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|4||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 2.7 V≤ V ≤3.6 V DD|-|16.6|ns|
||||C=50 pF, 1.62 V≤V ≤2.7 V DD|-|33.3||
||||C=30 pF, 2.7 V≤V ≤3.6 V DD|-|13.3||
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|25||
||||C=10 pF, 2.7 V≤V ≤3.6 V DD|-|10||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|20||
|01|F (2) max|Maximum frequency|C=50 pF, 2.7 V≤ V ≤3.6 V DD|-|60|MHz|
||||C=50 pF, 1.62 V≤V ≤2.7 V DD|-|15||
||||C=30 pF, 2.7 V≤V ≤3.6 V DD|-|80||
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|15||
||||C=10 pF, 2.7 V≤V ≤3.6 V DD|-|110||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|20||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 2.7 V≤ V ≤3.6 V DD|-|5.2|ns|
||||C=50 pF, 1.62 V≤V ≤2.7 V DD|-|10||
||||C=30 pF, 2.7 V≤V ≤3.6 V DD|-|4.2||
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|7.5||
||||C=10 pF, 2.7 V≤V ≤3.6 V DD|-|2.8||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|5.2||


DS13315 Rev 5 155/270


239

**Electrical characteristics** **STM32H730xB**

**Table 57. Out** **p** **ut timin** **g** **characteristics** **(** **HSLV OFF** **)** **[(1)]** **(** **continued** **)**





|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|10|F (2) max|Maximum frequency|C=50 pF, 2.7 V≤V ≤3.6 V(4) DD|-|85|MHz|
||||C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|35||
||||C=30 pF, 2.7 V≤V ≤3.6 V(4) DD|-|110||
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|40||
||||C=10 pF, 2.7 V≤V ≤3.6 V(4) DD|-|166||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|100||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 2.7 V≤V ≤3.6 V(4) DD|-|3.8|ns|
||||C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|6.9||
||||C=30 pF, 2.7 V≤V ≤3.6 V(4) DD|-|2.8||
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|5.2||
||||C=10 pF, 2.7 V≤V ≤3.6 V(4) DD|-|1.8||
||||C=10 pF, 1.62 V≤V ≤2.7 Vv DD|-|3.3||
|11|F (2) max|Maximum frequency|C=50 pF, 2.7 V≤V ≤3.6 Vv DD|-|100|MHz|
||||C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|50||
||||C=30 pF, 2.7 V≤V ≤3.6 Vv DD|-|133||
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|66||
||||C=10 pF, 2.7 V≤V ≤3.6 V(4) DD|-|220||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|85||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 2.7 V≤V ≤3.6 V(4) DD|-|3.3|ns|
||||C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|6.6||
||||C=30 pF, 2.7 V≤V ≤3.6 V(4) DD|-|2.4||
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|4.5||
||||C=10 pF, 2.7 V≤V ≤3.6 V(4) DD|-|1.5||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|2.7||


1. Guaranteed by design.

2. The maximum frequency is achieved with a duty cycle of 45 to 55 %, when loaded by the specified capacitance.

3. The fall and rise times are defined between 90% and 10% and between 10% and 90% of the output waveform, respectively.

4. Compensation system enabled.

156/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Output buffer timing characteristics (HSLV option enabled)**

**Table 58. Out** **p** **ut timin** **g** **characteristics** **(** **HSLV ON** **)** **[(1)]**




|Speed|Symbol|Parameter|conditions|Min|Max|Unit|
|---|---|---|---|---|---|---|
|00|F (2) max|Maximum frequency|C=50 pF, 1.62 V≤V ≤2.7 V DD|-|10|MHz|
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|10||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|10||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 1.62 V≤V ≤2.7 V DD|-|11|ns|
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|9||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|6.6||
|01|F (2) max|Maximum frequency|C=50 pF, 1.62 V≤V ≤2.7 V DD|-|50|MHz|
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|58||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|66||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 1.62 V≤V ≤2.7 V DD|-|6.6|ns|
||||C=30 pF, 1.62 V≤V ≤2.7 V DD|-|4.8||
||||C=10 pF, 1.62 V≤V ≤2.7 V DD|-|3||
|10|F (2) max|Maximum frequency|C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|55|MHz|
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|80||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|133||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|5.8|ns|
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|4||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|2.4||
|11|F (2) max|Maximum frequency|C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|60|MHz|
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|90||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|175||
||t/t(3) r f|Output high to low level fall time and output low to high level rise time|C=50 pF, 1.62 V≤V ≤2.7 V(4) DD|-|5.3|ns|
||||C=30 pF, 1.62 V≤V ≤2.7 V(4) DD|-|3.6||
||||C=10 pF, 1.62 V≤V ≤2.7 V(4) DD|-|1.9||


1. Guaranteed by design.

2. The maximum frequency is achieved with a duty cycle of 45 to 55 %, when loaded by the specified capacitance.

3. The fall and rise times are defined between 90% and 10% and between 10% and 90% of the output waveform, respectively.

4. Compensation system enabled.

DS13315 Rev 5 157/270


239

**Electrical characteristics** **STM32H730xB**

**Analog switch between ports Pxy_C and Pxy**

PA0_C, PA1_C, PC2_C and PC3_C can be connected internally to PA0, PA1, PC2 and
PC3, respectively (refer to SYSCFG_PMCR register in RM0468 reference manual). The
switch is controlled by V DDSWITCH voltage level. It is defined through BOOSTVDDSEL bit of
SYSCFG_PMCR. If the switch is closed the switch characteristics are given in the table
below.

**Table 59. Px** **y_** **C and Px** **y** **analo** **g** **switch characteristics**



|Parameter|Conditions|Col3|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|Switch impedance|Switch control boosted||-|-|315|Ω|
||Switch control not boosted|V > 2.7 V DDSWITCH|-|-|315||
|||V > 2.4 V DDSWITCH|-|-|335||
|||V > 2.0 V DDSWITCH|-|-|390||
|||V > 1.8 V DDSWITCH|-|-|445||
|||V > 1.62 V DDSWITCH|-|-|550||


**6.3.18** **NRST pin characteristics**

The NRST pin input driver uses CMOS technology. It is connected to a permanent pull-up
resistor, R PU (see *Table 54: I/O static characteristics* ).

Unless otherwise specified, the parameters given in *Table 60* are derived from tests
performed under the ambient temperature and V DD supply voltage conditions summarized
in *Table 12: General operating conditions* .

**Table 60. NRST** **p** **in characteristics**






|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|R (2) PU|Weak pull-up equivalent resistor(1)|V = V IN SS|30|40|50|㏀|
|V (2) F(NRST)|NRST Input filtered pulse|1.71 V < V < 3.6 V DD|-|-|50|ns|
|V (2) NF(NRST)|NRST Input not filtered pulse|1.71 V < V < 3.6 V DD|350|-|-||
|||1.62 V < V < 3.6 V DD|1000|-|-||


1. The pull-up is designed with a true resistance in series with a switchable PMOS. This PMOS contribution
to the series resistance must be minimum (~10% order) .

2. Guaranteed by design.

158/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 26. Recommended NRST** **p** **in** **p** **rotection**







1. The reset network protects the device against parasitic resets.

2. The user must ensure that the level on the NRST pin can go below the V IL(NRST) max level specified in
*Table 54* . Otherwise the reset is not taken into account by the device.

**6.3.19** **FMC characteristics**

Unless otherwise specified, the parameters given in *Table 61* to *Table 74* for the FMC
interface are derived from tests performed under the ambient temperature, f HCLK frequency
and V DD supply voltage conditions summarized in *Table 12: General operating conditions*,
with the following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 11

      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.

      - HSLV activated when V DD ≤ 2.7 V

      - VOS level set to VOS0.

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output alternate
function characteristics.

**Asynchronous waveforms and timings**

*Figure 27* through *Figure 29* represent asynchronous waveforms and *Table 61* through
*Table 68* provide the corresponding timings. The results shown in these tables are obtained
with the following FMC configuration:

      - AddressSetupTime = 0x1

      - AddressHoldTime = 0x1

      - DataSetupTime = 0x1 (except for asynchronous NWAIT mode, DataSetupTime = 0x5)

      - BusTurnAroundDuration = 0x0

      - Capacitive load C L = 30 pF

In all timing tables, the T KERCK is the f mc_ker_ck clock period.

DS13315 Rev 5 159/270


239

**Electrical characteristics** **STM32H730xB**

**Table 61. As** **y** **nchronous non-multi** **p** **lexed SRAM/PSRAM/NOR read timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|3T –1 fmc_ker_ck|3T +1 fmc_ker_ck|ns|
|t v(NOE_NE)|FMC_NEx low to FMC_NOE low|0|0.5||
|t w(NOE)|FMC_NOE low time|2T –1 fmc_ker_ck|2T +1 fmc_ker_ck||
|t h(NE_NOE)|FMC_NOE high to FMC_NE high hold time|T fmc_ker_ck|-||
|t v(A_NE)|FMC_NEx low to FMC_A valid|-|0.5||
|t h(A_NOE)|Address hold time after FMC_NOE high|2T fmc_ker_ck|-||
|t su(Data_NE)|Data to FMC_NEx high setup time|T +14 fmc_ker_ck|-||
|t su(Data_NOE)|Data to FMC_NOEx high setup time|13|-||
|t h(Data_NOE)|Data hold time after FMC_NOE high|0|-||
|t h(Data_NE)|Data hold time after FMC_NEx high|0|-||
|t v(NADV_NE)|FMC_NEx low to FMC_NADV low|-|4||
|t w(NADV)|FMC_NADV low time|-|T +1 fmc_ker_ck||


1. Guaranteed by characterization results.

**Table 62. Asynchronous non-multiplexed SRAM/PSRAM/NOR read-NWAIT**
**timin** **g** **s** **[(1)(2)]**




|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|7T –1 fmc_ker_ck|7T +1 fmc_ker_ck|ns|
|t w(NOE)|FMC_NOE low time|5T –1 fmc_ker_ck|5T +1 fmc_ker_ck||
|t w(NWAIT)|FMC_NWAIT low time|T – 0.5 fmc_ker_ck|-||
|t su(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|4T +9 fmc_ker_ck|-||
|t h(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|3T +12 fmc_ker_ck|-||


1. Guaranteed by characterization results.

2. N WAIT pulse width is equal to 1 fmc_ker_ck cycle.

160/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 27. As** **y** **nchronous non-multi** **p** **lexed SRAM/PSRAM/NOR read waveforms**


|tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
||Address|||
|||||
|||||
|||||
|||||


1. Mode 2/B, C and D only. In Mode 1, FMC_NADV is not used.







DS13315 Rev 5 161/270


239

**Electrical characteristics** **STM32H730xB**

**Table 63. As** **y** **nchronous non-multi** **p** **lexed SRAM/PSRAM/NOR write timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|3T –1 fmc_ker_ck|3T + 1 fmc_ker_ck|ns|
|t v(NWE_NE)|FMC_NEx low to FMC_NWE low|T –1 fmc_ker_ck|T fmc_ker_ck||
|t w(NWE)|FMC_NWE low time|T –0.5 fmc_ker_ck|T +0.5 fmc_ker_ck||
|t h(NE_NWE)|FMC_NWE high to FMC_NE high hold time|T fmc_ker_ck|-||
|t v(A_NE)|FMC_NEx low to FMC_A valid|-|1||
|t h(A_NWE)|Address hold time after FMC_NWE high|T –0.5 fmc_ker_ck|-||
|t v(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5||
|t h(BL_NWE)|FMC_BL hold time after FMC_NWE high|T –0.5 fmc_ker_ck|-||
|t v(Data_NE)|Data to FMC_NEx low to Data valid|-|T + 2 fmc_ker_ck||
|t h(Data_NWE)|Data hold time after FMC_NWE high|T fmc_ker_ck|-||
|t v(NADV_NE)|FMC_NEx low to FMC_NADV low|-|5||
|t w(NADV)|FMC_NADV low time|-|T + 1 fmc_ker_ck||


1. Guaranteed by characterization results.

**Table 64. Asynchronous non-multiplexed SRAM/PSRAM/NOR write-NWAIT**
**timin** **g** **s** **[(1)(2)]**




|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|8T –1 fmc_ker_ck|8T +1 fmc_ker_ck|ns|
|t w(NWE)|FMC_NWE low time|6T –1 fmc_ker_ck|6T +1 fmc_ker_ck||
|t su(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|5T +13 fmc_ker_ck|-||
|t h(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|4T +12 fmc_ker_ck|-||


1. Guaranteed by characterization results.

2. N WAIT pulse width is equal to 1 fmc_ker_ck cycle.

162/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 28. As** **y** **nchronous non-multi** **p** **lexed SRAM/PSRAM/NOR write waveforms**










1. Mode 2/B, C and D only. In Mode 1, FMC_NADV is not used.

DS13315 Rev 5 163/270


239

**Electrical characteristics** **STM32H730xB**

**Table 65. As** **y** **nchronous multi** **p** **lexed PSRAM/NOR read timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|4T –1 fmc_ker_ck|4T +1 fmc_ker_ck|ns|
|t v(NOE_NE)|FMC_NEx low to FMC_NOE low|2T fmc_ker_ck|2T fmc_ker_ck +0.5||
|t tw(NOE)|FMC_NOE low time|T –1 fmc_ker_ck|T +1 fmc_ker_ck||
|t h(NE_NOE)|FMC_NOE high to FMC_NE high hold time|T fmc_ker_ck|-||
|t v(A_NE)|FMC_NEx low to FMC_A valid|-|0.5||
|t v(NADV_NE)|FMC_NEx low to FMC_NADV low|0|4.0||
|t w(NADV)|FMC_NADV low time|T –0.5 fmc_ker_ck|T +1 fmc_ker_ck||
|t h(AD_NADV)|FMC_AD(address) valid hold time after FMC_NADV high)|T –4 fmc_ker_ckk|-||
|t h(A_NOE)|Address hold time after FMC_NOE high|T –0.5 fmc_ker_ck|-||
|t su(Data_NE)|Data to FMC_NEx high setup time|T +14 fmc_ker_ck|-||
|t su(Data_NOE)|Data to FMC_NOE high setup time|13|-||
|t h(Data_NE)|Data hold time after FMC_NEx high|0|-||
|t h(Data_NOE)|Data hold time after FMC_NOE high|0|-||


1. Guaranteed by characterization results.

**Table 66. As** **y** **nchronous multi** **p** **lexed PSRAM/NOR read-NWAIT timin** **g** **s** **[(1)]**




|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|8T –1 fmc_ker_ck|8T +1 fmc_ker_ck|ns|
|t w(NOE)|FMC_NWE low time|5T –1 fmc_ker_ck|5T +1 fmc_ker_ck||
|t su(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|4T +9 fmc_ker_ck|-||
|t h(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|3T +12 fmc_ker_ck|-||


1. Guaranteed by characterization results.

164/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 29. As** **y** **nchronous multi** **p** **lexed PSRAM/NOR read waveforms**



|tv(NOE_NE) th(NE_NOE) tw(NOE)|Col2|Col3|Col4|
|---|---|---|---|
|||||
|||||
|||||
||Address|||
|||||
|||||
|||||
|||||
|||||
|||||


DS13315 Rev 5 165/270









239

**Electrical characteristics** **STM32H730xB**

**Table 67. As** **y** **nchronous multi** **p** **lexed PSRAM/NOR write timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|4T –1 fmc_ker_ck|4T fmc_ker_ck|ns|
|t v(NWE_NE)|FMC_NEx low to FMC_NWE low|T –1 fmc_ker_ck|T +0.5 fmc_ker_ck||
|t w(NWE)|FMC_NWE low time|2T –0.5 fmc_ker_ck|2T +0.5 fmc_ker_ck||
|t h(NE_NWE)|FMC_NWE high to FMC_NE high hold time|T –0.5 fmc_ker_ck|-||
|t v(A_NE)|FMC_NEx low to FMC_A valid|-|1||
|t v(NADV_NE)|FMC_NEx low to FMC_NADV low|0|5.0||
|t w(NADV)|FMC_NADV low time|T –0.5 fmc_ker_ck|T + 1 fmc_ker_ck||
|t h(AD_NADV)|FMC_AD(adress) valid hold time after FMC_NADV high)|T –4.5 fmc_ker_ck|-||
|t h(A_NWE)|Address hold time after FMC_NWE high|T – 0.5 fmc_ker_ck|-||
|t h(BL_NWE)|FMC_BL hold time after FMC_NWE high|T – 0.5 fmc_ker_ck|-||
|t v(BL_NE)|FMC_NEx low to FMC_BL valid|-|0.5||
|t v(Data_NADV)|FMC_NADV high to Data valid|-|T +2 fmc_ker_ck||
|t h(Data_NWE)|Data hold time after FMC_NWE high|T fmc_ker_ck|-||


1. Guaranteed by characterization results.

**Table 68. As** **y** **nchronous multi** **p** **lexed PSRAM/NOR write-NWAIT timin** **g** **s** **[(1)(2)]**




|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NE)|FMC_NE low time|9T –1 fmc_ker_ck|9T fmc_ker_ck|ns|
|t w(NWE)|FMC_NWE low time|7T –0.5 fmc_ker_ck|7T +0.5 fmc_ker_ck||
|t su(NWAIT_NE)|FMC_NWAIT valid before FMC_NEx high|5T +9 fmc_ker_ck|-||
|t h(NE_NWAIT)|FMC_NEx hold time after FMC_NWAIT invalid|4T +12 fmc_ker_ck|-||


1. Guaranteed by characterization results.

2. N WAIT pulse width is equal to 1 fmc_ker_ck cycle.

166/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 30. As** **y** **nchronous multi** **p** **lexed PSRAM/NOR write waveforms**















**Synchronous waveforms and timings**

*Figure 33* through *Figure 32* represent synchronous waveforms and *Table 71* through
*Table 70* provide the corresponding timings. The results shown in these tables are obtained
with the following FMC configuration:

- BurstAccessMode = FMC_BurstAccessMode_Enable

- MemoryType = FMC_MemoryType_CRAM

- WriteBurst = FMC_WriteBurst_Enable

- CLKDivision = 1

- DataLatency = 1 for NOR flash, DataLatency = 0 for PSRAM, C L = 30 pF

In all the timing tables, the T fmc_ker_ck is the f mc_ker_ck clock period, with the following
FMC_CLK maximum values:

- For 2.7 V<V DD <3.6 V: maximum FMC_CLK = 137 MHz at C L = 20 pF

- For 1.8 V<V DD <1.9 V: maximum FMC_CLK = 100 MHz at C L = 20 pF

- For 1.62 V<V DD <1.8 V: maximumFMC_CLK = 88 MHz at C L = 15 pF

DS13315 Rev 5 167/270


239

**Electrical characteristics** **STM32H730xB**

**Table 69. S** **y** **nchronous non-multi** **p** **lexed NOR/PSRAM read timin** **g** **s** **[(1)]**




|Symbol|Parameter|Col3|Min|Max|Unit|
|---|---|---|---|---|---|
|t w(CLK)|FMC_CLK period||2T –0.5 fmc_ker_ck|-|ns|
|t (CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)||-|3||
|t d(CLKH-NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)||T +1.5 fmc_ker_ck|-||
|t d(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|1.62 V <V < 3.6 V DD|-|5.5||
|||2.7 V <V < 3.6 V DD||2.0||
|t d(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|1.62 V <V < 3.6 V DD|1|-||
|||2.7 V <V < 3.6 V DD||-||
|t d(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)||-|3||
|t d(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)||T fmc_ker_ck|-||
|t d(CLKL-NOEL)|FMC_CLK ow to FMC_NOE low||-|2.5||
|t d(CLKH-NOEH)|FMC_CLK high to FMC_NOE high||T +1 fmc_ker_ck|-||
|t su(DV-CLKH)|FMC_D[15:0] valid data before FMC_CLK high||3|-||
|t h(CLKH-DV)|FMC_D[15:0] valid data after FMC_CLK high||0|-||
|t (NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high||3|-||
|t h(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high||2.5|-||


1. Guaranteed by characterization results.

168/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 31. S** **y** **nchronous non-multi** **p** **lexed NOR/PSRAM read timin** **g** **s**



|td(CL|Da|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||ta latency = 0|||||
||td(CL KL-AV)|KL-NADVH)|||||
|||||td(CL|KH-AIV)||
||||||||
||||||||
||||OEL)|td(CLK|H-NOEH)||
||||||||
||tsu(||||||
||||||th(CL 2 ITV)||
||tsu(NW||||||
||||||||
||||||||
||||||||


|Col1|CLKH)|
|---|---|
|ITV-||
|||


DS13315 Rev 5 169/270


239

**Electrical characteristics** **STM32H730xB**

**Table 70. S** **y** **nchronous non-multi** **p** **lexed PSRAM write timin** **g** **s** **[(1)]**




|Symbol|Parameter|Col3|Min|Max|Unit|
|---|---|---|---|---|---|
|t (CLK)|FMC_CLK period||2T –0.5 fmc_ker_ck|-|ns|
|t d(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)||-|3||
|t (CLKH-NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)||T +1.5 fmc_ker_ck|-||
|t d(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|1.62 V <V < 3.6 V DD|-|5.5||
|||2.7 V <V < 3.6 V DD||2||
|t d(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|1.62 V <V < 3.6 V DD|1|-||
|||2.7 V <V < 3.6 V DD||-||
|t d(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)||-|3||
|t d(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)||T fmc_ker_ck|-||
|t d(CLKL-NWEL)|FMC_CLK low to FMC_NWE low||-|2.5||
|t d(CLKH-NWEH)|FMC_CLK high to FMC_NWE high||T +1 fmc_ker_ck|-||
|t d(CLKL-Data)|FMC_D[15:0] valid data after FMC_CLK low||-|3.5||
|t d(CLKL-NBLL)|FMC_CLK low to FMC_NBL low||-|2||
|t d(CLKH-NBLH)|FMC_CLK high to FMC_NBL high||T +0.5 fmc_ker_ck|-||
|t su(NWAIT- CLKH)|FMC_NWAIT valid before FMC_CLK high||3|-||
|t h(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high||2.5|-||


1. Guaranteed by characterization results.

170/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 32. S** **y** **nchronous non-multi** **p** **lexed PSRAM write timin** **g** **s**







|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|td(CL td(CL|Da|||||||
|||ta latency =|0|||||
||td(CL KL-AV)|KL-NADVH|)|||||
|||||t|d(CLKH-A|IV)||
|||||||||
|||||||||
||KL-NWEL)|||td(C|LKH-NWE|H)||
|||||||||
||td(CL|KL-Data)|||td(CLK D2 CLKH-NB -NWAITV)|L-Da LH)||
|||||D1||||
|||||||||
|||||||||
||tsu(NWA|||||||


DS13315 Rev 5 171/270


239

**Electrical characteristics** **STM32H730xB**

**Table 71. S** **y** **nchronous multi** **p** **lexed NOR/PSRAM read timin** **g** **s** **[(1)]**




|Symbol|Parameter|Col3|Min|Max|Unit|
|---|---|---|---|---|---|
|t w(CLK)|FMC_CLK period||2T –0.5 fmc_ker_ck|-|ns|
|t d(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x=0..2)||-|3||
|t d(CLKH_NExH)|FMC_CLK high to FMC_NEx high (x= 0…2)||T +1.5 fmc_ker_ck|-||
|t d(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|1.62 V <V < 3.6 V DD|-|5.5||
|||2.7 V <V < 3.6 V DD||2||
|t d(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|1.62 V <V < 3.6 V DD|1|-||
|||2.7 V <V < 3.6 V DD||-||
|t d(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x=16…25)||-|3||
|t d(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x=16…25)||T fmc_ker_ck|-||
|t d(CLKL-NOEL)|FMC_CLK low to FMC_NOE low||-|2.5||
|t d(CLKH-NOEH)|FMC_CLK high to FMC_NOE high||T +1 fmc_ker_ck|-||
|t d(CLKL-ADV)|FMC_CLK low to FMC_AD[15:0] valid||-|3||
|t d(CLKL-ADIV)|FMC_CLK low to FMC_AD[15:0] invalid||0|-||
|t su(ADV-CLKH)|FMC_A/D[15:0] valid data before FMC_CLK high||3|-||
|t h(CLKH-ADV)|FMC_A/D[15:0] valid data after FMC_CLK high||0|-||
|t su(NWAIT- CLKH)|FMC_NWAIT valid before FMC_CLK high||3|-||
|t h(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high||2.5|-||


1. Guaranteed by characterization results.

172/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 33. S** **y** **nchronous multi** **p** **lexed NOR/PSRAM read timin** **g** **s**













|td(CL td(CL|Da KL-NExL)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|||ta latency = 0|||||
||td(CL KL-AV)|KL-NADVH)|||||
|||||td(CL|KH-AIV)||
||||||||
||||||||
||||OEL)|td(CLKH|-NOEH)||
|td(CLK AD|L-ADIV) tsu(A||||||
||||||th(CL 2 ITV)||
||||||||
||[15:0]||||||
||tsu(NWA||||||
||||||||
||||||||
||||||||


|Col1|LKH)|
|---|---|
|TV-C||
|||


DS13315 Rev 5 173/270


239

**Electrical characteristics** **STM32H730xB**

**Table 72. S** **y** **nchronous multi** **p** **lexed PSRAM write timin** **g** **s** **[(1)]**




|Symbol|Parameter|Col3|Min|Max|Unit|
|---|---|---|---|---|---|
|t w(CLK)|FMC_CLK period, V = 2.7 to 3.6 V DD||2T –0.5 fmc_ker_ck|-|ns|
|t d(CLKL-NExL)|FMC_CLK low to FMC_NEx low (x =0..2)||-|3||
|t d(CLKH-NExH)|FMC_CLK high to FMC_NEx high (x = 0…2)||T +1.5 fmc_ker_ck|-||
|t d(CLKL-NADVL)|FMC_CLK low to FMC_NADV low|1.62 V <V < 3.6 V DD|-|5.5||
|||2.7 V <V < 3.6 V DD||2.0||
|t d(CLKL-NADVH)|FMC_CLK low to FMC_NADV high|1.62 V <V < 3.6 V DD|1|-||
|||2.7 V <V < 3.6 V DD||-||
|t d(CLKL-AV)|FMC_CLK low to FMC_Ax valid (x =16…25)||-|3||
|t d(CLKH-AIV)|FMC_CLK high to FMC_Ax invalid (x =16…25)||T fmc_ker_ck|-||
|t d(CLKL-NWEL)|FMC_CLK low to FMC_NWE low||-|2.5||
|t (CLKH-NWEH)|FMC_CLK high to FMC_NWE high||T +1 fmc_ker_ck|-||
|t d(CLKL-ADV)|FMC_CLK low to to FMC_AD[15:0] valid||-|2.5||
|t d(CLKL-ADIV)|FMC_CLK low to FMC_AD[15:0] invalid||0|-||
|t d(CLKL-DATA)|FMC_A/D[15:0] valid data after FMC_CLK low||-|3.5||
|t d(CLKL-NBLL)|FMC_CLK low to FMC_NBL low||-|2||
|t d(CLKH-NBLH)|FMC_CLK high to FMC_NBL high||T +0.5 fmc_ker_ck|-||
|t su(NWAIT-CLKH)|FMC_NWAIT valid before FMC_CLK high||3|-||
|t h(CLKH-NWAIT)|FMC_NWAIT valid after FMC_CLK high||2.5|-||


1. Guaranteed by characterization results.

174/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 34. S** **y** **nchronous multi** **p** **lexed PSRAM write timin** **g** **s**












|td(CL td(CL td(CL td(CLK AD|Da KL-NExL)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|||||||CLK|||
|||ta latency|= 0||||||
||td(CL KL-AV)|KL-NADVH|)||||||
||||||t|d(CL|KH-AIV)||
||||||||||
||KL-NWEL)||||td(C|LKH|-NWEH)||
||||||||||
||||||d(CLKL-Data)|-NW LKH|D2 AITV) -NBLH)||
||||||D1||||
||||||th(CLKH t d(C||||
||||||||||
||||||||||


DS13315 Rev 5 175/270


239

**Electrical characteristics** **STM32H730xB**

**NAND controller waveforms and timings**

*Figure 35* through *Figure 38* represent synchronous waveforms, and *Table 73* and *Table 74*
provide the corresponding timings. The results shown in this table are obtained with the
following FMC configuration and a capacitive load (C L ) of 30 pF:

      - COM.FMC_SetupTime = 0x01

      - COM.FMC_WaitSetupTime = 0x03

      - COM.FMC_HoldSetupTime = 0x02

      - COM.FMC_HiZSetupTime = 0x01

      - ATT.FMC_SetupTime = 0x01

      - ATT.FMC_WaitSetupTime = 0x03

      - ATT.FMC_HoldSetupTime = 0x02

      - ATT.FMC_HiZSetupTime = 0x01

      - Bank = FMC_Bank_NAND

      - MemoryDataWidth = FMC_MemoryDataWidth_16b

      - ECC = FMC_ECC_Enable

      - ECCPageSize = FMC_ECCPageSize_512Bytes

      - TCLRSetupTime = 0

      - TARSetupTime = 0

In all timing tables, the T fmc_ker_ck is the fmc_ker_ck clock period.

**Table 73. Switchin** **g** **characteristics for NAND flash read c** **y** **cles** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(N0E)|FMC_NOE low width|4T – 0.5 fmc_ker_ck|4T +0.5 fmc_ker_ck|ns|
|t su(D-NOE)|FMC_D[15-0] valid data before FMC_NOE high|11|-||
|t h(NOE-D)|FMC_D[15-0] valid data after FMC_NOE high|0|-||
|t d(ALE-NOE)|FMC_ALE valid before FMC_NOE low|-|3T +0.5 fmc_ker_ck||
|t h(NOE-ALE)|FMC_NWE high to FMC_ALE invalid|4T –1 fmc_ker_ck|-||


1. Guaranteed by characterization results.

176/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 35. NAND controller waveforms for read access**






1. y = 7 or 15 depending on the NAND flash memory interface.

**Table 74. Switchin** **g** **characteristics for NAND flash write c** **y** **cles** **[(1)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(NWE)|FMC_NWE low width|4T – 0.5 fmc_ker_ck|4T +0.5 fmc_ker_ck|ns|
|t v(NWE-D)|FMC_NWE low to FMC_D[15-0] valid|0|-||
|t h(NWE-D)|FMC_NWE high to FMC_D[15-0] invalid|2T +1.5 fmc_ker_ck|-||
|t d(D-NWE)|FMC_D[15-0] valid before FMC_NWE high|5T – 5 fmc_ker_ck|-||
|t d(ALE-NWE)|FMC_ALE valid before FMC_NWE low|-|3T +0.5 fmc_ker_ck||
|t h(NWE-ALE)|FMC_NWE high to FMC_ALE invalid|2T – 0.5 fmc_ker_ck|-||



1. Guaranteed by characterization results.

DS13315 Rev 5 177/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 36. NAND controller waveforms for write access**





1. y = 7 or 15 depending on the NAND flash memory interface.

**SDRAM waveforms and timings**

In all timing tables, the TKERCK is the fmc_ker_ck clock period, with the following
FMC_SDCLK maximum values:

- For 2.7 V<V DD <3.6 V: maximum FMC_CLK = 95 MHz at 20 pF

- For 1.8 V<V DD <1.9 V: maximum FMC_CLK = 90 MHz at 20 pF

- For 1.62 V< DD <1.8 V: maximum FMC_CLK = 85 MHz at 15 pF

**Table 75. SDRAM read timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(SDCLK)|FMC_SDCLK period|2T – fmc_ker_ck 0.5|2T fmc_ker_ck +0.5|ns|
|t su(SDCLKH _Data)|Data input setup time|3|-||
|t h(SDCLKH_Data)|Data input hold time|1.5|-||
|t d(SDCLKL_Add)|Address valid time|-|2.0||
|t d(SDCLKL- SDNE)|Chip select valid time|-|1.5(2)||
|t h(SDCLKL_SDNE)|Chip select hold time|0|-||
|t d(SDCLKL_SDNRAS)|SDNRAS valid time|-|1||
|t h(SDCLKL_SDNRAS)|SDNRAS hold time|0|-||
|t d(SDCLKL_SDNCAS)|SDNCAS valid time|-|2.0||
|t h(SDCLKL_SDNCAS)|SDNCAS hold time|0.5|-||


1. Guaranteed by characterization results.

2. Using PC2_C I/O adds 4.5 ns to this timing.

178/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Table 76. LPSDR SDRAM read timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t W(SDCLK)|FMC_SDCLK period|2T – fmc_ker_ck 0.5|2T +0.5 fmc_ker_ck|ns|
|t su(SDCLKH_Data)|Data input setup time|3|-||
|t h(SDCLKH_Data)|Data input hold time|2.5|-||
|t d(SDCLKL_Add)|Address valid time|-|2||
|t d(SDCLKL_SDNE)|Chip select valid time|-|1.5(2)(3)||
|t h(SDCLKL_SDNE)|Chip select hold time|0|-||
|t d(SDCLKL_SDNRAS|SDNRAS valid time|-|1||
|t h(SDCLKL_SDNRAS)|SDNRAS hold time|0|-||
|t d(SDCLKL_SDNCAS)|SDNCAS valid time|-|2||
|t h(SDCLKL_SDNCAS)|SDNCAS hold time|0.5|-||


1. Guaranteed by characterization results.

2. Using PC2 I/O adds 4 ns to this timing.

3. Using PC2_C I/O adds 16.5 ns to this timing.

**Fi** **g** **ure 37. SDRAM read access waveforms** **(** **CL = 1** **)**




|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|||Coln|||
||||||
||||||
|L_NRAS)|||||
|L_NCAS)|||||
||||||
||||||


DS13315 Rev 5 179/270





239

**Electrical characteristics** **STM32H730xB**

**Table 77. SDRAM Write timin** **g** **s** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(SDCLK)|FMC_SDCLK period|2T – 0.5 fmc_ker_ck|2T +0.5 fmc_ker_ck|ns|
|t ) d(SDCLKL _Data|Data output valid time|-|2||
|t h(SDCLKL _Data)|Data output hold time|0.5|-||
|t d(SDCLKL_Add)|Address valid time|-|2||
|t d(SDCLKL_SDNWE)|SDNWE valid time|-|2||
|t h(SDCLKL_SDNWE)|SDNWE hold time|0|-||
|t d(SDCLKL_ SDNE)|Chip select valid time|-|1.5(2)||
|t h(SDCLKL-_SDNE)|Chip select hold time|0|-||
|t d(SDCLKL_SDNRAS)|SDNRAS valid time|-|1||
|t h(SDCLKL_SDNRAS)|SDNRAS hold time|0|-||
|t d(SDCLKL_SDNCAS)|SDNCAS valid time|-|2||
|t d(SDCLKL_SDNCAS)|SDNCAS hold time|0.5|-||


1. Guaranteed by characterization results.

2. Using PC2_C I/O adds 4.5 ns to this timing.

**Table 78. LPSDR SDRAM Write timin** **g** **s** **[(1)]**




|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t w(SDCLK)|FMC_SDCLK period|2T – 0.5 fmc_ker_ck|2T +0.5 fmc_ker_ck|ns|
|t ) d(SDCLKL _Data|Data output valid time|-|2||
|t h(SDCLKL _Data)|Data output hold time|0|-||
|t d(SDCLKL_Add)|Address valid time|-|2.5||
|t d(SDCLKL-SDNWE)|SDNWE valid time|-|2||
|t h(SDCLKL-SDNWE)|SDNWE hold time|0|-||
|t d(SDCLKL- SDNE)|Chip select valid time|-|1.5(2)(3)||
|t h(SDCLKL- SDNE)|Chip select hold time|0|-||
|t d(SDCLKL-SDNRAS)|SDNRAS valid time|-|1||
|t h(SDCLKL-SDNRAS)|SDNRAS hold time|0|-||
|t d(SDCLKL-SDNCAS)|SDNCAS valid time|-|2||
|t d(SDCLKL-SDNCAS)|SDNCAS hold time|0.5|-||


1. Guaranteed by characterization results.

2. Using PC2 I/O adds 4 ns to this timing.

3. Using PC2_C I/O adds 16.5 ns to this timing.

180/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 38. SDRAM write access waveforms**







|DCLK DCLK|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||Col2|||Coln|||
|||th(S||||||
|E)||||||||
|||||||||
|DCLK||L_NR|AS)|||||
|DCLK||L_NC|AS)|||||
|||||||||
|DCLK||L_N|WE)|||||
|||||||||
|||||||||
||D|ata2|||atan|||


**6.3.20** **Octo-SPI interface characteristics**

Unless otherwise specified, the parameters given in *Table 79* and *Table 81* for OCTOSPI
are derived from tests performed under the ambient temperature, f HCLK frequency and V DD
supply voltage conditions summarized in *Table 12: General operating conditions*, with the
following configuration:

      - Output speed is set to OSPEEDRy[1:0] = 11

      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.

      - HSLV activated when V DD ≤ 2.5 V

      - VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output alternate
function characteristics.

DS13315 Rev 5 181/270


239

**Electrical characteristics** **STM32H730xB**

**Table 79. OCTOSPI characteristics in SDR mode** **[(1)(2)]**











|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F (CLK)|OCTOSPI clock frequency|1.71 V < V < 3.6 V, DD VOS0, C = 15 pF LOAD|-|-|92|MHz|
|||1.71 V < V < 3.6 V, DD VOS0, C =20 pF LOAD|-|-|90||
|||2.7 V < V < 3.6 V, DD VOS0, C = 20 pF LOAD|-|-|140||
|t w(CKH)|OCTOSPI clock high and low time, even division|PRESCALER[7:0] = n = 0,1,3,5|t /2 (CK)|-|t /2+1 (CK)|ns|
|t w(CKL)|||t /2–1 (CK)|-|t /2 (CK)||
|t w(CKH)|OCTOSPI clock high and low time, odd division|PRESCALER[7:0] = n = 2,4,6,8|(n/2)*t / (CK) (n+1)|-|(n/2)*t / (CK) (n+1)+1||
|t w(CKL)|||(n/2+1)*t / (CK) (n+1)–1|-|(n/2+1)*t (CK) /(n+1)||
|t (3) s(IN)|Data input setup time|-|3.0|-|-||
|t (3) h(IN)|Data input hold time|-|1.5|-|-||
|t v(OUT)|Data output valid time|-|-|0.5|1(4)||
|t h(OUT)|Data output hold time|-|0|-|-||


1. All values apply to Octal and Quad-SPI mode.

2. Guaranteed by characterization results.

3. Delay block bypassed.

4. Using PC2 or PC3 I/O in the data bus adds 4 ns to this timing value.

**Fi** **g** **ure 39. OCTOSPI SDR read/write timin** **g** **dia** **g** **ram**




|Col1|h(OU|
|---|---|
|||
|D0||


|ts(IN)|th(IN)|
|---|---|
|||
||D1|



182/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 80. OCTOSPI characteristics in DTR mode (no DQS)** **[(1)(2)]**












|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F (3) CK|OCTOSPI clock frequency|1.71 V < V < 3.6 V, DD VOS0, C = 15 pF LOAD|-|-|90(4)|MHz|
|||1.71 V < V < 3.6 V, DD VOS0, C = 20 pF LOAD|-|-|87(4)||
|||2.7 V < V < 3.6 V, DD VOS0, C = 20 pF LOAD|-|-|110||
|t w(CKH)|OCTOSPI clock high and low time, even division|PRESCALER[7:0] = n = 0,1,3,5|t /2 (CK)|-|t /2+1 (CK)|ns|
|t w(CKL)|||t /2–1 (CK)|-|t /2 (CK)||
|t w(CKH)|OCTOSPI clock high and low time, odd division|PRESCALER[7:0] = n = 2,4,6,8|(n/2)*t / (CK) (n+1)|-|(n/2)*t / (CK) (n+1)+1||
|t w(CKL)|||(n/2+1)*t /( (CK) n+1) – 1|-|(n/2+1)* t /(n+1) (CK)||
|t sr(IN) t (5) sf(IN)|Data input setup time|-|3.0|-|-||
|t hr(IN) t (5) hf(IN)|Data input hold time|-|1.50|-|-||
|t vr(OUT) t vf(OUT)|Data output valid time|DHQC = 0|-|6|7(6)||
|||DHQC = 1, Prescaler = 1,2 ...|-|t /4+ pclk 1|t /4+1.25 pclk (6)||
|thr(OUT) thf(OUT)|Data output hold time|DHQC = 0|4.5|-|-||
|||DHQC = 1, Prescaler = 1,2 ...|t /4 pclk|-|-||


1. All values apply to Octal and Quad-SPI mode.

2. Guaranteed by characterization results.



3. DHQC must be set to reach the mentioned frequency.

4. Using PC2 or PC3 I/O in the data bus decreases the frequency to 47 MHz.

5. Delay block bypassed.

6. Using PC2 or PC3 I/O in the data bus adds 4 ns to this timing value.

**Fi** **g** **ure 40. OCTOSPI DTR mode timin** **g** **dia** **g** **ram**







|Col1|r(OU|
|---|---|
|||
|D0||

|Col1|Col2|f(OU|
|---|---|---|
||||
|D2|D3||




|Col1|Col2|Col3|Col4|
|---|---|---|---|
|D0||D|1|

|Col1|Col2|Col3|Col4|
|---|---|---|---|
|D3||D|4|



DS13315 Rev 5 183/270


239

**Electrical characteristics** **STM32H730xB**

**Table 81. OCTOSPI characteristics in DTR mode** **(** **with DQS** **)** **/Octal and H** **y** **perbus** **[(1)]**










|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F (2)(3) CK|OCTOSPI clock frequency|2,7 V < V < 3.6 V, DD VOS0, C = 20 pF LOAD|-|-|100|MHz|
|||1.71 V < V < 3.6 V, DD VOS0, C = 20 pF LOAD|-|-|100(4)||
|t w(CKH)|OCTOSPI clock high and low time, even division|PRESCALER[7:0] = n = 0,1,3,5|t /2 (CK)|-|t /2+1 (CK)|ns|
|t w(CKL)|||t /2–1 (CK)|-|t /2 (CK)||
|t w(CKH)|OCTOSPI clock high and low time, odd division|PRESCALER[7:0] = n = 2,4,6,8|(n/2)*t / (CK) (n+1)|-|(n/2)*t / (CK) (n+1)+1|ns|
|t w(CKL)|||(n/2+1)*t /( (CK) n+1)–1|-|(n/2+1)*t / (CK) (n+1)||
|t v(CK)|Clock valid time|-|-|-|t +1 (CK)||
|t h(CK)|Clock hold time|-|t /2 (CK)|-|-||
|V ODr(CK)|CK,CK crossing level on CK rising edge|VDD = 1.8 V|922|-|1229|mV|
|V ODf(CK)|CK,CK crossing level on CK falling edge|VDD = 1.8 V|1000|-|1277||
|t w(CS)|Chip select high time|-|3*t (CK)|-|-|ns|
|t v(DQ)|Data input vallid time|-|0|-|-||
|t v(DS)|Data strobe input valid time|-|0|-|-||
|t h(DS)|Data strobe input hold time|-|0|-|-||
|t v(RWDS)|Data strobe output valid time|-|-|-|3 x t (CK)||
|t sr(DQ)|Data input setup time|Rising edge|0|-|-||
|t sf(DQ)||Falling edge|0|-|-||
|t hr(DQ)|Data input hold time|Rising edge|1|-|-||
|t hf(DQ)||Falling edge|1|-|-||
|t vr(OUT)|Data output valid time rising edge|DHQC = 0|-|6|7(5)||
|||DHQC = 1, Prescaler = 1,2...|-|t /4+ pclk 1|t /4+1.25 pclk (5)||
|t vf(OUT)|Data output valid time falling edge|DHQC = 0|-|5.5|6(5)||
|||DHQC = 1, Prescaler = 1,2...|-|t /4+ pclk 0.5|t /4+0.75 pclk (5)||
|t hr(OUT)|Data output hold time rising edge|DHQC = 0|4.5|-|-||
|||DHQC = 1, Prescaler = 1,2...|t /4 pclk|-|-||
|t hf(OUT)|Data output hold time falling edge|DHQC = 0|4.5|-|-||
|||DHQC = 1, Prescaler = 1,2...|t /4 pclk|-|-||


1. Guaranteed by characterization results.



184/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

2. Maximum frequency values are given for a RWDS to DQ skew of maximum +/-1.0 ns.

3. Activating DHQC is mandatory to reach this frequency

4. Using PC2 or PC3 I/O on data bus decreases the frequency to 47 MHz.

5. Using PC2 or PC3 I/O on the data bus adds 4 ns to this timing value.

**Fi** **g** **ure 41. OCTOSPI H** **yp** **erbus clock timin** **g** **dia** **g** **ram**




**Fi** **g** **ure 42. OCTOSPI H** **yp** **erbus read timin** **g** **dia** **g** **ram**














|tv(CLK)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|th(CLK)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||
||||||||||||||||||||||||
|||||||||||||||||||t|||||
||||||||||||||||||||||||
|||t (OUT) h|||||||||||||||||v(D||||
||||||||||||||||||||||||
||4|7:40|39:32||31|:24|23:16||15:8||7:0||||||||||||

|t Q) s|Col2|Col3|Col4|
|---|---|---|---|
|Dn A|Dn B|Dn+1 A|Dn+1 B|




DS13315 Rev 5 185/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 43. OCTOSPI H** **yp** **erbus write timin** **g** **dia** **g** **ram**













|ad write recovery Access latency t v(CLK) t h(CLK|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||
||||||||||||||||||||||||
|||igh = 2x lat ow = 1x lat||||ency ency|||||||||||||||||
|||t (OUT) h|||||||||||||||||||||
||||||||||||||||||||||||
||47|:40|39:32||31|:24|23:16||15:8||7:0||||||||||||

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||(O||
||||||
|Dn A|Dn B|Dn A|+1|Dn+1 B|




**6.3.21** **Delay block (DLYB) characteristics**

Unless otherwise specified, the parameters given in *Table 82* for Delay Block are derived
from tests performed under the ambient temperature, f rcc_c_ck frequency and VDD supply
voltage summarized in *Table 12: General operating conditions*, with the following
configuration:

**Table 82. Dela** **y** **Block characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|t init|Initial delay|-|900|1300|1900|ps|
|t ∆|Unit Delay|-|28|33|41|-|



**6.3.22** **16-bit ADC characteristics**

Unless otherwise specified, the parameters given in *Table 83*, *Table 84* and *Table 85* are
derived from tests performed under the ambient temperature, f HCLK frequency and V DDA
supply voltage conditions summarized in *Table 12: General operating conditions* .





|Col1|Col2|Table 83. 16-bit ADC characteristics(1)(2)|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|VDDA|Analog supply voltage for ADC ON|-|1.62|-|3.6|V|
|VREF+|Positive reference voltage|VDDA ≥ 2 V|1.62|-|VDDA||
|||VDDA < 2 V|VDDA||||
|VREF-|Negative reference voltage|-|VSSA||||


186/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 83. 16-bit ADC characteristics** **[(1)(2)]** **(** **continued** **)**


























|Symbol|Parameter|Conditions|Col4|Col5|Col6|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|---|---|
|fADC|ADC clock frequency|1.62 V ≤ VDDA ≤ 3.6 V|||BOOST = 11|0.12|-|50|MHz|
||||||BOOST = 10|0.12|-|25||
||||||BOOST = 01|0.12|-|12.5||
||||||BOOST = 00|-|-|6.25||
|fs(3)|Sampling rate for Direct channels|Resolution = 16 bits, VDDA >2.5 V|TJ = 90 °C|fADC = 36 MHz|SMP = 1.5|-|-|3.60|MSps|
|||Resolution = 16 bits||fADC = 37 MHz|SMP = 2.5|-|-|3.35||
|||Resolution = 14 bits|TJ = 125 °C|fADC = 50 MHz|SMP = 2.5|-|-|5.00||
|||Resolution = 12 bits||fADC = 50 MHz|SMP = 2.5|-|-|5.50||
|||Resolution = 10 bits||fADC = 50 MHz|SMP = 1.5|-|-|7.10||
|||Resolution = 8 bits||fADC = 50 MHz|SMP = 1.5|-|-|8.30||
|||Resolution = 14 bits|TJ = 140 °C|fADC = 49 MHz|SMP = 1.5|-|-|4.90||
|||Resolution = 12 bits||fADC = 50 MHz|SMP = 1.5|-|-|5.50||
|||Resolution = 10 bits||fADC = 50 MHz|SMP = 1.5|-|-|6.70||
|||Resolution = 8 bits||fADC = 50 MHz|SMP = 1.5|-|-|8.30||
||Sampling rate for Fast channels|Resolution = 16 bits, VDDA >2.5 V|TJ = 90 °C|fADC = 32 MHz|SMP = 2.5|-|-|2.90||
|||Resolution = 16 bits||fADC = 31 MHz|SMP = 2.5|-|-|2.80||
|||Resolution = 14 bits|TJ = 125 °C|fADC = 33 MHz|SMP = 2.5|-|-|3.30||
|||Resolution = 12 bits||fADC = 39 MHz|SMP = 2.5|-|-|4.30||
|||Resolution = 10 bits||fADC = 48 MHz|SMP = 2.5|-|-|6.00||
|||Resolution = 8 bits||fADC = 50 MHz|SMP = 2.5|-|-|7.10||
|||Resolution = 12 bits|TJ = 140 °C|fADC = 37 MHz|SMP = 2.5|-|-|4.10||
|||Resolution = 10 bits||fADC = 46 MHz|SMP = 2.5|-|-|5.70||
|||Resolution = 8 bits||fADC = 50 MHz|SMP = 2.5|-|-|7.10||
||Sampling rate for Slow channels(4)|Resolution = 16 bits|TJ = 90 °C|||-|-|1.00||
|||resolution = 14 bits|TJ = 125 °C|||-|-|||
|||resolution = 12 bits||||-|-|||
|||resolution = 10 bits||||-|-|||
|||resolution = 8 bits||||-|-|||
|||resolution = 12 bits|TJ = 140 °C|||-|-|||
|||resolution = 10 bits||||-|-|||
|||resolution = 8 bits||||-|-|||
|V (5) AIN|Conversion voltage range|-||||0|-|V REF+|V|
|VCMIV|Common mode input voltage|-||||VREF/2 − 10%|VREF/ 2|VREF/2 + 10%|V|


DS13315 Rev 5 187/270


239

**Electrical characteristics** **STM32H730xB**

**Table 83. 16-bit ADC characteristics** **[(1)(2)]** **(** **continued** **)**









|Symbol|Parameter|Conditions|Col4|Col5|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|---|
|RAIN(6)|External input impedance|Resolution = 16 bits, TJ = 125 °C|-|-|-|-|170|Ω|
|||Resolution = 14 bits, TJ = 125 °C|-|-|-|-|435||
|||Resolution = 12 bits, TJ =125 °C|-|-|-|-|1,150||
|||Resolution = 10 bits, TJ = 125 °C|-|-|-|-|5,650||
|||Resolution = 8 bits, TJ = 125 °C|-|-|-|-|26,500||
|CADC|Internal sample and hold capacitor|-|||-|4|-|pF|
|tADCVREG _STUP|ADC LDO startup time|-|||-|5|10|us|
|tSTAB|ADC Power-up time|LDO already started|||1|-|-|conver sion cycle|
|tCAL|Offset and linearity calibration time|-|||16,5010|||1/fADC|
|tOFF_ CAL|Offset calibration time|-|||1,280|||1/fADC|
|tLATR|Trigger conversion latency regular and injected channels without conversion abort|CKMODE = 00|||1.5|2|2.5|1/fADC|
|||CKMODE = 01|||-|-|2.5||
|||CKMODE = 10|||-|-|2.5||
|||CKMODE = 11|||-|-|2.25||
|tLATRINJ|Trigger conversion latency regular injected channels aborting a regular conversion|CKMODE = 00|||2.5|3|3.5|1/fADC|
|||CKMODE = 01|||-|-|3.5||
|||CKMODE = 10|||-|-|3.5||
|||CKMODE = 11|||-|-|3.25||
|tS|Sampling time|-|||1.5|-|810.5|1/fADC|
|tCONV|Total conversion time (including sampling time)|Resolution = N bits|||ts + 0.5 + N/2|-|-|1/fADC|
|tTRIG|External trigger period|-|||tCONV|-|-|1/fADC|


188/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 83. 16-bit ADC characteristics** **[(1)(2)]** **(** **continued** **)**





|Symbol|Parameter|Conditions|Col4|Col5|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|---|
|IDDA_D (ADC)|ADC consumption on VDDA, BOOST=11, Differential mode|Resolution = 16 bits, fADC = 25 MHz|-|-|-|1,440|-|µA|
|||Resolution = 14 bits, fADC = 30 MHz|-|-|-|1,350|-||
|||Resolution = 12 bits, fADC = 40 MHz|-|-|-|990|-||
||ADC consumption on VDDA, BOOST=10, Differential mode, fADC = 25 MHz|Resolution = 16 bits|-|-|-|1,080|-||
|||Resolution = 14 bits|-|-|-|810|-||
|||Resolution = 12 bits|-|-|-|585|-||
||ADC consumption on VDDA, BOOST=01, Differential mode, fADC = 12.5 MHz|Resolution = 16 bits|-|-|-|630|-||
|||Resolution = 14 bits|-|-|-|432|-||
|||Resolution = 12 bits|-|-|-|315|-||
||ADC consumption on VDDA, BOOST=00, Differential mode, fADC = 6.25 MHz|Resolution = 16 bits|-|-|-|360|-||
|||Resolution = 14 bits|-|-|-|270|-||
|||Resolution = 12 bits|-|-|-|225|-||
|IDDA_SE (ADC)|ADC consumption on VDDA, BOOST=11, Single-ended mode|Resolution = 16 bits, fADC=25 MHz|-|-|-|720|-||
|||Resolution = 14 bits, fADC=30 MHz|-|-|-|675|-||
|||Resolution = 12 bits, fADC=40 MHz|-|-|-|495|-||
||ADC consumption on VDDA, BOOST=10, Singl-ended mode, fADC = 25 MHz|Resolution = 16 bits|-|-|-|540|-||
|||Resolution = 14 bits|-|-|-|405|-||
|||Resolution = 12 bits|-|-|-|292.5|-||
||ADC consumption on VDDA, BOOST=01, Single-ended mode, fADC = 12.5 MHz|Resolution = 16 bits|-|-|-|315|-||
|||Resolution = 14 bits|-|-|-|216|-||
|||Resolution = 12 bits|-|-|-|157.5|-||
||ADC consumption on VDDA BOOST=00, Single-ended mode fADC=6.25 MHz|Resolution = 16 bits|-|-|-|180|-||
|||Resolution = 14 bits|-|-|-|135|-||
|||Resolution = 12 bits|-|-|-|112.5|-||
|I DD (ADC)|ADC consumption on V DD|fADC=50 MHz|-|-|-|400|-||
|||fADC=25 MHz|-|-|-|220|-||
|||fADC=12.5 MHz|-|-|-|180|-||
|||fADC=6.25 MHz|-|-|-|120|-||
|||fADC=3.125 MHz|-|-|-|80|-||


1. Guaranteed by design.

2. The voltage booster on ADC switches must be used for V DDA < 2.4 V (embedded I/O switches).

3. These values are valid for TFBGA100, UFBGA169 and UFBGA176+25 packages and one ADC. The values for other packages and multiple
ADCs may be different.

4. For slow channels, the performance should be limited to 1 Msps what ever the value of f ADC .

DS13315 Rev 5 189/270


239

**Electrical characteristics** **STM32H730xB**

5. Depending on the package, V REF+ can be internally connected to V DDA and V REF- to V SSA .

6. The tolerance is 10 LSBs for 16-bit resolution, 4 LSBs for 14-bit resolution, and 2 LSBs for 12-bit, 10-bit and 8-bit resolutions.






|Col1|Table 84. Minimum sampling|g time vs RAIN (16-bit ADC)(1)(2)|Col4|Col5|
|---|---|---|---|---|
|Resolution|RAIN (Ω)|Minimum sampling time (s)|||
|||Direct channels(3)|Fast channels(4)|Slow channels(5)|
|16 bits|47|7.37E-08|1.14E-07|1.72E-07|
|14 bits|47|6.29E-08|9.74E-08|1.55E-07|
||68|6.84E-08|1.02E-07|1.58E-07|
||100|7.80E-08|1.12E-07|1.62E-07|
||150|9.86E-08|1.32E-07|1.80E-07|
||220|1.32E-07|1.61E-07|2.01E-07|
|12 bits|47|5.32E-08|8.00E-08|1.29E-07|
||68|5.74E-08|8.50E-08|1.32E-07|
||100|6.58E-08|9.31E-08|1.40E-07|
||150|8.37E-08|1.10E-07|1.51E-07|
||220|1.11E-07|1.34E-07|1.73E-07|
||330|1.56E-07|1.78E-07|2.14E-07|
||470|2.16E-07|2.39E-07|2.68E-07|
||680|3.01E-07|3.29E-07|3.54E-07|
|10 bits|47|4.34E-08|6.51E-08|1.08E-07|
||68|4.68E-08|6.89E-08|1.11E-07|
||100|5.35E-08|7.55E-08|1.16E-07|
||150|6.68E-08|8.77E-08|1.26E-07|
||220|8.80E-08|1.08E-07|1.40E-07|
||330|1.24E-07|1.43E-07|1.71E-07|
||470|1.69E-07|1.89E-07|2.13E-07|
||680|2.38E-07|2.60E-07|2.80E-07|
||1000|3.45E-07|3.66E-07|3.84E-07|
||1500|5.15E-07|5.35E-07|5.48E-07|
||2200|7.42E-07|7.75E-07|7.78E-07|
||3300|1.10E-06|1.14E-06|1.14E-06|


190/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**




|Ta|Table 84. Minimum sampling time v|vs RAIN (16-bit ADC)(1)(2) (continued)|Col4|Col5|
|---|---|---|---|---|
|Resolution|RAIN (Ω)|Minimum sampling time (s)|||
|||Direct channels(3)|Fast channels(4)|Slow channels(5)|
|8 bits|47|3.32E-08|5.10E-08|8.61E-08|
||68|3.59E-08|5.35E-08|8.83E-08|
||100|4.10E-08|5.83E-08|9.22E-08|
||150|5.06E-08|6.76E-08|9.95E-08|
||220|6.61E-08|8.22E-08|1.11E-07|
||330|9.17E-08|1.08E-07|1.32E-07|
||470|1.24E-07|1.40E-07|1.63E-07|
||680|1.74E-07|1.91E-07|2.12E-07|
||1000|2.53E-07|2.70E-07|2.85E-07|
||1500|3.73E-07|3.93E-07|4.05E-07|
||2200|5.39E-07|5.67E-07|5.75E-07|
||3300|8.02E-07|8.36E-07|8.38E-07|
||4700|1.13E-06|1.18E-06|1.18E-06|
||6800|1.62E-06|1.69E-06|1.68E-06|
||10000|2.36E-06|2.47E-06|2.45E-06|
||15000|3.50E-06|3.69E-06|3.65E-06|


1. Guaranteed by design.



2. Data valid at up to 130 °C, with a 47 pF PCB capacitor, and V DDA =1.6 V.

3. Direct channels are connected to analog I/Os (PA0_C, PA1_C, PC2_C and PC3_C) to optimize ADC performance.

4. Fast channels correspond to PA6, PB1, PC4, PF11, PF13 for ADCx_INPx, and to PA7, PB0, PC5, PF12, PF14 for
ADCx_INNx.

5. Slow channels correspond to all ADC inputs except for the Direct and Fast channels.

DS13315 Rev 5 191/270


239

**Electrical characteristics** **STM32H730xB**

**Table 85. 16-bit ADC accurac** **y** **[(1)(2)]**



















|Symbol|Parameter|Conditions(3)|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|ET|Total undadjusted error|Direct channel|Single ended|-|+10/–20|-|LSB|
||||Differential|-|±15|-||
|||Fast channel|Single ended|-|+10/–20|-||
||||Differential|-|±15|-||
|||Slow channel|Single ended|-|±10|-||
||||Differential||±10|-||
|EO|Offset error|-||-|±10|-||
|EG|Gain error|-||-|±15|-||
|ED|Differential linearity error|Single ended||-|+3/–1|-||
|||Differential||-|+4.5/–1|-||
|EL|Integral linearity error|Direct channel|Single ended|-|±11|-||
||||Differential|-|±7|-||
|||Fast channel|Single ended|-|±13|-||
||||Differential|-|±7|-||
|||Slow channel|Single ended|-|±10|-||
||||Differential|-|±6|-||
|ENOB|Effective number of bits|Single ended||-|12.2|-|Bits|
|||Differential||-|13.2|-||
|SINAD|Signal-to-noise and distortion ratio|Single ended||-|75.2|-|dB|
|||Differential||-|81.2|-||
|SNR|Signal-to-noise ratio|Single ended||-|77.0|-||
|||Differential||-|81.0|-||
|THD|Total harmonic distortion|Single ended||-|87|-||
|||Differential||-|90|-||


1. Guaranteed by characterization results for BGA packages. The values for LQFP packages might differ.

2. ADC DC accuracy values are measured after internal calibration.

3. ADC clock frequency = 25 MHz, ADC resolution = 16 bits, V DDA =V REF+ =3.3 V, BOOST=11 and 16-bit mode.



Note: ADC accuracy vs. negative injection current: injecting a negative current on any analog
input pins should be avoided as this significantly reduces the accuracy of the conversion
being performed on another analog input. It is recommended to add a Schottky diode (pin to
ground) to analog pins which may potentially inject negative currents.

Any positive injection current within the limits specified for I INJ(PIN) and ΣI INJ(PIN) does not
affect the ADC accuracy.

192/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 44. ADC accurac** **y** **characteristics**
















1. Example of an actual transfer curve.

2. Ideal transfer curve.

3. End point correlation line.

4. E T = Total Unadjusted Error: maximum deviation between the actual and the ideal transfer curves.
EO = Offset Error: deviation between the first actual transition and the first ideal one.
EG = Gain Error: deviation between the last ideal transition and the last actual one.
ED = Differential Linearity Error: maximum deviation between actual steps and the ideal one.
EL = Integral Linearity Error: maximum deviation between any actual transition and the end point
correlation line.

**Figure 45. Typical connection diagram when using the ADC with FT/TT pins**
**featurin** **g** **analo** **g** **switch function**













1. Refer to *Table 83: 16-bit ADC characteristics* for the values of R AIN and C ADC .

2. C parasitic represents the capacitance of the PCB (dependent on soldering and PCB layout quality) plus the
pad capacitance (refer to *Table 54: I/O static characteristics* ). A high C parasitic value downgrades
conversion accuracy. To remedy this, f ADC should be reduced.

3. Refer to *Table 54: I/O static characteristics* for the value of I .
lkg

4. Refer to *Figure 13: Power supply scheme* .

DS13315 Rev 5 193/270


239

**Electrical characteristics** **STM32H730xB**

**General PCB design guidelines**

Power supply decoupling should be performed as shown in *Figure 46* or *Figure 47*,
depending on whether V REF+ is connected to V DDA or not. The 100 nF capacitors should be
ceramic (good quality). They should be placed them as close as possible to the chip.

**Fi** **g** **ure 46. Power su** **pp** **l** **y** **and reference decou** **p** **lin** **g** **(** **V** **REF+** **not connected to** **V** **DDA** **)**






1. When V REF+ and V REF- inputs are not available, they are internally connected to V DDA and V SSA,
respectively.

**Fi** **g** **ure 47. Power su** **pp** **l** **y** **and reference decou** **p** **lin** **g** **(** **V** **REF+** **connected to** **V** **DDA** **)**





1. When V REF+ and V REF- inputs are not available, they are internally connected to V DDA and V SSA,
respectively.

194/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.23** **12-bit ADC characteristics**

Unless otherwise specified, the parameters given in *Table 86*, *Table 87* and *Table 88* are
derived from tests performed under the ambient temperature and V DDA supply voltage
conditions summarized in *Table 12: General operating conditions* . In *Table 86*, *Table 87* and
*Table 88*, f ADC refers to f adc_ker_ck .






































|Col1|Col2|Table 86. 12-bit ADC characteristics(1)(2)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Sym- bol|Parameter|Conditions||||||Min|Typ|Max|Unit|
|VDDA|Analog power supply for ADC ON|-||||||1.62|-|3.6|V|
|VREF+ (3)|Positive reference voltage|VDDA ≥ VREF+||||||1.62|-|VDDA||
|VREF-|Negative reference voltage|-||||||VSSA|-|-||
|fADC|ADC clock frequency|1,62 V ≤ VDDA ≤ 3.6 V||||||1.5|-|75|MHz|
|fS(4)|Sampling rate for Direct channels|Resolution = 12 bits|Continuous and Discontinuous mode(5)|2.4 V ≤ VDDA ≤ 3.6 V|–40 °C ≤ TJ ≤ 130 °C|fADC = 75 MHz|SMP = 2.5|-|-|5|MSPS|
|||||1.6V ≤ VDDA≤ 3.6 V||fADC = 60 MHz||-|-|4||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||fADC = 50 MHz(6)||-|-|3.33||
|||||1.6 V ≤ VDDA ≤ 3.6 V||fADC = 38 MHz(6)||-|-|2.53||
|||Resolution = 10 bits|Continuous and Discontinuous mode(5)|1.6V ≤ V ≤ 3.6V DDA|–40 °C ≤ TJ ≤ 130 °C|fADC = 75 MHz|SMP = 2.5|-|-|5.77||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||f = 58 ADC MHz(6)||-|-|4.46||
|||||1.6V ≤ V ≤ 3.6V DDA||fADC = 42 MHz(6)||-|-|3.23||
|||Resolution = 8 bits|Continuous and Discontinuous mode(5)|1.6V ≤ VDDA ≤ 3.6V|–40 °C ≤ T ≤ 130 °C J|f = 75 ADC MHz|SMP = 2.5|-|-|6.82||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||fADC = 67 MHz(6)||-|-|6.09||
|||||1.6V ≤ VDDA ≤ 3.6V||f = 48 ADC MHz(6)||-|-|4.36||
|||Resolution = 6 bits|Continuous and Discontinuous mode(5)|1.6V ≤ VDDA ≤ 3.6V|–40 °C ≤ TJ ≤ 130 °C|fADC = 75 MHz|SMP = 2.5|-|-|8.33||
||||Single mode|2.4 V ≤ V ≤ 3.6 V DDA||fADC = 75 MHz(6)||-|-|8.33||
|||||1.6V ≤ VDDA ≤ 3.6V||fADC = 55 MHz(6)||-|-|6.11||


DS13315 Rev 5 195/270


239

**Electrical characteristics** **STM32H730xB**







































|Col1|Col2|Table 86. 12-bit ADC characteristics(1)(2) (continued)|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Sym- bol|Parameter|Conditions||||||Min|Typ|Max|Unit|
|fS(4) (conti- nued)|Sampling rate for fast channels (VIN[0:5])|Resolution = 12 bits|Continuous and Discontinuous mode(5)|2.4 V ≤ VDDA ≤ 3.6 V|–40 °C ≤ TJ ≤ 130 °C|fADC = 65 MHz|SMP = 2.5|-|-|4.33|MSPS|
|||||1.6V ≤ VDDA ≤ 3.6V||fADC = 58 MHz||-|-|3.87||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||fADC = 32 MHz(6)||-|-|2.13||
|||||1.6V ≤ VDDA ≤ 3.6V||fADC = 26 MHz(6)||-|-|1.73||
|||Resolution = 10 bits|Continuous and Discontinuous mode(5)|1.6V ≤ VDDA ≤ 3.6V|–40 °C ≤ TJ ≤ 130 °C|fADC = 75 MHz|SMP = 2.5|-|-|5.77||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||fADC = 36 MHz(6)||-|-|2.77||
|||||1.6V ≤ VDDA ≤ 3.6V||fADC = 30 MHz(6)||-|-|2.31||
|||Resolution = 8 bits|Continuous and Discontinuous mode(5)|1.6V ≤ VDDA ≤ 3.6V|–40 °C ≤ TJ ≤ 130 °C|fADC = 75 MHz|SMP = 2.5|-|-|6.82||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||fADC =44 MHz(6)||-|-|4.00||
|||||1.6V ≤ VDDA ≤ 3.6V||fADC = 35 MHz(6)||-|-|3.18||
|||Resolution = 6 bits|Continuous and Discontinuous mode(5)|1.6V ≤ VDDA ≤ 3.6V|–40 °C ≤ T ≤ 130 °C J|f = 75 ADC MHz|SMP = 2.5|-|-|8.33||
||||Single mode|2.4 V ≤ VDDA ≤ 3.6 V||fADC = 56 MHz(6)||-|-|6.22||
|||||1.6V ≤ VDDA ≤ 3.6V||f = 42 ADC MHz(6)||-|-|4.66||
||Sampling rate for slow channels|Resolution = 12 bits|-|-|–40 °C ≤ T ≤ 130 °C J|fADC = 15 MHz(6)|SMP = 2.5|-|-|1.00||
|||Resolution = 10 bits||||||-|-|1.28||
|||Resolution = 8 bits||||||-|-|1.63||
|||Resolution = 6 bits||||||-|-|2.08||
|t TRIG|External trigger period|Resolution = 12 bits||||||-|-|15|1/f ADC|
|VAIN|Conversion voltage range|-||||||0|-|VREF+|V|
|VCMIV|Common mode input voltage|-||||||V REF /2− 10%|VREF /2|VREF/2 + 10%||
|RAIN (7)|External input impedance|Resolution = 12 bits, TJ = 125 °C||||||-|-|220|Ω|
|||Resolution = 10 bits, TJ = 125 °C||||||-|-|2100||
|||Resolution = 8 bits, TJ = 125 °C||||||-|-|12000||
|||Resolution = 6 bits, TJ = 125 °C||||||-|-|80000||


196/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**
















|Col1|Col2|Table 86. 12-bit ADC characteristics(1)(2) (continued)|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Sym- bol|Parameter|Conditions|Min|Typ|Max|Unit|
|CADC|Internal sample and hold capacitor|-|-|5|-|pF|
|tADCV REG_ STUP|ADC LDO startup time|-|-|5|10|µs|
|tSTAB|ADC power- up time|LDO already started|1|-|-|con- version cycle|
|tOFF_ CAL|Offset calibration time|-|135|-|-|1/fADC|
|tLATR|Trigger conversion latency for regular and injected channels without aborting the conversion|CKMODE = 00|1.5|2|2.5||
|||CKMODE = 01|-|-|2.5||
|||CKMODE = 10|-|-|2.5||
|||CKMODE = 11|-|-|2.25||
|tLATR INJ|Trigger conversion latency for regular and injected channels when a regular conversion is aborted|CKMODE = 00|2.5|3|3.5||
|||CKMODE = 01|-|-|3.5||
|||CKMODE = 10|-|-|3.5||
|||CKMODE = 11|-|-|3.25||
|tS|Sampling time|-|2.5|-|640.5||
|tCONV|Total conversion time (including sampling time)|N-bits resolution|t + S 0.5 + N|-|-||
|IDDA_ D(ADC)|ADC consumption on VDDA and VREF, Differential mode|fS= 5 MSPS|-|430|-|µA|
|||fS = 1 MSPS|-|133|-||
|||f = 0.1 MSPS S|-|51|-||
|IDDA_ SE (ADC)|ADC consumption on V and DDA VREF, Single- ended mode|fS= 5 MSPS|-|350|-||
|||fS = 1 MSPS|-|122|-||
|||fS = 0.1 MSPS|-|47|-||
|IDD (ADC)|ADC consumption on VDD per f ADC|-|-|2.4|-|µA/ MHz|


1. Guaranteed by design.

2. The voltage booster on ADC switches must be used for V DDA < 2.4 V (embedded I/O switches).

3. Depending on the package, VREF+ can be internally connected to V DDA and VREF- to V SSA .

4. Guaranteed by characterization for BGA and CSP packages. The values for LQFP packages may be different.

5. The conversion of the first element in the group is excluded.

DS13315 Rev 5 197/270


239

**Electrical characteristics** **STM32H730xB**

6. f ADC value corresponds to the maximum frequency that can be reached considering a 2.5 sampling period. For other SMPy
sampling periods, the maximum frequency is f ADC value * SMPy / 2.5 with a limitation to 75 MHz.

7. The tolerance is 2 LSBs for 12-bit, 10-bit and 8-bit resolutions. It is otherwise specified.

**Table 87. Minimum sam** **p** **lin** **g** **time vs R** **AIN** **(** **12-bit ADC** **)** **[(1)(2)]**

|Resolution|) R (Ω AIN|Minimum sampling time (s)|Col4|Col5|
|---|---|---|---|---|
|||Direct channels(3)|Fast channels(4)|Slow channels(5)|
|12 bits|47|5.55E-08|7.04E-08|1.03E-07|
||68|5.76E-08|7.22E-08|1.05E-07|
||100|6.17E-08|7.65E-08|1.07E-07|
||150|7.02E-08|8.45E-08|1.13E-07|
||220|8.59E-08|1.00E-07|1.22E-07|
||330|1.11E-07|1.26E-07|1.41E-07|
||470|1.46E-07|1.61E-07|1.69E-07|
||680|1.98E-07|2.17E-07|2.25E-07|
|10 bits|47|4.90E-08|6.06E-08|8.77E-08|
||68|5.07E-08|6.27E-08|8.95E-08|
||100|5.41E-08|6.67E-08|9.22E-08|
||150|6.18E-08|7.50E-08|9.59E-08|
||220|7.51E-08|8.70E-08|1.04E-07|
||330|9.46E-08|1.07E-07|1.17E-07|
||470|1.22E-07|1.34E-07|1.42E-07|
||680|1.63E-07|1.77E-07|1.86E-07|
||1000|2.27E-07|2.42E-07|2.43E-07|
||1500|3.27E-07|3.40E-07|3.35E-07|
||2200|4.53E-07|4.86E-07|4.73E-07|
||3300|6.56E-07|6.93E-07|6.72E-07|



198/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 87. Minimum samplin** **g** **time vs R** **AIN** **(** **12-bit ADC** **)** **[(1)(2)]** **(** **continued** **)**

|Resolution|) R (Ω AIN|Minimum sampling time (s)|Col4|Col5|
|---|---|---|---|---|
|||Direct channels(3)|Fast channels(4)|Slow channels(5)|
|8 bits|47|4.35E-08|5.31E-08|7.36E-08|
||68|4.47E-08|5.48E-08|7.47E-08|
||100|4.72E-08|5.79E-08|7.63E-08|
||150|5.33E-08|6.35E-08|7.88E-08|
||220|6.26E-08|7.26E-08|8.47E-08|
||330|7.84E-08|8.80E-08|9.48E-08|
||470|9.80E-08|1.07E-07|1.14E-07|
||680|1.28E-07|1.39E-07|1.43E-07|
||1000|1.76E-07|1.88E-07|1.90E-07|
||1500|2.49E-07|2.66E-07|2.64E-07|
||2200|3.50E-07|3.63E-07|3.63E-07|
||3300|5.09E-07|5.27E-07|5.24E-07|
||4700|7.00E-07|7.28E-07|7.09E-07|
||6800|9.84E-07|1.03E-06|1.00E-06|
||10000|1.43E-06|1.48E-06|1.44E-06|
||15000|2.10E-06|2.18E-06|2.11E-06|
|6 bits|47|3.79E-08|4.58E-08|5.74E-08|
||68|3.88E-08|4.69E-08|5.81E-08|
||100|4.09E-08|4.89E-08|5.93E-08|
||150|4.48E-08|5.25E-08|6.14E-08|
||220|5.07E-08|5.81E-08|6.58E-08|
||330|6.04E-08|6.79E-08|7.46E-08|
||470|7.37E-08|8.10E-08|8.60E-08|
||680|9.31E-08|1.01E-07|1.04E-07|
||1000|1.23E-07|1.32E-07|1.34E-07|
||1500|1.71E-07|1.82E-07|1.82E-07|
||2200|2.39E-07|2.50E-07|2.49E-07|
||3300|3.43E-07|3.57E-07|3.49E-07|
||4700|4.72E-07|4.92E-07|4.81E-07|
||6800|6.65E-07|6.89E-07|6.68E-07|
||10000|9.54E-07|9.88E-07|9.54E-07|
||15000|1.40E-06|1.45E-06|1.39E-06|



1. Guaranteed by design.

2. Data valid up to 130 °C, with a 22 pF PCB capacitor and V DDA = 1.62 V.

DS13315 Rev 5 199/270


239

**Electrical characteristics** **STM32H730xB**

3. Direct channels are connected to analog I/Os (PA0_C, PA1_C, PC2_C and PC3_C) to optimize ADC performance.

4. Fast channels correspond to ADCx_INx[0:5].

5. Slow channels correspond to all ADC inputs except for the Direct and Fast channels.
















|Col1|Col2|Table 88. 12-bit ADC accuracy(1)(2)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Symbol|Parameter|Conditions||Min|Typ|Max|Unit|
|ET|Total unadjusted error|Direct channel|Single ended|-|3.5|5|±LSB|
||||Differential|-|2.5|3||
|||Fast channel|Single ended|-|3.5|5||
||||Differential|-|2.5|3||
|||Slow channel|Single ended|-|3.5|5||
||||Differential|-|2.5|3||
|EO|Offset error|-||-|+/-2|+/-5||
|EG|Gain error|-||-|+/-2|+/-5||
|ED|Differential linearity error|Single ended||-|+/- 0.75|+1.5/- 1||
|||Differential||-|+/-0.5|+1.25 /-1||
|EL|Integral linearity error|Direct channel|Single ended|-|+/-1|+/-2.5||
||||Differential|-|+/-1|+/-2||
|||Fast channel|Single ended|-|+/-1|+/-2.5||
||||Differential|-|+/-1|+/-2||
|||Slow channel|Single ended|-|+/-1|+/-2.5||
||||Differential|-|+/-1|+/-2||
|ENOB|Effective number of bits|Single ended||-|11.2|-|bits|
|||Differential||-|11.5|-||
|SINAD|Signal-to- noise and distortion ratio|Single ended||-|68.9|-|dB|
|||Differential||-|71.1|-||
|SNR|Signal-to- noise ratio|Single ended||-|69.1|-||
|||Differential||-|71.4|-||
|THD|Total harmonic distortion|Single ended||-|-79.6|-||
|||Differential||-|-81.8|-||


200/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

1. Guaranteed by characterization for BGA packages. The maximum values are preliminary data. The values for LQFP
packages may be different.

2. ADC DC accuracy values are measured after internal calibration in Continuous and Discontinuous mode.

**6.3.24** **DAC characteristics**

**Table 89. DAC characteristics** **[(1)]**

















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|V DDA|Analog supply voltage|-||1.8|3.3|3.6|V|
|V REF+|Positive reference voltage|-||1.80|-|V DDA||
|V REF-|Negative reference voltage|-||-|V SSA|-||
|R L|Resistive Load|DAC output buffer ON|connected to V SSA|5|-|-|kΩ|
||||connected to V DDA|25|-|-||
|R O|Output Impedance|DAC output buffer OFF||10.3|13|16||
|R BON|Output impedance sample and hold mode, output buffer ON|DAC output buffer ON|V = 2.7 V DD|-|-|1.6|kΩ|
||||V = 2.0 V DD|-|-|2.6||
|R BOFF|Output impedance sample and hold mode, output buffer OFF|DAC output buffer OFF|V = 2.7 V DD|-|-|17.8|kΩ|
||||V = 2.0 V DD|-|-|18.7||
|C L|Capacitive Load|DAC output buffer OFF||-|-|50|pF|
|C SH||Sample and Hold mode||-|0.1|1|µF|
|V DAC_OUT|Voltage on DAC_OUT output|DAC output buffer ON||0.2|-|V REF+ − 0.2|V|
|||DAC output buffer OFF||0|-|V REF+||
|t SETTLING|Settling time (full scale: for a 12-bit code transition between the lowest and the highest input codes when DAC_OUT reaches the final value of ±0.5LSB, ±1LSB, ±2LSB, ±4LSB, ±8LSB)|Normal mode, DAC output buffer ON, C ≤ 50 pF, L R ≥ 5 ㏀ L|±0.5 LSB|-|2.05|3|µs|
||||±1 LSB|-|1.97|2.87||
||||±2 LSB|-|1.67|2.84||
||||±4 LSB|-|1.66|2.78||
||||±8 LSB|-|1.65|2.7||
|||Normal mode, DAC output buffer OFF, ±1LSB C =10 pF L||-|1.7|2||
|t (2) WAKEUP|Wakeup time from off state (setting the ENx bit in the DAC Control register) until the final value of ±1LSB is reached|Normal mode, DAC output buffer ON, C ≤ 50 pF, R = 5 ㏀ L L||-|5|7.5|µs|
|||Normal mode, DAC output buffer OFF, C ≤ 10 pF L|||2|5||
|PSRR|DC V supply rejection DDA ratio|Normal mode, DAC output buffer ON, C ≤ 50 pF, R = 5 ㏀ L L||-|−80|−28|dB|


DS13315 Rev 5 201/270


239

**Electrical characteristics** **STM32H730xB**

**Table 89. DAC characteristics** **[(1)]** **(** **continued** **)**


















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|t SAMP|Sampling time in Sample and Hold mode C =100 nF L (code transition between the lowest input code and the highest input code when DAC_OUT reaches the ±1LSB final value)|MODE<2:0>_V12=100/101 (BUFFER ON)||-|0.7|2.6|ms|
|||MODE<2:0>_V12=110 (BUFFER OFF)||-|11.5|18.7||
|||MODE<2:0>_V12=111 (INTERNAL BUFFER OFF)||-|0.3|0.6|µs|
|I leak|Output leakage current|-||(3)|||nA|
|C Iint|Internal sample and hold capacitor|-||1.8|2.2|2.6|pF|
|t TRIM|Middle code offset trim time|Minimum time to verify the each code||50|-|-|µs|
|V offset|Middle code offset for 1 trim code step|V = 3.6 V REF+||-|850|-|µV|
|||V = 1.8 V REF+||-|425|-||
|I DDA(DAC)|DAC quiescent consumption from V DDA|DAC output buffer ON|No load, middle code (0x800)|-|360|-|µA|
||||No load, worst code (0xF1C)|-|490|-||
|||DAC output buffer OFF|No load, middle/ worst code (0x800)|-|20|-||
|||Sample and Hold mode, C =100 nF SH||-|360*T / ON (T +T ) ON OFF (4)|-||
|I (DAC) DDV|DAC consumption from V REF+|DAC output buffer ON|No load, middle code (0x800)|-|170|-||
||||No load, worst code (0xF1C)|-|170|-||
|||DAC output buffer OFF|No load, middle/ worst code (0x800)|-|160|-||
|||Sample and Hold mode, Buffer ON, C =100 nF (worst code) SH||-|170*T / ON (T +T ) ON OFF (4)|-||
|||Sample and Hold mode, Buffer OFF, C =100 nF (worst code) SH||-|160*T / ON (T +T ) ON OFF (4)|-||


1. Guaranteed by design unless otherwise specified.

202/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

2. In buffered mode, the output can overshoot above the final value for low input code (starting from the minimum value).

3. Refer to *Table 54: I/O static characteristics* .

4. T ON is the refresh phase duration, while T OFF is the hold phase duration. Refer to the product reference manual for more
details.













|Col1|Col2|Table 90. DAC accuracy(1)|Col4|)|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Symbol|Parameter|Conditions||Min|Typ|Max|Unit|
|DNL|Differential non linearity(2)|DAC output buffer ON||−2|-|2|LSB|
|||DAC output buffer OFF||−2|-|2||
|-|Monotonicity|10 bits||-|-|-|-|
|INL|Integral non linearity(3)|DAC output buffer ON, C ≤50 pF, L R ≥ 5 ㏀ L||−4|-|4|LSB|
|||DAC output buffer OFF, C ≤ 50 pF, no R L L||−4|-|4||
|Offset|Offset error at code 0x800 (3)|DAC output buffer ON, C ≤ 50 pF, L R ≥ 5 ㏀ L|V = 3.6 V REF+|-|-|±12|LSB|
||||V = 1.8 V REF+|-|-|±25||
|||DAC output buffer OFF, C ≤ 50 pF, no R L L||-|-|±8||
|Offset1|Offset error at code 0x001(4)|DAC output buffer OFF, C ≤ 50 pF, no R L L||-|-|±5|LSB|
|OffsetCal|Offset error at code 0x800 after factory calibration|DAC output buffer ON, C ≤ 50 pF, L R ≥ 5 ㏀ L|V = 3.6 V REF+|-|-|±5|LSB|
||||V = 1.8 V REF+|-|-|±7||
|Gain|Gain error(5)|DAC output buffer ON,C ≤50 pF, L R ≥ 5 ㏀ L||-|-|±1|%|
|||DAC output buffer OFF, C ≤ 50 pF, no R L L||-|-|±1||
|TUE|Total unadjusted error|DAC output buffer ON, C ≤50 pF, L R ≥ 5 ㏀ L||-|-|±30|LSB|
|||DAC output buffer OFF, C ≤ L 50 pF, no R L||||±12||
|TUECal|Total unadjusted error after calibration|DAC output buffer ON, C ≤50 pF, L R ≥ 5 ㏀ L||-|-|±23||
|SNR|Signal-to-noise ratio(6)|DAC output buffer ON,C ≤ 50 pF, L R ≥ 5 ㏀, 1 kHz, BW = 500 KHz L||-|67.8|-|dB|
|||DAC output buffer OFF, C ≤ 50 pF, no R,1 kHz, BW = L L 500 KHz||-|67.8|-||


DS13315 Rev 5 203/270


239

**Electrical characteristics** **STM32H730xB**

**Table 90. DAC accurac** **y** **[(1)]** **(** **continued** **)**



|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|THD|Total harmonic distortion(6)|DAC output buffer ON, C ≤50 pF, L R ≥ 5 ㏀, 1 kHz L|-|−78.6|-|dB|
|||DAC output buffer OFF, C ≤ 50 pF, no R, 1 kHz L L|-|−78.6|-||
|SINAD|Signal-to-noise and distortion ratio(6)|DAC output buffer ON, C ≤50 pF, L R ≥ 5 ㏀, 1 kHz L|-|67.5|-|dB|
|||DAC output buffer OFF, C ≤ 50 pF, no R, 1 kHz L L|-|67.5|-||
|ENOB|Effective number of bits|DAC output buffer ON, C ≤ 50 pF, R ≥ 5 ㏀, 1 kHz L L|-|10.9|-|bits|
|||DAC output buffer OFF, C ≤ 50 pF, no R, 1 kHz L L|-|10.9|-||


1. Guaranteed by characterization results.

2. Difference between two consecutive codes minus 1 LSB.

3. Difference between the value measured at Code i and the value measured at Code i on a line drawn between Code 0 and
last Code 4095.

4. Difference between the value measured at Code (0x001) and the ideal value.

5. Difference between the ideal slope of the transfer function and the measured slope computed from code 0x000 and 0xFFF
when the buffer is OFF, and from code giving 0.2 V and (V REF+   - 0.2 V) when the buffer is ON.

6. Signal is −0.5dBFS with F sampling =1 MHz.

**Fi** **g** **ure 48. 12-bit buffered /non-buffered DAC**






1. The DAC integrates an output buffer that can be used to reduce the output impedance and to drive external loads directly
without the use of an external operational amplifier. The buffer can be bypassed by configuring the BOFFx bit in the
DAC_CR register.

204/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.25** **Voltage reference buffer characteristics**

**Table 91. VREFBUF characteristics** **[(1)]**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|V DDA|Analog supply voltage|Normal mode, V = 3.3 V DDA|VSCALE = 000|2.8|3.3|3.6|V|
||||VSCALE = 001|2.4|-|3.6||
||||VSCALE = 010|2.1|-|3.6||
||||VSCALE = 011|1.8|-|3.6||
|||Degraded mode(2)|VSCALE = 000|1.62|-|2.80||
||||VSCALE = 001|1.62|-|2.40||
||||VSCALE = 010|1.62|-|2.10||
||||VSCALE = 011|1.62|-|1.80||
|V REFBUF _OUT|Voltage Reference Buffer Output, at 30 °C, I = 100 µA load|Normal mode at 30 °C, I = 100 µA load|VSCALE = 000|2.4980|2.5000|2.5035||
||||VSCALE = 001|2.0460|2.0490|2.0520||
||||VSCALE = 010|1.8010|1.8040|1.8060||
||||VSCALE = 011|1.4995|1.5015|1.5040||
|||Degraded mode(2)|VSCALE = 000|V − DDA 150 mV|-|V DDA||
||||VSCALE = 001|V − DDA 150 mV|-|V DDA||
||||VSCALE = 010|V − DDA 150 mV|-|V DDA||
||||VSCALE = 011|V − DDA 150 mV|-|V DDA||
|TRIM|Trim step resolution|-|-|-|±0.05|±0.1|%|
|C L|Load capacitor|-|-|0.5|1|1.50|µF|
|esr|Equivalent Serial Resistor of C L|-|-|-|-|2|Ω|
|I LOAD|Static load current|-|-|-|-|4|mA|
|I line_reg|Line regulation|2.8 V ≤ V ≤ 3.6 V DDA|I = 500 µA load|-|200|-|ppm/V|
||||I = 4 mA load|-|100|-||
|I load_reg|Load regulation|500 µA ≤ I ≤ 4 mA LOAD|Normal mode|-|50|-|ppm/ mA|
|T coeff|Temperature coefficient|−40 °C < T < +130 °C J||-|-|T coeff V REFINT + 100|ppm/ °C|
|PSRR|Power supply rejection|DC|-|-|60|-|dB|
|||100KHz|-|-|40|-||


DS13315 Rev 5 205/270


239

**Electrical characteristics** **STM32H730xB**

**Table 91. VREFBUF characteristics** **[(1)]** **(** **continued** **)**







|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|t START|Start-up time|C =0.5 µF L|-|-|300|-|µs|
|||C =1 µF L|-|-|500|-||
|||C =1.5 µF L|-|-|650|-||
|I INRUSH|Control of maximum DC current drive on V during REFBUF_OUT startup phase(3)|-||-|8|-|mA|
|I DDA (VREFBUF)|VREFBUF consumption from V DDA|I = 0 µA LOAD|-|-|15|25|µA|
|||I = 500 µA LOAD|-|-|16|30||
|||I = 4 mA LOAD|-|-|32|50||


1. Guaranteed by design, unless otherwise specified.

2. In degraded mode, the voltage reference buffer cannot accurately maintain the output voltage (V DDA −drop voltage).

3. To properly control VREFBUF I INRUSH current during the startup phase and the change of scaling, V DDA voltage should be in
the range of 1.8 V-3.6 V, 2.1 V-3.6 V, 2.4 V-3.6 V and 2.8 V-3.6 V for VSCALE = 011, 010, 001 and 000, respectively.

**6.3.26** **Analog temperature sensor characteristics**

**Table 92. Tem** **p** **erature sensor characteristics**




|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|T (1) L|V linearity with temperature SENSE|-|-|±3|°C|
|Avg_Slope(2)|Average slope|-|2|-|mV/°C|
|V (3) 30|Voltage at 30°C ± 5 °C|-|0.62|-|V|
|t start_run|Startup time in Run mode (buffer startup)|-|-|25.2|µs|
|t (1) S_temp|ADC sampling time when reading the temperature|9|-|-||
|I (1) sens|Sensor consumption|-|0.18|0.31|µA|
|I (1) sensbuf|Sensor buffer consumption|-|3.8|6.5||


1. Guaranteed by design.

2. Guaranteed by characterization results.

3. Measured at V DDA = 3.3 V ± 10 mV. The V 30 ADC conversion result is stored in the TS_CAL1
byte.

**Table 93. Tem** **p** **erature sensor calibration values**

|Symbol|Parameter|Memory address|
|---|---|---|
|TS_CAL1|Temperature sensor raw data acquired value at 30 °C, V =3.3 V DDA|0x1FF1 E820 -0x1FF1 E821|
|TS_CAL2|Temperature sensor raw data acquired value at 130 °C, V =3.3 V DDA|0x1FF1 E840 - 0x1FF1 E841|



206/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.27** **Digital temperature sensor characteristics**

**Table 94. Di** **g** **ital tem** **p** **erature sensor characteristics** **[(1)]**







|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f (2) DTS|Output Clock frequency|-|500|750|1150|kHz|
|T (2) LC|Temperature linearity coefficient|VOS2|1660|2100|2750|Hz/° C|
|T TOTAL_ERROR (2)|Temperature offset measurement, all VOS|T =−40°C to J 30°C|−13|-|4|°C|
|||T =30°C to J Tjmax|−7|-|2||
|T VDD_CORE|Additional error due to supply variation|VOS2|0|-|0|°C|
|||VOS0, VOS1, VOS3|−1|-|1||
|t TRIM|Calibration time|-|-|-|2|ms|
|t WAKE_UP|Wake-up time from off state until DTS ready bit is set|-|-|67|116.00|μs|
|I DDCORE_DTS|DTS consumption on VDD_CORE|-|8.5|30|70.0|μA|


1. Guaranteed by design, unless otherwise specified.

2. Guaranteed by characterization results.

**6.3.28** **Temperature and V** **BAT** **monitoring**

**Table 95. V** **BAT** **monitorin** **g** **characteristics**




|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|R|Resistor bridge for V BAT|-|26|-|KΩ|
|Q|Ratio on V measurement BAT|-|4|-|-|
|Er(1)|Error on Q|–10|-|+10|%|
|t (1) S_vbat|ADC sampling time when reading V input BAT|9|-|-|µs|
|V BAThigh|High supply monitoring|-|3.55|-|V|
|V BATlow|Low supply monitoring|-|1.36|-||


1. Guaranteed by design.

**Table 96. V** **BAT** **char** **g** **in** **g** **characteristics**

|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|R BC|Battery charging resistor|VBRS in PWR_CR3= 0|-|5|-|KΩ|
|||VBRS in PWR_CR3= 1||1.5|-||



DS13315 Rev 5 207/270


239

**Electrical characteristics** **STM32H730xB**

**Table 97. Tem** **p** **erature monitorin** **g** **characteristics**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|TEMP high|High temperature monitoring|-|117|-|°C|
|TEMP low|Low temperature monitoring|-|–25|-||



**6.3.29** **Voltage booster for analog switch**

**Table 98. Volta** **g** **e booster for analo** **g** **switch characteristics** **[(1)]**

|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V DD|Supply voltage|-|1.62|2.6|3.6|V|
|t SU(BOOST)|Booster startup time|-|-|-|50|µs|
|I DD(BOOST)|Booster consumption|1.62 V ≤ V ≤ 2.7 V DD|-|-|125|µA|
|||2.7 V < V < 3.6 V DD|-|-|250||



1. Guaranteed by characterization results.

**6.3.30** **Comparator characteristics**

**Table 99. COMP characteristics** **[(1)]**







|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V DDA|Analog supply voltage|-|1.62|3.3|3.6|V|
|V IN|Comparator input voltage range|-|0|-|V DDA||
|V BG|Scaler input voltage|-|(2)||||
|V SC|Scaler offset voltage|-|-|±5|±10|mV|
|I DDA(SCALER)|Scaler static consumption from V DDA|BRG_EN=0 (bridge disable)|-|0.2|0.3|µA|
|||BRG_EN=1 (bridge enable)|-|0.8|1||
|t START_SCALER|Scaler startup time|-|-|140|250|µs|
|t START|Comparator startup time to reach propagation delay specification|High-speed mode|-|2|5|µs|
|||Medium mode|-|5|20||
|||Ultra-low-power mode|-|15|80||
|t (3) D|Propagation delay for 200 mV step with 100 mV overdrive|High-speed mode|-|50|80|ns|
|||Medium mode|-|0.5|0.9|µs|
|||Ultra-low-power mode|-|2.5|7||
||Propagation delay for step > 200 mV with 100 mV overdrive only on positive inputs|High-speed mode|-|50|120|ns|
|||Medium mode|-|0.5|1.2|µs|
|||Ultra-low-power mode|-|2.5|7||
|V offset|Comparator offset error|Full common mode range|-|±5|±20|mV|


208/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 99. COMP characteristics** **[(1)]** **(** **continued** **)**





|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|V hys|Comparator hysteresis|No hysteresis||-|0|-|mV|
|||Low hysteresis||4|10|22||
|||Medium hysteresis||8|20|37||
|||High hysteresis||16|30|52||
|I (COMP) DDA|Comparator consumption from V DDA|Ultra-low- power mode|Static|-|400|600|nA|
||||With 50 kHz ±100 mV overdrive square signal|-|800|-||
|||Medium mode|Static|-|5|7|µA|
||||With 50 kHz ±100 mV overdrive square signal|-|6|-||
|||High-speed mode|Static|-|70|100||
||||With 50 kHz ±100 mV overdrive square signal|-|75|-||


1. Guaranteed by design, unless otherwise specified.

2. Refer to *Table 20: Embedded reference voltage* .

3. Guaranteed by characterization results.

**6.3.31** **Operational amplifier characteristics**

**Table 100. O** **p** **erational am** **p** **lifier characteristics** **[(1)]**








|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V DDA|Analog supply voltage Range|-|2|3.3|3.6|V|
|CMIR|Common Mode Input Range|-|0|-|V DDA||
|VI OFFSET|Input offset voltage|25°C, no load on output|-|-|±1.5|mV|
|||All voltages and temperature, no load|-|-|±2.5||
|ΔVI OFFSET|Input offset voltage drift|-|-|±3.0|-|μV/°C|
|TRIMOFFSETP TRIMLPOFFSETP|Offset trim step at low common input voltage (0.1*V ) DDA|-|-|1.1|1.5|mV|
|TRIMOFFSETN TRIMLPOFFSETN|Offset trim step at high common input voltage (0.9*V ) DDA|-|-|1.1|1.5||
|I LOAD|Drive current|-|-|-|500|μA|
|I LOAD_PGA|Drive current in PGA mode|-|-|-|270||


DS13315 Rev 5 209/270


239

**Electrical characteristics** **STM32H730xB**

**Table 100. O** **p** **erational am** **p** **lifier characteristics** **[(1)]** **(** **continued** **)**


















|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|C LOAD|Capacitive load|-||-|-|50|pF|
|CMRR|Common mode rejection ratio|-||-|80|-|dB|
|PSRR|Power supply rejection ratio|C ≤ 50pf / LOAD R ≥ 4 kΩ(2) at 1 kHz, LOAD V =V /2 com DDA||50|66|-|dB|
|GBW|Gain bandwidth for high supply range|200 mV ≤ Output dynamic range ≤ V - 200 mV DDA||4|7.3|12.3|MHz|
|SR|Slew rate (from 10% and 90% of output voltage)|Normal mode||-|3|-|V/µs|
|||High-speed mode||-|24|-||
|AO|Open loop gain|200 mV ≤ Output dynamic range ≤ V - 200 mV DDA||59|90|129|dB|
|φm|Phase margin|-||-|55|-|°|
|GM|Gain margin|-||-|12|-|dB|
|V OHSAT|High saturation voltage|I =max or R =min, load LOAD Input at V DDA||V DDA −100 mV|-|-|mV|
|V OLSAT|Low saturation voltage|I =max or R =min, load LOAD Input at 0 V||-|-|100||
|t WAKEUP|Wake up time from OFF state|Normal mode|C ≤ 50pf, LOAD R ≥ 4 kΩ, LOAD follower configuration|-|0.8|3.2|µs|
|||High speed mode|C ≤ 50pf, LOAD R ≥ 4 kΩ, LOAD follower configuration|-|0.9|2.8||
|PGA gain|Non inverting gain error value|PGA gain = 2||−1|-|1|%|
|||PGA gain = 4||−2|-|2||
|||PGA gain = 8||−2.5|-|2.5||
|||PGA gain = 16||−3|-|3||
||Inverting gain error value|PGA gain = 2||−1|-|1||
|||PGA gain = 4||−1|-|1||
|||PGA gain = 8||−2|-|2||
|||PGA gain = 16||−3|-|3||
||External non-inverting gain error value|PGA gain = 2||−1|-|1||
|||PGA gain = 4||−3|-|3||
|||PGA gain = 8||−3.5|-|3.5||
|||PGA gain = 16||−4|-|4||


210/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 100. O** **p** **erational am** **p** **lifier characteristics** **[(1)]** **(** **continued** **)**










|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|R network|R2/R1 internal resistance values in non-inverting PGA mode(3)|PGA Gain=2||-|10/10|-|kΩ/ kΩ|
|||PGA Gain=4||-|30/10|-||
|||PGA Gain=8||-|70/10|-||
|||PGA Gain=16||-|150/10|-||
||R2/R1 internal resistance values in inverting PGA mode(3)|PGA Gain = -1||-|10/10|-||
|||PGA Gain = -3||-|30/10|-||
|||PGA Gain = -7||-|70/10|-||
|||PGA Gain = -15||-|150/10|-||
|Delta R|Resistance variation (R1 or R2)|-||−15|-|15|%|
|PGA BW|PGA bandwidth for different non inverting gain|Gain=2||-|GBW/2|-|MHz|
|||Gain=4||-|GBW/4|-||
|||Gain=8||-|GBW/8|-||
|||Gain=16||-|GBW/16|-||
||PGA bandwidth for different inverting gain|Gain = -1||-|5.00|-|MHz|
|||Gain = -3||-|3.00|-||
|||Gain = -7||-|1.50|-||
|||Gain = -15||-|0.80|-||
|en|Voltage noise density|at 1 KHz|output loaded with 4 kΩ|-|140|-|nV/√ Hz|
|||at 10 KHz||-|55|-||
|I DDA(OPAMP)|OPAMP consumption from V DDA|Normal mode|no Load, quiescent mode, follower|-|570|1000|µA|
|||High- speed mode||-|610|1200||


1. Guaranteed by design, unless otherwise specified.





2. R LOAD is the resistive load connected to V SSA or to V DDA .

3. R2 is the internal resistance between the OPAMP output and th OPAMP inverting input. R1 is the internal resistance
between the OPAMP inverting input and ground. PGA gain = 1 + R2/R1.

DS13315 Rev 5 211/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.32** **Digital filter for Sigma-Delta Modulators (DFSDM) characteristics**

Unless otherwise specified, the parameters given in *Table 101* for DFSDM are derived from
tests performed under the ambient temperature, fPCLKx frequency and supply voltage
conditions summarized in *Table 12: General operating conditions* .

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C L = 30 pF

      - Measurement points are done at CMOS levels: 0.5V DD

      - VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output alternate
function characteristics (DìFSDM_CKINx, DFSDM_DATINx, DFSDM_CKOUT for DFSDM).

**Table 101. DFSDM measured timin** **g**











|Symbol|Parameter|Conditions|Col4|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|---|
|f DFSDMCLK|DFSDM clock|1.62 < V < 3.6 V DD||-|-|(1)|MHz|
|f CKIN (1/T ) CKIN|Input clock frequency|SPI mode (SITP[1:0] = 0,1), External clock mode (SPICKSEL[1:0] = 0)||-|-|20||
|||SPI mode (SITP[1:0] = 0,1), Internal clock mode (SPICKSEL[1:0] # 0)||-|-|20||
|f CKOUT|Output clock frequency|1.62 < V < 3.6 V DD||-|-|20||
|DuCy CKOUT|Output clock frequency duty cycle|1.62 < V DD < 3.6 V|Even division, CKOUTDIV = n, 1, 3, 5..|45|50|55|%|
||||Odd division, CKOUTDIV = n, 2, 4, 6..|(((n/2+1)/(n+1)) *100)−5|(((n/2+1)/(n+1)) *100)|(((n/2+1)/(n+1)) *100)+5||


212/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 101. DFSDM measured timin** **g** **(** **continued** **)**









|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|t wh(CKIN) t wl(CKIN)|Input clock high and low time|SPI mode (SITP[1:0] = 0,1), External clock mode (SPICKSEL[1:0] = 0)|T /2−0.5 CKIN|T /2 CKIN|-|ns|
|t su|Data input setup time|SPI mode (SITP[1:0] = 0,1), External clock mode (SPICKSEL[1:0] = 0)|2|-|-||
|t h|Data input hold time|SPI mode (SITP[1:0] = 0,1), External clock mode (SPICKSEL[1:0] = 0)|1|-|-||
|T Manchester|Manchester data period (recovered clock period)|Manchester mode (SITP[1:0] = 2,3), Internal clock mode (SPICKSEL[1:0] # 0)|(CKOUTDIV+1) * T DFSDMCLK|-|(2*CKOUTDIV) * T DFSDMCLK||


1. The maximum DFSDM kernel clock frequency is specified in the RCC chapter of the reference manual (RM0468).

DS13315 Rev 5 213/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 49. Channel transceiver timin** **g** **dia** **g** **rams**









214/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**6.3.33** **Camera interface (DCMI) timing specifications**

Unless otherwise specified, the parameters given in *Table 102* for DCMI are derived from
tests performed under the ambient temperature, f HCLK frequency and VDD supply voltage
summarized in *Table 12: General operating conditions*, with the following configuration:

      - DCMI_PIXCLK polarity: falling

      - DCMI_VSYNC and DCMI_HSYNC polarity: high

      - Data formats: 14 bits

      - Capacitive load C L =30 pF

      - Measurement points are done at CMOS levels: 0.5V DD

      - VOS level set to VOS0


|Col1|Table 102. DCMI characteristics(1)|Col3|Col4|Col5|
|---|---|---|---|---|
|Symbol|Parameter|Min|Max|Unit|
|-|Frequency ratio DCMI_PIXCLK/f HCLK|-|0.4|-|
|DCMI_PIXCLK|Pixel Clock input|-|110|MHz|
|D pixel|Pixel Clock input duty cycle|30|70|%|
|t DATA) su(|Data input setup time|2|-|ns|
|t (DATA) h|Data hold time|1|-||
|tsu(HSYNC), tsu(VSYNC)|DCMI_HSYNC/ DCMI_VSYNC input setup time|2|-||
|th(HSYNC), th(VSYNC)|DCMI_HSYNC/ DCMI_VSYNC input hold time|1|-||


1. Guaranteed by characterization results.

**Fi** **g** **ure 50. DCMI timin** **g** **dia** **g** **ram**





|Col1|Col2|
|---|---|
||t su(VSY|
|||


DS13315 Rev 5 215/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.34** **Parallel synchronous slave interface (PSSI) characteristics**

Unless otherwise specified, the parameters given in *Table 103* and *Table 104* for PSSI are
derived from tests performed under the ambient temperature, f HCLK frequency and VDD
supply voltage summarized in *Table 12: General operating conditions* .

**Table 103. PSSI transmit characteristics** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|-|Frequency ratio PSSI_PDCK/f HCLK|-|0.4|-|
|PSSI_PDCK|PSSI Clock input|-|50|MHz|
|||-|35(2)||
|D pixel|PSSI Clock input duty cycle|30|70|%|
|t (DATA) ov|Data output valid time|-|10|ns|
|-|-|-|(2) 14||
|t (DATA) oh|Data output hold time|4.5|-||
|t (DE) ov(|DE output valid time|-|10||
|t (DE) oh|DE output hold time|4|-||
|tsu(RDY)|RDY input setup time|0|-||
|th(RDY)|RDY input hold time|0|-||


1. Guaranteed by characterization results.

2. This value is obtained by using PA9, PA10 or PH4 I/O.

**Table 104. PSSI receive characteristics** **[(1)]**



|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|-|Frequency ratio PSSI_PDCK/f HCLK|-|0.4|-|
|PSSI_PDCK|PSSI Clock input|-|110|MHz|
|D pixel|PSSI Clock input duty cycle|30|70|%|
|t (DATA) su|Data input setup time|1.5|-|ns|
|t (DATA) h|Data input hold time|0.5|-||
|t (DE) su(|DE input setup time|2|-||
|t (DE) h|DE input hold time|1|-||
|tov(RDY)|RDY output valid time|-|15||
|toh(RDY)|RDY output hold time|5.5|-||


1. Guaranteed by characterization results.

216/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.35** **LCD-TFT controller (LTDC) characteristics**

Unless otherwise specified, the parameters given in *Table 105* for LCD-TFT are derived
from tests performed under the ambient temperature, f HCLK frequency and VDD supply
voltage summarized in *Table 12: General operating conditions*, with the following
configuration:

      - LCD_CLK polarity: high

      - LCD_DE polarity: low

      - LCD_VSYNC and LCD_HSYNC polarity: high

      - Pixel formats: 24 bits

      - Output speed is set to OSPEEDRy[1:0] = 11

      - Capacitive load C L =30 pF

      - Measurement points are done at CMOS levels: 0.5VDD

      - IO Compensation cell activated.

      - HSLV activated when V DD ≤ 2.7 V

      - VOS level set to VOS0

**Table 105. LTDC characteristics** **[(1)]**











|Symbol|Parameter|Col3|Col4|Min|Max|Unit|
|---|---|---|---|---|---|---|
|f CLK|LTDC clock output frequency|2.7<V <3.6 V, 20 pF DD||-|150|MHz|
|||2.7<V <3.6 V DD|||133||
|||1.62<V <3.6 V DD|||90/76.5(2)||
|D CLK|LTDC clock output duty cycle|||45|55|%|
|t w(CLKH), t w(CLKL)|Clock High time, low time|||t //2−0.5 w(CLK)|t /2+0.5 w(CLK)|ns|
|t v(DATA)|Data output valid time||2.7<V <3.6 V DD|-|2.0||
||||1.62<V <3.6 V DD||2.5/6.5(2)||
|t h(DATA)|Data output hold time|||0|-||
|t v(HSYNC), t v(VSYNC), t v(DE)|HSYNC/VSYNC/DE output valid time||2.7<V <3.6 V DD|-|1.5||
||||1.62<V <3.6 V DD|-|2.0||
|t h(HSYNC), t, h(VSYNC) t h(DE)|HSYNC/VSYNC/DE output hold time|||0|-||


1. Guaranteed by characterization results.

2. This value is valid when PA[9], PA[10], PA[11], PA[12], PA[15], PB[11], PH[4], PJ[8], PJ[9], PJ[10], PJ[11], PK[0], PK[1] or
PK[2] is used.

DS13315 Rev 5 217/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 51. LCD-TFT horizontal timin** **g** **dia** **g** **ram**




|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
||tv(DE)|||t|v(HSYNC)|
|||||th(DE)||
||tv(D|||||
|||||||




**Fi** **g** **ure 52. LCD-TFT vertical timin** **g** **dia** **g** **ram**







218/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**6.3.36** **Timer characteristics**

The parameters given in *Table 106* are guaranteed by design.

Refer to *Section 6.3.17: I/O port characteristics* for details on the input/output alternate
function characteristics (output compare, input capture, external clock, PWM output).

**Table 106. TIMx characteristics** **[(1)(2)]**






|Symbol|Parameter|Conditions(3)|Min|Max|Unit|
|---|---|---|---|---|---|
|t res(TIM)|Timer resolution time|AHB/APBx prescaler=1 or 2 or 4, f = TIMxCLK 275 MHz|1|-|t TIMxCLK|
|||AHB/APBx prescaler>4, f = TIMxCLK 137.5 MHz|1|-|t TIMxCLK|
|f EXT|Timer external clock frequency on CH1 to CH4|f = 240 MHz TIMxCLK|0|f /2 TIMxCLK|MHz|
|Res TIM|Timer resolution||-|16/32|bit|
|t MAX_COUNT|Maximum possible count with 32-bit counter|-|-|65536 × 65536|t TIMxCLK|


1. TIMx is used as a general term to refer to the TIM1 to TIM17 timers.

2. Guaranteed by design.

3. The maximum timer frequency on APB1 or APB2 is up to 275 MHz, by setting the TIMPRE bit in the
RCC_CFGR register, if APBx prescaler is 1 or 2 or 4, then TIMxCLK = rcc_hclk1, otherwise TIMxCLK = 4x
F or TIMxCLK = 4x F .
rcc_pclkx1 rcc_pclkx2

**6.3.37** **Low-power timer characteristics**

The parameters given in *Table 107* are guaranteed by design.

Refer to *Section 6.3.17: I/O port characteristics* for details on the input/output alternate
function characteristics (output compare, input capture, external clock, PWM output).

**Table 107. LPTIMx characteristics** **[(1)(2)]**

|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t res(TIM)|Timer resolution time|1|-|t TIMxCLK|
|f LPTIMxCLK|Timer kernel clock|0|137.5|MHz|
|f EXT|Timer external clock frequency on Input1 and Input2|0|f /2 LPTIMxCLK||
|Res TIM|Timer resolution|-|16|bit|
|t MAX_COUNT|Maximum possible count|-|65536|t TIMxCLK|



1. LPTIMx is used as a general term to refer to the LPTIM1 to LPTIM5 timers.

2. Guaranteed by design.

DS13315 Rev 5 219/270


239

**Electrical characteristics** **STM32H730xB**

**6.3.38** **Communication interfaces**

**I** **[2]** **C interface characteristics**

The I [2] C interface meets the timings requirements of the I [2] C-bus specification and user
manual revision 03 for:

      - Standard-mode (Sm): with a bit rate up to 100 kbit/s

      - Fast-mode (Fm): with a bit rate up to 400 kbit/s

      - Fast-mode Plus (Fm+): with a bit rate up to 1 Mbit/s.

The I [2] C timings requirements are guaranteed by design when the I [2] C peripheral is properly
configured (refer to RM0399 reference manual) and when the i2c_ker_ck frequency is
greater than the minimum shown in the table below:

**Table 108. Minimum i2c** **_** **ker** **_** **ck fre** **q** **uenc** **y** **in all I** **[2]** **C modes**



|Symbol|Parameter|Condition|Col4|Min|Unit|
|---|---|---|---|---|---|
|f(I2CCLK)|I2CCLK frequency|Standard-mode|-|2|MHz|
|||Fast-mode|Analog Filtre ON DNF=0|8||
||||Analog Filtre OFF DNF=1|9||
|||Fast-mode Plus|Analog Filtre ON DNF=0|17||
||||Analog Filtre OFF DNF=1|16|-|


The SDA and SCL I/O requirements are met with the following restrictions:

- The SDA and SCL I/O pins are not “true” open-drain. When configured as open-drain,
the PMOS connected between the I/O pin and V DD is disabled, but still present.

- The 20 mA output drive requirement in Fast-mode Plus is not supported. This limits the
maximum load C Load supported in Fm+, which is given by these formulas:

t r(SDA/SCL) =0.8473xR P * C Load
R P(min) = (V DD -V OL(max) )/I OL(max)
Where R P is the I2C lines pull-up. Refer to *Section 6.3.17: I/O port characteristics* for
the I [2] C I/Os characteristics.

All I [2] C SDA and SCL I/Os embed an analog filter. Refer to the table below for the analog fil
ter characteristics:

**Table 109. I** **[2]** **C analo** **g** **filter characteristics** **[(1)]**


|Symbol|Parameter|Min|Max|Unit|
|---|---|---|---|---|
|t AF|Maximum pulse width of spikes that are suppressed by analog filter|50(2)|80(3)|ns|


1. Guaranteed by characterization results.

2. Spikes with widths below t AF(min) are filtered.

3. Spikes with widths above t AF(max) are not filtered.

220/270 DS13315 Rev 5



**STM32H730xB** **Electrical characteristics**

**USART interface characteristics**

Unless otherwise specified, the parameters given in *Table 110* for USART are derived from
tests performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
conditions summarized in *Table 12: General operating conditions*, with the following
configuration:

       - Output speed is set to OSPEEDRy[1:0] = 11

       - Capacitive load C L = 30 pF

       - Measurement points are done at CMOS levels: 0.5V DD

       - IO Compensation cell activated.

       - VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output alternate
function characteristics (NSS, CK, TX, RX for USART).

**Table 110. USART** **(** **SPI mode** **)** **characteristics** **[(1)]**












|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f CK|USART clock frequency|SPI master mode, 1.62 V < V < 3.6 V DD|-|-|17.0|MHz|
|||SPI slave receiver mode, 1.62 V < V < 3.6 V DD|||45.0||
|||SPI slave transmitter mode, 1.62 V < V < 3.6 V DD|-|-|27.0||
|||SPI slave transmitter mode, 2.5 V < V < 3.6 V DD|||37.0||
|t su(NSS)|NSS setup time|SPI slave mode|t +1 ker|-|-|ns|
|t h(NSS)|NSS hold time|SPI slave mode|2|-|-||
|t, w(CKH) t w(CKL)|CK high and low time|SPI master mode|1/f /2-2 CK|1/f /2 CK|1/f /2+2 CK||
|t su(RX)|Data input setup time|SPI master mode|16|-|-||
|||SPI slave mode|1.0|-|-||
|t h(RX)|Data input hold time|SPI master mode|0|-|-||
|||SPI slave mode|2.0|-|-||
|t v(TX)|Data output valid time|SPI slave mode,, 1.62 V < V < 3.6 V DD|-|12.0|18||
|||SPI slave mode, 2.5 V < V < 3.6 V DD|-|12.0|13.5||
|||SPI master mode|-|0.5|1||
|t h(TX)|Data output hold time|SPI slave mode|9|-|-||
|||SPI master mode|0|-|-||


1. Guaranteed by characterization results.


DS13315 Rev 5 221/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 53. USART timin** **g** **dia** **g** **ram in SPI master mode**






1. Measurement points are done at 0.5V DD and with external C L = 30 pF.












|Col1|Figure 54. USART timing diagram in SPI slave mode|
|---|---|
||NSS input 1/f t CK h(NSS) t t su(NSS) w(CKH) CPHA=0 CPOL=0 input CK CPHA=0 CPOL=1 t v(TX) th(TX) wt (C K L) TX output First bit OUT Next bits OUT Last bit OUT t su(RX) t h(RX) RX input First bit IN Next bits IN Last bit IN MSv65387V6|
||NSS input 1/f t CK h(NSS) t t su(NSS) w(CKH) CPHA=0 CPOL=0 input CK CPHA=0 CPOL=1 t v(TX) th(TX) wt (C K L) TX output First bit OUT Next bits OUT Last bit OUT t su(RX) t h(RX) RX input First bit IN Next bits IN Last bit IN MSv65387V6|


222/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**SPI interface characteristics**

Unless otherwise specified, the parameters given in *Table 111* for SPI are derived from tests
performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
conditions summarized in *Table 12: General operating conditions*, with the following
configuration:

      - Output speed is set to OSPEEDRy[1:0] = 11

      - Capacitive load C L = 30 pF

      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.

      - HSLV activated when VDD ≤ 2.7 V

      - VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output alternate
function characteristics (SS, SCK, MOSI, MISO for SPI).

**Table 111. SPI characteristics** **[(1)(2)]**







|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f SCK|SPI clock frequency|Master mode, 2.7 V < V < 3.6 V, SPI1, 2, 3 DD|-|-|125|MHz|
|||Master mode, 1.62 V < V < 3.6 V, SPI1, 2, DD 3|||80/66(3)||
|||Master mode, 1.62 V < V < 3.6 V, SPI4, 5, DD 6|||68.5||
|||Slave receiver mode, 1.62 V < V < 3.6 V, SPI1, 2, DD 3|||100||
|||Slave receiver mode, 1.62 V < V < 3.6 V, SPI4, 5, DD 6|||68.5||
|||Slave mode transmitter/full duplex, 2.7 V < V < 3.6 V DD|||45||
|||Slave mode transmitter/full duplex, 1.62 V < V < 3.6 V DD|||42.5/31(4)||
|t su(NSS)|NSS setup time|Slave mode|2|-|-|-|
|t h(NSS)|NSS hold time|Slave mode|1|-|-||
|t, w(SCKH) t w(SCKL)|SCK high and low time|Master mode|t /2-1(5) SCK|t /2(5) SCK|t /2+1(5) SCK||


DS13315 Rev 5 223/270


239

**Electrical characteristics** **STM32H730xB**

**Table 111. SPI characteristics** **[(1)(2)]** **(** **continued** **)**





|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|t su(MI)|Data input setup time|Master mode|2.5|-|-|ns|
|t su(SI)||Slave mode|1|-|-||
|t h(MI)|Data input hold time|Master mode|3|-|-||
|t h(SI)||Slave mode|1.5|-|-||
|t a(SO)|Data output access time|Slave mode|9|13|27||
|t dis(SO)|Data output disable time|Slave mode|0|1|5||
|t v(SO)|Data output valid time|Slave mode, 2.7 V < V < 3.6 V DD|-|7.5|11||
|||Slave mode, 1.62 V < V < 3.6 V DD|-|7.5|12/16(4)||
|t v(MO)||Master mode, 1.62 V < V < 3.6 V DD|-|1|1.5/5.5(6)||
|t h(SO)|Data output hold time|Slave mode|7|-|-||
|t h(MO)||Master mode|0.5|-|-||


1. Guaranteed by characterization results.

2. The values given in the above table might be degraded when PC3_C/PC2_C I/Os are used (not available on all packages).

3. This value is obtained by using PA9 or PA12 I/O.

4. This value is obtained by using PC2 or PJ11 I/O.

5. t SCK = t ker_ ck - baud rate prescaler.

6. This value is obtained by using PC3 or PJ10 I/O.

**Fi** **g** **ure 55. SPI timin** **g** **dia** **g** **ram - slave mode and CPHA = 0**














224/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 56. SPI timin** **g** **dia** **g** **ram - slave mode and CPHA = 1**











**Fi** **g** **ure 57. SPI timin** **g** **dia** **g** **ram - master mode**









DS13315 Rev 5 225/270


239

**Electrical characteristics** **STM32H730xB**

**I** **[2]** **S Interface characteristics**

Unless otherwise specified, the parameters given in *Table 112* for I [2] S are derived from tests
performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
conditions summarized in *Table 12: General operating conditions*, with the following
configuration:

      - Output speed is set to OSPEEDRy[1:0] = 11

      - Capacitive load C L = 30 pF

      - Measurement points are done at CMOS levels: 0.5V DD

      - IO Compensation cell activated.

      - HSLV activated when VDD ≤ 2.7 V

      - VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output alternate
function characteristics (CK,SD,WS).

**Table 112. I** **[2]** **S d** **y** **namic characteristics** **[(1)]**











|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|f MCK|I2S main clock output|-|-|50|MHz|
|||Master transmitter|-|50/40(2)||
|||Master receiver|-|50/40(2)||
|||Slave transmitter|-|41.5/31(3)||
|||Slave receiver|-|50||
|t v(WS)|WS valid time|Master mode|-|2/6(4)|ns|
|t h(WS)|WS hold time||1|-||
|t su(WS)|WS setup time|Slave mode|3|-||
|t h(WS)|WS hold time||1|-||
|t su(SD_MR)|Data input setup time|Master receiver|2.5|-||
|t su(SD_SR)||Slave receiver|1|-||
|t h(SD_MR)|Data input hold time|Master receiver|3|-||
|t h(SD_SR)||Slave receiver|1.5|-||
|t v(SD_ST)|Data output valid time|Slave transmitter (after enable edge)|-|12/16(3)||
|t v(SD_MT)||Master transmitter (after enable edge)|-|2/6(5)||
|t h(SD_ST)|Data output hold time|Slave transmitter (after enable edge)|6.5|-||
|t h(SD_MT)||Master transmitter (after enable edge)|0.5|-||


1. Guaranteed by characterization results.

2. This value is obtained when PA9 or PA12 are used.

3. This value is obtained when PC2 is used.

4. This value is obtained when PA11 or PA15 are used.

226/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

5. This value is obtained when PC3 is used.

**Fi** **g** **ure 58. I** **[2]** **S slave timin** **g** **dia** **g** **ram** **(** **Phili** **p** **s** **p** **rotocol** **)** **[(1)]**

1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.

**Fi** **g** **ure 59. I** **[2]** **S master timin** **g** **dia** **g** **ram** **(** **Phili** **p** **s** **p** **rotocol** **)** **[(1)]**

1. LSB transmit/receive of the previously transmitted byte. No LSB transmit/receive is sent before the first
byte.

DS13315 Rev 5 227/270


239

**Electrical characteristics** **STM32H730xB**

**SAI characteristics**

Unless otherwise specified, the parameters given in *Table 113* for SAI are derived from tests
performed under the ambient temperature, f PCLKx frequency and VDD supply voltage
conditions summarized in *Table 12: General operating conditions*, with the following
configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - Capacitive load C L = 30 pF

      - IO Compensation cell activated.

      - Measurement points are done at CMOS levels: 0.5V DD

      - VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output

alternate function characteristics (SCK,SD,WS).

**Table 113. SAI characteristics** **[(1)]**





|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|f MCK|SAI Main clock output|-|-|50|MHz|
|f CK|SAI clock frequency(2)|Master transmitter, 2.7 V ≤ V ≤ 3.6 V DD|-|45||
|||Master transmitter, 1.62 V ≤ V ≤ 3.6 V DD|-|32||
|||Master receiver, 1.62 V ≤ V ≤ 3.6 V DD|-|32||
|||Slave transmitter, 2.7 V ≤ V ≤ 3.6 V DD|-|47.5||
|||Slave transmitter, 1.62 V ≤ V ≤ 3.6 V DD|-|41.5||
|||Slave receiver, 1.62 V ≤ V ≤ 3.6 V DD|-|50||


228/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 113. SAI characteristics** **[(1)]** **(** **continued)**









|Symbol|Parameter|Conditions|Min|Max|Unit|
|---|---|---|---|---|---|
|t v(FS)|F valid time S|Master mode, 2.7 V ≤ V ≤ 3.6 V DD|-|11|ns|
|||Master mode, 1.62 V ≤ V ≤ 3.6 V DD|-|15.5||
|t su(FS)|F setup time S|Slave mode|2.5|-||
|t h(FS)|F hold time S|Master mode|6|-||
|||Slave mode|0.5|-||
|t su(SD_A_MR)|Data input setup time|Master receiver|3|-||
|t su(SD_B_SR)||Slave receiver|3.5|-||
|t h(SD_A_MR)|Data input hold time|Master receiver|3.5|-||
|t h(SD_B_SR)||Slave receiver|0|-||
|t v(SD_B_ST)|Data output valid time|Slave transmitter (after enable edge), 2.7 V ≤ V ≤ 3.6 V DD|-|10.5||
|||Slave transmitter (after enable edge), 1.62 V ≤ V ≤ 3.6 V DD|-|12||
|t h(SD_B_ST)|Data output hold time|Slave transmitter (after enable edge)|6.5|-||
|t v(SD_A_MT)|Data output valid time|Master transmitter (after enable edge), 2.7 V ≤ V ≤ 3.6 V DD|-|10.5||
|||Master transmitter (after enable edge), 1.62 V ≤ V ≤ 3.6 V DD|-|14.5||
|t h(SD_A_MT)|Data output hold time|Master transmitter (after enable edge)|6|-||


1. Guaranteed by characterization results.

2. APB clock frequency must be at least twice SAI clock frequency.

**Fi** **g** **ure 60. SAI master timin** **g** **waveforms**









DS13315 Rev 5 229/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 61. SAI slave timin** **g** **waveforms**

1/fSCK

SAI_SCK_X
(CKSTR = 0)

SAI_SCK_X
(CKSTR = 1)

tw(CKH_X) tw(CKL_X) th(FS)

SAI_FS_X
(input)


tsu(FS)

SAI_SD_X
(transmit)

SAI_SD_X
(receive)

**MDIO characteristics**


tv(SD_ST) th(SD_ST)


Slot n+2


tsu(SD_SR)


Slot n

Slot n


th(SD_SR)


MS32772V2


Unless otherwise specified, the parameters given in *Table 114* for the MDIO are derived
from tests performed under the ambient temperature, f PCLKx frequency and VDD supply
voltage conditions summarized in *Table 12: General operating conditions*, with the following
configuration:

      - Output speed is set to OSPEEDRy[1:0] = 10

      - I/O Compensation cell activated.

      - Measurement points are done at CMOS levels: 0.5V DD

      - HSLV activated when V DD ≤ 2.7 V

      - VOS level set to VOS0

**Table 114. MDIO slave timin** **g** **p** **arameters**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|F MDC|Management Data Clock|-|-|30|MHz|
|t d(MDIO)|Management Data Iput/output output valid time|8|10|18|ns|
|t su(MDIO)|Management Data Iput/output setup time|1|-|-||
|t h(MDIO)|Management Data Iput/output hold time|1|-|-||



230/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 62. MDIO slave timin** **g** **dia** **g** **ram**





**SD/SDIO MMC card host interface (SDMMC) characteristics**

Unless otherwise specified, the parameters given in *Table 115* and *Table 116* for SDIO are
derived from tests performed under the ambient temperature, f PCLKx frequency and VDD
supply voltage summarized in *Table 12: General operating conditions*, with the following
configuration:

- Output speed is set to OSPEEDRy[1:0] = 11

- Capacitive load C L =30 pF

- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.

- HSLV activated when V DD ≤ 2.7 V

- VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output

characteristics.

**Table 115. D** **y** **namics characteristics: SD / MMC characteristics, V** **DD** **= 2.7 to 3.6 V** **(1)(2)**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f PP|Clock frequency in data transfer mode|-|0|-|120|MHz|
|-|SDIO_CK/fPCLK2 frequency ratio|-|-|-|8/3|-|
|t W(CKL)|Clock low time|f =52MHz PP|8.5|9.5|-|ns|
|t W(CKH)|Clock high time||8.5|9.5|-||
|CMD, D inputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR mode|||||||
|t ISU|Input setup time HS|-|2.5|-|-|ns|
|t IH|Input hold time HS|-|0.5|-|-||
|t (3) IDW|Input valid window (variable window)|-|1.5|-|-||
|CMD, D outputs (referenced to CK) in eMMC legacy/SDR/DDR and SD HS/SDR/DDR mode|||||||
|t OV|Output valid time HS|-|-|5.5|6|ns|
|t OH|Output hold time HS|-|4.5|-|-||



DS13315 Rev 5 231/270


239

**Electrical characteristics** **STM32H730xB**

**Table 115. D** **y** **namics characteristics: SD / MMC characteristics, V** **DD** **= 2.7 to 3.6 V** **[(1)(2)]**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|CMD, D inputs (referenced to CK) in SD default mode|||||||
|t ISUD|Input setup time SD|-|1.5||-|ns|
|t IHD|Input hold time SD|-|0.5||-||
|CMD, D outputs (referenced to CK) in SD default mode|||||||
|t OVD|Output valid default time SD|-|-|1|1|ns|
|t OHD|Output hold default time SD|-|0|-|-||



1. Guaranteed by characterization results.

2. Above 100 MHz, C L = 20 pF.

3. The minimum window of time where the data needs to be stable for proper sampling in tuning mode.

**Table 116. D** **y** **namics characteristics: eMMC characteristics VDD = 1.71V to 1.9V** **[(1)(2)]**




|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|f PP|Clock frequency in data transfer mode|-|0|-|85|MHz|
|-|SDIO_CK/fPCLK2 frequency ratio|-|-|-|8/3|-|
|t W(CKL)|Clock low time|f =52 MHz PP|8.5|9.5|-|ns|
|t W(CKH)|Clock high time||8.5|9.5|-||
|CMD, D inputs (referenced to CK) in eMMC mode|||||||
|t ISU|Input setup time HS|-|1.5|-|-|ns|
|t IH|Input hold time HS|-|1.5|-|-||
|t (3) IDW|Input valid window (variable window)|-|3.5|-|-||
|CMD, D outputs (referenced to CK) in eMMC mode|||||||
|t OVD|Output valid time HS|-|-|6|6.5|ns|
|t OHD|Output hold time HS|-|5.5|-|-||


1. Guaranteed by characterization results.

2. C L = 20 pF.

3. The minimum window of time where the data needs to be stable for proper sampling in tuning mode.

232/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 63. SD hi** **g** **h-s** **p** **eed mode**





**Fi** **g** **ure 64. SD default mode**





**Fi** **g** **ure 65. SDMMC DDR mode**










**USB OTG_FS characteristics**

Unless otherwise specified, the parameters given in *Table 118* for ULPI are derived from
tests performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
summarized in *Table 12: General operating conditions*, with the following configuration:

- Output speed is set to OSPEEDRy[1:0] = 11

- Capacitive load C L =20 pF

- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.

- VOS level set to VOS0

DS13315 Rev 5 233/270


239

**Electrical characteristics** **STM32H730xB**

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output

characteristics.

**Table 117. USB OTG** **_** **FS electrical characteristics**






|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|V DD33US B|USB transceiver operating voltage|-|3.0(1)|-|3.6|V|
|R PUI|Embedded USB_DP pull-up value during idle|-|900|1250|1600|Ω|
|R PUR|Embedded USB_DP pull-up value during reception|-|1400|2300|3200||
|Z DRV|Output driver impedance(2)|Driver high and low|28|36|44||


1. The USB functionality is ensured down to 2.7 V. However, not all USB electrical characteristics are
degraded in the 2.7 to 3.0 V voltage range.

2. No external termination series resistors are required on USB_DP (D+) and USB_DM (D-); the matching
impedance is already included in the embedded driver.

**USB OTG_HS characteristics**

Unless otherwise specified, the parameters given in *Table 118* for ULPI are derived from
tests performed under the ambient temperature, f PCLKx frequency and V DD supply voltage
summarized in *Table 12: General operating conditions*, with the following configuration:

- Output speed is set to OSPEEDRy[1:0] = 11

- Capacitive load C L =20 pF

- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.

- VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output

characteristics.

**Table 118. D** **y** **namics characteristics: USB ULPI** **[(1)]**


|Symbol|Parameter|Condition|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|t SC|Control in (ULPI_DIR, ULPI_NXT) setup time|-|5.5|-|-|ns|
|t HC|Control in (ULPI_DIR, ULPI_NXT) hold time|-|0|-|-||
|t SD|Data in setup time|-|2.5|-|-||
|t HD|Data in hold time|-|0|-|-||
|t /t DC DD|Control/Datal output delay|2.7 V < V < 3.6 V, DD C = 20 pF L|-|6.0|8.0||
|||1.71 V < V < 3.6 V DD, C = 15 pF L|-|6.0|12||


1. Guaranteed by characterization results.

234/270 DS13315 Rev 5


**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 66. ULPI timin** **g** **dia** **g** **ram**







**Ethernet interface characteristics**

Unless otherwise specified, the parameters given in *Table 119*, *Table 120* and *Table 121* for
SMI, RMII and MII are derived from tests performed under the ambient temperature,
f rcc_c_ck frequency and V DD supply voltage conditions summarized in *Table 12: General*
*operating conditions*, with the following configuration:

- Output speed is set to OSPEEDRy[1:0] = 10

- Capacitive load C L =20 pF

- Measurement points are done at CMOS levels: 0.5V DD

- IO Compensation cell activated.

- HSLV activated when VDD ≤ 2.7 V

- VOS level set to VOS1

Due to timing constraint Pxy_C I/Os cannot be used as ethernet signals.

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output

characteristics:

**Table 119. D** **y** **namics characteristics: Ethernet MAC si** **g** **nals for SMI** **[(1)]**

|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|t MDC|MDC cycle time( 2.5 MHz)|400|400|403|ns|
|T d(MDIO)|Write data valid time|0.5|1.5|4||
|t su(MDIO)|Read data setup time|12.5|-|-||
|t h(MDIO)|Read data hold time|0|-|-||



1. Guaranteed by characterization results.

DS13315 Rev 5 235/270


239

**Electrical characteristics** **STM32H730xB**

**Fi** **g** **ure 67. Ethernet SMI timin** **g** **dia** **g** **ram**

**Table 120. D** **y** **namics characteristics: Ethernet MAC si** **g** **nals for RMII** **[(1)]**


|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|t su(RXD)|Receive data setup time|2|-|-|ns|
|t ih(RXD)|Receive data hold time|2|-|-||
|t su(CRS)|Carrier sense setup time|1.5|-|-||
|t ih(CRS)|Carrier sense hold time|1.5|-|-||
|t d(TXEN)|Transmit enable valid delay time|8|9|10.5||
|t d(TXD)|Transmit data valid delay time|7|8|9.5||


1. Guaranteed by characterization results.

**Fi** **g** **ure 68. Ethernet RMII timin** **g** **dia** **g** **ram**





236/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Table 121. D** **y** **namics characteristics: Ethernet MAC si** **g** **nals for MII** **[(1)]**


|Symbol|Parameter|Min|Typ|Max|Unit|
|---|---|---|---|---|---|
|t su(RXD)|Receive data setup time|2.0|-|-|ns|
|t ih(RXD)|Receive data hold time|2.0|-|-||
|t su(DV)|Data valid setup time|1.5|-|-||
|t ih(DV)|Data valid hold time|1.5|-|-||
|t su(ER)|Error setup time|1.5|-|-||
|t ih(ER)|Error hold time|0.5|-|-||
|t d(TXEN)|Transmit enable valid delay time|9.0|11|19||
|t d(TXD)|Transmit data valid delay time|8.5|10|19||


1. Guaranteed by characterization results.

**Fi** **g** **ure 69. Ethernet MII timin** **g** **dia** **g** **ram**








**JTAG/SWD interface characteristics**

Unless otherwise specified, the parameters given in *Table 122* and *Table 123* for
JTAG/SWD are derived from tests performed under the ambient temperature, f rcc_c_ck
frequency and V DD supply voltage summarized in *Table 12: General operating conditions*,
with the following configuration:

- Output speed is set to OSPEEDRy[1:0] = 11

- Capacitive load C L =30 pF

- Measurement points are done at CMOS levels: 0.5V DD

- VOS level set to VOS0

Refer to *Section 6.3.17: I/O port characteristics* for more details on the input/output

characteristics:

DS13315 Rev 5 237/270


239

**Electrical characteristics** **STM32H730xB**

**Table 122. D** **y** **namics JTAG characteristics**

|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F pp|T clock frequency CK|2.7V <V < 3.6 V DD|-|-|37|MHz|
|1/t c(TCK)||1.62 <V < 3.6 V DD|-|-|27.5||
|ti su(TMS)|TMS input setup time|-|2.5|-|-||
|ti h(TMS)|TMS input hold time|-|1|-|-||
|ti su(TDI)|TDI input setup time|-|1.5|-|-|-|
|ti h(TDI)|TDI input hold time|-|1|-|-|-|
|t ov(TDO)|TDO output valid time|2.7V <V < 3.6 V DD|-|8|13.5|-|
|||1.62 <V < 3.6 V DD|-|8|18|-|
|t oh(TDO)|TDO output hold time|-|7|-|-|-|



**Table 123. D** **y** **namics SWD characteristics**




|Symbol|Parameter|Conditions|Min|Typ|Max|Unit|
|---|---|---|---|---|---|---|
|F pp|SWCLK clock frequency|2.7V <V < 3.6 V DD|-|-|71|MHz|
|1/t c(SWCLK)||1.62 <V < 3.6 V DD|-|-|52.5||
|ti su(SWDIO)|SWDIO input setup time|-|2.5|-|-|-|
|ti h(SWDIO)|SWDIO input hold time|-|1|-|-|-|
|t ov(SWDIO)|SWDIO output valid time|2.7V <V < 3.6 V DD|-|8.5|14|-|
|||1.62 <V < 3.6 V DD|-|8.5|19|-|
|t oh(SWDIO)|SWDIO output hold time|-|8|-|-|-|


**Fi** **g** **ure 70. JTAG timin** **g** **dia** **g** **ram**








238/270 DS13315 Rev 5

**STM32H730xB** **Electrical characteristics**

**Fi** **g** **ure 71. SWD timin** **g** **dia** **g** **ram**



|Col1|Col2|
|---|---|
||th(SWDIO)|
|||

|t|Col2|
|---|---|
|||



DS13315 Rev 5 239/270


239

**STM32H730xB** **Package information**
#### **7 Package information**

In order to meet environmental requirements, ST offers these devices in different grades of
ECOPACK packages, depending on their level of environmental compliance. ECOPACK
specifications, grade definitions and product status *are available at www.st.com.* ECOPACK
is an ST trademark.
###### **7.1 Device marking**

Refer to technical note “Reference device marking schematics for STM32 microcontrollers
and microprocessors” (TN1433) available on *[www.st.com](http://www.st.com)*, for the location of pin 1 / ball A1
as well as the location and orientation of the marking areas versus pin 1 / ball A1.

Parts marked as “ES”, “E” or accompanied by an engineering sample notification letter, are
not yet qualified and therefore not approved for use in production. ST is not responsible for
any consequences resulting from such use. In no event will ST be liable for the customer
using any of these engineering samples in production. ST’s Quality department must be
contacted prior to any decision to use these engineering samples to run a qualification
activity.

A WLCSP simplified marking example (if any) is provided in the corresponding package
information subsection.

DS13315 Rev 5 239/270


263

**Package information** **STM32H730xB**
###### **7.2 LQFP100 package information (1L)**

This LQFP is 100 lead, 14 x 14 mm low-profile quad flat package.

*Note:* *See list of notes in the notes section.*

**Fi** **g** **ure 72. LQFP100 - Outline** **[(15)]**




































|Col1|D (3)|
|---|---|
|||
|E1/4 D1/4 (6)||
|||


240/270 DS13315 Rev 5

**STM32H730xB** **Package information**

**Table 124. LQFP100 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min|Typ|Max|Min|Typ|Max|
|A|-|1.50|1.60|-|0.0590|0.0630|
|A1(12)|0.05|-|0.15|0.0019|-|0.0059|
|A2|1.35|1.40|1.45|0.0531|0.0551|0.0570|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0090|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|16.00 BSC|||0.6299 BSC|||
|D1(2)(5)|14.00 BSC|||0.5512 BSC|||
|E(4)|16.00 BSC|||0.6299 BSC|||
|E1(2)(5)|14.00 BSC|||0.5512 BSC|||
|e|0.50 BSC|||0.0197 BSC|||
|L|0.45|0.60|0.75|0.177|0.0236|0.0295|
|L1(1)(11)|1.00|||-|0.0394|-|
|N(13)|100||||||
||0°|3.5°|7°|0°|3.5°|7°|
||0°|-|-|0°|-|-|
||10°|12°|14°|10°|12°|14°|
||10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa(1)|0.20|||0.0079|||
|bbb(1)|0.20|||0.0079|||
|ccc(1)|0.08|||0.0031|||
|ddd(1)|0.08|||0.0031|||



DS13315 Rev 5 241/270


263

**Package information** **STM32H730xB**

**Notes:**

1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The Top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is “0.25 mm” per side. D1 and E1 are Maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All Dimensions are in millimeters.

8. No intrusion allowed inwards the leads.

9. Dimension “b” does not include dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum “b” dimension by more than 0.08 mm.
Dambar cannot be located on the lower radius or the foot. Minimum space between
protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch packages.

10. Exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead between 0.10 mm and 0.25 mm
from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. “N” is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to 4 decimal digits.

15. Drawing is not to scale.

**Fi** **g** **ure 73. LQFP100 - Foot** **p** **rint exam** **p** **le**






1. Dimensions are expressed in millimeters.

242/270 DS13315 Rev 5




**STM32H730xB** **Package information**
###### **7.3 TFBGA100 package information (A08Q)**

This TFBGA is 100 - ball, 8X8 mm, 0.8 mm pitch fine pitch ball grid array package.

*Note:* *See list of notes in the notes section.*



|ØeeeM|C|A|B|
|---|---|---|---|
|Øfff M|C|||


















|Col1|(DATUM A)|D|Col4|Col5|
|---|---|---|---|---|
||(DATUM B)||||
||||aaa|C|


|Col1|Figure 74. TFBGA100 - Outline(13)|
|---|---|
|||
||E1 e SE K J H e G SD F E D1 D C B A A1 ball pad corner 1 2 3 4 5 6 7 8 9 10 Øb (N balls) ØeeeM C A B BOTTOM VIEW Øfff M C ddd C ccc C Seating 7 plane A A1 A2 C SIDE VIEW B E A A1 ball pad 8 corner (DATUM A) D (DATUM B) (4x) aaa C TOP VIEW A08Q_UFBGA100_ME_V2|


DS13315 Rev 5 243/270


263

**Package information** **STM32H730xB**

**Table 125. TFBGA100 - Mechanical data**

|Symbol|millimeters(1)|Col3|Col4|inches(12)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min|Typ|Max|Min|Typ|Max|
|A(2)(3)|-|-|1.20|-|-|0.0472|
|A1(4)|0.15|-|-|0.0059|-|-|
|A2|-|0.74|-|-|0.0291|-|
|b(5)|0.35|0.40|0.45|0.0138|0.0157|0.0177|
|D|8.00 BSC(6)|||0.3150 BSC|||
|D1|7.20 BSC|||0.2835 BSC|||
|E|8.00 BSC|||0.3150 BSC|||
|E1|7.20 BSC|||0.2835 BSC|||
|e(9)|0.80 BSC|||0.0315 BSC|||
|N(11)|100||||||
|SD(12)|0.40 BSC|||0.0157 BSC|||
|SE(12)|0.40 BSC|||0.0157 BSC|||
|aaa|0.15|||0.0059|||
|ccc|0.20|||0.0079|||
|ddd|0.10|||0.0039|||
|eee|0.15|||0.0059|||
|fff|0.08|||0.0031|||



**Notes:**

1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-2018.

2. TFBGA stands for thin profile fine pitch ball grid array: 1.00 mm < A ≤ 1.20 mm / fine
pitch e < 1.00 mm.

3. The profile height, A, is the distance from the seating plane to the highest point on the
package. It is measured perpendicular to the seating plane.

4. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

5. Dimension b is measured at the maximum diameter of the terminal (ball) in a plane
parallel to primary datum C.

6. BSC stands for BASIC dimensions. It corresponds to the nominal value and has no
tolerance. For tolerances refer to form and position table. On the drawing these
dimensions are framed.

7. Primary datum C is defined by the plane established by the contact points of three or
more solder balls that support the device when it is placed on top of a planar surface.

8. The terminal (ball) A1 corner must be identified on the top surface of the package by
using a corner chamfer, ink or metalized markings, or other feature of package body or

244/270 DS13315 Rev 5

**STM32H730xB** **Package information**

integral heat slug. A distinguish feature is allowable on the bottom surface of the
package to identify the terminal A1 corner. Exact shape of each corner is optional.

9. e represents the solder ball grid pitch.

10. N represents the total number of balls on the BGA.

11. Basic dimensions SD and SE are defined with respect to datums A and B. It defines the
position of the centre ball(s) in the outer row or column of a fully populated matrix.

12. Values in inches are converted from mm and rounded to 4 decimal digits.

13. Drawing is not to scale.

**Fi** **g** **ure 75. TFBGA100 - Foot** **p** **rint exam** **p** **le**

**Table 126. TFBGA100 - Exam** **p** **le of PCB desi** **g** **n rules** **(** **0.8 mm** **p** **itch BGA** **)**

|Dimension|Values|
|---|---|
|Pitch|0.8|
|Dpad|0.400 mm|
|Dsm|0.470 mm typ. (depends on the soldermask registration tolerance)|
|Stencil opening|0.400 mm|
|Stencil thickness|Between 0.100 mm and 0.125 mm|
|Pad trace width|0.120 mm|



DS13315 Rev 5 245/270


263

**Package information** **STM32H730xB**
###### **7.4 LQFP144 package information (1A)**

This LQFP is a 144-pin, 20 x 20 mm low-profile quad flat package.

*Note:* *See list of notes in the notes section.*

**Fi** **g** **ure 76. LQFP144 - Outline** **[(15)]**













|Col1|aaa|C|A-B|D|
|---|---|---|---|---|
||||||

|Col1|bb|bH A-B D|
|---|---|---|
||||

|A|Col2|Col3|Col4|
|---|---|---|---|
|||||




















|Col1|Col2|
|---|---|
|||
|||
|A (Section A-A)||


246/270 DS13315 Rev 5



**STM32H730xB** **Package information**

**Table 127. LQFP144 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min|Typ|Max|Min|Typ|Max|
|A|-|-|1.60|-|-|0.0630|
|A1(12)|0.05|-|0.15|0.0020|-|0.0059|
|A2|1.35|1.40|1.45|0.0531|0.0551|0.0571|
|b(9)(11)|0.17|0.22|0.27|0.0067|0.0087|0.0106|
|b1(11)|0.17|0.20|0.23|0.0067|0.0079|0.0090|
|c(11)|0.09|-|0.20|0.0035|-|0.0079|
|c1(11)|0.09|-|0.16|0.0035|-|0.0063|
|D(4)|22.00 BSC|||0.8661 BSC|||
|D1(2)(5)|20.00 BSC|||0.7874 BSC|||
|E(4)|22.00 BSC|||0.8661 BSC|||
|E1(2)(5)|20.00 BSC|||0.7874 BSC|||
|e|0.50 BSC|||0.0197 BSC|||
|L|0.45|0.60|0.75|0.0177|0.0236|0.0295|
|L1|1.00 REF|||0.0394 REF|||
|N(13)|144||||||
||0°|3.5°|7°|0°|3.5°|7°|
||0°|-|-|0°|-|-|
||10°|12°|14°|10°|12°|14°|
||10°|12°|14°|10°|12°|14°|
|R1|0.08|-|-|0.0031|-|-|
|R2|0.08|-|0.20|0.0031|-|0.0079|
|S|0.20|-|-|0.0079|-|-|
|aaa|0.20|||0.0079|||
|bbb|0.20|||0.0079|||
|ccc|0.08|||0.0031|||
|ddd|0.08|||0.0031|||



DS13315 Rev 5 247/270


263

**Package information** **STM32H730xB**

**Notes:**

1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The Top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is “0.25 mm” per side. D1 and E1 are Maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All Dimensions are in millimeters.

8. No intrusion allowed inwards the leads.

9. Dimension “b” does not include dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum “b” dimension by more than 0.08 mm.
Dambar cannot be located on the lower radius or the foot. Minimum space between
protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch packages.

10. Exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead between 0.10 mm and 0.25 mm
from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. “N” is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to 4 decimal digits.

15. Drawing is not to scale.

248/270 DS13315 Rev 5

**STM32H730xB** **Package information**

**Fi** **g** **ure 77. LQFP144 - Foot** **p** **rint exam** **p** **le**






|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||



1. Dimensions are expressed in millimeters.



DS13315 Rev 5 249/270


263

**Package information** **STM32H730xB**
###### **7.5 UFBGA144 package information (A0AS)**

**Figure 78. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array**
**p** **acka** **g** **e outline**












|Col1|Col2|Col3|
|---|---|---|
||||



|Col1|ØeeeM|Z|Y|X|
|---|---|---|---|---|
||Øfff M|Z|||


1. Drawing is not to scale.

**Table 128. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array**
**p** **acka** **g** **e mechanical data**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min.|Typ.|Max.|Min.|Typ.|Max.|
|A|0.460|0.530|0.600|0.0181|0.0209|0.0236|
|A1|0.050|0.080|0.110|0.0020|0.0031|0.0043|
|A2|0.400|0.450|0.500|0.0157|0.0177|0.0197|
|A3|-|0.130|-|-|0.0051|-|
|A4|0.270|0.320|0.370|0.0106|0.0126|0.0146|
|b|0.230|0.280|0.320|0.0091|0.0110|0.0126|
|D|6.950|7.000|7.050|0.2736|0.2756|0.2776|
|D1|5.450|5.500|5.550|0.2146|0.2165|0.2185|
|E|6.950|7.000|7.050|0.2736|0.2756|0.2776|
|E1|5.450|5.500|5.550|0.2146|0.2165|0.2185|
|e|-|0.500|-|-|0.0197|-|
|F|0.700|0.750|0.800|0.0276|0.0295|0.0315|



250/270 DS13315 Rev 5

**STM32H730xB** **Package information**

**Table 128. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array**
**p** **acka** **g** **e mechanical data** **(** **continued** **)**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min.|Typ.|Max.|Min.|Typ.|Max.|
|ddd|-|-|0.100|-|-|0.0039|
|eee|-|-|0.150|-|-|0.0059|
|fff|-|-|0.050|-|-|0.0020|



1. Values in inches are converted from mm and rounded to 4 decimal digits.

**Figure 79. UFBGA - 144 balls, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array**
**p** **acka** **g** **e recommended foot** **p** **rint**

**Table 129. UFBGA144 recommended PCB desi** **g** **n rules** **(** **0.50 mm** **p** **itch BGA** **)**

|Dimension|Recommended values|
|---|---|
|Pitch|0.50 mm|
|Dpad|0.280 mm|
|Dsm|0.370 mm typ. (depends on the soldermask registration tolerance)|
|Stencil opening|0.280 mm|
|Stencil thickness|Between 0.100 mm and 0.125 mm|
|Pad trace width|0.120 mm|



DS13315 Rev 5 251/270


263

**Package information** **STM32H730xB**
###### **7.6 UFBGA169 package information (A0YV)**

This UFBGA is a 169-ball, 7 x 7 mm, 0.50 mm pitch, ultra fine pitch ball grid array package.

**Fi** **g** **ure 80. UFBGA169 - Outline**






|Col1|E1|Col3|Col4|Col5|
|---|---|---|---|---|
||SE||||
||||||
|||||e|
||||||
||||||







|Col1|ØeeeM|C|A B|
|---|---|---|---|
||Øfff M|C||











|Col1|(DATUM A)|
|---|---|
||(DATUM B)|




1. Drawing is not to scale.

2. Primary datum C is defined by the plane established by the contact points of three or more solder balls that
support the device when it is placed on top of a planar surface.

3. The terminal (ball) A1 corner must be identified on the top surface of the package by using a corner
chamfer, ink or metallized markings, or other feature of package body or integral heat slug. A distinguish
feature is allowable on the bottom surface of the package to identify the terminal A1 corner. Exact shape of
each corner is optional.

252/270 DS13315 Rev 5

**STM32H730xB** **Package information**

**Table 130. UFBGA169 - Mechanical data**













|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min.|Typ.|Max.|Min.|Typ.|Max.|
|A(2)|-|-|0.60|-|-|0.0236|
|A1(3)|0.05|-|-|0.0020|-|-|
|A2|-|0.43|-|-|0.0169|-|
|b(4)|0.23|0.28|0.33|0.0091|0.0110|0.0130|
|D(5)|7.00 BSC|||0.2756 BSC|||
|D1(5)|6.00 BSC|||0.2362 BSC|||
|E(5)|7.00 BSC|||0.2756 BSC|||
|E1(5)|6.00 BSC|||0.2362 BSC|||
|e(5)(6)|0.50 BSC|||0.0197 BSC|||
|N(7)|169||||||
|SD(5)(8)|0.50 BSC|||0.0197 BSC|||
|SE(5)(8)|0.50 BSC|||0.0197 BSC|||
|aaa(9)|0.15|||0.0059|||
|ccc(9)|0.20|||0.0079|||
|ddd(9)|0.08|||0.0031|||
|eee(9)|0.15|||0.0059|||
|fff(9)|0.05|||0.0020|||


1. Values in inches are converted from mm and rounded to 4 decimal digits.

2. The profile height, A, is the distance from the seating plane to the highest point on the package. It is
measured perpendicular to the seating plane.

3. A1 is defined as the distance from the seating plane to the lowest point on the package body.

4. Dimension b is measured at the maximum diameter of the terminal (ball) in a plane parallel to primary
datum C.

5. BSC stands for BASIC dimensions. It corresponds to the nominal value and has no tolerance. For
tolerances refer to form and position table.

6. e represents the solder ball grid pitch.

7. N represents the total number of balls on the BGA.

8. Basic dimensions SD and SE are defined with respect to datums A and B. It defines the position of the
centre ball(s) in the outer row or column of a fully populated matrix.

9. Tolerance of form and position drawing

DS13315 Rev 5 253/270


263

**Package information** **STM32H730xB**

**Fi** **g** **ure 81. UFBGA169 - Foot** **p** **rint exam** **p** **le**

**Table 131. UFBGA169 - Exam** **p** **le of PCB desi** **g** **n rules** **(** **0.5 mm** **p** **itch BGA** **)**

|Dimension|Values|
|---|---|
|Pitch|0.5 mm|
|Dpad|0.27 mm|
|Dsm|0.35 mm typ. (depends on the soldermask registration tolerance)|
|Solder paste|0.27 mm aperture diameter.|



*Note:* *Non-solder mask defined (NSMD) pads are recommended.*

*Note:* *4 to 6 mils solder paste screen printing process.*

254/270 DS13315 Rev 5

**STM32H730xB** **Package information**
###### **7.7 LQFP176 package information (1T)**

This LQFP is a 176-pin, 24 x 24 mm, 0.5 mm pitch, low profile quad flat package.

*Note:* *See list of notes in the notes section.*

**Fi** **g** **ure 82. LQFP176 - Outline** **[(15)]**






































DS13315 Rev 5 255/270


263

**Package information** **STM32H730xB**

**Table 132. LQFP176 - Mechanical data**

|Symbol|millimeters|Col3|Col4|inches(14)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min|Typ|Max|Min|Typ|Max|
|A|-|-|1.600|-|-|0.0630|
|A1(12)|0.050|-|0.150|0.0020|-|0.0059|
|A2|1.350|1.400|1.450|0.0531|0.0551|0.0571|
|b(9)(11)|0.170|0.220|0.270|0.0067|0.0087|0.0106|
|b1(11)|0.170|0.200|0.230|0.0067|0.0079|0.0091|
|c(11)|0.090|-|0.200|0.0035|-|0.0079|
|c1(11)|0.090|-|0.160|0.0035|-|0.063|
|D(4)|26.000|||1.0236|||
|D1(2)(5)|24.000|||0.9449|||
|E(4)|26.000|||0.0197|||
|E1(2)(5)|24.000|||0.9449|||
|e|0.500|||0.1970|||
|L|0.450|0.600|0.750|0.0177|0.0236|0.0295|
|L1(1)(11)|1|||0.0394 REF|||
|N(13)|176||||||
||0°|3.5°|7°|0°|3.5°|7°|
||0°|-|-|0°|-|-|
||10°|12°|14°|10°|12°|14°|
||10°|12°|14°|10°|12°|14°|
|R1|0.080|-|-|0.0031|-|-|
|R2|0.080|-|0.200|0.0031|-|0.0079|
|S|0.200|-|-|0.0079|-|-|
|aaa(1)|0.200|||0.0079|||
|bbb(1)|0.200|||0.0079|||
|ccc(1)|0.080|||0.0031|||
|ddd(1)|0.080|||0.0031|||



256/270 DS13315 Rev 5

**STM32H730xB** **Package information**

**Notes:**

1. Dimensioning and tolerancing schemes conform to ASME Y14.5M-1994.

2. The Top package body size may be smaller than the bottom package size by as much
as 0.15 mm.

3. Datums A-B and D to be determined at datum plane H.

4. To be determined at seating datum plane C.

5. Dimensions D1 and E1 do not include mold flash or protrusions. Allowable mold flash
or protrusions is “0.25 mm” per side. D1 and E1 are Maximum plastic body size
dimensions including mold mismatch.

6. Details of pin 1 identifier are optional but must be located within the zone indicated.

7. All Dimensions are in millimeters.

8. No intrusion allowed inwards the leads.

9. Dimension “b” does not include dambar protrusion. Allowable dambar protrusion shall
not cause the lead width to exceed the maximum “b” dimension by more than 0.08 mm.
Dambar cannot be located on the lower radius or the foot. Minimum space between
protrusion and an adjacent lead is 0.07 mm for 0.4 mm and 0.5 mm pitch packages.

10. Exact shape of each corner is optional.

11. These dimensions apply to the flat section of the lead between 0.10 mm and 0.25 mm
from the lead tip.

12. A1 is defined as the distance from the seating plane to the lowest point on the package
body.

13. “N” is the number of terminal positions for the specified body size.

14. Values in inches are converted from mm and rounded to 4 decimal digits.

15. Drawing is not to scale.

DS13315 Rev 5 257/270


263

**Package information** **STM32H730xB**

**Fi** **g** **ure 83. LQFP176 - Foot** **p** **rint exam** **p** **le**


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|Col39|Col40|Col41|Col42|Col43|Col44|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||176 1||||||||||||||||||||||133 0.5 132 0.3|||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
||44 45||||||||||||||||||||||89 88|||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||


1. Dimensions are expressed in millimeters.

258/270 DS13315 Rev 5




**STM32H730xB** **Package information**
###### **7.8 UFBGA(176+25) package information (A0E7)**

This UFBGA is a 176+25-ball, 10 x 10 mm, 0.65 mm pitch, ultra fine pitch ball grid array
package.

**Fi** **g** **ure 84. UFBGA** **(** **176+25** **)** **- Outline**




|Col1|Col2|Col3|Col4|Col5|Col6|Col7|ddd|C|
|---|---|---|---|---|---|---|---|---|
||||||||||











|Col1|Col2|Col3|
|---|---|---|
||||







|Col1|ØeeeM|C|A|B|
|---|---|---|---|---|
||Øfff M|C|||



1. Drawing is not to scale.

|Col1|Table 133. UFBGA(176+25) -|Col3|Col4|Mechanical data|Col6|Col7|
|---|---|---|---|---|---|---|
|Symbol|millimeters|||inches(1)|||
||Min.|Typ.|Max.|Min.|Typ.|Max.|
|A|-|-|0.600|-|-|0.0236|
|A1|0.050|0.080|0.110|0.0020|0.0031|0.0043|
|A2|-|0.450|-|-|0.0177|-|
|A3|-|0.130|-|-|0.0051|-|
|A4|-|0.320|-|-|0.0126|-|
|b|0.240|0.290|0.340|0.0094|0.0114|0.0134|
|D|9.850|10.000|10.150|0.3878|0.3937|0.3996|
|D1|-|9.100|-|-|0.3583|-|
|E|9.850|10.000|10.150|0.3878|0.3937|0.3996|
|E1|-|9.100|-|-|0.3583|-|
|e|-|0.650|-|-|0.0256|-|
|F|-|0.450|-|-|0.0177|-|
|ddd|-|-|0.080|-|-|0.0031|



DS13315 Rev 5 259/270


263

**Package information** **STM32H730xB**

**Table 133. UFBGA** **(** **176+25** **)** **- Mechanical data** **(** **continued** **)**

|Symbol|millimeters|Col3|Col4|inches(1)|Col6|Col7|
|---|---|---|---|---|---|---|
||Min.|Typ.|Max.|Min.|Typ.|Max.|
|eee|-|-|0.150|-|-|0.0059|
|fff|-|-|0.050|-|-|0.0020|



1. Values in inches are converted from mm and rounded to 4 decimal digits.

**Fi** **g** **ure 85. UFBGA** **(** **176+25** **)** **- Foot** **p** **rint exam** **p** **le**

|Table 134. UFBGA(176+25) - Example of|PCB design rules (0.65 mm pitch BGA)|
|---|---|
|Dimension|Values|
|Pitch|0.65 mm|
|Dpad|0.300 mm|
|Dsm|0.400 mm typ. (depends on the soldermask registration tolerance)|
|Stencil opening|0.300 mm|
|Stencil thickness|Between 0.100 mm and 0.125 mm|
|Pad trace width|0.100 mm|



260/270 DS13315 Rev 5

**STM32H730xB** **Package information**
###### **7.9 Thermal characteristics**

The maximum chip-junction temperature, T Jmax, in degrees Celsius, may be calculated
using the following equation:

T Jmax = T A max + (P D max × Θ JA )

Where:

      - T A max is the maximum ambient temperature in ° C,

      - Θ JA is the package junction-to-ambient thermal resistance, in ° C/W,

      - P D max is the sum of P INT max and P I/O max (P D max = P INT max + P I/O max),

      - P INT max is the product of I DD and V DD, expressed in Watts. This is the maximum chip
internal power.

P I/O max represents the maximum power dissipation on output pins where:

P I/O max = Σ (V OL × I OL ) + Σ ((V DD – V OH ) × I OH ),

taking into account the actual V OL / I OL and V OH / I OH of the I/Os at low and high level in the
application.

**Table 135. Thermal characteristics**




|Symbol|Definition|Parameter|Value|Unit|
|---|---|---|---|---|
|JA Θ|Thermal resistance junction-ambient|Thermal resistance junction-ambient LQFP100 - 14 x 14 mm /0.5 mm pitch|43.8|°C/W|
|||Thermal resistance junction-ambient TFBGA100 - 8 x 8 mm /0.8 mm pitch|43.2||
|||Thermal resistance junction-ambient LQFP144 - 20 x 20 mm /0.5 mm pitch|44.8||
|||Thermal resistance junction-ambient UFBGA144 - 7 x 7 mm /0.5 mm pitch|36||
|||Thermal resistance junction-ambient UFBGA169 - 7 x 7 mm / 0.5 mm pitch|38||
|||Thermal resistance junction-ambient LQFP176 - 24 x 24 mm / 0.5 mm pitch|48.3||
|||Thermal resistance junction-ambient UFBGA176+25 - 10 x 10 mm / 0.65 mm pitch|38||


DS13315 Rev 5 261/270


263

**Package information** **STM32H730xB**

**Table 135. Thermal characteristics** **(** **continued** **)**


|Symbol|Definition|Parameter|Value|Unit|
|---|---|---|---|---|
|JB Θ|Thermal resistance junction-board|Thermal resistance junction-ambient LQFP100 - 14 x 14 mm /0.5 mm pitch|19.8|°C/W|
|||Thermal resistance junction-ambient TFBGA100 - 8 x 8 mm /0.8 mm pitch|24.8||
|||Thermal resistance junction-ambient LQFP144 - 20 x 20 mm /0.5 mm pitch|24.4||
|||Thermal resistance junction-ambient UFBGA144 - 7 x 7 mm /0.5 mm pitch|21.1||
|||Thermal resistance junction-ambient UFBGA169 - 7 x 7 mm / 0.5 mm pitch|18||
|||Thermal resistance junction-ambient LQFP176 - 24 x 24 mm / 0.5 mm pitch|29.1||
|||Thermal resistance junction-ambient UFBGA176+25 - 10 x 10 mm / 0.65 mm pitch|20||
|JC Θ|Thermal resistance junction-case|Thermal resistance junction-ambient LQFP100 - 14 x 14 mm /0.5 mm pitch|7.3|°C/W|
|||Thermal resistance junction-ambient TFBGA100 - 8 x 8 mm /0.8 mm pitch|13.2||
|||Thermal resistance junction-ambient LQFP144 - 20 x 20 mm /0.5 mm pitch|7.4||
|||Thermal resistance junction-ambient UFBGA144 - 7 x 7 mm /0.5 mm pitch|8.7||
|||Thermal resistance junction-ambient UFBGA169 - 7 x 7 mm / 0.5 mm pitch|11||
|||Thermal resistance junction-ambient LQFP176 - 24 x 24 mm / 0.5 mm pitch|7.9||
|||Thermal resistance junction-ambient UFBGA176+25 - 10 x 10 mm / 0.65 mm pitch|24||


**7.9.1** **Reference documents**





      - JESD51-2 Integrated Circuits Thermal Test Method Environment Conditions - Natural
Convection (Still Air). Available from www.jedec.org.

      - For information on thermal management, refer to application note “ *Guidelines for*
*thermal management on STM32 applications* ” (AN5036) available from *www.st.com* .

262/270 DS13315 Rev 5

**STM32H730xB** **Ordering information**
#### **8 Ordering information**

Example: STM32 H 730 V B T 6 Q TR

TR = tape and reel

No character = tray or tube

For a list of available options (speed, package, etc.) or for further information on any aspect
of this device, please contact your nearest ST sales office.

DS13315 Rev 5 263/270


263

**Important security notice** **STM32H730xB**
#### **9 Important security notice**

The STMicroelectronics group of companies (ST) places a high value on product security,
which is why the ST product(s) identified in this documentation may be certified by various
security certification bodies and/or may implement our own security measures as set forth
herein. However, no level of security certification and/or built-in security measures can
guarantee that ST products are resistant to all forms of attacks. As such, it is the
responsibility of each of ST's customers to determine if the level of security provided in an
ST product meets the customer needs both in relation to the ST product alone, as well as
when combined with other components and/or software for the customer end product or
application. In particular, take note that:

      - ST products may have been certified by one or more security certification bodies, such
as Platform Security Architecture (www.psacertified.org) and/or Security Evaluation
standard for IoT Platforms (www.trustcb.com). For details concerning whether the ST
product(s) referenced herein have received security certification along with the level
and current status of such certification, either visit the relevant certification standards
website or go to the relevant product page on www.st.com for the most up to date
information. As the status and/or level of security certification for an ST product can
change from time to time, customers should re-check security certification status/level
as needed. If an ST product is not shown to be certified under a particular security
standard, customers should not assume it is certified.

      - Certification bodies have the right to evaluate, grant and revoke security certification in
relation to ST products. These certification bodies are therefore independently
responsible for granting or revoking security certification for an ST product, and ST
does not take any responsibility for mistakes, evaluations, assessments, testing, or
other activity carried out by the certification body with respect to any ST product.

      - Industry-based cryptographic algorithms (such as AES, DES, or MD5) and other open
standard technologies which may be used in conjunction with an ST product are based
on standards which were not developed by ST. ST does not take responsibility for any
flaws in such cryptographic algorithms or open technologies or for any methods which
have been or may be developed to bypass, decrypt or crack such algorithms or
technologies.

      - While robust security testing may be done, no level of certification can absolutely
guarantee protections against all attacks, including, for example, against advanced
attacks which have not been tested for, against new or unidentified forms of attack, or
against any form of attack when using an ST product outside of its specification or
intended use, or in conjunction with other components or software which are used by
customer to create their end product or application. ST is not responsible for resistance
against such attacks. As such, regardless of the incorporated security features and/or
any information or support that may be provided by ST, each customer is solely
responsible for determining if the level of attacks tested for meets their needs, both in
relation to the ST product alone and when incorporated into a customer end product or
application.

      - All security features of ST products (inclusive of any hardware, software,
documentation, and the like), including but not limited to any enhanced security
features added by ST, are provided on an "AS IS" BASIS. AS SUCH, TO THE EXTENT
PERMITTED BY APPLICABLE LAW, ST DISCLAIMS ALL WARRANTIES, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, unless the
applicable written and signed contract terms specifically provide otherwise.

264/270 DS13315 Rev 5

**STM32H730xB** **Revision history**
#### **10 Revision history**

**Table 136. Document revision histor** **y**



|Date|Revision|Changes|
|---|---|---|
|10-Jul-2020|1|Initial release.|
|03-Sep-2020|2|Renamed Section 3.31 into True random number generator (RNG). Replaced V by V in Section 6: Electrical characteristics. DDIOx DD Updated I in Table 10: Current characteristics and Table 17: Inrush IO current and inrush electric charge characteristics for LDO and SMPS. Removed Table 13: Supply voltage and maximum temperature configuration. Updated Table 27: Typical current consumption in Autonomous mode, Table 30: Typical and maximum current consumption in Standby mode and Table 31: Typical and maximum current consumption in VBAT mode. Added Section 6.3.16: I/O current injection characteristics. Removed reference to PI8 in Table 55: Output voltage characteristics for all I/Os except PC13, PC14 and PC15 and Table 56: Output voltage characteristics for PC13, PC14 and PC15. Added Section : Analog switch between ports Pxy_C and Pxy. Added Figure 83: LQFP176 - Footprint example and Figure 81: UFBGA169 - Footprint example.|
|07-Dec-2021|3|Added indication that patents apply to the devices in Section : Features. Table 1: STM32H730xB features and peripheral counts: – Changed number of general-purpose 32-bit timers to 4. – For LQFP100 and TFBGA100 packages, replaced 2 Octo-SPI/Quad- SPI interfaces by 1 and remove note – Changed number of SPI/I2S from 4/4 to 6/4 for UFBGA169. In Section 3.8.1: Power supply scheme, changed V power supply DD requirements. Section 3.8.3: Voltage regulator: Scale0 is available even without LDO. Section 3.37: Universal synchronous/asynchronous receiver transmitter (USART): changed USART communication speed to 17 Mbit/s. Table 7: STM32H730xB pin and ball descriptions: – for PA15(JTDI), replaced SPI3_NSS/I2S3_WS alternate function by SPI3_NSS(boot)/I2S3_WS. – Added Note 1.and Note 2.to the package pin/balls corresponding to Pxy and Pxy_C. Added V in Table 12: General operating conditions. BAT Moved LSI clock from backup domain to VDD domain in Figure 13: Power supply scheme. Modified Section 6.3.3: SMPS step-down converter including Figure 16: External components for SMPS step-down converter. Updated Table 18: Operating conditions at power-up/power-down title and added t . VCORE|


DS13315 Rev 5 265/270


269

**Revision history** **STM32H730xB**

**Table 136. Document revision histor** **y**



|Date|Revision|Changes|
|---|---|---|
|07-Dec-2021|3 (continued)|Section : On-chip peripheral current consumption: updated measurement conditions and Table 32: Peripheral current consumption in Run mode. Updated Table 34: High-speed external user clock characteristics. Changed unit for PLL long-term jitter in Table 42: PLL1 characteristics (wide VCO frequency range). Renamed parameter into I in Table 54: I/O static characteristics. ILEAK lkg Table 58: Output timing characteristics (HSLV ON): updated load capacitance condition for t/t and for speed = 10. r f Updated Figure 39: OCTOSPI SDR read/write timing diagram, Figure 40: OCTOSPI DTR mode timing diagram, Figure 41: OCTOSPI Hyperbus clock timing diagram, Figure 42: OCTOSPI Hyperbus read timing diagram and Figure 43: OCTOSPI Hyperbus write timing diagram. Table 83: 16-bit ADC characteristics: updated sampling rate for slow channels. Updated Figure 44: ADC accuracy characteristics and Figure 45: Typical connection diagram when using the ADC with FT/TT pins featuring analog switch function as well as notes below figure. Updated Figure 46: Power supply and reference decoupling (V not REF+ connected to V ). DDA Updated T max value in Table 92: Temperature sensor characteristics. L Changed temperature condition to 130 °C for TS_CAL2 in Table 93: Temperature sensor calibration values. Updated Figure 53: USART timing diagram in SPI master mode and Figure 54: USART timing diagram in SPI slave mode. Updated Figure 63: SD high-speed mode, Figure 64: SD default mode and Figure 65: SDMMC DDR mode. Updated Figure 69: Ethernet MII timing diagram. Updated Figure 72: LQFP100 - Outline(15), Table 132: LQFP176 - Mechanical data, Figure 75: TFBGA100 - Footprint example, Figure 82: LQFP176 - Outline(15) and Table 132: LQFP176 - Mechanical data.|


266/270 DS13315 Rev 5

**STM32H730xB** **Revision history**

**Table 136. Document revision histor** **y**



|Date|Revision|Changes|
|---|---|---|
|17-Nov-2023|4|Updated document title. Updated Figure 1: STM32H730xB block diagram. In Table 1: STM32H730xB features and peripheral counts: changed the number of available Ethernet MII and SAI PDM interfaces. Updated description of USB regulator bypass in Section 3.8.1: Power supply scheme. Updated Section 3.39: Serial peripheral interface (SPI)/inter- integrated sound interfaces (I2S). Updated Section 3.40: Serial audio interfaces (SAI). Updated Table 7: STM32H730xB pin and ball descriptions (removed ADC3_INP16 additional function from PH5 pin). Added note to Chapter 6.2. Updated I definition in Table 10: Current characteristics. IO Updated V in Table 12: General operating conditions to cover the case IN of Pxy_C. In Table 13: Supply voltage and maximum temperature configuration, updated V minimum value for VOS0 power source and external DDLDO bypass. Updated Figure 80: UFBGA169 - Outline and Table 130: UFBGA169 - Mechanical data.|


DS13315 Rev 5 267/270


269

**Revision history** **STM32H730xB**

**Table 136. Document revision histor** **y**



|Date|Revision|Changes|
|---|---|---|
|17-Nov-2023|4 (continued)|In Table 19: Reset and power control block characteristics: – renamed power-on/power-down reset threshold V into POR/PDR V . BOR0/POR/PDR – updated description of V . hyst_POR_PDR – renamed Hysteresis voltage for Power-on/power-down reset (including BOR0) into V . hyst_POR_PDR Updated measurement conditions for Typical and maximum current consumption parameters. Updated Section : High-speed external clock generated from a crystal/ceramic resonator. Updated Table 50: EMI characteristics for fHSE = 8 MHz and fCPU = 550 MHz. Updated Section : I/O static current consumption and Section : I/O dynamic current consumption. Updated V and V in Table 54: I/O static characteristics and Table 55: IH OH Output voltage characteristics for all I/Os except PC13, PC14 and PC15, respectively, to cover the case of Pxy_C I/Os. Updated note 2 in Table 57: Output timing characteristics (HSLV OFF) and Table 58: Output timing characteristics (HSLV ON). Reorganized Section 6.3.19: FMC characteristics and updated Figure 35: NAND controller waveforms for read access and Figure 36: NAND controller waveforms for write access. Updated t in Table 85: 16-bit ADC accuracy. TRIG Changed V maximum value (buffer ON) in Table 89: DAC DAC_OUT characteristics. Updated f maximum value in Table 101: DFSDM measured DFSDMCLK timing. In Table 110: USART (SPI mode) characteristics, changed t and w(SCKH) t into t and t, respectively. w(SCKL) w(CKH) w(CKL) Updated Figure 55: SPI timing diagram - slave mode and CPHA = 0, Figure 56: SPI timing diagram - slave mode and CPHA = 1 and Figure 57: SPI timing diagram - master mode. Updated Figure 60: SAI master timing waveforms and Figure 61: SAI slave timing waveforms. Section : Ethernet interface characteristics: – added constraints on Pxy_C I/Os. – updated typical t value in Table 121: Dynamics characteristics: d(TXEN) Ethernet MAC signals for MII. Added Section 7.1: Device marking, and removed device marking sections for all packages. Updated Table 135: Thermal characteristics with,, and values JA JB JC for the UFBGA144 package. Θ Θ Θ Changed SPIx_SS to SPIx_NSS in: – Figure 1: STM32H730xB block diagram. – Section 3.39: Serial peripheral interface (SPI)/inter- integrated sound interfaces (I2S). – Table 7: STM32H730xB pin and ball descriptions. – Table 8: STM32H730xB pin alternate functions. – Section : SPI interface characteristics.|


268/270 DS13315 Rev 5

**STM32H730xB** **Revision history**

**Table 136. Document revision histor** **y**



|Date|Revision|Changes|
|---|---|---|
|22-May-2025|5|In the context of I2C, replaced master and slave by controller and target, respectively. Features – Replaced Dhrystone/DMIPS by Coremark score on cover page. – Updated USART/UART/LPUART feature, modified the number of SPIs Added reference to errata sheet ES0491 in Section 1: Introduction. Updated Figure 2: Power-up/power-down sequence and moved figure to Section 3.8.2: Power supply supervisor. Updated note 1 in Table 4: Timer feature comparison. Updated Figure 6: UFBGA144 ballout (without SMPS). Section 6: Electrical characteristics: – Updated maximum input voltage on FT_xxx pins and added note 5.in Table 9: Voltage characteristics. – Changed CoreMark values to 2778 in Table 26: Typical consumption in Run mode and corresponding performance versus code position. – Updated Figure 24: Typical application with a 32.768 kHz crystal. – Replaced f by f in Section 6.3.22: 16-bit ADC characteristics. PCLK2 HCLK – Updated gain error (EG) in Table 88: 12-bit ADC accuracy. – Updated Table 110: USART (SPI mode) characteristics conditions, as well as Figure 54: USART timing diagram in SPI slave mode and Figure 53: USART timing diagram in SPI master mode. – Updated Figure 55: SPI timing diagram - slave mode and CPHA = 0 and Figure 56: SPI timing diagram - slave mode and CPHA = 1. – Added Figure 30: Asynchronous multiplexed PSRAM/NOR write waveforms. Updated Section 7.6: UFBGA169 package information (A0YV)|


DS13315 Rev 5 269/270


269

**STM32H730xB**

**IMPORTANT NOTICE – PLEASE READ CAREFULLY**

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and
improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on
ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order
acknowledgement.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or
the design of Purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, please refer to *www.st.com/trademarks* . All other
product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2025 STMicroelectronics – All rights reserved

270/270 DS13315 Rev 5

